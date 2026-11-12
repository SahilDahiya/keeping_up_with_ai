---
title: Cost-efficient, high-performance TTS with Qwen3-TTS
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/cost-efficient-high-performance-qwen3-tts
author: Ian Carrasco
published: '2026-05-14'
fetched: '2026-11-12T06:07:32Z'
classifier: null
taxonomy_rev: 2
words: 1616
content_sha256: b5395e626f0278c34bbf7f04af53bb105efc10faf613d8693d42b55f9a02ee98
---

# Cost-efficient, high-performance TTS with Qwen3-TTS

Model performance
# Cost-efficient, high-performance TTS with Qwen3-TTS

We optimized Qwen3-TTS to $3 per 1M characters. 90% lower-cost than closed-source alternatives, with high fidelity for voice agents and voice cloning.


- Authors
- Date
- May 14, 2026

Voice is quickly becoming a dominant interface for interacting with LLM systems. Having both high-performance and expressive text-to-speech capabilities can unlock new product experiences, such as voice agents, dictation, and content generation, to name a few.

To serve our customers’ generative voice workloads with high performance and cost-efficiency, we’ve been optimizing single-replica performance of the Qwen3-TTS family of models with vLLM-Omni. As a result, we achieve significant cost efficiency (about $3-$4 per million characters) while maintaining high voice fidelity.

We’ve been deploying Qwen3-TTS for use cases across voice agents, language learning, and enterprise call infrastructure domains, and have received overwhelmingly positive feedback across the board for both voice quality and speed. In this post, we’ll go over some of the optimizations we use to enable cost-efficient, high-performance TTS in production — about 90% lower-cost than comparable closed-source models (based on a $3 per 1M token estimate).

