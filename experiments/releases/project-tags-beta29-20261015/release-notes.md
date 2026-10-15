# Fab 0.1.0-beta.29 — project tags without renaming

Using library material now adds `project/fab`, `project/ujitsu`, `project/once`
or the accepted project tag, keeping all existing tags and source names.
This applies to research, books, articles and other reusable material.

- Existing Bookworm, custom and other-project tags remain.
- No source filename or heading changes for project use.
- Visible managed usage catalogues move from the introduction into an optional
  hidden EOF comment, preserving technical history and verification limits.
- Cosmetic migration does not refresh processing dates, other consumers or accepted
  decisions. Existing source-write permission applies; otherwise offer the tag once.
- A contained helper previews changes, requires the reviewed source hash and
  preserves reader-body bytes. Unsupported YAML/aliases require review.

77 regressions and two bounded source behavior cases pass. The root test-input
forecast overrun is retained as process failure. Ten explicitly approved legacy
blocks were migrated with body/name/tag/history preservation; private notes and
backups are excluded from public Git. No native-render, universal YAML or
long-context guarantee. Canvas and Bookworm implementation are unchanged.

[Install/update/rollback](https://github.com/iamjudin/Fab/blob/v0.1.0-beta.29/docs/install.md)
· [Detailed changes](https://github.com/iamjudin/Fab/blob/v0.1.0-beta.29/docs/releases/0.1.0-beta.29.md)
· [Maintained distribution verification](https://github.com/iamjudin/Fab/blob/codex/fab-maintenance/experiments/releases/project-tags-beta29-20261015/report.md).

Complete package, scope and checksums are attached. Rollback uses immutable
`v0.1.0-beta.28`. Updating the package does not automatically refresh old chat context.
