# Structure and scenario tables

Current Fab default: readable Markdown tables for structure/access and critical
scenarios. Canvas layout has an open label-overlap defect; produce it only when
explicitly requested as an experimental candidate. Do not make a map or a native
Obsidian render a prerequisite for downstream work. This is a presentation fallback,
not permission to simplify the product model or skip interface decisions.

Structure rows carry stable ID, surface/parent, repeated collection/item owner,
content/control, interaction type, applicable UC/context and open decisions.
Transition rows carry stable ID, initiating control, trigger/condition, destination,
state/result and return context. Distinguish save-success, cancel/back and failure;
preserve shared-form branch-specific destinations and compatible feedback/Undo.
If multiple tables help, link by IDs; never infer ownership from a label alone.
Missing information stays unknown, not a fabricated destination. Check every
in-scope UC through entry/action/result/return and all references to known IDs.

For an existing Canvas, `scripts/canvas_table.py <input.canvas> <output.md>` gives
a lossless text inventory of nodes/links/edges and geometric group membership.
It preserves all node/edge fields in an embedded JSON snapshot. Geometry isn't
semantic ownership: inspect nested collection/item levels and current rules before
handing the inventory off as the designed structure. This converter doesn't create
or verify new product behavior. Keep source maps immutable when used as evidence.

Keep low-detail block screens perceivable and executable prototypes available as
their own outputs; a table is not a screen mockup or an interaction test. Their
readiness doesn't inherit Canvas failures or a table's validation results.
