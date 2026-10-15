# Project tags for reusable library material

Read when a project actually uses a person's editable library source: research,
book notes, articles, templates or other reusable material. Bundled Fab methods
need no access to the maintainer's library. Merely finding a note or mentioning a
project is not proof of use. Keep project-local source/revision provenance.

## Tags, not filenames

Use nested lowercase tags `project/fab`, `project/ujitsu`, `project/once`, or the
person's accepted project slug. In YAML `tags`, omit the leading `#`. Preserve all
existing tags, including `bookworm/research`, `bookworm/book`, `bookworm/article`,
other projects and legacy labels. Add missing tags idempotently. Never rename a
note or its heading for project use, stack prefixes or automatically undo old names.
An explicit separate rename request owns collision/link checks.

Source mutation needs actual authorization. A standing instruction to mark this
project's consumed library sources is sufficient; don't ask again per note. If
no such permission exists, offer the exact project tag once after the useful
result is ready. Declining leaves the source unchanged and never blocks the
project result. This contract is not permission to retag the whole vault.

## Keep metadata out of the reader's way

Do not add a visible “Usage in project” section, project URL, hashes or artifact
catalogue before the material. Keep processing revisions and original/brief/full
paths in the consuming project's existing provenance. If cross-project metadata
is needed in the source, keep it in one hidden EOF HTML comment:

`<!-- fab-source-usage:v1` followed by JSON and a closing `-->`.

A tag-only change does not mean the source was reprocessed or its findings accepted.
Preserve other consumers' entries exactly. Update a current project's processing
record only from verified actual processing; do not stamp a new revision during
cosmetic migration. Preserve old managed usage data in the hidden footer as history,
including old dates, limitations and paths. Never convert old links into verified
current destinations or treat a recovered URL as scientific verification.

## Safe deterministic editing

Use the bundled [source helper](../skills/research/scripts/source_usage.py), which
is independent of Bookworm and other plugins. Resolve it from the installed package.
Preview one explicitly authorized file:

```sh
python3 <package>/skills/research/scripts/source_usage.py <note.md> --project fab
```

Retain a recoverable original in the task's existing private evidence location.
Then apply using the exact reviewed `beforeSha256`:

```sh
python3 <package>/skills/research/scripts/source_usage.py <note.md> --project fab --apply --expected-sha <beforeSha256>
```

The helper preserves reader-body bytes, names, existing properties and tags, handles
common scalar/flat-flow/block tag forms, and refuses ambiguous metadata, changed
sources or symlink/hardlink targets. Unsupported YAML is a manual review boundary,
not permission to rewrite it. Review actual output and tags, not just exit code.
Optional `--record <json>` accepts an actual current-project provenance record;
its `project` must match, and a supplied `bodySha256` must match the managed-body
boundary. This is not required for ordinary tag addition. Preserve unknown records.

Only explicitly bounded, unfenced legacy `fab-research-usage` blocks are migrated.
Unmarked usage-like prose, original examples/code fences and research sections
remain intact. Existing names remain untouched. For a legacy/source boundary that
cannot be established safely, stop that file and explain the uncertainty.

After source changes, tags identify possible consumers, not their revision status.
Use recorded revisions to identify affected projects and name unknowns. Do not
open/edit/update another project, create a monitor or override accepted decisions
without its actual authorization. Follow [artifact lifecycle](artifact-lifecycle.md)
for preservation and exact scratch cleanup.
