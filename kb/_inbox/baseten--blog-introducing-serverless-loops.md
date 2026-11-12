---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-serverless-loops
author: Kimbrian Canavan
published: '2026-11-06'
fetched: '2026-11-12T06:07:02Z'
classifier: null
taxonomy_rev: 2
words: 676
content_sha256: e7fe4b8b04549546d4b98e0ca964637acce0b7d41d92efbc7b37ef202b3374d9
---

# The platform for inference, training, and execution | Baseten

Product
# Introducing Serverless Loops: frontier RL training for everyone

Loops is now generally available. Post-train on frontier open models and deploy directly to Baseten Dedicated Inference.


- Authors
- Date
- November 6, 2026

Today, Serverless Loops is generally available. Loops is a training SDK for supervised fine-tuning (SFT) and reinforcement learning (RL) on frontier open models, with a direct path to production. Train through a familiar Tinker-compatible API, evaluate your checkpoints, and deploy the resulting model to Baseten [Dedicated Inference](https://docs.baseten.co/inference/overview).

With the API, you focus on the training signal rather than worrying about all the finicky details of building and operating a robust, large-scale training backend. We take care of the GPUs, the kernels, the model architectures, as well as the performance and numerical correctness of the distributed training infrastructure.

As part of our initial launch, you will have access to a selection of popular open-weight models for post-training at a 256k context length for both SFT and RL. We have a competitive per-token billing model (see full details below), so you only pay for what you use.

One of our simplest and favorite features of Serverless Loops is that you can deploy trained models straight onto Baseten’s production inference platform with a single click!

Baseten loads your adapter alongside its base model and creates a production endpoint on the same Baseten Inference Stack that serves 15B+ inference requests per day with full autoscaling, deployment management, and inference metrics. You don’t have to do that, of course, as you have full access to download your weights in the standard Hugging Face Safetensors format.

For this GA release, we’ve also improved how Loops handles transient network errors and GPU failures, reduced startup overhead, and accelerated weight transfers between trainers and samplers. These improvements let us support more concurrent workloads for our customers.

We validate Serverless Loops with end-to-end RL experiments alongside our numerical tests. We train with tasks from [τ-bench](https://taubench.com/) across retail, airline, and banking domains and evaluate on a set of held-out hard tasks:

Teams at NVIDIA, Datadog, LangChain Labs, and Ambience Healthcare have already been using Loops:

- NVIDIA post-trained their own Nemotron Super 3.5 VL model to see how it learns across text and vision—from intent classification and receipt extraction to RL for visual object counting. The post-trained model improved intent classification accuracy from 76.8% to 94% and achieved 87% validation F1 on receipt extraction.
- Datadog tests new training ideas for their SRE agent on frontier open models using multi-turn agentic RL.
- [LangChain Labs](https://www.baseten.co/resources/customers/langchain#from-training-to-production-with-baseten-loops) post-trains custom models on agent traces to solve difficult tasks in LangSmith Engine, such as reading a GitHub repository to diagnose why an issue is happening, then drafting the prompt or code change that goes into the PR.
- Ambience Healthcare post-trained models to handle the nuances of clinical language, from correcting transcription errors to accurately capturing medical terminology and formatting.

To get started:

1. Create a [Baseten API key](https://docs.baseten.co/organization/api-keys).
2. Follow the [Loops quickstart](https://docs.baseten.co/loops/quickstart) to create your first run.
3. Bring your dataset or use the [reinforcement learning guide](https://docs.baseten.co/loops/rl) to connect your reward function.
4. Adapt an example from the [Loops cookbook](https://github.com/basetenlabs/loops-cookbook) that fits your agent’s runtime and sandbox needs.

If you prefer dedicated throughput, [request dedicated capacity](https://www.baseten.co/talk-to-us/loops-signup/). If you’re bringing your own training stack, explore Baseten [Training Jobs](https://docs.baseten.co/training/overview) for managed GPU infrastructure or [RL Rollouts](https://docs.baseten.co/rl-rollouts/overview) for scalable rollouts with your own trainer.

We’ve also got a lot of exciting features lined up: new models, quantization techniques, score centering, and more! We’ll be releasing a series of technical write-ups explaining how we tackled some of the trickier problems in our training code and infrastructure.

Look out for explainers on how we find kernel bugs, how we select the LoRA targets for our trainer, and how we made the MoE LoRA kernels in our inference engine over 4x faster. We'll also be sharing details on how we've optimized cross-cluster weight syncs and how we make decisions to balance efficiency and raw speed in our trainer and sampler.

We’re excited to see what you create with Loops.
