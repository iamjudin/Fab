# Fab beta.34 — repository integrity and scoped completion

Repository checks now verify public links/anchors/images, installation pins and
explicit task-owned leftovers. Local staged checks read the prospective commit;
CI uses committed targets and the actual push/PR/new-tag baseline. The backlog
owns current state; dated snapshots retain original mistakes and private refs.

- 105regressions, including12negative/control cases.
- Maintained documents still reject unpublished dependencies; historical snapshots
  are not current outbound-link promises.
- The checker never deletes files or treats another workstream's draft as junk.
- Beta.33 remains an unreleased public tag candidate; both initial CI failures and
  their corrections are recorded. Existing tags are preserved, not moved.

Installed skill behavior is unchanged from beta.32; runtime version only changes.
No new model/native/organic proof, automatic cleanup or semantic truth guarantee.
Previous Canvas, continuity, source and forecast limits remain.

[Development](https://github.com/iamjudin/Fab/blob/v0.1.0-beta.34/docs/development.md) ·
[Maintenance](https://github.com/iamjudin/Fab/blob/v0.1.0-beta.34/experiments/maintenance/project-integrity-20261021/report.md) ·
[Distribution](https://github.com/iamjudin/Fab/blob/codex/fab-maintenance/experiments/releases/housekeeping-beta34-20261021/report.md).
Rollback: fully published beta.32.
