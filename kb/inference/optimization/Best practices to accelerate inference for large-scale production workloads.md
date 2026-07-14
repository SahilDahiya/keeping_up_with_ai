---
title: Best practices to accelerate inference for large-scale production workloads
topic: inference
subtopic: optimization
secondary_topics: []
summary: Best practices for accelerating inference in large-scale production workloads.
source: together
url: https://www.together.ai/blog/accelerate-inference-large-scale-workloads
author: Together AI
published: '2026-06-22'
fetched: '2026-07-11T04:22:23Z'
classifier: codex
taxonomy_rev: 1
words: 3986
content_sha256: 3ec44b2c3044ccb3b21aafac6c0fcbfab78a52e5c46541955cdd1e2a2540b215
triage: keep
skip_reason: null
---

# Best practices to accelerate inference for large-scale production workloads

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a39b555a6bc30633da4b161_Best_Practices_hero_IMG%20(1).jpg)

TL;DR

Running LLMs in production requires more than deploying a model.

This guide covers the four essential components that determine whether your inference infrastructure scales: optimized kernels that actually saturate GPU hardware, quantization strategies that preserve quality while cutting costs, speculative decoding that reduces latency without accuracy loss, and infrastructure design that handles real-world traffic patterns.

We'll walk through how each component works, why it matters, and how Together approaches the technical challenges that most teams hit in production.

When a user asks an AI assistant to analyze a 50-page document, answers that take seconds aren't fast enough. This expectation is reshaping infrastructure requirements across the AI industry. The competitive environment and pace of innovation in AI-native products has fundamentally changed what users consider acceptable — and what businesses must deliver to remain competitive.

This shift isn't just about user experience — it's economics. Inference costs account for the majority of operational expenses in AI-native applications achieving product-market fit and starting to scale. Higher throughput means serving more requests per GPU. Faster token generation means shorter end-to-end response times, which means handling more concurrent users on the same infrastructure. For companies running AI at scale, optimizing time to first token (TTFT) and throughput measured in tokens per second (TPS) can be the difference between sustainable unit economics and burning capital on excess hardware.

Speed is a competitive moat. Faster responses improve retention, enable new use cases, and reduce cost per request. The companies delivering the fastest inference aren't optimizing one layer of the stack — they're rethinking how models, runtimes, and hardware work together. Off-the-shelf inference frameworks leave substantial performance on the table, and closing that gap requires either deep expertise across the full stack — or partnering with platforms that have already invested in it.

## Understanding inference economics for AI-native apps

When you're AI native, inference isn't a line item, it's the foundation of your P&L. Unlike traditional SaaS that enjoys near-zero marginal costs, AI applications often face per-request costs that scale with usage. A typical SaaS company targets 80% gross margins;an AI-native product might operate closer to 40-60%.

**The compound effect of model orchestration destroys margins faster than most teams anticipate.** For example, a coding assistant might trigger many model calls for a single user request: understanding intent, searching documentation, generating code, checking syntax, writing tests, explaining the solution. The features users love most — deeper reasoning, more thorough analysis, cross-referencing multiple sources — are precisely the ones that burn through margins.

The path to profitability requires fundamental improvements in inference efficiency, not just user growth. Every percentage point of optimization directly impacts your bottom line. The technical strategies we'll explore aren't academic exercises. They're the difference between products that scale and products that don't.

## Balancing speed and economics in AI inference

Running AI in production means delivering on two fronts: Customer expectations and business fundamentals. These requirements aren't in tension, they're interconnected. Meeting one without the other leads to products users love but can't afford to scale, or efficient systems no one wants to use.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87caff6_690a38f978bfbc690720a0ac_20251028_dual_mandate.png)

#### Meeting customer expectations

