#!/usr/bin/env python3
"""Compare complete plugin package bytes, excluding generated Python caches."""
import argparse,hashlib,json
from pathlib import Path
def payload(root):
    return {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc')}
def fingerprint(files):
    h=hashlib.sha256()
    for name,content in sorted(files.items()):
        h.update(name.encode()+b'\0');h.update(hashlib.sha256(content).digest())
    return h.hexdigest()[:16]
def compare(source,installed):
    a,b=payload(source),payload(installed)
    if not a or not any(n in a for n in ('plugin.json','.codex-plugin/plugin.json')):
        raise ValueError('source is not a plugin package')
    differences=[n for n in sorted(a.keys()|b.keys()) if a.get(n)!=b.get(n)]
    return {'equal':not differences,'source':fingerprint(a),'installed':fingerprint(b),'differences':differences,'files':len(a)}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('installed',type=Path);a=p.parse_args()
    result=compare(a.source,a.installed);print(json.dumps(result,indent=2));raise SystemExit(0 if result['equal'] else 1)
