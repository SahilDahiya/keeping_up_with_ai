---
title: Agent and LLM views in Pydantic Logfire
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- infra-platform/cost
summary: Argues that non-deterministic agent workloads should be monitored on turns-per-run
  and tool-calling-turns-per-run at p90, not the mean, because a rare runaway retry
  loop (e.g. 40 tool calls, $12) hides in the average; built from the gen_ai.* spans
  agents already emit.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/logfire-agents-llms-view
author: Bill Easton
published: '2026-07-14'
fetched: '2026-07-16T22:02:47Z'
classifier: claude
taxonomy_rev: 2
words: 895
content_sha256: 754fbf269b692062146d110fc7939e993df90b88e7bd06cf5ee1e698f0c18e11
---

# Agent and LLM views in Pydantic Logfire

Your support agent fires three tools on a normal run: look up the order, check the policy, draft the reply. Your dashboard says the average is 3.1. Everything looks healthy.

Then the monthly bill arrives higher than it should be, and you go looking. Somewhere in the last ten thousand runs, one request hit a retry loop and fired forty tools before it gave up. It cost twelve dollars. It didn't error, so nothing paged you, and the average absorbed it without a ripple. There are probably a dozen more like it this month, and the mean will never tell you.

![Model detail page for gpt-4.1-mini: calls, errors, latency, cost, and speed up top, the agents using the model, and charts for calls, error rate, latency, and tokens over time](https://pydantic.dev/assets/blog/agents-week/llms-model-detail.png)



Two views, both drawn from the `gen_ai.*` spans your agents already emit.

**The Agents view** is an inventory of every agent shipping traces to your project: runs, cost, average duration, a usage sparkline, and last-seen, sortable by whichever is on fire today. Open one and you get its runs, cost, tokens, and exceptions over time, plus the two charts that matter most for a non-deterministic workload: **turns per run** and **tool-calling turns per run**, each shown as average *and* p90. The average is the story you want to believe. The p90 is the one that's costing you money.

Each run has a Summary, a Model view, the Tool Calls, the Messages, and the full Trace. And a **Tools tab** that reconstructs exactly what the agent was allowed to do on that specific run: the tool definitions it was given, the sampling parameters, the thinking budget, the max tokens. When a run goes strange, "what could it even do here" is usually the first question, and now it's a tab, not an archaeology project.

**The LLMs view** is the inventory from the model's side: one row per provider and model, with calls, errors, latency, **throughput** (output tokens per second), input and output and cache-read tokens, cost, how often the model truncated because it hit the length limit, and how often it stopped to call a tool. Cost comes from Pydantic's open-source [genai-prices](https://github.com/pydantic/genai-prices) dataset, so the dollar figure is something you can audit, not a number we made up. Open a model to see its trends, which agents depend on it, and its recent calls, each one a click from the trace.


An agent breaks in shapes a service doesn't, and these two views are built around three of them.

The **shape of a run is non-deterministic**, so summary statistics lie by design. A p99 over a hundred runs hides what the p99 over a hundred thousand will tell you. The avg-vs-p90 charts exist because the runaway run, the one that fired forty tools where the median fired three, is invisible in the mean and obvious in the tail. You should not have to write a dashboard to see the thing that's costing you the most.

The **cost is variable per request**, measured in dollars, on prices that move weekly. Putting cost on the agent, on the model, and on the individual run, from an open dataset you can check, turns "why is the bill up" from a quarterly surprise into a sortable column.

The **dependency moves under you**. A provider deprecates a model, throttles it, or swaps a snapshot on their schedule, and your latency doubles with no change on your side. The LLMs view is where that shows up first: per-model latency and throughput, side by side, so a regression has a name before it has a war room.

And all of it is one trace ID. A row in the LLMs view links to the agent runs behind it; an agent run links to its Tools tab and its messages; every one of them ends in the live view you already use, on the exact span. The LLM-tracing products understand the model call and stop at the SDK boundary. This is the model call *and* the agent runtime *and* the pod it ran on, on one trace, in one product. It also doesn't care which framework you used: Pydantic AI, LangGraph, the OpenAI SDK, the Vercel AI SDK, anything that speaks OpenTelemetry, normalized into the same views.

It's an inventory before it's a dashboard, and that's deliberate: past a handful of agents you stop watching them one at a time. Sort the fleet by cost, errors, or last-seen, and the sick animal is the top row. The runaway you're hunting, the agent doing something your evals never thought to describe, lives in the tail of a distribution you only see once you're looking at the whole herd.


Both views are live for every Logfire project (the LLMs view in Beta), and populate from your existing `gen_ai.*` traces within a minute or two. There is nothing to instrument.

In our support-agent scenario, the path is short. Sort the Agents inventory by cost, open the agent, and the tool-calling-turns p90 chart is three times the average. Click the tallest bar into the run, open the Tools tab, and the retry loop is right there: a tool with no stop condition, called until the turn limit. One guard, shipped, and the tail comes back down.

Not using Logfire yet? [Get started](https://pydantic.dev/logfire). The free tier includes 10 million spans a month, our AI gateway, and so much more.
