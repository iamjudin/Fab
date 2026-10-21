#!/usr/bin/env python3
"""Verify exact-tag installs without model execution or credential copying."""
from pathlib import Path
import json,os,subprocess,sys,hashlib
r=Path(__file__).resolve().parent
raw=r/'raw'; w=Path(json.loads((raw/'owned-workspace.json').read_text())['path'])
case=sys.argv[1]
assert case in ('clean','primary')
task_env=os.environ.copy()
if case=='clean':
    (w/'clean-home').mkdir(exist_ok=True)
    task_env['CODEX_HOME']=str(w/'clean-home')
    task_env.update({'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'credential.helper','GIT_CONFIG_VALUE_0':'','GIT_TERMINAL_PROMPT':'0'})
    for key in ('GH_TOKEN','GITHUB_TOKEN','OPENAI_API_KEY','CODEX_API_KEY'):
        task_env.pop(key,None)
commands=[]
if case=='primary': commands.append(['codex','plugin','marketplace','remove','fab-local'])
commands.extend([
    ['codex','plugin','marketplace','add','iamjudin/Fab','--ref','v0.1.0-beta.32'],
    ['codex','plugin','add','fab@fab-local','--json']])
records=[]
for n,cmd in enumerate(commands):
    result=subprocess.run(cmd,cwd=w,env=task_env,capture_output=True,text=True,timeout=120)
    (raw/f'{case}-{n}.stdout.txt').write_text(result.stdout)
    (raw/f'{case}-{n}.stderr.txt').write_text(result.stderr)
    records.append({'command':cmd,'exitCode':result.returncode})
    if result.returncode: raise SystemExit(f'{case} command{n} failed: see retained raw log')
home=Path(task_env.get('CODEX_HOME',str(Path.home()/'.codex')))
cache=home/'plugins/cache/fab-local/fab/0.1.0-beta.32'
source=Path(__file__).resolve().parents[3]/'plugins/fab'
def inventory(root):
    return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc')}
expected=inventory(source); actual=inventory(cache)
assert len(expected)==94 and actual==expected,(len(actual),len(expected))
version=json.loads((cache/'plugin.json').read_text())['version'];assert version=='0.1.0-beta.32'
snapshot=home/'.tmp/marketplaces/fab-local'
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=snapshot,env=task_env,text=True).strip()
receipt=json.loads((r/'receipt.json').read_text());assert head==receipt['sourceCommit']
meta={'case':case,'commands':records,'installedPath':str(cache),'version':version,'files':len(actual),'fullParity':True,'marketplaceHead':head,'isolatedHome':case=='clean','credentialCopied':False if case=='clean' else 'existing primary settings used','modelExecution':False}
(raw/f'{case}-install.json').write_text(json.dumps(meta,indent=2)+'\n')
receipt['checks']['cleanInstall' if case=='clean' else 'primaryInstall']='pass: exact tag and full94-file parity'
if case=='primary':receipt['installedPath']=str(cache)
(r/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(meta))
