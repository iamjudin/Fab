#!/usr/bin/env python3
"""Run the bounded fresh generated-package cleanup test."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
raw = ROOT / 'raw'
case = sys.argv[1]
cases = json.loads((ROOT / 'cases.json').read_text())
config = cases[case]
workspace = Path(json.loads((raw / 'owned-workspace.json').read_text())['path'])
cwd = workspace / config['fixture']
out = ROOT / 'behavior'
out.mkdir(exist_ok=True)

def inventory(folder):
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file() and not p.is_symlink()
            and '__pycache__' not in p.parts and not p.name.endswith('.pyc')}

def rollout(thread):
    if not thread:
        return None
    root = Path(os.environ.get('CODEX_HOME', '/Users/iamjudin/.codex')) / 'sessions'
    # Resume reuses the original creation date, not today's directory.
    for day in [datetime.datetime.now(datetime.timezone.utc).date(),
                datetime.datetime.now(datetime.timezone.utc).date() - datetime.timedelta(days=1)]:
        hits = list((root / day.strftime('%Y/%m/%d')).glob('*' + thread + '*.jsonl'))
        if hits:
            return hits[0]
    return None

def read_rollout(path):
    runtime, total = {'model': 'unknown', 'effort': 'unknown'}, None
    if path:
        for line in path.read_text().splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                continue
            payload = row.get('payload', {})
            if row.get('type') == 'turn_context':
                runtime = {'model': payload.get('model', 'unknown'),
                           'effort': payload.get('effort', payload.get('reasoning_effort', 'unknown'))}
            if row.get('type') == 'event_msg' and payload.get('type') == 'token_count':
                total = (payload.get('info') or {}).get('total_token_usage')
    return runtime, total

previous = config.get('resumeFrom')
thread = json.loads((out / f'{previous}.meta.json').read_text())['threadId'] if previous else None
_, before_usage = read_rollout(rollout(thread))
cmd = ['codex', 'exec', '--json', '--skip-git-repo-check', '-s', 'workspace-write',
       '-C', str(cwd), '-o', str(out / f'{case}.md')]
cmd += ['resume', thread, '-'] if thread else ['-']
before = inventory(cwd)
start = time.time()
with (raw / f'{case}.events.jsonl').open('w') as stdout, (raw / f'{case}.stderr.txt').open('w') as stderr:
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, start_new_session=True)
    try:
        proc.communicate((raw / f'{case}.prompt.txt').read_bytes(), timeout=240)
        timedout = False
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=10)
        timedout = True
rows = []
for line in (raw / f'{case}.events.jsonl').read_text().splitlines():
    try:
        rows.append(json.loads(line))
    except ValueError:
        pass
thread = next((r.get('thread_id') for r in rows if r.get('type') == 'thread.started'), thread)
runtime, after_usage = read_rollout(rollout(thread))
event_usage = next((r.get('usage') for r in reversed(rows) if r.get('type') == 'turn.completed'), None)
delta = None
if after_usage:
    delta = {k: value - (before_usage or {}).get(k, 0) for k, value in after_usage.items()}
    if any(value < 0 for value in delta.values()):
        delta = None
scope = ('rollout cumulative-counter difference for this invocation' if delta is not None
         else 'event-reported usage, scope unknown')
after = inventory(cwd)
meta = {'case': case, 'target': config['target'], 'threadId': thread,
        'resumeFrom': previous, 'actualRuntime': runtime, 'exitCode': proc.returncode,
        'timeout': timedout, 'seconds': round(time.time() - start, 2),
        'usage': delta if delta is not None else event_usage, 'usageScope': scope,
        'eventReportedUsage': event_usage,
        'changedFiles': [p for p in sorted(before.keys() | after.keys()) if before.get(p) != after.get(p)],
        'suppliedPackageUnchanged': all(before[p] == after.get(p) for p in before if p.startswith('plugin/')),
        'sentinelUnchanged': before.get('neighbor-sentinel.txt') == after.get('neighbor-sentinel.txt'),
        'command': cmd,
        'errors': [r for r in rows if r.get('type') in ('error', 'turn.failed')]}
(raw / f'{case}.inventory.json').write_text(json.dumps({'before': before, 'after': after}, indent=2)+'\n')
(out / f'{case}.meta.json').write_text(json.dumps(meta, indent=2)+'\n')
print(json.dumps(meta))
raise SystemExit(proc.returncode or timedout)
