---
title: 'Qwen 3 on Fireworks: Controllable Chain-of-Thought and Tool Calling at Frontier
  Scale'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/qwen-3
author: null
published: '2025-05-06'
fetched: '2026-08-12T06:29:05Z'
classifier: null
taxonomy_rev: 2
words: 442
content_sha256: 75ebf2e54ceb33e7b908e419df4491e8704bc78d1ecab5afaba12c73aeaafd8e
---

# Qwen 3 on Fireworks: Controllable Chain-of-Thought and Tool Calling at Frontier Scale

- •**Reasoning meets function calls.** Qwen 3 now streams an explicit … trace**and** the exact JSON tool call in the same completion.
- •**Turbo or stealth—your choice.** Flip reasoning_effort="none" (or use the /think / /no_think tags) to trade transparency for raw throughput on the fly.
- •**Mixture-of-Experts giant, pay-as-you-go.** The 235 B-parameter / 22 B-active**Qwen3-235B-A22B** runs serverlessly on Fireworks.
- •**Drop-in OpenAI compatibility.** Use the Fireworks endpoint with the official OpenAI client; everything else stays the same.

Until now, open-source LLMs forced a choice: **show the chain of thought** or **call tools deterministically**. Qwen 3’s new architecture does both in one pass, and keeps the reasoning block segregated so downstream code can ignore or audit it at will.

Pair that with a **128-expert MoE** that only activates eight experts (≈22 B live parameters) and you get near-frontier quality at a fraction of the compute- fully Apache-2.0 and live on Fireworks today ([Fireworks - Qwen3 235B-A22B model](https://fireworks.ai/models/fireworks/qwen3-235b-a22b)).

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455

The first call contains reasoning chain of thought + tool call, the second doesn’t think, and just makes the tool calls.

- •**Thinking mode** (`reasoning_effort!=”none”` )
  - •Generates `<think> … </think>` and a final answer.
  - •Recommended params: `temperature ≈ 0.6, top_p ≈ 0.95, top_k = 20` .
- •Generates 
- •**Non-thinking mode** (`reasoning_effort=”none”` or a`/no_think` tag)
  - •Omits the reasoning block to save tokens and latency.
  - •Use slightly spicier sampling: `temperature ≈ 0.7, top_p ≈ 0.8` .

Because the trace sits in its own tag, you can log, redact, or meter it independently- the same pattern we covered in **Constrained Generation with Reasoning**.

| - | Qwen 3-235B-A22B | 
|---|---|
| Total parameters | 235 B (Mixture-of-Experts) | 
| Active parameters | 22 B (8 / 128 experts) | 
| Layers | 94 | 
| Attention heads | 64 / 4 | 
| Context window | 32 768 tokens (native) 131 072 with YaRN | 
| License | Apache-2.0 | 
| Endpoint | accounts/fireworks/models/qwen3-235b-a22b | 

- •**Long answers** – Allocate at least 4 k output tokens for essays; up to 32 k for book-length generations.
- •**Cost & speed control** – Invoke reasoning only on the turns that need it, then strip`<think>` before storage.

Our endpoint is fully OpenAI compatible, please give it a try!

12345678

With **Qwen 3-235B-A22B**, open-source finally gets a model that:

1. Reveals its chain of thought when you ask.
2. Emits tool calls in the exact same request.
3. Scales to frontier-size contexts- all under Apache-2.0.

No secret weights, no bespoke SDKs. Just point your existing OpenAI-style client at Fireworks and build.

Questions, feedback, or cool demos? Drop by our [Discord](https://discord.gg/fireworks-ai) or tag us on X.

Happy shipping!
