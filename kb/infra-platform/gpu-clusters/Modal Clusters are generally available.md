---
title: Modal Clusters are generally available
kind: blog
topic: infra-platform
subtopic: gpu-clusters
secondary_topics:
- inference/serving
summary: Modal Clusters reach GA via a `@modal.clustered` decorator, offering gang-scheduled
  multi-node GPU jobs with RDMA at up to 6.4 Tbps; cites GLM 4.7 weight sync (~717GB
  BF16, under 2s over RDMA vs ~2min over 50Gbps TCP) and PD-disaggregated KV-cache
  transfer for Llama 3.1 70B as motivating workloads.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/modal-clusters-generally-available
author: null
published: '2026-10-01'
fetched: '2026-10-02T06:10:59Z'
classifier: claude
taxonomy_rev: 2
words: 1298
content_sha256: c417dd7c9c339385aab2d4d6ecbbe68f8d2bcaa36b5a70b73f210abdb3c0c9d2
---

# Modal Clusters are generally available

Organizations need to own their intelligence to be successful. Training and serving that intelligence at scale, however, requires petaFLOP/s of compute and terabit/s of networking, spread across many nodes. But owning intelligence doesn’t need to mean owning that hardware.

For the past 1.5 years, we’ve been battle-testing a new primitive: Modal Clusters. Today, we’re excited to announce that they are generally available through a single decorator, `@modal.clustered`:

