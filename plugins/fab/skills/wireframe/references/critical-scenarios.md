# Critical scenarios

Read when enough behavior/access is known to inspect steps, states, branches
or returns. Existing accepted requirements/artifacts may suffice without a new
structure document. Use relevant [structure/access](navigation-ia.md) and current slice/UC/rules;
use [scenario tables](table-view.md) by default. Only for explicitly requested
experimental Canvas use the [Canvas adapter](canvas-adapter.md). For screen-flow
maps read [screen flows](screen-flow.md): SC may stand alone; MOD needs actual
functional reuse; NAV is optional, not a prerequisite to every scenario.

## Second decision: critical scenarios

After sufficient structure under shared decision policy, map only the scenarios whose steps, branches,
temporal rules, unusual entries or risk need inspection. Reuse S-IDs and
link scenario rows to any existing useful overview by IDs. In opt-in Canvas,
choose sufficient areas/maps, without manufacturing an overview. Trace entry, actions, meaningful states,
observable result, safe exit and later return. Make Back, Close, Cancel and
Undo distinct where their semantics affect the path. If a scenario needs a
new surface or opening relationship, revise the structure and expose the
material change for review rather than silently adding a screen.

Preserve source owners and each actual caller's retained context. A selector
returns its selection; a separate next task owns downstream conditions. A shared
definition does not turn cancellation into successful continuation. Distinguish
a nested entity's commit from cancelling its parent task, using actual product
rules rather than an assumed global persistence policy.

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
