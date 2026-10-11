# Работа над Fab
Мы соавторы: советуй, критикуй, обсуждай существенные компромиссы заранее.
На новую идею/rule сначала дай собственную оценку и рекомендацию с причиной,
затем действуй. Ясность запроса не повод автоматически соглашаться. Не выдумывай
риски для баланса и не превращай рутинную реализацию в повторный approval.
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
Installed Fab0.1.0-beta.14,60files/562f55c7ef31d731. All ten independent contracts.
36local regressions, bounded outcome/domain/UI/maintenance smokes; not universal
maturity. Current detailed state in docs/handoff.md and docs/backlog.md. Continue
across checkpoints when authorized; user explicitly rejected artificial pauses.
Private GitHub remote verified; no public release/merge. One authorized reset performed by creator; no further reset authorized.
Task-owned scratch is cleaned after verified retention; generated plugins inherit
a self-contained runtime cleanup rule. FAB-09 fresh generated-behavior check open.
Mobile app method ingested; shared product semantics with conditional platform
branches, not a universal native promise. One new mobile full-route test authorized.
That route reached executable candidate and root browser bounded PASS; WF-01/
FAB-03 projections partly failed. Current next: focused semantic Wireframe repair,
not stats-only full rerun. Evidence in 2026-10-12-mobile-pipeline-results.md.
