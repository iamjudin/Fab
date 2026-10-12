# Git-процесс Fab: исследование и предложение

Статус: **proposal**, не принятое изменение правил Git. Дата:2026-10-12.
Вопрос: как сохранять пригодный к использованию Fab и выпускать версии, пока
отдельные чаты исследуют/перерабатывают части продукта? Исследование ограничено
GitHub flow, trunk-based, Git-flow и versioned plugin release; platform hosting
и организация большого коллектива не входят. Источники — первичная документация.
Stop: достаточно данных для выбора процесса и конкретного плана перехода.

## Вывод для Fab
Рекомендую одну постоянную `main`, короткие ветки задач, release-теги и отдельную
ветку поддержки версии только при реальной необходимости. Основа — GitHub flow,
с versioned release/hotfix расширением для плагина. Это собственная рекомендация
для одной активной beta-линии и нескольких изолированных рабочих чатов.
Постоянная `develop` сейчас добавит ещё одну интеграционную границу без названной
потребности. `main` содержит проверенные принятые изменения в заявленном beta-scope;
она может быть новее установленного/выпущенного пакета. Последний выпуск хранит tag.

## Фактическое состояние до исследования
Git checked at main-owner HEAD `983fbf6`; рабочий каталог чист.

| Ветка/объект | Фактическая роль |
| --- | --- |
| `main` | Нет ни локально, ни на GitHub. |
| `codex/bootstrap-beta` | Bootstrap/history; GitHub default branch. Local167c6be, remote e6dfeab. |
| `codex/fab-maintenance` | Текущая основная работа/установленная beta.20. HEAD983fbf6;22commits ahead удалённой базы при проверке. |
| `codex/fab-map-view` | Canvas-контекст и будущая переработка; c1681d5, отдельный checkout60c9. Source baseline beta.18, общий installed runtime beta.20. |
| `codex/canvas-branch-smoke` | Одноразовый Git-тест, marker-only25eaa72; не продуктовая feature. |
| `codex/partial-workflow-tests`, `codex/canvas-layout-research` | Завершённые checkpoints тестов/исследования; части истории основной текущей линии. |
| `checkpoint-beta18/19/20-2026-10-12` | Локальные immutable по нашей политике checkpoints; на GitHub пока отсутствуют. |

На GitHub обнаружена только heads/codex/bootstrap-beta и теги beta.1/beta.9.
Это не означает потерю новых изменений: они в локальном Git, но удалённая копия
ещё не содержит текущую линию. Installed beta.20 — локальный пакет, не публичный
релиз. Workflow Fab package/scope подготовлен локально; его remote run и фактические
GitHub protection settings этим исследованием не проверены.
Проверка chat recovery Canvas остаётся pending: native inventory ещё не раскрыла
real thread ID. Это не дефект Git; новый дубль не создаём.

## Что дают изученные подходы
GitHub flow описывает ветку для независимого изменения, review/PR, merge и
завершение ветки. Малые связанные изменения упрощают просмотр и отмену.
[GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).

Trunk-based делает акцент на коротком времени расхождения веток и частой
интеграции готовых частей. Для Fab возьмём малые завершённые порции, не обязательный
дедлайн в два дня для ожидающего прототипа исследования.
[Short-lived branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/).

