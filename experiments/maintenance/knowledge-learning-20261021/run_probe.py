#!/usr/bin/env python3
"""One frozen read-only discovery probe after explicit creator consent."""
from pathlib import Path
import hashlib,json,subprocess,time,os,signal
R=Path(__file__).resolve().parent;RAW=R/'raw';ROOT=R.parents[2]
def inv(root):
 return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
def main():
 assert not (RAW/'probe-events.jsonl').exists(),'Refuse a second launch'
 assert json.loads((RAW/'probe-authorization.json').read_text())['creatorApproved'] is True
 expected=json.loads((RAW/'source-inventory.json').read_text());assert inv(ROOT/'plugins/fab')==expected==inv(RAW/'frozen-package')
 work=Path(json.loads((RAW/'owned-workspace.json').read_text())['path']);before=inv(work);(RAW/'workspace-before.json').write_text(json.dumps(before,indent=2)+'\n')
 cmd=['codex','exec','--ignore-user-config','-m','gpt-6.1-sol','-c','model_reasoning_effort="medium"','-c','approval_policy="never"','-c','sandbox_workspace_write.network_access=false','--ephemeral','--json','--skip-git-repo-check','-s','read-only','-C',str(work),'-o',str(RAW/'probe-reply.md'),'-']
 (RAW/'probe-command.json').write_text(json.dumps(cmd,indent=2)+'\n')
 prompt='Use the available Fab source skills for the actual read-only request in request.md. Select the relevant capability from AGENTS.md and read its actual SKILL and applicable package references. Return the requested useful review, with actual evidence and next actions. Do not edit files, delegate, browse, install or publish.\n'
 start=time.monotonic();timeout=False
 with (RAW/'probe-events.jsonl').open('x') as out,(RAW/'probe-stderr.txt').open('x') as err:
  p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=out,stderr=err,start_new_session=True)
  try:p.communicate(prompt.encode(),timeout=180)
  except subprocess.TimeoutExpired:
   timeout=True;os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=10)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait(timeout=10)
 rows=[]
 for line in (RAW/'probe-events.jsonl').read_text().splitlines():
  try:rows.append(json.loads(line))
  except ValueError:pass
 turns=[x for x in rows if x.get('type')=='turn.completed'];commands=[x['item'] for x in rows if x.get('item',{}).get('type')=='command_execution' and x['item'].get('status')=='completed']
 meta={'configuredModel':'gpt-6.1-sol','effort':'medium','actualBackendIdentity':'not independently exposed by CLI','seconds':round(time.monotonic()-start,2),'exitCode':p.returncode,'timeout':timeout,'completedTurns':len(turns),'usage':turns[-1].get('usage') if turns else None,'workspaceUnchanged':inv(work)==before,'sourceUnchanged':inv(ROOT/'plugins/fab')==expected==inv(RAW/'frozen-package'),'commands':[{k:c.get(k) for k in ['command','exit_code','status']} for c in commands],'errors':[x for x in rows if x.get('type') in ['error','turn.failed']],'rootReview':'pending','installedNativeProof':False}
 (RAW/'probe-meta.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta))
if __name__=='__main__':main()
