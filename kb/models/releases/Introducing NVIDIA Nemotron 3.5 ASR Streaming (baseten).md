---
title: Introducing NVIDIA Nemotron 3.5 ASR Streaming
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/serving
summary: Details NVIDIA Nemotron 3.5 ASR, a cache-aware FastConformer-RNNT streaming
  speech model (24-layer encoder) in English and 40-language variants, benchmarked
  at 8.84% average WER on FLEURS and sustaining 100 concurrent real-time streams per
  H100 over WebSocket.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-nvidia-nemotron-35-asr-streaming
author: Ansel Erol
published: '2026-08-04'
fetched: '2026-11-12T06:08:22Z'
classifier: claude
taxonomy_rev: 2
words: 496
content_sha256: 6acc3b76d233e74e81a8ebbeab18e538414e6a66a522d9ad0fba6c791eab8e1f
---

# Introducing NVIDIA Nemotron 3.5 ASR Streaming

AI models
# Introducing NVIDIA Nemotron 3.5 ASR Streaming

Deploy NVIDIA Nemotron 3.5 ASR for low-latency, production-ready speech recognition with 6x higher throughput and multilingual support.


- Authors
- Date
- August 4, 2026

TLDR

NVIDIA Nemotron 3.5 ASR is in the Baseten Model Library, enabling developers to deploy low-latency, production-ready speech recognition with just a few clicks. It ships as two 600M-parameter streaming models: a dedicated English model and a multilingual model supporting 40 language locales. In our testing, a single H100 sustained up to 100 concurrent real-time streams over WebSocket, with even higher throughput achievable over gRPC.

Nemotron 3.5 ASR is built to deliver both low latency and high transcription accuracy. It comes in two variants that share one cache-aware FastConformer-RNNT architecture (a 24-layer encoder and an RNNT decoder): a dedicated English model, and a multilingual model that handles 40 language locales from a single model. Language-ID prompt conditioning lets the model auto-detect the spoken language or use one you specify, and it produces punctuation and capitalization by default.

The models are released under the [OpenMDW-1.1](https://openmdw.ai/) license and are deployed on Baseten using [NVIDIA Inference Microservices (NIM)](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/), providing highly optimized streaming inference with production-ready performance. We continue working with the NVIDIA team to distribute NIM releases as they become available.

We benchmarked Nemotron on a single H100, serving NVIDIA’s Realtime WebSocket API with audio paced at real time:

A key performance advantage from NVIDIA NIM is cache-aware inference, which reuses encoder context across chunks instead of reprocessing overlapping audio buffers. This significantly improves throughput, enabling up to 6x more concurrent streams than NVIDIA’s [Parakeet RNNT](https://huggingface.co/nvidia/parakeet-rnnt-1.1b) while maintaining low latency. While the prior measurements use a WebSocket, similar to other popular speech-to-text (STT) offerings, the NIM also exposes a gRPC interface, which carries less per-message serialization overhead than the WebSocket JSON path and can sustain considerably higher concurrency per replica for backends that can consume it.

The multilingual model delivers strong accuracy across transcription-ready languages. On the [FLEURS](https://huggingface.co/datasets/google/fleurs) benchmark, it achieves an average 8.84% WER across the 19 supported languages, including 4.11% WER for Spanish, 4.25% for Italian, and 7.91% for English. For English-only workloads, the dedicated English variant provides the highest possible accuracy, reaching 2.32% WER on [LibriSpeech Clean](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard).

Our multilingual testing, based on FLEURS and a realistic, noisy telephony benchmark ([μ-bench](https://huggingface.co/datasets/sierra-research/mu-bench)) aligns with findings of low WER across transcription-ready locales. The value is consistent real-time accuracy across a range of languages that few streaming models cover with only one model.

For specialized domains, under-resourced languages, or unique accents, developers can further improve transcription quality by fine-tuning Nemotron ASR using [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) through [Baseten Training](https://www.baseten.co/products/training/). If you’re interested in fine-tuning the model for your specific use case, you can learn more in [this blog](https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr).

The English and multilingual variants of Nemotron ASR Streaming are now live in the [Baseten Model Library](https://www.baseten.co/library/nvidia-nemotron-35-asr-multilingual/). Deploy production-ready, low-latency speech recognition in a couple of clicks, or [talk to one of our engineers](https://www.baseten.co/talk-to-us/) to discuss your voice AI workloads.
