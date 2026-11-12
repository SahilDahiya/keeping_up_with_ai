---
title: Private, secure DeepSeek-R1 in production in US & EU data centers
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/security
summary: Lays out dedicated and self-hosted VPC deployment options for DeepSeek-R1/V3
  in US and EU data centers as an alternative to shared third-party endpoints, for
  teams that need data residency and security guarantees DeepSeek's own API can't
  provide.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/private-secure-deepseek-r1-in-production-in-us-eu-data-centers
author: Yineng Zhang
published: '2025-01-28'
fetched: '2026-11-12T06:09:38Z'
classifier: claude
taxonomy_rev: 2
words: 1199
content_sha256: 63f56e36aea0839cbd612b42cf16aa7f901ae4ed4879451d9b2b443d5b6b8100
---

# Private, secure DeepSeek-R1 in production in US & EU data centers

AI engineering
# Private, secure DeepSeek-R1 in production in US & EU data centers

Dedicated deployments of DeepSeek-R1 and DeepSeek-V3 offer private, secure, high-performance inference that's cheaper than OpenAI


- Authors
- Date
- January 28, 2025

DeepSeek-R1 and DeepSeek-V3 launched within weeks of each other, challenging the assumption that training massive closed-source models like GPT-4o and o1 is a sustainable moat. The sudden advent of open-source models with strong benchmarks compared to OpenAI’s latest offerings signals a future where every business can have its own high-performance foundation models.

In a world where foundation models are commodities, not proprietary advantages, the challenge shifts from training to deploying these models reliably and cost-effectively. Executives and founders have three options for how they’ll respond to this shift:

1. Stay the course on OpenAI/Anthropic and wait for access to the latest models while dealing with rate limits, reliability issues, and high per-token costs.
2. Switch to DeepSeek on a shared API endpoint, putting user data, privacy, and security at risk.
3. Run DeepSeek-R1 on a dedicated deployment – after figuring out the infrastructure for fast, reliable, and cost-efficient inference.

Options 1 and 2 are non-starters. DeepSeek could be the catalyst for a 10x acceleration of AI products going into production, making applications built on today’s closed models economically unviable. But a shared DeepSeek endpoint brings massive security and compliance risks that no business can accept.

That leaves the third option – dedicated deployments of models like DeepSeek-R1 – as the only viable option. But this requires a major engineering effort to build internally.

