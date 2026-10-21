# Source → package → installed runtime
Resolve canonical repo/package root, manifest identity/version, marketplace root,
source path, actual installed state and loaded SKILL path. Root plugin.json is
current portable format; legacy .codex-plugin/plugin.json compatibility only
when host evidence requires it, one identity source. See official docs:
https://developers.openai.com/plugins/build/plugins
https://developers.openai.com/plugins/build/skills

Validate actual referenced files, skill descriptions/boundaries and package-contained
shared refs. Docs aren't mandatory runtime unless bundled/routed. Global methods
and user project evidence stay separate. Project tests don't prove installed behavior.
For a cache outcome compare full executable inventory, including shared/scripts/
assets, with SHA/fingerprint; preserve source version in experiment contract.
Resolve the [bundled runtime comparator](../scripts/compare_runtime.py) relative
to this reference, then run that script with <source-package> <installed-package>
for byte parity. Do not assume a helper under the repository root.
Source-only requested fix can finish source-only; requested install must finish
actual supported update and version/cache confirmation. Current CLI behavior is
verified, not inferred from a missing skill chip or remembered paths.
Clean installs may be needed when distribution/install instructions change;
isolated runtime not default every minor fix. No destructive cleanup without
scoped authorization/need. If fresh chat/restart is indispensable, state exact
remaining boundary without falsely declaring fresh behavioral smoke passed.
A runtime mismatch invalidates affected interpretation, not unrelated analysis.

For public packaging validate listing text and required icon/logo files against
current host limits. Include every referenced asset inside the package. Inspect
actual images and theme contrast; metadata/file checks do not prove host display.
Generated plugins inherit self-contained guidance separating conversation language
from English Git/GitHub artifacts and requiring approved public branding before
publication; do not make the new plugin depend on Fab for that guidance.
