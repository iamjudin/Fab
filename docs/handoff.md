# Рабочее состояние Fab

## Цель и договор

Один bundle с 10 самостоятельными навыками и необязательными маршрутами для инди-создателя. Mobile focus; Landlord исключён. Мы соавторы: рекомендации, критика и существенные компромиссы до действия. Русский на ты, сначала результат/польза/риск. Операторское внимание и токены — ресурсы. Checkpoint не повод остановиться.

## Где работаем

- Source: /Users/iamjudin/Desktop/Lab/Fab, текущая codex/fab-maintenance; публичный beta.22 tag v0.1.0-beta.22 на8186ed6. Canvas остаётся отдельно; merge не выполнялся.
- Public remote: https://github.com/iamjudin/Fab . GitHub beta.22 prerelease опубликован; main migration/Canvas merge нет.
- 2026-10-12 creator подтвердил самостоятельные Git checks и локальные коммиты
  проверенных этапов. Формат теста на наше усмотрение; evidence указывает actual
  model/effort и fresh-context boundary. Это не обязательные новые sidebar-чаты.
- Installed Fab0.1.0-beta.23,68files, fingerprint7a402724db9b66ae, marketplace fab-local.
-50local regressions and source/cache parity PASS. Public exact-tag install/CI/assets are verified for beta.23.
- Beta.18 закреплена локальным tag `checkpoint-beta18-2026-10-12`;
  [границы checkpoint](checkpoints/fab-beta.18.md). Пакет можно подключать к
  одному проекту для ограниченного реального использования; карта не имеет общего PASS.
- Partial-route suite завершён: 12turns, адресные FAB-11/FAB-03/WF-01 PASS;
  next — SVG readability/diagnostics WF-20 и наблюдение cleanup beta.18 FAB-09.
  [Актуальный вывод](../experiments/workflow-tests/2026-10-12-partial-routes-results.md).
- Основной рабочий чат — текущий чат в Lab/Fab с 2026-10-11; creator подтвердил, что дальше работаем здесь.
- FAB-02: первое восстановление контекста через Fab Cowork успешно; устойчивая непрерывность пока открыта.
- Wireframer0.2.5/recovery сохранены; Fabricator4543046/ahead3 и его чужие файлы не менялись.
- Ровно один разрешённый сброс выполнен пользователем; дальнейшие сбросы не разрешены.

## Что доказано

2026-10-11: два свежих прямых входа Fab Plugin (GPT-6.1 Sol/Low CLI) завершили
создание нового пакета и ремонт существующего с подготовкой контента страниц.
Root подтвердил локальные проверки и сохранность; тестовые пакеты не установлены
и не опубликованы. [Отчёт](../experiments/workflow-tests/2026-10-11-plugin-smokes-results.md).
Автоматический выбор skill и installed behavior созданных пакетов не проверены.

Пять самостоятельных исходов beta1; частичный Product→Wireframe; выбранные реальные UI-пути Prototype; Plugin source repair + честная Delivery readiness. Полный клиентский маршрут beta5 прошёл model→UC/slice→structure/scenarios→visible blocks→prototype. Это кандидат, не client acceptance.

Первый Canvas полного маршрута провалил владение: ноль групп. Beta7 corrective восстановил пять поверхностей и вложенность, исходные связи/IDs/роль/правила сохранены; prototype bytes при этой правке неизменны. Root просмотрел PNG из SVG, не native Obsidian.

Creator-axis corrective прошёл отдельно: оценка двух осей даже при одном акторе, без выдуманных BJ. Первичный FAIL не переписан как чистый PASS.

Root браузером проверил создание/Enter/валидацию, собственные задачи волонтёра, ready/undo/history, cancel edit, переназначение без потери ready, soft cancel/restore и reload. FAB-08 выявил недоступный persistent failure toggle за modal. Beta8 corrective заменил его однократной имитацией; root реально повторил сохранение в той же форме без работы с фоном. Результат и одна запись истории подтверждены.

## Завершённый пакет и следующий смысловой шаг

