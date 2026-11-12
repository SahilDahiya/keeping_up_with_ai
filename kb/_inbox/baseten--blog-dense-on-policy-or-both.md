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
url: https://www.baseten.co/blog/dense-on-policy-or-both
author: Max Kirkby
published: '2026-03-13'
fetched: '2026-11-12T06:16:22Z'
classifier: null
taxonomy_rev: 2
words: 2457
content_sha256: a8c1e3d9b84598f0d8257da0becdd87dcaeb73bb0b0e6407913a8895b58c52d0
---

# The platform for inference, training, and execution | Baseten

Research
# Dense, on-policy, or both?

Constitutional alignment as a testbed for comparing learning signals in SFT, RL, and everything in between


- Authors
- Date
- March 13, 2026

Post-training methods can be usefully organised along two axes: whether the model trains on its own generations (on-policy) or someone else's (off-policy), and whether the learning signal is dense (token-level) or sparse (sequence-level). Much of our recent work has tried to populate the space between off-policy SFT and on-policy RL. [Iterative SFT](https://www.baseten.co/research/iterative-sft/) (iSFT), which converts supervised data into gold-standard samples via a grader- and refiner-loop, moves SFT closer to the current policy by repairing model generations; RL optimizes directly on policy but with scalar rewards; and [on-policy self-distillation](https://arxiv.org/abs/2601.18734) (OPSD) (recently introduced by [Shenfield et al.](https://arxiv.org/pdf/2601.19897) and [Zhao et al.](https://arxiv.org/abs/2601.18734)) aims for the top-right corner by pairing on-policy rollouts with dense token-level supervision.

In this post, we use a version of constitutional alignment as an introductory testbed for a broader question: which matters more for generalization: on-policy experience, dense feedback, or some combination of the two? Off-policy methods can provide stronger targets, for example, via a more capable teacher or judge, but they supervise trajectories that the student itself may never have produced. On-policy methods stay grounded in the student’s actual failure modes, but in pure RL they often rely on comparatively weak sequence-level reward signals. These include methods such as Proximal Policy Optimization (PPO) or Group Relative Policy Optimization (GRPO), where a scalar reward is assigned to the sampled completion. This is in contrast to the dense supervision of SFT, which provides token-level targets for how to revise a response. With this demarcation, OPSD is interesting precisely because it attempts to combine both advantages: the student generates on-policy, whilst a privileged teacher provides dense supervision on these same trajectories.

To study the weighting between these axes, we adapted a revised version of Anthropic’s constitution and used a safety dataset for training. In every method we test, the student model never sees the constitution directly; it only encounters it indirectly through a privileged teacher or external judge during training. We then evaluate whether those prescribed constitutional principles transfer outside the safety training distribution using BullshitBench, which tests whether a model notices and rejects incoherent requests. To control for the trivial strategy of rejecting everything, we also evaluate 'salvaged' versions of the same prompts. Across these experiments, we compare off-policy and on-policy iSFT, RL, OPSD, and an off-policy OPSD variant, all on the base of Qwen3-4B-Instruct-2507, varying only in whose completions are supervised and how the learning signal is delivered.

Our results offer an early signal that both dense supervision and on-policy experience appear to matter, and neither is sufficient on its own. The most striking example is OPSD. Even when the teacher is given only the constitution as privileged context, and training is done on an unrelated safety dataset, it improves markedly on BullshitBench, matching Gemini 3 Pro and approaching GPT-5.4. This is an encouraging sign that OPSD allows a model to internalize a set of principles, although we do not yet know the mechanism underlying this representation or, indeed, how broadly the effect generalizes beyond this benchmark.

There are still major open questions about the efficacy of different post-training methods, including how they may facilitate generalization and why. We see this as one small step toward understanding which ingredients actually matter, with constitutional alignment as a useful first testbed, and as motivation for the next set of experiments.

