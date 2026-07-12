---
title: Fine-tuning LLMs as classifiers
topic: models
subtopic: fine-tuning
secondary_topics:
- prompt-engineering/structured-output
summary: Shows how to adapt generative LLMs for classification tasks while preserving
  probability outputs and efficient serving.
source: fireworks
url: https://fireworks.ai/blog/Finetuning-LLMs-as-Classifiers
author: null
published: '2025-12-04'
fetched: '2026-07-11T04:16:37Z'
classifier: codex
taxonomy_rev: 1
words: 1510
content_sha256: 459c888561fb5348a2edbc384f6933f82b743c6f1d41119be4f00526e376057d
triage: keep
skip_reason: null
---

# Fine-tuning LLMs as classifiers

Large language models aren’t just for free-form generation. A very common production use case is classification, where the model must choose among a small number of classes - and, crucially, return a probability (confidence) for each class.

In this post, we present a practical approach to tuning and serving LLMs for classification tasks. The method builds on existing model training and inference infrastructure and is grounded in a theoretical analysis of how class probabilities naturally emerge during training. These probabilities can then be leveraged for downstream applications - such as ranking and event prediction - or used directly as confidence estimates.

In many real-world setups, the training can be done with a surprisingly small budget - often as cheap as a couple of dollars in compute.

Large language models are trained to predict the next token - but many real-world applications don’t need free-form text at all. Instead, they boil down to making discrete decisions: picking one label, one intent, or one route among several options.

Think of:

- •Safety and moderation: allowed vs disallowed content.
- •Routing and triage: deciding whether to send a message to team A, B, or C.
- •Intent classification: identifying whether a user needs billing help or wants to cancel a subscription.
- •Domain-specific tagging: assigning medical codes, legal categories, or document types.

In each of these, the key output isn’t just a class - it’s the probability of each class. Those probabilities drive thresholding, ranking, and downstream decisions.

What makes this particularly interesting is that LLMs already model probabilities - over tokens. The challenge, then, is how to reinterpret or adapt those token probabilities into well-calibrated class probabilities, without giving up the general-purpose nature of the model.

There are multiple ways to turn a generative model into a classifier. They differ in how much they modify the model, the training stack, or the inference interface.

A traditional approach is to replace the LM head with a small classifier - a linear or MLP layer trained on top of a pooled hidden representation. This yields a clean softmax over the label space and integrates naturally with classical deep learning setups. However, it changes the model architecture, which means retraining, new exports, and often incompatibility with standard inference stacks or hosted APIs.

A more elegant path keeps the architecture completely intact. Each class is mapped to one or more tokens (e.g., "yes" / "no", "positive" / "negative", "0" / "1"). A short prompt is crafted to make the model respond with one of these tokens, and the next-token distribution becomes the class probability distribution.

This approach has several advantages:

- •**No architectural changes**– works seamlessly with standard fine-tuning and inference APIs.
- •**Cost-effective and robust**– especially for small or medium label sets.
- •**Interpretable**– token choices often align with human semantics, making debugging easier.

Of course, tokenization details matter: leading spaces, casing, or multi-token classes can slightly distort the mapping. And when multiple tokens represent one class, their probabilities must be aggregated. But in practice, these issues are manageable – and the benefits far outweigh the complexity.

For most production setups, this method offers the cleanest path to deploy classification models built on top of existing LLM infrastructure: no new heads, no custom serving code, just careful prompt design and calibration. Furthermore, this approach remains fully compatible with standard fine-tuning methods such as supervised fine-tuning (SFT) and reinforcement learning (RL), allowing seamless use of existing post-training platforms.

Let's focus on the approach that doesn’t modify the model architecture and instead leverages the vocabulary to represent classes. Once we map each class to a token, the model’s next-token probabilities effectively become class probabilities. But to make those probabilities useful – for ranking, thresholding, or downstream decision logic – they need to be calibrated, meaning they should reflect real-world likelihoods.

Let's first formalize the meaning of calibration. For class , define aggregate calibration as:

where is the predicted probability for class on example , is the one-hot label, and is the total number of examples in the evaluation dataset.

- •: predicted probability mass matches the true frequency (good calibration).
- •: model is over-confident for class .
- •: model is under-confident.

(You can also monitor standard metrics like ECE or Brier score, but this aggregate ratio is a simple, actionable signal during iteration.)

