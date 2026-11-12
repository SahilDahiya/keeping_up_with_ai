---
title: Understanding NVIDIA’s Datacenter GPU line
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/understanding-nvidias-datacenter-gpu-line
author: Philip Kiely
published: '2023-05-23'
fetched: '2026-11-12T06:11:16Z'
classifier: null
taxonomy_rev: 2
words: 727
content_sha256: a821e744a57421a48b9ad324eb7bfb84856c75ad1146ee2ea7b2d7253a66be3b
---

# Understanding NVIDIA’s Datacenter GPU line

Infrastructure
# Understanding NVIDIA’s Datacenter GPU line

This guide helps you navigate NVIDIA’s datacenter GPU lineup and map it to your model serving needs.


- Authors
- Date
- May 23, 2023

TLDR

NVIDIA has dozens of GPUs that can serve ML models of different sizes. But understanding the performance and cost of these different cards, not to mention just keeping the names straight, is a challenge. Each GPU’s name, an alphanumeric identifier, communicates information about its architecture and specs. This guide helps you navigate NVIDIA’s datacenter GPU lineup and map it to your model serving needs.

Everyone wants powerful, cost-effective hardware for running generative AI workloads and ML model inference. But picking a datacenter GPU isn’t as simple as walking into an Apple store and picking out a new laptop, where there are only a few options and a clear upgrade path. It’s more like buying a car, where your budget and use case guide your decision among a range of models and model years with differing capabilities, prices, and availabilities.

This piece first guides you through deciphering the naming scheme for NVIDIA’s datacenter GPUs to identify a card’s architecture and tier. Then, it provides methods for clear and direct comparisons of different GPUs along with a table of key specs for several cards that are popular for model training, fine-tuning, and serving.

Datacenter GPUs can have pretty arcane names: K80, T4, A100, L40. But these aren’t just random collections of letters and numbers. They encode important information about the GPU’s specs and performance.

The letter in a GPU name refers to the architecture of that GPU. Every couple of years, NVIDIA releases a new microarchitecture for GPUs across both consumer and datacenter products. New microarchitectures improve performance and power efficiency with updated instruction sets and often take advantage of smaller process nodes to pack more transistors onto each chip. Each new microarchitecture means a faster, better optimized GPU.

In a GPU’s name, the letter is the first letter of the architecture name. For example, A stands for Ampere and L stands for Lovelace. NVIDIA GPU architectures are named for famous scientists.

For each architecture, NVIDIA makes several GPUs with different price, performance, and power use targets. The larger the number, the more powerful and expensive the GPU.

Different tiers of GPUs are optimized for different compute workloads. Tiers from recent generations include:

- **4**: The smallest GPU of a generation, 4-tier cards have low energy consumption and are best for cost-effective invocation of moderately-sized models.
- **10:** A mid-range GPU optimized for AI inference.
- **40:** A high-end GPU best suited for virtual workstations, graphics, and rendering.
- **100:** The largest, most expensive, most powerful GPU of a generation. It has the highest core count and most VRAM and is designed for inference on large models as well as training and fine-tuning new models.

With these two factors, we can use the letter and number combination in a GPU name to infer some facts about the card.

*Example: What’s the difference between a T4 and an L4?*

The L4 is a next-gen replacement for the T4. The L4 uses the Lovelace architecture and was released in 2023, while the T4 uses Turing architecture and was released in 2018. The cards are of the same tier—they use a similar amount of power and are designed for similar use cases—but the newer L4 has more and more powerful cores and 24 GB of VRAM as opposed to the T4’s 16 GB.

*Example: What’s the difference between an A10 and an A100*

The A100 is a bigger, more powerful, more expensive version of the A10. Both cards have the same architecture, but the A100 has substantially more cores and VRAM and draws more power, so it can run larger models and run them faster.

*Example: How do you compare a K80 and a T4?*

Comparison between any two cards of different architectures and different tiers is complicated. The K80 uses the now decade-old Kepler architecture, while the T4 is on the more modern Turing architecture. So for many ML tasks, the T4 is cheaper per minute to run (due to its lower power consumption) while also substantially faster than the K80 thanks to its more powerful cores.

*Example: What models can you serve on a T4 vs an A10?*

For a detailed breakdown, check out [this comparison piece](https://www.baseten.co/blog/comparing-nvidia-gpus-for-ai-t4-vs-a10/).
