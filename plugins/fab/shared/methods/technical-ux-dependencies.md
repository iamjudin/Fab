# Technical UX dependencies — knowledge brief

Read when storage, network, sync, external operations or platform capabilities
change a user-visible promise or its evidence boundary.
[Preserved source](technical-ux-dependencies.full.json).

## Knowledge and limits

- Distinguish desired behavior, known technical conditions, an unresolved dependency
  that can change UX and behavior simulated for review. This is not a required phase.
- Record the promise, uncertainty, impact if false, adequate check and simulation
  boundary in an appropriate existing evidence record. Avoid a second mandatory graph.
- Defer implementation choices when plausible options preserve the same observable
  behavior. Material uncertainty needs a bounded promise, evidence or a blocker
  before claiming implementation readiness.
- Draft, durable local state, queued action and remote confirmation are different.
  Reload persistence, backup, device transfer and replica convergence are distinct.
  Sync does not automatically require an account or a particular architecture.
- Map connectivity per operation and preserve independent local work on failure.
  For consequential async effects distinguish pending, rejection, success, unknown
  and relevant partial outcomes. Timeout is not rejection, and closing UI is not
  necessarily cancellation. Retry needs safety evidence or reconciliation.
- OS permissions, notifications, widgets and billing have external lifecycle.
  Select an API after defining behavior. Simulation answers an interaction question,
  while platform documentation and probes answer feasibility questions.
- Choose the cheapest check that can challenge the actual assumption. A device,
  store sandbox, two replicas or server is necessary only for the property at issue.
- Prototype evidence identifies actual/simulated operations, persistence lifetime,
  fixtures, allowed conclusions and open risks. A network toggle must not disable
  unrelated local capabilities merely to manufacture an error state.

## Application in current Fab

[Domain rules](../../skills/product/references/domain-rules.md),
[prototype](../../skills/prototype/references/interaction-prototype.md) and
[realization](../../skills/delivery/references/realisation.md) own promises and
current verification. Update only artifacts affected by new knowledge. R049–R055
contain old process application and an illustrative case, not a prescribed route,
mandatory dependency schema or authority to replace accepted design decisions.

## Deeper reading and freshness

R003–R017 cover distinctions and examples, R018–R034 storage/network and dated
platforms, R035–R042 async truth/error ownership, R043–R048 prototype evidence,
R056–R063 sources. Mixed sections contain local terminology or process choices.

The source reports 23 unresolved bindings. A few async/offline distinctions were
spot-checked, not the entire platform layer. No universal state count, spike for
every feature or device check for every screen is established. Refresh against
primary sources when environment, promise or a probe changes the active decision.
