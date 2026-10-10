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
Small projects use one Canvas with separated areas; split by domain only when
readability actually requires it. Grey information, light blue local interaction,
blue navigation, green persistent mutation. These are diagram notation, not UI styling.
Use familiar terms (modal sheet/navigation stack/tab bar). Proposed scope additions
remain distinct. Creation/editing initial settings are checked together.
Preflight semantics before geometry; JSON/preview/native Obsidian are distinct.
Use ../product/scripts/product_workspace.py for registry/validate-canvas with
actual vault root; scripts/canvas_preview.py for fallback. Layout warnings are
not repaired by deleting required edges or hiding content. Renderer geometry is
still a known limitation; don't claim WF-20 closed by copying it.
Deliver requested visible candidate and gaps. A prototype is separately requested
executable work, not the automatic reward for a completed map.
