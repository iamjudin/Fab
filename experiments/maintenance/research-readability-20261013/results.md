# FAB-15 result and return packet

## Result and recommendation

The correction makes reader architecture an explicit part of research assignment
design and applies one reusable contract to synthesis, Deep Research prompts and
ingested briefs. Recommend integrating this focused correction after main-owner
review. It addresses the missing presentation boundary without changing research
scope or the lossless packet format. It is not installed or released.

Recovery verified from the supplied handoff and private references on 2026-10-13.
Checkout: the managed `b266/Fab` worktree. Branch:
`codex/fab-research-readability`, created from `7c4b26f`.
The creator-authorized scope was recovered without another briefing.
The main chat owns the canonical FAB-15 backlog and release decisions.

## Definition, application and review

| Layer | Change |
|---|---|
| Definition | New runtime `research/references/reader-contract.md` |
| Entry point | Research skill explicitly loads it for assignments, synthesis and human briefs |
| Deep Research | Replacement output tail and required topic-specific presentation plan |
| Ingestion | Human brief uses the contract, original and full packet stay preserved |
| Example | Synthetic before/after and assignment plan, no private research copied |
| Bookworm | Separate Refine/Digest engineering task and direct Refine helper reproduction |

The former literal Russian output tail is explicitly superseded by this authorized
correction. The canonical repository contract is English and is translated into
the requested report language when used. Older prompts and frozen evidence remain
unchanged. An external research result still needs review after generation.

## Evidence and limits

- `python3 scripts/check_package.py`: PASS, 70 files, candidate fingerprint
  `a6ba436383630a37`, manifest still beta.24. This is a source candidate, not
  installed beta.24 parity. Do not publish these edits under the old version.
- `python3 -m unittest discover -s tests -q`: 50 tests PASS. Printed ERROR lines
  are expected negative-path fixtures. No new packet or runtime algorithm.
- `git diff --check`: PASS.
- Direct Bookworm helper probe: dense paragraph remains verbatim, compact labeled
  fields become a table. No Bookworm modification, vault transfer or model turn.
- Source review: two private positive examples and a failing report/prompt were
  sampled for structure, not fact-checked. No private excerpt, screenshot or raw
  source path is included in the public candidate.
- Manual semantic review of [example](reading-example.md): see the mapping below.
- No fresh model behavior test, actual Deep Research run, native Obsidian rendering
  or creator reading observation. Deterministic regressions establish package and
  packet compatibility, not compliance by future model outputs or reader value.

### Example semantic mapping

| Original meaning | Reader view location and review |
|---|---|
| Six-person pilot with four guided and two free-entry completions | Comparison table retains counts, without inventing per-group denominators |
| Required fields help starting, two participants find them restrictive | Guided row and short argument preserve benefit and objection |
| Both free-entry completers already journal | Free row and causal explanation retain the confound |
| One session, repeat use unmeasured | Evidence boundary and causal explanation |
| Candidate for another trial, no proven retention effect | Opening states recommendation and limitation |
| Match experience, equal time, repeat sessions | Trial conditions retain all three cumulative requirements |
| Partial saving accepted, mode undecided | Opening and trial conditions retain decision status |
| Exact quote and identifier contain semicolons | Preserved evidence retains both exceptions |

Review caught and corrected a draft table denominator error before checkpoint:
“4 of 6” and “2 of 6” wrongly suggested six participants in each mode. The final
table uses completion counts only. This is precisely why a semantic mapping is
necessary even when the layout looks cleaner.

## Bookworm conclusion

The helper boundary is now reproduced, not merely assumed. It has no general
paragraph restructuring pass and deliberately retains long labeled prose. Refine's
instruction to preserve prose leaves the model's structural editing permission
ambiguous. These are actionable boundaries, but not proof that the entire
end-to-end workflow always fails its existing reader gate.

Recommend explicit semantic-preserving model editing after cosmetic cleanup,
followed by bidirectional claim/condition/source review. Keep the helper's guard
against prose-heavy tables. Bookworm owns its diagram-preservation policy, which
currently disallows splitting. The [engineering task](bookworm-engineering-task.md)
keeps that distinction and defines realistic fixtures and return evidence.

Creator extended this task to Digest on 2026-10-13. Read-only inspection confirms
that Digest already includes research information architecture, section coverage,
mechanisms/examples/limitations, visual preservation and reader review. The task
now applies the common reader contract during Digest composition and its quality
gates, with separate section-coverage and bounded Q&A checks. Digest's permitted
synthesis remains distinct from Refine's stricter preservation. No Digest behavior
probe was performed, and the Refine helper receipt is not evidence for Digest.

## Return criteria and integration proposal

Delivered:

- Runtime reader requirements and replacement prompt contract.
- Reviewable synthetic reading sample and assignment example.
- Bookworm engineering task with diagnosis, allowed edits, invariants and checks.
- Bounded evidence and explicit limits, with a local verified checkpoint.

Main owner can review or cherry-pick this branch, update the canonical FAB-15
record and decide any installation or versioned release. Integration authorization
is not inferred from this workstream. A useful follow-up is one fresh-context
research assignment/synthesis check and an actual Obsidian reading observation.
These would test the remaining behavior and rendering boundaries without a full
research rerun. Bookworm implementation requires its own authorized project task.
