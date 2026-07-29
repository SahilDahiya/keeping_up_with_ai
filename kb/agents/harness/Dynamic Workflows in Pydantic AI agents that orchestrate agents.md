---
title: 'Dynamic Workflows in Pydantic AI: agents that orchestrate agents'
kind: blog
topic: agents
subtopic: harness
secondary_topics: []
summary: 'Pydantic AI''s DynamicWorkflow extends its Code Mode pattern from tool-calls
  to sub-agents: an orchestrator agent gets a catalog of named agents and writes ordinary
  Python (async gather, loops, conditionals) to fan out and chain them in a single
  tool call, illustrated by the Bun-in-Rust port that ran ~50 such workflows with
  up to 64 Claude agents in parallel.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/dynamic-workflows
author: Aditya Vardhan
published: '2026-07-28'
fetched: '2026-07-29T06:58:55Z'
classifier: claude
taxonomy_rev: 2
words: 637
content_sha256: c324865488018865f5709ec73c1e1ba2b4672a4465ef2bf39088e1c62c5ccb64
---

# Dynamic Workflows in Pydantic AI: agents that orchestrate agents

TL;DR: Models are pretty good at orchestrating more of themselves. With Pydantic AI

`DynamicWorkflows`you can easily create your swarm of agents.

Bun got rewritten in Rust. Jarred took "Rewrite it in Rust bro" quite seriously.

Then he published [the blog post everyone was waiting for](https://bun.com/blog/bun-in-rust?utm_source=pydantic). A couple of things stood out to me.

- Dynamic Workflows
- Jarred being a cracked dev (who would have guessed)


The numbers are silly, but I will cite them anyway. Half a million lines of Zig ported, a diff of just over a million lines. 100% of the existing test suite still passing Eleven days from first commit to merge.

I would love to imagine Jarred prompting, "Yo dawg too many memory errors, can we do this in Rust?".

The actual workflow however was more nuanced.

He set up workflows where agents wrote plans for other agents. One workflow figured out Rust lifetimes for every struct field, another ported files. About 50 of these workflows ran over the 11 days, 64 Claudes at a time at peak, every file reviewed by two adversarial agents, you get the picture.

Do this in a loop and there you have it, Bun in Rust.

Models, it turns out, are pretty damn good at orchestrating more of themselves.


Yes. Absolutely!

You could already get pretty close. We've had [Code Mode](https://pydantic.dev/articles/your-agent-would-rather-write-code) for a while: instead of picking tools off a menu one call at a time, the model writes a Python script that calls them. Wire your agents in as tools, and you'd get part of the way there.

You don't have to do that plumbing anymore. Dynamic workflows are now a first-class capability in the [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/).


`DynamicWorkflow` is Code Mode moved up a level. Code Mode gives the model a script for its **tools**. `DynamicWorkflow` gives it a script for its **agents**.

You hand it a catalog of named agents. It hands the model a single tool. Inside that tool the model writes ordinary Python, where each sub-agent is an async function it can call, loop over, and combine or even graph(*if you know you know*). The whole script runs in one tool call, and only the last line finds its way back into context.

It looks something like this:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai_harness.experimental.dynamic_workflow import DynamicWorkflow
logfire.configure()
logfire.instrument_pydantic_ai()
reviewer = Agent('anthropic:claude-sonnet-5', name='reviewer', description='Reviews code for bugs.')
summarizer = Agent('anthropic:claude-sonnet-5', name='summarizer', description='Summarizes findings.')
orchestrator = Agent(
    'anthropic:claude-opus-4-8',
    capabilities=[DynamicWorkflow(agents=[reviewer, summarizer])],
)
```
The script the orchestrator writes at runtime looks something like this. It fans out, chains the results, and only the result survives:

```
import asyncio
reports = await asyncio.gather(
    reviewer(task="Review auth.py for bugs:\n<file contents>"),
    reviewer(task="Review parser.py for bugs:\n<file contents>"),
)
await summarizer(task="Summarize these findings:\n" + "\n\n".join(reports))
```

We got you.

```
workflow = DynamicWorkflow(agents=[reviewer])
orchestrator = Agent('anthropic:claude-opus-4-8', capabilities=[workflow])
# later, once a potato agent has been provisioned:
workflow.reveal(potato)
```
`potato` becomes callable on the very next step. The model finds out through a short note carrying the new function's signature, and the tool's own description never changes, so the reveal doesn't bust the cache.


Every agent run and model call lands on the same [OpenTelemetry trace](https://pydantic.dev/logfire). The `run_workflow` span carries the script the model wrote, so you can read what actually ran.

Running multiple agents with no trace is just an expensive way to generate slop. No judgment if you prefer the heartache, but **I** would much rather have a system I can debug.


```
uv add "pydantic-ai-harness[dynamic-workflow]"
```
Point an orchestrator at a couple of agents (or a few hundred), hand it a task that's too big for one context, and watch it write its own workflow. Then [open it up in Logfire](https://pydantic.dev/docs/logfire/get-started/ai-observability/) and watch the swarm work.

If it saves you from hand-rolling your own orchestration glue, a star on [GitHub](https://github.com/pydantic/pydantic-ai-harness) helps other people find it.
