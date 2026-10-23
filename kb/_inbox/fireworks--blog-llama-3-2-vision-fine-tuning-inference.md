---
title: 'Llama 3.2 Vision and Text Models: Run and Fine-Tune | Fireworks'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/llama-3-2-vision-fine-tuning-inference
author: null
published: '2024-09-25'
fetched: '2026-10-23T06:12:02Z'
classifier: null
taxonomy_rev: 2
words: 1143
content_sha256: 37a12152016d987766a90d30636af47a29d8e90f6035df7e31b24804dd472e4e
---

# Llama 3.2 Vision and Text Models: Run and Fine-Tune | Fireworks

We are excited to announce support for the newest additions to the **Llama collection** from Meta. With the addition of **Llama 3.2**, developers gain access to new tools that enable the creation of sophisticated multi-component AI systems that combine models, modalities, and external tools to deliver advanced real-world AI solutions.

# Llama 3.2: Seeing The World More Clearly (And Quickly)

The release of **Llama 3.2 1B**, **Llama 3.2 3B**, **Llama 3.2 11B Vision**, and **Llama 3.2 90B Vision** models brings a range of text-only and multimodal models designed to enhance modular AI workflows. These models provide deep customization, allowing developers to tailor solutions and accelerate specific tasks in compound AI systems.

**Get started today on Fireworks:**

