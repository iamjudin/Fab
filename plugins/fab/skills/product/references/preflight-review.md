# Review Compiler

Read this reference with the [interaction contract](../../../shared/decision-policy.md)
before presenting a mature candidate or re-presenting it after correction.

## Purpose

The Review Compiler turns source material and the approved product graph into
one reviewable decision for the active stage. Its result is a complete,
traceable and clean candidate that asks the person for one kind of judgment.

This is an internal compilation pass, not a visible questionnaire.

## Internal Model

### 1. Source Signal Register

Normalize every significant piece of input before relying on it downstream.
Each signal has:

- a stable `SIG-XX` identifier and concise meaning;
- source and authority inherited from Input Flexibility;
- knowledge status: `Evidence`, `Assumption` or `Decision`;
- current disposition: represented by exact graph IDs, routed to a later entity
  type, deferred with a reason and review trigger, or exposed as an open gap;
- affected stages when that disposition changes.

The register preserves meaning, not wording. Several source fragments may map
to one signal, and one signal may legitimately affect several graph nodes.
Before assigning one disposition to a signal, test whether every claim inside
it has the same authority, knowledge status and route. Split a composite signal
into separate stable `SIG-XX` entries when one clause is represented and
another is only a candidate mechanism, rule or open question. A structurally
valid JSON object does not establish semantic atomicity.

Before the first persisted mature review, compare the incoming source with the
register and project context, not just the generated signals with the graph.
Check explicit non-goals and exclusions as well as positive aims. A commissioned
product does not by itself preserve “not launching my own SaaS”. Preserve that
distinction with its original scope/authority; do not infer a hard constraint
from every negation. On later supplied input, check the new source delta too.
If the source is unavailable, state the coverage limit rather than certifying
complete capture from the register alone. This is an internal check, not another
approval gate or mandatory duplicate source database.

Before assigning or preserving a non-default authority, compare it with the
actual source statement or a specific creator decision. Current behaviour and
a reported episode can be evidence without being a constraint. Broad acceptance
of a startup summary does not silently upgrade every detail to a hard requirement.
Apply the distinction in [startup authority](startup-gates.md) even when correcting
an existing workspace after its frame was accepted. If an unsupported upgrade
is found, restore the inherited authority, preserve the factual signal and
check affected frame wording/routes. Keep explicit constraints intact and do
not reopen the whole frame when this corrects the agent's interpretation only.
Knowledge status and authority answer different questions; inspect both.

### 2. Active Stage Contract

Compile the current stage into a decision boundary:

- `Decision object`: the one connected product decision being formed now;
- `Required upstream`: approved or explicitly unresolved graph nodes needed for
  that decision;
- `Relevant signals`: source signals that this decision must represent or
  route;
- `Output types`: entities this stage is entitled to create or update;
- `Sufficiency`: the minimum state that makes the candidate honest;
- `Interaction disposition`: continue autonomously, briefly inform, or open a
  decision gate according to the human attention ladder;
- `Review question`: for a decision gate only, the one judgment the person can
  make about it;
- `Action contract`: what the person does now or what the agent does next and
  what follows.

The candidate expresses the active decision. Consequences and discoveries that
belong to another layer remain linked open decisions or routed signals until
their own decision boundary is active.

For structure, apply [ownership/access](../../wireframe/references/navigation-ia.md); after acceptance,
apply [critical scenarios](../../wireframe/references/critical-scenarios.md) and [block screens](../../wireframe/references/block-screens.md).
File/render checks use [Canvas adapter](../../wireframe/references/canvas-adapter.md). Keep semantic checks
and actual application opening distinct. For interaction, apply the
[prototype contract](../../prototype/references/interaction-prototype.md), preserving scope and simulated
versus actual outcomes.

### 3. Product Graph

Every mature entity has a stable ID, type, status and causal links. Validate:

- parent-child integrity such as `HJ -> JS` and `BJ -> BS`;
- exact upstream links where a causal relationship is claimed;
- source-signal disposition and authority propagation;
- unique IDs and absence of dangling references;
- downstream impact markers when an upstream decision changes;
- for a changed upstream decision, the `product_workspace.py impact` report
  and a semantic check of same-domain recommendations that lack a graph link;
- preservation of temporal, negative, correction, cancellation and recovery
  paths across the layers where they matter.

The graph is not an ID-only index. In schema 2, record the canonical meaning
of every mature node, its status and any classification that changes the
decision (`core`, `critical supporting`, `later`, etc.). Before a human review,
compare **each visible entity** with its graph node in both directions: ID,
meaning, status, classification, parent and current scope. Also check for a
graph entity in the active decision that disappeared from Markdown, and for a
visible entity absent from the graph. Repair both from one current decision;
do not approve a Markdown candidate whose graph says something else. A passing
JSON validator only proves that fields and links are shaped correctly, not
that two free-form statements have the same meaning.

For Product Capabilities, compare the visible `core` / `supporting` / `later`
priority of **each** CAP with its graph `classification`. The workspace
validator requires that field but cannot tell whether it matches the Markdown
decision. Keep membership in the first Product Slice as a separate scope
choice; `core` alone does not mean first slice.

