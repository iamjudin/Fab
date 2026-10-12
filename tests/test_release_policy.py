import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

release = module('plugins/fab/skills/delivery/scripts/check_release.py', 'release_gate')
table = module('plugins/fab/skills/wireframe/scripts/canvas_table.py', 'canvas_table')

class ReleasePolicyTests(unittest.TestCase):
    def plan(self):
        return {'schema': 1, 'version': '1-beta', 'fingerprint': 'abc', 'channel': 'beta',
                'surfaces': [{'id': 'prototype', 'status': 'limited', 'default': True,
                              'limitations': 'Selected browser paths only',
                              'checks': [{'name': 'interaction', 'result': 'pass', 'evidence': 'observed paths'}]},
                             {'id': 'canvas', 'status': 'blocked', 'default': False,
                              'limitations': 'Labels overlap', 'checks': [{'name': 'readability', 'result': 'fail'}]}]}

    def errors(self, plan):
        return release.check(plan, '1-beta', 'abc')

    def test_failed_excluded_map_does_not_block_bounded_prototype(self):
        self.assertEqual([], self.errors(self.plan()))

    def test_failed_default_is_rejected(self):
        p = self.plan(); p['surfaces'][1]['default'] = True
        self.assertTrue(self.errors(p))

    def test_unknown_experimental_or_missing_checks_cannot_be_default(self):
        for state in ('unknown', 'experimental', 'blocked'):
            with self.subTest(state=state):
                p = self.plan(); p['surfaces'][0]['status'] = state
                self.assertTrue(self.errors(p))
        p = self.plan(); p['surfaces'][0]['checks'] = []
        self.assertTrue(self.errors(p))

    def test_evidence_failure_and_unknown_each_reject(self):
        for change in ({'result': 'fail'}, {'result': 'unknown'}, {'evidence': ''}, {'evidence': '  '}, {'evidence': True}):
            p = self.plan(); p['surfaces'][0]['checks'][0].update(change)
            self.assertTrue(self.errors(p))

    def test_stale_identity_and_duplicate_scope_reject(self):
        for key in ('version', 'fingerprint'):
            p = self.plan(); p[key] = 'old'
            self.assertTrue(self.errors(p))
        p = self.plan(); p['surfaces'].append(copy.deepcopy(p['surfaces'][0]))
        self.assertTrue(self.errors(p))

    def test_fab_registry_cannot_omit_a_skill_or_presentation(self):
        wrapper = module('scripts/check_fab_release.py', 'fab_coverage')
        ids = [p.parent.name for p in (ROOT / 'plugins/fab/skills').glob('*/SKILL.md')]
        ids += ['wireframe.table-view', 'wireframe.canvas-preview', 'wireframe.native-canvas']
        plan = {'surfaces': [{'id': sid} for sid in ids]}
        self.assertEqual([], wrapper.coverage(plan))
        plan['surfaces'] = [s for s in plan['surfaces'] if s['id'] != 'wireframe.canvas-preview']
        self.assertEqual(['Missing declared outcome: wireframe.canvas-preview'], wrapper.coverage(plan))

    def test_stable_requires_verified_and_beta_limits_disclosed(self):
        p = self.plan(); p['channel'] = 'stable'
        self.assertTrue(self.errors(p))
        p['surfaces'][0]['status'] = 'verified'
        self.assertEqual([], self.errors(p))
        p = self.plan(); p['surfaces'][0]['limitations'] = ''
        self.assertTrue(self.errors(p))

    def test_no_defaults_or_undisclosed_exclusion_reject(self):
        p = self.plan(); p['surfaces'][0]['default'] = False
        self.assertTrue(self.errors(p))
        p = self.plan(); p['surfaces'][1]['limitations'] = ''
        self.assertTrue(self.errors(p))

class TableTests(unittest.TestCase):
    def data(self):
        return {'nodes': [{'id': 'S-01', 'type': 'group', 'x': 0, 'y': 0, 'width': 500, 'height': 400, 'label': 'Screen'},
                          {'id': 'save', 'type': 'text', 'x': 10, 'y': 10, 'width': 100, 'height': 50,
                           'text': 'Save | Cancel\n``` <tag>', 'custom': {'unknown': True}},
                          {'id': 'S-02', 'type': 'text', 'x': 600, 'y': 0, 'width': 100, 'height': 50, 'text': 'Other'}],
                'edges': [{'id': 'saved', 'fromNode': 'save', 'toNode': 'S-02', 'label': 'Success'},
                          {'id': 'cancelled', 'fromNode': 'save', 'toNode': 'S-01', 'label': 'Cancel', 'toEnd': 'none'}]}

    def test_inventory_preserves_all_data_and_branches(self):
        import json
        data = self.data(); rendered = table.render(data)
        snapshot = rendered.split('```json\n', 1)[1].split('\n```', 1)[0]
        self.assertEqual(data, json.loads(snapshot))
        self.assertIn('| save | text | S-01 |', rendered)
        self.assertIn('| saved | save | S-02 |', rendered)
        self.assertIn('| cancelled | save | S-01 |', rendered)
        self.assertIn('Save &#124; Cancel<br>', rendered)
        self.assertIn('&lt;tag&gt;', rendered)
        self.assertEqual(2, rendered.count('```'))

    def test_dangling_edge_and_duplicate_ids_reject(self):
        p = self.data(); p['edges'][0]['toNode'] = 'absent'
        with self.assertRaises(ValueError): table.render(p)
        p = self.data(); p['nodes'].append(copy.deepcopy(p['nodes'][1]))
        with self.assertRaises(ValueError): table.render(p)
        p = self.data(); p['edges'].append(copy.deepcopy(p['edges'][0]))
        with self.assertRaises(ValueError): table.render(p)

if __name__ == '__main__':
    unittest.main()