Fortunately, there’s another way to get private, secure, production-ready access to DeepSeek-R1. At Baseten, we were the first US-based platform to offer dedicated and self-hosted deployments for the DeepSeek-V3 model – a technical accomplishment that was featured in the [Latent Space podcast](https://www.latent.space/p/baseten) and [The New York Times](https://www.nytimes.com/2025/01/23/technology/deepseek-china-ai-chips.html) – and we offer secure, high-throughput deployments for any DeepSeek model with the option to self-host in your own VPC.

In the last month, DeepSeek has announced three important advancements:

- [DeepSeek-R1](https://www.baseten.co/library/deepseek-r1/) is the headline reasoning model that matches OpenAI’s o1 model
- DeepSeek-V3 is a traditional LLM that contends with GPT-4o and Sonnet 3.5
- [DeepSeek-R1 distills](https://www.baseten.co/library/family/deepseek/) bring the reasoning capabilities of the main R1 model down to the efficient footprint of leading open models like Qwen 7B, Qwen 32B, and Llama 70B.

This isn’t over. New models with new capabilities like vision are being released constantly, both from DeepSeek themselves and from the open-source community as they build on these foundation models.

Despite their advantages, DeepSeek models aren't plug-and-play. Companies looking to deploy DeepSeek-R1 in their own VPC face a new set of infrastructure and performance challenges.

DeepSeek-R1 and DeepSeek-V3 each have 671 billion parameters. In FP8, each parameter requires 1 GB of VRAM to load, and you want to reserve a substantial amount of GPU memory for the KV cache.

While DeepSeek-R1 can run efficiently on a full node of eight NVIDIA H200 GPUs with a combined 1,128 GB of VRAM, H100 GPUs are far more plentiful. However, a full node of H100 GPUs only has 640 GB of VRAM, which isn’t even enough to load model weights.

If you’re limited to H100 GPUs, you need multi-node inference to run DeepSeek-R1. Splitting an LLM across multiple nodes is a complicated model performance and infrastructure challenge that requires sophisticated compute orchestration and the latest performance tooling.

Once you can run DeepSeek-R1, you’ll need to replicate that setup across clusters, regions, and VPCs to secure compute capacity, ensure worldwide availability, and comply with regional regulations around data residency. Building and maintaining this infrastructure compounds the challenges of serving large models.

[H200 GPUs](https://www.baseten.co/blog/evaluating-nvidia-h200-gpus-for-llm-inference/) are scarce, and while H100 GPUs are becoming increasingly available on the market, you need twice as many of them per instance of a DeepSeek model. With limited on-demand availability, scaling to match demand can be difficult and expensive.

DeepSeek-R1 and DeepSeek-V3 are newer models, so the industry’s performance tooling doesn’t offer the same robust support as established LLM families like Llama and Qwen enjoy. While this is changing quickly, you don’t want to depend on a public release cadence to get model optimizations.

Baseten is uniquely positioned to help companies take advantage of DeepSeek without the typical roadblocks. Our engineering team has worked closely with DeepSeek and is ready to help you move quickly from testing to production, accelerating your time to market.

On Baseten’s multi-cloud infrastructure, we provide the specialized hardware like H200 GPUs needed to operate DeepSeek at scale. We also support high-performance multi-node inference, which expands DeepSeek access to regions where you can get H100 GPUs but not the scarcer H200 GPUs.

With Baseten, you get the security and efficiency of a dedicated deployment along with our unmatched uptime and reliability. Unlike shared inference endpoints, dedicated deployments are suitable for mission-critical production workloads, even in regulated industries.

We can also help you run DeepSeek on your own infrastructure with no shared resources and no data leakage. Baseten supports both [self-hosted](https://www.baseten.co/deployments/baseten-self-hosted/) and [hybrid](https://www.baseten.co/deployments/baseten-hybrid/) model deployments, where models are deployed directly into your VPC on any cloud provider.

Running a frontier model in your own VPC is a game-changer for what enterprises can build with AI, accelerating the transition to AI-native products.

Running large models like DeepSeek-R1 with low latency and high throughput is a unique model performance challenge. Baseten natively supports multiple options for fast inference frameworks, including SGLang and TensorRT-LLM.

With custom optimizations on top of these frameworks, Baseten offers best-in-class performance for DeepSeek models despite limited publicly-available tooling. As new performance improvements are released, Baseten’s model performance engineers integrate these enhancements into the platform, further improving performance.

Our optimized inference engines make running DeepSeek models cheaper and faster than relying on OpenAI’s hosted models.

For more cost-sensitive reasoning workloads, distilled models based on DeepSeek-R1 offer up to 32x lower costs. These models apply the same R1-style reasoning to leading open LLMs with smaller footprints, including Qwen 7B, Qwen 32B, and Llama 70B. The larger distilled models rival OpenAI’s o1-mini on benchmark performance.

While no company wants to risk its users' data, industries like financial services and healthcare are subject to strict regulations around how and where they store and process data. With DeepSeek models and Baseten, every company can offer their users secure, private, compliant access to cutting-edge intelligence.

Baseten is HIPAA compliant and SOC 2 type II certified for both Baseten-hosted and self-hosted deployments, and our region-locked deployments enable compliance with data residency laws and other local regulations worldwide.

DeepSeek-R1 is impressive as a point-in-time release, but more importantly it’s a preview of what’s coming. More companies will release models that match OpenAI and Anthropic in quality, which could push these incumbents to rethink their strategies. Enterprises now have a choice: rely on closed-source providers with high costs and data-sharing concerns, or take control of their own inference with solutions like Baseten.

The AI landscape has shifted, again. As model training becomes commoditized, the real challenge—and opportunity—lies in running these models efficiently. Baseten is leading the way, ensuring companies can deploy the best models on their terms.

Want to see DeepSeek-R1 in action? [Let’s talk](https://www.baseten.co/talk-to-us/deepseek/) about getting it running in your environment today.
