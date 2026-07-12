---
title: Compound AI systems explained
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/tool-use
summary: Explains compound AI systems and how multiple models, tools, and control
  logic combine into applications.
source: baseten
url: https://www.baseten.co/blog/compound-ai-systems-explained/
author: Rachel Rapp
published: '2024-08-06'
fetched: '2026-07-11T04:09:15Z'
classifier: codex
taxonomy_rev: 1
words: 1554
content_sha256: 04d534693b923c981e85bfb7067d50a9ff2f6fb9ee702a903cd9785cb57696d2
triage: keep
skip_reason: null
---

# Compound AI systems explained

![Compound AI Explained](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747439065-compound-ai.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Compound AI systems combine different AI models and processing steps to form one integrated workflow. Their modularity makes them more flexible, performant, and cost-efficient than monolithic workflows, although they can be more difficult to build and serve in production.

![A diagram comparing single model AI and compound AI with multiple components.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960435-untitled-6.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) In contrast to single model AI, compound AI systems combine multiple models and processing steps.

In contrast to single model AI, compound AI systems combine multiple models and processing steps.New AI models are constantly setting records across different domains. But as applied AI use cases become more complex, AI systems are adapting.

We're seeing it more and more: the next generation of AI products is being built using multiple models. To name just a few examples:

- [Bland.AI](https://www.bland.ai)does AI phone calling, a task requiring steps like transcription and text-to-speech generation.
- [Descript](https://descript.com/)enables users to edit videos (including AI voice and video generation) from their transcription.
- Open-source compound models and workflows like - [Mixtral](https://mistral.ai/news/mixtral-of-experts/)and- [ComfyUI](https://www.baseten.co/blog/deploying-custom-comfyui-workflows-as-apis/)are being used across multiple industries.
- Companies like - [Google](https://deepmind.google/technologies/gemini/ultra/),- [Microsoft](https://www.microsoft.com/en-us/research/blog/the-power-of-prompting/), and- [OpenAI](https://openai.com/index/chatgpt-plus/)use compound AI systems to set new records across multi-task language understanding, medical question answering, and chatbots used by millions of people.

In this article, we break down what compound AI systems are and why AI builders are shifting towards them. We’ll discuss their benefits, challenges, common use cases, and how you can leverage compound AI systems in production.

## What is a compound AI system?

Compound AI systems combine multiple interacting components to form a holistic workflow. Components can include:

- Multiple AI/ML models (e.g., speech-to-text and text-to-image).
- Distinct processing steps (like chunking an audio file before transcribing it).
- Varying architectures (such as combining rule-based systems with ML models).
- Dedicated hardware (CPUs and GPUs) and infrastructure for orchestration and inference.

![A diagram comparing monolithic AI with one workflow tightly coupled to its hardware, and compound AI with multiple models and processings steps, each with their own hardware.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960410-untitled-5.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Monolithic AI uses single models or workflows tightly coupled with their infrastructure, while compound AI leverages multiple modularized processing components.

Monolithic AI uses single models or workflows tightly coupled with their infrastructure, while compound AI leverages multiple modularized processing components.Berkeley AI first coined the term “compound AI systems” [in their blog post](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) analyzing the shift from single models to compound AI. While the first generation of AI products has used single models (for tasks like image generation, transcription, and chatbots), now we’re seeing the next generation of applied AI is multi-model: integrating different steps to perform complex tasks (like multi-modal chatbots, phone call agents, video editors, and more).

This approach isn’t new. AI has always benefitted from combining different processing steps to create new solutions—like adding a convolution operation to process images (CNNs) or gating mechanisms for processing time series data (LSTMs). Moving from single- to multi-component AI is a natural next step.

## Use cases for compound AI

Any system that can benefit from leveraging multiple models or processing steps is a use case for compound AI. Some examples include:

- **Healthcare.**Integrate medical imaging, patient health records, and predictive analytics to provide comprehensive diagnostic support and prognoses.
- **Customer service.**Enhance chatbot interactions by incorporating sentiment analysis and personalized recommendations into conversations.
- **Financial analysis.**Combine transaction data analysis, market trend forecasting, and anomaly detection to assess risk.
- **Manufacturing.**Optimize production processes by integrating predictive maintenance models, quality control algorithms, and supply chain optimization tools.
- **Robotics.**Use sensory data, environmental mapping, and decision-making processes for dynamic autonomous systems.

## The benefits of compound AI systems

Some tasks are impossible to perform without using compound systems, while others benefit from their inherent modularity, leading to improved performance, flexibility, and lowered costs.

### Performance benefits

Compound AI systems can perform more complicated tasks than single models, no matter how they’re trained.

Even the largest and most capable models can be improved by combining them with different techniques. Take Mixture of Experts (MoE), for example: by combining different models—each an “expert” in a specific task—it can leverage the strengths of each one, becoming more adaptable to different tasks and achieving higher overall performance.

By using a modularized workflow, we can also allocate different hardware for each step to improve resource usage. For example, for speech-to-text, we can dedicate CPUs for audio chunking and GPUs for the actual transcription, preventing CPU-bound operations from blocking the GPUs.

![A diagram of a compound AI system with specific resource allocation (GPU vs. CPU) per node.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1722960266-untitled-7.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A compound AI pipeline with modularized, custom hardware. Only the AI models use GPUs.

A compound AI pipeline with modularized, custom hardware. Only the AI models use GPUs.### Increased flexibility

Compound AI systems can adapt to a broader range of tasks and scenarios than single models. As a task's complexity increases, additional models or techniques can be added without overhauling the entire system.

Their modular nature also enables developers to iterate on a compound system’s design more easily. In theory, individual components can be improved or swapped out for more performant (or equally performant but cheaper) technology while leaving the rest of the system intact (in practice, this requires that [the infrastructure you’re building with](https://www.baseten.co/blog/introducing-baseten-chains/) is flexible enough to support this). 

Finally, modularizing an AI system is like modularizing your code: by defining components with single, well-defined tasks, you can reuse them in different pipelines. This is more effective than coding up one monolith from scratch each time you set out to build something, and is a more sustainable strategy for companies building multiple AI solutions.

### Cost efficiency 

Their modularity also makes compound systems more adaptable to cost-effective design options. For instance, instead of using or training one massive but expensive model, you can integrate a smaller model with other tools (like using a smaller, carefully-tuned LLM paired with search heuristics instead of one massive LLM). You can also swap out individual models or tools for cheaper ones as they become available.

Utilizing task-specific hardware can also make the entire workflow more cost-efficient. We want to spare an expensive GPU node any work that can be done on a cheaper CPU node, and parallelizing tasks across different nodes can improve GPU utilization.

## Challenges of implementing compound AI systems

Developing compound AI systems requires focusing on both the individual components in a pipeline and the overall workflow they create. Challenges can be divided into three groups: those related to building, optimizing, and serving compound AI systems in production.

### Building compound AI systems

For compound systems, coordination logic must be implemented to facilitate the data flow between different models and processing steps. Building robust metrics and logging for debugging and analyzing complex systems is also key.

Building all of this yourself is no small feat. At Baseten, [we built a solution for this](https://www.baseten.co/blog/baseten-chains-explained/) exactly so you don’t have to.

### Optimizing compound AI systems

Developers used to think only in terms of single models. With compound systems, optimizing latency and performance metrics involves [I/O between multiple models, plus any additional processing steps](https://www.baseten.co/blog/baseten-chains-explained/).

Intra-cloud roundtrips for retrieving inference results from each model add extra latency, and monolithic servers under-utilize compute by forcing different processes to run on the same hardware. Sub-optimal configurations like these ultimately lead to inefficient pipelines in terms of latency, compute, and cost.

### Serving compound AI systems in production

Does the modularity of your production infrastructure reflect the modularity of your AI system?

Each step in your system [may require different software, hardware, and horizontal scaling](https://www.baseten.co/blog/baseten-chains-explained/). Building this yourself would require a serious investment in engineering hours that might otherwise be spent building your product and serving customers. Plus, you’ll have to fight to make the solution cost-efficient, fast, reliable, and sustainable. 

## Using compound AI systems in production

The ability to easily transition from prototype to production is essential for utilizing compound AI systems efficiently. AI builders should be able to leverage open-source models in their modular workflows, with easy orchestration between components, built-in observability, and a delightful developer experience.

That’s why we built [Chains](https://www.baseten.co/blog/introducing-baseten-chains/), an SDK and framework for building and orchestrating compound AI systems. Chains enables you to:

- Combine business logic with ML models.
- Customize hardware (GPUs and CPUs) and scaling for distinct processing steps.
- View critical performance metrics across your entire workflow, with local testing and debugging.

In our [Chains webinar](https://www.baseten.co/resources/webinar/multi-model-inference-with-baseten-chains/), our CTO and Co-Founder, Amir Haghighat, explains how Chains solves multiple challenges in doing inference for compound AI systems.

![A clip from our webinar on Chains, an SDK and workflow for compound AI systems.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fnlilu4x3yIOmQMZnRn3AUB94Zd00iHUwc%2Fthumbnail.jpg&w=3840&q=75)

Chains are composed of “Chainlets,” modular services that can be linked together to form a full workflow (your “Chain”). Developers can tailor each Chainlet to their needs, from specifying compute hardware to customizing software dependencies. This flexibility ensures you can seamlessly integrate new models or functions into existing Chains, or adapt them for novel AI workflows.

![GPU Resourcing in Baseten Chains](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1719454284-chains-deployments.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) An example Chain viewed from our UI showing custom hardware and some metrics per Chainlet.

An example Chain viewed from our UI showing custom hardware and some metrics per Chainlet.For more information on Chains, check out our [launch post](https://www.baseten.co/blog/introducing-baseten-chains/), [on-demand webinar](https://www.baseten.co/resources/webinar/multi-model-inference-with-baseten-chains/), or [technical deep dive](https://www.baseten.co/blog/baseten-chains-explained/). If you’re building a product or solution using compound AI, we’d love to help you make your system performant, secure, and reliable—[reach out](https://www.baseten.co/talk-to-us/?ref=/)!
