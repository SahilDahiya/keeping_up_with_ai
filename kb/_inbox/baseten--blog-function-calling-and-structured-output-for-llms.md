---
title: Introducing function calling and structured output for open-source and fine-tuned
  LLMs
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/function-calling-and-structured-output-for-llms
author: Bryce Dubayah
published: '2024-09-12'
fetched: '2026-11-12T06:09:06Z'
classifier: null
taxonomy_rev: 2
words: 671
content_sha256: 8e8e2c3274978f983f3d24f80695e9a86de452a507d342b72f5f148f5139ed9a
---

# Introducing function calling and structured output for open-source and fine-tuned LLMs

News
# Introducing function calling and structured output for open-source and fine-tuned LLMs

Add function calling and structured output capabilities to any open-source or fine-tuned large language model supported by TensorRT-LLM automatically.


- Authors
- Date
- September 12, 2024

TLDR

Today, we’re launching a new feature in our TensorRT-LLM Engine Builder to generate structured output during LLM inference. This adds JSON mode, where the model output is guaranteed to match a given JSON schema, as well as function calling, where the LLM selects from provided tools to accomplish a given task. Both of these functionalities operate with no marginal impact on tokens per second and are available for all LLMs deployed using the Engine Builder.

LLMs aren’t just for chat. AI engineers have shifted to building multi-step, multi-model [compound AI workflows](https://www.baseten.co/blog/compound-ai-systems-explained/) that go beyond single model calls to build fully-featured applications and agents.

A fundamental difference between integrating traditional APIs and integrating LLMs is that traditional APIs work with structured data while LLMs work with unstructured data. Whether you’re building a new LLM application or integrating models into an existing platform, the interplay between structured and unstructured data is a major challenge.

LLMs are capable of creating structured data, but they don’t always do so reliably. A single issue – a snippet of text ahead of the data, a misplaced bracket, a string that should be an integer – brings LLM output out of alignment with the application spec, leading to broken systems.

Even if output issues are rare, software that works 99% of the time simply isn’t good enough. Compound that slight chance of failure across each step in the workflow, and LLM-powered systems become fragile, leading to:

- **Limited application capabilities**: granting tool/autonomous action access is infeasible when LLM output is unreliable.
- **Increased complexity**: every LLM call must be manually wrapped in error handling code.
- **Increased latency**: naive error handling strategies include LLM call retries, which increases latency and cost.

Instead, developers need a way to call LLMs with **100% guaranteed output structure** while adding **negligible marginal latency** to API calls.

To enable this, we’ve worked at the model server level to add built-in support for two essential capabilities:

1. **Function calling**: also known as “tool use,” this feature lets you pass a set of defined tools to a LLM as part of the request body. Based on the prompt, the model selects and returns the most appropriate function/tool from the provided options.
2. **Structured output**: an evolution of “JSON mode,” this feature enforces an output schema defined as part of the LLM input. The LLM output is guaranteed to adhere to the provided schema, with full Pydantic support.

Before now, function calling and structured output were available for certain models on shared inference APIs like GPT-4o – in fact, our implementation of both features precisely matches the respective OpenAI API specifications. But adding these features to dedicated deployments of your own LLMs took substantial engineering effort.

Our vision is for developers to be able to take any LLM – open-source, fine-tuned, or entirely custom – and deploy a high-performance, fully-featured model server on production-grade autoscaling infrastructure.

This vision is what guides the [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), which automatically builds high-performance inference servers for open-source models like Llama 3.1 as well as fine-tuned variants. Now, the Engine Builder supports both function calling and structured output for all new model deployments, meaning that you get access to these features with **zero additional engineering effort**.

We built function calling and structured output into our customized version of NVIDIA’s Triton inference server. The server builds a state machine representing the required output structure, then uses logit biasing to enforce that structure during inference. For technical details on how this works, check out [our engineering writeup of the new feature](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/).

Try these new structured output features for yourself:

- First, deploy Llama 3.1 8B with the TensorRT-LLM Engine Builder
- Then try function calling with an accurate LLM math demo
- And get JSON-mode output with in a document parsing demo
