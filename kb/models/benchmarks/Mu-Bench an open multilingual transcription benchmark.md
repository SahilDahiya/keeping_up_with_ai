---
title: 'Mu-Bench: an open multilingual transcription benchmark'
topic: models
subtopic: benchmarks
secondary_topics: []
summary: Introduces mu-Bench, an open multilingual transcription benchmark for evaluating
  speech recognition quality across languages.
source: sierra
url: https://sierra.ai/blog/mu-bench-an-open-multilingual-transcription-benchmark
author: Andrea Li; Soham Ray
published: '2026-05-12'
fetched: '2026-07-11T03:51:03Z'
classifier: codex
taxonomy_rev: 1
words: 426
content_sha256: fcd31b7528b28095f0769bf3cc9f80c7b61caeb670dffc19fecd3bad629f7c4e
---

# Mu-Bench: an open multilingual transcription benchmark

# Mu-Bench: an open multilingual transcription benchmark

*Representing work by Katie Echavia, Venu Satuluri, Ola Zytek, Victor Barres, Mindy Long, Nishita Jain, Nittai Malchin, Lydia Zarcone, Kelly Cooke*

Only about a quarter of the world speaks English. Yet it's the basis for most public automatic speech recognition (ASR) benchmarks — and the ones that cover other languages typically rely on read speech recorded in quiet studios. That leaves a huge gap in what you can measure before deploying a voice agent to handle real customer conversations.

To support voice across 70+ languages, Sierra uses a constellation of ASR models — no single provider performs best across them all. Internally, we benchmark 79 locale variants across 42 languages and 13+ providers. Today, we're open-sourcing a subset of that evaluation as μ-Bench: five locales, five providers, 4,270 human-annotated utterances from 250 real phone conversations recorded at 8 kHz mono.

## What we found

We evaluated Deepgram Nova-3, Google Chirp-3, Microsoft Azure Speech, ElevenLabs Scribe v2, and OpenAI GPT-4o Mini Transcribe on real customer service calls across English, Spanish, Turkish, Vietnamese, and Mandarin. A few highlights:

- **Word Error Rate alone is misleading.**Not all transcription errors are equal — a dropped "uh" and a misheard phone number digit count the same under WER. We introduce a new metric, Utterance Error Rate (UER), that isolates meaning-changing errors from surface-level ones. Two providers can have similar WER but very different UER, because they make different- *kinds*of errors — and the meaningful ones are what break voice agents.
- **No provider wins everywhere.**Google Chirp-3 leads on accuracy but is among the slowest. Deepgram Nova-3 is nearly 8× faster on p50 latency but trails on multilingual accuracy. The right choice depends on the deployment.
- **Mandarin transcription accuracy can be 5x worse than English**— and Vietnamese varies wildly across providers. These gaps are invisible if you only benchmark on English.

## Why it matters

Without per-locale measurements, you can't choose the right model for each language, route traffic between providers, or pinpoint where the agent is failing. μ-Bench gives the community a shared baseline for measuring what actually matters: real phone audio, multiple languages, and metrics that distinguish consequential errors from formatting ones.

The dataset, code, and an open leaderboard are all publicly available. We welcome submissions from other providers and approaches.

The full writeup covers how we built the dataset, why traditional normalization breaks down for Chinese homophones, how UER scoring works under the hood, statistical significance testing across all provider pairs, and what we've learned about deploying multi-provider ASR in production.
