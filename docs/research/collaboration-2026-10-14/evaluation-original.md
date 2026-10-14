# Evaluating sustained human–AI collaboration

Date: 2026-10-14. Method: bounded primary-source web review, not a Deep Research
provider output, independent experiment or systematic literature census.
Source records and limitations: [source ledger](sources.json).

## Answer and evidence boundary

Evaluate evolving work and its outcome alongside individual answers. A clean
snapshot can establish a narrow capability without exposing loss of commitments
across a conversation. A synthetic failure can reveal a mechanism without measuring
human usefulness. Use both deliberately, rather than deriving a universal quality
claim from either.

This is an author-designed evaluation approach informed by publications. It has
not itself been validated across long-running creator projects. No reviewed paper
establishes a universal minimum number of turns, trials or release threshold.

Navigation: [Context methods](#what-the-context-method-measures),
[Outcomes](#outcomes-judges-and-human-value),
[Diagnosis](#passing-baselines-and-causal-diagnosis),
[Protocol](#economical-protocol-and-release-decisions), [Sources](#sources).

## What the context method measures

The 2025 Lost-in-Conversation study distributes static tasks across simulated
turns. It reports weaker reliability and premature assumptions. Its narrow simulator
reveals information until the task becomes sufficient, so it is not representative
of all human interaction. Do not transfer its performance drop to an untested model.
[Laban and colleagues](https://arxiv.org/html/2505.06120v1).

A 2026 preprint adds disclosure, revision and task switching while retaining an
original final verifier. Its principal setup uses six transitions. Memory recaps
helped selected tests but did not eliminate the gap. Synthetic intent transitions
still omit substantial variation in real user behavior.
[Tack and colleagues](https://arxiv.org/html/2607.20734v1).

| Evaluation context | Best question answered | Main blind spot |
|---|---|---|
| Fresh state snapshot | Can the system act with sufficient current input? | How that state was acquired or lost |
| Historical transcript supplied at once | Does inherited context distort a response? | Live tools, memory updates and actual sequence |
| Sequential resumed dialogue | Does behavior survive disclosure, correction and stage changes? | Synthetic users and controlled environment |
| Read-only ordinary-use observation | Where does actual work fail or help? | Confounded causes and weak comparability |
| Controlled human task comparison | Does the intervention improve a chosen human outcome? | Cost and limited transfer across contexts |

The table is a methodological synthesis, not a ranking. Select context for the
uncertainty. A stage or decision is often the smallest useful outcome unit. A
response diagnoses a local error, a session tests cumulative effects, and a
longitudinal study tests recurring value. No single unit subsumes the others.

## Outcomes, judges and human value

The original τ-bench verifies simulated customer-service outcomes against database
state and distinguishes repeat reliability from finding one successful attempt.
Its simulated users and airline/retail policies do not establish real satisfaction
or a general knowledge-work benchmark.
[τ-bench](https://arxiv.org/html/2406.12045v1).

MT-Bench examines conversational grading and reports position, verbosity and
capability-related judge limitations. It does not establish that an arbitrary
model judge can measure long-project value. Its self-preference evidence is
explicitly limited, so do not assert a universal judge self-favoring effect.
[Zheng and colleagues](https://arxiv.org/html/2306.05685v4).

An industry protocol separates traces from resulting state, combines different
graders and recommends balanced trigger/non-trigger tasks. These are practitioner
recommendations, not an independent causal study of the protocol.
[Anthropic's evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

| Dimension | Appropriate evidence | Insufficient substitute |
|---|---|---|
| Accepted meaning preserved | Artifact/state checks and relevant history | Polite agreement |
| Useful contribution | Specific new distinction or consequence, contextual review | Word/idea counts |
| Actual execution | Observed tool result or resulting artifact/state | A future-work promise |
| Appropriate initiative | Goal, scope and authority at that point | Always acting or always asking |
| Human usefulness/agency | Actual experience and observed work | A simulated user's praise |
| Evidence honesty | Claim-to-support correspondence | Long source lists |

Use rule checks for deterministic properties, calibrated judgment for open quality,
and human observation for experienced value. In comparisons blind version labels,
swap answer order where relevant and retain disagreements or unknowns. These
controls are a proposed evaluation design, not a guaranteed bias removal technique.

Comparator choice changes the claim. A human–AI meta-analysis distinguishes
augmentation over humans alone from synergy over the better standalone performer.
For assistance products both can matter, alongside costs and agency.
[Vaccaro and colleagues](https://www.nature.com/articles/s41562-024-02024-1.pdf).

## Passing baselines and causal diagnosis

A real failure followed by a passing focused baseline has not been reproduced.
Possible explanations include simplified context, explicit cues, different runtime,
sampling and a criterion that missed the original defect. The correct conclusion
is limited fixture sensitivity, not demonstrated repair or a harmless original miss.
This is methodological reasoning, not an empirical result from this review.

An illustrative case, with no invented data:

1. Ordinary work ends with acknowledged scope feedback but no usable continuation.
2. A fresh fixture supplies current state explicitly and both versions continue.
3. A sequential reconstruction includes the earlier proposal, rejection and remaining
   goal. Evaluate accepted scope and next action at each affected point.
4. If a failure appears, introduce one identified correction, retain the original
   run and assess the corrective separately. Use an unseen related situation.

Separate tracking from acting: a system can state the current intention and still
perform the wrong action. Useful diagnostic controls compare unchanged history,
an explicit correct-state reminder and the actual resulting behavior. A supplied
reminder can bypass a tracking problem and does not prove autonomous recovery.
The distinction is informed by the [2026 evolving-intent analysis](https://arxiv.org/html/2607.20734v1),
but this proposed control has not been run for another system here.

## Economical protocol and release decisions

The following is a **proposed small-team protocol**, not a prescribed new harness:

1. State the decision, failure signature, current permission and forbidden effects.
2. Freeze package, input/history, actual runtime, environment and criterion. Retain
   accepted constraints without including the evaluator's desired answer.
3. Check deterministic causes first. Choose the smallest contextual comparison
   capable of distinguishing the remaining explanations.
4. Include a matching non-trigger control and an unexposed related situation.
   Inspect both outcome and trace, with original failures kept alongside corrections.
5. Count unresolved cases and disagreement separately. Repeated trials can test
   variation, but one best attempt does not establish reliability.
6. Report input/output/cached tokens, wall time and human effort when measured.
   Use actual pilot cost to bound continuation. Unmeasured costs stay unknown.
7. Stop once the question is answered, on substantive defeat of the hypothesis,
   budget/access exhaustion or repetition without signal. Release only claims
   supported on the actual distribution/runtime surface.

For a reversible narrow improvement, bounded regressions can support a limited
release with monitoring and a rollback path. Repeated ordinary work and eventual
human comparison are needed for claims about sustained usefulness. There is no
evidence-based universal test quota in the reviewed material.

Rollback/escalation signals are loss of accepted meaning, unagreed consequential
action, false completion or repeated human effort to restore the task. Thresholds
are local decisions. A source-only pass does not establish installed behavior, and
infrastructure errors should remain separate from behavioral defects.

## Sources

Context dynamics: Laban and Tack, linked above.
Outcomes/reliability: τ-bench and Vaccaro, linked above.
Judging/practice: Zheng and Anthropic, linked above.
Detailed source design/access records: [sources.json](sources.json).
