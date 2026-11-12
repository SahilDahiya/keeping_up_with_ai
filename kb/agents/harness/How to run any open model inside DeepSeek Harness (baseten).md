---
title: How to run any open model inside DeepSeek Harness
kind: blog
topic: agents
subtopic: harness
secondary_topics: []
summary: 'Describes the DeepSeek Harness (DSH) architecture: a plugin-based meta-harness
  where models, tools, sandboxes, and subagent harnesses are swappable components
  backed by an append-only, forkable/replayable event log.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-run-any-open-model-inside-deepseek-harness
author: Alex Ker
published: '2026-08-24'
fetched: '2026-11-12T06:15:18Z'
classifier: claude
taxonomy_rev: 2
words: 565
content_sha256: 13e960118d51b8210722ee288f631acb1b683a2adeda79c78467537f21b65445
---

# How to run any open model inside DeepSeek Harness

AI engineering
# How to run any open model inside DeepSeek Harness

Learn how to power DeepSeek Harness with Baseten Model APIs and run open models like Kimi K3, GLM 5.2, and DeepSeek V4 Pro in under 5 minutes.


- Authors
- Date
- August 24, 2026

TLDR

The DeepSeek Harness isn't a harness, but an interface for running many of them, with everything (models, tools, sandboxes, subagents) as a swappable plugin and an append-only event log you can fork and replay. Here's how to power it with Baseten Model APIs and run open models like Kimi K3, GLM 5.2, and DeepSeek V4 Pro in under 5 minutes.

The DeepSeek Harness (DSH) is, in some sense, a bigger release than the v4 models themselves. In this post you'll first understand the most useful parts of the DeepSeek Harness, which isn't really a harness, but an interface for running many harnesses. Then, we’ll walk through how to run any open model inside it with Baseten inference in \<5 minutes.

We previously wrote about what might come after harnesses: moving up the abstraction plane into a centralized interface that manages a fleet of N harnesses, each co-evolved to perform best for a given model and task (more [here](https://x.com/thealexker/status/2085808354660647405.)). DeepSeek Harness is an instantiation of that idea. Inside it you can run Claude Code, Codex, and various harness SDKs as components.

The core idea behind DSH is that everything is a plugin: models, tools, file systems, sandboxes, and loops are all modular components that can be swapped, composed, and extended. You run a suite of open and closed models inside ctx.llm, and other harnesses inside ctx.subagents as child processes.

There's also an append-only event log with fork and replay. This lets you track trajectories and tool calls, find where a run went wrong in the traces, and then rerun or modify the original session. The same property makes it useful for gathering post-training and RL data, and serves as a visual debugger.

Finally, DSH is self-evolving: it gives you a stable way to inspect the runtime, write plugins, and mount them in real time without breakage. As a result, we now have an amazing UI for people experimenting and testing on their setup with minimal friction.

Here's how to run frontier open-weight models like Kimi K3, GLM 5.2, and DeepSeek V4 Pro 0813 inside the harness, served from Baseten's Model APIs:

1\. Clone the repo in terminal and start the web UI

bash

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```
2\. Go to Settings → Models → Add a custom provider.

- Set Base URL as: [https://inference.baseten.co/v1](https://inference.baseten.co/v1)
- API protocol: openai-completions
- Grab and paste in the API key from [https://app.baseten.co/settings/api\_keys](https://app.baseten.co/settings/api_keys)

3\. Populate the model catalog. Under Model catalog, click Fetch to pull the available models with your API key. This hits Baseten's /v1/models endpoint and returns the current [supported models](https://docs.baseten.co/inference/model-apis/overview#supported-models). For this tutorial I've added just three to keep things simple.

4\. Now you can select model via the dropdown at the side of the chat window.

5\. Run and inspect. You can send a prompt and open the trajectory view. Each run streams its event log as a timeline. Per request, you can watch latency and throughput signals like time-to-first-token and cache hit rate, so you see the true cache hit rate and performance metrics for any provider.
