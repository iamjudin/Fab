# Layout, typography and interface text — qualified knowledge brief

Read when creating/reviewing visible layout, grouping, interface text or text
adaptation. [Preserved report](typography-layout.full.json) contains all 57 source
sections, including its unsupported claims. It is supplied research material,
not a platform standard or a new mandatory product workflow.

## Knowledge and limits

- Start with meaning: identify the object, its label, explanation, action and
  enclosing group. Judge whether spacing, alignment, type and region boundaries
  express those relationships. Equal tokens alone do not establish belonging.
- Compare spacing within and between the actual groups. A heading should visibly
  belong to its content. Diagnose which gap obscures the relation before changing
  it. Do not copy a fixed 2:1 ratio, blindly reverse the gap direction, or increase
  internal spacing merely because a source example says so.
- Use a coherent hierarchy and spacing system, with explained optical exceptions.
  Repeated emphasis or container decoration is not a substitute for clear groups.
  A preference for a denser or more open composition is not automatically a defect.
- Treat Russian text as actual content: check recognizable glyphs, punctuation,
  number/unit combinations, wrapping and labels. Preserve meaning when arranging
  or shortening text. A fixed manual break or nonbreaking sequence must also work
  at the actual width, localization and selected text size.
- Prefer text roles and content-driven composition over arbitrary fixed boxes.
  Inspect relevant long strings, increased text size and meaningful icon/label
  combinations. Exact font sizes, hit areas, category counts and scaling behavior
  require current target-platform evidence. CSS pixels and native points differ.
- Review structure/styles, rendered output and understanding separately. A token
  checker cannot determine semantic belonging. An optical judgment needs actual
  rendered size, and a screenshot alone does not establish user understanding or
  native accessibility behavior. Use the cases relevant to the requested change.

## Do not adopt as universal rules

| Preserved source claim | Application boundary |
| --- | --- |
| Mandatory 1.5 line height, 50–75 characters, 4/8 px spacing or 2:1 gaps | Source examples/practice require context. They are not a universal native-interface specification |
| A minimum/default font number settles readability | Text role, font, content, settings and target-platform guidance still matter |
| Fixed Russian expansion percentages or a precise Dynamic Type category count | Unverified here. Use actual localized text and current platform settings |
| Every important title is never truncated, every meaningful icon scales automatically | Component/runtime behavior must be checked. Do not infer a native guarantee |
| Increasing internal spacing repairs wrong nesting | First identify the incorrect relationship. That change may worsen grouping |

The report's bibliography was reconstructed during reader refinement. Eight
identified URLs do not prove claim-level attribution. No full study-quality or
Russian editorial-standard audit was performed. The requested Birman-specific
comparison is absent, and the report does not establish a unified Russian school.
Quoted source advice and its confidence remain preserved in the full packet.

## Independent ingestion check

On 2026-10-16, [W3C Understanding SC 1.4.12: Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
was opened. For applicable markup-based content, the criterion concerns preserving
content/function when a user overrides spacing. It explicitly does not require
those values as authored defaults. This checks one interpretation, not all
accessibility compliance or transfer to native UI.

[Apple WWDC24: Get started with Dynamic Type](https://developer.apple.com/videos/play/wwdc2024/10074/)
was opened as a platform reference. This does not verify every numerical or
component claim attributed to HIG in the supplied report. Consult current relevant
Apple guidance for the actual target and inspect the resulting implementation.

## Application in current Fab

[Shared interface principles](../interface-principles.md) own current reusable
wording/composition policy. [Browser layout](../web-layout.md) adds target-specific
adaptation; [public-site content](../web-content.md) applies only to that scenario.
These instructions specialize the qualified knowledge, not its preserved source.

[Block screens](../../skills/wireframe/references/block-screens.md) owns visible
composition. [Interactive prototypes](../../skills/prototype/references/interaction-prototype.md)
owns executable paths and observed adaptation. [Analysis](../../skills/analysis/SKILL.md)
can review an existing artifact within its requested scope. Use this brief for the
specific layout/text question, not as a compulsory visual redesign or styling
stage. Product behavior, accepted wording and accessibility obligations retain
their actual owners. Canvas geometry/readability remains a separate opt-in experimental surface
owned by Wireframe; source screen-flow integration does not prove native fit.

For an actual finding state the visible relation, supporting artifact, impact and
correction direction. Distinguish a confirmed mismatch, uncertain interpretation,
preference and platform dependency. A new research source does not itself prove
that generated layouts improved or authorize changing another project.

## Read deeper and refresh

- R010–R020: grouping, anchors, hierarchy and rhythm. Fixed spacing recipes remain
  qualified source advice, not automatic thresholds.
- R021–R031: Russian typography, text structure, labels and content. Preserve
  exceptions and verify a consequential editorial rule before treating it as law.
- R032–R037: platform-specific claims. Exact numbers and automatic behavior are
  not independently confirmed by this ingestion.
- R038–R050: symptoms, checks and procedure. Preserve the original inconsistent
  correction directions, but apply the relationship-based boundary above.
- R051–R057: bibliography and explicit source-status limitations.

Refresh the affected binding when actual use exposes a contradiction, a source or
platform changes, or a decision depends on missing detail. A deeper Birman/Russian
practice comparison is a named gap, not an already completed investigation or a
prerequisite for every layout task.