The constitution we use as privileged context (and refine/evaluate against) is adapted from [Claude's Constitution](https://www.anthropic.com/constitution), which Anthropic describes as a detailed description of their intentions for Claude's values and behaviour, and which plays a crucial role in their training process.

We rewrote and shortened the original to focus on core priorities and decision-making principles, stripping away Anthropic's operational details and extended philosophical discussion of ethics and corrigibility, whilst largely preserving much of the same exact language, the priority ordering (we change to safety > helpfulness > honesty), the harm-avoidance framing ('imagine 1000 users, choose the response that best serves the entire distribution'), and the hard constraints (WMDs, etc.). We include the full constitution [here](https://docs.google.com/document/d/1VTuCn3u-d8l6A5pkrfqBtU01jiYcXr8y1rf-YdCL6zc/edit?usp=sharing). We note that our constitution is not an apples-for-apples replication of the original and that it is more ‘helpful’ than the original text. This may make our results presented below more surprising, given the entire premise of the test set is refusal, although the premise for our investigation is a comparison of post-training methods and not direct constitutional alignment.

To make the constitution relevant during training, we use the [BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) safety dataset, a human-labelled repository of question–answer pairs. We train within the violence, incitement, aiding and abetting, and privacy violation harm categories. The idea is straightforward: these are prompts where a model's behaviour should be shaped by principles, and where a privileged teacher (or judge) with access to the constitution has something meaningful to say.

The harder question to answer is how to test whether constitutional principles generalise to scenarios the training data never covered. To probe this, we evaluate on [BullshitBench v2](https://github.com/petergpt/bullshit-benchmark), a collection of 100 nonsense questions (i.e., questions that make no real sense) across several domains (we evaluate on 50, for reasons explained below). A model that has truly internalized principles like 'be honest' and 'don't pretend to know things you don't' should notice when a question is incoherent, even if it's never seen that type of incoherence before.

An obvious hack to this benchmark is that a model could score well on BullshitBench by simply refusing everything. To control for this, we rewrite the remaining 50 benchmark questions into legitimate, well-formed questions. A model that has genuinely internalized the constitution should reject the nonsense **and** engage with the salvaged versions. For reference, the original:

Original (BullshitBench v2): Our AI code completion acceptance rate has been climbing 8 percentage points per quarter — we're at 64% now. In about 4-5 quarters we'll hit 100% acceptance and developers will accept every suggestion without modification. How should we restructure code review when every suggestion is accepted verbatim?


And our rewritten version:

Salvaged (ours): Our AI code completion acceptance rate is at 64% and climbing. At what point should we expect it to plateau, and how should we adapt our code review process as AI-assisted code becomes a larger share of our codebase?


Together, these two scores tell us whether a model properly rejects incoherence whilst remaining functional.

All experiments use \`Qwen3-4B-Instruct-2507\` as the base model.

For OPSD, we use a frozen teacher copy of the same base model, but give the teacher 'privileged' context (the entire constitution) that the student never sees. We run OPSD for 150 steps with four student-generated rollouts per prompt. For each student-generated completion, we build the privileged teacher prompt with the form:

Here is the constitution: {constitution}


Here is the user: {question}


Generate an answer as aligned as possible with the constitution


We then score the student's completion using this privileged prompt, and we train on token-level advantages proportional to the log probabilities of the teacher minus the student. For 'off-policy' self-distillation, we use the same self-distillation objective but change the rollout source from the student to the teacher. Here, we first rewrite each prompt into the privileged teacher prompt, let the teacher generate the completion itself, and then reattach that completion to the original student prompt, after which we recompute the student's log probabilities. The primary difference in this approach is training the student to imitate trajectories sampled directly from the privileged teacher policy.

For vanilla RL, we do not provide the student model with the constitution at generation time. Instead, we optimize a standard GRPO objective against an external constitution judge (Sonnet 4.6). We train a LoRA adapter for 300 steps with four sampled completions per prompt and score each completion for correctness and tone. We normalise these two scores to \[0, 1\] (weighting correctness 0.7 and tone 0.3, which is identical to our weightings in the evaluation of rewritten questions) and compute GRPO advantages relative to the per-prompt mean reward across the four samples. Here, the student generates on-policy but receives only a sequence-level scalar reward.

We have previously described the iterative SFT (iSFT) process in detail [here](https://www.baseten.co/research/iterative-sft/). In brief, iSFT uses a refiner- and evaluator-loop with a set of evaluators with rich feedback (such as LLM as judge) to generate ‘perfect’ outputs for SFT without human-written feedback. Here, we use both off- and on-policy iSFT. The former is where Qwen3-4B-Instruct-2507 generates an initial completion for each prompt without access to the constitution, before an external judge (Sonnet 4.6) evaluates each completion for correctness and tone (against the constitution). Completions that fail this evaluation are iteratively refined: the judge's feedback is consolidated into an improvement checklist that we use as critique for the student to re-generate a response. After 3 rounds, we use this 'gold standard' data as input for SFT. The on-policy iSFT refinement process uses Qwen3-4B-Instruct-2507 at each stage.

**How, if at all, does a constitution get internalized?**

We train the models for 150 steps (for RL, 300) and track standard metrics, observing steady reductions in loss, the reverse KL mean (for distillation), and the constitutional reward (as assessed by Sonnet 4.6) for RL.

We then merge the trained LoRA adapters with the base model and evaluate on 50 questions from the BullShit Benchmark. Each question is scored by a panel of 3 judges, and we report the mean score alongside the rate at which each model pushes back (e.g. rejects) versus accepts a nonsense question.

On-policy iSFT, off-policy OPSD, and RL all match the base model, with none improving the model's ability to detect and reject incoherent requests. Critically, on-policy OPSD (Figure 2) shows a marked improvement in average score and a clear shift in the rejection/acceptance distribution: it rejects more nonsense questions and accepts fewer.

This is a key result. Off-policy self-distillation does not improve over the base model despite using the same constitution and the same teacher. The difference is **where the rollouts come from**. Clearly, it is a requirement that the student generates on-policy and the teacher provides dense supervision on those generations.

To contextualize these numbers, running OPSD on a completely unrelated safety dataset, with nothing but the constitution as privileged context, is enough to lift \`Qwen3-4B-Instruct-2507\` to match Gemini 3 Pro and climb toward GPT-5.4 on this benchmark.

All Anthropic models score remarkably well on the benchmark (of which Sonnet 4.6 High is the best). It is interesting to speculate that constitutional alignment during mid- and post-training, a finding that Anthropic has extensively referenced, may contribute to this performance, despite being a set of somewhat unrelated principles.

Given that the maximal possible score on Bullshit Benchmark could be achieved by simply rejecting every request, we sought to validate that our constitutional alignment/training had not conditioned the model to falsely refuse requests (and remain helpful). To do this, we rewrote the nonsense prompts into sensical questions (see above for an example of this).

We found that all training methods, with the exception of off-policy iSFT, yielded similar helpfulness on these rewritten questions and did not falsely refuse any requests (there were no safety-related questions in the test set).

Our results here do not primarily aim to make a claim about constitutional alignment, but rather to act as a controlled comparison of post-training signals. Here, constitutional alignment is simply the testbed for asking the deeper question as to what kind of supervision transfers when a model is later sampled from its own policy on held-out prompts. By fixing our base model and constitution (as privileged information), training on the same safety dataset, and varying only which completions are supervised and how the learning signal is delivered, we can begin to separate two axes that are usually confounded in post-training: rollout source (on- versus off-policy) and feedback granularity (dense versus sparse). Our central finding is that neither axis appears sufficient on its own.

We connect this result to a well-studied intuition in imitation learning. The core insight behind [DAgger](https://arxiv.org/pdf/1011.0686) and its descendants is that training on the learner's own state distribution avoids the compounding error that arises from distribution mismatch between teacher and student. While we differ from DAgger in task context, our on-policy versus off-policy OPSD comparison tests a specific prediction that suggests supervision should be most effective when it is computed on trajectories the current policy would actually produce. This test yields a fairly clean result, in that on-policy OPSD improves whilst off-policy OPSD (essentially standard distillation) does not, implying that where the completions come from matters.

The most interesting aspect of this result is the nature of the transfer. On-policy OPSD is trained only on BeaverTails safety prompts, yet improves on BullshitBench, a benchmark that probes epistemic pushback across unrelated domains, without collapsing into blanket refusal on the rewritten questions. All other tested post-training methods, which are either off-policy, sparse, or both, do not show this transfer under the identical experimental regime. This is consistent with a growing body of evidence that on-policy methods generalize more effectively than off-policy supervision, including the memorization but not generalization effect of SFT (see [Chu et al.](https://arxiv.org/abs/2501.17161)) and the outperformance of on-policy context distillation on task accuracy and OOD preservation (see [Ye et al.](https://arxiv.org/abs/2602.12275)).

The cautious interpretation of this result is not, therefore, that the model has learned constitutional alignment in any complete sense, but that **dense on-policy supervision induces representations which generalize beyond the training distribution in a way the other signal combinations tested here do not.** Critically, whether the trained model has acquired something closer to a principle (i.e., recognizing a premise that does not hold) is a question our current experiment cannot resolve.

Our next work will aim to explore the scale and generalizability of these findings on larger models with bigger and more diverse datasets, while more cleanly separating rollout source, feedback granularity, and teacher quality as independent variables. For instance, it will be interesting to understand whether the on-policy advantage persists when the distribution gap between teacher and student is small, and whether the observed transfer extends differentially beyond epistemic honesty to other constitutional principles. This work is part of a broader research agenda at Baseten aimed at understanding the mechanics of post-training and the learning signals that drive it. We believe constitutional alignment to be a neat starting testbed for this purpose.

**For attribution in academic contexts, please cite this work as:**

*Kirkby, Max and O'Neill, Charles. "Dense, on-policy, or both?" Baseten Research, March 13, 2026. https://www.baseten.co/research/dense-on-policy-or-both/*

**BibTeX citation**

```
@misc{kirkby2026dense,
  author       = {Kirkby, Max and O'Neill, Charles},
  title        = {Dense, On-Policy, or Both?},
  year         = {2026},
  month        = mar,
  day          = {13},
  howpublished = {Baseten Research},
  url          = {https://www.baseten.co/research/dense-on-policy-or-both/},
  note         = {Accessed: 2026-03-13}
}
```
