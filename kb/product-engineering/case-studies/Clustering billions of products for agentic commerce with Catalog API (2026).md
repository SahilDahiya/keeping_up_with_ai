---
title: Clustering billions of products for agentic commerce with Catalog API (2026)
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- rag-retrieval/embeddings
summary: How Shopify clusters billions of product listings across millions of stores
  into canonical entities via embeddings for its agentic-commerce Catalog API, reconciling
  inconsistent merchant listing structures.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/catalog-clustering
author: Mariya Mansurova
published: '2026-06-17'
fetched: '2026-07-15T00:53:05Z'
classifier: claude
taxonomy_rev: 2
words: 2835
content_sha256: e3faf754bdfd97bc9a486fd3c08a8b88093dd143897de25b09c4de13a4e14a6d
---

# Clustering billions of products for agentic commerce with Catalog API (2026)

Picture two merchants that sell the same protein powder. One creates a single product listing with flavor variants. The other creates a separate listing for every flavor. Both are right. And on their own storefronts, neither structure causes any problems.

But Shopify hosts billions of product listings across millions of stores, and there's no shared schema between them. When an AI shopping agent needs to find the best protein powder across the whole dataset, it has to understand that one merchant's single listing and another merchant's twelve listings describe the same product line… without anyone telling it so.

This is a tale of teaching machines to read product data the way a human shopper would, at scale.