Автономная сборка beta и ограниченные технические проверки завершены. Не запускать новый полный продуктовый прогон ради статистики. Нужно оценить полезность bundle/кандидата с создателем; реальные continuity, native Obsidian, usability, большие карты и production guarantees не закрыты.

Отчёт: experiments/workflow-tests/2026-10-10-autonomous-beta-results.md .
Backlog содержит конкретные границы и триггеры. Native mobile экспертиза требует отдельного общего исследования: docs/research-briefs/mobile-structure-interaction-deep-research.md . После исследования применять его по вопросу, не добавлять обязательные этапы.

## Кандидат и среда

Full workspace: /private/tmp/fab-beta5-full-route-20261010 .
Preview: http://127.0.0.1:8873/prototype/ — root server session69883. Если завершится: запустить run.sh8873 из workspace. Долговечность сервера отделена от localStorage. Root tab14 сохранён как кандидат.

Reload и свежая вкладка сначала исполняли старый JS. Root добавил явную ревизию URL app.js?revision=recovery-beta8, затем наблюдал новое сообщение и успешный retry. Это поправка среды, не чистый исход первичного прогона. Beta9 уточняет проверку актуальности preview; новых агентных проверок ради этого не было.

Логи recovery-aborted-before-reset сохранены отдельно; первый лимитный abort не исчез из истории. 13 завершённых CLI попыток + 1 aborted; root overhead отдельно/неизвестен.

## Сохранность и ownership

Оригинал, map corrective и recovery result заморожены отдельно в beta5-full. Root environment/documentation edits перечислены в intervention packet. Старые архивы не перезаписаны. WF-01/17/20 owner Fab; WF-26/27/28 пока Wireframer. Основной рабочий чат перенесён в Lab/Fab; source старого плагина не изменён.

## 2026-10-11 — основной чат перенесён
Creator назначил текущий чат в Lab/Fab основной рабочей средой и подтвердил:
«Дальше работаем здесь». Через Fab Cowork прочитаны AGENTS, handoff, backlog,
beacon и autonomous-beta-results; проверены Git и общий runtime-договор.
В первом ответе восстановлены цель, соглашения соавторства, проверенные границы,
открытые вопросы и следующий полезный шаг. Creator подтвердил успешное первое
восстановление для FAB-02. Это наблюдаемый первый перенос, а не доказательство
устойчивой непрерывности: она остаётся открытой до дальнейшего продолжения работы
с сохранением решений и границ. Ветка codex/bootstrap-beta сохранена.
Mobile-structure Deep Research запущен creator; результат ожидается.

## 2026-10-11 — lifecycle временной работы
Beta.10 добавляет общий runtime-договор: один каталог задачи, сохранение полезных
результатов/evidence, проверка копии и уборка только своего disposable scratch.
Plugin переносит самостоятельное правило в создаваемые пакеты; Testing сохраняет
frozen evidence в архив проекта. Удаление результата Product отделено от housekeeping.
36 локальных регрессий и source/cache parity PASS; fresh model-run не выполнялся.
FAB-09 остаётся fixed-awaiting-check для будущего generated-plugin поведения.

Последний Plugin smoke сохранён (63 файла с проверенными SHA, плюс helpers) в
`experiments/workflow-tests/plugin-smokes-20261011/raw/local-run` (ignored local archive).
Тестовые пакеты и raw logs теперь там, а не в `/private/tmp`; отчёт и content pages
остаются в отслеживаемом evidence. Workspace и точные standalone helpers этого
прогона удалены. Старые tmp/preview inputs не тронуты; runtime старых тестовых пакетов
задним числом не менялся. Публикации нет.

