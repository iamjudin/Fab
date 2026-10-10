# Canvas file and render adapter

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

Apply the interaction palette from navigation-ia consistently. Use explicit
hex colours when numbered Canvas colours cannot express distinct blue navigation
and light-blue local interaction. For example: grey `#b6bcc3`, light blue
`#bae6fd`, blue `#2563eb`, green `#16a34a`; check contrast in the actual renderer.
Before and after layout cleanup, compare navigation actions/destinations with
the current access table, including creation, Back/Cancel and contextual returns.
Route or relabel a crowded edge while preserving its transition. Removing
essential edges to make the map quieter is a semantic regression.
