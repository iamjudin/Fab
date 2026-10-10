# Product Workspace

Use an isolated product workspace when pursuing a new product is authorized and the
product begins producing mature graph entities. The conversation coordinates
decisions; files preserve, validate and expose the evolving product system.

## Boundary

Methodology/plugin sources and product artifacts belong to different
workspaces. Resolve the product location before the first persistent product
artifact. Use a path supplied by the person or an existing product repository.
An already isolated, writable task directory dedicated to this product can be
the root. If no safe root exists, propose one sensible isolated location and
make location the only operational choice; do not mix it into the current
product review. Never write product artifacts into the Fab plugin
repository.

Initialize after sufficient authorized intent, before Human Jobs and Business
Jobs become mature review artifacts. Do not create a workspace for an unsolicited idea the
person has not asked to pursue. Partial tasks can reuse existing state.

Before the first mature review, check the full transition:

1. `project.json` records the approved creator intent, input flexibility,
   explicit boundaries and active stage; `signals.json` holds the meaningful
   source signals with stable IDs and honest dispositions.
2. `graph.json` holds the current typed candidate entities and their links.
   Do not invent a graph node merely to make a signal look represented; use
   `routed`, `deferred` or `open-gap` when the entity is not mature yet.
3. The current review has a stable Markdown file under `product/reviews/`.
   Track a new file and run `product_workspace.py validate <product-root>`.
4. Only then show the concise review and file link. If any check fails, repair
   the workspace before asking the person to approve the candidate.

## Minimal State

Maintain these logical objects; use JSON/YAML for machine state and Markdown
for human review when files are available:

- `project`: identity, creator intent, input flexibility and active stage;
- `signals`: stable `SIG-XX` source signals, authority, evidence status and
  disposition;
- `graph`: typed nodes, causal links, approval state and impact markers;
- `reviews`: complete current candidates with stable entity IDs;
- `evidence`: research and validation results linked to claims;
- `journal`: decisions, corrections, learning and recompilation events.

A compact default layout is:

```text
.wireframer/
  project.json
  signals.json
  graph.json
product/
  reviews/
  evidence/
  journal.md
```

Create only the directories and files needed by the current maturity. Avoid
placing speculative artifacts in the repository merely to satisfy the layout.

For the first Human Jobs review, the minimal machine shapes are:

`signals.json`:
```json
{"schemaVersion":1,"signals":[{"id":"SIG-01","meaning":"One source claim","authority":"direction","knowledgeStatus":"evidence","disposition":{"kind":"represented","refs":["HJ-01"]}}]}
```

`graph.json` (new workspaces use schema 2):
```json
{"schemaVersion":2,"nodes":[{"id":"HJ-01","type":"human-job","meaning":"One human transition from A to B","status":"assumption","links":[]},{"id":"JS-01.1","type":"job-story","meaning":"One context and desired human progress","status":"assumption","links":["HJ-01"]}]}
```

Keep the generated `schemaVersion` wrappers. The `authority` and `meaning` of
one signal are scalar; split different claims into separate `SIG-XX` entries.
For graph schema 2, every mature node has a canonical `meaning` and `status`;
add `classification` when the stage makes such a distinction. Every
`product-capability` node in schema 2 must have a non-empty `classification`
for its current priority role (`core`, `supporting`, `later`, etc.); the first
slice is recorded separately in scope and links. A Markdown priority without
this graph field is an incomplete candidate, even when all IDs and links pass.
Older schema 1 graphs remain readable; update their nodes before relying on
semantic parity in a new review. An ID and its links alone cannot represent
the meaning of the Markdown candidate.
`represented` requires exact existing graph IDs. Use `routed`, `deferred` or
`open-gap` when the corresponding entity is not mature. Put approved creator
intent, input flexibility and explicit boundaries in `project.json` alongside
the generated slug, language and active stage. Run the documented commands
below; inspect the script only when a command or schema example is insufficient.

Write every mature review object to a stable Markdown file such as
`product/reviews/human-jobs.md`, then show a concise decision-oriented summary
and a file link. A file being available does not make it mandatory reading:
technical specifications can remain agent-owned while the visible review
contains only consequences and decisions that belong to the person.

Navigation / IA first produces one structure overview `.canvas` with surface
IDs and control-to-destination relationships in `product/reviews/`, plus a
compact rationale/access table. After structure acceptance, add only needed
critical scenario maps using the same S-IDs. Keep full behaviour in sources,
not overview cards. Track each Canvas and validate JSON and vault-relative
file links with `product_workspace.py validate-canvas`; inspect visual
scanability independently. Meaning: `navigation-ia.md`, `critical-scenarios.md` and `block-screens.md`.
File/render instructions: `canvas-adapter.md`.

Keep product evidence inside the product workspace. A source becomes a
candidate for a shared Fab knowledge base only when it has been
synthesized beyond the immediate decision and carries provenance, date,
applicability, freshness risk and limitations. The shared base may inform later
research routes, but it does not replace current project evidence or silently
validate a claim.

When filesystem access is available, initialize the structure with:

```bash
python3 <skill-directory>/scripts/product_workspace.py init <product-root> --slug <slug>
```

After creating a new artifact file, register it for safe experiment cleanup:

```bash
python3 <skill-directory>/scripts/product_workspace.py track <product-root> <artifact-path> [...]
```

Run `validate <product-root>` before treating persisted graph state as ready for
review. The validator checks stable IDs, exact links, story parentage and signal
dispositions. For schema 2 it also rejects graph nodes without a canonical
meaning or status. It cannot establish that free-form Markdown means the same
thing: the Review Compiler must compare each visible entity's ID, meaning,
status and applicable classification to the graph before showing it.

For an explicitly disposable experiment, cleanup is available only when the
workspace identity and slug match:

```bash
python3 <skill-directory>/scripts/product_workspace.py clean <product-root> --slug <slug>
```

Cleanup removes only files registered in `.wireframer/workspace.json` and then
removes empty directories created for that workspace, including a newly created
empty container directory. It preserves untracked product files, keeps any
non-empty parent and refuses an identity mismatch. Ask for confirmation
immediately before cleanup when the person has not already explicitly requested
it.

## Update Semantics

- Markdown review files are the person's editing surface; machine state keeps
  IDs and relationships stable.
- A correction updates the graph first and regenerates the complete affected
  review object.
- After accepting a significant decision, update its graph node and run
  `python3 <skill-directory>/scripts/product_workspace.py impact <product-root> <changed-id>`.
  The read-only command lists nodes that link to the changed ID,
  directly or through other nodes, with the dependency path. Treat the list as
  candidates for recompilation, not as proof that their meaning changed.
- Inspect pending recommendations in the same domain even if the report is
  empty. A missing causal link is a graph defect: add it when one decision
  changes another's costs, risks or feasible behavior. For each affected
  candidate, record whether assumptions, alternatives, recommendation,
  evidence or review status changed. Recompile changed review objects and
  leave unresolved consequences open before presenting the next gate.
- Record the accepted decision and material propagation in the product
  journal; validate the workspace after updating graph and reviews.
- Git checkpoints capture approved decision boundaries and validated product
  increments, not every conversational draft.