User experience thresholds are well-documented and unforgiving. [Research](https://portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm) on eCommerce and lead generation sites shows that a site loading in one second has a conversion rate 3-5x higher than one loading in five seconds. For AI applications where users expect real-time interaction, the tolerance is even lower.

The "streaming illusion" matters: users perceive responsiveness through both **TTFT** and **sustained throughput (TPS)**. A model that begins streaming within 50 ms and completes in two seconds feels faster than one that pauses 500 ms before outputting tokens, even if their total completion times are identical.

**Balancing TTFT and TPS requires understanding your specific use case.** Chat applications prioritize TTFT— users need immediate feedback that the system is working. A 50ms TTFT with moderate TPS beats a 500ms TTFT with blazing-fast generation. Code completion tools might accept higher TTFT if the TPS delivers complete suggestions quickly. Document summarization can tolerate seconds of TTFT if the final output arrives fast enough for the workflow.

Your concurrency and volume patterns dictate optimization priorities. High-concurrency, low-volume scenarios (customer support during peak hours) need aggressive batching and TTFT optimization. Low-concurrency, high-volume workloads (overnight document processing) can trade TTFT for maximum throughput. Only after understanding these tradeoffs can you select infrastructure and design optimizations to meet your SLAs.

For interactive applications — code completion, real-time customer support, conversational agents — the bar is <500ms response times. Agentic workflows compound these requirements. A single user query might trigger five model calls in sequence, turning a 200ms per-call latency into a full second of wait time. When each interaction feels slow, the entire experience degrades.

The implication is clear: latency isn't a nice-to-have metric. It's a product requirement that defines what's possible to build.

#### Improving price-performance

At scale, teams graduate from per-token pricing to managed infrastructure, where speed directly determines cost. When you're paying for GPU-hours, not tokens, the math is simple: faster inference means more requests per GPU-hour. Run inference 2x faster, and you've effectively halved your infrastructure costs. This relationship holds whether you're building on third-party APIs or running your own infrastructure.

The business impact scales with usage. Doubling your user base without doubling inference spend is the difference between linear cost growth and exponential opportunity. For API providers, margin expansion comes from serving more requests per GPU. For AI-native SaaS companies, it's about keeping unit economics favorable as the product scales. A 50ms reduction in latency across millions of daily requests translates to fewer GPUs needed, lower cloud bills, and better capital efficiency.

In a world where the latest generation of GPUs are supply-constrained and expensive, squeezing more throughput from each chip isn't just an optimization, it's a business necessity. Doing more with existing infrastructure delays the need for additional hardware purchases or cloud commitments. Every percentage point of efficiency improvement directly impacts your bottom line.

### The four pillars of inference acceleration

Optimizing inference isn't a single problem with a single solution. It's a stack of complementary strategies, each targeting different bottlenecks in the end-to-end pipeline. The companies winning at inference today aren't picking one approach, they're combining all four to create compound performance gains.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87caff0_690e6967afea4eb2e6cda675_20251028_four_pillars_of_modern_inference_performance2.png)

**Speculative decoding** transforms how models generate text. Instead of producing one token at a time, smaller draft models propose multiple tokens the target model verifies in parallel. When successful, this approach can double or triple generation speed without changing model outputs. It's particularly powerful for [longer responses](https://www.together.ai/blog/speculative-decoding-for-high-throughput-long-context-inference) where the overhead of drafting pays off quickly.

**Optimized kernels** squeeze more performance from every GPU cycle. Custom CUDA kernels, operator fusion, and flash attention variants reduce memory movement and computational overhead. These low-level optimizations often deliver 20-40% speedups by eliminating inefficiencies in how operations execute on hardware.

**Near-lossless compression** shrinks models without sacrificing accuracy. Techniques like 8-bit and 4-bit quantization reduce memory footprint and bandwidth requirements, allowing larger models to fit on smaller hardware and process requests faster. When DeepSeek R1 introduced MLA (Multi-Head Latent Attention), it demonstrated that architectural choices and quantization strategies work together to maintain quality while improving throughput.

**Hardware acceleration** leverages next-generation GPUs designed specifically for inference workloads. NVIDIA's Blackwell GPUs, with higher memory bandwidth and tensor core improvements, deliver substantial gains over previous generation Hopper GPUs. But hardware alone isn't enough. Systems must orchestrate workloads intelligently to extract maximum value from each chip.

