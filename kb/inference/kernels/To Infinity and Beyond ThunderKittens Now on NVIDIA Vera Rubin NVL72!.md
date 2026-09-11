---
title: 'To Infinity and Beyond: ThunderKittens Now on NVIDIA Vera Rubin NVL72!'
kind: blog
topic: inference
subtopic: kernels
secondary_topics: []
summary: Together's kernels team ports ThunderKittens NVFP4/FP8 GEMM kernels to NVIDIA
  Vera Rubin NVL72, exploiting the doubled-K tensor-core step and expanded 576-column
  tensor memory to push past the ~42-44% of roofline achieved by naively reusing Blackwell
  kernels, reaching over 22 PFLOPS and competitive with cuBLAS and CuTe DSL.
triage: null
skip_reason: null
source: together
url: https://www.together.ai/blog/to-infinity-and-beyond-thunderkittens-now-on-nvidia-vera-rubin-nvl72
author: Dylan Lim; Xinyi Li; Sonny Li; Peter Wu; Dan Fu; Simran Arora
published: '2026-09-10'
fetched: '2026-09-11T06:11:35Z'
classifier: claude
taxonomy_rev: 2
words: 2204
content_sha256: 139a412ef4ed5a44bc5568f3c69376128f1db8258cd45142befa10c80c4bd683
---

# To Infinity and Beyond: ThunderKittens Now on NVIDIA Vera Rubin NVL72!

The kernels team at Together recently received access to the NVIDIA Vera Rubin NVL72 platform. We spent the past few days digging through the new ISA and poking the chip with micros. There are many fun new features! We finished adding some functionality into ThunderKittens to write NVFP4 and FP8 GEMMs on Vera Rubin, as well as help fellow kittens explore the stars.

![Illustration of three cartoon robot kittens with a telescope and glowing globe at “Vera Rubin Observatory,” a cat-shaped constellation above.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2b2ce17414168eba66494_6aa2b1b2428f651aef624504_tk-img-01.webp)

Before diving into what Vera Rubin delivers, we start our journey with a quick refresher of a Blackwell GPU GEMM.

## Starting Point: An NVIDIA HGX B200 GEMM

NVIDIA Blackwell architecture’s fifth-generation tensor cores fundamentally changed the GEMM programming model. While NVIDIA Hopper architecture’s `wgmma` instruction was issued collectively by a warpgroup, Blackwell’s `tcgen05` instruction is issued by a single thread, enabling one small producer warp to drive the tensor cores. The accumulator also moved out of registers into Tensor Memory and operands are read directly from shared memory, enabling a single MMA to span two CTAs across two SMs.

To reach competitive performance on Blackwell, our GEMM:

- Launches threadblock clusters so each CTA pair can share operands by TMA multicast, cutting memory traffic from HBM by half.
- Specializes warps within clusters: loaders bring A and B into shared memory over TMA, a single MMA warp drives the tensor cores, and a consumer warpgroup carries finished accumulators from tensor memory to HBM.
- Runs persistently, with one tile's inputs streaming in while the previous tile's outputs are still draining.

Through these efforts, we realized the following results.

![Bar chart “NVFP4 GEMMs on HGX B200”: TFLOPS by matrix size for ThunderKittens, cuBLASLt, and CuTeDSL.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747869_6aa2caa12c839e6c4270f640_tk-img-02-dark.webp)

![Bar chart “FP8 (E4M3) GEMMs on HGX B200”: TFLOPS by matrix size for ThunderKittens, cuBLASLt, and CuTeDSL.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747872_6aa2caa34cca1abe1327c81f_tk-img-03-dark.webp)

