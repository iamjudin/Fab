# Install, update and rollback

Fab is distributed through the GitHub repository marketplace. Use a Codex client
with Git-backed plugin support. The marketplace identifier is `fab-local` and the
plugin selector is `fab@fab-local`.

## First install

```sh
codex plugin marketplace add iamjudin/Fab --ref v0.1.0-beta.32
codex plugin add fab@fab-local
```

## Change version

Run outside the Fab source checkout. Remove the existing catalog registration,
add the desired published tag, then reinstall:

```sh
codex plugin marketplace remove fab-local
codex plugin marketplace add iamjudin/Fab --ref v0.1.0-beta.32
codex plugin add fab@fab-local
```

Use the target tag for an update or rollback. The tested host retains the installed
plugin until reinstall. Adding a different ref without removing the existing
registration is rejected. A pinned marketplace stays on its selected release.

## Continue an existing chat after updating

After installing the new package, ask the existing chat to check the installed
Fab version, reread the current Cowork/Research instructions and relevant
references, then continue with accepted project decisions intact. A chat message
requests rereading; it does not install a plugin or advance a pinned marketplace.
Codex detects skill changes automatically; restart Codex if the updated skill is
not available. Desktop continuation and resumed CLI behavior are separate checks.
See [official skill guidance](https://learn.chatgpt.com/docs/build-skills).

For rollback, repeat the version-change commands with `v0.1.0-beta.31`.

If older global or project instructions mandate a literal research footer,
resolve that conflict with the owner. Keep general routing in host guidance and
reader requirements in the active research contract, avoiding duplicate templates.

## Environment

The package contains its methods and does not require the maintainer's Obsidian
vault or other plugins. It has no MCP server or service credentials of its own;
research, Git and UI work use capabilities available in your host. This GitHub
channel is separate from the public Plugins Directory.

See the [official packaging documentation](https://developers.openai.com/plugins/build/plugins)
and the [verified beta.22 distribution route](../experiments/releases/public-beta22-20261012/report.md).
