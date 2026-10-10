# Human Jobs And Job Stories

Read this reference when Human Jobs are the nearest product decision: after the
startup frame is accepted, when raw input must be reconstructed into human
progress, or when existing jobs/stories need review.


Указанные review question/action contract применяются при реальном decision
gate; уже принятое решение не требует повторного approval. Сохраняй отдельные
типы и фокус каждой оси, выбирая глубину по активному решению.

## Purpose

The stage separates human progress from its contexts and from downstream
product behavior. It uses JTBD ideas as decision tools, not as a ritual or a
claim that one school owns the final definition.

Use the bundled [JTBD brief](../../../shared/methods/jtbd.md) for research provenance and the
conditional routes into detailed school/evidence/abstraction material. The
maintained stage contract below defines Wireframer policy; source-school examples
do not override it. No external Brain note is required.

`Human Job` is the source-of-truth entity: a meaningful transition from a human
situation A to a preferred situation B that remains meaningful when the
considered product is removed.

`Job Story` is a derived contextual view used for product and design review.
One Human Job can produce several Job Stories when different situations imply
meaningfully different product behavior.

## Stage Contract

- `Decision object`: a coherent map of Human Jobs and the Job Stories derived
  from them for the current product scope.
- `Agent responsibility`: classify the input, reconstruct candidate progress,
  test abstraction boundaries, separate entity types, attach evidence status,
  organize contextual stories and expose real uncertainty.
- `Human contribution`: provide personal episodes or known domain meaning and
  judge whether the proposed progress and contexts reflect reality. The agent
  chooses the analysis method.
- `Sufficiency`: key jobs and stories are solution-independent and useful for
  the current decision; contexts and outcomes are separate; evidence and
  hypotheses are distinguishable; every significant input signal is linked to
  the hierarchy, routed to its proper entity type or exposed as a gap.
- `Review question`: do these Human Jobs and their contextual stories correctly
  describe the human progress the product should serve?
- `Action contract`: apply the shared decision policy; review a real human-owned
  choice, otherwise continue the requested outcome. HJ/BJ/Core can form one
  coherent model; their types remain distinct.

## Entity Boundaries

| Entity | Meaning |
| --- | --- |
| Human Job | Meaningful solution-independent human progress from A to B. |
| Context | Circumstances and causal event that make the job relevant. |
| Outcome | Criterion by which the person judges execution quality. |
| Evidence | Real episode, observation or source. Without it, the job remains a hypothesis. |
| Alternative | Another way to make the same progress, including manual action or non-consumption. |
| Forces | Push, Pull, Anxiety and Inertia when choice, adoption or switching matters. |
| Job Step / Related Job | Hierarchy used when the distinction changes product boundaries or scenarios. |
| Job Story | Solution-independent contextual view derived from one Human Job; it describes when the progress becomes relevant, not how this product performs it. |
| Use Case / Task | Interaction with a particular product or system. |
| Rule / Constraint | Required, allowed or forbidden system behavior. |
| Capability / Feature | A mechanism through which a product can serve a job, scenario or requirement. |

Route statements by meaning, not syntax:

- a system obligation belongs to a rule or constraint;
- interaction with a concrete product belongs to a use case or task;
- a mechanism or implementation belongs to a capability or feature;
- `faster`, `simpler`, `more accurately` and similar criteria are usually
  outcomes;
- a pain or struggle is evidence of an unresolved situation and a trigger for
  discovering progress, not automatically a job;
- contractual and regulatory requirements may create rules or capabilities
  without a fabricated Human Job.

## Working Method

1. Atomize the relevant input and distinguish evidence, interpretation,
   requirement, solution, rule and assumption.
2. Reconstruct candidate human transitions at more than one abstraction level
   when the useful boundary is unclear.
3. Test each candidate:
   - does it retain meaning without this product, interface or technology;
   - are situations A and B distinguishable;
   - is it human progress rather than an outcome, operation or mechanism;
   - can substantially different alternatives perform it;
   - is its level useful for the next product decision.
4. Split or merge candidates by causal context, preferred state, alternatives,
   success criteria and independence of the decision episode. Explain uncertain
   boundaries instead of pretending they are natural law. A shared topic is not
   enough to merge two transitions: if their desired states, success criteria
   or decision episodes differ, create separate parent jobs and attach each
   story to the matching parent.
5. Attach evidence or mark `Assumption`. For a personal product, the creator's
   real episode is evidence about that creator, not evidence of market scale.
6. Derive Job Stories for the contexts that change downstream product behavior.
   Test every story independently: it expresses a causal situation and desired
   human progress without requiring an operation in the considered product.
   Opening, clicking and viewing belong to Use Cases; notifications and other
   ways of helping belong to capabilities. Keep speed, effort, accuracy and
   similar quality criteria as outcomes rather than hiding them inside the job
   identity.
7. Route negative situations correctly. Error, forgetting, cancellation, later
   return or recovery become a separate Human Job only when they create an
   independent meaningful transition; otherwise they are a context, use-case
   branch, state or rule.
8. Build an internal coverage register for the complete relevant input. For
   every significant signal record one disposition: linked HJ/JS, evidence,
   outcome, rule/constraint, Business Job/Story, future Use Case/capability, or
   open question. Resolve accidental omissions before review and expose
   intentional gaps. A fixed count is not a completeness criterion.

Alternatives and switching forces are especially useful for adoption, purchase,
replacement and market questions. They are optional when they do not improve
the current decision. Emotional and social meaning should be investigated when
relevant and supported by evidence; it is not mandatory sentence decoration.

## Review Presentation

Show the parent job first and its stories directly beneath it:

```text
HJ-01 - <meaningful solution-independent progress>
Status: Assumption | Evidence

  JS-01.1 - <first context title>
  Когда...
  Я хочу...
  Чтобы...

  JS-01.2 - <another context of HJ-01>
  Когда...
  Я хочу...
  Чтобы...
```

Use `HJ-01`, `HJ-02` for Human Jobs and `JS-01.1`, `JS-01.2` for their derived
stories. A story must link to exactly one parent Human Job. Preserve additional
evidence, outcomes, forces and boundary notes in the product graph, but show
them in the review only when they affect the person's current judgment.

A focused HJ review contains the Human Job hierarchy; a combined model may show both axes when one real decision is being made. Use Cases, rules,
capabilities, prioritization and product slice may inform an internal coherence
check but retain their separate semantic types and decision focus.

When the person corrects any part, regenerate the complete current hierarchy
and present that self-contained version; ask only if a real decision remains. A delta may explain what
changed, but it is not the review object.
