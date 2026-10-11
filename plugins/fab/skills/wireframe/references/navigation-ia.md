# Structure and access

Read after selecting a Product Slice and before composing screen layouts.
Review structure first. Detailed paths belong to
[critical scenarios](critical-scenarios.md); layout belongs to
[block screens](block-screens.md). Presentation/file QA uses the
[Canvas adapter](canvas-adapter.md).

For a research basis or unresolved surface/access choice, read the bundled
[structure brief](../../../shared/methods/product-structure.md) selectively. Historical
research does not override current creator decisions or stage contracts.

## First decision: structure and access

Show how the product is organised: its main screen, other necessary screens
or panels, primary and secondary controls, and where the in-scope Use Cases
start. A surface has a purpose and context; its presentation may be a full
screen, sheet, dialog, tab destination or embedded area. Several UC may share
one surface, and one UC may cross several surfaces.

Compile from the selected slice, current UC, capabilities and domain rules.
Before drawing, synchronise any newly included goal into the UC Markdown
review and graph. Keep accepted scope distinct from unapproved policy detail.
A UI control can implement an existing UC without being named in the domain model;
that is not a newly included goal. Compare its behavior with the rules before
calling it unsupported. Preserve compatible current interactions during repair;
unresolved semantics stay explicit, not silently removed from the interface.
Explain the main screen and access priority using frequency, importance,
urgency and working context; label inferred frequency as a hypothesis.
Do not invent a dashboard, tab or detail screen merely to give a feature a node.
Before splitting a small contextual setting into another surface, compare an
embedded section with a separate opening. Choose based on task size, context
and an independent purpose; feature importance alone is not a reason for an
extra modal layer. Record the substantive trade-off briefly outside the map.

## Reconstruct ownership before drawing

Model two relationships separately:
- composition: section/screen -> collection -> repeated object item -> its
  information and actions, plus screen-level/global actions;
- navigation: a particular action opens a destination with a defined context.

Preserve these levels visually. An item action belongs to the item, not to
its whole collection or screen. Distinguish settings of an object from
application/account settings and per-object reminders from OS permissions.
For an object used across UC, compare inline operations with an object detail
context where history, information and related actions live. Frequency of one
operation alone must not flatten the remaining object model. Check creation
and editing together: meaningful initial configuration must not require
creating an object and immediately entering edit without an explicit reason.

Use domain objects, UC and creator corrections to build a compact composition
tree and access table internally. Missing ownership or scope decisions cannot
be repaired by arranging rectangles. New creator signals remain visible with
scope status: accepted, proposed addition or unresolved. Do not silently
invent subscription policy, accounts or technical guarantees from their labels.

## Overview notation

Create one overview Canvas with stable surface IDs and a short linked
rationale/access table. Start with top-level areas and screens, then show
compact lists of their content. A repeated collection shows one representative
item and its nested fields/actions. Use grey for noninteractive information,
light blue for input and selection within the current surface, green for
controls that submit a persistent change (Create, Save, add/remove a fact),
and blue for navigation that opens another screen, sheet, scenario
context or modality, including Back/Close returning to another surface.
A saving or error state drawn separately on a scenario map is not navigation
by itself: colour follows the actual interaction, not the diagram arrow.
Green denotes the requested mutation, not confirmed success. An automatic
return after successful saving is the result, not the colour of the Save
control. A check that immediately saves a fact is green; a draft checkbox is
light blue. Retry of a mutation is green; checking its uncertain outcome is
local interaction. Split them if their effects differ.
Apply this notation to the overview and detailed scenarios. Do not prefix
rows with I/A/N letters.
Distinguish on-the-spot actions from navigation through wording and edges.
Keep a short legend. Split mixed information/action or local/navigation rows
so their interaction types are unambiguous; a read-only status is not a control.

Use a compact surface container with short rows, indentation and smaller
containers only for genuine semantic composition. Avoid turning each control
or explanatory sentence into a large equal-sized card. Connect transitions
from the initiating row/action, not from a paragraph or anonymous screen edge.
Global navigation has one visible owner in an overview. Draw each tab and
its destination from that single tab bar. Do not duplicate a tab bar or detach
a control below a screen merely to shorten an edge; adjust layout instead.
Canvas action nodes may be used as row anchors inside their actual owner;
matching S-ID text does not replace ownership. Composition uses indentation
or containers, not transition arrows. Linked detailed functional/scenario maps
are documentation references, distinct from runtime navigation.

Retain familiar presentation terms: tab bar, navigation stack, modal sheet,
modal presentation, embedded section. Name purpose and presentation separately.
Record parent context and concise Back/Close/Cancel return semantics without
expanding the whole flow. The map is structural, not a wireframe layout.

Before review, verify ownership down to the repeated item; distinct object
and global settings; visible navigation from the source action; necessary
content shared by creation/editing; and explicit status of scope additions.
Only after these semantic checks inspect geometry, labels and file links.

The overview is a map of structure, not a behavioural specification. Keep
validation errors, saving mechanics, detailed date-state rules, confirmations,
and full return branches in source notes or later scenarios. Mention only a
return/context constraint that changes the structure. If a card becomes a
paragraph, move explanation into the linked rationale rather than shrinking
text or expanding every card. Prioritise scanability at overview scale.

Keep surfaces at a comparable level of composition and principal actions.
An inspected scenario must not make its screen disproportionately deep in the
overview: keep step sequences, states and recovery in the linked detail map.
Preserve meaningful ownership through indentation or a necessary container;
equal depth does not mean flattening collections or object actions.
The creator should be able to locate a function, see how to open it and
understand where they return. Review the whole structure against this criterion.

Internally walk the critical UC through the proposed structure before showing
it: entry, action, context change, result, return. Choose those that expose
structural risk; no fixed number is required. This check should find missing
surfaces or lost context without producing all detailed scenario maps.
Keep product requirements, design proposals and technical guarantees separate.

First review question: are the main screen, access to important actions,
secondary surfaces and hierarchy organised appropriately for this slice?
For a structure-only request finish here. For authorized downstream candidate
work apply shared decision policy: resolve consequential structure choices, use
accepted inputs or explicit candidate assumptions; never invent human acceptance. In a delegated test, record a test
operator's choices as simulated assumptions, never as creator approval.

## Входные зависимости

Когда entry/setup/account/permissions/paywall меняют доступ к результату,
применяй [первую ценность](../../../shared/methods/first-value.md) и при платном доступе
[монетизацию](../../../shared/methods/monetization.md). Структура показывает владельца,
применимый вход и возврат; сама не добавляет обязательные welcome slides,
аккаунт, синхронизацию или paywall. Детальные ветки остаются в сценариях.

## Physical projection check
When controls are separate coloured Canvas nodes, their surface must be a real
group, with collections/items nested where meaningful. S-ID text and a written
access table cannot substitute for this physical ownership. Run the structure
guard for included surfaces; it's a narrow projection check, not semantic proof.
Critical flow-only diagrams don't need fake screen containers. Fix ownership
before declaring structure sufficient for downstream candidate work.
