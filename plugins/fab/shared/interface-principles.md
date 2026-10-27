# Shared interface principles

Read when authoring or reviewing visible interface wording or composition, on
any target. This is a small set of Fab decisions, not a new skill, workflow stage,
design system or platform standard. Use accepted project meaning and foundations.
Domain rules remain with Product; evidence gathering is conditional.

## Meaning, expression and economy

- Identify the person's task, the object, its explanation, available action and
  actual outcome. Text should make those understandable in the relevant context.
  A heading labels its content; a control identifies its action/consequence.
  Do not substitute an empty slogan, decorative label or generic promise for
  missing meaning. Preserve accepted voice and useful personality; clarity does
  not require sterile prose or maximal wording on every small control.
- Make each element contribute information or function. Remove redundant text,
  emphasis and containers when authorized, without removing distinct meaning,
  needed conditions or behavior. Brevity is not a reason to hide important detail.
  Supplied facts, accepted decisions, draft wording and unknowns stay distinct.
  Do not invent proof or change locked content merely to fill a composition.
- Let grouping, alignment, spacing and type express those relationships. A heading
  should visibly belong to its content; a label to its control. Diagnose the actual
  relation before changing gaps. Neither equal tokens nor more card decoration
  establish semantic belonging. No universal spacing ratio applies to every group.
- Reuse a small coherent set of text roles. Add a style only for a useful reading
  role or justified optical/context need, not for every new section or component.
  Do not impose a fixed style count. Responsive values are adaptations of roles,
  not automatically new roles. Equal values do not erase distinct semantics;
  differing declarations do not alone prove excess or poor rendering.
- Fit real content: relevant long text, Cyrillic/localization, glyphs, punctuation,
  meaningful short units and larger text. Prefer content-driven growth/wrapping to
  arbitrary boxes or hiding overflow. Preserve meaning when shortening. A deliberate
  break or optical exception must survive its actual applicable contexts.
- Choose the font, size, measure, line height and tracking together for the role.
  A short display title and long explanation have different needs. Avoid arbitrary
  per-element tuning; use the project's coherent foundation. Do not promote a
  platform example into a universal font, unit, size or automatic-scaling guarantee.

## Authoring and revision preflight

For an existing candidate, translate the request into the actual objects and
relationship being changed before editing. Use the supplied reference and accepted
composition to identify the alignment anchor, text role, behavior or grouping.
Keep unaffected content, column structure, ordering and interaction intact.
This is working reasoning, not a required plan, checklist file or approval step.

An alignment request does not by itself authorize changing column counts, moving
portraits or rebuilding neighboring sections. If plausible interpretations would
materially change the accepted composition, explain that choice before dependent
edits. A clear local request needs no extra confirmation. An explicitly requested
global redesign can change those structures; do not preserve a layout the person
has asked to replace.

After editing, inspect the actual difference and affected rendered relationship:
did the named elements align with the intended anchor, and did preserved neighbors
stay intact? Verify the requested relation, not just that boxes fit or controls
exist. For shared styles, inspect another affected instance and a relevant
exception. Stop a spillover at its owning selector/component instead of compensating
with more unrelated adjustments. Do not claim rendered verification from a diff.

When authoring a new composition or adding text styles, map the visible text to
the existing roles first. Inspect equivalent roles together at the relevant sizes:
headings, explanations, card titles and notes should not acquire incidental
variants through successive section edits. Reuse or consolidate equivalent roles;
retain a distinct value when meaning, optical need or adaptation justifies it.
Check real content and wrapping after consolidation. A uniform number can still
serve the wrong role; a role inventory alone does not establish visual quality.

## Separate concerns instead of multiplying profiles

Start from the requested outcome and known context. For an ordinary task, read
these principles and only the relevant existing guidance; no required routing
form, profile manifest, decision matrix or all-platform survey.

1. **Task/scenario:** public offer content can use [web content](web-content.md)
   and [landing scope](landing-pages.md). App state/navigation retain their existing
   Product/Wireframe owners. Not every app screen needs an offer or primary CTA.
2. **Target environment:** browser presentation uses [web layout](web-layout.md).
   Mobile app behavior uses [mobile structure](methods/mobile-structure.md) and
   current target guidance when needed. A narrow browser viewport is not native
   iOS/Android; a browser-built app prototype does not change its target platform.
3. **Implementation:** use the accepted stack and sufficient tools. For a new
   public site, [web implementation](web-implementation.md) owns the plain-web
   default. It does not prescribe the production stack of a native app.

These are different questions, not three mandatory stages. Add a target-specific
reference only when an actual task exposes a reusable difference. Do not invent
desktop, watch or other adapters for hypothetical coverage.

## Evidence and source boundary

Check the changed output at the level actually promised. Source/style inventories,
rendered grouping, platform behavior, user understanding and measured effects are
different evidence. Reading this file is not proof of application. Ordinary author
preflight is continuous; it does not add an approval after every artifact.

For unresolved detail consult [qualified layout/typography knowledge](methods/typography-layout.md)
or [design-system knowledge](methods/design-systems.md) as appropriate. The original
mobile-origin report remains source evidence with universal, dated and iOS-specific
claims; its full packet is not rewritten. Shared principles are current Fab policy,
scenario/target references specialize them, and technical choices implement them.
