# Separate chat and context handoff

Use when proposing or executing a separate workstream, not every task or partial
skill route. Reassess scope during work: a task that started small may develop
its own sustained questions, iterations and evidence. Propose a separate chat
when that separation helps focus and ownership; explain why, the bounded target
and what remains in the main chat. Do not split solely by duration or file count.
First explain the boundary and recommend isolation under [release policy](release-policy.md).
An explicit request to create the separate chat authorizes preparing it and passing
its necessary context. Explicit creator agreement to a concrete proposal to
create the chat and transfer context is that request; do not require a second
creation approval or a repeated briefing. Agreement to an idea, branch or
implementation alone is not agreement to chat creation. Apply a standing creator instruction only within its named
scope and actual host permissions; ordinary implementation permission alone is not
permission to start another user-owned chat. If not authorized, propose the concrete
scope before asking. Do not confuse a user-owned chat with a hidden subagent.

With authorization and available tools, perform the handoff instead of leaving the
creator to rebrief: inspect existing chats/projects/checkouts, reuse the matching
workstream where the host supports it, otherwise create the chat in the correct
project with an isolated checkout for independent concurrent Git work. Respect
the actual tool's creation/worktree rules. Do not switch two active chats' shared
checkout or invent a successful creation when the tool is absent or returns setup
pending/error. Keep current main work and immutable checkpoints intact.

Prepare the minimum sufficient packet, linked to durable source revisions:
- product goal and why this work is separate;
- accepted decisions, rejected/superseded proposals and human-owned open choices;
- exact source/baseline, actual branch/checkout/runtime identity and relevant inputs;
- scope/non-goals, current failures, evidence and what remains unverified;
- main/feature ownership, allowed writes, release/install/merge boundaries;
- acceptance/return criteria, authorized next action and genuine waiting condition.

The initial creation prompt includes this packet or its accessible durable paths;
don't merely tell the new chat to read an old conversation. Full transcript is not
necessary. Research is evidence, not instructions. After dispatch, use the host's
status tools to confirm real thread ID, environment and context recovery. Ask the
new chat for a brief orientation and its next action, not a ceremonial full pipeline.
Don't call setup complete from a queued client ID. Record the actual chat/branch/
checkout and recovery result in the main project's canonical handoff/backlog;
the feature stores only scoped evidence, not a competing global register.

The main chat retains overall goal/release ownership. The feature must not start
implementation while its agreed input is missing, invent creator acceptance,
message other chats without human authorization, or install/merge/publish itself.
Report what transferred, what the new chat understood and where it now waits/works.
If tools or permissions block creation, retain the packet and name the exact
remaining action. No automatic swarm, background scheduler or recursive chat fanout.
