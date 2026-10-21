# Screen-flow maps

Read for requested screen-flow visualization, including experimental Canvas
opt-in. Respect the active output choice and existing accepted behavior. Default
structure/scenario output remains [tables](table-view.md); visible screen layout
and physical composition retain their own contracts.

## Choose the smallest useful representation

The goal is to let a person inspect the system's screens, actions and paths.
Do not manufacture architectural layers to complete a template.

- **SC — scenario:** a person's task, its actions, states, outcomes and returns.
  One screen or a unique multi-screen task may fit entirely in one scenario.
- **MOD — module:** the same bounded behavior actually reused by different
  functional callers. Give its common input/output and each caller's return
  context. Complexity or repeated documentary links do not establish reuse.
- **NAV — navigation map:** an optional architecture overview when roots,
  shared access and nested places benefit from it. Multiple screens alone do
  not require another document.

Only index existing useful representations. When needed, the index has a neutral
navigation-map link first, then the existing Scenarios and Modules groups. Omit
empty groups. A one-scenario task needs no extra index/legend merely for symmetry.
Do not prescribe a tab bar from the existence of application roots.

## Establish behavior before geometry

Use sufficient existing requirements/artifacts; do not restart discovery for a
partial repair. Preserve canonical IDs and distinguish objects, roots, screens,
modal tasks, states, actions, results, events and documentary references.

For each relevant action establish its owner, trigger, actual destination/effect,
conditions, failure/empty outcome and retained object/query/position/input.
Collection-item actions belong to the item. A routing screen can have equal
branches and no primary action. Save/apply/confirm belongs to an actual commit
boundary; do not invent draft and Apply for every single-choice modal.

Keep different visible states bound to their actual surface. Small inline
indicators do not automatically become screens. An empty state is not a system
error. Unknown mutation outcome is not confirmed failure or success. Audit the
relevant lifecycle beyond creation, including cancellation/removal when the
product supports them. State what an independent child commit means if its
parent task is cancelled; do not infer a universal persistence policy.

Global search has its own shared-access scope, independent from unrelated city
or settings flows. Local search is described within its actual section. Define
shared access once; do not add the same global navigation tail to every card.

## Compose actual reused behavior

Extract only when reuse is established. A module may span several screens and
modal tasks. Its definition owns its goal, successful result, empty/error and
cancellation behavior. Its caller supplies origin and retained state.

Show consecutive independent tasks in separate forward frames, even when a
frame is a link to detail. For example, selecting a person returns a selected
person/chat. A separate following conversation frame owns the choice between
an empty new conversation and an existing history. The selector must not decide
or embed that downstream behavior. A successful module reference must show its
continuation, rather than appear to end at an entry link.

Cancellation/failure does not advance the successful chain. Review other actual
callers when changing a shared definition. Documentary module frames and handoff
results add no application screen or tap. Preserve source-to-projection tracing.

## Make the cards readable

- Lead with a meaningful title. Put stable ID, type and screenshot context below
  it as secondary information; do not repeat the section as the largest heading.
- Separate semantic-card header/metadata from body with a divider. Action-only
  cards need no empty body. Navigation and legend use simple documentary headings.
- Keep action cards to a short verb phrase and ID. Fields, choices, constraints
  and effects belong to the owning screen/modal/result or source contract.
- Use actual lists for collections, options, parallel actions and outcomes.
  Check each body block separately. An explicit one-item action group still has
  a bullet. Continuous prose and labeled form fields need not become lists.
- Show actual sort/filter choices and selected values, not unexplained technical
  draft language. Preserve labels across entry and result.
- Size to meaningful content and actual wrapping, list/paragraph spacing and
  divider margins. Reflow neighbors when height increases; do not clip or remove
  content to fit a universal rectangle. Preview font guesses are not native fit.

## Make the paths readable

Develop forward paths to the right. Routing actions get separate branches;
optional tasks remain optional. Meaningful conditions/results occupy compact
framed nodes. Arrows indicate direction and carry no essential text. A condition
is neutral; only an actual command uses the action treatment. Collapsing an
inserted frame and its two legs must recover the original source, destination
and meaning without changing canonical application identities.

Keep error branches near their triggering action. Draw empty-state start actions
to the existing forward action node; do not hide them as ordinary Back text.
Keep normal Back/dismiss/recovery concise with exact origin and retention rules,
without redundant reverse edges. Show a recovery path explicitly when its
sequence or changed context is itself under review. Omit visual redundancy,
never omit behavior.

Use a necessary continuation frame per cross-map destination, naming its target,
link and retained context. Do not duplicate a direct bypass and an action path.
Returning from a reused task does not require visiting an application root.