## 2026-10-11 — видимая маркировка исследований Fab
Research ingestion теперь явно задаёт для включённых maintainer-оригиналов
`Fab: <исходное название>.md`, `Использование в Fab`, fab-import marker и
`#fab/imported`, без переименования исходного исследовательского заголовка.
Восемь notes в Brain/Library перенесены с Wireframer: на Fab:, top-блок указывает
на текущие brief/full и сохраняет историю Wireframer. Тела исследований совпали
по SHA; существующих ссылок с прежними именами/URI-encoding не найдено.
Оригинальные backups в ignored `experiments/maintenance/research-labels-20261011/raw/originals`,
receipt — migration.json рядом. Scratch helper удалён. Beta.11 installed parity
PASS. Старые пакеты/исследовательские titles/историческое evidence не переписаны.

## 2026-10-12 — опциональная маркировка проекта и связи исходника
Creator уточнил: после обработки спросить, добавить ли имя текущего проекта
к исходному документу и тег внутри; прежние имена сохранить и добавить новое.
Beta.12: вопрос после готового brief/full, конкретные before/after/tag, согласие
нужно только для пометки исходника. `Fab: Title.md` → `Fab + Murmur: Title.md`,
`#project/murmur`; без дублей, при отказе исходник неизменен.
Top usage-блок хранит список проектов, расположения brief/full и обработанную
ревизию/дату. Local provenance остаётся при отказе от внешней пометки.
При повторной обработке изменённого исходника перечисляются отстающие/непроверенные
проекты; их файлы и решения не обновляются автоматически. Annotation-only правки
отличаются от ревизии research body. Legacy boundaries не угадываются.
36 регрессий и beta.12 source/cache parity PASS. Fresh model behavior ещё не
наблюдалось — FAB-10 reopened fixed-awaiting-check. Старые originals не менялись.

## 2026-10-12 — обратная связь соавтора до изменений
Creator указал на автоматическое согласие без собственной оценки. Предыдущий
coauthor-договор существовал, но core оставался общим, Cowork явно требовал
recommendation лишь при неоднозначности; в текущем чате принцип не был выдержан.
Beta.13 конкретизирует реакцию на новую идею/rule/behavior: обоснованное согласие
либо конкретное сомнение/tradeoff, полезная рекомендация до implementation.
Это сквозной договор всех навыков, не обязательный Cowork gate. Значимые
неразрешённые развилки обсуждаем до зависимых edits; уже принятые решения и
рутину не открываем заново, риски/возражения ради формы не придумываем.
36 регрессий и installed parity PASS; реальная следующая дискуссия — наблюдение
для FAB-11, а не автоматически подтверждённый behavioral PASS.

## 2026-10-12 — мобильное исследование и новый pipeline
Creator предоставил мобильное исследование и запросил новый полный app-маршрут
до рабочего прототипа, с возможностью позже поддержать web. Beta.14: mobile
brief/full,49losslesssections, Product/Wireframe/Prototype/Delivery conditional links.
Root primary-check Apple modality/tab-bars и Android back-stack; поиск не всегда
команда, dedicated search surface возможна. 7 source binding unknowns сохранены.
Общий смысл/правила остаются переносимыми, platform surfaces/evidence условные.
36regressions/source-cache PASS. После ingestion creator согласился на пометку:
исходник теперь `Fab: Мобильная структура и взаимодействие для Fab.md`, tags
`#project/fab`/`#fab/imported` и usage-блок, body SHA прежний. Receipt в
experiments/maintenance/mobile-ingestion-20261012/source-usage.json.
Один fresh iOS-first travel-packing candidate в mobile-pipeline-20261012 завершён.
Root UI/структурная проверка отдельно от author harness; итог ниже.
Нативная реализация/OS/device и desktop web не объявляются проверенными.

## 2026-10-12 — результат app-пайплайна
241.1s/input708771/cached659968/output10996, GPT-6.1 Sol/Low default CLI,
один primary без corrective. Product/сценарии/отдельные blocks до кода; mobile
метод прочитан, отсутствие отдельных BJ обосновано. Root browser IAB реально
прошёл создание/Enter/валидацию, edit-cancel/save, packed/Undo/Осталось,
one-shot failure → draft → retry без дубликата, trip isolation, same-origin reload,
Escape и long-name layout при320/430CSSpx. Selected UI bounded PASS.

