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
    def test_missing_public_icon_is_rejected(self):
        p=self.root/'plugin.json';d=json.loads(p.read_text())
        del d['extensions']['com.openai']['interface']['logo'];p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_branding_cannot_reference_outside_package(self):
        p=self.root/'plugin.json';d=json.loads(p.read_text())
        d['extensions']['com.openai']['interface']['logo']='./../outside.png'
        p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_corrupt_icon_is_rejected(self):
        p=self.root/'assets/icon.png';data=bytearray(p.read_bytes());data[29]^=1;p.write_bytes(data)
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_localized_public_subtitle_is_rejected(self):
        p=self.root/'plugin.json';d=json.loads(p.read_text())
        d['extensions']['com.openai']['interface']['shortDescription']='Публичное описание'
        p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_runtime_cannot_reference_outside_package(self):
        p=self.root/'skills/analysis/SKILL.md'
        p.write_text(p.read_text()+'\n[External](../../../../outside.md)\n')
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_research_content_tampering_detected(self):
        p=self.root/'shared/methods/jtbd.full.json';d=json.loads(p.read_text())
        d['sections'][0]['text']+='changed';p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_invalid_research_context_is_rejected(self):
        p=self.root/'shared/methods/jtbd.full.json';d=json.loads(p.read_text())
        d['sections'][0]['readingContext']={'kind':'current-policy','note':'Wrong authority'}
        p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_registry_rejects_drift_and_omissions(self):
        p=self.root/'shared/methods/registry.json';original=p.read_text()
        for change in ('hash', 'title', 'context', 'duplicate', 'missing'):
            with self.subTest(change=change):
                d=json.loads(original)
                if change=='hash':d['modules'][0]['sourceSha256']='0'*64
                elif change=='title':d['modules'][0]['sourceTitle']='Another source'
                elif change=='context':d['modules'][0]['readingContext']['sectionKinds']['mixed']+=1
                elif change=='duplicate':d['modules'].append(d['modules'][0])
                else:d['modules'].pop()
                p.write_text(json.dumps(d))
                with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_registered_brief_must_link_its_actual_packet(self):
        p=self.root/'shared/methods/jtbd.md';p.write_text(p.read_text().replace('jtbd.full.json','first-value.full.json'))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_brief_application_requires_executable_owner(self):
        p=self.root/'shared/methods/jtbd.md';original=p.read_text()
        start=original.index('## Application in current Fab')
        end=original.index('## Deeper reading', start)
        for replacement in ('## Application in current Fab\nNo owner reference.\n\n',
                            '## Application in current Fab\n[Another brief](first-value.md).\n\n',
                            '## Application in current Fab\n[Source](jtbd.full.json).\n\n'):
            with self.subTest(replacement=replacement):
                p.write_text(original[:start]+replacement+original[end:])
                with self.assertRaisesRegex(AssertionError, 'missing current policy owner'):
                    guard.validate(self.root)
        p.write_text(original)
    def test_brief_cannot_erase_source_application_boundary(self):
        p=self.root/'shared/methods/jtbd.md'
        p.write_text(p.read_text().replace('## Application in current Fab','## Source continuation'))
        with self.assertRaisesRegex(AssertionError, 'missing current application boundary'):
            guard.validate(self.root)
    def test_registry_pair_cannot_escape_methods(self):
        p=self.root/'shared/methods/registry.json';d=json.loads(p.read_text())
        d['modules'][0]['brief']='../core.md';p.write_text(json.dumps(d))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_split_method_table_is_rejected(self):
        p=self.root/'shared/methods/index.md'
        p.write_text(p.read_text().replace('\n| Technical uncertainty', '\n\n| Technical uncertainty'))
        with self.assertRaises(AssertionError):guard.validate(self.root)
    def test_parity_detects_shared_file_drift(self):
        before=guard.payload(self.root);p=self.root/'shared/core.md'
        p.write_text(p.read_text()+'changed')
        self.assertNotEqual(guard.fingerprint(before),guard.fingerprint(guard.payload(self.root)))
