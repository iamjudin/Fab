# В дорогу: результат мобильного прогона Fab

Рабочий browser prototype — [открыть](http://127.0.0.1:8842/prototype/).
Root server session3372 обслуживает неизменённый candidate; он может завершиться
позже, поэтому live lifetime отдельно от данных browser origin.

Воспроизводимый запуск:
```sh
python3 -m http.server 8842 --bind 127.0.0.1 --directory /Users/iamjudin/Desktop/Lab/Fab/experiments/workflow-tests/mobile-pipeline-20261012/candidate
```
Демонстрационные поездки/вещи созданы root для UI-проверки, не импортированы
из реальных пользовательских списков. LocalStorage привязан к origin;
native storage, backup/sync и lifecycle не доказаны.

[Модель](candidate/product/reviews/model.md),
[интерфейс](candidate/product/reviews/interface.md),
[Canvas](candidate/product/reviews/structure.canvas),
[блоковые экраны](http://127.0.0.1:8842/product/reviews/blocks.html),
[полный отчёт](../2026-10-12-mobile-pipeline-results.md).

Кандидат работает в проверенных сценариях; карта имеет две сохранённые находки
ownership/return projection. Полного clean pipeline/native/usability PASS нет.
Candidate и initial snapshot — local ignored artifacts, не часть runtime Fab.
