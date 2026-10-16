# Agent-assisted design systems: from concept to maintainable Figma and code

Research assignment, prepared 2026-10-16. Return the report in Russian.
This is an independent domain foundation, not a design-system build request.

## Purpose and sufficient outcome

Investigate how an individual creator working with an AI agent can turn a visual
concept and product context into a small, usable and maintainable design system
in Figma and implementation code. Cover contemporary methods, atomic design,
tokens, components, platform conventions, accessibility and agent interaction.
Do not filter the knowledge through one consuming project's current skills.

Recommend a minimal sufficient approach and explain when a different architecture
becomes preferable. Occam's razor means removing unjustified machinery while
preserving real requirements, not omitting states, semantics or accessibility.
The objective is reliable reuse and change, not the largest component inventory.

Success is a decision framework, grounded architecture comparisons, a concrete
concept-to-system method and an executable validation plan. Desk research alone
cannot establish that an agent actually built and maintained a working system.
Label documented, inferred, locally observed and untested capabilities separately.

## Required research questions

### 1. What system is actually needed?

- Distinguish visual language, style guide, tokens, component library, patterns,
  product-specific components and a governed design system.
- Assess atomic design as a mental model. Compare useful alternatives, composition
  and feature-local patterns. Do not make atoms/molecules/organisms a compulsory
  directory structure or linear delivery pipeline.
- Define a sufficient first system for one creator and one product. Explain
  triggers for a shared core, extensions, multiple brands or larger governance.
- Explain when adapting platform or existing component foundations beats
  generating a new library, and when that would erase the concept's intent.

### 2. How does the agent interpret a concept?

- Compare inputs such as a concept screen, several reference screens, a moodboard,
  brand rules, existing code and an existing library. Identify what each reveals
  and cannot determine.
- Separate observed properties, inferred rules, proposals, accepted choices and
  unknown behavior. Explain how to preserve character without copying accidental
  inconsistencies or turning every sampled value into a global token.
- Identify genuinely necessary questions and safe reversible defaults. Avoid
  repeated approval of routine details and unsupported autonomous product choices.
- Describe a small representative composition that can disprove a proposed
  system before building a large catalogue. Explain how one concept can bias the
  result and when additional examples become necessary.

### 3. What token model and naming grammar work across tools?

- Compare primitives, semantic roles and optional component tokens. Explain when
  a layer earns its maintenance cost. Do not require three layers universally.
- Cover color, typography, spacing/grouping, sizing, radius, border, elevation,
  motion and other properties only where they serve real use.
- Separate theme, brand, density, platform, state, emphasis and surface context.
  Explain aliases, scopes, modes and component properties without creating a
  Cartesian product of every possible axis.
- Compare exact current DTCG format/resolver capabilities with tool-specific
  dialects and transforms. Pin the version. Provide small valid examples for
  color, dimension, typography and an alias, or name what cannot be validated.
- Explain mapping between Figma Variables, styles, API field types, exported
  tokens and code identifiers. A style, a variable and a code component mapping
  are not assumed to be the same object.
- Propose a consistent grammar with examples, descriptions, allowed values,
  units and migration rules. Test names against ambiguous selection tasks,
  cross-platform use, search and change rather than aesthetic preference alone.

### 4. How should the supplied naming approach be evaluated?

The attached reference tables use Category / Subcategory / Style / Mod.
Examples include Title/Primary, Title/BarPrimary, Label/Primary,
Label/PrimaryInverse and Label/PositivePrimary. Typography groups include title,
heading, body, caption and control. Color groups include label, stroke, fill,
surface and gradient, with common/accent/status families and emphasis levels.

Evaluate this as an input candidate, not an accepted universal specification.

- Determine whether the complete namespace disambiguates Primary as a size,
  emphasis, action type or semantic role. Repeated words alone are not a defect.
- Compare retaining it, minimally adjusting it and replacing its grammar. Give
  old-to-new examples, change cost, alias compatibility and a recommendation.
- Evaluate Common/Default omission, Inverse versus theme/surface context, status
  naming and whether gradient endpoints should be modeled as related parts.
- The color reference labels 100/60/20 and 10/3 do not establish actual paint
  values. Do not assume they mean opacity. Compare alpha-based scales, opaque
  tones and semantic mappings, including compositing over different backgrounds.
- Examine light/dark, elevated/brand surfaces, contrast, disabled appearance,
  long Russian text and large text. A pleasing swatch sheet is not evidence of
  accessibility or reliable component use.

If attachments are unavailable, use this transcription and state that exact
values, font metrics and layer structure cannot be recovered from it.

### 5. How do Figma and code share responsibility?

Compare Figma-led, code-led and shared-token approaches. For each, explain:

- The authoritative object for values, component API, behavior and documentation.
- Direction of generation and human edits. Bidirectional edits are not assumed
  to be a safe conflict-free synchronization strategy.
