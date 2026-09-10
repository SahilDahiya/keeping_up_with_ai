---
title: How Baseten makes pyannote’s diarization models 9.6x faster
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-baseten-makes-pyannotes-diarization-models-96x-faster/
author: Matte Lim; Ansel Erol
published: '2026-09-09'
fetched: '2026-09-10T06:10:47Z'
classifier: null
taxonomy_rev: 2
words: 1456
content_sha256: e08d38c4391decf7912a0824ce87d06474e7d8f04e8ebecf635cbe5524f76741
---

# How Baseten makes pyannote’s diarization models 9.6x faster

![How Baseten makes pyannote’s diarization models 9.6x faster](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788904783-pyannote-diarization-blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Pyannote’s Community and Precision research models add state-of-the-art speaker attribution to your ASR workloads, but serving them efficiently required careful optimization. We combined quality-aware quantization, index-based clustering algorithms, and scheduling optimizations to reduce latency by up to 9.6x and increase throughput by 3x on long audio, unlocking rapid diarization at scale.

Speaker diarization — figuring out who spoke when in an audio recording — is one of the harder problems in speech AI, and one of the most useful once it works: meeting notes, call-center analytics, podcast transcripts, and media archives all depend on knowing which voice said what.

The problem is that high-quality models are typically slow and expensive to run, while affordable models are often not good enough for people building voice products. Additionally, running diarization in production workloads at scale also comes with a unique set of challenges because of how these models operate.

We’re excited to share that we have optimized both of pyannote’s latest open-source ([Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1)) and proprietary ([Precision-2](https://huggingface.co/pyannote/speaker-diarization-precision-2)) diarization models, which currently provide industry-leading Diarization Error Rate (DER) in their respective categories. We’ve improved the efficiency of these models by up to 9.6x, making them lower-cost to run while delivering exceptional diarization quality.

![Processing time vs. audio duration for upstream pyannote Community-1 versus Baseten's optimized version. Upstream's processing time grows steeply, hitting 891s at 15h and projected to cross the 1200s single-request limit around 20, while Baseten's line stays nearly flat, reaching only 128s at 20h — a 9.6x speedup at the 15-hour mark. The optimized version scales to long audio where the unoptimized pipeline can't complete in a single request.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788846577-linegraph_diarization_update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Processing time vs. audio duration for upstream pyannote Community-1 versus Baseten's optimized version. Upstream's processing time grows steeply, hitting 891s at 15h and projected to cross the 1200s single-request limit around 20, while Baseten's line stays nearly flat, reaching only 128s at 20h — a 9.6x speedup at the 15-hour mark. The optimized version scales to long audio where the unoptimized pipeline can't complete in a single request.

## Precise speaker attribution for any transcription model 

[Pyannote](https://www.pyannote.ai/) is the speaker intelligence layer for human conversations. Where speech-to-text tells you what was said, pyannote tells you who said it and when. Built on more than a decade of dedicated research, it offers open-weight models and diarization APIs that pair with any transcription model.

That focus shows up exactly where general-purpose transcription struggles. Deriving speakers from word timings falls apart the moment two people talk over each other; pyannote works from the acoustics, resolving overlap and cross-talk and placing speaker boundaries at centisecond precision instead of snapping them to word boundaries. It also returns confidence levels at the turn level, which matters when a human reviews the output or when you’re filtering training data.

Pyannote’s open-source models have been downloaded more than a billion times on Hugging Face, and over 300,000 developers build on them.

Improving diarization throughput and latency

We improved Precision-2’s throughput by 3.2x and Community-1’s long-audio latency by up to 9.6x through a mix of different techniques. This included:

- improving the scheduling and batching of internal segmentation and embedding model predictions,
- reducing memory transfers between the CPU and GPU, and
- fusing the pipeline in a single forward pass.

Many of these same techniques also help with per-request latency. Additionally, we tuned these parameters per GPU to squeeze out as much performance as we can from each chip.

### Dealing with the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality) and memory explosion

Many production workloads require running diarization on audio longer than 1h, which is a fundamental challenge for most diarization models because they require full context to provide the best quality.

Diarization models work by performing clustering over high-dimensional embeddings. Clustering at such high dimensions, especially over long audio lengths, becomes a memory issue. We applied an indexing strategy to enable **diarizing 20 hours of audio in just two minutes on a single GPU** — a workload the unoptimized pipeline cannot complete in a single request.

![Two approaches to speaker clustering: the upstream method compares every embedding pair directly, so cost grows quadratically with N; Baseten's approach first indexes and merges near-duplicate embeddings into far fewer micro-clusters, then runs the same clustering algorithm on that smaller set. This reduces the problem size before clustering rather than changing the clustering logic itself, so quality stays the same while the computation shrinks.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788846664-diagram-2_diarization-update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Two approaches to speaker clustering: the upstream method compares every embedding pair directly, so cost grows quadratically with N; Baseten's approach first indexes and merges near-duplicate embeddings into far fewer micro-clusters, then runs the same clustering algorithm on that smaller set. This reduces the problem size before clustering rather than changing the clustering logic itself, so quality stays the same while the computation shrinks.

### Quantization without quality loss

Not all parts of the diarization pipeline can be easily quantized, so we turned to quality-aware quantization. We also run the different parts of the pipeline at mixed precisions, based on their sensitivity and effectiveness in handling lower data precision. This allowed us to boost throughput by 3.2x for the proprietary model by fitting more batches within a forward pass with only a 0.5% absolute DER penalty.

Notably, one stage runs at higher precision rather than lower: the clustering loop runs in float64 on the GPU, made faster by moving it there rather than by shrinking it.

![Different stages of the diarization pipeline run at different numerical precisions based on their sensitivity: FP8 for the first convolution (smallest format, biggest memory savings), BF16 for segmentation, FP32 left unchanged for the fragile embeddings stage, and FP64 for clustering. FP64 is a move towards higher precision, made faster by running on the GPU rather than by shrinking it. Mixed precision enables speed gains without a noticeable effect on quality.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788846728-diagram-1_diarization-update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Different stages of the diarization pipeline run at different numerical precisions based on their sensitivity: FP8 for the first convolution (smallest format, biggest memory savings), BF16 for segmentation, FP32 left unchanged for the fragile embeddings stage, and FP64 for clustering. FP64 is a move towards higher precision, made faster by running on the GPU rather than by shrinking it. Mixed precision enables speed gains without a noticeable effect on quality.

## Results

We’ll let the results speak for themselves.

### Quality

Diarization Error Rate (DER, lower = better) on the [VoxConverse](https://huggingface.co/datasets/diarizers-community/voxconverse) dataset.

- Open-source pyannote [Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) : 11.1%
- Proprietary pyannote [Precision-2](https://huggingface.co/pyannote/speaker-diarization-precision-2) : 8.8%

These results represent state-of-the-art performance for models of their size and speed.

### Efficiency

“Vanilla” is upstream pyannote, installed from `pip`.

#### Open-source pyannote Community-1

Tested on a single RTX PRO 6000, concurrency 1:

#### Pyannote Precision-2

Latency tested on a single RTX PRO 6000, 5 minutes of audio:

![Latency vs. concurrent requests for upstream pyannote Precision-2 versus Baseten's optimized version. The vanilla model’s latency climbs steadily with concurrency, reaching 20.0s at 16 concurrent requests, while Baseten's line stays consistently lower, hitting only 6.12s at the same point; a 3.3x speedup.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788846861-linegraph_diarization-2_update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Latency vs. concurrent requests for upstream pyannote Precision-2 versus Baseten's optimized version. The vanilla model’s latency climbs steadily with concurrency, reaching 20.0s at 16 concurrent requests, while Baseten's line stays consistently lower, hitting only 6.12s at the same point; a 3.3x speedup.

*Latency vs. concurrent requests for upstream pyannote Precision-2 versus Baseten's optimized version. The vanilla model’s latency climbs steadily with concurrency, reaching 20.0s at 16 concurrent requests, while Baseten's line stays consistently lower, hitting only 6.12s at the same point; a 3.3x speedup.*

The full results:

The advantage peaks at concurrency 4 and narrows as the GPU saturates; batching buys the most before you run out of capacity. Our optimizations enable 3.2x the throughput on 5-minute requests.

Most of the optimizations we shared here target pre-recorded diarization use cases; we’ll have exciting news soon about improvements to our [streaming diarization model](https://www.baseten.co/blog/the-fastest-whisper-transcription-with-streaming-and-diarization/#the-foundation-the-fastest-whisper-transcription-gets-even-faster). Additionally, we serve our diarization models in different flavors, from standalone deployments to fully packaged transcription and diarization solutions.

## Coming soon: voiceprints and speaker identification

Diarization tells you that speaker 1 and speaker 2 are different people, but it doesn’t tell you who they are. Across two recordings, today’s “speaker 1” and tomorrow’s might have nothing to do with each other.

Next, we’re bringing voiceprint enrollment and cross-session speaker identification to our diarization deployments with pyannote. Enroll a speaker from a short sample, and later recordings return that person by name with a calibrated confidence score. It costs no additional GPU work: a diarization pass already computes the per-speaker embeddings and the calibration this needs, so identification is arithmetic over values that have already been paid for.

If you’re interested in running the fastest and most accurate diarization models available, [reach out](https://www.baseten.co/talk-to-us/) to speak to our engineers!
