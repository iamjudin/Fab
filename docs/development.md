# Development

The runtime package is `plugins/fab`; the marketplace is
`.agents/plugins/marketplace.json`. Public metadata, documentation, examples,
commit messages and release notes are English. Chat language is independent.
Source research and frozen evidence retain their recorded language.

Run from the repository root:

```sh
python3 -B scripts/check_package.py
python3 -B -m unittest discover -s tests -q
python3 -B scripts/check_fab_release.py
```

Package checks include declared branding assets. The scope gate checks promises
and identity, not whether every behavior works. Inspect relevant outputs and
host behavior before making a readiness claim.

[Working index](../AGENTS.md) · [Beacon](beacon.md) · [Backlog](backlog.md) ·
[Handoff](handoff.md) · [Project journal](project-journal.md).
