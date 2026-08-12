---
title: Introducing NVIDIA Nemotron 3.5 Lightning
kind: blog
topic: models
subtopic: releases
secondary_topics:
- inference/optimization
summary: NVIDIA Nemotron 3.5 Lightning is a 30B MoE model (3B active) distilled from
  Nemotron 3 Ultra for agentic workloads, achieving ~4x higher throughput and 30%
  lower task completion time than comparable open models, now available on Baseten
  Dedicated Inference.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-nemotron-35-lightning/
author: Marylise Tauzia; Albert Lee
published: '2026-08-11'
fetched: '2026-08-12T06:27:59Z'
classifier: claude
taxonomy_rev: 2
words: 653
content_sha256: 8b1f40b9aa2abfb28c38f6f6b94a00efda3beec818886f3a9ecc1297941f3782
---

# Introducing NVIDIA Nemotron 3.5 Lightning

![Nemotron 3.5 Lightning](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786393631-nemotron-35-lightning-blog-4x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

NVIDIA Nemotron 3.5 Lightning is a 30B MoE model with 3B active parameters and distilled from Nemotron 3 Ultra, built for agentic use cases. Nemotron 3.5 Lightning achieves leading accuracy on agentic tasks and also 4x higher throughput compared to other leading open models in its class and 30% lower time to task completion. Now available on Baseten Dedicated Inference, Lightning provides the high-throughput your always-on agents require.

[NVIDIA Nemotron 3.5 Lightning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) is now available on Baseten through Dedicated Inference, and it runs on NVIDIA accelerated infrastructure.

Nemotron 3.5 Lightning is distilled from NVIDIA [Nemotron 3 Ultra](https://www.baseten.co/blog/nvidia-nemotron-3x-model-family/), a powerful model built for agentic tasks. Nemotron 3.5 Lightning inherits core agentic capabilities while optimizing for the efficiency, high throughput, and rapid token generation required for the specialized, high-volume agentic workflows highlighted below:

- Personal agents: Manage email, calendar, projects, and bookings.
- Financial services: Extract data, check policies, monitor risk, and summarize reports.
- Cybersecurity: Enrich alerts, classify incidents, query logs, and prepare findings.
- Telecom: Triage network alarms, optimize configurations, and answer billing questions.
- Retail: Enrich catalogs, resolve inventory exceptions, and assist product discovery.

## A small and speedy architecture for agents

Nemotron 3.5 Lightning is a 30B Mixture-of-Experts (MoE) model with 3B active parameters. Designed specifically for always-on agents, this hybrid MoE architecture balances efficient processing with the reasoning power needed for complex, multi-turn tasks. It supports a 1M token context window, allowing agents to maintain deep context across long interactions.

The model is *lightning*-fast; its 3B active parameters and multi-token prediction architecture enable almost 4 times higher throughput compared to other open models of similar size, and its rapid token generation capabilities allow agents to complete tasks more quickly.

## 30% Lower task completion time

Nemotron 3.5 Lightning delivers performance on quality benchmarks comparable to other leading open models of similar size and can complete tasks 30% faster.

![PinchBench Accuracy vs. Time To Complete 10,000 Tasks](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786454938-img_1160.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) PinchBench Accuracy vs. Time To Complete 10,000 Tasks

Notably, Nemotron 3.5 Lightning’s speed advantage enables lower task-completion times through faster reasoning. By completing each reasoning step more quickly, agents can move from planning to execution sooner, iterate rapidly, and finish complex workflows in less time.

### Fine-tuning Lightning to improve quality

Baseten worked with [CodeRabbit](https://www.coderabbit.ai/), the AI code review application, to provide early access to Nemotron 3.5 Lightning on Baseten. The goal was to leverage the model to run a routing decision at the start of every code review. Nemotron 3.5 Lightning reads a code change and assigns complexity tags, and a scorer converts those tags into a review configuration. It's a very high-volume model call, which made it the right place to test whether a smaller model could carry a real piece of the pipeline.

CodeRabbit post-trained Lightning in two stages, both on [Baseten Training](https://docs.baseten.co/training/index). The first was supervised fine-tuning (SFT), using [NVIDIA NeMo AutoModel](https://github.com/nvidia-nemo/automodel) on managed H100 Training Jobs, which moved exact route agreement from 75.8% to 80.4% on a frozen 1,000-task evaluation. For the second they ran reinforcement learning with verifiable rewards through NVIDIA [NeMo RL,](https://github.com/nvidia-nemo/rl) scored against CodeRabbit's own routing policy. Cohen's kappa went from 0.461 to 0.544 and route accuracy held.

![SFT loss on managed H100 training jobs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786394683-sft_loss_h100_training_upscaled_4x.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) SFT loss on managed H100 training jobs

The finished adapter went straight to [Dedicated Inference](https://docs.baseten.co/inference/overview). It loads as a single rank-16 LoRA over stock Nemotron 3.5 Lightning and serves on a relatively small GPU like A100. Throughput measured 314.82 aggregate output tokens per second across eight concurrent requests. On the same workload the tuned model achieved ~4% higher accuracy than the baseline, ran at roughly half the cost of the baseline API calls, and produced 63.4% fewer output tokens getting there.

## Deploy Nemotron 3.5 Lightning on Baseten today

Achieve higher accuracy through superior speed. [Deploy Nemotron 3.5 Lightning](https://www.baseten.co/library/nemotron-35-lightning/) on Baseten Dedicated Inference to power your autonomous agents with the fast reasoning they need to solve complex tasks.
