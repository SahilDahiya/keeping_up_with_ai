---
title: Sidekick's continual learning loop (2026)
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/llm-as-judge
- agents/harness
summary: 'Shopify''s continual learning flywheel for its GraphQL merchant agent: calibrate
  an LLM judge with Cohen''s kappa against expert annotators, use GEPA/ACE and Toloka
  human review to heal failed production trajectories, then distill them into a smaller
  model via SFT and GRPO, plus gist-token prompt compression (6k to ~1.5k tokens).
  The specialized model cut serving cost from an estimated $27M to $1M/year (96%)
  and reduced end-to-end latency ~38% while beating the frontier baseline.'
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/sidekicks-continual-learning-loop
author: Andrew McNamara
published: '2026-08-05'
fetched: '2026-08-06T06:58:58Z'
classifier: claude
taxonomy_rev: 2
words: 1971
content_sha256: 3aaba8f18d0ac363f14eeab3cc7078125e87c36c064062b49d784e1fa8e813fb
---

# Sidekick's continual learning loop (2026)

Frontier models are often the fastest way to launch a new AI product. A small team can get something useful in front of users quickly and learn from real-world usage. But as usage grows, the economics change: frontier models can be too slow and expensive to serve every request at scale.

Frontier models are general-purpose, not tailored to your product. More importantly, they do not learn from production on their own. A user correction, rejected output, or recurring failure does not make the next response better. But each failure is hard-won knowledge about your product, and continual learning begins by capturing that knowledge and feeding it back into the system.

A deployed frontier model is also frozen. It has no mechanism for internalizing what production teaches it. Instead, improvements accumulate in the discrete artifacts around it: prompt edits, retrieval examples, routing rules, and harness code. Production knowledge piles up in words and code while the model’s weights remain untouched. The flywheel is our answer: a continual learning loop that compresses production experience into the continuous space of the model’s weights.

Shopify's GraphQL agent is our clearest example of that loop running in production. That flywheel delivers higher quality than frontier models while reducing latency and cutting costs by 96%.

