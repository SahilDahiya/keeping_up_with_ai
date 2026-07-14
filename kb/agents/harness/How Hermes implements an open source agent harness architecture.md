---
title: How Hermes implements an open source agent harness architecture
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/architecture
summary: Breaks down Hermes as an open-source agent harness architecture, focusing
  on components, control flow, and implementation boundaries.
source: arize
url: https://arize.com/blog/how-hermes-implements-open-source-agent-harness-architecture/
author: Aparna Dhinakaran
published: '2026-06-01'
fetched: '2026-07-11T04:56:20Z'
classifier: codex
taxonomy_rev: 1
words: 1379
content_sha256: e3899190bf07b5cfea30ca42785ee2559a73a24f11874bccb00ca3832810f407
---

# How Hermes implements an open source agent harness architecture

*A **version of this blog originally appeared on X**.*

**TLDR: **Hermes is one of the most complete open-source agent harnesses available today. Beyond the standard agent loop, it treats sessions as infrastructure, separates tool registration from tool exposure, implements lineage-based context compression, and supports long-running agents across CLI, messaging, and scheduled execution. While durable child-run orchestration is still emerging, Hermes already provides a strong reference architecture for building production-grade agent systems.

**What Is Hermes?**

[Hermes](https://hermes-agent.nousresearch.com/?_gl=1*1r669u2*_ga*MTkxMTcxMDUzMy4xNzgwMzMyNTUw*_ga_4KWYPJ8SPY*czE3ODAzMzI1NTAkbzEkZzAkdDE3ODAzMzI1NTAkajYwJGwwJGgw) from [NousResearch](https://nousresearch.com/) is one of the strongest open-source agent harnesses in the ecosystem right now. We looked at the implementation directly to understand how it works, where its architecture is strongest, and what it suggests about the next generation of long-running coding agents.

In our earlier piece, “[What is an agent harness?](https://arize.com/blog/what-is-an-agent-harness/)”, we used a nine-part model for analyzing harness architecture:

- outer iteration loop
- context management and compression
- skills and tools management
- subagent management
- built-in pre-packaged skills
- session persistence and recovery
- system prompt assembly with project context injection
- lifecycle hooks
- permission and safety layer

Hermes implements all nine pieces of that model, and the useful lesson is how the runtime boundaries are drawn: provider adapters normalize model APIs, tool exposure is separated from tool registration, sessions are treated as infrastructure, and compression creates lineage rather than rewriting history.

That makes Hermes more than a coding-agent wrapper. It is a useful reference architecture for open, long-running agent systems.

**How Hermes implements the agent harness loop**

The core loop is familiar: model call, tool dispatch, tool result append, repeat until final response or interrupt.

Where Hermes is stronger than most open harnesses is provider abstraction. The same runtime can drive chat-completions style APIs, Anthropic Messages, Codex Responses, an out-of-process Codex app-server path, and Bedrock. Tool-call formats and provider quirks are normalized by transport adapters. At the loop level, the model surface looks consistent. For those of us, who really like having an open harness provider who supports all models, this open approach is much better than Claude Code.

**Context management and compression in Hermes**

Hermes has a full compression path, not a simplistic context trim.

Older turns are summarized by an auxiliary model. Head and tail segments are protected by token budget. Tool outputs that are older than a configurable threshold are pruned before summarization. The summary budget scales with compressed content at roughly twenty percent, with a two-thousand-token floor and a twelve-thousand-token ceiling. In practice this avoids spending too much context on tiny compressions while still giving large compressions enough room to be useful.

Compression is also a session lifecycle event. On compression, Hermes closes the current SQLite session row, creates a child session seeded by the summary, rotates the session ID, and records parent-child lineage. Plugin context engines and memory providers are notified that a boundary moved. If a long conversation compresses multiple times, you get a lineage chain instead of one repeatedly rewritten transcript. This is pretty unique relative to other harness architectures we’ve reviewed.

**Tool registration, tool exposure, and runtime scoping**

Tool registration and tool exposure are separate concerns in Hermes.

Tools register into a central registry at import time. A separate toolset layer decides what the model actually sees in a given run. That exposed set is scoped by platform and scenario, and can be narrowed again for delegated runs. A profile has its own enabled footprint.

This separation matters operationally. You can keep a broad installed tool library while keeping any single run’s model-visible surface small enough to manage for token cost and safety.

**Subagent delegation and the limits of child-run control**

Delegation primitives are solid. A child run gets its own task ID, its own terminal context, and returns a structured summary to the parent. Dangerous commands default to deny in delegated contexts, and recursion depth is capped.

The current limit is lifecycle ownership. Most child work still lives under the parent call path. When the parent is done, the child is done. There is not yet a durable, externally steerable child-run plane with independent control semantics.

**Session persistence, recovery, and search **

This is where Hermes departs most from editor-first harnesses.

Session state is stored in SQLite with FTS5 search and WAL journaling, with fallback behavior for filesystems that cannot support WAL coordination. Sessions track source tags for turns, parent-child lineage for compression splits, and metadata the gateway can use to resolve routing before the model runs.

That design effectively treats sessions as runtime infrastructure, not just transcripts for resume. CLI, messaging platforms, and scheduled jobs can all attach to the same session plane. A message can be routed to the right session before inference. A scheduled job can write to a session even with no active terminal.

Hermes also exposes a model-facing session_search tool for focused recall over prior sessions. This is a concrete example of pushing context management decisions into the model loop itself rather than relying only on static injection.

**System prompt assembly and project context injection**

Hermes explicitly composes the system prompt in three tiers: stable, context, and volatile.

The stable tier carries identity (SOUL.md when present), tool guidance for enabled tools only, skills index content, environment hints (like Tmux/container detection), and platform hints. The context tier reads project files from cwd (AGENTS.md, CLAUDE.md, .cursorrules) and runs prompt-injection scanning before loading that content. The volatile tier carries memory snapshots, user profile material, external memory-provider blocks, and a timestamp line with model/provider metadata.

The tiering itself is explicit in code, which makes invariants easier to reason about. Stable stays stable, context stays cwd-derived, volatile changes turn-by-turn. Prompt rebuild is tied to compression and related invalidation points, which helps keep prompt prefixes cache-friendly across normal turns.

**Lifecycle hooks for policy, auditing, and host effects**

Hermes has two hook surfaces with different trust models.

First, plugin lifecycle hooks run inside the harness process and can block, rewrite, or pass through operations at events like pre/post tool call, gateway pre-dispatch, and approval request/response. Second, filesystem-driven gateway hooks let users install shell or Python scripts that run on events like gateway startup, agent step, and command-triggered paths.

Architecturally, both surfaces serve the same purpose: policy enforcement, auditing, and host side-effects should execute independently of model cooperation.

**What Hermes adds beyond a standard agent harness**

Three subsystems stand out beyond the nine-component harness model.

The first is the messaging gateway. Hermes supports a broad platform adapter surface (Telegram, Discord, Slack, WhatsApp, and others) and routes traffic through a shared session model. This feels like a user interface experience that was successful with OpenClaw, designed for user interaction with long running agents.

The second is the profile system. A profile is an isolated agent root. Two profiles on the same machine behave like two different agents from a state and footprint perspective.

The third is cron as a first-class subsystem. Jobs are durable, gated by the same permissions machinery as interactive sessions, delivered through gateway paths, and isolated per profile. That forces unattended operation concerns into the main architecture rather than leaving them as peripheral scripts.

**Where Hermes should go next: durable agent orchestration**

The obvious next step is moving from strong delegation to first-class orchestration.

delegate_task already produces useful worker behavior and structured returns. What is still missing is durable child-run control: run IDs, explicit lifecycle management, external steering, and cleanup semantics that survive parent completion. Hermes already has much of the substrate through session infrastructure and gateway routing. Promoting child runs to first-class control-plane objects is the most natural next architectural step. It is one of the gaps we see versus the OpenClaw agent orchestration layer.

**Final takeaway**

Hermes already has excellent execution quality and a strong systems foundation for an open harness. It is probably one of the best open model harnesses in the ecosystem. The pace of shipping is … insane, and most of the hard substrate work is already in place. We’re excited to see an agent orchestration layer mature on top of that base. Hermes can already support much broader long-lived agent workloads than typical coding harnesses handle today, and we’re excited to see where it goes.

*This piece references my previous** What is an Agent Harness*,* as framing, and is informed by ** Swarm management in agent harnesses**, plus Anthropic’s posts on** Managed Agents**. *
