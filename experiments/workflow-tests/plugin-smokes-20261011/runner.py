from pathlib import Path
import subprocess, os, signal, time, json, sys

root=Path('/private/tmp/fab-plugin-smokes-20261011')
case=sys.argv[1]
start=time.monotonic()
cmd=['codex','exec','--json','--skip-git-repo-check','--approve-for-me','-C',str(root/case),'-o',str(root/f'{case}.final.md'),'-']
with (root/f'{case}.jsonl').open('wb') as out,(root/f'{case}.stderr').open('wb') as err:
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=out,stderr=err,start_new_session=True,cwd=root/case)
    try:p.communicate((root/f'{case}.prompt.md').read_bytes(),timeout=600)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid,signal.SIGTERM)
        p.wait(timeout=15)
meta={'exit':p.returncode,'seconds':round(time.monotonic()-start,1),'command':cmd,'events':[]}
for line in (root/f'{case}.jsonl').read_text().splitlines():
    try:e=json.loads(line)
    except ValueError:continue
    if e.get('type') in ('turn.completed','turn.failed','error','thread.started'):meta['events'].append(e)
(root/f'{case}.meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
print(json.dumps(meta,ensure_ascii=False))
sys.exit(p.returncode)
