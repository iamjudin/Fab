# Fab — coauthor skills for indie creators

Fab helps you assess an idea, explore alternatives, use research, define product
behavior, organize an interface, build an executable prototype, engineer a plugin
or prepare delivery. Start with the task you need; a full pipeline is optional.
The working language is Russian, with direct recommendations and explicit evidence.

**Public beta: 0.1.0-beta.22.** Mobile apps are the current focus. Browser prototypes
check selected interactions; they do not establish native or production readiness.

## Install in Codex

Use a Codex client with plugin marketplace support. Install this fixed release:

```sh
codex plugin marketplace add iamjudin/Fab --ref v0.1.0-beta.22
codex plugin add fab@fab-local
```

`fab-local` is the existing marketplace identifier, including for Git installs.
The package is `plugins/fab`; it includes its methods and does not need the
maintainer's Obsidian vault, other plugins, or development reports.
The package has no MCP server or external service credentials of its own.
Research, Git and UI tasks use capabilities available in your host environment.

For later releases, select the new release tag with the same marketplace-add
command, then run `codex plugin add fab@fab-local` again. Review the new release's
limits first. To return to this version, select its tag and reinstall. A pinned
marketplace stays on its selected release; it does not follow development commits.

The commands follow the [official plugin packaging documentation](https://developers.openai.com/plugins/build/plugins)
and the installed CLI. Distribution-test results are recorded in the
[release report](https://github.com/iamjudin/Fab/blob/codex/fab-maintenance/experiments/releases/public-beta22-20261012/report.md).
This GitHub distribution is separate from publication in the public Plugins Directory.

## Use

Choose a Fab skill in your client, or explicitly name it in the request. Examples:

- **Fab Analysis:** «Оцени этот существующий онбординг: где пользователь застрянет?»
- **Fab Brainstorm:** «Предложи три подхода к приложению для сборов в поездку и выбери лучший для первого теста».
- **Fab Product → Wireframe:** «Уточни поведение редактирования, затем обнови структуру существующего интерфейса».
- **Fab Cowork:** «Продолжим проект: восстанови решения, открытые вопросы и следующий полезный шаг».

The ten independent skills are Cowork, Research, Analysis, Brainstorm, Testing,
Product, Wireframe, Prototype, Plugin and Delivery. Each can produce a bounded
useful outcome. Explicit instructions and project agreements determine scope;
ordinary changes do not authorize public releases or messages to other people.

## Beta limits

- Structure and scenarios default to Markdown tables. Canvas is opt-in and
  experimental: labels can overlap; native Obsidian rendering is unverified.
- Executable prototypes have evidence for selected browser paths. Device,
  native, offline, payment and production guarantees need their own checks.
- Fresh-context tests support bounded independent tasks and partial routes.
  They do not prove that every skill succeeds on every input in this version.
- Automatic chat handoff depends on host tools; sustained continuity and the
  last queued Canvas-chat recovery remain unverified.
- Research citation coverage is partial. Recheck changing platform, legal and
  economic claims against current primary sources before using them.
- Temporary-output cleanup and cross-project research updates still have
  open behavioral cases. Read [known work](docs/backlog.md) before relying on them.

See [release notes](docs/releases/0.1.0-beta.22.md) and
[scoped readiness](docs/release-policy.md). A valid package is not whole-product approval.

## Development

```sh
python3 -B scripts/check_package.py
python3 -B -m unittest discover -s tests -q
python3 -B scripts/check_fab_release.py
```

[Working index](AGENTS.md) · [Beacon](docs/beacon.md) · [Backlog](docs/backlog.md) ·
[Handoff](docs/handoff.md) · [Project journal](docs/project-journal.md).
Development reports include retained synthetic test products and historical failures;
those products are evidence, not Fab's product roadmap.

## License

Original Fab code, instructions and authored documentation are available under
[MIT](LICENSE). Referenced third-party materials retain their own rights;
see [notices](NOTICE.md). Please retain attribution when redistributing Fab.
