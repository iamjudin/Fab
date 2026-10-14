# Бэклог Fab

## Сейчас

Installed/public beta.27: ten independent skills,72files/fingerprint `b6a149b9ebfa968f`. [Release checks](../experiments/releases/continuation-beta27-20261014/report.md) confirm50regressions, scope, CI, anonymous assets and clean/primary exact-tag parity. Research contracts improve framing/readability/reuse/output review. Initial global-footer conflict and source corrective retained. External compliance remains PARTIAL. Bookworm task unimplemented, Canvas experimental.
Реализован и проверен ограниченный пакет переноса. Полный клиентский маршрут дошёл до прототипа; два сбоя потребовали отдельных коррекций. Общего PASS нет.

**Итог пакета:** Fab способен собрать исполняемый кандидат, но передача смысла между интерфейсными артефактами ещё ненадёжна. FAB-08 проверен в реальном браузере после коррекции и отдельно записанного обновления ресурса preview. Две проекции исправлены адресным partial corrective; текущий default — таблицы структуры/переходов; Canvas отдельно ждёт прототип creator, наблюдение уборки preview открыто. Оценка creator полезности/вкуса отдельна и не заменяет технический вывод. Новых полных прогонов ради статистики не нужно. Один разрешённый сброс использован.

**2026-10-12, mobile-first:** исследование включено; один новый app-маршрут дошёл
до прототипа, root UI bounded PASS, но ownership/return projection частично FAIL.
Узкий partial corrective завершён с сохранением model/IDs; текущая граница
в новом partial report. Полный маршрут ради статистики не повторяем. [Отчёт](../experiments/workflow-tests/2026-10-12-mobile-pipeline-results.md).


