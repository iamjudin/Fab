#!/usr/bin/env python3
"""Bounded direct-skill dialogue probes; no scoring prompt is sent to the model."""
import argparse,datetime,hashlib,json,os,signal,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=ROOT/'raw'
a=argparse.ArgumentParser();a.add_argument('--variant',required=True);a.add_argument('--case',required=True);a.add_argument('--turn',choices=['initial','followup'],default='initial');args=a.parse_args()
c=next(x for x in json.loads((ROOT/'cases.json').read_text()) if x['id']==args.case)
w=Path(json.loads((raw/'owned-workspace.json').read_text())['path'])/args.variant
out=ROOT/args.variant/args.case;out.mkdir(parents=True,exist_ok=True)
private=raw/args.variant/args.case;private.mkdir(parents=True,exist_ok=True)
message=c[args.turn]
if args.turn=='initial':
 skill=c.get('entry','brainstorm')
 prompt='Use Fab '+skill+' at '+str(w/('fab/skills/'+skill+'/SKILL.md'))+'. Read its contract and required references. This is a conversation-only request; respond to the person in Russian on ты.\n\n'+message
 cmd=['codex','exec','--json','--skip-git-repo-check','-s','read-only','-C',str(w),'-o',str(out/(args.turn+'.md')),'-']
else:
 prior=json.loads((out/'initial.meta.json').read_text())
 prompt=message
 cmd=['codex','exec','-C',str(w),'-s','read-only','resume','--json','--skip-git-repo-check',prior['threadId'],'-o',str(out/(args.turn+'.md')),'-']
(private/(args.turn+'.prompt.txt')).write_text(prompt)
before={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in w.rglob('*') if p.is_file()}
started=time.time()
with (private/(args.turn+'.events.jsonl')).open('w') as stdout,(private/(args.turn+'.stderr.txt')).open('w') as stderr:
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=stdout,stderr=stderr,start_new_session=True)
 try:
  proc.communicate(prompt.encode(),timeout=240);timedout=False
 except subprocess.TimeoutExpired:
  os.killpg(proc.pid,signal.SIGTERM);proc.wait(timeout=10);timedout=True
rows=[]
for line in (private/(args.turn+'.events.jsonl')).read_text().splitlines():
 try: rows.append(json.loads(line))
 except ValueError: pass
thread=next((r.get('thread_id') for r in rows if r.get('type')=='thread.started'),None)
if not thread and args.turn=='followup': thread=prior['threadId']
usage=[r.get('usage') for r in rows if r.get('type')=='turn.completed']
runtime={'model':'unknown','effort':'unknown'}
if thread:
 day=Path(os.environ.get('CODEX_HOME','/Users/iamjudin/.codex'))/'sessions'/datetime.datetime.now(datetime.timezone.utc).strftime('%Y/%m/%d')
 matches=list(day.glob('*'+thread+'*.jsonl')) if day.exists() else []
 for path in matches:
  for line in path.read_text().splitlines():
   try: row=json.loads(line)
   except ValueError: continue
   if row.get('type')=='turn_context':
    data=row.get('payload',{});runtime={'model':data.get('model','unknown'),'effort':data.get('effort',data.get('reasoning_effort','unknown'))}
after={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in w.rglob('*') if p.is_file()}
meta={'variant':args.variant,'case':args.case,'turn':args.turn,'exitCode':proc.returncode,'timeout':timedout,'seconds':round(time.time()-started,2),'threadId':thread,'actualRuntime':runtime,'usage':usage[-1] if usage else None,'workspaceUnchanged':before==after,'workspaceChanges':[k for k in set(before)|set(after) if before.get(k)!=after.get(k)],'command':cmd,'errors':[r for r in rows if r.get('type') in ['error','turn.failed']]}
(out/(args.turn+'.meta.json')).write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
