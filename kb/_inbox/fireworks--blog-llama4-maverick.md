---
title: Optimizing Llama 4 Maverick on Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/llama4-maverick
author: null
published: '2025-04-28'
fetched: '2026-08-12T06:30:37Z'
classifier: null
taxonomy_rev: 2
words: 387
content_sha256: 55e30a636e84f6373e5de9d13410dd3749cf154c02b6a941db17dd07f2196ddb
---

# Optimizing Llama 4 Maverick on Fireworks

Meta's Llama 4 Maverick is their initial natively-multimodal, Mixture-of-Experts (MoE) model.

This model processes both text and images, directing tokens through specialized expert blocks. Notably, it features a significantly expanded **context window of 1 million tokens**, a 10x increase compared to other models. This advancement allows for keeping extensive code repositories, complete product specifications, or lengthy user conversations in its memory.

Minutes after Meta published the weights, the model showed up in the Fireworks catalogue ([accounts/fireworks/models/llama4-maverick-instruct-basic](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic)). Early adopters, including many of the edge-AI researchers who benchmarked the model, were already hitting the endpoint before most providers finished container builds.

To enable superior performance of Llama 4 we leveraged multiple components of Fireworks Platform:

1. Tuned FP8 quantization scheme through [FireOptimizer](https://fireworks.ai/blog/fireoptimizer) that follows recommended Llama quantization strategy (delivering both memory savings and faster generation speeds due to less memory bandwidth required)
2. Combination of tensor and expert parallelism depending on target workload
3. Custom attention implementation ([FireAttention](https://fireworks.ai/blog/fireattention-v2-long-context-inference) ) that we extended to include Llama 4’s novel chunked local attention variant.
4. Customized speculative decoding with a drafter model trained through [FireOptimizer](https://fireworks.ai/blog/fireoptimizer)
5. Out of box support for prompt caching and prefill-heavy optimizations
6. Highly optimized LLM runtime that ensures sufficient batching and overlapping for fully unblocked asynchronous GPU execution 100% of time.

The flexibility of the platform enabled Fireworks to be the **first public Llama 4 API**.

Independent testing by [Artificial Analysis](https://artificialanalysis.ai/models/llama-4-maverick/providers) [on April 27, 2025](https://artificialanalysis.ai/models/llama-4-maverick/providers), demonstrates that Fireworks delivers **145 tokens per second** for streaming throughput of [Llama 4 Maverick](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic), running on H200. This performance is **10-20% faster** than the closest competitor and more than double the speed of managed Azure endpoints (Artificial Analysis).

**Figure 1.** Llama 4 Maverick Output-Token Speed (27 Apr 2025).

Fireworks exposes an **OpenAI-compatible function-calling interface**; just pass a JSON schema via tools and receive a deterministic function_call object.

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103

If you need the fastest, largest-context, multimodal Llama 4 endpoint with production-grade function calling, Fireworks is the current engineering sweet spot.

Spin up the API, point your existing OpenAI client to it, and enjoy 145 tokens-per-second chat with a million-token brain: [https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic)

PS: The llama4-maverick running on Serverless is on the public tier, and hence performance might vary, depending on traffic. If you intend to achieve optimal speeds, and customize for your needs, we recommend running it on on-demand deployment.

Happy building! 🚀
