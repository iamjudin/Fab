# Critical scenarios

Read after sufficient structure under shared decision policy when steps, states, branches or returns need
inspection. Use [structure/access](navigation-ia.md) and current slice/UC/rules;
use the [Canvas adapter](canvas-adapter.md) for file and visual checks.

## Second decision: critical scenarios

After sufficient structure under shared decision policy, map only the scenarios whose steps, branches,
temporal rules, unusual entries or risk need inspection. Reuse S-IDs and
place details in a distinct area of the same canvas, or link them from the
overview when the project needs separate canvases. Trace entry, actions, meaningful states,
observable result, safe exit and later return. Make Back, Close, Cancel and
Undo distinct where their semantics affect the path. If a scenario needs a
new surface or opening relationship, revise the structure and expose the
material change for review rather than silently adding a screen.

For an unavailable dependency, show what remains usable without false success.
An unknown recovery stays open with the required technical evidence; never
invent a successful retry or restoration. A diagram approval is not evidence
of storage integrity or user usability.

Second review question: can the known critical scenarios be understood from
entry to result and return, with unresolved branches named separately?
When this decision is sufficient and further layout is authorized, create low-detail block screens using Design Kernel as a
criterion; ask for judgement of a perceivable candidate, not its wording alone.


Continue to [block screens](block-screens.md) for visible composition, then
[interactive prototype](../../prototype/references/interaction-prototype.md) for selected executable checks.

## Выбор проверяемых веток

Используй [полноту среза](../../../shared/methods/slice-completeness.md), когда выбираешь
применимые state/data/failure classes: разреженное покрытие по риску, без
фиксированного набора или всех сочетаний. Открытое существенное правило
возвращается в domain model, а не чинится случайным экраном. Для первого
входа/позднего возврата применяй [first value](../../../shared/methods/first-value.md),
для purchase/access — [monetization](../../../shared/methods/monetization.md).

## Technical dependency route

For applicable network, lifecycle or external-operation risks use [technical dependencies](../../../shared/methods/technical-ux-dependencies.md). Preserve unknown/partial outcomes, truthful cancellation and safe recovery; independent local functions remain available. Do not add every branch to every scenario.
