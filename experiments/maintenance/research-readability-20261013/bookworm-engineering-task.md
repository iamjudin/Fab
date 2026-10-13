# Bookworm engineering task: readable Refine, Digest and Enrich notes

## Requested outcome and ownership

Make Bookworm Refine produce a readable working note when an export contains
long paragraphs mixing comparisons, independent items and causal explanation.
Keep substantive content intact. Apply the same reader requirements when Digest
creates a working note from a book or standalone article and when Enrich adds
new source-backed meaning and depth to an existing note. Implement in Bookworm's own isolated workstream,
not in Fab. No Bookworm edit, install or vault transfer was performed here.

Refine remains distinct from Digest and Enrich. For Refine, the correction permits
structural editing, not summarization, new analysis or source claim correction.
Digest synthesizes the source under its existing fullness standard, preserving
mechanisms, important examples, limitations and anchors for later Q&A. A source's
unsupported claim must remain an attributed source claim unless the user separately
requests verification. Layout quality does not make the claim reliable.

## Evidence and diagnosed boundary

| Surface | Observed behavior | Engineering implication |
|---|---|---|
| `plugins/bookworm/skills/refine/SKILL.md`, Core Promise | Allows structural change but explicitly says to preserve prose | Clarify preservation of meaning versus preservation of paragraph shape |
| Same skill, note formatting and Reader Review Gate | Already requests compact tables, portrait diagrams and reader review | Connect the rules to dense paragraph editing, do not add duplicate slogans |
| `plugins/bookworm/scripts/bookworm_helper.py`, `refine_markdown` | Cosmetic passes, no general paragraph restructuring | Helper output is an intermediate copy, not sufficient reader completion |
| Helper, `convert_label_value_runs` | Converts short labeled fields, explicitly retains long values as prose | This guard usefully prevents prose-heavy tables. Keep it |
| Helper, `assert_sources_preserved` and `audit_refined_sources` | Checks source counts and added URL provenance | Counts do not prove claim coverage or source-to-claim association |
| `plugins/bookworm/skills/digest/SKILL.md`, Research Information Architecture | Already requests tables, lists, causal prose and portrait Mermaid | Apply the shared reader contract during composition, not just final cleanup |
| Same Digest skill, Fullness Standard, Workflow and quality gates | Requires section coverage, mechanisms, examples, limitations, evidence anchors and reader review | Make readability compatible with this coverage, not a reason to over-compress |
| `plugins/bookworm/skills/enrich/SKILL.md`, Content Rules and Enrich Structure Gate | Requires clearly attributed additions near relevant sections, with opened sources and no second catalogue | Preserve attribution while making the purpose and contribution of each new block explicit |
| Same Enrich skill, Obsidian Layout Rules and Reader Review Gate | Already defines compact tables, lists, portrait diagrams and labelled-block checks | Review the added meaning and combined reading path, not just block count or formatting |
| `plugins/bookworm/tests/test_bookworm_helper.py` | Existing syntax/source/handoff tests | Add targeted structural and semantic workflow cases, preserve existing safeguards |

A read-only direct-helper probe preserved a synthetic dense paragraph verbatim
and converted compact labeled fields into a table. See [receipt](bookworm-probe.json)
and [reproducer](probe_bookworm.py). The source helper fingerprint is recorded.
This proves the helper boundary for those fixtures. It does not prove that every
agent executing Refine skips its reader review, or establish end-to-end causality
for the creator's original export. Private examples remain outside public Git.

## Recommended correction

Resolve the contract ambiguity in favor of meaning preservation. Add an explicit
model editing step after cosmetic cleanup and before reader/source review.

Permit:

- Split a multi-topic paragraph into short paragraphs at actual argument boundaries.
- Move peer items into a list and procedures into numbered steps.
- Turn explicit comparisons into compact tables when the same dimensions occur
  for each item. Keep missing values unknown, do not manufacture parallel evidence.
- Extract short headings or field labels from existing meaning. Do not introduce
  a new taxonomy or turn author interpretations into facts.
- Move long explanation out of table cells while retaining its subject and sources.
- Replace semicolons in newly authored reader text with a list or short connected
  sentences. Preserve punctuation in code and exact quotations.

Preserve claims, numbers and denominators, units, populations, dates, negations,
conditions, logical relations, uncertainty, accepted decisions, source links,
quotes, code and meaningful assets. A conjunction may encode cumulative conditions.
A contrast or causal argument may need connected prose rather than a bullet list.
Do not delete disagreement or repeat an entire record in a new summary layer.

Keep the original and a baseline separately. Use a claim/condition/source mapping
for the paragraphs actually restructured, not a duplicate full research archive.
Check both directions: every original meaningful point is retained and every
output substantive point is supported. Do not rely on a regex sentence splitter,
source counts or similarity scores as a semantic acceptance gate.

