# Six Thinking Hats and optional Brainstorm strategies for Fab

Date: 2026-10-13. Status: research and proposal; no runtime change or accepted method selection.

## Decision and research boundary

Should Fab Brainstorm use Six Thinking Hats, and how can it help without imposing
a workshop on every request? The creator confirms repetitive ideas, premature
convergence and weak dialogue/critique. Precise causes are not yet established
from concrete failing examples. This review compares the installed
contract, earlier bounded outputs, original method descriptions and limited
empirical work. It stops at an actionable design choice and a validation proposal.
It is not a systematic literature review, a new behavioral experiment or ingestion
of a supplied third-party report.

## Current implementation and diagnostic hypothesis

[Brainstorm](../../../plugins/fab/skills/brainstorm/SKILL.md) already calls for
divergence, critical examination or convergence, distinct alternatives, grounded
tradeoffs and a recommendation. It protects evidence and acceptance boundaries.
It gives little operational guidance on choosing and switching techniques.

Earlier [idea output](../../../experiments/workflow-tests/partial-routes-20261012/ideas/final.md)
offers five distinct approaches and recommends one; its follow-up narrows to two
manual variants while preserving constraints. These bounded successes do not
establish that ordinary brainstorming feels useful to the creator.

Working hypothesis: selection of thinking strategy and timing of convergence
are under-specified. This could explain a repetitive options list or premature
recommendation, but source inspection does not prove the reported root cause.
Do not replace all Brainstorm behavior on that assumption.

## What the original method contributes

The author's [one-page description](https://www.debono.com/_files/ugd/acf405_0ec0d7f959d7424fad5a9f9e9ec581e7.pdf)
separates six directions:

| Direction | Question it helps address |
| --- | --- |
| White | What is known, missing or needs verification? |
| Red | What reactions or intuitions do people express? |
| Yellow | Where could this create value, and why? |
| Black | What justified difficulties could prevent success? |
| Green | What other possibilities could we create? |
| Blue | What question, sequence and conclusion does this discussion need? |

The same source supports individual use, shared directions in groups and
sequences suited to different situations. It does not prescribe one universal
six-section answer.

