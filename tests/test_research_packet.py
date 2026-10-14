import importlib.util
import json
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
