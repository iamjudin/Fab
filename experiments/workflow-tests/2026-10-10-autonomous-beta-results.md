# Fab: автономная реализация и проверки · 2026-10-10

## Вывод

**Модульный пакет работает в проверенных границах; полного PASS нет.** Все десять навыков реализованы и установлены. Прямые запросы не вынуждают проходить продуктовую лестницу. Полный новый клиентский маршрут дошёл до прототипа, сохранив intent и роли, но вскрыл два дефекта интерфейсной проверки.

## Что проверили

| Проверка | Результат | Практический вывод |
| --- | --- | --- |
| Пять прямых запросов: Research/Analysis/Brainstorm/Cowork/Testing | Ограниченный PASS | Самостоятельные исходы, без принудительной разработки продукта; Testing честно сообщил FAIL тестируемого поведения. |
| Product→Wireframe на существующем контексте | Ограниченный PASS | Сохранил сигналы/правила, не заставил делать Jobs заново. |
| Ранний Prototype и Plugin→Delivery | Выбранные проверки PASS | Реальные браузерные пути отдельно от harness; source fix/readiness без публикации или выдуманной установки. Ранний prototype не доказывает всю лестницу. |
| Полная новая личная модель | Первичный частичный FAIL, corrective PASS | Creator=user ошибочно посчитан причиной пропустить создательскую ось. Контракт исправлен: оценить обе оси, не выдумывать BJ. |
| Полный новый клиентский маршрут до прототипа | Прогресс; structure FAIL | HJ/BJ, роли, UC/срез, сценарии и visible blocks перед кодом сохранены. Canvas был плоским: 20 text/0 groups. |
| Узкая коррекция Canvas | Ограниченный PASS | 5 реальных поверхностей, вложенные коллекции/элементы/контролы, 15 связей; e0…e11 сохранены. Только три map-файла изменены, prototype/model bytes прежние. |
| Реальный браузер полного прототипа | Большинство выбранных путей PASS; recovery FAIL | Создание/Enter/валидация, ready/undo/history, cancel edit, переназначение, cancel/restore, reload работают. Persistent отказ недоступно отключить за modal, retry требует потери draft. |
| Beta8 recovery corrective | Corrective + root UI bounded PASS | One-shot failure retains draft; retry succeeds in the open modal, one history entry, ready preserved. Initial limit abort and root asset revision recorded separately. |

## Берём в пакет

- Общий договор прямых навыков и optional routes; core читается при прямом входе.
- Самодостаточные brief/full методы с происхождением; Brain не runtime dependency.
- Содержательные зависимости вместо автоматических approval-пауз.
- Проверку физического Canvas ownership с отдельной семантической оценкой.
- SVG/PNG routing и диагностику; предупреждение не заменяет фактический просмотр.
- Контракт реальной UI-проверки recovery, включая доступность управляющих условий при modal.
- Честное различение live preview, run command и срока хранения данных.

## Что остаётся

FAB-08 закрыт только для проверенного контракта имитации и повтора. WF-01 corrective не доказывает будущую чистую генерацию. WF-20: native Obsidian и большие карты не проверены. Реальная непрерывность нового основного чата, creator judgement, HIG/Material/gamification и production auth/sync/payment остаются отдельными границами.

Автономный пакет beta завершён. Далее — оценка полезности bundle и кандидата создателем, затем конкретные оставшиеся риски и исследования. Новый полный прогон ради статистики не нужен.

## Цена и честность evidence

13 completed CLI attempts (10 primary, 3 corrective), plus 1 initial recovery abort by limit. Total input4,199,219, cached3,815,168, output70,621; CLI wall2157.8s. Root orchestration/browser/other chats excluded; these counters are not account percentages.

Map corrective input652164/cached605440/output8435/248.2s, 30.4% above input forecast500000. Recovery corrective input325474/cached289024/output3531/94.3s, 30.2% above forecast250000. Forecasts were not hard token limits. Original full within forecast1.5M/25000. Initial recovery abort17s had no usage; its logs retained.

Full initial runtime beta5/4096c3342f8d8939; map corrective beta7/fcadd1dc3216d714; recovery corrective beta8/27ff6de3cf87a07d. Current beta9/462d4cc828c5d99f adds preview freshness contract, locally checked/installed, no new model run. 36 local regressions PASS and current source/cache parity PASS. One reset performed by creator. Root observer is not an independent third-party audit.

## Где evidence

- [Beta1](2026-10-10-beta1-results.md), [частичный маршрут](2026-10-10-beta2-domain-results.md), [ранний прототип/Plugin/Delivery](2026-10-10-beta3-results.md).
- [Первичная новая модель](2026-10-10-beta4-new-model-initial.md), corrective packet в beta4-new-model/corrective.
- [Первичный full](2026-10-10-beta5-full-initial.md), frozen initial в beta5-full/initial-workspace.
- [Map contract](2026-10-10-beta7-map-corrective-contract.md), packet/PNG в beta5-full/map-corrective.
- [Recovery contract](2026-10-10-beta8-recovery-contract.md); recovery-blocked AX/PNG и restored-reload AX/PNG в beta5-full.

Кандидаты синтетические; исходный FAIL не переписан задним числом. Root SVG-render отличается от native Obsidian, браузерная проверка — от client acceptance.

## Root environment intervention
Reload and a fresh same-origin tab still ran the earlier script/message. Server
served the correct workspace; root revised the script URL only, then actual UI
showed the new one-shot error and retry result. Root also repaired one stale
toggle sentence and attribution in candidate notes. This is recorded separately
from CLI output; not proof of a pristine initial run. Recovery-retained and
recovery-success AX/PNG saved; restored-reload evidence saved beforehand.
