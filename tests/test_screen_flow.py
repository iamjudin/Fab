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
    def test_producer_anchors_lower_branch_and_named_merge(self):
        spec = {'view': 'behavior', 'mapPath': 'tests/flow.canvas', 'cards': [
            dict(id='start', title='Start', kind='screen', lane=0, minHeight=400),
            dict(id='commit', title='Commit', kind='action', lane=0),
            dict(id='ok', title='Known result', kind='result', lane=0),
            dict(id='lost', title='Unknown result', kind='error', lane=1),
            dict(id='check', title='Reconcile same request', kind='action', lane=1),
            dict(id='merge', title='Same known result', kind='screen', lane=0)],
            'edges': [dict(id=str(i), fromNode=a, toNode=b, kind='forward') for i,(a,b) in enumerate([
                ('start','commit'), ('commit','ok'), ('commit','lost'), ('lost','check'), ('check','merge'), ('ok','merge')])]}
        before=copy.deepcopy(spec); canvas,audit=FLOW.produce(spec)
        nodes=FLOW.indexed(canvas['nodes'])
        self.assertEqual(spec,before)
        self.assertGreater(nodes['lost']['x'], nodes['commit']['x'])
        self.assertGreater(nodes['merge']['x'], nodes['check']['x'])
        self.assertEqual(nodes['lost']['x'], nodes['ok']['x'])
        for edge in canvas['edges']:
            self.assertGreater(nodes[edge['toNode']]['x'], nodes[edge['fromNode']]['x'])
        self.assertEqual(len([k for k in nodes if k.startswith('SF-legend')]), 1)
        for kind in audit['usedRoles']:
            self.assertIn(FLOW.NOTATION[kind][1], nodes['SF-legend']['text'])
        self.assertNotIn(FLOW.NOTATION['modal'][1], nodes['SF-legend']['text'])
        self.assertEqual(nodes['commit']['y'] + nodes['commit']['height']/2,
                         nodes['start']['y'] + nodes['start']['height']/2)
        self.assertGreaterEqual(nodes['commit']['x'] - nodes['start']['x'] - nodes['start']['width'],400)
        self.assertEqual(audit['nativeFit'],'unverified')

    def test_producer_preserves_return_and_refuses_forward_cycle(self):
        spec={'view':'behavior','mapPath':'flow.canvas','cards':[
            dict(id='a',title='Draft',kind='screen',lane=0),
            dict(id='b',title='Access',kind='module',lane=0)],
            'edges':[dict(id='ab',fromNode='a',toNode='b',kind='forward'),
                     dict(id='cancel',fromNode='b',toNode='a',kind='return',label='Back to draft',retained=['Items and dates'])]}
        canvas,audit=FLOW.produce(spec); nodes=FLOW.indexed(canvas['nodes'])
        self.assertEqual(audit['returnRelations'],[spec['edges'][1]])
        self.assertNotIn('label', next(e for e in canvas['edges'] if e['id']=='cancel'))
        self.assertIn('[[flow.canvas|Draft]]',nodes['SF-return-cancel']['text'])
        self.assertGreater(nodes['SF-return-cancel']['x'],nodes['b']['x'])
        spec['edges'][1]['kind']='forward'
        with self.assertRaisesRegex(ValueError,'Forward cycle'):
            FLOW.produce(spec)

    def test_markdown_fit_preserves_long_reader_content_and_requires_media_measure(self):
        text=FLOW.card_text('Длинное название операции', '- Первый пункт\n- Последняя обязательная строка')
        self.assertGreater(FLOW.markdown_height(text,300),FLOW.markdown_height('Action',300))
        self.assertGreater(FLOW.markdown_height(text,300),FLOW.markdown_height(text,600))
        self.assertGreater(FLOW.markdown_height('## Title\n\n---\n\nBody',460),FLOW.markdown_height('## Title\nBody',460))
        with self.assertRaisesRegex(ValueError,'mediaHeight'):
            FLOW.markdown_height('![[photo.png]]',460)
        self.assertGreater(FLOW.markdown_height('![[photo.png]]',460,300),300)

    def test_interface_view_rejects_story_only_screen_and_preserves_controls(self):
        spec = {'mapPath': 'demo.canvas', 'cards': [dict(id='screen', kind='screen', lane=0, displayId='S01',
                title='Draft', body='Submitting retains input.')], 'edges': []}
        with self.assertRaisesRegex(ValueError, 'explicit surface'):
            FLOW.produce(spec)
        spec['cards'][0]['surface'] = {'content': ['Item list', 'Total amount'],
                                      'controls': [{'label': 'Remove selected item', 'kind':'local', 'effect':'Remove only an unsaved draft line'}]}
        canvas,audit=FLOW.produce(spec)
        text=canvas['nodes'][0]['text']
        self.assertIn('- Item list',text)
        self.assertIn('- Remove selected item',text)
        self.assertIn('Submitting retains input.',text)
        self.assertIn('Submitting retains input.\n\n---\n\n**Visible content**',text)
        self.assertIn('- Total amount\n\n---\n\n**Controls**',text)
        self.assertEqual(audit['view'],'interface')
        spec['cards'][0]['surface']['controls']=[]
        readonly,_=FLOW.produce(spec)
        self.assertNotIn('**Controls**',readonly['nodes'][0]['text'])
        spec['cards'][0]['surface']['controls']=[{'label':'Continue'}]
        spec['cards'][0]['surface']['controls'][0]['target']='missing'
        with self.assertRaisesRegex(ValueError,'Unknown surface control'):
            FLOW.produce(spec)

    def test_compact_legend_materializes_bundled_swatches_and_preserves_existing_assets(self):
        spec={'mapPath':'maps/demo.canvas','cards':[dict(id='a',kind='action',title='Save',lane=0,displayId='A01')],'edges':[]}
        canvas,audit=FLOW.produce(spec)
        legend=next(n for n in canvas['nodes'] if n['id']=='SF-legend')
        self.assertIn('![[maps/assets/sf-action.svg|12]]',legend['text'])
        with tempfile.TemporaryDirectory() as temp:
            output=Path(temp)
            FLOW.write_producer_assets(output,audit)
            asset=output/'assets/sf-action.svg'
            original=asset.read_bytes()
            self.assertIn(b'<svg',original)
            FLOW.write_producer_assets(output,audit)
            self.assertEqual(asset.read_bytes(),original)
            asset.write_text('User asset')
            with self.assertRaisesRegex(ValueError,'conflicting existing swatch'):
                FLOW.write_producer_assets(output,audit)
            self.assertEqual(asset.read_text(),'User asset')

    def test_column_layout_does_not_inherit_unrelated_global_row_height(self):
        spec={'view':'behavior','mapPath':'column.canvas','cards':[
            dict(id='root',title='Origin',kind='screen',lane=0,minHeight=100),
            dict(id='main',title='Main',kind='result',lane=0,minHeight=100),
            dict(id='large',title='Unrelated tall branch',kind='result',lane=1,minHeight=2000),
            dict(id='side',title='Short branch',kind='result',lane=2,minHeight=100),
            dict(id='next',title='Continuation',kind='action',lane=2)],
            'edges':[dict(id='r-m',fromNode='root',toNode='main',kind='forward'),
                     dict(id='r-s',fromNode='root',toNode='side',kind='forward'),
                     dict(id='s-n',fromNode='side',toNode='next',kind='forward')]}
        canvas,_=FLOW.produce(spec);nodes=FLOW.indexed(canvas['nodes'])
        # large is a separate root at column zero. It must not push the side
        # branch thousands of pixels down in another column.
        self.assertLess(nodes['side']['y'],600)
        self.assertEqual(nodes['side']['y']+nodes['side']['height']/2,
                         nodes['next']['y']+nodes['next']['height']/2)
        self.assertLess(nodes['main']['y']+nodes['main']['height'],nodes['side']['y'])
        for i,a in enumerate(canvas['nodes']):
            for b in canvas['nodes'][i+1:]:
                self.assertFalse(FLOW.overlap(a,b))

    def test_reader_ids_are_explicit_stable_and_number_the_return_target(self):
        spec={'mapPath':'demo.canvas','cards':[
            dict(id='raw-entry',displayId='S03',kind='screen',title='Draft',lane=0,
                 surface={'content':['Items'], 'controls':[{'label':'Continue','target':'raw-save'}]}),
            dict(id='raw-save',displayId='A08',kind='action',title='Save',lane=0)],
            'edges':[dict(id='save',fromNode='raw-entry',toNode='raw-save',kind='forward'),
                     dict(id='back',displayId='P02',fromNode='raw-save',toNode='raw-entry',kind='return',label='Back to draft',retained=['Items'])]}
        canvas,audit=FLOW.produce(spec);nodes=FLOW.indexed(canvas['nodes'])
        self.assertIn('S03 · Screen / state',nodes['raw-entry']['text'])
        self.assertIn('Continue → A08',nodes['raw-entry']['text'])
        self.assertIn('P02 · Continuation / return',nodes['SF-return-back']['text'])
        self.assertIn('[[demo.canvas|S03 · Draft]]',nodes['SF-return-back']['text'])
        self.assertNotIn('Target ID:',nodes['SF-return-back']['text'])
        self.assertNotIn('raw-entry',nodes['SF-return-back']['text'])
        self.assertEqual(audit['displayIds']['raw-entry'],'S03')
        spec['cards'][1]['displayId']='S03'
        with self.assertRaisesRegex(ValueError,'Duplicate reader'):
            FLOW.produce(spec)
        del spec['cards'][1]['displayId']
        with self.assertRaisesRegex(ValueError,'stable displayId'):
            FLOW.produce(spec)

    def test_declared_import_command_materializes_action_and_untyped_transition_fails(self):
        spec={'mapPath':'import.canvas','cards':[
            dict(id='library',displayId='S01',kind='screen',title='Library',lane=0,
                 surface={'content':['Files'], 'controls':[{'label':'Import file','target':'import-command'}]}),
            dict(id='options',displayId='M01',kind='modal',title='Import settings',lane=0,
                 surface={'content':['File and options'],'controls':[]})],
            'edges':[dict(id='open',fromNode='library',toNode='options',kind='forward')]}
        with self.assertRaisesRegex(ValueError,'user trigger'):
            FLOW.produce(spec)
        spec['edges'][0]['trigger']={'id':'import-command','displayId':'A03','title':'Import file'}
        before=copy.deepcopy(spec);canvas,audit=FLOW.produce(spec);nodes=FLOW.indexed(canvas['nodes'])
        self.assertEqual(spec,before)
        self.assertEqual(nodes['import-command']['fab']['kind'],'action')
        self.assertIn('Import file → A03',nodes['library']['text'])
        self.assertEqual(audit['userTriggers'][0]['originalEdge'],spec['edges'][0])
        self.assertEqual([(e['fromNode'],e['toNode']) for e in canvas['edges']],
                         [('library','import-command'),('import-command','options')])

    def test_automatic_empty_state_does_not_invent_a_user_command(self):
        spec={'mapPath':'query.canvas','cards':[
            dict(id='list',displayId='S01',kind='screen',title='Results',lane=0,
                 surface={'content':['Query and results'],'controls':[]}),
            dict(id='empty',displayId='S02',kind='empty',title='No results',lane=0,
                 surface={'content':['No matches'],'controls':[]})],
            'edges':[dict(id='update',fromNode='list',toNode='empty',kind='forward',
                          cause='input',reason='Query change updates results without a separate command')]}
        canvas,audit=FLOW.produce(spec)
        self.assertFalse(audit['userTriggers'])
        self.assertFalse(any(n.get('fab',{}).get('kind')=='action' for n in canvas['nodes']))
        self.assertEqual(audit['assets']['assets/sf-screen.svg'],'neutral')
        legend=next(n for n in canvas['nodes'] if n['id']=='SF-legend')
        self.assertIn('![[assets/sf-screen.svg|12]]',legend['text'])
        spec['edges'][0]['cause']='unresolved'
        _,audit=FLOW.produce(spec)
        self.assertEqual(len(audit['unresolvedTransitions']),1)

    def test_project_legend_is_complete_on_maps_with_different_local_roles(self):
        first={'view':'behavior','mapPath':'maps/one.canvas','cards':[
            dict(id='screen',displayId='S01',kind='screen',title='Screen',lane=0)],'edges':[]}
        second={'view':'behavior','mapPath':'maps/two.canvas','cards':[
            dict(id='gate',displayId='C01',kind='condition',title='Check',lane=0),
            dict(id='update',displayId='SYS01',kind='event',title='External update',lane=0)],
            'edges':[dict(id='e',fromNode='gate',toNode='update',kind='forward')]}
        before=copy.deepcopy([first,second]);outputs=FLOW.produce_project([first,second])
        self.assertEqual([first,second],before)
        legends=[next(n['text'] for n in canvas['nodes'] if n['id']=='SF-legend') for canvas,_ in outputs]
        self.assertEqual(legends[0],legends[1])
        self.assertIn('C — Condition',legends[0])
        self.assertIn('SYS — Service event',legends[0])
        nodes=FLOW.indexed(outputs[1][0]['nodes'])
        self.assertEqual(nodes['gate']['color'],nodes['update']['color'])
        self.assertEqual(outputs[0][1]['legendScope'],'project')
        self.assertEqual(set(outputs[0][1]['legendRoles']),{'screen','condition','event'})
        self.assertNotIn('modal',outputs[0][1]['legendRoles'])
        bad=copy.deepcopy(first);bad['projectLegend']={'roles':['screen'],'families':{},'notation':{}}
        bad['cards'][0]['kind']='condition'
        with self.assertRaisesRegex(ValueError,'omits a role'):
            FLOW.produce(bad)

    def test_current_navigation_marks_exact_map_and_preserves_other_links(self):
        menu='- [[Project/a/page.canvas|Current module]]\n- [[Project/b/page.canvas|Other module]]'
        marked=FLOW.mark_current_navigation(menu,'Project/a/page.canvas')
        self.assertIn('- **Current module**',marked)
        self.assertNotIn('[[Project/a/page.canvas',marked)
        self.assertIn('[[Project/b/page.canvas|Other module]]',marked)
        spec={'view':'behavior','mapPath':'Project/a/page.canvas','navigation':menu,
              'cards':[dict(id='one',kind='screen',title='Screen',lane=0)],'edges':[]}
        canvas,_=FLOW.produce(spec)
        navigation=next(n for n in canvas['nodes'] if n['id']=='SF-navigation')
        self.assertIn('**Current module**',navigation['text'])
        self.assertIn('[[Project/b/page.canvas|Other module]]',navigation['text'])

    def test_every_command_requires_its_owned_action_and_a_continuation(self):
        spec={'mapPath':'compose.canvas','cards':[
            dict(id='draft',displayId='S01',kind='screen',title='Draft',lane=0,
                 surface={'content':['Text'],'controls':[{'label':'Send'}]}),
            dict(id='send',displayId='A01',kind='action',title='Send',lane=0),
            dict(id='result',displayId='R01',kind='result',title='Sent',lane=0)],'edges':[]}
        with self.assertRaisesRegex(ValueError,'explicit action target'):
            FLOW.produce(spec)
        spec['cards'][0]['surface']['controls'][0]['target']='send'
        with self.assertRaisesRegex(ValueError,'not owned'):
            FLOW.produce(spec)
        spec['edges']=[dict(id='press',fromNode='draft',toNode='send',kind='forward')]
        with self.assertRaisesRegex(ValueError,'no represented continuation'):
            FLOW.produce(spec)
        spec['edges'].append(dict(id='done',fromNode='send',toNode='result',kind='forward'))
        _,audit=FLOW.produce(spec)
        self.assertEqual(audit['controlBindings'][0]['target'],'send')
        spec['cards'][0]['surface']['controls'][0]['target']='result'
        with self.assertRaisesRegex(ValueError,'must be an action'):
            FLOW.produce(spec)

    def test_invoked_interface_module_cannot_end_at_a_documentary_link(self):
        spec={'mapPath':'call.canvas','cards':[
            dict(id='source',displayId='S01',kind='screen',title='Draft',lane=0,
                 surface={'content':['Text'], 'controls':[{'label':'Choose','target':'choose'}]}),
            dict(id='choose',displayId='A01',kind='action',title='Choose',lane=0),
            dict(id='call',displayId='MOD01',kind='module',title='Shared choice',lane=0,
                 body='See shared module. Success returns selected data.'),
            dict(id='done',displayId='R01',kind='result',title='Selection received',lane=0)],
            'edges':[dict(id='press',fromNode='source',toNode='choose',kind='forward'),
                     dict(id='invoke',fromNode='choose',toNode='call',kind='forward')]}
        with self.assertRaisesRegex(ValueError,'Invoked module needs'):
            FLOW.produce(spec)
        # Prose and a disconnected result cannot substitute for the actual chain.
        spec['edges'].append(dict(id='complete',fromNode='call',toNode='done',kind='forward'))
        FLOW.produce(spec)
        spec['edges'].pop();spec['view']='behavior';spec['cards'][-1]['lane']=1
        FLOW.produce(spec)  # Abstract/documentary behavior maps remain a separate view.

    def test_local_input_and_explicit_unknown_do_not_invent_actions(self):
        spec={'mapPath':'edit.canvas','cards':[dict(id='draft',displayId='S01',kind='screen',title='Draft',lane=0,
            surface={'content':['Text'], 'controls':[{'label':'Edit text','kind':'input'},
                {'label':'Expand details','kind':'local','effect':'Reveal the existing local detail panel'},
                {'label':'Export','kind':'unresolved','reason':'Destination policy is not supplied'}]})],'edges':[]}
        canvas,audit=FLOW.produce(spec)
        self.assertEqual(len(audit['controlBindings']),3)
        self.assertEqual(len(audit['unresolvedControls']),1)
        self.assertFalse(any(n.get('fab',{}).get('kind')=='action' for n in canvas['nodes']))
        spec['cards'][0]['surface']['controls'][1].pop('effect')
        with self.assertRaises(ValueError):FLOW.produce(spec)

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

    def test_entry_guard_rejects_bypass_even_when_recovery_exists(self):
        canvas = {'nodes': [{'id': k} for k in ['entry', 'launch', 'guard', 'unknown']],
                  'edges': [dict(id='start', fromNode='entry', toNode='launch'),
                            dict(id='status', fromNode='launch', toNode='unknown'),
                            dict(id='reconcile', fromNode='unknown', toNode='guard'),
                            dict(id='retry', fromNode='guard', toNode='launch')]}
        with self.assertRaisesRegex(ValueError, 'bypasses'):
            FLOW.check_entry_guard(canvas, 'entry', 'launch', 'guard')
        canvas['edges'][0]['toNode'] = 'guard'
        self.assertIn('explicit local graph', FLOW.check_entry_guard(canvas, 'entry', 'launch', 'guard')['scope'])
        canvas['edges'].append(dict(id='shortcut', fromNode='entry', toNode='launch'))
        with self.assertRaisesRegex(ValueError, 'bypasses'):
            FLOW.check_entry_guard(canvas, 'entry', 'launch', 'guard')

    def test_entry_guard_rejects_disconnected_or_degenerate_claim(self):
        canvas = {'nodes': [{'id': k} for k in ['entry', 'launch', 'guard']],
                  'edges': [dict(id='start', fromNode='entry', toNode='launch')]}
        with self.assertRaisesRegex(ValueError, 'does not lie'):
            FLOW.check_entry_guard(canvas, 'entry', 'launch', 'guard')
        with self.assertRaisesRegex(ValueError, 'distinct'):
            FLOW.check_entry_guard(canvas, 'entry', 'launch', 'entry')

    def test_reader_inventory_keeps_full_text_without_claiming_review(self):
        canvas = copy.deepcopy(self.original)
        raw = '## Human title\n\n[[maps/detail.canvas|Readable destination]]\n\n' + ('Long body\n' * 80) + 'Final required line'
        canvas['nodes'][0]['text'] = raw
        canvas['nodes'][0]['height'] = 20  # Deliberately clipped; extraction is not fit proof.
        canvas['nodes'].append(dict(id='legend', type='group', label='Legend', x=0, y=0, width=50, height=50))
        before = copy.deepcopy(canvas)
        result = FLOW.reader_inventory(canvas)
        card = result['cards'][0]
        self.assertEqual(card['rawText'], raw)
        self.assertIn('Readable destination', card['readingText'])
        self.assertNotIn('maps/detail.canvas', card['readingText'])
        self.assertTrue(card['readingText'].endswith('Final required line'))
        self.assertEqual(result['nativeFit'], 'unverified')
        self.assertEqual(result['editorialReview'], 'not assessed')
        self.assertEqual(result['cards'][-1]['readingText'], 'Legend')
        self.assertEqual(canvas, before)
        canvas['nodes'][0]['height'] += 1
        self.assertNotEqual(FLOW.reader_inventory(canvas)['canvasSha256'], result['canvasSha256'])

    def test_reader_inventory_preserves_embeds_and_rejects_duplicate_ids(self):
        canvas = copy.deepcopy(self.original)
        canvas['nodes'][0]['text'] = '![[asset.png]] [[target.canvas|Caption]]'
        self.assertEqual(FLOW.reader_inventory(canvas)['cards'][0]['readingText'], '![[asset.png]] Caption')
        canvas['nodes'].append(copy.deepcopy(canvas['nodes'][0]))
        with self.assertRaises(ValueError):
            FLOW.reader_inventory(canvas)

    def test_reversible_frames_and_no_source_mutation(self):
        before = copy.deepcopy(self.original)
        canvas, audit = FLOW.project(self.original, {'M1': 'modal'}, {'forward': 'condition'})
        FLOW.assert_preserved(before, canvas, audit)
        self.assertEqual(self.original, before)
        self.assertEqual(audit['frames'][0]['originalEdge'], before['edges'][0])
        self.assertEqual(canvas['edges'][0]['fromEnd'], 'none')
        self.assertTrue(all(not e.get('label') for e in canvas['edges'][:2]))
        self.assertEqual(canvas['nodes'][-1]['color'], FLOW.PALETTE['condition'])
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


