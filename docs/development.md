# Development

The runtime package is `plugins/fab`; the marketplace is
`.agents/plugins/marketplace.json`. Public metadata, documentation, examples,
commit messages and release notes are English. Chat language is independent.
Source research and frozen evidence retain their recorded language.

Run from the repository root:

```sh
python3 -B scripts/check_package.py
python3 -B scripts/check_project.py
python3 -B -m unittest discover -s tests -q
python3 -B scripts/check_fab_release.py
```

Before a focused checkpoint, stage only its intended public files, then run:

```sh
python3 -B scripts/check_project.py --staged --task-dir experiments/maintenance/your-task
```

The local check reads the Git index: an untracked local file cannot satisfy a
public link. It checks changed Markdown plus maintained entry documents, anchors,
image paths and current installation pins. Explicit task roots expose forgotten
non-private files without treating another workstream's drafts as errors. Classify
each leftover: stage a public deliverable, retain useful private evidence in that
experiment's ignored `raw/`, or remove exact owned disposable work after retention.
The checker never deletes files. GitHub repeats public-document checks against the
push/PR base; it cannot inspect files that were never committed locally.

With `--base-ref`, both documents and their targets are read from committed HEAD,
so a local unstaged heading cannot conceal a broken public reference. Exact dated
`docs/backlog-history-YYYY-MM-DD.md` and `docs/architecture/history-YYYY-MM-DD.md`
snapshots preserve original mistakes/private references and are not maintained
outbound-link promises. Links into their actual files/headings are still checked;
current docs and ordinary reports do not receive that exemption.

Current task/distribution state belongs to [the backlog](backlog.md). Architecture
and handoff indexes point there; dated reports preserve what happened at the time.
At release completion, reconcile included task dispositions with the actual
distribution receipt. Link/version checks cannot decide whether prose is true or
whether an unresolved behavioral defect is fixed; that review remains main's job.

Bundled Fab method briefs keep their current policy owner in an explicit
`## Application in current Fab` section. That section links a package-local
shared policy or skill/reference outside the preserved method set. A source packet
or another brief alone is not an executable owner. This is the maintainer
package contract, not a compulsory heading for every project research report.
The guard checks the boundary and reference, not semantic applicability or use.

Package checks include declared branding assets. The scope gate checks promises
and identity, not whether every behavior works. Inspect relevant outputs and
host behavior before making a readiness claim.

[Working index](../AGENTS.md) · [Beacon](beacon.md) · [Backlog](backlog.md) ·
[Handoff](handoff.md) · [Project journal](project-journal.md).
