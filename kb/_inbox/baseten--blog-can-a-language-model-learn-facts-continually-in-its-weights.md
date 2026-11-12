---
title: Can a Language Model Learn Facts Continually in Its Weights?
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/can-a-language-model-learn-facts-continually-in-its-weights
author: Charles O'Neill
published: '2026-07-14'
fetched: '2026-11-12T06:16:00Z'
classifier: null
taxonomy_rev: 2
words: 326
content_sha256: 0a32148a4c8f85845c78f9d0925ac0bca8bab659fb4785cd685cd34838f7fc58
---

# Can a Language Model Learn Facts Continually in Its Weights?

Research
# Can a Language Model Learn Facts Continually in Its Weights?

Continual learning asks the weights to acquire facts after training and retain them through further writes.


- Authors
- Date
- July 14, 2026

**Abstract:** Continual learning promises a language model that keeps acquiring knowledge after training, with each new fact written into its weights. Whether weight writes can support accumulation remains undecided. We follow invented facts written into Qwen3 models from creation through sequences of twenty to one hundred later writes, using held-out questions of five types, with the original model given the fact in its prompt as the reference. 

Across these experiments, the breadth of the training data determines the kind of knowledge created. Bare-statement training produces recitation, while diverse restatements reduce the recitation-to-use gap from 27.4 to 5.4 points without showing the model a conclusion. This difference carries into later writes: after twenty sequential writes, bare-statement facts retain 1% accuracy while facts written from broad study data retain 46%. We also find that facts can be behaviourally forgotten without being erased. Forgotten facts keep most of the log-probability added by their write, and under bare-statement training 70% of wrong answers about them contain the most recently written fact. The same writes barely degrade the model’s use of facts in context, and a forgotten study fact supplied in the prompt recovers to 77–80% on its questions. 

These results describe knowledge that is stored but question-keyed: later writes redirect the questions that reached it. Damage to unrelated abilities tracks KL divergence from the original model, and the later writes cause interference regardless of how the earlier fact was stored. Broad data can create usable knowledge, and a frozen reference can preserve capability, but no intervention we tested, including those built on accurate local measurements of each write, keeps earlier facts reachable. When facts must be composed or survive later writes, the reliable channel is context rather than the weights.

Read the paper [here](https://arxiv.org/abs/2607.11020).
