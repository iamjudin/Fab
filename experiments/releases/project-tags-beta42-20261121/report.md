# Fab beta.42 distribution — 2026-11-21

Fab 0.1.0-beta.42 is published as a GitHub prerelease and installed and enabled
in the main Codex profile. The tag resolves to `8ecc640e790a00f50a9ce16c36643309ca0a0248`.
The 102-file package fingerprint is `fd74fdba2c5ea4e8`.

The release uses the public beta.41 baseline and the FAB-10 source removal.
Project decision and artifact provenance still records the source and known
revision. The former source-note tagging policy, references and tool are absent.
The separate Design System workstream and other unpublished changes are excluded.

All 197 regressions, package and scope checks, and branch and tag CI passed.
All three downloadable assets matched the uploaded bytes. A clean Codex
profile and the main installation matched the tag and all 102 source files.
Settings for the other 19 plugins were preserved. An initial clean-install
test harness used a TOML module unavailable in the local Python. The
corrected harness passed before the main installation.

GitHub reports a prerelease without server-enforced immutability. To roll
back, reinstall published beta.41. This records installed package parity.
Application behavior after resuming an existing chat remains unobserved.

[Receipt](receipt.json) · [GitHub Release](https://github.com/iamjudin/Fab/releases/tag/v0.1.0-beta.42) ·
[Branch CI](https://github.com/iamjudin/Fab/actions/runs/44825107891) · [Tag CI](https://github.com/iamjudin/Fab/actions/runs/44825176423).
