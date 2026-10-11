from pathlib import Path
import subprocess, json, hashlib, shutil, sys, re

root=Path('/private/tmp/fab-plugin-smokes-20261011')
mode=sys.argv[1]
source=root/('frozen-repair' if mode=='baseline' else 'repair')
helper=source/'plugins/local-index/scripts/index_notes.py'
arena=root/f'observer-{mode}'
arena.mkdir(exist_ok=False)
notes=arena/'notes'
notes.mkdir()
(notes/'alpha.md').write_text('# Alpha\nOriginal source note.\n')
(notes/'index.md').write_text('# User index\nOriginal user file.\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
original={p.name:sha(p) for p in notes.glob('*.md')}
def run(out):
    p=subprocess.run([sys.executable,str(helper),str(notes),str(out)],capture_output=True,text=True)
    return {'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
collision=run(notes/'index.md')
protected=sha(notes/'index.md')==original['index.md']
out=notes/'generated.md'
first=run(out)
first_bytes=out.read_bytes() if out.exists() else None
second=run(out)
second_bytes=out.read_bytes() if out.exists() else None
result={'mode':mode,'collision':collision,'foreign_file_preserved':protected,
        'first':first,'second':second,'repeat_bytes_equal':first_bytes==second_bytes,
        'self_excluded':bool(second_bytes) and 'generated.md' not in second_bytes.decode(),
        'alpha_preserved':sha(notes/'alpha.md')==original['alpha.md'],
        'output':second_bytes.decode() if second_bytes else None}
if mode=='after':
    baseline=json.loads((root/'baseline.json').read_text())['repair']
    keep=['README.md','accepted.md','notes/alpha.md','notes/index.md','plugins/local-index/skills/index/references/method.md']
    result['baseline_byte_comparison']={f:sha(source/f)==baseline[f] for f in keep}
    result['README_original_prefix_preserved']=(source/'README.md').read_bytes().startswith((root/'frozen-repair/README.md').read_bytes())
    result['method_original_prefix_preserved']=(source/'plugins/local-index/skills/index/references/method.md').read_bytes().startswith((root/'frozen-repair/plugins/local-index/skills/index/references/method.md').read_bytes())
    result['git_status']=subprocess.run(['git','status','--short'],cwd=source,capture_output=True,text=True).stdout
    result['git_remotes']=subprocess.run(['git','remote','-v'],cwd=source,capture_output=True,text=True).stdout
    result['git_commit_exists']=subprocess.run(['git','rev-parse','--verify','HEAD'],cwd=source,capture_output=True,text=True).returncode==0
(root/f'observer-{mode}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
