---
title: Introducing NVIDIA Nemotron 3.5 ASR Streaming
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/serving
summary: Baseten benchmarks NVIDIA's Nemotron 3.5 ASR streaming models (a 600M-parameter
  cache-aware FastConformer-RNNT architecture) on H100s, sustaining 100 concurrent
  WebSocket streams with 98-138ms finalization latency, 8.84% average WER across 19
  languages, and 2.32% WER on LibriSpeech Clean for the English-only variant.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-nvidia-nemotron-35-asr-streaming/
author: Ansel Erol; Ian Carrasco
published: '2026-08-04'
fetched: '2026-08-05T06:52:25Z'
classifier: claude
taxonomy_rev: 2
words: 605
content_sha256: f5ed2aeefc80e8ccce02c6093fde4c6ae15c8bf60cafe455977ea24f9bdddbc9
---

# Introducing NVIDIA Nemotron 3.5 ASR Streaming

![Nemotron 3.5 ASR](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785796898-nemotron_3-5_asr_blog_enhanced_4x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

NVIDIA Nemotron 3.5 ASR is in the Baseten Model Library, enabling developers to deploy low-latency, production-ready speech recognition with just a few clicks. It ships as two 600M-parameter streaming models: a [dedicated English model](https://www.baseten.co/library/nvidia-nemotron-3-asr-english/) and a [multilingual model](https://www.baseten.co/library/nvidia-nemotron-35-asr-multilingual/) supporting 40 language locales. In our testing, a single H100 sustained up to 100 concurrent real-time streams over WebSocket, with even higher throughput achievable over gRPC.

## Two models, one streaming architecture

Nemotron 3.5 ASR is built to deliver both low latency and high transcription accuracy. It comes in two variants that share one cache-aware FastConformer-RNNT architecture (a 24-layer encoder and an RNNT decoder): a dedicated English model, and a multilingual model that handles 40 language locales from a single model. Language-ID prompt conditioning lets the model auto-detect the spoken language or use one you specify, and it produces punctuation and capitalization by default.

![A shared cache-aware FastConfirmer-RNNT pipeline, shipped as English and multilingual weight sets. Deployed on Baseten over WebSocket.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785451328-nemotron-diagram-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

The models are released under the [OpenMDW-1.1](https://openmdw.ai/) license and are deployed on Baseten using [NVIDIA Inference Microservices (NIM)](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/), providing highly optimized streaming inference with production-ready performance. We continue working with the NVIDIA team to distribute NIM releases as they become available.

## Nemotron 3.5 ASR performance on Baseten

We benchmarked Nemotron on a single H100, serving NVIDIA’s Realtime WebSocket API with audio paced at real time:

![First-token latency holds near 100ms as concurrency grows, reaching ~140ms at 100 streams. Zero errors at every level.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785470796-nemotron-diagram-2-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Finalization latency (the time between a speaker finishing and the final transcription being ready) remained nearly flat as concurrency increased from 8 to 100 real-time streams (98 ms to 138 ms). This consistency is especially important for interactive AI  agents, captioning, and voice applications. We also observed a stable time-to-first-token, which is determined primarily by the model’s 1-second lookahead window used to enhance transcription accuracy.

A key performance advantage from NVIDIA NIM is cache-aware inference, which reuses encoder context across chunks instead of reprocessing overlapping audio buffers. This significantly improves throughput, enabling up to 6x more concurrent streams than NVIDIA’s [Parakeet RNNT](https://huggingface.co/nvidia/parakeet-rnnt-1.1b) while maintaining low latency. While the prior measurements use a WebSocket, similar to other popular speech-to-text (STT) offerings, the NIM also exposes a gRPC interface, which carries less per-message serialization overhead than the WebSocket JSON path and can sustain considerably higher concurrency per replica for backends that can consume it.

## One streaming model across 40 language locales

The multilingual model delivers strong accuracy across transcription-ready languages. On the [FLEURS](https://huggingface.co/datasets/google/fleurs) benchmark, it achieves an average 8.84% WER across the 19 supported languages, including 4.11% WER for Spanish, 4.25% for Italian, and 7.91% for English. For English-only workloads, the dedicated English variant provides the highest possible accuracy, reaching 2.32% WER on [LibriSpeech Clean](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard).

![One model, 40 language-locales: NVIDIA-published FLEURS word error rate, 1.12s, language provided. Lower is better.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785470858-nemotraon-diagram-3-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Our multilingual testing, based on FLEURS and a realistic, noisy telephony benchmark ([μ-bench](https://huggingface.co/datasets/sierra-research/mu-bench)) aligns with findings of low WER across transcription-ready locales. The value is consistent real-time accuracy across a range of languages that few streaming models cover with only one model.

For specialized domains, under-resourced languages, or unique accents, developers can further improve transcription quality by fine-tuning Nemotron ASR using [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) through [Baseten Training](https://www.baseten.co/products/training/). If you’re interested in fine-tuning the model for your specific use case, you can learn more in [this blog](https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr).

## Try Nemotron ASR Streaming

The English and multilingual variants of Nemotron ASR Streaming are now live in the [Baseten Model Library](https://www.baseten.co/library/nvidia-nemotron-35-asr-multilingual/). Deploy production-ready, low-latency speech recognition in a couple of clicks, or [talk to one of our engineers](https://www.baseten.co/talk-to-us/) to discuss your voice AI workloads.
