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

## Match the requested visual review

Smallest useful representation means sufficient inspection with minimal
duplication, not the fewest files. Preserve an accepted reference's way of
separating navigation, scenario paths and reused behavior without copying its
domain, number of maps or arbitrary module boundaries.

For a structure-only review, a compact NAV map can be sufficient. For a requested
application screen-flow review, including a product pass ending in reviewable
Canvas maps, identify the critical tasks the creator needs to follow visually.
Represent their actions, important states, conditions, failure/empty/cancel paths
and returns at a readable scale. A broad NAV map and detailed Markdown alone do
not deliver those visual paths. The source model still owns the behavior; maps
are linked projections, not a replacement model or a second source of rules.

Separate a compact overview from scenario detail when unrelated journeys, actor
contexts or mixed levels make one map difficult to follow. Split by inspectable
tasks and meaningful boundaries rather than one file per screen. Extract MOD
only for actual functional reuse, with caller-specific input, continuation and
return. Keep a unique task in its scenario; do not create modules merely because
the product is large. One sufficient scenario still needs no mandatory NAV or MOD.

When NAV helps, keep it focused on roots, access and links to the useful detail
maps. Do not accumulate every scenario, state, future contour and service role
there to avoid decomposition. Cross-map references must let the person continue
the path with the correct object and retained context, without copying a shared
definition into each caller.

Before handoff, trace the requested critical tasks through the delivered maps,
including relevant alternate origins and recovery. Name what is represented,
where to inspect it and which requested paths remain missing. Build missing
in-scope projections before claiming completion; the absence of overlap warnings
or valid links does not establish sufficient representation. Do not silently
shrink a requested flow review into an architecture-only review. A genuine scope
choice remains explicit; already-authorized scenario work needs no new approval.

## Reader pass and transfer acceptance

An accepted example transfers its useful properties, not just its filenames or
palette. Before generation identify the relevant properties: local Scenarios /
Modules navigation, readable critical paths, genuine reuse and understandable
returns. After generation inspect those properties on the new product. Do not
copy the example's domain, map count or component boundaries as requirements.

Keep the accepted navigation vocabulary. In Russian use «Сценарии» and «Модули»;
do not replace those categories with a new synonym for tasks. Scenario names
identify the person's concrete action/object; module names identify the reused
behavior. Documentary catalogues, groupings and continuation references are not
application screens and must not receive a screen caption merely to fill a type.

Delivery scope is not flow order. If phase membership helps the review, name the
actual agreed stages in familiar language (for Russian, «Первый этап», «Второй
этап»), explain each stage's useful outcome once and preserve deferral decisions.
Do not repeat planning status under every link, invent phase numbers from map
order or silently promote future scope. Product owns coherent value increments;
Wireframe projects the agreed scope, not a new roadmap.

Read every delivered title, caption, menu and card body as prose after transforms.
Use `scripts/screen_flow.py review-text <canvas> <inventory.json>` to extract the
full text with link aliases and a revision fingerprint. Read all inventories;
record actual findings and the reviewed revisions in existing task evidence.
This helper does not judge grammar or meaning. Token substitution is not an
editorial pass: rewrite complete sentences in context, retaining the original
object, condition, result and uncertainty. Keep authoring instructions and
technical provenance outside the primary reading path; retain necessary behavior
and locators in the appropriate secondary layer. No forbidden-word list can
establish understandable meaning.

The map bridges product behavior to interface work: a reader must locate the
current surface, available action, visible result, failure/cancel and continuation.
It is not a substitute for perceivable screen composition needed by a prototype.
Before handoff walk a critical task to its result, a negative/recovery path and,
when shared behavior exists, two callers with their own success/cancel context.
Inspect their actual text, not only existing IDs or relation counts.

### Check entry and reader failures on the actual candidate

For consequential re-entry apply [critical scenarios](critical-scenarios.md).
A reconciliation branch somewhere in the graph is not an entry condition.
When a local explicit gate must precede a new operation, the optional command
`scripts/screen_flow.py check-entry <canvas> --entry <id> --launch <id> --guard <id>`
rejects a bypass. Choose these nodes from actual source meaning first. The helper
checks local graph paths only; cross-map/documentary paths and the state's real
allowed outcome still require a walkthrough. Do not add a fake guard to satisfy it.

