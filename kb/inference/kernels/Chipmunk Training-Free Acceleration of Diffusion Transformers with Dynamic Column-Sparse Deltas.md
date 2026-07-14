---
title: 'Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic
  Column-Sparse Deltas'
topic: inference
subtopic: kernels
secondary_topics:
- models/multimodal
summary: Describes Chipmunk, a training-free acceleration method for diffusion transformers.
source: together
url: https://www.together.ai/blog/chipmunk
author: Austin Silveria; Soham Govande; Dan Fu
published: '2025-04-21'
fetched: '2026-07-11T04:22:43Z'
classifier: codex
taxonomy_rev: 1
words: 1488
content_sha256: ca16b30839ef088f58edd08296d679d438d6a5ee0c4b5791e733a157a73388bf
triage: keep
skip_reason: null
---

# Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas

**TL;DR: **We present Chipmunk, a training-free method to accelerate diffusion transformers with hardware-aware dynamic sparsity.  Chipmunk caches attention weights and MLP activations from previous steps and dynamically computes a sparse “*delta*” against the cached weights. Chipmunk achieves up to 3.7x faster video generation on HunyuanVideo at 720x1280 resolution for a 5s video, and 1.6x faster image generations on FLUX.1-dev at 1280x768 resolution.

This blog is cross-posted to the [Sandy Research](https://sandyresearch.github.io/chipmunk-part-I/) blog at UCSD. Check out [Part II](https://sandyresearch.github.io/chipmunk-part-II/) and [Part III](https://sandyresearch.github.io/chipmunk-part-III/) on the Sandy Research blog for a deeper dive into the sparsity patterns and the kernels behind Chipmunk!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b14795f_68061f8ff87eb9a4b5020814_blog-1-comparison.jpeg)

*Images of cute chipmunks can be generated 1.37x faster! Left: Fully Dense FLUX.1-dev. Right: Ours (84% sparse attention and 70% sparse MLP)*

**Motivation: **Diffusion Transformers (DiTs) have become the standard for video generation, but the time and cost of generation keeps them out of reach of many applications. We raise two questions: (1) What do the model activations want to do? (2) What does the hardware want to do? We then use these insights to design hardware-friendly algorithms that maximize quality per unit of generation time.

In this post, we unpack:

- **Slow-Changing, Sparse Activations:**DiT activations for MLP and attention change slowly across steps, and they are naturally sparse.
- **Cross-Step Deltas:**Because of the slow changing activations and natural sparsity, reformulating them to compute cross-step deltas make them even sparser.
- **Hardware-Aware Sparsity Pattern:**For both attention and MLP, we can pack dense shared memory tiles from non-contiguous columns in global memory. We open-source fast kernels for this!

But first, a preview of our results:

* 93% sparsity on 44 out of 50 steps for an average of 82% sparsity.

These FLUX.1-dev numbers were evaluated on 1280x768 images, and we’ve found that if we increase image size to 2304x1280, we can get speedups of up to 1.65x per-image without stacking on top of step caching methods, and 1.9x with step caching! We’ve also found that we can sparsify FP8 Flux to get a 1.1x end-to-end speedup over the fastest open-source implementation.

### Slow-Changing, Sparse Activations

Chipmunk exploits two simple observations about diffusion transformers:

- **Activations move slowly:**In each step a Diffusion Transformer (DiT) denoises a latent noise vector. This noise vector changes slowly across successive steps in the diffusion process – and so do the- [per-layer](https://arxiv.org/abs/2411.02397)- [activations](https://arxiv.org/abs/2410.05317).
- **Activations are sparse:**In attention, it is common to see queries place a very large percentage of their attention probability mass on a small subset of keys–this means that the output will mostly be made up of the small subset of associated rows of $V$. And in MLP, previous works have observed significant sparsity in the intermediate activations of both- [ReLU](https://arxiv.org/abs/2210.06313)and- [GeLU](https://arxiv.org/abs/2408.14690)-based layers, meaning that the output will mostly be made up of the top activated rows of $W_2$.

### Activation Deltas Across Diffusion Steps are *Very *Sparse

Chipmunk uses these two observations to reduce the compute costs of the diffusion model – we can effectively capture nearly all the cross-step changes in the activations by *only* recomputing a small subset of attention and MLP. 

What does this mean, concretely? Let’s revisit the attention and MLP equations:

- **Attention:**$\text{softmax}(Q @ K^T) @ V)$
- **MLP:**$\text{gelu}(x @ W_1) @ W_2)$

Both operations use a non-linearity to compute the scalar coefficients for a linear combination of value vectors. In attention, the value vectors are dynamic ($V$ is projected from the current token representation). In MLP, the value vectors are static (rows of the weights $W_2$). Thus, in attention, our outputs are a sum of scaled rows in the V matrix, and in MLP, our outputs are a sum of scaled rows in the $W_2$ matrix (the bias is one extra static vector). We can visualize these individual vectors as being summed to produce the total operation output.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b147957_68061ffe0a6d7f4438e3cd31_blog-3-sum.png)

