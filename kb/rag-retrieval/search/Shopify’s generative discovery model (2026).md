---
title: Shopify’s generative discovery model (2026)
kind: blog
topic: rag-retrieval
subtopic: search
secondary_topics:
- product-engineering/case-studies
summary: Describes Shopify's shared generative model, jointly trained on search and
  recommendation data over a catalog of billions of products, using semantic-ID tokenization
  of product embeddings; reports production gains of +7.95% orders and +9.85% CVR
  on the Shop home feed, plus a 2.1-2.7 point OneDCG@10 improvement in search.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/generative-discovery
author: Shuying Sun
published: '2026-11-11'
fetched: '2026-11-13T06:12:19Z'
classifier: claude
taxonomy_rev: 2
words: 2566
content_sha256: f213f615e1e720975863c87bddbfa691e98ce26c524fac08a5ce3be6f7a89be0
---

# Shopify’s generative discovery model (2026)

Two people open their phones and search for “backpack.” One of them has been comparing waterproof laptop bags ever since an airborne-coffee-on-bus incident. The other has been exploring larger packs for traversing the Colorado Rockies.

The query is a starting point.

But what each buyer has explored and purchased tells us what *matters* to them. We can use that context to personalize the search results they see and the recommendations they get, so each buyer discovers relevant products from both familiar merchants and merchants they haven’t visited before.

Commerce activity across millions of participating Shopify merchants provides insights into how shoppers discover and purchase products across categories, and our commerce ecosystem spans many merchant storefronts, the Shop app, and the Catalog API designed for conversational commerce and AI agents.

The challenge is using those search, browsing, and purchase signals to find relevant products for each buyer across a catalog of billions, all within the latency budget of a live request.

Our approach builds on what search and recommendation have in common: both use product knowledge and buyer context to identify relevant products. A search query adds an explicit signal of intent; recommendation relies more on behavior to infer what may be useful next. These shared inputs and objectives make them natural tasks to train together.

We put this into practice with **a shared generative discovery model**, trained jointly on Shopify’s search and recommendation data. It generates product candidates for both experiences and is now deployed in production, bringing significant gains both offline and online.

This post explains the product representations, training recipe, and serving decisions that brought it into production.