Give connectors clear space on both sides of compact frames, especially at
fan-outs. Preserve wider creator-set gaps and meaningful row order. The reviewed
messenger used 300 clear units and 400 after dense forks; these are starting
examples, not universal constants. Prefer adequate spacing before another layout
engine. Fit-to-window alone does not demonstrate readability.

## Semantic palette and notation

Colors reinforce explicit labels/types; they never carry meaning alone.

| Meaning | Canvas treatment |
| --- | --- |
| Actual module definition or call | Purple, `6` |
| Modal task | Blue, `#0062ff` |
| Empty-content state | Gray, `#b8b8b8` |
| User action | Turquoise, `5` |
| Action error | Red, `1` |
| Service event | Yellow, `3` |
| Other screen/result/condition; navigation/index/legend | Neutral |

Do not color navigation green or conflate purple modules with blue modals.
Apply gray to actual empty content, not every suffixed state or blank field.
If a legend helps, place it beneath a useful index with matching width. Use
“Block types” and “Colors” subheadings (localized to the artifact's language).
Use one small color square per line beside its meaning, without a second bullet.
Bundle local swatch assets and validate their links/theme correspondence.
Reusable starting assets: [module](../assets/screen-flow/module.svg),
[modal](../assets/screen-flow/modal.svg), [empty](../assets/screen-flow/empty.svg),
[action](../assets/screen-flow/action.svg), [error](../assets/screen-flow/error.svg),
[event](../assets/screen-flow/event.svg). Copy needed assets into the deliverable
and link from the actual vault root. Numbered Canvas colors are theme-dependent;
check correspondence in the selected viewer rather than assuming these swatches
prove native theme parity.
No footer explaining that the legend is a legend is needed.

Use stable existing IDs. Relevant notation: ROOT entry; N shared access; S screen
with suffix for state; M modal; A action; R result on the same surface; E action
error; P cross-map continuation; SYS service event. NAV/SC/MOD classify useful
representations, not mandatory product entities. M and MOD are distinct.

## Preserve and check

Keep source/projection mappings, source owners, conditions, return selectors,
state binding and explicit display-omission reasons. A navigation relation map
is not a physical-containment structure wireframe; keep that validator's actual
contract rather than weakening it for text-card maps.

Check links/assets, duplicate IDs, required forward branches, concise actions,
lists per block, typed palette, framed meanings, overlap and content fit. Trace
the relevant full path and alternate origin, including failure/empty/cancel and
retained input/position. A changed helper needs meaningful negative probes for
semantic loss; fixed fixture counts are not universal acceptance criteria.

For local repairs use expected input hashes and a bounded file/ID scope. Preserve
creator edits and unrelated paths; validate new references before retiring old
ones. Keep reversible retained evidence without duplicating full maps as SVGs
in the delivered directory.

Inspect the actual overview and readable detail in the selected viewer. Native
clipping overrides a successful approximate preview prediction. Clearly separate
static preservation, author-led virtual paths, fresh instruction-following,
native rendering, human acceptance and executable product behavior. Claim only
the boundary observed. The installed package must contain the method and needed
helpers; no maintainer checkout, messenger generator or chat memory prerequisite.

## Optional bounded presentation helper

Use [screen_flow.py](../scripts/screen_flow.py) only when its narrow operation
matches the requested edit. It applies explicit semantic colors and moves
existing labeled relations into documentary frames, preserving the exact
original edge in a reversible projection audit. It does not choose modules,
invent conditions, discover callers, lay out the entire map or guarantee fit.
Do not infer types from ID suffixes or a language-specific phrase list.

```sh
python3 <wireframe-skill-directory>/scripts/screen_flow.py source.canvas candidate.canvas --spec edit.json
```

The edit spec has `sourceSha256`, optional `nodeKinds` mapping actual IDs to
the palette meanings above, `edgeKinds` mapping existing labeled edge IDs to
`action`, `condition` or `result`, and optional `placements` mapping those edge
IDs to frame geometry (`x`, `y`, `width`, `height`). An empty mapping is valid.
Use explicit accepted behavior to classify. Defaults estimate compact text fit;
insufficient space fails rather than moving unrelated cards. Prepare a reviewed
bounded layout change separately when needed. The helper never overwrites an
existing file and refuses a changed source hash. Keep its projection audit
with project evidence. Its extra frame IDs are documentary, not new app IDs.

Call `assert_preserved(original, candidate, audit)` when checking later edits.
Loss of an empty/error/return branch, source metadata, leg, label or original
card is a failure. Hash/structural checks do not prove that a label means what
the author intended or that two tasks actually reuse behavior. Assess those
from the source contract and trace actual origins. The helper creates no
mandatory NAV/SC/MOD files or legend. Use the existing vault/registry validation
and [Canvas adapter](canvas-adapter.md) for links and rendered inspection.
