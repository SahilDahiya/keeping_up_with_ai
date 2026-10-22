---
title: 'Train Muse Glimmer for free: Our recipe for out-betting Jev'
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/evaluation
- inference/serving
summary: Fireworks fine-tuned Muse Glimmer 30B with a LoRA/SFT adapter and K-way cross-entropy
  loss on Kalshi prediction-market questions, beating Jev by 11.2pp on unseen topics
  (58.3% vs 47.1%) after per-question-type confidence calibration, and served the
  result 2-3x faster via the System One API on a single B200.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/train-muse-glimmer-for-free
author: null
published: '2026-10-20'
fetched: '2026-10-22T06:09:40Z'
classifier: claude
taxonomy_rev: 2
words: 1479
content_sha256: 465c91f551b1b264cea93969d85321cffdd53cf165671ef22b9c9a2ff9bd3a7c
---

# Train Muse Glimmer for free: Our recipe for out-betting Jev

- •**Muse Glimmer 30B is free to train with supervised fine-tuning (SFT) through November 30**, kicking off our Free Weights Club.
- •**Tuned Muse Glimmer outperformed Jev by 11.2 percentage points in prediction accuracy on unseen topics**, reaching 58.3% versus 47.1%. In a historical backtest, it also turned a hypothetical **$1,000 into $1,071 after modeled trading fees**, while both Jev and base Glimmer lost money.
- •**Fireworks’ optimized System One serving stack delivered 2-3× faster median server processing** than standard BF16 chat completions in a separate synthetic benchmark. Both used the same adapter and a single B200 GPU; precision and runtime differed.
- •**Try our experiment with the [Kalshi cookbook](https://github.com/fw-ai/cookbook/blob/main/training/examples/decision/kalshi_v1/README.md).** For your own projects, [Managed Training](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) runs the SFT job from your examples, while the [Serverless Training API](https://docs.fireworks.ai/fine-tuning/training-api/serverless) gives you control over the training loop.

Welcome to the **Fireworks Free Weights Club**. For a limited time, we’ll bring you new post-training research, a recipe you can build on, and free training on a featured model so you can run experiments of your own.

First up: **Muse Glimmer 30B, with SFT training free through November 30.** It’s multimodal, offers strong performance for the cost, and makes a great starting point for personal agents.

For our first experiment, we asked whether training Muse Glimmer on historical Kalshi markets could give it an edge in predicting outcomes. We evaluated its predictions against Jev and the original model on markets excluded from the training set.

We call the version we trained **tuned Glimmer** and the original model **base Glimmer**. Tuned Glimmer came out ahead of both comparison models on prediction accuracy. In a historical backtest, it turned a hypothetical **$1,000 into $1,071** after modeled fees, while both comparison models lost money.

Here’s what we trained, how we tested it, and how you can try it yourself.

Jev gave us a model to beat; Kalshi gave us a way to keep score.

Settled markets come with an answer key: take “Will the high in New York exceed 80°F?” Once the market settles, there’s an outcome to check the prediction against. The challenge is learning something that carries over to the next question.

Each example contained the market’s title, description, rules, and date, with the settled outcome as its label. The model saw no market prices or news.

We kept training, calibration, and evaluation separate:

- •**Training:** 20,051 questions from 6,461 events that settled before January 4, 2026.
- •**Calibration:** 6,232 questions from 2,000 events that opened January 11 or later and settled before April 1, 2026.
- •**Evaluation:** 33,712 questions from 8,765 events that opened April 8, 2026 or later.

Within the evaluation set, **3,567 questions came from 113 topic families excluded from both training and calibration**. We report results for the full test set and this unseen-topic subset to examine how well Glimmer handled later events and unfamiliar topics.

We removed near-duplicate inputs, rule edits made after markets opened, and later-added winning options that could reveal outcomes. Each test event was evaluated once.

These questions already have a menu of possible answers. We used the **Fireworks Training API with K-way cross-entropy loss** to train Glimmer to assign higher probability to the correct outcome. The loss considers only the answer choices for that question, rather than the model’s full vocabulary.

We trained a LoRA adapter using SFT, with one pass through the training data.

On the full test set, tuned Glimmer reached **64.8% accuracy**, compared with **56.4%** for base Glimmer and **45.9%** for Jev.

On unseen topics, tuned Glimmer reached **58.3%**, ahead of base Glimmer’s **53.2%** and Jev’s **47.1%**. That puts it **11.2 percentage points ahead of Jev** on topic families it hadn’t encountered during training.

The common-answer reference always chooses “No” for yes/no questions and the most frequent correct option position for multiple-choice questions. It uses the evaluation answers to establish that reference, so it provides context rather than representing a trained predictor.

A 51% prediction and a 90% prediction might both land on “Yes,” but we’d want to treat those calls differently. Before using tuned Glimmer’s probabilities to select and size bets, we calibrated its confidence against observed outcomes.

We fitted a separate **calibration temperature for each question type** using the held-out calibration set. This rescales tuned Glimmer’s probabilities without retraining its weights. The goal: predictions assigned an 80% probability should come true about eight times out of ten.

Only tuned Glimmer received this calibration step, base Glimmer received neither task-specific training nor calibration. We used Jev’s probabilities directly from its API without additional calibration, consistent with its intended out-of-the-box use.

The chart shows accuracy minus confidence on the evaluation data. Closer to zero is better; negative values indicate overconfidence and positive values indicate underconfidence.

Tuned Glimmer’s confidence wasn’t just bravado. When it assigned an answer **at least 80% probability**, it was right **86.8% of the time**, both across the full test and within the unseen-topic subset.

It was also selective: **14.4% of full-test questions and 6.1% of unseen-topic questions** cleared that threshold. Filtering for confidence gave us fewer predictions, but a much stronger hit rate.

There’s a pattern to those confident calls. Many were “No” answers to related threshold questions, such as whether a value would exceed 100, 110, or 120. Those outcomes often move together, so the correct predictions aren’t all independent successes.

A confident prediction still needs a worthwhile price. If a bet pays $1 when it wins and the model estimates an 80% chance of winning, its expected payout is 80¢. Our rule required the purchase price plus modeled fees to be at least 5¢ below that estimate.

We gave each model **$1,000 in hypothetical money** to allocate across qualifying bets. Every model used the same rule and the same set of eligible historical quotes. An outcome had to have more than a 50% predicted chance of winning, and higher probabilities received larger allocations.

We used the last completed hourly bid/ask quote at or before **two hours after each market opened**. The models never saw those prices; we used them afterward to decide which bets qualified.

Tuned Glimmer’s allocation finished at **$1,071 (+7.1%)**, compared with **$950 for base Glimmer (−5.0%)** and **$919 for Jev (−8.1%)**, after modeled trading fees. We were glad to keep those last two losses hypothetical.

The backtest spread a fixed budget across historical bets, including overlapping ones, rather than simulating cash being reinvested over time. It allowed fractional contracts and did not model liquidity, slippage, or historical fee changes.

How much did the result depend on which events happened to be in the test? We estimated uncertainty by resampling whole events, keeping related bets together. Tuned Glimmer’s **90% event-bootstrap interval was +1.6% to +12.4%**.

On unseen topics alone, a separate $1,000 allocation returned **15.2%**, but its wider interval of **−2.9% to +33.5%** still included losses. These intervals capture variation across events, not every source of uncertainty in model selection or trade execution.

We have a reason to keep testing. Whether the result holds up with real money remains an open question.

For this task, we needed probabilities for a fixed set of answers. Generating a written response added work we could skip.

Fireworks’ [**System One API**](https://docs.fireworks.ai/api-reference/post-systemone) reads option probabilities directly, without generating answer text. It also packs multiple questions about a shared context into one request. Each question can use that context without attending to the other question branches, so we can reuse the context while keeping the decisions separate.

In a separate synthetic benchmark, System One delivered **2-3× faster median server processing** than standard BF16 chat completions, using the **same adapter and single B200 GPU**. At **16-32 questions per request**, it delivered **up to 3.6× more decisions per second**.

Precision and runtime differed, so these results compare the complete serving stacks. This benchmark is separate from the Kalshi comparison with Jev.

The cookbook includes instructions for serving the trained model through `/inference/v1/systemone`.

You don’t need trading ambitions to try this. Your first experiment could start with a mistake you’ve corrected one too many times.

Maybe your agent keeps choosing the wrong tool. If you save its runs, successful calls and corrected mistakes could become examples for SFT. Train on some, test on others, and see whether you’re making that correction less often.

**[Try the Kalshi experiment yourself](https://github.com/fw-ai/cookbook/blob/main/training/examples/decision/kalshi_v1/README.md).** The cookbook includes the code, evaluation results, and methodology, and walks you through the experiment using the Training API.

For your own experiment:

- •**Let Fireworks run the job.** Bring your examples to [Managed Training](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) and start in the app or via API.
- •**Control your training loop.** Use the [Serverless Training API](https://docs.fireworks.ai/fine-tuning/training-api/serverless) to write your own SFT loop.
- •**Put your coding agent to work.** Install Fireworks training skills with the [Agent Skills guide](https://docs.fireworks.ai/fine-tuning/agent/use-with-coding-agents), then describe what you want to train.

Muse Glimmer 30B is free to train with SFT through November 30, with no credit card required. Inference, including evaluation calls, is billed separately.
