---
title: 'Swarm management in agent harnesses: owning long-running agents'
topic: agents
subtopic: multi-agent
secondary_topics: []
summary: Explains swarm management patterns for long-running agent harnesses and how
  ownership/control should be structured.
source: arize
url: https://arize.com/blog/swarm-management-of-agent-harnesses/
author: Aparna Dhinakaran
published: '2026-05-04'
fetched: '2026-07-11T04:55:50Z'
classifier: codex
taxonomy_rev: 1
words: 3228
content_sha256: cf5b95bc584fbdece1712b73b65a500b671e0e7599b6790d9723025451b06bf8
---

# Swarm management in agent harnesses: owning long-running agents

*Originally shared  as an X Article on May 3, 2026.*

One thing has become clear as we have built our own harness management tools internally at Arize and watched external systems like Devin at Cognition start [managing other Devins,](https://x.com/cognition/status/2034679897084264659) [managed agents](https://www.anthropic.com/engineering/managed-agents) at Anthropic and [long-running agents](https://cursor.com/blog/long-running-agents) from Lee Robinson at Cursor: *swarm management is the next real systems problem in AI.*

Not single agents or one-off tool calls. Instead, managing swarms of long-running agents is a key challenge many are circling around in the industry right now.

Most agent frameworks have crossed the first line: they can spawn subagents.

That is not swarm management.

It is the beginning of the problem.

The interesting question is what happens after the child exists. Where does it live? Who owns it? Can it be addressed? Can it be steered? Can it finish after the parent has moved on? If the process restarts, does the system know what was still running?

This is the next layer above the agent harness. A harness lets one agent call tools, read files, run commands, and keep a loop going. A delegation tool lets one agent borrow workers. A swarm manager owns a fleet.

The core feature of an agent harness is a loop over tools. A swarm manager is a loop over running harnesses, making sure they are progressing.

![Diagram of a “Swarm Management Layer” showing how a runtime manages multiple long-running agent sessions. At the top, a “Swarm Manager” bar is divided into six lifecycle stages: Identity (session + run IDs), Policy (roles and limits), Lanes (queues and backpressure), Control (steer or kill), Completion (route results), and Recovery (restore and sweep). A note indicates this layer owns long-running harnesses over time. Below, a “Managed Agent Swarm” section visualizes a hierarchy of agent sessions. A central orchestrator node manages multiple child nodes, including both orchestrators (which can have their own children) and leaf agents (which do not). The structure branches outward, showing delegation within a parent session. A legend distinguishes root orchestrator, orchestrators with children, and leaf nodes. A note emphasizes that swarm management owns the lifecycle of many agent sessions.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051003146063982592.jpeg)

That distinction sounds academic until you look at real systems.

Hermes has a very good delegation primitive. Its delegate_task tool creates child AIAgent instances, runs them in parallel, streams progress, applies timeouts, interrupts them, and returns structured summaries back to the parent. Clean. Useful. Understandable.

But the child lives inside the parent tool call.

As we looked around the ecosystem for examples of swarm management really working, one of the absolute best examples was hiding in plain sight: **OpenClaw**.

OpenClaw has a solid swarm management system. Its subagents become gateway sessions. They get durable session keys, run IDs, lifecycle records, parent-child lineage, cleanup policy, and a push-based completion path back to the requester.

That is the architectural line.

Delegation asks: how does one agent split work? Swarm management asks: how does a runtime own many agents over time?

This blog will spend a lot of time highlighting what we think needs to be in swarm management driven by a lot of ideas in OpenClaw.

## The agent needs durable identity

The first requirement of swarm management is identity.

If you cannot address a child, you cannot manage it. You can wait for it. You can cancel the local future. You can ask the parent to summarize what happened.

But you cannot operate a fleet.

In OpenClaw, a spawned child gets a session key:

agent:<targetAgentId>:subagent:<uuid>

That key is doing real work.

![Diagram titled “Identity Management for Swarms,” explaining how spawned agent sessions become addressable and manageable. At the top, a dashed blue box labeled “Gateway-visible child session” contains two required identifiers: “Session key” (agent/target/agentID/subtask/runID; where the call lives) “Run ID” (current execution; what is running now) A note states: “The runtime needs both.” An arrow labeled “addressable” points to a green dashed box on the right titled “Gateway can,” listing actions the system can take once a session is identifiable: list session, patch session, delete session, link to parent, and show in session UI. Below the blue box, an orange box shows “SubagentRunRecord + SessionEntry metadata,” described as the control plane used to list, route, recover, clean up, and enforce policy across sessions. At the bottom, a purple dashed section titled “Questions identity lets the swarm manager answer” includes examples: who spawned it, is it running, any descendants, keep or delete, and result delivered.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051005818674536448.jpeg)

It turns the child into something the gateway can see. The child can be listed, patched, deleted, and linked back to a parent. It can show up next to normal chat sessions, cron sessions, and ACP sessions.

The child also gets a run ID. The session key names where the child lives. The run ID names the current execution.

You need both.

A swarm manager has to know the basics: child session key, run ID, requester, controller, depth, role, workspace, task label, cleanup policy, timestamps, and outcome. That metadata answers the questions the runtime cannot hand-wave away.

Who spawned this child? Is it still running? Does it have descendants? Should it be kept as a session or deleted after completion? Did the result actually get delivered?

If those answers only live inside a model’s context window, the runtime cannot manage the swarm.

**Completion is routed, not returned**

Most delegation systems have a simple contract:

- Parent calls a tool.
- Child runs.
- Parent blocks.
- Child returns a summary.
- Parent continues.

That is a good contract for bounded delegation.

It breaks down once the parent is not just waiting on the same call stack.

In a real swarm, the parent may be active. Or idle. Or another subagent. Or restarted. Or gone. The child may have children of its own. The result may need to be private orchestration context, not a user-facing message.

OpenClaw handles this with a push-based model. sessions_spawn returns acceptance and bookkeeping. The result arrives later through the registry and announce flow.

Roughly:

- Parent spawns a child through sessions_spawn.
- OpenClaw creates a child session.
- The child run is registered.
- The child runs in its own session.
- The registry waits for lifecycle completion.
- OpenClaw captures the child’s latest output.
- It builds an internal task_completion event.
- It routes that event back to the requester session.

The important part is the event:

```
{
  type: "task_completion",
  source: "subagent",
  childSessionKey,
  childSessionId,
  taskLabel,
  status,
  result,
  replyInstruction
}
```
That is the parent-child contract: capture completion, preserve provenance, route it to the right session, and let that session decide what to do next.

![Diagram titled “Completion Is Routed, Not Returned,” showing how a swarm manager separates accepting work from delivering results later. In the center, a “Requester’s session” sends a request to a “Swarm manager,” which accepts the task, records who asked, and keeps delivery state. The swarm manager starts a “Child agent,” which runs independently and may finish later. On the right, when the child finishes, it emits a “Completion event” containing the result, status, child identity, and routing info. This event flows to a “Delivery policy” box, which decides how to deliver the result (wake if active, queue if idle, retry if delivery fails) and routes it back to the correct requester session. On the left, a dashed box lists possible requester states: active (steer into current run), idle (start follow-up run), another subagent (private orchestration context), user-facing (normal assistant response), or temporarily unavailable (retry or fallback). A note at the bottom emphasizes: completion is a routing problem, and the runtime owns the handoff after the child stops running.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051008215421493248.jpeg)

The delivery layer has policy. It can steer an active requester session, queue an announce for later, call the gateway agent method directly, deliver a user-facing channel message, retry, or fall back to direct send. Most subagent systems skip this part.

They treat completion as a return value. In a swarm manager, completion is a routing problem.

**Queues matter more than prompts**

Once agents can spawn agents, the runtime has to care about concurrency in a very practical way.

You need strict ordering within a session. Two messages should not collide inside the same active agent loop. You also need parallelism across sessions. Otherwise the fleet becomes a single-file line.

This is why swarm management starts to look less like an agent framework and more like runtime infrastructure.

Main agent work is one lane. Subagent work is another. Cron or background work may be another. Each lane can have its own concurrency limit, while each session still serializes its own active run.

A user sends a follow up while an agent is busy. A child finishes while a parent is still running. A child has children. A cron job completes and needs to notify a session. A steer message arrives while a model is streaming.

If all of those are just messages, the system gets messy fast.

![Diagram titled “Queues Matter More Than Prompts,” illustrating how OpenLane separates per-session ordering from system-wide parallelism. On the left, a “Concurrent events” box lists inputs such as user follow-up, child completion, cron notification, and steering while streaming. These feed into a “Queue policy” box, which defines actions like steering the active run, enqueueing follow-ups, collecting backlog, or interrupting/waiting. In the center, a “Per-session lane (sessionKey)” shows how work is handled for a single session: an “active run” (serialized turn) processes work, with a “follow-up queue” for deferred tasks. If capacity is exceeded, a “cap overflow” path summarizes or drops excess work. On the right, “Global lanes (enqueueCommandInLane)” distribute work across system-wide queues: main (user concurrent work), subagent (separate capacity), cron (background work), and cron-nested (timer-driven tasks). Arrows indicate how per-session work is routed into these global lanes for parallel execution. The diagram emphasizes that queueing and scheduling—not just prompts—determine how concurrent events are ordered, processed, and scaled.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051009090089033728.jpeg)

Some messages should steer the active run. Some should be queued as follow-ups. Some should interrupt. Some should be summarized or dropped when the backlog gets too large. The answer lives in queue policy, not better prompting.

**Cancellation is too weak for agent swarms and fleets**

The simplest systems can cancel a future. That is table stakes.

A real swarm manager needs to steer, interrupt, kill, and cascade. Steering is the interesting one.

![Diagram titled “Cancellation Is Too Weak,” explaining how a swarm manager handles stopping or redirecting work in a hierarchy of agent sessions. On the left, a “Live session tree” shows a parent orchestrator spawning a child session, which in turn has worker nodes beneath it. In the center, a “Control plane” box presents two options: “Steer” (preserve the session) “Kill” (clean subtree), with a note that this is more than simple cancellation. On the right, two outcomes are illustrated: Steer (green): keep the child session but replace the current run by aborting it, sending new instructions, and updating the registry to point to the new run. Kill (red): terminate the run, clear queues, and decide whether to cascade termination to descendant sessions based on policy. Arrows show the control plane directing either a redirect (steer) or termination (kill) of the child session within the tree.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051009293978374144.jpeg)

When a child is doing the wrong thing, you do not always want to kill it and lose the session. You may want to redirect it.

In OpenClaw, steering a controlled subagent is a control-plane operation. It marks the current run for steer-restart, suppresses stale completion announcement, aborts the in-flight run, clears queues, waits for abort to settle, sends a new agent message, and remaps the registry from the old run to the new one. The system is telling the child to stop what it is doing and pivot.

Kill is different. Kill should terminate the run, mark session state, suppress inappropriate completion announcements, and optionally cascade to descendants.

Cascade matters because a swarm is a tree. Killing an orchestrator while leaving its workers alive is usually wrong. Sometimes it is exactly what you want. The runtime needs to know the graph well enough to make that distinction.

This is where prompt-only coordination falls apart.

You cannot ask the model to remember every live child and manually clean up the tree. The runtime has to own the graph.

**Roles are a runtime safety mechanism**

Flat swarms do not scale. If every child can spawn every other child indefinitely, the system eventually becomes useless or dangerous.

The simple split is orchestrator and leaf. Orchestrators coordinate. They can spawn workers, inspect status, and synthesize results. Leaves do work. They cannot coordinate further.

This should be enforced in tools, not just suggested in prompts.

![Diagram titled “Roles Are a Safety Mechanism,” showing how a runtime controls whether agent spawning is allowed. On the left, a “Spawn request” box shows a model asking for a child, resulting in a requested subagent. An arrow labeled “legal?” points to a central “Runtime role gate.” In the center, the “Runtime role gate (enforced in tools)” evaluates rules such as spawn depth, child limit, role from depth, and tool deny policy. On the right, a “Child capability envelope” shows two possible outcomes: If allowed (green): an “Orchestrator” that can spawn and control, with management tools available. If denied or at the lowest level (red): a “Leaf” that only does work, with spawn/control tools disabled. The diagram emphasizes that the runtime—not the model—decides whether the swarm structure is permitted and what capabilities each role receives.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051014311703904256.jpeg)

OpenClaw tracks spawn depth and resolves subagent capabilities from that depth. It stores spawnDepth, subagentRole, and subagentControlScope in the child session. Leaves lose management tools. Orchestrators keep them within configured depth and child limits.

Hermes has a similar idea in delegate_task: role=”leaf” vs role=”orchestrator”, configurable delegation.max_spawn_depth, and a kill switch for orchestrator behavior. That is the right instinct.

But in a swarm manager, the boundary belongs in the control plane. The model can request a spawn. The runtime decides whether it is legal.

The runtime should know how deep the child is, how many children the parent already owns, which tools are denied to this role, and whether the child can create more children.

No labels, no hand-holding. The system enforces the shape of the swarm.

**Recovery keeps the runtime in control**

A swarm manager cannot fire and forget.

If the system owns children, it needs to know when they are stuck, missing, orphaned, completed, or completed but undelivered.

OpenClaw’s subagent registry listens to lifecycle events. It uses agent.wait. It tracks active run context. It persists the registry to disk. It restores runs on startup. It has retry timers for announce delivery and grace windows for transient lifecycle errors.

It also runs a sweeper.

The sweeper is not glamorous. It is the part that makes the system real.

![Diagram titled “Recovery Is How The Runtime Keeps Ownership,” explaining how a swarm manager maintains control over agent execution through persistence and recovery. On the left, a purple “Subagent registry (the process table)” stores metadata for each run, including run ID, owner, child session, state, outcome, and delivery, with a note that it is persisted to disk. At the top right, a “Startup restore” box shows the system reloading from a file (runs.json) and resuming pending work. At the bottom right, a green “Sweeper loop” continuously checks for issues such as missing live context, stuck pending state, completed work within a session, or undelivered results. It then takes actions like retrying, reconciling, expiring, or marking runs as failed. Arrows indicate the registry feeding both startup restoration and ongoing sweeper checks, emphasizing that recovery mechanisms ensure the runtime retains ownership and consistency across agent sessions.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051010759757549568.jpeg)

It checks active runs without live run context. It reconciles them against session state. It expires old session-mode records after cleanup. It removes or retries stuck pending lifecycle states. It marks delivery failed instead of leaving cleanup half-done forever.

This is operating-system work.

The analogy is not perfect, but it is useful: a swarm manager needs something close to a process table, because the management problem rhymes.

What is running? Who owns it? What happens when it exits? Which children should die with the parent? Which sessions should survive restart? Which outputs have not been delivered?

Without that, the system is mostly launching work and hoping.

**Agent state outlives the run**

Every swarm manager eventually becomes a cleanup system.

Subagents create state: transcripts, run records, browser sessions, bundle MCP runtimes, attachment directories, workspace files, delivery status, lifecycle hooks, and cost metadata.

Someone has to own that state after the model stops thinking about it.

OpenClaw lets a child be kept or deleted. That choice matters. A one-shot run can clean up transcript and runtime state. A persistent child session should remain addressable. Attachments may be retained or removed. Browser and MCP runtimes need retirement. Context engines need to know whether a subagent ended or was deleted.

![Diagram titled “State Outlives The Run,” showing how the runtime manages cleanup and persistence after a model finishes executing. On the left, a “Run ended” box indicates the model has stopped thinking, but state remains, including transcripts, run records, browser, MCP runtime, attachments, and delivery. In the center, a “cleanup state machine” (owned by the registry after completion) outlines steps: freeze completion output, clean browser and MCP, attempt delivery (retry or give up), and finally apply a keep-or-delete decision. On the right, “cleanup outcomes” include: Delete child (remove session, transcript, runtime) Keep child (session remains addressable) Attachments (retain or remove) Context engine (completed or deleted) At the bottom, a comparison explains this differs from bounded delegation: instead of the child object closing immediately, the swarm’s session, delivery, descendants, and retained state may continue. A final note emphasizes that cleanup is not the end of a task, but how the runtime prevents stale agent work from accumulating.](https://arize.com/wp-content/uploads/2026/05/swarm-management-2051011779136978944.jpeg)

This is another place where delegation and swarm management diverge.

In bounded delegation, cleanup can be local. The child object closes. The thread exits. The parent gets JSON.

In swarm management, cleanup is distributed. The child may be a session. The run may be done but delivery not complete. The session may be kept but attachments removed. The parent may need one more wake-up after descendants settle.

Cleanup is a state machine.

That sounds heavy because it is.

But long-running multi-agent systems accumulate state. Pretending otherwise just moves the complexity into bugs.

**Swarm management is the layer above the agent**

OpenClaw is interesting because it exposes the swarm manager layer in code.

There is no magical SwarmManager object that makes everything elegant. The swarm emerges from ordinary runtime machinery:

- session keys
- lanes
- run IDs
- registry records
- lifecycle events
- internal completion events
- queue policy
- delivery routing
- cleanup decisions
- recovery sweeps

That is probably what real swarm management looks like: a set of boring control-plane primitives that make many agents survivable.

Hermes shows what good delegation looks like. Spawn workers, stream progress, return summaries, synthesize.

OpenClaw shows what happens when delegation becomes session infrastructure.

The next generation of agent systems will not just ask whether an agent can call tools. That was the harness question.

The next question is where agents live, who owns them, how they report back, how they are stopped, and what survives after restart.

That is the layer that turns “a single agent harness” into a fleet of well coordinated “agents” that can tackle a wide range of tasks.
