---
title: Cross-store product clustering across millions of stores (2026)
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- rag-retrieval/embeddings
- evals-observability/llm-as-judge
summary: 'Shopify describes the architecture behind cross-store product clustering
  in its Catalog API: embedding-based ANN retrieval narrows billions of listings to
  candidate pairs, three LLM-judge pair scorers (L1/L2/L3) of increasing cost label
  matches, and a graph-based UPI builder evaluates proposed cluster merges rather
  than relying on simple connected components, since pairwise match judgments are
  non-transitive.'
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/catalog-clustering-part-ii
author: Ilia Kuchumov
published: '2026-10-20'
fetched: '2026-10-24T06:16:03Z'
classifier: claude
taxonomy_rev: 2
words: 2941
content_sha256: 4faad8a6a8352f27319b69e07257df606be7e5fa9681e2a83370bbfb968ec543
---

# Cross-store product clustering across millions of stores (2026)

[Read Part I](https://shopify.engineering/catalog-clustering) in this series covering how we group related listings within a single store.

Shopify hosts billions of product listings across millions of stores. Merchants have the freedom to organize their products however works best for them, but that flexibility becomes a challenge when we need to work with the entire catalog. Different listings can represent the same product, and we need to recognize those relationships to give buyers, developers, and AI agents a unified view of products and the stores that sell them.

The [Shopify Catalog](https://www.shopify.com/blog/what-is-shopify-catalog) is a unified intelligence layer that standardizes product data across the platform and makes it available to developers and AI agents via the [Catalog API](https://shopify.dev/docs/agents/catalog). At the heart of Catalog is product clustering. Different merchants may structure the same real-world item very differently; one might create a single product with all size and color variants, another might create separate products per color.

Clustering allows us to group all of these related variants and products under a single Universal Product Identifier (listed as UPID in the Catalog API). Regardless of how merchants structure their listings, any version of the same real-world item lives under one roof.

In [Part I](https://shopify.engineering/catalog-clustering) of this series, we described how we group related listings within a single store under a UPI. But the Shopify Catalog needs to answer a harder question: **when different merchants sell the same product or its variants, how do we *know* it’s the same item?** This is cross-store clustering: bringing listings of the same product across merchants together under a single, global UPI.

The [intra-store approach](https://shopify.engineering/catalog-clustering) does not transfer directly. Within one store, we can use the merchant’s catalog as context: how they name products, describe brands, and distinguish models from variants. Across stores, those conventions change. Merchants write different titles and descriptions, photograph the same products differently, and place important details in different fields. A model number that appears in one merchant’s title might be buried in another’s description. Barcodes can help, but they are not consistently available or reliable.

The search space continues to change too. We can no longer divide the problem neatly by merchant: a product’s matching listings may be in any other store. We need to find those matches across billions of listings without comparing every possible pair—and without grouping together products that should remain distinct.

## From product comparisons to global clusters

Rather than asking an LLM to assign globally consistent product labels, we ask a narrower question: **should these two product listings belong to the same UPI?**

A model can compare their titles, images, options, and other metadata without requiring independent model calls to produce exactly the same label for the same product. Starting with pairwise comparisons also avoids needing an existing catalog of reliable global clusters: we can collect matching evidence first, then use it to build those clusters. Pairwise judgments can still be non-transitive: the model might match A with B and B with C, but reject A with C, so that’s why we can't use simple approaches like connected components and need to use more advanced clustering algorithms.

We organize the system around three steps: **find plausible pairs, score each pair, and turn those scores into clusters.**

### Find plausible pairs

Candidate generation is the first step. We represent products with embeddings and use approximate nearest-neighbor search to retrieve nearby listings for each product.

Even finding that shortlist is not a small problem: we are searching across billions of vectors, not a single merchant’s catalog. We have to balance retrieval quality, index size, and search throughput. Approximate search makes the computation practical, but both the approximation and the shortlist limit can leave true matches out of the candidate pool. Those pairs never reach the matching models. A missed match does not remove a product from Catalog (the listing stays searchable under its own identifier), it just isn't grouped with other stores' listings of the same item until a later build finds the connection.

Retrieval narrows the search dramatically. But it still leaves trillions of candidate pairs, and proximity in embedding space is not proof that two listings represent the same product.

### Score each pair

A capable LLM can reason about these comparisons using product information and our definition of product identity. But asking it to evaluate trillions of pairs would be far too expensive.

Instead, we use an [LLM judge](https://shopify.engineering/catalog-clustering) to label sampled comparisons, validate its judgments against human annotations, and use LLM-generated labels to train specialized matching models. Scores from stronger models also provide a training signal for cheaper ones. This lets us use expensive reasoning to produce reusable training data rather than paying for it on every comparison.

We use three pair scorers (L1, L2, and L3) with different capabilities and inference costs. We collect their scores for the cluster builder, and more expensive comparisons are processed through background queues.

### Turn scores into clusters

We represent products as graph nodes and scored relationships as edges. But we cannot simply group everything connected by a path: one incorrect connection could join two otherwise unrelated product groups.

We first partition the graph into **bounded-by-size components** that can be processed independently. These are computational work units, not final product identities. The **UPI builder** then evaluates proposed cluster merges using a trained model to weigh evidence for and against each merge, not just the score of the pair that triggered the proposal.

![Cross-store clustering pipeline](https://cdn.shopify.com/s/files/1/0779/4361/files/Cross-store_clustering_pipeline.png?v=1792445992)

## Each scorer does a different job

Scoring every candidate pair with our richest model would be too expensive. Relying only on the cheapest model would miss distinctions that require closer examination. We therefore divide the work:

- L1 provides fast, feature-based scoring across a large set of candidate pairs
- L2 evaluates both listings' text together
- L3 adds images and richer metadata for selected comparisons

Here’s how each model works and why we use it.

### L1: make the first pass inexpensive

L1 is a GBDT classifier that uses inexpensive pair features, including embedding distances, title and vendor similarity, and price relationships. It evaluates trillions of candidate pairs without running a neural cross-encoder on every pair.

L1 has two jobs: provide fast matching evidence and help decide which candidates deserve more expensive attention. Those are related but different objectives. A pair can be worth sending to a stronger model even when L1’s score provides insufficient evidence for a merge. Keeping that distinction lets us balance the cost of additional model calls against the chance of finding more true matches.

### L2: read the two products together

L2 is a fine-tuned multilingual E5 cross-encoder. It reads both listings jointly, using titles, vendor names, predicted categories, URLs, and shop names. Joint encoding lets the model attend to differences between the two inputs rather than relying only on separately generated embeddings.

That matters when most of the text agrees but one detail changes the identity. Two phone-case listings can share a brand and a product line and still be different products: "for iPhone 15" versus "for iPhone 15 Pro." Joint encoding lets L2 weigh that short compatibility suffix against the long stretch of matching brand and product-line text, instead of letting the overall similarity swamp it.

The limitation is in the inputs. L2 reads many things, but not descriptions. When the distinguishing detail appears only in the description, L2 has nothing to find and the pair looks like a match. That's part of why we send selected pairs to L3, which can look for the difference in the images.

We use joint encoding for this higher-precision decision, while independent embeddings remain central to retrieval.

### L3: bring images into the decision

L3 is a fine-tuned open model reranker that sees product images alongside text and metadata. Images provide evidence that text alone may omit: a different connector, button layout, or case cutout. They also introduce ambiguity—two merchants can photograph the same item from different angles—so the model must interpret them in context, not merely compare pixels.

We ask L3 for a match score rather than a generated explanation. That’s an important serving choice: at serving time, the cluster builder needs a match score, not a written explanation. The more expensive reasoning belongs in the training-data pipeline.

A larger LLM judge supplies labels for sampled examples, and stronger-model scores also provide training signal for cheaper models. We validate the judge against human annotations because its errors can propagate into the models trained on its labels.

These levels provide complementary evidence, but their scores are not directly interchangeable. We set thresholds separately for each scorer and evaluate their combined effect on clustering. Better pair scores only matter if they produce better product groups.

### Building on intra-store clustering

We didn’t build the pipeline in [Part I](https://shopify.engineering/catalog-clustering) just to retire it in Part II. Intra-store groups provide candidate relationships for the cross-store system.

The difference is that we can now look beyond a single store. Listings from other merchants provide additional evidence about which products belong together. The UPI builder considers the intra-store relationships alongside this broader evidence, rather than carrying each group forward unchanged.

That way, we keep the value of the earlier work while allowing the final clusters to benefit from information we didn’t have when looking at one store alone.

## Bounded components

We split the graph into components small enough for the UPI builder to process on a single machine. Different components can then be processed independently and in parallel.

The challenge is deciding where to split. Randomly dividing products between machines would separate many valid matches. Ordinary connected components keep connected products together, but some components become too large to process efficiently. Our goal is to keep as many true matches as possible within the same component, while limiting component size.

### Start with a single-machine algorithm

We use a bounded version of union-find, a data structure that tracks which component each product belongs to:

- Start with every product in its own component.
- Process edges from highest to lowest score.
- If the edge’s endpoints already belong to the same component, skip it. Otherwise, merge their components if the combined result stays within the budget.

We measure that budget using the sum of the products’ degrees (the number of connections attached to them) rather than product count alone. A densely connected group requires more work than a similarly sized group with few connections.

This gives us a straightforward algorithm: stronger connections get considered first, and no merge is allowed to grow a component beyond the budget.

### Parallelize the edge processing

At our scale, processing the entire edge set on one machine becomes a bottleneck. We reduce the number of edges the final bounded pass needs to process.

We divide the edges among parallel workers. Each worker uses ordinary union-find to remove redundant connections within its partition. For example, if three products form a triangle (each connected to the other two) the worker can discard one edge without breaking connectivity. The worker retains these connecting edges, producing a spanning forest instead of forwarding the full edge list.

We then combine the workers’ forests and run the bounded merge algorithm over that reduced set, again considering edges in score order. The forests preserve connectivity, but they don’t guarantee the same bounded components we would get from processing every edge. The size budget still uses connection counts from the original graph, not the reduced forests.

The workers handle the bulk of the edge processing in parallel, while the final pass enforces a shared component-size limit. The resulting components can then be handed to independent UPI-builder workers.

![Bounded components](https://cdn.shopify.com/s/files/1/0779/4361/files/Bounded_compontents.png?v=1792446057)

## UPI builder

Splitting the graph into bounded components turns one catalog-wide problem into many smaller, independent problems. **Each component is small enough to process on a single machine**, while different components can be processed in parallel. This lets the UPI builder evaluate cluster-level relationships without coordinating individual merge decisions across machines.

Within each component, **we use hierarchical agglomerative clustering (HAC) with a learned merge rule.** We progressively merge smaller clusters into larger ones, using a GBDT model to score each proposed merge. The goal is to group as many matching listings as possible under the same UPI, without combining distinct products.

We set a **very high precision target** for these merges. An incorrect merge can mix two entire product groups; rejecting a valid merge leaves those groups separate. We therefore tune the model’s acceptance threshold for precision first, then maximize recall within that constraint.

### Use the information already in the edges

By this point, our edges carry both a **type** and a **score**. Those scores summarize substantial product information: depending on the scorer, they reflect comparisons of titles, brands, categories, images, and other metadata. Edge types distinguish the source of the evidence and its confidence level.

The UPI builder’s job is to use that information efficiently. Rather than reading the product data again for every proposed merge, it combines the existing predictions into a cluster-level decision: **does the evidence support joining these two groups?**

We use a GBDT model with features describing both clusters and their potential union:

- **Support:** How many edges connect the two clusters, and how dense are those connections relative to their sizes?
- **Coverage:** Do connections involve many products on both sides, or are they concentrated around just one or two products?
- **Cohesion:** How strongly connected are the products within each cluster, compared with their connections outside it?
- **Contradiction:** How much low-scoring L2 or L3 evidence argues against combining the groups?

We compute these features across different types of edge evidence, keeping stronger matches and negative judgments distinguishable. This gives the merge model a compact view of the relationships between the groups, not just the score of the pair that triggered the proposal.

![A strong pair is evidence](https://cdn.shopify.com/s/files/1/0779/4361/files/A_strong_pair_is_evidence.png?v=1792446088)

### Collect data from the model’s decisions

Building the training set took several iterations. A new model changes which merges are accepted, which changes the intermediate clusters, and therefore the decisions it encounters later. Training data collected from the previous policy does not fully cover the situations the new policy creates.

We repeated a cycle of running the builder, sampling its merge proposals, labeling them with the LLM judge, and retraining. We needed examples of both acceptable and unacceptable merges, rather than simply teaching the model to reproduce the previous builder’s decisions. Each iteration expanded the training set to cover more of the situations the learned policy encountered.

Changes to the graph also affect the model’s inputs. As new scores arrive or products leave the catalog, cluster densities and connections change, so we need to refresh graph-derived training features as well as collect new labels.

We now collect fresh merge proposals and retrain regularly, keeping the training data aligned with both the builder’s changing behavior and the evolving catalog.

## Keeping up with a changing catalog

The Catalog does not stand still. New products arrive, merchants update titles and images, and previously unrelated listings become candidates for matching. We therefore need to keep evaluating new candidate pairs and refreshing existing scores when the underlying product information changes.

### Keep inference running

L1 runs on CPUs and is fast enough to score the full candidate set. As new and changed products produce candidate pairs, L1 assigns each pair an initial match score.

L2 and L3 require GPU inference, so we cannot apply them to every candidate at the same scale. Instead, we maintain queues of comparisons waiting for these models. New work joins those queues alongside existing candidates that have not yet received the more expensive scoring.

This lets us keep our GPU fleet supplied with a steady stream of work. Rather than trying to finish all expensive comparisons in each daily clustering run, we make progress continuously with the compute available.

### Put useful comparisons first

Choosing the *right* work to keep our GPUs occupied is the important part.

We prioritize candidates using earlier model scores, purchase and search signals, and the current graph structure. Model scores help identify promising matches or comparisons worth a closer look. Demand signals help prioritize products that buyers interact with. Graph context helps prioritize comparisons whose results could influence the UPI builder’s merge decisions.

The queues therefore serve two purposes: keeping up with changes to the catalog and improving matching coverage for products already in it. New comparisons are selected by priority, so they can be processed ahead of older work.

### Reuse results across cluster builds

We cache completed scores, tracking the model and relevant product features used to produce them. When the model and relevant product features are unchanged, we reuse the cached score.

Each daily UPI build combines current L1 results with the L2 and L3 scores available for that run. It doesn’t wait for the inference queues to empty. Meanwhile, background inference continues processing new, changed, and previously unscored pairs.

This lets us update clusters daily while background GPU inference continues to add and refresh the scores used by the UPI builder.

## The result

We built a system that lets merchants keep their individual product listings while helping AI agents recognize which listings belong together and treat them as a group, with high precision. It keeps those groups up to date as products are added or changed, and is designed to do so quickly and reliably at Shopify’s scale.

The key was to make expensive judgments reusable: as training data for faster models ,and as cached scores for later builds. That lets us keep improving the evidence behind product identities while focusing expensive inference on new, changed, or previously unscored comparisons.

*With thanks for contributions from Mariya Mansurova, Boris Nazarov, Oleg Akimov.*