Git-flow вводит постоянные development/release линии. Автор отдельно объясняет,
что контекст важен: простое continuous delivery допускает более лёгкий процесс,
поддержка нескольких версий может оправдать Git-flow. Fab версионируемый, но
несколько одновременно поддерживаемых версий пока не заявлены — полный процесс
нам сейчас не нужен. Это вывод для Fab, не универсальная оценка Git-flow.
[Автор модели](https://nvie.com/posts/a-successful-git-branching-model/).

Release branch можно создать поздно от проверенного тега, когда нужен patch старой
версии. Исправление желательно сначала воспроизвести/сохранить в основной линии,
потом адресно перенести в поддержку; исключение требует явно отследить обратный
перенос, иначе дефект вернётся в следующем выпуске.
[Branch for release](https://trunkbaseddevelopment.com/branch-for-release/).

## Предлагаемые правила по ситуациям

| Ситуация | Ветка и база | Чат/среда | Завершение |
| --- | --- | --- | --- |
| Мнение, идеи, анализ без правок | Новая ветка не нужна | Текущий чат | Ответ/evidence достаточного размера |
| Правка в рамках текущей задачи | Та же task-ветка; новая задача от `main` | Текущий owner | Проверка + локальный commit, затем integration review |
| Новая функция | `codex/feat-<scope>` от актуальной `main` | Отдельный чат/worktree при самостоятельном потоке и разрешении | Готовый малый increment → review/checks → согласованный merge |
| Неизвестное решение/переработка | `codex/spike-<scope>` от названной базы | Изолированная среда, отдельный scoped packet | Вывод/проверенный кусок; эксперимент целиком автоматически не интегрируется |
| Обычный баг текущего продукта | `codex/fix-<scope>` от `main` | Без обязательного нового чата | Проверка конкретного дефекта и зависимостей → integration review |
| Срочный patch выпущенной версии | Если `main` подходит — обычный fix; иначе `codex/hotfix-<version>-<scope>` от release tag | Отдельный checkout старой версии | Только необходимый patch, новый tag/version; исправление должно попасть и в основную линию |
| Выпуск новой версии | Проверенный SHA `main`, tag `v<version>` | Release owner в основном чате | Package/поведение/scoped gate/parity/rollback; выбранный канал, не автоматическая публикация |
| Параллельная поддержка версии | `codex/release-<line>` только по потребности | Явный owner | Адресные fixes, без новых features и смешения с текущей разработкой |

Префикс `codex/` сохраняет соглашение проекта; `main` — каноническая линия,
не ветка конкретного агента. Имена выше — предлагаемый convention, не новые refs.
Один результат может состоять из нескольких небольших PR, если каждый полезен
самостоятельно. Ожидающая input ветка может жить долго; опасны растущий code delta
и несогласованные общие контракты, а не календарный возраст сам по себе.

## Как интегрировать
Мой default для одной законченной задачи — squash merge: понятный общий commit и
простая отмена результата. Для meaningful independently validated checkpoints
оставляем merge commit, когда история нужна. Исторические release/checkpoint tags
и их коммиты не переписываем ради линейной красоты. После squash работу продолжаем
в новой task-ветке, а не добавляем новую задачу в прежнюю долгую ветку.
Это выбор Fab с учётом tradeoffs из
[документации merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges).

Перед интеграцией review diff относительно actual target, разрешить конфликты,
проверить смысл/затронутые сценарии и package gate на окончательном состоянии.
Технически чистый merge не доказывает совместимость продуктовых правил.
Проверки отдельной ветки не заменяют проверки её сочетания с текущей основной.
Общую/выпущенную историю не переписывать; проблемы исправлять новым commit/revert.
Релизная идентичность — SHA+version+fingerprint; tag по политике не сдвигается.
Создание branch/commit, private push, merge, install, tag и публикация — разные
действия. В текущем соглашении локальные checkpoints уже разрешены, исследование
не расширяет scope до migration/default-branch change/merge/push.

## Git и отдельные чаты
Branch хранит последовательность коммитов. Worktree даёт разные файлы, HEAD и index
при общем репозитории/refs. Chat хранит взаимодействие и рабочий контекст. Tag
отмечает конкретный выпуск. Эти роли связаны, но не заменяют друг друга.
[Git worktree](https://git-scm.com/docs/git-worktree),
[Git tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging).

Для независимых одновременно работающих чатов нужны разные checkouts и один
writer на общую область. Общий installed Fab, серверные порты и browser storage
автоматически не изолируются worktree. Feature-owner не обновляет общий plugin
cache; локальные тесты имеют свою среду/порты/data и явно записанную версию.
Main владеет общими core/backlog/release; feature передаёт scoped findings и
дифф/проверки, не копию глобального backlog и не заявление о creator acceptance.
Новый чат создаётся с packet/изоляцией в разрешённом scope; host ID/cwd и реальное
восстановление проверяются. Это необязательно для каждого мелкого исправления.

Перед закрытием ветки сохранить полезное evidence и необходимые commits/tags.
Ignored raw/results не спасаются одним merge; managed archive сохраняет не всё
ignored. Проверить сохранность нужных ignored файлов отдельно. Затем завершённый
worktree архивировать, ненужную ветку закрыть по принятой cleanup-политике.
В текущем исследовании cleanup существующих веток не выполнялась.

## Защита и проверки на GitHub
Предлагаю PR для попадания в `main`, required package/tests/scope check, запрет
force-push/delete основной ветки. Наличие workflow само по себе merge не запрещает;
нужны реально настроенные required checks и понятные bypass rules.
Для solo-owner не требовать второго человека ради формального approving review;
содержательный creator выбор обсуждаем, техническую проверку делает Fab.
В приватном GitHub-репозитории доступность protection зависит от тарифа; по docs
private protected branches доступны Pro/Team/Enterprise. Actual plan/permissions
в этом исследовании не проверены. Нельзя объявлять защиту включённой или менять
visibility ради неё без разрешённого scope.
[Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Конкретный переход, если предложение принято
1. Проверить актуальный private remote/refs и кандидат beta.20, заявленный scope,
   retained evidence/проверки. Создать `main` от выбранного проверенного SHA текущей
   основной линии; исторические ветки/tags сохраняются. Создание указателя само
   по себе не добавляет зрелости. Не squash всю старую историю и не начинать с
   устаревшей GitHub beta.9 с потерей локальных изменений.
2. В согласованном scope сохранить выбранные refs/tags на private origin,
   настроить default branch `main`, получить реальный remote CI результат.
3. Проверить доступность и согласовать protection settings; отметить любой
   отсутствующий механизм как отсутствие механической защиты.
4. Основной чат координирует `main` и task-ветки; одна бесконечная maintenance-ветка
   перестаёт быть второй постоянной линией. Общие docs остаются каноническими.
5. Canvas сохраняет контекст/изоляцию. Перед реальной реализацией после UI-прототипа
   согласованно синхронизировать его старую source baseline с новой `main`;
   не включать smoke-marker и не объединять research с готовой feature по названию.
6. Классифицировать законченные bootstrap/test/research/smoke refs, сохранить
   evidence и убрать ненужные активные копии/ветки после согласованного завершения.

Действия migration не выполнялись: текущий запрос — исследование/объяснение.
Runtime beta.20 не менялся. Значимая развилка — принять лёгкую схему и переход,
либо назвать реальную потребность в нескольких постоянных release/develop линиях.

## Источники
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/)
- [Branch for release](https://trunkbaseddevelopment.com/branch-for-release/)
- [Git-flow и оговорка автора](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git worktree](https://git-scm.com/docs/git-worktree)
- [Git tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
- [Pull request merge strategies](https://docs.github.com/en/pull-requests/reference/pull-request-merges)
- [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
