---
title: The fastest, lowest-cost batch transcription with Qwen3-ASR
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/fastest-lowest-cost-qwen3-asr-batch-transcription
author: Hasan Khan
published: '2026-11-01'
fetched: '2026-11-12T06:13:22Z'
classifier: null
taxonomy_rev: 2
words: 1417
content_sha256: aeeb702aea5d175e0b0c0089c696f2cc7fd9db03b52b7fa910b750ede956e3a3
---

# The fastest, lowest-cost batch transcription with Qwen3-ASR

Model performance
# The fastest, lowest-cost batch transcription with Qwen3-ASR

Transcribe an hour of audio with Qwen3-ASR for 1/10th of a cent, with 7x higher throughput, 6.9x lower latency, and no meaningful effect on quality.


- Authors
- Date
- November 1, 2026

TLDR

Qwen3-ASR 1.7B sits on the Pareto frontier of Hugging Face's Open ASR Leaderboard, but serving it efficiently for batch transcription requires careful optimization. We combined native audio decoding, KV cache quantization, and reduced unnecessary host-to-device syncs to serve 7x more audio per second at high concurrency on a single RTX PRO 6000. On hour-long files, we sustain over 3,000x real-time factor (RTF) at about 1/10th of a cent per audio hour, with no meaningful change in word error rate.

Speech-to-text splits into two very different workloads. On the one hand, real-time transcription is about latency: a voice agent needs words back within a few hundred milliseconds of someone speaking. On the other, batch transcription is about throughput: podcast networks, meeting-notes products, and call-center archives have hours of recorded audio and want it transcribed as cheaply as possible. That means getting as many hours of audio through each GPU as it can handle.

