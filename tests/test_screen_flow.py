import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('screen_flow', Path(__file__).parents[1] / 'plugins/fab/skills/wireframe/scripts/screen_flow.py')
FLOW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FLOW)


class ScreenFlowTests(unittest.TestCase):
    def setUp(self):
        self.original = {
            'nodes': [dict(id='S1', type='text', x=0, y=0, width=300, height=200,
                           text='# Select\nS1 · screen\n\n---\n\n- Existing\n- New', owner='item'),
                      dict(id='M1', type='text', x=1000, y=0, width=300, height=200,
                           text='# Confirm\nM1 · modal', color='6', retained={'origin': 'caller-A'}),
                      dict(id='S-empty', type='text', x=1000, y=500, width=300, height=200,
                           text='# Empty', color='4')],
            'edges': [dict(id='forward', fromNode='S1', toNode='M1', label='Selected',
                           fromSide='right', toSide='left', owner='item', condition='valid',
                           retained={'query': 'abc'}, fromEnd='none'),
                      dict(id='empty', fromNode='S1', toNode='S-empty', label='No matches'),
                      dict(id='cancel', fromNode='M1', toNode='S1', label='Cancel', retained=['query', 'position'])],
            'custom': {'source': 'accepted', 'unknownOutcome': True}}

    def test_reversible_frames_and_no_source_mutation(self):
        before = copy.deepcopy(self.original)
        canvas, audit = FLOW.project(self.original, {'M1': 'modal'}, {'forward': 'condition'})
        FLOW.assert_preserved(before, canvas, audit)
        self.assertEqual(self.original, before)
        self.assertEqual(audit['frames'][0]['originalEdge'], before['edges'][0])
        self.assertEqual(canvas['edges'][0]['fromEnd'], 'none')
        self.assertTrue(all(not e.get('label') for e in canvas['edges'][:2]))
        self.assertNotIn('color', canvas['nodes'][-1])
        self.assertEqual(canvas['nodes'][1]['color'], '#0062ff')

    def test_explicit_types_not_suffixes_or_language(self):
        canvas, audit = FLOW.project(self.original, {'S-empty': 'navigation'}, {'forward': 'action'})
        self.assertNotIn('color', canvas['nodes'][2])
        self.assertEqual(canvas['nodes'][-1]['color'], '5')
        self.assertEqual(canvas['nodes'][0], self.original['nodes'][0])

    def test_no_mandatory_architecture_or_palette_edit(self):
        one = {'nodes': [self.original['nodes'][0]], 'edges': []}
        canvas, audit = FLOW.project(one)
        self.assertEqual(canvas, one)
        self.assertEqual(audit['frames'], [])

    def test_lost_empty_error_cancel_or_original_fields_rejected(self):
        canvas, audit = FLOW.project(self.original, edge_kinds={'forward': 'result'})
        for change in ('remove-cancel', 'remove-empty', 'owner', 'context', 'text'):
            broken = copy.deepcopy(canvas)
            if change.startswith('remove-'):
                broken['edges'] = [e for e in broken['edges'] if e['id'] != change[7:]]
            elif change == 'owner':
                broken['nodes'][0]['owner'] = 'screen'
            elif change == 'context':
                broken['edges'][-1]['retained'] = []
            else:
                broken['nodes'][0]['text'] = 'Shortened'
            with self.subTest(change=change), self.assertRaises(ValueError):
                FLOW.assert_preserved(self.original, broken, audit)

    def test_tampered_frame_leg_or_palette_rejected(self):
        canvas, audit = FLOW.project(self.original, {'M1': 'modal'}, {'forward': 'condition'})
        for change in ('frame', 'leg', 'palette'):
            broken = copy.deepcopy(canvas)
            if change == 'frame': broken['nodes'][-1]['text'] = 'Success'
            elif change == 'leg': broken['edges'][1]['toNode'] = 'S-empty'
            else: broken['nodes'][1]['color'] = '6'
            with self.subTest(change=change), self.assertRaises(ValueError):
                FLOW.assert_preserved(self.original, broken, audit)

    def test_no_text_kind_guess_or_unknown_scope(self):
        for kwargs in ({'edge_kinds': {'forward': 'guess'}}, {'node_kinds': {'absent': 'modal'}},
                       {'placements': {'cancel': {'x': 40}}}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError): FLOW.project(self.original, **kwargs)

    def test_bad_fit_and_insufficient_space_do_not_move_neighbors(self):
        for placement in ({'x': 0, 'y': 0}, {'height': 20}, {'x': float('nan')}, {'color': '1'}):
            before = copy.deepcopy(self.original)
            with self.subTest(placement=placement), self.assertRaises(ValueError):
                FLOW.project(self.original, edge_kinds={'forward': 'action'}, placements={'forward': placement})
            self.assertEqual(self.original, before)

    def test_duplicate_ids_and_dangling_source_rejected(self):
        bad = copy.deepcopy(self.original); bad['nodes'].append(copy.deepcopy(bad['nodes'][0]))
        with self.assertRaises(ValueError): FLOW.project(bad)

    def test_projection_id_collision_or_missing_label_rejected(self):
        bad = copy.deepcopy(self.original)
        extra = copy.deepcopy(bad['nodes'][0]); extra['id'] = 'SF-frame-forward'
        bad['nodes'].append(extra)
        with self.assertRaises(ValueError): FLOW.project(bad, edge_kinds={'forward': 'condition'})
        bad = copy.deepcopy(self.original); bad['edges'][0].pop('label')
        with self.assertRaises(ValueError): FLOW.project(bad, edge_kinds={'forward': 'condition'})

    def test_unknown_spec_or_geometry_types_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                FLOW.write_projection(Path(tmp)/'absent', Path(tmp)/'out', {'moves': {}})
        for geometry in ({'width': '220'}, {'width': -1}, {'height': True}):
            with self.subTest(geometry=geometry), self.assertRaises(ValueError):
                FLOW.project(self.original, edge_kinds={'forward': 'condition'}, placements={'forward': geometry})
        bad = copy.deepcopy(self.original); bad['edges'][0]['toNode'] = 'absent'
        with self.assertRaises(ValueError): FLOW.project(bad)

    def test_changed_hash_and_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, out = Path(tmp)/'input.canvas', Path(tmp)/'output.canvas'
            source.write_text(json.dumps(self.original)); initial = source.read_bytes()
            with self.assertRaises(ValueError): FLOW.write_projection(source, out, {'sourceSha256': 'wrong'})
            self.assertFalse(out.exists())
            spec = {'sourceSha256': hashlib.sha256(initial).hexdigest(), 'edgeKinds': {'forward': 'condition'}}
            FLOW.write_projection(source, out, spec)
            saved = out.read_bytes()
            with self.assertRaises(ValueError): FLOW.write_projection(source, out, spec)
            self.assertEqual(out.read_bytes(), saved)
            self.assertEqual(source.read_bytes(), initial)


if __name__ == '__main__': unittest.main()
