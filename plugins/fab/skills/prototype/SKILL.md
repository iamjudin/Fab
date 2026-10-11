---
name: prototype
description: Build or revise an executable prototype to check selected interactions from sufficient behavior and interface inputs. Use for functional interaction candidates before production, not static diagrams or claims of native platform readiness.
---
Read [shared core](../../shared/core.md), [decision policy](../../shared/decision-policy.md), and [project contract](../../shared/project-contract.md) for existing/durable work. Read only active references.
# Prototype
Read [interactive prototype contract](references/interaction-prototype.md).
Select question, applicable UC/rules/surfaces and minimum executable paths.
Existing inputs count; early prototypes can have explicit assumptions. Don't
reconstruct a whole product or style the app as a marketing landing.
Implement relevant validation, error/cancel/recovery and data lifetime honestly.
Keep simulation controls compact and separate from product UI. An actual saved
state, UI feedback and simulated OS/billing are different claims.
Inspect chosen interactions with actual available UI/runtime tools; code/syntax
can't substitute. If UI unavailable produce usable candidate/run instructions
and report unverified interaction; don't invent an observation. Use project
registry at ../product/scripts/product_workspace.py when it already applies.
For mobile candidates read [mobile structure](../../shared/methods/mobile-structure.md):
test selected viewport/input/return paths and distinguish browser observations
from native keyboard, gestures, system Back and lifecycle evidence.
Propagate changed behavior to Product/flows; stable IDs and scope persist.
Stop at requested interactive check. Production delivery is a different owner.
