# FAB-15 integration and release handoff

## Authorization and ownership

Creator explicitly asked this workstream to send its changes to Main Fab for
integration and a new release on 2026-10-13. Main owns integration, canonical
backlog, versioning, local plugin update and public GitHub Release under the
project's release shorthand. This packet is not proof any of those occurred.

Source branch: `codex/fab-research-readability`, managed checkout `b266/Fab`.
Base: `7c4b26f`. All subsequent commits belong to this authorized workstream.
Preserve unrelated main changes, especially observation records. No Canvas merge.

## Runtime changes to integrate

- Research assignments, synthesis and ingestion briefs share the reader contract.
- Replace the former literal Russian Deep Research footer with a localized contract
  plus topic-specific evidence/presentation planning.
- Independent topic research retains relevant conditions but separates consuming-
  project identity and decisions into an application record. Tags record use,
  not applicability. Existing brief can serve as the application.
- New topic filenames stay independent of project names. Source annotations remain
  optional and authorized. Preserve historical sources/labels, no bulk migration.
- Output review checks coverage/gaps, supporting links and conditional numerical
  consistency. Separate experiment fields and avoid duplicate full profiles.
- Keep source originals and supported lossless packets intact. No schema change,
  automatic global library, runtime bundling or other-project dependency.

Primary files are in `plugins/fab/skills/research/` plus the small source-usage
wording change in `plugins/fab/shared/project-contract.md`.

## Verification and release claims

Latest package guard PASS: 72 files, candidate fingerprint `0f58099fc60e3d7c`.
Manifest remains beta.24 only because this branch has not versioned or installed
its candidate. Release with a new version, never mutate the old tag.
Existing 50 regressions and diff checks PASS. Re-run required source checks after
integration and validate each promised install/publication surface separately.

Two creator-run raw comparisons are preserved privately. V2 improved orientation
but missed fields/coverage. V3 visibly improved independent framing and experiment
fields, but retained source-support, arithmetic and layout failures. See
[results](../../experiments/maintenance/research-readability-20261013/results.md),
[V3 assessment](../../experiments/maintenance/research-readability-20261013/v3-results.md)
and [V3 contract](../../experiments/maintenance/research-readability-20261013/v3-contract.md).

Do not claim reliable external Deep Research compliance, decision-grade research,
full source verification, native Obsidian rendering, demonstrated cross-project
transfer or Bookworm behavior. External model/effort unknown. Exported citation
loss versus missing underlying evidence cannot be resolved from the raw file.
No fresh Fab model execution validates the whole new contract yet.

## Bookworm and private evidence

[Bookworm task](../../experiments/maintenance/research-readability-20261013/bookworm-engineering-task.md)
covers Refine, Digest and Enrich with distinct semantic boundaries and targeted
fixtures. Direct helper evidence covers Refine only. No Bookworm edit, install or
task transfer occurred. Creator's message authorizes sending to Main Fab, not a
new Bookworm chat or hidden delegation. Main should keep that scope explicit.

The task-owned ignored `experiments/maintenance/research-readability-20261013/raw/`
contains creator inputs, prompt candidates, hashes and detailed private audits.
It is not carried by Git. Access it in the existing source checkout only if needed,
without copying private reports/screenshots into public history. Public evidence
contains abstract findings and synthetic examples.

## Main return action

Review and integrate the focused branch, update FAB-15 in the canonical backlog,
version and perform the authorized local update plus public release. Preserve
original failures and verification limits in release evidence. The workstream
has not installed, merged, pushed or published anything itself.
