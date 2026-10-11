from pathlib import Path
import json, hashlib, subprocess

root = Path('/private/tmp/fab-plugin-smokes-20261011')
root.mkdir(exist_ok=False)
runtime = '/Users/iamjudin/.codex/plugins/cache/fab-local/fab/0.1.0-beta.9/skills/plugin/SKILL.md'
def write(base, path, value):
    p = base / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value)
    return p
boundary = f'''Используй установленный Fab Plugin: {runtime}
Это автономный тест в отдельном workspace. Не используй другие исходные плагины или subagents. Не меняй Fab и глобальные настройки. Не устанавливай результат, не создавай remote, не коммить и не публикуй в GitHub/marketplace. Контент страницы подготовь локально, без внешних записей. Не заявляй проверенное поведение установленного результата без фактической проверки. Заверши доступную работу самостоятельно; фиксируй разумные предположения, а реальный блокер назови. Отвечай по-русски.
'''
new = root / 'create'
new.mkdir()
write(new, 'AGENTS.md', '# Test workspace\nРаботай только здесь. Сохраняй пользовательские файлы. Нет разрешения на установку, публикацию, remote или коммиты.\n')
write(new, 'samples/meeting.md', '# Встреча\nРешили проверить спрос до разработки.\nВозможно, начнём с Android.\nДоговорились до пятницы собрать пять интервью.\n')
write(new, 'samples/idea.md', '# Идея\nХочу инструмент для личной библиотеки заметок.\nНадо узнать, теряют ли люди решения после встреч.\nЦена пока неизвестна.\n')
prompt = boundary + '''Хочу небольшой плагин для Codex, который помогает инди-создателю разобрать присланные заметки: отдельно показать принятые решения, предположения, открытые вопросы и следующие действия, не додумывая отсутствующие факты. Иногда нужна только разборка одной заметки, иногда сравнение нескольких. Собери первую локальную рабочую версию; примеры в samples. Продумай достаточную нарезку навыков и проверь то, что можешь. Подготовь также контент для странички плагина: кому полезен, что делает, примеры запросов, ограничения и как начать. До публикации сейчас не идём.
'''
write(root, 'create.prompt.md', prompt)
repair = root / 'repair'
repair.mkdir()
write(repair, 'AGENTS.md', '# Test workspace\nСохраняй принятый метод и пользовательские правки. Нет разрешения на установку, публикацию, remote или коммиты.\n')
write(repair, 'accepted.md', '''# Принятый метод
Local Index составляет перечень имён Markdown-заметок, без чтения содержимого и без AI-сводки. Исходные заметки неизменяемы. Выход может лежать в каталоге заметок, но индекс не должен индексировать себя. Повтор своего индекса допустим; существующий чужой файл перезаписывать нельзя. Не расширять метод до разбора задач/решений.
''')
write(repair, 'plugins/local-index/plugin.json', json.dumps({'name':'local-index','version':'0.1.0','description':'Local Markdown filename index'}, indent=2)+'\n')
write(repair, 'plugins/local-index/skills/index/SKILL.md', '''---
name: index
description: Use for all notes, project planning, research, summarization, tasks and indexing.
---
# Local Index
Read [method](references/method.md). Run `python3 scripts/index_notes.py NOTES_DIR OUTPUT` from the package root. Do not change source notes. Follow the accepted filename-only method.
''')
write(repair, 'plugins/local-index/skills/index/references/method.md', '# Filename index\nList Markdown filenames only, sorted. Do not read note bodies, infer decisions or alter notes.\n')
write(repair, 'plugins/local-index/scripts/index_notes.py', '''from pathlib import Path
import sys

def build(folder, output):
    names = sorted(p.name for p in Path(folder).glob('*.md'))
    Path(output).write_text('# Notes index\\n\\n' + ''.join('- ' + name + '\\n' for name in names))

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
''')
write(repair, 'notes/alpha.md', '# Alpha\nНе менять эту заметку.\n')
write(repair, 'notes/index.md', '# Личная заметка\nЭто мой файл, а не сгенерированный индекс.\n')
write(repair, 'README.md', '# Local Index\nМой черновик страницы: сохранить эту строку.\n')
write(repair, 'docs/backlog.md', '# Backlog\n- Исправить повторную индексацию без расширения метода.\n')
subprocess.run(['git','init','-q'],cwd=repair,check=True)
subprocess.run(['git','add','.'],cwd=repair,check=True)
write(repair, 'README.md', '# Local Index\nМой черновик страницы: сохранить эту строку.\n\nНезакоммиченная правка автора: нужен простой пример запуска.\n')
prompt = boundary + '''У меня уже есть Local Index в plugins/local-index. При повторном запуске он добавляет свой результат в список заметок. Ещё я заметил, что он может затереть мой существующий index.md — это недопустимо. Исправь причины, сохрани принятый filename-only метод из accepted.md и мои незакоммиченные правки. Заодно проверь, что skill активируется именно для этой задачи, и что его инструкции реально исполнимы. Проверь исправление локально. Подготовь контент для странички этого плагина с понятным примером запуска и честными ограничениями. Не переизобретай плагин и не выпускай его в Git.
'''
write(root, 'repair.prompt.md', prompt)
baseline = {case: {str(p.relative_to(root/case)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/case).rglob('*') if p.is_file() and '.git' not in p.parts} for case in ('create','repair')}
write(root, 'baseline.json', json.dumps(baseline,indent=2))
print(root)
