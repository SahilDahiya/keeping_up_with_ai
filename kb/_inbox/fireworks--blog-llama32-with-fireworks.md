---
title: 'Partnering with Meta: Bringing Llama 3.2 to Fireworks for Fine-Tuning and
  Inference'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/llama32-with-fireworks
author: null
published: '2024-09-25'
fetched: '2026-08-12T06:28:37Z'
classifier: null
taxonomy_rev: 2
words: 1332
content_sha256: 960d524eb76ac6458ab312c2b6a39110c5dabb89fc95e5f8b064a7b75ebdac0d
---

# Partnering with Meta: Bringing Llama 3.2 to Fireworks for Fine-Tuning and Inference

We are excited to announce support for the newest additions to the **Llama collection** from Meta. With the addition of **Llama 3.2**, developers gain access to new tools that enable the creation of sophisticated multi-component AI systems that combine models, modalities, and external tools to deliver advanced real-world AI solutions.

The release of **Llama 3.2 1B**, **Llama 3.2 3B**, **Llama 3.2 11B Vision**, and **Llama 3.2 90B Vision** models brings a range of text-only and multimodal models designed to enhance modular AI workflows. These models provide deep customization, allowing developers to tailor solutions and accelerate specific tasks in compound AI systems.

**Get started today on Fireworks:**

