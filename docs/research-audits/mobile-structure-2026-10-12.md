# Мобильный метод: включение в Fab · 2026-10-12

## Вывод и применимость
Отчёт закрывает конкретный пробел FAB-05: выбор mobile surfaces, владельцев,
возврата, input/lifecycle и платформенных ветвей. В runtime включена рабочая
выжимка и lossless indexed full, без новой обязательной стадии.
Общая продуктовая модель сохраняется; iOS/Android/mobile web читаются по вопросу.
Desktop web остаётся возможным направлением, но его полнота этим отчётом не доказана.

Original: Brain/Library/Мобильная структура и взаимодействие для Fab.md.
Source/retained SHA256: `f72f0d703fb94d10dafa04dd9ccc2da2a43570b88c2f4701d32631daa258dc3d`.
49 разделов сохранены без исключений. Ingested 2026-10-12; исследовательская дата
публикации неизвестна, sourceDate=null. Исходник пока не переименован/помечен:
опциональная пометка требует ответа после готового ingestion.

## Что переносим
Оперативный метод: вход/owner/результат перехода/сохраняемый контекст,
минимальная достаточная topology, локальное владение, различие Back/Close/Cancel/
commit, применимые проверки draft/ошибки/возврата и честная граница browser/native.
Полный материал сохраняет детали платформ/API/числовых порогов и источники;
он читается выборочно, а текущие платформенные факты перепроверяются.
Четыре владельца Product/Wireframe/Prototype/Delivery имеют условные ссылки.

## Проверки и пределы
Структура packet/retained hash и ссылки package проверяются локально. Brief
сопоставлен с активными разделами R002–R009/R011/R017–R021/R038–R043.
Отчёт сам заявляет **7 unresolved source bindings**; они сохранены как предел,
не восстановлены догадкой и не выданы за полностью проверенные ссылки.

Primary spot-check 2026-10-12:
- [Apple Modality](https://developer.apple.com/design/human-interface-guidelines/modality):
  JS-page прочитана через browser DOM; подтверждены временный родительский
  контекст, явный выход, защита пользовательского ввода и ограниченная задача.
- [Apple Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars):
  JS-page прочитана через browser DOM; подтверждены destinations вместо команд
  и сохранение navigation state. В текущей iOS guidance допустим dedicated search
  tab. Поэтому категоричный пример отчёта «Search — всегда действие» уточнён в
  brief: роль поиска определяется контекстом, постоянная search surface допустима.
  Полный источник не переписан, расхождение сохранено как evidence.
- [Android back stack](https://developer.android.com/guide/navigation/backstack):
  primary page подтверждает стек destinations и сохранение/восстановление
  navigation state; page update 2026-05-29. Это API/guidance, не device evidence.
- [Android navigation bar](https://developer.android.com/develop/ui/compose/components/navigation-bar):
  primary page доступна; numeric defaults не включены в краткий универсальный слой.

Это выборочная проверка оснований, не полный фактчек отчёта, не подтверждение
native usability или поведения устройства. Следующий опыт — один свежий
мобильный продуктовый маршрут до browser prototype с отдельным root UI-наблюдением.
Обязательного нового полного прогона каждого standalone skill не требуется.
