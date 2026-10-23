---
title: Introducing our Training API
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/introducing-training-api
author: Kailash Ranganathan; Micah Yong
published: '2026-10-22'
fetched: '2026-10-23T06:15:58Z'
classifier: null
taxonomy_rev: 2
words: 1554
content_sha256: a18a0fef45c56d16961db4f44e38f182de9c1b53567ea17dc6028a2d15a5a86b
---

# Introducing our Training API

Thinking Machines’ [Tinker](https://thinkingmachines.ai/news/announcing-tinker/) changed how people do post-training. You write the training loop in plain Python on your laptop, and Tinker runs the forward and backward passes on its GPUs. We’re big fans, and so are many of the teams we work with.

As those teams scale up, however, they keep raising the same two problems:

1. Per-token pricing gets expensive once you’re running dozens of experiments.
2. You can only use the models and features the provider decides to support.

We think a good API deserves more than one implementation. Today we’re releasing [Spindle](https://github.com/modal-projects/spindle), an open-source, Tinker-compatible training server that runs in your Modal workspace. Because you own the server, you can customize anything in it, and you pay for GPU time instead of tokens. Our default configs are tuned to maximize GPU utilization out of the box, and we plan to keep shipping optimizations to push price-performance further.

All it takes is a single command to deploy a server:

`spindle deploy`
Then, run your training script against the server.

## When should your team use Spindle?

Modal now covers the whole post-training stack, from on-demand clusters to a library that runs the loop for you. Where do you start?

![The Modal post-training stack: Modal Dojo for hands-off training, Spindle for writing your own loop, and Modal primitives for full control](https://modal-cdn.com/cdnbot/modal-training-stack-recipes_cc70350d.png) 

If you’d rather not write a training loop, use our training library, [Modal Dojo](https://modal.com/blog/get-started-with-llm-training-on-modal), which we released yesterday. Simply bring a model and a dataset, and Dojo will handle the rest. If you want to own everything down to the cluster, Modal gives you the raw primitives: [on-demand multi-node clusters](https://modal.com/blog/modal-clusters-generally-available) and [sandboxes for RL rollouts](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds).

Spindle sits in between. You write the training loop with your own losses, rewards, and environments, and Spindle handles the distributed training underneath it. It supports full-parameter training and multi-LoRA on a wide range of open models. For teams running many experiments, Spindle supports hundreds of concurrent training runs at similar performance and significantly reduced cost compared to closed-source APIs.

## Under the hood

Spindle’s Tinker-compatible API is backed by a distributed control plane that handles request and session management, and container autoscaling built on [Modal Functions](https://modal.com/docs/guide/functions).

Spindle’s backend features a set of disaggregated trainer engines and inference pools. Note that they don’t have to run on the same accelerators or precisions! We’ve [written about](https://modal.com/blog/toward-rl-on-mixed-precision-mixed-accelerator-samplers) how to keep RL stable in these cases and take advantage of the inherent cost savings and higher GPU availability.

Our whole system is built on top of Modal primitives: [Modal Clusters](https://modal.com/blog/modal-clusters-generally-available) enable incoming requests for large-models to be scheduled on dynamically-available RDMA-connected nodes without requiring a cluster reservation, [Modal Volumes](https://modal.com/docs/guide/volumes) provide fast, durable checkpointing, and [Modal Servers](https://modal.com/blog/serverless-servers) provide a fast inference layer. While building multi-LoRA training, we’ve also upstreamed various improvements to [Miles](https://github.com/radixark/miles/pull/3320) and [SGLang](https://github.com/sgl-project/sglang/pull/41951), and we’ll continue investing in the open-source ecosystem.

Designing a performant multi-tenant training system involved overcoming a variety of challenges which we had to carefully think about. This led to a lot of exciting work that now powers core components of Spindle, including multi-client batch scheduling, async checkpointing, delta weight syncs, and a custom inference router for multi-LoRA and KV-aware request routing. You can read more about our design [here](https://github.com/modal-projects/spindle/blob/main/docs/design.md).

## Spindle in action

Over the past couple months, we’ve run an expansive set of RL workloads across [math reasoning, agentic coding, and search agents.](https://github.com/modal-projects/spindle/blob/fc1ba7e00e5ff12e56ed8541373da5e870fecf11/docs/lora_validation.md) Here are a few examples.

### Post-training a multi-turn search agent

We reproduced [Training Search Agents with GRPO](https://jasperlu.com/blog/training-search-agents-grpo/) by Jasper Lu, which trains `gpt-oss-20b` to perform multi-turn agentic search over a corpus of SEC filings with keyword-matching, grep, and read tools. The task is to curate a set of documents that answer a query.

We pulled [his open-source code](https://github.com/jasper-lu/sec-search-rl/tree/a461bf07ac96e78bffd6fe44112d9f8a74304223), changed only the `BASE_URL` and `API_KEY` to point at our Spindle deployment, and hit `uv run`. That was it.

Comparing two Spindle seeds, our own rerun of the same code on Tinker, and the training results that the author published, we see that Spindle tracks both to within 0.01 reward across all updates.

![Search-agent training reward for two Spindle seeds, a Tinker rerun, and the author's published run across 24 updates](https://modal-cdn.com/cdnbot/spindle-fig4-training_2f167efd.png) 

We then scored checkpoints at updates 16, 20, and 24 on the same 32 held-out queries and observed similar parity:

![Search-agent held-out F4 and curated recall at checkpoints 16, 20, and 24](https://modal-cdn.com/cdnbot/spindle-fig3-heldout_4e6b10aa.png) 

### Extending Spindle to fit your workload

If you’re training through a closed API, you’re limited to whatever models and features the provider decides to support. When you need something they don’t have, there isn’t much you can do besides wait or find a workaround.

Since Spindle is open-source and runs in your Modal workspace, you can make changes as needed, and our config layer makes this incredibly simple. For example, when we wanted to train Qwen3.5-9B on [long-horizon software tasks](https://modal.com/docs/examples/swe_gym), we only had a default 16k-context config at the time. With two simple changes, we bumped it to 256k in the config:

```
class Config(Qwen35_9B_16k):
    ...
    max_context_length = "256k"     # was "16k"
    context_parallel_size = 4       # was 1
```
![SWE-Gym training: average reward, batch time, and logprob difference across 8 clients](https://modal-cdn.com/cdnbot/swegym-grpo-qwen35-9b_74b26719.png) 

This run trained for about 3 days on preemptible GPUs, resuming from checkpoints automatically whenever a machine was reclaimed. It also had 8 clients sharing the same GPUs through multi-LoRA, which means you can do 8 long-context ablations for the cost and time of one. More on that next.

## Compounding cost savings

Agentic RL spends most of its time generating rollouts, requiring both long decode times and execution latency. While a client waits on long multi-turn rollouts, its trainer GPUs mostly sit idle. Depending on the workload, we’ve observed that a trainer serving a single client (even running async RL) is only busy for less than half the time.

In fully async RL, the standard approach to trainer underutilization is to scale out inference compute and allow slightly off-policy rollouts to always feed the trainer. Multi-LoRA fits perfectly with this approach: for a fixed trainer size, you can scale out inference for a single run, scale up the number of runs on a fixed inference budget, or do both!

Spindle’s multi-LoRA backend puts trainer idle time to work by letting many clients share the same trainer. While one client waits on rollouts, the trainer runs another client’s training step. When several clients share the same GPUs, each run costs a fraction of what it would on dedicated compute.

To quantify this, consider the same simple GRPO job (a 27B model on DAPO-math) with one to eight clients sharing the same trainer and inference GPUs (4×H200s for training, 12×B200s for inference).

![Total output throughput, throughput per client, update interval, and cost per client for 1, 2, and 4 independent clients](https://modal-cdn.com/cdnbot/cost-13d3bmd62_d1c5322e.webp) 

Looking at the trainer’s utilization, we can see where the cost benefits come from:

![GPU busy timeline for 1, 2, and 4 clients: 37.0%, 70.0%, and 87.7% busy](https://modal-cdn.com/cdnbot/utilpbvq9iq1_393ce946.webp) 

With a single client, the trainer has long idle periods. With four clients interleaving their training steps, it stays \~88% busy. Adding clients lowers the cost of each run, at the expense of each run finishing a bit more slowly. Note that there is a limit: past four clients here, we observe thrashing of the trainer which significantly degrades per-client throughput.

The same effect scales to agentic workloads. Here are some workloads we ran on Spindle, from single-turn math to long-horizon agents, each compared with running the same script on Tinker:

| Workload | Setup | Clients | $/1M output tokens | Price reduction vs. Tinker | 
|---|---|---|---|---|
| **DAPO-math**, single-turn (Qwen3.8-27B) | Tinker | 1 | $9.77 | — | 
|  | Spindle: 4×H200 train, 12×B200 inference | 2 | $3.57 | −63% | 
|  | Spindle: 8×H200 train, 8×H200 inference | 8 | **$1.99** | −80% | 
| **Search agent**, up to 40 turns (gpt-oss-20b) | Tinker | 1 | $5.06 | — | 
|  | Spindle: 8×H200 train, 16×H200 inference | 4 | $4.06 | −20% | 
|  | Spindle: 8×H200 train, 16×H200 inference | 8 | **$3.80** | −25% | 
| **SWE-Gym**, 256K context (Qwen3.8-27B) | Tinker | — | $15.04 | — | 
|  | Spindle: 8×B200 train, 8×B200 inference | 4 | $6.17 | −59% | 
|  | Spindle: 8×B200 train, 12×B200 inference | 8 | **$5.82** | −61% | 

Paying for the GPUs instead of tokens means every bit of extra throughput you get out of them lowers your price per token. The broader takeaway from these experiments is that if you keep your GPUs busy, for example by running several experiments at once, Spindle offers much better price-performance than closed-source APIs.

## Try it now

To get started, follow the [setup instructions](https://modal.com/docs/guide/spindle) to deploy Spindle in your Modal workspace.

Spindle is open source, and we want to build it with the people using it. If you hit a bug or need a model or feature we don’t support yet, [open an issue](https://github.com/modal-projects/spindle/issues). You can open a PR directly for new model configs or performance tuning on existing ones. To upstream anything bigger, come chat with us in [our Slack](https://modallabscommunity.slack.com/join/shared_invite/zt-3f0ci4ckg-Oo7wIlg3zTrSFSbpbyWwSg) so we can discuss your ideas!

We’re still in beta, and we’re cooking up performance optimizations, improved autoscaling, new features and training recipes, and much more. Stay tuned and happy Spindling! 🍽️
