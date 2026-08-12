---
title: 'MiniMax M3 is live: long context + native multimodality at 1/20th the price'
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- inference/kernels
summary: MiniMax M3's extended context comes from MSA (MiniMax Sparse Attention),
  which pre-filters and blocks KV caches with a 'KV outer gather Q' operator ordering
  that fetches each block once, delivering >4x speedup over Flash-Sparse-Attention/flash-moba,
  95% lower per-token compute, and 9x/15x faster prefill/decode at 1M-token context
  versus M2.7.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/minimax-m3-launch
author: null
published: '2026-06-12'
fetched: '2026-08-12T06:29:29Z'
classifier: claude
taxonomy_rev: 2
words: 944
content_sha256: 40bb2000bb58e36ed34aaab5f7304653063bd0455577769b5c939ea9bba9e3c7
---

# MiniMax M3 is live: long context + native multimodality at 1/20th the price

MiniMax M3 is MiniMax's flagship frontier model and a meaningful step forward for the open-weight ecosystem — delivering strong agentic capabilities, native multimodality, and a >500K token context window in a single model.

The open-weight frontier has been advancing quickly. Kimi K2.5 pushed the bar on native multimodal input in January 2026, natively understanding text, images, and video for visual-to-code workflows. DeepSeek V4 extended long-context capabilities with its 1M-token window in April, but remains text-input only. M3 brings that long context scaling and multimodal understanding together in one package. At launch, we're supporting up to 500K tokens of context, but are partnering closely with the MiniMax team to bring the full 1M-token context window length in the coming days.

We are launching Day-0 support for MiniMax M3 on Fireworks. Fireworks offers the fastest endpoint for the full MiniMax model series. With M3 now live, developers can immediately take advantage of its long-horizon agentic capabilities, image and video understanding, and strong context scaling for demanding production workloads.

MiniMax M3 sets a high bar for what open-weight models can do. Across provider-reported benchmarks and affirmed by Artificial Analysis' 3rd-party intelligence index, MiniMax M3 surpasses all other open-source models in overall intelligence and exceeds several closed-source models including Opus 4.6.

While benchmark fatigue is real, knowing that a model is at least on the frontier of major benchmarks remains a useful litmus for whether it's worth evaluating first-hand. In that sense, MiniMax M3 passes the first-look test.

The breakthrough enabling M3's extended context window is MSA (MiniMax Sparse Attention). Standard full attention scales exponentially as context grows. MSA scales sub-quadratically by implementing a pre-filtering stage that partitions KV (key-value) caches into blocks with higher effective context coverage than approaches like DeepSeek's Sparse Attention (DSA) or Moonshot's Mixture of Blocks Attention (MoBA).

MiniMax also optimized at the operator level with a "KV outer gather Q" approach, iterating over KV blocks in the outer loop so each block is fetched from memory only once. The result: **more than 4× faster** than open-source Flash-Sparse-Attention and flash-moba, with arithmetic intensity that scales cleanly with M3's head configuration.

At its full 1M-token context ceiling, M3's gains vs. M2.7 represent a meaningful architectural step:

- •Per-token compute **dropped by 95%**
- •**9× speedup** in the pre-filling stage
- •**15× speedup** in the decoding stage

__*Note on context at launch__: The current open-weight release supports up to 500K tokens of context. This covers the majority of long-context workloads (full-repository understanding, long-document analysis, multi-turn agentic sessions) while we work to enable the full 1M-token capability. We'll update this post when that's available.

In MiniMax's own testing, MSA doesn't meaningfully hurt quality despite being computationally much more efficient. The speedup figures mean that long-context inference is viable at real-time production latency.

M3 was built with real-world coding and agentic workflows at its core. MiniMax developed an **interactive user simulator framework** to train M3 on multi-turn development scenarios that mirror how engineers actually work: clarifying requirements, adjusting solutions, switching tasks, and iterating based on intermediate results.

To read about real-world demonstrations of M3 across multiple 12hr+ autonomous agentic tasks demonstrated by MiniMax (academic paper reproduction, kernel optimization, and model fine-tuning), [head over to the official launch post](https://www.minimax.io/blog/minimax-m3). 

As is the expectation for frontier models in June 2026, M3 goes well beyond single-turn code generation into long-horizon autonomous collaboration. It is well-suited for agentic existing and new use cases running on Fireworks today.

MiniMax M3 is priced at 2x the price of M2.7 on Fireworks’ [Serverless inference](https://docs.fireworks.ai/serverless/overview):

For teams already running M2.7 workloads that would benefit from longer context, agentic execution, or multimodal inputs, M3 offers a competitive price-to-capability ratio relative to closed-source alternatives, even at the initial private launch pricing (~2x higher than M2.7). As of the open-weights launch, pricing has been permanently dropped to remain on-par with M2.7, making it a no-brainer for any developers currently running workloads on MiniMax M2.7.

- •__Note on long-context pricing__**:** Calls with input tokens ≤512K are billed at the standard rate. Calls above 512K are billed at a higher long-context rate, suited to workloads like full-repository code understanding and ultra-long document parsing. (Note: only <500K context is supported at launch; the higher tier will apply when full 1M support ships, and will still be ~2x higher than the lower context requests.)
- •__Thinking mode__**:** M3 supports toggling thinking on or off at request time, with both modes sharing the same pricing. Enable thinking for complex reasoning and agentic tasks; disable it for lower-latency scenarios like chat and code completion.

M3 is the right choice when your workload demands long-horizon agentic execution, complex multi-turn coding collaboration, long-document understanding, or multimodal inputs (images and video). For tasks that are primarily text-based conversation, retrieval, or lower-latency scenarios where M2.7's capabilities are sufficient, M2.7 remains a highly cost-effective option.

For video inputs, note that currently video input is supported with URL-based uploads (raw .mp4 uploads not yet supported).

To get started, test MiniMax M3 on our chat completions endpoint. Here's a multimodal request using the Fireworks API:

123456789101112131415161718192021222324252627282930313233343536373839

To enable thinking mode, add `"thinking": {"type": "enabled"}` to your request payload. For more details on controlling reasoning behavior, [see our docs](https://docs.fireworks.ai/guides/reasoning).

MiniMax M3 is available on Fireworks via serverless for teams that want to get started fast, and on-demand deployments for production workloads that need the best performance and predictable throughput. Start building today with strong agentic coding capabilities, 500K-token context, and native multimodality — or if you're evaluating M3 for a specific workload, we'd love to support what you're working on.

[→](https://fireworks.ai/models/fireworks/minimax-m3)[Start building with MiniMax M3 on Fireworks](https://fireworks.ai/models/fireworks/minimax-m3) [←](https://fireworks.ai/models/fireworks/minimax-m3)

Questions? Join our [Discord](https://discord.gg/fireworks-ai) or [contact us](https://fireworks.ai/contact) to schedule a meeting with our solutions team.