Chipmunk’s key insight is that the value vectors (the colored columns of **v** above) change slowly, as do the scalar weights themselves (the colored values in the attention matrix above). Chipmunk caches the value vectors and the scalar weights, and dynamically chooses which ones to recompute in each step:

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b147962_6806200b5160f80332a981ce_blog-4-cache.png)

Given an attention/MLP output cache, an equivalent definition of a normal dense forward pass on step $n$ is the following: Subtract all of step $n-1$’s output vectors from the cache, and add all of step $n$’s new vectors. Therefore, given the natural sparsity in intermediate matrices, we can reformulate attention and MLP to compute a *delta* based on the previous step’s outputs. That is, we *replace* a subset of the output vectors and reuse the rest from the previous step. The output vectors that we replace correspond to sparsifying keys/values at the granularity of a single token in the intermediate matrix.

### Hardware-Efficient Sparsity Pattern

The sparsity pattern we’ve been describing thus far, recomputing individual scaled output vectors for each token, corresponds to [1, 1] unstructured sparsity on the intermediate activations. GPUs do not like this. What they do like is computing large blocks at once, in the size ballpark of [128, 256] (in the current generation). This corresponds to 128 contiguous tokens and 256 contiguous keys/values.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b147952_680622b0ee121413812d8b3f_blog-5-tiles-framed.png)

Computing with block sparsity that aligns with the native tile sizes of the kernel is essentially free because the GPU is using the same large matrix multiplication sizes and skips full blocks of work.

However, there is one optimization we can make to efficiently get to [128, 1] column sparsity. Looking at our matrix multiplication diagram, let’s think through what happens if we reorder the columns of $k^t$ and** **$v^t$. A reordering of $k^t$ will apply the same reordering to the columns of $A = q @ k^t$. And if we apply the same reordering to $v^t$, then the end result $o$** **is actually the same because the columns of $A$ still align with the correct columns of $v^t$**.**

What this allows us to do is compute attention or MLP with any ordering of the keys/values in shared memory–thus we can pack our sparse keys/values from non-contiguous rows in global memory into a [dense tile in shared memory](https://arxiv.org/abs/2301.10936).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b14795a_680622b9e7307f5af1991f2c_blog-6-sram-framed.png)

The more granular loads incur a small performance penalty, but we find that the sparsity levels make up for this–e.g. at 93% sparsity, our column-sparse attention kernel in [ThunderKittens](https://github.com/HazyResearch/ThunderKittens) is ~10x times faster than the dense baseline.

Ok, so now we’re working with [128, 1] column sparsity, which corresponds to 128 contiguous tokens recomputing the same set of individual output vectors across steps. Intuitively, we expect that small 2D *patches* of an image have similar color and brightness. And in video, we expect the same for small 3D cubes (*voxels*). Yet, the natural token order is *raster order* from left to right, top down, and frame zero onwards. To create 128-size chunks with the most similar tokens, we **reorder** the tokens (and RoPe embeddings) once at the beginning of the diffusion process such that a **chunk** in the flattened sequence corresponds to a **patch/voxel**. These similar tokens, which we expect to interact with similar keys/values, now share the same set of sparse indices because they occupy contiguous rows of the input matrix. At the end of the diffusion process, we then reverse this reordering before decoding to pixel space.

### Kernel Optimizations

Our kernel optimizations achieve efficient dynamic sparsity and caching through:

- **Fast sparsity identification**: We fuse custom kernels to quickly compute sparse indices by reusing softmax constants and implementing a fast approximate top-k CUDA kernel with shared memory atomics, which is ≥2x faster than PyTorch’s native implementations
- **Fast cache writeback**: We use the CUDA driver API to overlap the cache writeback with subsequent GEMM computations by allocating leftover streaming multiprocessors (SMs) to custom TMA-based reduction kernels (with PTX instructions like cp.reduce.async.bulk) during the tail effects of wave quantization, achieving a 2x speedup over naive implementations and saving ~20 microseconds per MLP invocation.
- **Warp-Specialized Persistent Kernel:**We let the producer warpgroup’s memory loads overlap with consumer epilogues (which are expensive because of all the caching computation), and store swizzle offsets in registers, minimizing address computation overhead when using granular cp.async loads instead of TMA.

### Come and play with Chipmunks!

The only thing we love more than chipmunks is the open-source community! Check out our [GitHub repository](https://github.com/sandyresearch/chipmunk) and make your image and video models go brrrr. This post was just a sneak peek—we’re also releasing [in-depth technical blogs](https://sandyresearch.github.io) on a deep dive through the math and kernel optimizations.

![Cartoon ninja dog and happy orange cat with a laptop on a computer chip.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afd2ba823e87b147967_680622ce891a21be668c2716_blog-7-kittens-framed.jpeg)

*We’re big fans of ThunderKittens, and so are our chipmunks! Our sparse attention and MLP kernels let our chipmunks play nicely with their kitten friends.*

At Together AI, we’re constantly pushing the state of the art in model acceleration to serve the fastest models at the lowest cost: [FLUX-1.dev](https://www.together.ai/models/flux-1-dev), [DeepSeek R1](https://www.together.ai/models/deepseek-r1), [Llama 4](https://www.together.ai/models/llama-4-maverick). We’re excited to continue our research to extend granular sparsity across more model architectures and integrate with training algorithms for even more acceleration.
