---
title: The best open-source large language models (LLMs)
kind: blog
topic: models
subtopic: benchmarks
secondary_topics:
- inference/speculative-decoding
summary: Compares 9 open-source LLMs (DeepSeek V4 Pro 0813, Gemma 4, GLM-5.3, GPT
  OSS 120B, Kimi K3, MiniMax M3, Nemotron 3 Ultra, Qwen 3.6) for agentic coding and
  long-context use, detailing DeepSeek's CSA/HCA compressed-sparse-attention KV cache
  (10% of standard memory) and built-in DSpark speculative decoding module.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-best-open-source-large-language-models-llms
author: Chloe Florit
published: '2026-06-17'
fetched: '2026-11-12T06:07:40Z'
classifier: claude
taxonomy_rev: 2
words: 2230
content_sha256: 027eee8dc1a38d647e162e9d562c556aa25dd43cdcdda5434e908f3fe374301a
---

# The best open-source large language models (LLMs)

AI models
# The best open-source large language models (LLMs)

We compare 9 top open-source LLMs in production. Find the best model for agentic coding, long-context reasoning, cost, and speed.


- Authors
- Date
- June 17, 2026

TLDR

We evaluated nine of the best open-source models: DeepSeek V4 Pro 0813, Gemma 4, GLM-5.3, GPT OSS 120B, Kimi K3, MiniMax M3, Nemotron 3 Ultra, and Qwen 3.6. Kimi K3 is the most well-rounded; Qwen 3.6 and GLM-5.3 lead for agentic coding; DeepSeek and Nemotron dominate long-context and enterprise workloads; and GPT OSS 120B performs well on cost and speed.

New LLMs drop every day. With so many choices, it might be hard to select the right one! You might have a variety of tasks in front of you that could require coding, agentic workflows, or long context reasoning, for example. Whatever your use case is, we want to help you find the best open-source LLMs for it.

In this blog, we’ll review the technical specifications, benchmarks, and first-hand data from models we currently run for customers in production at Baseten.

DeepSeek V4 Pro 0813 is a frontier open-source model built for agentic coding and complex STEM reasoning. Its architecture allows for a 1M-token context window through a hybrid attention mechanism:

