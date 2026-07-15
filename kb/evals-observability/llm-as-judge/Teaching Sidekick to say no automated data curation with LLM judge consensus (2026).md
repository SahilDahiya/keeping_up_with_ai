---
title: 'Teaching Sidekick to say no: automated data curation with LLM judge consensus
  (2026)'
kind: blog
topic: evals-observability
subtopic: llm-as-judge
secondary_topics:
- models/fine-tuning
summary: Shopify curates Sidekick training data using LLM-judge consensus to automatically
  filter examples ('teaching Sidekick to say no'), replacing manual labeling with
  judge-based quality and coverage control.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/sidekick-curation
author: Shuang Xie
published: '2026-06-15'
fetched: '2026-07-15T00:53:31Z'
classifier: claude
taxonomy_rev: 2
words: 1925
content_sha256: a7c3a6dd5166e9536ce4500b4ba8350ec0065c305b58aa9be0ee3c5bd1712819
---

# Teaching Sidekick to say no: automated data curation with LLM judge consensus (2026)

Training data has always been the hard part of machine learning. Not the architecture, not the compute, but the data itself. You need enough of it, you need it clean and diverse, and you need it to cover the cases that actually matter. Before LLMs, that mostly meant labeling pipelines and feature engineering. Now, with LLMs, the problem doesn't go away but it shifts. When you fine-tune a foundation model for a specific domain, you're teaching behavior: how the model should interpret requests, handle ambiguity, and recognize when a request is genuinely impossible. We’ve learned that the last one is the hardest to teach.

It's hardest because production data has a blind spot. Every example in a production training corpus is a success story: the model did something right, it got evaluated, it shipped. The cases where it should have refused, the edge cases, the impossible requests… those never make it into the logs. So you end up with a model trained entirely on successful queries. When it hits something it can't fulfill, there's no learned behavior to fall back on. It improvises, usually badly.

We ran into this while building Sidekick, our AI assistant for merchants. Sidekick works on two layers: an outer planner that interprets the merchant's overall intent, and a set of specialized skill models that each handle a specific capability. The planner routes "send a discount to my best customers" to segmentation, analytics, email, and so on. As we covered in our [article on building production-ready agentic systems](https://shopify.engineering/building-production-ready-agentic-systems), keeping those skills performing well takes continuous work.

Customer segmentation was the skill we started with. Segments power targeted marketing and merchandising decisions, but expressing them requires Shopify's domain-specific query syntax, which most merchants can't write by hand. We wanted a merchant to describe what they needed in plain English and have the model generate the right syntax. Fine-tuning an open-source model got us there for the common cases, but then the blind spots showed up. Our training data was tens of thousands of de-identified production queries, all successful, with zero refusals. The model had never learned to say no.

![Customer segmentation](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_1.png?v=1781896823)

**Figure 1. **Sidekick lets merchants ask questions in plain language across domain-specific skills. Customer segmentation turns requests into customer lists for campaigns, discounts, and purchasing analysis, while analytics answers store-performance questions like recent sales. Both skills hide query languages that would otherwise be difficult for non-technical merchants to write by hand.

## When it goes wrong

