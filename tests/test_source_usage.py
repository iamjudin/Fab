import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'plugins/fab/skills/research/scripts/source_usage.py'
spec=importlib.util.spec_from_file_location('source_usage',SCRIPT)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


class SourceUsageTests(unittest.TestCase):
    def test_add_project_keeps_entire_reader_body_and_filename_contract(self):
        data='# A book\n\nUnique evidence.\n#personal\n'.encode()
        out,receipt=m.transform(data,'fab')
        self.assertEqual(m.frontmatter(out.decode())[1].encode(),data)
        self.assertIn('project/fab',out.decode());self.assertFalse(receipt['renamed'])
        self.assertNotIn(m.FOOTER,out.decode())
        self.assertEqual(m.transform(out,'fab')[0],out)

    def test_existing_frontmatter_and_all_tags_survive_three_forms(self):
        cases=['tags: [bookworm/research, "special,tag"] # keep\n',
               "tags: 'bookworm/book' # keep\n",
               'tags:\n  - bookworm/article\n  - "#Once"\n# keep\n']
        for tags in cases:
            with self.subTest(tags=tags):
                data=('---\naliases: [A, B]\n'+tags+'created: 2026-10-13\n---\n\n# Reader\nExact.').encode()
                out,_=m.transform(data,'ujitsu');s=out.decode()
                self.assertIn('aliases: [A, B]',s);self.assertIn('created: 2026-10-13',s);self.assertIn('# keep',s)
                self.assertIn('bookworm/',s);self.assertIn('project/ujitsu',s)
                self.assertEqual(m.frontmatter(s)[1],m.frontmatter(data.decode())[1]);self.assertEqual(m.transform(out,'ujitsu')[0],out)

    def test_case_insensitive_tags_and_flow_comments_do_not_duplicate_or_corrupt(self):
        for line in ['tags: [personal,] # keep ] comment', 'tags: [personal] # keep ] comment', 'tags: ["Project/FAB", personal]']:
            with self.subTest(line=line):
                data=('---\n'+line+'\n---\n# Body\n').encode()
                out,_=m.transform(data,'fab')
                self.assertEqual(m.transform(out,'fab')[0],out)
                if 'Project/FAB' in line:self.assertNotIn('project/fab',out.decode())
                else:self.assertIn('"project/fab"] # keep ] comment',out.decode())

    def test_existing_other_projects_are_additive(self):
        data=b'---\ntags:\n- project/once\n- personal\n---\n# Reader\n'
        out,_=m.transform(data,'fab');out2,_=m.transform(out,'ujitsu')
        for tag in ['project/once','personal','project/fab','project/ujitsu']:self.assertIn(tag,out2.decode())
        self.assertEqual(m.transform(out2,'fab')[0],out2)

    def test_legacy_visible_block_becomes_hidden_footer_with_tags_intact(self):
        legacy=m.START+'\n## Использование в Once\n\n#Once #personal\n\n- Old revision: abc\n- [Brief](brief.md)\n'+m.END+'\n'
        body='\n# Исследование\n\nОговорка: это пример.\n'
        source=('---\ntags:\n  - bookworm/research\n---\n'+legacy+body).encode()
        out,_=m.transform(source,'once');s=out.decode();clean,meta,remaining=m.unpack(s)
        self.assertNotIn('Использование',clean);self.assertNotIn(m.START,clean)
        self.assertIn('project/once',clean);self.assertIn('"Once"',clean);self.assertIn('"personal"',clean)
        self.assertEqual(meta['legacy'][0]['text'],legacy);self.assertEqual(remaining,[])
        self.assertEqual(m.frontmatter(clean)[1],body);self.assertEqual(m.transform(out,'once')[0],out)
        self.assertTrue(s.endswith('-->\n'));self.assertNotIn('projects',meta)

    def test_legacy_json_other_usage_and_terminators_are_retained_safely(self):
        old={'projects':[{'project':'Other','tag':'#Other','bodySha256':'old','note':'x --> y'}]}
        block=m.START+'\n'+json.dumps(old)+'\n'+m.END+'\n'
        out,_=m.transform((block+'# Body\n').encode(),'fab');s=out.decode()
        self.assertIn('"Other"',s);self.assertNotIn('x --> y',s)
        _,meta,_=m.unpack(s);self.assertEqual(meta['legacy'][0]['text'],block)
        self.assertEqual(m.transform(out,'fab')[0],out)

    def test_record_refresh_preserves_other_consumer_exactly(self):
        source=b'# Evidence\n'
        sha=m.digest(source)
        first={'project':'once','bodySha256':sha,'processedAt':'2026-10-13','brief':'old/brief.md'}
        second={'project':'fab','bodySha256':sha,'processedAt':'2026-10-15','brief':'new/brief.md'}
        a,_=m.transform(source,'once',first);b,_=m.transform(a,'fab',second)
        _,meta,_=m.unpack(b.decode());self.assertEqual(meta['projects'],[first,second])
        self.assertEqual(m.transform(b,'fab',second)[0],b)
        with self.assertRaises(ValueError):m.transform(b,'fab',{**second,'bodySha256':'wrong'})

    def test_fenced_marker_examples_are_source_content(self):
        source=('```md\n'+m.START+'\n# Example\n'+m.END+'\n```\n# Actual\n').encode()
        out,_=m.transform(source,'fab');self.assertEqual(m.frontmatter(out.decode())[1].encode(),source)

    def test_bom_crlf_and_no_final_newline_survive(self):
        for ending in ['', '\r\n']:
            data=('\ufeff---\r\ntags: [personal]\r\n---\r\n# Текст\r\nДанные'+ending).encode()
            out,_=m.transform(data,'fab');self.assertTrue(out.startswith(b'\xef\xbb\xbf'))
            self.assertNotIn(b'\n',out.replace(b'\r\n',b''));self.assertTrue(out.endswith(ending.encode()) if ending else out.endswith('Данные'.encode()))
            self.assertEqual(m.transform(out,'fab')[0],out)

    def test_ambiguous_yaml_and_managed_blocks_fail_without_guessing(self):
        cases=['---\ntags: [a,\n---\nBody','---\ntags: &alias a\n---\nBody','---\ntags: [a]\ntags: [b]\n---\nBody','---\ntags: [a]\nBody',m.START+'\nBody',m.END+'\nBody', '---\n{"tags": ["personal"]}\n---\nBody', '---\n<<: *defaults\n---\nBody']
        for text in cases:
            with self.subTest(text=text),self.assertRaises(ValueError):m.transform(text.encode(),'fab')

    def test_apply_hash_identity_and_exact_target_preservation(self):
        with tempfile.TemporaryDirectory() as temp:
            source=Path(temp)/'unchanged-name.md';data=b'# Body\n';source.write_bytes(data);os.chmod(source,0o640)
            cmd=[sys.executable,str(SCRIPT),str(source),'--project','fab']
            dry=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(dry.returncode,0);self.assertEqual(source.read_bytes(),data)
            wrong=subprocess.run(cmd+['--apply','--expected-sha','wrong'],capture_output=True,text=True);self.assertNotEqual(wrong.returncode,0);self.assertEqual(source.read_bytes(),data)
            done=subprocess.run(cmd+['--apply','--expected-sha',m.digest(data)],capture_output=True,text=True);self.assertEqual(done.returncode,0,done.stdout)
            self.assertEqual(source.stat().st_mode&0o777,0o640);self.assertEqual([p.name for p in Path(temp).iterdir()],['unchanged-name.md'])
            for kind in ['symlink','hardlink']:
                alias=Path(temp)/kind
                if kind=='symlink':alias.symlink_to(source)
                else:os.link(source,alias)
                result=subprocess.run([sys.executable,str(SCRIPT),str(alias),'--project','once','--apply','--expected-sha',m.digest(source.read_bytes())],capture_output=True,text=True)
                self.assertNotEqual(result.returncode,0)
