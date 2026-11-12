---
title: The best open-source large language model
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-best-open-source-large-language-model
author: Philip Kiely
published: '2024-02-09'
fetched: '2026-11-12T06:13:48Z'
classifier: null
taxonomy_rev: 2
words: 1708
content_sha256: 3770d2b54bd2ffbd860eba7f228a12e42238f60e6188c6b72b1a2753768b0377
---

# The best open-source large language model

AI engineering
# The best open-source large language model

Explore the best open-source large language models for 2025 for any budget, license, and use case.


- Authors
- Date
- February 9, 2024

**Update:** we’ve created a new list of the [best open-source LLMs in 2026](https://www.baseten.co/blog/the-best-open-source-large-language-models-llms)!

Large language models (LLMs) are the definitive category in generative AI. But with tens of thousands of options, it can be hard to feel confident about making the right tradeoffs between output quality, speed, and cost — especially when models specialize in different tasks.

Taking a holistic view across technical specifications, customer conversations, and our own testing, we’ve put together this list of models to guide you in finding the right starting place for building on top of open source text generation models for chat, code completion, retrieval-augmented generation, and more LLM use cases.

Meta's latest LLM family, Llama 3, offers 8B, 70B, and 405B parameter instruct-tuned models with excellent benchmark performance. The midsize model, Llama 3.3 70B Instruct, [compares favorably to top closed-source models including GPT-4o](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md). The models were trained on over 15 trillion tokens, with an emphasis on code and a knowledge cutoff date of December 2023 for Llama 3.3 70B (versus March 2024 for Llama 3.1 8B).

What we love about Llama 3.3 70B Instruct:

- 128k-token context window with excellent retrieval benchmarks for building RAG-type applications.
- Along with Meta's systematic investments in safety, Llama 3 models have been instruct-tuned to reduce false refusal rates.
- Strong code generation and mathematical reasoning capabilities in a general model.
- New, more efficient tokenizer yields up to 15% fewer tokens, meaning you generate fewer tokens per request.

What to watch out for with Llama 3.3 70B Instruct:

- Llama 3.3 70B only supports eight languages, while many models support 2-3x as many.
- Llama 3.3 models have [a custom commercial license](https://github.com/facebookresearch/llama/blob/main/LICENSE) that also applies to any fine-tuned derivatives.

Get started with [Llama 3.3 70B Instruct](https://www.baseten.co/library/llama-3-3-70b-instruct/) or try the smaller but still excellent Llama 3.1 8B Instruct.

DeepSeek-V3 is a 671B-parameter open-source LLM that truly rivals closed-source heavyweights like Sonnet 3.5 and GPT-4o. While other large models like Mistral Large 2 and Cohere Command-R plus are also extremely powerful, DeepSeek-V3 is licensed for commercial use with some restrictions, [including military use](https://github.com/deepseek-ai/DeepSeek-V3/?tab=License-2-ov-file).

What we love about DeepSeek-V3:

- Benchmarks favorably against the best closed-source models and backs up those scores with excellent observed real-world performance.
- Massive 128k-token context window with excellent needle-in-the-haystack retrieval benchmarks across all input sequence lengths.
- Additional multi-token prediction module to enable optimizations like speculative sampling.

What to watch out for with DeepSeek-V3:

- The model is so large that it generally must be [run in FP8](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/) on [H200 GPUs](https://www.baseten.co/blog/evaluating-nvidia-h200-gpus-for-llm-inference/).
- Mixture of Experts architecture can affect batch performance.
- Inference is expensive even with optimizations, for many use cases a less-powerful model like Llama 3.3 70B will suffice at a lower cost.
- DeepSeek-V3 has [a custom commercial license](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL) that also applies to any fine-tuned derivatives.

DeepSeek also released the R1 family of models, based around a technique for fine-tuning existing LLMs to impart Chain of Thought reasoning. While DeepSeek-R1 matches DeepSeek-V3's massive 671B MoE architecture, the research lab also released distilled models based on popular open-source LLMs like Qwen and Llama.

What we love about DeepSeek-R1:

- Exhibits true o1-style CoT reasoning capabilities.
- Tons of options for distilled models in a wide range of sizes for cost-efficient inference.
- Permissive MIT license and open research.

What to watch out for with DeepSeek-R1:

- Midsize distills that are practical for inference are a better match for o1-mini.
- Reasoning models can get stuck in thought loops outside of a narrow temperature range.
- Reasoning models consume a lot of tokens and may not be the right choice for many inference tasks.

Deploy DeekSeek-R1-Distill-Qwen-32B today and experiment with open-source reasoning.

On the opposite end of the spectrum, Phi 3 Mini is an open source instruct-tuned LLM by Microsoft that achieves state of the art performance for models of its size at just 3.8 billion parameters. Phi 3 Mini runs fast on cheap hardware, making it a strong option for low-cost inference.

What we love about Phi 3 Mini:

- Excellent output quality rivals 7B/8B LLMs from just a few months ago.
- 128k-token context window variant allows for unprecedented use cases for models of this size class.
- Permissive MIT license for unrestricted commercial use.

What to watch out for with Phi 3 Mini models:

- While the LLM is outstanding for its class, output quality falls behind larger models, especially for factual recall.
- The 4k-token context window variant consistently scores slightly higher on evals; only use the 128k-token variant when the increased context window is strictly necessary.
- Phi 3 Mini is an English-only model.

Deploy Phi 3 Mini 4k (or the 128k variant) on a T4 GPU.

[Mistral AI](https://www.baseten.co/library/publisher/mistral-ai/) is a foundation model lab founded in France that builds both open-source and proprietary language models. Their open-source models include three sizes of base and instruct-tuned foundation LLM as well as vision models and domain-specific models for math and code.

What we love about Mistral models:

- Large context windows and function calling capabilities on relatively small foundation models allows for low-cost inference.
- Full support for TensorRT-LLM Engine Builder for low-latency deployments.
- Permissive Apache 2.0 license for unrestricted commercial use on some models.

What to watch out for with Mistral models:

- Batching model requests reduces efficiency gains from Mixture of Experts architecture for 8x7B and 8x22B models.
- Newer models like Mistral Large are not licensed for commercial use.
- Light-touch alignment may not be suitable for all use cases.

Choose a model from the Mistral family: 7B, 8x7B, [8x22B](https://www.baseten.co/library/mixtral-8x22b/), or Pixtral!

Qwen Coder is a project by Alibaba to finetune their Qwen 2.5 family of models to specialize in code generation tasks. The Qwen Coder family has three sizes for server-side inference (7B, 14B, and 32B) and three sizes for edge inference (0.5B, 1.5B, 3B) with both Base and Instruct variants.

What we love about Qwen Coder:

- The 32B size matches Claude Sonnet 3.5 on some coding benchmarks.
- Six sizes and two variants (Base and Instruct, and Python) for maximum flexibility.
- Large context window (up to 128K tokens) is essential for working with code as context (code is much more token-dense than natural language).

What to watch out for:

- The most powerful 72B Qwen 2.5 model does not yet have a Coder variant.
- The 0.5B, 1.5B, and 3B edge models, while powerful for their size, are very limited in real-world use.
- The Base variant is intended for finetuning, not for out of the box code completion.

Deploy Qwen Coder 7B, 14B, or 32B optimized with TensorRT-LLM.

The Llama 3.1 family of LLMs offers the most flexibility for fine tuning projects across size (8B, 70B, 405B) and focus (base and code variants). Given Llama 3 models’ strong base performance, any model from the family is a powerful foundation to build on.

What we love about Llama 3.1 for fine tuning:

- Base models in 2 different sizes (8B, 70B, 405B) lets you make tradeoffs between cost and performance.
- New Llama 3.1 license explicitly allows for derivatives and teacher models.
- Llama models have a history as popular choices for fine tuning work, so there’s plenty of research and tooling to build on.

- Heavy-handed alignment in the instruct/chat variants of the models means you may need to start from scratch from the base variant.
- Llama 3.1 models have [a special license](https://github.com/facebookresearch/llama/blob/main/LICENSE) that also applies to fine tuned variants.

Experiment with Llama 3.1 8B Instruct on autoscaling infrastructure.

Yes. The largest open-source models, DeepSeek-V3 and DeepSeek-R1, match GPT-4o and o1-pro, respectively.

Newer open source LLMs like Nemotron Llama 3.1 70B Instruct compare favorably to closed-source options like GPT-3.5, Gemini Pro 1.5, and Claude 3 Sonnet. And with fine-tuning, open source models can match or beat the best closed-source models for specific tasks at much lower costs.

Model evaluation benchmarks measure an LLM’s performance on a fixed set of tasks. These benchmarks are designed to assess the accuracy and quality of the model’s output. While there is no universal standard benchmark, there are a number of popular options including ARC, HellaSwag, and MMLU.

There are some worries about the usefulness of evaluation benchmarks. Generally, evaluation benchmarks could be too narrow to fully capture a model’s performance, and more recently there have been concerns about evaluation sets leaking into models’ training data. These problems have solutions. It’s standard practice to look at a model’s average performance across several benchmarks to account for the limitations of any one benchmark, and researchers check for contamination of their training data before releasing models.

Benchmarks performance is a solid signal when picking an LLM, but isn’t the whole story. There’s no need to switch models every time a new variant comes out with a slight uptick in benchmark score, and the most important thing to do is evaluate model output for your exact use case.

In many cases, you can get better domain-specific performance for LLMs by fine-tuning open-source models or building custom models. Domain-specific models can rival frontier models on specific topics, like medicine or finance, with a fraction of the parameters, leading to more cost-efficient inference. For example, [Writer built custom domain-specific LLMs for medicine and finance](https://www.baseten.co/resources/customers/writer/) and optimized them for fast inference with Baseten.

There’s no one best open source LLM, only the LLM that’s best for you. This selection depends on capabilities, features, price point, and license. New models are released every day, and it can feel overwhelming to keep up. But finding the right model for your use case is possible with a bit of guidance and experimentation.

Deploy the best open source LLM for your use case in just a couple of clicks:

- The best overall open source LLM: [Llama 3.3 70B Instruct](https://www.baseten.co/library/llama-3-3-70b-instruct/)
- The best big LLM: [DeepSeek-V3](https://www.baseten.co/library/deepseek-r1/)
- The best reasoning LLM: DeepSeek-R1-Distill-Qwen-32B
- The best small LLM under 7 billion parameters: Phi 3 Mini
- Another great open-source LLM family: [Mistral](https://www.baseten.co/library/publisher/mistral-ai/)
- The best LLM for code generation: Qwen 3.5 Coder
- The best LLM for fine tuning: [Llama 3.1](https://www.baseten.co/library/family/llama/)
