---
title: Introducing GLM 5.2 Fast
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-glm-52-fast/
author: Abu Qader; Philip Kiely; Alina Weinstein
published: '2026-07-23'
fetched: '2026-07-24T06:49:43Z'
classifier: null
taxonomy_rev: 2
words: 371
content_sha256: a74ee2fb74988cd5ef6494e45240797754198441367f80c1dbb45a906481b3b9
---

# Introducing GLM 5.2 Fast

![Baseten's Fast GLM-5.2 endpoint](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1784828449-model-release-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Today, we're introducing GLM-5.2 Fast: a separate Model API tier that serves the same GLM-5.2 weights on infrastructure tuned for per-user throughput for real-time applications. You can [try it here now](https://app.baseten.co/model-apis/glm-5-2-Fast) or switch over your GLM-5.2 standard to the endpoint `zai-org/GLM-5.2-Fast`.

![Video](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2FTxjFcGXZ4M5n00jYB4dy1Yxvkq493bzdZ%2Fthumbnail.jpg&w=3840&q=75)

## Why agentic workloads need a different tier

When GLM-5.2 shipped, it was strong enough at coding and tool use that teams started moving real-time agentic workloads onto it.

Agentic workflows are systems: a main agent plans, delegates to subagents, reviews their work, and merges the results. Each handoff is another inference call and another place latency can compound.

GLM-5.2 Fast transforms this workflow because it’s an open model we trust as the main agent, not just for the subagents around it. It’s smart enough to coordinate the workflow, cost-effective enough to scale across subagents, and fast enough to keep the entire system competitive.

## GLM-5.2 Fast preserves ease-of-use with tighter performance guardrails

GLM 5.2 Fast serves the same weights as standard GLM-5.2, on infrastructure provisioned differently for real-time agentic use cases. It offers:

- Ease-of-use: Model APIs are just that; OpenAI-compatible API endpoints you point your code at. There’s no infrastructure to manage, and you pay only for what you use (per 1M tokens). 
- Tighter performance SLAs: our Fast tier is built to handle even the most variable, bursty workloads while maintaining a small variance in throughput and latency metrics. 

## Switching from standard GLM-5.2

Because Fast is just a model slug, switching is a one-line change:

```
1import os
2from openai import OpenAI
3
4client = OpenAI(
5    api_key=os.environ["BASETEN_API_KEY"],
6    base_url="<https://inference.baseten.co/v1>",
7)
8
9response = client.chat.completions.create(
10    model="zai-org/GLM-5.2-Fast",
11    messages=[{"role": "user", "content": "Refactor this function to be async."}],
12    stream=True,
13)
```
You can run Fast alongside standard GLM-5.2, route by workload — agentic loops to Fast, batch summarization to standard — and see usage per tier separately in your dashboard. Most real deployments mix latency-sensitive and latency-tolerant traffic; routing each to the tier it needs cost-efficiently.

## Getting started

Access is fully open at launch. Customers can access directly through the UI or through their account team. Switching over is a one-line model slug change. You can start using it [here](https://app.baseten.co/model-apis/glm-5-2-fast).
