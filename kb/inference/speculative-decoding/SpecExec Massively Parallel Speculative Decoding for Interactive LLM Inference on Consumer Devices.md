---
title: 'SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference
  on Consumer Devices'
topic: inference
subtopic: speculative-decoding
secondary_topics:
- models/reasoning
summary: Introduces SpecExec for massively parallel speculative decoding on consumer
  devices.
source: together
url: https://www.together.ai/blog/specexec
author: Ruslan Svirschevski; Avner May; Zhuoming Chen; Beidi Chen; Zhihao Jia; Max
  Ryabinin
published: '2024-06-18'
fetched: '2026-07-11T04:25:51Z'
classifier: codex
taxonomy_rev: 1
words: 1217
content_sha256: a464b4c594487d8ab58f7508488336a56bee71851588e32a6c4123d2645520b9
triage: keep
skip_reason: null
---

# SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices

We introduce SpecExec, a new speculative decoding method that applies the classical approach of “[speculative execution](https://en.wikipedia.org/wiki/Speculative_execution)” to LLM inference. Using SpecExec, we attain inference speeds for 70B parameter LLMs on consumer GPUs with RAM offloading at 4-6 tokens per second with 4-bit quantization or 2-3 tokens per second with 16-bit weights. These speeds correspond to speedups over autoregressive decoding of up to 10.6x and 18.7x, respectively.

### Background

As large language models (LLMs) like LLaMA and Mistral gain widespread adoption, AI enthusiasts and practitioners are looking for ways to run them faster and on less expensive consumer hardware. Given the limited memory available on consumer GPUs (e.g., 24 GB on RTX 4090), many large models cannot even fit on such devices, thus necessitating offloading model parameters for inference. In offloading, the model is stored in RAM and layers are loaded onto the GPU sequentially during a forward pass. Naturally, this is quite slow, since transferring a 70B parameter model from RAM to GPU in 16-bit precision can take over 5 seconds even with a PCIe gen 4 bus.

To accelerate LLM inference, one can use [speculative decoding](https://arxiv.org/abs/2211.17192). This approach typically involves using a much smaller “draft” model to quickly generate proposed continuation tokens for the input sequence. The main “target” model can then verify these proposed tokens in parallel and choose which (if any) tokens to accept, using a stochastic sampling algorithm. Given that LLM decoding is extremely memory-bound (*especially* when offloading), the target model can verify *many* (several thousand when offloading!) speculated tokens in the same amount of time as it would take to generate a single token. Therefore, as long as the average number of generated tokens per iteration can compensate for the overhead of running the draft model, this approach speeds up inference.

### The SpecExec method

Our method named SpecExec (after [Speculative Execution](https://en.wikipedia.org/wiki/Speculative_execution)) was designed to maximize the speedups from speculative decoding with offloading. Unlike most speculative decoding methods, SpecExec does not use a stochastic verification algorithm to decide which tokens to accept by comparing their respective probabilities from the draft and target models. Instead, SpecExec directly applies speculative execution to LLM inference. It uses a powerful draft model to deterministically construct a large draft tree containing the most likely continuations of the input text (according to the draft model). It then precomputes and caches the target model’s next-token distributions for each node in the tree (representing a partial continuation of the text) using a single forward pass of the target model. Lastly, it sequentially samples from these distributions, starting at the root of the tree, until a token is sampled that falls outside of the tree ("cache miss"); at this point, the process repeats, and a new draft tree is constructed.

The correctness of this algorithm is easy to see: because we are always sampling from the *target* model’s next-token distributions, it is clear that we maintain the same output distribution as regular autoregressive decoding from the target model.

This method works especially well because of the “spikiness” of token probability distributions in modern LLMs. As shown in the figure below (left), the top-1 token in the Llama-2 70B model contains almost 90%+ of its probability mass on average. Furthermore, a strong draft model is often able to predict these very likely tokens from the target model. For example, the top-4 tokens according to Llama-2 7B on average cover almost 90% of the Llama-2 70B probability distribution. This means that even with a small “cache” generated from the most likely draft model tokens, a sample from the target model is very likely to get a “cache hit”.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1c6a1aa7511d13b27d_66722d7a6e02b4df1588ebbe_fig_coverage_no_gptq.png)

We note that this method performs best with a very capable draft model (e.g., Llama2-7B for Llama2-70B target), but this is perfectly suited for the offloading regime. While small draft models are often preferable for on-chip speculative decoding due to their speed, in the offloading setting we can afford much larger draft models: as long as the draft model fits on the GPU, a single forward pass of the draft model will still be much faster than a forward pass from the offloaded target model!

### SpecExec Performance

![Line graph showing SpecExec generates more tokens per step than SpecInfer as draft model output size increases.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1b6a1aa7511d13b278_66722d857be42af4f0ab462c_fig_frontiers_main_mtb.png)

In the figure above, we compare SpecExec’s performance with the popular speculative decoding method named [SpecInfer](https://arxiv.org/abs/2305.09781). Specifically, we compare the average number of generated tokens per iteration for different speculative budget sizes, as we want to understand which method scales better to larger budgets. Both methods perform similarly at low token budgets, but as the budget grows, SpecInfer’s performance plateaus while SpecExec continues improving to over 20 generated tokens per step with budgets beyond 1K. The chart above is based on the MT-Bench dataset and Llama 2-7B/70B chat models (temperature=0.6, top-p=0.9).

The table below compares the end-to-end speedups from SpecExec vs SpecInfer with offloading on an A100 GPU. While SpecInfer shows impressive speedups, SpecExec more than doubles its performance both in speed and in accepted token counts, attaining speedups of 16.4x-18.7x relative to autoregressive decoding with offloading.

*Inference speed with RAM offloading, A100 GPU, Chat / Instruct models, using SpecExec (SX) and SpecInfer (SI) methods*

SpecExec can speed up LLM inference for various types of hardware. In addition to researcher-grade A100, we evaluated SpecExec with consumer GPUS ranging from 2080Ti to 4090. The results below were achieved with a quantized model ([4-bit AWQ Llama-2 70B](https://huggingface.co/TheBloke/Llama-2-70B-AWQ)) that fits in the RAM of most consumer-grade computers. Note that speedup ranges from 4.6x to 10.6x, allowing generation speed in the 3-6 tokens/s range.


*SpecExec inference on consumer GPUs with offloading, chat/instruct models, Llama-2-70B-GPTQ target model, $t=0.6$, OpenAssistant dataset*

### Comparison to Sequoia

We recently released [Sequoia](https://www.together.ai/blog/sequoia), another speculative decoding method similarly aimed at speeding up LLM inference by generating optimized tree structures. Although SpecExec and Sequoia have similarities at a high level, they have different strengths and target different use cases. In particular, Sequoia is more amenable to on-chip inference due to its use of *static* trees, as they are easier to optimize with methods like CUDA Graphs and torch.compile. Furthermore, Sequoia can attain high acceptance rates across both high and low temperatures, whereas SpecExec shines at lower temperatures where the target model distribution is more “spiky”. SpecExec, on the other hand, targets the offloading regime, where the relative overhead of dynamic search is much smaller, and where using large and powerful draft models is practical. In this regime, it can reach faster speeds than Sequoia by *dynamically* constructing trees tailored to each input. As an example, when using a Llama-3 8B draft model for a Llama-3 70B target model (with offloading), Sequoia attains 2.2 tokens per second on average on the MT-Bench dataset, whereas SpecExec attains 2.8 tokens per second — a 27% improvement.

### Conclusion

SpecExec represents a significant advancement in running large language models on consumer hardware. By leveraging the spikiness in token probability distributions and a capable draft model, it achieves impressive inference speedups, thus helping make LLMs more accessible and usable by a broader audience.

At Together, we are obsessed with making LLM inference as efficient as possible (among other things), through a combination of algorithmic and systems research. If you share our passion, and found SpecExec interesting, please contact us, or apply to open roles [here](https://www.together.ai/about#careers)!
