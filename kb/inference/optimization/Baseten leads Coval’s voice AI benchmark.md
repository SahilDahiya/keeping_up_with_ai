---
title: Baseten leads Coval’s voice AI benchmark
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- evals-observability/benchmark-design
summary: Baseten's STT deployment (Qwen3 ASR 1.7B Streaming) tops Coval's voice AI
  benchmark, running ~5x faster than OpenAI's while posting the lowest WER; argues
  voice AI benchmarks must measure the full turn (STT, LLM, TTS, VAD, orchestration,
  autoscaling) rather than a single model's throughput, since p95 latency and infrastructure
  placement matter as much as model choice.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-leads-covals-voice-ai-benchmark/
author: Alina Weinstein
published: '2026-09-08'
fetched: '2026-09-09T06:10:13Z'
classifier: claude
taxonomy_rev: 2
words: 863
content_sha256: c12f8a4903819b2632ab4643030f0e8152f3f5500d4ba3530a826132f38ada16
---

# Baseten leads Coval’s voice AI benchmark

![leads covals voice ai benchmark](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788905247-baseten-blog-2026-thumbnails.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Baseten leads Coval’s voice AI benchmark by sitting on the quality-latency Pareto frontier: its STT deployment is about 5× faster than OpenAI’s while also delivering the lowest WER. Production voice AI performance is not just about model choice, it depends on the full inference stack, from STT and TTS latency to orchestration, networking, autoscaling, and deployment placement.

[Coval](https://www.coval.ai/) is a voice AI evaluation platform that helps teams test, compare, and improve AI agents with reproducible, independent benchmarks. Its open benchmark methodology highlights the core inputs behind every leaderboard result: the dataset, provider model versions, normalization pipelines, and latency measurement approaches.

In Coval’s early-access benchmarks in September 2026, Baseten is positioned at the top of the leaderboard, sitting on the quality-latency Pareto frontier. The benchmark measures what end-users experience: for speech-to-text (STT), that means evaluating both speed and quality together. For text-to-speech (TTS), latency (or time to first audio) determines whether the agent feels responsive. Word Error Rate (WER) measures transcription accuracy and determines whether the agent understands the user.

In these tests, Baseten’s STT deployment is approximately 5× faster than OpenAI’s while also showing the best WER. This result shows that optimized inference can improve responsiveness without forcing teams to sacrifice transcription quality.

## **On the frontier of quality and latency**

Baseten defines the Pareto frontier with Qwen3 ASR 1.7B Streaming for STT with both latency and quality: no provider in the current benchmark is faster while also producing a lower WER*.

![*as of Sept 8, 2026](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788898704-image-12.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) STT

*as of Sept 8, 2026

For TTS, Baseten still sits close to the quality-latency frontier even though performance across providers is more tightly clustered.

![TTS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788540844-screenshot-2026-08-31-at-9-33-03-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) TTS

## **For voice AI, inference infrastructure defines product quality**

Voice agents require many models working together, but this adds a network tax that increases end-user latency. Even a few hundred milliseconds of delay can ruin realism in a live conversation.

![Hear the difference between a flagship provider and Baseten for STT](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2F4015xCrq8YBgnxues01RuJ7jOiagTHkMdr%2Fthumbnail.jpg&w=3840&q=75)

A typical voice stack sends audio to one provider for speech-to-text, forwards text to another provider for reasoning, then sends the response to a third provider for text-to-speech. Latency compounds across the voice pipeline. Every hop between STT, LLM, TTS, orchestration, and networking adds latency the user can feel. The fastest voice experiences come from optimizing the inference stack and tightening the distance between every part of the voice stack.

![Hear the latency difference between flagship providers and Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2F02ATgbBgQakapPiP01E5GiIXm01goN1W91o%2Fthumbnail.jpg&w=3840&q=75)

The path to lower latency compounds: optimize each model, keep scaling behavior consistent, and co-locate the pipeline as close as possible to the end user.

## **Benchmarks should measure the inference layer**

That’s why the right benchmark for a voice agent can’t just measure a single model’s throughput; it must include the full turn from when a user stops speaking to when the system starts speaking back. That means measuring how quickly the speech-to-text model streams or finalizes the transcript, how fast the LLM begins responding, how quickly the text-to-speech model produces first audio, and how much delay comes from voice activity detection (VAD), telephony, orchestration, networking, autoscaling, and concurrency.

Without that full-stack view, a strong median (p50) latency can still hide a p95 latency that hurts 5% of conversation turns for every user, and degrades the overall voice agent experience in production.

For teams building voice AI, the challenge goes beyond choosing models; it’s deciding which combination of providers, models, and infrastructure will make the product feel better in production.

## **Benchmarks are more complete with infrastructure**

At Baseten, we’re not only optimizing for peak speed, but for the reliability and consistency production voice agents need. Reliability matters as much as customizability; for voice workloads, a fast median is not enough if latency swings under load. Dedicated hardware helps avoid noisy neighbors, keeping the latency distribution tighter and performance more consistent. Coval’s benchmark accounts for that consistency.

The “best” configuration depends on the use case:

- **Streaming STT** needs low time to first transcript and stable finalization behavior.
- **Batch transcription** can optimize more heavily for throughput and cost.
- **TTS** needs low time to first audio for interactive agents, but may optimize differently for non-streaming generation.
- **Full voice agents** need all components to fit inside one end-to-end conversational latency budget.

Coval’s benchmark currently runs from a fixed region by design, which is useful for fairness and reproducibility. But in production, workload placement is one of the most important levers voice builders have. The benchmark gives teams a baseline; deployment architecture determines how that baseline translates in production.

Baseten’s deployments slot into Coval’s benchmark as normal API endpoints, but with dedicated inference levers underneath. That means the benchmark can reflect more than model quality; it can show what happens when inference is tuned for production voice AI, including reliability and performance consistency.

## **Get started**

Deploy the benchmark models in one click from our Model Library:

Deploy: [https://www.baseten.co/library/qwen3-tts-12hz-base-streaming-1-7b/](https://www.baseten.co/library/qwen3-tts-12hz-base-streaming-1-7b/)

Deploy: [https://www.baseten.co/library/qwen3-asr-1-7b-streaming/](https://www.baseten.co/library/qwen3-asr-1-7b-streaming/)

From there, teams can plug the model into their own voice pipeline, test it on their own data, and tune the deployment for their latency, quality, and cost targets. If you need something more custom, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
