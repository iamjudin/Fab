#!/usr/bin/env python3
"""Compile curated meanings and checked source receipts; repository build only."""
import argparse,hashlib,importlib.util,json,tempfile,sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
def read_module(root):
    spec=importlib.util.spec_from_file_location('fab_current_view',root/'plugins/fab/skills/research/scripts/knowledge_view.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def compile_view(root=ROOT,authoring=None):
    view=read_module(root);path=authoring or root/'knowledge/current.json';source=json.loads(path.read_text());provenance={};units=[]
    if source.get('schemaVersion')!=1 or source.get('family')!='fab-knowledge':raise ValueError('invalid-authoring-format')
    packets={}
    for record in source['records']:
        unit={k:v for k,v in record.items() if k!='sources'};refs=[]
        if record.get('authority') not in {'qualified-knowledge','historical-source'}:raise ValueError('non-shared-evidence-in-shared-build')
        if not record['sources']:raise ValueError('missing-source-binding')
        for ref in record['sources']:
            archive=(root/ref['archive']).resolve()
            if not archive.is_relative_to(root.resolve()):raise ValueError('source-outside-repository')
            if archive not in packets:
                raw=archive.read_bytes();packets[archive]=(json.loads(raw),hashlib.sha256(raw).hexdigest())
            packet,filehash=packets[archive];matches=[s for s in packet['sections'] if s['id']==ref['section']]
            if len(matches)!=1 or hashlib.sha256(matches[0]['text'].encode()).hexdigest()!=ref['textSha256']:raise ValueError('source-section-mismatch')
            section=matches[0];source_id=archive.name.removesuffix('.full.json')+':'+section['id']
            receipt={'sourceId':source_id,'archiveRepositoryPath':archive.relative_to(root.resolve()).as_posix(),'section':section['id'],'sectionTitle':section['title'],'textSha256':ref['textSha256'],'packetSha256':filehash,'authority':'source-material-not-runtime-instructions','verification':'source binding checked at build; not independent claim verification'}
            if source_id in provenance and provenance[source_id]!=receipt:raise ValueError('ambiguous-source-id')
            provenance[source_id]=receipt;refs.append({'sourceId':source_id,'textSha256':ref['textSha256']})
        unit['sources']=refs;unit['revision']=view.checked_revision(unit);units.append(unit)
    out={'schemaVersion':2,'family':source['family'],'authority':source['authority'],'authoringSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'records':units,'provenance':provenance,'legacyStateFamilies':source.get('legacyStateFamilies',{})};out['revision']=view.checked_revision(out);view.validate_data(out);return out

def render(data):return (json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode()
def build(root=ROOT,check=False):
    data=render(compile_view(root));target=root/'plugins/fab/shared/knowledge/current.json'
    if check:
        if not target.is_file() or target.read_bytes()!=data:raise ValueError('stale-compiled-knowledge')
    else:
        name=None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent,delete=False) as f:name=Path(f.name);f.write(data)
            name.replace(target)
        finally:
            if name and name.exists():name.unlink()
    return data

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    try:data=build(check=args.check)
    except (ValueError,KeyError,TypeError,OSError) as error:raise SystemExit(str(error))
    print(json.dumps({'mode':'check' if args.check else 'build','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
if __name__=='__main__':main()
