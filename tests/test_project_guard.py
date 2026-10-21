import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('project_guard', Path(__file__).resolve().parents[1] / 'scripts/check_project.py')
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class ProjectGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.put('.gitignore', '**/raw/\n')
        self.put('README.md', '# Start\n\n[Guide](docs/guide.md#current-rule)\n\n--ref v0.1.0-beta.1\n')
        self.put('docs/guide.md', '# Current rule\n')
        self.put('plugins/fab/plugin.json', json.dumps({'version': '0.1.0-beta.1'}))
        self.git('add', '.')
        self.git('commit', '-qm', 'Initial fixture')

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], text=True, stderr=subprocess.PIPE)

    def put(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_local_file_is_not_public_until_staged(self):
        self.put('docs/new.md', '# New\n')
        self.put('README.md', '[New](docs/new.md)\n--ref v0.1.0-beta.1\n')
        self.assertFalse(guard.check(self.root)['eligible'])
        self.git('add', 'README.md', 'docs/new.md')
        self.assertTrue(guard.check(self.root, staged=True)['eligible'])

    def test_index_not_unstaged_worktree_controls_commit(self):
        self.put('README.md', '[Bad](missing.md)\n--ref v0.1.0-beta.1\n')
        self.git('add', 'README.md')
        self.put('README.md', '[Guide](docs/guide.md)\n--ref v0.1.0-beta.1\n')
        self.assertFalse(guard.check(self.root, staged=True)['eligible'])
        self.assertTrue(guard.check(self.root)['eligible'])

    def test_changed_report_checked_from_actual_base(self):
        base = self.git('rev-parse', 'HEAD').strip()
        self.put('experiments/check/report.md', '[Runner](runner.py)\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'Missing support')
        self.assertFalse(guard.check(self.root, base_ref=base)['eligible'])

    def test_removed_heading_is_detected(self):
        self.put('docs/guide.md', '# Renamed\n')
        self.assertFalse(guard.check(self.root)['eligible'])

    def test_committed_check_does_not_use_uncommitted_target_heading(self):
        base = self.git('rev-parse', 'HEAD').strip()
        self.put('README.md', '[Future](docs/guide.md#future)\n--ref v0.1.0-beta.1\n')
        self.git('add', 'README.md')
        self.git('commit', '-qm', 'Unpublished heading dependency')
        self.put('docs/guide.md', '# Future\n')
        self.assertFalse(guard.check(self.root, base_ref=base)['eligible'])

    def test_new_tag_zero_base_checks_tip_not_old_archive(self):
        self.put('experiments/old/report.md', '[Historical local result](raw/output.md)\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'Old report predates guard')
        self.put('docs/current.md', '# Current\n')
        self.git('add', 'docs/current.md')
        self.git('commit', '-qm', 'New tagged increment')
        self.assertTrue(guard.check(self.root, base_ref='0' * 40)['eligible'])
        self.put('docs/current.md', '[Missing](missing.md)\n')
        self.git('add', 'docs/current.md')
        self.git('commit', '-qm', 'Broken tagged increment')
        self.assertFalse(guard.check(self.root, base_ref='0' * 40)['eligible'])

    def test_frozen_history_keeps_mistakes_but_current_documents_do_not(self):
        self.put('docs/backlog-history-2026-10-21.md', '[Old pending evidence](unpublished.md#future)\n')
        self.git('add', 'docs/backlog-history-2026-10-21.md')
        self.assertTrue(guard.check(self.root, staged=True)['eligible'])
        self.put('docs/current.md', '[Pending](unpublished.md#future)\n')
        self.git('add', 'docs/current.md')
        self.assertFalse(guard.check(self.root, staged=True)['eligible'])

    def test_frozen_example_and_external_link_are_not_local_resources(self):
        self.put('README.md', '```md\n[example](not-a-resource.md)\n```\n[Docs](https://example.invalid/x)\n--ref v0.1.0-beta.1\n')
        self.assertTrue(guard.check(self.root)['eligible'])

    def test_owned_leftovers_fail_without_blocking_other_work(self):
        self.put('experiments/current/raw/evidence.json', '{}')
        self.put('experiments/other/draft.md', 'Other ongoing work')
        self.assertTrue(guard.check(self.root, task_dirs=['experiments/current'])['eligible'])
        self.put('experiments/current/scratch.py', 'Temporary helper')
        result = guard.check(self.root, task_dirs=['experiments/current'])
        self.assertFalse(result['eligible'])
        self.assertEqual(len(result['errors']), 1)
        self.assertIn('scratch.py', result['errors'][0])

    def test_stale_install_pin_fails(self):
        self.put('plugins/fab/plugin.json', json.dumps({'version': '0.1.0-beta.2'}))
        self.assertFalse(guard.check(self.root)['eligible'])

    def test_symlink_does_not_make_external_material_a_public_document(self):
        outside = Path(self.tmp.name).parent / (self.root.name + '-external.md')
        outside.write_text('Private material')
        self.addCleanup(outside.unlink)
        (self.root / 'docs/guide.md').unlink()
        (self.root / 'docs/guide.md').symlink_to(outside)
        self.git('add', 'docs/guide.md')
        self.assertFalse(guard.check(self.root, staged=True)['eligible'])

    def test_task_boundary_cannot_be_whole_repo_or_escape(self):
        for path in ['.', '..', '/tmp']:
            with self.subTest(path=path):
                self.assertFalse(guard.check(self.root, task_dirs=[path])['eligible'])
