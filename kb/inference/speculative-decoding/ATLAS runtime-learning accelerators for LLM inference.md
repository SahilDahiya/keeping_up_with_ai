---
title: ATLAS runtime-learning accelerators for LLM inference
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Introduces ATLAS, a runtime-learning accelerator for improving LLM inference.
source: together
url: https://www.together.ai/blog/adaptive-learning-speculator-system-atlas
author: Junxiong Wang; Shirley Wu; Zelei Shao; Vikranth Srivatsa; Jue Wang; Roy Yuan;
  Qingyang Wu; Alpay Ariyak; Rupert Wu; Wai Tong Chung; Chenfeng Xu; Yonatan Oren;
  Pragaash Ponnusamy; Yineng Zhang; Avner May; Leon Song; Tri Dao; Percy Liang; Ce
  Zhang; Ben Athiwaratkun
published: '2025-10-10'
fetched: '2026-07-11T04:21:16Z'
classifier: codex
taxonomy_rev: 1
words: 1294
content_sha256: 7290e22a30df6637ff95152667e5eaa2aabf5a82b554949f7ad6a1ecfc2318f6
triage: keep
skip_reason: null
---

# ATLAS runtime-learning accelerators for LLM inference

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0afa82ed24e9ae1622f3_68e6f6e725f6da7515bd4407_ATLAS-Hero.png)

At Together AI, the AI Native Cloud, we’re obsessed with performance. Making large language models faster, cheaper, and more efficient is not a one-trick problem — it requires optimizing along multiple axes. That is the philosophy behind **Together Turbo**, our suite of inference innovations that draw from research in algorithms, architectures, and modeling recipes. We’re excited to introduce the AdapTive-LeArning Speculator System (ATLAS), the first speculator of its kind that gives automatic performance improvements without any manual tuning.

