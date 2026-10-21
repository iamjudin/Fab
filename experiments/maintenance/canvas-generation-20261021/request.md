# Local chat search — accepted behavior

Create a readable Obsidian Canvas screen-flow for finding a message in the
currently open chat with Lena. Use Fab Wireframe and the smallest sufficient
representation. The requirements below are accepted behavior, not a request to
redesign the messenger. Artifact text stays Russian.

Canonical identities and behavior:

- S10 is the existing chat. Before search it has a scroll position and an unsent
  draft. Search never sends or alters that draft.
- M10 is search within this chat. The query starts empty. Entering a query and
  searching invokes A28. This does not search people or other chats.
- A28 performs the search. Example query: «семь».
- S10-found is the found state of the same S10, not a new application screen.
  Example: two matches, selected one of two, message «Буду в семь». Next/previous
  steps between matches. Clear empties the query.
- S10-no-match is the empty-results state of the same S10. Example query «семмь»,
  zero matches. Change the query and search again through A28; clear empties it.
- E28 means history is unavailable, so completeness of results is unknown. Retain
  the query and allow retry through A28. It must never be shown as zero results.
- Closing search from entry, found, empty or unavailable restores the same chat,
  its pre-search scroll position and the existing unsent draft. A failed search
  does not clear the query or invent a successful result.

No evidence of distinct functional callers reusing this search has been supplied.
Draw enough of the flow to inspect the actual paths and outcomes. Keep the
canonical identities; documentary frames may have their own IDs. Do not change
scope, add persistence, invent navigation or remove alternate behavior for fit.

Return only a JSON object with keys `canvas` and `assessment`. `canvas` contains
the complete Canvas `nodes` and `edges`, including geometry. `assessment` briefly
explains the chosen representation and any unverified claims. Do not write files
or execute a generated edit. Root will save and inspect the original result.
