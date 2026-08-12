---
title: Fireworks Now Supports NVIDIA NIM Deployments for Blazing AI Inference
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/nvidia-nim-on-fireworks
author: null
published: '2025-03-18'
fetched: '2026-08-12T06:28:31Z'
classifier: null
taxonomy_rev: 2
words: 831
content_sha256: 72b8542e1f36b3375675d5b3c6b8b4534147c405bba97aff8688de47c1f4e225
---

# Fireworks Now Supports NVIDIA NIM Deployments for Blazing AI Inference

Today, we’re pleased to announce that Fireworks supports [NVIDIA NIM](https://developer.nvidia.com/nim) microservices, part of the [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/) software platform, making it faster and easier for enterprises to deploy AI models on Fireworks and innovate on their product experiences.

Fireworks offers industry-leading speed, customization and cost efficiency for leading open source AI models like DeepSeek and Llama. NVIDIA NIM microservices offer a wide range of AI models for a range of modalities including embeddings, video, 3D and more.

With today's announcement, you can load the NVIDIA NIM models, including the latest NVIDIA Llama Nemotron Reasoning models, on the Fireworks platform. Or you could run [DeepSeek R1](https://fireworks.ai/models/fireworks/deepseek-r1) or Llama 405B models on Fireworks to take full advantage of Fireworks' optimizations and platform offerings, while also running NeMo Guardrails NemoGuard models on Fireworks via NVIDIA NIM.

Together, this allows enterprises to build innovative AI experiences with:

- •**Blazing-fast inference** processing that responds in milliseconds, not seconds
- •**Seamless model customization options** tailored to your specific requirements
- •**Crystal-clear pricing** structure with no hidden costs or surprises
- •**Enterprise-grade performance** that scales with your business demands
- •**Rock-solid privacy protection** built into every layer of our infrastructure

Today's AI landscape demands tailored solutions, not generic approaches. Fireworks has always provided access to premium models across critical domains, and now with NVIDIA NIM integration, we're taking capabilities to new heights.

Our comprehensive ecosystem now offers:

- •**Text Generation** – Access industry-leading models like Llama, Mistral, DeepSeek, and the Nemotron family for creating engaging chatbots, compelling content, and powerful automation workflows.
- •**Image & Vision** – Leverage cutting-edge solutions including Stable Diffusion, SSD, OpenUSD, and NV-CLIP for everything from creative design to medical imaging, 3D simulations, and advanced vision-language understanding.
- •**Embeddings & Search** – Transform unstructured data into actionable insights with NV-EmbedQA and NV-RerankQA, and other advanced models that enhance search capabilities and knowledge retrieval.
- •**Audio Processing** – Enable high-accuracy transcription and voice recognition with Whisper AI and specialized audio processing capabilities across diverse applications.

With Fireworks and NVIDIA NIM, you get a unified ecosystem of models and architectures, optimized for seamless multi-model workflows. Whether running foundation models for core processing or specialized models for targeted tasks, this integration ensures maximum efficiency without added complexity. Here’s how it works:

**Deploy NIM Models Directly on Fireworks** – Access both Fireworks' optimized models and NVIDIA NIM specialized capabilities through a single intuitive interface. Behind the scenes, each NIM model is packaged as an optimized container that we deploy directly within our GPU clusters. This containerized approach means the models run locally on our infrastructure—not as API calls to external services—ensuring maximum performance and data privacy while eliminating network latency.

**Supercharge Your Workflows with Compound AI** – With NIM containers seamlessly deployed alongside our existing models, you can leverage Fireworks' innovative Compound AI capabilities to orchestrate complex, multi-step AI processes exactly as you need them. Chain these models together with other specialized models for sophisticated reasoning, dynamic content generation, and in-depth data analysis.

The result is a frictionless experience that focuses on solving problems, not managing infrastructure—with instant access to innovations, one-click deployment, optimized performance, and flexible workflows. Together, Fireworks and NVIDIA NIM deliver a complete solution that makes advanced AI truly accessible, affordable, and immediately actionable for your business.

Drug discovery could soon be dramatically accelerated through the combined capabilities of Fireworks and NVIDIA NIM. By bringing together Fireworks' Compound AI framework with specialized [NVIDIA BioNeMo](https://www.nvidia.com/en-us/clara/biopharma/) NIM microservices, the process of creating and evaluating new molecular compounds could become significantly faster and more precise.

This compound system architecture orchestrates four specialized AI modules:

- •**Protein Structure Analysis** – the BioNeMo AlphaFold2 NIM functions as a predictive agent, generating high-fidelity 3D protein conformations with sub-1.5Å accuracy. These structural predictions establish the foundation for rational drug design by identifying potential binding sites.
- •**Molecular Design Engine** – Fireworks deploys generative models including Mistral for SMILES string generation and the MolMIM NIM microservice for 3D conformation prediction, creating novel compounds optimized for target-specific parameters while maintaining synthetic feasibility.
- •**Similarity-Based Screening** – NVIDIA NIM NV-EmbedQA creates vector representations of molecular fingerprints, enabling rapid comparison across vast compound libraries and prioritizing candidates based on similarity to known active molecules.
- •**Binding Validation System** – the DiffDock NIM microservice employs diffusion processes to simulate protein-ligand interactions without requiring prior binding site information, generating quantitative binding metrics with confidence scores.

Fireworks’ optimized function calling models like Llama 3.1 70B can serve as the orchestration layer, coordinating the execution sequence and data flow between these specialized components. This compound approach delivers dramatic improvements in throughput, computational efficiency, and discovery success rates compared to traditional approaches.

The integration of Fireworks and NVIDIA NIM demonstrates how leveraging specialized, orchestrated AI models can revolutionize complex workflows. By enabling precise, multi-step processes tailored to specific needs, this approach delivers faster results, enhanced efficiency, and scalable solutions. With dedicated hosted NVIDIA NIM endpoints available at build.nvidia.com, businesses can seamlessly adopt this cutting-edge technology to drive AI-driven innovation across industries.
