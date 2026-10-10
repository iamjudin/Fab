import importlib.util, shutil, tempfile, unittest
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('compare_runtime', BASE/'plugins/fab/skills/plugin/scripts/compare_runtime.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class RuntimeCompareTests(unittest.TestCase):
    def test_full_shared_payload_matches(self):
        with tempfile.TemporaryDirectory() as t:
            clone=Path(t)/'copy';shutil.copytree(BASE/'plugins/fab',clone)
            self.assertTrue(m.compare(BASE/'plugins/fab',clone)['equal'])
    def test_shared_drift_is_not_hidden_by_same_manifest(self):
        with tempfile.TemporaryDirectory() as t:
            clone=Path(t)/'copy';shutil.copytree(BASE/'plugins/fab',clone)
            p=clone/'shared/core.md';p.write_text('different')
            d=m.compare(BASE/'plugins/fab',clone)
            self.assertFalse(d['equal']);self.assertIn('shared/core.md',d['differences'])
    def test_nonpackage_cannot_claim_parity(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(ValueError):m.compare(Path(t),Path(t))
