---
title: Optimizing delta weight syncs for managed rollouts
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/optimizing-delta-weight-syncs-for-managed-rollouts/
author: Paras Stefanopoulos
published: '2026-09-08'
fetched: '2026-09-09T06:10:11Z'
classifier: null
taxonomy_rev: 2
words: 1729
content_sha256: c70cdbf7129ad80872c0d31cf2fac65536be6331f49fa01dd5ba0abdb579fa75
---

# Optimizing delta weight syncs for managed rollouts

![The trainer publishes each checkpoint or delta once to Amazon S3 and the Baseten Delivery Network distributes it to independent rollout clusters without a direct trainer-to-GPU connection.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902100-1-a.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Baseten supports [delta weight syncs](https://huggingface.co/blog/delta-weight-sync) to leading frontier models like GLM-5.3 across global, independent clusters in **under 40 seconds**, with only **6 seconds** of request pause. AI labs and frontier research teams use our managed rollouts offering to run their frontier-scale RL. They control the trainer and we run the rollouts on the same infrastructure that powers inference for Cursor, Hubspot, Lovable, and Notion.

A trainer runs in the customer's environment. It publishes full checkpoints and small deltas to object storage. A Baseten deployment leveraging a global pool of capacity watches the same stream, reconstructs the requested policy, updates GPUs across our fleet, and keeps serving. We use the Baseten Delivery Network for the large object transfers so each cluster only downloads model weights once which minimizes repeated public-cloud egress costs. See Stephen Day’s explanation of the Baseten Delivery Network [here](https://x.com/stevvooe/status/2042306285379731726).

![The trainer publishes each checkpoint or delta once to Amazon S3 and the Baseten Delivery Network distributes it to independent rollout clusters without a direct trainer-to-GPU connection.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902100-1-a.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The trainer publishes each checkpoint or delta once to Amazon S3 and the Baseten Delivery Network distributes it to independent rollout clusters without a direct trainer-to-GPU connection.

## Utilizing a global fleet of clusters

Many very fast weight-update systems assume the trainer and rollout GPUs are connected by the same high-bandwidth network. We do not.

The customer’s trainer and Baseten’s rollout clusters can have different schedulers, networks, regions, clouds, and failure domains. They do not share GPU memory or a distributed process group, and they need no direct connection. In a capacity constrained world, we think it’s important for flexibility and access to different compute clusters.

The trainer publishes a checkpoint or delta and moves on. Each rollout cluster independently discovers the new version, downloads it, reconstructs the changed weights, and applies them to its own GPUs. Each cluster can be added or restarted without reconfiguring or blocking the trainer or the other clusters.

## What is a delta weight?

For each tensor, we apply an exclusive or (XOR) to the serialized weight bytes from policy N and the corresponding serialized weight bytes from policy N+1. This is a byte-level encoding rather than numerical subtraction of the weight values.

About **0.09%** of tensor elements in our fixture differ at all in their serialized representation. Most XOR bytes are zero. [Zstandard](https://github.com/facebook/zstd) (zstd) compression is extremely good at compressing those zeroes. On our real GLM-5.3 fixture, **716.56 GiB** of logical XOR data compressed to **1.55 GiB**.

![XOR over serialized policy bytes turns unchanged data into zeros. In our GLM-5.3 fixture, 716.56 GiB of logical XOR data compresses to a 1.55 GiB delta.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902815-2-b.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) XOR over serialized policy bytes turns unchanged data into zeros. In our GLM-5.3 fixture, 716.56 GiB of logical XOR data compresses to a 1.55 GiB delta.

This form of delta weight sync has become recently popularized and is easy to implement on the learner side. The trouble is loading this in and applying it to the sampler GPUs quickly.

At first, we thought the trainer should add a separate run-length encoding step before zstd. That would make the sparse positions explicit, but it would also require changing the learner-side format.

We found that zstd already contains nearly the same information. It represents compressed data as a small literal stream plus commands such as “copy 2,700 bytes from a location just behind the current output.” On an XOR tensor that is almost entirely zero, those commands describe the long zero gaps between changed bytes. We can read that structure directly, so the trainer continues publishing the same compressed delta format.

## **Why ordinary zstd decoding does too much work**

The complete parent checkpoint is held in CPU memory. Our previous fast-decoder also avoided allocating a single 700 GB buffer. It used a reusable **16 MB CPU buffer**:

1. Decompress the next chunk of XOR bytes into the buffer.
2. Scan the chunk to find non-zero values.
3. Read the corresponding old elements from the parent checkpoint.
4. Apply XOR to produce absolute new values.
5. Reuse the buffer for the next chunk.

A simple trick to speed up step 2 was to ingest 8 bytes at a time (or 64 with AVX 512 instructions) so we could scan through the incoming bytes in less CPU cycles. This was pretty quick!

![A reusable 16 MB buffer and 64-bit comparisons make scanning faster, but the decoder still materializes and inspects all 716.56 GiB of logical output.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902827-3-e.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A reusable 16 MB buffer and 64-bit comparisons make scanning faster, but the decoder still materializes and inspects all 716.56 GiB of logical output.

The processors still had to produce and inspect every byte in **716.56 GiB** of logical output. Almost every answer to “did this sequence of bits change?” was “no.”

Looking only at zstd block headers does not solve this. A zstd block covers at most 128 KiB of output, and the real changes are scattered widely enough that essentially every block contains at least one change. We need to look inside the compressed blocks.

## Going a step beyond: reading the zstd commands directly

A compressed zstd block contains two important pieces:

- **Literals:** byte values stored directly, usually compressed with a Huffman code.
- **Sequences:** compact commands containing a literal length, match length, and offset. zstd stores these commands with Finite State Entropy, a compact bit-level encoding.

A normal decoder executes every sequence by copying bytes into a dense output buffer. Our custom decoder uses zstd’s own entropy-decoding routines to recover the same literals and sequence commands, but replaces the dense copy step.

![The sparse decoder follows zstd’s literal and match commands directly: zero runs advance a logical cursor, while only changed bytes and copied non-zero values are emitted.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902830-4-k.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The sparse decoder follows zstd’s literal and match commands directly: zero runs advance a logical cursor, while only changed bytes and copied non-zero values are emitted.

For one tensor, the decoder:

1. Keeps a logical cursor for where it would be in the decompressed tensor.
2. Records a literal only when its byte value is non-zero.
3. For a match command, inspects the sparse history that the command refers to.
4. If that source range contains only zeroes, advances the cursor by the full match length without allocating or copying those bytes.
5. If the match copies an earlier non-zero value, reproduces only that sparse value at its new positions.

The fifth step is important. A zstd match does not always copy zeroes, and it can overlap its own output so that a short pattern repeats many times. Ignoring copied non-zero values would silently miss changes. The sparse decoder preserves those semantics without writing the intervening zeroes.

Hence, we still decode the compressed zstd command stream, but we do not materialize or scan its full logical output. The work is driven by compressed commands and non-zero values instead of the 700 GB model representation.

## From changed bytes to a safe (and quick) GPU update

The decoder groups changed bytes into logical tensor elements. It fetches the required tensor from CPU memory, applies XOR and generates absolute new values.

We serialize the result as a sparse manifest: an array of element positions and an array of absolute values. Absolute values make retries safe: writing one twice is harmless, whereas applying XOR twice would undo the update.

Then we briefly pause new requests and apply the prepared changes to the weights already resident on each GPU.

The checkpoint divides the model into many small tensors, while vLLM combines those weights into fewer, larger GPU tensors. Our first implementation updated each small checkpoint tensor separately. Because GLM-5.3 contains tens of thousands of them, this caused tens of thousands of small GPU transfers and operations.

We now translate every changed element to its final location in the GPU layout, group changes that share the same destination, and apply each group together. We also read the next sparse-stage shard in parallel and cache the layout translation for reuse.

![Changed elements are translated into the final vLLM GPU layout and grouped by destination, replacing tens of thousands of small updates with a few batched operations.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902832-5-h.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Changed elements are translated into the final vLLM GPU layout and grouped by destination, replacing tens of thousands of small updates with a few batched operations.

On one 8×B300 replica, this reduced the measured pause/load/resume interval from approximately **12 seconds to 6 seconds**, while preserving the same absolute-value, retry-safe update behavior.

## Persisting the patched checkpoint after requests resume

Once the GPUs are serving N+1, the complete checkpoint in memory still represents N. We need to rebuild it because the next delta was calculated against N+1; using the wrong parent would produce nonsense bytes. This work is asynchronous. Requests keep running while workers each patch the original weights.

![Requests resume as soon as policy N+1 is live on the GPUs; the on-disk/in-memory checkpoint is promoted in the background so it becomes the durable parent for the next delta.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902834-6-d.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Requests resume as soon as policy N+1 is live on the GPUs; the on-disk/in-memory checkpoint is promoted in the background so it becomes the durable parent for the next delta.

## The final pipeline

The previous policy serves while the next delta downloads and the sparse update is prepared. Only the final GPU scatter requires a request pause.

In production, our zstd custom decode takes **17.30 seconds**, the sparse staging can take another **5 to 10**. The complete path from publishing the marker in S3 to receiving the first response from the new policy is down to an average of **36 seconds**.

## What this looks like across a fleet

A rollout service has to repeat fast updates across independent clusters without a long tail. Each cluster receives the same compact delta and independently turns it into the sparse positions and values needed by its local GPUs.

![Across independent rollout clusters, the complete update averages 36 seconds, with requests paused only for the final six-second GPU update.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1788902836-7-i.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Across independent rollout clusters, the complete update averages 36 seconds, with requests paused only for the final six-second GPU update.

If you want this for your training stack, [talk to our team](https://www.baseten.co/). If this kind of systems work sounds fun, [we are hiring](https://www.baseten.co/resources/careers/).
