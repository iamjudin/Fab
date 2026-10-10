import importlib.util, json, shutil, tempfile, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('guard',Path(__file__).resolve().parents[1]/'scripts/check_package.py')
guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
class GuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'package'
        shutil.copytree(guard.ROOT,self.root)
    def tearDown(self):self.tmp.cleanup()
    def test_valid_package(self):guard.validate(self.root)
    def test_runtime_cannot_reference_outside_package(self):
        p=self.root/'skills/analysis/SKILL.md'
        p.write_text(p.read_text()+'\n[External](../../../../outside.md)\n')
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_research_content_tampering_detected(self):
        p=self.root/'shared/methods/jtbd.full.json';d=json.loads(p.read_text())
        d['sections'][0]['text']+='changed';p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_parity_detects_shared_file_drift(self):
        before=guard.payload(self.root);p=self.root/'shared/core.md'
        p.write_text(p.read_text()+'changed')
        self.assertNotEqual(guard.fingerprint(before),guard.fingerprint(guard.payload(self.root)))