| ID | Статус | Задача | Evidence и следующая граница |
| --- | --- | --- | --- |
| FAB-01 | Закрыто | Начальный bundle и независимые исходы | Пять естественных запросов beta1; ограниченный PASS, не зрелость всех методов. |
| FAB-02 | Первое восстановление PASS; непрерывность открыта | Реальная непрерывность основного чата | 2026-10-11: текущий чат в Lab/Fab назначен основным; Fab Cowork восстановил цель, соглашения, evidence/границы и следующий шаг из проектных документов, Git проверен. Creator подтвердил успешное первое восстановление. Устойчивую непрерывность проверить при дальнейшей работе: сохранение решений, границ и текущего состояния без повторного брифинга. |
| FAB-03 | Открыто; адресный repair PASS | Перенос Product/Wireframe | Full beta.14 потерял branch-specific commit/cancel. Partial beta.15 исправил returns/ownership, но удалил совместимый feedback/Undo из-за отсутствия имени в domain model. Beta.16 fresh corrective сохраняет механизм и открытые детали, source/IDs; root guards/семантика PASS. [Evidence](../experiments/workflow-tests/2026-10-12-partial-routes-results.md). Next: наблюдать сохранение смысла в обычных интерфейсных изменениях; не выдавать partial за universal full-route maturity. |
| FAB-04 | Закрыто | Начальные контракты Prototype/Plugin/Delivery | Выбранные реальные UI-пути и source repair/readiness проверены. 2026-10-11: два fresh Plugin входа (создание/maintenance) завершили локальные исходы и content pages; root подтвердил сохранность и исправление self-indexing/перезаписи. [Evidence](../experiments/workflow-tests/2026-10-11-plugin-smokes-results.md). Это не installed discovery/generated-plugin behavior или выпуск в production. FAB-08 отдельно сохраняет новый сбой. |
| FAB-05 | Метод включён, bounded evidence | Экспертиза HIG/Material | Beta.14: lossless49sections и brief, четыре conditional owners; 7 unresolved bindings и partial primary check. [Audit](research-audits/mobile-structure-2026-10-12.md). Новый mobile route реально прочитал метод, сохранил app target и native boundary; root UI bounded PASS, map findings отдельно. Next: native/device и новые platform decisions только по конкретному вопросу; universal mobile maturity не заявлена. |
| FAB-06 | Закрыто | Явная оценка создательской оси в полной модели | Один corrective: Creator Intent сохранён, HJ/BJ оценены раздельно, неподтверждённые BJ не придуманы. Первый прогон был частичным FAIL; закрытие только проверенного контракта, не всех новых контекстов. |
| FAB-07 | Закрыто | Честная жизнь локального preview | Договор различает live link/run command и хранение данных. Полный маршрут дал run command; root поднял сервер и реально проверил reload. Не обещание фоновой работы любого сервера. |
| FAB-08 | Закрыто | Доступное восстановление в тестовом UI | Однократная имитация beta8; root браузером подтвердил draft → retry → сохранение без фонового контрола, готовность/история сохранены. Cache intervention отдельно; не универсальная гарантия recovery хранилища. |
| FAB-09 | Повторный FAIL; правка ждёт проверки | Уборка временной работы и наследование правила новыми плагинами | Beta.10 lifecycle/inheritance contract и root retention63files PASS. Partial beta.16 Wireframe оставил внешний SVG в общем tmp после final. Root сохранил SHA и убрал точный файл; [receipt](../experiments/workflow-tests/partial-routes-20261012/external-preview-cleanup.json). Beta.18 явно маршрутизирует transient renders в lifecycle: лимит deliverables не оправдывает tmp parking. Next: в следующем preview наблюдать фактическую уборку; generated-plugin inheritance отдельно ещё не проверен. |
| FAB-10 | Исправлено, ждёт проверки | Маркировка исследований и связи с проектами | Beta.11 eight-note migration PASS; beta.12 additive labels/usage revision contract. 2026-10-12 mobile ingestion: вопрос после ready pair → явное согласие → Fab:/tags/usage, body SHA сохранён; [receipt](../experiments/maintenance/mobile-ingestion-20261012/source-usage.json). Root workflow evidence, не independent model smoke. Отказ/второе имя/changed-source across projects ещё не наблюдались. |
| FAB-11 | Continuation correction released in beta.27; native consistency open | Соавторская оценка до работы и содержательные выводы после | Partial beta.15 дала мнение/реальное возражение/варианты/диалог, но Product final остался file-status-only. Beta.16 улучшение неполное; beta.17 fresh same-input corrective даёт рекомендацию, пользу и trip/reload компромисс, новые правила не объявлены принятыми. [Evidence](../experiments/workflow-tests/2026-10-12-partial-routes-results.md). Это developer/synthetic bounded evidence; next — сохранять такой вывод в обычной работе, не повторять ради статистики.2026-10-14: creator reports a correct scope acknowledgment with no continuation of the active goal. [Four source turns](../experiments/workflow-tests/dialogue-continuation-20261014/results.md), GPT-6.1 Sol/Medium: fresh beta.26 baseline already asks a concrete blocked choice. Shared-core/Brainstorm correction passes blocked choice, actual authorized output and completed-thanks controls. Source72files/fe44274906582314 and50regressions pass. Native original miss preserved, no comparative superiority or long-context closure. Creator approved local/public beta.27, [distribution](../experiments/releases/continuation-beta27-20261014/report.md) passes CI/assets/exact-tag clean-primary parity. Next: actual post-feedback continuation under real scope/choice constraints, native consistency remains open. |
| FAB-12 | Проверено ограниченно | Частичные задачи и короткие связки | 7primary + dialogue + natural-entry diagnostic: мнение, идеи, source-only audit, analysis→options, bounded Product, existing Wireframe, evidence→slice. Частичные дефекты и correctives различены; 12turns, input2073222/output30703. [Report](../experiments/workflow-tests/2026-10-12-partial-routes-results.md). Next: реальные короткие задачи/новые seams только по конкретной неопределённости; не обязательный full process. |
| FAB-14 | Released in beta.24; real-use stability open | Useful Brainstorm dialogue and optional techniques | Creator wants new thinking, grounded critique and useful questions, without a framework mask. [16 generic v1 turns](../experiments/workflow-tests/brainstorm-dialogue-20261013/results.md) were inconclusive; [6 contextual turns](../experiments/workflow-tests/brainstorm-context-20261013/results.md) preserve v1's depth miss and separate v2 corrective. [Five virtual situations/seven new v2 turns](../experiments/workflow-tests/brainstorm-v2-situations-20261013/results.md), GPT-6.1 Sol/Medium, satisfy bounded contribution, critique/agreement, feedback, exploration and accepted-scope checks; copy-anchor caveat retained. Source e7d94f8/evidence a572d3e; creator authorized promotion and public/local beta.24 release on 2026-10-13, integrated via 10ba4e6. [Release checks](../experiments/releases/dialogue-beta24-20261013/report.md) confirm beta.24 public/local parity and bounded installed behavior. Next: ordinary-use stability and actual creator usefulness; native desktop reread remains unobserved. Observed beta.23 project is separate; not a prerequisite for v2 testing. Complements FAB-11/FAB-12. |
| FAB-15 | Foundation correction released in beta.26; ordinary-use calibration open | Readable and reusable research | Creator authorized integration/local-public release in the feature chat on2026-10-13. [Return packet](handoffs/research-readability-return-2026-10-13.md): reader contract, localized presentation plan, independent topic/application, optional additive usage tags without new filename prefixes, output coverage/source/numeric review. [V3](../experiments/maintenance/research-readability-20261013/v3-results.md) is PARTIAL with source/arithmetic/layout failures retained.50regressions pass. Two source GPT-6.1 Sol/Medium turns preserve legacy host conflict and host-only corrective. [Distribution](../experiments/releases/research-beta25-20261013/report.md) verified: CI, anonymous assets, clean/primary exact-tag parity. No installed-model or native-render claim. Bookworm task prepared, not implemented/transferred. No automatic source migration or Canvas promotion. Creator-approved2026-10-14 foundation correction8145814 is integrated in main source: existing knowledge first, context without current-feature filtering, bounded foundation/focused uncertainty.72files/37cbf14af3e5a51b and50regressions pass. At source integration installed/public beta.25 remained unchanged. [Two fresh GPT-6.1 Sol/Medium source cases](../experiments/workflow-tests/research-foundation-20261014/results.md) satisfy bounded foundation/covered-question checks. Unspecified age-scope assumption retained, no baseline comparison or installed efficacy. Creator authorized beta.26 release, [exact distribution](../experiments/releases/foundation-beta26-20261014/report.md) passes CI/assets/clean-primary parity. Ordinary-use calibration and installed-model behavior remain open. |
| WF-01 | Адресный PASS | Физическое владение в IA | Partial beta.15 и beta.16 corrective вложили поездки/вещи в collections/items, сохранив исходные IDs/model; root JSON/guards/PNG проверены. Original full-route пропуск остаётся историческим FAIL, semantic preservation отдельно FAB-03. Next: применять смысловой review всех повторяемых owners в реальных изменениях, не только механический guard. |
| WF-17 | Исправлено, ждёт проверки | Содержательные gates и глубина | Partial/full и beta.14 mobile route без approval-пауз; model/blocks до кода. Semantic review карты всё ещё пропустил WF-01/FAB-03. Реальные спорные creator decisions/другие контексты не обобщены; глубина проверяется смыслом, не именами этапов. |
| FAB-13 | Proactive trigger failed; bounded recovery PASS | Готовность по поверхностям и изоляция переработок | [Политика](release-policy.md): beta.20 включает разрешённое создание/context transfer/recovery check. [Git smoke](../experiments/workflow-tests/2026-10-12-canvas-branch-smoke.md) PASS. [Chat receipt](../experiments/maintenance/chat-handoff-20261012/receipt.json): packet byte-equal, checkout чист, actual recovery pending; не создавать дубль. [Git workflow proposal](research/git-workflow-options-2026-10-12.md): main отсутствует, remote default bootstrap; рекомендована одна main/task branches/tags с conditional hotfix. Принятие/migration не авторизованы этим research. Native Obsidian/fresh routing открыты; Canvas FAIL не блокирует Prototype. 2026-10-13: main failed to propose separation before substantial research despite existing guidance. Creator sarcasm triggered the proposal, then approved transfer. [Actual handoff](handoffs/research-readability-2026-10-13.md) confirms chat/branch/context recovery, not proactive initiation. Canvas recovery remains separately unobserved. Next: assess the first workflow decision on substantial requests without a creator reminder, including a small-task control. Do not add duplicate wording or close this from creation success alone. |
| WF-20 | Открыто | Геометрия и читаемость Canvas | Два partial PNG root просмотрел: owners понятны, но стрелки плотные и return labels перекрываются даже при automatic no-warning. [Preview](../experiments/workflow-tests/partial-routes-20261012/wireframe-corrective/ui/structure.png). Read-only repro подтвердил пропущенный label-label overlap; [research/options](research/canvas-layout-options-2026-10-12.md). Default заменён таблицами; Canvas opt-in. Ветка codex/fab-map-view изолирована, parked до прототипа creator; затем варианты реализации. ELK spike не принят; viewer/engine не выбран. Native UI/community plugins/ELK не тестировались. |

