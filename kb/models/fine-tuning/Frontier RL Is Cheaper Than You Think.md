---
title: Frontier RL Is Cheaper Than You Think
topic: models
subtopic: fine-tuning
secondary_topics:
- infra-platform/cost
summary: Argues that frontier reinforcement learning can be cost-effective with the
  right infrastructure and training-loop design.
source: fireworks
url: https://fireworks.ai/blog/frontier-rl-is-cheaper-than-you-think
author: null
published: '2026-03-23'
fetched: '2026-07-11T04:13:38Z'
classifier: codex
taxonomy_rev: 1
words: 1479
content_sha256: 6dacd5a1a053a343ac2f9fc4eb763de989d5863588374c8a957405d6bd650692
triage: keep
skip_reason: null
---

# Frontier RL Is Cheaper Than You Think

On this page

The conventional wisdom on RL infrastructure is wrong, and it is costing teams that could be competing at the frontier.

The entire mega-cluster narrative rests on a single assumption: that you have to ship 1 TB of weights every time you update your rollout fleet. You do not.

Researchers have spent the last year writing about asynchronous RL and rollout-training disaggregation in systems like [AReaL](https://arxiv.org/abs/2505.24298). Teams like [Kimi](https://moonshotai.github.io/checkpoint-engine/) and [MiniMax](https://www.minimax.io/news/forge-scalable-agent-rl-framework-and-algorithm) have also published engineering notes on RL parameter updates and asynchronous scheduling. We have been running that pattern in production.

That mega-cluster instinct comes from pretraining, where the main systems problem is keeping one huge synchronous training job saturated. RL is a different problem. The question is not just how to run the trainer. It is also how to keep a large rollout fleet generating data from a fresh enough policy without constantly stalling on full checkpoint transfers.

An RL training run has two jobs:

- The **trainer**does forward pass, reward computation, backward pass, and parameter updates.
- The **rollout fleet**samples trajectories from the current policy, i.e. runs inference on the latest updated model.

The trainer needs dense, tightly coupled hardware. The rollout fleet needs inference throughput across many parallel requests. Pretraining only has the first job. RL has both, which is why the infrastructure question is different.

A typical frontier checkpoint is around 1 TB. If every policy refresh required shipping that full checkpoint to the rollout fleet, then the natural conclusion would be that RL needs one giant co-located cluster with RDMA-class internal networking. Keep trainer and inference on the same fabric, avoid long-distance transfers, and treat remote capacity as second class.

That is the mega-cluster story. It makes frontier RL look like a market only a handful of companies can enter, because everyone else gets boxed out by infrastructure economics before they even get to compete on algorithms or product execution.

But the premise is wrong. You do not need to move the full 1 TB on every update.

Between nearby RL checkpoints, most weights change only a little. That makes it practical to send a compressed delta against the previous checkpoint instead of sending the full 1 TB again.

Last year, we empirically observed that more than 98% of weights in bf16 format remain bit-equivalent between consecutive checkpoints, and the unchanged fraction is even higher at lower precision. Our intuition was that post-training updates are extremely fine-grained and RL provides very sparse information signal with just a few bits per rollout. In practice that means RL training uses a fairly small learning rate, and most parameters move only slightly in fp32. Those changes often do not cross the threshold required to alter their 16-bit or lower-precision representation. A recently published paper, [Understanding and Exploiting Weight Update Sparsity for Communication-Efficient Distributed RL](https://arxiv.org/pdf/2602.03839), provides a theoretical foundation for the same phenomenon and reports similarly high sparsity, often around 99% in practical RL settings.

In the sample setup behind this post, a full checkpoint is 1024 GiB. The average delta between adjacent checkpoints is 20.3 GiB, or 1.98% of the full model. Over the 50-step window shown below, that cuts cross-region transfer volume by about 94% compared to moving the full model every time.

The cadence looks like this: publish a full base checkpoint every N steps, then ship compressed deltas in between. The compression focuses on sending only the changed weights, with checksummed reconstruction so every rollout cluster can rebuild the exact checkpoint losslessly from shared storage.

The point is that delta-compressed weight updates make cross-region synchronization practical over ordinary network links, without requiring trainer and rollout inference to share one RDMA fabric.

Asynchronous RL (also often called Pipeline RL) explicitly trades being a little off-policy for much better compute efficiency. Idle samplers are expensive, and a little policy staleness is often acceptable if it keeps training and rollout generation overlapped.

That tradeoff only works if policy updates move quickly enough. Delta-compressed weight updates make it practical by keeping the handoff small: distributing a new checkpoint across globally distributed rollout clusters takes only a few minutes end to end, which bounds the overall off-policy delay. The actual weight swap in GPU memory can stay well under a minute because most of the work, especially download and decompression, is pipelined ahead of the swap itself.

Trainer implementation is pipelined too. Every training step can upload updated weights to shared object storage, with each rank caching its previous upload and transmitting only the diff against the new weights. Upload is sharded across training GPUs, download is sharded across inference replicas, and compression plus transfer plus signaling are pipelined in background so training is never blocked.

The practical payoff is straightforward: less time waiting on checkpoint movement during synchronization, and more throughput generating rollouts on fresher weights.

Running trainer and rollout fleet asynchronously means the fleet is always serving a policy that is a few steps behind the trainer. That gap is called **staleness**, and it is a real tradeoff worth naming directly.

Our systems layer does not eliminate staleness. The algorithm has to tolerate some off-policy data. What the systems layer can do is keep the gap bounded and predictable. Delta-compressed updates do that by shrinking policy movement into a routine background operation rather than a stop-the-world event.

This is where the systems point becomes strategic. Most teams do not have one perfectly contiguous giant cluster sitting idle for rollouts. They have capacity scattered across regions, clouds, and availability zones, and assembling one giant sampler fleet in one place is often tedious even if the aggregate GPU count exists.

Once weight updates are small, that fragmented capacity becomes usable for RL instead of stranded. Each rollout cluster can independently download and reconstruct weights from the same shared delta chain, without any direct connection back to the training cluster.

This is not just a hypothetical systems design. Fireworks used this architecture to support Cursor's Composer 2 training run. Federico Cassano wrote that the Composer 2 RL run was "distributed across 3 (sometimes 4) different clusters around the world." ([Federico Cassano on X](https://x.com/ellev3n11/status/2034778708163404102))

That makes the rollout fleet elastic. You can add clusters, remove clusters, or rebalance across regions as capacity and cost change, while keeping all of them pointed at the same stream of policy updates. In Fireworks Virtual Cloud, those clusters are abstracted behind a single control plane so they appear as one uniform capacity pool rather than a set of separate regional deployments that the user has to manage individually.

This architecture is not the right answer in every RL setup.

- If the model is small enough that trainer and rollout inference comfortably fit on one node or one compact cluster, bandwidth is not the main bottleneck and the simpler setup usually wins.
- If checkpoints are emitted so frequently that the delta pipeline cannot distribute and apply one update before the next one matters, then staleness becomes the limiting factor and tighter co-location can make more sense.
- If the rollout stack does not cleanly separate inference from training, then treating rollout workers like a standard inference fleet is a poor fit and the disaggregated design gets less attractive.

For frontier-scale models where those constraints do not hold, this setup is the practical way to turn fragmented capacity into usable RL throughput.

Fireworks supports three ways to run RL:

- **Fully managed RL**: provide the dataset and evaluators, and Fireworks runs the trainer, rollout inference, checkpointing, and weight-update workflow.
- **Tinker-compatible SDK**: customize the training flow while still hosting the GPU-heavy work for both training and inference on Fireworks.
- **Bring your own trainer**: keep the trainer where it is, upload checkpoints to shared object storage, and use Fireworks for rollout serving and weight-update orchestration.

In the bring-your-own-trainer setup, the interface is still a normal inference deployment, with a few RL-specific additions:

- OpenAI-compatible sampling endpoints for rollouts
- a weight update API to signal that a new checkpoint is available
- status reporting for update progress
- sampling features for training-sampling numerical alignment, for example returning selected experts in MoE layers to implement router replay
- fine-grained control of prompt caching behavior during weight updates

The common requirement is the same in every deployment model: make model updates small, verifiable, and routine.

Giant co-located clusters can be the right tool for synchronous pretraining. That does not mean RL rollouts have to live on one giant co-located cluster. The important question is whether your system can keep a distributed sampler fleet updated cheaply and reliably enough to use whatever capacity is available.

If you want to explore that setup, start with the [Fireworks Training SDK introduction](https://docs.fireworks.ai/fine-tuning/training-sdk/introduction), which covers the Tinker-compatible control loop, checkpointing, weight updates, and training/sampling workflow.

If you want to talk through a rollout architecture or pair a Tinker-style trainer with Fireworks-hosted rollouts, email [[email protected]](https://fireworks.ai/cdn-cgi/l/email-protection#f59c9b84809c879c9086b5939c8790829a879e86db949c) or reach out on [Discord](https://discord.gg/fireworks-ai).
