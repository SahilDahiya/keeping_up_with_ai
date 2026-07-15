---
title: '2,000 robots walk into a shop: Simulated A/B testing (2026)'
kind: blog
topic: evals-observability
subtopic: testing
secondary_topics:
- agents/multi-agent
summary: 'SimGym: Shopify''s simulated A/B testing environment where thousands of
  LLM-driven shopper agents exercise storefronts, letting teams test changes against
  synthetic-but-realistic buyer behavior before real traffic.'
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/simgym
author: Javier Moreno
published: '2026-02-27'
fetched: '2026-07-15T00:53:34Z'
classifier: claude
taxonomy_rev: 2
words: 1808
content_sha256: f7b306fe59bfa8f59c69039ecf0c0cf5ee5e2904f76c3900e1c6978a263ef663
---

# 2,000 robots walk into a shop: Simulated A/B testing (2026)

I am sure you have seen the videos, they're quite something. Picture Black Friday morning at a popular store. Six a.m. Still a little dark. Crowds of people pushing through the doors at once, each with a different list, a different budget, different taste. Some know exactly what they want. Some are browsing. Some will leave if the line is too long. Often, chaos ensues.

Now imagine they are robots in the ether, each running in its own cloud browser, each with a persona and a shopping intent, and each one needing an LLM to guide them and decide what to do next. Click, scroll, add to cart, or leave.

## SimGym

A merchant changes their storefront. New theme, different layout. How do they know if it is better? Deploy it, A/B test it, wait days or weeks for statistical significance, pray to the gods you did not tank conversion. Small merchants have it worse: typically they don't have enough traffic for testing to converge at all.

