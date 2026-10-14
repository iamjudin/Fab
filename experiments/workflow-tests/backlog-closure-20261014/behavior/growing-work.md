I’m using the local Cowork skill. I recommend treating the desktop viewer as a separate workstream: its own model, interaction design and layout-engine comparisons need sustained discussion and evidence. Mixing those decisions into routine maintenance would make both harder to track.

The proposed boundary is:

- **Main:** plugin maintenance, shared compatibility decisions and release ownership. Viewer progress should not become a prerequisite for unrelated maintenance releases.
- **Viewer:** define the intended experience, compare alternatives and validate selected interactions. Keep engine selection open until the required behavior and comparison criteria are clear.
- **Coordination:** viewer findings that affect shared plugin behavior return to main as explicit proposals. Maintain one canonical backlog, with separate maintenance and viewer sections.

For eventual implementation, I recommend a dedicated viewer branch and, if work runs concurrently, a separate checkout. A separate viewer chat would also help contain its iterations; that is a recommendation only, with no chat or branch created here.

Before implementation, the next useful step is to agree on a bounded first viewer slice: its primary user task, essential interactions, non-goals and observable success criteria. That gives us a basis for comparing layout engines without choosing one prematurely.

No files were changed, and no external actions were taken.