# Business Jobs And Business Stories

Read this reference when the creator-side value of the product is the nearest
decision, when commercial or operational intent matters, or before Product Core
is assembled from Human Jobs and Business Jobs.


Указанные review question/action contract применяются при реальном decision
gate; уже принятое решение не требует повторного approval. Сохраняй отдельные
типы и фокус каждой оси, выбирая глубину по активному решению.

## Purpose

The stage separates progress expected from the product as a creator's venture
from human progress expected by a person using it.

`Business Job` is the source-of-truth entity: a meaningful transition from a
current creator, business or operating situation A to a preferred situation B.
It remains meaningful when a particular feature, integration or implementation
is removed.

`Business Story` is a derived contextual view. One Business Job can produce
several Business Stories when different situations imply meaningfully different
product obligations or decisions.

Assess this axis for every product. A personal utility can still need to become
a dependable, maintainable or useful learning instrument. Keep the map as small
as the evidence allows; do not invent a commercial strategy merely to fill it.

## Stage Contract

- `Decision object`: a coherent map of Business Jobs and Business Stories for
  the current product scope.
- `Agent responsibility`: reconstruct creator-side progress, separate it from
  intent, metrics, constraints and implementation, attach evidence status and
  expose implications for product viability.
- `Human contribution`: explain the desired result of creating, operating,
  integrating, learning from or commercializing the product and judge whether
  the proposed transitions reflect that aim.
- `Sufficiency`: every material creator-side expectation is linked to a BJ/BS,
  routed to its proper entity type or exposed as a gap; selected jobs remain
  solution-independent and useful for Product Core. For each selected BJ,
  at least one BS or explicitly routed creator-side process describes a path
  to an observable instance of its preferred situation B. If the current scope
  only prepares for that result, mark the BJ as preparatory or leave the
  completion gap open instead of presenting enabling work as completion.
- `Review question`: do these Business Jobs and contextual stories correctly
  describe what the product must enable as a creator's venture?
- `Action contract`: apply the shared decision policy; no automatic hierarchy
  approval if work/choice already authorized. Both value axes may inform one
  coherent decision without merging their types.

## Entity Boundaries

| Entity | Meaning |
| --- | --- |
| Creator Intent | Why the creator starts or continues the project now. |
| Business Job | Meaningful creator-side progress from A to B. |
| Business Story | Contextual view derived from one Business Job. |
| Business Outcome / Metric | Evidence that the job is being performed well. |
| Constraint / Rule | A required, allowed or forbidden property of the product. |
| Capability / Feature | A mechanism that helps perform a Human Job or Business Job. |
| Technical Strategy / Implementation | How the product is built or operated. |
| Business Process / Use Case | A concrete sequence involving this product or organization. |

Route statements by meaning:

- `earn enough to sustain development` can express progress; a revenue target
  is its outcome;
- `complete a real paid distribution loop` can express progress; App Store,
  StoreKit and a paywall are possible channel, capability and implementation;
- `remain operable by one person` can express progress; no server or no complex
  integrations are possible constraints or strategies;
- compliance, privacy and integration obligations remain rules or constraints
  unless they reveal a distinct creator-side transition;
- a desire to test the entire product-making process can be a Business Job even
  when revenue is secondary.

Human Jobs are not functionality. Business Jobs are not implementation. Both
are reasons for downstream product behavior.

## Working Method

1. Start from confirmed Creator Intent, input signals and evidence. Identify
   what must become possible or different for the creator because the product
   exists.
2. Reconstruct candidate transitions across only the lenses relevant to the
   context: commercial, operational, integration/ecosystem, trust/compliance or
   learning/experiment.
3. Test each candidate:
   - are situations A and B distinguishable;
   - can different means achieve the progress;
   - does it remain meaningful without a named feature or technology;
   - does it affect whether the product can exist, operate, integrate, learn or
     sustain itself;
   - is it distinct from a creator motive, target metric or constraint.
4. Derive Business Stories only for contexts that change downstream product
   decisions. A fixed channel may appear in context when the input makes it a
   real boundary, but it does not become the job itself.
5. Attach evidence or mark `Assumption`. Do not infer market demand from the
   creator's preference.
6. Build an internal coverage register for every material creator-side signal:
   linked BJ/BS, outcome, rule/constraint, capability, technical strategy,
   future process/use case or open gap.
7. Reverse-check each selected BJ from its preferred situation B: identify
   the story or routed process that can actually reach it, the observable
   completion signal and what current evidence supports. Research, pricing,
   channel setup and release preparation may enable a commercial job, but do
   not by themselves complete a stated publish-and-sell outcome. Do not force
   a sale into a personal or experimental job whose desired result is learning
   or dependable use.
8. Calibrate the strength of the claim to the signal. A first transaction
   shows that one paid path worked and gives initial willingness-to-pay
   evidence; it does not establish repeatable demand or business viability.
   Keep the stronger claim open until proportionate evidence exists.

## Review Presentation

Show the parent job first and its stories directly beneath it:

```text
BJ-01 - <meaningful creator-side progress>
Status: Assumption | Evidence

  BS-01.1 - <first context title>
  Когда...
  Я хочу...
  Чтобы...

  BS-01.2 - <another context of BJ-01>
  Когда...
  Я хочу...
  Чтобы...
```

Use `BJ-01`, `BJ-02` for Business Jobs and `BS-01.1`, `BS-01.2` for their
derived stories. Each story has exactly one parent Business Job.

Example boundary:

```text
BJ-01 - превратить полезный личный инструмент в продукт, способный пройти
реальный цикл платного распространения

  BS-01.1 - когда первая коммерческая версия готова к выпуску...
  BS-01.2 - когда покупатель восстанавливает приобретение...
```

The job is the paid product transition. Distribution channel, payment API,
receipt handling and restore behavior remain downstream context, capabilities,
rules and implementation.

A focused BJ review contains that hierarchy; a combined decision may show both value axes. Do not prioritize a Human
Job as `core` or `later` because its current capability looks expensive; job
importance and implementation sequence are different decisions.

After any correction, regenerate the complete current hierarchy before showing the current decision; approval only for a substantive choice.

## Платная ценность

Когда intent или BJ действительно требуют выручки/оплаты, используй
[метод монетизации](../../../shared/methods/monetization.md). Объясни paying actor, платный
результат, модель и cost-to-serve; trial/freemium не обязательны. Для личного
продукта не открывай коммерческий цикл без нового сигнала. Исследование
поддерживает выбор, но не выбирает тарифы и не доказывает спрос.