After the full text inventory pass, follow the candidate using only human titles,
link aliases and prose. Can the reader name the next surface and result without
resolving an internal entry/return-row code? If not, rewrite the affected outcome
and reference as a named destination, retaining the locator secondarily in a
compact reference or audit. A list of internal caller-row IDs is not a reader
menu. Check all instances of a generated pattern, including overview catalogues,
not only the corrected sample. Keep existing scenario/module categories for
later scope too; phase membership is secondary and does not create another type.
Check grammar around link aliases in the complete rendered sentence. State the
actual corrections or remaining misses in existing evidence; an inventory hash
alone establishes the revision read, not that the editorial pass succeeded.
Reflow final text and remove obsolete fixed-height padding where it creates
empty space; do not trade clipped text for arbitrary huge cards or claim native
fit from a different fallback estimate.

## Compose a linked set for local reading

For a linked multi-map review, keep orientation available where the person is
reading, not only on START. A compact local navigator groups the useful existing
NAV, scenarios and actual modules; keep the notation/legend beside it when these
types need decoding. Reuse the same navigation data and local swatch assets.
The current scenario/module is emphasized non-link text in its navigation group;
other entries remain links. Match the exact vault-relative current map path,
not just a repeated filename or title. Apply this in both new production and
bounded composition; a uniform list of self-links hides the reading location.
A back-to-START metadata card alone is not equivalent to an accepted reference
with local task/module navigation. When the full set is large, show a useful local
subset and an explicit all-maps link; explain that bounded choice rather than
copying an unreadable catalogue into every map. One self-contained task still
needs no invented index, legend, module or extra document.

Before drawing return arrows, classify each return by meaning. Ordinary Back,
dismissal and a simple correction to an existing form can use a nearby neutral
return-reference card: actual destination map/title/ID, retained object/input and
any relevant condition. Connect forward to that reference instead of drawing a
long redundant wire across the successful flow. It is a documentary reference,
not another screen or tap. Keep the original relation in projection evidence.
Do not replace a multi-step recovery, consequential retry/reconciliation or
changed-context transition with an unexplained Back label. Keep its decision
sequence explicitly traceable; a necessary reverse edge is valid. No zero-reverse-
edge quota applies. Native navigation to a particular Canvas node must not be
assumed: a map link plus exact target ID is a locatable reference, not a verified
node jump. Check actual file links in the selected vault.

Use the bounded helper's composition operation below when it fits this work.
Whether generated by helper or manually, preflight the actual delivered maps:
local orientation at readable detail, main forward path, each return target and
retention, necessary recovery and cross-map caller continuation. An overlap-free
preview or source-ID count does not satisfy those review questions. Record any
unreviewed reverse connectors as review candidates, never silently delete them.

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
continuation, rather than appear to end at an entry link. In interface view the
producer rejects an invoked module with no outgoing relation. Connect its real
caller outcomes locally; disconnected outcome cards and prose return promises
do not form a readable chain. This checks presence, not correct success/cancel
semantics; the caller walkthrough still owns that assessment.

Cancellation/failure does not advance the successful chain. Review other actual
callers when changing a shared definition. Documentary module frames and handoff
results add no application screen or tap. Preserve source-to-projection tracing.

## Verify the human walkthrough, not only graph reachability

The review purpose is to understand the product and follow a person's task
without decoding implementation identifiers or reconstructing another document.
At each boundary name the current task, visible surface, action, outcome and
actual next destination. Prefer reader-facing titles grounded in product meaning;
keep unsettled behavior explicitly unknown instead of inventing a concrete UI.

For every linked continuation provide the named destination map and surface,
plus its stable target ID as secondary locator when useful. Do not write "first
meaningful entry", "next frame" or "of this map" when the target is actually
owned by another map. Navigation roots with several genuine outcomes must expose
those useful choices, rather than link only one and leave the others as ID prose.
Select a local related-task menu from actual connections; numerical neighbors
or an arbitrary equal item quota do not establish relevance.

For reused behavior, trace an invocation from its caller, through the common
entry and outcomes, back to that caller's named continuation or cancel origin.
The same module from a second task must preserve that second task's own object,
input and destination. Caller-contract rows explain this binding; they are not
additional application screens or a disconnected substitute for the shared path.
Before handoff walk these concrete paths through the delivered text and links,
including the error/cancel alternative. Existing file/ID validity alone is not
an understandable-continuation verdict.

