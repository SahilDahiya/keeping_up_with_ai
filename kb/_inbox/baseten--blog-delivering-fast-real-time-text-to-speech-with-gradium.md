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
url: https://www.baseten.co/blog/delivering-fast-real-time-text-to-speech-with-gradium/
author: Albert Lee
published: '2026-10-13'
fetched: '2026-10-14T06:09:53Z'
classifier: null
taxonomy_rev: 2
words: 1456
content_sha256: fbc8b4fee564dd6a69d9e03467533d83183bd09badf59d8d47c898c0533b68b6
---

# Delivering real-time text-to-speech with Gradium

### Published

![Delivering real-time text-to-speech with Gradium](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791912355-gradium-tts-model-release-2.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Gradium TTS is built for real-time voice agents, achieving TTFA faster than typical human response times through its Delayed Streams Modeling architecture and GPU optimizations, including kernel fusion and CUDA Graphs. It is available in [Baseten's Model Library](https://www.baseten.co/library/gradium-tts/) now as a dedicated deployment.

## Gradium TTS: TTFA faster than human speech

Gradium’s text-to-speech (TTS) model converts written text into spoken audio and is designed specifically for real-time AI voice agent interactions.

Time-to-First-Audio (TTFA) measures the duration between sending a TTS request and receiving the first playable audio. It is critical for natural-sounding conversations.

To deliver reliably natural conversations, Gradium TTS achieves a TTFA faster than human speech response times.

### **Gradium latency race demo**

![Gradium delivers low TTFA for natural conversational experiences.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2FiBSjR67BCDvMifRtwc01TBy1I0202uGHfY01%2Fthumbnail.jpg&w=3840&q=75)

*Try the TTS Latency Race demo yourself and access its code repository here.*

Independent Coval benchmarks place Gradium TTS in the faster-than-human-speech tier, giving voice agents time to reason or retrieve context without breaking conversational flow. On the [Coval TTS benchmark](https://gradium.ai/content/tts-latency-benchmark-2026) (as of September 2026), Gradium TTS achieved a median TTFA of 214 ms with an interquartile range tight enough that developers can set reliable latency budgets across the rest of their pipeline.

## Gradium's TTS doesn't wait for the full sentence

Gradium TTS is streaming: it can start speaking before the upstream text generator, such as an LLM, has finished producing the full response. Specifically, Gradium's models use [Delayed Streams Modeling (DSM)](https://arxiv.org/pdf/2509.08753), a framework developed by Kyutai that treats text and audio as two parallel streams running on a shared clock, so audio can be generated before text has finished arriving.

Both streams align to the same frame rate, one step every 80 ms, so the model can generate audio as text arrives. The key idea of DSM is the audio stream runs a few steps behind the text, giving the model a glimpse of what comes next, similar to how a human speaker adjusts tone, inflection, and pacing based on the words they're about to say. A longer delay gives the model more context and better voice quality, while a shorter one lowers latency.

**Audio output follows text by a tuned number of decoding steps**

![Delayed Streams Modeling aligns text and audio to a shared 80 ms clock and runs the audio stream a fixed number of steps behind the text, so each audio frame is generated with the next few words already in view.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791571172-gradium-delayed-streams-restyled.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Delayed Streams Modeling aligns text and audio to a shared 80 ms clock and runs the audio stream a fixed number of steps behind the text, so each audio frame is generated with the next few words already in view.

Gradium TTS starts speaking after the first few tokens, not the full token generation. The model's design also keeps each 80 ms frame quick to generate, maintaining low latency once speech begins.

## How each 80 ms audio frame gets built

Each step in the audio stream is produced by two transformers with distinct roles:

- **Temporal transformer (the "reader"):** Moves through the streams one step at a time, taking in the newest text token and the previous audio frame. It produces one vector describing what the next frame of audio should sound like, and signals when it's ready for the next word, which keeps the speech naturally paced when text arrives unevenly.
- **Depth transformer (the "refiner"):** Turns that vector into an audio frame. Each frame is encoded as up to 32 tokens, arranged so the first captures the most important features and each later one adds finer detail. The refiner generates them in that order, so the frame becomes progressively more accurate with every token.

**One large read, one small refinement loop**

![Within each 80 ms step, the temporal transformer reads the newest text token and the previous audio frame and produces a single summary vector. The depth transformer then generates the frame's audio tokens one at a time, coarse to fine.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791571593-gradium-80ms-step-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Within each 80 ms step, the temporal transformer reads the newest text token and the previous audio frame and produces a single summary vector. The depth transformer then generates the frame's audio tokens one at a time, coarse to fine.

This split enables Gradium TTS's low TTFA. The larger temporal transformer, which has to track context, runs only once per step, while the smaller depth transformer runs up to 32 times per step but stays cheap because it never looks back in time. Those many small refiner passes also benefit from additional GPU optimization.

## GPU optimization specifically for smaller, latency-optimized models

GPUs do the heavy computation for AI models, but they don't work alone. The CPU acts as the dispatcher, and for each computational step, it selects the right GPU kernel, prepares its inputs, and issues the command to launch it. Every one of those handoffs takes a small, fixed amount of time.

In large language models, the GPU is the bottleneck, and each GPU kernel runs long enough that the CPU can queue the next launch before the current one finishes. However, in smaller AI models like streaming TTS, GPU kernels complete faster than the CPU can queue them. As a result, the CPU becomes the latency bottleneck, leading to lower GPU utilization.

Gradium addresses this challenge in two ways:

- **Kernel Fusion**: Using torch.compile and Triton, Gradium merges operations that previously required several separate GPU kernel launches into a single kernel, so each launch does more work.
- **CUDA Graphs**: The full sequence of kernels for a forward step is recorded once. On every subsequent step, the CPU issues a single replay command and the GPU driver runs the entire recorded sequence back-to-back, rather than waiting for each kernel to be launched individually.

**Typical kernel launches versus CUDA Graph Replay**

![With CUDA Graphs, the CPU issues one replay command and the recorded kernel sequence runs back-to-back, reducing TTFA.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791571896-cuda-graph-replay-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) With CUDA Graphs, the CPU issues one replay command and the recorded kernel sequence runs back-to-back, reducing TTFA.

In [Gradium's published benchmarks](https://gradium.ai/blog/optimizing-quality-vs-latency), enabling CUDA Graphs cut median TTFA by more than 2.5x at small batch sizes.

## Scaling Gradium TTS on Baseten

Traffic to voice AI applications tends to be bursty. There is high demand at the start of business hours and during triggering events such as outages or marketing campaigns. Required concurrency can rise and fall in minutes, so provisioning for the peak leaves GPUs idle most of the day, while provisioning for the average degrades performance during the first minutes of every spike.

Autoscaling resolves this, but a new replica can't serve calls until its model weights are loaded into GPU memory. Weights are typically pulled from upstream sources such as Hugging Face or S3, where rate limits and cross-region latency stretch cold starts further, especially when many replicas request the same files at once.

The [Baseten Delivery Network (BDN)](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast) reduces cold start time in three ways:

- **Push-time mirroring:** At deploy time, BDN copies the model's weights into Baseten-managed storage and records a content-hashed manifest. Upstream is touched once; every cold start after that reads from Baseten's own storage.
- **Three-tier caching:** Each GPU node checks node-local NVMe disk first, then an in-cluster peer cache, then the mirrored origin, delivering weights to H100 nodes at over 2 GB/s.
- **Coordinated downloads:** During a burst, each chunk of the model is pulled from origin by one node and shared with peers over the in-cluster network, so origin bandwidth for a 50-replica scale-up is 1x the model size, not 50x.

**How BDN pulls a model into a cluster during a scale-up**

![In a cold cluster, each node fetches only its assigned chunks from origin, so total origin bandwidth equals one copy of the model regardless of how many replicas are starting. In a warm cluster, a node assembles the file from peers over the in-cluster network without touching origin at all.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791572025-bdn-scale-up-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) In a cold cluster, each node fetches only its assigned chunks from origin, so total origin bandwidth equals one copy of the model regardless of how many replicas are starting. In a warm cluster, a node assembles the file from peers over the in-cluster network without touching origin at all.

*Source: How the Baseten Delivery Network (BDN) makes cold starts fast.*

Because weights arrive before the model container starts, the transfer also happens outside the billable GPU window. The result is 2–3x faster cold starts, so a Gradium TTS deployment on Baseten can follow sudden swings in call volume without customers waiting on a cold replica. Gradium makes each interaction fast, and Baseten makes that performance available as traffic rises and falls.

Gradium TTS is available as a [dedicated deployment on Baseten](https://www.baseten.co/library/gradium-tts/). Try it today and see these benefits on your own workload.
