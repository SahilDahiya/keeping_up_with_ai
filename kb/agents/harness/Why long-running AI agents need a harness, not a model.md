---
title: Why long-running AI agents need a harness, not a model
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/architecture
summary: 'Foundational argument that a capable model is not a reliable agent: long-running
  agents need a ''harness'' — the layer of tools, coordination, context, orchestration,
  safety checks, fallbacks, and memory around the model that turns intent into durable
  work legible to humans and systems.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/the-harness-thesis
author: Jameson Lee
published: '2026-06-03'
fetched: '2026-07-16T22:03:25Z'
classifier: claude
taxonomy_rev: 2
words: 1812
content_sha256: 9549b23dbf800c54a048c8b9751a3f1eaaa4c43493d37b528a624a8d02499fed
---

# Why long-running AI agents need a harness, not a model

The industry still talks about AI agents as if the model is the whole system.

It is not.

The model matters. Better reasoning, larger context windows, lower latency, and lower cost all change what agents can do. But a more intelligent model does not automatically create a more reliable agentic service on its own.

A bigger shovel can dig faster, but a tunnel is not only a digging problem. As the project gets larger, it demands more sophisticated tools, coordination, context, orchestration, execution, safety checks, fallback plans, and memory of what the ground has already revealed. The harness is that governing concept for agents. It turns intent into durable work.

Long-running agents need the same thing. They need a system. They need a harness.

A harness is the layer around the model that makes agent work understandable to humans, communicable to systems, and durable over time. It lets agents operate at agent speed without forcing the rest of the organization to rely on transcripts, summaries, and trust.

