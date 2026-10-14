Keep the accepted Markdown tables. R027 offers a historical Canvas presentation, not a reason to reopen the behavior or the creator’s format choice.

I inspected R027 with the bundled reader. Its useful principles are to distinguish ownership from navigation, separate documentation links from runtime transitions, and keep detailed branches out of the structure overview. Those principles transfer directly to tables. The [current presentation contract](fab/skills/wireframe/references/table-view.md) also defaults to Markdown and reserves Canvas for explicitly requested experiments.

For UC-01, present **Edit label as an action owned by the item inside its collection**. In the transition table, make the two outcomes explicit:

| Initiating control | State/result | Destination and context |
|---|---|---|
| Save, on success | Commit the label change | Return to the same item, preserving its parent collection context |
| Cancel | Discard only the current draft | Return to the same item, preserving its parent collection context |

The main presentation risk is wording Cancel as a generic “Back” or showing a return to the collection. That would obscure the accepted return target and draft scope. Save likewise needs both effects visible: persistence and return.

My recommendation is a compact structure table linked by stable IDs to these transition rows. Keep Canvas parked. The supplied state supports this semantic review, but provides no rendered interface or failure behavior to assess, so neither visual usability nor those additional branches is verified.