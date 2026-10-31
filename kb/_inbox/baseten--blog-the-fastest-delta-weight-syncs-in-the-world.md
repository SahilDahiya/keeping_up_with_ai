---
title: The fastest delta weight syncs in the world
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-fastest-delta-weight-syncs-in-the-world/
author: Jerry Hong; Paras Stefanopoulos
published: '2026-10-30'
fetched: '2026-10-31T06:05:54Z'
classifier: null
taxonomy_rev: 2
words: 1492
content_sha256: 7647629edf69ed4a9749d3d7ee594ec314950dba580afa05c2644d00722b6073
---

# The fastest delta weight syncs in the world

### Published

![The fastest delta weight syncs in the world](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793386760-baseten-blog-2026-thumbnails-24.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

In our [last technical blog](https://www.baseten.co/blog/optimizing-delta-weight-syncs-for-managed-rollouts), we showed [delta weight syncs](https://huggingface.co/blog/delta-weight-sync) for a \~770 GB GLM-5.3 checkpoint in **36 seconds**, with **6 seconds** of request pause. The same sync now takes 15 seconds, with a 0.8-second pause, enabling throughput improvements by as much as 3.2x.

We rebuilt the weight sync path around the weights already on the GPU. This removes the need for us to maintain a second full copy in CPU memory. This new design lets us:

- Verify updates by reading only changed GPU positions
- Minimize pause time by preparing GPU writes beforehand
- Use freed host memory for KV cache, improving throughput
- Unlock Kimi K3 RL rollout on 8:GB300, previously blocked by CPU memory

## A quick recap of delta weight syncs

A trainer in the customer's environment publishes full checkpoints and sparse deltas to object storage. Each delta tensor is `zstd(parent_bytes XOR new_bytes)`. Once a snapshot is uploaded, the trainer sends a delta weight sync request naming the policy it wants served. Rollout clusters across our fleet pull each object once, through the Baseten Delivery Network (BDN), reconstruct the new policy, and update their GPUs in place. It’s also important to note that the trainer and rollout GPUs share no infrastructure.

That part is unchanged.

![figure 1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384193-fig1-publishing-a-delta.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 1: The trainer publishes each checkpoint and delta once to object storage in its own environment; every replica pulls the same objects through the Baseten Delivery Network and syncs on its own.

## The CPU copy was the bottleneck

Our first design kept the complete parent checkpoint in host memory. The decoder needed it to turn XOR bytes into new values, and after every update it had to be patched so the next delta decoded against the right parent.

That copy cost us three ways:

1. **Memory.** Every replica held its full parent in host RAM: \~770 GB for GLM-5.3. On an 8×B300 node, the copy and a 1.1 TB host KV cache could not coexist; the cache had to shrink to 275 GB.
2. **Time.** Promoting the CPU copy to the new policy took about **45 seconds** per update, blocking the next delta.
3. **Two sources of truth.** Every update had to land on the GPU and in the CPU copy, or the next delta decoded against the wrong parent.

The GPU already holds every byte of policy N. We only needed a way to read the few bytes that change.

![2](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384271-fig2-gpu-is-the-parent.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 2: Before, every delta was decoded against a \~770 GB CPU copy that then took 45 seconds to promote; now the GPU weights are the parent, and the same update goes live in 15 seconds with a 0.8-second pause.

## The GPU is the parent

At startup we load the model from a local disk copy, verify every served tensor against it through the engine's actual GPU layout, record a per-tensor Adler-32 checksum, and delete the copy. From then on, GPU memory holds the only parent.

When a delta arrives, our native decoder walks zstd's commands directly and keeps only the nonzero XOR bytes: for each changed element, its position and its XOR mask. It never materializes the dense XOR tensor and never reads model weights.

Then, while the old policy keeps serving, each GPU worker:

1. Gathers the **old values at the changed positions only**.
2. Applies the XOR mask to get the **absolute new values**.
3. Verifies the result against the trainer's checksum.
4. Seals the new values into a write plan in the engine's native tensor layout.

![3](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384796-fig3-one-delta-flow.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 3: Everything up to the write runs while the old policy keeps serving; inside the pause, each rank writes absolute values, and all ranks must agree before the new policy is published.

## Delta checksums with O(1) updates

The trainer publishes the Adler-32 of every changed tensor's new bytes. Checking that naively means rehashing the whole tensor, this is inefficient.

Each byte contributes to Adler-32 independently, by an amount that depends only on its (position, value). So a changed byte's effect on the checksum can be computed in constant time from its position, old value and new value. We start from the checksum recorded at startup, add one correction per changed byte, and compare with the trainer's. Unchanged bytes are never read.

This optimization made the whole update up to **2.3×** faster (Kimi K3 on a 30 GB delta went from \~230 to \~100 seconds) whilst ensuring correctness. A corrupted download or a wrong parent is rejected before any GPU write.

![4](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384823-fig4-delta-checksum.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 4: Only the changed byte is read: its old and new values correct the stored checksum in constant time, and the corrected checksum must match the trainer's.

## A sub-second pause

The purpose of such extensive preparation before the pause is to minimize the operations we perform inside the pause. The pause now becomes:

1. Close admission and pause running requests in place.
2. Write new values in place + refresh derived weights.
3. Publish the new policy version, reopen admission.

On GLM-5.3 the pause is now **0.8 seconds**, down from 6. Also, the 45-second CPU promotion is gone, so the next delta can apply as soon as it lands.

## Further optimizations

Avoiding the CPU checkpoint was a huge unlock. However, with no CPU copy, the update work shares the GPUs and CPUs that serve traffic. These optimizations keep it from cutting into serving throughput.

### Parallelism-aware delta decoder

Under tensor and expert parallelism, each GPU serves its own shard. Our decoder splits every delta by the GPU that owns each change, and each GPU maps its changes straight to addresses in its own packed layout, down to swizzled FP8 and FP4 scale factors.

### Avoiding contention between delta weight sync and serving

SGLang's scheduler is a Python event loop, so any CPU-heavy work in its process contends for the GIL and stalls batch scheduling. Our update planning runs in a separate, CUDA-free helper process instead, exchanging bulk data with the GPU worker through shared pinned memory.

### Decoding starts before the download finishes

A delta arrives as many shards, and each is decoded as soon as it lands. Download and decode are pipelined rather than sequential. The decoder runs on persistent, low-priority native threads sized to leave 16 cores for serving.

## Kimi K3 on two GB300 nodes

Kimi K3 is **1.7 TB** in its served MXFP4 layout. With a CPU checkpoint, each GB300 node would need roughly 838 GB of host memory just for its half of the weights, nearly a serving container's entire memory limit. This is a hard constraint since GB300s come with pre-configured hardware.

Now it runs on **two** GB300 nodes with four GPUs each. Each node decodes, verifies and stages **only the tensors it owns**, and never holds the other node's weights. Both nodes must write successfully before the new policy is published and requests resume.

On an 8.4 GB delta, Kimi K3 goes from delta weight sync request to live weights in **75 seconds**, with a **4.1 second** pause.

![5](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384858-fig5-kimi-k3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 5: Each GB300 node decodes, verifies and writes only the tensors it owns; host RAM holds no weight copy, just a bounded delta budget and the host KV tier.

## Spending the memory on KV cache

Throughout this blog, we’ve mentioned that the biggest unlock from not keeping the checkpoint on host memory, is the additional memory overhead we gain that allows for KV cache offloading. Here is how it works + some measurements:

- Evicted GPU KV pages are written back to host memory instead of dropped, and a later request with the same prefix reloads them instead of re-running prefill.
- RL rollouts are multi-turn with long shared prefixes: reloading an evicted 150k-token prefix from CPU memory takes **0.48 seconds**, versus **4.9 seconds** of fresh prefill.

We also ran Kimi K3 on the AgentX benchmark with offloading on the new design versus the old CPU-checkpoint setup.

- At a concurrency of 16, the KV cache already fits on the GPU, so it makes no difference.
- At a concurrency of 48, the agents’ prefixes no longer fit in GPU memory but do fit in host memory, so offloading turns misses into hits: the hit rate jumps from **2% to 92%** and **output throughput per GPU rises 3.2×.**

![6](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793384899-fig6-cpu-vs-gpu-checkpoint.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Figure 6: At a concurrency of 16, both setups fit everything on the GPU; at 48, only the GPU-checkpoint replica has host memory free for offloading, and cache hits rise from 2% to 92%.

## Results

All runs are one replica with trainer-shaped fixture deltas, measured from the trainer's delta weight sync request to the replica serving the new policy. This is timed from the S3 marker to the first new response.

If you want this for your training stack, read the [RL rollouts docs](https://docs.baseten.co/rl-rollouts/overview) or [talk to our team](https://www.baseten.co/). If this kind of systems work sounds fun, [we are hiring](https://www.baseten.co/resources/careers/).
