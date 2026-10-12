# Работа над Fab
Мы соавторы: советуй, критикуй, обсуждай существенные компромиссы заранее.
На новую идею/rule сначала дай собственную оценку и рекомендацию с причиной,
затем действуй. Ясность запроса не повод автоматически соглашаться. Не выдумывай
риски для баланса и не превращай рутинную реализацию в повторный approval.
После работы объясни, что результат означает для цели проекта, дай собственный
вывод и следующий полезный шаг с причиной. Техническую оценку не перекладывай
на creator; реальные развилки обсуждай кратко с вариантами и рекомендацией.
Если следующий необходимый шаг уже авторизован, продолжай, а не только предлагай.
Русский на ты; операторское внимание — ресурс. Результат/польза/риск/next сначала.
Актуальная цель — самостоятельные полезные навыки и optional routes для
инди-создателя; mobile focus, не обязательный greenfield pipeline.

## Индекс
1. docs/backlog.md — текущий пакет и единственный реестр Fab.
2. docs/beacon.md → plugins/fab/shared/core.md — канонические принципы.
3. docs/architecture/design.md — implemented vs planned skill boundaries.
4. docs/decisions.md, docs/journal.md — решения и технические checkpoints;
   docs/project-journal.md — значимые повороты, причины и evidence для истории проекта.
5. experiments/workflow-tests/ — test contracts/results.
6. docs/handoff.md — состояние для нового основного чата, когда подготовлено.

Перед edits Git/guidance/backlog; preserve others. Commit key verified stages.
Creator подтвердил 2026-10-12: проверять Git и делать локальные checkpoint-коммиты
самостоятельно после проверки; отдельное согласие на каждый commit не требуется.
После значимых решений/итераций/проверок поддерживать docs/project-journal.md:
коротко контекст/решение/результат/лимиты/evidence, новые записи сверху. Не каждый
tool call, полный чат или копия backlog. Publicator story packets — датированные
срезы evidence для будущего текста, не новые канонические списки задач.
Формат тестов выбираем по цели: fresh context для поведения, bounded CLI для
технических проверок. Фиксируем реальную модель/effort и изоляцию в evidence.
Experimental branch codex/; не merge/main/public release без явного scope.
Runtime package plugins/fab, docs не скрытый обязательный runtime источник.
Устанавливаемая beta самодостаточна, Brain/old cache не prerequisites.
Старый Landlord исключён. Не читать/использовать его. Старые тестовые продукты
не становятся целью Fab. Старый paused sprng heartbeat не возобновлять.
Основной рабочий чат — текущий чат в Lab/Fab с 2026-10-11; дальше работаем здесь.
FAB-02: первое восстановление контекста успешно; устойчивая непрерывность открыта.
Creator 2026-10-12 запросил создание отдельного Canvas-чата с переносом контекста.
При принятом отделении workstream не оставлять повторный брифинг creator:
подготовить packet, выполнить разрешённое создание/перенос и проверить восстановление.
Другие новые чаты — по прямому запросу; не расширять этот scope до hidden delegation.
Не создавай subagents без явного разрешения на делегацию.

## Current boundary
Installed Fab0.1.0-beta.21,65files/4760530ec4471a3a. All ten independent contracts.
46local regressions, bounded outcome/domain/UI/maintenance smokes; not universal
maturity. Current detailed state in docs/handoff.md and docs/backlog.md. Continue
across checkpoints when authorized; user explicitly rejected artificial pauses.
Private GitHub remote verified; no public release/merge. One authorized reset performed by creator; no further reset authorized.
Task-owned scratch is cleaned after verified retention; generated plugins inherit
a self-contained runtime cleanup rule. FAB-09 fresh generated-behavior check open.
Mobile app method ingested; shared product semantics with conditional platform
branches, not a universal native promise. One new mobile full-route test authorized.
That route reached executable candidate and root browser bounded PASS; WF-01/
FAB-03 projections partly failed; partial corrective now passed those owners/returns
and preserves compatible feedback. Partial-route suite completed12turns, useful
bounded outcomes; FAB-11 addressed in beta.17. Current next: Canvas readability/
SVG diagnostics (WF-20), observe beta.18 preview cleanup (FAB-09). No stats-only
full rerun. Evidence in 2026-10-12-partial-routes-results.md.
Beta.18 pinned at checkpoint-beta18-2026-10-12 (10e44cf), immutable.
Current main branch codex/fab-maintenance: core/general debugging and table fallback.
Canvas is experimental opt-in; default structure/scenarios are Markdown tables.
WF-20 remains open, prototypes have independent readiness. Release promises use
per-surface checks; see docs/release-policy.md and runtime shared/release-policy.md.
Map work isolated in codex/fab-map-view at separate managed checkout; parked until
creator supplies prototype, then propose implementation options. No engine choice
or ELK spike accepted. Main chat owns global backlog/release/runtime installation.
