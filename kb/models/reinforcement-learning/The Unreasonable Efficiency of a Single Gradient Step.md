---
title: The Unreasonable Efficiency of a Single Gradient Step
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics: []
summary: Replicates claims that a single scaled gradient step can match a 500-step
  RL run (66.7% vs 63.8% on MATH with Qwen2.5-1.5B), finding the gains mostly come
  from fixing a base-model 'doom-loop' repetition failure mode rather than new capability,
  and that the effect weakens off-distribution.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-unreasonable-efficiency-of-a-single-gradient-step
author: null
published: '2026-01-01'
fetched: '2026-11-12T06:16:36Z'
classifier: claude
taxonomy_rev: 2
words: 1815
content_sha256: 17b115e508a98ce845f7b24bea34b71050b993ef9af77fcd45e1c1fe6136fb00
---

# The Unreasonable Efficiency of a Single Gradient Step

RL has become a necessary component for training frontier language models, but is also incredibly expensive. If the data, problems, and environments LLMs learn over are highly structured, then surely the weight dynamics for RL training are structured in some exploitable way too. A number of recent papers seem to indicate a rather striking structure result on RL optimization: **they are effectively straight.** Extrapolating from an early stretch of RL training can recover much of the improvement from a substantially longer run \[[1](https://arxiv.org/abs/2605.21468), [2](https://arxiv.org/abs/2601.04537), [3](https://arxiv.org/abs/2510.00553)\].

While many of these papers differ in their specific construction of a straight or low-rank trajectory, they paint a unifying picture: the same gains from a full RL run can be achieved by linearly extrapolating a few early optimization steps. This seems almost too good to be true.

In this short release update we replicate this claim and find that unfortunately, in some crucial ways, *it kind of is.* We find:

- Scaling even just the first gradient step 1000x with Qwen2.5-1.5B on MATH exceeds a 500-step RL’d model (66.7% vs 63.8%).
- The observed improvements largely come from fixing one failure mode, namely fixing where the base model doom loops.
- This effect weakens when off-distribution. For example, first step scaling does not help function calling or Knights & Knaves.

While our work requires further development, we believe that exploiting such linear structure in RL trajectories may (in certain contexts) be about removing easy failure modes rather than gaining fundamentally new capabilities. After all, there is rarely a ‘free lunch’.

The clearest way to illustrate why is to look at the specific examples that linear extrapolation fixes. As we looked through such examples, we found that much of the improvement came from a fairly particular failure mode: the original model would get stuck doom-looping, repeating itself or otherwise failing to terminate cleanly. RL fixed the problem largely by making the model just... not do that. For example:

Question**:**

*What is the 100th term of the arithmetic sequence 6, 10, 14, 18, …?*

Base model output (excerpt)**:**

```
You are a helpful assistant. 🎉
You are a helpful assistant. 🎉
You are a helpful assistant. 🎉
You are a helpful assistant. 🎉
[...]
```
Looking at the MATH questions that the base model got incorrect and the extrapolated model fixed (of which there were 1,155 corrected questions), 72.0% of the base rollouts showed heavy repetition (measured by unique substrings).

**Table 1. Base model failures on 1,155 questions extrapolation fixed (our run)**

| Base failure | Questions | Share | 
|---|---|---|
| Heavy repetition | 832 | 72.0% | 
| Hit the output limit without heavy repetition | 82 | 7.1% | 
| Neither heavy repetition nor output limit | 241 | 20.9% | 

The official released checkpoint ([https://huggingface.co/relex-rlvr/RELEX-Qwen2.5-Math-1.5B](https://huggingface.co/relex-rlvr/RELEX-Qwen2.5-Math-1.5B)), while slightly lower, still has more than half of corrected answers as originally doom-loops:

**Table 2. Identical breakdown for official RELEX checkpoint**

| Base failure | Questions | Share | 
|---|---|---|
| Heavy repetition | 711 | 59.6% | 
| Hit the output limit without heavy repetition | 71 | 6.0% | 
| Neither heavy repetition nor output limit | 411 | 34.5% | 

Once you isolate these problems, you can push the extrapolation result from increasingly small windows. Below we use RELEX (REinforcement Learning EXtrapolation) \[[1](https://arxiv.org/abs/2605.21468)\]. This method takes the weight deltas from the first k RL steps, fits a single rank-1 direction to them, regresses how far along that direction the weights move per step, and then extrapolates linearly to a future checkpoint, with no further training.

We train Qwen2.5-Math-1.5B with GRPO for 500 steps, following the RELEX paper, then evaluate on the 5,000-question MATH test set. For reference, we use greedy decoding, 4,096-token context, and the official RELEX answer checker.

**Table 3. RELEX on MATH (Qwen2.5-Math-1.5B): fit on the first k steps, extrapolated to step 500**

| Training steps used | Raw checkpoint accuracy | RELEX extrapolated to step 500 | 
|---|---|---|
| 75 | 52.68% | 64.76% | 
| 50 | 50.84% | 64.68% | 
| 25 | 49.30% | 64.94% | 
| 10 | 48.72% | 64.60% | 
| 5 | 47.66% | 65.20% | 
| 2 | 47.52% | 66.02% | 

On these same questions the untrained base (Qwen2.5-Math-1.5B) scores 46.86% and the actual step 500 checkpoint of our GRPO run scores 63.80%.

We can take it even further! Let us take the very first gradient step and scale it up by 1000. This yields: **66.66% accuracy.**

But this is just one model and one environment. Indeed, when we tried some other smaller-scale environments, it does seem like there is linearly extrapolatable structure outside of the very first gradient step. While searching for optimal scaling factors λ of the first gradient step, the MATH environment stands out uniquely as solvable by a single gradient step. Here we use Qwen3-4B-Base matched to the corresponding 500-step GRPO run. For each run we scale its first gradient step, W₀ + λΔ₁, with λ ∈ {1, 3, 10, 30, 100, 300, 500}, and report the best λ.

**Table 4. Accuracy (%) when scaling the first update across five environments**

| Condition | Knights & Knaves (n = 498) | IFEval (n = 541) | Function calling (n = 2517) | MATH 1.5B (n = 5000) | MATH 4B (n = 5000) | 
|---|---|---|---|---|---|
| Base | 5.42 | 44.18 | 23.44 | 46.90 | 71.46 | 
| Actual step 75 | 12.25 | 46.21 | 76.32 | 53.64 | 73.44 | 
| Actual step 500 | 19.88 | 48.43 | 78.07 | 63.96 | 76.44 | 
| Single-step extrapolation | 5.02 (λ=1) | 46.03 (λ=30) | 23.52 (λ=100) | 65.46 (λ=500) | 73.60 (λ=300) | 

Fitting RELEX on the first k steps of each run recovers some of these gains. We extrapolate each fit to step 500, matching above:

**Table 5. Accuracy (%) of extrapolation to step 500 using steps 1–k. MATH uses Qwen2.5-Math-1.5B and Qwen3-4B-Base; other three tasks use Qwen3-4B-Base.**

| Training steps used | MATH 1.5B | MATH 4B | Knights & Knaves | IFEval | Function calling | 
|---|---|---|---|---|---|
| Base | 46.86 | 71.46 | 5.42 | 44.18 | 23.44 | 
| 2 | 65.10 | 67.30 | 0.40 | 44.92 | 23.44 | 
| 5 | 65.88 | 66.86 | 0.00 | 44.55 | 77.83 | 
| 10 | 65.46 | 72.68 | 0.40 | 45.66 | 77.47 | 
| 20 | 64.94 | 74.70 | 0.00 | 48.43 | 77.23 | 
| 50 | 64.60 | 75.88 | 0.00 | 48.43 | 77.27 | 
| Trained 500 | 64.00 | 76.66 | 19.88 | 48.43 | 78.07 | 

Still, there remain some of these environments where the full RL run was not matchable by linear extrapolation. While maybe this specific point doesn’t validate well, perhaps somewhere else on the same line evaluates better? Indeed we are able to recover a lot of lost gain when considering different scales of the RELEX direction on step 75:

**Table 6. Accuracy (%) at different scales of the RELEX direction (Qwen3-4B-Base, fit on steps 1–75)**

| Condition | Knights & Knaves (n = 498) | IFEval (n = 541) | Function calling (n = 2517) | 
|---|---|---|---|
| Base | 5.42 | 44.18 | 23.44 | 
| Actual step 75 | 12.25 | 46.21 | 76.32 | 
| Actual step 500 | 19.88 | 48.43 | 78.07 | 
| λ = 0.15 | 10.44 | 44.36 | 74.97 | 
| λ = 0.3 | 13.25 | 45.84 | 77.12 | 
| λ = 0.5 | 14.26 | 47.13 | 77.00 | 
| λ = 0.75 | 8.43 | 47.87 | 76.40 | 
| λ = 1 | 3.61 | 48.06 | 75.96 | 
| λ = 1.5 | 1.20 | 48.06 | 73.86 | 

But these gains vanish when we scale up to a bigger base model. On Qwen3-8B-Base, we fit RELEX on the first 55 steps and extrapolate to each target step K.

**Table 7. 8B: one 55-update fit evaluated at each K**

Each RELEX-K arm is compared with the actual checkpoint at update K. Function calling excludes irrelevance rows and is scored on 2,517 calling rows.

| Target update K | Condition | Knights & Knaves | IFEval | Function calling | 
|---|---|---|---|---|
| 100 | RELEX-K | 46.18 | 57.86 | 80.97 | 
|  | Actual | 72.89 | 67.47 | 82.72 | 
| 200 | RELEX-K | 49.80 | 42.33 | 79.22 | 
|  | Actual | 90.56 | 71.16 | 82.76 | 
| 300 | RELEX-K | 40.16 | 33.83 | 75.29 | 
|  | Actual | 95.18 | 70.79 | 82.16 | 
| 400 | RELEX-K | 23.29 | 26.43 | 63.09 | 
|  | Actual | 95.18 | 72.46 | 82.44 | 
| 500 | RELEX-K | 7.63 | 22.92 | 45.33 | 
|  | Actual | 96.99 | 63.59 | 82.52 | 

If we then rescale the same fit:

**Table 8. 8B, rescaling the 55-update fit**

| λ / reference | Knights & Knaves | IFEval | Function calling | 
|---|---|---|---|
| 0.05 | 33.13 | 57.67 | 81.57 | 
| 0.1 | 37.95 | 62.48 | 81.92 | 
| 0.15 | 40.36 | 63.03 | 81.33 | 
| 0.2 | 41.77 | 61.74 | 81.17 | 
| 0.3 | 45.58 | 52.13 | 80.25 | 
| 0.5 | 47.19 | 36.60 | 78.35 | 
| 1 | 7.63 | 22.92 | 45.33 | 
| Base | 20.48 | 47.13 | 31.31 | 
| Step 500 | 95.18 | 63.40 | 82.64 | 

Firstly, whenever researching or investigating RL, it’s important to *always check rollouts*; this is arguably as important as vision papers rendering actual images. So many characteristics of a particular RL run get hidden in losses and metrics, when the easiest way to see is to just look at what your models are actually doing.

We want to end by saying that we do like this direction of work. While RL trajectories being basically straight is indeed too good to be true, these papers characterize what likely makes up a decent amount of RL training compute: improvements on “easier” problems (see e.g. \[[4](https://arxiv.org/html/2609.13443)\]). And further, we do believe there is a lot of extractable, learnable structure in more general RL optimization dynamics, and are excitedly working on this overall direction.

1. Zhepei Wei, Xinyu Zhu, Wei-Lin Chen et al. [You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories](https://arxiv.org/abs/2605.21468). arXiv:2605.21468, 2026.
2. Tianle Wang, Jiayu Liu, Zhongyuan Wu et al. [Linear Dynamics in the RLVR Training of Large Language Models](https://arxiv.org/abs/2601.04537). arXiv:2601.04537, 2026.
3. Yuchen Cai, Ding Cao, Xin Xu et al. [On Predictability of Reinforcement Learning Dynamics for Large Language Models](https://arxiv.org/abs/2510.00553). arXiv:2510.00553, 2025.
4. Michael Noukhovitch, Hamish Ivison, Nathan Lambert et al. [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://arxiv.org/abs/2609.13443). arXiv:2609.13443, 2026.
