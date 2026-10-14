from pathlib import Path
import json,hashlib,subprocess,sys,re
r=Path(__file__).resolve().parent
w=r/'raw/fixtures'
if not w.exists():
    w=Path(json.loads((r/'raw/owned-workspace.json').read_text())['path'])
recorded_root=Path(json.loads((r/'raw/owned-workspace.json').read_text())['path']).resolve()
def retained_path(value):
    path=Path(value).resolve()
    try:
        return (w/path.relative_to(recorded_root)).resolve()
    except ValueError:
        return path
sha=lambda b:hashlib.sha256(b).hexdigest()
checks={}
metas=[json.loads(f.read_text()) for f in sorted((r/'behavior').glob('*.meta.json'))]
checks['all_invocations_completed']=len(metas)==11 and all(m['exitCode']==0 and not m['timeout'] and not m['errors'] for m in metas)
checks['all_package_and_sentinel_preserved']=all(m['suppliedPackageUnchanged'] and m['sentinelUnchanged'] for m in metas)
start='<!-- fab-research-usage:start -->';end='<!-- fab-research-usage:end -->'
def usage(text):return json.loads(text.split(start,1)[1].split(end,1)[0])
for c in ['mark-declined','mark-additive','mark-revision']:
 root=w/c;inv=json.loads((r/'raw'/f'{c}.inventory.json').read_text());before,after=inv['before'],inv['after']
 protected=[n for n in before if n.startswith('Alpha/') or n.endswith('decisions.md') or n.startswith('fab/') or n in ['state.md','neighbor-sentinel.txt']]
 checks[c+'_protected_hashes']=all(before[n]==after.get(n) for n in protected)
 text=(root/'Library/Alpha: Queue design.md').read_text();body=text[text.index('# Queue design\n'):]
 packet=json.loads((root/'Beta/research/full.json').read_text());prov=json.loads((root/'Beta/research/provenance.json').read_text())
 checks[c+'_body_pair_hash']=body==(root/'Beta/research/original.md').read_text()==''.join(s['text'] for s in packet['sections']) and sha(body.encode())==prov['bodySha256']==packet['sourceSha256']
 if c=='mark-declined':
  checks[c+'_source_exact']=before['Library/Alpha: Queue design.md']==after['Library/Alpha: Queue design.md']
 else:
  rows=[json.loads(l) for l in (r/'raw'/f'{c}.events.jsonl').read_text().splitlines()]
  pre=next(d['item']['aggregated_output'] for d in rows if d.get('type')=='item.completed' and d.get('item',{}).get('type')=='command_execution' and d['item'].get('aggregated_output','').startswith(start))
  original_usage=usage(pre);final_usage=usage(text)
  old_alpha=next(x for x in original_usage['projects'] if x['project']=='Alpha');alpha=next(x for x in final_usage['projects'] if x['project']=='Alpha');beta=[x for x in final_usage['projects'] if x['project']=='Beta']
  checks[c+'_alpha_entry_exact']=old_alpha==alpha
  checks[c+'_one_beta_entry_tag']=len(beta)==1 and text.count('#Beta')==2 and text.split(end,1)[1].startswith('\n\n#Alpha #Beta\n\n')
  checks[c+'_beta_revision_links']=beta[0]['bodySha256']==sha(body.encode()) and all(retained_path(beta[0][k])==(root/'Beta/research'/name).resolve() for k,name in [('original','original.md'),('brief','brief.md'),('packet','full.json')])
  # Recover the explicitly bounded source body from the first pre-edit cat output.
  expected=(root/'Alpha/research/original.md').read_text() if c=='mark-additive' else (root/'Alpha/research/original.md').read_text()+'\n## New observation\nUse an inline error beside the affected field.\n'
  checks[c+'_body_preserved']=body==expected
  if c=='mark-revision':checks[c+'_other_consumer_named']='Alpha needs review' in (r/'behavior'/f'{c}.md').read_text() and all('Alpha/research/'+name in (r/'behavior'/f'{c}.md').read_text() for name in ['original.md','brief.md','full.json']) and alpha['bodySha256']!=beta[0]['bodySha256']
for c in ['sequence-source','sequence-shipped']:
 root=w/c;brief=(root/'implementation-brief.md').read_text();todo=(root/'checklist.txt').read_text()
 checks[c+'_actual_outputs']=all(token in brief.lower() for token in ['required','optional','retain','validation','correct']) and 'pending' in todo.lower()
 checks[c+'_social_no_mutation']=json.loads((r/'behavior'/f'{c}-3.meta.json').read_text())['changedFiles']==[]
gen=w/'generated-plugin/generated';package=gen/'csv-summary'
skill=(package/'skills/summarize-csv/SKILL.md').read_text();runtime=(package/'shared/runtime.md').read_text()
checks['generated_runtime_self_contained']=(package/'skills/summarize-csv/../../shared/runtime.md').resolve().is_file() and all(t in runtime.lower() for t in ['task-owned','retain useful','verify','symlinks','neighboring','incomplete cleanup'])
checks['generated_scratch_removed']=not any(p.is_dir() and (p.name.startswith('csv-summary-check-') or p.name=='__pycache__') for p in gen.rglob('*'))
cmd=['python3',str(gen/'checks/check_candidate.py')]
import os
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
p=subprocess.run(cmd,cwd=w/'generated-plugin',capture_output=True,text=True,env=env)
(r/'raw/root-generated-checks.txt').write_text(p.stdout+p.stderr)
checks['root_generated_checks']=p.returncode==0
usage_total={k:sum(m['usage'].get(k,0) for m in metas) for k in ['input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens']}
report={'checks':checks,'allChecksPass':all(checks.values()),'invocations':len(metas),'usage':usage_total,'seconds':round(sum(m['seconds'] for m in metas),2),'remainingInputBudget':1300000-usage_total['input_tokens'],'generatedOnlyModelExecution':'NOT RUN: remaining input budget below observed per-turn costs','reviewer':'root; unblinded; synthetic operator fixtures'}
(r/'root-assessment.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
