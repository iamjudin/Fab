# Prevent stale status and unpublished evidence dependencies

2026-10-21. Owner main, FAB-15 / FAB-09. Creator accepts the proposed maintenance
mechanisms and explicitly requests the next local/public release.

## Cause and implementation

Existing package checks protected installed runtime references, not the maintained
repository documents around it. Repeating current distribution in several indexes
and linking untracked local runners allowed a valid plugin with confusing project
state. Cleanup instructions existed, but task completion did not expose leftovers.

One repository helper, `scripts/check_project.py`, now checks maintained entry
documents plus changed Markdown. Public local paths must be in the Git index;
headings, image targets and source-version installation pins are checked. Staged
mode reads staged contents, so unstaged repairs cannot conceal a broken commit.
CI checks changes from the actual push/PR base. Fenced examples/external addresses
are not treated as local resources; symlinks do not import external documents.

Local `--task-dir` checks expose untracked non-private files only in explicit
owned directories. Useful private evidence can remain in their ignored `raw/`;
unrelated drafts do not fail. The helper never removes files. Existing scoped
retention/cleanup policy still owns deletion decisions, not an age/wildcard sweep.

Architecture and handoff entry points now link to the current backlog instead of
maintaining another live version statement. Dated reports retain historical
results. Development guidance and main instructions require the staged check and
file disposition before an owned checkpoint, without an extra registry/skill.

## Verification and limits

Twelve negative/control tests cover unpublished dependency, staged/worktree
divergence, changed-report support, deleted anchor, fenced/external examples,
owned-versus-other leftovers, stale installation pin, external symlink and task
boundary. All105regressions pass, including all twelve. Expected diagnostics in
earlier negative tests remain expected failures, not hidden suite errors.

The source package remains94files; only its version changes for beta.33. No
runtime instruction change, new model/native/organic test or general reliability
claim. Link/version checks cannot decide whether a task is truly done or prose
is truthful; main still reconciles dispositions with actual release receipts.
CI cannot see files never committed locally. Separate research/observer work is
preserved. [Release status](../../releases/housekeeping-beta34-20261021/report.md).

## Initial CI failure and correction

The first exact-source CI run fails at the new project check, before package /
regression steps. A frozen prior backlog references a heading in a separate,
uncommitted observation update. The earlier offline housekeeping check read the
working tree and therefore overstated that public-anchor boundary. Its original
receipt is retained; no observation content is published to conceal the mismatch.
[Original failed run](https://github.com/iamjudin/Fab/actions/runs/39675237661).

The repair makes committed-mode targets read actual HEAD, and explicitly treats
exact dated backlog/architecture snapshots as historical evidence rather than
current outbound-link promises. Incoming paths/anchors remain checked; current
reports still reject the same missing dependency. Two additional control tests
cover both boundaries. The original snapshot and separate observer work remain
unchanged. Then-current suite:104regressions,11new controls. The
[corrected exact-source CI](https://github.com/iamjudin/Fab/actions/runs/39677093005)
passes independently at cc65d59. Beta.33 local install/source-tag checks complete, before its later tag-baseline
failure; the roll-forward below owns final distribution.

## New-tag baseline failure and roll-forward

The beta.33 tag run exposes the all-zero baseline case: the checker scans480old
files instead of the new increment. A new contrasting test keeps an old archived
result outside the change scope while still rejecting a broken current document.
For zero-base tag/branch events, use the actual tip parent; only a repository's
first commit has no parent. Final local suite:105tests,12new controls. Preserve
both original CI failures and beta.33's public tag; beta.34 owns corrected
publication. No runtime policy or scientific verdict changes.
