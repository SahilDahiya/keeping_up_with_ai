---
title: 'TEAL: Training-Free Activation Sparsity in Large Language Models'
topic: inference
subtopic: optimization
secondary_topics:
- models/reasoning
summary: Explains TEAL, a training-free activation sparsity method for large language
  models.
source: together
url: https://www.together.ai/blog/teal-training-free-activation-sparsity-in-large-language-models
author: James Liu; Pragaash Ponnusamy; Tianle Cai; Han Guo; Yoon Kim; Ben Athiwaratkun
published: '2024-08-28'
fetched: '2026-07-11T04:25:59Z'
classifier: codex
taxonomy_rev: 1
words: 969
content_sha256: 00ae3bb1af6aa784529c7ea5f2a98b36e1dbc52e6a9a3f019459c6c66ba7550b
triage: keep
skip_reason: null
---

# TEAL: Training-Free Activation Sparsity in Large Language Models

We present TEAL (**T**raining-Fre**e A**ctivation Sparsity in **L**LMs), a simple training-free approach to activation sparsity that applies magnitude pruning to hidden states throughout the model. In particular, TEAL achieves **40-50%** model-wide activation sparsity with minimal degradation, allowing us to transfer less weights to on-chip memory. Because LLM inference is ** memory-bound**, we can translate this into

**1.53-1.8x**wall-clock speedups in single-batch decoding!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7d3_66cf7117d79f2b17ae3facbf_66cf6fbea3375f1f5c2d4e5e_image%252520(1).png)

## Background

Large Language Models (LLMs) are very large, which leads to many challenges in inference. LLM Inference is unique in that it is memory bound: it’s bottlenecked by the speed at which the parameters can be moved from device memory to registers. As such, a variety of subfields have emerged that address this **memory wall,** including quantization, weight sparsity, speculative decoding, etc.


Activation sparsity is a less studied method that leverages zero values in the hidden states of LLMs. Weight channels associated with zero-valued activations are unnecessary during decoding, and we can thus achieve speedup by avoiding the transfer of such channels to on-chip memory.


