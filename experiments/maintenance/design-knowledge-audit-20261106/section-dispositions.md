# Component-architecture report: section dispositions

All85indexed sections are retained in the privately preserved source packet.
These are audit dispositions and proposed owners, not implemented knowledge.

| Section | Title | Owner | Disposition and boundary |
| --- | --- | --- | --- |
| R001 | Preamble | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R002 | Содержание | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R003 | Ориентация и статус доказательств | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R004 | Короткий ответ | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R005 | Границы компонентов и смысл Atomic Design | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R006 | Что Atomic Design действительно утверждает | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R007 | Концептуальная часть, слой и компонент — разные вещи | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R008 | Альтернативы атомной классификации | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R009 | Когда извлечение действительно окупается | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R010 | Четыре конструкции | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R011 | Прямая конструкция | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R012 | Общий Base | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R013 | Раздельные masters содержимого, основы и оформления | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R014 | Композиция с ограниченной областью замены | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R015 | Когда фрейм должен остаться фреймом | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R016 | Решение без фиксированной глубины | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R017 | Что известно эмпирически | verification-fit | evidence-gap. No measured optimal nesting or quantitative maintenance superiority. Unidentified CHI structural-comprehension claims and missing source mappings stay unverified. |
| R018 | Свойства, допустимые комбинации и состояния | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R019 | Что должно быть публичным свойством | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R020 | Допустимые комбинации важнее произведения всех свойств | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R021 | Избыточная настраиваемость | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R022 | Переменные и режимы | token-projection | qualified-reference. Context values versus structures already covered. Six documented product types do not prove Plugin API or workspace support. |
| R023 | Сохранение overrides | system-evolution | enrich-existing. Preserve overrides and defaults. Source names/hierarchy participate in migration. A native-slot migration can break consumers. |
| R024 | Состояния нельзя сводить к одному `State` | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R025 | Перекрывающиеся состояния и приоритеты | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R026 | Представление библиотеки и связь с кодом | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R027 | Организация по назначению обычно полезнее атомных папок | naming | enrich-existing. Consumer search/public asset identity versus internal helpers. No mandatory namespace or automatic rename of accepted libraries. |
| R028 | Иконкам нужно собственное пространство имён, а не размножение вариантов | naming | enrich-existing. Consumer search/public asset identity versus internal helpers. No mandatory namespace or automatic rename of accepted libraries. |
| R029 | Публичные и внутренние ресурсы | naming | enrich-existing. Consumer search/public asset identity versus internal helpers. No mandatory namespace or automatic rename of accepted libraries. |
| R030 | Исходный master и документационный экземпляр — разные объекты | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R031 | Что показывать, а что только документировать | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R032 | Схема устройства и матрица состояний выполняют разные задачи | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R033 | Figma и код должны совпадать семантически, а не деревом | ownership | enrich-existing. Map semantic contracts and public choices without identical internal trees. Legacy Code Connect parser examples are not a current implementation prescription. |
| R034 | Ответственность за обновления | ownership | enrich-existing. Map semantic contracts and public choices without identical internal trees. Legacy Code Connect parser examples are not a current implementation prescription. |
| R035 | Эволюция и миграция | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R036 | Расширить или разделить | system-reuse | already-covered. Behavioral contract determines extension/split and domain/core ownership. Retain concrete counterexamples. |
| R037 | Совместимые и несовместимые дополнения | system-evolution | enrich-existing. Preserve overrides and defaults. Source names/hierarchy participate in migration. A native-slot migration can break consumers. |
| R038 | Миграция — часть архитектуры | system-evolution | enrich-existing. Preserve overrides and defaults. Source names/hierarchy participate in migration. A native-slot migration can break consumers. |
| R039 | Локальные доменные композиции | system-reuse | already-covered. Behavioral contract determines extension/split and domain/core ownership. Retain concrete counterexamples. |
| R040 | Изменение общих определений | system-evolution | enrich-existing. Preserve overrides and defaults. Source names/hierarchy participate in migration. A native-slot migration can break consumers. |
| R041 | Рабочие сравнения | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R042 | Кнопка с необязательными иконками | component-contract | retained-reference. Case framing. Read actual construction/interaction children before applying. |
| R043 | Задача | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R044 | Вариант A — прямой Button | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R045 | Вариант B — Button с внутренним Base | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R046 | Вариант C — отдельные masters оформления и содержимого | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R047 | Загрузка | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R048 | Длинная подпись | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R049 | Поле ввода с подсказкой и ошибкой | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R050 | Задача | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R051 | Наивная модель | context-axes | enrich-existing. Explain supported overlaps, state precedence and specimen/configuration/runtime differences. The five-axis model is synthesis, not a universal standard. |
| R052 | Более устойчивый контракт | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R053 | Изменение общих отступов | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R054 | Длинное содержимое | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R055 | Строка с аватаром, текстом и завершающим содержимым | component-contract | retained-reference. Case framing. Read actual construction/interaction children before applying. |
| R056 | Задача | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R057 | Вариант A — всё фиксировано | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R058 | Вариант B — ограниченная замена завершающего элемента | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R059 | Вариант C — trailing Slot | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R060 | Почему нельзя решить всё вариантами | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R061 | Семантика взаимодействия | ownership | enrich-existing. Map semantic contracts and public choices without identical internal trees. Legacy Code Connect parser examples are not a current implementation prescription. |
| R062 | Контейнер с произвольным содержимым | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R063 | Задача | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R064 | Компонент-заполнитель | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R065 | Нативный Slot | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R066 | Изменение общих отступов | component-contract | enrich-existing. Distinguish public content/configuration, bounded replacement and free composition. Keep actual tool/API availability separate from documented mechanisms. |
| R067 | Длинное содержимое | browser-integration | already-covered. A slot does not define runtime scrolling or overflow behavior. |
| R068 | Сводка четырёх случаев | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R069 | Кнопка и поле ввода | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R070 | Строка и контейнер | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R071 | Пример страницы документации | verification-fit | enrich-existing. Separate source masters from linked documentation specimens. Show representative risk/content/state cases instead of materializing every combination. |
| R072 | Приложение по доказательствам и источникам | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R073 | Что можно считать достаточно подтверждённым | verification-fit | qualified-reference. Report self-assessment is not independent verification. Primary spot checks and explicit synthesis boundaries are recorded in the audit report. |
| R074 | Что остаётся соглашением или исследовательским выводом | verification-fit | qualified-reference. Report self-assessment is not independent verification. Primary spot checks and explicit synthesis boundaries are recorded in the audit report. |
| R075 | Пробелы в доказательствах | verification-fit | evidence-gap. No measured optimal nesting or quantitative maintenance superiority. Unidentified CHI structural-comprehension claims and missing source mappings stay unverified. |
| R076 | Применение к переданному локальному случаю | concept-extraction | project-only. Local supplied-library application is not adopted architecture or authority to rebuild a file. |
| R077 | Итоговое решение | system-reuse | enrich-existing. Explain independent change/consumer responsibility versus anatomy. Compare direct construction and internal bases. No fixed nesting depth or reuse quota. |
| R078 | Источники | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R079 | Методология и границы компонентов | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R080 | Архитектура компонентов Figma | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R081 | Переменные и режимы | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R082 | Документация промышленных систем | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R083 | Доступность и поведение на платформах | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R084 | Связь дизайна и кода | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
| R085 | Эмпирика | - | retained-reference. Navigation, provenance or section framing. The substantive child sections are assessed separately. |
