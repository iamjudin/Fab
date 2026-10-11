---
name: wireframe
description: Design or revise interface structure, navigation, critical flows and low-detail block screens from sufficient product behavior or existing artifacts. Use for visible interface organization, not new product discovery or executable prototypes.
---
Read [shared core](../../shared/core.md), [decision policy](../../shared/decision-policy.md), and [project contract](../../shared/project-contract.md) for existing/durable work. Choose only relevant references.
# Wireframe
Accept sufficient current requirements/UC/slice or an existing interface. Missing
behavior returns only the dependent question to Product; no mandatory full Jobs.
Choose the requested mode: [structure/access](references/navigation-ia.md),
[critical scenarios](references/critical-scenarios.md), or
[block screens](references/block-screens.md). Semantic dependencies remain;
existing accepted inputs count. Read [Canvas adapter](references/canvas-adapter.md)
only when producing/checking Canvas. Stable S-IDs, actual control ownership,
composition vs navigation and return context must survive all projections.
In partial repairs preserve existing interactions compatible with the UC/rules.
Absence of a control's exact name in the domain model is not a contradiction or
permission to delete its mechanism. Separate a genuine behavior conflict from
an underspecified interface detail; expose a material experience change before
dependent edits, rather than simplifying it away to make projections agree.
Small projects use one Canvas with separated areas; split by domain only when
readability actually requires it. Grey information, light blue local interaction,
blue navigation, green persistent mutation. These are diagram notation, not UI styling.
Use familiar terms (modal sheet/navigation stack/tab bar). Proposed scope additions
remain distinct. Creation/editing initial settings are checked together.
For mobile application structure/input read [mobile structure](../../shared/methods/mobile-structure.md).
Use the selected platform branch without prescribing tabs/dashboard or replacing
the domain model; future web navigation/input gets its own platform assessment.
Preflight semantics before geometry; JSON/preview/native Obsidian are distinct.
When producing or revising a Canvas structure overview, run
scripts/check_structure.py <canvas>
--surface-id <S-ID> for each included surface before progressing. Each declared
surface is a real group; separate control rows physically belong inside it.
A separate app/global tab bar can own controls in a group whose ID starts with
global-navigation; keep one meaningful owner per actor context, not duplicated
inside every screen. Repeated collection/item nesting still needs semantic preflight. Labels like
S-01/card aren't containment; a flat flow can be valid for scenarios but not this
structure projection. Repair physical ownership failures autonomously; don't
call the structure ready or drop arrows to silence the guard.
Use ../product/scripts/product_workspace.py for registry/validate-canvas with
actual vault root; scripts/canvas_preview.py for fallback. Layout warnings are
not repaired by deleting required edges or hiding content. Renderer geometry is
still a known limitation; don't claim WF-20 closed by copying it.
Deliver requested visible candidate and gaps. A prototype is separately requested
executable work, not the automatic reward for a completed map.
