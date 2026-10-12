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
4. docs/decisions.md, docs/journal.md — решения и checkpoints.
5. experiments/workflow-tests/ — test contracts/results.
6. docs/handoff.md — состояние для нового основного чата, когда подготовлено.

Перед edits Git/guidance/backlog; preserve others. Commit key verified stages.
Creator подтвердил 2026-10-12: проверять Git и делать локальные checkpoint-коммиты
самостоятельно после проверки; отдельное согласие на каждый commit не требуется.
Формат тестов выбираем по цели: fresh context для поведения, bounded CLI для
технических проверок. Фиксируем реальную модель/effort и изоляцию в evidence.
Experimental branch codex/; не merge/main/public release без явного scope.
Runtime package plugins/fab, docs не скрытый обязательный runtime источник.
Устанавливаемая beta самодостаточна, Brain/old cache не prerequisites.
Старый Landlord исключён. Не читать/использовать его. Старые тестовые продукты
не становятся целью Fab. Старый paused sprng heartbeat не возобновлять.
Основной рабочий чат — текущий чат в Lab/Fab с 2026-10-11; дальше работаем здесь.
FAB-02: первое восстановление контекста успешно; устойчивая непрерывность открыта.
Новый чат только по прямому запросу.
Не создавай subagents без явного разрешения на делегацию.

## Current boundary
Installed Fab0.1.0-beta.18,60files/c463bb6928771c74. All ten independent contracts.
36local regressions, bounded outcome/domain/UI/maintenance smokes; not universal
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
Beta.18 pinned at checkpoint-beta18-2026-10-12 (10e44cf). Current work: research
Canvas/card layout alternatives before implementation; see docs/research/
canvas-layout-options-2026-10-12.md. Proposed ELK adapter is not accepted yet;
primary interactive viewer choice remains open. No third-party installs or map edits.
