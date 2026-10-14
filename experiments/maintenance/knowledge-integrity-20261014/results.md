# Knowledge integrity refactor — results

Date: 2026-10-14. Owner: main Fab, FAB-15. Source-only maintenance PASS within
the inspected boundary. Additional investigations are creator-rate-limited, not
silently replaced. Installed/public beta.27 remains unchanged.

## Judgment and scope

The cleaned knowledge/application boundary is coherent across shared principles,
the ten active skill entries, nine method briefs, Research reuse/ingestion/output
contracts and actual reader/package checks. Relevant knowledge is conditional
input, historical material is not current authority, and additional foundation
research is not a prerequisite for ordinary partial work.

Confirmed holes concern ingestion safety, source/index interpretation and release
validation relationships. The old structural PASS checked internally retained
text but missed drift between source identity, declared authority, registry and
discoverability. Correct those owning mechanisms rather than adding another
general instruction about careful work. This is a bounded audit, not proof that
every project behavior is free from logical errors.

## Original failures and corrections

| Finding | Before | Corrected boundary |
|---|---|---|
| Original overwritten | `build` with source as output succeeds and replaces the source with JSON. | Refuse identical file identity, including symbolic/hard links, before any write. |
| Source bytes changed | CLI ingestion normalizes CRLF/CR line endings, so its source fingerprint differs from the actual UTF-8 original. | Read without newline conversion, retain exact source text and hash. |
| Exclusion intent lost | An absent requested heading is silently ignored. Excluding the level-zero preamble excludes the entire following report. | Reject unknown titles, stop a preamble exclusion at the first real heading, preserve explicit exclusions separately. |
| Code misindexed | A shorter/different fence or a fence with trailing text toggles the parser, turning example headings into sections and hiding later real headings. | Match fence character, minimum closing length and permissible trailing whitespace. |
| Source metadata unchecked | A no-exclusion packet with a false source hash or promoted runtime authority still validates. | Check supported schema/source authority, source-versus-retained hash when complete, and disjoint retained/excluded IDs. |
| Registry detached | A mismatched registered hash still passes. Missing/duplicate pairs and classification-summary drift are unchecked. | Verify actual pairs, source identity/title, context counts, scoped paths and complete packet inventory. |
| Discovery incomplete | A blank line breaks the method table, leaving two methods outside its rows. | Restore the table and require each registered brief in its decision rows, with a link to the correct full packet. |

The fence correction follows the relevant character/length/closing rules in
[CommonMark 0.31.2](https://spec.commonmark.org/0.31.2/#fenced-code-blocks).
The reader is still a limited ATX sectioner, not a full CommonMark renderer.
Nested containers, every Markdown heading form and native presentation are not
claimed. Historical packets are never rebuilt merely because the parser changed.

Original reproductions are retained in ignored `raw/baseline-probes.json` and a
frozen baseline package. No user original was modified to reproduce a failure.
Disposable fixtures were context-managed and removed on completion.

## Verification and preservation

- **66 regressions PASS**, including 12 added test methods with additional variants
  for line endings, mixed/unequal/unclosed fences, identity aliases, unknown
  exclusions, preamble boundaries, source authority/hash, exclusion overlap and
  registry/brief/index drift. Expected negative-fixture diagnostics remain normal.
- Package guard PASS: **72 files, `891e6db46b47b4bf`**. Baseline source was
  `6b0b0537851e5a1c`. Runtime changes are the method index, ingestion reference
  and reader. Maintainer guard now uses the reader validation instead of repeating
  the retained-content hash check and adds registry correspondence checks.
- All **nine full packet files are byte-identical** to the baseline, including all
  **437 original sections**, metadata and provenance. All nine validate through
  the corrected reader. An actual selected R027 read retains historical context.
- Legacy packets produced by the supported builder remain compatible without
  optional reading context. No new packet schema, external dependency or mandatory
  full-library read. An excluded packet's source hash still requires correspondence
  against its preserved original, as explicitly documented.
- Architecture documentation now separates current knowledge ownership from older
  beta checkpoints and correctly identifies Delivery as the implemented release
  owner. Source readiness is distinct from installed beta.27 availability.
- [Receipt](receipt.json) retains exact package fingerprints, changed paths and
  all packet-validation results. Before/after packages remain in ignored `raw/`.
  No model turns, reset, account-limit inference, provider launch, native audit,
  library edits, other-project changes, installation, push or release.

## Open limits and next action

This refactor prevents concrete structural/safety failures. It does not independently
verify source citations, rebuild domain knowledge or establish useful long-context
behavior. Existing attribution gaps and the real conversational dead-end evidence
remain open. Integrity hashes detect inconsistency, not deliberate replacement
of an original by a different self-consistent source or scientific correctness.

Main owns the reviewed source candidate, which includes the preceding cleaned
knowledge and handoff/method corrections. Recommend it for the next separately
authorized local/public release, then calibrate actual use instead of repeating
synthetic full pipelines. No release authorization is inferred from refactoring.

Creator-run [initiative](../../../docs/research-briefs/collaborative-initiative-deep-research.md)
and [evaluation](../../../docs/research-briefs/multi-turn-collaboration-evaluation-deep-research.md)
assignments remain prepared until access is restored and the creator chooses to
run them. Main reviews complete returns before ingestion and local application.
No unsupported estimate of the research-limit reset time. Canvas and Bookworm
retain their separate owners/boundaries, the observer remains read-only toward
the observed project.
