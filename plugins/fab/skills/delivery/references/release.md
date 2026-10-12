# Release mode: scope and honest readiness
Resolve release object, canonical source, requested version/channel/audience,
rollback and authorization. Local install, repository visibility, push, tag,
GitHub Release and marketplace publication are distinct outputs; no implicit
public release from a repair or ordinary checkpoint push.

For plugin release read [Plugin](../../plugin/SKILL.md) and its runtime checklist.
Plugin owns manifest/package/assets/discovery/install compatibility; Delivery
owns organizing channel/readiness/version/evidence/rollback. App Store/native
requirements need current platform evidence, not an untested generic checklist.
Optional companion assets need own evidence only when actually present.

Before external Git actions check local Git, target remotes and actual auth;
no interactive login or new public remote by default. Preserve existing permissions
and finish authorized preparation before any genuinely needed approval. If auth
is missing, report exact action; don't label ready. CI/private/public/license
choices are scoped to the intended distribution. No compulsory issue templates,
banner or public repository for a personal tool.

For public release: README/current usage/install/update/version/license/limitations
and required release notes must match actual behavior. Relevant page metadata/
assets aren't silently stale. Before publishing, resolve the approved display name,
short/long descriptions and required icon/logo with the creator. Reuse accepted
assets; missing branding is a concrete creator choice, not permission to invent
it or call public presentation complete. Follow the intended host's current image
and text limits, and check included files as well as paths. Put practical use
cases before installation details; move lengthy technical material to linked
docs. Keep GitHub-facing copy and examples in English under the shared contract.
Check pushed source/tag/Release in the requested
channel. A branch push isn't Release evidence. Compare exact remote SHA when
raw branch content lags; report propagation delay rather than skip verification.
If install instructions changed run them in an isolated clean setup before claim.
Actual distribution path is needed for public install evidence; a local marketplace
smoke is only local evidence. Don't claim unobserved host/native interactions.

For shared standards inspect only affected downstream projects in authorized scope;
record unavailable pending owners instead of rewriting all projects. Future
learning is concrete symptom/user-use evidence, not schedule-driven audits.
Output ready/blocked/pending for each promised surface, exact evidence and limits.
Public publication is never performed just because this skill was selected.

## Executable scope gate
Read [shared release policy](../../../shared/release-policy.md). Prepare a project
release plan outside the package (so its fingerprint can bind the complete payload).
Run `python3 <delivery-directory>/scripts/check_release.py <plan.json>
--package-root <package>`, alongside package checks and actual behavior checks.
A failure stops the dependent release/install promise; fix or explicitly remove
the default promise rather than ignoring the gate. Promotion remains an authorized
action, never an automatic effect of this script.

Plan schema1: `version`, `fingerprint` (16-character sorted-path/content SHA256
payload identity), `channel` (`beta`/`stable`), `surfaces` (nonempty list). Each surface
has unique `id`, `default` boolean, `status` (`verified`/`limited`/`experimental`/
`blocked`/`unknown`), `limitations`, and `checks`: named required results with
`name`, `result` (`pass`/`fail`/`unknown`) and `evidence` (actual report/observation).
Default outcomes require passing checks with evidence. Limited defaults require
beta and disclosed bounds; blocked/unknown/experimental cannot be default.
Excluded/opt-in outcomes require disclosure. Register all promised outcomes, not
just the easiest check; native adapters and prototypes are separate surfaces.
The tool does not run tests or verify evidence truth; review actual evidence.
