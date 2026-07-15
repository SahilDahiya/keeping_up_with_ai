---
title: The generative recommender behind Shopify's commerce engine (2026)
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- rag-retrieval/search
summary: Shopify's generative recommender treats a buyer's cross-storefront event
  history as a sequence and predicts the next action, a sequence-modeling approach
  to commerce recommendations over months-long journeys.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/generative-recommendations
author: Yang Liu
published: '2026-02-25'
fetched: '2026-07-15T00:53:11Z'
classifier: claude
taxonomy_rev: 2
words: 1729
content_sha256: 6a9ae26654ecd0c020f4f326e3c2985698bca6675b61cade4828bfff558d4780
---

# The generative recommender behind Shopify's commerce engine (2026)

A buyer's journey through Shopify isn't a click. It's a sequence—searches, views, add-to-carts, favorites, purchases—spread across storefronts and the Shop app, stretching back months. That sequence carries meaning in its order, timing, and gaps between events.

A good recommendation reads that sequence and predicts what comes next. At Shopify's scale (millions of products and billions of events), getting this right requires a model that can work with the full sequence, not just a summary of it.

This is how we built a foundational generative recommender: a system that learns directly from raw event sequences, operates within real production latency constraints, and delivers measurable impact at scale. We'll cover the architecture decisions, the training strategies that actually moved the needle, and what happened when we shipped it.

## The scale of the opportunity

The Black Friday Cyber Monday weekend is the clearest reminder that recommendations at Shopify are built in an environment defined by scale. During BFCM 2025, Shopify observed 2.2 trillion edge requests, and more than 81 million consumers bought from Shopify-powered brands. That customer count is based on unique buyer emails associated with purchases made from Shopify merchants over the BFCM weekend.

Those numbers describe the amount of signal available to learn from, and they also describe the engineering constraints of serving recommendations in real time. If you want recommendations that feel consistently relevant, you need a model that can read that story and predict what comes next.

## The problem we set out to solve

We frame the core task in a simple way: given a buyer journey, recommend the next products, and in some contexts the next ads. This framing matters because it turns recommendation into next-step prediction over sequences. That is exactly the setting where generative modeling performs well.

Instead of relying on extensive feature engineering to represent every possible context signal, we train an autoregressive model with a causal mask so it learns to predict the next token. In our case, the token is typically a product. When the model is trained on raw event sequences, it can learn patterns that would otherwise be difficult to specify by hand, including subtle shifts in intent, long-range preferences, and seasonal behavior.

## Scaling toward production

