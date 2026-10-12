# Структура и переходы

Инвентаризация исходной карты. Геометрические группы не доказывают смыслового владельца.

| ID | Тип | Геометрические группы | Содержание / ссылка | Цвет |
| --- | --- | --- | --- | --- |
| S-01 | group | — | label: S-01 Поездки • вход | — |
| trips | text | S-01, trip-list, trip-owner | text: Название поездки<br>Собрано X из Y | #b6bcc3 |
| open | text | S-01, trip-list, trip-owner | text: Открыть поездку → S-02 | #2563eb |
| newtrip | text | S-01 | text: Новая поездка → S-03 | #2563eb |
| S-02 | group | — | label: S-02 Выбранная поездка | — |
| back | text | S-02 | text: Назад к поездкам | #2563eb |
| filter | text | S-02 | text: Все / Осталось | #bae6fd |
| items | text | S-02, item-owner, item-list | text: Название вещи / собрана ли | #b6bcc3 |
| toggle | text | S-02, item-owner, item-list | text: Отметить / вернуть | #16a34a |
| edit | text | S-02, item-owner, item-list | text: Править вещь → S-03 | #2563eb |
| add | text | S-02 | text: Добавить вещь → S-03 | #2563eb |
| S-03 | group | — | label: S-03 Временная форма | — |
| name | text | S-03 | text: Название<br>Поле черновика | #bae6fd |
| save | text | S-03 | text: Создать / Сохранить | #16a34a |
| cancel | text | S-03 | text: Отмена / Escape | #2563eb |
| item-owner | group | S-02, item-list | label: Вещь (повторяется) | — |
| trip-list | group | S-01 | label: Список поездок | — |
| trip-owner | group | S-01, trip-list | label: Поездка (повторяется) | — |
| trip-summary | text | S-02 | text: Полное название поездки<br>Собрано X из Y | #b6bcc3 |
| item-list | group | S-02 | label: Список вещей поездки | — |
| feedback-return | text | S-02 | text: Вернуть отметку через feedback | #16a34a |
| empty-state | text | S-02 | text: Нет вещей / Всё собрано | #b6bcc3 |
| form-heading | text | S-03 | text: Новая поездка /<br>Добавить / Править вещь | #b6bcc3 |
| form-error | text | S-03 | text: Ошибка ввода / записи | #b6bcc3 |
| legend | text | — | text: Обозначения<br>Серый — информация<br>Голубой — локальный ввод<br>Синий — переход; зелёный — запись<br>Возврат после записи: только успех | #b6bcc3 |

| ID перехода | Откуда | Куда | Условие / действие | Направление концов |
| --- | --- | --- | --- | --- |
| openedge | open | S-02 | — | none → arrow |
| backedge | back | S-01 | — | none → arrow |
| newtripedge | newtrip | S-03 | — | none → arrow |
| editedge | edit | S-03 | — | none → arrow |
| addedge | add | S-03 | — | none → arrow |
| save-return | save | S-02 | Успешная запись | none → arrow |
| cancel-trip-return | cancel | S-01 | Новая поездка: отмена | none → arrow |
| cancel-item-return | cancel | S-02 | Вещь: отмена | none → arrow |

## Полный исходный снимок

