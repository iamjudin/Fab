# Бэклог Fab

## Сейчас

Установлена beta.19: 10 самостоятельных навыков, 64 файла, fingerprint `40cf2ca557e185fb`. Табличный default, Canvas opt-in; ограниченная готовность по поверхностям, не общий PASS.
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
| FAB-11 | Адресный PASS | Соавторская оценка до работы и содержательные выводы после | Partial beta.15 дала мнение/реальное возражение/варианты/диалог, но Product final остался file-status-only. Beta.16 улучшение неполное; beta.17 fresh same-input corrective даёт рекомендацию, пользу и trip/reload компромисс, новые правила не объявлены принятыми. [Evidence](../experiments/workflow-tests/2026-10-12-partial-routes-results.md). Это developer/synthetic bounded evidence; next — сохранять такой вывод в обычной работе, не повторять ради статистики. |
| FAB-12 | Проверено ограниченно | Частичные задачи и короткие связки | 7primary + dialogue + natural-entry diagnostic: мнение, идеи, source-only audit, analysis→options, bounded Product, existing Wireframe, evidence→slice. Частичные дефекты и correctives различены; 12turns, input2073222/output30703. [Report](../experiments/workflow-tests/2026-10-12-partial-routes-results.md). Next: реальные короткие задачи/новые seams только по конкретной неопределённости; не обязательный full process. |
| WF-01 | Адресный PASS | Физическое владение в IA | Partial beta.15 и beta.16 corrective вложили поездки/вещи в collections/items, сохранив исходные IDs/model; root JSON/guards/PNG проверены. Original full-route пропуск остаётся историческим FAIL, semantic preservation отдельно FAB-03. Next: применять смысловой review всех повторяемых owners в реальных изменениях, не только механический guard. |
| WF-17 | Исправлено, ждёт проверки | Содержательные gates и глубина | Partial/full и beta.14 mobile route без approval-пауз; model/blocks до кода. Semantic review карты всё ещё пропустил WF-01/FAB-03. Реальные спорные creator decisions/другие контексты не обобщены; глубина проверяется смыслом, не именами этапов. |
| FAB-13 | Реализовано; Git isolation PASS; fresh behavior открыто | Готовность по поверхностям и изоляция переработок | [Политика](release-policy.md): runtime core предлагает изоляцию существенных независимых изменений; machine gate проверяет exact package/default promises, не истинность evidence. [Новая ветка/commit/возврат](../experiments/workflow-tests/2026-10-12-canvas-branch-smoke.md) технически PASS: main и installed runtime сохранены. Табличный fallback с сохранностью старой карты проверен; native Obsidian и fresh model routing не проверены. Canvas FAIL не блокирует независимый Prototype. |
| WF-20 | Открыто | Геометрия и читаемость Canvas | Два partial PNG root просмотрел: owners понятны, но стрелки плотные и return labels перекрываются даже при automatic no-warning. [Preview](../experiments/workflow-tests/partial-routes-20261012/wireframe-corrective/ui/structure.png). Read-only repro подтвердил пропущенный label-label overlap; [research/options](research/canvas-layout-options-2026-10-12.md). Default заменён таблицами; Canvas opt-in. Ветка codex/fab-map-view изолирована, parked до прототипа creator; затем варианты реализации. ELK spike не принят; viewer/engine не выбран. Native UI/community plugins/ELK не тестировались. |

## Правила

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