```
@app.function(gpu="B300:8")
@modal.clustered(size=4, rdma=True)
def train_model():
    cluster = modal.Cluster.from_context()
    container_ips = cluster.container_ips()
    container_rank = cluster.container_rank()
    world_size = len(container_ips)
    main_addr = container_ips[0]
    print(f"{container_rank=} {world_size=} {main_addr=}")
    ...
```
Modal Clusters seamlessly integrate with all existing Modal primitives. Write your checkpoints to [Volumes](https://modal.com/docs/guide/volumes), load data in through [Cloud Bucket Mounts](https://modal.com/docs/guide/cloud-bucket-mounts), and orchestrate your jobs with [Queues](https://modal.com/docs/guide/queues). On top of existing integration, you get:

- **Communication between nodes via InfiniBand verbs at up to 6.4 Tbps** , automatically configured for PyTorch and NCCL
- **Your code running on a cluster within seconds of requesting it** , billed by the second
- **Our robust, automated [GPU health assurance and remediation](https://modal.com/blog/gpu-health)** , now extended to RDMA health

Elsewhere, on-demand cluster access means paying by the hour or taking a reservation. On Modal, you run whenever you want and only pay for what you use.

## Reimagining the Modal stack

Clusters (groups of containers) are a fundamentally new unit of work in Modal’s stack. In supporting them, we had to build new systems at each layer of our stack.

### Gang scheduling: placing N nodes at once

Modal’s traditional scheduler is greedy. All nodes in the fleet constantly poll for new work to do, and our scheduler checks its backlog for eligible work, assigning the work if it fits. There are heuristics around placement, fragmentation, and cost, but fundamentally, the scheduler makes the choice about whether a node should pick up an item on a per-node basis.

For multi-node scheduling, a single-node view is not sufficient - the atomic unit for scheduling expands from a single node to N nodes. This meant we had to build an entirely new scheduler with an explicit [observe, plan, and act loop](https://en.wikipedia.org/wiki/OODA_loop): look at the whole fleet, decide on a placement for every pending cluster, then act on it. This is the direction the rest of Modal’s scheduling systems are moving in too. On each iteration, the gang scheduler:

1. Collects metadata for all multi-node workloads in the system
2. Assigns all workloads to nodes, grouping by AZ and network ID
3. Spins up any new capacity for workloads which do not currently fit
4. Sends schedule notifications to all nodes which are alive

The gang scheduler pulls from the same capacity pool as everything else on Modal, allowing for cluster acquisition in seconds. This is the fastest time to get a multi-node cluster on the market, and the only place where you pay truly serverless pricing.

### RDMA support

Multi-node workloads move a lot of bytes. [Every training step](https://modal.com/blog/reinforcement-learning-infrastructure-problem) of GLM 4.7 has to sync ~717 GB of BF16 weights from the trainer to the rollout engine: nearly two minutes over 50 Gbps TCP, under two seconds over RDMA, repeated for thousands of steps. For inference, prefill-decode disaggregation on Llama 3.1 70B moves ~10 GB of KV cache per 32k-token prompt, and it has to arrive within a time-to-first-token budget of a few hundred milliseconds.

RDMA (Remote Direct Memory Access) allows GPU or CPU memory to be transferred between hosts over the network without ever passing through kernel-space. Skipping the software layer allows RDMA to push up to 6.4 Tbps! This capability is critical for most multi-node workloads - training requires it for DDP all-reduce and all types of model parallelism; inference requires it for KV cache transfer when doing PD disaggregation.

RDMA is notoriously difficult to support. Each cloud provider has a slightly different implementation, requiring different drivers, environment variables, and userspace libraries.

**We set out with an ambitious goal: hide all of this complexity behind a single flag, `rdma=True`.** Today, you can set this flag, and any workload using PyTorch with NCCL will work out of the box. We’ve automated RDMA setup across many clouds, giving you deep access to on-demand clustered capacity without any of the headaches.

`rdma=True` sets up This integration was still not good enough for us. Since Modal runs a multi-tenant compute environment, we prefer the secure gVisor container runtime over `runc`. However, it did not have RDMA support, so we [built it into gVisor](https://github.com/google/gvisor/pull/13964) ourselves. We’ve upstreamed these changes so that other folks in the OSS ecosystem get access to secure RDMA.

## Customers building intelligent applications on Clusters

We’re proud of the cutting-edge research and production applications built on top of multi-node clusters.

### Decagon trained a better customer experience agent

[Decagon](https://decagon.ai) builds AI agents for customer experience. In partnership with Modal, Decagon fine-tuned open models with up to a trillion parameters using [Miles](https://github.com/radixark/miles) on Modal Clusters, tailoring them to the demands of customer interactions with a focus on response quality and inference efficiency. As part of this collaboration, Modal [contributed LoRA support](https://github.com/radixark/miles/pull/1361) to Miles and helped establish a stable, open training recipe.

“Model performance is central to the customer experience at Decagon. Our agents need to understand the nuances of each business and reliably handle complex customer conversations. Fine-tuning lets us shape model behavior around those demands, but doing it at trillion-parameter scale is a substantial infrastructure challenge. Modal Clusters helped us train at that scale, so we could focus on improving the quality and reliability of our agents.”

Cyrus Asgari, Research Lead, Decagon


![Stacked Decagon chat windows for several brands, with an agent asking a customer how it can help](https://modal-cdn.com/blog/images/decagon-clusters-ga.webp)

### 1x pre-trains NEO

[1x](https://www.1x.tech) is building NEO, the home robot. Behind NEO is a world model that 1x pre-trains on Modal Clusters: multi-node B300 clusters with RDMA for the big runs, and fleets of single-node jobs for the evals that tell them how the model is doing. The same scheduler handles both, so 1x can burst up to hundreds of GPUs when they need to fan out experiments and scale back down between runs.

“Building NEO requires flexible workloads; some days it’s a few multi-node runs on a single spine, and other days we want to kick off a bunch of single-node evals at once to deeply understand model performance. Modal Clusters let us scale up to hundreds of B300s with RDMA, then spin them down when we’re done, with minimal overhead. We only pay for what we use, and the team gets to think about how to build intelligence for NEO instead of GPUs and where to find them.”

Sam Sinha, Head of World Model Lab, 1x


### Runway’s frontier models bring ideas to life

[Runway](https://runway.com) is building real-world intelligence for the world model era. Their latest frontier video generation and editing models, [Gen-4.5](https://runway.com/research/introducing-runway-gen-4.5) and [Aleph 2.0](https://www.youtube.com/watch?v=8vAqhBxCxc0), generate production-quality video in seconds. Each generation uses Modal Clusters, spreading inference across multiple nodes, and Modal’s autoscaler scales those clusters as a unit across our global compute pool.

“Multi-node inference is a challenging infrastructure problem. It makes elasticity hard, which is table stakes for inference workloads. Modal’s platform, with out of the box features like clustering and configurable autoscaling, has helped us rapidly scale multiple production inference workloads to meet growing demand.”

Kamil Sindi, CTO, Runway


## Get started today

Modal Clusters are available to all workspaces today. Whether you’re scaling out inference or post-training a frontier model, all it takes is one line of code to scale out your Modal App. Cluster size is bounded by your plan’s GPU limits, so if you’re planning something big, [reach out](https://modal.com/slack).

To get started:

1. Install Modal: `pip install modal`
2. Create an account: `python -m modal setup`
3. Check out our [Multi-node Clusters Documentation](https://modal.com/docs/guide/multi-node-clusters)

We can’t wait to see what you build.
