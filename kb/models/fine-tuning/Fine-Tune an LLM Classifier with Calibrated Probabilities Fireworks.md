---
title: Fine-Tune an LLM Classifier with Calibrated Probabilities | Fireworks
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Presents a method for tuning and serving LLMs as calibrated-probability classifiers,
  grounded in a theoretical analysis of how class probabilities emerge during training,
  achievable on a training budget of a few dollars.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/fine-tune-llm-classifier
author: null
published: '2025-12-04'
fetched: '2026-10-23T06:14:00Z'
classifier: claude
taxonomy_rev: 2
words: 1679
content_sha256: 1ba0036d941518e0c4e708086d244e68fcc90c5888ef745d31e3c71f0b470488
---

# Fine-Tune an LLM Classifier with Calibrated Probabilities | Fireworks

Large language models aren’t just for free-form generation. A very common production use case is classification, where the model must choose among a small number of classes - and, crucially, return a probability (confidence) for each class.

In this post, we present a practical approach to tuning and serving LLMs for classification tasks. The method builds on existing model training and inference infrastructure and is grounded in a theoretical analysis of how class probabilities naturally emerge during training. These probabilities can then be leveraged for downstream applications - such as ranking and event prediction - or used directly as confidence estimates.

In many real-world setups, the training can be done with a surprisingly small budget - often as cheap as a couple of dollars in compute.

## Why Use LLMs for Classification?

Large language models are trained to predict the next token - but many real-world applications don’t need free-form text at all. Instead, they boil down to making discrete decisions: picking one label, one intent, or one route among several options.

Think of:

- Safety and moderation: allowed vs disallowed content.
- Routing and triage: deciding whether to send a message to team A, B, or C.
- Intent classification: identifying whether a user needs billing help or wants to cancel a subscription.
- Domain-specific tagging: assigning medical codes, legal categories, or document types.

In each of these, the key output isn’t just a class - it’s the probability of each class. Those probabilities drive thresholding, ranking, and downstream decisions.

What makes this particularly interesting is that LLMs already model probabilities - over tokens. The challenge, then, is how to reinterpret or adapt those token probabilities into well-calibrated class probabilities, without giving up the general-purpose nature of the model.

## Adapting LLMs for Classification

There are multiple ways to turn a generative model into a classifier. They differ in how much they modify the model, the training stack, or the inference interface.

#### Adding a Classification Head

A traditional approach is to replace the LM head with a small classifier - a linear or MLP layer trained on top of a pooled hidden representation. This yields a clean softmax over the label space and integrates naturally with classical deep learning setups. However, it changes the model architecture, which means retraining, new exports, and often incompatibility with standard inference stacks or hosted APIs.

#### Using Tokens as Classes

A more elegant path keeps the architecture completely intact. Each class is mapped to one or more tokens (e.g., “yes” / “no”, “positive” / “negative”, “0” / “1”). A short prompt is crafted to make the model respond with one of these tokens, and the next-token distribution becomes the class probability distribution.

This approach has several advantages:

- **No architectural changes** – works seamlessly with standard fine-tuning and inference APIs.
- **Cost-effective and robust** – especially for small or medium label sets.
- **Interpretable** – token choices often align with human semantics, making debugging easier.

Of course, tokenization details matter: leading spaces, casing, or multi-token classes can slightly distort the mapping. And when multiple tokens represent one class, their probabilities must be aggregated. But in practice, these issues are manageable – and the benefits far outweigh the complexity.

For most production setups, this method offers the cleanest path to deploy classification models built on top of existing LLM infrastructure: no new heads, no custom serving code, just careful prompt design and calibration. Furthermore, this approach remains fully compatible with standard fine-tuning methods such as supervised fine-tuning (SFT) and reinforcement learning (RL), allowing seamless use of existing post-training platforms.

## Label Probabilities and Calibration

Let’s focus on the approach that doesn’t modify the model architecture and instead leverages the vocabulary to represent classes. Once we map each class to a token, the model’s next-token probabilities effectively become class probabilities. But to make those probabilities useful – for ranking, thresholding, or downstream decision logic – they need to be calibrated, meaning they should reflect real-world likelihoods.

#### Calibration

Let’s first formalize the meaning of calibration. For class $c$, define aggregate calibration as:

![calibration calibration](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F1a4d207284c87a1073584dc6c807a211cee1f54e-1850x386.png%3Fauto%3Dformat&w=3840&q=75)

where $p_{i,c}$ is the predicted probability for class $c$ on example $i$, $y_{i,c} \in \{0,1\}$ is the one-hot label, and $N$ is the total number of examples in the evaluation dataset.

- $\mathrm{Calib}(c) \approx 1$: predicted probability mass matches the true frequency (good calibration).
- $\mathrm{Calib}(c) > 1$: model is over-confident for class $c$.
- $\mathrm{Calib}(c) < 1$: model is under-confident.

(You can also monitor standard metrics like ECE or Brier score, but this aggregate ratio is a simple, actionable signal during iteration.)

#### Getting class probabilities

Suppose each class $c$ is represented by a single token $t_c$. When the model is prompted so that its next token should be the class token, it produces a log-probability $\log P(t \mid \text{context})$ for every token $t$ in the vocabulary.

In principle, we care only about the probabilities of the class tokens - lets denote these tokes as $\mathcal{C}$. The challenge is that the softmax normalization spans the entire vocabulary – so probability mass assigned to unrelated tokens can distort the class probabilities. To generate calibrated class probabilities – lets denote them $\hat{p}_c$, we would need to renormalize them:

