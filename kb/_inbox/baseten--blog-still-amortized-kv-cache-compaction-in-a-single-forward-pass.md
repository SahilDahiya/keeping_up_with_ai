---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/still-amortized-kv-cache-compaction-in-a-single-forward-pass
author: Charles O'Neill
published: '2026-06-10'
fetched: '2026-11-12T06:16:28Z'
classifier: null
taxonomy_rev: 2
words: 237
content_sha256: b192575839c9099f3dad309ae39936ddd04e1d4b14c6b30d08d6f4cbfa1dac64
---

# The platform for inference, training, and execution | Baseten

Research
# Still: Amortized KV Cache Compaction in a Single Forward Pass

You can shrink a language model's KV cache by 200×, in a single forward pass, and it still answers correctly.


- Authors
- Date
- June 10, 2026

**Abstract:** The KV cache is the memory bottleneck of long-horizon language model deployment. Practically, a deployable compactor must be lightweight enough to call during inference, expressive enough to preserve context under constraint, and reusable across a trajectory. Existing compaction methods satisfy only part of this requirement: selection methods are lightweight but subset-bound, while synthesis methods are expressive but rely on per-context optimization. Here we introduce Still, a small per-layer Perceiver trained once against a frozen base model that produces compact keys and values in a single forward pass. On Qwen and Gemma models, Still occupies the favorable side of the speed--quality frontier across compression ratios from 8× to 200× and context lengths from 8k to 128k. On the long-context RULER grid, Still exceeds the strongest baseline by 8--22 points. The same compact cache also supports free-form summarization, preserving most of the full-context gain on HELMET and winning a pairwise LongBench summarization comparison against KV-Distill. Because compaction is a forward pass, Still can be applied iteratively, entering a long-horizon regime unavailable to per-context methods. We show that amortization makes long-context cache compaction tractable, and synthesis makes its compact state useful at extreme compression.

Read the paper here: [https://arxiv.org/abs/2606.07878v1](https://arxiv.org/abs/2606.07878v1)
