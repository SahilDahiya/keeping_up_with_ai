---
title: A checklist for switching to open source ML models
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/a-checklist-for-switching-to-open-source-ml-models
author: Philip Kiely
published: '2023-11-20'
fetched: '2026-11-12T06:13:44Z'
classifier: null
taxonomy_rev: 2
words: 477
content_sha256: 3d3cf44e9793cee6bd3b923e1548404c0b520eb434e37c3ba218314a6d8255c6
---

# A checklist for switching to open source ML models

AI engineering
# A checklist for switching to open source ML models

Transitioning from using ML models via closed source APIs to open source ML models? This checklist provides all necessary resources for the shift.


- Authors
- Date
- November 20, 2023

Switching from a closed source ecosystem where you consume ML models from API endpoints to the world of open source ML models can seem intimidating. But this checklist will give you all of the resources you need to make the leap.

The biggest advantage of the open source ecosystem in ML is the sheer number and variety of models to choose from. But that amount of choice can be overwhelming. Here are some alternatives to closed-source models to get you started:

- Text embedding models: Closed source: [OpenAI text-embedding-3](https://platform.openai.com/docs/guides/embeddings/embedding-models)
Open source: [BAAI text embedding models](https://www.baseten.co/library/tag/embedding/)
- Speech to text (audio transcription) models: Closed source: [Whisper from the Audio API](https://platform.openai.com/docs/guides/speech-to-text)
Open source: Whisper on your own infra
- Text to speech (audio generation) models: Closed source: [Audio API text to speech endpoint](https://platform.openai.com/docs/guides/text-to-speech)
Open source: [Orpheus TTS](https://www.baseten.co/library/orpheus-tts/)

Inference for most generative models like LLMs requires GPUs. Picking the right GPU is essential: you want the least expensive GPU powerful enough to run the model with acceptable performance.

For a 70 billion parameter LLM like [Llama 3.3 70B](https://www.baseten.co/library/llama-3-3-70b-instruct/), you need 2-4 H100 GPUs, but for the largest LLMs like DeepSeek-R1, you'll need H200 GPUs or multi-node inference. Partial H100 GPUs via multi-instance GPU (MIG) or smaller, cheaper L4 GPUs give great performance for smaller models like Whisper and embedding models.

Here are some buyer’s guides to GPUs:

If you’re just experimenting with open source models or you need to get something in production yesterday, you can skip this step. But one of the most powerful things that switching to open source models unlocks is the ability to optimize a balance of latency, throughput, quality, and cost to align with your use case.

Get started with:

Once you have your model and hardware configuration, it’s time to deploy. You can deploy a curated selection of models from our model library in just a couple of clicks or use Truss, our open source model packaging framework, to get any model up and running behind an API endpoint.

Dive into deployment with:

- Open source models in [the Baseten model library](https://www.baseten.co/library).
- [A quickstart guide for Truss](https://docs.baseten.co/quickstart), an open source model packaging framework.

Once you’ve deployed your model, you’ll need to use the [model endpoint](https://docs.baseten.co/inference/calling-your-model) to integrate your model into your application.

Baseten has guides for:

- Streaming model output for LLMs.
- Working with base64 output for image and audio generation.

If you want to dive deeper, check out our [guide to open source alternatives for ML models](https://www.baseten.co/blog/open-source-alternatives-for-machine-learning-models/). Wherever you are in your journey from evaluation to adoption for open source ML models, we’re here to help at [support@baseten.co](mailto:support@baseten.co).
