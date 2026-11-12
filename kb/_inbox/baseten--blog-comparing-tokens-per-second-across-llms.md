---
title: Comparing tokens per second across LLMs
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/comparing-tokens-per-second-across-llms
author: Philip Kiely
published: '2024-05-09'
fetched: '2026-11-12T06:12:18Z'
classifier: null
taxonomy_rev: 2
words: 921
content_sha256: f9f9b9e59b163e56ab41ada1277f49d4f68fa44978259bf154a37239126ee069
---

# Comparing tokens per second across LLMs

Model performance
# Comparing tokens per second across LLMs

To accurately compare tokens per second between different large language models, we need to adjust for tokenizer efficiency.


- Authors
- Date
- May 9, 2024

TLDR

LLMs like Llama 3 and Mixtral 8x22B process input and generate output in tokens, or chunks of text ranging from a single character to a full word. To figure out how fast an LLM runs during inference, we measure the number of tokens it can consume and generate as tokens per second (TPS). As different models use different tokenizers, we need to be careful when comparing TPS metrics across models, especially Llama 2 versus Llama 3.

Tokens per second (TPS) is one of the most important metrics we track for LLM performance. When comparing performance across two different LLMs, you need to adjust TPS based on the models’ tokenizers. The tokenizer is a small model that takes human-readable input text and turns it into the tokens that an LLM uses for inference. Different LLMs have different tokenizers of varying levels of efficiency:

- **Llama 3** models use a variant of [tiktoken](https://github.com/openai/tiktoken), a tokenizer developed by OpenAI and used by GPT-4.
- **Llama 2** models use a custom-made [LlamaTokenizer](https://huggingface.co/docs/transformers/en/model_doc/llama2#transformers.LlamaTokenizer) developed by Meta based on [sentencepiece](https://github.com/google/sentencepiece).
- **Mistral 7B** and **Mixtral 8x7B** use Mistral’s first-generation tokenizer, while **Mixtral 8x22B** uses [Mistral’s third-generation tokenizer](https://docs.mistral.ai/guides/tokenization/).
- **GPT-4** uses [tiktoken](https://github.com/openai/tiktoken), an open source tokenizer developed by OpenAI.

Tokenizers vary widely in efficiency. In the [Llama 3 announcement](https://ai.meta.com/blog/meta-llama-3/), Meta claimed that the Llama 3 tokenizer is up to 15% more efficient than the Llama 2 tokenizer. If that’s the case, generating 85 tokens with Llama 3 yields the same human-readable output as generating 100 tokens with Llama 2.

But making a true comparison across LLMs is more complicated than that. Depending on the language, style, and structure of the model input and output, different tokenizers can be more or less efficient. For example, the Llama 3 tokenizer is substantially better than the Llama 2 tokenizer for code, but only slightly better for prose.

When evaluating multiple LLMs, or upgrading to the latest generation (e.g. switching from Llama 2 to Llama 3), you need to adjust your TPS comparisons to reflect real-world use to accurately calculate changes in latency, throughput, and cost.

As a simple demonstration of tokenizer variance across different inputs, I ran three different text samples through various tokenizers:

1. **Novel**: the first paragraph of *Moby Dick* (1,107 characters)
2. **Poetry**: Shakespeare’s *Sonnet 18* (620 characters)
3. **Code**: The sample inference code for Llama 3 from its model card on Hugging Face (842 characters).

Token counts were generated using [this fantastic tokenizer playground by](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) [Joshua Lochner (Xenova)](https://huggingface.co/spaces/Xenova/the-tokenizer-playground), which runs in-browser with `transformers.js`.

Here's how many tokens each model takes to encode each text sample:

| Sample | Llama 3 | Llama 2 | Mistral v3 | GPT-4 | 
|---|---|---|---|---|
| Novel (1107 chars) | 238 | 266 | 253 | 238 | 
| Poetry (620 chars) | 148 | 187 | 181 | 148 | 
| Code (842 chars) | 210 | 318 | 307 | 214 | 

Versus Llama 3’s efficient tokenizer, other open source LLMs like Llama 2 and Mistral need substantially more tokens to encode the same text. GPT-4 has nearly identical performance, as it uses a very similar tiktoken-based tokenizer.

Here's the relative increase in tokens needed by each model versus Llama 3:

| Sample | Llama 3 | Llama 2 | Mistral v3 | GPT-4 | 
|---|---|---|---|---|
| Novel (1107 chars) | Baseline | 12% more tokens | 6% more tokens | 0% more tokens | 
| Poetry (620 chars) | Baseline | 26% more tokens | 22% more tokens | 0% more tokens | 
| Code (842 chars) | Baseline | 51% more tokens | 46% more tokens | 1% more tokens | 

Llama 3’s tokenizer is more efficient in general, but shines brightest when tokenizing code samples. So if you’re building a code completion app, you should adjust TPS metrics differently than if you’re building a novel summarizing tool.

End users don’t explicitly care about tokens per second. They care that the software they’re using is fast and responsive. When switching between open source LLMs, such as upgrading from Llama 2 to Llama 3, ensure your TPS metrics for latency and total throughput are accurate by:

1. Curating a representative sample of inputs and outputs for your use case, whether it’s code autocomplete in Python or summarizing YouTube videos in Korean.
2. Running your sample texts through the tokenizer for the old and new models. Calculate the relative efficiency of each tokenizer.
3. Adjusting your TPS calculation to account for the relative value of each token generated.

As an example, let’s say that I was switching from Llama 2 to Llama 3. My app, running on Llama 2, required 100 tokens per second for a great user experience. When I deploy Llama 3 with the same configuration and batch size, I notice I’m only getting 90 tokens per second. But after testing the tokenizer, I find that it’s 15% more efficient on sample input and output from my app. In this case, the 90 tokens per second is actually slightly faster than what I had before with Llama 2 in real-world use.

By adjusting TPS calculations for variance in tokenizer, you can set accurate performance targets when switching between open source models. Then, you can hit these performance targets with hardware like [H100 MIG GPUs](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/) and software optimizations like [TensorRT-LLM](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/) and [FP8 precision](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/).