Полный clean PASS не дан: trip-row ownership S-01/open не отражён group,
shared S-03 «Save/Create → parent» и interface.md не различают create-trip
commit в S-02 от cancel в S-01; egress edges отсутствуют. Mechanical guard PASS
не доказывает этот смысл. Next — focused Wireframe semantic preflight/коррекция,
не full rerun и не изменение рабочей модели/прототипа ради карты.

Preview http://127.0.0.1:8842/prototype/ , root server session3372. Авторский
server закончился после CLI; root запустил ту же root/port, source/JS не менял.
Запуск и материалы: experiments/workflow-tests/mobile-pipeline-20261012/README.md.
Candidate ignored, initial snapshot/raw logs preserved; runner removed, other
previews untouched. Prototype bytes/SHA прежние после root наблюдения.
Отчёт: experiments/workflow-tests/2026-10-12-mobile-pipeline-results.md.
Native Obsidian/device, 200% scaling, usability/creator acceptance не проверены.

## 2026-10-12 — соавторский вывод после работы
Creator указал: итог прогона читался как диспетчерский отчёт; техническую
интерпретацию и выбор следующего полезного шага нельзя оставлять ему.
Наш вывод: Fab собирает рабочий кандидат, но интерфейсные проекции ещё могут
передать следующему разработчику неверный смысл. Рекомендуемый шаг — semantic
preflight/узкая коррекция WF-01 и FAB-03 с сохранением модели и прототипа.
Beta.15 закрепляет в core/Cowork вывод для цели, последствия и рекомендацию с
причиной, реальные варианты при развилке. Нет обязательного шаблона, нового
gate или остановки авторизованной работы. FAB-11 остаётся awaiting behavior;
следующее обычное продолжение должно показать содержательный итог без напоминания.

## 2026-10-12 — автономные частичные задачи
Creator разрешил отдельные partial-task tests и автономные адресные исправления;
2–3five-hour windows — допустимый запас при необходимости, credit resets не
разрешены. Экспериментальная ветка codex/partial-workflow-tests; не merge обратно.
Baseline beta.15:7primary+1synthetic follow-up+1natural-entry diagnostic, свежие
CLI contexts вне repo, GPT-6.1 Sol/Low.9turns522.4sum-seconds/input1280784/
cached1105920/output18988. Консультации, варианты, read-only audit и короткие
analysis→options/evidence→slice полезны без обязательного full process.
Два partial FAIL: Undo document достаточен, но final только file status (FAB-11);
Wireframe owners/returns исправлены, однако совместимый Undo удалён из-за
отсутствия имени команды в domain model (FAB-03). Исходные ответы сохранены.
Beta.16 установлена с узкой правкой этих различений; source/cache и36tests PASS.
Следующий шаг — два fresh correctives с теми же inputs, без подсказки findings.
Contract/evidence: experiments/workflow-tests/2026-10-12-partial-routes-contract.md,
partial-routes-20261012. Это developer evaluation, не independent human acceptance.

## Итог автономного partial-пакета — 2026-10-12
Прогоны завершены:12turns/835.4sum-seconds/input2073222/cached1817472/output30703,
GPT-6.1 Sol/Low. [Результат](../experiments/workflow-tests/2026-10-12-partial-routes-results.md).
Fab полезен для мнения/альтернатив/read-only audit и коротких analysis→options/
evidence→slice без обязательного pipeline. Beta.17 Product corrective исправил
file-status-only итог: рекомендация/причина/компромисс с honest proposal status.
Beta.16 Wireframe corrective сохраняет feedback/Undo, owners/returns/model/IDs.
Это scoped developer/synthetic PASS, не все реальные пользовательские контексты.

Current beta.18:60files/c463bb6928771c74, source/cache/36tests PASS. Последняя правка
явно связывает temporary renders с lifecycle после фактически оставленного SVG;
fresh model cleanup18 ещё не наблюдался. Root SVG сохранил/SHA проверил/убрал.
Все11workspaces+5helpers verified и owned scratch удалён; raw retained/ignored,
readable/results долговечны. Старые previews и server3372 не тронуты.

