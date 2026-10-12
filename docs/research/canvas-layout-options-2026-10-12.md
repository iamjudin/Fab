# Fab: карта с карточками и структурой — варианты

## Рекомендация
Я рекомендую проверить небольшой общий механизм раскладки внутри Fab на ELK,
с сохранением `.canvas` и существующих IDs. Он должен знать роли карточек,
владельцев и типы связей, а не только распределять прямоугольники. Отдельный
Obsidian-плагин имеет смысл как адаптер этого механизма, если нужен управляемый
интерактивный показ именно в Obsidian. Большой новый редактор сейчас не выбираю:
это отдельная поверхность продукта и существенная стоимость сопровождения.

Это предложение после исследования, не принятое архитектурное решение.
Implementation/spike/установка community plugins не выполнялись. Fab beta.18
не изменена: checkpoint `10e44cf`, tag `checkpoint-beta18-2026-10-12`,
60files/c463bb6928771c74. [Checkpoint](../checkpoints/fab-beta.18.md).

## Что установлено о проблеме
Read-only воспроизведение на текущей карте даёт пустой список предупреждений,
но label rectangles `save-return` и `cancel-item-return` пересекаются. Их y=908,
height=30; второй прямоугольник целиком попадает в первый по x.
`canvas_preview.py::layout_warnings` сравнивает edge labels с non-group nodes,
но не друг с другом. Маршруты рассчитываются для каждой стрелки отдельно;
взаимное размещение подписей не решается глобально.
[Данные воспроизведения](../../experiments/analysis/canvas-layout-20261012/reproduction.json).
Дефект диагностики необходимо устранить при любом выбранном варианте.

У JSON Canvas есть карточки/группы с координатами и связи с концами/сторонами/
подписью. В спецификации нет координат подписи, waypoint-ов маршрута или явного
`parentId`. Поэтому результат собственной геометрии SVG нельзя объявлять
тождественным native Obsidian. Иерархию layout нужно сохранять явно внутри
адаптера и проецировать на визуальные контейнеры; формат стандартного `.canvas`
остаётся совместимым. [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/).

## Готовые решения

