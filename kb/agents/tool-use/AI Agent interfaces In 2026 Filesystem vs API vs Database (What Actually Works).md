---
title: 'AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually
  Works)'
topic: agents
subtopic: tool-use
secondary_topics:
- agents/memory-context
summary: Compares filesystem, API, and database interfaces for agents, using memory
  benchmarks and practical interface tradeoffs to evaluate what works in production.
source: arize
url: https://arize.com/blog/agent-interfaces-in-2026-filesystem-vs-api-vs-database-what-actually-works/
author: Chris Cooning
published: '2026-01-21'
fetched: '2026-07-11T04:54:26Z'
classifier: codex
taxonomy_rev: 1
words: 1222
content_sha256: 644f7799c251da4826b45a3172610793f8639870d33534b7ea700a6e8edf6ba2
---

# AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)

## We Don’t Know How to Build Agent Interfaces Yet (And That’s Fine)

Letta just [published benchmark](https://www.letta.com/blog/benchmarking-ai-agent-memory) results showing a filesystem-based agent scored 74% on memory tasks by simply storing conversation histories in files, beating specialized memory tools.

The result sparked an internal debate at Arize that surfaced two separate questions we’re still wrestling with. And honestly? That uncertainty might be the most valuable thing to share.

## The Filesystem “Victory” Reveals the Problem

[Tony Powell](https://www.linkedin.com/in/anthony-powell-05788696/), Open Source Engineer at Arize, had an immediate reaction to the Letta results: “Filesystems and bash are probably one of the largest sources of pretraining related to computing an LLM may have access to.”

It’s not that filesystems are good. It’s that everything else is worse.

Think about what happens when you expose an API to an agent. “By the time the LLM is taught how to use a particular API you’ve gobbled up a bunch of your context window,” Tony points out. Every endpoint needs documentation. Every schema needs examples. You’re spending thousands of tokens on education instead of reasoning.

Tony’s theory: Filesystem wins by default because the education already happened during pretraining.

## But MCP Isn’t Solving It Either

You might think: “Just use MCP, wrap your API, problem solved.”

[Laurie Voss](https://www.linkedin.com/in/seldo/), our Head of DevRel (ex-LlamaIndex). isn’t buying it: “I think giving agents access to an API directly or via MCP is ineffective. MCP servers that just wrap a REST API are pointless.”

Why? Because most MCP implementations are just thin wrappers around the same complex APIs. You haven’t actually solved the interface problem, you’ve just added another layer.

Laurie’s proposal: “You need your MCP server to be an agent that can answer natural language questions as an expert in the domain, because natural language questions are what the other agent has.”

Agent-to-agent communication instead of agent-to-API. Your calling agent doesn’t learn your observability schema. It asks questions of a specialized observability agent that already knows the domain.

But here’s the problem: nobody’s really building this yet. And we don’t know if it’ll work at scale.

## Wait, We’re Conflating Two Separate Problems

[Aman Khan](https://www.linkedin.com/in/amanberkeley/), AI Product Manager at Arize reframed the discussion: we’re conflating the interface question (how does the agent interact with data?) with the deployment question (where does the agent run and what does it operate on?).

His framing:

- **Stateless/DB-backed → API-based agents –**Agent calls APIs, data lives remotely
- **VM/sandbox → Filesystem agents –**Agent runs in isolated environment, operates on files

But these don’t have to be coupled.

Tony’s been exploring a third path: “I’ve been exploring ‘pre processing’ API data into a sandboxed filesystem. So it’s as if you’re operating on local data (it is at agent runtime) but you don’t necessarily need to maintain a directory of files all the time.”

Let’s think about what this unlocks:

- **Filesystem interface**(agent already knows the tools)
- **Remote data**(don’t need local-first architecture)
- **Sandboxed execution**(safe to run)
- **Session-scoped**(data exists during agent runtime, no persistent storage burden)

As Tony puts it: “The same agent can operate on truly local data you already have, or against remote data that you preprocess into files. It doesn’t care.”

This is actually the model [Phoenix Insight](https://github.com/cephalization/phoenix-insight) uses. We materialize your Phoenix/Arize observability data as a structured filesystem at runtime, but you’re not maintaining local file copies.

## The Database Folks Have Entered the Chat

Once you separate interface from deployment, the database critique becomes clear. While we’re celebrating filesystem interfaces, Dax from OpenCode [points out](https://x.com/thdxr/status/2011638639831499041): “A filesystem is just the worst kind of database.”

He’s right. If you actually implement agent memory as literal files on disk, you’re accidentally reinventing:

- Search indexes
- Transaction logs
- Locking mechanisms
- Permission management
- Schema validation

All the things databases solved decades ago. Badly.

This is why the “virtual filesystem” pattern is emerging. LangSmith stores data in a database but [exposes it to the agent as files](https://x.com/hwchase17/status/2011834318172422279). Anthropic’s memory tool leaves storage up to you. The interface layer (what the agent sees) is decoupled from the storage layer (what actually persists).

This is exactly what Tony’s preprocessing approach does with Phoenix Insight. A filesystem interface for the agent, with proper data infrastructure underneath.

But notice: this solves the storage problem, not the interface abstraction problem. We’re still using filesystem because the agent knows bash, not because it’s the ideal way to think about observability data.

## The Unresolved Tension on Interfaces

Here’s where our discussion on the interface question landed. Or rather, didn’t land:

*Laurie*: “The success of file systems as an interface is a symptom of the fact that we are bad at exposing APIs in a useful way, rather than any particular strength in the file system API itself.”

He’s right. APIs are better interfaces for humans, or we’d have built everything as filesystems already. The fact that we’re retreating to filesystem primitives for agents is an admission of failure.

*But also Laurie*: “APIs are better than file systems to a human, or all our APIs would just look like file systems already. We just need to figure out how to effectively communicate that utility to an LLM.”

Great. How?

Agent-to-agent communication? Maybe, but unproven at scale.

Better skills files? Laurie calls this “a crutch.”

Framework orchestrators like LangGraph and CrewAI? As Laurie notes: “I think CrewAi and LangGraph are solving one level of abstraction and are necessary but not sufficient.” They handle orchestration. They don’t solve the interface problem.

## What This Means for Architecture

The Letta benchmark revealed something deeper than “filesystem beats vector databases.” It showed that **interface design and deployment model are independent choices**.

You can have:

- API interface + stateless deployment (traditional agent)
- Filesystem interface + local deployment (Claude Code, Cursor)
- Filesystem interface + remote data + runtime materialization (Phoenix Insight’s model)
- Hypothetically: agent-to-agent interface + any deployment model

The main benefit Tony sees in the hybrid approach: “An LLM doesn’t need to learn how to use your API or db schema, and instead just uses the FS.”

For observability specifically, this means agents can explore your traces using cat, grep, jq without you maintaining a local directory of trace files or teaching the agent your query language.

As Tony found in his experiments: “The agent comes up with interesting query strategies that wouldn’t be easily contained within a SQL-like language.”

## Why We’re Sharing This

Phoenix Insight (experimental) uses the hybrid model: filesystem interface, remote observability data, runtime materialization. Why?

- The agent already knows bash
- The interface is transparent. You can literally see what files the agent is reading
- It performs well on real observability tasks
- You don’t need to restructure your data storage

But we’re watching the ecosystem closely. When agent-to-agent communication matures, when the deployment models evolve, when the right abstractions emerge, we’ll adapt.

The Letta benchmark didn’t prove filesystem is the best interface. It proved we’re still in the experimental phase of agent architecture, and that’s exactly where the interesting work happens.

### Try Phoenix Insight (Experimental POC)

bash (requires node v22 or newer)

```
```
npm install -g @cephalization/phoenix-insight
pxi ui

			Point it at your [Phoenix instance](https://arize.com/docs/phoenix) and see an agent explore your observability data using filesystem tools.

Not because it’s perfect. Because it works today while we figure out what comes next.
