# Fab architecture: implementation boundary
Design v0.2 accepted for bounded autonomous beta implementation on 2026-10-10.
Target owners: cowork, research, product, wireframe, prototype, analysis,
brainstorm, testing, plugin, delivery. Historical beta.1 had five skills:
cowork/research/analysis/brainstorm/testing plus shared core.
All ten skill contracts are now installed in beta.11. Meaning/behavior maturity
is bounded by concrete smoke evidence, not availability. Product/Wireframe use
compatible graph adapter; Prototype/Plugin/Delivery have independent modes.
Cowork maintains collaboration/intent/continuity; direct invocation bypasses it.
Research acquires/synthesizes evidence; analysis evaluates existing material;
brainstorm explores alternatives; testing produces experimental evidence.
Delivery future owner of public release; plugin owns packaging/runtime criteria.
Common Git culture is not a separate skill. No orchestrator/MCP/queue/hidden swarm.

New repo with independent history, package plugins/fab, portable package-root plugin.json.
Old repositories remain untouched source/recovery. Selected reusable knowledge
pairs copied with hashes/limits; project reports/test products excluded.
Mobile-specific expertise/gamification remain research gaps. Landlord excluded.

Shared artifact lifecycle covers task-owned scratch, verified retention and
bounded cleanup. Plugin exports an equivalent self-contained rule to generated
packages; this is a runtime responsibility, not a new mandatory workflow stage.
Beta.10 installed parity/local regression checked; fresh generated-rule behavior
not yet observed (FAB-09).
Beta.11 makes maintainer research labels explicit: `Fab:` filename prefix and
top Fab marker/tag, preserving source titles, body and inclusion history.
Eight existing Brain originals migrated with verified hashes; runtime has no
dependency on those external originals. Fresh ingestion behavior not generalized.

Original rationale: Wireframer docs/fab at checkpoint cb4d220. Those documents
are provenance, not required runtime resources. Working project guidance is here.
