---
title: Baseten joins the NVIDIA Nemotron Coalition to advance custom AI in production
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-joins-the-nvidia-nemotron-coalition-to-advance-custom-ai-in-production
author: Charles O'Neill
published: '2026-11-05'
fetched: '2026-11-12T06:07:08Z'
classifier: null
taxonomy_rev: 2
words: 834
content_sha256: f885f5e87a095f53dfa703772069ab29a943c6a9e03f0619923b89dc3ceba713
---

# Baseten joins the NVIDIA Nemotron Coalition to advance custom AI in production

News
# Baseten joins the NVIDIA Nemotron Coalition to advance custom AI in production

We're expanding our NVIDIA collaboration to help enterprises customize, deploy, and scale open models for production AI.


- Authors
- Date
- November 5, 2026

Baseten has joined the [NVIDIA Nemotron Coalition](https://nvidianews.nvidia.com/news/nvidia-launches-nemotron-coalition-of-leading-global-ai-labs-to-advance-open-frontier-models), expanding our collaboration with NVIDIA to advance open frontier models and accelerate enterprise AI adoption.

Together, we are helping enterprises move beyond general-purpose AI to models customized for their specific business needs. Our collaboration spans day-zero model launches, reinforcement learning (RL) environments, post-training expertise and infrastructure, and high-performance dedicated inference. By connecting model development with real-world production environments, we aim to improve model quality, cost efficiency, and deployment flexibility.

Through the coalition, Baseten will contribute insights from enterprise workloads and expertise in post-training and inference to help advance [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/), NVIDIA’s family of open models, and the broader open-source ecosystem.

Our collaboration already spans several Nemotron releases. Baseten was a day-zero launch partner for [Nemotron Super 3.5 VL](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/) and Nemotron 3 Ultra. We also support customers such as [Harvey](https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence), a leading legal AI platform, and [CodeRabbit](https://www.coderabbit.ai/blog/teaching-nvidia-nemotron-3-5-lightning-to-route-code-reviews), an AI-powered code review platform, with early model access, customization, and deployment on Baseten.

Enterprise AI demands more than strong performance on general benchmarks. Models must reliably follow complex instructions, reason across multiple steps, use tools efficiently, and operate within domain-specific requirements.

Instruction following emerged as an important opportunity for Nemotron. Real-world applications come with detailed instructions in system prompts and tool definitions, and follow-ups embedded in user messages, tool responses, and error messages.

To address these challenges, Baseten developed RL environments that targeted this directly, teaching the model to follow complex instruction hierarchies, ignore extraneous information, and adhere to detailed style preferences.

We also built environments for long-horizon reasoning and planning, including statistical analysis of complex biological datasets, mathematical theorem proving, and competitive game playing. They are designed to challenge state-of-the-art models through their inherent structure rather than artificial complexity.

Our work extends to multimodal reasoning. Building on our research into [training vision adapters for frontier models](https://arxiv.org/abs/2610.05897), we built visual and spatial reasoning tasks, including multi-turn tool-calling scenarios requiring real visual understanding.

We [trained vision adapters](https://arxiv.org/html/2610.05897v1) for Nemotron 3 Ultra, [GLM-5.2](https://www.baseten.co/library/glm-52/), and [GLM-5.3](https://www.baseten.co/library/glm-53/). Post-training in these environments led to significant improvements on [MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro), a benchmark evaluating expert-level multimodal reasoning.

At Baseten, we help enterprises transform open models into AI applications that meet their specific requirements for quality, performance, and cost.

By combining model [training](https://www.baseten.co/products/training/), the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/), and hands-on engineering expertise, we enable teams to improve task-specific accuracy while optimizing inference latency and cost.

Open models give enterprises greater control over their AI improvements. Organizations can train on proprietary data, evaluate against business-specific requirements, retain ownership of model improvements, and choose how and where to deploy.

Our collaboration with NVIDIA helps bring these capabilities together, connecting Nemotron’s open model foundation with the tools, infrastructure, and expertise to operate custom AI in production.

CodeRabbit demonstrates how targeted post-training can translate into measurable production benefits.

Working with NVIDIA and Baseten, CodeRabbit customized Nemotron 3.5 Lightning for code review routing using [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) tools for supervised fine-tuning and RL on [Baseten Training](https://docs.baseten.co/training).

In a fixed evaluation of 1,000 tasks, agreement with CodeRabbit’s routing policy increased from 75.8% to 80.7%. CodeRabbit also achieved 50.4% lower inference cost at saturated throughput.

These results illustrate the value of combining open-model customization with optimized inference, improving performance on a specialized task while reducing the cost of serving the model at scale.

Harvey, a leading legal AI platform, post-trains NVIDIA Nemotron on Baseten to support specialized legal AI workflows serving tens of thousands of lawyers daily.

This work illustrates how open-model customization can help address domain-specific enterprise requirements.

Our engineering collaboration with NVIDIA also extends to voice AI, where model accuracy, responsiveness, and inference efficiency are essential for real-time applications.

Our teams are working together on Nemotron-powered voice agents, evaluating model quality and responsiveness across a complete application.

Baseten also supports [Nemotron 3.5 ASR Streaming](https://www.baseten.co/library/nvidia-nemotron-35-asr-multilingual) for real-time speech recognition. In our [published benchmark](https://www.baseten.co/blog/introducing-nvidia-nemotron-35-asr-streaming/), a single [NVIDIA Hopper GPU](https://www.nvidia.com/en-us/data-center/h100/) sustained up to 100 concurrent real-time audio streams over WebSocket.

This work helps enterprises build responsive voice applications while maintaining control over inference performance and operating costs.

We are continuing to expand how customers customize, evaluate, and deploy Nemotron models on Baseten.

[Baseten Loops](https://docs.baseten.co/loops/overview) connects managed RL workflows with deployment to Dedicated Inference, helping teams move from model improvement to production serving within a unified platform. Customers retain ownership of their trained model weights, giving them flexibility to build on their domain expertise and continue improving their models over time.

Baseten Loops supports Nemotron 3.5 Super VL and Nemotron 3 Ultra. Nemotron 3.5 Super VL is available with both BF16 and NVFP4 training.

Through the NVIDIA Nemotron Coalition, we look forward to deepening our collaboration across model development, post-training, and inference to help enterprises turn the flexibility of open models into measurable business value.

Ready to build with Nemotron? Deploy from our [Model Library](https://www.baseten.co/library/nemotron-35-super-vl) or start [post-training on Loops](https://app.baseten.co/explore?availability=Loops) today.