Enter the [Shopify Catalog](https://www.shopify.com/blog/what-is-shopify-catalog): a unified intelligence layer that standardizes product data across the platform and makes it available to developers and AI agents via the [Catalog API](https://shopify.dev/docs/agents/catalog). *(Take a look at all of Catalog's new features coming out of our  Spring 2026 Edition.)*

At the heart of Catalog is product clustering. To understand it, it helps to know how Shopify's data model works. Merchants organize their offerings into products (e.g., "Classic Denim Flare Jean"), each of which can have multiple variants (e.g., size 28 in light wash, size 30 in dark wash). Different merchants may structure the same real-world item very differently. One might create a single product with all size and color variants, another might create separate products per color.

Clustering allows us to group all of these related variants and products under a single Universal Product Identifier (UPI). Regardless of how merchants structure their listings, every version of the same real-world item lives under one roof. When we get this right, merchants' products show up exactly where they should across every agent, which helps them get customers from new agentic distribution channels. If we get it wrong, things break in two distinct ways:

- 
**Precision failures:**different products get incorrectly grouped under the same UPI. Imagine men's and women's versions of the same sneaker getting merged into one cluster. A buyer asks an agent for women's sneakers, adds a pair to cart, and receives the men's version. With lower precision, customers may see the wrong item and can inadvertently purchase it.
- 
**Recall failures:**a variant that belongs in a cluster gets missed. Say a merchant lists a jacket in six colors, but one color variant doesn't get linked to the UPI. A buyer searching for that specific color either can't find it at all, or sees it as a separate duplicate product in the results, which is a confusing experience either way.

![Precision vs recall failure](https://cdn.shopify.com/s/files/1/0779/4361/files/Precision_vs_recall_failure.png?v=1781618416)

These metrics are in constant tension: tighten thresholds to boost precision and you miss valid matches; loosen them to improve recall and you start grouping things that don't belong together.

We chose precision-first: if precision slips, buckets surface the wrong product; if recall slips, the item stays findable, just ungrouped. Our approach is to set a hard precision threshold and then maximize recall subject to that constraint. Surfacing wrong results is worse than incomplete results; buyers can forgive missing a variant, but they won't forgive getting the wrong product.

We measure both using curated ground-truth datasets (human-labeled product samples stratified across categories and merchant types) and LLM-based judges that evaluate precision and recall at scale, calibrated against human annotations. This lets us track quality continuously as the catalog grows and changes daily, and ensure that our experiments are improving overall quality.

This is how we tackled the clustering of billions of products in Shopify Catalog: from building LLM-based intra-store clustering, to scaling our solution, to cross-store clustering—along with the inevitable challenges we hit at each step.

## Intra-store clustering

### Starting smaller

The full product matching problem is enormous: identify identical products across every merchant on Shopify, despite each merchant modeling their catalog differently. Trying to solve that globally from day one would mean comparing everything to everything: billions of products, countless naming conventions, and an impossible candidate space.

So we started with a simpler question: what if many clusters never need to leave the store?

Many Shopify merchants sell products that are unique to them: their own brand, their own designs, their own formulations. For these merchants, the clustering problem isn’t “which products across Shopify are the same?” It’s “which listings inside this shop are actually variants of the same product?”

That partitioning changed the shape of the problem. Instead of one massive global clustering task, we could solve millions of smaller shop-level clustering tasks independently. It gave us a tractable starting point, and more importantly, a place to build intuition about what product identity really means.

### Why LLMs are a natural fit

When a human browses a shop, they usually don’t need a formal ontology to understand what belongs together. They read the catalog listings in context.

They can see that something like “Geometric Design Black Flatwoven Rug” and “Geometric Design Cream Flatwoven Rug” are probably the same rug in different colors. They can see that “Whey Protein—Chocolate” and “Whey Protein—Vanilla” are probably the same nutritional product in different flavors. But they can also see that 'Midnight Blue' and 'Sage Green' from a paint shop are different products, because the color is what the buyer is choosing.

That kind of judgment depends on unstructured context: titles, descriptions, tags, vendor fields, option names, and each merchant’s naming conventions. Shopify’s flexibility is both a strength and a trade‑off: merchants can model products however they like, but the same signal may live in different fields across shops. The data is there; it just needs to be read. So we use LLMs to extract the signals and standardize them into a consistent structure.

LLMs gave us a way to move beyond brittle rules while still staying close to the product data. But we didn’t want to ask the model to “just cluster these products.” That is too vague, and vague prompts produce inconsistent clusters. We needed to teach the model the principle we wanted it to apply.

That principle became the core of the prompt.

## The "core value proposition" framework

The key question we ask the model is: What is the buyer primarily purchasing this product for?

If an attribute does not change the answer, it is a variant. If it does change the answer, it is part of the product identity and should split products into separate UPIs. This became our core value proposition framework.

For protein powder, flavor usually does not change the core value proposition: the buyer is purchasing nutrition, protein content, and fitness goals. Chocolate and vanilla are variants.

For paint, colour often does change the core value proposition: the buyer is purchasing the appearance. Midnight Blue and Sage Green should likely be separate products.

We encoded this reasoning directly into the prompt. First, the model analyzes the shop as a whole: what naming patterns repeat, which terms vary, and which terms appear to define families of products. Then it extracts the brand, using the merchant-provided vendor field as the primary signal. Finally, it identifies the model-defining attributes by applying the core value proposition test.

The prompt includes examples like:

These are teaching examples. The goal is to help the model learn the underlying product-identity principle, then apply it to categories and merchant naming patterns it has never seen before.

### Rules first, LLMs where judgment matters

At the scale of millions of merchants with billions of products, we had to think outside the box. We realized that not every product needs an LLM to figure out where it belongs. Our pipeline starts with the singleton detector—a pre-filtering step that analyzes each merchant's storefront theme code to determine whether their products need clustering at all.

Many Shopify merchants use Liquid templates that define explicit cross-product linking patterns: metafield references connecting related items, tag-based grouping conventions, or collection lookups that tie variants together. The singleton detector parses these theme files and identifies the linking mechanism each shop uses. If a shop's products are already structured as standalone items with no variant grouping in the theme, we mark them as singletons: each product gets its own UPI without hitting the clustering pipeline.

This matters at scale. Only a small percentage of shops actually require LLM-based clustering. The rest can be resolved deterministically, through merchant-defined schemas, tag matching, title similarity, or metafield grouping rules. By layering deterministic rules first and reserving LLMs for the ambiguous cases that genuinely require judgment, we dramatically reduce cost while avoiding unnecessary false merges that would hurt precision.

Okay, back to our LLM-based clustering.

## System architecture: two-stage LLM pipeline

![Intra-store clustering pipeline](https://cdn.shopify.com/s/files/1/0779/4361/files/Intra-store_clustering_pipeline.png?v=1781618476)

### The scaling problem

Most merchants are too big for a single prompt. A few merchants list millions of products; even a mid-sized catalog with a few thousand items is more than an LLM can read in one go and still do good work on. But clustering depends on context. If we feed the model isolated products, it loses the naming patterns and category cues that make sense of a shop’s structure.

So we stepped back and asked: what is the smallest unit of context the model needs to make good judgments? The answer wasn’t “the whole shop,” and it definitely wasn’t “random samples.” The model needs neighborhoods—sets of products that are close enough to reveal how a merchant names and organizes items, but diverse enough to show what varies within a line. That became the job of pre-chunking: assemble coherent neighborhoods before getting the LLM involved. In other words, don’t ask the model to find structure in a haystack; hand it well-formed bundles of hay.

### Pre-chunking: ANN retrieval + average linkage

Our first attempt used a straightforward [linkage-tree clustering](https://en.wikipedia.org/wiki/Complete-linkage_clustering) based on product features. It was fine for small shops, but performance fell off a cliff beyond ~10,000 products. We replaced it with approximate nearest neighbor (ANN) retrieval plus a modified average-linkage approach that scales:

- 
**Build a nearest-neighbor graph:**We embed every product and use HNSW (a fast approximate search via FAISS, Meta's vector search library) to connect each one to its 100 closest neighbors by cosine similarity. Each product connects to its nearest neighbors in embedding space.
- 
**Sparse average linkage:**Starting from singletons, we merge the closest cluster pairs. Distances between clusters use UPGMA (an unweighted average of member-to-member distances). Pairs not connected in the graph get a penalty set just above the threshold, preventing clusters from hopping across the graph without strong evidence. We stop merging when the closest remaining pair exceeds the distance threshold (0.25) or the cluster hits the maximum chunk size (200 products).

The result is a set of chunks (up to 200 products each) that are semantically related. The LLM sees a neighborhood that’s similar enough to expose shop-level conventions, but not so tight that it’s all duplicates.

## From chunks to decisions: the two stages

With coherent chunks in hand, we run a simple, complementary two-step process:

- 
**Stage 1**proposes clusters by extracting brand and model strings for each product in a chunk and assigning UPIs accordingly.
- 
**Stage 2**critiques those proposals, scanning each cluster for mismatches and flagging outliers while defaulting to keeping items together unless there’s clear evidence of a different core value.

### Stage 1: brand + model extraction

Each chunk goes to the LLM with shop context (name, domain, brand) and per-product metadata (titles, URLs, additional fields). The model returns a strict JSON object that assigns every product ID a `brand` and `model` string. Products with the same `brand:model` pair are grouped under one UPI, scoped by shop as `shop_id:brand:model`.

To force the model to read the shop in context, the system prompt asks it to output a patterns array first (what conventions it sees, how names vary, which terms look model-defining) before labeling individual products. This nudges the model to reason about the shop’s language instead of just pattern-matching titles.

### Stage 2: outlier detection

Deciding clusters from scratch is creative work: how many groups exist, what they are, and where each product belongs. The space of possibilities is huge, and a single pass must be globally consistent. But testing a proposed cluster is a critique task, and critique is much easier. Given a cluster of sweatshirt blazers, noticing that three tailored blazers don’t fit only requires local judgment, not a full re-clustering of the shop.

We lean into that asymmetry with a second pass:

- 
**Input:**all products in a proposed cluster (titles and additional metadata)
- 
**Output:**a reason string explaining the analysis, plus an outliers array of product IDs that do not belong
- 
**Default bias:**keep items together unless there’s clear evidence the core value differs

Stage 1 proposes; Stage 2 reviews. Because critique is cheaper and more reliable, the second stage catches mixed product lines, accidental merges (like licensed collaborations pulled into a baseline), or bundles mixed with standalones without re-solving the whole clustering problem.

## The prompt engineering struggle: getting LLMs to be reliable

### The fundamental problem

“Here are 200 products—group them” sounds simple, but free-form prompts fell apart in practice. The model would skip items, merge IDs, invent brands that weren’t in the data, or return malformed JSON. For clustering to work, we need exactly one brand + model for every product ID in a chunk. One missed ID means it never gets a UPI. Hallucinated brands mean products that should sit together are split across groups.

Early on, we tried regex parsers, retry loops for bad JSON, and heuristics to catch missing items. It was brittle, costly, and error-prone.

### The breakthrough: dynamic structured output schemas

The turning point was adopting [the OpenAI Structured Output](https://developers.openai.com/api/docs/guides/structured-outputs) with strict JSON schema enforcement. Instead of hoping the LLM returns well-formed output, we guarantee it by defining a schema that the model must conform to.

The key innovation is that the schema is generated dynamically per chunk. For each product ID in the input, the schema defines a required property in the output products object with brand and model string fields. The LLM literally cannot return a response that skips a product; the schema enforces completeness.

![Dynamically generated schema](https://cdn.shopify.com/s/files/1/0779/4361/files/Schema_dynamic_generation.png?v=1781618528)

This is what made chunking viable. We can split a shop of any size into arbitrary chunks and guarantee every product gets classified, regardless of chunk boundaries. Without this guarantee, the system would need complex reconciliation logic to handle products the LLM forgot to mention.

In a later iteration, we further improved efficiency by increasing cache hit rates and reducing costs through `product_id` remapping. Instead of sending shop-specific IDs like `[product_id: 12345, product_id: 12346, …]`, each prompt remaps them to normalized IDs like `[product_id: 1, product_id: 2, …]`. This makes prompts more reusable across runs while preserving the ability to map results back to the original products.

### Schema as a design tool

We also learned that the schema shapes behavior more reliably than prompt wording alone.

- 
**Ordering controls reasoning:**The schema requires the patterns array before the products object. This forces the LLM to analyze the shop's naming patterns before extracting individual brand/model values. Changing the order of fields in the schema changed the quality of extractions.
- 
**Enum constraints prevent hallucination:**In stage 2 (outlier detection), the outliers array uses an enum constraint listing every valid product ID in the cluster (capped at 500). The LLM can only output IDs that actually exist. No hallucinated product IDs, no typos in IDs, no`"product_123"`when the real ID is`"7891234567890."`
- 
**Schema = hyperparameter:**We found that the output schema has as much impact on cluster quality as the prompt text itself. Cleaning non-ASCII tokens from the output structure improved recall by 8% on our Toloka evaluation dataset. But misaligning the title format between prompt input and schema expectations dropped recall on our GTX dataset. When we removed all structure (free-form output), parsing errors were surprisingly rare (0.25%) but quality didn't improve. Structured output won on both reliability and quality.

## Solving intra-shop clustering

We started with a precision-first stance and a clear definition of product identity: the core value proposition. From there, we built an intra-store pipeline that scales: rules before judgment via the singleton detector, pre-chunking with ANN + sparse average linkage to give the model the right context, and a two-stage LLM flow that proposes clusters and then critiques them.

Dynamic structured outputs turned reliability into an engineering constraint rather than a hope, guaranteeing every product is labeled and making chunking viable at any shop size. Together, these pieces let us cluster billions of products with high precision while steadily pushing recall upward, measured against continuously refreshed ground truth and calibrated LLM judges.

But a buyer doesn’t shop in just one store, and agents won’t either. The next step is cross-store clustering: unifying identical products across merchants under a single, global UPI so agents and developers can search, compare, and recommend with true catalog awareness. This is where intra-store judgments meet a much noisier world. We’ll be back soon to tell that part of the story.

*This article contains contributions from Boris Nazarov, Ilia Kuchumov, and Andrei Danilchenko.*
