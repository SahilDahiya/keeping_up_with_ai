---
title: The RLVR Revolution — with Nathan Lambert (AI2, Interconnects.ai)
topic: models
subtopic: fine-tuning
secondary_topics:
- models/reasoning
summary: Nathan Lambert discussion of RLVR and why reinforcement learning is reshaping
  post-training for reasoning models.
source: latent-space
url: https://www.latent.space/p/the-rlvr-revolution-with-nathan-lambert
author: Latent Space
published: '2025-07-31'
fetched: '2026-07-11T05:17:00Z'
classifier: codex
taxonomy_rev: 1
words: 679
content_sha256: 246f73588815a1a2ebea14c24bfac55c4ca078f441006aa2f1afba59fb84c7ee
---

# The RLVR Revolution — with Nathan Lambert (AI2, Interconnects.ai)

We first had **Nathan** on to give us his RLHF deep dive when he was joining **AI2**, and now he’s back to help us catch up on the evolution to RLVR (Reinforcement Learning with Verifiable Rewards), first proposed in his **Tulu 3** paper. While RLHF remains foundational, RLVR has emerged as a powerful approach for training models on tasks with clear success criteria and using verifiable, objective functions as reward signals—particularly useful in domains like math, code correctness, and instruction-following. Instead of relying solely on subjective human feedback, RLVR leverages deterministic signals to guide optimization, making it more scalable and potentially more reliable across many domains. However, he notes that RLVR is still rapidly evolving, especially regarding how it handles tool use and multi-step reasoning.

We also discussed the **Tulu** model series, a family of instruction-tuned open models developed at AI2. Tulu is designed to be a reproducible, state-of-the-art post-training recipe for the open community. Unlike frontier labs like **OpenAI** or **Anthropic**, which rely on vast and often proprietary datasets, Tulu aims to distill and democratize best practices for instruction and preference tuning. We are impressed with how small eval suites, careful task selection, and transparent methodology can rival even the best proprietary models on specific benchmarks.

One of the most fascinating threads is the challenge of incorporating tool use into RL frameworks. Lambert highlights that while you can prompt a model to use tools like search or code execution, **getting the model to reliably learn when and how to use them through RL is much harder**. This is compounded by the difficulty of designing reward functions that avoid overoptimization—where models learn to “game” the reward signal rather than solve the underlying task. This is particularly problematic in code generation, where models might reward hack unit tests by inserting pass statements instead of correct logic. As models become more agentic and are expected to plan, retrieve, and act across multiple tools, reward design becomes a critical bottleneck.

Other topics covered:

- The evolution from RLHF (Reinforcement Learning from Human Feedback) to RLVR (Reinforcement Learning from Verifiable Rewards)

- The goals and technical architecture of the Tulu models, including the motivation to open-source post-training recipes

- Challenges of tool use in RL: verifiability, reward design, and scaling across domains

- Evaluation frameworks and the role of platforms like Chatbot Arena and emerging “arena”-style benchmarks

- The strategic tension between hybrid reasoning models and unified reasoning models at the frontier

- Planning, abstraction, and calibration in reasoning agents and why these concepts matter

- The future of open-source AI models, including DeepSeek, OLMo, and the potential for an “American DeepSeek”

- The importance of model personality, character tuning, and the model spec paradigm

- Overoptimization in RL settings and how it manifests in different domains (control tasks, code, math)

- Industry trends in inference-time scaling and model parallelism

Finally, the episode closes with a vision for the future of open-source AI. Nathan has now written up his ambition to build an “American DeepSeek”—a fully open, end-to-end reasoning-capable model with transparent training data, tools, and infrastructure. He emphasizes that open-source AI is not just about weights; it’s about releasing recipes, evaluations, and methods that lower the barrier for everyone to build and understand cutting-edge systems.

## Full Video Episode

## Timestamps

00:00 Welcome and Guest Introduction

01:18 Tulu, OVR, and the RLVR Journey

03:40 Industry Approaches to Post-Training and Preference Data

06:08 Understanding RLVR and Its Impact

06:18 Agents, Tool Use, and Training Environments

10:34 Open Data, Human Feedback, and Benchmarking

12:44 Chatbot Arena, Sycophancy, and Evaluation Platforms

15:42 RLHF vs RLVR: Books, Algorithms, and Future Directions

17:54 Frontier Models: Reasoning, Hybrid Models, and Data

22:11 Search, Retrieval, and Emerging Model Capabilities

29:23 Tool Use, Curriculum, and Model Training Challenges

38:06 Skills, Planning, and Abstraction in Agent Models

46:50 Parallelism, Verifiers, and Scaling Approaches

54:33 Overoptimization and Reward Design in RL

1:02:27 Open Models, Personalization, and the Model Spec

1:06:50 Open Model Ecosystem and Infrastructure

1:13:05 Meta, Hardware, and the Future of AI Competition

1:15:42 Building an Open DeepSeek and Closing Thoughts
