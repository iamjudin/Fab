import importlib.util
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('canvas_preview', Path(__file__).parents[1] / 'plugins/fab/skills/wireframe/scripts/canvas_preview.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def node(identity, kind, x, y, width, height, **extra):
    return dict(id=identity, type=kind, x=x, y=y, width=width, height=height, **extra)


class CanvasGroupTests(unittest.TestCase):
    def test_native_title_band_catches_previous_control(self):
        group = node('collection', 'group', 20, 180, 400, 200, label='Collection')
        previous = node('create', 'text', 20, 120, 400, 50, text='Create')
        warnings = MODULE.layout_warnings({'nodes': [group, previous]})
        self.assertIn('group title overlaps node: collection, create', warnings)
        previous['y'] = 80
        self.assertEqual(MODULE.layout_warnings({'nodes': [group, previous]}), [])

    def test_svg_group_title_is_above_its_frame(self):
        root = ET.fromstring(MODULE.render({'nodes': [self.group, self.action], 'edges': []}))
        title = root.findall('{http://www.w3.org/2000/svg}text')[0]
        self.assertLess(float(title.get('y')), self.group['y'])

    def setUp(self):
        self.group = node('screen', 'group', 0, 0, 500, 400, label='Main screen')
        self.action = node('add', 'text', 40, 100, 200, 70, text='Add')

    def test_native_hex_color_is_preserved_in_svg(self):
        self.action['color'] = '#dbeafe'
        root = ET.fromstring(MODULE.render({'nodes': [self.action], 'edges': []}))
        rects = root.findall('{http://www.w3.org/2000/svg}rect')
        self.assertEqual(rects[-1].get('fill'), '#dbeafe')
        self.assertEqual(MODULE.node_fill({'color': '4'}), MODULE.COLORS['4'])
        self.assertEqual(MODULE.node_fill({'color': '#invalid'}), '#fff')

    def test_containment_is_valid_but_colliding_controls_are_not(self):
        other = node('edit', 'text', 70, 120, 200, 70, text='Edit')
        warnings = MODULE.layout_warnings({'nodes': [self.group, self.action, other]})
        self.assertEqual(warnings, ['overlapping nodes: add, edit'])

    def test_control_crossing_group_boundary_is_reported(self):
        crossing = node('outside', 'text', 450, 100, 200, 70, text='Outside')
        self.assertIn('overlapping nodes: screen, outside', MODULE.layout_warnings({'nodes': [self.group, crossing]}))

    def test_group_renders_behind_control_regardless_of_node_order(self):
        root = ET.fromstring(MODULE.render({'nodes': [self.action, self.group], 'edges': []}))
        ns = {'s': 'http://www.w3.org/2000/svg'}
        rects = root.findall('s:rect', ns)
        self.assertEqual([r.get('width') for r in rects[-2:]], ['500', '200'])
        self.assertEqual([t.text for t in root.findall('s:text', ns)], ['Main screen', 'Add'])


if __name__ == '__main__':
    unittest.main()

class EdgeRoutingTests(unittest.TestCase):
    def fixture(self):
        a=node('a','text',0,0,100,100,text='A')
        b=node('b','text',500,0,100,100,text='B')
        obstacle=node('middle','text',200,0,100,100,text='Obstacle')
        edge={'id':'route','fromNode':'a','toNode':'b','fromSide':'right','toSide':'left'}
        return a,b,obstacle,edge
    def test_routed_preview_preserves_endpoints_and_avoids_middle_card(self):
        a,b,obstacle,edge=self.fixture();route=MODULE.edge_route(edge,{n['id']:n for n in (a,b,obstacle)})
        self.assertEqual(route[0],MODULE.anchor(a,'right'));self.assertEqual(route[-1],MODULE.anchor(b,'left'))
        self.assertGreater(len(route),2)
        self.assertFalse(any(MODULE.segment_hits_box(x,y,obstacle) for x,y in zip(route,route[1:])))
        root=ET.fromstring(MODULE.render({'nodes':[a,b,obstacle],'edges':[edge]}))
        self.assertEqual(len(root.findall('{http://www.w3.org/2000/svg}polyline')),1)
    def test_warning_exposes_label_collision_instead_of_silencing_it(self):
        a,b,obstacle,edge=self.fixture();edge['label']='A long transition label'
        route=MODULE.edge_route(edge,{n['id']:n for n in (a,b,obstacle)})
        cx,cy,width=MODULE.edge_label_position(route,edge['label'])
        hidden=node('label-content','text',cx-width/2,cy-18,width,30,text='Meaning')
        warnings=MODULE.layout_warnings({'nodes':[a,b,obstacle,hidden],'edges':[edge]})
        # The route may change around the new card, so assert the actual collision diagnostic
        # on a direct route with a label above it and content above the line.
        a,b,_,edge=self.fixture();edge['label']='Navigation'
        hidden=node('label-content','text',250,5,100,25,text='Meaning')
        warnings=MODULE.layout_warnings({'nodes':[a,b,hidden],'edges':[edge]})
        self.assertTrue(any('edge label overlaps content' in w for w in warnings))
    def test_overflow_check_does_not_hide_ninth_line(self):
        a=node('small','text',0,0,200,210,text='\n'.join(['line']*12))
        self.assertTrue(any('overflow' in w for w in MODULE.layout_warnings({'nodes':[a],'edges':[]})))


class MarkdownHierarchyTests(unittest.TestCase):
    def test_native_metadata_setext_is_heading_and_not_divider(self):
        card = node('cancel', 'text', 0, 0, 360, 120,
                    text='## Return after cancellation\ncaller-register-cancel · result\n---\nReturn without creating a request')
        rows = MODULE.text_layout(card)
        self.assertTrue(any(r['kind'] == 'heading' and 'caller-register' in r['text'] for r in rows))
        self.assertFalse(any(r['kind'] == 'divider' for r in rows))
        warnings = MODULE.layout_warnings({'nodes': [card], 'edges': []})
        self.assertIn('setext heading changes card hierarchy: cancel', warnings)
        self.assertIn('text may overflow node: cancel', warnings)

    def test_blank_line_preserves_thematic_break_and_plain_caption(self):
        card = node('safe', 'text', 0, 0, 400, 400,
                    text='## Continue editing\n\nResult\n\n---\n\nSame form and entered values')
        rows = MODULE.text_layout(card)
        self.assertEqual(sum(r['kind'] == 'divider' for r in rows), 1)
        self.assertEqual(MODULE.layout_warnings({'nodes': [card], 'edges': []}), [])

    def test_multiline_setext_and_equals_underlines(self):
        headings, underlines = MODULE.setext_lines('First line\nSecond line\n===\n\nBody')
        self.assertEqual(headings, {0, 1})
        self.assertEqual(underlines, {2})
        self.assertEqual(MODULE.setext_lines('## Explicit heading\n---')[0], set())
        self.assertEqual(MODULE.setext_lines('```\ncode\n---\n```')[0], set())
