---
title: How the Baseten Delivery Network (BDN) makes cold starts fast
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/optimization
summary: Deep dive into how the Baseten Delivery Network reduces cold starts for model
  serving.
source: baseten
url: https://www.baseten.co/blog/how-the-baseten-delivery-network-bdn-makes-cold-starts-fast/
author: Gregory Kofman; Ujjwal Sarin; Stephen Day
published: '2026-04-09'
fetched: '2026-07-11T04:05:43Z'
classifier: codex
taxonomy_rev: 1
words: 2067
content_sha256: d0760dfe78a2a695d04abb2a194e662bef2bb8ceefa5c88fa8624daf4648d282
triage: keep
skip_reason: null
---

# How the Baseten Delivery Network (BDN) makes cold starts fast

![How the Baseten Delivery Network (BDN) makes cold starts fast](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775594447-baseten-blog-2026-thumbnails-4.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The Baseten Delivery Network (BDN) is an opt-in weight delivery system for model deployments. It reduces runtime dependency on upstream providers by mirroring model weights into securely managed storage at deploy time. BDN caches weights across a three-tier hierarchy — node-local disk, an in-cluster peer cache backed by a consistent hash ring, and mirrored origin — and coordinates downloads so that cold starts stay fast even during thundering-herd scale events.

BDN also reduces costs: because BDN delivers weights before the user's container starts, weight transfer doesn't consume billable GPU time. And because data from weight sources is only transferred when changed at deployment time, egress costs stay low.

## The problem: Weight transfer is brittle at scale

When a new replica starts, model weights must be loaded into GPU memory before it can serve a request. A single checkpoint ranges from ~10 GB (a quantized 7B model) to 100s of gigabytes (a full-precision 70B+ model, or a multi-expert architecture like DeepSeek-R1). Weight transfer ends up taking up most of the cold start time.

This could be manageable if weight transfer were fast and reliable, but at scale, it's neither. Three failure modes make weight transfer brittle at scale:

- **Slow pulls:**Upstream rate limiting and cross-region latency make download throughput unpredictable. For instance, a Hugging Face download that typically takes 90 seconds can take 10 minutes during a popular model launch.
- **Upstream fragility:**Hugging Face, S3, and GCS experience outages, and a runtime dependency on them means their availability is your availability.
- **Thundering herd:**When an autoscaler fires up 50 replicas simultaneously, all 50 try to pull the same files, multiplying bandwidth consumption and upstream load.

A single cache layer doesn't solve this. A shared NFS volume becomes the bottleneck during burst events. And node-local-only cache helps warm nodes but does nothing for cold ones.

BDN addresses all three failure modes with a layered approach: own the source, cache by locality, and deduplicate work across the cluster.

![High-level architecture overview of BDN.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775594513-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) High-level architecture overview of BDN. Each section is described in more detail below; connections are state-dependent and not all are represented here (e.g., “BDN resolver” (in the workload plane) would also link to “mirrored chunks” (in secure storage) if cached weights are not present on the node or cluster). Security checks and pod initiation are also excluded to help maintain clarity of the caching system.

High-level architecture overview of BDN. Each section is described in more detail below; connections are state-dependent and not all are represented here (e.g., “BDN resolver” (in the workload plane) would also link to “mirrored chunks” (in secure storage) if cached weights are not present on the node or cluster). Security checks and pod initiation are also excluded to help maintain clarity of the caching system.## Own the source: Push-time mirroring

When a user deploys a model with BDN enabled, the mirroring pipeline reads the weights configuration from the Truss config and mirrors files into Baseten-managed secure blob storage. The output is a manifest: a list of files with their content hashes or etags, which serves as the authoritative record for what a deployment needs to start.

Files are keyed by content hash or etag, depending on what is available from the user’s weight source. This means identical files across different models (the norm for fine-tunes sharing a base) are mirrored and stored once. The mirroring decision is metadata-based: BDN checks whether it already holds a matching file before transferring any bytes. Subsequent pushes that reference already-mirrored content resolve in a metadata check, not a data transfer. The mirroring workflow can achieve 1-5GB/s through high parallelism: file chunks are distributed across a pool of workers to maximize throughput.

![When a user deploys a model, BDN checks whether it already holds matching files (via a metadata check). If the weights are not already mirrored (first-time deployment), BDN mirrors files into Baseten-managed secure blob storage. The output is a manifest containing the list of files with their content hashes or etags.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775594507-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) When a user deploys a model, BDN checks whether it already holds matching files (via a metadata check). If the weights are not already mirrored (first-time deployment), BDN mirrors files into Baseten-managed secure blob storage. The output is a manifest containing the list of files with their content hashes or etags.

When a user deploys a model, BDN checks whether it already holds matching files (via a metadata check). If the weights are not already mirrored (first-time deployment), BDN mirrors files into Baseten-managed secure blob storage. The output is a manifest containing the list of files with their content hashes or etags. The only time BDN accesses a model’s upstream sources is during deploy-time mirroring; after that, every subsequent cold start reads from Baseten-managed storage. This has two implications: first, upstream outages, rate limits, and credential rotations don't affect serving. Second, egress costs are minimized to genuinely new weight data on subsequent model deployments, not repeated pulls of the same model weights across deployments or scale events.

Access control is enforced at the deployment level. While content/etag-addressable storage means identical weights aren't duplicated, a deployment's replicas can only read the specific files enumerated in its manifest.

## Speeding up weight pulls via multi-tier caching

Baseten deployments run in workload planes: isolated clusters across regions and availability zones. Each workload plane has its own cache hierarchy. These caching layers allow BDN to achieve a throughput of >2 GB/s to download weights onto H100 nodes.

When a deployment has BDN enabled, the BDN CSI (a Container Storage Interface driver running on each node) fetches the deployment's manifest and resolves each file through three tiers.

**Tier 1: Node-local disk**

Each GPU node has a local NVMe SSD for weight caching. If a model's weights have been loaded on this node before by any replica for any deployment, the files are already on disk. Reads happen at NVMe speeds (multiple GB/s) with zero network traffic.

Because files are content/etag-addressed, a new deployment sharing most weights with a previous version hits cache for the shared files and only fetches the delta. And, because the BDN CSI delivers weights before the model container starts, weight transfer happens outside the billable compute window. Without a solution like BDN, models load their own weights at runtime. Customers pay for GPU time while waiting for downloads to complete.

**Tier 2: In-cluster peer cache** 

Each workload plane maintains a distributed cache backed by a consistent hash ring spanning essentially all nodes in the cluster. This is not a passive lookup layer; it actively participates in origin downloads.

When a file isn't on local disk and needs to come from origin, it's split into fixed-size chunks, and each chunk is assigned to a node on the hash ring. Nearly all nodes pull their assigned chunks from origin concurrently, so the fetch bottleneck is the cluster's aggregate origin bandwidth, not any single node's. When a node needs to assemble the full file, it already holds its assigned chunks and requests the rest from peers in parallel over in-cluster fabric. The origin fetch is distributed across the cluster; each node fans in chunks from many peers concurrently, with all data ultimately converging on the node whose GPU needs it.

For files already cached in the cluster, the same hash ring provides the lookup. The requesting node knows which peers hold which chunks and pulls them directly, skipping the origin entirely. Replica scale-ups in a warm cluster rarely touch origin at all.

![For cold clusters, weights are split into fixed-sized chunks which are pulled from origin concurrently by their assigned nodes. For warm clusters, when a node needs to assemble the full file, it already holds its assigned chunks and requests the rest from peers in parallel over in-cluster fabric.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1775594627-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) For cold clusters, weights are split into fixed-sized chunks which are pulled from origin concurrently by their assigned nodes. For warm clusters, when a node needs to assemble the full file, it already holds its assigned chunks and requests the rest from peers in parallel over in-cluster fabric.

For cold clusters, weights are split into fixed-sized chunks which are pulled from origin concurrently by their assigned nodes. For warm clusters, when a node needs to assemble the full file, it already holds its assigned chunks and requests the rest from peers in parallel over in-cluster fabric.**Tier 3: Mirrored origin** 

For true cache misses (the first cold start of a new model in a new cluster), BDN falls back to Baseten-managed blob storage. Downloads use parallelized byte-range fetches, achieving aggregate throughput in GB/s.

The lookup path for each file chunk: local disk → peer cache → origin, tried sequentially, short-circuits on hit. Files are resolved independently and in parallel, so a 20-shard model can pull each shard from a different tier simultaneously. And because files are immutable once mirrored throughout the BDN stack, weights can be delivered fast without spending cycles on locking, invalidation, and coherence protocols.

## Example download coordination

Two mechanisms prevent redundant work.

**Node-level, single-flight downloads:** When multiple pods on the same node request the same file (which is common during scale-up), the BDN CSI coalesces them into one download. At most one fetch per (node, content-hash) pair is in progress at a time. All waiters share the result via local disk.

**Cluster-level hash ring:** The consistent hash ring assigns chunk ownership deterministically from the content hash/etag, serving as both cache-lookup and fetch-coordination. No protocol is needed to decide who fetches what: every node independently computes the assignment.

What happens during a burst? Let’s consider 50 replicas of a 140 GB model across 20 nodes in a fully cold cluster:

- The hash ring assigns each chunk to a node.
- All 20 nodes pull their assigned chunks from origin in parallel (~7 GB each).
- As chunks arrive, they're written to local disk and become available to peers.
- Nodes simultaneously request chunks they don't have from peers that do, pulling them in parallel over the in-cluster fabric.
- Node-level, single-flight downloads ensure each file is assembled once per node.

The net result: origin bandwidth is 1× the model size (not 50×) and parallelized across the cluster, with each node fanning in from many peers concurrently.

## Transfer centralization

One problem we faced before BDN was the large performance gap between different client systems that perform data transfers.

An optimized client can mean the difference between an anemic download speed and saturating the pipe. The problem, however, is that as the number of systems grows, optimizing each one for our particular deployment is a massive effort. Keeping them monitored and tuned for different hardware becomes unmanageable.

Rather than patching each individual system, we've centralized data transfer into a single optimized chunk-transfer implementation that we tune to the use case. It can be configured to use simple prefetch, file-backed resumable download, or can even operate in a powerful 2Q caching mode. These features allow us to saturate upstream bandwidth regardless of the access pattern while reducing the impact of overfetch.

New applications of our chunk transfer system are already in the works, and BDN powers weight transfer, proxies, and container image downloads. This has given us an amazing point of leverage: improving one library makes our entire system faster.

## Eviction and resource sharing

Node-local SSDs have finite capacity that they have to share with inference workloads.

BDN uses LRU eviction so that recently-accessed weights stay warm. Files fetched from lower tiers are written to local disk on arrival, promoting them to Tier 1. Then BDN CSI rate-limits background cache fills to avoid starving inference I/O when cold starts and active serving share a node.

We tend to evict more at the Tier 1 level, but try to keep a low eviction rate at Tier 2 to keep performance manageable.

## Start using BDN (also: we’re hiring!)

BDN started as a solution to the cold start problem for model weights, but much of the architecture extends to container images, training checkpoints, and deployment artifacts — and that’s exactly what we’re working on now.

If you want to work on a container stack purpose-built for AI workloads, check out our [open roles](https://www.baseten.co/resources/careers/?department=engineering#join-our-team): our Runtime Fabric team is hiring! And if you're running inference on Baseten and want to enable BDN for your deployments, get started with [our docs](https://docs.baseten.co/development/model/bdn) or reach out to [talk to our engineers](https://www.baseten.co/talk-to-us/).
