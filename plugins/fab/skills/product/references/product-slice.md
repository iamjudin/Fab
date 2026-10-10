# Product Slice

Read when prioritization has made the first end-to-end experience the nearest
decision. This is a product/value gate, even when a technical spike is needed
before building it.

## Stage Contract

- `Decision object`: one smallest coherent experience from the triggering
  situation to an observable result that tests a material product assumption.
- `Agent responsibility`: reconstruct the intended value loop from approved
  Human/Business Jobs, Product Core, Use Cases, rules, capabilities and explicit
  success signals; compare viable slice options and route separate technical
  unknowns to an appropriately sized spike.
- `Human contribution`: judge whether the proposed result is the progress the
  creator wants the first release to demonstrate and choose any consequential
  trade-off in product direction or cost.
- `Sufficiency`: the path, included/excluded behavior, observable result, main
  uncertainty, evidence plan and relation to the approved success signal are
  explicit. Critical negative and recovery branches are represented or their
  omission is justified.
- `Review question`: is this the right first experience and learning target?
- `Action contract`: apply shared decision policy; a new consequential slice
  choice belongs to the creator, an already chosen slice needs no repeated approval.

## Choose The Uncertainty Before The Option

Classify the questions that could change the slice:

- `product/value`: will the experience create the promised progress;
- `behavior`: will people actually enter, return to or complete the loop;
- `usability`: can they understand and perform it;
- `technical`: can the critical mechanism work in the intended conditions.

Name the **main uncertainty for this release**, with evidence for its priority
and the cost of being wrong. Do not silently promote the hardest implementation
problem to the product goal. A technical risk may be tested by a spike before
the slice while the slice itself still tests the value loop.

## Compare Slice Options

For each serious option, briefly trace:

1. Entry situation and linked HJ/JS/BJ/BS.
2. End-to-end steps and required capabilities/rules, including correction or
   recovery that is essential to the promise.
3. Observable result for the person and for the creator's current aim.
4. Which uncertainty it tests, by what observation, and what it leaves unknown.
5. Match or mismatch with every **explicitly approved** success signal. Do not
   invent a metric in the startup frame. If no signal was approved, derive a
   candidate from the current jobs and label it for this decision.
6. Cost, dependencies and what is deliberately deferred, preserving any hard
   input constraints.

Reject an attractive technical demonstration that never reaches the promised
human result. If a characteristic entry mechanism is risky, compare a slice
that carries it through to the later useful result with a cheaper value test,
and say which learning each buys. Keep `Product Core` importance distinct from
the membership of this first slice.

Before review, reverse-trace the chosen result to the original success signal
and the main uncertainty. State what observation would change the next
decision. An artifact that only proves a subsystem works is a spike, not a
product slice, unless the approved product goal itself is that subsystem.

## Coverage и первый результат

При проверке состава/готовности выбранного среза используй
[полноту среза](../../../shared/methods/slice-completeness.md): in/out/unresolved отличимы
от priority и ведут к поведению/проверке. Не заводи второй обязательный реестр.
Если первая ценность зависит от entry/setup/account/данных, используй
[первый вход](../../../shared/methods/first-value.md): success signal — реальный outcome,
не завершение onboarding или demo. Платный доступ требует отдельного выбора
[монетизации](../../../shared/methods/monetization.md), не подразумевается названием подписки.

## Technical dependency route

For a promise affected by technical uncertainty use [technical dependencies](../../../shared/methods/technical-ux-dependencies.md). Link promise, unknown, UX impact, check and simulation boundary in existing evidence. Bound or block a dependent guarantee before implementation readiness; a candidate with an explicit unknown may still be reviewed.
