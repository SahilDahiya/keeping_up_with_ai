---
title: How to train custom EAGLE-3 heads for speculative decoding
topic: models
subtopic: fine-tuning
secondary_topics:
- inference/optimization
summary: Explains training custom EAGLE-3 heads for speculative decoding acceleration.
source: baseten
url: https://www.baseten.co/blog/how-to-train-custom-eagle-3-heads-for-speculative-decoding/
author: Model Performance Team
published: '2026-04-13'
fetched: '2026-07-11T04:05:41Z'
classifier: codex
taxonomy_rev: 1
words: 1405
content_sha256: 130f2f260f74eb7ef03165d2196ffb068e0e916e7bd4ec7afda649310e812165
triage: keep
skip_reason: null
---

# How to train custom EAGLE-3 heads for speculative decoding

![eagle 3](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775838266-eagle-3-blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Speculative decoding has emerged as one of the most effective techniques for reducing LLM inference latency without sacrificing output quality. Among the approaches available today, EAGLE-3 is used commonly for its balance of simplicity, performance, and flexibility.

In this post, we walk through everything you need to know to train custom EAGLE-3 heads, including dataset preparation to hyperparameter tuning to deployment. At Baseten, we’ve found **1.5-2.5x latency improvements** on models trained with EAGLE heads. The target model used was a Qwen3-4B.

## What is EAGLE-3?

[EAGLE-3](https://arxiv.org/abs/2503.01840) is a speculative decoding method for autoregressive LLM inference. The core idea is that you attach a small, lightweight "draft head" to your target model that predicts multiple future tokens at once. The target model then verifies those predictions in a single forward pass. When the draft head is accurate, you skip multiple decoding steps, which dramatically reduces end-to-end latency.

![eagle](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775838553-screenshot-2026-04-10-at-12-13-37-pm.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

While EAGLE papers report up to 4–6x speedups in benchmarks, some of that gain comes from differences in serving frameworks rather than the draft head alone. In production, we typically observe **1.5–2.5x latency improvements** attributable to the EAGLE head itself.

A few key properties make EAGLE-3 practical:

- **Latency improvement without quality loss:**verified tokens are identical to what the target model would have generated.
- **Memory-bound workloads benefit most:**if your inference is bottlenecked by memory bandwidth (common for long-context or single-batch serving), EAGLE heads can cut latency significantly.
- **Lightweight training:**the draft head is just a single transformer decoder layer, typically only 1–5% of the target model's parameters, so training is fast and resource-efficient.

## When EAGLE helps

EAGLE works best when your workload is latency-sensitive but not heavily batched. It's especially effective when users care about end-to-end response time more than time to first token (TTFT), such as:

- **Code generation**, where the full output must be complete before it can be compiled or executed
- **Agentic workflows**, where downstream tool calls or reasoning steps block on the model's full response
- **Structured output (JSON, function calls)**, where partial tokens aren't useful until the entire response is valid
- **Real-time conversational assistants**, where perceived responsiveness depends on total reply time

## EAGLE concepts and parameters

Before diving into the training workflow, it helps to understand what you can adjust:

### TTT-length (test time training length)

This controls how many tokens the EAGLE head generates *using its own prior predictions as context* during training. Higher values improve training stability because the head learns to recover from its own mistakes.

- **Recommended:**7–9
- Setting this too low can cause the head to be brittle at inference time when it encounters its own (imperfect) draft tokens as input.

### Number of draft tokens

The number of tokens the head proposes during inference before the target model verifies. More draft tokens means more potential speedup per step, but also a higher chance of a mismatch (and wasted compute on incorrect predictions).

- **Recommended:**3–4 at inference time
- Going higher (e.g., 8) rarely helps because prediction accuracy drops off and verification cost grows.

### Learning rate (LR)

Scaling the learning rate with model size is important. Larger models have more parameters and are more sensitive to large gradient updates, so they need smaller learning rates to train stably.

We use AdamW as the optimizer across all model sizes; it handles weight decay well and is the standard choice for transformer training. The key variable is the learning rate itself:

**Model sizeRecommended LR**Small (~3–7B)1e-4Medium (~7–20B)5e-5Large (20B+)2e-5

### Sampling parameters

EAGLE heads perform best under greedy decoding (`temperature=0`). Non-greedy sampling (`temperature>0`), repetition penalties, and top-p/top-k all reduce draft token acceptance rates. The EAGLE paper reports roughly a **15–25% reduction in speedup** at `temperature=1` vs. `temperature=0`.

Output quality remains lossless regardless; it's the speedup that degrades, not correctness. Some serving frameworks disable sampling entirely during speculative decoding, while others (e.g., TRT-LLM) require an explicit flag to allow it.

For a deeper dive, see [Temperature-Centric Investigation of Speculative Decoding](https://arxiv.org/abs/2410.10141).

## Dataset preparation

Dataset quality is the most important factor in EAGLE head training. **The EAGLE head must learn the token distribution of the target model**, not just any generic text distribution.

EAGLE heads need large datasets to train effectively.

**Task typeSmall models (~20B or less)Large models**Generic (conversations, creative writing)200k–300k samples~500k samplesSpecialized (structured output, JSON, specific formats)~100k samples~100k samples

Aim for **1k–2k total tokens per sample** (prompt + completion combined). More data is always better if time permits, but we’ve found these to be solid baselines.

### The golden rule: regenerate outputs with the target model

This is the single most important step. The EAGLE head must predict tokens *as the target model would generate them*. If you train on outputs from a different model (or from human-written text), the draft head's distribution will be misaligned with the target model and acceptance rates will suffer.

**For general-purpose heads**, take an existing instruction dataset and **regenerate the outputs** by running your target model over the prompts. For example, you can start from a dataset like [UltraChat-200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) and regenerate all completions using your target model.

**For task-specific heads**, collect prompt–output pairs from your actual production traffic or a representative sample, then regenerate the outputs with the target model.

## Training workflow

Here's the end-to-end workflow for training an EAGLE-3 head.

### Step 1: Environment setup

Download and set up your preferred EAGLE training framework — [https://github.com/NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer), [https://github.com/sgl-project/SpecForge](https://github.com/sgl-project/SpecForge), and [https://github.com/torchspec-project/TorchSpec](https://github.com/torchspec-project/TorchSpec) all work fine.

### Step 2: Prepare your data

If you have pre-prepared prompt/output pairs:

- Apply the correct chat template to your prompts
- Upload the formatted dataset to Hugging Face

If you're regenerating from scratch:

- Run the dataset generation script against your target model
- The regenerated dataset will be saved to Hugging Face automatically

### Step 3: Launch training

A minimal training launch looks like configuring a run script with:

- Target model Hugging Face path
- Dataset Hugging Face path
- TTT-length (7–9)
- Learning rate (see table above)
- Batch size and max sequence length
- Number of epochs

### Step 4: Monitor training

Watch for these signals during training:

- **Loss curve**should decrease steeply then plateau- Expected shape: a sharp drop in the first 10–20% of steps, then a slow taper to a stable plateau.


![loss](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775839642-loss.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

- **Accuracy**should climb steeply and stabilize at- **70–80%**

![accuracy](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775839692-accuracy.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

- **Make sure to verify your data is correctly formatted**. Incorrectly formatted data (wrong chat template, prompt leaking into output, etc.) is the most common source of poor results.

<aside> 💡

**Pro tip:** If training is not converging, the two most common fixes are: (1) increase TTT-length to 7–9, and (2) adjust the learning rate. Also double-check that the training samples are correct.

</aside>

## Evaluation

Before deploying, benchmark your head against the baseline — that is, run examples with and without the EAGLE head attached to the model.

Compare latency and throughput between the two. A well-trained head should show **1.5–2.5x latency improvement** on memory-bound workloads.

## Deployment

Trained EAGLE heads are saved to Hugging Face and can be referenced by any serving framework that supports EAGLE-3 speculative decoding.

Reference the EAGLE head's Hugging Face path in your serving configuration, and the serving framework handles the rest: loading the head, running draft generation, and performing verification.

## Debugging common issues

### Training won't converge

- Increase TTT-length to 7–9
- Check learning rate against model size recommendations
- Verify data formatting by inspecting the CLI output at training start
- Ensure you're training on data - *from the target model's distribution*

### Low acceptance rate at inference

- Reduce - `num_draft_tokens`to 3–4
- Verify that inference input format matches training format exactly
- Check that the chat template applied at inference matches what was used during training

## Conclusion

Training custom EAGLE-3 heads is a high-leverage optimization for any team serving LLMs in latency-sensitive settings. The process is straightforward: prepare a representative dataset with regenerated outputs, configure a handful of hyperparameters, and train a lightweight head. But getting the data distribution right, matching chat templates, and tuning TTT-length make the difference between a head that provides meaningful speedup and one that doesn't.

The result is a **1.5–2.5x latency improvement** with zero degradation in output quality, a rare combination in the inference optimization space. Get started training custom EAGLE heads on [Baseten Training](https://docs.baseten.co/training/overview). In Part 2, we’ll talk more about other SpecDec methods like [DFlash](https://arxiv.org/html/2602.06036v1) and how to scale EAGLE training to achieve even lower latency.
