---
title: LLM Judge Evals for Ollama Models with Eval Protocol | Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/llm-judge-eval-ollama-local-models
author: null
published: '2025-10-15'
fetched: '2026-10-23T06:15:12Z'
classifier: null
taxonomy_rev: 2
words: 496
content_sha256: bf33737b7ae9ad3f88259c2d31070735ebcbd4ed883df95e2f04ba27cc300e0f
---

# LLM Judge Evals for Ollama Models with Eval Protocol | Fireworks

Modern AI apps rarely run on a single model forever. Teams iterate, swap providers, and increasingly run open-source models locally for privacy, latency, and cost. This post shows how to use [**Fireworks Eval Protocol**](https://evalprotocol.io/introduction) to do robust model picking and how to **host models locally with Ollama** so you can replace OpenAI usage at scale—without rewriting your app logic.

We’ll walk through two real examples in this repo:

- End-to-end agent evaluation on the Chinook dataset (PydanticAI)
- LLM-judge over Langfuse traces you already have in production

The core idea: keep your evaluation harness the same; only swap the model backend using an OpenAI-compatible endpoint (Ollama).

![image image](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2Fdceddc756a7deebd325c9f4623823db932cb94bd-1378x1386.png%3Fauto%3Dformat&w=3840&q=75)

### Why this approach works

- **Standard interface**: Eval Protocol treats models as swappable via `completion_params` (model name, provider, base\_url, etc.).
- **OpenAI-compatible**: Ollama exposes an OpenAI-style API locally, so clients keep working with only config changes.
- **Evidence-based model picking**: Run apples-to-apples comparisons across datasets and traces. Keep the judge and scoring constant while changing only the model backend.

### Prerequisites

- This repo set up locally (Python environment ready)
- macOS or Linux
- [Ollama](https://ollama.com/) installed and running

### Install and run Ollama

`bashCopy`
123456789101112

### Example 1: End-to-end agent evaluation (Chinook + PydanticAI)

In this example, the agent is created from `completion_params` and automatically supports either OpenAI or Ollama depending on `provider` and `base_url`.

`pythonCopy`
1234567891011121314151617

To add a local OSS model (via Ollama), include an entry like the one below in completion\_params alongside any OpenAI models you want to compare against:

`pythonCopy`
123

Run the evaluation locally:

`bashCopy`
123

The harness executes multiple runs, collects assistant outputs, and scores them with an LLM judge, so you can compare models head-to-head with the same prompts and tasks.

From running the evaluation, we can see that qwen3:8b is actually better than gpt-4o-mini out of the box, so for this task, if I was using gpt-4o-mini, I can now just seamlessly transition to qwen3:8b local! It is definitely still worse than gpt-5-nano and other bigger model remotely. Unfortunately qwen3:4b and granite4:micro is still doing very badly on these tasks, and we really hope IBM can put out better small models for us to experiment with in the future.

### Example 2: Judge Langfuse traces and swap the model to Ollama

Already logging to Langfuse? You can convert those traces into evaluation rows and judge them—then point the judge at a local model by changing only `completion_params`.

The data loader pulls traces:

`pythonCopy`
123456789

Swap in a local model by parametrizing with an Ollama-backed entry:

`pythonCopy`
12345678910

The evaluation harness remains unchanged; the judge remains unchanged; your traces remain the same. Only the model backend switches, making it safe and fast to validate replacement candidates.

### Takeaway

[**Fireworks Eval Protocol**](https://evalprotocol.io/introduction) lets you make data-driven model choices, test replacements quickly, and migrate from OpenAI to local open-source models on **Ollama**—all with minimal code changes. Keep your evaluation and logging workflows intact; just point the model at a different backend.
