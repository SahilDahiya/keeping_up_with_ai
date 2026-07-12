---
title: ThunderKittens Now Optimized for NVIDIA Blackwell GPUs
topic: inference
subtopic: hardware
secondary_topics:
- inference/optimization
summary: Describes ThunderKittens optimizations for NVIDIA Blackwell GPUs.
source: together
url: https://www.together.ai/blog/thunderkittens-nvidia-blackwell-gpus
author: Benjamin Spector; Aaryan Singhal; Dan Fu; Chris Ré
published: '2025-03-15'
fetched: '2026-07-11T04:26:05Z'
classifier: codex
taxonomy_rev: 1
words: 1652
content_sha256: a1cd197236dc14185d9bd8df51ee6656ab15cb2f045f75956f32e33b679bdcd3
triage: keep
skip_reason: null
---

# ThunderKittens Now Optimized for NVIDIA Blackwell GPUs

*At Together AI, we have been investing in the ThunderKittens framework - a software library that we developed in collaboration with researchers at Stanford to make it easier to quickly write performant GPU kernels. Today, we're open-sourcing some kernels written for NVIDIA Blackwell architecture. Our customers can use these on **Together GPU Clusters** today, and they're coming soon to the **Together Kernel Collection**.*

*This blog is cross-posted to the **Hazy Research blog** at Stanford University.*

We've been having fun playing around with some NVIDIA Blackwell GPUs with our collaborators at Together AI over the past few weeks and reading about all the exciting new features. The cool thing is – turns out the new features, from 5th-generation tensor cores, to Tensor Memory and CTA pairs, fit pretty well into TK's existing tile-based abstractions. It's all about dataflow!

Today, we're releasing a few new kernels for the NVIDIA Blackwell architecture, written in ThunderKittens:

