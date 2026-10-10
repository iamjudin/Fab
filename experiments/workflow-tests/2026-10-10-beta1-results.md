# Fab beta.1 — результаты пяти ограниченных запросов

**Вывод: beta пригодна для следующего ограниченного этапа реализации.** Пять
естественных запросов «Используй Fab» выбрали соответствующий installed skill,
без mandatory Jobs/IA/product framing. Это по одному синтетическому кейсу на
outcome, не общая устойчивость, не независимый audit и не весь продуктовый путь.

Runtime: Fab0.1.0-beta.1, fab-local,31files/a15d99d2c6ea21a1;
source checkpoint c8471f1; installed /Users/iamjudin/.codex/plugins/cache/fab-local/fab/0.1.0-beta.1.
Portable root plugin.json установлен без compatibility fallback.
Source/cache parity PASS; четыре local guard tests PASS (package refs containment,
research content tampering, shared-file parity drift, valid bundle).

| Запрос | Наблюдение | Граница |
| --- | --- | --- |
| Research | Compatible brief/full, все6разделов/исходный SHA сохранены; конфликт/гипотеза/синтетический контекст различимы | Не проверял реальную достоверность рынка; conditional global full-read не вызван |
| Analysis | Три прямых противоречия найдены; неизвестные отделены; target не изменён | Текстовый макет, не Figma/UI |
| Brainstorm | Варианты/компромиссы/рекомендация, нет forced choice/реализации | Один после-analysis handoff, не доказательство универсального brainstorming |
| Cowork | В новом контексте восстановлены цель, finding vs decision, договор соавторства и next; без rebrief | Fixture continuity, не фактический переезд основного чата |
| Testing | Один Python experiment дал отрицательный результат; кодsubject не изменён; report различает exit0 и requirementFAIL | Исходный saved не изменён, returned result = draft; не UI и не integration test |

**Находки:** подтверждённых дефектов Fab на этих пяти путях не получено.
Отрицательный cancellation result — намеренно несовместимый тестовый subject,
не провал Fab; он честно описан и не исправлен. Для mobile/product маршрутов,
Figma, native UI, global full-packet conditional read, release и сложной
continuity evidence нет. WF-17/20/26/27/28 не закрываются этим результатом.

Testing получил один transport timeout/reconnect, затем завершился. Отдельный
новый модельный запуск не потребовался; не скрывать environmental event.
Ни одного корректирующего prompt, дополнительных agents или reset.

## Расход

5 fresh CLI turns, 470,621 input, 410,624 cached input,
5,886 output; 305.9 s CLI wall суммарно.
Это actual CLI events, без overhead работы основного чата/аккаунта; cached
входит в контекст и не переводится напрямую в процент лимита. Начальный budget
1.5млн input/60тыс output не достигнут; within-turn forecast не hard cap.

[Подробные счётчики/прочитанные skills](beta1/usage.json),
[исходный контракт](2026-10-10-beta1-contract.md).
В beta1/outputs сохранены prompts/final; beta1/workspaces — фактические малые
artifacts; full JSONL в beta1/raw остаётся локально вне Git. Original refs в
неизменённых ответах могут указывать на исходный private tmp.

## Дальше

Закрепить beta checkpoint/handoff. Следующий пакет — Product + Wireframe с
сохранением сигналов/graph semantics и отдельной коррекцией known WF-17/20,
а не новый full greenfield smoke. До него actual основной чат не перенесён;
один дальнейший bounded case на реальном запросе лучше повторения этих fixtures.
Public release/remote не создавались. Старые Wireframer/Fabricator сохранены.
