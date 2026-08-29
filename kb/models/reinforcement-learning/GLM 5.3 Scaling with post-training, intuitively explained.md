---
title: 'GLM 5.3: Scaling with post-training, intuitively explained'
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics:
- inference/speculative-decoding
summary: 'Explains how GLM-5.3 improved over 50% on the identical GLM-5.2 base purely
  through scaled RL post-training: agent-generated environments verified by reward-hacking-resistant
  checks, SAO (Single-Rollout Asynchronous Optimization) with trajectory compaction
  for stable long-horizon RL, and a slime-based pipeline pairing SGLang rollout generation
  with Megatron training; also covers GLM 5.2''s Multi-head Latent Attention, DeepSeek
  Sparse Attention, MTP speculative decoding, and the IndexShare optimization that
  cuts indexer FLOPs 2.9x.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/glm-53/
author: Chloe Florit; Alex Ker
published: '2026-08-28'
fetched: '2026-08-29T06:09:10Z'
classifier: claude
taxonomy_rev: 2
words: 1988
content_sha256: 6a24fcc26b06625dba0cbca6467f5810b80e9ae87ff178391a105f0598143163
---

# GLM 5.3: Scaling with post-training, intuitively explained

![GLM 5.3](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787947495-baseten-blog-2026-thumbnails-11.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Sutton's bitter lesson said general-purpose methods that scale with compute will win. GLM-5.3 is a perfect application of this law to RL, and it means a model can leapfrog its predecessor without a new pre-training run: an identical base model (GLM-5.2) improved over 50% through scaled post-training compute, deliberate environment design, and efficient infrastructure engineering.

In this post, we'll look at how environment design led to GLM-5.3. Then we'll look at how the architecture behind GLM 5.2 carried over to enable efficient training and inference possible. Lastly, we'll cover the RL algorithm and infrastructure, specifically SAO and slime, that turned those cheap rollouts into stable, large-scale post-training.

## Environment design

**The focus of GLM 5.3’s post-training work comes down to realistic environment design:** creating tasks that mirror expert work rather than leetcode-style problems. For example, ML infrastructure problems mimic those that a human engineer would solve. A model is given access to the same resources as a human engineer, including access to compute clusters, storage, and docs. The task is to identify bottlenecks in the training stack, then optimize them by running experiments and iterating on speedups while maintaining correctness.

**The environment generation is also agent-first.** Research agents convert task patterns from real-world workflows into runnable, long-horizon environments (task setups where an agent must work through many steps). A judge agent then checks that each environment is solvable so no bad training signal gets added. Separately, a verifier is automatically generated for each environment without getting access to the reference solution. 

![Closing reward shortcuts: the three-check verifier test](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787944759-diagram-container.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Closing reward shortcuts: the three-check verifier test

To prevent reward hacking (common in RL), the team also used solver trajectories to close reward shortcuts and trivial solutions. Each verifier is tested before use. It must pass three checks: given the known-correct solution, it awards reward (the oracle check); given a run where the agent did nothing, it awards none; and given a run where the task was left unfinished, it awards none. A verifier that rewards only correct, complete solutions is what makes the training signal trustworthy. In short, this pipeline generates synthetic environments at a high volume and quality, which are critical to the success of post-training.

## Breaking down GLM 5.2 & 5.3’s architecture

![GLM 5.2: Model Architecture](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787945612-graphicglm-jpg.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) GLM 5.2: Model Architecture

GLM-5.3’s architecture is entirely carried over from GLM 5.2, which uses a Mixture of Experts (MoE) architecture: 744B total parameters, but only ~40B active per token. Each MoE layer has 256 experts, routing just 8 experts per token, so you get the reasoning capacity of a massive model at a lower compute cost.

### 

**Multi-head Latent Attention: shrinking the KV cache**

**What's a KV (Key-Value) cache?** "Keys" help the model figure out which words to pay attention to, and "values" determine what information gets added to a word's meaning based on the context. Together, they're cached as the "KV cache," so the model doesn't recompute them for every new token. In standard multi-head attention, every head keeps its own unique KV pair for every token. 

**Multi-head Latent Attention (MLA)** compresses each token's keys and values into a small shared latent vector (one per token, per layer), and only this latent is stored in the KV cache. When computing attention, lightweight projection matrices reconstruct (up-project) the per-head keys and values from the latent. This shrinks the KV cache, keeping memory use low as context grows and enabling longer context windows without sacrificing quality.

### **DeepSeek Sparse Attention: making attention efficient**

DeepSeek Sparse Attention (DSA) has two main components. First, a tiny lightning indexer scores all past tokens for relevance to the current query token. Then a token selector picks the top‑k previous tokens for the MLA to run on. The indexer and selector are both learned. Together, they create an attention mask that filters out less relevant tokens.

One of the biggest bottlenecks for running LLMs is that multihead attention is a quadratic, O(N^2), operation. However, since the lightning indexer is in FP8 with a handful of heads, its nominal quadratic cost is dwarfed by the savings from not doing full MLA on the entire context. End‑to‑end cost per token is almost flat out to 128k during prefilling, and only grows linearly in k during decoding, on the order of O(N*k) where k<<N. This makes long reasoning chains affordable. We explained this architecture originally introduced in the [DSV3.2 release](https://www.baseten.co/blog/deepseek-v3-2/#1-dsa--mla-reducing-costs) last year.

### **Multi-token prediction: high acceptance speculative decoding**

MTP is a form of speculative decoding. Speculative decoding is a technique used to speed up LLM inference by using a smaller, faster draft model to predict multiple tokens in parallel, which the larger, more accurate LLM then verifies. If the target model generated those same tokens itself, it would have to do so sequentially, one token at a time.

GLM 5.2 takes a different approach with MTP. Instead of using a separate draft model, GLM-5.2 adds a single lightweight MTP layer on top of its main model. The MTP layer is one transformer block whose weights are reused for every draft step (one step per draft token). At inference, this layer takes the main model's final hidden state (which encodes the full context) plus the embedding of the just-sampled token. But since the MTP layer is a transformer block, its attention still needs to look back over the context (one summary vector isn't enough).

Rather than computing its own keys and values over the context, it reuses the main model's KV cache and sparse-attention indices. GLM 5.3’s MTP allows better draft acceptance over other methods like EAGLE. It sequentially drafts up to 5 tokens ahead, which the main model verifies in one parallel forward pass, accepting ~4.5 tokens per pass on average. This outperforms classic speculative decoding with a separate draft model because the MTP uses the target model's representations, and drafting costs one small extra layer instead of an entire second model.

### **IndexShare: building upon DSA**

IndexShare repairs a shortcoming in DSA's lightning indexer. The lightning indexer picks the top-k tokens for each query to attend to because only a small subset of past tokens matters. However, to *select* the most relevant tokens, the indexer must scan every token, at every layer, which consumes ~81% of prefill time at 200k context. Scanning time is quadratic even though the attention computation has become cheaper, which is a problem at long sequence lengths.

However, between neighboring layers, 70-100% of the tokens that the indexer selects overlap, leading to repeated work. IndexShare caches these computations and creates shared and full layers. In each group of four sparse attention layers, layer 1 of the group runs the lightning indexer and picks the top‑k token indices to attend to. Layers 2–4 reuse those same indices instead of recomputing them. At 1M context the indexer dominates compute, so removing it from 3 of every 4 layers cuts per‑token FLOPs by 2.9×. As a result, the 1.82x prefill speedup and 1.48x decode speedup compared to DSA makes each rollout* cheaper, which translated directly to generating more rollouts with a fixed compute budget.

**Rollout: one complete sample output the model generates during RL.* 

## RL algorithm and infrastructure

### [**SAO**](https://arxiv.org/abs/2607.07508) **with compaction**

**SAO**

SAO (Single-Rollout Asynchronous Optimization) can be thought of as solving the instability problem with asynchronous RL, a problem common to GRPO variants. Agentic tasks have variable rollouts. which leads to wasted compute if we were waiting for a batch to finish before an update. However, the asynchronous updates usually cause policy lag, off-policy traces, and collapse. SAO’s design (single-rollout sampling, practical value-model training, and token-level clipping) solves these issues, enabling stable long-horizon RL training.

But stable training only helps if trajectories can get long, and a trajectory is normally capped at the context window. Compaction removes that ceiling: when a trajectory exceeds the window, the history gets summarized and the model continues from the summary. Together, SAO keeps the training stable, and compaction allows for long horizon RL.

### **slime**

[slime](https://github.com/THUDM/slime) is the RL post-training framework behind GLM models, connecting SGLang to generate fast rollouts with NVIDIA's Megatron to efficiently train on them. 

#### **SGLang (for generation)** 

During RL, the model has to produce millions of sample outputs (rollouts), so they can be scored and learned from. Producing rollouts is inference, and SGLang is built for optimizing inference: it maximizes tokens-per-second using [continuous batching](https://www.baseten.co/blog/how-to-optimize-llm-inference-speed-and-reduce-costs-in-production/#1-continuous-batching) (GPU processes all active requests together), efficient [KV-cache management](https://www.baseten.co/blog/how-to-optimize-llm-inference-speed-and-reduce-costs-in-production/#3-kv-cache-optimizations) (reusing computation across shared prompt prefixes), and [optimized decoding kernels](https://www.baseten.co/blog/how-to-optimize-llm-inference-speed-and-reduce-costs-in-production/#5-kernel-optimizations) (custom GPU operations that make each token-generation step faster). 

#### **Megatron (for training)** 

Once the rollouts are scored, you need to compute gradients and update the model's weights. For a model with hundreds of billions of parameters, the model doesn't fit on one GPU. A long sequence's activations won't fit either. Megatron solves this by **splitting the model and input sequences across many GPUs**:

- **Tensor parallelism** : individual layers are sliced across GPUs
- **Pipeline parallelism** : different layers live on different GPUs
- **Expert parallelism** : for MoE models, different experts live on different GPUs
- **Context parallelism (CP)** : long sequences are split into chunks across GPUs

SGLang and Megatron store the model's weights in completely different layouts for training vs. inference slime's core job is orchestrating the loop between them:

1. SGLang generates a batch of rollouts with the current model
2. Rollouts get scored (rewards)
3. Megatron trains on them and produces updated weights
4. slime **converts and transfers those new weights back into SGLang**
5. Loop repeats, with generation now using the improved model

## **What's new in slime for GLM 5.3**

### **Multi-teacher on-policy distillation (OPD)**

**OPD (on-policy distillation):** the student model generates an answer, and a stronger teacher model grades it token by token. It’s like the teacher is saying: "Here's the probability I would have assigned to each token you wrote." The student is trained to match the teacher's per-token probability distribution. It's "on-policy" because the training data is the student's output. 

**Multi-teacher:** instead of one teacher, you use several because no single model is the best teacher at everything. A coding model grades the student's code, a math model grades its math, a reasoning model grades its reasoning. Each teacher provides the signal in its strongest domain.

### **Dynamic teacher switching + prefetching** 

Typically, with OPD, each teacher would need its own GPU deployment. Most of those GPUs would be idle at any given moment, since training with OPD requires only one teacher at a time. Instead, only the active teacher is loaded on GPUs; the rest are kept in local storage instead of occupying host memory. The next teacher's weights are loaded in the background ahead of time, so switching teachers causes minimal delay.

### **Joint scheduling + load balancing between router and slime**

Rollout requests with varying lengths/completion times get distributed across GPUs so GPUs don't sit idle. For example, if you assign a batch of rollouts to multiple GPUs and they end at different times, the freed capacity will sit idle. But with router-slime joint scheduling, the moment capacity frees up, the scheduler immediately routes it to a new request from the queue.

## Takeaway

GLM 5.3's gains came from scaling post-training, and we explained how each part works intuitively. IndexShare made every rollout cheaper to generate. SAO enabled RL to teach long-horizon behavior. slime's multi-teacher OPD upgrades optimized GPU usage with more training signal out of every GPU-hour. RL is now a proven way to iterate on a predecessor base model without a new pretraining run, and open model releases like this one show you exactly how.

## **Build with GLM 5.3 on Baseten**

We’re excited to offer day-0 access via Model APIs, and look forward to continuing to optimize our implementation of this model to achieve the highest standards in performance and reliability.

[GLM 5.3](https://www.baseten.co/library/glm-53/?utm_term=glm%205.3%20api&utm_campaign=Search+-+Models&utm_source=adwords&utm_medium=ppc&utm_id=24181001182&hsa_acc=9990356727&hsa_cam=24181001182&hsa_grp=202015539960&hsa_ad=822132807083&hsa_src=g&hsa_tgt=kwd-2491432609678&hsa_kw=glm%205.3%20api&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=24181001182&gbraid=0AAAAAqCKh1sUDnN0z9XnmI568X1_BIC5f&gclid=CjwKCAjw48TUBhBREiwAK0GnQTMMRZGkyVniNUR8r3cFoF1IFlMF5UutFk7Ii3LYWf4gqqkjGh7lsBoC7DwQAvD_BwE) is available today on Baseten Model APIs. Welcome to the new frontier in open weight intelligence.
