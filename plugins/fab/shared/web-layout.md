# Browser layout and text adaptation

Read for visible browser presentation or review, whether a public page or a web
application. Apply [shared interface principles](interface-principles.md) for
meaning, grouping and economical text roles. Public offer copy additionally uses
[website content](web-content.md); an application does not acquire a sales funnel.
These concerns do not choose the framework. For coding tactics and stack choices,
use [web implementation](web-implementation.md) only when implementation is active.

## Browser-specific adaptation

A mobile-width website is still a browser surface. Check real narrow/wide widths,
reflow, relevant zoom or text enlargement, long localized content and the chosen
font's actual loading/fallback behavior. Do not transfer native point sizes,
font families or automatic text-scaling claims to the web.

Responsive values adapt existing roles; they do not imply new type families per
breakpoint. Keep the content and reading order understandable when columns stack,
headings wrap and controls grow. Deliberate heading line breaks require inspection
at affected widths, rather than a blanket ban or a desktop-only screenshot PASS.
Meaningful short units should stay readable without making entire lines unbreakable.

For executable output inspect relevant browser keyboard/focus, labels and controls
as well as the composition. Keep source inventories, rendering and understanding
separate. A count of font declarations is not a judgment about roles or appearance.
Do not hide meaningful overflow to make geometry checks pass.

## Accessible adaptation and evidence

Use applicable WCAG tests when accessibility is in scope. Reflow and preservation
under user text-spacing overrides are distinct from imposed authored metrics.
A normal desktop screenshot cannot establish either. Keep relevant exceptions,
actual test conditions and unobserved behavior explicit. Platform details may need
current primary verification; a token check is not a full accessibility audit.

[WAI headings](https://www.w3.org/WAI/tutorials/page-structure/headings/) describes
semantic organization. [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
and [text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
describe browser content/adaptation conditions and exceptions. They do not define
a universal visual style, type-role count or conversion optimum.
