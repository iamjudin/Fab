# Бэклог Fab

## Сейчас

Установлена beta.15: 10 самостоятельных навыков, 60 файлов, fingerprint `cf1d23be54742d51`.
Реализован и проверен ограниченный пакет переноса. Полный клиентский маршрут дошёл до прототипа; два сбоя потребовали отдельных коррекций. Общего PASS нет.

**Итог пакета:** Fab способен собрать исполняемый кандидат, но передача смысла между интерфейсными артефактами ещё ненадёжна. FAB-08 проверен в реальном браузере после коррекции и отдельно записанного обновления ресурса preview. Следующий технический шаг — исправить semantic preflight и две проекции Wireframe; оценка creator полезности/вкуса отдельна и не заменяет технический вывод. Новых полных прогонов ради статистики не нужно. Один разрешённый сброс использован.

**2026-10-12, mobile-first:** исследование включено; один новый app-маршрут дошёл
до прототипа, root UI bounded PASS, но ownership/return projection частично FAIL.
Next — узкая коррекция Wireframe по двум находкам с сохранением модели/кода,
не новый полный прогон. [Отчёт](../experiments/workflow-tests/2026-10-12-mobile-pipeline-results.md).


| ID | Статус | Задача | Evidence и следующая граница |
| --- | --- | --- | --- |
| FAB-01 | Закрыто | Начальный bundle и независимые исходы | Пять естественных запросов beta1; ограниченный PASS, не зрелость всех методов. |
| FAB-02 | Первое восстановление PASS; непрерывность открыта | Реальная непрерывность основного чата | 2026-10-11: текущий чат в Lab/Fab назначен основным; Fab Cowork восстановил цель, соглашения, evidence/границы и следующий шаг из проектных документов, Git проверен. Creator подтвердил успешное первое восстановление. Устойчивую непрерывность проверить при дальнейшей работе: сохранение решений, границ и текущего состояния без повторного брифинга. |
| FAB-03 | Открыто | Перенос Product/Wireframe | Прежние partial/full маршруты дошли до prototype. 2026-10-12 beta.14 mobile route: model/UC/rules сохранены, но S-03 «commit → parent» не отражает create-trip S-01→S-03→S-02; Save/Cancel egress edges отсутствуют. Root UI работает; находка в интерфейсной проекции. Next: явные branch-specific outcomes shared form + узкая проверка, без full rerun. |
| FAB-04 | Закрыто | Начальные контракты Prototype/Plugin/Delivery | Выбранные реальные UI-пути и source repair/readiness проверены. 2026-10-11: два fresh Plugin входа (создание/maintenance) завершили локальные исходы и content pages; root подтвердил сохранность и исправление self-indexing/перезаписи. [Evidence](../experiments/workflow-tests/2026-10-11-plugin-smokes-results.md). Это не installed discovery/generated-plugin behavior или выпуск в production. FAB-08 отдельно сохраняет новый сбой. |
| FAB-05 | Метод включён, bounded evidence | Экспертиза HIG/Material | Beta.14: lossless49sections и brief, четыре conditional owners; 7 unresolved bindings и partial primary check. [Audit](research-audits/mobile-structure-2026-10-12.md). Новый mobile route реально прочитал метод, сохранил app target и native boundary; root UI bounded PASS, map findings отдельно. Next: native/device и новые platform decisions только по конкретному вопросу; universal mobile maturity не заявлена. |
| FAB-06 | Закрыто | Явная оценка создательской оси в полной модели | Один corrective: Creator Intent сохранён, HJ/BJ оценены раздельно, неподтверждённые BJ не придуманы. Первый прогон был частичным FAIL; закрытие только проверенного контракта, не всех новых контекстов. |
| FAB-07 | Закрыто | Честная жизнь локального preview | Договор различает live link/run command и хранение данных. Полный маршрут дал run command; root поднял сервер и реально проверил reload. Не обещание фоновой работы любого сервера. |
| FAB-08 | Закрыто | Доступное восстановление в тестовом UI | Однократная имитация beta8; root браузером подтвердил draft → retry → сохранение без фонового контрола, готовность/история сохранены. Cache intervention отдельно; не универсальная гарантия recovery хранилища. |
| FAB-09 | Исправлено, ждёт проверки | Уборка временной работы и наследование правила новыми плагинами | 2026-10-11: после Plugin smoke пакеты/evidence оставались в `/tmp` вместе с helpers. Beta.10: task-owned scratch → verified retention → cleanup в core/Plugin/Testing; новые плагины получают автономное runtime-правило. 36 regressions и installed parity PASS. Root сохранил 63 файла текущего прогона, сверил SHA и удалил только его workspace/helpers; [evidence](../experiments/workflow-tests/plugin-smokes-20261011/cleanup.json). Next: при следующем создании/тесте наблюдать фактическое наследование и уборку; статические проверки это не закрывают. |
| FAB-10 | Исправлено, ждёт проверки | Маркировка исследований и связи с проектами | Beta.11 eight-note migration PASS; beta.12 additive labels/usage revision contract. 2026-10-12 mobile ingestion: вопрос после ready pair → явное согласие → Fab:/tags/usage, body SHA сохранён; [receipt](../experiments/maintenance/mobile-ingestion-20261012/source-usage.json). Root workflow evidence, не independent model smoke. Отказ/второе имя/changed-source across projects ещё не наблюдались. |
| FAB-11 | Исправлено, ждёт проверки | Соавторская оценка до работы и содержательные выводы после | Beta.13 pre-action contract; beta.14 fresh mobile route начал с обоснованной оценки, bounded signal. Creator затем указал на диспетчерский итог без достаточной интерпретации/мнения. Beta.15 core/Cowork требует вывод для цели, последствия и рекомендацию с причиной; реальные развилки — варианты/компромиссы до зависимой работы. Установка/регрессии не доказывают смену поведения. Next: наблюдать содержательные итоги и dialogue в обычной работе, не гонять тест ради статистики. |
| WF-01 | Открыто | Физическое владение в IA | Старый full: flat20/0 → beta7 corrective5surfaces. Beta.14 fresh mobile: 3surface groups + item-owner; mechanical PASS, но trip-row owner для S-01/open отсутствует вопреки interface.md. Root JSON/PNG просмотр. Next: semantic preflight всех повторяемых collections/items, не только одной card; узкий corrective с IDs/прототипом прежними. |
| WF-17 | Исправлено, ждёт проверки | Содержательные gates и глубина | Partial/full и beta.14 mobile route без approval-пауз; model/blocks до кода. Semantic review карты всё ещё пропустил WF-01/FAB-03. Реальные спорные creator decisions/другие контексты не обобщены; глубина проверяется смыслом, не именами этапов. |
| WF-20 | В следующее обновление | Геометрия и читаемость Canvas | SVG/PNG routing и диагностика проверены; corrected map просмотрена root. Native render, большие карты и creator readability требуют конкретной проверки. |

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
Next: narrow shared artifact-handoff + Wireframe semantics correction, два fresh
corrective; no repeat successful cases. [Контракт](../experiments/workflow-tests/2026-10-12-partial-routes-contract.md),
[baseline usage](../experiments/workflow-tests/partial-routes-20261012/baseline-usage.json).