No single pillar solves everything. Compression makes models smaller and faster, but only if optimized kernels can take advantage of reduced precision. Speculative decoding accelerates generation, provided the system is optimized to run both models efficiently on the same hardware. The sections that follow break down each pillar in detail: what it solves, how it works in production, and why it matters for building competitive AI products.

## 1. Speculative decoding

Speculative decoding addresses a fundamental bottleneck in language model generation. Normally, models generate text sequentially. Each token depends on all the tokens before it, which prevents true parallelism. For large models, most of the latency comes not from computation but from repeatedly moving weights in and out of GPU memory. The model spends more time loading data than thinking.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87cafed_690a397b7c8654e930c089d7_20251028_Speculative_Decoding.png)

Speculative decoding breaks this pattern by introducing a lightweight draft model that runs ahead of the target model. The draft generates several candidate tokens quickly, and the larger target model verifies them in parallel with a single forward pass. Tokens that match are accepted. Everything after the first mismatch is discarded and regenerated.

The result is faster generation without changing the output distribution. The target model still makes every final decision and the draft model simply proposes likely continuations.

### When speculative decoding delivers

The technique shines when the draft model can accurately predict the target's behavior. High-predictability workloads like code completion, structured JSON generation, or templated outputs often achieve 60–80% acceptance rates, translating to 1.5–3x speedups in practice.

The main trade-off is memory. Running two models simultaneously increases GPU utilization and can reduce batch size capacity. That's acceptable for latency-critical single-request workloads, but less efficient for large-batch, high-throughput serving.

Speculative decoding isn't a universal accelerator. But when applied to the right workloads, it transforms sequential generation into near-parallel verification, unlocking substantial performance gains without altering model quality.

### Out-of-the-box acceleration

We ship pre-trained draft models optimized for the most widely used base models in production. These speculators integrate directly into existing inference stacks without requiring custom training or tuning. For DeepSeek-R1, our Turbo Speculator delivers [measurable speedups](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200) right out of the box.

The design prioritizes two qualities: Speed and alignment. Speed comes from using smaller, computationally efficient architectures that minimize overhead. Alignment means generating predictions that closely match the target model's outputs, measured by acceptance rate. The higher the acceptance rate, the more tokens verified per forward pass, and the faster overall generation becomes.

#### How Turbo Speculator works

Model pairing matters. For a 70B target model, a well-tuned 7B drafter can predict likely continuations without introducing significant latency. The key is maintaining high acceptance rates as the speculation lookahead increases. Lookahead refers to how many tokens the draft model generates before the target model verifies them — higher lookahead means more potential speedup, but only if the draft model remains aligned with the target.

Most open-source speculators struggle here. DeepSeek-R1's own 14B Multi-Token Prediction (MTP) module shows strong performance at low lookahead values, but acceptance rates degrade quickly as lookahead increases. This limits the practical speedup in production workloads where higher lookahead is needed to offset verification overhead.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87cb008_690a39c27db14c38a4c7ee2e_R1-0528%2520Decoding%2520Speed%2520with%2520Speculators_%2520Together%2520Turbo%2520Speculator%2520vs.%2520MTP%2520Speculator2.png)

Turbo Speculator solves this by maintaining high acceptance rates even at large lookaheads. The result is consistently faster generation across a wider range of speculation depths. We achieve this through a combination of architecture optimizations, dataset curation, and training techniques developed specifically for speculative decoding.

#### When to use pre-built vs. custom speculators

Pre-built speculators like Turbo work well for general-purpose tasks where the target model's behavior is relatively predictable. Code generation, structured outputs, and reasoning tasks all benefit immediately. For highly specialized domains or fine-tuned models, custom speculators trained on domain-specific data can push acceptance rates even higher.

The trade-off is development time. Training a custom speculator requires high-quality paired data and careful alignment tuning. For most applications, the pre-built option delivers strong performance without the overhead. When acceptance rates justify the investment, custom speculators become worth building.

### Custom speculators: domain-specific acceleration

Pre-built speculators deliver strong baseline performance, but custom speculators trained on domain-specific data unlock significantly higher speedups. By fine-tuning a draft model on actual production traffic, we can push acceptance rates higher and reduce latency even further.

