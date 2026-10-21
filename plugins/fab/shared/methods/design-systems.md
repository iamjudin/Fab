# Design systems — knowledge brief

Read when repeated UI needs, themes or divergence between design and code make
reuse valuable. [Preserved source](design-systems.full.json).

## Knowledge and limits

- Distinguish tokens, components, composed patterns and product extensions.
  Semantic tokens connect values to intended use, including themes.
- Define relevant component anatomy, behavior, states and accessibility alongside
  appearance. Variants alone do not describe a usable component.
- Preserve meaning between design and code, including focus, errors and disabled
  states where applicable. Review representative compositions, not only atoms.
- Give shared decisions an owner and an update path. Lightweight governance can
  suffice for one person. Enterprise practices are examples, not prerequisites.
- Start from actual repeated needs and appropriate platform conventions. A
  comprehensive component library is not required before every product decision.

## Application in current Fab

[Shared interface principles](../interface-principles.md) own common wording and
composition policy. This knowledge explains reuse/tokens/components when needed;
it does not require constructing a full library for each interface revision.

[Block screens](../../skills/wireframe/references/block-screens.md) and
[interaction prototypes](../../skills/prototype/references/interaction-prototype.md)
set the current output boundary. Apply design-system knowledge when it helps that
boundary. The study's rollout sequence is a source proposal, not a compulsory
Fab route. Token consistency does not establish real platform or runtime behavior.

## Deeper reading and freshness

R003–R010 cover method and its assumptions, R011–R019 organization and quality,
R027–R036 extension and metrics. R020–R026 are company examples. R011–R015/R032
contain dated tooling guidance, R037–R042 sources.

Structural correspondence was reviewed. Current vendor APIs, numeric rules and
performance claims are not exhaustively checked. Verify relevant primary evidence
when using them. Revisit design/code divergence or an important source update.
