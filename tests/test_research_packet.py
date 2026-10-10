import importlib.util
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


if __name__ == '__main__':
    unittest.main()
