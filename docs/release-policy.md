# Политика выпуска и изоляции Fab

## Решение
Релиз фиксирует точный пакет и обещанный набор результатов, а не универсальную
готовность всех навыков. Каноническое runtime-правило —
[release-policy](../plugins/fab/shared/release-policy.md), gate —
[check_release.py](../plugins/fab/skills/delivery/scripts/check_release.py).
Проверка пакета, наблюдаемое поведение и пользовательская оценка независимы.

Три слоя: смысл Product/Wireframe → представление (таблица, Canvas, экран) →
исполнение Prototype. Формат представления не владеет смыслом. Его замена сохраняет
ID, владельцев, UC, ветки результата/ошибки/возврата. Новый viewer может читать тот
же смысловой договор; layout engine пока не выбран. Нативный адаптер отдельно.

## Текущий scope
- Структура/сценарии: Markdown-таблицы по умолчанию. Конвертер старой Canvas
  проверен на сохранность; это не доказательство качества всех будущих новых таблиц.
- Canvas/preview: выключен из default-маршрута; явный experimental opt-in,
  известный FAIL наложения подписей. WF-20 остаётся открытым.
- Native Obsidian Canvas: не проверен, не обещается как готовая поверхность.
- Видимые блоковые экраны и исполняемые прототипы: самостоятельные результаты.
  Выбранные browser paths проверены; native/device/production не подтверждены.
  Canvas не является обязательным условием продолжения к прототипу.
- Остальные самостоятельные навыки: сохраняется прежняя bounded beta-граница;
  новой общей поведенческой проверки этим изменением не заявляем.

## Выпуск
1. Зафиксировать version, fingerprint, все обещанные поверхности и ограничения.
2. Для каждой default-поверхности определить существенные проверки и реальные
   evidence. FAIL/unknown блокирует эту поверхность; общий green не перекрывает FAIL.
3. Исправить дефект, ограничить обещание проверенным исходом или исключить
   поверхность из default. Замена имеет собственные проверки и ограничения.
4. Run package/regression + executable scope gate. В Fab `scripts/check_fab_release.py`
   также требует записей всех десяти навыков и трёх Wireframe-представлений;
   plan хранится в docs/release-plan.json. CI workflow повторяет эти проверки
   на push/PR после загрузки в GitHub; remote run PASS для beta.22 release preparation; см. distribution report. Это не
   branch protection: без настройки required checks прямые действия не запрещены.
   Никогда не объявлять limited исторические проверки свежим PASS новой beta.
    Beta допускает limited с
   явными границами; stable требует verified в обещанном scope. Experimental
   отключён по умолчанию. Gate проверяет заявления/identity, не истинность evidence.
5. Commit проверенный checkpoint; install/tag/push/merge/publication — разные
   действия. Предыдущий tag не сдвигается. Интеграция feature-ветки только после
   согласованного возвращения результата и явного разрешения merge.

Beta.18 сохранена как исторический checkpoint с известным Canvas FAIL. Её tag
checkpoint-beta18-2026-10-12 на10e44cf неизменен. Beta.19 сохранена checkpoint3e53097.
Пакет установлен локально как beta.22 (67files/71349e50dbffe9c0);
переименование версии не превращает эксперимент в зрелую функциональность.

## Git и владение
Основной чат «Восстановить контекст Fab» / Lab/Fab / codex/fab-maintenance:
core, независимые навыки, таблицы, общая отладка, release policy и канонический backlog.
Отдельный codex/fab-map-view стартует с14f4dbf, исследовательская beta.18 база;
scope guard75540f1 и handoff packet c1681d5. При создании отдельного чата host
подготовил checkout /Users/iamjudin/.codex/worktrees/60c9/Fab; прежняя ручная
рабочая копия архивирована после сохранения packet, чтобы не было двух active copies.
Это физическая изоляция; два чата не должны переключать branch одной папки.
Старые codex/canvas-layout-research и codex/partial-workflow-tests сохранены.

Map-workstream сейчас parked: сначала creator приносит свой прототип, затем
предлагаем способы реализации. Не запускать ELK spike или выбирать engine заранее.
Scope: карточки, соединения, неналожение, сворачивание/слои по прототипу, viewer
и его собственные проверки. Не менять общий core/version/release/backlog,
не устанавливать feature-source в общий default runtime. Находки — scoped report
с proposal для основной ветки; main owner принимает решения о переносе.
Creator запросил отдельный Canvas-чат с автоматическим переносом контекста.
Packet: [Canvas handoff](handoffs/canvas-workstream-2026-10-12.md). При разрешённом
отделении Fab выполняет создание чата/изоляцию/context transfer и проверяет реальное
восстановление. Новый чат ждёт прототипа; разрешение на чат не запускает layout spike.

Для возвращения нужны: согласованный контракт данных, сохранность IDs/связей,
читаемость representative и сложных случаев, отрицательные/return branches,
проверки реального выбранного viewer и явный scope/лимиты. Native Obsidian —
отдельная проверка, SVG/JSON её не заменяет. Только затем обсуждается promotion.

Fab сам предлагает изоляцию для самостоятельной существенной переработки после
checkpoint/release: причина, scope, baseline, branch и критерий возврата. Рутинная
маленькая правка не требует нового чата или обязательного отдельного процесса.

Передача контекста — [runtime handoff](../plugins/fab/shared/workstream-handoff.md):
цель/решения/revisions/evidence/scope/owner/next; actual thread ID и checkout,
содержательный ответ нового чата. Без инструмента не утверждать создание.
Сейчас `cowork.chat-handoff` — opt-in experimental: packet/Git проверены, создание
чата queued с client ID, actual recovery не наблюдалось. Это отдельная строка
release plan; остальные самостоятельные Cowork-исходы не объявлены заблокированными.

Workflow использует официальный [actions/checkout](https://github.com/actions/checkout) v7;
первый remote CI PASS: [run38269178037](https://github.com/iamjudin/Fab/actions/runs/38269178037).
Публичный distribution route описан в [отчёте](../experiments/releases/public-beta22-20261012/report.md).
