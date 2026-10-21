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

Nine negative/control tests cover unpublished dependency, staged/worktree
divergence, changed-report support, deleted anchor, fenced/external examples,
owned-versus-other leftovers, stale installation pin, external symlink and task
boundary. All102regressions pass, including those nine. Expected diagnostics in
earlier negative tests remain expected failures, not hidden suite errors.

The source package remains94files; only its version changes for beta.33. No
runtime instruction change, new model/native/organic test or general reliability
claim. Link/version checks cannot decide whether a task is truly done or prose
is truthful; main still reconciles dispositions with actual release receipts.
CI cannot see files never committed locally. Separate research/observer work is
preserved. [Release status](../../releases/housekeeping-beta33-20261021/report.md).
