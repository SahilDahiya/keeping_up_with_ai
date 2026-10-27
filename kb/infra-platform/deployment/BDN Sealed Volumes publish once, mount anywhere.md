---
title: 'BDN Sealed Volumes: publish once, mount anywhere'
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Introduces Baseten's BDN Sealed Volumes, which let teams publish read-only
  model artifacts (weights, LoRA adapters, checkpoints, vector/embedding indexes)
  once and mount an immutable, content-addressed version in any deployment, borrowing
  the container-registry tag/digest split to stop drift between staging and production
  copies.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/bdn-sealed-volumes-publish-once-mount-anywhere/
author: Stephen Day; Gregory Kofman; Yun Zou; Rajesh Malireddy
published: '2026-10-26'
fetched: '2026-10-27T06:11:07Z'
classifier: claude
taxonomy_rev: 2
words: 1916
content_sha256: ffab51f966e34500cc885d2412aed16e53240225e6b96d89eb5667e2dd6ae94f
---

# BDN Sealed Volumes: publish once, mount anywhere

### Published

![BDN Sealed Volumes: publish once, mount anywhere](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793047673-baseten-blog-2026-thumbnails-22.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

BDN is built to distribute any content (weights, container images, training checkpoints) across model serving infrastructure. Now, BDN Sealed Volumes let you publish any read-only data once and mount it in any deployment. Sealed Volumes are available today with the Baseten CLI 1.1.0 or newer.

When there’s no single source of truth for model files, data drifts from its source.

Say you fine-tune a model, then save the checkpoint to cloud storage. Then someone downloads a copy to their laptop to test it, uploads it somewhere else so it can be served, and each deployment—e.g., staging, production, and testing—has its own config file pointing to the checkpoint. When one person pins another revision, nobody notices until the outputs differ.

The same problem applies to LoRA adapters, vector indexes, tokenizers, embedding indexes, lookup tables, and any model or deployment artifact. Container images solved this problem for code a decade ago: you build once, get a digest, then run that digest anywhere. We’re releasing BDN Sealed Volumes to do the same for model data, and help our customers keep data consistent across iterations.

## What is a Sealed Volume?

Sealed Volumes let you publish any read-only data once and mount it in any deployment. Push a directory, or sync a Hugging Face repo, a bucket, or a training checkpoint, and BDN seals the result as an immutable version with a digest. Reference that digest in your `config.yaml`, and every replica streams in identical data without needing to manually download anything.

A volume specifically is a named, versioned set of files that the [Baseten Delivery Network (BDN)](https://docs.baseten.co/development/model/bdn) delivers to your deployments. Volumes live in namespaces, such as `weights`, and hold a series of versions. When `baseten volume push` or `baseten volume sync` finishes, BDN commits the files as a new version and seals it. A sealed version never changes, and BDN identifies it by a digest of its contents:

`bdn:weights/qwen3-8b@b3:9f3c…`
You can use the `--tag` parameter when pushing to give a mutable name (the only mutable part) to a particular version. For instance, pushing with `--tag prod` points prod at the new version; so while `bdn:weights/qwen3-8b:prod` is a name people can read, the digest is what a deployment should pin. If you've used container registries, this is the same split between a tag and an image digest, and exists for the same reasons.

Because your digest sits in your config files, mismatches between versions show up in a diff.

![One volume with three sealed versions. The “prod” tag points at version two, moved there by a push or a tag command, and both deployments pin its digest.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793048537-volume-versions-elevated-baseten-figures.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) One volume with three sealed versions. The “prod” tag points at version two, moved there by a push or a tag command, and both deployments pin its digest.

## Why Sealed Volumes?

Sealing volumes is what keeps data consistent when you build on top of them. Because they’re sealed:

1. **Every replica serves the same bytes:** A sealed version never changes, and every deployment that references it mounts the same files, read-only, so every replica streams the same bytes. Pinning the digest means later pushes can't change what this deployment mounts. To roll back, just point `config.yaml` at an earlier digest.
2. **Updates upload only what changed:** BDN splits files into chunks and stores each chunk once by its content hash, so a new checkpoint that shares most of its bytes with the previous one uploads only the chunks that changed. Files are keyed by hash, so BDN never transfers a file it already holds. This makes iterative uploads (like fine-tuning a base model) fast.
3. **Deployments start without a download step:** Because a sealed volume is mounted at the path you choose in `config.yaml`, the files are available as soon as the container starts. Bytes stream in from the [BDN cache tiers](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast/#speeding-up-weight-pulls-via-multi-tier-caching) as your model reads them. Startup time no longer depends on how big the volume is.

## How to publish a Sealed Volume in two commands

For a model on Hugging Face, the sync runs as a durable background job on Baseten; nothing downloads to your machine. This is the whole loop:

```
baseten volume sync start \
  --source hf://Qwen/Qwen3-8B \
  --dest bdn:weights/qwen3-8b:prod \
  --include "*.safetensors" --include "*.json" \
  --wait
```
When the job reports `READY`, it prints the sealed version's reference. Copy that into the deployment:

```
model_name: qwen3-8b
resources:
  accelerator: H100
bdn:
  mounts:
    - source: bdn:weights/qwen3-8b@b3:<digest>
      path: /mnt/weights/qwen3-8b
```
Point your server at `/mnt/weights/qwen3-8b` and deploy with `baseten model push`.

There’s no `weights` block to maintain, or credentials in the deployment. Subsequent deployments that reference already-mirrored content resolve in a metadata check, not a data transfer.

`sync` works the same way for Hugging Face, S3, GCS, Azure Blob, Cloudflare R2, and CoreWeave buckets. Private sources take a Baseten secret, and for S3 and GCS you can skip stored credentials entirely and grant access with OIDC. To publish a local directory instead, use:

`baseten volume push ./dir bdn:weights/qwen3-8b --tag prod`
`push` uploads chunks in parallel, and skips any chunk BDN already holds.

## Updating versions and rolling back

Pushing with `--tag prod` moves the tag to the new version, without publishing anything:

`baseten volume tag set --volume-ref bdn:weights/qwen3-8b@b3:<digest> --tag prod`
Deployments that pin a digest keep serving the old version until you change the `source` and redeploy. Moving the tag later doesn't change what running replicas serve, but new and scaled-up replicas mount the tag's new target. A deployment that mounts a tag can therefore serve two versions at once after a push.

To roll back, pick the earlier digest from `baseten volume versions`, set it as `source`, and redeploy. A deleted version stays restorable for 7 days via `baseten volume restore`.

## BDN Sealed Volumes are for more than model weights

Anything your model reads and doesn't write belongs in a volume. Common files a deployment reads at runtime that belong in volumes include:

- **Adapters and sub-models.** Deploy multiple LoRA adapters on a single base model and switch between them at inference time. Each adapter can be its own volume, and a new adapter needs no new image.
- **Prebuilt engines.** A TensorRT-LLM engine or a compiled graph is large, GPU-specific, and immutable. Publish it once per GPU type and mount it by digest, so redeploys don’t need to rebuild it.
- **Indexes and tables.** This includes embedding indexes, vocabulary files, tokenizer configs, lookup tables, and safety classifiers. Today these get downloaded in `load()`, or vendored into the image, but with a volume they're versioned, shared across deployments, and available at start.
- **Evaluation and reference data.** For instance, the golden set a deployment scores itself against, or the prompt templates a serving layer renders.
- **Compile caches.** The BDN Startup Cache, the first thing we built on volumes, publishes a replica's compiled kernels and captured graphs as a Sealed Volume and restores it in every later replica of the deployment. It shows up in `baseten volume ls` next to the volumes you publish yourself.

Each of these is a directory and a separate `baseten volume push`. Mounting more than one is more entries under `bdn.mounts`, and two deployments that mount the same digest share identical bytes on every cache tier.

## Building consistency into the training-to-deployment loop

The “copy problem” is worst when it comes to model training: a job writes a checkpoint to storage, then to serve it you download the weights, upload them elsewhere, and edit a config file per deployment.

Volumes help stop data drift in the training-to-deployment loop. If you train on your own cluster, a job with the CLI and an API key publishes its own output as it finishes:

`baseten volume push ./checkpoints/step-4000 bdn:weights/my-model --tag candidate`
On the other hand, if you train on Baseten, the job's checkpoints already sync to Baseten storage, and a checkpoint syncs into a volume from there (with no credentials to manage):

```
baseten volume sync start \
  --source bt://my-project@job123/checkpoint-1 \
  --dest bdn:weights/my-model:candidate \
  --wait
```
A checkpoint in your own bucket syncs from there with `s3://`, `gs://`, or the other sources above.

Because `push` and `sync` upload only the chunks that changed, a training run that publishes a checkpoint every few hundred steps only moves a fraction of the model each time, and every version stays addressable. For the higher-frequency version of this loop, where a trainer publishes deltas every few minutes and rollout clusters apply them live, see [how we sync delta weights for managed RL rollouts](https://www.baseten.co/blog/optimizing-delta-weight-syncs-for-managed-rollouts/) (BDN is the transport in both cases).

## How fast are BDN Sealed Volumes?

Sealed Volumes are read through the same three cache tiers as BDN weights: node disk, the in-cluster cache, and the mirrored origin. The difference is that a `weights` block pulls every file before the container starts, so startup time grows with the size of the model.

In contrast, a BDN Sealed Volume mounts in seconds, and the model reads from it at the same rate it reads from a `weights` mount. That means that the pull phase drops out of the startup time (nothing else changes). Data is served as fast as the network and disk allow, and avoids unnecessary fetches at every layer of the stack.

![The same model with a “weights” block and with a BDN Sealed Volume. The pull phase becomes a mount, and the loading model phase is the same work in both.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793051977-weights-delivery-timeline-baseten-figures-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The same model with a “weights” block and with a BDN Sealed Volume. The pull phase becomes a mount, and the loading model phase is the same work in both.

The lazy read path also enables volumes larger than a node's disk, because the node holds the chunks the model touched, and evicts the ones it can fetch again. When the model reads an evicted chunk, the in-cluster cache (the same tier that helps [make BDN cold starts fast](https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast/)) serves it back at network line rate.

## The future of `weights` blocks vs. Sealed Volumes

If you deploy with a `weights` block today, you don't need to change anything. We'll automatically move `weights` deployments to Sealed Volumes as the migration rolls out, with no config change needed on your side.

For new weights, we encourage you to use Sealed Volumes directly: sync the source into a volume and mount it.

Here's how `weight` blocks and volumes compare today:

To migrate, run a sync against the source in `weights`, then mount the result at the same `mount_location`. Nothing in your model code changes.

Mounts are read-only; for files your model writes at runtime, use [b10cache](https://docs.baseten.co/development/model/runtime-caching).

## Get started

To start using BDN Sealed Volumes, upgrade the Baseten CLI to 1.1.0 or newer (`brew upgrade baseten`), and Truss to 0.18.30 or newer if you [deploy with Truss](https://docs.baseten.co/development/model/overview). Then run the [quickstart](https://docs.baseten.co/development/volumes/overview), which publishes a directory, mounts it, and deploys a model in about five minutes. The [manage](https://docs.baseten.co/development/volumes/manage) and [sync](https://docs.baseten.co/development/volumes/sync) pages cover versions, rollback, and every source type.

Sealed Volumes are the first user-facing primitive of BDN Fabric, the next generation of the Baseten Delivery Network. If you want to talk through your weight pipeline, reach out [to our engineers](https://www.baseten.co/talk-to-us/).

*Note: Volume mounts aren't available on T4 or L4 instances as of the last update date of this article.*

## Acknowledgements

Many thanks to the many people involved in making BDN Sealed Volumes a reality: Angie Montemayor, Xiaoqian Liu, Kamal Haddad, Ahmet Balkan, Amy Hu, Christine Wang, Shreya Ravi, Brian Broll, Sid Gupta, Chad Retz, and Patrick R.
