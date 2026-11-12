---
title: Delivering real-time text-to-speech with Gradium
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/delivering-fast-real-time-text-to-speech-with-gradium
author: Albert Lee
published: '2026-10-13'
fetched: '2026-11-12T06:08:52Z'
classifier: null
taxonomy_rev: 2
words: 1132
content_sha256: 2933056cf8104b3bbd32ab9d0dd0bc246565189d7f3f079043bb2dcc83e5a2c8
---

# Delivering real-time text-to-speech with Gradium

AI models
# Delivering real-time text-to-speech with Gradium

Achieve natural-sounding conversational experiences using Gradium TTS on Baseten.


- Authors
- Date
- October 13, 2026

TLDR

Gradium TTS is built for real-time voice agents, achieving TTFA faster than typical human response times through its Delayed Streams Modeling architecture and GPU optimizations, including kernel fusion and CUDA Graphs. It is available in Baseten's Model Library now as a dedicated deployment.

Gradium’s text-to-speech (TTS) model converts written text into spoken audio and is designed specifically for real-time AI voice agent interactions.

Time-to-First-Audio (TTFA) measures the duration between sending a TTS request and receiving the first playable audio. It is critical for natural-sounding conversations.

To deliver reliably natural conversations, Gradium TTS achieves a TTFA faster than human speech response times.

| Interaction rhythm | TTFA range | 
|---|---|
| Slower than human speech | 400+ ms | 
| At human speech | 200 ms - 400 ms | 
| Faster than human speech | \<200 ms | 

*Try the TTS Latency Race demo yourself and access its code repository here.*

Independent Coval benchmarks place Gradium TTS in the faster-than-human-speech tier, giving voice agents time to reason or retrieve context without breaking conversational flow. On the [Coval TTS benchmark](https://gradium.ai/content/tts-latency-benchmark-2026) (as of September 2026), Gradium TTS achieved a median TTFA of 214 ms with an interquartile range tight enough that developers can set reliable latency budgets across the rest of their pipeline.

Gradium TTS is streaming: it can start speaking before the upstream text generator, such as an LLM, has finished producing the full response. Specifically, Gradium's models use [Delayed Streams Modeling (DSM)](https://arxiv.org/pdf/2509.08753), a framework developed by Kyutai that treats text and audio as two parallel streams running on a shared clock, so audio can be generated before text has finished arriving.

Both streams align to the same frame rate, one step every 80 ms, so the model can generate audio as text arrives. The key idea of DSM is the audio stream runs a few steps behind the text, giving the model a glimpse of what comes next, similar to how a human speaker adjusts tone, inflection, and pacing based on the words they're about to say. A longer delay gives the model more context and better voice quality, while a shorter one lowers latency.

Audio output follows text by a tuned number of decoding steps, shown in the figure below.

Gradium TTS starts speaking after the first few tokens, not the full token generation. The model's design also keeps each 80 ms frame quick to generate, maintaining low latency once speech begins.

Each step in the audio stream is produced by two transformers with distinct roles:

- **Temporal transformer (the "reader"):** Moves through the streams one step at a time, taking in the newest text token and the previous audio frame. It produces one vector describing what the next frame of audio should sound like, and signals when it's ready for the next word, which keeps the speech naturally paced when text arrives unevenly.
- **Depth transformer (the "refiner"):** Turns that vector into an audio frame. Each frame is encoded as up to 32 tokens, arranged so the first captures the most important features and each later one adds finer detail. The refiner generates them in that order, so the frame becomes progressively more accurate with every token.

This split enables Gradium TTS's low TTFA. The larger temporal transformer, which has to track context, runs only once per step, while the smaller depth transformer runs up to 32 times per step but stays cheap because it never looks back in time. Those many small refiner passes also benefit from additional GPU optimization.

GPUs do the heavy computation for AI models, but they don't work alone. The CPU acts as the dispatcher, and for each computational step, it selects the right GPU kernel, prepares its inputs, and issues the command to launch it. Every one of those handoffs takes a small, fixed amount of time.

In large language models, the GPU is the bottleneck, and each GPU kernel runs long enough that the CPU can queue the next launch before the current one finishes. However, in smaller AI models like streaming TTS, GPU kernels complete faster than the CPU can queue them. As a result, the CPU becomes the latency bottleneck, leading to lower GPU utilization.

Gradium addresses this challenge in two ways:

- **Kernel Fusion**: Using `torch.compile` and Triton, Gradium merges operations that previously required several separate GPU kernel launches into a single kernel, so each launch does more work.
- **CUDA Graphs**: The full sequence of kernels for a forward step is recorded once. On every subsequent step, the CPU issues a single replay command and the GPU driver runs the entire recorded sequence back-to-back, rather than waiting for each kernel to be launched individually.

In [Gradium's published benchmarks](https://gradium.ai/blog/optimizing-quality-vs-latency), enabling CUDA Graphs cut median TTFA by more than 2.5x at small batch sizes.

Traffic to voice AI applications tends to be bursty. There is high demand at the start of business hours and during triggering events such as outages or marketing campaigns. Required concurrency can rise and fall in minutes, so provisioning for the peak leaves GPUs idle most of the day, while provisioning for the average degrades performance during the first minutes of every spike.

Autoscaling resolves this, but a new replica can't serve calls until its model weights are loaded into GPU memory. Weights are typically pulled from upstream sources such as Hugging Face or S3, where rate limits and cross-region latency stretch cold starts further, especially when many replicas request the same files at once.

The [Baseten Delivery Network (BDN)](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast) reduces cold start time in three ways:

- **Push-time mirroring:** At deploy time, BDN copies the model's weights into Baseten-managed storage and records a content-hashed manifest. Upstream is touched once; every cold start after that reads from Baseten's own storage.
- **Three-tier caching:** Each GPU node checks node-local NVMe disk first, then an in-cluster peer cache, then the mirrored origin, delivering weights to H100 nodes at over 2 GB/s.
- **Coordinated downloads:** During a burst, each chunk of the model is pulled from origin by one node and shared with peers over the in-cluster network, so origin bandwidth for a 50-replica scale-up is 1x the model size, not 50x.

Because weights arrive before the model container starts, the transfer also happens outside the billable GPU window. The result is 2–3x faster cold starts, so a Gradium TTS deployment on Baseten can follow sudden swings in call volume without customers waiting on a cold replica. Gradium makes each interaction fast, and Baseten makes that performance available as traffic rises and falls.

Gradium TTS is available as a [dedicated deployment on Baseten](https://www.baseten.co/library/gradium-tts/). Try it today and see these benefits on your own workload.
