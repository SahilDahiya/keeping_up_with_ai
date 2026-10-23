---
title: 'FireLLaVA: Commercially Permissive Open Source LLaVA Model | Fireworks'
kind: blog
topic: models
subtopic: multimodal
secondary_topics: []
summary: Describes FireLLaVA, a commercially-licensed open-source LLaVA vision-language
  model combining a Vicuna-13B LLM with an OpenAI CLIP-ViT vision encoder, and its
  training methodology for joint image-text understanding.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/firellava-commercial-open-source-llava-model
author: null
published: '2024-01-18'
fetched: '2026-10-23T06:13:42Z'
classifier: claude
taxonomy_rev: 2
words: 798
content_sha256: e8d59f21a678414b5774e21b2d165c8b0146d0ab5a28aa1a2a412eba4e6b6fb2
---

# FireLLaVA: Commercially Permissive Open Source LLaVA Model | Fireworks

We have come to rely heavily on text as input for foundation models to generate responses. However, in real-world applications, we frequently process and analyze data from various sources, such as images and sound. Notably, images often contain more intricate and dense information than text. To address this, multi-modality models have been developed to process and analyze data from multiple sources effectively, providing a more comprehensive and accurate understanding of the input data.

We are excited to announce that we have open-sourced FireLLaVA under the Llama 2 Community License. It is the first LLaVA multi-modality model with a commercially permissive license. You can now download FireLLaVA from our [Huggingface repository](https://huggingface.co/fireworks-ai/FireLLaVA-13b), use it directly from our fast API, or experiment with it in our [playground](https://fireworks.ai/models/fireworks/firellava-13b). By utilizing FireLLaVA, we can advance the development of more sophisticated and versatile models capable of handling diverse data sources.

### What is a VLM model and what are the use cases

Vision-Language Models (VLMs) are multi-modal models that understand both visual content and text prompts.VLMs are valuable for a variety of use cases, such as writing marketing descriptions given product images or building chatbots that can interpret charts. LLaVA is a Visual Language Model (VLM) developed by Haotian Liu et al that achieves strong performance on 11 benchmarks. The best performing open source version of LLaVA 1.5 is based on the Vicuna v1.5 13B language model as the LLM component and the OpenAI CLIP-Vit as the vision component. It proposes a generic architecture and a training methodology that enables the language model to understand vision content and respond accordingly.

While LLaVA v1.5 13B model weights are open sourced, a big hurdle to using the OSS LLaVA model for commercial usage is that it was trained with GPT4 generated training data and is subject to non-commercial licenses like cc by-nc-4.0.

Do note that FireLLaVA, similar to the original LLaVA model, was also trained with a single image in the conversation, and therefore its performance may degrade with multiple images present in the conversation. When using the FireLLaVA model to build a vision-capable chat bot, we recommend including only the last image in the conversation. It also has similar limitations as the original LLaVA model in that input images are generally downscaled and small texts in the input images may be hard for the model to read.

### FireLLaVA

Fireworks.ai set out to recreate a commercially-usable version of the LLaVA model leveraging only OSS models for data generation and training. More specifically, LLaVA authors came up with a novel approach to generate visual language conversations using GPT4 language-only model by giving the model bounding box labels and captions of images, and using them for instruction fine-tuning. We recreated these training data with a language-only OSS model, the CodeLlama 34B Instruct model following their approach (more details in the [original paper](https://arxiv.org/abs/2310.03744)). CodeLlama 34B Instruct model was picked to strike a balance between model quality and efficiency. The final mix of the data for the instruction fine-tuning stage consists of 588K lines of single and multi-turn visual question answering or conversation data, mixed from the permissive portion of the original LLaVA training data and Fireworks.ai generated training data. Moreover, we are open-sourcing the model at [fireworks-ai/FireLLaVA-13b](https://huggingface.co/fireworks-ai/FireLLaVA-13b) that can be loaded for inference with transformers version >= 4.35.3, and named it FireLLaVA.

### Demo

You can now try out FireLLaVA in our [playground](https://fireworks.ai/models/fireworks/firellava-13b). The model is able to respond reasonably well to clear instructions such as And perform some reasoning based on visual inputs such as Or, visual understanding of more abstract content such as

### Model performance

To grasp an understanding of how well FireLLaVA compared to one that was trained on GPT-4 generated data, we conducted seven benchmarks that are commonly included in visual understanding model academic papers, following the instructions [here](https://github.com/haotian-liu/LLaVA/blob/main/docs/Evaluation.md). The result is as follows:

As the results show, FireLLaVA trained on our OSS model training data performs close to the original LLaVA model trained on GPT4 generated data, and even slightly beats the original LLaVA model on four of the seven benchmarks.

This result highlights the fact that bootstrapping Language-Only Model for high quality VLM model training data generation is useful, and with careful prompt engineering, getting training data at a similar level of quality as GPT4 generated data is achievable.

### Using the API

We are providing both the completions API and chat completions API to the commercially-viable LLaVA model. The API interface is compatible with OpenAI Vision models except that the “detail” parameter is currently ignored since all images are treated uniformly by the nature of LLaVA model. Developers can easily integrate the vision-capable APIs into their applications to unlock new capabilities. Here is an example:

`pythonCopy`
12345678910111213141516171819202122232425

### References:

- LLaVA: Large Language and Vision Assistant Visual Instruction Tuning: [https://llava-vl.github.io/](https://llava-vl.github.io/)
