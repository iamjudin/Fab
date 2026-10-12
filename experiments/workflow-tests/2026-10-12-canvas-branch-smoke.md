# Canvas: проверка создания и изоляции ветки

## Контракт до запуска
Запрос creator: проверить создание новой ветки для Canvas в проекте Fab.
Исполнитель — основной чат, Fab Testing; без model/subagent runs и без нового чата.
Гипотеза: новая ветка и её собственный коммит в отдельном checkout не меняют
ветку/HEAD/файлы основного проекта или установленную beta.19.

Основной checkout: `/Users/iamjudin/Desktop/Lab/Fab`, `codex/fab-maintenance`.
Переиспользуем managed checkout `/Users/iamjudin/.codex/worktrees/fab-map-view/Fab`.
Новая тестовая ветка: `codex/canvas-branch-smoke`, от проверенного main checkpoint.
Она служит только smoke; рабочая ветка карты остаётся `codex/fab-map-view`.
Контрольный файл — scoped smoke-marker; продуктовую схему/renderer не меняем.

Сигналы: новый branch создан от точного SHA; marker существует только в тестовой
ветке; после commit main HEAD/branch/tracked files и source/cache fingerprint прежние;
после возврата `codex/fab-map-view` чиста и marker в checkout отсутствует.
Budget: одно создание ветки, один контрольный commit, одна проверка изоляции,
один возврат. Stop на достаточном evidence или первой несогласованной мутации.
Никакого merge/push/install/release, layout spike или выбора engine.

## Результат
**PASS в заявленной технической границе.** Новая ветка создана от `3e53097`,
контрольный commit `25eaa72` содержит только один marker. Его нет в main checkout;
main branch/HEAD/tracked files и установленная beta.19 `40cf2ca557e185fb` не менялись.
В основном checkout добавлены только собственные записи этого теста; они не
считались сторонним изменением и будут сохранены отдельным documentation commit.

Рабочая копия возвращена на `codex/fab-map-view` / `75540f1`, чиста, marker исчез.
Тестовая ветка/commit сохранены локально для проверки, ничего не слито/опубликовано.
Содержательная разработка карты по-прежнему parked до прототипа creator.

Evidence: [before](canvas-branch-smoke-20261012/before.json),
[after commit](canvas-branch-smoke-20261012/after-commit.json),
[restored](canvas-branch-smoke-20261012/restored.json).
Исполнитель — root; model runs0, resets0, external writes0. Это технический тест
Git и наблюдение текущего исполнения правила, не independent fresh-model behavioral
PASS и не проверка качества Canvas. Лимиты/токены модели отдельно не измерялись.

Вывод: физическая и историческая изоляция работает; для карты безопасно использовать
отдельную рабочую копию. Создавать новый checkout/branch на каждое продолжение не
нужно. Следующая содержательная граница — прототип creator; основная отладка Fab
продолжается здесь. FAB-13 поведенческая проверка остаётся открытой, WF-20 не закрыт.