### Canvas Mindmap и Mindvas — структура как дерево
Canvas Mindmap предлагает создание детей/соседей, выбор дерева и раскладку по
направлению. Он уже установлен и включён у creator:1.0.2, Obsidian1.12.7.
[README](https://github.com/Quorafind/Obsidian-Canvas-MindMap),
[локальная проверка](../../experiments/analysis/canvas-layout-20261012/environment.json).

Mindvas добавляет tree layout, outline panel, forest внутри группы, auto-resize
и работу с обычными `.canvas`. Manifest0.3.0 объявляет desktop-only и minimum1.5.0.
Автоматические цвета ветвей по умолчанию включены. Для Fab их пришлось бы
отключить, чтобы сохранить цвета информации, навигации и изменения данных.
[README](https://github.com/mobench/mindvas),
[manifest](https://raw.githubusercontent.com/mobench/mindvas/main/manifest.json).

Мой вывод: это хорошие кандидаты для ручного дерева карточек. Документация не
подтверждает сохранение нашей смешанной карты с nested owners и return/cross-level
navigation. Нельзя превращать все стрелки в отношения parent/child. На pilot
нужно отдельно проверить cycles, общую форму и несколько входов, не отключая
нужные связи ради красивого дерева. Реальная проверка plugins ещё не проводилась.

### Advanced Canvas — улучшение native просмотра
Есть collapsing groups, auto node resize, floating edges, highlight/focus и
несколько pathfinding modes, а также экспорт SVG/PNG. Это полезные функции
просмотра/редактирования. Я не нашёл в прочитанной документации подтверждения
автоматической compound-раскладки всего графа и устранения всех label collisions.
[README](https://github.com/Developer-Mike/obsidian-advanced-canvas).

Latest release7.1.0 и проверенный6.5.4 требуют minimum Obsidian1.13.0. Локально
стоит1.12.7; эти версии нельзя считать совместимыми по manifest. Более старый
совместимый release здесь не выбран и не проверен. Obsidian не обновлялся.
[Releases](https://github.com/Developer-Mike/obsidian-advanced-canvas/releases),
[7.1.0 manifest](https://raw.githubusercontent.com/Developer-Mike/obsidian-advanced-canvas/7.1.0/manifest.json),
[6.5.4 manifest](https://raw.githubusercontent.com/Developer-Mike/obsidian-advanced-canvas/6.5.4/manifest.json).

Мой вывод: optional viewer enhancement, не основной обещанный layout engine.
Его расширенный формат потребует отдельной проверки при отключённом плагине.

### Другие найденные направления
Kanvas раскладывает карточки по dependency depth, вертикально/горизонтально, но
также несёт собственный протокол управления проектными состояниями. Для Fab
я не выбираю подмену UC/owners этим workflow; сохранение наших групп/подписей не
доказано. [Kanvas](https://github.com/XMihura/Kanvas).

Excalidraw Auto Layout уже использует ELK для выбранных элементов/групп. Это
полезный пример интеграции готового движка, но переход к Excalidraw меняет
проекцию/формат; round-trip Fab graph/IDs/Canvas не проверен. Скрипт не доказывает
нужную нам вложенную раскладку сам по себе.
[Auto Layout source](https://raw.githubusercontent.com/zsviczian/obsidian-excalidraw-plugin/master/ea-scripts/Auto%20Layout.md).

Каталог Codex показал MindMap, Whimsical, Miro, tldraw и установленный Figma.
Новые подключения не предлагаются: это альтернативные whiteboards/viewers,
а не проверенный способ сохранить существующую `.canvas` проекцию Fab. Каталог
не является каталогом community plugins Obsidian и не исчерпывает их варианты.

## На чём строить свой механизм
ELK Layered поддерживает compound graphs, ports, несколько связей между узлами,
edge labels и маршрутизацию. Cross-hierarchy layout требует соответствующей
настройки hierarchy handling. elkjs вычисляет координаты, не предоставляет
готовый UI. Это подходящая база для spike, не доказанная гарантия нашей карты.
[ELK Layered](https://eclipse.dev/elk/reference/algorithms/org-eclipse-elk-layered.html),
[hierarchy handling](https://eclipse.dev/elk/reference/options/org-eclipse-elk-hierarchyHandling.html),
[elkjs](https://github.com/kieler/elkjs).

Для возможного web viewer React Flow отделяет rendering от layout. В его
документации ELK поддерживает sub-flows и routing, а для Dagre указан известный
случай некорректной раскладки sub-flow со связью наружу. Поэтому простой Dagre
не мой первый выбор для nested owners. Это evidence о выборе кандидата, не
проверка совместимости Fab. [React Flow layout guide](https://reactflow.dev/learn/layouting/layouting).

## Варианты решения

| Вариант | Результат | Польза | Основной компромисс |
| --- | --- | --- | --- |
| A. Починить текущий renderer | Label-label checks, честные warnings и placement подписей | Малый scope, сразу убирает false no-warning | Не решает общий auto-layout и не гарантирует native Canvas |
| B. Community plugin | Mindmap-редактирование/outline или Advanced Canvas viewer | Быстрый interactive pilot, можно начать с уже установленного Mindmap | Tree assumptions/версии/цвета; наш полный graph не проверен |
| C. ELK-механизм в Fab + адаптеры | Общая layout-модель → `.canvas` и проверяемый preview | Контроль semantics/IDs, compound routing, возможность разных viewers | Нужно измерять карточки и делать адаптер; native геометрия отдельно |
| D. Свой Obsidian plugin или local web viewer | Управляемые карточки, folding, слои связей и layout | Полный контроль вида и взаимодействия | Существенно больший scope; Obsidian интеграция и web UI — разные поверхности |

Предлагаю A как обязательную часть корректности, затем небольшой C-spike.
B может быть быстрым эталоном ручного просмотра, а D — только после выявления
реального ограничения native viewer. Так мы улучшаем Fab и не начинаем новый
редактор до доказанной необходимости.

## Предлагаемый вид карты
Структура выглядит как дерево карточек: приложение → поверхность → коллекция →
повторяемый объект → его информация/действия. Карточка содержит роль, короткое
описание, критичные состояния и источники; стрелка начинается у нужного действия.
Переходы, Cancel/Back/Undo — другой тип отношения. Они должны оставаться в данных
и быть доступны в отдельном scenario view или слое, а не превращаться в дерево
и не исчезать при «упрощении». Это мой design proposal, не новый принятый контракт.

Одно semantic основание, разные виды. StableIDs/владельцы и принятые правила не
изменяются раскладчиком. Adapter не создаёт конкурирующую новую product model и
не переименовывает `.wireframer`. Folding/выбор слоёв не должен уничтожать связи.
Экспорт `.canvas` не обещает сохранение всех ELK bend/label coordinates: для
точного интерактивного вида потребуется renderer/плагин, который их использует.

## Маленький следующий проверочный шаг
После выбора основного места просмотра взять копии трёх fixtures: текущая
трёхповерхностная карта, nested groups с cross-level return и длинные русские
подписи/несколько входов. Сравнить текущий renderer, выбранный plugin или ELK
adapter на одинаковом semantic input. Это proposal, запуск не выполнен.

Критерии: не потеряны IDs/содержание/цветовые роли/файловые ссылки; owners и
commit/cancel/feedback сохраняют контекст; нет скрытых label/content collisions
или честно показана неразрешённая геометрия; одинаковый input даёт устойчивую
раскладку; overview читается без расшифровки кода. Native Obsidian и preview
оцениваются отдельно. Исключены установка в основной vault, автоматическое
изменение исходной карты, редактирование beta.18 и публичный release.

Необходимая развилка перед реализацией: основной interactive view должен
оставаться в Obsidian или допустим local web viewer с экспортом `.canvas`?
По существующему workflow я предполагаю Obsidian основным; это предположение,
не ответ creator. Второй случай позволяет хранить и использовать точную геометрию
и переключаемые слои в нашем viewer; первый требует проверить native adapter.

## Границы исследования
Проверены первичные README/manifest/spec/исходный script, местные app/plugin
metadata и детерминированный дефект текущего renderer. Community UI не запускался,
ELK package не устанавливался/не исполнялся, native layout/round-trip не доказаны.
Копирования внешних ресурсов в runtime или Brain не было. Для readable source
tim-smart Canvas Mindmap Helper README оказался пустым, поэтому он не shortlisted.
