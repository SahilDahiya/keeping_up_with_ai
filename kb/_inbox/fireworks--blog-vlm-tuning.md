---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/vlm-tuning
author: null
published: '2025-07-29'
fetched: '2026-08-12T06:30:25Z'
classifier: null
taxonomy_rev: 2
words: 852
content_sha256: 497449bfd55f3c3dc8c9de72608f86c80ae1dd42d66761100f372b79b3af016a
---

# Fireworks AI

Fireworks now offers supervised fine-tuning for Vision-Language Models (Qwen 2.5 VL family), letting you adapt state-of-the-art VLMs to your specific visual domain. Train models on your images and text data to achieve higher accuracy for specialized tasks like medical imaging, financial document analysis, or product cataloging. Built for production with optimized kernels, 64K context support, and deployment on the same platform powering Cursor fast-apply.

Enterprises across healthcare, finance, and ecommerce accumulate massive amounts of domain-specific visual data—from medical imaging and financial documents to product catalogs. Vision-Language Models can understand and reason about both images and text simultaneously, unlocking applications like automated document processing, visual Q&A, and multimodal workflows.

While general-purpose vision-language models are powerful, they often miss the nuanced patterns and terminology specific to an industry. Fine-tuning VLMs on your domain-specific data dramatically improves accuracy for specialized visual tasks and enables models to understand your unique terminology and response formats.

Today, we're launching **supervised fine-tuning for Vision-Language Models** on Fireworks, enabling you to adapt state-of-the-art Qwen 2.5 VL models to understand your specific visual domain with the precision your applications demand. This extends our comprehensive [Supervised Fine-tuning V2 platform](https://fireworks.ai/blog/supervised-finetuning-v2) to multimodal capabilities, giving you the tools to turn your visual data into a competitive advantage.

Many applications we see on the Fireworks platform solve problems that seemed impossible just a 1-2 years ago. Automation companies process streams of screenshots to automate complex workflows. E-commerce companies enrich product catalogues with additional tags for retrieval and personalization. Financial institutions analyze complex documents combining charts, tables, and text with unprecedented accuracy.

But generic & out-of-the-box models, no matter how capable, can only take you so far. When you need to categorize products across thousands of SKUs with nuanced attribute differences, automate complex workflows for niche legacy enterprise software, or extracted structured data from documents with a mixture of charts, tables, checkboxes — you need models trained on your data, understanding your terminology, responding in your preferred format.

VLM fine-tuning bridges this gap, allowing you to:

- •**Improve accuracy for specialized tasks** : Achieve higher performance on domain-specific visual understanding - one of our clients was able to match accuracy on their task compared to closed source providers allowing them 1.5x lower latency and 100x lower cost.
- •**Adapt models to your visual domain** : Train on your specific types of images and visual patterns
- •**Customize response styles** : Train models to respond in your preferred format and tone
- •**Handle multi-modal workflows** : Seamlessly process documents, images, and text together

We're launching with support for the complete Qwen 2.5 VL family, giving you flexibility to choose the right model size for your needs:

- •**Qwen 2.5 VL 3B Instruct** : Ideal for strict latency or low-cost requirements. E.g., Simple product tagging, basic document extraction, image classification
- •**Qwen 2.5 VL 7B Instruct** : Good balance between additional reasoning power and latency/cost. Still fits on one A100/H100. We’ve seen use-cases for document extraction, mid-level VQA, screenshot grounding
- •**Qwen 2.5 VL 32B Instruct** : High-performance option for complex visual tasks. Complex VQA, multi-lingual image captioning, RPA workflows, support chatbots with visual understanding
- •**Qwen 2.5 VL 72B Instruct** : Maximum capability for the most demanding applications. E.g., synthetic data generation, long-context multi-turn workflows, detailed medical image interpretation

Each model supports fine-tuning with datasets containing both images and text, enabling sophisticated multi-modal understanding tailored to your specific requirements.

We've designed the fine-tuning process to be as straightforward as possible:

1. **Prepare Your Dataset** : Format your images and text in our JSONL format with base64-encoded images
2. **Upload to Fireworks** : Use our CLI, web interface, or REST API to upload your training data
3. **Launch Training** : Start your fine-tuning job with just a few commands
4. **Deploy and Test** : Once training completes, deploy your custom model and start making inference calls

Our [documentation](https://docs.fireworks.ai/fine-tuning/fine-tuning-vlm) includes conversion scripts, and best practices to help you get up and running quickly.

VLM fine-tuning on Fireworks isn't just a research tool—it's built for production workloads using our [Supervised Fine-tuning V2 platform](https://fireworks.ai/blog/supervised-finetuning-v2):

- •**Optimized Training Speed** : Fine-tune models 2x faster than our previous generation with ongoing optimizations continuously being added
- •**Extended Context Support** : Handle training with context lengths up to 64K tokens for complex visual documents and multi-image conversations
- •**Comprehensive Monitoring** : Track training progress, monitor model performance, and optimize continuously
- •**Low Latency and High Throughput deployments** : Deploy on the same serving platform that powers[Cursor fast apply](https://fireworks.ai/blog/cursor) . One of our enterprise VLM clients have achieved 100x lower cost and 1.5x lower latency than closed source providers

VLM fine-tuning is available now for all Fireworks users. Whether you're processing medical records at scale, analyzing financial documents, or building the next breakthrough in visual AI, our platform provides the speed, efficiency, and flexibility you need.

Ready to build domain-specific visual intelligence? Check out our [fine-tuning documentation](https://docs.fireworks.ai/fine-tuning/fine-tuning-vlm), join our [Discord community](https://discord.gg/fireworks-ai) for support, and start training your first specialized VLM today.

**Need help getting started?** Our team can help you design the right approach for your use case. [Contact us](https://fireworks.ai/contact) to discuss your specific requirements.
