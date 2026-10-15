#!/usr/bin/env python3
"""Verify anonymous release assets and exact immutable tag identities."""
from pathlib import Path
import hashlib,json,subprocess,time,urllib.request,urllib.error,zipfile
r=Path(__file__).resolve().parent
raw=r/'raw';w=Path(json.loads((raw/'owned-workspace.json').read_text())['path'])
p=r/'receipt.json';receipt=json.loads(p.read_text());tag=receipt['tag']
cmd=['gh','release','view',tag,'--repo','iamjudin/Fab','--json','tagName,isDraft,isPrerelease,url,assets']
result=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
assert result.returncode==0,result.stderr
publication=json.loads(result.stdout);assert publication['tagName']==tag and publication['isPrerelease'] and not publication['isDraft']
(raw/'publication.json').write_text(json.dumps(publication,indent=2)+'\n')
assert {x['name'] for x in publication['assets']}==set(receipt['assetsSha256'])
downloads=w/'anonymous';downloads.mkdir(exist_ok=True);attempts=[]
for name,digest in receipt['assetsSha256'].items():
 url=f'https://github.com/iamjudin/Fab/releases/download/{tag}/{name}'
 for attempt in range(3):
  try:
   request=urllib.request.Request(url,headers={'User-Agent':'Fab-release-verification'})
   with urllib.request.urlopen(request,timeout=60) as response:data=response.read()
   attempts.append({'asset':name,'attempt':attempt+1,'status':'downloaded anonymously'})
   break
  except urllib.error.HTTPError as exc:
   attempts.append({'asset':name,'attempt':attempt+1,'status':exc.code})
   if attempt==2:raise
   time.sleep(2*(attempt+1))
 assert hashlib.sha256(data).hexdigest()==digest,name
 (downloads/name).write_bytes(data)
source=Path(__file__).resolve().parents[3]/'plugins/fab'
expected={str(f.relative_to(source)):f.read_bytes() for f in source.rglob('*') if f.is_file() and '__pycache__' not in f.parts and not f.name.endswith('.pyc')}
with zipfile.ZipFile(downloads/f'fab-{receipt["version"]}.zip') as z:
 assert len(z.namelist())==74 and len(set(z.namelist()))==74 and set(z.namelist())==set(expected)
 assert all(z.read(name)==data for name,data in expected.items())
assert (downloads/'release-scope.json').read_bytes()==(source.parents[1]/'docs/release-plan.json').read_bytes()
for line in (downloads/'SHA256SUMS.txt').read_text().splitlines():
 digest,name=line.split('  ',1);assert hashlib.sha256((downloads/name).read_bytes()).hexdigest()==digest
remote=subprocess.check_output(['git','ls-remote','origin','refs/tags/v0.1.0-beta.*'],cwd=source.parents[1],text=True)
refs={ref.removeprefix('refs/tags/').removesuffix('^{}'):sha for sha,ref in (line.split('\t') for line in remote.splitlines()) if ref.endswith('^{}')}
assert refs[tag]==receipt['sourceCommit']
old=json.loads((raw/'previous-tags.json').read_text());assert all(refs[t]==sha for t,sha in old.items())
(raw/'remote-tags.txt').write_text(remote);(raw/'anonymous-downloads.json').write_text(json.dumps(attempts,indent=2)+'\n')
receipt['checks']['assets']='pass: anonymous hashes, full74-file ZIP/source and scope parity'
receipt['checks']['immutableTags']='pass: new source SHA and all previous peeled SHAs preserved'
receipt['publication']={k:publication[k] for k in ['url','isDraft','isPrerelease']}
p.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'publication':receipt['publication'],'assets':'pass','zipFiles':74,'oldTagsUnchanged':len(old)}))
