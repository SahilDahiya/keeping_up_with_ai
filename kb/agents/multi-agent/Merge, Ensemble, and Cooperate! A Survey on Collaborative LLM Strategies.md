---
title: Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies
topic: agents
subtopic: multi-agent
secondary_topics:
- models/reasoning
summary: Summarizes collaborative LLM strategies such as merging, ensembling, and
  cooperation for multi-model or multi-agent systems.
source: arize
url: https://arize.com/blog/merge-ensemble-and-cooperate-a-survey-on-collaborative-llm-strategies/
author: Sarah Welsh
published: '2024-12-10'
fetched: '2026-07-11T04:50:58Z'
classifier: codex
taxonomy_rev: 1
words: 933
content_sha256: 30429262053559374d30a6a39ce178e04b8f80609aa060c04787554c352a54f3
---

# Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies

![Survey on Collaborative Strategies Blog B1 Text reads: Community Paper Reading, with a graphic from the merge ensemble cooperate paper](https://arize.com/wp-content/uploads/2024/12/CPR-Survey-on-Collaborative-Strategies-Blog-B1-1021x560.jpg)

              # Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies

LLMs have revolutionized natural language processing, showcasing remarkable versatility and capabilities. But individual LLMs often exhibit distinct strengths and weaknesses, influenced by differences in their training corpora. This diversity poses a challenge: how can we maximize the efficiency and utility of large language models?

We discuss “Merge, Ensemble, and Cooperate: A Survey on Collaborative Strategies in the Era of Large Language Models,” a paper that highlights collaborative strategies to address this challenge. In this week’s episode, we summarize key insights from this paper and discuss practical implications of LLM collaboration strategies across three main approaches: merging, ensemble, and cooperation. We also review some new open source models we’re excited about.

### Watch

### Listen

### Dive In

- [Merge, Ensemble, Cooperate! A Survey on Collaborative Strategies in the Era of Large Language Models](https://arxiv.org/pdf/2407.06089)
- [See more AI research papers](https://arize.com/ai-research-papers/)

## New and Noteworthy AI Models

Before we got into the paper, we kicked things off we covered two new open source models you should know about…

**OLMo 2**

OLMo 2 was released at the end of November 2024 by the Allen Institute for AI. Allen AI (or Ai2) is a non-profit that’s committed to open-source principles, including the release of model weights, training data, code, intermediate checkpoints, and tuned models. OLMo2 achieves performance comparable to Llama 3.1 on English datasets.

We like this model because it promotes transparency and reproducibility in AI model development, and offers a comprehensive view of the model creation process, potentially contributing to broader advancements in the field.

Key techniques used in its development include:

- Stabilizing training runs to avoid spikes in loss ratios.
- Patching models late in the pre-training phase to address gaps in subject matter knowledge.
- Presetting evaluation metrics and using a “Pareto frontier” metric to assess performance relative to training compute.

**QwQ-32B Preview**

This model was also announced in late November and stands for “Qwen with Questions,” a variant of the Qwen model. It’s known for its strong performance in mathematical and analytical reasoning tasks, similar to OpenAI’s 01 model. QwQ-32B employs a chain-of-thought approach to enhance analytical capabilities, but may not be as proficient in nuanced language or language-based reasoning compared to other models.

Noteworthy:

- Exemplifies a growing trend of developing models specialized for analytical and logical reasoning.
- Further demonstrates the effectiveness of chain-of-thought approaches in enhancing analytical abilities.
- Has gained significant popularity within open-source AI communities.

Onto this week’s paper.

## Summary: Merge, Ensemble, Cooperate!

In this paper, researchers categorize collaborative strategies into three primary approaches (which make up the title of the paper). We review each below.

### Merge: Combining Models at the Core

Merging involves integrating the parameters of multiple LLMs into a single model, creating a unified system that leverages their collective capabilities.

**Techniques**

- Uniform Soup: Averages parameter weights across models.
- Greedy Soup: Selectively adds parameters to optimize accuracy.
- DIWA: Ranks models based on validation performance and combines accordingly.

**Applications**

- Task-Specific Optimization (MROS): Aims to find an optimal solution for a specific task by blending and averaging weights.
- Enhanced Multi Task Capabilities (MMTC): Connects models at various layers to tackle multiple tasks without averaging weights.

## Ensemble: Combining Outputs for Optimal Results

Unlike merging, ensemble strategies keep models separate, focusing on combining their outputs to generate a single, high-quality result. Ensemble before inference is widely used in practical applications, especially when paired with specialized smaller language models (SLMs) to optimize costs.

**Methods**

- Before Inference: A router directs input to the most suitable model based on expertise.
- During Inference: Multiple models process inputs step-by-step, combining their outputs during decoding.
- After Inference: Models independently process inputs, and the system selects the best response.

**Trade-offs**

- Inference Time: Increases with the number of models involved.
- Latency: Higher for approaches requiring routing or step-by-step processing.
- Cost: Ensemble after inference incurs the highest computational overhead.

### Cooperation: Harnessing Complementary Strengths

Cooperation encompasses a broad range of techniques where LLMs collaborate to achieve specific objectives, leveraging their unique strengths.

**Strategies**

- Efficient Computation: Reducing the workload of the final LLM by using preliminary models for tasks like prompt pruning or summarization.
- Knowledge Transfer: Having one LLM refine or enhance the outputs of another.
- Compensatory Cooperation: Using multiple models with shared reward mechanisms to work towards a common goal, e.g., retriever models in Retrieval-Augmented Generation (RAG) systems.
- Federated Cooperation: Combining a powerful server-based LLM with smaller, client-side models to balance performance with privacy and security—ideal for resource-constrained environments.

## Final Thoughts on Collaborative LLM Strategies

While these strategies highlight innovative ways to maximize the capabilities of LLMs, real-world applications require balancing performance, cost, and latency. For instance, federated cooperation offers privacy advantages but may require careful tuning to ensure efficiency. Similarly, ensemble strategies can provide robust outputs but come with increased computational demands.

The strategies outlined—merging, ensemble, and cooperation—illustrate the immense potential of LLM collaborations. While the distinctions between these approaches are helpful, many real-world implementations blur the lines, combining elements from each strategy to meet specific needs.

For practitioners and researchers, exploring these collaborative techniques opens new doors for creating advanced NLP applications, from enhanced chatbots to federated systems that respect user privacy. As this field evolves, further innovations in LLM collaboration will undoubtedly push the boundaries of what’s possible.

For a deeper dive into the methods and their mathematical foundations, we recommend reading the full paper.
