---
name: wireframe
description: Design or revise interface structure, navigation, critical flows and low-detail block screens from sufficient product behavior or existing artifacts. Use for visible interface organization, not new product discovery or executable prototypes.
---
Read [shared core](../../shared/core.md), [decision policy](../../shared/decision-policy.md), and [project contract](../../shared/project-contract.md) for existing/durable work. Choose only relevant references.
For a public promotional/offer landing-page task, read
[landing pages](../../shared/landing-pages.md). Apply this route to the
active object, not an app entry screen called landing or the whole project.
For visible interface composition/wording, read
[shared principles](../../shared/interface-principles.md). Browser presentation uses
[web layout](../../shared/web-layout.md); public-page meaning uses
[website content](../../shared/web-content.md). Native mobile behavior keeps its
existing mobile-structure route; a browser prototype does not change its target.

# Wireframe
For requested creation, evolution or review of reusable interface definitions
or their Figma/code relationship, read [design-system work](../../shared/design-system-work.md).
This conditional route does not turn an ordinary interface edit into a library task.

Accept sufficient current requirements/UC/slice or an existing interface. Missing
behavior returns only the dependent question to Product; no mandatory full Jobs.
Choose the requested mode: [structure/access](references/navigation-ia.md),
[critical scenarios](references/critical-scenarios.md), or
[block screens](references/block-screens.md). Semantic dependencies remain;
existing accepted inputs count. Default structure/scenario representation is
[Markdown tables](references/table-view.md); preserve owners, IDs and all relevant
branches. This fallback does not replace perceivable block screens or executable
prototypes. Canvas is opt-in experimental while readability is unresolved.
For explicitly requested Canvas or screen-flow maps, read
[screen flows](references/screen-flow.md) before choosing overview versus detail.
Match the creator's intended visual review and any accepted reference format;
check representation coverage before declaring the requested map set complete.
For a linked set, apply its local-orientation/return-composition contract and
inspect the actual paths, not only START, counts or overlap warnings.
One scenario may suffice; modules need actual functional reuse, and NAV is
optional when an architectural overview helps. These are not mandatory layers.
Read [Canvas adapter](references/canvas-adapter.md)
only when producing/checking Canvas. Stable S-IDs, actual control ownership,
composition vs navigation and return context must survive all projections.
In partial repairs preserve existing interactions compatible with the UC/rules.
Absence of a control's exact name in the domain model is not a contradiction or
permission to delete its mechanism. Separate a genuine behavior conflict from
an underspecified interface detail; expose a material experience change before
dependent edits, rather than simplifying it away to make projections agree.
For explicit Canvas work choose the smallest useful representation from meaning
and readability, not product size or a document quota. Screen-flow semantic types
use the screen-flow palette; physical composition/control overviews use the
separate notation in navigation-ia. Neither palette is application UI styling.
Use familiar terms (modal sheet/navigation stack/tab bar). Proposed scope additions
remain distinct. Creation/editing initial settings are checked together.
For mobile application structure/input read [mobile structure](../../shared/methods/mobile-structure.md).
Use the selected platform branch without prescribing tabs/dashboard or replacing
the domain model; future web navigation/input gets its own platform assessment.
Preflight semantics before geometry; JSON/preview/native Obsidian are distinct.
For temporary renders read [artifact lifecycle](../../shared/artifact-lifecycle.md).
A limit on final deliverables is not a reason to park previews in shared temp:
contain them in a task-owned directory, retain useful evidence and clean the
disposable preview when observation ends.
Only when producing or revising a physical-containment Canvas overview, run
scripts/check_structure.py <canvas>
--surface-id <S-ID> for each included surface before progressing. Each declared
surface is a real group; separate control rows physically belong inside it.
A separate app/global tab bar can own controls in a group whose ID starts with
global-navigation; keep one meaningful owner per actor context, not duplicated
inside every screen. Repeated collection/item nesting still needs semantic preflight. Labels like
S-01/card aren't containment; a flat flow can be valid for scenarios but not this
structure projection. A NAV relation map or screen flow needs no fake containment
groups and does not claim that guard's PASS. Repair physical ownership failures autonomously; don't
call the structure ready or drop arrows to silence the guard.
Use ../product/scripts/product_workspace.py for registry/validate-canvas with
actual vault root; scripts/canvas_preview.py for fallback. Layout warnings are
not repaired by deleting required edges or hiding content. Renderer geometry is
still a known limitation; don't claim WF-20 closed by copying it.
Deliver requested visible candidate and gaps. A prototype is separately requested
executable work, not the automatic reward for a completed map.
