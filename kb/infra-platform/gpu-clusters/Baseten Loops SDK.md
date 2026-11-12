---
title: Baseten Loops SDK
kind: blog
topic: infra-platform
subtopic: gpu-clusters
secondary_topics:
- models/reinforcement-learning
summary: Early-access announcement of Baseten Loops, a Tinker-compatible training
  SDK exposing forward_backward/optim_step/sample primitives for asynchronous RL at
  131K+ sequence lengths with direct deploy to production inference.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-the-baseten-loops-sdk
author: Raymond Cano
published: '2026-05-08'
fetched: '2026-11-12T06:06:54Z'
classifier: claude
taxonomy_rev: 2
words: 718
content_sha256: 871c1e62ad66427c615ab4cc8f6e7fe21ef1fed9bf1dbbcd13bb94bd8b65a311
---

# Baseten Loops SDK

Product
# Introducing Baseten Loops

A training SDK that supports long sequence length, async RL, and one-click checkpoint deploys on the Baseten Inference Stack.


- Authors
- Date
- May 8, 2026

TLDR

Loops is a training SDK that abstracts away hardware and enables researchers to focus solely on their training scripts. By bringing Baseten's inference expertise to RL, Loops offers dedicated infra for predictable performance and a one-click path from training directly to production inference. ML teams can train and deploy RL-specialized models with asynchronous RL and 131K+ sequence length training using Baseten Loops, now available in early access. We're excited to work with leading companies like Harvey and OpenEvidence as early partners.

Over the past year, open-source models have continued to scale their architectures and intelligence. Demand for post-training has surged to specialize these models through supervised finetuning (SFT) and reinforcement learning (RL). As ML teams build more advanced main agents, voice systems, and long-horizon reasoning systems, RL is quickly becoming the default method to achieve frontier-level, task-specific performance.

Previously, RL at scale was a capability restricted to the largest AI research labs. Frontier-scale runs require stitching together a trainer, a high-throughput inference engine, and a rollout orchestrator on multi-node hardware setups. Open-source libraries have made real progress, but with the largest models, they fall short.

When ML engineers and researchers try to scale their post-training workloads on current solutions, they typically run into a few major challenges:

- **Open-source library gaps:** Existing RL libraries get you to a working small-scale run, but breaking into frontier-scale territory both on size, architecture and context length requires manual testing of memory and parallelism strategies the framework doesn’t come with.
- **Deploying to inference:** Training on one platform and serving on another breaks the development loop. There are no set recipes for LoRA merging, and quantizing across formats to get them into production is painful, slow workflow.
- **Slow rollouts:** Many of today’s libraries are synchronous, forcing sampling and training to take turns. Every time the model updates, sampling pauses while new weights are pushed. For agentic RL with long, multi-turn rollouts, this causes runs to slow down significantly or silently hurts model quality by using stale rollouts.
- **Unpredictable performance:** Shared-infra serverless platforms behave like a black box with identical runs taking minutes one day and hours the next.

Baseten Loops enables you to scale post-training from your first RL run to production inference on a single platform. Loops simplifies a full gradient step into just a few lines of code using familiar primitives like `forward_backward`, `optim_step`, and `sample`. Behind the scenes, it manages all the complexity of executing that step at frontier model sizes and 131K+ sequence lengths including sharding, memory management, and parallelism strategy.

You write the algorithm and Loops handles the infra. Loops is Tinker-compatible, allowing you to migrate with a single import change while unlocking new capabilities like:

- **Train → deploy loop:** Models trained with Loops promote directly to Baseten [Dedicated Inference](https://www.baseten.co/products/dedicated-deployments/) with one command.
- **Async & bounded off-policy RL:** Loops automatically implements bounded off-policy learning. Training and sampling overlap seamlessly, with no custom sync logic required.
- **Long-context RL:** Built for agentic workflows with 131K+ sequence length capabilities out of the box.
- **Predictable performance:** With dedicated infra, Loops provides stable, predictable throughput and run-time for the same script, so you always know exactly how long a run will take and can confidently plan.

In our beta, we are currently supporting SFT and RL of dense and MoE models including the Qwen3.5/3.6 family and Kimi family. Other models including the Nemotron, Deepseek, GLM, and MiniMax series will follow shortly.

Looking forward, we are building **Online and Environment-Driven RL**, where training agents interact continuously with live environments. We are also building **Rollout Manager**, a tool that decouples your RL inference from your trainer by providing seamless weight syncs as a platform directly into inference. Beyond that, we're exploring end-to-end pipelines between training and production inference to eliminate the friction of quantizations and the inference/trainer runtime mismatch, so companies can close the loop from the first step of training to serving models in production.

The Baseten Loops SDK is currently in early access. If you’re interested in scaling your post-training, fill this [form](https://www.baseten.co/talk-to-us/loops-signup/) out and a member of our team will reach out.