- •[**Llama 3.2 1B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) : Ideal for**retrieval and summarization** tasks such as**personal information management** ,**multilingual knowledge retrieval** , and**rewriting tasks** .
- •[**Llama 3.2 3B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-3b-instruct) : Optimized for**query and prompt rewriting** , it supports applications like**mobile AI-powered writing assistants** and**customer service tools** running on**edge devices** .
- •[**Llama 3.2 11B Vision**](https://fireworks.ai/models/fireworks/llama-v3p2-11b-vision-instruct) and[**Llama 3.2 90B Vision**](https://fireworks.ai/models/fireworks/llama-v3p2-90b-vision-instruct) : These models extend capabilities with**image understanding** and**visual reasoning** for tasks such as**image captioning** ,**visual question answering** , and**document visual analysis** .

The instruct variants of these models are available serverless (pay-per-token for models on Fireworks-configured GPUs). Both the instruct and non-instruct variants of these models are available [on-demand](https://docs.fireworks.ai/guides/ondemand-deployments) (private GPU instances billed per GPU second). Meta’s Llama Guard 3 models for detecting violating content are also available on-demand.

|  | Text | Multimodal | Recommendation | Use Case | 
|---|---|---|---|---|
| Llama 3.2 1B | ✅ |  | Ideal for retrieval and summarization tasks. | This model can be effectively deployed for personal information management, multilingual knowledge retrieval, and rewriting tasks running locally on edge devices, offering efficiency in handling data close to the user. | 
| Llama 3.2 3B | ✅ |  | Recommended for query and prompt rewriting and optimized for mobile AI-powered writing assistants and edge devices. | This model is perfect for customer service applications and mobile AI-powered writing assistants, allowing businesses to deploy high-performance models that deliver real-time AI solutions at scale. | 
| Llama 3.2 11B Vision | ✅ | ✅ | Optimized for image understanding and visual reasoning, it excels in image captioning, image-text retrieval, visual grounding, and document visual question answering. | This model is critical for any application needing advanced visual and text-based comprehension, such as enterprise search and expert copilots in areas like coding, math, and medicine. | 
| Llama 3.2 90B Vision | ✅ | ✅ | Similar to the 11B model, this larger model offers exceptional performance in visual question answering, visual reasoning, and other complex multimodal tasks. | Its ability to handle both image and text inputs allows for a range of applications, from image captioning to document analysis, making it ideal for industries like healthcare, legal, and finance. | 

The release of multimodal models unlocks exciting new production use cases for developers, from enterprise to everyday applications.

Examples of use cases for Llama 3 models on Fireworks includes:

- •**Visual Question Answering and Reasoning** : In healthcare, clinicians can use multimodal systems to ask questions about medical images, like "Is there a fracture in this X-ray?" The system analyzes the image, provides a precise answer, and highlights key areas, enabling faster, more accurate diagnoses and reducing human error in time-sensitive situations.
- •**Document Visual Question Answering** : For document-heavy fields like legal and finance, visual-language models can extract specific information from PDFs or charts, such as "What is the total amount due?" This reduces manual effort, speeds up analysis, and boosts accuracy in reviewing complex documents.
- •**Image Captioning** : In retail, compound-AI systems can automatically generate product descriptions from images, such as "A sleek black leather handbag with gold hardware." The system analyzes the product image and creates a detailed, engaging caption that enhances customer experience and boosts metrics like conversion rates. By eliminating the need for manual captioning, this approach enables businesses to quickly scale as their product catalogs grow, while maintaining consistency and accuracy.

See how customers like AlliumAI are supporting multimodal models in production with Fireworks in this [blog post](https://fireworks.ai/blog/multimodal-enterprise).

**Llama models**, fine-tuned and deployed through Fireworks, offer developers the flexibility to build personalized AI systems tailored to specific needs.

With Fireworks handling the **fine-tuning and inference**, developers can leverage these powerful tools to accelerate innovation and bring their AI solutions to market faster. For example, **Fireworks** can serve **Llama 3.2 1B** in approximately **500 tokens/second** and **Llama 3.2 3B in 270 tokens/second.**

There’s no one-size-fits-all approach to developing compound AI systems, which is why Fireworks offers a number of different options for using and deploying models like **Llama-3.2** for production AI (including [serverless, on-demand, and enterprise reserved](https://fireworks.ai/blog/why-gpus-on-demand)).

We’re also happy to announce **new, competitive pricing** for text and multimodal models, especially for the Llama 3.2 - 11B and Llama 3.2 - 90B multimodal models which will be the **same price as the text-only models**. Images will be charged as text tokens. The exact number of tokens depends on image resolution and model. Images for the Llama 3.2 vision models are typically counted as 6400 text tokens.

Fireworks serverless is the easiest way to get started. Serverless offers the new Llama models on pre-configured GPUs, no set-up required.

| Base Model Parameter Bucket | Specific Model | $/1M tokens | 
|---|---|---|
| 0B - 4B | Llama 3.2 1B Instruct | $0.1 | 
| 0B - 4B | Llama 3.2 3B Instruct | $0.1 | 
| 4B - 18B | Llama 3.2 11B Vision Instruct | $0.2 | 
| 16B+ | Llama 3.2 90B Vision Instruct | $0.9 | 

For heavier volume and fully configurable latency and reliability, Fireworks on-demand provides private GPUs to host Llama 3.2. Developers pay per second for on-demand with no commitments. The efficiency of Fireworks’ software stack enables significant price, throughput and latency improvements compared to running vLLM on private GPUs (see [pricing](https://fireworks.ai/pricing#ondemand) and performance [tests](https://fireworks.ai/blog/why-gpus-on-demand)).

For high-volume applications, Fireworks offers private, enterprise GPU deployments options that are fully personalized and backed by SLAs and performance guarantees.

[Contact us](https://fireworks.ai/company/contact-us) for additional information.

Meta is releasing the Llama 3.2 models under very open and permissive licensing that makes them ideal for fine-tuning and additional model customization.

Today you can fine-tune the [**Llama 3.2 1B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) and [**Llama 3.2 3B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-3b-instruct) models on Fireworks, with fine-tuning for multimodal models like Llama 3.2 11B Vision and Llama 3.2 90B Vision coming soon.

For more information about fine-tuning, read our documentation [here](https://docs.fireworks.ai/fine-tuning/fine-tuning-models).

With our model playground, you can focus on developing a feel for a model’s behavior, adjusting prompt and parameter values, and then grabbing the code to test our inference APIs.

For example, how would you describe making pancakes from scratch to someone that’s learning to make breakfast for themselves, the very first time?

Is date night coming up and you need some ideas on the fly? Try out the Llama 3.2 3B chat API.

Writing a paper for an art history class about comedic paraodies of famous artworks but need help getting started? [**Llama 3.2 90B Vision](https://fireworks.ai/models/fireworks/llama-v3p2-90b-vision-instruct) can help out.**

To quickly get up and running using Llama 3.2 on the Fireworks visit [fireworks.ai](https://fireworks.ai/) to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.

`pip install --upgrade fireworks-ai`

Below code snippet instantiates Fireworks client and uses chat completions API to call the Llama 3.2 listed at - `accounts/fireworks/models/llama-v3p2-3b-instruct`.

1234567891011121314

The above API request results in the below response.

12345678910

Ready to start building with Llama 3.2? Here’s how to get started:

- •**Run****inference:** Run the models with blazing fast speeds[serverless](https://fireworks.ai/models/fireworks/llama-v3p2-11b-vision-instruct) or on-demand
- •**Fine Tune Llama 3.2** : Follow our[step-by-step guide](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) on fine-tuning models.
- •**Deploy Your Model** : Follow our[deployment guide](https://docs.fireworks.ai/models/deploying) to quickly deploy your fine-tuned model.
- •**Join Our Community** : Join our[Discord channel](https://discord.gg/fireworks-ai) to connect with other developers and the Fireworks team

**Contact us**: [Reach out](https://fireworks.ai/company/contact-us) to discuss how we can help you leverage Llama 3.2 and the Fireworks inference engine for your specific use case.
