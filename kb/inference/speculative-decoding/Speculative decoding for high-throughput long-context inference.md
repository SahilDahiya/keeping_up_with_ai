---
title: Speculative decoding for high-throughput long-context inference
topic: inference
subtopic: speculative-decoding
secondary_topics:
- prompt-engineering/context-engineering
summary: Explains speculative decoding for high-throughput long-context inference.
source: together
url: https://www.together.ai/blog/speculative-decoding-for-high-throughput-long-context-inference
author: Jian Chen; Vashisth Tiwari; Ranajoy Sadhukhan; Yunho Jin; Zhuoming Chen; Jinyuan
  Shi; Ian En-Hsu Yen; Avner May; Beidi Chen
published: '2024-09-05'
fetched: '2026-07-11T04:25:53Z'
classifier: codex
taxonomy_rev: 1
words: 2037
content_sha256: be84dd5747ab23e69de6ff44921ee0b230cef3d87df881c589f2c7b5b58dc81a
triage: keep
skip_reason: null
---

# Speculative decoding for high-throughput long-context inference

## Introduction

The amount of inference being performed with LLMs is [growing](https://foundationcapital.com/why-2024-will-be-the-year-of-inference/) [dramatically](https://www.tweaktown.com/news/91202/heres-how-much-it-costs-openai-to-run-chatgpt-every-day/index.html) across many different use cases, many of which utilize the ever-increasing [context](https://ai.meta.com/blog/meta-llama-3-1/) [lengths](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#sundar-note) supported by these models. Thus, maximizing the inference throughput of these models—including at long context—is becoming an increasingly important problem. Higher throughput enables lower price per token for consumers and lower carbon footprint per token. From a capability perspective, higher throughput at long context unlocks numerous applications such as information extraction from large sets of documents, synthetic data generation for LLM training/fine-tuning, extended user-assistant chats, and agentic workflows (which typically require numerous LLM calls per user request). These applications often involve processing very long input sequences (e.g., long documents or chat histories), requiring models to process thousands of tokens to deliver intelligent outputs. High throughput at long context is particularly technically challenging due to its huge memory requirements for the KV cache. Conventional wisdom (e.g., [Chen et al., 2023](https://arxiv.org/pdf/2302.01318); [Li et al., 2024](https://arxiv.org/pdf/2401.15077); [Liu et al., 2024](https://arxiv.org/pdf/2406.14066)) is that in the high-throughput regime (i.e., large batch sizes), speculative decoding—which leverages underutilized GPU compute during memory-bound decoding—does not make sense, because decoding will be compute-bound and the GPUs will thus be fully utilized. Surprisingly, we show analytically and empirically that for large batch sizes, if the input sequences are long enough, decoding once again becomes memory-bound due to the large size of the KV cache. Building on this key observation, **we demonstrate that speculative decoding can improve throughput and latency by up to 2x on 8 A100s in this large-batch, long-context setting**.

In this blogpost, we first do a deep dive into the forward pass time of a single transformer layer during autoregressive decoding. We show that at large batch sizes, if the context length is large enough, decoding becomes memory-bound, dominated by the time to load the KV cache. After presenting the above analysis, we describe how we can use speculative decoding to increase throughput in the long-context and large batch regime. In particular, we propose two algorithmic innovations:

- **MagicDec**- *we can even use the full target model as the draft model*, as long as it uses a fixed context window. Based on these insights, MagicDec combines ideas from- [TriForce](https://arxiv.org/pdf/2404.11912)and- [StreamingLLM](https://arxiv.org/pdf/2309.17453)—as the draft model, it uses a StreamingLLM draft model (using sliding window attention + attention sink) with staged speculative decoding for further speedups during drafting. Intriguingly, in this regime, we get larger speedups the higher the batch size!
- **Adaptive Sequoia trees**: Leveraging our observation that there is a sequence length threshold above which decoding becomes memory bound—and that it becomes increasingly memory bound for even longer sequence lengths—we propose choosing the amount of speculation as a function of the sequence length (longer sequence length -> more speculated tokens). We leverage the Sequoia algorithm (see our- [paper](https://arxiv.org/pdf/2408.11049),- [blog](https://www.together.ai/blog/sequoia)) to determine the tree structure for the speculated tokens that maximizes the expected number of generated tokens.

We now jump into our deep dive of a single transformer layer.

## Deep dive: When is decoding for a single transformer layer dominated by loading the KV cache?

Here, we analyze when the decoding forward pass time of a single transformer layer is dominated by loading the KV cache. We show that as the context length and batch size increase, most of the time is spent on loading the KV cache.

For this analysis, we split the operations during the forward pass into two types: operations involving model parameters, and operations involving the KV cache. For each type of operation, we compute the number of FLOPS as well as the amount of memory that must be communicated. We note that while the operations involving model parameters become compute-bound as the batch size increases (as their arithmetic intensity equals the batch size $b$), operations involving the KV cache are always memory-bound (as their arithmetic intensity is constant, because each sequence in the batch has its own KV cache). Because the memory taken by the KV cache grows linearly with both the batch size and the average sequence length, whereas the model parameter FLOPS are constant with respect to the sequence length, the forward pass time becomes dominated by the loading of the KV cache as the average sequence length increases.

Here, we will assume that we use a regular MLP, intermediate size=4*d, d=model dim, b=batch size, and n=current prefix length. We assume we are using GQA, where "g" corresponds to the ratio of query heads to key/value heads.

| Model Params | KV cache | |
|---|---|---|
| Memory (bytes) | 2 * (10d 2+ 2d2/ g) | 2 * 2bnd / g |
| Compute (FLOPs) | 2b * (10d 2+ 2d2/g) | 2 * 2bnd |
| Arithmetic intensity | b | g |

Table 1: Memory and compute of a single transformer layer during decoding, split up in terms of operations with model parameters (MLP params, W_{Q,K,V,O}) and with the KV cache. `g` corresponds to the memory reduction factor from GQA (g = num_attention_heads / num_key_value_heads).

From this table, it is easy to see that for large enough sequence length n (and batch size b), the time to load the KV cache will far exceed the operations involving the model parameters, regardless of whether those operations are compute bound or memory-bound.

In Figure 1 we empirically validate that loading the KV cache dominates the forward pass time for a transformer layer, as the sequence length and batch size increase. In particular, we plot the fraction of decode time taken by the operations over the KV cache for a transformer layer with a model dimension of 1024. As you can see, as the sequence length increases, the empirical fraction approaches 1, and it approaches 1 more quickly for larger batch size. This result was quite exciting and surprising to us—counterintuitively, in the long-context regime, a larger batch size results in decoding **being more memory bound**, instead of the other way around. The communities focus on short/medium context may have resulted in this fact being overlooked until now.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1cb5c04b8ed13f82ce_66d9d6d48aedfd7e25483b61_66d9d5636ffb7f56ab21f210_image4.png)

## Enter speculative decoding

Based on the above observations, we propose using speculative decoding to improve LLM throughput and latency during decoding in the large batch + long context regime. Intuitively, because the KV cache operations are memory-bound and dominate the compute time in this regime, there is idle compute that we can utilize with speculative decoding. More specifically, we can show that the verification time ($T_{verify}$) during speculative decoding (when verifying $L$ tokens) will be quite similar to the regular decode time ($T_{decode}$), because the operations involving the KV cache will remain memory bound as $L$ increases (and therefore will take the same amount of time). Although the time for the operations involving the model parameters can increase by a factor of $L$, the total time will not increase very much in the cases where the KV cache loading dominated the decode time. Therefore, as long as our time to speculate these $L$ tokens ($T_{draft}$) is relatively fast, and we have a high enough acceptance rate, we will attain speedups from using speculative decoding (see speedup equation below).

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1cb5c04b8ed13f82c4_66d9d6d48aedfd7e25483b6a_66d8cdc77a38efc4e74f0edf_image5.png)

In Figure 2, we show that for large sequence lengths, $T_{verify}$/$T_{decode}$ approaches 1, which implies that speculative decoding can give meaningful speedups.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1cb5c04b8ed13f82ca_66d9d6d48aedfd7e25483b67_66d9d5a64dfc73db7c44f40f_image5.png)

We will now detail our two algorithmic innovations—MagicDec and adaptive Sequoia trees—related to performing speculative decoding in this high-throughput regime.

### MagicDec

A low draft-to-verify cost ratio is ideal for speculative decoding. In the low-latency regime in which speculative decoding is normally applied (i.e., low batch size), the bottleneck during decoding is the time to load the target model parameters—therefore, using a small draft model is generally the key to attaining a low draft to verify ratio. However, in the high throughput regime we are interested in here, the bottleneck is loading the target model KV cache. This shift in bottlenecks opens up the possibility of using better strategies for drafting. In particular, we can afford to use a larger and more powerful target model as long as its KV cache is kept small. Thus, we propose using self-speculation, where the* target model is used as the draft model*, but with limited context size. More specifically, we use [StreamingLLM](https://arxiv.org/pdf/2309.17453), which uses sliding window attention combined with an "attention sink" (allows attending over the first token) to limit the size of the KV cache. While the draft cost increases with larger batch sizes mainly due to increased computation time, the verification cost rises even more due to the greater KV loading time. This makes the draft-to-target cost ratio decrease with increasing batch size (see Figure 3), **surprisingly making speculative decoding more effective for larger batch sizes**. To further speed up the drafting process, we can use [staged speculative decoding](https://arxiv.org/pdf/2308.04623), similarly to [TriForce](https://arxiv.org/pdf/2404.11912).

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1cb5c04b8ed13f82da_66d9dbfd4dfc73db7c4b5e79_66d9dbed62a22a73e5e9c1f4_image%252520(15).png)

In Table 2, we demonstrate results attaining speedups of up to 2x for LLaMA-2-7B-32K and 1.84x for LLaMA-3.1-8B on 8 A100 GPUs.

| Target | Draft | Prefill | Batch-size | Optimal spec len | Speedup |
|---|---|---|---|---|---|
| Llama2-7b-32k | TinyLlama-1.1B | 8000 | 32 | 3 | 1.29 |
| TinyLlama-1.1B | 8000 | 64 | 3 | 1.57 | |
| TinyLlama-1.1B | 8000 | 128 | 4 | 1.66 | |
| TinyLlama-1.1B | 32000 | 32 | 4 | 1.91 | |
| Llama2-7b-32k | Self-spec | 8000 | 32 | 3 | 1.18 |
| Self-spec | 8000 | 64 | 3 | 1.48 | |
| Self-spec | 8000 | 128 | 4 | 1.63 | |
| Self-spec | 32000 | 32 | 4 | 2.00 | |
| Llama3.1-8b | Self-spec | 32000 | 32 | 3 | 1.22 |
| Self-spec | 32000 | 64 | 3 | 1.38 | |
| Self-spec | 32000 | 128 | 4 | 1.47 | |
| Self-spec | 100000 | 32 | 5 | 1.84 |

Table 2: End-to-end Speculative Decoding Speedups for Various Target-Draft pairs on 8xA100s.

For more details about this work, and additional results, please refer to our [paper](https://arxiv.org/pdf/2408.11049).

### Adaptive Sequoia trees

When we do speculative decoding with a tree of size L, we multiply the total number of flops by L+1 (because the new token generated by the target model, as well as the L speculated tokens, need to be processed by the target model), but keep the amount of memory that needs to be transported constant. Therefore, the flops/memory ratio R is simply multiplied by (L+1). Based on this observation, one simple approach would be to use the equation for R to find the largest value of L for which verification remains memory-bound, for each context-length. However, this approach is a bit coarse, as it ignores the cost of drafting the tree, as well as the marginal gain of increasing the size of the tree.

Therefore, we propose to refine the above approach by explicitly searching for the tree size which maximizes a speedup equation, for each context length. Similar to section 3.3.1 of the[ Sequoia](https://arxiv.org/pdf/2402.12374) paper, we can express speedup as follows (let b=batch size, n=sequence length, L=tree size, D=tree depth, G(L,D) = expected number of generated tokens, and T_model=forward pass time):

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1cb5c04b8ed13f82c7_66d9d6d48aedfd7e25483b64_66d8cd8b9f7c1ae117fb9de5_image3.png)

For $G(L, D)$, we can find the maximal expected number of generated tokens for a Sequoia tree of size $L$ and depth $D$. For $T_{model}(b, n, L)$, we can just measure forward pass times for the target/draft models for many combinations of $b$, $n$, $L$, and perhaps fit these results with a parametric function.

Please be on the lookout for our forthcoming paper, which combines adaptive Sequoia trees with a highly-optimized pipeline parallel FP8 system, designed to maximize throughput.

## Conclusion and Future Work

This work reassesses the trade-off between throughput and latency in long-context scenarios. We demonstrate that speculative decoding can enhance throughput, reduce latency, and maintain accuracy. Our theoretical and empirical analysis reveals that as the sequence length and batch size increase, bottlenecks shift from being compute-bound to memory-bound. This shift enables effective use of speculative decoding for longer sequences, even with large batch sizes, achieving up to 2x speedup for LLaMA-2-7B-32K and 1.84x for LLaMA-3.1-8B on 8 A100 GPUs. These results highlight the importance of integrating speculative decoding into throughput optimization systems as long-context workloads become more prevalent.
