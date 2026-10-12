# Журнал проекта Fab

Этот журнал сохраняет значимые решения, повороты и результаты с evidence для
восстановления контекста и будущих материалов. Текущие задачи остаются в
[backlog](backlog.md), подробные технические checkpoints — в [journal](journal.md),
актуальный рабочий договор — в [handoff](handoff.md).

Записи идут от новых к старым. `confirmed` означает подтверждение конкретного
события/результата в названной границе; `needs-check` — открытое утверждение;
`do-not-use` — вывод, который evidence не позволяет использовать.
Backfill выполнен по текущему чату и проектным материалам за2026-10-10–12;
старый технический журнал сохранён без переписывания. Это внутренний контекст,
не готовый публичный текст и не подтверждение принятия открытых предложений.

<!-- Добавлять значимые этапы: контекст, решение/альтернатива, результат,
     предел evidence, ценность для будущего материала и следующий вопрос.
     Не записывать каждый tool call, полный чат или частные детали. -->

## 2026-10-12 — Fab adopts an approved icon and use-case-first presentation

- Type: decision
- Project area: public branding, repository language and release checks
- Status: confirmed — approved identity and local checks; pending — public beta.23 delivery and native display.
- Evidence: [verification report](../experiments/releases/branding-beta23-20261012/report.md); creator icon and accepted tagline in this chat.
- Summary: role nouns were discussed and rejected before the creator chose “brainstorm, build, ship”. Fab remains the name; Fabricator is explained in the description. The original icon is bundled unchanged, use cases precede installation, and technical detail moves to linked docs. New Git-facing authored text is English; conversation language and historical research are independent. Package checks now catch missing/corrupt/outside-package branding and localized listing text;50regressions pass.
- Article value: successful installation did not prove public presentation was complete. Creator feedback exposed a concrete missing check rather than a need for another full product run.
- Follow-up: verify remote beta.23 and exact-tag package/assets; keep native host rendering and fresh language-rule behavior explicitly unknown.

## 2026-10-12 — Fab проходит реальный публичный delivery route