Текущий рекомендуемый next — читаемость Canvas/исправление SVG label diagnostics
(WF-20): root PNG показывает наложение return labels вопреки no-warning. Следующий
нужный preview также проверит cleanup18; нет необходимости нового full model-run.
Ветка codex/partial-workflow-tests остаётся отдельной, merge/public release нет.

## 2026-10-12 — checkpoint18 и исследование карт
Creator выбрал WF-20 следующим фокусом, запросил research/options до реализации
и закрепление текущей версии для возможного подключения к одному проекту.
Beta.18 закреплена tag checkpoint-beta18-2026-10-12 на10e44cf; source/runtime
c463bb6928771c74 совпадают, package не менялась. Ветка research отделена.
Read-only repro: checker warnings=[], но save-return/cancel-item-return labels
пересекаются; label-vs-label проверки нет. JSON Canvas не хранит bends/label
positions, поэтому собственный preview не обещает native fidelity.
Исследованы Canvas Mindmap/Mindvas/Advanced Canvas, Kanvas/Excalidraw, ELK и
viewer alternatives. Local Obsidian1.12.7, Canvas Mindmap1.0.2 enabled;
Advanced Canvas7.1.0 и6.5.4 требуют1.13.0. Ничего не устанавливалось.
[Варианты и рекомендация](research/canvas-layout-options-2026-10-12.md): честная
diagnostics correction + маленький ELK core/adapter spike; собственный полноценный
viewer/plugin только по результату. Это proposal, не принятое решение.
Вопрос creator об основном interactive view (Obsidian vs local web) отправлен;
ожидаемый выбор определяет native adapter scope. До него implementation нет.
Creator затем выразил предпочтение своему редактору и запросил оценку с отладкой,
готов набросать UI. Предварительно: layout spike6–12h, prototype24–40h total,
bounded MVP60–100h total; Obsidian custom-view wrapper+24–48h. Это rough engineering
estimate, не подтверждённая скорость;35–45%внутри диапазонов на debug/checks.
Own UI на готовом layout engine рекомендован; container/manual-pin UX ещё открыты,
implementation не запускалась. Детальный scope/границы в research note.

## 2026-10-12 — изоляция карты и политика готовности
Creator сначала подготовит свой UI-прототип карты; затем предложим реализацию.
Это отменяет прежний предлагаемый порядок ELK spike первым. Сейчас принят
табличный fallback: Markdown-структура/переходы default, Canvas experimental opt-in.
Prototype и блоковые экраны отдельны; сбой Canvas не блокирует их. WF-20 не закрыт.

Основная работа перенесена в codex/fab-maintenance в Lab/Fab. Отдельная ветка
codex/fab-map-view и managed checkout готовы, parked до creator prototype.
Исторический checkpoint beta.18/tag сохранён. Main owns backlog/core/release;
feature не меняет общий runtime и не merge автоматически. Новый чат пока не создан.
Архитектура/политика: [release-policy](release-policy.md). Runtime policy и
executable gate фиксируют exact identity/default scope/checks/limits; это не
автоматическое доказательство качества и не технический запрет любого git push.
Beta.19 source candidate; установка/проверки отмечаются отдельным checkpoint ниже.

### Проверенный локальный checkpoint beta.19
Установлена через `codex plugin add fab@fab-local --json`:64files/40cf2ca557e185fb,
source/cache parity PASS,46deterministic regressions PASS, release plan eligibility
PASS для объявленного limited beta scope; Canvas default=false и readability FAIL
сохранён. [Пример таблицы](../experiments/maintenance/release-policy-20261012/structure-table.md)
сохранил25nodes/8edges/full JSON snapshot; старые map bytes не менялись.
Ветка карты имеет собственный scope-checkpoint75540f1, изменений renderer нет.
GitHub workflow подготовлен, не запускался на remote; branch protection не меняли.
Fresh model table generation/proactive isolation/native Obsidian ещё не наблюдались.
Next: пользоваться table/default на реальной частичной задаче; карту разбираем после
creator prototype. Main продолжает общую отладку Fab. Public release/merge/push нет.

