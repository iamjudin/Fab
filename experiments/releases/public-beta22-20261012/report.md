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
Final version tag, GitHub prerelease/assets and exact-tag replay still pending.
The immutable tagged report is a preparation snapshot; the current report on the
maintenance lane retains final observations without moving the version tag.

## Interpretation

Success requires that another person can access the repository/release and obtain
the exact package through the documented Git marketplace route. It does not close
Canvas, native readiness or independent skill behavioral gaps. No model turn,
operator simulation or credit reset is needed for this technical distribution test.
