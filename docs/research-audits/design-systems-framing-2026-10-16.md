# Design-system research framing checks — 2026-10-16

This is a selected source/gap check for a new assignment, not the completed
foundation. FAB-15 owns research quality and method refresh. Main proposes a
separate research chat and the creator explicitly accepts its creation/handoff.

## Existing source and specific limits

The retained design-system brief covers tokens, semantic roles, components,
states, representative composition and lightweight governance. That knowledge
remains useful. Its full packet is preserved unchanged.

R007 defaults to a separate designer, developer and owner. It does not establish
the minimal workflow for one creator and an agent. R032 lists tools without a
documented operation/recovery contract. This is a coverage gap, not a claim that
those tools are unusable. R036 calls string dimensions such as `4px`
DTCG-compatible. The [2025.10 dimension format](https://www.designtokens.org/tr/2025.10/format/#dimension)
requires an object with numeric value and unit for a dimension value. That example
must not be reused as a valid 2025.10 token without conversion/validation. A JSON
parse alone would not establish conformance. No full packet or runtime repair is
performed as part of this framing.

## Current primary-source anchors checked

- [Figma MCP tools](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
  documents both design/code reading and native canvas writing, system discovery
  and code mappings. Do not frame the new study around an assumed read-only MCP.
- [Write to canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)
  distinguishes current write capability and prerequisites. Account-specific
  availability and successful execution here are not established by documentation.
- [Code Connect](https://developers.figma.com/docs/code-connect/)
  describes component/code connections with plan/seat conditions. A mapping is
  not independent evidence of lossless bidirectional design/code synchronization.
- [DTCG reports 2025.10](https://www.designtokens.org/tr/2025.10/)
  provides the versioned starting point. Pin exact modules and verify examples,
  rather than calling a convenient JSON dialect standards-compliant.
- [Atomic Design, Chapter 2](https://atomicdesign.bradfrost.com/chapter-2/)
  presents atomic design as a mental model, not a linear process. Its five
  levels do not automatically mandate five delivery stages or directories.

These are selected opened primary documents, not an exhaustive tool, plan,
platform or empirical audit. Search snippets alone were not treated as a test.
No Figma API was invoked, account plan inspected or design-system build executed.
Prices, limits, framework support and guarantees need current evidence in the
actual study. The local tool surface may differ from published documentation.

## Creator references and research implication

The naming/color tables are evidence of a candidate scheme. Complete names can
disambiguate repeated Primary labels. The image numbers do not establish alpha
values. Compare retaining, minimally revising and replacing the scheme against
semantic clarity, agent selection, contrast, theme/context changes and migration
cost. Do not decide a universal grammar from one screenshot.

[Assignment](../research-briefs/agent-design-systems-foundation.md) covers a
concept-to-system method, architectural alternatives, agent operations, recovery,
working component behavior and a future bounded validation plan. The research
title/body are independent. [Handoff](../handoffs/design-systems-research-2026-10-16.md)
keeps Fab ownership, creator references and project application separate.
