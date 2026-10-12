# Scoped readiness and isolated work

A packaged/installed version is an identity, not proof that every output works.
Separate package integrity, each promised outcome's behavioral evidence, and
experimental surfaces. A failure blocks its dependent promise; preserve useful
independent outcomes. Never average failures into a whole-product PASS.

Before release/install after changes, record exact version and package fingerprint,
promised surfaces, default/opt-in availability, required checks, evidence and known
limits. Unknown is not pass. A default surface with a failed required check cannot
ship as ready: fix it, replace it with a checked sufficient representation, or
explicitly exclude it from the promise and default routes. Mark the replacement's
own evidence; it does not close the original defect. Beta permits bounded/limited
outcomes with disclosed limits. Stable claims require passing checks for their
actual scope, not a claim of universal maturity. Opt-in experiments remain named
experiments, never silently enabled to satisfy a default route.

When work introduces an independent outcome, substantial redesign or uncertain
implementation beyond a released checkpoint, proactively recommend isolation:
explain the scope, current baseline, benefit/risk and proposed branch before
dependent work. For routine bounded repairs do not demand a new branch or chat.
Respect existing authorization. Preserve the release tag; work in a codex/ branch
under project conventions. Branch alone isolates history, not concurrent files:
independent simultaneous chats need separate checkouts/worktrees. A chat is a
coordination choice, not a release boundary. Never install an experimental branch
into shared default runtime, merge, publish or change another workstream's scope
without authorization. Record owner, branch/checkout, allowed files, acceptance
checks and return condition in the owning project's existing documents.

Delivery owns release scope and promotion; Plugin owns package/runtime evidence.
For a machine-checked plan use [release mode](../skills/delivery/references/release.md).
The check verifies declared evidence and eligibility, not the truth of an assertion;
run actual relevant tests and review outputs. A new version invalidates old package
identity; affected behavior needs fresh evidence or an explicit unverified status.
Generated plugins/products inherit this policy in self-contained runtime guidance,
adapted to their surfaces; a link back to Fab is not sufficient.
