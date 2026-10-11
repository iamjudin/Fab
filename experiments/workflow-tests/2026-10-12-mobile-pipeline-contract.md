# Полный мобильный маршрут Fab · 2026-10-12

## Вопрос
Сможет ли fresh installed Fab по запросу создать новое мобильное приложение
сохранить смысл/правила и пройти Product → Wireframe → Prototype, включая
видимые блоковые экраны до кода, до реально доступного интерактивного кандидата?
Проверяет FAB-03/WF-01/WF-17 и подключение mobile-method FAB-05.
Тестовый продукт не цель Fab; это новый различающий сигнал после исследования,
не повтор полного маршрута ради статистики. FAB-02/09/10/11 не закрываются автоматически.

## Вход и границы
Небольшой личный app для сборов в поездки, один актор, вложенность
поездка → список вещей → конкретная вещь. Создание, правка/отмена,
packed/undo, просмотр несобранного и возврат в контекст. Без коммерческого продукта,
аккаунтов, сети, платежей, push, команды, marketplace или публичного выпуска.
Synthetic operator choices: iOS-first phone candidate, русский текст,
браузерная среда прототипа с явно ограниченной local persistence.
Это выборы теста, не реальная creator acceptance.

Один естественный запрос без upstream fixture/model/IA и без golden output.
Installed runtime beta.14, actual source/cache/fingerprint записать до запуска.
Один fresh CLI-context, без subagents, установки/remote/publication/Git commits
в тестовом workspace. Системный model/effort по умолчанию; actual записать.
Root отдельно проверит структуру/сохранность и реальные браузерные пути.

Workspace/candidate: `mobile-pipeline-20261012/candidate` рядом с этим контрактом,
игнорируется Git для сохранения тестового продукта отдельно от Fab sources.
Все run helpers/raw logs в `mobile-pipeline-20261012/raw/`; после выделения
evidence убрать disposable work, сохранив воспроизводимые inputs/logs в archive.
Не распылять helpers в `/tmp`; активный preview не удалять под видом уборки.

## Отличающие сигналы
- Сохранён новый личный intent, human/creator axes оценены без выдуманного BJ.
- UC/rules/slice → реальные surfaces/owners → critical flows → visible blocks → code.
- Canvas ownership физический; group validator не подменяет семантический review.
- Mobile метод реально прочитан и влияет на выбранную topology/return/input;
  нет обязательных dashboard/tabs и mobile/browser/native не перепутаны.
- Нет искусственных approval-пауз. Разумные неключевые assumptions прозрачны;
  реальные нерешённые зависимости называются, не маскируются принятием creator.
- Root UI: создать trip/item, validation/keyboard activation, edit-cancel,
  packed/undo, navigation/filter return, reload, применимый recovery без потери
  draft. Длинный текст/узкий viewport — если меняет выбранный риск.
- Native OS/keyboard/gestures/accessibility не названы доказанными браузером.

## Бюджет и остановка
Один primary run, прогноз input1500000/output25000, максимум900s wall.
Прогноз не hard within-turn token cap. Без автоматического полного/corrective
повтора; substantive failure сохраняется отдельно и даёт следующую рекомендацию.
Остановить на исчерпании лимита/доступа или повторном transport failure;
нового reset нет. После turn записать input/cached/output/wall и вмешательства.
Root overhead неизвестен/отдельно. UI/server/environment fixes не domain clean PASS.
Начальный результат заморозить до root observation; авторский harness и root UI
имеют разные evidence. Root — observer, не независимый сторонний аудит.
