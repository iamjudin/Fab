# Experiment policy
Before run record: decision/hypothesis, claim type, frozen input/target/runtime,
expected differentiating signal, method, maximum model turns/runs and token
estimate, wall stop, end boundary and permitted side effects. Runtime source/cache
must match for installed behavior claims; record version/path/fingerprint.
Local validation before model smoke where it can answer the question. A narrow
upstream fixture tests a transition, not a full natural-input path. End-to-end only
for meaningful seams. One technical PASS doesn't prove generality or user value.

After each model turn record input_tokens, cached_input_tokens, output_tokens,
wall time, interventions and unknown usage. Cached counts are not account-limit
percentages. Forecast is not a hard within-turn cap. Estimate after pilot;
if resume context inflates, stop that method or use an honest focused snapshot.
Pause on budget/window exhaustion; no automatic reset. User controls actual
window resets. Never use a fixed account percentage as universal contract.

Observer receives original input/target/version/events/outputs, not intended
answer or author's interpretation; no edits to the tested object. Independent
agent only with permission. A root self-check isn't independent evidence.
Triage: process defect, contract gap, product unknown, environment/test problem.
For findings record expected→observed, source, scope, confidence, owner, next and
closure criterion. Backlog statuses: verify, next update, deferred(with trigger),
fixed-awaiting-check, closed(with evidence boundary). Reuse an existing finding ID.
Stop on first substantive failure when it defeats the question; don't fix halfway
and call the run clean. Corrective tests separately state intervention.
Full text/logs are not automatically copied into instructions or product memory.
Keep each run's helpers/logs/fixtures in one task-owned directory. Follow
[artifact lifecycle](../../../shared/artifact-lifecycle.md): promote useful
evidence and requested candidates, verify preservation, then remove owned scratch.
Frozen evidence is retained in the project archive, not abandoned in shared temp.