class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.original = {
            'nodes': [dict(id='form', type='text', x=0, y=0, width=300, height=220, text='# Edit details'),
                      dict(id='error', type='text', x=700, y=500, width=300, height=200, text='# Invalid field')],
            'edges': [dict(id='submit', fromNode='form', toNode='error', condition='invalid'),
                      dict(id='fix', fromNode='error', toNode='form', label='Correct field',
                           retained={'draft': True}, owner='form')], 'sourceRevision': 'accepted-v1'}
        self.spec = {'mapPath': 'Demo/sc-edit.canvas', 'returnReferences': {
            'fix': {'label': 'Continue editing', 'retained': ['Same object and entered values'],
                    'reason': 'Simple correction to the existing form; no recovery subtask',
                    'placement': dict(x=1400, y=500, width=420, height=600)}},
            'panels': [dict(id='nav', kind='navigation', title='Navigation',
                            groups=[{'title': 'Scenarios', 'items': [{'label': 'Edit', 'map': 'Demo/sc-edit.canvas'},
                                                                   {'label': 'Inspect', 'map': 'Demo/sc-inspect.canvas'}]}],
                            placement=dict(x=-700, y=0, width=450, height=500)),
                       dict(id='legend', kind='legend', title='Notation', body='A — action\nE — action error',
                            placement=dict(x=-700, y=600, width=450, height=300))]}

    def test_return_and_orientation_preserve_exact_source(self):
        before = copy.deepcopy(self.original)
        canvas, audit = FLOW.project(self.original, composition=self.spec)
        FLOW.assert_preserved(self.original, canvas, audit)
        self.assertEqual(before, self.original)
        self.assertEqual(audit['returns'][0]['originalEdge'], self.original['edges'][1])
        self.assertEqual(canvas['edges'][1]['toNode'], 'SF-return-fix')
        ref = next(n for n in canvas['nodes'] if n['id'] == 'SF-return-fix')
        self.assertIn('Target ID: form', ref['text'])
        self.assertIn('[[Demo/sc-edit.canvas|Edit details]]', ref['text'])
        self.assertEqual(FLOW.review_composition(canvas, audit)['reverseEdgesToReview'], [])

    def test_return_reference_loss_wrong_target_and_panel_changes_fail(self):
        canvas, audit = FLOW.project(self.original, composition=self.spec)
        for change in ('text', 'edge', 'panel', 'remove'):
            broken = copy.deepcopy(canvas)
            if change == 'text': broken['nodes'][2]['text'] = 'Everything is fine'
            elif change == 'edge': broken['edges'][1]['toNode'] = 'form'
            elif change == 'panel': broken['nodes'][-1]['text'] = 'Lost navigator'
            else: broken['nodes'] = broken['nodes'][:2]
            with self.subTest(change=change), self.assertRaises(ValueError):
                FLOW.assert_preserved(self.original, broken, audit)

    def test_recovery_edge_is_not_automatically_removed(self):
        canvas, audit = FLOW.project(self.original)
        self.assertEqual(canvas, self.original)
        self.assertEqual(FLOW.review_composition(canvas, audit)['reverseEdgesToReview'], ['fix'])
        self.assertNotIn('panels', audit)

    def test_missing_context_bad_paths_and_collision_rejected(self):
        for change in ('context', 'path', 'duplicate', 'overlap', 'target'):
            spec = copy.deepcopy(self.spec)
            if change == 'context': spec['returnReferences']['fix']['retained'] = []
            elif change == 'path': spec['mapPath'] = '../private.canvas'
            elif change == 'duplicate': spec['panels'][0]['id'] = 'form'
            elif change == 'overlap': spec['returnReferences']['fix']['placement']['x'] = 700
            else: spec['returnReferences']['missing'] = spec['returnReferences'].pop('fix')
            with self.subTest(change=change), self.assertRaises(ValueError):
                FLOW.project(self.original, composition=spec)

    def test_invalid_geometry_labels_empty_groups_and_unknown_fields_fail(self):
        for change in ('boolean', 'nan', 'small', 'label', 'empty', 'extra'):
            spec = copy.deepcopy(self.spec)
            if change == 'boolean': spec['panels'][0]['placement']['width'] = True
            elif change == 'nan': spec['panels'][0]['placement']['x'] = float('nan')
            elif change == 'small': spec['panels'][0]['placement']['height'] = 5
            elif change == 'label': spec['panels'][0]['groups'][0]['items'][0]['label'] = 'Bad]label'
            elif change == 'empty': spec['panels'][0]['groups'][0]['items'] = []
            else: spec['unchecked'] = True
            with self.subTest(change=change), self.assertRaises(ValueError):
                FLOW.project(self.original, composition=spec)

    def test_file_interface_and_safe_repeated_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, out = Path(tmp)/'input.canvas', Path(tmp)/'candidate.canvas'
            source.write_text(json.dumps(self.original)); initial = source.read_bytes()
            spec = {'sourceSha256': hashlib.sha256(initial).hexdigest(), 'composition': self.spec}
            canvas, audit = FLOW.write_projection(source, out, spec)
            FLOW.assert_preserved(json.loads(initial), json.loads(out.read_text()), audit)
            with self.assertRaises(ValueError): FLOW.write_projection(source, out, spec)
            self.assertEqual(source.read_bytes(), initial)

    def test_composition_labels_follow_artifact_language(self):
        self.spec['labels'] = {'return': 'Возврат', 'target': 'Цель', 'source': 'Переход', 'retained': 'Сохранить'}
        canvas, audit = FLOW.project(self.original, composition=self.spec)
        ref = next(n for n in canvas['nodes'] if n['id'] == 'SF-return-fix')
        self.assertIn('Цель: form', ref['text'])
        self.assertIn('Сохранить:', ref['text'])
        FLOW.assert_preserved(self.original, canvas, audit)

    def test_framed_forward_relation_and_return_compose_together(self):
        self.original['edges'][0]['label'] = 'Invalid input'
        canvas, audit = FLOW.project(self.original, edge_kinds={'submit': 'condition'},
                                     placements={'submit': dict(x=350, y=0, width=250, height=120)},
                                     composition=self.spec)
        FLOW.assert_preserved(self.original, canvas, audit)
        self.assertEqual(len(audit['frames']), 1)
        self.assertEqual(len(audit['returns']), 1)

    def test_paths_reject_absolute_fragments_and_markup(self):
        for path in ('/Demo/a.canvas','Demo/../a.canvas','Demo/a.canvas#node','Demo/a.canvas|oops','Demo//a.canvas'):
            with self.subTest(path=path), self.assertRaises(ValueError): FLOW.vault_map(path)



