# Fab Canvas — контекст отдельного чата

## Цель и текущее действие
Fab — модульный плагин для инди-создателя, десять самостоятельных навыков и
optional routes. Продукт сейчас сам Fab; тестовые приложения только evidence.
Этот workstream улучшает представление структурированных карточек и связей.
**Сейчас только восстановить контекст и ждать UI-прототип creator.** После него
предложить варианты реализации, пользу/риски и свою рекомендацию до разработки.
Прежнее предложение ELK spike первым отменено; engine/viewer пока не выбран.

## Что принято
Основной чат «Восстановить контекст Fab» (`01a12c88-4869-7f31-bf24-d56638a1408f`)
в `/Users/iamjudin/Desktop/Lab/Fab`, ветка `codex/fab-maintenance`, владеет
core, независимыми навыками, общим backlog, установленным runtime и релизами.
Здесь соавторство: русский на ты, своё мнение с причиной, реальные развилки до
зависимой работы; после работы вывод для цели и полезный следующий шаг.
Не быть диспетчером файлов. Не требовать повторного брифинга по известным решениям.

Default структуры/сценариев временно Markdown-таблицы. Canvas opt-in experimental
с открытым WF-20. Видимые блоковые экраны и исполняемые прототипы самостоятельны;
selected browser interactions уже проверены, native/production не объявлены готовыми.
Создатель предпочитает собственное представление карточек, но принесёт прототип
первым. Не заменять эту очередность своим layout spike.

## Источники и evidence
Feature baseline `codex/fab-map-view`: research commit `14f4dbf`, scope guard
`75540f1`, source package beta.18 (это source baseline, не текущий installed runtime).
Основная beta.19 закреплена `3e53097` / `checkpoint-beta19-2026-10-12`;
проверка новой ветки `25eaa72` на smoke-ветке, отчёт в main `860da1b`.
Beta.18 tag `checkpoint-beta18-2026-10-12` / `10e44cf` неизменен.
Main готовит beta.20 с новым handoff-договором; фактическую installed identity
проверить при входе, не брать старый путь cache как обязательный ресурс.

В feature baseline доступны:
- `docs/research/canvas-layout-options-2026-10-12.md`: исследование и грубые оценки;
- `experiments/analysis/canvas-layout-20261012/reproduction.json`: конкретный дефект;
- `experiments/workflow-tests/2026-10-12-partial-routes-results.md`: partial evidence;
- `experiments/workflow-tests/partial-routes-20261012/wireframe-corrective/result/product/reviews/structure.canvas`: immutable пример;
- `plugins/fab/skills/wireframe/scripts/canvas_preview.py`: текущий fallback renderer.

Актуальная общая политика в main (читать, не редактировать из feature):
`docs/release-policy.md`, `docs/backlog.md`, `docs/handoff.md` и этот packet.
Root path main указан выше; документы старого feature snapshot исторические.
Brain и старый cache не prerequisites. Landlord не читать/использовать.

## Что сломано и что неизвестно
`layout_warnings` проверяет подписи против карточек, но пропускает label-vs-label.
`save-return` и `cancel-item-return` перекрываются, хотя warnings=[]; root PNG
подтверждает дефект. JSON Canvas не хранит точные bends/label coordinates/parentId;
SVG-геометрия не доказывает нативную отрисовку Obsidian. Native UI не проверен.
Canvas Mindmap/Mindvas/Advanced Canvas и ELK исследованы, не внедрены/не тестированы
как решение. Снимок среды на дату research: Obsidian1.12.7, Canvas Mindmap1.0.2;
при практическом выборе совместимость проверить заново. Предварительные оценки
своего bounded MVP60–100h (+24–48h Obsidian wrapper) — rough, не обещание скорости.

## Владение и критерий возврата
Scope: cards/structure, соединения/неналожение, слои/сворачивание по прототипу,
выбранный viewer и его проверки. Не менять global core/version/release/backlog;
не устанавливать experimental source в shared runtime. Сохранять IDs, владельцев
вложенных коллекций/элементов, UC, commit/cancel/failure/return branches и Undo.
Feature хранит scoped findings/proposals; main принимает перенос/готовность.
Для возврата нужны согласованный data contract, representative и сложные cases,
семантическая сохранность, наблюдение реального viewer и честные границы.
Native Obsidian проверяется отдельно. Merge/publication/push только по явному scope.
Локальные проверенные checkpoints разрешены; reset/credit purchase не разрешены,
один ранее разрешённый reset уже использован. Subagents и новые чаты рекурсивно
не создавать. Не писать в другие чаты без прямой человеческой авторизации.

## Проверка восстановления
Проверить реальные cwd/branch/HEAD. Работать в изолированной рабочей копии,
не переключать branch основного checkout. Если host создал detached/new branch,
сообщить фактическое состояние; не объявлять ожидаемую ветку подтверждённой.
Прочитать релевантное evidence и кратко сообщить: цель, принятые решения,
известный дефект, ограничения и следующее действие. Пока нет прототипа — закончить
ориентацию с ожиданием его, без реализации, полного pipeline и новых тестов.
