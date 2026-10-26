# Canvas file and render adapter

Opt-in experimental: known label-overlap diagnostic gap. Default to
[table view](table-view.md). A valid file or empty warning list does not prove
readability; inspect the actual output and disclose native-render unknowns.

Read only when producing or checking Canvas artifacts. Structure/scenario/layout
contracts decide what the map must mean; this adapter checks its physical files
and presentation. JSON, a fallback preview and actual Obsidian opening are
different evidence. The active stage is not complete merely because JSON passes.

## File and visual preflight

Use one explicit product root for manifests, maps and sources. Canvas file
links are relative to the actual Obsidian vault root; record that root separately
from the product workspace and include any product-folder prefix. Do not assume
they coincide. Copying only the map to
a different vault does not preserve them. Register every Canvas, then run:

`python3 <product-skill-directory>/scripts/product_workspace.py validate-canvas
<product-root> <canvas-path> --vault-root <actual-vault-root>`

This checks JSON, node/edge references and source paths, not semantics or
actual opening in Obsidian. Inspect the rendered map separately. When Obsidian
is unavailable, use the bundled `scripts/canvas_preview.py <canvas> <preview.svg>`
and report that the app rendering and links remain unverified. Inspect overview
scale for scanability and transitions; inspect details at readable scale.
Obsidian places group titles outside, above their frames. Leave a clear title
band before nested groups and shorten their labels rather than relying on
wrapping. Check that these bands do not overlap the previous control or an
adjacent frame. Fix concrete overlap/overflow/label defects and recheck only changed maps.
Use the documented SVG fallback if PNG dependencies are unavailable; avoid
renderer experiments. Keep explanation outside the diagram and route returns
away from cards. Structural validation cannot establish visual readiness.
The fallback recognizes setext headings and flags their effect on card hierarchy.
It does not assume a plain metadata paragraph has a smaller native font. Repair
ambiguous card Markdown at authoring, then resize/reflow affected cards; enlarging
one clipped box alone leaves the shared cause. A warning-free approximation still
needs actual Obsidian inspection, especially after native counterevidence.

## Independent fit evidence

Sizing a card from the fallback layout and checking it with that same layout is
one estimate, not independent fit verification. Its zero warnings must not be
reported as readable native output. Reflow after final wording; reserve room for
actual heading/list/paragraph spacing without shortening away required meaning.
No fixed padding multiplier establishes fit across themes or text settings.

For actual-app inspection include dense navigation/legend cards, long headings,
multiline lists and caller continuations at readable scale, including lower lines.
Record the map revision and inspected cards/settings with the observed result in
existing task evidence. Any clipped native card is a failed observation even if
the fallback is clean. A stale screenshot or changed window title is not evidence
of the selected revision. If native inspection fails, return a candidate with
native fit unverified; do not repeat the fallback as a stronger acceptance claim.
Complete text extraction for the editorial pass is documented in
[reader acceptance](screen-flow.md#reader-pass-and-transfer-acceptance).

## Choose the projection contract

First check [visual-review coverage](screen-flow.md#match-the-requested-visual-review)
against the requested result and any accepted reference format. Decide which
overview and task/detail maps actually support that review before file/layout QA.
An otherwise valid NAV-only file is insufficient when the requested critical
screen-flow paths have no inspectable visual representation. Record this as an
incomplete deliverable, not merely a native-rendering unknown.
For linked maps, inspect useful navigation/notation at the working location and
ordinary returns versus substantive recovery. A metadata link back to START or
zero collision warnings alone does not establish these qualities. Inspect exact
return-reference targets/retained context; a map link plus ID is not a verified
native jump to that node. Preserve the original relation in projection evidence.

For screen-flow or navigation-relation maps, apply [screen flows](screen-flow.md).
Use semantic types: purple modules, blue modal tasks, gray empty content and
neutral conditions/navigation. Put meaningful conditions/results in compact
documentary frames; arrows carry direction rather than essential text. A frame
adds no app screen/tap. Keep the source relation and retained context traceable.
Optional helpers and bounded-edit checks are documented in that reference.

A relation map is not the physical-composition overview checked by
`check_structure.py`. Do not weaken that guard or invent groups just to pass it.
Table and block-screen routes remain independent.

For physical composition/control overviews only, apply the interaction palette
from navigation-ia consistently. Use explicit
hex colours when numbered Canvas colours cannot express distinct blue navigation
and light-blue local interaction. For example: grey `#b6bcc3`, light blue
`#bae6fd`, blue `#2563eb`, green `#16a34a`; check contrast in the actual renderer.
Before and after layout cleanup, compare navigation actions/destinations with
the current access table, including creation, Back/Cancel and contextual returns.
Route or relabel a crowded edge while preserving its transition. Removing
essential edges to make the map quieter is a semantic regression.

Fallback SVG now routes around non-group content and reports remaining edge/label
collisions. This is approximate evidence, not native Obsidian geometry. SVG and optional PNG now share logical edge routes; font/render differences
remain approximate. Make the declared
primary entry a clear first overview anchor when the product has one. Main-screen
placement, containment and native group header bands still need visual inspection.

The fallback displays wiki-link aliases rather than raw targets and approximates
heading/metadata hierarchy, lists, paragraph spacing and dividers. It is not a
complete Markdown renderer: image embeds use placeholders, not verified swatch
pixels or clickable native links. Overflow is reported rather than silently
dropping later lines. A warning-free fallback still does not prove native fit,
theme parity, asset resolution or successful links in the creator's vault.
