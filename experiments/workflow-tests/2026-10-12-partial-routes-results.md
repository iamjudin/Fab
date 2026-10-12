# Fab: короткие задачи и частичные связки · 2026-10-12

## Вывод для продукта
**Fab полезен для ограниченных консультаций и коротких смысловых связок.** В этих
входах он высказывает мнение, различает варианты, объясняет причины проблем и
рекомендует следующую проверку; не тащит человека в обязательный полный процесс.
Сложнее оказалась работа с артефактами: недостаточное завершение ответа и потеря
совместимого взаимодействия при сверке карты. Два адресных corrective подтвердили
исправление этих случаев. Общего PASS качества всех выходов нет: уборка preview
повторно нарушена, а карта с формальным no-warning результатом всё ещё имеет
перекрывающиеся подписи стрелок в fallback.

Моё мнение: продолжать развивать Fab через реальные ограниченные задачи полезнее,
чем повторять весь pipeline. Содержательные навыки уже дают пользу; следующая
техническая инвестиция — читаемость Canvas и достоверность диагностики renderer.
Следующий preview одновременно позволит наблюдать уборку beta.18. Не требуются
новый full run или creator evaluation для вынесения этого технического вывода.
Оценка личной полезности, вкуса и принятие новых правил остаются за человеком.

## Контракт, среда и независимость
[Контракт](2026-10-12-partial-routes-contract.md) зафиксирован до pilot на ветке
`codex/partial-workflow-tests` от167c6be, checkpoint e33aeb8. Baseline ответы и
findings сохранены9e4217e до edits. Исходный установленный Fab beta.15:
60files/cf1d23be54742d51, parity PASS. Для каждого primary — отдельный workspace
вне Fab repo и fresh CLI, без основной переписки, Brain/maintainer docs/golden
ответов. Общая конфигурация хоста/доступные skills остаются; entry явно указан.
Это не чистая установка, не автоматическое discovery и не blind human trial.

Фактически все12turns — GPT-6.1 Sol/Low, без override. Root оценивал исходники,
ответы, команды, SHA и изображения; это developer assessment, не независимый
рецензент. Synthetic operator correction — одна настоящая resume-сессия, но не
реальное одобрение creator. Source-only audit честно назван source-only; root
fixture oracle использует Node VM/минимальный DOM, не доказательство browser UI.

## Полезные результаты по задачам

| Задача | Оценка и смысл результата | Ответ для чтения |
| --- | --- | --- |
| Мнение о широкой app-идее | PASS с оговоркой: обоснованно возражает «больше функций — больше пользы», разбирает срок/интеграцию/offline; новое направление всё ещё широкое, его срок не доказан | [Мнение](partial-routes-20261012/opinion/readable.md) |
| Пять подходов к возвращению в прозу | PASS: разные механизмы, затраты и первая ручная проверка; сохраняет no-AI/push/streak/social | [Идеи](partial-routes-20261012/ideas/readable.md) |
| Read-only аудит HTML | PASS: находит потерю draft, отмену с мутацией, retry duplicate, глобальный счётчик; дополнительно замечает UI/state mismatch и скрытую ошибку. Объясняет общую причину и приоритет | [Аудит](partial-routes-20261012/audit/readable.md) |
| Анализ → варианты улучшения | PASS: различает whole-list replacement, per-item manual choice и recovery; не придумывает точную причину потери количества и не обобщает четыре попытки | [Разбор и варианты](partial-routes-20261012/audit-options/readable.md) |
| Одна функция Undo → Product | Артефакт PASS, исходный final FAIL. Beta.16 улучшил summary, но reason/next неполны. Beta.17 fresh corrective PASS: рекомендация, польза скрытой вещи, реальный trip/reload компромисс и статус предложения | [Исходный итог](partial-routes-20261012/feature/readable.md), [последний corrective](partial-routes-20261012/feature-final/readable.md), [правила](partial-routes-20261012/feature-final/result/undo.md) |
| Согласование готовой модели/карты | Ownership/egress PASS, initial preservation FAIL: удалил feedback/Undo, потому что имя не в domain model. Beta.16 corrective сохраняет механизм и открытые детали, IDs/model; семантика PASS, housekeeping FAIL и readability caveat | [Исходный итог](partial-routes-20261012/wireframe/readable.md), [corrective](partial-routes-20261012/wireframe-corrective/readable.md), [интерфейс](partial-routes-20261012/wireframe-corrective/result/product/reviews/interface.md) |
| Малые наблюдения → небольшой срез | PASS: контрпример и confounds сохранены, «всем нужен автоматический план» не подтверждает. Предлагает добровольную локальную записку и проверку cost/value без расширения редактора | [Вывод](partial-routes-20261012/evidence-slice/readable.md), [срез](partial-routes-20261012/evidence-slice/result/slice.md) |
| Уточнение в прежнем диалоге | PASS: два low-burden ручных подхода, голос/уведомления исключены, вариант не объявлен принятым | [Follow-up](partial-routes-20261012/ideas-followup/readable.md) |
| Короткий естественный вопрос без stop | PASS: мнение и альтернативы без code/docs/forced pipeline; гипотеза завершения историй не выдана за спрос | [Ответ](partial-routes-20261012/natural-advice/readable.md) |