## 2026-10-12 — тест новой Canvas-ветки
По запросу creator выполнен bounded deterministic Git smoke: новая
codex/canvas-branch-smoke от main3e53097, marker-only commit25eaa72 в отдельном
checkout. Основная ветка/HEAD/tracked files и installed beta19 не изменились.
Checkout возвращён на codex/fab-map-view75540f1, clean; test branch сохранён отдельно.
[Отчёт](../experiments/workflow-tests/2026-10-12-canvas-branch-smoke.md).
Без model runs/new chat/merge/push/install. FAB-13 independent behavioral boundary
открыта; WF-20/ожидание UI-прототипа не менялись. Не создавать дубли map-workstream.

## 2026-10-12 — реальное отделение Canvas-чата
Creator уточнил: система должна сама создавать отдельный чат и переносить
необходимый контекст при разрешённом отделении задачи. Beta.20 добавляет
self-contained shared/workstream-handoff.md, routes из release/project/Cowork.
46regressions/package/scoped gate PASS; installed65files/597115ccbb4b0a59,
source/cache parity PASS. Новые чаты не создаются из обычного implementation
permission без соответствующей человеческой авторизации.

Подготовлен [packet](handoffs/canvas-workstream-2026-10-12.md), byte-for-byte copy
закреплена в feature c1681d5. Старый managed checkout архивирован после проверки
clean/no ignored files. create_thread в проекте Fab с worktree/ref codex/fab-map-view
принял запрос и вернул client ID; host подготовил /Users/iamjudin/.codex/worktrees/60c9/Fab.
Пока фактический thread ID/ответ не подтверждены — восстановление не считать PASS.
Initial prompt: orientation только, проверить Git, сохранить creator-first prototype
order, не реализовывать/merge/install/publish. Основной чат остаётся общей отладкой.

### Наблюдаемая граница handoff
Main checkpoint beta20:83ab56e. Новый checkout /Users/iamjudin/.codex/worktrees/60c9/Fab
на codex/fab-map-view/c1681d5, clean; packet в main и feature byte-equal.
create_thread client ID `client-new-thread:64e92d6c-ad1f-4658-b27c-a25aa7a90cb8`.
Повторные штатные list_threads пока не раскрыли фактический thread ID; не передавать
client ID в read_thread/wait_threads. Recovery pending, не PASS. Дополнительный
дублирующий чат не создавать. После появления thread ID — read/wait его ориентацию
и записать, сохранил ли creator-first prototype и разделение scope.
[Receipt](../experiments/maintenance/chat-handoff-20261012/receipt.json).
Опциональная `cowork.chat-handoff` в release plan experimental/default=false;
отсутствие observed recovery не блокирует прежние независимые исходы Cowork.

## 2026-10-12 — исследование общего Git-процесса
Creator запросил объяснение веток по ситуациям и best-practice research.
[Результат/proposal](research/git-workflow-options-2026-10-12.md): одна постоянная
main + короткие codex/task branches + version tags; conditional release/hotfix,
полный Git-flow/develop пока не нужен. Это рекомендация, не принятое новое правило.
Readonly remote confirmed: main нет, default codex/bootstrap-beta/e6dfeab,
новые checkpoints18/19/20 ещё локальные; HEAD983fbf6 был22commits ahead remote
до сохранения этого research. Canonical integration line/remote backup — реальный
следующий пробел, не новая необходимость ещё одного viewer/plugin.
Migration/default-branch change/merge/push/cleanup не выполнялись. Runtime beta20
не менялся. Canvas checkout/recovery pending и creator-first prototype сохранены.
Следующий полезный шаг — согласовать конкретный переход из proposal; не считать
исследование разрешением на изменение shared GitHub settings или интеграцию.

