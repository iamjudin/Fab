# Web implementation choices

Read for actual website implementation or its technical review. Content and
presentation are separate concerns: use [shared interface principles](interface-principles.md),
[public-page content](web-content.md) and [browser layout](web-layout.md) as applicable. A stack does not supply
meaning or visual hierarchy, and these principles do not depend on this stack.

## Plain web first

For a new landing or compact informational/service site without a selected stack,
start with semantic HTML, ordinary CSS and vanilla JavaScript only for behavior
HTML/CSS cannot sufficiently provide. Typical files are `index.html`, `styles.css`,
optional `script.js` and local assets, not a prescribed file count. Reuse coherent
text/spacing roles and classes rather than inventing per-block styling.

Do not automatically add a framework, component/CSS library, package manager,
bundler, transpiler, CMS, hosted builder or CDN dependency. Prefer system fonts
unless accepted brand assets or a concrete requirement justify another source.
Do not add tracking, remote fonts or third-party runtime scripts by habit.
Preview servers and test tools do not by themselves require product dependencies.

Existing repositories and explicit stack choices take precedence over this new-
project default. Preserve the actual working foundation; no automatic migration
to plain HTML. For a requirement the baseline cannot sufficiently meet, explain
the unmet need, smallest viable alternative and relevant maintenance consequence.
Discuss a material stack/scope change before adopting it; routine implementation
needs no repeated approval. Simplicity is not a quality/scale ceiling, and this
default does not prescribe the architecture of an application.

## Implement the real contract

Use semantic headings/regions, labels and appropriate links/buttons. Keep content
and essential navigation usable without JavaScript where practical. Verify the
selected interactions and applicable negative/return paths; responsive code does
not establish observed rendering. Separate source checks from browser evidence.

Static files alone do not deliver remote form submission, lead storage, email or
payments. Identify the actual dependency and existing service/API before promising
it; do not silently choose a backend or present simulated success as real delivery.
Do not invent a diagnosis from a behavioral report without code/runtime evidence.

Local preview, real hosting, indexing, social preview and analytics have distinct
needs and authority. Do not fabricate domains, service IDs or verification values,
or require every SEO asset for every site. Use current primary guidance for the
actual stack/service when implementing those outputs. Ordinary local work does
not authorize deployment, tracking or publication.

Editable Figma output, when requested, follows current Figma capabilities and
the agreed foundation. A capture is not automatically editable design. A screenshot
or mock form proves neither a working backend nor visitor comprehension/conversion.
Retain operational gaps and actual readiness; do not force a design/code round trip.

## Browser text implementation

Choose semantic heading elements for content hierarchy and style roles separately.
Use paragraphs/margins for paragraph spacing, not repeated line-break elements.
Let containers grow; use deliberate breaks or short nonbreaking units only with
the affected content/width checks. Keep role values in the existing CSS/token
foundation rather than appending another per-section override for every revision.
These are implementation choices, not a universal CSS scale or forced refactor.
[MDN text styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
and [line breaks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
describe browser mechanics; their examples are not a mandatory visual system.
