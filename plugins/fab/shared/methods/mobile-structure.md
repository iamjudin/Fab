# Mobile structure and interaction — knowledge brief

Read for mobile surface ownership, navigation, return context, input, lifecycle
or platform boundaries. [Preserved source](mobile-structure.full.json).

## Knowledge and limits

- Separate shared behavior from platform presentation. App context matters when
  it changes the decision. A browser prototype does not make the target a web app.
- Choose structure from the actual scenario, owner, transition and retained context.
  One main context need not have a dashboard or tabs. Top-level places, commands,
  temporary tasks and short blocking decisions have different purposes.
- Collection/object drill-down, stack, modal task or dialog are alternatives whose
  suitability depends on the task. A name or fixed number of levels is not proof.
- Back, Close, Cancel, commit and dismissal have different meaning. Explicitly
  define draft behavior and autosave rather than silently treating Close as Save.
- Preserve ownership, context and applicable failure/recovery paths. Do not add
  fake loading, offline or network states to satisfy a checklist.
- Consider long text, window size, increased text size, focus and relevant keyboard
  behavior. Hit regions, semantics and focus order matter beyond appearance.
  Platform units and numerical thresholds are not interchangeable.
- Preserve semantic intent when moving to another platform, then reassess URL/history,
  input, permissions, responsive layout and accessibility under its actual conditions.

## Application in current Fab

[Navigation and IA](../../skills/wireframe/references/navigation-ia.md),
[table view](../../skills/wireframe/references/table-view.md) and
[prototype](../../skills/prototype/references/interaction-prototype.md) own current
outputs. Mobile focus supplies depth, not a ban on web or a new mandatory stage.
Canvas remains optional. Source-local Canvas or briefing prescriptions in marked
mixed sections and R043 do not override those contracts.

## Deeper reading and freshness

R002–R009 cover structure/returns/input, R010–R021 lifecycle/platform boundaries,
R022–R042 contextual decisions and checks. R043 is historical packet-application
advice. R044–R049 preserve sources. Read the packet's context before adopting detail.

Open current primary iOS/Android/web guidance for the platform decision at issue.
Seven citation bindings are unresolved, with partial primary verification only.
General synthesis is not a uniquely correct IA, exhaustive platform audit or native
proof. Browser evidence cannot establish system gestures, process restoration,
native keyboard, assistive technology, permissions, widgets or hardware behavior.
Revisit a platform change, real-path contradiction or missing decision basis.