Several years after the dawn of ChatGPT, teams are finally looking past the model. The problem is not only whether a model can reason. It is whether the tools around the model can be unified into a system that agents and humans can both use. Tool dispersion creates enormous friction. Agent reliability does not come from inference alone.[1](https://pydantic.dev#user-content-fn-1)[2](https://pydantic.dev#user-content-fn-2)[3](https://pydantic.dev#user-content-fn-3)

That is the shift for engineering leaders building agentic services: long-horizon agents depend more on the harness than they depend on any individual model.


Most teams start agent development by asking about the model:

Which model should we use?


That is a valid question, but it is not the architectural one. The architectural question is this:

What must exist around the model for the work to become reliable, inspectable, and useful to other people and systems?


The agent must know what context already exists. It must decide when to retrieve, when to act, when to ask, when to stop, and when to hand off. It must leave behind evidence. It must make its work available to future runs. It must expose enough runtime information that a human can understand what happened without reading a private chat transcript line by line.

The model cannot provide that alone.

At Pydantic, we believe a database is integral to long-horizon agent systems because agent work needs durable state at the scale and speed agents operate. The database is not the harness by itself. It gives the harness a substrate for memory, work state, decisions, and handoffs. Durable knowledge has to live where agents can inspect and use it, not scattered across chat threads or people's heads.[2](https://pydantic.dev#user-content-fn-2)

[Pydantic Logfire](https://pydantic.dev/logfire) is an AI observability and evals platform, and it is the harness layer built for agents in production. It puts model calls, tool calls, application code, database work, metrics, and evals on a shared runtime surface.


Teams choosing tools for agentic services should look beyond model access and prompt ergonomics. Those matter, but they are not enough.

A serious harness should cover a few distinct categories:

| Category | What it answers | 
|---|---|
| Durable context | What state, memory, and work artifacts survive the run? | 
| Runtime control | When can agents act, retrieve, call tools, escalate, or stop? | 
| End-to-end observability | Can traces connect models, tools, app code, and data writes? | 
| Evaluation and governance | Can offline and online evals measure quality, compliance, and policy adherence? | 
| Economic accountability | Can teams track cost, latency, usage, and value from the managed runtime? | 
| Collaboration | Can humans, agents, and systems coordinate through shared records? | 
| Adaptability | Can the same harness enter new domains without starting over? | 

For technical teams, these are implementation requirements. For executives, they are the difference between experimenting with agents and operating agentic services.

Without a harness, each agent run is mostly private. With a harness, each run adds to a shared operating layer.


The hard part of agent systems is no longer prototyping the agent loop. A developer can stitch together a model, a prompt, and a few tools quickly.

The hard part is unifying all the pieces that make production-grade agents possible:

- observability that follows traces end to end across models, tools, application code, and data writes
- offline and online evaluations that measure performance, compliance, and governance behavior
- metrics that connect agent activity to cost, latency, usage, and business value
- memory that survives a single model call and can be reused by future work
- tools that agents can call safely within the policies of the system
- runtime control that decides when work should continue, pause, escalate, or stop

Coding harnesses make this shift obvious. Developers now lean on agents that can work inside a repo, run tests, inspect failures, edit files, and recover from feedback. The model is important, but the experience works because the harness gives the model execution, context, tools, feedback, and guardrails.[2](https://pydantic.dev#user-content-fn-2)

The same pattern appears in longer-running application work. Planner, generator, and evaluator agents only become useful when the harness decomposes the work, preserves artifacts, and checks output against criteria.[4](https://pydantic.dev#user-content-fn-4)

When these pieces live in separate tools with separate timelines, the agent may work, but the service is hard to understand. Leaders cannot govern it. Operators cannot debug it quickly. Future agents cannot reliably build on what happened before.

The harness turns that stitched-together stack into an operating system for agentic work.


Pydantic already sits inside the developer workflow, and is increasingly legible to AI coding agents writing today's code.

[Pydantic Validation](https://pydantic.dev/docs/validation/latest/) is widely adopted across the Python ecosystem. It gives developers a common way to describe, validate, and reason about application data. That matters for agents because agentic systems still need ordinary engineering discipline: data has to be shaped, checked, stored, routed, and explained.

[Pydantic AI](https://pydantic.dev/docs/ai/overview/) builds on that developer experience. It lets teams scaffold agentic systems in normal Python, using patterns that developers and AI coding agents can both understand quickly.

[Pydantic Logfire](https://pydantic.dev/logfire) brings those pieces together at runtime. It observes model calls, tool calls, application code, and database work on one OpenTelemetry timeline. Because it is built on OpenTelemetry, it traces any stack, not just Python. It gives teams the trace, metric, and evaluation surface they need to operate agents after the prototype works. Trace data is queryable in standard SQL, and the Logfire MCP server lets a coding agent query it the same way you would, so debugging an agent can itself become agent work.

[Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) closes that loop inside Logfire. Teams measure behavior offline and online on the same traces: not just final output quality, but whether the agent followed policy, used the right context, and left useful evidence behind. A strong base model does not make that evaluation reliable on its own. The evaluation loop itself has to be designed, observed, and tuned like anything else in production.[4](https://pydantic.dev#user-content-fn-4)

That combination is what the Pydantic stack gives you. Pydantic AI makes agent systems easy to scaffold. Pydantic Validation gives those systems a familiar foundation for data. Logfire is the harness that makes the whole system observable, governable, and reusable, with Pydantic Evals measuring quality on the same traces.

For teams building their own harness, the historical default has been to build most of that runtime from scratch: traces in one place, evals somewhere else, metrics in a dashboard, memory in a database, cost controls in a proxy, and handoff state in whatever artifact the team remembered to write. Logfire changes that starting point. You get a harness for the runtime, and you spend time on the agentic service instead of rebuilding the operating layer around it.


The first useful agent in an organization is rarely the last.

Once a team sees that an agent can help with one workflow, adjacent workflows appear quickly. Support wants case triage. Sales wants account research. Product wants feedback synthesis. Engineering wants code review and incident analysis. Events teams want live audience intake. Executives want briefings that combine all of it.

These workflows do not share the same data model. They do not share the same risk profile. They do not share the same users. They share the need for a harness.

The harness adapts to the context:

- In research workflows, it may store sources, claims, decisions, and reports.
- In customer workflows, it may store accounts, conversations, escalations, and follow-ups.
- In engineering workflows, it may store traces, incidents, test failures, and code changes.
- In event workflows, it may store attendees, interests, moderation outcomes, and engagement metrics.

The database matters, but the specific database does not. Long-horizon work needs a durable context layer that agents and humans can share.

This is why a harness should be horizontal. It should not be a narrow demo assembled for one workflow. It should be a repeatable pattern for letting agents enter new contexts without losing observability, governance, or continuity.


Here is a useful test for an agentic architecture:

If the model call disappeared, what useful context would remain?


If the answer is "a transcript," the system is still model-centered.

If the answer is "traces, state, decisions, evidence, metrics, evals, and records that another person or agent can use," the system has started to become harness-centered.

That distinction changes how teams should evaluate agent problems. The first question should not be only "which model should we use?" or "which tools can the agent call?"

The better question is:

What harness is missing?


Or, to borrow the old civic framing:

Ask not what you can do for your agent. Ask what your harness can do for your agent.


If the agent cannot be inspected, that is a harness problem. If agents cannot coordinate through shared state, it is a harness problem. If leadership cannot understand cost, value, risk, and compliance, it is a harness problem. If each new use case requires another pile of stitched-together glue, it is a harness problem.

The common thread across current harness engineering work is that stronger models still need a surrounding system that turns intent into reliable work.[1](https://pydantic.dev#user-content-fn-1)[2](https://pydantic.dev#user-content-fn-2)[3](https://pydantic.dev#user-content-fn-3)[4](https://pydantic.dev#user-content-fn-4)

The model is a component. The harness is the architecture that turns model output into durable work.

For teams that want to experiment with this pattern, start with open-source examples: build an agent with the [Pydantic AI examples](https://github.com/pydantic/pydantic-ai/tree/main/examples), observe it with [Pydantic Logfire](https://pydantic.dev/logfire), and reference the example agents in our docs to scaffold harnesses and groups of agents on the same stack.

The future of agentic systems will not be built by prompts alone. It will be built by harnesses that let humans understand agent work, and let agents act inside systems we can trust.


## Footnotes

- 
Birgitta Böckeler, ["Harness engineering for coding agent users"](https://martinfowler.com/articles/harness-engineering.html), MartinFowler.com.[↩](https://pydantic.dev#user-content-fnref-1)[↩](https://pydantic.dev#user-content-fnref-1-2)2
- 
OpenAI, ["Harness engineering: leveraging Codex in an agent-first world"](https://openai.com/index/harness-engineering/).[↩](https://pydantic.dev#user-content-fnref-2)[↩](https://pydantic.dev#user-content-fnref-2-2)2[↩](https://pydantic.dev#user-content-fnref-2-3)3[↩](https://pydantic.dev#user-content-fnref-2-4)4
- 
Anthropic, ["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).[↩](https://pydantic.dev#user-content-fnref-3)[↩](https://pydantic.dev#user-content-fnref-3-2)2
- 
Anthropic, ["Harness design for long-running application development"](https://www.anthropic.com/engineering/harness-design-long-running-apps).[↩](https://pydantic.dev#user-content-fnref-4)[↩](https://pydantic.dev#user-content-fnref-4-2)2[↩](https://pydantic.dev#user-content-fnref-4-3)3