Early in this work, we built on [HSTU](https://rectools.readthedocs.io/en/stable/examples/tutorials/transformers_HSTU_tutorial.html), a generative recommender architecture designed for sequential recommendation. It aligned well with our problem and also showed encouraging scaling behavior, where validation loss improves as model capacity grows.

As the project matured, the system evolved along three main dimensions:

- 
**Data:**We enriched the data as we combined more sources to represent the buyer journey more completely. This includes user activity within the Shop app and across various storefronts.
- 
**Model:**We introduced innovative time encoding into the model along with improved negative sampling.
- 
**Compute:**We implemented optimized CUDA kernels that have allowed us to train and serve the model within memory and latency budgets.

That last point is easy to underestimate. A recommender that is powerful but slow does not help buyers. A recommender that is fast but simplistic can leave value on the table. The work only matters when it can be deployed and measured.

## What actually improved quality

Over time, we saw substantial gains in offline quality, and we also saw these gains translate online. The improvements did not come from a single change. They originated from a set of ideas that reinforce each other, and they all trace back to one principle: Commerce is context. Below, we will highlight a few techniques we used to extract maximum information from commerce contextual signals.

### Time is meaning in commerce

If a buyer searches for t-shirts, views a few, and purchases one, an obvious next recommendation might be more t-shirts. That recommendation can be correct in the moment, but it can become wrong as soon as the season shifts. Browsing history in June and the same browsing history in December should not lead to the same outcome.

In commerce, the time of past events matters, and the time of the current session often matters even more because it anchors what is relevant *right now.*

![Time is meaning](https://cdn.shopify.com/s/files/1/0779/4361/files/Time_is_meaning.png?v=1771950359)

We treated time as a first-class signal inside attention by encoding timestamps directly. We used a RoPE-inspired rotary encoding so attention can carry an absolute (like notion of time), and we combined it with relative attention bias so the model can represent time gaps and recency. We also designed the approach so the model can incorporate the current session timestamp at inference, which helps the model adapt to seasonality without requiring manual rules.

Once time is encoded in a way the model can use, the system stops behaving like a generic sequence predictor and starts behaving like a commerce model that understands that context changes.

### Negative sampling is a scaling axis, not a training detail

In a large commerce catalog like Shopify’s, the output space is enormous. Training a next item model over millions of products requires approximations, and sampled softmax is a practical choice. The behavior of sampled softmax depends on the negatives you show the model. If the negatives are too easy, the model learns a weak representation. If the negatives are informative, the model learns sharper boundaries between similar products, and retrieval quality improves.

![Negative sampling](https://cdn.shopify.com/s/files/1/0779/4361/files/Negative_sampling.png?v=1771950412)

We invested deeply in negative sampling because we kept seeing the same pattern: as the number and quality of negatives improved, the model improved. The challenge is that scaling negatives increases memory use, and that forces you to pay attention to GPU utilization and end-to-end efficiency.

Two strategies helped:

- Shared negatives let us effectively expand the negative pool by sharing across the batch, which increases coverage without exploding memory the way per-example negatives can.
- Positive-aware hard negatives helped because sampling negatives uniformly from a large pool can treat potential true positives as negatives, which can catastrophically mislead contrastive learning. The most useful mistakes are usually near misses, but those near misses must be selected carefully to avoid false negatives that look incorrect only because the user never saw the item.

Negative sampling became one of the most important levers we had, and it only worked because we treated systems efficiency as part of the modeling problem.

### Incremental recall matters more than isolated recall

A production recommender system is usually an ensemble. Multiple retrieval models generate candidates, rankers reorder them, and aggregation layers handle deduplication, diversity, and business constraints. In that environment, a single model can look strong offline while adding little value to the overall system if it mostly repeats what other models already find.

![Incremental recall](https://cdn.shopify.com/s/files/1/0779/4361/files/Incremental_recall.png?v=1771950446)

We wanted our generative recommender to provide incremental value, which means it should find true positives that other retrieval models miss. That requirement changes how we train. We used a boosting-inspired approach that increases training pressure on the parts of the space where the ensemble is weak, and can also treat other models’ predictions as hard negatives. The goal is not novelty for novelty’s sake; the goal is coverage where it matters so the ensemble becomes stronger, not just bigger.

## Making it fast enough to matter

Long sequences, time-aware attention, and large negative pools are expensive. If you train them naively, you get slow iteration cycles and limit how far you can scale. We focused heavily on training efficiency and optimized the pipeline so we could move faster.

In our internal benchmarking, the full training pipeline reached up to 7.3x speedup relative to a baseline implementation for the workloads we cared about.

![Speed](https://cdn.shopify.com/s/files/1/0779/4361/files/Speed.png?v=1771950484)

That speedup matters because it translates directly into iteration velocity. When training becomes faster, you can explore model capacity, batch size, and context length more aggressively. You can also test hypotheses that would otherwise be too costly to evaluate. At Shopify scale, the practical ability to iterate is part of what makes a system competitive.

## What this delivered in production

Offline improvements only matter if they lead to better buyer experiences and better outcomes. In online AB testing of an August model version, we saw positive movement across key metrics.

Shop orders increased by 0.94% relative. High quality click-through rate increased by 5% percent relative (defined as clicks that led to actions closer to buying like favoriting, adding to cart, or purchasing). Conversion rate increased by 0.71% relative.

We also saw a lift in final served product recall at 2 by 4.8% relative, which supports the idea that offline retrieval quality can correlate with online outcomes when the system is trained and evaluated carefully.

![Stats](https://cdn.shopify.com/s/files/1/0779/4361/files/Stats.png?v=1771950510)

## Where we go next

As generative recommenders scale, one limitation becomes more visible: when products are modeled independently, the system relies on very large embedding tables and operates over a huge product ID space. That can become a bottleneck, especially when you want to incorporate richer signals like text queries and assistant interactions while keeping serving costs predictable.

One direction we’re exploring is moving from product ID space to token space through semantic IDs. The idea is to learn a representation where products and other entities can be expressed as sequences of tokens from a much smaller vocabulary. Once that exists, the next step is to train a model that can work over both semantic ID tokens and text tokens so it can integrate additional context sources. This direction is promising because it can reduce the dependence on massive product ID embeddings while opening the door to more flexible behaviors, including prompt-driven task adaptation in a way that stays grounded in Shopify’s commerce context.

## What foundational means to us

Foundational generative recommendations are not a single model release. They are an approach that treats buyer journeys as sequences, time as context, negative sampling as a core scaling lever, and system-level value as the objective.

When these pieces come together, you get a recommender that is not only accurate offline but also impactful online, and you get a platform that can keep improving as data, models, and infrastructure evolve.

For more, check out our talk on this topic at [NeurIPS 2025](https://neurips.cc/virtual/2025/loc/san-diego/128667).

*If you’re interested in joining us on our mission to make commerce better for everyone, check out our  careers page.*

Yang Liu is a Senior Staff Machine Learning Engineer at Shopify. His interests include artificial intelligence and multimedia. Contact him at [yang.liu@shopify.com](https://shopify.com).

Ali Khanafer is a Senior Staff Machine Learning Engineer at Shopify. His interests include machine learning and control theory. Email [ali.khanafer@shopify.com](https://shopify.com).