## Публичный delivery route — 2026-10-12

Creator авторизовал публичный текущий iamjudin/Fab с историей и MIT. Local46tests, GitHub CI,
public tag/Release, anonymous assets и exact-tag install в отдельный cache PASS.
Обнаружен ref-switch FAIL: fixed README/Release notes требуют remove registration
перед add нового ref; реальный rollback beta.9 → update beta.22 PASS. Frozen tagged
README имеет явно исправленную erratum; tag/archive не переписывались. [Отчёт](../experiments/releases/public-beta22-20261012/report.md).
Это новый distribution outcome в FAB-13; Canvas/continuity/open behavior не закрывает.

## Research-library audit — 2026-10-14

FAB-15: [library audit](research-audits/library-2026-10-14.md) retains nine active
method sources and verifies that all 437 packet section texts remain present in
the corresponding library notes. One retired architecture note is moved out of
active Library into a recoverable historical archive with an unchanged file hash.
No permanent deletion, source rewrite, runtime change or new investigation.
Important attribution gaps remain in product structure, AI-native workflow and
technical UX dependencies. Eight source notes still have legacy service tags.
Proposed next knowledge work: evaluation of collaborative agents across evolving
multi-turn tasks, then shared initiative in human–AI problem solving. These
extend FAB-02/FAB-11/FAB-13/FAB-14 evidence needs, not new completed capabilities.
Readability and Canvas already have relevant knowledge. Native/UI/source validity
and real human value are not established by section retention.

