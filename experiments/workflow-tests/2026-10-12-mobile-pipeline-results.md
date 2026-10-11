# Fab: новый мобильный проект до прототипа · 2026-10-12

## Вывод
**Fab дошёл от естественного запроса до рабочего интерактивного кандидата.
Полного чистого PASS маршрута нет: структура/return projection частично FAIL.**
Product и последовательность structure/scenarios/visible blocks → code сохранены;
root реально проверил выбранные UI-пути, persistence и recovery. Проекция
владельца поездки и условных выходов общей формы потеряла часть смысла.
Новые runtime/core fixes и corrective runs в этот тест не добавлялись.

## Что запускали
Один свежий CLI-контекст, установленный Fab beta.14, 60 файлов,
fingerprint `562f55c7ef31d731`, source checkpoint `1c11df4`; parity до запуска.
Actual модель **GPT-6.1 Sol / Low**, штатный CLI default, не High основного чата.
Новый личный app для сборов в поездки: поездки, вещи, packed/undo, правка/отмена,
фильтр остатка и поздний возврат. Без upstream fixtures/model/IA или golden output.
iOS-first/русский/один актор/browser prototype — synthetic operator choices,
не реальные решения о запуске продукта или creator acceptance.

[Контракт](2026-10-12-mobile-pipeline-contract.md),
[полный запрос](mobile-pipeline-20261012/prompt.md),
[ответ](mobile-pipeline-20261012/final.md),
[runtime](mobile-pipeline-20261012/runtime.json),
[compact events](mobile-pipeline-20261012/observed-events.json).

## Исходы по утверждениям

| Утверждение | Итог и evidence |
| --- | --- |
| Личный intent, UC/rules/slice сохранены | Ограниченный PASS: модель содержит шесть UC, candidate assumptions и scope; unsupported BJ не выдуман, creator axis явно оценена |
| Работа действительно идёт по шагам | PASS для этой последовательности: model и blocks.html записаны до prototype code; Product/Wireframe/Prototype contracts прочитаны |
| Mobile method подключён | PASS как чтение/применение brief: stack/parent/input/return/native boundary, без лишних tabs/dashboard; это не native HIG conformance |
| Физический structure guard | PASS: 3 surface groups и отдельная группа повторяющейся вещи; это слабее полной семантической проверки |
| Владение и return semantics во всех проекциях | Частичный FAIL: две конкретные находки ниже |
| Видимые блоки перед кодом | PASS: отдельный blocks.html с тремя поверхностями и empty states; root DOM/изображение просмотрены |
| Исполняемый прототип | Root bounded UI PASS: выбранные реальные browser paths ниже; без domain/source исправлений |
| Native iOS, большие карты, creator usability | Не проверены; ни browser, ни SVG не объявлены этим evidence |

Fab начал с собственной оценки идеи и компромисса: узкий срез без категорий/
шаблонов, явное сохранение имён и обратимые отметки. Это положительный сигнал
FAB-11 в новом контексте, не доказательство всех случаев согласия/возражения.
Формальных approval-пауз и дополнительных агентов не было.

## Две находки Wireframe

**WF-01: trip row ownership не доведён до физической проекции.**
interface.md говорит, что каждая строка поездки владеет именем/прогрессом/открытием.
В Canvas `trips` и `open` лежат отдельно прямо в S-01; trip-item owner group нет.
Для вещи group `item-owner` существует. Screen containment guard принимает
плоскую часть S-01, но не подтверждает требуемую семантическую вложенность.
Влияние: карту можно прочитать как screen-level действие вместо действия
конкретной поездки. Уверенность высокая: JSON, SVG/PNG и текст кандидата согласованы
в наблюдении этого расхождения. Next: семантическая проверка повторяемых элементов,
включая все коллекции, а не только одну показанную card.

