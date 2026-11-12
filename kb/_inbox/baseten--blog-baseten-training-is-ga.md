---
title: Train AI Models When You Want. Deploy on Ultra Performant Infrastructure. Baseten
  Training Is GA.
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-training-is-ga
author: Raymond Cano
published: '2025-10-30'
fetched: '2026-11-12T06:14:10Z'
classifier: null
taxonomy_rev: 2
words: 942
content_sha256: a977f55957ca949a65ade3aadf4677ca64b00e65739bb894c8e859570519d532
---

# Train AI Models When You Want. Deploy on Ultra Performant Infrastructure. Baseten Training Is GA.

News
# Train AI Models When You Want. Deploy on Ultra Performant Infrastructure. Baseten Training Is GA.

After months of working with early users, we have received very positive feedback and are ready to make our training product GA for all Baseten customers.


- Authors
- Date
- October 30, 2025

TLDR

When we launched Baseten Training in beta on May 19, our goals were two-fold: We wanted to bring the Baseten performant infrastructure to AI model trainingWe set out to address core pain points our customers were reporting to us when training models, including: Limited access to compute for trainingOpaque pricing and underutilized capacity Limited control over what’s running under the hood Since then, we’ve worked hand in hand with early users to run thousands of training jobs across various scales, ranging from small LoRA-supervised finetunes to multi-node RL endeavors. We started with the goal of not building Y-A-T-P (Yet Another Training Product). We wanted to build something that addressed the pain we and our customers felt every day while training models. Based on the feedback so far, we’re confident that we’ve built something unique in the market, and we’re excited to make the product even more powerful as users push it to its limits.

Today, we’re excited to announce that Baseten Training is now generally available (GA) to all businesses on Baseten. It delivers tools such as caching, checkpointing, deploy-from-checkpoint, and new training recipes, making it the most agile training infrastructure for developers.

*“Baseten helped us train models to be 23x faster and is projected to save us $1.9M while making the process so easy that even non-ML engineers could get results in under 30 minutes.” - Eric Lehman, Head of Clinical NLP, OpenEvidence*


Baseten Training enables you to train any AI model on any dataset. Some examples include:

- Training of a vision language embedding model for powerful multimodality models
- Training of large sequence LoRAs or full finetunes across any family of models
- Building custom RL environments to empower models to learn your domain.

Baseten’s AI model training leverages the infrastructure we built for performance and developer velocity. But more importantly, it brings together the power of Baseten’s platform in a simple workflow. Developers get easy access to everything needed to go from a fine-tuned script to a fully deployed checkpoint and can run fast inference on Baseten in just a few clicks. All of it, without the overhead of managing GPUs, networking, or distributed orchestration, which saves our customers countless hours.

"Our goal at Oxen has always been to get customers from raw datasets to production-ready models as fast as possible. But building and managing GPU infrastructure ourselves would have pulled us away from where we add the most value. Whenever I’ve seen a platform try to do both hardware and software, they usually fail at one of them. That’s why partnering with Baseten to handle infrastructure was the obvious choice. It lets us stay focused on delivering the best possible experience for our customers." — Greg Schoeninger, CEO, Oxen AI


With Baseten Training, you can:

- **Run multi-node jobs** with persistent storage. Cache models and datasets to power lightning-fast iteration and experimentation
- **Deploy checkpoints** directly to inference endpoints
- **Track metrics** at granular levels: per GPU, per node, and per run
- **Spin up jobs on demand**, with rapid access to H100s and other GPUs, and only pay for the compute you use

Baseten handles the infrastructure so you can focus entirely on training your model.

We’ve trained and tuned plenty of models ourselves. And like most developers, we’ve felt the pain of existing AI model training solutions, such as limited access to compute, opaque pricing, and limited control over what’s running under the hood.

We built Baseten Training to offer performance, reliability and a developer-first experience with:

- Flexible infrastructure that scales from a single GPU to an entire cluster.
- First-class observability with per-GPU and multinode metrics.
- Simple checkpointing, logging, and deployment workflows.

Since the beta launch, we’ve made significant performance, scalability and usability improvements to bring Baseten Training to GA. Here are the highlights of the improvements we have made:

- **ML Cookbook** offers a collection of open-source recipes that make it easy to get started training on Baseten. We have included ready-made examples for Gemma3, GPT OSS 20B and 120B, Qwen3 30B, Orpheus, and Whisper. Each recipe is a known-good configuration designed to help new users get to “training success” faster.
- **UI Improvements** bring developers a refreshed, hardened experience across the entire training UI. We now include per-GPU and multinode metrics, a new Training Projects page, and streamlined job management and checkpoint tracking – all in the same interface.
- **Resume from Checkpoint** enables you to restart any job exactly where it left off. You can now choose the latest checkpoint or pin a specific one to resume from.
- **Deploy from Checkpoint** provides full support for deploying fine-tuned models for chat completion and audio transcription, with CLI wizard and UI support.
- **New Infiniband-Backed Clusters** bring two new high-performance node pools. Both run on Infiniband fabric, enabling faster communication and scaling for distributed training.
- **Logging & Observability Improvements** with improved CLI log handling, better checkpointing transparency, and more visibility into infrastructure-level events.
- **Faster Multinode Deployments** with an optimized orchestration ensure the leader node boots before workers, improving reliability and reducing startup time.

Most model training systems constrain you with fixed node sizes, rigid runtimes, or capped modalities.

Baseten Training flips that model: you bring your training job, and we provide the scalable infrastructure to run it fast.

Ready to Train? [Get started with Baseten Training](https://app.baseten.co/training)
