# Active-dialogue continuation correction

The creator reports an ordinary-use dead end: a scope rejection receives a correct
acknowledgment but leaves the active project without a concrete continuation.
The supplied screenshot and relevant conversation corroborate the reply. This
extends FAB-11, with FAB-14/WF-17 context, not a new missing named method.

## Diagnosis and intervention

Existing shared rules already require continuation and useful next-step reasoning.
The observed response corrects scope but does not return to the remaining goal or
expose its pending choice. Treating the last message as the complete task is a
working interpretation of the reply, not access to internal model reasoning.

The actual programme had a proposed, unaccepted age range. Continuing should not
mean inventing acceptance or commissioning research. A specific scope question
could move the dialogue while preserving the creator's decision.

Canonical core now operationalizes ending an active turn: reconnect feedback to
goal, completed/remaining work and authority, perform the authorized next action
or advance the discussion, and expose a real blocking choice concretely. A scope
rejection preserves unaffected work. Completed small/social exchanges may finish
naturally. Brainstorm's progressive dialogue reference follows the same boundary.
No mandatory state artifact, question template, pipeline or extra permission ritual.

## Bounded checks

| Case | Target and observed result | Judgment |
|---|---|---|
| Fresh blocked-choice baseline | Shipped-identical beta.26 asks about the unaccepted age range after scope correction | PASS, original native failure not reproduced |
| Same-input blocked-choice candidate | Asks the specific age question and explains its effect on coverage | Bounded PASS, not proof of superiority |
| Authorized work after rejected expansion | Candidate actually delivers both requested assignment drafts in chat, with research unexecuted | Bounded PASS, continuation is action rather than a promise |
| Thanks after completion | Candidate replies only “You're welcome!” | Bounded PASS, no forced plan or question |

All four actual runtime turns are GPT-6.1 Sol/Medium, fresh read-only CLI contexts.
Execution traces show the frozen source core was read. The active case additionally
reads Research and its references. The Brainstorm reference is inspected structurally,
not independently invoked in a fresh Brainstorm model case.

Baseline:72files/772681e0da09331f, exact installed-beta.26 correspondence.
Candidate:72files/fe44274906582314, same manifest version, unreleased source only.
Only shared/core.md and Brainstorm references/dialogue.md differ. Fifty existing
regressions, package references and source diff checks pass.

## Cost, limitations and next

Four model turns,294,363input/234,496cached/2,635output tokens,135.29seconds
excluding root overhead. Within the4turn/350,000input forecast. No reset/purchase,
subagent, external research, source-project mutation/message or installed update.

The real failure is preserved separately from synthetic successes. Contexts are
focused fixtures with explicit authority, not a full replay of the native long
conversation. The original model/effort is unknown. Root judgment is unblinded,
with no independent evaluation. Comparative improvement and long-context stability
remain unproved. Candidate control success does not close the ordinary-use defect.

The correction is ready for a limited release decision. Next observe an actual
post-feedback project turn, checking useful continuation and preservation of scope,
including a genuine blocking choice. Keep completion controls naturally complete.
Installed/public beta.26 remains immutable until separately authorized promotion.

## Retention

[Inputs](inputs.json), [contract](contract.md), [usage](usage.json), frozen answers
and metadata under behavior/ retain the check. Ignored raw contains command events,
real-case provenance, baseline/candidate source snapshots and cleanup proof.
Full candidate fixture matched retained hashes. Baseline matched installed cache.
Owned scratch removed after verified preservation. The runner needs a restored
fixture and a new owned-workspace record before reuse.