- [**Llama 3.2 1B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-1b-instruct): Ideal for **retrieval and summarization** tasks such as **personal information management**, **multilingual knowledge retrieval**, and **rewriting tasks**.
- [**Llama 3.2 3B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-3b-instruct): Optimized for **query and prompt rewriting**, it supports applications like **mobile AI-powered writing assistants** and **customer service tools** running on **edge devices**.
- [**Llama 3.2 11B Vision**](https://fireworks.ai/models/fireworks/llama-v3p2-11b-vision-instruct) and [**Llama 3.2 90B Vision**](https://fireworks.ai/models/fireworks/llama-v3p2-90b-vision-instruct): These models extend capabilities with **image understanding** and **visual reasoning** for tasks such as **image captioning**, **visual question answering**, and **document visual analysis**.

The instruct variants of these models are available serverless (pay-per-token for models on Fireworks-configured GPUs). Both the instruct and non-instruct variants of these models are available [on-demand](https://docs.fireworks.ai/guides/ondemand-deployments) (private GPU instances billed per GPU second). Meta’s Llama Guard 3 models for detecting violating content are also available on-demand.

## Key Highlights

## Llama 3.2 Adds New Multimodal Capabilities, Expanding Use Cases For Developers

The release of multimodal models unlocks exciting new production use cases for developers, from enterprise to everyday applications.

Examples of use cases for Llama 3 models on Fireworks includes:

- **Visual Question Answering and Reasoning**: In healthcare, clinicians can use multimodal systems to ask questions about medical images, like “Is there a fracture in this X-ray?” The system analyzes the image, provides a precise answer, and highlights key areas, enabling faster, more accurate diagnoses and reducing human error in time-sensitive situations.
- **Document Visual Question Answering**: For document-heavy fields like legal and finance, visual-language models can extract specific information from PDFs or charts, such as “What is the total amount due?” This reduces manual effort, speeds up analysis, and boosts accuracy in reviewing complex documents.
- **Image Captioning**: In retail, compound-AI systems can automatically generate product descriptions from images, such as “A sleek black leather handbag with gold hardware.” The system analyzes the product image and creates a detailed, engaging caption that enhances customer experience and boosts metrics like conversion rates. By eliminating the need for manual captioning, this approach enables businesses to quickly scale as their product catalogs grow, while maintaining consistency and accuracy.

See how customers like AlliumAI are supporting multimodal models in production with Fireworks in this [blog post](https://fireworks.ai/blog/multimodal-enterprise).

# Start Small Then Scale Quickly and Efficiently with Llama 3.2 Models on Fireworks

**Llama models**, fine-tuned and deployed through Fireworks, offer developers the flexibility to build personalized AI systems tailored to specific needs.

With Fireworks handling the **fine-tuning and inference**, developers can leverage these powerful tools to accelerate innovation and bring their AI solutions to market faster. For example, **Fireworks** can serve **Llama 3.2 1B** in approximately **500 tokens/second** and **Llama 3.2 3B in 270 tokens/second.**

## Pricing and Deployment Options: The Great News

There’s no one-size-fits-all approach to developing compound AI systems, which is why Fireworks offers a number of different options for using and deploying models like **Llama-3.2** for production AI (including [serverless, on-demand, and enterprise reserved](https://fireworks.ai/blog/why-gpus-on-demand)).

We’re also happy to announce **new, competitive pricing** for text and multimodal models, especially for the Llama 3.2 - 11B and Llama 3.2 - 90B multimodal models which will be the **same price as the text-only models**. Images will be charged as text tokens. The exact number of tokens depends on image resolution and model. Images for the Llama 3.2 vision models are typically counted as 6400 text tokens.

### Serverless

Fireworks serverless is the easiest way to get started. Serverless offers the new Llama models on pre-configured GPUs, no set-up required.

### On-Demand

For heavier volume and fully configurable latency and reliability, Fireworks on-demand provides private GPUs to host Llama 3.2. Developers pay per second for on-demand with no commitments. The efficiency of Fireworks’ software stack enables significant price, throughput and latency improvements compared to running vLLM on private GPUs (see [pricing](https://fireworks.ai/pricing#ondemand) and performance [tests](https://fireworks.ai/blog/why-gpus-on-demand)).

### Enterprise Reserved

For high-volume applications, Fireworks offers private, enterprise GPU deployments options that are fully personalized and backed by SLAs and performance guarantees.

[Contact us](https://fireworks.ai/company/contact-us) for additional information.

## Customize Llama 3.2 With Fine-Tuning

Meta is releasing the Llama 3.2 models under very open and permissive licensing that makes them ideal for fine-tuning and additional model customization.

Today you can fine-tune the [**Llama 3.2 1B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) and [**Llama 3.2 3B (text-only)**](https://fireworks.ai/models/fireworks/llama-v3p2-3b-instruct) models on Fireworks, with fine-tuning for multimodal models like Llama 3.2 11B Vision and Llama 3.2 90B Vision coming soon.

For more information about fine-tuning, read our documentation [here](https://docs.fireworks.ai/fine-tuning/fine-tuning-models).

# Getting Started with Llama 3.2

## Try the models out directly in our playground

With our model playground, you can focus on developing a feel for a model’s behavior, adjusting prompt and parameter values, and then grabbing the code to test our inference APIs.

For example, how would you describe making pancakes from scratch to someone that’s learning to make breakfast for themselves, the very first time?

Is date night coming up and you need some ideas on the fly? Try out the Llama 3.2 3B chat API.

Writing a paper for an art history class about comedic paraodies of famous artworks but need help getting started? [\*\*Llama 3.2 90B Vision](https://fireworks.ai/models/fireworks/llama-v3p2-90b-vision-instruct) can help out.\*\*

## Next, try using the models with our inference APIs

To quickly get up and running using Llama 3.2 on the Fireworks visit [fireworks.ai](https://fireworks.ai/) to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.

### Install the Fireworks Python package

`pip install --upgrade fireworks-ai`

### Accessing Llama 3.2 on Serverless Inference API

Below code snippet instantiates Fireworks client and uses chat completions API to call the Llama 3.2 listed at - `accounts/fireworks/models/llama-v3p2-3b-instruct`.

`jsxCopy`
1234567891011121314

The above API request results in the below response.

`jsxCopy`
12345678910

# Get Started Today

Ready to start building with Llama 3.2? Here’s how to get started:

- **Run inference:** Run the models with blazing fast speeds [serverless](https://fireworks.ai/models/fireworks/llama-v3p2-11b-vision-instruct) or on-demand
- **Fine Tune Llama 3.2**: Follow our [step-by-step guide](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) on fine-tuning models.
- **Deploy Your Model**: Follow our [deployment guide](https://docs.fireworks.ai/models/deploying) to quickly deploy your fine-tuned model.
- **Join Our Community**: Join our [Discord channel](https://discord.gg/fireworks-ai) to connect with other developers and the Fireworks team

**Contact us**: [Reach out](https://fireworks.ai/company/contact-us) to discuss how we can help you leverage Llama 3.2 and the Fireworks inference engine for your specific use case.
