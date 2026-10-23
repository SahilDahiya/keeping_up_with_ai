---
title: 'NVIDIA Nemotron 3 Ultra: Deploy and Fine-Tune Day Zero | Fireworks'
kind: blog
topic: models
subtopic: architectures
secondary_topics: []
summary: Details Nemotron 3 Ultra's 550B/55B-active hybrid Transformer-Mamba MoE architecture
  for long-running autonomous agents, reporting NVIDIA's claimed 5x faster inference
  and 30% lower cost on agentic tasks versus comparable open models.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/nvidia-nemotron-3-ultra
author: null
published: '2026-06-04'
fetched: '2026-10-23T06:12:28Z'
classifier: claude
taxonomy_rev: 2
words: 532
content_sha256: 59eccd3f4df60c3a6dad2f481b057613fa2cbe3197d4be5aa355f9f7ddbd542d
---

# NVIDIA Nemotron 3 Ultra: Deploy and Fine-Tune Day Zero | Fireworks

Agents don’t solve single prompts. They execute long-running tasks: planning, calling tools, spawning sub-agents, evaluating intermediate results, correcting mistakes, and iterating across hundreds of steps before producing something useful.

Every step consumes time and compute. As a result, the relevant unit of measurement is no longer the cost of a response, but the cost of completing a task. The question is no longer just how a model ranks on a benchmark, but how much it costs and how long it takes to get the job done.

That is what NVIDIA built [Nemotron 3 Ultra](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/) to optimize for.

It is an open model for frontier reasoning and orchestration in long-running autonomous agents, designed for use cases such as coding agents, deep research, and complex enterprise workflows. 550B total parameters with 55B active, a hybrid Transformer-Mamba MoE architecture, and up to 1M context. NVIDIA reports 5x faster inference and up to 30% lower cost for agentic tasks versus other open models in its class.

And starting today, Nemotron 3 Ultra is [available on Fireworks](https://fireworks.ai/models/fireworks/nemotron-3-ultra-bf16) with day-zero support, ready to deploy on dedicated GPUs through [on-demand deployments](https://docs.fireworks.ai/guides/ondemand-deployments).

### Why run it on Fireworks

We build the best-performing inference platform, running on the latest NVIDIA GPUs including B300 and B200. On top of the hardware, our proprietary optimizations like our FireAttention custom kernels deliver up to 4x higher throughput while fully preserving model quality. For a family of models whose entire point is fast, efficient task completion across long agent runs, that’s the environment you want them in.

Day-zero support means you don’t wait. Nemotron 3 Ultra is deployable on Fireworks the moment it launches.

“Factory enables enterprises to build and operate an autonomous Software Factory, orchestrating software development from planning to production across large codebases. Factory is model-agnostic, and Fireworks provides rapid access to frontier open models like Nemotron 3 Ultra, enabling us to quickly bring the latest AI capabilities to enterprise software development.”

Eno Reyes, CTO & Co-Founder at[Factory AI](https://factory.ai/)

### Train and deploy on the same platform

Nemotron 3 Ultra isn’t just available for inference on Fireworks. It’s also ready for post-training using the same platform and serving stack.

Teams can customize Nemotron 3 Ultra with supervised fine-tuning (SFT) and direct preference optimization (DPO) using either LoRA or full-parameter training, depending on their performance and deployment requirements.

Because training and inference run on the same platform, there are no handoffs between systems, no model repackaging, and no uncertainty about how a checkpoint will behave in production. The model you train is served on the same infrastructure, using the same optimized kernels and deployment stack.

Whether you’re adapting Nemotron 3 Ultra for enterprise workflows, coding agents, or domain-specific reasoning, you can move from training to production easily on Fireworks.

### Deploy in one command

On-demand deployments give you dedicated GPUs: lower latency, no hard rate limits, and predictable performance unaffected by other users. You’re billed by GPU-second, so it’s cost-effective under real load.

Deploy Nemotron 3 Ultra on Fireworks today with a single command. We’re excited to work with NVIDIA to make these breakthrough models available to developers worldwide.

Questions? Join our [Discord](https://discord.gg/fireworks-ai) or [contact us](https://fireworks.ai/contact) to schedule a meeting with our solutions team.
