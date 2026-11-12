---
title: Best open-source models for post-training
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- inference/optimization
summary: Ranks open-source models for post-training by cost tier based on active vs.
  total MoE parameters (e.g. Kimi K2.6's 1T total / 32B active params), recommending
  DeepSeek-V4-Flash for long-context, GLM-5.2 for async RL, and Qwen3 as the safe
  default.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/best-open-source-models-for-post-training
author: Chloe Florit
published: '2026-11-01'
fetched: '2026-11-12T06:09:04Z'
classifier: claude
taxonomy_rev: 2
words: 1797
content_sha256: 371025b934ae4c94eaa5c2dc724fe119969c180e3245fd9bc75121df40e71de1
---

# Best open-source models for post-training

AI models
# Best open-source models for post-training

Compare top open-source models for post-training. Learn what drives cost and which model fits use case.


- Authors
- Date
- November 1, 2026

TLDR

Choosing an open-source model for post-training comes down to cost and use case. Cost is driven by active parameters, total parameters, and KV cache size. We grouped the best models into five cost tiers, from ultra-expensive (Kimi K3) to ultra-cheap (Qwen3.6-35B-A3B), and explained which to pick for text, vision, and coding-agent work. DeepSeek-V4-Flash is great for long-context, cost-sensitive tasks; GLM-5.2 provides fast, asynchronous RL; Kimi K2.6 and K2.7 Code fine-tune the most stably, with K2.7 best for coding agents; Nemotron-3-Super-120B is efficient to fine-tune with native FP4; and Qwen3 is the safe default with the widest size and library support.

During post-training, an open-source model can be specialized for your use case with methods like supervised fine-tuning, preference optimization, and reinforcement learning (RL).

RL is one of the most common methods. It works as a feedback loop: the model generates responses (rollouts), an evaluator (human, AI, or algorithmic check) scores them, that feedback is turned into a reward, and the model is adjusted so high-scoring behavior becomes more likely and low-scoring behavior less likely. The cycle repeats until the model reliably produces the results you want.

In this post, we break down what drives post-training cost, then rank the best open models by cost tier so you can choose the right model for your budget and use case.

Most frontier models use a Mixture of Experts (MoE) architecture. A Mixture-of-Experts model routes each token through a small subset of its 'experts,' so you get the reasoning capacity of a massive model at a lower compute cost. With MoE, only a fraction of parameters (active parameters) are used to generate each token. Kimi K2.6, for example, has 1 trillion total parameters but only activates 32B per token. (Some models, like the smaller Qwen3 variants, are still dense: every parameter is used to generate a token.)

The split between total and active parameters is why two models of the same size can have different post-training and inference costs.

Every token the model generates requires math proportional to its active parameters. Each active weight gets used in the calculation (to turn input text into the next word), so more active parameters means more floating point operations (FLOPs) per generated token. Since RL post-training generates many rollout tokens, active parameter count is the biggest driver of post-training cost.

During serving, weights must be streamed from GPU memory to the compute cores for every token generation step, and the size of that transfer can be a bottleneck for inference speed. You might expect an MoE to only stream its active experts, but in practice models serve many requests at once, and different tokens route to different experts. Across a batch, nearly *all* the weights move through GPU memory for each token generation. This is why total parameters determine how fast inference can run.

As the model processes a sequence, it caches a key and value for every token it has seen and it typically re-reads that entire cache each time it generates a new token. The cache grows with context length. KV cache size per token is how much memory the model needs to store the keys and values of a token.

A large KV cache limits inference speed the same way total parameters do: the cache has to be streamed from GPU memory to the compute cores for every new token, alongside the weights.

*KV Cache:  Keys help the model figure out which words to pay attention to, and values determine what information gets added to a word's meaning based on which other words are relevant. Keys and values are collectively cached as the “KV cache”. Each layer generates a unique KV pair per token.*

| Cost-to-serve | Best text model | Best vision model | Best American Model | Other important models | 
|---|---|---|---|---|
| Ultra expensive | Kimi K3 | Kimi K3 | — | DeepSeek V4 Pro | 
| Expensive | GLM-5.3 (coming soon) | Kimi K2.6 | Inkling | Kimi K2.7 Code; MiMo V2.5 Pro; Nemotron 3 Ultra | 
| Medium | Qwen3.8-27B | Qwen3.8-27B | Inkling Small | Qwen3.5-397B-A17B; MiniMax M3; Step 3.7 Flash; Gemma 4 31B; Motif 3; Muse Glimmer | 
| Cheap | DeepSeek V4 Flash | Qwen3.5-122B-A10B | Nemotron 3 Super | gpt-oss-120b; Laguna S2.1 | 
| Ultra cheap | Qwen3.6-35B-A3B | Qwen3.6-35B-A3B | Gemma 4 26B-A4B | gpt-oss-20b; Nemotron 3 Nano; Laguna XS2.1 | 

Below, we’ll dive into the models most commonly used for post-training and what makes each one a strong choice.

*(Best text model in cheap tier)*

- **Architecture:** 284B total parameters, 13B activated per token (MoE). DeepSeek V4’s hybrid attention (CSA + HCA) improves efficiency by compressing the KV cache to \~4.8 KB per token in FP8/FP4 serving.
- **Why it’s cheap to post-train:** 
- The compressed KV cache makes it cheap to fine-tune very long training examples like long documents or long agent trajectories.
- 13B active parameters and a light KV cache make large RL (Reinforcement Learning) runs cost less.
- **Post-training use cases:** long-context, cost-sensitive tasks.

*(Best text model in expensive tier)* 

**Architecture:** It uses a MoE architecture with 256 experts, routing just 8 experts per token. GLM’s sparse attention selects a subset of the keys to use in the attention algorithm rather than using them all. This helps reduce the KV cache traffic per token and the cost of long context windows.

**Why it’s good for post-training:** 

- GLM 5.2’s slime (an open-source RL training framework) provides strong, fast RL support. It is asynchronous, which means the different stages of the RL loop (generating rollouts, scoring them, and updating the model) can run concurrently instead of waiting for each other. GPUs spend less time idle and RL runs finish faster thanks to model-specific tooling.

*(Best vision model in expensive tier)* 

**Architecture:** Moonshot AI's 1-trillion-parameter MoE model activates 32B per token. Kimi K2.6 has multimodal support via MoonViT (a 400M visual encoder) and can take text, images, and video as input. (Note: 1T total parameters makes the model expensive to post-train and serve.)

- Good tool calling: handles agentic tool use well, including coding tools
- Strong baseline coding ability: less effort is needed to improve coding performance during post-training.
- Good vision: can read images and video, not just text.
- **Post-training use cases:** fine-tune/specialize agent behavior. Best suited as the main orchestrating agent, not a lightweight sub-agent.

*(Best for coding agents in expensive tier)*

**Architecture:** K2.7 Code is trained on an additional 15.5T tokens. The extra training improves coding performance while teaching the model to use fewer reasoning tokens: K2.7 Code uses \~30% fewer tokens per coding task and is more efficient over long agent sessions.

- It inherits everything that makes K2.6 great for post-training. K2.7 just adds stronger coding and token efficiency on top.
- Cheaper to run than K2.6. Kimi K2.7 has cheaper rollout loops during RL post-training because K2.7 uses \~30% fewer thinking tokens per task than K2.6. (Most of RL's cost comes from generating rollouts, and the more tokens the model produces, the more each rollout costs.)

**Post-training use cases:** coding agent fine-tunes.

*(Best American model in cheap tier)*

**Architecture:** NVIDIA's Nemotron-3-Super-120B is an open-weight mixture-of-experts (MoE) language model designed for high-throughput agentic reasoning. It has 120 billion total parameters but activates only 12 billion per token. It handles up to 1 million tokens of context. Its hybrid Mamba-Transformer architecture means most layers don’t have a KV cache and instead keep a running summary of the context. This keeps inference time roughly flat as context grows.

- It works with the standard fine-tuning tools teams already use (NeMo, Megatron-Bridge, and TRL on Baseten). No custom setup required.
- Well-supported by NVIDIA ecosystem: native FP4 makes post-training quantization easy, and on Blackwell, the model runs faster than INT4, FP8, or FP16 alternatives.

*(Safe default across all price tiers)*

**Architecture**: The Qwen3 series includes models of both dense and Mixture-of-Experts (MoE) architectures, with parameter scales ranging from 0.6 to 397 billion.

- Full size ladder. Qwen comes in many sizes (0.6B - 397B). You can pick a size that matches what you have: a small model if you have limited data or a small GPU, a large one if you have lots of compute or a big training set.
- Supports popular fine-tuning libraries: Unsloth (fast, memory efficient fine-tuning): specializes in making fine-tuning faster and more memory efficient. Unsloth also supports LoRA (and more memory efficient QLoRA). 
TRL (RLHF-style training) has built-in implementations of GRPO and PPO
Industry standard: almost every library and package supports Qwen3.

**Post-training use cases (smaller Qwen models):** classification, searching, summarization, retrieval, sub-agent tasks

*Note: GRPO and PPO are reinforcement learning algorithms used to fine-tune models based on reward signals.* 

Three things are important when deciding which model to pick for post-training:

- **Library support.** Does it work with the fine-tuning tools your team wants to use: TRL, NeMo, Megatron-Bridge, Tinker?
- **Benchmarks**. How does it perform on tasks close to yours?
- **Cost**. How cheap is it to run through the post-training loop?

**What is post-training?**

Post-training is everything you do to a model after pre-training to adapt it to a specific task or behavior. It includes supervised fine-tuning (SFT) on labeled examples, preference optimization methods like DPO, and reinforcement learning (RL) that improves the model using reward signals. Post-training is how a general-purpose base model becomes a specialized coding agent, support bot, or domain expert.

**What's the difference between LoRA and full fine-tuning?**

Full fine-tuning updates every weight in the model, which delivers maximum flexibility but requires significant GPU memory. LoRA (Low-Rank Adaptation) freezes the base model and trains small adapter matrices instead, cutting memory requirements dramatically with minimal quality loss. QLoRA goes further by quantizing the base model to 4-bit precision during training. Libraries like Unsloth make both approaches faster and more memory-efficient.

**What frameworks and libraries do I need for post-training?**

The most common stack includes TRL for SFT and RL; NeMo for RL; Megatron-Bridge, the go-to for SFT with wide model support; and slime, Zhipu's open-source asynchronous RL framework for Qwen, DeepSeek V4, and Llama 3 models.

**Why do fewer active parameters and a smaller KV cache make RL training cheaper?**

RL training generates many candidate outputs per task (rollouts) to learn which ones are right and which ones are wrong. If tokens are expensive to generate because of a large number of active parameters or a large KV cache, the cost of RL will be high. Fewer active parameters and a smaller KV cache make each token cheaper and faster to generate, keeping the cost of RL low.