Older models such as [OPT-175B](https://arxiv.org/abs/2205.01068) are very conducive to activation sparsity. In fact, [past work](https://arxiv.org/abs/2210.06313) finds that the intermediate states of ReLU-based MLPs (in Transformers) exhibit extreme emergent sparsity (around 95%!). This largely enables [DejaVu](https://arxiv.org/abs/2310.17157) to realize a 2x wall-clock speedup. However, newer models (including LLaMA) have moved away from ReLU-based MLPs and towards variants like [SwiGLU](https://arxiv.org/abs/2002.05202), due to empirically better performance of the latter. As such, the intermediate states are no longer naturally sparse, making it more difficult to apply methods like DejaVu. Recent work has found that replacing SiLU with ReLU in the MLP blocks and performing continued pretraining can “recover” models that exhibit activation sparsity (thus making older methods applicable) ([ReLUfication](https://openreview.net/forum?id=osoWxY8q2E), [ProSparse](https://arxiv.org/abs/2402.13516), [TurboSparse](https://arxiv.org/abs/2406.05955)), but they require training on up to hundreds of billions of tokens. 


Most recently, [CATS](https://arxiv.org/abs/2404.08763) realizes *training-free activation sparsity* on SwiGLU based LLMs, and impressively achieves up to 50% sparsity in $\textbf{W}_\text{up}$ and $\textbf{W}_\text{down}$ for Mistral and Llama-2-7B without fine-tuning. However, other tensors (including $\textbf{W}_\text{gate}$ and $\textbf{W}_\text{q,k,v,o}$) are computed without sparsification, resulting in lower model-wide sparsity (roughly 25%). 


A cheap and accessible approach for activation sparsity would be valuable. However, existing methods face limitations that inhibit widespread adoption. Some approaches require extensive continued pretraining on up to hundreds of billions of tokens. Other training-free approaches achieve impressive activation sparsity in certain areas of the model but do not achieve enough model-wide sparsity. TEAL aims to bridge this gap.


## Motivating Study: Distributional Properties of Activations in LLMs

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7ca_66cf7117d79f2b17ae3facd7_66cf7047dd49e760b29eb60a_image4.png)

Past work finds that hidden states in LLMs exhibit outliers ([SmoothQuant](https://arxiv.org/abs/2211.10438), [LLM.int8()](https://arxiv.org/abs/2208.07339)). We additionally find that they are zero-centered and exhibit similar *distributional shapes* across layers. In particular, those before MLP and Attention Blocks are Gaussian shaped, and those in the intermediate of such blocks are Laplacian shaped. We don’t have a strong explanation as to why this occurs, but we do leave a few theories in our paper. In particular, [multiplying a Gaussian Matrix with a Gaussian Vector](https://arxiv.org/abs/1702.02815) results in a Laplacian-like distribution, which may be related. Nevertheless, as both distributions are densely concentrated near and around zero, we should potentially be able to prune out many low-magnitude activations with negligible model degradation (footnote: [CATS](https://arxiv.org/abs/2404.08763) makes a similar observation with respect to the output of $\text{SiLU}(\textbf{x}\textbf{W}_\text{gate}^\top)$). To that end, we define our sparsification function as follows:

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7d7_66cf7117d79f2b17ae3facc5_66cf706789b2287763509cae_image5.png)

## TEAL

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7da_66cf7117d79f2b17ae3facb4_66cf7097454a6cc98aa0ab0a_image6.png)

As it turns out, we actually can! In our paper, we introduce another small optimization – optimizing sparsity levels for each tensor at the transformer block level. TEAL sparsifies every tensor in the model, showcasing near-zero degradation at 25%, and minimal degradation at 40% sparsity. At 50% sparsity, Llama-3 variants show slightly more degradation compared to older Llama-2 and Mistral variants which are still fairly performant.


Most notably, TEAL outperforms CATS due to two reasons. First, and most importantly, our ability to sparsify every tensor. Second, our design choice to sparsify $\mathbf{W}_\text{up}$ through input $\mathbf{x}$ yields lower error than CATS’ choice to sparsify through gated output $\text{SiLU}(\mathbf{x}\mathbf{W}_\text{gate}^\top)$, which we further analyze in the paper.


## Hardware-Aware Speed-up


We make a few improvements targeting overhead in the sparse kernel introduced by [DejaVu](https://arxiv.org/abs/2310.17157), which we also discuss in the paper. To benchmark real world speedup, we integrate TEAL with [GPT-Fast](https://github.com/pytorch-labs/gpt-fast), and enable \texttt{torch.compile} with CUDA Graphs. As shown below, TEAL achieves significant speed-ups of up to **1.53x** and **1.8x** at 40% and 50% sparsity respectively. We note that on A100, our kernel is faster than \texttt{torch.matmul} (cuBLAS) at 0% sparsity, but is slower than the GEMV kernel generated by \texttt{torch.compile}. Evidently, there still may be room for further kernel optimization!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7cd_66cf7117d79f2b17ae3facb7_66cf70c69c7d0bc28097dfe2_image3.png)

## Compatibility with Quantization

Finally, we demonstrate compatibility with quantization, which is another promising direction for efficient LLM inference. We consider 8-bit channel-wise RTN, 4-bit [AWQ](https://arxiv.org/abs/2306.00978), and 2/3-bit

[QuIP#](https://arxiv.org/abs/2402.04396). The point of sharp perplexity degradation is similar across bit-widths, suggesting that errors from activation sparsity and quantization compound somewhat independently. Combining these techniques unlocks new regimes with respect to memory transferred to GPU registers, allowing for higher inference speed-up. This requires developing specialized sparse + quantized kernels, which we leave for future work.

![Two graphs showing Llama-2-7B perplexity versus sparsity and normalized performance by bitwidth.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1ee25f9d6a956cd7d0_66cf7117d79f2b17ae3facc2_66cf70dc6512a2e64a921b24_image2.png)

## Applications

The most immediate application of TEAL is accelerating inference in resource constrained edge settings. These settings are typically single batch, which is where TEAL realizes the most salient speed-up. We find that TEAL is performant at low batch sizes greater than 1 (albeit with less sparsity), but does not scale as well to higher batch sizes.


TEAL can also help inference providers! Together AI hosts over 100 leading open-source models across a large fleet of GPUs. There are often times where the active batch size across models is fairly low on any given instance and with improvements like TEAL, we are able to serve models more efficiently in this regime.
