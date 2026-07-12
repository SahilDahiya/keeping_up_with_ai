---
title: Measuring Embedding Drift
topic: rag-retrieval
subtopic: embeddings
secondary_topics:
- evals-observability/monitoring
summary: Explains embedding drift and how teams can measure changes in embedding distributions
  over time.
source: arize
url: https://arize.com/blog/embedding-drift/
author: Aparna Dhinakaran
published: '2022-12-31'
fetched: '2026-07-11T04:46:17Z'
classifier: codex
taxonomy_rev: 1
words: 460
content_sha256: 79c22e9e98d9cac77339dbb2e6688200c0b78fab758ea202b323190fdab71db9
---

# Measuring Embedding Drift

![umap-abstract-art umap abstract art](https://arize.com/wp-content/uploads/2022/12/umap-abstract-art-1021x560.png)

              # Measuring Embedding Drift

## Approaches for measuring embedding/vector drift for unstructured data, including for computer vision and natural language processing models

**This article is co-authored by  Jason Lopatecki, CEO and Co-Founder of Arize**

Measuring data drift in unstructured data such as images can be a complex task. Traditional measures used to detect drift in structured data, such as the population stability index (PSI), Kullback-Leibler divergence (KL divergence), and Jensen-Shannon divergence (JS divergence), are useful for statistical analysis of structured labels, but they do not apply to unstructured data. The difficulty in measuring data drift in unstructured data arises from the need to comprehend the alterations in relationships within the unstructured data itself. Therefore, a deeper understanding of the data is necessary before one can identify drift.

The objective of detecting unstructured drift is to determine whether two unstructured datasets are dissimilar and, if so, to provide approaches to comprehend the reasons for the differences between them. This article proposes a universal measure and method to identify unstructured drift. After detecting drift, the previous articles cover the root cause workflows that are used to troubleshoot the issue.

Teams often encounter a wide range of issues with image data, such as images that are blurry, spotted, lightened, darkened, rotated, or cropped. However, it’s challenging to identify all possible combinations of issues that could arise, making it impractical to have prior knowledge of every type of issue.

One of the most prevalent data drift issues that teams seek to identify has nothing to do with image quality. It involves identifying objects that were not part of the original training set, such as unique situations, events, people, or objects observed in the production data.

For instance, a training set might include pictures of a single apple but not pictures of multiple apples or other fruit. If the production data contains images of a fruit basket with multiple apples and other fruit, this could cause problems for the model trained only on images of apples by themselves.

Text drift poses diverse challenges for natural language processing (NLP) models, particularly due to the constantly evolving nature of language. Changes in terminology, context, or meaning of words or phrases over time, low-resource languages, and cultural speech gaps can all contribute to drift.

One of the common scenarios for text drift is when a word, category, or language that is absent in the training data appears in production. For instance, a sentiment classification model trained on millions of apparel product reviews in English could experience reduced performance if it encounters reviews in Spanish for the first time in production. Similarly, such a model would struggle to predict the sentiment of reviews of specialized medical devices, for which it has no prior training data.