- Stable identities, mapping, versioning, diffs, deprecation and accepted updates.
- Detecting drift and handling a token rename, removed component, changed state
  or incompatible code API without silently losing manual edits.
- What an indie creator maintains, what is generated and when additional
  services, Storybook, build tooling or paid plugins are actually justified.

Use current primary documentation for candidate tools. Compare minimal native
Figma/code options with a token pipeline where warranted, without a product list
standing in for an architecture recommendation. Preserve mobile-first needs.
Discuss SwiftUI/iOS and Android distinctions alongside an applicable web route.
Do not equate React output, a browser screenshot or an editable Figma import
with a working native component library.

### 6. What can an agent actually read, create and update in Figma?

Make this the main implementation-facing investigation. Distinguish remote and
desktop MCP, Plugin API, REST API, Code Connect, generated native design layers,
code layers and other relevant surfaces. Recheck availability as of the report
date. Do not inherit claims that MCP is read-only or that any write tool can
publish a whole design-system library.

For material operations record capability, authoritative source, prerequisites
and remaining proof needed. Cover discovery/reuse, variables/collections/modes,
styles, component definitions/sets/properties/instances, bindings, Auto Layout,
fonts, library import/publishing and code mappings as relevant. Keep plan/seat,
permissions, client support, quotas and tool availability distinct. Unknown is
unknown. Do not invent fixed costs or promise account-specific access.

Explain the agent workflow: inspect the existing system, plan bounded changes,
create or reuse definitions, bind instances, inspect rendered results, repair
the owning definition and report a meaningful diff. Include idempotent reruns,
partial failure, interruption/resume, stale identifiers and concurrent edits.
Explain how agent-readable descriptions and component APIs reduce guesswork,
and what they cannot guarantee. Research examples are not authority to edit a
creator's live file or publish a library.

### 7. What makes the result working rather than decorative?

- Include component anatomy, appropriate states, interaction/accessibility,
  resizing, content variation, localization and platform expectations.
- Distinguish structural/token checks, actual rendering, executable behavior,
  accessibility checks and user understanding. Do not report one as the others.
- Design bounded probes for first creation, repeated creation without duplicates,
  theme/context change, long/large text, a new component, a token rename,
  interrupted write and conflicting manual edits.
- Define what can be checked mechanically and what needs visual or human
  judgment. Separate representative coverage from universal maturity.
- Measure useful maintenance cost and failure recovery where evidence exists.
  Do not infer reliability or labor savings from vendor demonstrations alone.

## Evidence and comparisons

Use primary sources: current Figma developer/help documentation and release
information, DTCG specifications, original atomic-design material, platform
guidelines and maintainers' real component/token repositories. Use empirical
studies for agent reliability or human outcomes if available. Otherwise explicitly
retain those unknowns. Tutorials and vendor case studies may illustrate practice
but do not establish independent effect sizes.

Inspect a purposeful mix of native/mobile, cross-platform and smaller code-led
systems. Explain selection, transfer limits and disagreements. Enterprise systems
are examples, not the assumed operating model for one creator. Cite pinned
versions/revisions when describing repository examples or executable snippets.

## Reader-facing deliverables

1. A concise orientation: what to build first, the main architecture choice,
   recommendation and evidence limits.
2. A map of principles, tradeoffs and conditional growth triggers.
3. Compact architecture, naming and Figma capability comparisons. Put long
   operation records in an appendix rather than a single oversized table.
4. A worked synthetic concept-to-system example. Label assumptions and show
   the same semantic decisions in tokens, Figma objects and component/code API.
   Keep it small enough to inspect. State whether code was executed or merely
   checked against documentation.
5. A practical agent operating contract covering inputs, decisions, object
   ownership, bounded writes, checks, recovery and return conditions.
6. A proposed validation plan and explicit open questions for later hands-on
   work. Do not fabricate completed Figma mutations or native execution.

## Output contract

Return clean Russian Markdown suitable for Obsidian. Use meaningful headings and
navigation. Begin with the useful answer, evidence status and main limit. Use
compact tables for genuine comparisons, lists for independent points and short
paragraphs for causes, conditions and disagreements. Keep each detailed record
once, linked from summaries. Preserve counterevidence and transfer limits.

Do not use semicolons in newly authored reader text. Preserve code and exact
quotations. Use descriptive source-title links next to supported claims and
group sources by topic at the end. State the date and versions. Prefer tables
or lists to wide diagrams. If Mermaid is essential, keep it editable and narrow
enough to read without horizontal scrolling. Do not claim rendering was checked
if it was not.

Before delivery map every required question to an answer or named evidence gap.
Validate the exact version claimed by code/schema examples. Reconcile comparisons,
assumptions and any numerical estimates. Mark unperformed experiments and unclear
source support. A plausible prompt or a well-formatted report is not proof of a
working autonomous design-system workflow.
