---
name: product
description: Define a product model, use cases, rules or a bounded change in an existing product from intent, requirements and evidence. Use for deciding product behavior or a slice, not for research-only, artifact audit or drawing screens.
---
Read [shared core](../../shared/core.md), [decision policy](../../shared/decision-policy.md), and [project contract](../../shared/project-contract.md) for existing/durable work. Choose only relevant references.
# Product
Find new/existing/limited-change and requested stopping outcome. Preserve explicit
requirements/non-goals/authority; accepted input is usable without full discovery.
- New/ambiguous input: [intake](references/startup-gates.md).
- Persistent domain state: [workspace](references/product-workspace.md).
- Human progress: [HJ/JS](references/human-jobs.md); creator progress: [BJ/BS](references/business-jobs.md), only when these decisions are needed.
- Promise/UC/capabilities: [shaping](references/product-shaping.md).
- States/time/error/history/policies: [rules](references/domain-rules.md).
- First/next coherent experience: [slice](references/product-slice.md).
- Before mature output/change propagation: [preflight](references/preflight-review.md).
For a whole new product model, assess both human and creator-side progress using
HJ/JS and BJ/BS contracts even when the creator is also the only user. Same actor
is not proof the axes are identical. If no distinct creator-side transition is
supported, retain Creator Intent and explicitly record that assessment/limit;
don't manufacture a Business Job to fill a quota, or claim HJ replaces the axis.
A bounded feature/UC task needn't manufacture new Jobs or a whole product graph.
Use existing .wireframer state when available; don't rename it to .fab or lose IDs.
For new durable domain state retain its compatible schema while .fab remains an
index. Missing empirical/technical evidence routes conditionally to Research or
Testing/actual spike; simulation is not proof. Methods in shared/methods are read
by active question. Keep intent personal/commercial/client distinct.
For application platform choices that affect behaviour, read
[mobile structure](../../shared/methods/mobile-structure.md). Keep domain intent/
rules separate from platform surfaces; don't make a browser prototype a web target.
Finish requested model/change with sufficient behavior, source coverage, unknowns
and honest acceptance state. Wireframe is a next owner only if interface outcome
was requested or a real dependency within authorized scope. No automatic full run.