![Flywheel loop](https://cdn.shopify.com/s/files/1/0779/4361/files/Ground_truth_set.png?v=1785936533)

## Start with defining quality; it becomes the reward signal

Defining quality is the most important step in the loop—and the one that teams most often rush. It begins as a specification of what good looks like and becomes the reward signal that drives learning. When you get it wrong, everything downstream optimizes the wrong behavior.

Quality starts with a rubric, and that rubric turns your product requirements into a few scored criteria: completeness, execution, response quality, and safety. Each one has concrete anchors for what every score means. Think of it as your product team's definition of good and bad. It’s the quality contract for everything downstream, and what annotators use to turn conversations into ground truth. Crucially, that ground truth should include randomly sampled traffic, not only curated examples. Golden sets test the cases you already know to look for; random samples reveal what good and bad actually look like in production.

Once you’re happy with the rubric, have your two best annotators/product experts blindly annotate 25 random samples and record their inter-annotator agreement. We use [Cohen's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa), which measures agreement above chance. If it’s very low (around 0.2), the rubric is ambiguous: meet again and iterate. If the rubric confuses several product experts who work on this product every day, it will confuse an LLM too.

That agreement is the judge's ceiling: even expert annotators do not agree 100% of the time, because some conversations are genuinely ambiguous. The goal is not a judge that is "perfect," but one that matches humans about as well as humans match each other.

When you collect annotations, push for detail. A score and one sentence is not enough for the calibration algorithms to learn from. You want the *why* behind every score, and that reasoning is gold.

![Judges' agreement](https://cdn.shopify.com/s/files/1/0779/4361/files/Judges.png?v=1785936577)

## Calibrate your judge

The rubric is just the starting point. It’s the judge's first prompt, but it hasn’t learned anything from your ground truth yet. Calibration will take that rubric and turn it into a judge that can be run on infinite production datapoints.

We’re big fans of DSPy for this, and we calibrate with reflection-based optimizers like GEPA and Agentic Context Engineering [1,2]. GEPA evolves the prompt by reflecting on natural-language failure traces and keeps a Pareto frontier of candidates instead of greedily choosing a single winner. ACE curates a structured playbook through small incremental edits.

The judge is your offline metric, the thing you optimize against before you ship. But it’s only a proxy, so you need to establish that it reflects performance on real traffic and is aligned with your online metric. Backtest it against previous A/B tests: can it recover the direction of known wins and losses in engagement, retention, or the behavior your product is designed to drive?

Then run targeted degradation tests, either offline or on a carefully controlled slice of traffic. Deliberately make one behavior worse and confirm that the corresponding criterion responds. If the system stops trying to fulfil the user’s goal, for example, the goal-fulfilment score should fall specifically.

Keep each judge small and targeted rather than cramming all of your product’s behavior into one. Focused judges make these tests easier to interpret and the resulting metrics easier to trust. You can always add more.

## Improve the frontier baseline with autoresearch

Now that we have a reliable judge, we can use it to improve the initial frontier-powered product we launched, the baseline built to get in front of users quickly. At this stage, we push that system as far as it will go without touching the weights. Every improvement lands in prompts, tool definitions, and harness.

But improving this baseline system is a different problem from building the judge. It’s already a production application, with dynamically assembled prompts, custom control loops, and bespoke orchestration spread across a large codebase. No single prompt determines its behavior, so prompt tuning reaches only a small part of the system. The optimization target is the entire harness: its prompts, tool definitions, and orchestration code.

So we treat it as an [autoresearch](https://shopify.engineering/autoresearch) problem, in the spirit of [Karpathy's recent project](https://github.com/karpathy/autoresearch): an agent proposes a change to a prompt, a tool definition, or the harness; evaluates it against the judge; keeps the change if the score improves; and discards it otherwise.

We configure the whole thing in one readable markdown file: where to get data, which directories the agent may edit, the judge as the metric, the optimizer to use, and the propose-evaluate-keep-or-discard loop.

![Autoresearch format](https://cdn.shopify.com/s/files/1/0779/4361/files/program.md.png?v=1785936868)

## From discrete artifacts to continuous parameter updates

Once harness improvements plateau, we begin optimizing in parameter space by mining anonymized production traffic for hard negatives: conversations the judge correctly scores low and that expose where the model is weakest.

Across millions of diverse merchants, real traffic produces a continual stream of difficult cases: partial context, ambiguous requests, business-specific workflows, tool failures, and many ways of expressing the same intent. In a traditional workflow, each failure becomes a bug report or Slack thread. In the flywheel, these failures automatically enter a self-healing pipeline, where a panel of frontier reasoning models turns them into training signal that reinforcement learning folds back into the model’s weights.

![Flywheel self healing pipeline](https://cdn.shopify.com/s/files/1/0779/4361/files/Failed_convo_flow.png?v=1785936914)

A panel of frontier reasoning models critiques each failure. An arbiter merges those critiques into a single repair instruction, which is injected before the user’s turn, a technique sometimes called “hinting.” We replay the conversation from that point, and the judge scores it again. If the repair passes, the replay becomes a trajectory for reinforcement learning, with the judge’s score serving as its reward. If it still fails, we flag it for human annotation. That is where [Toloka](https://toloka.ai/) comes in: its expert annotators correct the conversations our critics could not fix, scoring them against the same rubric used to calibrate the judge.

Training proceeds in two stages. First, we distill the healed trajectories into a smaller model through supervised fine-tuning. We train on the complete trajectories—including the reasoning that produced them—not just their final answers (see [Toloka’s Fine-tuning for agentic workflows](https://toloka.ai/blog/fine-tuning-for-agentic-workflows-building-a-production-cv-parser-with-shopifys-tangle/)). This chain-of-thought distillation lets the smaller model inherit behavior it could not learn from answers alone [3].

Second, we apply GRPO, using the calibrated judge as the reward signal. For each prompt, the model samples a group of responses, the judges score them, and GRPO reinforces the responses that perform best. Supervised fine-tuning teaches the model successful trajectories to imitate; GRPO optimizes it directly against our definition of quality.

The self-healing pipeline runs daily, continually adding new trajectories to the training corpus. On the same cadence, we run a full-parameter fine-tune over the accumulated data and then repeat GRPO. Training on both new and previous trajectories limits drift and catastrophic forgetting across cycles [4]. As the flywheel turns, quality rises and eventually surpasses the frontier-powered baseline.

## Compress the prompt to serve it faster

A better model still has to run, and an agent's system prompt is long and static. Attention scales with sequence length, so every generated token attends over that entire prefix. A long prompt is a fixed tax on latency and serving cost, paid on every request.

Gist compression removes most of that tax. We run the same model two ways: a teacher with the full system prompt, and a student with a short sequence of learned gist tokens instead. We train the gist token embeddings to match the teacher's output distribution, with the model weights frozen. The result is a handful of tokens that reproduce the prompt's behavior at a fraction of the length, with no measured quality loss on the judge [5,6].

![System prompt vs gist tokens](https://cdn.shopify.com/s/files/1/0779/4361/files/System_prompt_vs_gist_tokens.png?v=1785936976)

## The flywheel in action: the GraphQL agent

![Flywheel in action: Merchant Sidekick conversation](https://cdn.shopify.com/s/files/1/0779/4361/files/Merchant_Sidekick_convo.png?v=1785937014)

The clearest place to see the whole loop at work is our GraphQL agent, which serves up to 2,000 requests per minute in production. It answers merchant questions about their store by writing and running queries against Shopify's Admin GraphQL API: a merchant might ask which products are almost out of stock, and the agent works out the right query, runs it against the store, and turns the result into a plain-language answer.

![GraphQL distillation](https://cdn.shopify.com/s/files/1/0779/4361/files/GraphQL_distillation.png?v=1785937045)

Here’s how it’s working:

**It made the model better.** The self-healing pipeline turns low-scoring production conversations into successful trajectories, giving the model a continual stream of lessons drawn from real merchant needs. Together, SFT and RL enable the specialized model to surpass the frontier model performance.

**It made the model far cheaper to serve.** Serving this traffic on a frontier model could easily cost an estimated $27M per year based on average token costs. The fine-tuned model could come in at a fraction of the cost, closer to $1M: a 96% reduction in serving cost. That is the difference between a feature that is painful to run at Shopify's scale and one we can comfortably leave on for every merchant.

**It made the model faster, and the gap grows under load.** Gisting compressed the agent's long, static system prompt from roughly 6,000 tokens down to about 1,500 learned gist tokens. In a load test at 350 requests per minute, time-to-first-token dropped about 19%, and end-to-end latency dropped about 38%.

**It freed up hardware.** The same compression raises throughput: about 16% more requests per second and about 12% more output tokens per second on identical GPUs, which works out to roughly 14% fewer GPUs for the same traffic.

## Beyond the harness: continual learning that compounds

Frontier models help you launch, and the first improvements live in the discrete artifacts around them: prompts, context, tool definitions, and control flow. Those changes strengthen the harness but leave the model unchanged.

Continual learning goes further, translating those lessons into updates in the model’s continuous parameter space. Each cycle begins with a more capable model, not merely a more elaborate harness. That is how a smaller model becomes faster, cheaper, and better at your task than the frontier baseline. The durable advantage is the loop that keeps turning production experience into better weights.

### References

1. Agrawal et al. GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning. arXiv:2507.19457
2. Zhang et al. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models. arXiv:2510.04618
3. Hsieh et al. Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes. arXiv:2305.02301
4. Shuttleworth et al. LoRA vs Full Fine-tuning: An Illusion of Equivalence. arXiv:2410.21228
5. Wingate et al. Prompt Compression and Contrastive Conditioning for Controllability and Toxicity Reduction in Language Models. arXiv:2210.03162
6. Mu et al. Learning to Compress Prompts with Gist Tokens. arXiv:2304.08467
