# Temporary work and retained results

Apply whenever a task creates scratch scripts, downloads, renders, test fixtures
or model-run logs. This is housekeeping, not another workflow stage.

## Create and contain
Use one task-owned scratch directory, preferably the project's existing ignored
work area. If system temporary storage is needed, create a unique scoped directory;
put helpers inside it rather than scattering files in `/tmp`. Use context-managed
temporary directories for disposable checks. Keep inputs, accepted outputs and
live previews separate from disposable work. A matching filename prefix alone
does not prove ownership. Track the exact paths created by the current task.

## Retain before removing
At completion, including failure/abort when possible, extract the useful result,
findings, provenance/version, checks and actual cost. Save deliverable code and
assets in the project or the explicitly requested destination; final links point
there. Keep raw logs/frozen fixtures only when needed to explain or reproduce the
result, in the project's existing ignored evidence archive. Do not commit every
log by default, turn test products into runtime dependencies or call an archive
a publication. Verify retained files exist and match the originals before deletion.

## Clean the owned remainder
After verified retention, remove this task's disposable files and helper scripts
without a separate approval ritual. Check exact paths and ownership; refuse
symlinks or resolved paths that escape the owned boundary. Never sweep a shared
temp directory, delete by broad wildcard/age/prefix, or clean neighboring tasks,
user files or unrelated caches. Do not delete active server/preview inputs or
user-requested retained work. Stop only task-owned temporary processes no longer
needed; retained previews keep their explicit lifecycle agreement.

If ownership or retention is uncertain, leave that item and state the reason.
Record any intentional retention or blocked cleanup briefly; do not claim a clean
workspace when leftovers remain. Follow an explicit user retention request.
Deleting a delivered product/workspace is a separate action from scratch cleanup.

## Pass the rule to generated plugins
Fab Plugin must place an equivalent self-contained rule in the generated
plugin's runtime instructions. All generated skills that create temporary work
must read it; scripts should use scoped temporary directories and cleanup/finally
where appropriate. The generated package must not depend on Fab, this file,
maintainer docs or an installed cache path to know how to clean its own work.
Even a plugin without helpers must preserve user inputs and avoid leaving
temporary work behind when future tasks need it. Document retained outputs and
their paths; cleanup never removes the requested result or valuable failure evidence.