Before re-presenting a candidate after a significant accepted decision, use
the impact report to identify linked dependents. Re-evaluate their actual
trade-offs against the new decision, and repair missing causal links found in
the same domain. When a rule or slice introduces a new user goal, update the UC review as well
as the graph before using it in capabilities, structure or scenarios. Compare
the complete set of in-scope UC IDs and their meaning with the current Markdown
review; remove stale exclusions. Record accepted membership separately from
working policy details. Merely adding a graph node is incomplete propagation.

A report with no dependents is not evidence that the decision
has no consequences. Do not carry an earlier recommendation into a new gate
until its assumptions and material costs have been checked again.

### 4. Visible Output

When interaction is needed, the visible result is one self-contained current
version. It uses the selected language, contains no drafting residue and ends
with one action contract. A decision gate has one review question; an
informational update does not simulate one. After a correction, compile the
whole object again rather than emitting a patch that depends on earlier
messages.

Before sending, inspect every visible question or numbered list for an implied
request to answer now. Keep only questions that belong to the active decision
in its action contract. Keep future-stage unknowns in the workspace when they
do not help the current review; if a brief mention matters, label it as open
for a named later stage and say explicitly that no answer is needed now. The
next stage turns those unknowns into its own candidate and decision gate.

## Two-Pass Compilation

### Builder Pass

1. Select the active stage contract from the approved graph and uncertainty
   map.
2. Build the candidate from relevant upstream nodes, source signals and
   evidence.
3. Record every new node, link, routing decision and unresolved gap.

### Critic Pass

Start from the source register and upstream graph, independently of the
builder's prose:

1. Reconstruct what the active decision must cover.
2. Compare that reconstruction with the candidate's entities and links.
3. Classify each mismatch as a mechanical defect, missing evidence, unresolved
   product decision or legitimate routing to another layer.
4. Check the rendered response as a user-visible artifact.

For the startup frame, compare every proposed question with the original input:
mark it already answered, unresolved for this decision, or useful only at a
later stage. Ask only the second kind; count independent requested decisions
again after wording the response.

For Human Jobs, reverse-map each meaningful input signal to an exact HJ/JS,
another typed entity, or an explicit gap. Then test each parent job for one
human transition. If its stories require different preferred states, success
criteria or decision episodes, split it before review. Do not mark a signal
`represented` merely because a broad title sounds related.

For Business Jobs, reverse-map each selected BJ from its desired creator-side
result to a BS or routed process with an observable completion signal. Mark
preparation as preparation, and keep a viability claim open when evidence only
shows an initial milestone such as one sale.

For Use Cases, type-check the compact map before detailing flows: one actor
goal and primary completion signal per UC, alternatives sharing that goal,
negative paths with honest stop or recovery signals, and exact
JS/BS links justified by the scenario's result. Route standalone outcomes,
capabilities, rules and technical checks to their own layers. For Domain Rules,
test decision blocks for independent choices and compare strong, current
alternatives symmetrically before a human gate.

For Product Capabilities, apply the independent-result check in
`product-shaping.md` before review: a complete end-to-end Use Case may require
several separately testable capabilities. Keep their links; do not merge them
into one CAP to make the review shorter.

Use an independent critic or subagent when authorised, available and proportionate. When it
is unavailable, perform the same reverse trace explicitly; rereading the draft
from top to bottom is not an independent pass.

## Compile Result

- Mechanical omissions, broken links, type errors and presentation defects are
  repaired and the compiler runs again.
- A substantive gap resolvable from current evidence is resolved and linked.
- An empirical unknown is sent to the Research Router.
- A decision that belongs to the person is surfaced inside the active review
  only when it changes that decision; otherwise it remains routed.
- The candidate receives `READY_AUTONOMOUS`, `READY_TO_INFORM` or
  `READY_FOR_REVIEW` only when stage sufficiency, graph integrity, signal
  disposition and any required visible-output integrity all hold.

Keep compiler mechanics internal unless an unresolved gap changes the review or
the next action.

## Feedback Notation

Когда отдаешь список для ревью, добавляй простой способ пометок:

```text
Пиши рядом с номером или в поле "Твоя пометка":

- ok - оставить;
- no - убрать;
- rewrite - переписать;
- merge with HJ-XX / JS-XX.X - объединить на соответствующем уровне;
- split - разделить;
- core - похоже на ядро продукта;
- later - важно, но не для первого среза;
- personal - особенно похоже на твой сценарий;
- market - скорее рыночный сценарий, не твой.

Все Human Jobs и Job Stories без указанного evidence пока имеют статус
Assumption.
```

## Selected-slice coverage

For a candidate that relies on a selected slice and its downstream behaviour,
use [slice completeness](../../../shared/methods/slice-completeness.md) when coverage is the
active uncertainty. Check in/out/unresolved, source-to-behaviour-and-check trace
and representative relevant risks. Keep the scope of each stage distinct; do
not repeat a giant checklist during startup or every jobs review. Findings get
their actual class and evidence/disposition; new needs are not silently imported
into the accepted slice. This is a semantic pass, not proof from schema alone.