The [De Bono Group explanation](https://www.debonogroup.com/services/core-programs/lateral-thinking/parallel-thinking/)
presents cooperative exploration through successive modes, rather than opposing
positions trying to defeat each other. For Fab, the useful mechanism is changing
the question being explored. Assigning fixed personalities to six imaginary
experts is our rejected adaptation, not a requirement of the original method.

These sources describe and promote the method. Their benefit claims are not
independent evidence that it improves Fab or every creative task.

## Evidence for effectiveness and transfer limits

A [2022 study abstract/highlights](https://doi.org/10.1016/j.tsc.2022.101185)
reports more ideas under green/yellow than red instructions in individual tasks,
and more unique ideas for green-red than red-red dyads. Only the publisher's
search-visible abstract/highlights were accessible; a direct page open returned
403. Full methods and effect sizes were not reviewed. These comparisons do not
establish superiority of a full six-hat session over Fab's current behavior.

The [PTFA paper, version 2](https://arxiv.org/html/2503.12499v2) studies an LLM
facilitator with 48 participants in 16 three-person groups and 32 short discussions
about activities and films. It records useful suggestions and perspective prompts,
but mixed ratings and poorly timed interventions. The facilitator sometimes kept
requesting ideas after participants were converging or had agreed, and sometimes
added emotional interpretation where it was unhelpful. This supports a concrete
timing concern, not proof that a one-creator Fab chat will behave the same way.

Research takeaway: method plausibility justifies a bounded candidate comparison.
Evidence reviewed here does not justify a claim of proven superior creativity,
independent expert consensus or six roles guaranteeing comprehensive coverage.

## Complementary strategies

[Stanford d.school's How Might We tool](https://dschool.stanford.edu/tools/how-might-we-questions)
uses reframing questions to provoke meaningful, relevant ideas, including looking
at an opposite or an extreme. This provides a generation tactic when an existing
framing yields only small variations. For Fab, translate the move into a natural
question; do not force an HMW worksheet or copy its materials into the MIT package.

[Design Council's framework](https://www.designcouncil.org.uk/resources/framework-for-innovation/)
distinguishes opening exploration from focusing action. This is a useful phase
distinction, not a concrete idea-generation technique and not authorization for
a mandatory Discover-to-Deliver pipeline.

Fab-specific assumption reversal is another candidate tactic: identify a movable
assumption, explore a counterfactual and compare the resulting mechanism. It must
preserve accepted constraints; it is proposed here, without an effectiveness claim.

## Integration options

| Option | Benefit | Cost or limitation | Recommendation |
| --- | --- | --- | --- |
| Always output six hats | Predictable visible structure | Padding, duplicates and premature evaluation on simple tasks | Reject as default |
| Separate Six Hats skill | Easy explicit invocation and a full workshop contract | Another entry point; does not repair strategy selection in Brainstorm | Consider only if repeated standalone demand appears |
| Optional methods inside Brainstorm | Matches the actual question; preserves a natural conversation | Requires clear selection, switching and stopping behavior | Preferred candidate |

The preferred design has three conversation modes: open possibilities, examine an
idea and compare options. Techniques serve those modes; they are not mandatory
stages. Six Hats is one technique, reframing is another. A short ordinary response
remains sufficient when it answers the question.

## Proposed behavior for the preferred candidate

1. Identify the decision/question and whether the creator is exploring, examining
   or choosing. Do not require a form when context is sufficient.
2. Select the smallest helpful strategy. If the conversation is stuck, offer a
   specific perspective switch with a reason, rather than a menu of all methods.
3. For exploration, use reframing or green-hat-style generation. Hold ranking
   until the requested alternatives exist; preserve hard constraints throughout.
4. For examining an idea, separate evidence, value and failure mechanisms. Use
   other perspectives only when they add something. A grounded own judgment
   remains part of collaboration; hats must not produce artificial balance.
5. For comparison, name the deciding tradeoff and recommendation with confidence
   and a useful next check. Do not silently convert a preference into acceptance.
6. On an explicit Six Hats request, offer a visible, tailored sequence. A full
   pass can include all six; the ending should explain what changed in the choice.
   Proposed sequences here are Fab adaptations, not quoted official curricula.
7. Stop when new modes add only repetition or the requested decision is sufficiently
   supported. Respect an accepted conclusion; reopen it only for relevant new
   evidence, a creator request or an exposed material contradiction.

No extra agents are needed for these modes. Multiple roles produced by one model
do not provide independent corroboration. White-hat factual claims retain Fab's
normal source-verification requirements. Red-hat work may reflect expressed
creator reactions or label possible audience reactions as hypotheses; it must
not invent the creator's feelings or simulate feelings as evidence.

## Example adaptation, not a tested output

Question: how can an indie creator resume a project after a week away?

Start by opening alternatives: a retained next action, a replayable decision trail,
or a small re-entry task. Reframe: what if returning required no advance note?
That could produce a different mechanism based on the recent artifact, not a
renaming of the same reminder. Next examine value and failure: saved intent may
help, but the cost of leaving notes could prevent use. A useful synthesis asks
which obstacle is real and proposes a small comparison; it need not print hat
names. This is an illustrative design, not empirical evidence of improvement.

## Validation proposal and stop

After creator feedback and acceptance of a candidate, compare unchanged beta.23
with the candidate on four matched short inputs: open ideation, critique of an
appealing idea, comparison with a real tradeoff, and a follow-up after a preferred
direction has been selected. Include an explicit full-hat request as a separate
format check if that surface is promised.

Assess distinct mechanisms, constraint preservation, factual/assumption separation,
useful judgment, attention cost and whether follow-up develops the conversation
instead of reopening it. Keep initial failures and corrections. Record actual
model, effort, isolation and outcome; do not treat longer answers or number of
hats as quality. No runs have been authorized or executed as part of this research.
The creator's comparative judgment of usefulness is distinct from technical checks.

## Recommendation and open choice

Improve Brainstorm through an optional strategy selector and operational guidance;
include a bounded Six Hats adaptation rather than replacing the skill with a
six-column report. The creator confirms all three pains: repetitive ideas,
premature convergence and weak dialogue. Prioritize conversation-state behavior
and strategy selection together, rather than only a Six Hats format. A bounded
comparison should cover all three. Runtime edits, installation, release and a
standalone skill remain unaccepted.

## Sources and review scope

- [Edward de Bono: Six Thinking Hats overview](https://www.debono.com/_files/ugd/acf405_0ec0d7f959d7424fad5a9f9e9ec581e7.pdf) — original method roles and usage notes; extracted one-page text reviewed.
- [De Bono Group: Parallel Thinking](https://www.debonogroup.com/services/core-programs/lateral-thinking/parallel-thinking/) — method framing; practitioner/promotional evidence.
- [De Bono Group: Six Thinking Hats](https://www.debonogroup.com/services/core-programs/six-thinking-hats/) — corroborating description; promotional outcome claims not adopted.
- [Do De Bono's green hat and green-red combination increase creativity?](https://doi.org/10.1016/j.tsc.2022.101185) — publisher abstract/highlights only; full text not reviewed.
- [PTFA: LLM facilitation through parallel thinking, v2](https://arxiv.org/html/2503.12499v2) — full HTML, especially study/results/discussion; external validity limited.
- [Stanford d.school: How Might We Questions](https://dschool.stanford.edu/tools/how-might-we-questions) — first-party tool description; worksheet not reproduced.
- [Design Council: Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/) — first-party divergence/convergence framing.

Accessed 2026-10-13. This document is Fab's authored synthesis, not a preserved
copy of the linked works or a licensed training course. The indexed packet
preserves this synthesis; it does not imply that source full texts were archived.