Число прочитанных skills не критерий успеха: Cowork может дать достаточную
консультацию сам. В analysis-options/evidence-slice он прочитал нужные contracts;
Research ingestion/full packet не создавался для небольшой интерпретации supplied
notes. Неоднозначный самостоятельный спор не превращён в реальный creator approval.

## Изменения Fab и оставшиеся границы
- Beta.16 (683c747): synthesis в ответе на artifact delivery; различение UI
  механизма и доменного goal. Первоначальные FAIL не заменены исправленными файлами.
- Beta.17 (bba356f): конкретный Product exit — рекомендация/причина/компромисс/next.
  Fresh same-input corrective без findings в prompt дал bounded PASS.
- Beta.18: Wireframe явно маршрутизирует transient renders в artifact lifecycle.
  Повод — оставленный `/private/tmp/wireframe-corrective-preview.svg`; root сохранил
  SVG, проверил SHA и убрал точный файл. Model cleanup этой правки ещё не наблюдался.
- WF-01/FAB-03: owners и branch-specific returns проверены адресно, full-route
  устойчивость не обобщена. WF-20: root увидел наложение return labels в SVG,
  несмотря на автоматический no-warning. Native Obsidian отдельно не проверен.

Обновлятор после завершения beta.16 Wireframe retired старый cache при установке
beta.17. Post-update compare отсутствующего16path FAIL; metadata подтверждает,
что run закончился22:38:12UTC, новый cache создан22:38:15UTC. Все команды run
завершились0; изменений runtime во время run нет. Frozen16archive сохранён,
[хронология](partial-routes-20261012/wireframe-corrective/runtime-retirement.json).
Устанавливать следующий пакет следует после завершения всех активных runs.

## Расход и сохранность
7primary+1synthetic follow-up+1diagnostic+3corrective =12model turns.
Сумма run time **835.4s (13.9min)**, не elapsed wall при параллельных запусках.
Input2073222, cached1817472, output30703; неизвестной usage нет. Прогноз5M/150k/
75min не превышен. Account limit percentages не выводятся из token counts;
credit reset/покупки/дожигание окон ради статистики не выполнялись.
[Actual usage](partial-routes-20261012/usage.json).

Текущая beta.18:60files/c463bb6928771c74, source/cache PASS,36regressions PASS.
Реальные поведенческие correctives относятся к16/17;18 имеет только scoped
package/regression evidence для последней lifecycle route правки.
Оригинальные ответы/requests/fixtures/observer/selected outputs доступны рядом;
readable copies меняют только пути ссылок. Полные logs/runtime/workspaces/helpers
в ignored raw archive.11workspaces+5helpers сверены и owned scratch удалён;
[receipt](partial-routes-20261012/cleanup.json),
[preview receipt](partial-routes-20261012/external-preview-cleanup.json).
Старые previews/серверы/чужие tmp не тронуты. Коммиты локальные на экспериментальной
ветке, merge/public release нет; тестовые продукты не runtime зависимости Fab.
