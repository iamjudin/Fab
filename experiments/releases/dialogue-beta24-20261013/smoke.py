#!/usr/bin/env python3
"""Bounded installed-skill probes; target is immutable during each turn."""
import datetime, hashlib, json, os, signal, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = ROOT / 'raw'
workspace = Path(json.loads((raw / 'owned-workspace.json').read_text())['path'])
case = sys.argv[1]
old = '/Users/iamjudin/.codex/plugins/cache/fab-local/fab/0.1.0-beta.23'
new = '/Users/iamjudin/.codex/plugins/cache/fab-local/fab/0.1.0-beta.24'
prompts = {
    'before': f'Use Fab Cowork at {old}/skills/cowork/SKILL.md. Read required references.\n\nРазрабатываем личное приложение для заметок о прогулках. Уже решили: одна короткая запись, без аккаунта и уведомлений. Сейчас мне нужно только уточнить, стоит ли делать заголовок обязательным. Дай мнение, ничего не реализуй.',
    'resume': 'Fab обновлён. Проверь доступную установленную версию Fab и заново прочитай актуальные инструкции Cowork и Brainstorm с нужными ссылочными материалами. Назови фактически прочитанную версию и путь. Продолжим эту же задачу, сохранив наши решения: я думаю сделать заголовок автоматически из первой строки, но позволить потом исправить. Что думаешь?',
    'brainstorm': f'Use Fab Brainstorm at {new}/skills/brainstorm/SKILL.md. Read required references.\n\nДелаю приложение для заметок о прогулках. В пилоте семь человек: записи делают по дороге несколько раз в день, перечитывают раз в неделю. Хочу заменить быстрые записи одной обязательной вечерней формой: впечатление, место, оценка, план следующей прогулки. Так будет меньше экранов, значит проще. Что думаешь? Пока обсуждаем, не выбирай за меня и ничего не реализуй.',
    'growth': f'Use Fab Cowork at {new}/skills/cowork/SKILL.md. Read required references.\n\nМы ведём общую отладку плагина. Правка рендера, которую считали маленькой, выросла: нужен свой контракт карточек, несколько вариантов соединений, отдельные серии визуальных проверок и, вероятно, несколько недель итераций. Общие вопросы релиза тоже продолжаются здесь. Как бы ты организовал дальнейшую работу? Пока хочу рекомендацию, ничего не создавай.',
}
cwd = workspace / ('conversation' if case in ['before', 'resume'] else 'fresh')
out = ROOT / 'behavior'; out.mkdir(exist_ok=True)
(raw / f'{case}.prompt.txt').write_text(prompts[case])
cmd = ['codex', 'exec', '--json', '--skip-git-repo-check', '-s', 'read-only', '-C', str(cwd), '-o', str(out / f'{case}.md'), '-']
if case == 'resume':
    prior = json.loads((out / 'before.meta.json').read_text())
    cmd = ['codex', 'exec', '-C', str(cwd), '-s', 'read-only', 'resume', '--json', '--skip-git-repo-check', prior['threadId'], '-o', str(out / f'{case}.md'), '-']
def inventory():
    return {str(p.relative_to(cwd)): hashlib.sha256(p.read_bytes()).hexdigest() for p in cwd.rglob('*') if p.is_file()}
before = inventory(); start = time.time()
with (raw / f'{case}.events.jsonl').open('w') as stdout, (raw / f'{case}.stderr.txt').open('w') as stderr:
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=stdout, stderr=stderr, start_new_session=True)
    try:
        proc.communicate(prompts[case].encode(), timeout=240); timedout = False
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGTERM); proc.wait(timeout=10); timedout = True
rows = []
for line in (raw / f'{case}.events.jsonl').read_text().splitlines():
    try: rows.append(json.loads(line))
    except ValueError: pass
thread = next((r.get('thread_id') for r in rows if r.get('type') == 'thread.started'), None)
if not thread and case == 'resume': thread = prior['threadId']
runtime = {'model': 'unknown', 'effort': 'unknown'}
day = Path(os.environ.get('CODEX_HOME', '/Users/iamjudin/.codex')) / 'sessions' / datetime.datetime.now(datetime.timezone.utc).strftime('%Y/%m/%d')
for path in day.glob('*' + str(thread) + '*.jsonl'):
    for line in path.read_text().splitlines():
        try: row = json.loads(line)
        except ValueError: continue
        if row.get('type') == 'turn_context':
            d = row.get('payload', {}); runtime = {'model': d.get('model', 'unknown'), 'effort': d.get('effort', d.get('reasoning_effort', 'unknown'))}
usage = [r.get('usage') for r in rows if r.get('type') == 'turn.completed']
meta = {'case': case, 'exitCode': proc.returncode, 'timeout': timedout, 'threadId': thread, 'actualRuntime': runtime, 'seconds': round(time.time() - start, 2), 'usage': usage[-1] if usage else None, 'workspaceUnchanged': inventory() == before, 'command': cmd, 'errors': [r for r in rows if r.get('type') in ['error', 'turn.failed']]}
(out / f'{case}.meta.json').write_text(json.dumps(meta, indent=2) + '\n')
print(json.dumps(meta))
raise SystemExit(proc.returncode or timedout)
