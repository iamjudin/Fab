# Research readability workstream packet

## Goal and creator requirements

Improve Fab's research assignment design and output requirements so human-facing
reports are useful to scan and read in Obsidian. Prepare a separate engineering
task for Bookworm so post-processing improves information architecture rather
than only export syntax. The creator supplied a structured market study and a
concise integrated report as positive references, with reservations about both.

- Replace dense prose and inline enumerations with meaningful structure.
- Use compact tables for comparisons and repeated short fields, lists for peer
  items and procedures, short prose for causal arguments and necessary context.
- Preserve evidence, exceptions, qualifications, accepted decisions and source
  traceability. A complete research archive need not be pasted into the reader report.
- Avoid horizontal Mermaid scrolling. Top-to-bottom direction alone does not
  establish readability. Prefer a table/list when it explains the relationship.
- The latest creator instruction bans semicolons in newly authored reader prose.
  Convert independent items to a list and connected arguments to short sentences.
  Preserve source quotations and code punctuation. Do not use this as a synonym
  for blindly converting every sentence into a bullet.
- Reconsider the old mandatory Deep Research output tail explicitly. The creator's
  newer request supersedes its earlier verbatim requirement for this correction.

## Source and work ownership

Main project: Fab, codex/fab-maintenance at515a7f5, installed/public beta.24,
69files/fingerprint24fcdfca505a5a13. No runtime edit has been made for readability.
Main chat owns canonical backlog, release decisions and default installation.
Canvas remains separate and parked. An unrelated pending observation-record
change in the main checkout must be preserved and excluded from this workstream.

The feature owns Fab Research prompt/output guidance, its bounded verification
and a reviewable Bookworm task packet. It may read supplied examples and relevant
Bookworm source/runtime to diagnose boundaries. It must not change Bookworm,
other product repositories, Brain source documents or frozen research evidence.
An actual Bookworm change belongs in that project after a separate scoped handoff.
No public release, shared runtime installation or merge is authorized by chat
creation. No subagents or further chats without explicit creator authorization.

## Findings already established

1. Fab's Deep Research tail specifies Markdown, headings, citations and conditional
   tables but leaves reader information architecture and paragraph density largely
   undefined. Topic prompts request many heterogeneous evidence fields without a
   corresponding presentation plan. Prompt breadth is not by itself a defect.
2. Bookworm Refine already includes compact tables, portrait Mermaid and a reader
   review. It also preserves source prose and prohibits default summarization.
   A correction needs a clear semantic preservation/structural editing boundary,
   not another duplicate table rule. Its large helpers have not yet been audited
   or tested for the long-paragraph case. Do not claim the exact root cause proven.
3. Sample text inspection supports the creator's complaint. The positive market
   reference has9,363words,193prose paragraphs,47table headers and a longest prose
   paragraph of71words. A supplied science report has3,094words,28prose paragraphs,
   no tables and three paragraphs above120words. The corresponding vault note
   still has the same longest129-word paragraphs. These rough counts are diagnosis
   aids, not quality thresholds or proof of causality.
4. A sampled Fab method report already has20tables but a long introductory block.
   Merely increasing table count cannot be the acceptance criterion. The newer
   integrated product report provides a stronger mix of comparisons, evidence
   limits, short causal explanations and optional-support lists.
5. In the reference, a portrait Mermaid graph still has multiple parallel branches.
   Actual width/label readability needs inspection or an explicit unverified limit.

## Next authorized work and return criteria

Read the private input references, inspect the relevant Bookworm helper boundary,
then implement the smallest coherent Fab correction. Prefer one reusable reader
contract, a short prompt-tail form and task-specific evidence/presentation choices
over a universal long template. Route Research synthesis, prompt preparation and
the human brief to that contract while preserving immutable original/full packets.

Prepare a Bookworm task with the diagnosed scope, proposed semantic-preserving
restructuring, source/claim/link invariants and realistic checks. Include actual
positive and failing example paths only in private handoff material. Do not copy
private research or screenshots into the public Fab history.

Validate references and appropriate existing guards. If behavior probes add useful
confidence, record a bounded contract, real model/effort, cost, original failures
and limits, with synthetic or ignored-private inputs. No statistics-only reruns.
Provide a concrete before/after reading sample and own judgment. Do not call native
Obsidian readability checked from Markdown counts alone. End with results and a
reviewable integration proposal to the main chat, without requiring a new briefing.

Private local input paths and latest creator feedback are retained by the main
chat at experiments/maintenance/research-readability-20261013/raw/inputs.json.
That file is ignored and is not a required installed-runtime dependency.

## Handoff status

Recovery verified on 2026-10-13 in managed checkout `b266/Fab`, branch
`codex/fab-research-readability` from `7c4b26f`. The isolated chat read this packet,
private input references and applicable project guidance without another briefing.

The scoped correction, synthetic reading example, Bookworm task and checks are
complete. See [result and return packet](../../experiments/maintenance/research-readability-20261013/results.md).
Main retains canonical backlog/integration/install/release ownership. No Bookworm
edit, additional chat, subagent, install, merge or publication occurred.
