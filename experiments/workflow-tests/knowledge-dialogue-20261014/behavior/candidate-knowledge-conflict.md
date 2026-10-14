Keep the accepted Markdown tables. R027 is explicitly marked **historical application** by the bundled reader, so its Canvas proposal does not reopen the creator’s presentation choice.

Its useful contribution is semantic: distinguish ownership from navigation, and documentation links from runtime transitions. Keep the structure overview compact and put outcome branches in the transition table. These principles transfer to Markdown without adopting Canvas. See [R027’s full packet](./fab/shared/methods/product-structure.full.json) and the [current table guidance](./fab/skills/wireframe/references/table-view.md).

For UC-01, the presentation should make these distinctions explicit:

| Element | What to show |
|---|---|
| Ownership | Collection → item → label and edit action |
| Edit context | The selected item and its parent collection |
| Save | Commits the label change and returns to that same item, preserving collection context |
| Cancel | Discards only the current draft and returns to that same item, preserving collection context |

The main presentation risk is collapsing Save and Cancel into a generic “return” row. Their destination matches, but their effects differ. Explicit item ownership also prevents the edit action from appearing collection-wide. Confidence is high against the supplied accepted behavior.

I recommend separate Save and Cancel transition rows linked to stable structure IDs. Keep Canvas parked as an optional experiment. This completes the bounded review: R027 was inspected with the bundled reader, but no existing table artifact or running interface was supplied, so their actual fidelity remains unverified.