```json
{
  "nodes": [
    {
      "id": "S-01",
      "type": "group",
      "x": 0,
      "y": 0,
      "width": 440,
      "height": 1010,
      "label": "S-01 Поездки • вход"
    },
    {
      "id": "trips",
      "type": "text",
      "x": 50,
      "y": 165,
      "width": 340,
      "height": 70,
      "text": "Название поездки\nСобрано X из Y",
      "color": "#b6bcc3"
    },
    {
      "id": "open",
      "type": "text",
      "x": 50,
      "y": 255,
      "width": 340,
      "height": 60,
      "text": "Открыть поездку → S-02",
      "color": "#2563eb"
    },
    {
      "id": "newtrip",
      "type": "text",
      "x": 25,
      "y": 455,
      "width": 390,
      "height": 60,
      "text": "Новая поездка → S-03",
      "color": "#2563eb"
    },
    {
      "id": "S-02",
      "type": "group",
      "x": 640,
      "y": 0,
      "width": 440,
      "height": 950,
      "label": "S-02 Выбранная поездка"
    },
    {
      "id": "back",
      "type": "text",
      "x": 665,
      "y": 45,
      "width": 390,
      "height": 55,
      "text": "Назад к поездкам",
      "color": "#2563eb"
    },
    {
      "id": "filter",
      "type": "text",
      "x": 665,
      "y": 215,
      "width": 390,
      "height": 55,
      "text": "Все / Осталось",
      "color": "#bae6fd"
    },
    {
      "id": "items",
      "type": "text",
      "x": 685,
      "y": 415,
      "width": 350,
      "height": 55,
      "text": "Название вещи / собрана ли",
      "color": "#b6bcc3"
    },
    {
      "id": "toggle",
      "type": "text",
      "x": 685,
      "y": 490,
      "width": 350,
      "height": 55,
      "text": "Отметить / вернуть",
      "color": "#16a34a"
    },
    {
      "id": "edit",
      "type": "text",
      "x": 685,
      "y": 565,
      "width": 350,
      "height": 55,
      "text": "Править вещь → S-03",
      "color": "#2563eb"
    },
    {
      "id": "add",
      "type": "text",
      "x": 665,
      "y": 705,
      "width": 390,
      "height": 55,
      "text": "Добавить вещь → S-03",
      "color": "#2563eb"
    },
    {
      "id": "S-03",
      "type": "group",
      "x": 1280,
      "y": 0,
      "width": 440,
      "height": 630,
      "label": "S-03 Временная форма"
    },
    {
      "id": "name",
      "type": "text",
      "x": 1305,
      "y": 140,
      "width": 390,
      "height": 80,
      "text": "Название\nПоле черновика",
      "color": "#bae6fd"
    },
    {
      "id": "save",
      "type": "text",
      "x": 1305,
      "y": 335,
      "width": 390,
      "height": 60,
      "text": "Создать / Сохранить",
      "color": "#16a34a"
    },
    {
      "id": "cancel",
      "type": "text",
      "x": 1305,
      "y": 445,
      "width": 390,
      "height": 60,
      "text": "Отмена / Escape",
      "color": "#2563eb"
    },
    {
      "id": "item-owner",
      "type": "group",
      "x": 670,
      "y": 395,
      "width": 380,
      "height": 250,
      "label": "Вещь (повторяется)"
    },
    {
      "id": "trip-list",
      "type": "group",
      "x": 20,
      "y": 90,
      "width": 400,
      "height": 310,
      "label": "Список поездок"
    },
    {
      "id": "trip-owner",
      "type": "group",
      "x": 35,
      "y": 140,
      "width": 370,
      "height": 230,
      "label": "Поездка (повторяется)"
    },
    {
      "id": "trip-summary",
      "type": "text",
      "x": 665,
      "y": 120,
      "width": 390,
      "height": 70,
      "text": "Полное название поездки\nСобрано X из Y",
      "color": "#b6bcc3"
    },
    {
      "id": "item-list",
      "type": "group",
      "x": 655,
      "y": 345,
      "width": 410,
      "height": 330,
      "label": "Список вещей поездки"
    },
    {
      "id": "feedback-return",
      "type": "text",
      "x": 665,
      "y": 785,
      "width": 390,
      "height": 55,
      "text": "Вернуть отметку через feedback",
      "color": "#16a34a"
    },
    {
      "id": "empty-state",
      "type": "text",
      "x": 665,
      "y": 860,
      "width": 390,
      "height": 55,
      "text": "Нет вещей / Всё собрано",
      "color": "#b6bcc3"
    },
    {
      "id": "form-heading",
      "type": "text",
      "x": 1305,
      "y": 45,
      "width": 390,
      "height": 70,
      "text": "Новая поездка /\nДобавить / Править вещь",
      "color": "#b6bcc3"
    },
    {
      "id": "form-error",
      "type": "text",
      "x": 1305,
      "y": 225,
      "width": 390,
      "height": 60,
      "text": "Ошибка ввода / записи",
      "color": "#b6bcc3"
    },
    {
      "id": "legend",
      "type": "text",
      "x": 0,
      "y": 1110,
      "width": 580,
      "height": 155,
      "text": "Обозначения\nСерый — информация\nГолубой — локальный ввод\nСиний — переход; зелёный — запись\nВозврат после записи: только успех",
      "color": "#b6bcc3"
    }
  ],
  "edges": [
    {
      "id": "openedge",
      "fromNode": "open",
      "toNode": "S-02",
      "fromSide": "right",
      "toSide": "left"
    },
    {
      "id": "backedge",
      "fromNode": "back",
      "toNode": "S-01",
      "fromSide": "left",
      "toSide": "right"
    },
    {
      "id": "newtripedge",
      "fromNode": "newtrip",
      "toNode": "S-03",
      "fromSide": "right",
      "toSide": "left"
    },
    {
      "id": "editedge",
      "fromNode": "edit",
      "toNode": "S-03",
      "fromSide": "right",
      "toSide": "left"
    },
    {
      "id": "addedge",
      "fromNode": "add",
      "toNode": "S-03",
      "fromSide": "right",
      "toSide": "left"
    },
    {
      "id": "save-return",
      "fromNode": "save",
      "toNode": "S-02",
      "fromSide": "right",
      "toSide": "bottom",
      "label": "Успешная запись"
    },
    {
      "id": "cancel-trip-return",
      "fromNode": "cancel",
      "toNode": "S-01",
      "fromSide": "right",
      "toSide": "left",
      "label": "Новая поездка: отмена"
    },
    {
      "id": "cancel-item-return",
      "fromNode": "cancel",
      "toNode": "S-02",
      "fromSide": "right",
      "toSide": "bottom",
      "label": "Вещь: отмена"
    }
  ]
}
```