You can try our optimized Qwen3-TTS model today from our [model library](https://www.baseten.co/library/qwen3-tts-12hz-base-streaming-1-7b/), or [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers about customizing Qwen3-TTS for your workload. As part of our work improving voice AI performance with vLLM-Omni, we’ve also been [shipping updates back to the OSS community](https://github.com/vllm-project/vllm-omni/issues/2603); more details on that, plus how to optimize Qwen3-TTS for voice cloning specifically, are coming in a future blog post!

Most commonly, managed TTS APIs charge based on the number of characters (per 1K or 1M characters) passed to the model. This rate includes a combination of serving costs (including GPU usage) and the concurrency at which the model can process multiple requests to amortize those costs.

With closed-source providers, the precise formula is opaque. The only ways to bring costs down are to hope that the provider lowers their prices, or to switch models or providers entirely. With open-source, dedicated TTS offerings, this calculation is much clearer: you pay for GPU usage directly. At the same time, any optimizations that push more concurrency on the same GPUs will directly reduce the price per 1K/1M characters.

To derive the cost per 1M tokens for open-source TTS models, we first ran benchmarks across a corpus of mixed-length prompts (20–500 chars, spanning short utterances, IVR-style scripts, informational blurbs, and paragraph-length narration). The table below shows how our chars/sec process changes with increasing concurrency.

As we push throughput on a single replica, we can amortize its cost across more streams, lowering the price per million characters.

P = $6.50 (H100 usage per hour list price)

T = Throughput (chars/sec)

M = (1,000,000 \* P) / (3600 \* T) 

(We divide by 3,600 to convert the hourly list price to per-second cost.)

With P = 1 H100 replica and T = 594 characters/second @ 25 concurrent streams, M ≈ $3.04/1M chars ($0.00304 per 1K chars).

And the full benchmarks:

| Concurrent streams | Chars/sec (T) | RTF p50/p90 | TTFA p50/p90 (ms) | Price/1M characters | 
|---|---|---|---|---|
| 1 | 110 | 0.172 / 0.182 | 57 / 60 | $16.41 | 
| 8 | 325 | 0.446 / 0.478 | 142 / 167 | $5.56 | 
| 16 | 493 | 0.581 / 0.643 | 193 / 238 | $3.66 | 
| 25 | 594 | 0.752 / 0.834 | 271 / 431 | $3.04 | 
| 32 | 511 | 1.118 / 1.690 | 678 / 950 | $3.53 | 

To hit these aggressive cost, latency, and throughput numbers, we used vLLM-Omni for serving and focused on squeezing maximum performance out of a single replica. Below are the key aspects of the serving stack that made it possible.

Qwen3-TTS and similar transformer-based TTS models often have two distinct compute stages: an autoregressive (AR) Talker that generates acoustic tokens (analogous to standard LLM token generation), and a neural audio codec decoder that converts those generated tokens into audio that can be streamed back to a client.

Out of the box, these stages run serially within a single request. The AR step generates the complete sequence of acoustic tokens before vLLM’s `Code2Wav` begins decoding them into audio. Since both stages share the same engine context, the decoder sits idle during token generation, and the AR stage sits idle during decode, preventing subsequent requests from being processed until the in-flight request has fully cleared the pipeline.

vLLM-Omni's disaggregated stage execution runs each stage as an independent engine with its own scheduler, connected through a stage-to-stage connector that handles intermediate data transfer. This unlocks pipelining across requests: `Code2Wav` can decode request A's tokens while the Talker is already generating tokens for request B. Each stage also independently batches its in-flight work so that multiple requests can be processed in parallel within a single forward pass at either stage.

For most workloads, this is the single most important architectural lever for supporting concurrent requests in a single-replica setup.

The Talker (AR) stage is derived from the Qwen3 LLM backbone. This means we can leverage common techniques for improving TPS on transformer-based LLMs — particularly, CUDA graph optimization.

To leverage CUDA graphs, we first profiled the model across various concurrency settings in an offline manner to identify common tensor shapes at key points in the forward pass. These statistics then informed the graph sizes to capture at vLLM startup, minimizing the number of kernel launch sequences post-warmup while keeping graph memory overhead low. This significantly speeds up the model, especially on hot paths with many kernel launches during the forward pass.

Having a disaggregated setup has several advantages, as we outlined in the previous section. Still, it fundamentally introduces a new bottleneck: the need to serialize and transfer the results from the Talker stage to the decoder. At higher concurrency, we observed that GPU-to-CPU transfers and serialization accounted for an increasing share of the end-to-end generation time.

By default, vLLM uses a backend designed for multi-GPU communication via IPC, which inherently introduces a serialization boundary between processes, something that isn’t necessary when running on a single replica. By switching to vLLM’s `uniproc` executor, particularly for cloning use cases, we saw significant performance gains by skipping serialization entirely while staying within a single process. We shipped this change back to the vLLM OSS community [here.](https://github.com/vllm-project/vllm-omni/issues/2603)

One of the primary flows Qwen3-TTS helps unlock is zero-shot voice cloning. This involves uploading a reference audio recording of a speaker, processing it via a speaker embedding step, and then using that embedding to condition the subsequent speech generation.

We’ve seen that customers often have a subset of voices that are commonly reused, so repeating the above embedding process on a per-request basis can lead to increased time to first audio (TTFA) and reduced throughput. By using an in-memory LRU cache, frequently reused speaker embeddings can be retrieved instantly by speaker name, minimizing time to first audio for cloned voices. This can sometimes deliver comparable performance and quality to a fine-tuned voice without requiring additional fine-tuning.

With most modern TTS systems, there is a tradeoff between latency (time to first audio, TTFA) and throughput (RTF). One key lever to balancing the two is the number of audio frames accumulated before the first decode step.

By minimizing this number, audio chunks are sent at much more frequent intervals but do not leverage dynamic batching at the decoder level. This means audio starts streaming sooner, but the decoder has limited context, which can hurt prosody.

On the other end of the spectrum is increasing the frame accumulation, which gives the decoder richer context but means we’ll wait longer to accumulate more frames before its first audio generation. This has more preferable batching mechanics, as there is a larger window for multiple requests to be included in the same batched decode call. The result is improving throughput at the cost of higher TTFA.

To reap the benefits of low TTFA but high concurrency, the frame accumulation count must be dynamic. We use a low initial frame count to minimize time to first audio, and ramp it up for subsequent chunks that can afford higher latency bounds to improve utilization of in-flight requests.

For voice agent use cases, knowing what has actually been spoken before an interruption is critical to a natural conversation. This typically requires word- or character-level timestamps on the generated audio so the interruption point can be mapped back to the last spoken word.

To add this capability (which is usually only available in third-party offerings), we integrated the Qwen3 Forced Aligner as a post-processing step in the Qwen3-TTS forward pass, allowing timestamps to be emitted in both synchronous and asynchronous modes. This makes it a viable choice for E2E voice applications that need robust interruption handling.

With Qwen3-TTS, it’s possible to fine-tune new voices via supervised fine-tuning (SFT). This typically requires a larger set of reference audio examples upfront (\~1hr), but can achieve higher quality and voice resemblance while even slightly boosting performance by avoiding speaker embedding prefill.

Practically, this means a high-quality custom voice (e.g., a specific accent, character, brand voice) can be generated at open-source economics. You can run this on [Baseten’s Training platform](https://www.baseten.co/products/training/), and once fine-tuning is complete, the resulting checkpoint can be seamlessly hooked into the vLLM-Omni serving stack and immediately benefit from the optimizations described above (we have multiple customers fine-tuning and deploying Qwen3-TTS with exactly this workflow, and we'll be publishing the full fine-tuning recipe in our ml-cookbook shortly!).

Our optimized Qwen3-TTS model is available to self-serve today via our [model library](https://www.baseten.co/library/qwen3-tts-12hz-base-streaming-1-7b/), supporting streaming and voice cloning use cases. For more advanced or larger-scale use cases, [reach out](https://www.baseten.co/talk-to-us/) to talk to us!