- BF16 and FP8 ThunderKittens GEMM kernels – running at or near cuBLAS speeds, and up to 2x faster than cuBLAS GEMMs on H100.
- Attention forwards and backwards – both running at near-cuDNN speeds on [B200](https://www.together.ai/nvidia-hgx-b200), and up to 2x faster than FA3 on H100.

You can now try out the [new GEMM kernels](https://github.com/HazyResearch/ThunderKittens/tree/blackwell/kernels/matmul) and the [attention fwd/bwd kernels](https://github.com/HazyResearch/ThunderKittens/blob/blackwell/kernels/attn/b200/b200.cu)).

In the remainder of this blog, we're going to take a deep dive into how we use the new hardware features for these kernels, as well as how we adapt kernels written for the NVIDIA Hopper architecture to the new NVIDIA Blackwell architecture. By the end of this blog, you'll learn all about these new features and how they make attention go vroom!

## It's All About the Dataflow

In our experience, writing performant kernels on NVIDIA Blackwell GPUs feels a lot more like programming a dataflow-machine than writing traditional (circa ~2022) CUDA kernels. It's all about loading in enough data at a high enough throughput to keep the tensor cores hot. In the H100, the main mechanism for doing this was using warp-specialized TMA loads to asynchronously fetch data while the tensor cores are doing their computation (e.g., in attention, you asynchronously load the next tiles of K and V while computing the current QK^T tiles and online softmax).

On the B200, this is even more important – the tensor cores now have 2–2.5x the power of those on the H100. And to fully utilize all that compute, we need to be loading in a lot more data all at once. Luckily, the new hardware features make it easier to build deeper pipelines on B200.

#### Matrix Multiplication

Of all of the kernels one can run, a matrix multiply kernel has the *least* excuse for bubbles in the data pipeline. It turns out with a little bit of care, one can eliminate just about all of them!

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1e25cdbcb766933c6e_67d46755439d45486c7423f2_01_tensor_pipe_sampling.png)

*Top: TK's Tensor Pipe PM Sampling – almost no bubbles!*

Bottom: cuBLAS Tensor Pipe PM Sampling for reference.

Bottom: cuBLAS Tensor Pipe PM Sampling for reference.

Our new matrix multiplication kernel has a few tricks up its sleeve that are different from the NVIDIA Hopper architecture:

- We launch threadblock clusters to take advantage of the CTA pair mechanism (more on that later) – this increases reuse and reduces bandwidth requirements on shared memory.
- We reserve two producer warps to launch the matrix multiplies for each consumer warpgroup. Consumers no longer launch their own matrix multiplies!
- MMA instructions directly signal to the producer load warps that pipeline stages are freed and ready to be filled.
- Producers signal consumers that output accumulators are finished and ready.
- Consumers pipeline output accumulators into registers, into shared memory, and then out into HBM. - We even serialize the consumer warpgroups and force one to load tensor memory into registers and signal the producers before the other can load its tensor memory, so that these loads are pipelined, too.

- We adopt a persistent kernel, so that we can pipeline the next inputs while the previous outputs are being written out. - In fact, we can even launch the next matrix multiply accumulate block while the previous is still in tensor memory.


The end result is that there is only one bubble in the whole tensor pipeline: when the first consumer warpgroup reads its output accumulator into registers. We think this takes about 140 ns every few hundred microseconds; the rest is all tensor cores.

#### Attention

One important optimization turns out to be launching the AV MMA's from the previous iteration of the attention loop while starting the QK MMA of the iteration, and loading the K and V tiles of the next iteration. In pseudocode, this looks like:

```

```
```
        // Producer warpgroup
        if (warpgroup::is_producer()) {
          if (warpgroup::warpid() == 0) {
            // do QK.T matmul
          }
          if (warpgroup::warpid() == 1) {
            // do AV matmul
          }
          if (warpgroup::warpid() == 2) {
            // load next K
          }
          if (warpgroup::warpid() == 3) {
            // load next V
          }
        }
        // Consumer warpgroups
        else {
          // Do O online softmax while signaling next AV
        }

```
Below, we'll go into each of these new features in more detail.

### Fifth-Generation Tensor Cores

A major new feature of the [B200](https://www.together.ai/nvidia-hgx-b200) is the larger, faster tensor cores. These run around ~2–2.5x faster than the tensor cores in the H100, and they're a major source of speedups on the new generation of hardware.

For review: tensor cores are on-chip compute units that compute large GEMMs: the computation $D = A @ B + D$, where $A$, $B$, and $D$ are all matrices. In this blog, we'll use an $M \times N \times K$ notation for GEMMs, meaning that $A$ has shape $M \times K$, $B$ has shape $K \times N$, and $D$ has shape $M \times N$.

The B200 tensor cores aren't just faster than the H100 tensor cores – they're also much larger. From our microbenchmarking, they seem to behave like $128 \times 128$ systolics. That means – in order to get the full FLOP utilization out of the tensor cores, you want $M$ and $N$ to be 128 (or larger multiples of 128). Smaller values of $M$ and $N$ run at the corresponding fraction of 128; e.g., a $64 \times 64 \times 64$ GEMM will run at one-quarter the FLOP rate of a $128 \times 128 \times 64$ GEMM. This is a bit of a departure from the H100, where smaller GEMM shapes were enough to max out the tensor cores.

In ThunderKittens, the new operations are nicely abstracted:

```

```
```
        using namespace kittens;
        tt d; // 128 x 128 FP32 tensor memory tile
        __shared__ st_bf<128, 64> a, b; // 128 x 64 BF16 shared tile
        __shared__ semaphore sem; // semaphore (mbarrier)
        // init...
        mma(d, a, b, sem); // do it

```
### Tensor Memory

There's also a new layer of the memory hierarchy: tensor memory, a set of registers specifically allocated for tensor core instructions. This is nice for kernels because it gives us an extra 256KB of register memory to play with, in addition to the 256KB we had already, and up to 227KB of shared memory.

This is especially useful for building more complex dataflow pipelines, which are always trading off the degree of preloading we can accomplish, vs. how much SRAM is available on each SM. Tensor memory gives us more room to work!

In the TK attention kernel, we make extensive use of tensor memory, especially during the backwards pass (which has a higher footprint due to the need to store gradient values):

```

```
```
    // The tensor memory used by a warpgroup in attention backwards.
    struct wg_tmem_t {
        tt &kg;
        tt &vg;
        tt  &sb;
        tt  &dp;
        tt  &pb_bf;
        tt  &dp_bf;
        semaphore *mma_sem;
    };

```
### CTA Pairs

There's another nice set of abstractions that allows for deeper coordination between different CUDA thread blocks – CTA pairs.

Brief review: NVIDIA's CUDA programming model has a notion of "thread blocks" – sets of threads that work together to execute a kernel. In classic (pre-2022) CUDA, thread blocks executed independently; but starting with the NVIDIA Hopper architecture, thread blocks in the same "cluster" were able to start to coordinate with each other. CTA pairs are deeply related to these notions – CTA stands for "Cooperative Thread Array," the PTX implementation of a thread block.

The NVIDIA Blackwell platform introduces the notion of CTA pairs – two CTAs operating within the same cluster, scheduled on the same SM. Two CTAs can coordinate to execute tensor core instructions, accessing the Tensor Memory of both of the CTAs within the CTA pair. The [NVIDIA PTX guide](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-cta-pair) has more details for those interested.

You've actually already seen the ThunderKittens abstraction for CTA pairs in this very blog post! If the `ncta` variable in the `mma` template is set to `2`, we can have two CTAs on a single SM coordinate to do a larger GEMM:

```

```
```
        using namespace kittens;
        template
        __device__ static inline void mma(D &d, const A &a, const B &b, semaphore &sem);

```
## Conclusion

We hope you enjoyed this whirlwind of new features and how you can use them to write blazing fast attention kernels!

Check out our kernels and read more about ThunderKittens below!

If you'd like to learn more about these kernels or work with us on developing the next set of updates, please reach out to Ben or Dan!

- Ben: <[bfs@stanford.edu](mailto:bfs@stanford.edu)>
- Dan: <[danfu@together.ai](mailto:danfu@together.ai)>

And thanks again to Together AI for collaborating with us and helping us get running with NVIDIA B200's to write these kernels!

Finally, if you'd like to learn how to build kernels like this and contribute to the cutting edge, please [apply to work with](https://job-boards.greenhouse.io/togetherai/jobs/4188119007) us on the kernels team at Together AI. We are looking for talented folks who are passionate about performance and eager to learn. Come build with us!

Watch this space for more updates soon!
