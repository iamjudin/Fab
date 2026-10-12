# Public distribution route — Fab beta.22

Date: 2026-10-12. Owner: primary Fab chat. Route: Fab Delivery with Plugin package
checks. This is an actual distribution test, not a simulated publication.

## Contract

Creator explicitly authorized a public GitHub release and chose to open the
existing `iamjudin/Fab` repository after review, rather than create a separate
distribution repository. MIT was explicitly selected for original Fab material.
Creator explicitly accepted retaining the personal author email and local paths
in the existing history. No history rewrite is authorized or needed for this route.

Scope: inspect exposed history/current payload, prepare documented beta.22,
validate locally, push only the release lane/tag, check real GitHub CI, publish a
prerelease, and install from the public pinned tag in an isolated Codex home.
No merge from the Canvas branch, no `main` migration, no public-directory submission.
The current release lane becomes the repository landing branch so a new visitor
sees the released README; historical bootstrap and tags are retained.

## Preflight

- Starting source: `740fa94146fd07d63035c6fe47ba4b455ae9b5f2` on `codex/fab-maintenance`, clean.
- GitHub repository PRIVATE, ADMIN access; only `codex/bootstrap-beta` and two
  historical checkpoint tags remote at review. No existing GitHub Releases.
- History/payload scan: 1,109 reachable objects, 590 distinct paths. No recognizable
  GitHub/OpenAI/AWS credential, credential-URL or private-key pattern hit. This is
  a bounded pattern scan, not a security certification.
- Seventeen tracked preview images reviewed as a contact sheet: synthetic test
  products, no real account/credential UI observed. Text references to secrets
  are methodological discussion and `persist-credentials: false` in CI.
- Personal author email and local paths occur in history. No destructive rewriting
  is attempted. Ignored raw archives, rendered scratch and mobile prototype
  candidate are not tracked and are not included in the uploaded plugin ZIP.
- Methods are attributed authored syntheses, including explicit incomplete
  citation verification. MIT applies to original material, not external sources.

## Publication and installation

Local package/reference checks PASS: 67 files, fingerprint `71349e50dbffe9c0`.
All 46 regression tests PASS; negative-fixture errors are expected assertions.
The declared beta scope is eligible; `git diff --check` PASS.
GitHub had no previous Actions runs, issues or forks at review.
First remote CI PASS: [run38269178037](https://github.com/iamjudin/Fab/actions/runs/38269178037)
for source `0763ceaf034ccabd03f699d710656271b044f794`, all check steps succeeded.
The first push failed with HTTP400/disconnect; a retry with per-command
HTTP/1.1 and 50MiB postBuffer passed. No global Git setting changed; the exact
transport cause is not proven. No oversized file or secret-pattern blocker found.

Repository PUBLIC and anonymous API access observed; default branch
`codex/fab-maintenance`, GitHub recognizes MIT. Clean remote marketplace/install
at that exact commit PASS, from an empty cwd outside the repository with Git's
credential helper disabled and a task-specific Codex home. The resolved marketplace
is the Git snapshot, not the source checkout. No auth/config was copied into that
home; the host still lists its personal catalog, but Fab resolution and all67
installed bytes match the Git snapshot/source. Initial isolated-home invocation
failed because the directory did not yet exist; creating it resolved the harness
error. No model behavior turn was run.

Primary installed runtime also updated through supported updater: beta.22,
67 files, fingerprint `71349e50dbffe9c0`, exact parity PASS.
Final version tag `v0.1.0-beta.22` targets
`8186ed6ce417dde0ca2d84a68ef5f5b3d9e543d9` and is unchanged.
Tagged source CI PASS: [run38269761589](https://github.com/iamjudin/Fab/actions/runs/38269761589).
[GitHub prerelease](https://github.com/iamjudin/Fab/releases/tag/v0.1.0-beta.22)
published at 2026-10-12T15:23:32Z with plugin ZIP, scope snapshot and SHA256SUMS.
Anonymous downloads PASS; checksums and all67 ZIP-member bytes match source.
Clean exact-tag marketplace/install PASS in a second new home, outside the source
checkout; fetched Git HEAD equals the version-tag commit. Primary cache also matches.

A real update test exposed a documentation defect: adding a new ref to an existing
marketplace rejects it as a different source. The initial update paragraph was
incorrect. Corrected sequence: remove only the named marketplace registration,
add the target ref, then reinstall the plugin. Actual rollback to historical
beta.9 PASS (57 files/fingerprint462d4cc828c5d99f), followed by return to beta.22
PASS and full byte parity. Removing the registration retained beta.9 cache until
reinstall; supported reinstall retired the old version. These observations are
specific to Codex CLI0.162.0-alpha.17.2, Git2.39.3, gh2.95.0 on this host.

The version tag/archive are never rewritten. The immutable tagged README has the
original incorrect update paragraph; maintained README and GitHub Release notes
include a clear erratum and the verified sequence. This is a real initial FAIL
and a corrected distribution route, not a claim that the first attempt was clean.
Machine-readable [receipt](receipt.json) retains source, assets, checks and failures.
The immutable tagged report is a preparation snapshot; the current report on the
maintenance lane retains final observations without moving the version tag.

## Interpretation

Observed result: the public repository, prerelease and exact-tag install are
accessible, downloaded assets match source, and corrected update/rollback commands
work in isolated caches. The initial frozen update paragraph remains explicitly
superseded by the maintained instructions. This is a bounded distribution PASS
after correction, not an untouched first-attempt PASS. It does not close
Canvas, native readiness or independent skill behavioral gaps. No model turn,
operator simulation or credit reset is needed for this technical distribution test.

## Retention and cleanup

Final receipt, downloaded/uploaded artifacts and original tracked preview images
retain the useful results. Both task-owned Codex homes, derivative contact sheet
and empty scratch cwd were removed after another asset/cache byte comparison.
Primary installed beta.22 and other workstreams/previews were not touched.
