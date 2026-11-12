---
title: 'Generally Available: The fastest, most accurate and cost-efficient Whisper
  transcription'
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- models/benchmarks
summary: Describes Baseten's Whisper transcription pipeline built on Chains, achieving
  a 10.0 WER on the Rev16 benchmark and transcribing 1 hour of audio in 3.6 seconds
  (2400x real-time factor).
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-fastest-most-accurate-and-cost-efficient-whisper-transcription
author: William Gao
published: '2024-12-11'
fetched: '2026-11-12T06:09:26Z'
classifier: claude
taxonomy_rev: 2
words: 1162
content_sha256: e6b5d238e64761d9a21ce63f3060187e84037276d2e980f5a5ee2879aa5a3664
---

# Generally Available: The fastest, most accurate and cost-efficient Whisper transcription

Model performance
# Generally Available: The fastest, most accurate and cost-efficient Whisper transcription

At Baseten, we've built the most performant (2400x real-time factor), accurate, and cost-efficient speech-to-text pipeline for production AI audio transcription


- Authors
- Date
- December 11, 2024

TLDR

At Baseten, we’ve built the most performant, accurate, and cost-efficient speech-to-text pipeline for production AI workloads. We achieved over 2400x real-time factor (1000x at the time of writing) and the lowest word error rate through a series of in-house optimizations to Whisper to improve both transcription accuracy and speed, all built into one compound solution using Baseten Chains.

**Note: We've since shipped more features to our Whisper transcription pipeline, including a 2.4x speed increase, streaming, and diarization! Check out the latest blog here.**

Our customers run user-facing applications with critical requirements for speed, accuracy, and cost-efficiency. Whether you’re processing large batches of varied-length audio files or building real-time applications, you need a transcription pipeline that performs rapidly and reliably to ensure customer adoption and retention—and ultimately outpace the competition.

The Whisper family of models is state-of-the-art for transcription and a popular choice because they’re open-source, robust, and multi-lingual out of the box. But if you just grab the vanilla open-source model, you’ll find it far from production quality. Aside from the fact that vanilla Whisper can’t handle audio longer than 30 seconds, it also hallucinates, produces missing chunks, is inefficient—and slow.

