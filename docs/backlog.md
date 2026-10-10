# Бэклог Fab
## Сейчас
Минимальная beta проверена и handoff подготовлен. Следующий пакет — bounded
Product/Wireframe migration; фиксируем незакрытые WF findings при переносе. Автономная
реализация/локальная установка/ограниченные тесты разрешены 2026-10-10;
один reset при необходимости разрешён, пока не использован. Без public release.

| ID | Статус | Работа | Следующая проверяемая граница |
| --- | --- | --- | --- |
| FAB-01 | Закрыто | Упаковка/пять skills/общий core/методы | Source/install parity + five natural Fab requests PASS; see beta1-results |
| FAB-02 | Исправлено, ждёт проверки | Continuity/соавторство | Fixture PASS; фактический переход основного чата ещё не проверен |
| FAB-03 | Отложено | Product/wireframe перенос | После beta; preserve graph semantics, address relevant WF findings |
| FAB-04 | Отложено | Prototype/plugin/delivery | После bounded domain transfer; no maturity from copied text |
| FAB-05 | Отложено | Mobile HIG/Material expertise | Глобальные исследования и conditional platform criteria |

## Наследованные findings: пока у исходного владельца
WF-17/20/26/27/28 остаются в Wireframer docs/backlog.md. Здесь pointers, не
новые дубли task records. Переход статуса/owner отдельно при реальном domain
переносе; не объявлять закрытыми от переупаковки. WF-26 частично касается FAB-02,
но один handoff smoke не закрывает всю устойчивость общения.

## Правила
Задача: stable ID, тип, expected→observed, evidence/version, owner/status,
next/closure. Unknown продукта в product workspace, общий дефект в Fab.
Статусы: Проверить; В следующее обновление; Отложено с trigger;
Исправлено, ждёт проверки; Закрыто с границей evidence.
Сверять duplicate перед добавлением; сверху текущий пакет, история в journal.
