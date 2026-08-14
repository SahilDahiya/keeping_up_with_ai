---
title: Inference engineering for DeepSeek V4 Pro 0813
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/inference-engineering-for-deepseek-v4-pro-0813/
author: Model Performance Team
published: '2026-08-14'
fetched: '2026-08-14T06:27:59Z'
classifier: null
taxonomy_rev: 2
words: 657
content_sha256: 39b2dff9a1cdd3239a05ca02d6cb5106cb499947436554870f136028ac2c6a1a
---

# Inference engineering for DeepSeek V4 Pro 0813

![Inference engineering for DeepSeek V4 Pro 0813](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786659070-deepseek-x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

DeepSeek V4 Pro 0813 weights were open-sourced today. This 1.7T-parameter frontier open model is MIT-licensed, meaning that every enterprise has the opportunity to run and fine-tune the model without restrictions, and is [available today as a Model API on Baseten](https://www.baseten.co/library/deepseek-v4-pro-0813/) with zero data retention by default.

![DeepSeek AI published first-party quality benchmarks for DeepSeek V4 Pro 0813](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1786659402-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) DeepSeek AI published first-party quality benchmarks for DeepSeek V4 Pro 0813

Benchmarks were run using DeepSeek’s new coding harness, which was open-sourced alongside the new models as a developer preview. Alex Ker’s [breakdown of the new harness](https://x.com/thealexker/status/2087944116172693910) reveals its plugin-first approach to operate at a higher level of abstraction than a standard coding loop.

DeepSeek V4 Pro 0813 is a new open frontier model that sits alongside GLM-5.2 on quality on [Artificial Analysis’ all-around intelligence index](https://artificialanalysis.ai/#intelligence), though at a lower cost per task.

This post summarizes the inference engineering work we did on DeepSeek V4 Pro 0813 to create a production-ready day zero API for the model.

## From preview to pro

This release is an update of the DeepSeek V4 Pro Preview model, released in April, with additional post-training for code generation and agentic behavior. While the new model performs substantially better on both benchmarks and real-world use, those gains are achieved on the same base architecture. This is increasingly common – more and more gains in model quality are coming from post-training.

The advantage of serving a new model with a familiar base architecture is that the inference setup can be heavily informed by work on the earlier model.

For DeepSeek, we run the native MXFP4 weights on our proprietary inference engine within the Baseten Inference Stack using many of the features we originally built to support the preview model. However, it’s not quite as simple as swapping out the weights and shipping.

First off, traffic patterns have evolved materially since April. The input and output sequence lengths are longer, cache hit rates are higher, and topics are more focused in today’s agentic coding landscape. This in turn affects the optimal configs across the inference stack, from parallelism to KV cache allocation to prefill-decode worker ratio. We configured every knob of the inference stack for an efficient balance of low latency and high throughput.

Additionally, DeepSeek V4 Pro 0813 ships with some changes to the frontend and chat template to match the last four months of evolution in harness expectations and API specs. The [documentation in the Hugging Face repository](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813/blob/main/encoding/README.md) explains this change, which replaces a traditional Jinja-format chat template with a folder of scripts demonstrating input encoding and output parsing. Adherence to this spec is essential to high quality across tool calls and other structured outputs.

Finally, the new model has slightly more parameters than the preview model as it ships with a DSpark speculator. While this doesn’t change the underlying architecture, it gives us the opportunity to support speculative decoding for higher TPS. While the native speculator is good for the most common use cases for the model – coding and agentic tasks – we would want to train a new speculator for most dedicated deployments on a narrower dataset that is representative of expected usage for that specific deployment.

## Production inference for DeepSeek V4 Pro 0813

DeepSeek V4 Pro 0813 is [available today on Baseten Model APIs](https://www.baseten.co/library/deepseek-v4-pro-0813/), as well as on dedicated deployments. DeepSeek V4 Pro 0813 brings frontier performance at lower prices than closed models:

- Input tokens (cache miss): $1.32/m
- Input tokens (cache hit): $0.132/m
- Output tokens: $3.96/m

You can get started today with a single API call:

```
1import os
2from openai import OpenAI
3
4client = OpenAI(
5    api_key=os.environ["BASETEN_API_KEY"],
6    base_url="https://inference.baseten.co/v1")
7
8response = client.chat.completions.create(
9    model="deepseek-ai/DeepSeek-V4-Pro-0813",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant"},
12        {"role": "user", "content": "Write Hello World in Python"},
13    ],
14    stream=True,
15    reasoning_effort="low",
16    extra_body={"thinking": {"type": "enabled"}}
17)
18
19print(response.choices[0].message.content)
```