At Baseten, we’ve built the fastest, most accurate, and most cost-effective transcription pipeline on the market, per public benchmarks, using Whisper and our compound AI framework, [Chains](https://www.baseten.co/blog/introducing-baseten-chains/). In this blog, we break down how we optimized transcription speed while achieving the lowest word error rate (WER) of just 10.0 on the Rev16 benchmark, enabling users to reliably transcribe 1 hour of audio in only 3.6 seconds! ([Now 1.5 seconds at 2400x RTF](https://www.baseten.co/blog/the-fastest-whisper-transcription-with-streaming-and-diarization/).)

Unless you’re processing sub-30-second audio clips (and speed and accuracy aren’t important to you), you can’t just take vanilla Whisper and use it in your production pipelines out of the box.

That’s because:

1. It’s prone to hallucinations and missing chunks.
2. It can’t process arbitrary audio lengths.
3. It can’t handle long silences.
4. It’s slow.

Whisper interprets longer pauses as the end of your speech and either stops transcribing or generates hallucinations. It can also produce missing chunks even when given valid audio, leading to a confusing user experience.

Vanilla Whisper also doesn’t do [batching](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/); in other words, it doesn’t use the GPU to perform model inference in parallel. Batching drastically reduces latency when handling concurrent requests and is important for optimal GPU utilization.

Plus, you can only transcribe 30 seconds of audio. From hours of meeting notes to quick customer conversations, most speech-to-text use cases require transcribing arbitrary (or variable) lengths of audio, making this a serious limitation.

While optimizing for speed is crucial, performance is nothing without accuracy.

By implementing multiple fixes, our Whisper implementation is more robust against hallucinations and missing chunks. As a result, Baseten’s Whisper isn’t just the fastest on the market—it’s also the most accurate.

To make end-to-end transcription latency lightning-fast for any length of audio, we adopted a two-stage approach:

1. Chunk the audio.
2. Transcribe each chunk.

We use a voice activity detection (VAD) model to analyze the audio waveform and:

1. Detect periods of speech and silence.
2. Chunk the audio into short segments of speech.

By chunking these segments, we can:

- Process longer audio files by breaking them into Whisper-compatible 30-second chunks.
- Remove extended periods of silence, eliminating unnecessary GPU processing (which is faster and more cost-efficient).

With our audio chunked, we can start transcribing.

[Chains](https://www.baseten.co/blog/introducing-baseten-chains/) is a framework for building multi-step inference pipelines (a.k.a., compound AI systems), where you can define custom hardware and scaling parameters for each model and processing step. Chains are composed of [Chainlets](https://docs.baseten.co/chains/concepts#chainlet): the individual components of your pipeline (for example, individual AI models).

In our transcription pipeline, we have two Chainlets:

1. The first Chainlet performs chunking. Since the VAD model is small and fast, we can run this on a CPU or less-powerful GPU.
2. The second Chainlet will transcribe the chunks with Whisper. This step requires a more powerful GPU.

By enabling us to scale each Chainlet independently, Chains is essential for speeding up performance while keeping costs low. One request to the chunking Chainlet often turns into hundreds of requests to the transcription Chainlet. By decoupling the scaling between each step, we can:

- Provision more Whisper replicas to accommodate any audio length.
- Prevent idle GPUs, since the chunking is run in parallel, preventing bottlenecks.
- Lower costs, since we’re only using GPUs for the steps that require them.

While Chains provides the low-latency model orchestration, we also need to optimize the backbone of our pipeline: the Whisper model.

We started with a TensorRT-LLM Python runtime, which provided a **6-7x speedup** compared to [OpenAI’s Whisper](https://github.com/openai/whisper). While effective, the Python runtime still introduced some latency due to the Global Interpreter Lock (GIL) and other overheads. GIL restricts only 1 Python thread to run at a time, whereas the C++ version gives us true multithreading capabilities. Essentially, we can already start preprocessing the next request while the TensorRT-LLM engine is doing inference on the current one.

Transitioning to TensorRT-LLM’s **C++ executor runtime** showed an initial 18% speed improvement compared to the Python runtime.

Initially, we used [dynamic batching](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/), which collects requests made in a short time period in a batch. However, this approach is suboptimal because it requires waiting for the batch to fill, and incoming requests must wait for the current batch to complete processing—even if there’s capacity for additional requests.

**In-flight batching** addresses these issues, speeding up inference by:

- **Processing requests immediately**: No waiting period to fill batches.
- **Grouping on-the-fly**: Requests that arrive while a batch is being processed are immediately added to the batch if there’s room.

Switching to in-flight batching further cut processing times nearly in half. You can learn more about in-flight batching (a.k.a. [continuous batching](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/)) in [this blog post](https://www.baseten.co/blog/continuous-vs-dynamic-batching-for-ai-inference/).

Altogether, our performance enhancements make our Whisper transcription pipeline over **10x faster than OpenAI** while also being **the most accurate and cost-efficient Whisper** on the market.

Of course, you can always throw more GPUs at your pipeline for further speed improvements. But unlike other inference providers, on Baseten you can customize how many GPUs you leverage to achieve an ideal balance between cost and performance.

Create industry-leading user experiences, service more customers, and save on costs with our optimized Whisper pipeline. With over [2400x real-time factor](https://www.baseten.co/blog/the-fastest-whisper-transcription-with-streaming-and-diarization/) (1000x at the time of writing), you can transcribe hours of audio in seconds.

Baseten’s transcription pipeline is trusted by companies like Bland AI and Patreon, with HIPAA, SOC 2 Type II, and GDPR-compliant dedicated, [self-hosted](https://www.baseten.co/blog/baseten-self-hosted/), or [hybrid](https://www.baseten.co/blog/baseten-hybrid-control-and-flexibility-in-your-cloud-and-ours/) deployments.

[Check out our documentation](https://docs.baseten.co/chains/overview) to start building low-latency compound AI pipelines with Chains, or [connect with our engineers](https://www.baseten.co/talk-to-us/) and we’ll help you customize a transcription pipeline to meet your own aggressive performance targets!
