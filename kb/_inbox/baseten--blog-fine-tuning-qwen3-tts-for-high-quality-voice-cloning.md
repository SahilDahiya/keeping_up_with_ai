---
title: Fine-tuning Qwen3-TTS for high-quality voice cloning
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/fine-tuning-qwen3-tts-for-high-quality-voice-cloning/
author: Ian Carrasco
published: '2026-07-31'
fetched: '2026-08-01T06:49:20Z'
classifier: null
taxonomy_rev: 2
words: 1412
content_sha256: 040cf5f7d5db82a0f46a8c103ac7992b261cb2f377ad6945b2aa6d12b1f8203e
---

# Fine-tuning Qwen3-TTS for high-quality voice cloning

![Fine-tuning Qwen3-TTS for high-quality voice cloning](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785491261-baseten-blog-2026-thumbnails-14.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Building expressive speech experiences that capture the mannerisms and nuance of human speech requires richer, more extensive datasets across a wide range of speech scenarios. Models like [Qwen3-TTS](https://www.baseten.co/library/qwen3-tts-12hz-base-streaming-1-7b/) already ship with a remarkable ability to perform zero-shot voice cloning from a few seconds of audio. But richer cloning capabilities require fine-tuning over a larger corpus of utterance-level examples. 

Closed-source providers typically call this "professional voice cloning," as opposed to "instant voice cloning." It requires a larger upfront dataset curation step, including sourcing a voice actor.

We’ve published a modified version of the official published Qwen3-TTS training recipe in our [ml-cookbook](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-tts-transformers) for creating single-speaker fine-tuned checkpoints on Baseten Training, which can then be easily deployed on Baseten Cloud as a dedicated deployment.

## Three approaches to voice cloning: ICL vs. speaker-embedding-only vs. fine-tuning

Qwen3-TTS was designed with strong voice cloning capabilities in mind, but extracting the best quality and performance from the model requires fine-tuning. Qwen3-TTS has two primary instant voice cloning modes: in-context learning (ICL) and speaker-embedding-only.

### In-context learning (ICL)

ICL mode tokenizes your reference audio and reference text and includes them as a prefix for every request. This teaches the relationship between reference audio and reference text at inference time, but it costs a considerable prefill overhead (~100s of tokens) for stronger voice conditioning.

ICL mode can also cause speaker inconsistency due to inherent non-determinism in attention and the current prompt being generated. For longer, non-streaming generations, this is often a solid approach, since those cases avoid frequent reconditioning per utterance.

### Speaker-embedding-only mode

Speaker-embedding-only mode passes your reference audio through a smaller speaker embedding model (ECAPA-TDNN) that produces a roughly 10-token embedding, added as a prefix before generation. This yields lower time to first audio (TTFA) at the expense of better speaker capture due to the reduced dimensionality of the speaker embedding. However, the smaller speaker embedding means lower prefill overhead, especially at higher concurrency.

### Fine-tuning 

The goal of fine-tuning is to capture a richer text-audio alignment relationship without the additional overhead of ICL-based cloning. We accomplish this by training on significantly more text-audio pairings via supervised fine-tuning (SFT) and conditioning the model to generate based on an accumulated speaker embedding across a subset of the pairs.

![The input "shapes" for the three voice cloning approaches.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785492476-whisper-fine-tuning-diagram-1-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The input "shapes" for the three voice cloning approaches: ICL mode stacks a speaker embedding, reference audio, reference text, and the text prompt; speaker-embedding-only mode drops the reference audio and text, using just the embedding plus prompt; and fine-tuning drops the speaker input entirely, since voice identity is baked into the model weights. Each step down removes conditioning inputs (and their inference overhead).

### Different prompt constructions based on cloning paradigm

## Fine-tuning recipe

### Step 1: Building the dataset

Performing TTS fine-tuning commonly requires a dataset of single-speaker (audio, text) pairs. You can produce these by having the target speaker read a pre-existing transcript, or by generating the dataset with an ASR model in the loop, which only requires audio as input.

Given a long-form audio file, we transcribe it while simultaneously emitting character-level timestamps. These timestamps let us split the transcript and reference audio at closing punctuation, producing utterance-level paired training examples.

We repeat this until the full audio is processed. For the published example, we used the [LJ Speech dataset](https://keithito.com/LJ-Speech-Dataset/), which contains roughly 24 hours of single-speaker audio (but we fine-tuned on only about 1.5 hours as a more realistic starting point).

![The voice cloning dataset-building pipeline.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785492698-whisper-fine-tuning-diagram-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The dataset-building pipeline: a long-form audio file runs through Whisper for ASR, which produces character-level timestamps used to split the audio at closing punctuation. The result is a table of utterance-level pairs, matching each transcript segment to its corresponding audio clip, ready for training.

### Step 2: Training the model

Qwen3-TTS uses a multi-codebook approach to produce audio features that are then decoded into a waveform. Raw waveform audio is too high-rate to model directly; predicting it sample by sample would explode sequence lengths and compute. Instead, vector quantization is applied iteratively to the upstream residuals to produce a compact residual vector-quantized (RVQ) representation: 12 codec frames per second, each spanning 16 codebooks.

As in LLM training, we use cross-entropy loss between the tokenized ground-truth audio and generated speech, split into two components: talker loss and sub-talker loss. Talker loss is the cross-entropy at the first codebook, which carries most of the phonetic and prosodic content. Sub-talker loss aggregates the remaining 15 codebook layers, which capture more fine-grained acoustic detail. The weighting of sub-talker loss relative to talker loss is tunable and an area for further exploration; our recipe used the upstream default of 0.3.

We also updated how the target speaker embedding is derived. Instead of using a single reference clip, we compute it as a centroid: the frozen speaker encoder runs over 64 training clips, and the embeddings are averaged. A single clip is a noisy estimate of voice identity. Per-clip embeddings of the same speaker typically agree at roughly 0.7 cosine similarity with each other, but at 0.85+ with their centroid, so the mean across clips is a more stable target. Sensitivity to the selected reference clip is a known issue with zero-shot cloning, and this approach helps address it systematically. The centroid embedding is then baked directly into the fine-tuned checkpoint, eliminating the need for any reference audio processing at inference time.

We extended the published recipe with linear warmup and cosine learning-rate decay. TTS fine-tuning, like other modalities, is sensitive to learning rate. Values above 1e-5 tend to degrade speaker quality on smaller voice datasets, and a flat schedule both overshoots early (while the speaker head is still adapting) and overfits late. Warmup plus cosine decay smooths both ends, helping the model adapt to the target speaker without degrading its pretrained speech capabilities.

![Fine-tuning loss computation across talker and sub-talker codebooks.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1785492744-whisper-fine-tuning-diagram-3-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Fine-tuning loss computation across talker and sub-talker codebooks. Ground-truth speech is tokenized by a frozen RVQ tokenizer, while ground-truth text plus the speaker embedding feed the TTS model, and cross-entropy loss compares the two sets of codebook outputs. Codebook 0 (talker) carries the main phonetic and prosodic signal, while codebooks 1–15 (sub-talker, generated by one MTP module) capture finer acoustic detail. Both loss terms are computed in parallel and weighted separately during training.

## Fine-tuning in action

To illustrate the quality difference between zero-shot voice cloning and fine-tuning, we ran the recipe on a slice of the LJ Speech dataset (800 clips, about 1.5 hours) to resemble the data-constrained settings most voice products actually operate in, where collecting even a few hours of clean, single-speaker audio is a considerable effort.

The fine-tuning run took about 1 hour on a single H100 for 8 epochs. The fine-tuned model achieves a TTFA of roughly 130 ms, matching speaker-embedding-only performance and about 16% faster than ICL (roughly 154 ms), which pays a prefill cost to process reference audio at inference time.

Fine-tuning on 1.5 hours of audio didn't materially beat zero-shot on similarity or MOS-style quality. The case for it is operational (no reference audio, stable latency at scale) and perceptual (better expressiveness on prompts where cloning sounds flat), with room to improve as your dataset grows beyond a few hours of speech.

Some examples where fine-tuning had meaningful improvements on perceived naturalness and expressiveness:

One-shot

Fine-tuned

And with more emotion:

One-shot

Fine-tuned

And more prosody:

One-shot

Fine-tuned

## How to further improve text-to-speech fine-tuning results

Beyond SFT, there's growing interest in incorporating RL reward signals (DPO, GRPO) into the post-training loop.

Voice has been a difficult domain for automated evals like LLM-as-judge and is often bottlenecked by more extensive human evals. Automated metrics like EmergentTTS and TTSDSv2 aim to correlate strongly with human ratings on the same audio samples. These can further enhance fine-tuning runs, optimizing checkpoints for human preference rather than a naive cross-entropy objective.

We're also seeing growing demand for richer control over pronunciation and emotion. These are typically closed-source API features, and developing techniques to fine-tune them into existing open-source models is a promising research direction.

## Fine-tune your own speech models

We have a Qwen3-TTS fine-tuning recipe published in our [ml-cookbook](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-tts-transformers), and you can self-deploy it directly on [Baseten Training](https://docs.baseten.co/training/index). Checkpoints produced from Baseten Training can also be referenced directly from a [Truss config](https://docs.baseten.co/development/model/overview), for a seamless training-to-inference workflow.

If you have any questions or need support fine-tuning your TTS models, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers.