In this example, we deployed custom speculators for three real-world DeepSeek-R1 workloads: document extraction, a social media chat assistant, and résumé screening. These are cost- and latency-sensitive applications where every millisecond matters. Our Base Speculator already achieves 1.44–2.27x speedups over standard next-token prediction. Custom speculators trained on workload-specific data push that further, reaching 1.23–1.45x over the Base Speculator and 1.85–2.97x overall speedups. In absolute terms, that translates to 100–170 tokens per second in production on NVIDIA H100 GPUs.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87caff9_690a3c48f30bcb8ccf789fed_DSR1%2520across%2520workloads.png)

The training process is straightforward. We collect representative prompts and outputs from customer traffic, then fine-tune the Base Speculator using a proprietary pipeline optimized for target-aware alignment. With as few as 10,000 prompt-response pairs (roughly 20M tokens), we see measurable gains. At 50M tokens, speedups exceed 1.20x over the Base Speculator. As customers continue using our API, this dataset grows organically, and so does speculator performance.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87caff3_690a3fe0045259b10e8187c5_Scaling%2520behavior%2520of%2520custom%2520speculators.png)

#### Throughput and cost benefits

Custom speculators don't just reduce latency. They also increase GPU throughput, which lowers overall inference costs. For enterprise customers processing millions of requests per day, this matters. By using custom speculators, we reduce the GPU hours needed to generate 1 billion tokens by 23–26% compared to the Base Speculator, and 49–61% compared to no speculative decoding at all. Fewer GPUs means lower costs without sacrificing quality.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87caffd_690a4278fc9574ba52d35229_GPU-Hours-Across-Workloads.png)

*Speedup factors attained by Together’s Custom Speculators, fine-tuned for three different R1 customer use cases at the low latency regime, as a function of millions of customer training tokens. All Custom Speculators are trained from Together’s Base Speculators. 20M tokens is approximately 10K prompt-response pairs at 2048 sequence length.*

#### When custom speculators make sense

The investment pays off when you have consistent, high-volume traffic in a specific domain. If your application generates structured outputs, follows predictable templates, or operates in a narrow task space, a custom speculator will outperform a general-purpose draft model. The key is having enough representative data to capture the target model's behavior in your specific use case.

#### The limitation of static speculators

Custom speculators capture a snapshot of your workload at training time. They excel at the traffic patterns they were trained on, but as workloads evolve, performance can degrade. Your codebase grows. Traffic patterns shift, request distributions change, and even highly customized speculators can fall behind without retraining.

Standard speculators are trained for general workloads. Custom speculators are trained on your specific data, but only for a specific snapshot in time. Both approaches share the same fundamental constraint: once deployed, the speculator cannot adapt. This problem is particularly pronounced in serverless, multi-tenant environments where input diversity is extreme. New users continuously arrive, bringing unique workloads the fixed speculator may not have seen during training. Furthermore, these speculators typically use a fixed lookahead, predicting the same number of tokens regardless of the speculator's confidence. A static speculator simply cannot keep up.

### Adaptive speculators: Real-time learning at scale

We built [ATLAS (AdapTive-LeArning Speculator System)](https://www.together.ai/blog/adaptive-learning-speculator-system-atlas) to solve this. It's the first speculator system that dynamically improves at runtime, evolving automatically with usage and learning from both historical patterns and live traffic to continuously align with the target model's behavior in real time. The more you use our inference service, the better ATLAS performs.

Built on top of Together Turbo Speculator, ATLAS reaches up to 500 tokens per second on DeepSeek-V3.1 and up to 460 tokens per second on Kimi-K2 in fully adapted scenarios. That's 2.65x faster than standard decoding — outperforming even specialized hardware like Groq.

![Two bar charts showing ATLAS outperforming no and turbo speculators in speed (Tok/Sec) across batch sizes 1, 4, and 8.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87cb000_690a43b65306818b3fbba24d_Self-Adaptive%2520Spec%2520-%2520DS%2520V3.1%2520and%2520Kimi-k2-3.png)

#### The architecture: Two speculators, one controller

ATLAS combines three components working in concert. At the core is a **heavyweight static speculator** trained on a broad corpus that provides strong, general speculation. This serves as an always-on speed floor. It's trained on diverse data and remains stable across workloads, so throughput doesn't collapse when traffic shifts or the adaptive path is cold. If confidence drops or drift is detected, the system can fall back to the static speculator to preserve latency while the adaptive speculator relearns.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af9f1c356f7f87cb003_690a43cd21e4809bd475a85e_Adaptive-Learning%2520Speculator%2520System%2520Design-2.png)

