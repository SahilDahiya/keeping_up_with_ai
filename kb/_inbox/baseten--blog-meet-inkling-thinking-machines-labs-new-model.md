---
title: 'Meet Inkling: Thinking Machines Lab''s new customizable model'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/meet-inkling-thinking-machines-labs-new-model
author: Albert Lee
published: '2026-07-15'
fetched: '2026-11-12T06:07:56Z'
classifier: null
taxonomy_rev: 2
words: 797
content_sha256: 5b7e52db695fd54ea591e755e0c60fd48ef13ecf0d4b26109ecbbb2303922c85
---

# Meet Inkling: Thinking Machines Lab's new customizable model

AI models
# Meet Inkling: Thinking Machines Lab's new customizable model

Thinking Machines Lab's newest model, Inkling, is available day 0 on Baseten.


- Authors
- Date
- July 15, 2026

TLDR

Inkling is Thinking Machines Lab’s new 975B-parameter open-weight model. It reasons natively over text, images, and audio, and balances cost against performance with variable and efficient thinking effort. We are excited to support Inkling day 0 on the Baseten Platform through Baseten Model APIs and Dedicated Inference.

Today, we’re proud to support Thinking Machines Lab by bringing **Inkling**, its newest open-weight model, to the Baseten Platform with day 0 support.

Thinking Machines Lab’s mission is to build AI that extends human will and judgment.


Thinking Machines Lab chose the name *Inkling* to evoke an idea in its earliest stage, with the potential to grow into something greater. Inkling is built as an extremely knowledgeable, generalist base that can be extended via fine-tuning. Here’s a closer look at its capabilities, technical architecture, and why we’re so excited about it.

You can start using Inkling now on [Baseten Model APIs](https://www.baseten.co/library/inkling/), or reach out about getting a [Dedicated Inference](https://www.baseten.co/talk-to-us/?Inkling) deployment. Shout out to the Inferact team for their work supporting Inkling in vLLM and for their tremendous partnership, which enabled us to provide day-0 support for Inkling with vLLM and the Baseten Inference Stack! We’re continuing to optimize the model, and many performance optimizations are on their way.

Inkling is a general-purpose, multimodal, autoregressive transformer model that accepts text, image, and audio inputs and generates text outputs (it was pre-trained on 45 trillion tokens of text, images, audio, and video). Inkling has a mixture-of-experts (MoE) architecture with 975B total parameters, 41B active and a 1 million token context window.

Inkling is the first in a new family of models, and because Thinking Machines Lab wants to make customization accessible for more use cases, they are releasing the full weights today and making the model available for fine-tuning on [Tinker](https://thinkingmachines.ai/tinker/) as well.

Inkling is purpose-built for developers building AI-powered applications: agentic and tool-use systems, coding assistants, chatbots, and retrieval-augmented generation systems. You can try it now on our Model APIs.

Inkling is a 66-layer, sparse mixture-of-experts transformer with 975 billion total parameters, 41 billion active parameters, and up to a 1M token context window.

Rather than activate the entire model for every token, Inkling routes each token through six of its 256 specialized experts, along with two shared experts. In practical terms, Inkling can draw on a broad set of capabilities without activating all 975 billion parameters for every token.

Thinking Machines Lab’s evaluations show how that breadth translates into performance across reasoning, coding, vision, audio, and safety:

| Category | Benchmark | What it measures | Inkling score | 
|---|---|---|---|
| Reasoning | GPQA Diamond | Graduate-level scientific reasoning | 87.9% | 
| Coding | SWE-bench Verified | Resolving real software issues | 77.6% | 
| Math | AIME 2026 | Competition mathematics | 97.1% | 
| Vision | MMMU Pro | Multidisciplinary visual reasoning | 73.3% | 
| Audio | VoiceBench | Spoken-language understanding | 91.4% | 
| Safety | StrongReject | Resistance to harmful requests | 99.1% | 

*Higher is better. Scores use different metrics and are not directly comparable across benchmarks. Source: Thinking Machines Lab, Inkling model card, July 2026.*

Open weights give you more control over how you customize and deploy Inkling. But that flexibility comes with a substantial infrastructure footprint: the BF16 checkpoint requires at least 2 TB of aggregate GPU memory, while the NVFP4 checkpoint lowers that requirement to at least 600 GB. Putting a 975-billion-parameter model into production is no small task.

Baseten handles the infrastructure required to deploy Inkling, adapt to changing traffic, and keep the model available as capacity shifts across clouds. The [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) provides the autoscaling, weight distribution, and cross-cloud capacity needed to serve a model of this size, natively on day 0.

Scale with demand: Baseten’s autoscaler adds or removes model replicas as demand changes. The [Baseten Delivery Network](https://www.baseten.co/blog/baseten-delivery-network-fast-cold-starts-big-models/) keeps model weights close to available compute and coordinates downloads when many replicas start simultaneously. BDN delivers 2–3× faster cold starts, helping new Inkling replicas come online quickly as usage grows.

Stay available across clouds: [Multi-cloud Capacity Management](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/) brings GPUs across more than 20 clouds into one global pool. If capacity becomes constrained or unavailable in one cloud, Baseten can place the workload in another.

You can use Inkling today through [Baseten Model APIs](https://www.baseten.co/library/inkling/) and [Dedicated Inference](https://www.baseten.co/library/inkling/).

With open weights and the ability to reason across text, images, and audio, Inkling gives you room to explore a wide range of ideas. We have an *inkling* that many of its most compelling uses have yet to be imagined, and we can’t wait to see what you build.
