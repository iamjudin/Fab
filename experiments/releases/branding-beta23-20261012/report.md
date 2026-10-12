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
Remote source/tag/Release, CI and public exact-tag install remain pending.

## Evidence limits

Native Codex icon/card rendering is unknown. Image inclusion and cache parity
must not be reported as UI observation. No public Plugins Directory submission.
Shared language-rule behavior has not been observed in a fresh model run.