Suppose each class is represented by a single token . When the model is prompted so that its next token should be the class token, it produces a log-probability for every token in the vocabulary.

In principle, we care only about the probabilities of the class tokens - lets denote these tokes as . The challenge is that the softmax normalization spans the entire vocabulary – so probability mass assigned to unrelated tokens can distort the class probabilities. To generate calibrated class probabilities – lets denote them , we would need to renormalize them:


In practice, however, this renormalization turns out to be unnecessary once the model is fine-tuned for the classification task. As shown in the Appendix, the fine-tuning objective implicitly rebalances the token probabilities such that . That is, the raw next-token probabilities already behave as calibrated class probabilities, even when the number of classes is tiny relative to the vocabulary size.

- •**Prompting matters**: If the model is not fine-tuned, constrain it to single-token answers via careful prompting (e.g., “Answer with ‘yes’ or ‘no’ only”), and use logit bias or decoding constraints to suppress non-label tokens.
- •**Fine-tuning helps**: Once fine-tuned, the model naturally focuses its probability mass on the label tokens – no special inference logic is required.
- •**Mind tokenization**: Some tokenizers include a leading space (e.g., " yes" instead of "yes"). Always check which token IDs correspond to your labels before training or evaluation.

To verify these ideas empirically, we trained a classification model and tracked both its accuracy and calibration throughout training.

We used the [AG News](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html) dataset, which consists of short news summaries labeled into one of four categories: World, Sports, Business, and Sci/Tech. For the base model, we fine-tuned Qwen3-4B using LoRA, enabling efficient supervised adaptation without modifying the model’s architecture or inference stack. The total cost of the training on this dataset on the Fireworks platform was around $2.

During training, each batch was evaluated on held-out examples: we computed both label accuracy and aggregate calibration before every weight update. This ensured that calibration was measured on unseen data rather than the current mini-batch.

The results confirm the earlier hypothesis: calibration naturally converges toward 1.0 even when we leave the model’s language-modeling head untouched – i.e., without renormalizing class token probabilities. In other words, a standard fine-tuning setup is sufficient to produce well-calibrated class probabilities directly from the model’s native token distribution.

Fig 1: Calibration and accuracy per training batch. The accuracy is defined as the fraction of samples in the current batch that were classified correctly.

When categories are mapped to individual tokens, you can obtain their probabilities directly using a standard inference API – no architectural changes required.

While most closed-model providers do not expose token-level probabilities, open-source and developer-oriented platforms such as Fireworks AI make this fully accessible. This allows you to compute calibrated class probabilities exactly as discussed above.

Below is a minimal example showing how to query a model hosted on Fireworks AI and extract the probability assigned to each class token:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546

If you can’t (or don’t want to) fine-tune a model, you can still get normalized class probabilities from any base model using Fireworks’ [/v1/embeddings](https://docs.fireworks.ai/guides/querying-embeddings-models#using-the-%2Fembeddings-endpoint) endpoint.

Instead of pulling full-vocab logprobs and renormalizing client-side, you:

- •Provide the input text and a small list of label token IDs.
- •Call the embeddings endpoint with return_logits=true and normalize=true.

The server computes logits only for those label tokens and applies a softmax over that subset, returning a probability distribution that sums to 1 over your classes. This lets you reuse the “tokens as labels” idea from this post, but without any fine-tuning or custom inference logic - just a single embeddings API call.

Let be the vocabulary, be the class tokens. For a specific input with target label token , the model outputs and probabilities .

We analyze the dynamics of the logit gap between the target class and any non-class token under gradient descent with learning rate . The gradients for the cross-entropy loss imply the following updates:





We define the gap The update rule for this gap is:


Note that Since is one of those non-target tokens, we know that .

Therefore:


This implies that at every step where the model assigns non-zero probability to token , the gap decreases (becomes more negative) by at least


As , the probability is forced to . Consequently, the probability mass concentrates entirely on the class tokens , making . Thus, explicit renormalization becomes unnecessary after fine-tuning.

Ready to start training? Our [Supervised Fine-Tuning](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) and [Reinforcement Fine-Tuning](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models) docs walk you through how to tune base LLMs on your own data, step by step. Prefer video? Check out our [quickstart walkthrough](https://www.loom.com/share/24ba433601de45ba8b63d9fb34c31fd5?t=72) to see the full training flow in action.
