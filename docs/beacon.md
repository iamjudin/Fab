# Маяк Fab

Канонические принципы: [runtime core](../plugins/fab/shared/core.md). Каждый навык читает их при прямом входе; этот документ — индекс, а не вторая копия инструкций.

## Пять групп

1. **Полезный результат и соразмерность.** Делаем запрошенный исход; глубина зависит от задачи и риска.
2. **Сохранность замысла.** Требование, гипотеза, принятый выбор и проверенный факт различаются; перенос между этапами сохраняет смысл.
3. **Соавторство и внимание.** Совет, критика и обсуждение существенных компромиссов; человеку легко считать вывод и требуемое действие.
4. **Честная проверка.** Структура, семантика, исполнение, независимость и creator judgement — разные evidence.
5. **Движение и обучение.** Находки имеют владельца и следующий шаг; checkpoint сохраняет прогресс, не создаёт остановку.

## Маршруты

Прямой Research/Analysis/Brainstorm/Testing/Cowork может завершить задачу сам. Plugin и Delivery обслуживают разработку и выпуск плагина. Git и культура проекта сквозные.

Обычный продуктовый маршрут: Product определяет смысл, UC, правила и срез → Wireframe организует поверхности/вложенность/навигацию, критические сценарии и блоковую композицию → Prototype исполняет выбранное поведение → Delivery организует дальнейшую реализацию, проверку и выпуск. Реальные зависимости сохраняются, но принятый существующий материал не нужно создавать заново. Ранний prototype/spike допустим для названного риска.

Детали и границы: [decision policy](../plugins/fab/shared/decision-policy.md), [архитектура](architecture/design.md), соответствующий SKILL и reference. Новое исследование уточняет метод, не создаёт обязательный дополнительный этап.

## Research foundation

The project supplies context and priorities, not a filter for the knowledge base.
Research supports reusable understanding and joint ideation. Consult existing
knowledge before proposing a focused investigation of consequential uncertainty.
Canonical principle: [research as reusable knowledge](../plugins/fab/shared/core.md#research-as-reusable-knowledge).
Operational scope: [foundation and focused investigation](../plugins/fab/skills/research/references/reuse.md).

## Актуальность

Новый устойчивый принцип проверяем по core → skill → check → evidence. Инцидент или конкретная ошибка сначала попадают в backlog, а не раздувают Маяк. Автотесты не доказывают реальную ценность и принятие создателем. Текущая проверенная граница — [handoff](handoff.md) и [backlog](backlog.md).
