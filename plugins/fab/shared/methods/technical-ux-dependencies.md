# Technical dependencies of product behaviour

Read when storage, sync, network, permissions, background work, widgets or
external operations may change a product promise; also when defining prototype
simulation and handoff evidence. This is a conditional method, not a new phase.
Source: «Технические зависимости продуктового поведения до реализации».
[Detailed source packet](technical-ux-dependencies.full.json).

## Operational method

- Separate desired behaviour, known platform conditions, a dependency whose
  answer can change UX, and behaviour simulated for interaction review.
- Record a material dependency against existing UC/rules/slice: promise →
  unknown → UX impact if false → adequate check → simulation boundary. Reuse
  an existing evidence note; no mandatory second graph or new entity type.
  Keep status, environment/date and recheck trigger when applicable.
- Defer implementation choices when plausible alternatives preserve the same
  observable contract. An uncertainty that changes that contract needs evidence,
  a bounded promise or explicit blocking disposition before implementation
  readiness. Candidate scenarios may show that unresolved dependency honestly.
- Define the truth boundary of Saved/Sent/Paid: draft, durable local state,
  queued operation and remote confirmation are different facts. Local save
  need not wait for sync if that is the agreed contract.
- Distinguish reload/restart persistence, backup, device transfer and replica
  convergence. Sync does not itself require a visible account or a particular
  stack. Map network dependencies per operation; preserve independent local
  work when remote operations fail.
- For consequential async effects distinguish pending, confirmed rejection,
  confirmed success and unknown result; include partial success when relevant.
  Timeout does not establish rejection. Retry needs known safety or reconciliation;
  closing the UI does not establish cancellation of the effect.
- Notifications, widgets, permissions and purchases involve OS/store surfaces
  and lifecycle. Define required behaviour before selecting an API. Fresh primary
  documentation and an appropriate probe address platform feasibility; simulated
  UI only addresses the interaction question.
- Choose the cheapest evidence capable of challenging the specific assumption.
  Physical devices, two replicas, store sandbox or a real service are required
  only when that property cannot be established in the cheaper environment.
- Prototype evidence states actual/simulated operations, persistence lifetime,
  controllable fixtures and failures, allowed conclusions and unresolved risks.
  Applicable error scope is action → feature → screen → app; do not make a
  network toggle disable unrelated local capabilities.
- New evidence updates UC if prerequisites/sequence/outcome change, rules if
  truth changes, scenarios if states change, slice if its promise cannot hold,
  and prototype notes if real/simulated boundaries change.

## Limits and deeper reading

This is methodological synthesis, not proof of plugin behaviour. Source reports
23 unresolved citation bindings; preserved links and section hashes do not
repair them. Platform snapshots and API/version claims are not runtime rules:
verify primary evidence when a consequential decision depends on them, and at
handoff/release where relevant. AWS timeout/retry and Android local/network
source distinctions were spot-checked; no exhaustive platform/legal audit.
No universal state count, mandatory spike per feature, device test for every
mobile screen, or requirement to select an architecture during discovery.

- R003–R017: distinction, spike/defer decision and dependency examples.
- R018–R034: persistence, identity/network and dated platform conditions.
- R035–R042: async truth, retry/cancellation, partial results and error ownership.
- R043–R048: prototype evidence and choice of environment.
- R049–R055: propagation, handoff and sufficient readiness.
- R056–R063: source attribution and its limitations.

Refresh when the implementation environment changes, a probe contradicts the
promise, source conditions change or the brief cannot resolve the active risk.