For wide TD/TB graphs, inspect actual width and labels. Do not promise that changing
direction fixes the problem. Bookworm currently forbids diagram splitting and
preserves diagrams. Respect that boundary by default. If a graph remains too wide,
report it as unresolved or ask for the separate visual scope that Bookworm requires.
Any change to that preservation rule needs an explicit decision in Bookworm.

## Digest application and distinct preservation boundary

Creator explicitly added Digest to this engineering scope on 2026-10-13.
Use one self-contained Bookworm reader contract for all three modes. Do not depend on
Fab runtime or copy two divergent rule sets. Readability requirements apply to
Digest's headings, tables, lists, causal paragraphs, sources and editable diagrams.
This includes no semicolons in newly authored reader text, with exact quotation
and code exceptions, and observed diagram width rather than a TD/TB assumption.

In Digest, apply the contract while building the section/argument map and composing
each section. Recheck it in both the Internal Quality Gate and Reader Review Gate.
A cleanup pass after a dense note has already been written is insufficient.

Preserve the existing fullness standard. For each substantive section, retain
its central mechanism, important example or case, failure mode or limitation and
practical implication when the source provides them. Keep the motivation and
sequence of methods, definitions, causal links and source anchors. Mark absence
or uncertainty instead of inventing an example or implication to fill a template.
Keep essential visuals or a faithful useful reconstruction and verify asset links.

Digest may select and synthesize rather than reproduce every sentence. Its mapping
must therefore check substantive section/argument coverage and output grounding.
Do not apply Refine's requirement to retain every original meaningful point as
an obligation to copy an entire book. Do not weaken Refine's stricter preservation
boundary merely because Digest allows synthesis. Preserve originals separately.

The first reading path should help the reader orient and compare. Detailed
mechanisms and cases should occur once in their appropriate sections, with clear
navigation. Neither a short abstract nor a giant catalogue of tables satisfies
Digest's purpose as a working note for future Q&A and method application.

The helper probe above is Refine evidence only. Source inspection confirms
Digest's existing requirements, but no Digest output or fresh behavior has been
tested here. Verify its execution independently in Bookworm.

## Enrich application and purposeful depth

Creator explicitly included Enrich on 2026-10-13. Apply the common reader contract
to new content during enrichment and to the combined note before handoff.
Enrich adds substance. It must not merely lengthen the source or rephrase existing
material. Identify a relevant knowledge gap from the request and note before
researching additions. Stay within the requested focus and stop when it is served.

Each addition should have a concrete contribution, for example:

- Explain how or why a mechanism works, retaining its conditions and limits.
- Add a worked example that makes an abstract principle usable.
- Contrast a relevant alternative and explain when the choice changes.
- Add a counterexample, failure mode or applicability boundary.
- Extend an application procedure with grounded details and their reasons.

This is a set of possible contributions, not a checklist that every section must
receive. Do not invent a new taxonomy, add filler examples or repeat the original
record just to create more blocks. Claims and source material must support the
actual addition, not only share its broad topic.

Place new meaning near the relevant original section inside the existing labelled
addition format, with opened and verified source links. New topics or profiles
also stay inside attributed blocks. Use meaningful subheadings where needed,
compact comparisons, lists for peer points or steps, and short connected prose
for causal depth. Avoid long paragraphs and prose-heavy table cells. The ban on
semicolons applies to newly authored reader text, with code and exact quotations
preserved. Preserve existing visual and diagram policies and inspect actual width.

Keep original reasoning and claims distinct from external additions. Do not
silently repair unresolved original sources or present new evidence as the book
or source author's view. If new evidence disagrees, state the disagreement within
the attributed addition with its applicability limit. Do not rewrite the original
layer without explicit rewrite scope. Keep ledger evidence of each addition's
source and claim. No new metadata ceremony is needed in the reader note.

Review both the contribution and the combined reading path: can the reader see
what was added, why it helps, how to use it and where it stops applying? Verify
that the original remains identifiable and accessible, that additions do not
create a second catalogue, and that depth survives without dense prose. More
blocks, more words or more tables do not establish successful enrichment.

Source inspection confirms these existing attribution and layout boundaries.
No Enrich behavior, external-source research or enriched-note output was tested
here. The earlier Refine helper reproduction does not validate Enrich.

## Bounded verification contract

Run existing tests and separate fresh-context Refine and Digest workflows on
synthetic fixtures, plus an independent Enrich workflow. For Digest use a small multi-section book fixture and a
standalone article fixture, including an important visual.
Record actual model/effort, input/runtime revision, tools, cost and isolation.
No installation, source deletion or vault write is needed to test temporary output.

