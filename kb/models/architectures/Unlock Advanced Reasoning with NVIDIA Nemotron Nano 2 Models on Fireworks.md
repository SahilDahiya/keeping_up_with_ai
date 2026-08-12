---
title: Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- inference/optimization
summary: NVIDIA Nemotron Nano 2 uses a hybrid Mamba-Transformer design where only
  ~8% of layers use quadratic-cost self-attention (placed where long-range links matter)
  and the rest use constant-cost Mamba-2/FFN blocks, giving transformer-level accuracy
  with much lower compute and stable memory for long-context reasoning.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/nvidia-nemotron-nano2
author: null
published: '2025-12-02'
fetched: '2026-08-12T06:28:30Z'
classifier: claude
taxonomy_rev: 2
words: 894
content_sha256: a711acf633d3a0e57352bf0f59a463968be4d23a1b616b98ab9f1438afbe0563
---

# Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks

We're excited to collaborate with NVIDIA to bring their groundbreaking **NVIDIA Nemotron Nano 2 9B** models to the Fireworks platform. NVIDIA Nemotron is a family of open models, datasets, and technologies that unlock developers to build highly efficient and accurate specialized agents. The Nemotron models are trained from scratch by NVIDIA, designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response. Nemotron Nano 2 is built on a hybrid Mamba-Transformer architecture that delivers expert-level reasoning with unprecedented efficiency.

Deploying Nemotron models on Fireworks can unlock more powerful use cases for developers. In scientific research, Nemotron models acts as the ideal lab partner that can easily process dense papers, explain complex concepts, and rapidly generate new hypotheses. For Search and Code Understanding, its comprehensive long-context up to 128K enables developers to digest larger code repositories or pull information from many different sources, all while maintaining context across different scenarios. Ultimately, from scientific research to automated agentic workflows, Nemotron delivers the high-level complex reasoning skills necessary to provide reliable, actionable decision support where simpler models often struggle.

Traditional Transformers face a fundamental bottleneck: self-attention scales quadratically with sequence length**.** What does this mean? Transformers models often hit a wall when dealing with longer documents or more complex large datasets. Self-Attention works by comparing every single word to every other word in the text. For example if a document is twice as long, the work doesn't just double—it quadruples. This concept is known as O(L²) scaling, and it quickly creates massive computing and memory bottlenecks for anything requiring truly long context.

NVIDIA's Nemotron models solve this challenge through an ingenious hybrid Mamba-Transformer design that provides a major leap in efficiency. The architecture rather than comparing every token, operates more like a selective human brain that’s focus is:

- •**Attention on demand:** Only a small fraction (around**8%** ) of the layers use the heavy-lifting self-attention mechanism, and they are positioned precisely where the model needs to link distant ideas.
- •**Speed and stability:** The majority of layers use efficient Mamba-2 and FFN blocks, which ensure that the computational work is constant for every token.

By blending these two approaches, Nemotron provides the necessary attention for accuracy while dramatically reducing computational overhead and ensuring stable, constant memory usage—a game-changer for long-context inference. This results in transformer-level accuracy with faster inference on long sequences, expert-level reasoning, and efficient scaling for production deployments.

Available in two sizes (**Nemotron-Nano-9B-v2** and **Nemotron-Nano-12B-v2**), both models combine breakthrough architecture with industry-leading performance on Fireworks infrastructure.

Developers can unlock significant advantages by migrating to NVIDIA Nemotron Nano models on Fireworks:

1. **Unlock expert level reasoning** capabilities with high efficiency and optimized accuracy, that can lead to reduced costs
2. **Go from experimentation to production quickly and seamlessly.** With Fireworks, you can effortlessly scale your production workloads globally, accessing cutting-edge hardware across 18+ regions and 8 providers without managing infrastructure. Optimize for superior speed, greater capacity, and reduced costs through on-demand GPUs, auto-scaling, and pay-per-second pricing.

Read more about the Nemotron architecture in [NVIDIA's Technical Whitepaper](https://arxiv.org/pdf/2504.03624).

**📓 Complete Example:** To accelerate your development, we have created an extensive cookbook for your end-to-end development: [here](https://github.com/fw-ai/cookbook/blob/main/experiments/nvidia_nemotron/NVIDIA_Nemotron_Fireworks_Benchmark.ipynb).

Below we have included some key snippets from the cookbook on how to get started.

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950

__Hardware Requirements__

NVIDIA-Nemotron-Nano-9B-v2 and NVIDIA-Nemotron-Nano-12B-v2 can both run on 1x H100 GPU with excellent performance.

To evaluate reasoning capabilities, we tested all models on a random sample from GPQA Diamond–a rigorous benchmark of 198 graduate-level questions in biology, physics, and chemistry.

**What is GPQA?**

GPQA is the Graduate-Level Google-Proof Q&A Benchmark, a challenging dataset of multiple-choice questions written by domain experts. According to the [original paper](https://arxiv.org/abs/2311.12022) researchers under the following categories are looking for different levels of accuracy

- PhD experts in their field: **65-74% accuracy**

- Baseline Highly Skilled Non-Experts with approximately 30 minutes to do a quick google search: **34% accuracy**

- GPT-4 (at publication): **39% accuracy**

- Random guessing: **25% accuracy**

**Our Results (50 questions):**

| Model | Accuracy | 
|---|---|
| NVIDIA-Nemotron-Nano-12B-v2 | 62% | 
| Qwen3 8B | 60% | 
| NVIDIA-Nemotron-Nano-9B-v2 | 56% | 
| Qwen3 14B | 56% | 
| Llama 3.1 8B | 24% | 

**Question Distribution**

The 50-question sample provided balanced coverage across scientific domains:

12345678910

This diverse distribution ensures the models are tested across the full spectrum of graduate-level scientific reasoning.

The GPQA performance benchmarks demonstrated the Nemotron Nano family is perfect for scientific research, complex agentic applications, and more. The Nemotron-Nano-12B-v2 model achieves an accuracy of 62%, placing its scientific reasoning capabilities firmly within the range of PhD-level experts. Even the highly efficient Nemotron-Nano-9B-v2 model delivers a powerful 56% accuracy, which significantly exceeds the GPT-4 baseline (39%). Another important metric is that both Nemotron models significantly surpass the GPQA baseline search metric of 34%.

We are excited to bring these powerful, efficient models from NVIDIA to everyone.

The Mamba-Transformer hybrid architecture of Nemotron Nano 2 delivers the best of both worlds: expert-level reasoning (62% on GPQA Diamond) combined with efficient inference.

Deploy Nemotron models on Fireworks today with a single command and experience the future of efficient AI. We're excited to work with NVIDIA to make these breakthrough models available to developers worldwide.

Visit fireworks.ai to get started.

Questions? Join our [Discord](https://discord.gg/fireworks) or contact [support@fireworks.ai](mailto:support@fireworks.ai)