The second component is a **lightweight adaptive speculator** that allows for rapid, low-overhead updates from real-time traffic. This speculator specializes on the fly to emerging domains. During a vibe-coding session, for example, the adaptive system can tune itself to the specific code files being edited, even if those files were never seen during training. This kind of on-the-fly specialization is impossible with static speculators. The adaptive speculator learns continuously from production traffic, adjusting to new patterns without waiting for manual retraining cycles.

The third component is a **confidence-aware controller** that chooses which speculator to trust at each step and determines what speculation lookahead to use. When the speculator has high confidence, the controller uses longer speculations to maximize speedup. When confidence drops, it shortens lookahead or routes back to the static path. This dynamic adjustment means the system operates at the optimal point of the speed-accuracy trade-off in real time, adapting to the difficulty of each individual request.

#### Why adaptive matters in production

Static speculators work well for predictable workloads. Custom speculators work even better when you have consistent traffic in a specific domain. But the most demanding AI-native applications operate at massive scale with dynamic user behavior and rapidly evolving workloads. A fintech platform processing millions of transactions shifts between fraud detection, risk analysis, and customer support throughout the day. A developer tool sees traffic patterns change as codebases grow and new features ship. Even within a single application, user intent varies dramatically from request to request.

ATLAS turns inference into a feedback loop. Every request improves the system. Traffic patterns shift? The adaptive speculator adjusts automatically. A user starts working in a new domain? The system specializes in real time. Code repositories grow and evolve? The speculator tracks those changes without manual intervention.

#### Customized speculators vs. adaptive learning

We know from our work with custom speculators that training on samples from real traffic delivers meaningful speed boosts. ATLAS enables us to be even more customized, but without the latency of batch retraining. The adaptive system can specialize a lightweight speculator for the exact context it's operating in right now, not the context it saw during training weeks ago.

This creates a compounding advantage for customers using dedicated inference products. Static speculators require periodic retraining to stay current. Custom speculators need new training cycles as workloads evolve. Adaptive speculators stay current by design, improving continuously as you use them. The system captures emerging patterns in real time and adjusts drafting behavior accordingly, maintaining high acceptance rates even as traffic distributions shift.

For high-volume customers, this translates directly to cost savings. Better acceptance rates mean fewer verification steps, which means higher throughput per GPU. As the adaptive speculator learns your specific patterns, you get faster inference and lower costs without lifting a finger.

## 2. Optimized kernels

GPUs are fast, but stock operations often leave significant performance on the table. The real constraint in transformer inference isn't compute. It's memory bandwidth. Most operations don't generate enough work to saturate the GPU's computational units, especially during autoregressive decoding where batch sizes are small and arithmetic intensity is low. The hardware spends more time moving data than performing calculations.

This is where optimized kernels matter. By improving memory access patterns, fusing operations to eliminate intermediate writes, and reducing kernel launch overhead, custom kernels can deliver 2–5x improvements over stock implementations. For LLM inference, where every token is generated one at a time in a memory-bound regime, these optimizations translate directly to faster generation and lower costs.

**Why inference engines live or die by kernel quality**

Open-source inference engines like vLLM, TensorRT-LLM, and SGLang have democratized production LLM serving. But under the hood, they all rely on the same fundamental operations: matrix multiplies, attention, layer norms, and activations. The difference between a fast engine and a slow one comes down to kernel implementation.

Most engines ship with reasonable defaults. NVIDIA's cuBLAS and cuDNN provide a solid baseline, and frameworks like FlashAttention have become table stakes. But reaching the performance ceiling requires going deeper. Custom kernels that exploit the specific memory hierarchy of the target GPU, minimize instruction latency, and eliminate unnecessary data movement can unlock 2–3x on top of standard libraries.