- Type: milestone
- Project area: Delivery, GitHub distribution
- Status: confirmed — явный public/MIT/history scope, remote CI и commit-pinned clean install; confirmed — final tag/Release и corrected update/rollback; frozen README erratum сохранена.
- Evidence: [distribution report](../experiments/releases/public-beta22-20261012/report.md), [first CI](https://github.com/iamjudin/Fab/actions/runs/38269178037), source0763cea.
- Summary: creator выбрал открытие текущего репозитория с историей вместо отдельного public distribution repo и подтвердил сохранение author email/paths. Beta.22 добавляет MIT/notices и install/update/rollback copy. Первый push получил HTTP400; per-command HTTP/1.1/postBuffer retry прошёл, глобальный Git не менялся. Repo PUBLIC, default maintenance; CI и remote Git marketplace/install из отдельной cwd/cache PASS. Все67files совпадают по bytes/fingerprint.
- Article value: локальная сборка не доказывает публичную доставку; проверяется канал, а не только package gate. Исходный transport failure сохранён в evidence.
- Result: v0.1.0-beta.22/8186ed6 опубликован, exact-tag clean install и anonymous ZIP SHA/bytes PASS. Add нового ref на существующий marketplace FAIL: исправлена последовательность remove/add/reinstall. Rollback9 → update22 реально прошёл. Tagged README не переписан; maintained README/Release notes явно исправляют update erratum.
- Follow-up: подключать к реальному проекту по проверенным инструкциям; Canvas/native и прочие behavioral границы не закрываются релизом.

## 2026-10-12 — Видимая маркировка исследования упрощена до имени проекта

- Type: decision
- Project area: Research metadata
- Status: confirmed — явный выбор creator и точечная миграция; needs-check — новые model-generated annotations.
- Evidence: выбор `#Fab` в текущем чате, [receipt](../experiments/maintenance/research-tag-style-20261012/receipt.json), [ingestion rule](../plugins/fab/skills/research/references/ingestion.md).
- Summary: namespace `#project/fab` и служебный `#fab/imported` были выведены рядом. Создатель выбрал один простой `#Fab`. Beta.21 меняет новый default; mobile note исправлена только внутри технического блока, тело по SHA/bytes сохранено. Import status остался в скрытой metadata, обработанная research revision прежняя.
- Article value: пользовательская маркировка и служебный статус должны иметь понятные разные роли; изменение metadata не является новой редакцией исследования.
- Follow-up: другие старые notes не мигрировались без явного scope; прочие FAB-10 cases остаются открытыми.

## 2026-10-12 — От отдельных веток к общему Git-процессу

- Type: question
- Project area: Git и интеграция
- Status: confirmed — исследование и фактические refs; needs-check — принятие и внедрение процесса.
- Evidence: [research/proposal](research/git-workflow-options-2026-10-12.md), commit9501996.
- Summary: изоляция задач уже работала, но `main` отсутствовала, GitHub default оставалась bootstrap-ветка, а современные checkpoints были локальными. Исследованы GitHub flow, trunk-based и Git-flow; предложены одна постоянная `main`, короткие task-ветки и release-теги с conditional поддержкой версий. Это предложение, не миграция.
- Article value: локальные checkpoints и разветвление ещё не образуют управляемую интеграцию и удалённое сохранение актуального продукта.
- Follow-up: согласовать переход/default branch/private push/CI/protection scope; Canvas сохранить отдельно. Не описывать `main` как уже созданную.

## 2026-10-12 — Изоляция задачи потребовала переноса контекста

- Type: milestone
- Project area: Cowork и рабочие среды
- Status: confirmed — Git smoke и context packet; needs-check — фактическое восстановление нового Canvas-чата.
- Evidence: [Git smoke](../experiments/workflow-tests/2026-10-12-canvas-branch-smoke.md), [handoff packet](handoffs/canvas-workstream-2026-10-12.md), [chat receipt](../experiments/maintenance/chat-handoff-20261012/receipt.json);860da1b/83ab56e/983fbf6.
- Summary: создатель уточнил, что Fab должен передавать отдельную задачу вместе с необходимым контекстом. Проверены новая ветка/marker-only commit/возврат без изменения общего runtime. Beta.20 добавила разрешённое создание чата, durable packet и проверку recovery. Новый checkout и byte-equal packet подтверждены; сервис вернул только client ID, ответ нового чата на последней проверке не наблюдался.
- Article value: ветка, отдельные файлы и рабочий контекст имеют разные роли; подготовленный prompt не доказывает реальное восстановление.
- Follow-up: получить actual thread ID и проверить ориентацию без создания дубля. Учитывать права/tool availability; не превращать это в скрытый swarm.

## 2026-10-12 — Готовность разделена по результатам, карта заменена таблицей

- Type: decision
- Project area: release policy и Wireframe
- Status: confirmed — правило, установка и сохранность преобразования; needs-check — fresh table generation/native display.
- Evidence: [политика](release-policy.md), [verification](../experiments/maintenance/release-policy-20261012/verification.json), [таблица](../experiments/maintenance/release-policy-20261012/structure-table.md);3e53097.
- Summary: создатель предложил временно показывать информацию схемы таблицей, сохранив работающие прототипы. Beta.19 сделала Markdown-структуру/переходы default, Canvas — explicit experimental. Конвертер сохранил25nodes/8edges/full snapshot. Добавлены per-surface release plan и executable gate: известный FAIL/unknown не допускается как готовый default. Проверены46локальных регрессий, source/cache parity.
- Article value: дефект одного представления можно ограничить, сохранив полезные независимые выходы; замена формата имеет свои проверки и не закрывает исходный баг.
- Follow-up: наблюдать таблицы в реальных задачах. Canvas WF-20 остаётся открытым; общий PASS всего Fab не заявлен.

## 2026-10-12 — «Нет предупреждений» оказалось слабее видимой читабельности

- Type: experiment
- Project area: Canvas layout
- Status: confirmed — воспроизведение дефекта и research; needs-check — новое представление/engine.
- Evidence: [исследование](research/canvas-layout-options-2026-10-12.md), [reproduction](../experiments/analysis/canvas-layout-20261012/reproduction.json), [PNG](../experiments/workflow-tests/partial-routes-20261012/wireframe-corrective/ui/structure.png);43972e1/14f4dbf.
- Summary: подписи return-стрелок пересекались при `warnings=[]`: проверка сравнивала labels с карточками, но пропускала label-vs-label. Исследованы community Canvas-решения, ELK/адаптер и собственный viewer. Создатель предпочёл собственное представление и изменил порядок: сначала его UI-прототип, затем варианты реализации. Предложение начать с ELK spike не принято.
- Article value: механическая диагностика не заменяет просмотр; геометрия SVG и native Obsidian имеют разные возможности. Rough estimate не равен подтверждённой скорости разработки.
- Follow-up: дождаться прототипа. Engine/viewer, нативная совместимость и layout больших карт пока открыты; ничего из рассмотренных решений не внедрено.

## 2026-10-12 — Частичные связки оказались полезнее нового полного прогона

- Type: experiment
- Project area: самостоятельные навыки
- Status: confirmed — bounded developer evaluation; needs-check — перенос на обычные проекты.
- Evidence: [partial report](../experiments/workflow-tests/2026-10-12-partial-routes-results.md), [contract](../experiments/workflow-tests/2026-10-12-partial-routes-contract.md);9e4217e/23f0fa8.
- Summary: проверены мнение об идее, варианты, source audit, analysis→options, evidence→slice, отдельная функция и repair готовой карты.12turns включали первичные входы, dialogue/diagnostic и адресные correctives. Первичные FAIL сохранили: итог Product сводился к статусу файла, Wireframe удалил совместимый Undo из-за отсутствия имени кнопки в domain model. Beta.16/17 адресно исправили эти случаи; preview cleanup и readability остались отдельными проблемами.
- Article value: modular outcome подтверждается конкретным полезным выходом, не числом вызванных навыков; повтор полного маршрута скрывает локальную причину хуже, чем focused corrective.
- Follow-up: проверять новые рисковые seams по сигналу, не запускать успешные случаи ради статистики. Эти synthetic/developer проверки не являются внешним user acceptance.

## 2026-10-12 — Соавторство стало проверяемым поведением

- Type: decision
- Project area: ядро и коммуникация
- Status: confirmed — запросы creator, правки и selected correctives; needs-check — устойчивость в новых контекстах.
- Evidence: текущая переписка, [core](../plugins/fab/shared/core.md), [partial results](../experiments/workflow-tests/2026-10-12-partial-routes-results.md);ed7b64a/337b30c/683c747/bba356f.
- Summary: автоматическое согласие и сообщение «файл готов» не удовлетворяли роли Cowork. Договор уточнили: собственное суждение с причиной до edits, после — смысл результата для цели, последствия и полезный next. Core-инструкции сначала не решили artifact handoff полностью; понадобилась конкретизация Product exit и fresh corrective. Реальные creator предпочтения остаются отдельными от технического вердикта.
- Article value: хороший документ внутри папки не заменяет полезное завершение разговора; ценность соавтора проявляется в интерпретации и выборе следующего шага.
- Follow-up: сохранять это поведение без речевого шаблона, искусственной критики и лишних approval-пауз; не обобщать один corrective на все будущие ответы.

## 2026-10-12 — Мобильный маршрут дошёл до прототипа, но потерял смысл в проекции

- Type: experiment
- Project area: Product → Wireframe → Prototype
- Status: confirmed — выбранный browser behavior и semantic FAIL; needs-check — native/platform/usability.
- Evidence: [mobile results](../experiments/workflow-tests/2026-10-12-mobile-pipeline-results.md), [method audit](research-audits/mobile-structure-2026-10-12.md), [recovery asset](../experiments/workflow-tests/mobile-pipeline-20261012/ui/recovery-retained.jpg);1c11df4/cc98664.
- Summary: исследование мобильной структуры встроено как brief/full с conditional platform routes;7source binding unknowns сохранены. Один свежий iOS-first packing candidate прошёл model/blocks перед кодом. Root браузером подтвердил выбранные create/edit/cancel/Undo/retry/reload пути. Карта потеряла owner строки поездки и различие commit/cancel returns общей формы, хотя physical guard проходил.
- Article value: работающий код и правильная семантическая передача между артефактами независимы; app-focus не отменяет переносимую предметную модель и не доказывает native implementation.
- Follow-up: адресные semantic correctives позже дали scoped PASS; чистый общий full-route PASS и реальный native/device опыт не получены.

## 2026-10-12 — Исследование получило ревизию и список проектов-потребителей

- Type: decision
- Project area: Research provenance
- Status: confirmed — договор и один согласованный mobile ingestion; needs-check — refusal/additive multi-project/source-change behavior.
- Evidence: [решения](decisions.md), [ingestion](../plugins/fab/skills/research/references/ingestion.md), [source usage](../experiments/maintenance/mobile-ingestion-20261012/source-usage.json);8e1f4b5.
- Summary: после обработки исходника Fab предлагает добавить проект к имени и тег внутри, сохраняя прежние labels. Usage-блок хранит проекты, brief/full и обработанную ревизию. Mobile source помечен только после явного согласия, body SHA сохранён. Изменённый источник должен выявлять отстающих потребителей, но не автоматически переписывать другие проекты.
- Article value: research re-use требует provenance и понятного consent boundary, иначе название файла скрывает, где знание применено и устарело.
- Follow-up: наблюдать отказ, второе имя и обновление источника; один успешный ingestion не закрывает все случаи.

## 2026-10-11 — Исследовательские имена перенесены с Wireframer на Fab

- Type: milestone
- Project area: источник знания и identity
- Status: confirmed — конкретная миграция.
- Evidence: [technical journal](journal.md), [Research ingestion](../plugins/fab/skills/research/references/ingestion.md);fb5f5f0.
- Summary: для включённых maintainer-исследований ввели видимое `Fab:` и top marker/tag/pointers. Восемь notes перенесены с сохранением research bodies по SHA и исторических ссылок/контекста; пакет не зависит от внешней библиотеки.
- Article value: новая identity должна прослеживаться в знаниях, сохраняя происхождение и не выдавая чужой исследовательский текст за новую редакцию.
- Follow-up: последующий договор расширил этот конкретный prefix до добровольных additive project labels, а не переименования всех файлов подключённого проекта.

## 2026-10-11 — Сохранить полезное и убрать своё стало частью runtime

- Type: decision
- Project area: artifact lifecycle
- Status: confirmed — правило и verified retention; needs-check — устойчивое исполнение/наследование.
- Evidence: [lifecycle](../plugins/fab/shared/artifact-lifecycle.md), [technical journal](journal.md), [partial results](../experiments/workflow-tests/2026-10-12-partial-routes-results.md);31ef463.
- Summary: после обнаружения накопленных временных файлов введены task-owned scratch, durable retention, проверка копии и удаление только своего disposable. Тестовые63files/helpers сохранены и сверены. Создаваемые плагины должны наследовать самостоятельное правило, а не ссылку на Fab. Позже Wireframe снова оставил SVG: root сохранил SHA/убрал файл, beta.18 уточнила route, поведенческая проверка этой правки открыта.
- Article value: наличие инструкции не равно исполнению; housekeeping не должно стирать результат и evidence или затрагивать чужую временную работу.
- Follow-up: FAB-09 — observe fresh preview cleanup и отдельное generated-plugin inheritance, без общего tmp sweep.

## 2026-10-11 — Два отдельных входа проверили Plugin без выпуска тестовых продуктов

- Type: experiment
- Project area: Plugin engineering
- Status: confirmed — source-level outcomes; needs-check — installed discovery/real distribution.
- Evidence: [Plugin smoke report](../experiments/workflow-tests/2026-10-11-plugin-smokes-results.md);5005d97.
- Summary: свежие CLI-contexts проверили создание Note Compass и maintenance Local Index, включая контент страниц. Root подтвердил сохранность исходников и исправление overwrite/self-indexing. Пакеты честно оставлены с непроверенной установкой/discovery; тестовые продукты не стали целью Fab и не были опубликованы.
- Article value: отдельные create/repair входы лучше показывают границу навыка, чем один счастливый общий pipeline.
- Follow-up: следующий smoke выбирать по новому риску — установка, маршрутизация или сложный repair; source PASS не объявлять готовностью к распространению.

## 2026-10-11 — Основной чат переехал в проект Fab

- Type: milestone
- Project area: контекст и непрерывность
- Status: confirmed — первое восстановление; needs-check — устойчивая дальнейшая непрерывность.
- Evidence: текущий чат и последние turns [Plugin Wireframer](codex://threads/01a0aad1-0c37-7f03-a52f-e1b5f830dc8e), [handoff](handoff.md), [backlog FAB-02](backlog.md);8a19ba7.
- Summary: новый чат восстановил цель Fab, соавторство, installed beta.9 и различие проверенных/открытых результатов по durable документам. Создатель подтвердил первый перенос; старый чат сохранён как история. Критерием стало сохранение смысла и границ, а не наличие готового стартового запроса.
- Article value: handoff — самостоятельный пользовательский результат, который нужно наблюдать после передачи.
- Follow-up: FAB-02 не закрыт первым восстановлением; сохранять дальнейшие decisions/scope без повторного брифинга.

## 2026-10-10 — Реальный recovery отличался от управляющего test harness

- Type: experiment
- Project area: исполняемый прототип и доказательства
- Status: confirmed — конкретный corrective/root UI outcome; needs-check — обобщение на storage/production.
- Evidence: [autonomous results](../experiments/workflow-tests/2026-10-10-autonomous-beta-results.md), [recovery contract](../experiments/workflow-tests/2026-10-10-beta8-recovery-contract.md);ac0b6ef/a9b1048.
- Summary: проверка полного кандидата обнаружила недоступный за modal failure-control: retry требовал потери draft. Адресный corrective дал доступный one-shot failure/retry; root подтвердил сохранение данных и одну history entry. Browser продолжал старый JS до явной ревизии asset URL; это вмешательство среды сохранено отдельно от модельного результата.
- Article value: тестировать восстановление нужно в реальном failed state доступными человеку средствами; reload и правильный файл на сервере не доказывают исполнение новой ревизии.
- Follow-up: выбранный recovery исправлен, универсальная целостность storage/client/production не доказана. Ограничение запуска и вмешательство root не скрыты из evidence.

## 2026-10-10 — Fab выделен как самостоятельный модульный продукт

- Type: decision
- Project area: архитектура и границы продукта
- Status: confirmed — repo/bundle/contracts и selected transfer; needs-check — полная ранняя история обсуждения объединения.
- Evidence: [architecture](architecture/design.md), [source provenance](architecture/source-provenance.json), [beacon](beacon.md), [initial beta results](../experiments/workflow-tests/2026-10-10-autonomous-beta-results.md);c8471f1/4e0d7d5.
- Summary: выбран самостоятельный Fab repo/package с shared core и независимыми outcomes. От первых пяти beta-навыков дошли до десяти; общий процесс остаётся optional, имеющиеся входы не требуют новой полной discovery. Выбранные методы перенесены с происхождением, внешний Brain не обязателен для runtime, прежние плагины сохранены. Synthetic products проверяют процесс, но не подменяют его цель.
- Article value: модульность определяется способностью закончить полезную частичную задачу и сохранить смысл при совместном маршруте; установленный набор навыков ещё не доказывает зрелость.
- Follow-up: для точного рассказа о первоначальном объединении плагинов нужен адресный разбор ранней переписки; нельзя утверждать механическое слияние всех старых codebases.

## Пакет истории и текущие ограничения

[Evidence map и story packet](story-packets/fab-development-2026-10-12.md) содержат
проверяемые claims, недопустимые обобщения, варианты и открытые вопросы.
На последнем сохранённом checkpoint: installed beta.20,65files/597115ccbb4b0a59,
46локальных регрессий/parity PASS; Canvas и chat recovery не получили общий PASS.
Git migration к main только предложена. Реальные external-project value/usability,
native/device, generated cleanup inheritance и универсальная устойчивость методов
не установлены. Актуальные статусы смотреть в backlog/handoff, не переносить этот
датированный срез на следующую версию автоматически.