[SimGym](https://apps.shopify.com/simgym?utm_source=w26-editions-website&utm_medium=product-cta&utm_campaign=winter26edition) changes this. We send hundreds of robots to browse the merchant's store in a contained environment. Each has a persona, a budget, and a shopping intent. Each runs in a cloud browser. No mocked DOM, no shortcuts. The robot sees the page, decides what to do, clicks, scrolls, adds to cart. A twin does the same on the alternate theme. A simulated A/B test in minutes instead of weeks, even for stores with zero real traffic.

Under the hood live two machines. [Browserbase](https://www.browserbase.com/) runs the cloud browsers: up to 2,000 concurrent Chromium sessions. Our inference cluster runs the model behind the robots. The loop is tight: Browserbase sends the page state, the model returns a JSON action, Browserbase executes it. Repeat 10-13 times. The model sees a one-sentence system prompt, a buyer profile, accumulated memory, and a representation tree of the current page (3,000 to 15,000 tokens depending on storefront complexity).

Browserbase bills per minute. The model needs seconds to think. That coupling is the central tension: inference latency is operational cost.

## The challenge

![Table](https://cdn.shopify.com/s/files/1/0779/4361/files/SimGym_The_challenge_table.png?v=1772207535)

94% of all tokens are input. Every millisecond the model spends reading is a millisecond the browser spends billing.

We measured this: a ~20% reduction in average LLM latency cut cost per merchant run by ~10% and increased daily throughput by ~12%.

## Our journey

First version: GPT-4o and other models through a standard API. It was slow and expensive. 75 out of 100 simulated buyers completed their task. Promising.

Then GPT-5 came in and behaved even better. But at hundreds of thousands of sessions per day per-token API costs were not sustainable.

The pivot: `gpt-oss-120b`, an open-source 120B MoE model, plus the [Notte browser](https://github.com/nottelabs/notte) automation framework. Session times dropped from 15+ minutes to under 3. And open source gave us predictable costs instead of per-token pricing. In addition, we could potentially train task-specific variants. The model was fast and more than enough for the task.

That commitment, self-hosting a mid-size MoE model at production scale, is what made everything that follows necessary.

Next problem: where to run it. [Groq](https://groq.com/)'s hosted API was fast but hit a ceiling at 5 million tokens per minute with 50 concurrent sessions. We needed more. Working with NVIDIA/CentML allowed us to remove rate limits but introduced 10x latency spikes at high concurrency. It was clear very soon that we needed dedicated custom infrastructure and subsequent optimization.

## Agentic inference

SimGym violates almost every assumption that standard LLM serving was designed for.

![Table](https://cdn.shopify.com/s/files/1/0779/4361/files/SimGym_Agentic_inference.png?v=1772207577)

A chatbot handles independent short requests arriving randomly. SimGym fires 600 correlated long-context requests at once. Each depends on the previous step. Each requires JSON schema enforcement. Each accumulates 89K-127K tokens over the session.

Then there is the model itself. `gpt-oss-120b` is a Mixture-of-Experts: only a fraction of its 120B parameters activates per token, so compute per token is comparable to a 15-20B dense model. But all 120B parameters must sit in GPU memory. The bottleneck is loading expert weights from HBM, not arithmetic. Memory-bound, not compute-bound. Standard [vLLM](https://github.com/vllm-project/vllm) was not efficient at this.

## The collaboration

CentML, acquired by NVIDIA eight months ago, was already Shopify's preferred inference platform. We have run similar inference optimization collaborations with them on Search, Shopify Catalog (Product Classification), Recommendation Systems, and Sidekick, each with its own constraints, latency requirements, and optimization objectives. SimGym was a different enough beast to need its own track: the application team, the inference platform, and the GPU kernel engineers worked together with profiling data and production traffic shapes.

### Enter Blackwell

The first task was getting `gpt-oss-120b` running on Blackwell. The model is memory-bound, so the biggest wins came from reducing how much data moves through HBM: **MXFP4 quantization** for expert weights, **FP8 attention** for the KV-cache, and optimized **FlashInfer kernels** for the attention and MoE operations themselves. The team tuned chunked prefill and request scheduling, and fixed bugs that only surface under production agentic load (vLLM [PR #28000](https://github.com/vllm-project/vllm/pull/28000)).

The baseline: 80K tokens per second on B200.

### Benchmarking paradise

Standard benchmarks do not capture agentic workloads. The NVIDIA team collected our production traffic shapes, prompt distributions, concurrency patterns, and token lengths, then replayed them against H100, H200, and B200 hardware.

**11K tokens/second per H200, versus 57K tokens/second per B200. A 5.2x speedup.** That made Blackwell a clear choice for SimGym.

### Custom design

This is where our workload shaped the engineering.

**Custom FlashInfer kernels for long-context speculative decoding on Blackwell.** The NVIDIA kernel team used profiling data from our workload to build optimized attention kernels for long context + speculative decoding + Blackwell. This went upstream as FlashInfer [PR #2265](https://github.com/flashinfer-ai/flashinfer/pull/2265), available in FlashInfer 0.6.1. Result: roughly 2x attention kernel speedup for speculative decoding at long context.

**The three-way integration: async scheduling + guided decoding + speculative decoding.** SimGym needs all three at once. Async scheduling for throughput. Guided decoding for JSON schema enforcement. Speculative decoding for latency. Making them work together without sacrificing individual gains was a significant challenge that led to vLLM contribution ([PR #29821](https://github.com/vllm-project/vllm/pull/29821)).

You may wonder: why does speculative decoding matter for agents? Standard decoding produces one token per forward pass. Speculative decoding uses a small draft model to propose multiple tokens, then verifies them in a single pass of the large model. This works well for SimGym because the output is structured JSON. Field names like `"action"`, `"nodeSelector"`, and `"method"` are highly predictable, so the draft model's acceptance rate is high. And since agent steps are strictly sequential, you cannot parallelize across steps. The only way to speed up a session is faster individual steps.

NVIDIA trained and published an **EAGLE-3 speculative decoding head** for this: [nvidia/gpt-oss-120b-Eagle3-throughput](https://huggingface.co/nvidia/gpt-oss-120b-Eagle3-throughput) on HuggingFace.

Runtime work already in production—async scheduling, stream interval buffering, torch.compile kernel fusion—contributed immediate gains. The vLLM and NVIDIA teams published full details in [a joint blog post](https://blog.vllm.ai/2026/02/01/gpt-oss-optimizations.html): 38% throughput increase and 13% latency improvement overall. Teams from Red Hat, NVIDIA, vLLM, and Meta were involved in this project.

Production results so far: 10% speedup from async scheduling (80K to 88K TPS per B200) and 57% reduction in HTTP/gRPC overhead from stream interval optimization. In benchmarks, speculative decoding added a further 6% at 100-200 concurrent sessions (33K to 35K TPS) and is next to go live. More is expected as FlashInfer kernels continue to improve.

### Today

Our current gear: 48 dedicated NVIDIA B200 GPUs on CentML. Fixed allocation, no autoscaling.

```
model: openai/gpt-oss-120b
replicas: 48
max_model_len: 131072      # 128K context
max_num_seqs: 2048          # max concurrent sequences
chunked_prefill_size: 32768 # 32K chunked prefill
cache_dtype: fp8            # FP8 KV-cache
gpu_mem_util: 0.92
# FlashInfer MXFP4/MXFP8 and TRT-LLM attention enabled
```
The serving stack: **vLLM** wrapped by CentML's `cserve` acceleration layer (with a custom build for `gpt-oss`), with **FlashInfer** providing optimized GPU kernels. Speculative decoding via the EAGLE-3 head is validated and queued for production deployment.

We also investigated **MIG (Multi-Instance GPU)** partitioning: splitting each B200 into two isolated instances. In end-to-end experiments at production QPS, MIG reduced average LLM latency by ~20% (27.8s to 21.9s), dropped session duration from 7.3 to 6.6 minutes, and increased daily throughput from 1,311 to 1,463 merchant runs. Near-linear scaling, no quality regression. MIG is a different optimization profile from speculative decoding: partitioning GPU memory means the draft model does not fit alongside the main model, and prefill-decode disaggregation does not apply. But the latency and throughput wins from doubling the number of serving instances are substantial on their own.

### Prompt optimizations

We restructured the system prompt to move dynamic elements (persona, intent) out of the shared prefix so prefix caching can hit more often. With caching enabled and caching-friendly prompts, NVIDIA's experiments showed ~12% throughput increase at concurrency above 1,000 and meaningful TTFT (time-to-first-token) improvements at all concurrency levels.

We also tried lowering the reasoning effort. Session duration dropped ~75%, but error rates jumped from 0.5-0.75% to 4.5-10.9% across trials. Not worth it.

## Next

The collaboration produced a deep bench of validated optimizations. The question now is sequencing.

**MIG partitioning** is nearest to production. Doubling serving instances gives us ~20% latency reduction and ~12% more daily throughput with no quality regression. A straightforward win for our current workload shape.

On full-GPU configurations, a different set of levers opens up. **Speculative decoding** with the EAGLE-3 head is validated and ready to deploy. **Disaggregated serving**—separating prefill and decode so they scale independently—is the next big architectural shift. When 94% of your tokens are input, you want more prefill capacity than decode capacity. Today they share the same GPUs. Alongside that, continued FlashInfer kernel improvements including RoPE+Q+Cache fusions.

On our side: **prefix caching** in production. **Smaller finetuned models** trained on our 16 H200 GPUs on Nebius. Qwen3-32B is already a candidate.

## Coda

Seven months ago SimGym was a dreamy and promising prototype making API calls. Today: a cluster of Blackwell GPUs, custom FlashInfer kernels, and a deep pipeline of optimizations let us spawn 400,000 shopping sessions a day. The cost per merchant run is in single digits and falling.

Long context, structured output, bursty correlated traffic, sequential dependency, per-minute billing pressure. None of this was in the standard playbook. Engineers from Shopify, NVIDIA/CentML, and vLLM worked with production profiling data to build an inference engine for it. And we are not done.

Meanwhile, somewhere far away, a merchant who has never had enough traffic for an A/B test just got results in four minutes. A crowd of robots back them up.

## One of us

Behind all this work there are people like you. People who hate to be trapped in small boxes. Who nerd-snip into GPU kernels some days, and then spend others setting up fine-tuning experiments at scale. Equally at ease running production systems and presenting work at top conferences. We do not care about credentials. We care about curiosity, courage, and taste.

If this got you excited, you should already be here. [Join us](https://www.shopify.com/careers).
