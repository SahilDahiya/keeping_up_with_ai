---
title: 'DeepSeek-V4.1-Flash: more efficient prefill for coding agents'
kind: blog
topic: models
subtopic: releases
secondary_topics: []
summary: 'DeepSeek-V4.1-Flash: a 552B-parameter multimodal MoE model (8B active for
  prefill, 16B for decode, 1M context) with a causal encoder-decoder architecture;
  beats V4-Pro on long-horizon agentic benchmarks with a third of the parameters but
  still scores only 54.8 on Automation-Bench.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deepseek-v41-flash-more-efficient-prefill-for-coding-agents
author: Albert Lee
published: '2026-09-11'
fetched: '2026-11-12T06:08:38Z'
classifier: claude
taxonomy_rev: 2
words: 968
content_sha256: ff8436545b0a311f5faee1577a3fe211b7450834cd4e05d69cb5d36d0409d847
---

# DeepSeek-V4.1-Flash: more efficient prefill for coding agents

AI models
# DeepSeek-V4.1-Flash: more efficient prefill for coding agents

Discover DeepSeek-V4.1-Flash, a 552B multimodal MoE model featuring a Causal Encoder-Decoder architecture and efficient KV caching.


- Authors
- Date
- September 11, 2026

TLDR

DeepSeek released V4.1-Flash this week: a 552B-parameter multimodal MoE model with a Causal Encoder-Decoder architecture built for coding agents. It's available now as a Baseten Model API, with improved KV cache efficiency and asymmetric prefill/decode compute over its V4 predecessors.

This week, DeepSeek [released the open weights for DeepSeek-V4.1-Flash on HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), and the model is already [available on Baseten Model APIs](https://www.baseten.co/library/deepseek-v41-flash/) (with [Loops](https://www.baseten.co/products/training/) support coming soon). Key specifications include:

- 552B total parameters
- 8B active parameters for prefill, 16B for decode
- 1M token context window
- Multimodal input (text + image), text output

Originally popularized by Google's Gemini series, the "flash" designation describes lighter, less expensive models designed to perform similarly to larger ones. V4.1-Flash marks DeepSeek's third open-weight flash release this year, joining recent offerings from Z.ai and Alibaba as model labs deliver higher intelligence at lower price points for coding agent workloads.

DeepSeek V4.1-Flash demonstrates improvements over V4-Flash and V4-Pro models in both text and multimodal capabilities.

On coding and agentic benchmarks, V4.1-Flash beats V4-Pro with roughly a third of the total parameters. The biggest jumps are on long-horizon agentic tasks, which improve by double digits, while single-shot command-line tasks improve more modestly. The gains are real, but a 54.8 on Automation-Bench means it fails roughly half of complex workflows. Keep a human in the loop for agent pipelines.

| Benchmark | Good indication for | V4.1-Flash | V4-Flash-0731 | V4-Pro | 
|---|---|---|---|---|
| Terminal Bench 2.1\*: Complete command-line coding tasks | Shell scripting, build and deploy steps, environment setup, terminal-based coding agents | 90.6 | 82.7 | 87.9 | 
| DeepSWE v1.1\*: Submit PRs to resolve bugs in GitHub repositories | Autonomous bug fixing and multi-file code changes in real repos (issue-to-PR agents) | 74.2 | 54.4 | 62.7 | 
| Automation-Bench\*: Execute business workflows across SaaS applications | Multi-step tool calling across SaaS APIs: CRM updates, ticket triage, ops workflows | 54.8 | 37.7 | 43.2 | 

*Taken from HuggingFace DeepSeek-ai/DeepSeek-V4.1-Flash model card\*Top score is 100 for all noted benchmarks.*

V4.1-Flash is DeepSeek's first non-experimental model with native image input, which was previously limited to V4-Flash-Vision-Exp. Visual reasoning improves in this generation too, particularly on chart interpretation and logical reasoning over images, which are useful if you're feeding it screenshots, dashboards, or UI mockups. However, the ZeroBench score still falls short of 50, and at that level, you'll still want a human reviewing image-based reasoning for anything consequential.

| Benchmark | Good indication for | V4.1-Flash | V4-Flash-Vision-Exp | 
|---|---|---|---|
| Chartography\*: Interpret data visualizations | Reading charts, dashboards, and reports; extracting numbers or trends from plotted data | 78.9 | 64.3 | 
| ZeroBench\*: Answer logical questions using images | Reasoning over screenshots, diagrams, and UI mockups where the answer requires logic, not just recognition | 49 | 35 | 

*Taken from HuggingFace DeepSeek-ai/DeepSeek-V4-Flash-Vision-Exp model card\*Top score is 100 for all noted benchmarks.*

DeepSeek has retired the V4-Flash models on its platform and now routes their traffic to V4.1-Flash. V4-Pro traffic will also be rerouted beginning September 14. If you're running any DeepSeek V4 model, upgrade to V4.1-Flash. It's also worth a look if you're using a large general-purpose model from another lab and want stronger, more efficient coding and agentic performance.

DeepSeek-V4.1-Flash is the only model of its scale to use a Causal Encoder-Decoder (CED) architecture.

Two key steps in model computation are:

- Prefill: Reading the input
- Decode: Generating the output

Other MoE models activate the same number of parameters for both the prefill and decode steps. CED splits V4.1-Flash's 40 layers into a 20-layer causal encoder and a 20-layer decoder, and the decoder's KV cache is projected directly from the encoder's output. That means prefill only needs to run the encoder, activating 8B parameters per token, while decode runs the full model at 16B.

The idea is that generating output is harder than reading input, so computation is prioritized for decode over prefill. For comparison, V4-Flash activates 13B for both prefill and decode, so V4.1-Flash trades a heavier decode (16B) for a much lighter prefill (8B).

This setup boosts cost efficiency for coding agents, where agentic loops generate far more prefill tokens than decode tokens. Additionally, because the decoder's key-value states are projected from the encoder output rather than computed independently in every layer, CED contributes to a much smaller KV cache, which cuts caching costs.

According to DeepSeek, V4.1-Flash's global KV cache requires just a quarter of the memory of V4-Flash's. The CED architecture contributes by projecting the decoder's KV cache from the encoder's output rather than computing it independently. It also works with two other techniques to further reduce KV cache.

- Compressed Sparse Attention 2: Share key-value entries across attention layers
- FP4 KV caching: Store key-value entries at lower precision.

Less memory per token means more context fits in the cache, raising the hit rate. When a prompt's prefix is already cached, the model skips recomputing attention over those tokens, cutting time-to-first-token and raising throughput per GPU. Coding agents benefit most, since agentic loops resend largely the same context on every step. Capturing that reuse in production depends on how requests are routed across GPUs, which is where the serving stack comes in.

The Baseten Inference Stack handles that routing with NVIDIA Dynamo and KV cache-aware routing, which steer each request to the replica already holding its prefix instead of whichever replica is free.

All of this runs behind [Baseten Model APIs](https://app.baseten.co/model-apis/deepseek-ai/DeepSeek-V4.1-Flash), where DeepSeek-V4.1-Flash is available now. Try it in our [Model Library](https://www.baseten.co/library/deepseek-v41-flash/) or [reach out to us](https://www.baseten.co/talk-to-us/?model=deepseek-v41-flash) about a dedicated deployment if your team needs reserve capacity.