**CSA (Compressed Sparse Attention)** shrinks the KV cache: instead of keeping one entry for every token, it summarizes groups of tokens into a smaller set of compressed entries. (Keys help the model figure out which words to pay attention to, and values determine what information gets added to a word's meaning based on which is relevant. They are collectively cached as the “KV cache”.) It then attends sparsely over that compressed sequence: each token picks out only a handful of the most relevant compressed blocks instead of reading everything, so it keeps detail where it matters while cutting memory.

**HCA (Heavily Compressed Attention)** compresses much more aggressively, squeezing large spans of tokens into a single entry, but drops the sparse selection. Because the compressed sequence is now so short, the model can afford to attend densely across all of it. Together, CSA and HCA reduce KV cache memory to roughly 10% of what standard models require.

**Manifold-Constrained Hyper-Connections (mHC)** keep training stable at scale, allowing DeepSeek to reliably train models with massive context windows by replacing the standard residual addition between layers with a mathematically constrained mixing operation.

[Speculative decoding](https://www.baseten.co/blog/a-quick-introduction-to-speculative-decoding/) is a technique used to speed up LLM inference by using a smaller, faster draft model to predict multiple tokens in parallel, which the larger, more accurate LLM then verifies. DeepSeek V4 Pro builds speculation directly into the model, which makes deployment easier. The V4 Pro 0813 includes an attached DSpark speculative decoding module: the draft weights are part of the model itself, so no separate draft model is needed. DeepSeek's reference configuration speculates 7 tokens per pass.

**What we love about DeepSeek V4 Pro:**

- DeepSeek V4 Pro leads open-source models on agentic coding and matches closed-source frontier models
- 1M token context window to feed it an entire codebase or document library in a single call
- CSA + HCA reduce KV cache memory to \~2% of standard transformer requirements which lowers inference costs and allows more requests to run on the same GPU
- mHC keeps training stable at scale, enabling reliable performance across massive contexts
- Significantly cheaper than comparable closed-source models on mid-to-high complexity tasks

You can try [DeepSeek V4 Pro 0813](https://www.baseten.co/library/deepseek-v4-pro-0813/) on Baseten.

Google DeepMind’s open-weight Gemma model is built for enterprise fine-tuning and multimodal reasoning.

Gemma 4 alternates between sliding window attention, where each token only looks at a fixed window of neighboring tokens, and sparsely placed global attention layers, where every token attends to every other token in the full sequence. This cuts compute overhead sharply while preserving long-range reasoning.

Context windows go up to 128K on edge deployments and 256K in the cloud.

There are two notable Gemma 4 models:

- Gemma 4 12B is encoder-free, with native audio support. The model is best for local deployment and agentic workflows on consumer hardware.
- Gemma 4 31B is a more capable dense model, better for high-quality outputs where hardware isn’t a constraint. It does not have native audio and uses more VRAM.

**What we love about Gemma 4:**

- Great for agentic apps and fine-tuning custom models
- Interleaved local/global attention reduces memory and compute costs
- Up to 256K context window in cloud deployments
- Strong multimodal reasoning and agentic workflow performance

[GLM-5.3](https://www.baseten.co/blog/glm-53/#environment-design) is Z.AI's latest model for agentic engineering, with stronger coding, long-horizon agentic capabilities, and emergent cybersecurity analysis. GLM-5.3 supports three thinking effort levels (low, high, and max, with max recommended for coding), making it a strong fit for agentic coding workflows that require sustained planning, implementation, and verification at production scale. It supports text-only inputs, with a 1M-token context window and a maximum output length of 128K tokens.

GLM-5.3's gains come entirely from post-training: it shares an identical base model and architecture with GLM-5.2 (744B-parameter MoE, \~40B active per token, with MLA, sparse attention, and IndexShare).

Agentic tasks have variable rollouts, which leads to wasted compute if training waited for a batch to finish before an update. The fix is to update the model as each rollout finishes. But then slow rollouts come back generated by an older version of the model, and this stale data would normally derail training.

SAO (Single-Rollout Asynchronous Optimization) prevents that by learning from one rollout at a time and capping how much any single stale token can shift the model, while compaction summarizes a rollout's history whenever it fills the context window, letting tasks run for hours.

**What we love about GLM-5.3:**

- Stronger multi-hour agentic coding workflows
- Over 50% improvement on GLM-5.2 from post-training alone
- 1M context window via sparse attention and IndexShare

OpenAI's open-weight reasoning model, GPT OSS, is optimized for text generation and conversational AI. It’s cost-efficient and hits 650+ tokens/second on Baseten with NVIDIA GPUs, making it one of the fastest and most affordable 120B models available.

Baseten reached [650+ TPS on GPT OSS 120B](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/) by using TensorRT-LLM on B200 GPUs and [NVIDIA Dynamo](https://www.baseten.co/blog/nvidia-dynamo-day-baseten-inference-stack/) (for KV cache-aware routing) at launch, then added [EAGLE-3 speculative decoding](https://www.baseten.co/blog/how-to-train-custom-eagle-3-heads-for-speculative-decoding/#what-is-eagle-3), which uses a smaller \~1B draft model to predict tokens in parallel and delivers a 60% speed boost.

**What we love about GPT OSS 120B:**

- 650+ tokens/second on Baseten; one of the fastest 120B models available
- Optimized for consumer hardware (\~80GB), making deployment straightforward
- One of the cheapest 120B models to run without sacrificing generation quality

Notable improvements in Kimi K2.7 Code over Kimi K2.6 include stronger coding and agent performance on long-horizon, repo-level tasks.

While Kimi K2.6 is already highly reliable for day-to-day programming, K2.7 is tuned for multi-step software engineering workflows: planning, editing, debugging, and iterating across many steps.

K2.7 Code is trained on 15.5T tokens, with code-focused training that improves coding performance while using fewer reasoning tokens. Lower thinking-token usage makes K2.7 Code more efficient over long agent sessions using \~30% fewer tokens per coding task.

Unlike Kimi K2.6, which would let you toggle between thinking and non-thinking modes, K2.7 is always in a mandatory "thinking mode" for deeper reasoning.

**What we love about Kimi K2.7 Code:**

- Built for multi-step software engineering (plan → edit → debug across many steps)
- Cheaper and faster coding workflows: uses fewer tokens and less unnecessary reasoning, which lowers inference cost
- More reliable agentic execution

Kimi K3 is Moonshot AI's 2.8-trillion-parameter model, built for long-horizon coding sessions that run autonomously for hours. The model is rewriting the stack it runs on: an early K3 handled most of the team’s kernel optimization work during development. K3 has native vision, a 1M-token context window, and uses Stable LatentMoE, activating just 16 of 896 experts per token.

**AttnRes (Attention Residuals):** To generate a token, the input passes through a stack of layers. Usually, the outputs of these layers are summed to determine which token to generate. But, AttnRes multiplies each element of that sum by a specialized weight, letting the model give more importance to whichever layers are most useful in context instead of treating them all equally.

**KDA + MLA (Kimi Delta Attention + Multi-head Latent Attention)** tackle the long-context problem: the KV cache grows with every token, so generation slows as context gets longer. KDA replaces the growing cache with a fixed-size memory that updates as tokens arrive. But fixed memory can’t perfectly recall everything as well as a full KV cache can, so that’s why Kimi K3 interleaves MLA layers, which keep full recall efficiently by compressing each token's KV into a small latent vector. This keeps compute low and recall accurate as context grows.

Why we love Kimi K3:

- **Long-horizon agentic coding**: sustained multi-hour autonomous sessions
- **Native multimodality with vision-in-the-loop**: iterates between code and live screenshots for frontend, game dev, and CAD; strong 3D reasoning
- **Strong visual output:** turns research into interactive dashboards and frontend UI
- **Great for creative writing**: one of the best models for writing, with a style that stands out from other LLMs

MiniMax M3 is a strong choice for frontend and UI work, visual reasoning, and creative tasks. It supports a 1M token context window using MiniMax Sparse Attention (MSA), which keeps memory costs manageable at scale. It produces clean results on design-adjacent tasks: UI generation, code review with visual context, creative writing.

**What we love about MiniMax M3:**

- 1M token context window via sparse attention, without the memory costs of standard transformers
- Stands out for frontend/UI generation and visual reasoning tasks
- Strong on creative and design-heavy workflows

NVIDIA’s 550B model is a frontier open-weight mixture of experts (MoE) language model designed for long-running agents. You get the knowledge capacity of a 550B model at the cost of running a 55B one. Its hybrid Mamba-Transformer architecture keeps inference time roughly flat as context grows. On long-running agentic workflows, that translates to up to 5x faster inference and up to 30% lower cost.

Ultra is one of three models in NVIDIA's Nemotron 3 family, alongside Nano and Super. The three are designed to be complementary.

**What we love about Nemotron 3 Ultra:**

- 1M-token context with hybrid Mamba-Transformer: step time stays flat as context scales
- Built for long-running agents and long-context enterprise workloads
- Sets a thinking token limit per step to avoid over-reasoning on simple tasks
- Affordable for a 1M token context window model

The Qwen 3.6 open-source family includes two models: the 27B dense and the 35B-A3B MoE (3B active params). For agentic coding specifically, Qwen 3.6 provides repo-level reasoning and strong frontend workflow performance.

Notable improvements over Qwen 3.5 include natively multimodal support across both models, which handles images and video in a single checkpoint. On the coding side, Qwen 3.5 handled general programming but struggled with complex, repo-level tasks. The Qwen 3.6 27B model outperforms the previous 397B open-source flagship on every major coding benchmark, despite being a fraction of the size.

**What we love about Qwen 3.6:**

- Runs well on consumer hardware across the family
- Top-tier agentic coding: repo-level reasoning with minimal mid-task corrections
- Reliable performance across frontend and devops workflows
- Natively multimodal (text, image, video) in both open-source models

Benchmarks are a starting point. A model that tops a leaderboard may underperform on your specific task. You should run evaluations on your own task workload to find the model that will work for you. Once you've chosen a model, you can [optimize inference performance](https://www.baseten.co/blog/ai-model-performance-metrics-explained/) metrics like TTFT, TPS, and end-to-end latency.

The best open-source LLM depends on your workload and what you’re optimizing for. All models mentioned here are used in production today for many AI applications.

**What is a context window?**

The maximum amount of text a model can process at once: your prompt, conversation history, documents, and output combined. A 1M token window means you can usually include entire codebases or document libraries in a single call.

**What is Mixture of Experts (MoE)?**

An architecture where the model is divided into many specialized sub-networks, but only a small subset activates for any given input. You get the reasoning capacity of a much larger model at a fraction of the inference cost. MoE doesn't use less memory: all the parameter weights need to be stored in VRAM.

MoE was popularized by DeepSeek R1 and is the typical architecture used in LLMs today.

**What is a dense model?** 

A dense model means all parameters are active for every token/input during the forward pass, as opposed to a Mixture of Experts (MoE) model.

**What does “open-weight” mean? Is it the same as open-source?**

Open-weight means the model’s trained weights are public. You can then run inference and post-training with an infrastructure platform like Baseten or yourself.

Open-source means the training code, data, and methodology are also public. Most models here are open-weight but not fully open-source.

**Which open source LLMs can run locally on consumer hardware?**

Qwen 3.6 and Gemma 4 12B are the best options for running LLMs locally; both run well on consumer hardware. GPT OSS 120B needs \~80GB VRAM but is one of the cheapest 120B models available.

**What is KV cache-aware routing?** 

KV cache-aware routing sends requests to the GPU worker that already has the relevant cache loaded, cutting time-to-first-token.
