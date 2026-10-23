---
title: 'Llama 3.1 405B API: Serverless Inference Endpoints | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/llama-3-1-405b-api
author: null
published: '2024-07-23'
fetched: '2026-10-23T06:13:46Z'
classifier: null
taxonomy_rev: 2
words: 500
content_sha256: ac8fa1d5639da71f4c6694d57f42291cb3d045c1c49286a10433a8d25b61f130
---

# Llama 3.1 405B API: Serverless Inference Endpoints | Fireworks

We’re thrilled to introduce Llama 3.1 inference endpoints in partnership with Meta. With expanded context length, multilingual support, tool calling, and the inclusion of Llama 3.1 405B, Llama 3.1 represents a significant leap forward in AI capabilities. Fireworks is proud to be a launch partner, offering AI developers immediate access to Llama 3.1 for production use from day one. Llama 3.1 is available on Fireworks inference engine and optimized for performance, which means you benefit from the lowest latency and most-efficient deployment.

List of Llama 3.1 models available on Fireworks

Our mission is to provide the fastest and most efficient inference platform and tools for building compound AI systems, equipping developers with the essential building blocks to create custom, production-ready AI applications. Fireworks is at the forefront of the rapid shift towards compound AI systems, which integrate multiple models and tools to enhance performance, reliability, and control. With the addition of Llama 3.1 to our portfolio of over 100 state-of-the-art models, and its new tool-calling capabilities, we are advancing this mission even further.

This week, we are also introducing [AMD Instinct MI300 accelerators](https://www.amd.com/en/products/accelerators/instinct/mi300.html) alongside [NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/) to power serverless inference for Llama 3.1 405B Instruct.

### Key Highlights about Llama 3.1

- **Unmatched Flexibility and Control**: Llama 3.1 405B is the largest openly available foundation model, offering state-of-the-art capabilities that rival the best closed-source models.
- **Expanded Context and Multilingual Support**: The new models support context lengths up to 128K and span 8 languages, enabling richer and more nuanced interactions.
- **Enabling New Capabilities**: With Llama 3.1, the community can unlock new possibilities in synthetic data generation and model distillation.
- **Commitment to Open AI**: Fireworks continues to champion openness in AI, fostering innovation and safety in the ecosystem.
- **Tools for Developers**: Llama 3.1 provides robust tools for creating custom agents and new agentic behaviors, bolstered by new security and safety measures.

## Getting Started with Llama 3.1 405B

To quickly get up and running using Llama 3.1 on the Fireworks visit [**fireworks.ai**](https://fireworks.ai/) to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.

### Install the Fireworks Python package

`pip install *--*upgrade fireworks-ai`

### Accessing Llama 3.1 on Serverless Inference API

Below code snippet instantiates `Fireworks` client and uses chat completions API to call the Llama 3.1 listed at - `accounts/fireworks/models/llama-v3p1-405b-instruct`.

`pythonCopy`
12345678910111213

The above API request results in the below response.

`pythonCopy`
12345678910

### Commitment to Open and Responsible AI Development

At Fireworks, we believe that openness leads to better, safer products, faster innovation, and a healthier market. We are dedicated to the responsible release of models with our partners and continuously work with them on developing tools to ensure safety and security in AI applications.

### Building Compound AI Systems with Llama 3.1

We’re excited to see how the community leverages Fireworks to create groundbreaking applications with Llama 3.1. For inference pricing and deployment options, visit [fireworks.ai/pricing](https://fireworks.ai/pricing).

For more information and to get started with Llama 3.1, visit [fireworks.ai](https://fireworks.ai/).