In practice, however, this renormalization turns out to be unnecessary once the model is fine-tuned for the classification task. As shown in the Appendix, the fine-tuning objective implicitly rebalances the token probabilities such that $\hat{p}_c \approx p_c$. That is, the raw next-token probabilities already behave as calibrated class probabilities, even when the number of classes is tiny relative to the vocabulary size.

#### Practical Tips

- **Prompting matters**: If the model is not fine-tuned, constrain it to single-token answers via careful prompting (e.g., “Answer with ‘yes’ or ‘no’ only”), and use logit bias or decoding constraints to suppress non-label tokens.
- **Fine-tuning helps**: Once fine-tuned, the model naturally focuses its probability mass on the label tokens – no special inference logic is required.
- **Mind tokenization**: Some tokenizers include a leading space (e.g., “ yes” instead of “yes”). Always check which token IDs correspond to your labels before training or evaluation.

## Experimental Validation

To verify these ideas empirically, we trained a classification model and tracked both its accuracy and calibration throughout training.

We used the [AG News](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html) dataset, which consists of short news summaries labeled into one of four categories: World, Sports, Business, and Sci/Tech. For the base model, we fine-tuned Qwen3-4B using LoRA, enabling efficient supervised adaptation without modifying the model’s architecture or inference stack. The total cost of the training on this dataset on the Fireworks platform was around $2.

During training, each batch was evaluated on held-out examples: we computed both label accuracy and aggregate calibration before every weight update. This ensured that calibration was measured on unseen data rather than the current mini-batch.

The results confirm the earlier hypothesis: calibration naturally converges toward 1.0 even when we leave the model’s language-modeling head untouched – i.e., without renormalizing class token probabilities. In other words, a standard fine-tuning setup is sufficient to produce well-calibrated class probabilities directly from the model’s native token distribution.

Fig 1: Calibration and accuracy per training batch. The accuracy is defined as the fraction of samples in the current batch that were classified correctly.

## Code Example

When categories are mapped to individual tokens, you can obtain their probabilities directly using a standard inference API – no architectural changes required.

While most closed-model providers do not expose token-level probabilities, open-source and developer-oriented platforms such as Fireworks make this fully accessible. This allows you to compute calibrated class probabilities exactly as discussed above.

Below is a minimal example showing how to query a model hosted on Fireworks and extract the probability assigned to each class token:

`pythonCopy`
12345678910111213141516171819202122232425262728293031323334353637383940414243444546

## No Fine-Tuning? Use the Embeddings API

If you can’t (or don’t want to) fine-tune a model, you can still get normalized class probabilities from any base model using Fireworks’ [/v1/embeddings](https://docs.fireworks.ai/guides/querying-embeddings-models#using-the-%2Fembeddings-endpoint) endpoint.

Instead of pulling full-vocab logprobs and renormalizing client-side, you:

- Provide the input text and a small list of label token IDs.
- Call the embeddings endpoint with return\_logits=true and normalize=true.

The server computes logits only for those label tokens and applies a softmax over that subset, returning a probability distribution that sums to 1 over your classes. This lets you reuse the “tokens as labels” idea from this post, but without any fine-tuning or custom inference logic - just a single embeddings API call.

## Appendix: Why renormalization is not needed when fine tuning

Let $V$ be the vocabulary, $\mathcal{C}$ be the class tokens. For a specific input $x$ with target label token $c \in \mathcal{C}$, the model outputs $z \in \mathbb{R}^{|V|}$ and probabilities $p = \mathrm{softmax}(z)$.

We analyze the dynamics of the logit gap between the target class $c$ and any non-class token $j \notin \mathcal{C}$ under gradient descent with learning rate $\eta$. The gradients for the cross-entropy loss imply the following updates:

$z_c^{t+1} = z_c^{t} + \eta (1 - p_c^{t}),$

$z_j^{t+1} = z_j^{t} - \eta p_j^{t}.$

We define the gap $\Delta_j^{t} = z_j^{t} - z_c^{t}$ The update rule for this gap is:

$\Delta_j^{t+1} = \Delta_j^{t} - \eta (1 + p_j^{t} - p_c^{t}).$

Note that $1 - p_c^{t} = \sum_{k \neq c} p_k^{t}$ Since $j$ is one of those non-target tokens, we know that $1 - p_c^{t} \ge p_j^{t}$.

Therefore:

$1 + p_j^{t} - p_c^{t} \ge 2 p_j^{t}.$

This implies that at every step where the model assigns non-zero probability to token $j$, the gap $\Delta_j^{t}$ decreases (becomes more negative) by at least $2 \eta p_j^{t}.$

$p_j^{t} = \frac{e^{z_j^{t}}}{\sum_{k} e^{z_k^{t}}} < \frac{e^{z_j^{t}}}{e^{z_c^{t}}} = e^{\Delta_j^{t}}.$

As $\Delta_j \to -\infty$, the probability $p_j$ is forced to $0$. Consequently, the probability mass concentrates entirely on the class tokens $\mathcal{C}$, making $\sum_{c \in \mathcal{C}} p_c \to 1$. Thus, explicit renormalization becomes unnecessary after fine-tuning.

## Getting Started

Ready to start training? Our [Supervised Fine-Tuning](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) and [Reinforcement Fine-Tuning](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models) docs walk you through how to tune base LLMs on your own data, step by step. Prefer video? Check out our [quickstart walkthrough](https://www.loom.com/share/24ba433601de45ba8b63d9fb34c31fd5?t=72) to see the full training flow in action.
