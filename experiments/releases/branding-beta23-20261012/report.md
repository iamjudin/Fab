# Fab beta.23 — public presentation verification

Date: 2026-10-12. Primary agent, Fab Plugin + Delivery. Bounded technical checks;
no fresh model turn or behavioral claim for changed language guidance.

## Accepted scope

Creator supplied the factory icon, kept Fab as the short name, identified
Fabricator as the full name, rejected role nouns and accepted
**Fab — brainstorm, build, ship**. Discussion preceded implementation after the
creator explicitly asked to pause. This iteration raises use cases, reduces and
moves technical details, uses Tarsy as a read-only presentation reference and
separates English Git/GitHub artifacts from Russian conversation.

## Changes and checks

- The original opaque 512×512 PNG is byte-preserved in both icon manifest slots.
- Public title/subtitle/long description and examples are English. Use cases lead
  the README; install/developer details move to short linked documents.
- Runtime guidance resolves approved public branding before publication and
  uses English for new authored Git-facing artifacts. Supplied research and
  frozen historical evidence retain their recorded language.
- English commit/release/documentation rules are self-contained in Fab and are
  explicitly inherited by generated plugins.
- Fab-specific package checks now validate listing text and included PNG paths,
  container CRCs and dimensions. Real image decoding was verified with Pillow;
  this is not a general image decoder or native host UI check.
- All50regressions, package integrity and declared beta-scope gate PASS.
  Four new negative cases cover the actual missing-icon/localized-listing gap,
  escaping asset references and corrupted PNG bytes.
- Package:68files, fingerprint `7a402724db9b66ae`. No Canvas/native readiness change.

[Receipt](receipt.json) records image identity, copy reduction and scope.
Public [beta.23 prerelease](https://github.com/iamjudin/Fab/releases/tag/v0.1.0-beta.23)
uses immutable tag `v0.1.0-beta.23` at `c97c29d1d5b01af3749c9864ea790d5d78d584f3`.
[Source CI](https://github.com/iamjudin/Fab/actions/runs/38274601566) PASS.
Clean exact-tag install from an external empty cwd and task-specific Codex home
PASS; no auth/config copied and Git credential helper disabled. The resolved
snapshot SHA matches the tag; all68installed files match source, including the
unchanged original icon. Primary supported installation also has exact parity.
Anonymous downloads of ZIP/scope/SHA256SUMS PASS; every ZIP member matches source.
The README is286words versus645before, with seven English use cases before install.

Initial fetch began while tag push was still running and failed on missing tag;
the dependent plugin add then found no marketplace. Waiting for completed push
and retrying sequentially passed. This was a harness ordering mistake, preserved
here rather than reported as an untouched first-pass success.

Verified assets, receipt and source remain retained. The task-owned isolated home
and empty external cwd were removed after another cache/archive comparison.
[Official packaging metadata guidance](https://developers.openai.com/plugins/deploy/submission)
supports the image slots/text bounds; file checks are not native UI observation.

## Evidence limits

Native Codex icon/card rendering is unknown. Image inclusion and cache parity
must not be reported as UI observation. No public Plugins Directory submission.
Shared language-rule behavior has not been observed in a fresh model run.
