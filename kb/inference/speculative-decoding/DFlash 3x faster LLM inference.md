---
title: 'DFlash: 3x faster LLM inference'
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Explains DFlash as an optimization for faster LLM inference.
source: baseten
url: https://www.baseten.co/blog/dflash-faster-llm-inference/
author: Aaryam Sharma
published: '2026-05-08'
fetched: '2026-07-11T04:05:31Z'
classifier: codex
taxonomy_rev: 1
words: 1822
content_sha256: ab35f192d37e4366d60a041a1d8d548736e014b7b6c31d55c3ae468a17d5264c
triage: keep
skip_reason: null
---

# DFlash: 3x faster LLM inference

![DFlash: 3x faster LLM inference](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1778161821-baseten-blog-2026-thumbnails-6.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

By design, LLMs today only output one token at a time. As a result, speculative decoding (SpecDec) has become one of the most effective ways to improve LLM inference latency: a smaller draft model proposes tokens that the target model verifies in parallel, yielding 2x+ speed improvements depending on proposal acceptance rates.

EAGLE ([original](https://arxiv.org/abs/2401.15077), [EAGLE-2](https://arxiv.org/abs/2406.16858), and now [EAGLE-3](https://arxiv.org/abs/2503.01840)) emerged as one of the most popular SpecDec techniques, using the target model's hidden states to predict draft tokens with better acceptance rates than earlier approaches. But EAGLE is autoregressive; each predicted token requires its own forward pass from the draft model, which in practice often caps its speedups at roughly 2x as it lets errors accumulate across forward passes.

DFlash was introduced in February 2026 ([paper](https://arxiv.org/abs/2602.06036),[ code](https://github.com/z-lab/dflash)) to push past the ceiling that autoregressive drafting imposes on SpecDec speedups. A single DFlash forward pass completes faster than the entire EAGLE draft phase, while predicting several more tokens. In practice, we see that translates to a 50% speed bump: on Qwen3-8B on a single B200, Baseten's DFlash implementation delivers ~3x speedups across various benchmarks (in terms of inference latency and throughput), compared to 2x with EAGLE. 

![Throughput for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the highest mean throughput at 654 TPS, a 3x improvement compared to baseline and 10% (1.1x) faster than vLLM’s DFlash implementation.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1778162288-dflash-bar-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Throughput for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the highest mean throughput at 654 TPS, a 3x improvement compared to baseline and 10% (1.1x) faster than vLLM’s DFlash implementation.

Throughput for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the highest mean throughput at 654 TPS, a 3x improvement compared to baseline and 10% (1.1x) faster than vLLM’s DFlash implementation.![Latency for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the lowest mean latency at 1.2 seconds, a 2.9x improvement compared to baseline and 25% (1.3x) faster than vLLM.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1778162307-dflash-bar.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Latency for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the lowest mean latency at 1.2 seconds, a 2.9x improvement compared to baseline and 25% (1.3x) faster than vLLM.

Latency for 3 different speculative decoding techniques (and one baseline without SpecDec) on the GSM8k benchmark. Baseten’s DFlash implementation achieves the lowest mean latency at 1.2 seconds, a 2.9x improvement compared to baseline and 25% (1.3x) faster than vLLM.This post covers how DFlash works, how Baseten's implementation differs from vLLM and SGLang, training details, and full benchmark results, including inference latency and throughput across GSM8k, MATH-500, and NVIDIA’s Nemotron post-training dataset.

## DFlash: Block diffusion for speculative decoding

DFlash aims to bridge the quality of autoregressive decoding with the speed of diffusion LLMs. Like EAGLE, DFlash uses the hidden states of the target model as input features, as they provide very rich data representations aligned with the target model. But unlike EAGLE, DFlash:

- Predicts multiple (γ) tokens in parallel in a single forward pass by using bidirectional attention
- Allows for a much deeper draft model without sacrificing speed

Although a single forward pass for the larger DFlash draft model might be 2-4x slower than a single forward pass for EAGLE (depending on model sizes), DFlash predicts 8-16 tokens at once, while EAGLE could only predict 1. That means that despite the larger draft model, a single DFlash forward pass is faster than the entire EAGLE draft phase, while also predicting several more tokens. The larger model size also allows DFlash draft models to learn more and produce higher-quality drafts.

The DFlash model looks like this:

![The DFlash draft model takes fused target context features (hidden states from the target model), the last valid decode token, and a block of mask tokens as input. It then runs these through multiple draft layers using bidirectional attention — predicting all masked tokens in parallel in a single forward pass — before passing them to the target language model head for speculative verification.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1778162547-figure-1-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The DFlash draft model takes fused target context features (hidden states from the target model), the last valid decode token, and a block of mask tokens as input. It then runs these through multiple draft layers using bidirectional attention — predicting all masked tokens in parallel in a single forward pass — before passing them to the target language model head for speculative verification.

The DFlash draft model takes fused target context features (hidden states from the target model), the last valid decode token, and a block of mask tokens as input. It then runs these through multiple draft layers using bidirectional attention — predicting all masked tokens in parallel in a single forward pass — before passing them to the target language model head for speculative verification.## DFlash in the Baseten Inference Stack

For drafting the new tokens, DFlash creates a block of size `block_size` (a parameter), with the first token being the last valid token (either the last context token or the last accepted token), and the rest being mask tokens. Then, similar to masked language modeling, the DFlash model proceeds to unmask the mask tokens.

In practice, we take the hidden states from 5-6 evenly spaced layers of the target model. The same hidden states are passed through all layers of the DFlash model. These are projected to construct the KV cache for each layer.

We have failed to find a faster DFlash implementation than our own. To make DFlash so fast, we tested each backend to leverage the fastest one and implemented a custom forward pass mechanism to prepare the KV cache and produce output tokens. We also support guided decoding.

## Results: DFlash speed improvements on 3 benchmarks

To assess inference latency and throughput improvements from using DFlash, we tested our implementation with Qwen3-8B across three benchmarks. We used GSM8k and MATH-500 because they were used in the original DFlash paper (making the results directly comparable), and we added a diverse prompt dataset (NVIDIA’s Nemotron post-training dataset covering science, coding, and general chat) to test generalization beyond math.

Our DFlash implementation outperforms both EAGLE and other DFlash backends (vLLM, SGLang) across all three benchmarks. We don't report the numbers for SGLang here since we could not reproduce reliable results (more details below), but even after cleaning up the output sequences post-hoc, both our imlementation and vLLM were faster that SGLang.

### GSM8k (arithmetic reasoning)

The [GSM8k](https://huggingface.co/datasets/openai/gsm8k) benchmarks were conducted at concurrency 16 on a single B200 GPU. Throughput results (higher is better):

And latency results (lower is better):

SGLang also supports DFlash, however, in our evaluation, SGLang produced unreliable results due to a high rate of looping outputs. In these cases, a sequence of tokens near the end of the response was repeated until generation completed.

Because these repeated tokens did not represent meaningful generation, the resulting outputs were unsuitable for evaluation and resulted in unusually high acceptance rates and throughput. This made the aggregate statistics unrepresentative of usable generation quality. Although we filtered out these samples, this altered the output length distribution and biased our data towards shorter and faster generations. We therefore decided to exclude SGLang from our comparisons as these were not directly comparable.

In the filtered results, we found SGLang’s performance was slightly slower than vLLM in terms of TPS, and lower than the Baseten implementation for both throughput and latency.

### Math 500 Dataset (complicated mathematical reasoning)

This is from the [HuggingFaceH4/MATH-500 dataset](https://huggingface.co/datasets/HuggingFaceH4/MATH-500), also used in the DFlash research paper.

In terms of throughput (higher is better):

And latency (lower is better):

### Diverse prompts (NVIDIA’s Nemotron post-training dataset)

This benchmark comes from the [nvidia/Nemotron-Post-Training-Dataset-v2](https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2) dataset and tests science, math, coding, and general chat abilities.

First, throughput (higher is better):

And latency (lower is better):

## How to train DFlash draft models

At Baseten, we also train DFlash draft models from scratch when the application calls for it. Training takes two inputs:

- Input IDs
- Target model hidden states

We sample random anchors to define the last accepted token. Everything before it is treated as context, and we pass the target model's hidden states for those tokens. For the `block_size` number of tokens starting at the anchor, we use the input IDs as targets and run the denoising step with standard cross-entropy loss. The embedding and `lm_head` are both frozen.

Since earlier tokens are more important in speculative decoding, we weight them higher: the token is weighted by for a decay parameter .

![The attention mask structure used in DFlash's bidirectional drafting. The target model provides context features (pink, left side) that condition the draft model. The input consists of clean prompt tokens p and clean response tokens r. Within each masked block, a subset of clean response tokens (dark green) is randomly sampled as anchors, while mark tokens m (light green) mark positions for parallel prediction. Invisible tokens (gray) denote the attention mask, which enforces causal consistency and prevents inter-block information leakage during training. (The diagram shows three anchors positioned one after the other. For the masked token <M> right after R1, the label is set to be R2, for the next <M> the label is R3, and so on.)](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1778163494-figure-2-4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The attention mask structure used in DFlash's bidirectional drafting. The target model provides context features (pink, left side) that condition the draft model. The input consists of clean prompt tokens p and clean response tokens r. Within each masked block, a subset of clean response tokens (dark green) is randomly sampled as anchors, while mark tokens m (light green) mark positions for parallel prediction. Invisible tokens (gray) denote the attention mask, which enforces causal consistency and prevents inter-block information leakage during training. (The diagram shows three anchors positioned one after the other. For the masked token <M> right after R1, the label is set to be R2, for the next <M> the label is R3, and so on.)

The attention mask structure used in DFlash's bidirectional drafting. The target model provides context features (pink, left side) that condition the draft model. The input consists of clean prompt tokens p and clean response tokens r. Within each masked block, a subset of clean response tokens (dark green) is randomly sampled as anchors, while mark tokens m (light green) mark positions for parallel prediction. Invisible tokens (gray) denote the attention mask, which enforces causal consistency and prevents inter-block information leakage during training. (The diagram shows three anchors positioned one after the other. For the masked token <M> right after R1, the label is set to be R2, for the next <M> the label is R3, and so on.)If you want to learn more about the Baseten Speculation Engine or use it for your own workloads, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers!
