---
title: Introducing GLM-5.2 Fast
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-glm-52-fast
author: Abu Qader
published: '2026-07-23'
fetched: '2026-11-12T06:08:08Z'
classifier: null
taxonomy_rev: 2
words: 356
content_sha256: d43388d44fa661a32c8bfbe1602caddf5bc6cd0eb7cee1c5444589ab2e7ddc73
---

# Introducing GLM-5.2 Fast

News
# Introducing GLM-5.2 Fast

Introducing our new tier of Fast Model APIs.


- Authors
- Date
- July 23, 2026

Today, we're introducing GLM-5.2 Fast: a separate Model API tier that serves the same GLM-5.2 weights on infrastructure tuned for per-user throughput for real-time applications. You can [try it here now](https://app.baseten.co/model-apis/glm-5-2-Fast) or switch over your GLM-5.2 standard to the endpoint `zai-org/GLM-5.2-Fast`.

When GLM-5.2 shipped, it was strong enough at coding and tool use that teams started moving real-time agentic workloads onto it.

Agentic workflows are systems: a main agent plans, delegates to subagents, reviews their work, and merges the results. Each handoff is another inference call and another place latency can compound.

GLM-5.2 Fast transforms this workflow because it’s an open model we trust as the main agent, not just for the subagents around it. It’s smart enough to coordinate the workflow, cost-effective enough to scale across subagents, and fast enough to keep the entire system competitive.

GLM 5.2 Fast serves the same weights as standard GLM-5.2, on infrastructure provisioned differently for real-time agentic use cases. It offers:

- Ease-of-use: Model APIs are just that; OpenAI-compatible API endpoints you point your code at. There’s no infrastructure to manage, and you pay only for what you use (per 1M tokens).
- Tighter performance SLAs: our Fast tier is built to handle even the most variable, bursty workloads while maintaining a small variance in throughput and latency metrics.

Because Fast is just a model slug, switching is a one-line change:

python

```
import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["BASETEN_API_KEY"],
    base_url="<https://inference.baseten.co/v1>",
)
response = client.chat.completions.create(
    model="zai-org/GLM-5.2-Fast",
    messages=[{"role": "user", "content": "Refactor this function to be async."}],
    stream=True,
)
```
You can run Fast alongside standard GLM-5.2, route by workload — agentic loops to Fast, batch summarization to standard — and see usage per tier separately in your dashboard. Most real deployments mix latency-sensitive and latency-tolerant traffic; routing each to the tier it needs cost-efficiently.

Access is fully open at launch. Customers can access directly through the UI or through their account team. Switching over is a one-line model slug change. You can start using it [here](https://app.baseten.co/model-apis/glm-5-2-fast).
