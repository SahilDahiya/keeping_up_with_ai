---
title: 'Deferred tool loading: Make your agent 62.5% cheaper without changing your
  model or harness'
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- prompt-engineering/context-engineering
- inference/optimization
summary: Deferred (just-in-time) tool loading retrieves MCP tool schemas on demand
  instead of preloading all of them into context, cutting coding-agent costs 62.5%
  and latency 26% on open models (DeepSeek, Kimi, GLM) with no model or harness change.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deferred-tool-loading-without-changing-model-harness/
author: Fred Liu; Alex Ker
published: '2026-11-19'
fetched: '2026-11-24T06:06:38Z'
classifier: claude
taxonomy_rev: 2
words: 1239
content_sha256: 98347ab39e93295cd00672d718882122b5097dec5911b3d38cfcfeb82f89ac6d
---

# Deferred tool loading: Make your agent 62.5% cheaper without changing your model or harness

AI engineering
# Deferred tool loading: Make your agent 62.5% cheaper without changing your model or harness

We brought deferred tool loading to open models, making coding agents up to 62% cheaper and 26% faster with the exact same model and harness.


- Authors
- Published

The best way to cut costs and speed up your agents has always been hidden in plain sight.

Building harnesses have evolved from a discipline of addition to one of subtraction as we move into a world of lean, bitter-lesson-pilled harnesses. Edge cases and guardrails that used to contextualize the model for a task are now more often than not bloat.

So how do we let the model's judgment and intelligence shine through? One way to do this in practice is to retrieve tools just in time on a per-task basis, instead of preloading them, called deferred tool loading. This technique can also be understood as a form of [progressive disclosure](https://www.aihero.dev/a-complete-guide-to-agents-md#the-instruction-budget#use-progressive-disclosure) applied to tools to reduce wasted context.

Suppose you point your agent to any gateway so you can switch between frontier models and open-source models. In theory, this should work great. However, most miss deferred tool loading, which is typically supported by OpenAI and Anthropic APIs. Both Codex and Claude Code turn off deferred tool loading when pointing at a third-party open model provider (like Baseten). You need to remember to turn it back on and ensure that open model providers support this paradigm, because it requires specific server-side gateway and inference implementation.

As a result, gateways that support these models have fallen behind. Without deferred tool loading, every tool schema from your registered MCPs, including many that are unused, is inefficiently passed back with every request, easily costing hundreds of thousands of tokens.

We recently added deferred tool loading to open models (DeepSeek, Kimi, GLM) on Baseten Model APIs to support Chat Completions and Messages API format. In Claude Code, with 3 MCPs turned on (Slack, Notion, Baseten), coding benchmarks were, on average, 62.5% cheaper and 26.2% faster. For agentic benchmarks, we used the preset tools and MCPs in the benchmark and found the tasks were, on average, 51.1% cheaper and 14.9% faster.

Taking a step back, the closest parallel to deferred tool loading comes from web development. Modern frontend development relies on lazy loading that defers resources until they are definitely needed; agents should be no different. Deferred tool loading keeps all tools out of the system prompt and gives models a search tool so they can find the tool they need when they need it.

Without deferred tool loading, for each MCP / plugin that you register (Slack, Notion, Baseten), the full list of tools provided by that MCP and its schema are injected into the system prompt at the start. For example, with 3 MCP servers registered, tool call schemas added \~141k tokens to our system prompt on *every request*. Deferred loading reduced that to \~1.3k tokens. So how does deferred tool loading work under the hood in the harness, and where are the savings coming from?

In eager tool loading, all tool schemas are passed to the API at every request alongside the system prompt. This results in a very bloated cache. Although this prefix is cached, every output token attends to all existing cached KV entries, resulting in significantly more compute and thus time required.

In comparison, deferred loading works by passing the tool names plus a `tool_search` tool (\~1.3k tokens) initially (see client tool search diagram). When the model needs one or more tools, it calls `tool_search`, and the client returns a list of `tool_reference` blocks naming the matching tools. The server then renders the full schema inline at the bottom of the transcript, rather than modifying the system prompt, so the KV cache built over the prefix stays valid. Finally, the assistant calls the real tool.

This maintains the KV cache because future requests share the same prefix through the `tool_search` call, with only the rendered schema and subsequent turns added as new tokens. In both modes, during decode, each new token attends to every token in the cached context, so attention cost per token scales linearly with context length.

In eager mode, the context includes the full list of tool schemas whether or not they’re used, which means reading \~141k KV entries on every generated token. Remember that attention cost is roughly n \* output length per request required to complete the task, where n is the number of tokens in the KV cache. n is \~100x higher in the eager setting in our example. Therefore, a smaller, high-hit-rate prefix via deferred loading makes every decode step cheaper, translating to faster end-to-end request serving time and a better development experience.

We sampled 55 tasks from 8 benchmarks. For each task, we used GLM 5.3 with and without deferred tool loading to measure cost and time.

We wanted to test two kinds of coding harness use cases. What benefit does deferred tool loading provide for almost pure coding tasks, like when you give it a plan and ask it to make a PR? These require minimal tool calls, yet the cost of all registered MCP tools bleeds into every request.

What is the benefit in agentic tasks where the model must search for many tools and go through tool-discovery loops? We chose these two benchmark groups and wanted to understand the trade-offs of deferred tool loading. We found that deferred tool loading performs better than eager loading in both cases and rarely has downsides.

For the coding benchmarks, we chose the combination of:

- Terminal-Bench
- SWE-bench Verified
- SWE-bench Pro v2
- DeepSWE v1.1

For the agentic benchmarks, we used:

- MCP-Atlas
- AutomationBench
- ComplexMCP
- Toolathlon-GYM

We ran these tasks headlessly in Claude Code; for coding benchmarks, we registered 3 MCPs (Slack, Notion, Baseten), and for agentic benchmarks, we registered no MCPs beyond what the benchmarks included natively.

Coding benchmarks saved an average of 62.5% in costs, while agentic benchmarks saved an average of 51.1% compared to eager mode. We found cost savings are greater when:

- Many or bulky MCPs are registered in setup
- Many requests to complete a task (Each one saving a significant chunk of input tokens), like agentic benchmarks

The overall task time drops because each request has fewer tokens on average. The cost of an output token is linear in sequence length, with a large constant n, where n is the KV cache size. Even in agentic benchmarks where the model needed to make many tool searches to load the required tool, time improved significantly. We also measured the average number of tool calls per task; only in the Toolathlon-GYM benchmark (68 tool calls) did we see that loading tools eagerly (or turning off deferred tool loading) inline at the system prompt is more efficient. The DeepSWE and MCP-Atlas tasks were slightly slower, but we consider it negligible because the cost savings outweighed the small time increases.

[Deferred tool loading](https://docs.baseten.co/inference/model-apis/deferred-tool-loading#define-deferred-tools) is a powerful pattern for controlling MCP and tool sprawl inside the agentic harnesses you already use. It’s also generally available through the API if you’re building a context-conscious internal harness for your organization. By adding support for it to open models on Baseten Model APIs, we showed that deferred tool loading can drive outsized savings in tokens and task time on agentic and coding benchmarks.

Try deferred tool loading on [Baseten Model APIs](https://www.baseten.co/products/model-apis) today.