Keep a substantive recovery sequence and its distinct decisions/actions visible.
Its terminal recurrence may use a locatable reference to the earlier operation,
retaining the original object/attempt and condition. Keeping recovery explicit
does not require a long reverse wire. Do not replace the sequence with generic
Back or erase pending/unknown/rejected/confirmed distinctions. A short readable
reverse connector can remain when it best explains the relation. Review geometry
and meaning together, not one permitted list of operation names.

## Make the cards readable

- Lead with a meaningful title. Put stable ID, type and screenshot context below
  it as secondary information; do not repeat the section as the largest heading.
- Preserve compact reader addresses such as S03, A08 and E11 on every semantic
  node in a linked screen-flow set. Put the number, type and useful screen/state
  context below the title. These addresses are not projection plumbing: hiding
  `caller-*` must not remove them. Reuse accepted numbers, allocate unused numbers
  only for new nodes and check uniqueness across the linked set. Do not renumber
  on a layout change. Numbered target names belong in link aliases and relevant
  control/outcome references; raw keys remain in source/audit data.
- Keep projection plumbing such as `caller-*`, raw edge IDs and implementation
  field names out of visible headings. Preserve them in node IDs/audit/source
  mappings. Canonical surface IDs may appear as secondary locators where useful.
  Give technical retention fields a human explanation when they affect review.
- Use blank lines around both captions and thematic breaks. `caption` immediately
  followed by `---` becomes a setext heading in Markdown; it is not a divider
  beneath small metadata. The helper's `card_text(title, body, caption)` produces
  unambiguous boundaries without inserting internal IDs. Plain Markdown captions
  have no guaranteed smaller native font. Size after actual wrapping/hierarchy.
- Separate semantic-card header/metadata from body with a divider. Action-only
  cards need no empty body. Navigation and legend use simple documentary headings.
- Keep action cards to a short verb phrase and ID. Fields, choices, constraints
  and effects belong to the owning screen/modal/result or source contract.
- Keep screen context/state as useful explanation, then show visible information,
  actual input/choices and available controls. For example, a conversation shows
  recipient, messages, draft input and sending/attachment actions. A narrative
  about retaining input is context, not that screen's composition. Keep both.
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
uses yellow, like a service event; C and SYS labels keep their meanings distinct.
Only an actual command uses the action treatment. Collapsing an
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
| Service event or explicit condition | Yellow, `3` |
| Other screen/result; navigation/index/legend | Neutral |