For the full methodology and experimental results, see our [detailed technical report](https://arxiv.org/pdf/2611.08804).

## One foundation model for search and recommendation

An open-weight pretrained language model provides the starting point. Its general world knowledge offers a base for understanding product descriptions, attributes, and buyer queries. We then adapt the model using commerce data available to Shopify for this purpose, including our product catalog and eligible buyer interactions across search and recommendation.

![Buyers, queries, merchants, products, and purchases form a connected commerce foundation shared by search and recommendation.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-1-commerce-foundation.png?v=1794416267) 

To evaluate the model, we measure buyer outcomes online and retrieval quality offline.

### Current model performance

For recommendation, adding the generative model delivered the following online gains on the Shop home feed:

| **Online home feed recommendation metric** | **Relative lift** | 
|---|---|
| Orders | +7.95% | 
| Converters | +8.60% | 
| Conversion rate (CVR) | +9.85% | 

In offline evaluation, the generative model contributes **2.65pp Incremental Pool Recall** to the recommendation production system. It is also our **strongest standalone candidate generator**.

For search, the model delivers strong quality on its own and further improves the production system, with a **2.1-point gain in OneDCG@10 overall**. For signed-in users where the model can personalize the buyer's results, it delivers a **2.7-point gain in OneDCG@10**, with **25% of queries improving on net in top 10 relevance**.

OneDCG@10 is a variant of NDCG that measures search quality across the top ten results. It normalizes against ten perfect results rather than each query’s ideal ranking, giving all queries the same reference point.

| **Search configuration** | **Combined** **OneDCG@10** | **Personalized only** **OneDCG@10** | 
|---|---|---|
| Current production system without the generative model | 30.6 | 33.0 | 
| Current production system with the generative model | **32.7** (+2.1) | **35.7** (+2.7) | 
| Generative model only | 28.5 | 33.6 | 

These results rest on decisions about product representation, training, and serving. **We’ll walk through each decision,** starting with a practical way for the model to represent products.

## Giving the model a product vocabulary

Shopify’s catalog contains several billion products. A raw product ID distinguishes a database record, but its digits carry no information about the product. Treating every product as an independent output would create a vocabulary with billions of entries, each with its own representation to learn. Training examples are sparse for many products, making it inefficient to learn a useful representation for each ID independently.

Our [earlier post on generative recommendations](https://shopify.engineering/generative-recommendations) outlined a next step: representing products as semantic-ID tokens alongside text. We build on that direction by encoding product content into an embedding, which is a vector representation of the product. A tokenizer converts that embedding into a **semantic ID**: a short sequence of discrete codes that the model can learn and generate.

![Product content passes through an encoder to create an embedding, which a tokenizer converts into a three-token semantic ID.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-02-semantic-id-tokenization.png?v=1793810129) 

We evaluated RQ-VAE and RQ-KMeans, two common tokenizer methods, and selected **RQ-KMeans** because it produced better downstream performance at the same codebook shape. RQ-KMeans clusters product embeddings, subtracts the selected cluster centers, and repeats on the remaining residuals. Each level captures information left over from the previous one. Our selected configuration uses **three codebooks of 8,192 entries each**, giving each product a three-token semantic ID.

Related products can share codes, allowing their training examples to update shared representations. This gives products with few interactions a way to benefit from training on their neighbors.

A real catalog example makes this easier to see.

Products sharing the prefix \[6001\] include vests and gilets across styles and fabrics. Following one branch, \[6001, 5561\] groups padded gilets in different colors, and \[6001, 5561, 0\] narrows to gray padded designs. A second branch, \[6001, 4551\], groups workwear style gilets; \[6001, 4551, 879\] contains indigo denim vests.

![Two semantic-ID branches share the prefix \[6001\] for vests and gilets, then distinguish smaller groups as additional tokens are added.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-03-semantic-id-example.png?v=1793810179) 

Multiple products can share the same complete code sequence. We explored several ways to resolve these collisions at serving time, including a lightweight ranking step that uses product popularity when mapping semantic IDs back to products. Our [technical report](https://arxiv.org/pdf/2611.08804) covers these approaches in more detail.

## Training for product meaning and buyer intent

Our training recipe builds commerce knowledge into a pretrained language model: connecting semantic IDs to product meaning, learning from buyer journeys, refining predictions for each task, and bringing specialized experts back into one shared model. Figure 4 outlines these stages.

We uncovered **four key lessons while developing this recipe**.

![Shared commerce training develops into specialized search and recommendation experts, whose capabilities are distilled back into one shared discovery model.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-4-training-stages.png?v=1794421526) 

### Lesson 1: Search and recommendation learn from each other

We train search and recommendation together using a common product vocabulary. Figure 5 shows examples from continued pretraining, each pairing context with a completion that the model learns to predict.

![Continued-pretraining examples pair input context with target completions. The model learns from the completion tokens rather than the prompt tokens.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-05-cpt-data-examples.png?v=1793810282) 

To understand how the tasks contribute to each other, we removed search or recommendation data from the training mix:

| **Training mix** | **Search relevance OneDCG@10** | **Search purchases Recall@10** | **Recommendation Recall@50** | 
|---|---|---|---|
| Baseline | **28.8** | **33.4** | **21.0** | 
| No search data | — | — | 20.9 | 
| No recommendation data | 28.5 | 32.6 | — | 

*When a stream is removed, its share of training tokens is redistributed proportionally across the remaining streams. Dashes indicate metrics not reported for the excluded task.*

These results show that **search and recommendation improve each other through shared training**.

### Lesson 2: Discovery needs explicit training

Our existing rule-based candidate generators already handle retargeting products in the buyer’s interaction history. The harder recommendation problem is finding useful products a buyer has *never* interacted with. Histories contain many repeat visits, so a model trained on them can overemphasize products the buyer already knows.

To teach discovery explicitly, we **upsample training streams built around first purchases**: a buyer’s first purchase of a product, their first purchase from a merchant, or their first purchase in a category. This gives discovery events more weight during fine-tuning. We also compress histories by dropping old clicks and other stale interactions while retaining purchases, leaving more room for recent behavior in the context.

Discovery recall measures purchases of products the buyer had never interacted with, making it a more direct measure of this goal.

In an offline experiment, the combined history-compression and discovery recipe **improved discovery recall by roughly 10–15% relative** at cutoffs of 10 and 50, while overall recall increased by about 2% relative.

### Lesson 3: Reinforcement learning improves retrieval quality

Supervised fine-tuning teaches the model to reproduce historical examples, but **predicting the next token accurately doesn’t fully capture retrieval quality**. Multiple products can satisfy the same intent, even when the training example contains only one observed purchase or click.

For search, we use an **LLM relevance judge to provide the reward signal**. The model generates candidates, the judge evaluates their relevance, and reinforcement learning uses that feedback to refine the model’s choices. This brings training closer to what we care about: the quality of the products we retrieve for the buyer. Applying reinforcement learning for search delivered a **+1.5 lift in OneDCG@10**.

### Lesson 4: Specialized experts can strengthen a shared model

Joint training gives us a shared understanding of products and buyers. Task-specific fine-tuning and post-training build on that foundation to develop specialized search and recommendation experts. Our goal is **one shared discovery model that retains the quality improvements achieved by optimizing each task separately**.

We apply **multi-teacher distillation** to transfer both experts’ capabilities into a shared student. The idea is: let each expert specialize, then combine their learning in one model. As each expert improves on its own task, distillation lets the shared model inherit those advances.

## Serving generative discovery at production speed

A live search or recommendation request leaves little time for candidate generation. We optimize the serving path for both quality and latency, starting with the model and then reducing the work needed to generate valid product codes.

### Choosing a base model for the serving budget

We serve our model as a candidate generator, sharing the live request’s latency budget with downstream ranking. For that role, we chose **Liquid AI’s LFM2-2.6B** because it offered the best balance of quality and latency while leaving enough time for the remaining stages. In production, we use the [RIPL](https://www.liquid.ai/blog/low-latency) inference stack to serve the Liquid model.

| **Model** | **Search relevance** **OneDCG@10** | **Search purchases** **Recall@10** | **Recommendation** **Recall@50** | **p95 latency** | 
|---|---|---|---|---|
| **LFM2-2.6B — selected** | 24.9 | 32.3 | 25.3 | **25.5 ms** | 
| Qwen3-1.7B | 24.9 | 32.5 | 26.0 | 46.1 ms | 
| Qwen3-14B | 25.3 | 35.0 | 26.7 | 108.4 ms | 

*For a fair comparison, all models use the same training data mix and are evaluated on the same search and recommendation benchmarks. p95 latency is measured at the server with TensorRT-LLM using a closed-loop benchmark: each client waits for its request to complete before sending the next. In this table, latency measures only the wall-clock time of the server-side generator call, using a beam width of 100 to generate 100 candidates. LFM2-2.6B uses a customized TensorRT-LLM engine. The latency benchmark uses requests sampled from real production traffic. Prompt lengths are 22 tokens at p50 and 620 tokens at p95.*

### Making constrained decoding fast

The model also needs to generate codes that resolve to eligible products. Only some token combinations correspond to products in the catalog, so we constrain generation with an index of valid semantic-ID paths.

Checking those paths can become expensive. We build on [STATIC](https://arxiv.org/abs/2602.22647), which represents the catalog’s prefix tree, or trie, as a sparse index on the GPU. This lets the engine check valid continuations through vectorized operations. A CUDA/C++ plugin inside TurboMind enforces these decoding constraints. In our setting, **constraint overhead fell from over 50 ms to about 1 ms per request**.

Another challenge is **metadata routing for constrained generative retrieval**. Each request can carry its own eligibility filters, such as the buyer’s market, and those filters must constrain which semantic-ID paths the model can generate. We’ll share details about how we approach this in a follow-up piece.

### Predicting a semantic ID sequence in one pass

Our output has a useful structure: we need many candidate products, but each product is represented by just three codewords. Autoregressive (AR) generation predicts those codewords one at a time.

**Multi-token prediction (MTP)** predicts distributions for all three positions in a single model pass, then combines them into valid semantic IDs. This reduces the sequential model work needed to generate candidates. A future post will explain the multi-token prediction design, its serving optimizations, and the tradeoffs between quality, latency, and throughput.

Figure 6 compares AR and MTP at our current production setting. Non-personalized search uses the query; personalized search also includes buyer-profile context in the prompt.

![Comparison of autoregressive generation and multi-token prediction for non-personalized and personalized search, showing lower p95 latency with multi-token prediction.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-07-latency-summary.png?v=1793810340) 

We use the time saved to generate a larger candidate set with MTP, then apply a lightweight ranker to select the best candidates. Together, MTP and the ranker improve quality significantly over AR while retaining lower p95 latency.

## Where we go next

Today, product discovery runs through a **multi-stage funnel**. Retrieval selects candidates from a large catalog, and successive ranking stages narrow and order them for the buyer. Our shared generative discovery model currently serves as a candidate generator within that stack. Each stage shapes what the next can consider: a relevant product missed during retrieval cannot be recovered by a later ranker.

Looking ahead, our goal is to incorporate more of that discovery stack into **one discovery model**. The model would reason about a buyer’s situation, infer shopping intent, generate product candidates through semantic IDs, and rank them. That shared understanding would support search, recommendation, and ads, while respecting the buyer’s privacy choices. The fully shared path below is our longer-term direction.

![Proposed future architecture: one shared model handles intent understanding, candidate generation, and ranking, with fresh buyer feedback driving continuous training.](https://cdn.shopify.com/s/files/1/0779/4361/files/figure-08-discovery-vision.png?v=1793810361) 

To support this direction, we need **a richer, ordered view** of the user's shopping journey**,** bringing search queries, product views, purchases, and store visits into one ordered sequence. Preserving their order and timing would give search and recommendation a shared view of how each buyer’s interests and intent evolve.

We’re **making three bets** that build on this shared context.

The first is **reasoning about intent**. For someone furnishing a small apartment, buying a table changes what might be useful next. Maybe the buyer needs chairs that fit the table *and* their space. We want the model to connect those clues across the journey and carry that understanding through candidate generation and ranking.

The second is **richer multimodal representations**, with a focus on visual information. Product images reveal details that descriptions may leave out: shape, texture, pattern, and style. Connecting these visual signals with text and the products a buyer has explored would help the model understand their preferences and identify other products that match.

The third is **online continuous training**. We want fresh clicks, purchases, and other outcomes to feed ongoing updates to the shared model, so it can adapt as buyer preferences and the catalog change. Shortening the path from interaction to model update would let learning from either search or recommendation improve both experiences.

*This article contains contributions from Aaron Yuen, Darshan Fofadiya, Kyumin Park, Michael Garner, Joshua Antonio Crisologo, Ryan Synk, Jose Sepulveda, and Anthony Maltsev (Liquid AI).*

*Special thanks to Darian Bhathena and Edoardo Mosca from the Liquid AI team.*