**FAB-03: общий «возврат к родителю» теряет ветвь создания поездки.**
S-03 содержит labels `Создать/Сохранить → родитель` и `Отмена → родитель`, без
Save/Cancel egress edges. interface.md также обещает возврат к родителю после
успешной записи. Реальное создание поездки из S-01 открывает её список S-02.
Для создания/правки вещи родитель уже S-02. Модель/основной сценарий правильно
описывают открытие поездки, но общий contract формы и карта не отражают разные
entry/commit/cancel contexts. Влияние: перенос в реализацию может потерять
правильную цель перехода. Next: branch-specific transition outcomes на той же
форме, не обязательные новые экраны и не новый полный Product discovery.

[Root preview структуры](mobile-pipeline-20261012/structure-root.png).
Это SVG-render, не native Obsidian. Карта/интерфейс/код не исправлены root;
первичный исход сохранён. Общий guard PASS не переписан в semantic PASS.

## Root браузерная проверка
IAB, один origin `http://127.0.0.1:8842/prototype/`, реальные DOM/UI handlers
и browser localStorage. Наблюдались:
- пробельная валидация с возвратом фокуса, создание поездки и вещи через Enter;
- длинное неразрывное имя вещи, edit/cancel сохраняет исходное имя, edit/save Enter;
- packed исчезает из «Осталось», Undo в том же контексте возвращает вещь;
- one-shot сбой записи оставляет открытую форму и `Очки`; retry без закрытия
  создаёт одну вещь, список меняется с двух на три, без дубликата;
- две поездки с независимым прогрессом;
- same-origin reload сохраняет поездку, фильтр «Осталось» и `1 из 3`;
- Escape отменяет правку; при 320 и 430 CSS px нет горизонтального overflow,
  длинное слово и кнопки просмотрены визуально.

[Сбой/draft](mobile-pipeline-20261012/ui/recovery-retained.jpg),
[retry](mobile-pipeline-20261012/ui/recovery-success.jpg),
[узкий viewport](mobile-pipeline-20261012/ui/narrow-320.jpg),
[reload DOM](mobile-pipeline-20261012/ui/reload.dom.txt),
[блоки](mobile-pipeline-20261012/ui/blocks.jpg).
Авторский минимальный DOM harness повторён root в ожидаемой cwd: PASS;
он отдельно покрывает corrupt storage/escaping и failed toggle, не выдаётся
за наблюдение этих путей в настоящем browser. 200% text scaling, native keyboard,
screen reader, OS Back/gestures/background restoration и реальная польза не проверены.

## Среда, сохранность и цена
Автор честно сообщил, что его Chrome UI access был отклонён, и не назвал harness
браузерной проверкой. Его server закончился с CLI: root первое открытие получило
connection refused. Root поднял тот же порт/root в server session3372 и потом
реально наблюдал UI. Это environment intervention; source/JS/cache не менялись.
Занятый 8765 во время author run не освобождался: прежние preview сохранены.
Root CUA combined documentation call был отклонён auto-review; корректные
раздельные initialization/docs actions разрешены, обхода/новых разрешений нет.

До root observation workspace заморожен в ignored raw/initial-workspace;
[initial SHA](mobile-pipeline-20261012/initial-sha.json) совпали после всех проверок.
Helper runner удалён; prompt/version/logs/usage и воспроизводимый author harness
сохранены. Test package/source не включены в Git Fab, raw logs/archive ignored.
Нет установки тестового app, commit/remote/publication/subagents/reset.

Один primary: **241.1s / input708771 / cached659968 / output10996**,
в пределах прогноза 1.5M/25k/900s. Root orchestration/browser/ingestion overhead
отдельно/неизвестен; это не account-limit percentages. [Usage](mobile-pipeline-20261012/usage.json).
Root — observer, не независимый сторонний аудит. Без автоматического corrective.

## Рекомендуемый следующий шаг
Укрепить семантический preflight Wireframe для всех повторяемых owner contexts
и разных исходов shared form. Затем один узкий corrective этой карты/контракта,
с прежними UC/IDs/prototype bytes, а не новый полный маршрут ради статистики.
Мобильный метод сохраняем как условную ветку общего продукта; будущий web
переиспользует intent/rules и отдельно уточняет URL/history/input/layout.
Desktop web и native implementation требуют своего evidence.
