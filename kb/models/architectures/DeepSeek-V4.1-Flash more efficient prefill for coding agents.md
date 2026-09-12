---
title: 'DeepSeek-V4.1-Flash: more efficient prefill for coding agents'
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- inference/optimization
summary: DeepSeek-V4.1-Flash introduces a Causal Encoder-Decoder architecture that
  splits its 40 layers into a 20-layer encoder and 20-layer decoder, activating only
  8B params for prefill vs 16B for decode, and combines this with Compressed Sparse
  Attention 2 and FP4 KV caching to cut the global KV cache to a quarter of V4-Flash's
  size.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deepseek-v41-flash-more-efficient-prefill-for-coding-agents/
author: Albert Lee; Kenzie Amack; Marylise Tauzia
published: '2026-09-11'
fetched: '2026-09-12T06:08:55Z'
classifier: claude
taxonomy_rev: 2
words: 906
content_sha256: 456917e590ee7831a0cedddebb555a798c4e50c7cac8996a8eb9b2f72eeb7bdb
---

# DeepSeek-V4.1-Flash: more efficient prefill for coding agents

![DeepSeek-V4.1-Flash](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789155458-model-release-upscaled-2x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

DeepSeek released V4.1-Flash this week: a 552B-parameter multimodal MoE model with a Causal Encoder-Decoder architecture built for coding agents. It's available now as a Baseten Model API, with improved KV cache efficiency and asymmetric prefill/decode compute over its V4 predecessors.

This week, DeepSeek [released the open weights for DeepSeek-V4.1-Flash on HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash), and the model is already [available on Baseten Model APIs](https://www.baseten.co/library/deepseek-v41-flash/) (with [Loops](https://www.baseten.co/products/training/) support coming soon). Key specifications include:

- 552B total parameters
- 8B active parameters for prefill, 16B for decode
- 1M token context window
- Multimodal input (text + image), text output

Originally popularized by Google's Gemini series, the "flash" designation describes lighter, less expensive models designed to perform similarly to larger ones. V4.1-Flash marks DeepSeek's third open-weight flash release this year, joining recent offerings from Z.ai and Alibaba as model labs deliver higher intelligence at lower price points for coding agent workloads.

## Comparing DeepSeek models: old versus new 

DeepSeek V4.1-Flash demonstrates improvements over V4-Flash and V4-Pro models in both text and multimodal capabilities.

On coding and agentic benchmarks, V4.1-Flash beats V4-Pro with roughly a third of the total parameters. The biggest jumps are on long-horizon agentic tasks, which improve by double digits, while single-shot command-line tasks improve more modestly. The gains are real, but a 54.8 on Automation-Bench means it fails roughly half of complex workflows. Keep a human in the loop for agent pipelines.

*Taken from* *HuggingFace DeepSeek-ai/DeepSeek-V4.1-Flash model card***Top score is 100 for all noted benchmarks.*

V4.1-Flash is DeepSeek's first non-experimental model with native image input, which was previously limited to V4-Flash-Vision-Exp. Visual reasoning improves in this generation too, particularly on chart interpretation and logical reasoning over images, which are useful if you're feeding it screenshots, dashboards, or UI mockups. However, the ZeroBench score still falls short of 50, and at that level, you'll still want a human reviewing image-based reasoning for anything consequential.

*Taken from* *HuggingFace DeepSeek-ai/DeepSeek-V4-Flash-Vision-Exp model card***Top score is 100 for all noted benchmarks.*

DeepSeek has retired the V4-Flash models on its platform and now routes their traffic to V4.1-Flash. V4-Pro traffic will also be rerouted beginning September 14. If you're running any DeepSeek V4 model, upgrade to V4.1-Flash. It's also worth a look if you're using a large general-purpose model from another lab and want stronger, more efficient coding and agentic performance.

## Asymmetric activation parameters for more efficient compute usage

DeepSeek-V4.1-Flash is the only model of its scale to use a Causal Encoder-Decoder (CED) architecture.

Two key steps in model computation are:

- Prefill: Reading the input
- Decode: Generating the output

Other MoE models activate the same number of parameters for both the prefill and decode steps. CED splits V4.1-Flash's 40 layers into a 20-layer causal encoder and a 20-layer decoder, and the decoder's KV cache is projected directly from the encoder's output. That means prefill only needs to run the encoder, activating 8B parameters per token, while decode runs the full model at 16B.

The idea is that generating output is harder than reading input, so computation is prioritized for decode over prefill. For comparison, V4-Flash activates 13B for both prefill and decode, so V4.1-Flash trades a heavier decode (16B) for a much lighter prefill (8B).

![CED reduces prefill computation by stopping at the encoder and reusing a projected KV cache during decoding.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789154587-screenshot-2026-09-11-at-12-22-57-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) CED reduces prefill computation by stopping at the encoder and reusing a projected KV cache during decoding.

This setup boosts cost efficiency for coding agents, where agentic loops generate far more prefill tokens than decode tokens. Additionally, because the decoder's key-value states are projected from the encoder output rather than computed independently in every layer, CED contributes to a much smaller KV cache, which cuts caching costs.

## More savings through KV cache improvements

According to DeepSeek, V4.1-Flash's global KV cache requires just a quarter of the memory of V4-Flash's. The CED architecture contributes by projecting the decoder's KV cache from the encoder's output rather than computing it independently. It also works with two other techniques to further reduce KV cache.

- Compressed Sparse Attention 2: Share key-value entries across attention layers
- FP4 KV caching: Store key-value entries at lower precision.

![DeepSeek-V4.1-Flash’s global KV cache requires less memory per token.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789154884-img_4007.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) DeepSeek-V4.1-Flash’s global KV cache requires less memory per token.

*Taken from* *Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.*

Less memory per token means more context fits in the cache, raising the hit rate. When a prompt's prefix is already cached, the model skips recomputing attention over those tokens, cutting time-to-first-token and raising throughput per GPU. Coding agents benefit most, since agentic loops resend largely the same context on every step. Capturing that reuse in production depends on how requests are routed across GPUs, which is where the serving stack comes in.

## Production inference for DeepSeek-V4.1-Flash

The Baseten Inference Stack handles that routing with NVIDIA Dynamo and KV cache-aware routing, which steer each request to the replica already holding its prefix instead of whichever replica is free.

![“KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.”](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789154969-1763057468-kvroutingchart.avif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) “KV-aware routing sends requests to replicas that already have relevant context cached, saving time by avoiding redundant prefill computation.”

*Taken from* *2x faster inference with KV cache-aware routing*

All of this runs behind [Baseten Model APIs](https://app.baseten.co/model-apis/deepseek-ai/DeepSeek-V4.1-Flash), where DeepSeek-V4.1-Flash is available now. Try it in our [Model Library](https://www.baseten.co/library/deepseek-v41-flash/) or [reach out to us](https://www.baseten.co/talk-to-us/?model=deepseek-v41-flash) about a dedicated deployment if your team needs reserve capacity.