Do not color navigation green or conflate purple modules with blue modals.
Apply gray to actual empty content, not every suffixed state or blank field.
For a linked project, repeat the same complete project-wide legend on every
map, including roles used elsewhere in that project. Derive it from the complete
actual map set; do not include all unused Fab roles or filter it by current card.
Place it beneath a useful index with matching width. Use
“Block types” and “Colors” subheadings (localized to the artifact's language).
Use one small square per line beside its meaning, without a second bullet.
Use filled role-color squares for colored types and the bundled
[neutral outline](../assets/screen-flow/neutral.svg) for neutral types; do not
mix square rows with ordinary bullet rows.
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

Use [screen_flow.py](../scripts/screen_flow.py) for explicit new-map production
(described below) or when its bounded projection matches the requested edit. It applies explicit semantic colors and moves
existing labeled relations into documentary frames, preserving the exact
original edge in a reversible projection audit. It does not choose modules,
invent conditions, discover callers or guarantee native fit. The projection mode does not lay out a whole map.
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

### Optional local orientation and return-reference composition

The same edit spec can add `composition` with `mapPath` (actual vault-relative
Canvas path), `returnReferences` and `panels`. No new generator or product schema
is required. The source must already contain the actual behavior and relations.
Choose semantic returns explicitly; this operation never infers them from words,
position or an ID prefix. An unchanged single task can use an empty edit spec.

```json
{
  "sourceSha256": "<current source file SHA-256>",
  "composition": {
    "mapPath": "Project/sc-edit.canvas",
    "returnReferences": {
      "correct-fields": {
        "label": "Continue editing",
        "retained": ["Same object and all entered values"],
        "reason": "Simple correction to the existing form",
        "placement": {"x": 2100, "y": 600, "width": 420, "height": 600}
      }
    },
    "panels": [
      {
        "id": "local-navigation", "kind": "navigation", "title": "Navigation",
        "groups": [{"title": "Scenarios", "items": [
          {"label": "Edit details", "map": "Project/sc-edit.canvas"}
        ]}],
        "placement": {"x": -700, "y": 0, "width": 450, "height": 450}
      },
      {
        "id": "local-legend", "kind": "legend", "title": "Notation",
        "body": "A — action; E — action error. Use the relevant types/colors and local swatch links.",
        "placement": {"x": -700, "y": 550, "width": 450, "height": 450}
      }
    ]
  }
}
```

Optional `labels` maps `return`, `target`, `source` and `retained` to localized
single-line labels, so generated metadata follows the artifact language.
Positions, labels, language, useful groups and actual notation are authored for
the artifact. Empty groups, invalid paths, collisions, insufficient estimated
space and missing return context fail. The helper validates path syntax, not
file existence: run vault validation afterward. The audit retains exact original
return edges, new reference legs, target IDs/context and orientation panels;
`assert_preserved` rejects loss/tampering and reconstructs the exact source.
`review_composition` lists remaining leftward connectors for semantic/visual
review. That diagnostic does not classify recovery or prove native readability.
The helper adds no native-node-link capability and does not choose whole layouts.

### Reader-facing authoring helpers

`card_text(title, body='', caption=None)` writes one explicit title, an optional
plain type caption and a safely separated body. It never invents an ID caption.
`continuation_text(title, target_map, target_id, target_title, retained,
target_label='Target ID', target_display_id=None, caption=None)` writes a named
destination with supplied context. For reader-facing output supply the actual
target's stable `target_display_id` and the reference card's numbered `caption`.
The alias then reads `S03 · Draft` without a separate raw-key locator. The legacy
raw-key branch is retained for old technical projections, not the reader contract.
Resolve map/surface/caller ownership first; the helper cannot infer whether the
chosen destination is correct. Cross-check actual targets and the walkthrough.


### New-map producer: topology before space packing

For a new linked Canvas candidate, prefer the bundled `produce` operation over
an ad hoc row generator. Author explicit meaning first; this is a presentation
producer, not product discovery. It accepts cards (`id`, `kind`, `title`, optional
`body`/`caption`, explicit nonnegative integer `lane`) and edges (`id`, `fromNode`,
`toNode`, `kind`: `forward` or `return`). Supply `mapPath`, a vault-relative
`.canvas` path. Default `view` is `interface`. Every semantic card and every
return relation then needs an explicit stable `displayId` (for example S03, A08,
E11 or P02), separate from its internal `id`. Reuse the source model's accepted
addresses; persist new allocations in existing source/case metadata, not a new
registry. Missing/duplicate reader IDs fail inside a map; cross-map uniqueness
and actual reference targets still require set-level checks. The producer adds
number/type to captions and derives used code families in the compact legend.
Numbered return targets replace raw-key locator lines.

For an interface view, cards typed `screen`, `modal` or
`empty` require explicit `surface` with a nonempty `content` list and a `controls`
list. Each control has a readable `label` and explicit meaning. Default `kind` is
`command`: it requires `target` pointing to an actual A-node, a forward edge from
this owning surface to that action, and a represented continuation/outcome from
the action. A target elsewhere in the graph or a direct module link is insufficient.
`kind: input` describes local uncommitted editing without a graph target.
`kind: local` requires an `effect` explaining the local-only change, without a
graph target. Do not classify remote saves, navigation, provider operations or
other consequential commands as local to bypass the check.
`kind: unresolved` requires an actual missing-choice `reason`; it is retained
in the receipt as a gap, not accepted coverage. No target is fabricated.
An explicitly read-only surface may have no controls. The receipt inventories
all control bindings and unresolved controls for semantic review. Structural
checks cannot decide whether the author misclassified a command as input/local. Original `body` remains
as opening context/state, followed by visible composition and controls. Localize
`labels.content`, `labels.controls` and `labels.behavior` as appropriate. Do not
infer or fabricate missing fields from prose to satisfy the helper.

For a genuinely abstract behavior diagram, explicitly use `view: behavior`;
its receipt says it is not an interface projection. This mode does not satisfy
a requested screen-flow candidate for interface/prototype work. Structural
fields do not prove that the authored composition is correct. Use a distinct
lane for concurrent cards in the same column.
Lanes express meaningful branch groups, not a command to fill empty cells.

```sh
python3 <wireframe-skill-directory>/scripts/screen_flow.py produce spec.json new.canvas
```

For a person-triggered transition, bind the source control's `target` to the
action node, not directly to the next screen. Existing explicit A-nodes remain
valid. Alternatively, a forward edge may declare
`trigger: {"id": "open-form", "displayId": "A03", "title": "Create record"}`.
The producer materializes that numbered action between the source and destination
and retains the exact original edge in `userTriggers` evidence. Multiple origins
may share one explicit command only when its identity, definition and destination
really agree. It does not discover actions from nouns, text matching or geometry.

A direct screen/modal/empty-state to another such surface in an interface view
requires either this trigger or an explicit `cause` (`automatic`, `input`,
`external`, `unresolved`) plus a meaningful `reason`. Automatic/input-driven
state changes must not acquire invented clicks. `unresolved` preserves an actual
source gap in the receipt; it does not confer readiness. These bounded structural
checks do not certify every command, actor boundary or business rule. Review
controls and full paths against source meaning; do not complete a fixture product
as a substitute for checking the general mechanism.

Forward relations determine columns across the whole map, including branch origins
and named merges. A lower branch cannot restart to the left of its trigger.
Forward cycles fail; classify actual recovery/return relations, never delete them
to satisfy the layout. A `return` needs a human `label` and nonempty `retained`
list. It produces a named destination reference with secondary locator and keeps
the exact original relation in `.canvas.producer.json`. Verify the real target;
this is not a native jump to the node. Other cross-map links belong in card bodies
with actual caller-specific entry/result/cancel context.

`navigation` is optional Markdown containing the actual scenario/module links;
verify their completeness against delivered files. `notation` may localize known
roles with `label` and `description`; `labels` may localize `navigation`, `legend`,
`target`, `continuation`, `content`, `controls` and `behavior`. Every used role gets an explanation with the same
role swatch in one compact legend panel, using the bundled assets. The CLI
copies needed swatches next to the output; Python callers must also call
`write_producer_assets(output_directory, audit)`. Preserve the native theme-color
qualification above. Do not make one full card per legend entry. No unused code
family is introduced.

Markdown height preparation accounts for headings, paragraphs, lists, rules and
visible link aliases; it preserves content, grows rows and never truncates text
to match a neighbour. Cards may specify `width` (default460, actions260) and `minHeight`.
`layout.columnGap` defaults to400 and `layout.laneGap` to160; these are adjustable
presentation defaults, not universal design rules. Layout proceeds by columns:
prefer the incoming block's centre, then resolve collisions only inside the target
column, preserving explicit lane order. A tall unrelated block never stretches a
whole global row. The nearest predecessor in the same lane anchors a continuation;
a join without one uses the middle incoming centre. An action stays centred on its
origin unless a real local collision requires displacement. Lanes order branches,
not fixed absolute Y coordinates. Do not pack backward into earlier columns or
hide a return/merge to improve geometry.
Embeds require explicit measured `mediaHeight`; unknown rendering is not a tiny
placeholder. The native-informed profile remains an estimate: inspect the exact
native revision and adjust the profile or explicit measured height on evidence.
Do not call fallback inspection native acceptance. Preserve first failures and
validate reader text, graph behavior and native fit as separate claims.


### Shared legend for a linked project

Python callers use `produce_project(specs)` with the complete list of project map
specifications. It derives one `project_legend(specs)` and calls the producer for
each map with the same roles, code families and localized definitions. Write each
returned Canvas/audit and call `write_producer_assets` for its destination. This
reads no external vault and creates no separate notation registry.

For separately executed CLI calls, compute that same contract once and include
it as `projectLegend` in each spec; recompute when project-used roles change.
The producer rejects a contract that omits a local role. A single-map call without
this contract explicitly reports `legendScope: single-map only`, not project
completeness. Conflicting localized project definitions fail rather than silently
producing different meanings on different maps. Unused Fab roles stay out.