The challenge is that writing high-performance kernels is hard. NVIDIA's B200 delivers up to 4.5 PFLOPS of INT8 tensor compute, but reaching that peak requires a deep understanding of Blackwell's memory hierarchy, tensor layouts, and instruction scheduling nuances. The tensor cores need to stay fed, which means managing shared memory bandwidth, avoiding bank conflicts, minimizing address generation costs, and using asynchronous instructions like WGMMA and TMA. Most teams don't have the expertise or time to optimize at this level.

**We take kernels seriously**

Our [inference engine](https://www.together.ai/blog/together-inference-engine-2) is built on the principle that kernel quality is not negotiable. We maintain a library of hand-tuned CUDA kernels for every critical operation in the inference pipeline. Each kernel is profiled, benchmarked, and iterated on until it saturates the hardware. When NVIDIA releases new architecture features, we rewrite from scratch to take full advantage.

This matters because the gap between a good kernel and a great one compounds across millions of requests. A 20% improvement in attention throughput translates directly to 20% lower latency or 20% higher request capacity. Over the course of a day, that's the difference between needing 100 GPUs or 120.

We don't just optimize for synthetic benchmarks. Our kernels are battle-tested in production, handling real workloads with variable sequence lengths, diverse batch compositions, and mixed precision requirements. The result is an engine that consistently delivers near-theoretical peak performance, even under conditions where other systems degrade.

### Thunder Kittens: Open-source kernel optimization

We built Thunder Kittens to make kernel optimization more accessible. It's an embedded DSL within CUDA that provides high-level abstractions for the operations that matter most in AI workloads: matrix multiplies, reductions, and reshapes. Instead of wrestling with WGMMA layouts or TMA descriptors, you work with register tiles and shared tiles that handle the complexity automatically.

Thunder Kittens enforces a tile-based programming model. A "register" isn't a 32-bit word like on old CPUs. It's a 16x16 tile of data, which maps naturally to how modern GPUs actually want to work. The abstraction is simple and constrained, but that constraint matches the hardware. Small matrix multiplies under 16x16 aren't well-supported anyway, and most AI workloads operate on larger tiles.

The library includes optimized implementations of FlashAttention, quantization-aware kernels, and fused operations that reduce memory I/O. With Thunder Kittens, FlashAttention-3 matches cuDNN on B200 GPUs with only 200 lines of code (nearly a 95% reduction vs the full FlashAttention-3 kernel). A Based linear attention kernel hits 215 TFLOPs, or over 300 TFLOPs when accounting for recompute inherent in the algorithm. [Qwen3-Next](https://www.together.ai/models/qwen3-next-80b-a3b-thinking), for example, is a hybrid model that uses linear attention. These aren't experimental research kernels. They're production-grade implementations that run at 75%+ hardware utilization.

Thunder Kittens is open source. The code is available, documented, and designed for researchers and engineers who want to experiment with new architectures or optimize specific operations. If the library is missing something, you can extend it. The abstractions fail gracefully because it's embedded in CUDA, not a separate compiler stack.

### Together Kernel Collection: Drop-in performance

For production deployments, we offer the Together Kernel Collection (TKC): highly optimized kernels packaged as native PyTorch-compatible operations that our team can drop directly into the Together inference engine. These are the same kernels that power our platform. They're not experimental. They're enterprise-grade implementations that have been extensively tested and validated across different hardware configurations and workloads.

TKC delivers substantial speedups, particularly in scenarios where PyTorch's standard implementations struggle. FP8 inference operations run roughly 75% faster than standard PyTorch paths. For LLM inference, where skinny-matrix, memory-bound workloads dominate, this matters enormously. Modern LLM decoding processes one token at a time with batch size of one. Arithmetic intensity is low. Memory bandwidth is critical. Kernel launch overhead and synchronization costs become significant.

TKC's kernels are optimized specifically for these challenging conditions. Better memory access patterns maximize bandwidth utilization. Fused operations eliminate intermediate memory writes. Reduced kernel launches through intelligent operation batching cut overhead. FP8 support doubles effective memory bandwidth compared to FP16, which tran