We optimized [Qwen3-ASR 1.7B on Baseten](https://www.baseten.co/library/qwen3-asr-1-7b/) to achieve the lowest cost per audio minute across all transcription providers. Compared with out-of-the-box vLLM, the optimized stack transcribes 7x more audio per second at high concurrency.

Qwen3-ASR 1.7B is the Qwen team's open-weight speech recognition model, released under an Apache 2.0 license. It supports more than 30 languages and 22 Chinese dialects, and it sits on the Pareto frontier of the [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) with a 5.4% average word error rate (WER).

Our real-time deployment of Qwen3-ASR 1.7B also has the highest quality (i.e., the lowest WER) and the lowest latency on [Coval's speech-to-text benchmark](https://www.baseten.co/blog/baseten-leads-covals-voice-ai-benchmark/), which includes leading transcription models across the market, open and closed.

Qwen3-ASR has been served for batch transcription on Baseten since the day it launched. Here’s how we made it faster than the vanilla implementation.

We started with vLLM's OpenAI-compatible transcriptions endpoint, which chunks audio into 30-second windows and batches them through the model. From there, we profiled every stage of a request under load, honing in on four things specifically:

1. Native audio decoding
2. KV cache quantization (without quality loss)
3. Host-to-device syncs
4. Request handling

Below are some of the key changes that made our 7x+ higher throughput possible.

Before any model work happens, the server must convert the uploaded M4A or MP3 file into 16 kHz mono samples.

By default, vLLM's audio loader uses [PyAV](https://pyav.org/docs/stable/) to decode audio one frame at a time in Python, resampling on the fly. Each frame step holds Python's global interpreter lock, so the decode threads are serialized rather than running in parallel. This creates a CPU bottleneck at high concurrency, while the GPU sits idle.

We replaced the loader with [torchcodec](https://github.com/meta-pytorch/torchcodec), which hands the whole file to FFmpeg in a single native call that decodes, resamples, and downmixes before returning a tensor. This asynchronous approach releases the interpreter lock while the codec processes the request, with identical output to PyAV.

For long files, we go one step further and decode and downmix files parallelized across time ranges. Each range is processed with a small overlap, ensuring they splice back together with bit-exact correctness. With these changes, we can preprocess an hour of audio in well under a second.

At high concurrency, attention over the KV cache is the largest share of GPU time. Decode attention is memory-bound: every step reads every cached key and value for every running sequence, and with 1,000 30-second windows in flight, that is the whole cache, every step.

Storing the KV cache in FP8 halves the bytes each step reads and doubles the number of sequences that fit in GPU memory. One challenge was that vLLM's default FlashAttention-2 backend does not support FP8 cache on RTX PRO 6000, motivating us to use FlashInfer kernels instead. FlashInfer FP8 improved memory utilization for the attention kernel from 50% to 80%.

We kept the weights in BF16 because weight quantization increased word error rate (WER) on our test sets. While the FP8 cache is also lossy, the effect on accuracy is minimal since the attention computation remains in full precision, and each layer recomputes its cache from full-precision activations.

Under load, GPU traces showed idling between steps even with the kernels near their hardware limits.

The gaps came from the CPU; normally, the CPU prepares the next step while the GPU is still working, but to do so, the attention backend needed each sequence’s length, which was stored on the GPU. Copying it back forced the CPU to wait until the GPU had finished. So the CPU couldn’t prepare the next step in advance, and the GPU sat idle while it did.

The audio encoder did the same once per layer, reading the maximum clip length back to size its attention mask. Each readback is a synchronization point: the CPU cannot enqueue the next kernels until it returns, so the GPU runs dry.

Because both values are known on the CPU before the step begins, we keep host-side copies and build the metadata and masks from those instead, eliminating idle time. GPU utilization under load went from 86% to 97%, and the engine went from CPU-bound to GPU-bound.

Alongside these changes, we also tuned how requests move through the server so that preprocessing keeps pace with the GPU at 64 concurrent requests.

Four API-server processes run ahead of the engine, so audio decoding and log-mel feature extraction for different requests proceed in parallel across processes instead of contending inside one.

With decode no longer serializing on the interpreter lock, we doubled the preprocessing thread pool in each process.

For all of the results reported below, "Vanilla vLLM" is Qwen3-ASR 1.7B on upstream vLLM with no changes, vs. our optimized implementation with the changes outlined above. Both run on a single RTX PRO 6000 with the same weights.

Audio seconds transcribed per second of wall time, tested at 64 concurrent requests, show up to a 7x throughput improvement on our optimized implementation vs. vLLM.

We weren’t able to test vanilla vLLM on audio clips beyond 10 minutes, because they don’t fit in one request.

| Clip length | Vanilla vLLM | Baseten-optimized | Gain | 
|---|---|---|---|
| 10 sec | 149x | 602x | 4.0x | 
| 30 sec | 346x | 1,358x | 3.9x | 
| 1 min | 358x | 1,861x | 5.2x | 
| 5 min | 380x | 2,645x | 7.0x | 
| 30 min | Not possible in a single request | 2,688x (16 concurrent) | N/A | 
| 1 hr | Not possible in a single request | 3,128x (16 concurrent) | N/A | 

The gain grows with clip length, from 4x on 10-second clips to 7x on 5-minute clips, and our stack continues climbing on 30-minute and 1-hour files that previously did not fit in a single request.

Like throughput, latency improvements also widen with load. For 5-minute clips, a single request went from 5.1 seconds to 1.5 seconds, and at 64 concurrent requests, the median fell from 50 seconds to 7.3 seconds.

Files that previously had to be split by the caller now return in a single request: 3.0 seconds for 30 minutes of audio, and 4.7 seconds for a full hour.

Throughput affects the price, since you can get more done with the same GPU minute (or second).

At Baseten's list price for a dedicated RTX PRO 6000 and the sustained throughput listed above, the optimized deployment transcribes an hour of audio for about 1/10th of a cent ($0.0013 per audio hour), 8x lower than the same model on vanilla vLLM at $0.011.

Our implementation also costs around 277x less than popular closed-weight providers, which range between $0.21-$0.36.

*Baseten cost is estimated by saturating one RTX PRO 6000 on hour-long files and using list pricing; closed provider pricing is estimated from published pay-as-you-go pricing for their current flagship batch models as of the last update date of this blog.*

This optimized Qwen3-ASR deployment is the default [in our Model Library](https://www.baseten.co/library/qwen3-asr-1-7b/). Deploy it in one click and call it with any OpenAI-compatible transcription client, or pair it with [Nemotron 3 Diarization](https://www.baseten.co/blog/nvidia-nemotron-3-diarization/) for speaker-attributed transcripts.

If you need live transcription instead, our [real-time Qwen3-ASR preset](https://www.baseten.co/library/qwen3-asr-1-7b-streaming/) serves the same model. For larger batch workloads or a specific model you would like us to optimize, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers!