if __name__ == '__main__': unittest.main()


class ReaderFacingCardTests(unittest.TestCase):
    def test_authoring_keeps_divider_separate_and_internal_id_out(self):
        text = FLOW.card_text('Continue registration', 'Same form and correct fields', 'Result')
        self.assertIn('Result\n\n---\n\n', text)
        self.assertNotIn('caller-', text)
        self.assertEqual(FLOW.card_text('Save'), '## Save')

    def test_named_caller_destinations_do_not_assume_this_map(self):
        a = FLOW.continuation_text('Continue registration', 'Demo/registration.canvas', 'S-form',
                                   'Registration — participant details', ['Same draft and selected event'])
        b = FLOW.continuation_text('Continue profile edit', 'Demo/profile.canvas', 'S-profile',
                                   'Profile — personal details', ['Same person and unsaved values'])
        self.assertIn('Demo/registration.canvas|Registration — participant details', a)
        self.assertIn('Target ID: S-form', a)
        self.assertNotIn('S-profile', a)
        self.assertIn('Target ID: S-profile', b)
        with self.assertRaises(ValueError):
            FLOW.continuation_text('Continue', '../absent.canvas', 'S1', 'Form', ['Draft'])
        with self.assertRaises(ValueError): FLOW.card_text('Bad\nheading')

    def test_generated_return_hides_relation_id_but_audit_keeps_it(self):
        case = CompositionTests(); case.setUp()
        canvas, audit = FLOW.project(case.original, composition=case.spec)
        frame = next(n for n in canvas['nodes'] if n['id'] == 'SF-return-fix')
        self.assertNotIn('Return reference · fix', frame['text'])
        self.assertEqual(audit['returns'][0]['originalEdge']['id'], 'fix')
        FLOW.assert_preserved(case.original, canvas, audit)
