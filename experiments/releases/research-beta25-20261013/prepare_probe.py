from pathlib import Path
import json, shutil

r = Path(__file__).resolve().parent
w = Path(json.loads((r / 'raw/owned-workspace.json').read_text())['path'])
shutil.copytree('plugins/fab', w / 'fab', dirs_exist_ok=True)
source = w / 'fab'
installed = Path('/Users/iamjudin/.codex/plugins/cache/fab-local/fab/0.1.0-beta.25')
prompts = {
    'assignment': f'Use Fab Research at {source}/skills/research/SKILL.md. Read applicable contracts and references.\n\nНужен готовый промпт для Deep Research по продукту Murmur: приложение для взрослых семейных групп, чтобы сохранять короткие рассказы о совместных поездках. Сравниваем запись без подсказок и с необязательными вопросами. Принято: без публичной ленты и обязательной ежедневной записи. Исследование потом может пригодиться другим продуктам. Сохрани условия аудитории и ситуации, а применение к Murmur вынеси отдельно. Само исследование сейчас не запускай. Результат на русском, компактные сравнения и понятные поля, причинные объяснения оставь коротким текстом.',
    'review': f'Use Fab Research at {installed}/skills/research/SKILL.md. Read applicable contracts and references.\n\nНиже синтетический учебный отчёт, все наблюдения вымышлены. Задание было сравнить необязательные вопросы и свободную запись в небольшой группе взрослых, включая эффект после недели. Отчёт: «В сессии участвовали шесть человек, четыре завершили запись с вопросами, двое без вопросов. Участники сказали, что интерфейс приятный, поэтому доказан рост еженедельного использования. Источник: University A. Каждая запись стоит 2 условные единицы и содержит 3 поездки, значит итоговая стоимость 12 единиц. Недельного наблюдения не было. В другом разделе стоимость названа 6 единиц». Проведи bounded review на пригодность для решения. Сведения извне не ищи, исходник не исправляй и не проводи новый тест. Покажи, что можно использовать, что не проверено и что делать дальше.',
}
(r / 'raw/prompts.json').write_text(json.dumps(prompts, ensure_ascii=False, indent=2) + '\n')
s = Path('experiments/releases/dialogue-beta24-20261013/smoke.py').read_text()
a = s.index('old = ')
b = s.index('out = ROOT', a)
s = s[:a] + "prompts = json.loads((raw / 'prompts.json').read_text())\ncwd = workspace / 'fresh'\n" + s[b:]
a = s.index("if case == 'resume':")
b = s.index('def inventory():', a)
s = s[:a] + s[b:]
s = s.replace("if not thread and case == 'resume': thread = prior['threadId']", '')
(r / 'smoke.py').write_text(s)
