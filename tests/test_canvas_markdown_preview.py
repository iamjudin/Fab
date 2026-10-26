import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location('preview', Path(__file__).parents[1]/'plugins/fab/skills/wireframe/scripts/canvas_preview.py')
PREVIEW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREVIEW)


class MarkdownPreviewTests(unittest.TestCase):
    def node(self, text, height=420):
        return dict(id='S1', type='text', x=0, y=0, width=500, height=height, text=text)

    def test_actual_link_alias_title_metadata_divider_and_list(self):
        node = self.node('## Find message\nM10 · modal\n\n---\n\n- [[far/long/path.canvas|Open history]]\n- **Close:** retain query')
        svg = PREVIEW.render({'nodes':[node], 'edges':[]})
        rows = PREVIEW.text_layout(node)
        sizes = {r['kind']:r['size'] for r in rows if r['kind'] != 'divider'}
        self.assertGreater(sizes['heading'], sizes['body'])
        self.assertEqual(sizes['body'], sizes['metadata'])  # Plain captions have no native small-font guarantee.
        self.assertIn('font-weight="bold"', svg)
        self.assertIn('<line ', svg)
        self.assertIn('• Open history', svg)
        self.assertNotIn('far/long/path', svg)
        self.assertNotIn('**', svg)
        self.assertIn('retain query', svg)

    def test_overflow_remains_visible_and_warned_not_silently_dropped(self):
        node = self.node('## Title\n'+'\n'.join('Meaningful line '+str(i) for i in range(30))+'\nLAST_REQUIRED_RESULT', height=80)
        self.assertIn('LAST_REQUIRED_RESULT', PREVIEW.render({'nodes':[node], 'edges':[]}))
        self.assertTrue(any('overflow' in w for w in PREVIEW.layout_warnings({'nodes':[node], 'edges':[]})))

    def test_normal_body_not_metadata_and_explicit_one_item_list(self):
        rows = PREVIEW.text_layout(self.node('# Title\n\nA complete explanatory paragraph\n\n- Only action'))
        self.assertEqual(rows[1]['kind'], 'body')
        self.assertEqual(rows[-1]['text'], '• Only action')


if __name__ == '__main__': unittest.main()