## 2026-10-12 — история проекта для дальнейшего продолжения
По запросу creator через Publicator Extractor проверен существующий технический
docs/journal.md; он сохранён без переписывания. Создан [project journal](project-journal.md):
14значимых этапов в обратной хронологии, причины/альтернативы/turns/результаты/лимиты
с evidence. [Story packet](story-packets/fab-development-2026-10-12.md) содержит
evidence map confirmed/needs-check/do-not-use и story spine для возможного Writer.
Просмотрены текущая переписка, durable Fab docs/reports/receipts/Git и последние
пять turns старого Plugin Wireframer о переезде; ранняя дискуссия объединения
целиком не восстановлена, поэтому точный состав старого merger остаётся needs-check.
AGENTS задаёт дальнейшее обновление нового журнала на значимых границах; backlog
остаётся единственным реестром задач. Runtime/version/Git-process не менялись.

## 2026-10-12 — простой проектный тег
Creator выбрал `#Fab` вместо namespace/service pair в показанной mobile note.
Beta.21: Research использует простой принятый project tag; bundle import хранится
в metadata marker, без видимого imported tag. В исходнике mobile заменена только
строка технического блока на `#Fab`, research body побайтно прежний и import marker
сохранён. Filename/processing revision и другие notes не менялись. Backup verified;
[receipt](../experiments/maintenance/research-tag-style-20261012/receipt.json).
Installed65files/4760530ec4471a3a, source/cache/46tests/scoped gate PASS.
Fresh model generation по новой tag policy отдельно не наблюдалась. FAB-10 другие
consent/refusal/additive/source-revision границы остаются открытыми.

## 2026-10-12 — Первый публичный delivery route

Creator разрешил открыть текущий iamjudin/Fab, выбрал MIT и сохранение истории
с author email/local paths. Repo PUBLIC, default codex/fab-maintenance; main
не создавалась, Canvas не merged. Beta.22: metadata/license/notice/public README,
поведенческие инструкции beta.21 сохранены. Installed67files/71349e50dbffe9c0,
source/cache parity и46regressions/scoped gate PASS. Первый GitHub CI PASS;
публичный commit-pinned remote marketplace/install из отдельной cwd/cache PASS.
Tag v0.1.0-beta.22 на8186ed6/GitHub prerelease/exact-tag install PASS; anonymous
assets SHA/source bytes PASS. Исправлена update-инструкция: marketplace remove
перед add другого ref; реальный rollback9/update22 PASS. Tagged README сохраняет
ошибочную историческую update-фразу, maintained README и Release notes её явно исправляют. [Distribution report](../experiments/releases/public-beta22-20261012/report.md).

## 2026-10-12 — Approved public presentation

Fab — brainstorm, build, ship; full name Fabricator. Original opaque512px factory
icon bundled unchanged in logo/composerIcon. New Git/GitHub authored text is English;
conversation remains Russian. Source research/frozen evidence retain their language.
README now leads with use cases; install/limits/developer detail are linked below.
Beta.23 installed:68files/7a402724db9b66ae,50local checks/parity PASS; public
delivery/CI/exact-tag installation/anonymous asset parity PASS. Native card display and fresh language-rule behavior are unobserved.
[Evidence](../experiments/releases/branding-beta23-20261012/report.md).

## 2026-10-12 — Legacy retirement completed

Local Landlord, Wireframer, Fabricator and Separator folders are retained as
ordinary directories with verified working-file preservation. Local/remote Git
history is saved in ignored archives; Desktop entries and installed old plugins
are removed. Landlord/Separator were not installed; chats remain untouched.
GitHub deletion completed after creator refreshed delete_repo and confirmed
ready: iamjudin/-plug, Wireframer, Fabricator and Separator-1 are absent from the
authenticated repository list; the other six repositories remain. Final346file
and archive SHA checks PASS. Runtime Fab beta.23 unchanged.
[Local checkpoint](../experiments/maintenance/retire-legacy-20261012/status.md).

2026-10-12 follow-up: empty iamjudin/igolka_pro also retired at creator request.
No branches/tags/releases/issues existed; local metadata retained. GitHub and
Desktop now list Fab, Storyteller, Bookworm, Tarsy and Publicator. No local file
or chat was removed for this additional cleanup.