ATLAS offers a new way of doing speculative decoding — one that dynamically improves at runtime — and it fits seamlessly alongside our other Turbo techniques like the proprietary [Together Turbo Speculator](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200) or [Custom Speculators](https://www.together.ai/blog/customized-speculative-decoding). But why create an adaptive-learning speculator system?

Standard speculators are trained for general workloads. Custom speculators are trained on your specific data, but only for a specific snapshot in time. However, as the workload evolves (codebase grows, traffic patterns shift, request distributions change), even highly customized speculators can fall behind. In contrast, ATLAS evolves automatically with usage, learning from both historical patterns and live traffic to continuously align with the target model’s behaviors in real time. This means the more you use our inference service, the better ATLAS will perform!

Built on top of Together Turbo Speculator, ATLAS reaches up to 500 TPS on [DeepSeek-V3.1](https://artificialanalysis.ai/models/deepseek-v3-1/providers#output-speed) and up to 460 TPS on [Kimi-K2](https://artificialanalysis.ai/models/kimi-k2-0905/providers#output-speed) in a fully adapted scenario — 2.65x faster than standard decoding, outperforming even specialized hardware like Groq (Figure 1).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af982ed24e9ae162273_68e6f5c39323d811dc587281_Self-Adaptive%2520Spec%2520-%2520DS%2520V3.1%2520and%2520Kimi-k2-v6.png)

**1. Speculative Decoding**

Speculative decoding is one of the most powerful levers for accelerating inference.2 Instead of having the target model generate every token step by step, a faster **speculator **(also known as the **draft model**)** **proposes multiple tokens ahead, and the target model *verifies* them in parallel in a single forward pass. The verification process ensures that the quality of the output matches the distribution of non-speculative decoding, while achieving speedups by accepting many tokens at a time.

The overall speed is influenced by the acceptance rate $α$ (i.e., how often the target model agrees with the drafted tokens from the speculator) and the relative latency $c$ of the draft versus the target. Typically, larger speculators with more parameters yield higher acceptance rates due to their higher capacity but are slower to generate draft tokens. Progress therefore comes from both sides: aligning draft and target models to increase $α$ (training objectives, data, and algorithms) and designing draft models/kernels that keep $c$ low while maintaining $α$ (sparsity, quantization, lightweight & kernel-efficient architectures). The sweet spot is where a high $α$ meets a low $c$, minimizing end-to-end latency.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a1c32efa5899624e5069ff_atlas-chart.png)

At Together AI, the Turbo team has developed high-performance speculators that have achieved [ the world’s fastest decoding speeds on NVIDIA Blackwell](https://www.together.ai/blog/fastest-inference-for-deepseek-r1-0528-with-nvidia-hgx-b200) by drawing on advances across architecture, sparsity, algorithms, post-training recipes, and data [1-9]. We’ve built a

**speculator design and selection framework**that determines the optimal speculator architecture (width/depth, lookahead, sparsity/quantization, KV reuse) and a

**scalable training system**that brings up speculators for the largest and most challenging open-source targets quickly and reproducibly (e.g., DeepSeek-V3.1 and Kimi-K2). For instance, while Kimi ships without a ready-to-use speculator, we can train and deploy one rapidly and take Kimi from ~150 TPS out of the box to 270+ TPS on the same hardware and batch settings, while preserving target-model quality (see Figure 1, yellow bars).

**This pipeline powers Turbo Speculators that deliver state-of-the-art decoding latency, and it sets the stage for what comes next:**

**an Adaptive-Learning Speculator System**that adjusts token drafting to the workload in real time.

**2. Introducing Turbo’s Adaptive-Learning Speculator System**

At Together AI, we power a broad range of inference workloads. But today’s speculative decoding methods are constrained to using a **static** speculator, trained on a fixed dataset. Once deployed, the speculator cannot adapt, leading to degrading performance if the input distribution evolves. This problem is particularly pronounced in serverless, multi-tenant environments, where input diversity is sky-high. New users continuously arrive, and bring with them unique workloads that the fixed speculator may not have seen during training. Furthermore, these speculators typically use a *fixed lookahead*, predicting the same number of tokens regardless of the speculator’s confidence. Put simply, *a static speculator cannot keep up*.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af882ed24e9ae162266_68e5f97cde692a7dd4e66daf_Adaptive-Learning%2520Speculator%2520System%2520Design.png)

To address these limitations, we designed the** Adaptive-Learning Speculative System **with two cooperating speculators, as shown in Figure 3:

- **A heavyweight**trained on a broad corpus that provides strong, general speculation.- *static*speculator
- **A lightweight**that allows for rapid, low-overhead updates from real-time traffic, specializing on-the-fly to emerging domains.- *adaptive*speculator
- A **confidence-aware controller that**chooses which speculator to trust at each step and what speculation lookahead to use, using longer speculations when the speculator has high confidence.

**Efficiency Guardrail via Static Speculator. **The static Turbo Speculator serves as an always-on speed floor: it is trained on a broad corpus and remains stable across workloads, so TPS does not collapse when traffic shifts or the adaptive path is cold. In ATLAS, we use it to jump-start speed and provide a fail-safe fallback—if confidence drops or drift is detected, the controller shortens lookahead or routes back to the static path to preserve latency while the adaptive speculator relearns.

**Customized Speculator vs. Adaptive-Learning**.** **We know from our previous studies that a [customized speculator](https://www.together.ai/blog/customized-speculative-decoding) trained on samples from real traffic that mirror expected usage delivers an additional speed boost. The Adaptive-Learning Speculator enables us to be even more customized in real time. For instance, during a vibe-coding session, the adaptive system can specialize a lightweight speculator for the relevant code files being edited and not seen during training, further increasing the acceptance rate and decoding speed. This kind of on-the-fly specialization is hard to achieve with static speculators.

**Accelerating RL Training**. Reinforcement learning (RL) alternates between two phases: (1) a rollout phase, where the current policy generates trajectories and receives rewards, and (2) an update phase, where we use the rewards to update the policy. In practice, rollouts are often the bottleneck, accounting for roughly 70% of total wall-clock time3. In general, because the policy distribution shifts throughout training, static speculators quickly fall out of alignment with the target policy, resulting in sub-optimal throughput.4 ATLAS addresses this by adapting online to the evolving policy and the specific RL domain, maintaining alignment and reducing the overall rollout time. The domain-specific, iterative nature of RL further enables rapid adaptation, yielding sustained and growing speedups. As shown in Figure 4, applying ATLAS to the RL-MATH pipeline produces increasing speedups as training progresses.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af882ed24e9ae162263_68e5cccee6c757846d59aed8_acceptance-rate-during-RL-training-3.png)

**Built as part of the Turbo optimization suite. **The Adaptive-Learning Speculator System is a core component of the broader Turbo optimization suite, where each layer of optimization compounds the benefits of the others. As illustrated in Figure 5, performance progressively improves through near-lossless quantization (calibrated to preserve quality), the Turbo Speculator, and finally the Adaptive-Learning Speculator System. Additional optimizations in the suite include TurboBoost-TTFT (not shown) for reducing time-to-first-token latency, further contributing to end-to-end acceleration.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0af982ed24e9ae16226e_68e6f5e6a8a424ecee85949a_Together%2520Turbo%2520Optimization%2520Suite-v5.png)

**Extreme Peak Efficiency**. When the input distribution is narrow and outputs closely echo previously seen tokens, the adaptive system specializes quickly. In this scenario, the controller becomes confident in utilizing more tokens from the lightweight speculator and lengthens lookahead tokens. This yields consistently higher TPS than static or one-off custom speculators can maintain. As shown in Figures 1 and 5, once fully adapted to Arena-Hard traffic, DeepSeek achieves up to 500 tokens per second for batch size 1 on 4 B200 GPUs, delivering a 400% speedup over the FP8 baseline (improvement from 105 TPS to 501 TPS).

{{custom-cta-1}}

**Related Work**

We build on a vibrant ecosystem of research in speculative decoding—from early *draft-and-verify* methods like [ Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192?utm_source=chatgpt.com) and

[, to structured variants including](https://arxiv.org/abs/2302.01318?utm_source=chatgpt.com)

*Speculative Sampling*[,](https://arxiv.org/abs/2401.10774)

*Medusa*[, and the](https://arxiv.org/abs/2406.17276?utm_source=chatgpt.com)

*OPT-Tree*[series. More recent studies made speculation adaptive:](https://arxiv.org/abs/2503.01840)

*EAGLE*

*Online Speculative Decoding**,*