Read more about these kernels and their optimizations in our earlier [Together blog post](https://www.together.ai/blog/thunderkittens-nvidia-blackwell-gpus) or the [ThunderKittens 2.0](https://hazyresearch.stanford.edu/blog/2026-02-19-tk-2) release!

As Rubin preserves the Blackwell programming model, our old GEMMs still work. However, naively running them on Vera Rubin, we observe that our NVFP4 and FP8 kernels only achieve around 42.1% and 44.4% of the roofline — plenty of room for optimization!

![Bar chart “TK B200 NVFP4 and FP8 GEMMs on Vera Rubin”: ThunderKittens TFLOPS by matrix size, NVFP4 vs FP8.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff52574786f_6aa2caa40a32b0d6687868d1_tk-img-04-dark.webp)

The rest of this post is in two parts. First, we cover the new Rubin features that matter for a GEMM and how to use them in ThunderKittens. Then, we slowly integrate these features into our existing Blackwell NVFP4 kernel, taking it to over 22 PFLOPS and competitive with cuBLAS and CuTE DSL.

The core issue we find is that while Rubin enables tensor cores to consume operands twice as fast, our old Blackwell kernel does not feed them fast enough. To reach the compute ceiling, we need tiles to squeeze more reuse out of the data they already have on-chip.

## What’s new with the NVIDIA Vera Rubin Platform?

Comparing vendor specifications, we see the following improvements from Blackwell to Vera Rubin.

As it relates to writing performant GEMMs, we specifically take note of the subsequent features.

### 1. Tensor cores take twice the K

For review, a `tcgen05.mma` computes C = A@B + C over a MxNxK tile, consuming a fixed number of bytes along K per step. On Blackwell, this step is 32 bytes, but on Vera Rubin it can be increased to 64 bytes. The MMA itself still takes the same number of cycles, so doubled-K allows us to pack twice as much work into the same instruction window.

![Diagram comparing Blackwell's 32-byte K step to Vera Rubin's 64-byte K step, doubling the operand tile per instruction.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747878_6aa2caa6aa6b74b23843b798_tk-img-05-dark.webp)

In ThunderKittens, we express this through a new template parameter to our existing mma operation.

### 2. Tensor memory grows to 576 Columns

Blackwell introduced the concept of tensor memory, a 128 lane x 512 column x 32-bit space which tensor cores could directly read and write to. On Vera Rubin, this space increases to 576 columns, providing an extra 32 KiB of tensor memory to play with.

Note that these extra columns are reachable only through the `.exclusive` qualifier, a PTX 9.4 addition that ensures there’s only one live tensor memory allocation on an SM. Non-exclusive allocations are still capped at 512 and must be a power of two.

In ThunderKittens users may request this with a template parameter to our tensor memory allocator, specifying that the allocation is exclusive.

### 3. Shared memory increases to 328 KiB

While Hopper and Blackwell provided 228 KiB of shared memory, Vera Rubin introduces an oversized shared memory mode that can be dynamically increased to 328 KiB. This is a host-side specification that can be called as below.

### 4. B Side Collector

Blackwell introduced the concept of a collector buffer, a small MMA staging buffer that could latch onto an A tile so the next instruction takes it from there instead of from shared memory. Vera Rubin extends this functionality to the B tile as well with `.collector::b::*`.

![Diagram of two MMAs sharing a collector buffer: B is fetched once (FILL) and reused (LASTUSE) without a second fetch.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2e51e0a18e2400b8ccf08_6aa2e4e5c3b01f76bbebe98b_tk-img-06-dark.webp)

To utilize this, we annotate each MMA’s operands with one of four labels that describe its action on the collector buffer.

- “FILL” reads the operand from shared memory and latches it
- “USE” reads from the buffer
- “LASTUSE” reads from the buffer and releases it
- “DISCARD” is the default and skips the latch

These labels are permission qualifiers for reuse, not guarantees. This means that the Tensor Core could still reload a matrix even if it has permission to reuse.

Now that either operand can be resident in the collector buffer, we can experiment with new patterns. Over a 2x2 block, for instance, collecting on both sides takes four MMAs from eight operand reads to only five.

![Diagram of a 2x2 MMA block using both-sided collector latching to balance 512 port cycles against 512 math cycles.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2e51e0a18e2400b8ccf10_6aa2e4e6bd804e298d6dc4a7_tk-img-07-dark.webp)

In ThunderKittens, we can expose this through the following.

### 5. Early A release

A `tcgen05.commit` arrives on an mbarrier once the MMA it processes is finished, signaling the producer that a stage slot is free for reuse. PTX 9.4 introduces `tcgen05.commit.sync_restrict::shared::read::mma::a`, a new instruction that allows us to move the signal earlier for A tiles. Rather than waiting for the MMA to finish, we can fire the barrier as soon as an MMA has finished reading its A operand out of shared memory, enabling us to signal the tma loader to start storing the next stage’s memory.

![Timeline diagram showing the early-A-release barrier firing once the MMA finishes reading A, before the MMA fully retires.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2e51e0a18e2400b8ccf13_6aa2e4e7bd804e298d6dc4f9_tk-img-08-dark.webp)

ThunderKittens introduces a new commit type for a user to express this.

## Building the GEMM

We now have new features and a Blackwell GEMM. The following sections slowly integrate these features into our existing Blackwell kernel, and explain why they’re needed as we move to Vera Rubin.

### Widening the Instruction:

The most intuitive bottleneck comes from still relying on Blackwell’s 32-byte K step. On Vera Rubin, that encoding's ISA ceiling is ~16.8 PFLOPs, and our NVFP4 Blackwell GEMM already achieves 14.7 PFLOPs out of the box (88% of the ceiling). To push further, we must double the K bytes processed by our MMAs.

![Chart showing the 32-byte K step kernel reaching 14,741 TFLOPS, 88% of its 16.8 PFLOPS ceiling, versus a 35 PFLOPS 64-byte ceiling.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2e51e0a18e2400b8ccf0d_6aa2e4e825ceac00ddd9b55e_tk-img-09-dark.webp)

However, simply flipping on the wider encoding for the existing Blackwell kernel, we notice that performance only marginally improves, instead of a supposed 2x. While the wider MMA doubles how fast the tensor cores can consume operands, it does not help with how fast we can supply them. For double-K to be useful, we pull two levers to keep our cores happy: moving fewer bytes and deepening the pipeline to ensure these fetches are overlapped.

### Reading fewer bytes:

To fetch fewer bytes, we stack a second output tile on the same CTA pair along the M dimension. As the two accumulators differ only in M, we are able to share the same B chunk for them both. Our original Blackwell NVFP4 kernel utilized a 1x1 tiling format, meaning that covering M512xN256 of output took two pair jobs that each independently transferred their own copy of B. By moving towards a 2x1 format, we can fetch B only once and cover the same output, reducing our operand traffic.

![Diagram of a 2x1 tiling layout: two M-tiles (A0, A1) sharing one B chunk to produce a 512x256 accumulator region.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747853_6aa2caad68d2aff525740d11_tk-img-10-dark.webp)

This 2x1 tiling format was not easily achievable in our NVFP4 Blackwell kernel as tensor memory was capped at 256 KiB. Two M256xN256 accumulators already take up 512 columns, meaning that block-scaled MMAs do not have space to store their A and B scales. While programmers could work around this constraint by having the epilogue warps load only a subset of the accumulator columns before signaling the MMA-empty state, allowing the MMA for the next K tile to begin, this introduced a small amount of latency that could not be hidden. Luckily, with Vera Rubin’s 64 extra columns we can store the scaling factors without needing to do this dance.

![Diagram of tensor-memory columns: two accumulators plus A/B scale factors use 560 of Rubin's 576 columns, versus Blackwell's 512.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2e51e0a18e2400b8ccf16_6aa2e4e92eef231c8b0aa369_tk-img-11-dark.webp)

### Deepening the pipeline:

The changed tiling format reduces operand traffic, but it does not help decrease how long each fetch takes. The next challenge is to keep the tensor cores continuously fed. Vera Rubin’s larger shared memory allows us to create deeper pipelines, staging more tiles ahead of time and giving transfers more time to complete. Sweeping ring depths for our NVFP4 and FP8, 16k square GEMMs, we see the following.

NVFP4 16k Square GEMM:

FP8 (E4M3) 16k Square GEMM:

While the most gain appears from this final peg, we note that these gains are dependent on our earlier optimizations. Below are results from sweeping the K step size, shared memory pipeline, and tiling strategy independently.

![Line chart “NVFP4 Square 16,384 GEMM”: TFLOPS vs shared memory per CTA across three kernel configs (2x1/1x1, 64-byte/32-byte).](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747856_6aa2cab02990205c3c928cdb_tk-img-12-dark.webp)

### Final Touches:

To push our kernels even further, we play around with a few final knobs

1. **Kernel Config Tuning:** We further tune our kernels across varying workloads for maximal performance. Regarding CTA pair sizing, we found the original 1x1 tile format from the Blackwell kernel to be most performant for smaller square workloads. For larger shapes, we utilize the 2x1 CTA pair tiling, along with a tuned cluster size of 2, 4, or 8 CTAs.  Additionally, across all shapes, we permute tile rasterization order to improve memory locality and performance.
2. **B side collector:** As we follow a 2x1 tiling format, we can utilize the B-side collector.  By specifying “FILL” on one MMA and “LASTUSE” on the next, we can reduce B reads to only occur once instead of twice. We measured this at around 1-3% improvement.
3. **Utilizing `sync_restrict::shared::read::mma::a`:** For larger 64k and 128k square NVFP4 GEMMs , we observed that early A release led to 13.5% and 22.1% speedups respectively. We found this instruction useful at larger sizes where the A tile contends with other resources for residency, causing its rows to get evicted between reuses and forcing the loader to wait on them. This allows us to then realize the gains from early A reuse. At smaller sizes, the A tiles never leave L2, meaning reads are already fast enough without early A.In order to utilize this instruction, we modify traditional ring order logic.  In a normal GEMM, A and B tiles are part of the same ring and operate in lockstep under a single commit. However, in order for early A release to work, we need to decouple the two tiles, enabling A loads to act independently.  Early A release needs A's slot to be freed on the earlier signal, so we give A its own ring and its own arrived/finished barrier pair.
4. **L2 eviction hints:** We mark the A operands with EVICT_LAST to encourage L2 residency for later jobs that reuse them. The reuse benefit comes from across jobs, not within a cluster, and helps by a few tenths of a percent.

### Results:

![Bar chart “NVFP4 GEMMs on Vera Rubin”: final TFLOPS by matrix size for ThunderKittens, cuBLASLt, and CuTeDSL.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff52574786c_6aa2cab2af1c08b025056683_tk-img-13-dark.webp)

![Bar chart “FP8 GEMMs on Vera Rubin”: final TFLOPS by matrix size for ThunderKittens, cuBLASLt, and CuTeDSL.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6aa2cc0068d2aff525747866_6aa2cab32c839e6c427106a2_tk-img-14-dark.webp)

We note that all measurements above were produced using NVIDIA CUDA 13.4 on a Qualification Sample (QS) GPU. We expect performance of all baselines to continue to improve with Vera Rubin software releases.

## Conclusion:

We hope you found some of this useful, and we are excited for everyone to start playing with them soon. From LUT GEMMs, hardware native megakernels, and new engine optimizations, there’s still plenty of interesting snippets to share. More on that soon!

The kernels and performance teams at Together AI are actively hiring! If you’d like to learn more about these kernels or work with us on developing the next set of updates, please reach out to Simran or Dan!

- Simran: simran@together.ai
- Dan: danfu@together.ai
