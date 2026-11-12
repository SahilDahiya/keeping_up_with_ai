---
title: Understanding the compute efficiency of value functions in RL
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics: []
summary: Re-examines whether PPO-style learned critics are worth their compute versus
  GRPO's group-mean baseline, finding a 'perfect critic' removes at most 40-60% of
  advantage variance on two single-turn tasks and that recent papers' wins over GRPO
  (e.g. TCG-GRPO, AC2) come from auxiliary uses of the critic rather than variance
  reduction alone.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/understanding-the-compute-efficiency-of-value-functions-in-rl
author: null
published: '2026-01-01'
fetched: '2026-11-12T06:15:34Z'
classifier: claude
taxonomy_rev: 2
words: 1905
content_sha256: e948cda540e06abf4fe21b2f8871bc7eed653d7532cb333a0d43b548ec4b2276
---

# Understanding the compute efficiency of value functions in RL

The starting of a research lab often involves revisiting the eminent literature and understanding why something worked (or why it did not). A theme of this week at Base Labs has been thoroughly understanding and internalizing the historical canon of the post-training field. One canonical example (that is very front of mind) is the introduction of GRPO \[[1](https://arxiv.org/abs/2402.03300)\] and correspondingly, the decline of PPO.

Before GRPO was introduced, doing RL on a language model meant doing PPO \[[2](https://arxiv.org/abs/1707.06347)\]. In brief, PPO involves some policy and a value model (a ‘critic’ of this policy) that attempts to predict how well the answer will score at each token \[[3](https://arxiv.org/abs/1506.02438)\]. The creation of GRPO meant removing the critic in place of scoring each answer *against* the mean reward of a group of completions sampled for the same prompt. The theoretical argument here was that instantiating and training a second network is basically the same number of parameters as the policy, and perhaps more importantly, must try to make accurate per-token predictions from a single scalar reward given at end. The month that GRPO was released RLOO \[[4](https://arxiv.org/abs/2402.14740)\] also outperformed PPO on summarisation and dialogue tasks using REINFORCE with a leave-one-out baseline (e.g. the mean reward of the prompt’s other answers).

With the release of DeepSeek-R1-Zero \[[5](https://arxiv.org/abs/2501.12948)\] in January 2025 GRPO “officially” replaced PPO as the default for reasoning RL. But has the tide turned? Indeed, many of the recent ICLR submissions we have read (these of course remain anonymous) return to retraining a critic!

We decided to run some toy experiments to investigate when a critic is actually worth the extra compute required to train it. Theoretically, a value function should only be “worth it” if it removes more gradient noise than what it costs to run (in opportunity cost to more rollouts). This is not usually the case. Most papers that swap the group mean for a PPO critic or a proxy thereof perform equally at equal steps.

A more interesting question one may then ask is: what about adding a critic on top of the group itself? We find that this helps even less than we hoped. For example, a “perfect critic” removes at most 40-60% of the advantage variance that we test on two single-turn tasks. The only area that we find a critic may help is the use of a small value head, and even then this benefit may be marginal.

As a starting point we decided to get our hands dirty with the latest value function literature. In those published (but not necessarily peer reviewed, we make no claims about their holistic quality), we found that PPO critics tied or lost to GRPO at equal steps (Table 1). An intuition for understanding this result is that for a baseline (as common across every policy-gradient method) GRPO uses the group mean and PPO the learned critic. At equal steps, the baseline requires the “value” of the prompt, which is neat in GRPO where it is a fresh Monte Carlo estimate but poor for PPO that must rather learn this value.

**Table 1. Standard PPO critic vs GRPO compared at equal steps**

| Paper and context (brackets) | PPO | GRPO | 
|---|---|---|
| GAVE \[6\] (ALFWorld / maths) | 63.9 / 36.8 | 64.1 / 44.4 | 
| PACT \[7\] (agentic maths) | 59.7 | 64.1 | 
| GenAC \[8\] (maths, 3 seeds) | 50.85 | 49.96 | 

Many of these papers do however report large wins over GRPO! These gains come from a variety of mechanisms. For instance, TCG-GRPO \[[9](https://openreview.net/forum?id=6LRYa55PMD)\] keeps GRPO’s group and uses its critic to assign credit between turns whilst AC2 \[[10](https://openreview.net/forum?id=bUk8OiOoR9)\] uses its critic to stop generating early, matching GRPO with less decoding compute.

The central theme running through many of these papers, at least to us, appears to be what a value function can add on top of a group.

An important point to make at this stage is that group-relative rewards and learned value functions do not have to be mutually exclusive; indeed, we can learn a value function to estimate the expected difference between the finite group estimate and the true value function. We formalize this below.

For a fixed prompt and policy, sample $G\geq2$ independent answers with rewards $R_i$, mean $\mu$, and variance $\sigma_R^2$. Define the leave-one-out baseline and advantage, without division by the group reward standard deviation \[[11](https://arxiv.org/abs/2503.20783)\], as

$$
B_i=\frac{1}{G-1}\sum_{j\ne i}R_j,\qquad A_i^{(0)}=R_i-B_i.
$$

Since $R_i$ and $B_i$ are independent,

$$
\operatorname{Var}(A_i^{(0)})=\sigma_R^2+\frac{\sigma_R^2}{G-1}.
$$

The second term is noise introduced by estimating the prompt’s mean reward from only $G-1$ other answers.

Now let $S_{i,t}$ be the prefix before token $t$, and define the ideal value function $V_{i,t}=\mathbb E[R_i\mid S_{i,t}]$. By the law of total variance,

$$
\sigma_R^2=\operatorname{Var}(V_{i,t})+\mathbb E[\operatorname{Var}(R_i\mid S_{i,t})].
$$

An early, irreversible sign error may make failure predictable; an error in the final digit may leave success uncertain until the end.

A prefix-only residual critic trained to predict $R_i-B_i$ has ideal prediction

$$
v_{i,t}^*=\mathbb E[R_i-B_i\mid S_{i,t}]=V_{i,t}-\mu.
$$

Subtracting it gives

$$
A_{i,t}^{(*)}=(R_i-V_{i,t})-(B_i-\mu),
$$

with variance

$$
\operatorname{Var}(A_{i,t}^{(*)})=(1-f_t)\sigma_R^2+\frac{\sigma_R^2}{G-1},
$$

where $f_t=\operatorname{Var}(V_{i,t})/\sigma_R^2$ is the fraction of reward variance predictable from the prefix. Note that this is a sum of the standard optimal value function variance (first summand) with the group reward variance (second summand). The critic removes predictable reward variation, but cannot predict the independently sampled baseline noise. This information-based distinction is central to interpreting critic variance reductions \[[7](https://openreview.net/forum?id=4TBXSf38jT), [12](https://openreview.net/forum?id=Rq6wikzBdc), [13](https://arxiv.org/abs/1802.10031), [14](https://arxiv.org/abs/2608.16739)\].

Finally, define explained variance as the fraction of original advantage variance removed (higher means lower remaining variance):

$$
\mathrm{EV}_t=1-\frac{\operatorname{Var}(R_i-B_i-v_{i,t})}{\operatorname{Var}(R_i-B_i)}.
$$

The preceding formulas give the ceiling

$$
\mathrm{EV}_t\leq\left(1-\frac1G\right)f_t.
$$

If the residual predictor also receives the realized baseline $B_i$, its ideal prediction can subtract that baseline explicitly. Denote this baseline-aware predictor and advantage by $\widetilde v$ and $\widetilde A$:

$$
\begin{aligned}\widetilde v_{i,t}^*&=\mathbb E[R_i-B_i\mid S_{i,t},B_i]=V_{i,t}-B_i,\\\widetilde A_{i,t}^{(*)}&=R_i-B_i-\widetilde v_{i,t}^*=R_i-V_{i,t}.\end{aligned}
$$

The group-baseline noise now cancels, leaving only the reward variation that is unpredictable from the prefix:

$$
\operatorname{Var}(\widetilde A_{i,t}^{(*)})=(1-f_t)\sigma_R^2.
$$

Relative to the same group-only advantage, this gives the higher explained-variance ceiling:

$$
\mathrm{EV}_t\leq 1-\frac{(1-f_t)\sigma_R^2}{\sigma_R^2+\sigma_R^2/(G-1)}=\frac1G+\left(1-\frac1G\right)f_t.
$$

The extra $1/G$ is exactly the fraction of original advantage variance contributed by group-baseline noise. This higher ceiling requires access to $B_i$; with a perfect predictor, the resulting advantage is identical to that of an ordinary value function.

We estimated prefix values on two single-turn tasks (the maths dataset from DAPO and an internal dataset we called register-tracking) with Qwen3-4B. We sampled 16 fresh continuations at eight positions along each of eight answers for 64 prompts. These averages estimate conditional expected rewards, with finite-sample uncertainty. Our estimated $f$ values of 0.31–0.54 imply prefix-only ceilings of approximately 27–47% for $G=8$. This gives us a baseline cancellation of approximately 40–60%.

While a learned value function can reduce variance, this comes with physical constraints, namely the following:

1. The Carnot-style maximum efficiencies established in the EV bounds above, and
2. The opportunity cost in extra compute for evaluating the learned value function.

The relevant comparison is therefore reward-derived advantage variance per unit of compute. The critic does not change the reward variance $\sigma_R^2$ itself; it reduces the variance of the residual used as an advantage. Let $A^{(0)}=R-B$, $A^{(v)}=R-B-v_t$, and $\sigma_A^2=\operatorname{Var}(A^{(0)})$. By the definition of EV,

$$
\operatorname{Var}(A^{(v)})=(1-\mathrm{EV})\operatorname{Var}(A^{(0)})=(1-\mathrm{EV})\sigma_A^2.
$$

For $K$ independent groups, take one designated answer at a fixed token position from each group. The mean of these independent advantage samples has variance $\sigma_A^2/K$ without the critic and $(1-\mathrm{EV})\sigma_A^2/K$ with it. Here $G$ counts answers per prompt, while $K$ counts independent groups; this avoids treating advantages that share a group baseline as independent.

Suppose the critic adds a fraction $c$ to total compute per group, including its evaluation and training. Assuming linear cost scaling, this compute could instead process $(1+c)K$ groups without a critic. The critic yields lower variance at equal compute when

$$
\frac{(1-\mathrm{EV})\sigma_A^2}{K}<\frac{\sigma_A^2}{(1+c)K},
$$

or equivalently,

$$
\mathrm{EV}>\frac{c}{1+c}.
$$

The implied compute-efficiency multiplier is $1/[(1+c)(1-\mathrm{EV})]$. This is the standard cost–variance comparison for Monte Carlo estimators \[[15](https://doi.org/10.1007/978-94-009-5819-7)\].

This calculation uses the advantage EV measured in our experiments. Interpreting its efficiency multiplier as policy-gradient efficiency additionally assumes that gradient variance falls proportionally to advantage variance. The values in Table 2 are therefore EV-based compute-efficiency estimates.

**Table 2. Additional critic compute** $c$ **and advantage EV measured offline on reasoning-gym rollouts from Qwen3-4B. This uses critics that also receive the group baseline. Required EV is the break-even threshold** $c/(1+c)$**. The multipliers here are EV-based estimates.**

| Critic type | c | Required EV | Advantage EV | Compute efficiency multiplier | 
|---|---|---|---|---|
| Value head (last 3 of 36 layers) | 0.083 | 0.08 | 0.248 | 1.23x | 
| Value head (last 6 of 36 layers) | 0.17 | 0.15 | 0.286 | 1.20x | 
| Separate critic (trained once per batch) | 0.75 | 0.43 | 0.354 | 0.88x | 
| Our critic (trained twice per batch) | 1.83 | 0.65 | 0.354 | 0.55x | 

Amidst a resurgence in papers revisiting the tradeoffs of learned value functions and group estimates, we conduct some analysis in the combined regime of the two to see how much we can push efficiency of the variance reduction. Theoretically, and to some extent empirically, we find that even a perfect critic only removes at most 40-60% of advantage variance, and to be compute efficient it must remove more of this variance than the proportional compute used to train it. As seen in recent ICLR submissions, and by our positive results for a cheaper critic on an easier-to-learn function (residuals to held-out group reward means), critics are better suited to more specialized tasks that require less predictive power, such as providing intermediate credit assignment (e.g. between turns) \[[9](https://openreview.net/forum?id=6LRYa55PMD)\] or stopping rollout generation early \[[10](https://openreview.net/forum?id=bUk8OiOoR9)\].

1. Zhihong Shao, Peiyi Wang, Qihao Zhu et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. [arXiv:2402.03300](https://arxiv.org/abs/2402.03300), 2024.
2. John Schulman, Filip Wolski, Prafulla Dhariwal et al. Proximal Policy Optimization Algorithms. [arXiv:1707.06347](https://arxiv.org/abs/1707.06347), 2017.
3. John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, Pieter Abbeel. High-Dimensional Continuous Control Using Generalized Advantage Estimation. ICLR 2016; [arXiv:1506.02438](https://arxiv.org/abs/1506.02438).
4. Arash Ahmadian, Chris Cremer, Matthias Gallé et al. Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs. [ACL 2024](https://aclanthology.org/2024.acl-long.662/); [arXiv:2402.14740](https://arxiv.org/abs/2402.14740).
5. DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), 2025.
6. Anonymous. Learning What the Group Cannot Tell: Decomposed Critics for LLM Reinforcement Learning (GAVE). ICLR 2027 submission #40160 (under review), [openreview.net/forum?id=Mar13jaBrq](https://openreview.net/forum?id=Mar13jaBrq), 2026.
7. Anonymous. PACT: From Credit Assignment to Critic Alignment. ICLR 2027 submission #30208 (under review), [openreview.net/forum?id=4TBXSf38jT](https://openreview.net/forum?id=4TBXSf38jT), 2026.
8. Anonymous. Bringing Value Models Back: Generative Critics for LLM Reinforcement Learning (GenAC). ICLR 2027 submission #9841 (under review), [openreview.net/forum?id=fLtvoMCPTj](https://openreview.net/forum?id=fLtvoMCPTj), 2026.
9. Anonymous. Turn-Level Critic Guidance for Training and Inference in Terminal Agents (TCG-GRPO). ICLR 2027 submission #45676 (under review), [openreview.net/forum?id=6LRYa55PMD](https://openreview.net/forum?id=6LRYa55PMD), 2026.
10. Anonymous. Trust the Critic More (AC2: Actor-Critic with Action Chunking). ICLR 2027 submission #34211 (under review), [openreview.net/forum?id=bUk8OiOoR9](https://openreview.net/forum?id=bUk8OiOoR9), 2026.
11. Zichen Liu, Changyu Chen, Wenjun Li et al. Understanding R1-Zero-Like Training: A Critical Perspective (Dr. GRPO). [arXiv:2503.20783](https://arxiv.org/abs/2503.20783), 2025.
12. Anonymous. When Does Branching Pay? An Exact Variance Analysis of Tree-Structured Policy Gradients. ICLR 2027 submission #47574 (under review), [openreview.net/forum?id=Rq6wikzBdc](https://openreview.net/forum?id=Rq6wikzBdc), 2026.
13. George Tucker, Surya Bhupatiraju, Shixiang Gu, Richard E. Turner, Zoubin Ghahramani, Sergey Levine. The Mirage of Action-Dependent Baselines in Reinforcement Learning. ICML 2018; [arXiv:1802.10031](https://arxiv.org/abs/1802.10031).
14. Siddarth Venkatraman, Matthieu Dinot, Laurence Aitchison. Le Critique: Privileged Value Functions for LLM Reinforcement Learning. [arXiv:2608.16739](https://arxiv.org/abs/2608.16739), 2026.
15. J. M. Hammersley, D. C. Handscomb. Monte Carlo Methods. Methuen, 1964; [doi:10.1007/978-94-009-5819-7](https://doi.org/10.1007/978-94-009-5819-7).
