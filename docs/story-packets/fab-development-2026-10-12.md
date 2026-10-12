# Fab — пакет истории разработки

Срез:2026-10-12, до journal backfill. Назначение — проверяемый контекст для
продолжения проекта и возможного Publicator Writer, не готовая статья.
Канонические задачи — [backlog](../backlog.md); история значимых этапов —
[project journal](../project-journal.md). Приватные детали переписки и полные логи
не копировались. Публикация не запрошена.

## Источники, реально просмотренные
- Текущая переписка Fab: цель, предложения, корректировки создателя и результаты.
- Последние пять turn старого чата [Plugin Wireframer](codex://threads/01a0aad1-0c37-7f03-a52f-e1b5f830dc8e): подготовка и подтверждение переезда. Более ранняя история этого чата целиком не восстановлена.
- [Технический журнал](../journal.md), [решения](../decisions.md), [handoff](../handoff.md), [маяк](../beacon.md), [архитектура](../architecture/design.md), [provenance](../architecture/source-provenance.json), Git history.
- Отчёты [начальной beta](../../experiments/workflow-tests/2026-10-10-autonomous-beta-results.md), [Plugin smokes](../../experiments/workflow-tests/2026-10-11-plugin-smokes-results.md), [mobile pipeline](../../experiments/workflow-tests/2026-10-12-mobile-pipeline-results.md), [partial routes](../../experiments/workflow-tests/2026-10-12-partial-routes-results.md).
- [Canvas research](../research/canvas-layout-options-2026-10-12.md), [Git research](../research/git-workflow-options-2026-10-12.md), [release policy](../release-policy.md), receipts [table/release](../../experiments/maintenance/release-policy-20261012/verification.json) и [chat handoff](../../experiments/maintenance/chat-handoff-20261012/receipt.json).

## Карта evidence

| Claim | Evidence | Status | Narrative role |
| --- | --- | --- | --- |
| Fab выделен в самостоятельный модульный bundle с десятью независимыми навыками; выбранные методы перенесены с provenance | architecture/design, source-provenance; c8471f1/4e0d7d5 | confirmed | desired state / decision |
| Весь код нескольких старых плагинов механически слит в Fab | Source-provenance доказывает selected transfer, не это обобщение | do-not-use | ограничение рассказа о происхождении |
| Первый перенос основного контекста в Fab прошёл успешно | Текущий чат, старый chat final, handoff;8a19ba7 | confirmed | milestone |
| Устойчивая непрерывность любых новых чатов доказана | FAB-02 остаётся открытым | do-not-use | limit |
| Два Plugin smoke дали локальные создание/repair и контент страниц | Plugin-smokes-results;5005d97 | confirmed | early result |
| Созданные тестовые плагины готовы к реальной установке и распространению | Установку/discovery/production эти smoke не доказали | do-not-use | limit |
| Нужны собственная оценка до работы и техническая интерпретация результата после | Прямые запросы creator; ed7b64a/337b30c/683c747/bba356f, partial correctives | confirmed | pain / decision / turn |
| Mobile full route дошёл до исполняемого кандидата, выбранные browser пути проверены | Mobile-pipeline-results;cc98664 | confirmed | result |
| Полный маршрут, native mobile и все проекции получили чистый PASS | Mobile report содержит два semantic FAIL и native unknown | do-not-use | limit |
| Partial skills полезны в проверенных входах; два исходных дефекта исправлены адресно | Partial-routes-results;9e4217e/23f0fa8 | confirmed | experiment / lesson |
| Preview оставался в tmp после правила уборки; root сохранил/убрал точный файл | Partial report/external-preview-cleanup receipt | confirmed | failure / lesson |
| Beta.18 lifecycle и наследование уборки свежим generated plugin устойчиво работают | FAB-09 после исправления ждёт наблюдения | needs-check | open question |
| Две подписи перекрывались при warnings=[] | Canvas reproduction и сохранённый PNG | confirmed | turning point |
| Табличный fallback сохраняет25nodes/8edges/full snapshot старой карты | Release-policy verification.json;3e53097 | confirmed | bounded result |
| Будущие таблицы модели и native Obsidian отображение всегда корректны | В receipt это unobserved | needs-check | limit |
| Создание ветки/контрольного коммита не поменяло main checkout и installed runtime | Canvas-branch-smoke report;25eaa72/860da1b | confirmed | mechanism |
| Canvas context packet перенесён; отдельный checkout подготовлен | Chat receipt; c1681d5/83ab56e/983fbf6 | confirmed | bounded result |
| Новый Canvas-чат восстановил контекст | На последней проверке real thread ID/ответ отсутствовали | needs-check | open question |
| Main/лёгкий Git workflow уже введены | Git research имеет статус proposal; main отсутствовала при проверке | do-not-use | limit |
| Beta.20 установлена локально,65files/fingerprint597115ccbb4b0a59,46regressions/parity PASS | Chat receipt, source/checkpoint20 | confirmed | current checkpoint |

Коммиты идентифицируются локальными SHA. Современные checkpoints и эти материалы
не считать автоматически размещёнными на GitHub или публично опубликованными.
Source/package checks и developer observation не равны независимой пользовательской
оценке. `confirmed` не переносится с версии/fixture на любую следующую версию.

## Каркас истории
- **Old state:** прежний продуктовый процесс Wireframer и Fabricator-style работа с плагинами служили контекстом объединения; точную раннюю дискуссию и состав альтернатив ещё нужно уточнить. Selected method transfer подтверждён.
- **Pain:** полный процесс не подходит каждому небольшому запросу; формально корректные артефакты могли терять смысл; ответы сообщали факт выполнения без полезного вывода.
- **Desired state:** Fab как соавтор инди-создателя: самостоятельные полезные навыки, optional routes, сохранение смысла, проверяемые результаты и ограничение операторского внимания.
- **Alternatives:** полный pipeline на каждый запрос; только общие coauthor-инструкции; повторять full runs вместо targeted corrections; community Canvas, ELK adapter или свой viewer; постоянный develop/Git-flow либо одна main с task branches. Это обсуждавшиеся пути, не все отвергнуты навсегда.
- **Decisions:** десять независимых outcomes; перед работой собственное суждение, после — последствия/рекомендация; mobile first с переносимым смыслом; точечные behavioral correctives; table default и Canvas opt-in; readiness по поверхностям; разрешённый отдельный чат с durable packet.
- **Turning point:** браузерный прототип оказался работоспособным в выбранных сценариях, но его карта теряла ownership/returns. Позже no-warning preview всё ещё перекрывал подписи. Возникла необходимость проверять каждый обещанный результат отдельно.
- **Result:** локальная beta.20, проверенные partial outcomes, адресные коррекции, сохранённые FAIL, табличный fallback и Git-изоляция; пакет контекста подготовлен для отдельной работы над картой.
- **Limits:** renderer не исправлен, prototype-first решение не реализовано до поступления UI; native/mobile usability/general continuity не доказаны; chat recovery pending; main migration только proposal; нет публичного релиза/production maturity.
- **Lessons:** валидный файл не равен корректному смыслу и читабельности; хорошие инструкции нуждаются в наблюдении выхода; закрывать узкий контракт, а не весь продукт; сохранять исходный FAIL и проверять полезный corrective; перенос контекста включает фактическое восстановление.

Этот каркас имеет проверенный поворот, варианты и ограничения. Для технической
истории о разработке достаточно исходного материала; для заявления о ценности
реальным пользователям доказательств пока нет.

## Ключевые артефакты
- [Partial outcomes и исходные/исправленные ответы](../../experiments/workflow-tests/2026-10-12-partial-routes-results.md).
- [Проблемная карта — PNG](../../experiments/workflow-tests/partial-routes-20261012/wireframe-corrective/ui/structure.png).
- [Таблица той же карты](../../experiments/maintenance/release-policy-20261012/structure-table.md).
- [Recovery прототипа: сохранённый draft](../../experiments/workflow-tests/mobile-pipeline-20261012/ui/recovery-retained.jpg).
- [Canvas handoff packet](../handoffs/canvas-workstream-2026-10-12.md).
- [Новый журнал](../project-journal.md).

Это индекс существующих assets; план иллюстраций не создавался. Перед публичным
использованием проверить конкретный asset/revision, убрать внутренние ссылки и
не выдавать synthetic prototype за запущенный пользовательский продукт.

## Открытые вопросы
1. Какие именно роли/плагины и альтернативы были названы в первой дискуссии до bootstrap Fab? Нужно отдельное адресное восстановление ранней истории, если она нужна статье.
2. Сохраняются ли смысл и полезное завершение в обычных новых проектах, вне corrective fixtures?
3. Подтвердится ли recovery нового Canvas-чата и устойчивость дальнейшей непрерывности?
4. Какой UI-прототип предложит creator, какой viewer/engine под него подходит?
5. Будут ли приняты main migration и GitHub protection/backup scope?
6. Какая реальная пользовательская ценность Fab наблюдалась после подключения к внешнему проекту? Пока evidence нет.

## Следующая передача
Рекомендованный следующий Publicator skill при явном запросе текста — **Writer**.
Передать этот packet и journal, выбрать угол истории и соблюдать статусы claims.
Текущая задача заканчивается журналом/evidence; публикационный текст не запрошен.