Our skill models were trying to be too helpful. When asked for impossible queries (finding customers who are doctors, say, when Shopify doesn't store occupation data), they couldn't just say no. Instead, the model would generate a query that returned zero results.

This gave merchants the wrong impression: not that the request was impossible, but that zero customers matched. The result was bad targeting and confused users. None of it showed up in our training metrics.

The root cause was the training data. Production logs, by construction, only capture successful queries.

## Our first attempt

To train the model to refuse impossible queries, we needed training examples showing correct refusals. The problem: our existing training data was tens of thousands of examples sampled from production traffic, and every single one was a successful query that had already passed evaluation. Production data, by construction, cannot contain the failures you're trying to train away.

We initially partnered with the Toloka team to produce a balanced dataset of roughly 600 standard queries and 602 refusal annotations.

Because this dataset was small relative to our production corpus, we tried the obvious first move: merge the two sources directly and fine-tune. This led to limited improvement.

![Naive merge problem](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_2.png?v=1781896865)

**Figure 2.** The naive merge problem. The same query appears in both datasets with opposite labels. The model receives contradictory training signals. The result is degraded stability and worse generation quality. Semantically similar requests appeared in both datasets with completely different labels. The same query that passed as successful in production was flagged as a refusal in the Toloka data. We had no way to reconcile conflicting labels at scale.

## Our approach

Instead of more manual annotation, we turned the small Toloka dataset into a seed for an automated curation engine. The idea: run a panel of frontier LLMs (Frontier LLM A, B, C, and D) as automated data judges.

### Calibrating the judges

Before turning the judges loose on the production corpus, we calibrated each one using few-shot examples from the Toloka dataset, pairing representative queries with their ground-truth labels. This kept each judge's decisions anchored to what human annotators actually flagged as impossible, not what the model assumed about Shopify's data schema.

Once calibrated, we ran the ensemble across our full training corpus. Rather than just labeling queries, the judges acted as conflict resolvers: when a query had conflicting labels across sources, the ensemble evaluated it against the seed distribution and gave it a label.

### Strict consensus over loose confidence

![LLM judge ensemble](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_3.png?v=1781896891)

**Figure 3.** The LLM judge ensemble. Each of the four judges evaluates the query independently. Only when all four agree on the same verdict, and provide consistent reasoning, does the label pass the consensus gate. Disagreements are filtered out rather than arbitrated, keeping precision high at the cost of some coverage. To avoid erratic training shifts, we required all judges to agree on both the decision and the reasoning before accepting any label change. This filters out edge cases where even the best models disagree. And they do disagree, often. We prioritized precision over recall: better to miss a valid refusal than to mislabel a legitimate merchant request. If four independent models can't agree on a label, a human should make the call.

### A taxonomy that leaves no room for ambiguity

We gave the judges four mutually exclusive categories to work with. A query was one of:

- Solvable with more context: the outer planner needed to fetch additional information first.
- Missing capability: the request asked for a Shopify segmentation feature that doesn't exist yet.
- Wrong skill: not a segmentation task at all; the planner should route it to analytics instead.
- Ambiguous: needed clarification from the merchant.

The categories had to be mutually exclusive. When they aren't, judges disagree, labels become inconsistent, and those inconsistencies propagate downstream.

![Annotation pipeline](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_4.png?v=1781896923)

**Figure 4.** The annotation pipeline decides whether to keep a production label, replace it with an annotated label, ask for clarification, or opt out entirely. Ambiguous requests are separated first, unsolvable requests become refusal examples, and solvable requests are checked against the original label.

## The data flywheel: closing the loop

The flywheel only started to matter once every production gap became fuel for the next training run. For us, that meant production traffic could not just sit in dashboards. It had to become the input to the next training run.

Once the improved model ships, its production traffic becomes the next sample. Merchants keep finding new ways to ask for the same thing, and partial phrasings expose gaps we did not have in the original training set. The judge ensemble labels those new patterns, drops the examples where the judges disagree, and adds the accepted ones back into the corpus. The next fine-tuning run starts with more data and cleaner labels.

![The complete flywheel loop](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_5.png?v=1781896959)

**Figure 5.**** **The complete flywheel loop. The improved model deploys to production. Its queries (including new edge cases it now handles correctly) become the next sampling pool. New patterns get labeled by the judge ensemble and added to the training corpus. Each cycle starts with more data and a cleaner label set than the last. Once the improved model ships, its production traffic becomes the next training sample. Patterns that didn't exist before (new refusal scenarios, new merchant phrasings) get labeled by the judge ensemble and added to the corpus. Each fine-tuning cycle starts from a bigger and cleaner baseline than the last. Each deployment funds the next improvement.

## The outcome

Resolving data conflicts stabilized training, and token prediction accuracy improved over naive merging.

With refusal capabilities enabled, our segmentation skill evaluation score went from 0.619 to 0.798, a 28.9% relative gain. But that number needs context: the production model had zero refusal training examples, so part of the gain just reflects adding any refusal data at all. Figure 7 gives a cleaner read: comparing naive merging vs. automated curation on the same baseline, curation pushed segmentation pass rate from 0.762 to 0.798.

![Production model vs. flywheel-enhanced model](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_6.png?v=1781896986)

**Figure 6:** Production model vs. flywheel-enhanced model

![Naive merging vs. automated curation](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_7.png?v=1781897014)

**Figure 7: **Naive merging vs. automated curation (both strategies fine-tuned from the same starting point)

**Note on figures:** Figure 6 compares the original production model (no refusal data) against the flywheel-enhanced model. Figure 7 compares two fine-tuning strategies applied to the same refusal-aware base.

We validated the model's behavior manually. Refusal accuracy came in at 86.3% with a false positive rate of 4.6%. For the judge ensemble, agreement with the ground truth seed data was strong: near 90% prediction accuracy and a Cohen's kappa above 0.75 across all four models. A kappa above 0.75 is substantial agreement. These offline evaluation results show the proper gains in our production tasks.

![LLM judge ensemble performance vs. ground truth](https://cdn.shopify.com/s/files/1/0779/4361/files/Sidekick_Figure_8.png?v=1781897041)

**Figure 8:** LLM judge ensemble performance against ground truth seed data

## Lessons learned

We came away with four things we hadn't fully appreciated before this.

### Small seed datasets punch above their weight

A small but high-quality annotated dataset can drive an automated curation pipeline that no manual labeling budget could replicate. The Toloka annotations were the foundation of everything, not because of their volume but because of their quality. Garbage in, garbage out applies here with extra force: the judges inherit whatever biases or errors the seed contains.

### Mutual exclusivity in taxonomy is non-negotiable

Ambiguous categories create judge disagreements that compound downstream. The upfront work of defining clean, non-overlapping categories paid for itself. Calibration was faster. Labels were more consistent. Fine-tuning was more stable.

### Consensus beats confidence in early-stage pipelines

When you don't yet know the shape of the problem, unanimous agreement is worth more than individual confidence scores. Multi-judge agreement kept precision high while we were still figuring out which edge cases mattered. If four independent models can't agree on a label, that example belongs in front of a human.

### Refusals are product features, not failures

If a system can't do something, a hallucinated answer is the worst outcome. A truthful refusal (ideally with a suggestion about what to try instead) lets the outer planner keep the conversation productive. We spent a lot of time teaching the model when to say yes. We should have started with when to say no.

## What's next

The flywheel we built for segmentation refusals is infrastructure, not a one-time fix. Each deployment generates more signal, and each gap we find becomes the seed for another annotation round. The same pattern applies any time production traffic can't capture the failures you care about.

We're now running this framework across other skill models in Sidekick, applying the same process to other data quality problems. The details change per domain (different models, thresholds, taxonomies), but the shape is the same: small high-quality seed, judges calibrated against it, unanimous consensus gate, feedback loop back to production.

The hardest part of this project wasn't the ML. It was building the infrastructure around the model well enough that the model could keep improving. That's the actual work of a data flywheel.
