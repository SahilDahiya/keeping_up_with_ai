---
title: The fastest Whisper — with streaming and diarization
kind: blog
topic: inference
subtopic: optimization
secondary_topics: []
summary: Adds real-time streaming and speaker diarization to Baseten's Whisper Large
  V3 Turbo pipeline (8 H100 MIGs, 2400x RTF), decoupling WebSocket server (CPU) from
  the model server (GPU) via Baseten Chains for independent autoscaling.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-fastest-whisper-transcription-with-streaming-and-diarization
author: Tianshu Cheng
published: '2026-01-15'
fetched: '2026-11-12T06:10:50Z'
classifier: claude
taxonomy_rev: 2
words: 895
content_sha256: 0b1013f0acc839acb5bd6345bffa10e377dd3284ab1c138c43e68d54896ef91c
---

# The fastest Whisper — with streaming and diarization

Model performance
# The fastest Whisper — with streaming and diarization

Baseten powers the fastest, most accurate, and cost-efficient Whisper transcription on the market, with streaming and diarization.


- Authors
- Date
- January 15, 2026

Since 2024, we’ve been proud to offer the fastest, most accurate, and cost-efficient Whisper transcription on the market. Now, we’re excited to announce the latest iteration of our work: real-time, speaker-aware transcription that’s even faster and lower in cost.

We focus on engineering flexible solutions for production applications, not just optimizing specific models. As a result, our Whisper transcription pipeline can be customized for each use case—with or without streaming or diarization, and with a configurable number of GPUs (vs. being coupled to entire nodes as so many inference providers do).

We’re proud to power real-time transcription and diarization for products like Notion’s AI Meeting Notes.

Our engineers are constantly pushing the envelope on inference performance across each model modality. [Since we first announced](https://www.baseten.co/blog/the-fastest-most-accurate-and-cost-efficient-whisper-transcription/) the fastest, most accurate, and most cost-efficient Whisper transcription, we’ve continued to iterate on our pipeline for our customers who use it daily in production. As of this writing, our Whisper transcription pipeline is over 2x faster than before—with 2400x real-time factor (RTF) using Whisper Large V3 Turbo running on 8 H100 MIGs.

Speed is crucial, but the pipeline also has to be designed for real-world use cases. We’ve consistently heard from our customers and prospects that other inference providers bundle solutions with rigid hardware commitments. That’s why our team focused on engineering a flexible solution that can be coupled with a configurable number of GPUs for more control and flexibility for cost-sensitive use cases.

We built our Whisper transcription pipeline (including the streaming and diarization variants) on top of [Baseten Chains](https://www.baseten.co/products/chains/). Chains is an SDK for compound AI systems that lets us decouple different parts of the pipeline, running each on dedicated hardware with custom autoscaling (like running the WebSocket server on a CPU vs. the Whisper model server on H100 MIGs). This delivers incredible cost-efficiency through clever engineering alone—put head-to-head with our competitors in multiple bake-offs, nobody has been able to come close.

| Provider | Cost (per audio min) | 
|---|---|
| OpenAI Whisper V2 | $0.006 | 
| Fireworks Whisper Large V3 | $0.0015 | 
| Fireworks Whisper Large V3 Turbo | $0.0009 | 
| Baseten Whisper Large V3 | \~$0.0002 | 
| Baseten Whisper Large V3 Turbo | \~$0.0001 | 

In addition to these performance and cost improvements on our standard Whisper transcription offering, we’ve added two additional features: **streaming audio transcription for real-time use cases, and speaker annotation** (a.k.a. diarization – also possible with streaming).

You can deploy our optimized Whisper model server from our [model library](https://www.baseten.co/library/whisper/), or [reach out](https://www.baseten.co/talk-to-us/transcription-and-diarization/) to talk to our engineers about leveraging it for higher-scale workloads.

For use cases that require streaming, we’ve expanded our Whisper pipeline to support real-time transcription. Our live transcription is ideal for use cases like live note-taking applications, content captioning, customer support, and any real-time, voice-powered apps.

Features include:

- Configurable update cadence for the partial transcriptions delivered
- Consistent real-time latency under high volume of concurrent audio streams
- Automatic language detection for multilingual transcription

Built on top of our ultra-low-cost Whisper transcription pipeline, our real-time Whisper transcription offering also consistently outprices other solutions without sacrificing quality.

| Product | Pricing | 
|---|---|
| Fireworks Streaming ASR v2 | $0.0035 | 
| Baseten Whisper Large V3 (Multilingual) | $0.003 | 
| Baseten Whisper Large V3 Turbo (Multilingual) | $0.0015 | 

You can deploy our optimized Whisper (streaming) model server from our [model library](https://www.baseten.co/library/whisper-streaming-large-v3-truss/), or [reach out](https://www.baseten.co/talk-to-us/transcription-and-diarization/) to talk to our engineers about leveraging it for higher-scale workloads.

Diarization is an inherently hard problem to solve: it’s often unknown how many speakers will be in a dialogue, when a new speaker joins, and it’s challenging to align speaker tags with a transcript. All of this becomes even more complicated when you do diarization in real time (i.e., with streaming).

Our team swarmed to tackle this problem, building an accurate, low-cost, and insanely fast diarization pipeline for our customers’ production use cases. We developed a number of custom optimizations on top of state-of-the-art diarization libraries, along with a custom speaker assignment algorithm to accurately map the annotation results to transcripts.

As a result, we achieve the fastest, most accurate production-ready diarization on the market. Our solution is also 50-90% cheaper than competitors' while offering higher throughput with the same number of GPUs.

Diarization is an optional add-on to any of our Whisper transcription pipelines (with or without streaming). Currently, our diarization + transcription pipeline powers Notion’s AI Meeting Notes.

Traditional diarization pipelines require full audio context. Ours does not. We use a sliding‑window approach that produces high‑quality results in real time while preserving speaker consistency across extended streaming sessions.

Our real-time diarization is ideal for use cases like AI notetaking, live conferencing, customer support, and any speaker-aware conversational AI apps. In contrast to other solutions that use visual cues or annotative data, **our approach is audio-only, with no additional inputs**. Our diarization feature has been validated under heavy load, with thousands of concurrent audio streams in production, without degrading accuracy or cost-efficiency.

We’re continuously iterating to push the frontier of diarization performance. [Reach out](https://www.baseten.co/talk-to-us/transcription-and-diarization/) to our engineers to discuss how we can customize our speaker-aware Whisper transcription for your workload!
