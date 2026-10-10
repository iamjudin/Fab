# Interactive prototype

Read when an interactive model is selected to test product behaviour before
implementation, usually after structure, critical scenarios and block screens.
Early prototypes and technical spikes remain possible for a specific risk.
If an existing working increment can answer the question, test it rather than
building a duplicate prototype. This stage is not a promise of production readiness.

## Decision and inputs

Name the behaviour or uncertainty being checked, the selected slice, applicable
UC, domain states/rules and current surfaces. Use the accepted structure and
block candidates when available; unresolved scope and policies remain explicit.
For an early prototype, name assumptions and which dependencies are unverified.
Do not invent an account, network dependency, payment policy or platform guarantee.

## Executable candidate

Make the selected paths actually operable: entry, action, feedback, observable
result, safe exit and return where relevant. A static map is not evidence of
interaction. Preserve distinctions between navigation, draft selection, mutation
and confirmed outcome; diagrams and executable behaviour must correspond.

Choose state/data fixtures and failure controls from the question and risk.
A recovery check must be operable from the failed state without discarding the
draft or closing a modal to reach a background-only test control. Use a one-shot
failure or an accessible recovery control when the question requires a retry.
Verify the real UI sequence: failure, retained input, retry, confirmed result.
A harness that changes an inert background toggle does not prove recovery.

Include known alternate/error paths relevant to those checks; report untested
coverage instead of asserting that all corner cases are handled. Domain states
must not be collapsed merely to simplify code. Trace a missing input signal,
an out-of-slice goal, an unresolved policy and a new creator requirement separately.

Keep the review interface functional. Put simulation controls in a compact test
panel and tasks/limitations in the review note. Avoid marketing copy or decorative
work that does not serve the current check. Full visual styling is not required;
legibility, actionable controls and necessary feedback are required.

Inspect the user's observable result as well as stored state. When history is
part of the selected path, show when and what changed with understandable
previous/new values; technical identifiers and whole-record dumps do not by
themselves let the person recover that change.

Exercise the native activation relevant to the surface. For a browser form,
check keyboard submission alongside clicking Save: auxiliary buttons need
explicit types and submission must reach the same validation/save path.
Choose boundary data and viewport from in-scope risks; freely entered text can
break a narrow layout even when ordinary fixtures fit. Preserve meaning and
data when repairing presentation, without inventing domain length limits.
These are checks of selected behaviour, not a requirement to test every input
modality, string or screen size.

## Boundaries and review

Record the entry/run instructions, test conditions, actual versus simulated
operations, persistence lifetime and platform limitations. An imitated save,
notification permission or payment is not proof of real storage, OS behaviour
or purchase recovery. Test a critical technical dependency with a focused spike
before treating dependent behaviour as feasible.

Check the chosen interactions in the actual executable candidate using the
available runtime/UI tools. Code inspection or syntax validation alone does
not prove navigation, rendered state or recovery. When execution is unavailable,
mark those checks unverified and give the creator an actionable way to inspect.
Distinguish structural checks, observed interaction and creator/usability judgement.

Ask the creator to assess the selected behaviour, not to approve the existence of
files. Record the judgement separately from mechanical checks. Preserve current
scope while discussing material additions. No new general agent run is required
merely because a prototype file was added.

## Output and progression

Register the candidate and a short evidence/review note in the product workspace,
linked to its slice, UC and surfaces using the existing manifest/graph mechanism.
Record findings, limitations and unresolved decisions. Update affected UC, rules,
structure and block screens when a correction changes their meaning, retaining
stable IDs. A creator review does not prove technical guarantees.

Proceed when the chosen question has sufficient evidence, findings have a clear
disposition and remaining risks are explicitly assigned to implementation, spike
or later review. Do not wait for every conceivable state, and do not declare the
whole product complete because the prototype worked. Broader completeness rules
remain subject to targeted research and real workflow evidence.

## Coverage basis

When choosing fixtures, failure controls or the sufficiency boundary, read
[slice completeness](../../../shared/methods/slice-completeness.md). Use sparse coverage of
in-scope behaviour and applicable high risks, not a fixed screen-state count.
Fixture data and environment/response toggles differ. Keep a compact coverage/
evidence note linked to existing slice/UC/rules/surfaces, tracking it in the
workspace; reuse existing notes when sufficient, do not introduce a second graph.
An in-scope obligation needs a route to behaviour and an adequate check. Critical
unknowns must be resolved or explicitly block the dependent part before treating
it as ready for implementation. Return a finding to its earliest false assumption.

Classify a lost accepted requirement, known out-of-slice goal, unresolved policy
and newly discovered need separately. New or out-of-slice features do not become
approved because a reviewer noticed them. First-use tests use the
[first-value brief](../../../shared/methods/first-value.md); payment/access tests use
[monetization](../../../shared/methods/monetization.md). Real platform/payment evidence remains
separate from simulated interactions. These rules await a natural workflow check.

## Technical dependency route

Use [technical dependencies](../../../shared/methods/technical-ux-dependencies.md) for actual/simulated operations, persistence lifetime and evidence environment. A failure toggle tests interaction, not the underlying platform guarantee. Keep a compact linked note rather than a second mandatory registry.

## Local run lifetime
When providing a live local preview, confirm the server remains available after
the generating task exits or identify it as a run command, not a live link. A
process inside a short test session may be terminated with that session. Record
actual root/origin/run command; keep server lifecycle separate from product data
persistence. Do not claim reload passed if a dead preview server prevented it.
