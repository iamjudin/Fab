import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    'research_packet', Path(__file__).resolve().parents[1] /
    'plugins/fab/skills/research/scripts/research_packet.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ResearchPacketTests(unittest.TestCase):
    def test_build_refuses_source_identity_even_through_aliases(self):
        for kind in ('same-path', 'symlink', 'hardlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temp:
                source = Path(temp) / 'original.md'
                content = b'## Method\nOriginal evidence.\n'
                source.write_bytes(content)
                output = source if kind == 'same-path' else Path(temp) / 'output.json'
                if kind == 'symlink':output.symlink_to(source)
                elif kind == 'hardlink':os.link(source, output)
                result = subprocess.run([sys.executable, module.__file__, 'build', str(source), str(output), '--title', 'Protected'], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('must not overwrite', result.stderr)
                self.assertEqual(source.read_bytes(), content)

    def test_unknown_exclusion_fails_before_creating_packet(self):
        with tempfile.TemporaryDirectory() as temp:
            source, output = Path(temp) / 'original.md', Path(temp) / 'output.json'
            content = b'## Method\nOriginal evidence.\n'
            source.write_bytes(content)
            result = subprocess.run([sys.executable, module.__file__, 'build', str(source), str(output), '--title', 'Test', '--exclude-title', 'Absent section'], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Unknown exclusion titles', result.stderr)
            self.assertFalse(output.exists())
            self.assertEqual(source.read_bytes(), content)

    def test_cli_preserves_utf8_bytes_and_line_endings(self):
        for ending in ('\n', '\r\n', '\r'):
            with self.subTest(ending=repr(ending)), tempfile.TemporaryDirectory() as temp:
                source = ('Intro' + ending + '## Method' + ending + 'Keep this condition ✓.' + ending).encode('utf-8')
                path, output = Path(temp) / 'original.md', Path(temp) / 'packet.json'
                path.write_bytes(source)
                subprocess.check_output([sys.executable, module.__file__, 'build', str(path), str(output), '--title', 'Exact source'])
                data = json.loads(output.read_text())
                self.assertEqual(''.join(s['text'] for s in data['sections']).encode('utf-8'), source)
                self.assertEqual(data['sourceSha256'], module.digest(source.decode('utf-8')))

    def test_code_fence_matching_preserves_section_boundaries(self):
        for opening, inner, closing in [('````text', '```', '`````'),
                                        ('~~~text', '```', '~~~'),
                                        ('```text', '```not-a-close', '```')]:
            with self.subTest(opening=opening, inner=inner):
                source = f'## Method\n{opening}\n{inner}\n## Still code\n{closing}\n## Limits\nUnknown\n'
                data = module.packet(source, 'Fence')
                self.assertEqual([s['title'] for s in data['sections']], ['Method', 'Limits'])
                self.assertEqual(''.join(s['text'] for s in data['sections']), source)

    def test_unclosed_fence_keeps_heading_in_code(self):
        source = '## Method\n```text\n## Still code\n'
        data = module.packet(source, 'Fence')
        self.assertEqual(len(data['sections']), 1)
        self.assertEqual(data['sections'][0]['text'], source)

    def test_source_authority_and_unexcluded_hash_cannot_drift(self):
        for key, value in [('schemaVersion', 2), ('authority', 'current-runtime-instructions'),
                           ('sourceSha256', '0' * 64)]:
            with self.subTest(key=key):
                data = module.packet('## Method\nText\n', 'Test')
                data[key] = value
                with self.assertRaises(AssertionError):
                    module.validate(data)

    def test_exclusion_cannot_hide_a_retained_section(self):
        data = module.packet('## Method\nText\n## Example\nCase\n', 'Test', excluded_titles=('Example',))
        module.validate(data)
        data['excluded'][0]['id'] = data['sections'][0]['id']
        with self.assertRaises(AssertionError):
            module.validate(data)

    def test_excluding_preamble_does_not_exclude_the_report(self):
        source = 'Technical preamble\n## Method\nKeep the condition.\n## Limits\nUnknown\n'
        data = module.packet(source, 'Test', excluded_titles=('Preamble',))
        self.assertEqual([s['title'] for s in data['sections']], ['Method', 'Limits'])
        self.assertEqual([s['title'] for s in data['excluded']], ['Preamble'])
        module.validate(data)

    def test_lossless_and_code_headings(self):
        source = 'Intro\n## Method\n```text\n## not a heading\n```\nClaim [source](https://example.com)\n## Limits\nUnknown\n'
        data = module.packet(source, 'Test', 'project-evidence')
        self.assertEqual(''.join(s['text'] for s in data['sections']), source)
        self.assertEqual([s['title'] for s in data['sections']], ['Preamble', 'Method', 'Limits'])
        self.assertEqual(data['scope'], 'project-evidence')
        module.validate(data)

    def test_excludes_case_not_following_sources(self):
        source = '## Method\nGeneric\n## Local case\nCase\n### Child\nDetail\n## Sources\nLink\n'
        data = module.packet(source, 'Test', excluded_titles=('Local case',))
        self.assertEqual([s['title'] for s in data['sections']], ['Method', 'Sources'])
        self.assertEqual([s['title'] for s in data['excluded']], ['Local case', 'Child'])
        self.assertTrue(all(s['sha256'] for s in data['excluded']))

    def test_content_corruption_is_detected(self):
        data = module.packet('## Method\nImportant limitation\n', 'Test')
        data['sections'][0]['text'] = 'Claim without limitation\n'
        with self.assertRaises(AssertionError):
            module.validate(data)

    def test_unqualified_legacy_section_output_stays_exact(self):
        source = '## Method\nA qualified claim with its exception.\n'
        data = module.packet(source, 'Legacy')
        self.assertEqual(module.section_view(data['sections'][0]), source)

    def test_cli_exposes_historical_context_and_preserves_source(self):
        source = '## Local application\nAlways require the old project pipeline.\n'
        data = module.packet(source, 'Historical source')
        data['sections'][0]['readingContext'] = {
            'kind': 'historical-application',
            'note': 'Retained proposal for a former project, not current policy.',
        }
        module.validate(data)
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / 'packet.json'
            p.write_text(json.dumps(data))
            script = Path(module.__file__)
            index = subprocess.check_output([sys.executable, str(script), 'read', str(p), '--index'], text=True)
            content = subprocess.check_output([sys.executable, str(script), 'read', str(p), '--section', 'R001'], text=True)
        self.assertIn('historical-application', index)
        self.assertIn('not current policy', content)
        self.assertTrue(content.endswith(source))
        self.assertEqual(data['retainedSha256'], module.digest(source))

    def test_invalid_or_unexplained_context_is_rejected(self):
        data = module.packet('## Method\nText\n', 'Test')
        for context in ({'kind': 'current-policy', 'note': 'Promoted silently'},
                        {'kind': 'mixed', 'note': ''}, 'historical-application'):
            with self.subTest(context=context):
                data['sections'][0]['readingContext'] = context
                with self.assertRaises(AssertionError):
                    module.validate(data)


if __name__ == '__main__':
    unittest.main()