| Case | Required result |
|---|---|
| Dense independent attributes | Scannable list, all attributes and qualifications retained |
| Comparison mixed with explanation | Compact table plus causal prose, no invented equivalence |
| Necessary causal prose | Short connected argument, no automatic table or bullet conversion |
| Negation, cumulative conditions, number/denominator | Meaning and logical relation unchanged |
| Link attached to a qualified claim | Same supporting association, not merely same URL count |
| Exact quote and fenced code with semicolons | Bytes retained, authored connective text has no semicolons |
| Already readable note | No needless summary layer or structural churn |
| Wide parallel TD graph | Observed fit at target width or explicit unresolved layout status |
| Long prose-heavy table | Readable item sections, preserved fields and source associations |

For Digest, also check:

| Case | Required result |
|---|---|
| Multi-section source with comparisons and methods | Scan-friendly comparisons plus complete mechanisms, ordered steps and reasons |
| Article with a causal argument and counterexample | Connected explanation retains the counterexample and applicability boundary |
| Important case, term and essential visual | Enough context for later Q&A, source anchor and faithful visual/explanation |
| Method application question after reading only the digest | Answer accurately explains the sequence, its motivation and failure condition |
| Orientation plus detailed sections | One navigation layer, no repeated record catalogue or content-free template sections |

Audit coverage against the source map, then ask bounded questions using only the
resulting note. Distinguish this controlled Q&A check from proof that the digest
can answer every future question without returning to the source.

For Enrich, also check:

| Case | Required result |
|---|---|
| Thin explanation of a mechanism | Source-backed causal depth with conditions, no unsupported conclusion |
| Abstract principle needing application | Worked example or usable procedure that adds meaning rather than restating the principle |
| Relevant alternative or counterexample | Explicit comparison and applicability boundary inside an attributed addition |
| Unresolved original source or conflicting new evidence | Original status preserved, new evidence attributed, no silent source repair |
| Already sufficient section | No obligatory expansion, duplicate catalogue or filler block |
| Combined note after enrichment | Original and additions distinguishable, navigation and reading flow remain useful |

Use a controlled source set for reproducible Enrich fixtures and actually open
sources before attributing them. Record source availability and failures. Compare
the input and enriched copy, map added claims to their support and review whether
each addition answers the requested gap. Keep originals and vaults untouched.

Render representative notes at ordinary and narrow reading widths in Obsidian
when available. Record the actual widths and inspect overflow, label readability,
table scanning and the opening navigation. Without that surface, mark native
rendering unobserved and distinguish any browser approximation.

Acceptance requires that the reader can find the conclusion, compare the
relevant options and locate the main exception, while the semantic mapping passes.
No minimum table count, fixed compression percentage or universal word threshold.
Do not claim useful reading from Markdown counts alone. Creator preference remains
an additional human observation, not a substitute for the author's own review.

## Return packet

Return the corrected boundary and its application path, focused diff, existing
regressions, Refine before/after fixtures with semantic mappings, Digest fixtures
with section coverage and bounded Q&A evidence, Enrich additions with
contribution/source mappings, separate fresh behavior evidence for all three modes,
rendering evidence or named limitation, and remaining failures. Keep source,
transfer-confirmation and cleanup safeguards intact. Stop before install/release
unless that project authorizes them. No further chat creation is included here.

## Transfer timing

Creator asked to wait for the raw Deep Research result before transferring the
Bookworm task. Refine, Digest and Enrich are included in the prepared scope, but
no task transfer or implementation is authorized by this packet alone. First
review the new raw report against the previous report, then refine examples and
remaining processing needs. That comparison does not substitute for independent
Digest or Enrich behavior checks.

## Raw comparison observation, 2026-10-13

The creator supplied the second raw report and it has now been reviewed before
Bookworm. See [comparison result](once-market-comparison-results.md). Waiting for
this observation is complete, but no task transfer has occurred or been inferred.

Add these observed pattern classes to synthetic Refine fixtures:

- Numbered experiments whose fields remain inside long paragraphs.
- Comparison tables that repeat preceding full profiles.
- Mixed-purpose cells containing multiple claims and explanations.
- New reader prose that retains prohibited punctuation.
- Unsupported substantive claims embedded in otherwise reformattable content.

Verify that structural editing preserves the claims and their evidence status.
Do not mistake improved formatting for completed economics or source verification.
Missing costs, unsupported projections or inconsistent assumptions require an
explicit substantive scope beyond ordinary Refine. No raw private report excerpts
belong in public test fixtures. This observation does not validate Digest/Enrich.

## V3 raw comparison observation

[V3 review](v3-results.md) observes independent topic framing and separate experiment
fields, but only partial overall compliance. Add HTML tables, long orientation
paragraphs, duplicate full profiles and heading/anchor mismatches to structural
fixtures. Preserve original claims and their unsupported status during layout
repair. Do not silently correct contradictory numerical models or introduce
unverified sources under Refine. Numeric/source repair requires an explicit scope.
No Digest/Enrich behavior is established by this external research result.
