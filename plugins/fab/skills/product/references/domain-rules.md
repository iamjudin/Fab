# Domain Rules Contract

Read this reference when Use Cases have exposed states, time, history,
permissions, destructive actions, persistence or other behavioral rules.

## Purpose

Build a coherent model that can support design, architecture and tests without
turning the creator into a reviewer of technical specifications.

## Internal Work

1. Build a complete compact map of domain areas required by approved Use Cases,
   constraints and routed signals.
2. For each area record current clarity, consequence of error, dependencies,
   evidence status and decision owner.
3. Derive entities, facts, computed states, transitions, temporal rules,
   invariants and failure behavior internally.
4. Route UI projection to IA or Design, empirical uncertainty to research or a
   spike, and implementation mechanics to Technical Strategy.
5. Save the full working specification and graph updates in the product
   workspace and validate them before relying on them downstream.
6. After accepting a policy choice, update its graph node and run the impact
   procedure in `product-workspace.md` before preparing another policy gate.
   Recalculate options against the accepted choice, including cost, privacy,
   reversibility and recovery where relevant. A previously drafted
   recommendation is stale until this check is complete.

## Human Attention Ladder

Classify each result before showing it:

- `Autonomous`: reversible or sufficiently grounded. Decide, record and keep
  moving without approval.
- `Inform`: consequential enough to preserve shared understanding, but no human
  choice is required. Report it briefly without asking for confirmation.
- `Decision gate`: meaningfully changes observable product behavior, creator
  intent, subjective quality, a hard constraint, or an expensive/irreversible
  compromise that cannot be resolved honestly from evidence.

Only a decision gate may stop the process for input. Approval is never proof
that the person read a technical document.

## Visible Sequence

On first entry to the stage, show one compact domain map: area, what must become
clear, current status, risk and whether human input is expected. This is an
orientation surface, not a request to approve every row.

Continue the detailed work under the hood. When a decision gate remains, expose
one independent product fork through:

- a concrete human situation;
- observable behavior of each viable option;
- strengths, weaknesses and downstream consequences;
- the agent's recommendation and grounds;
- one precise question with a short answer format.

If no human-owned decision remains, state the next result and continue
autonomously. After the stage is sufficiently coherent, show a compact final
domain model and links to the full files; require review only for unresolved
product decisions.

Before recommending an option, compare the strongest practicable versions of
each distinct approach against the same situation and criteria. Include a
relevant safeguard that makes an alternative viable, such as explicit human
verification of a canonical transcript or immediate Undo alongside a
time-limited Trash. Do not assign a failure mode to only one option when it
also applies to the other. If a strong alternative is missing, rebuild the
gate before asking the creator. Record remaining empirical uncertainty
without turning it into a preference vote.

## Boundary Checks

- A decision block contains only choices that must be accepted together.
- Independent policies with different consequences or evidence get separate
  decision blocks, even when one Use Case exposed them together.
- Technical uncertainty is not converted into a preference question.
- Domain meaning and visual representation remain distinct.
- Automatic state and explicit human fact remain distinguishable when their
  consequences differ.
- Temporal, correction, cancellation, destructive and recovery paths are
  represented for every critical Use Case.
- Detail remains available for architecture, implementation and auditing even
  when it is not shown in conversation.

## Покрытие поведения и форм

Если возникает вопрос о полноте состояний/форм, прочитай
[coverage brief](../../../shared/methods/slice-completeness.md). Разделяй устойчивый статус,
действие/попытку, исполнение, известный результат и UI; применимые validation
включают формат, доменные ограничения, зависимости полей и сохранность ввода.
Не выдумывай enum или лимит ради checklist. Для платной функции payment attempt
и entitlement различаются по [методу монетизации](../../../shared/methods/monetization.md).
Неизвестная реальная гарантия требует technical evidence, не рисунка ошибки.

## Technical dependency route

For storage, sync or consequential async effects use [technical dependencies](../../../shared/methods/technical-ux-dependencies.md): define the truth boundary of success, cancellation and retry. Unknown outcome differs from confirmed rejection; apply only to relevant operations.