## Правила

2026-10-13: [natural-use observation](../experiments/workflow-tests/2026-10-13-external-chat-observation.md)
extends FAB-03/FAB-11/FAB-12 evidence: useful contextual jobs and editable review
transfer, but reading ability from supplied research needed creator prompting.
Correction and initial omission remain distinct. Native board QA and full semantic
coverage were not independently verified. Hourly monitoring now records meaningful
changes; repairs are deferred for discussion, not automatic product interventions.

Один ID, один владелец и статус. Запись содержит ожидаемое → наблюдаемое, версию/evidence, следующий проверяемый шаг и границу закрытия. Дедуплицировать с прежними WF-ID; локальные продуктовые неизвестные остаются в проекте. Отложенный пункт имеет триггер. Закрытие не означает универсальную зрелость.

WF-01/17/20 сопровождаются здесь; Wireframer хранит историческое evidence и указатель. WF-26/27/28 пока имеют прежнего владельца. История — journal, текущий договор — handoff. Проверки запускаем, когда результат меняет решение.

## 2026-10-12 — partial-route baseline beta.15
9model turns:7primary,1synthetic follow-up,1natural-input diagnostic; GPT-6.1 Sol/Low.
Мнение/варианты/audit/analysis→options/evidence→slice и короткий диалог дали
полезные bounded outputs без full pipeline. Product Undo artifact PASS, final
reply «сохранил файл» — FAB-11 FAIL. Wireframe исправил WF-01/egress при сохранении
model/IDs, но удалил совместимый feedback/Undo лишь из-за отсутствия отдельного
названия в domain model — FAB-03 preservation FAIL. Initial runs сохранены.
Последующие correctives записаны в [итогах](../experiments/workflow-tests/2026-10-12-partial-routes-results.md);
исходные FAIL не переписаны, successful cases не повторялись. [Контракт](../experiments/workflow-tests/2026-10-12-partial-routes-contract.md),
[baseline usage](../experiments/workflow-tests/partial-routes-20261012/baseline-usage.json).

## Public presentation — 2026-10-12

Beta.23 candidate uses the approved Fab/Fabricator identity, creator icon and
English use-case-first copy. Local50regressions/package/scope checks pass.
[Evidence](../experiments/releases/branding-beta23-20261012/report.md).
Public beta.23/CI/exact-tag install/assets PASS; native icon display and fresh generated-language
behavior are unobserved. This extends FAB-13 without closing its chat-recovery gap.
