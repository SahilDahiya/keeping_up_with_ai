---
title: Fireworks Raises $52M Series B to Lead Industry Shift to Compound AI Systems
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/fireworks-ai-series-b-compound-ai
author: null
published: '2024-07-11'
fetched: '2026-08-12T06:29:53Z'
classifier: null
taxonomy_rev: 2
words: 1022
content_sha256: 29453a78a2b4f70777514f56ea39c4866ae7468663955cee99e55f1d1bcb5f18
---

# Fireworks Raises $52M Series B to Lead Industry Shift to Compound AI Systems

- •**Fireworks raises $52M led by Sequoia, boosting its valuation to $552M.** The funds will speed up the development of compound AI systems, team growth, and platform enhancements to increase AI adoption in production.
- •**Fireworks enhances its inference platform with the latest models, advanced customization, and improved production readiness.** These features make it easier and faster for businesses to customize models and build AI applications without needing a large team of ML engineers or data scientists.
- •**Fireworks partners with MongoDB, Meta, NVIDIA, AMD, and more.** These partnerships provide developers with fundamental building blocks, from SOTA models to vector databases, on a production-ready platform.
- •**Fireworks is pioneering the shift to compound AI systems** . Our inference platform offers the fastest and most cost-efficient model APIs, now enhanced with powerful tools for composing systems with multiple models, modalities, retrievers, and external tools.

We’re thrilled to announce our $52M Series B funding round led by Sequoia Capital, raising our valuation to $552M. Other investors in this round include NVIDIA, AMD, and MongoDB Ventures. Previous investors include Benchmark, Databricks Ventures, former Snowflake CEO Frank Slootman, former Meta COO Sheryl Sandberg, Airtable CEO Howie Liu, Scale AI CEO Alexandr Wang, as well as executives from LinkedIn, Confluent, Meta, and OnePassword.

This new funding round brings the total capital raised by Fireworks to $77M. This investment will help us drive the industry shift to compound AI systems, expand our team, and enhance our platform, enabling developers to quickly move AI applications from prototype to production.

Sequoia General Partner Sonya Huang shared with me “Fireworks is perfectly positioned to lead this industry shift. Their team's expertise in building high-performance inference stacks and innovative approach to enabling compound AI systems will empower developers with scalable AI solutions that were previously accessible only to tech giants.”

Since its inception, Fireworks has empowered developers with the fastest and most cost-effective inference for popular models. Today, we serve over 100 state-of-the-art models in text, image, audio, embedding, and multimodal formats, optimized for latency, throughput, and cost per token. We've reduced [inference times by up to 12x](https://fireworks.ai/blog/fireattention-v2-long-context-inference) compared to vLLM and 40x compared to GPT4. We process 140 billion tokens daily on our platform with 99.99% API uptime.

Unlike proprietary mega models that are generic, non-private, and hard to customize, Fireworks provides smaller, production-grade models that can be deployed privately and securely. Using minimal human-curated data, our ultra-fast [LoRA fine-tuning](https://fireworks.ai/blog/fine-tune-launch) allows developers to quickly customize models to their specific needs, transitioning from dataset preparation to querying a fine-tuned model in minutes. These fine-tuned models are seamlessly deployed, maintaining the same performance and cost benefits as our base models.

Developers at leading AI startups like Cresta, Cursor, and Liner, as well as digital-native giants like DoorDash, Quora, and Upwork, choose Fireworks for our smaller, specialized models. [Curso](https://fireworks.ai/blog/cursor)r, for example, has used Fireworks' custom Llama 3-70b model to achieve 1000 tokens/sec for code generation use cases such as instant apply, smart rewrites, and cursor prediction, which boost developer productivity.

We continue to enhance our platform through deep collaboration with top providers across the AI stack, including partnerships with:

- •[MongoDB](https://fireworks.ai/blog/optimize-rag-with-mongodb-atlas-and-fireworks) for Interactive Retrieval Augmented Generation (RAG).
- •Meta, Mistral, and Stability AI to deliver the [lowest latency](https://artificialanalysis.ai/providers/fireworks) on SOTA models: 0.27s for Llama 3 70b, 0.25s for Mixtral 8x22b and 7b, and 1.2s for 1024x1024 image on Stable Diffusion XL respectively.
- •NVIDIA, AMD, AWS, Google Cloud Platform, and Oracle Cloud for infrastructure optimizations.

In the past three months, we've launched new features that drastically boost performance and cut costs, bridging the gap between prototyping and production. These include:

- •[FireAttention V2](https://fireworks.ai/blog/fireattention-v2-long-context-inference) , a custom CUDA kernel-based serving stack with 12x faster inference for long context prompts used for RAG, multiturn inference, and multimodal applications.
- •[Firefunction-v2](https://fireworks.ai/blog/firefunction-v2-launch-post) , a function calling model on par with GPT4o at 2.5x the speed and 10% of the cost.
- •[On-demand GPU](https://fireworks.ai/blog/why-gpus-on-demand) deployment option, in addition to serverless and reserved cloud, for scaling companies that need reliability and speed without long-term commitments.
- •Pay-as-you-go pricing, team collaboration and a new metrics dashboard are available to developers on all the pricing tiers.

While leaderboards emphasize larger models, real-world AI results, especially in production, increasingly come from compound systems with multiple components. Compound AI systems tackle tasks using various interacting parts, such as multiple models, modalities, retrievers, external tools, data, and knowledge. Similar to microservices, agents in a compound AI system use LLMs to complete individual tasks and collectively solve complex problems. This modular approach allows developers to create multi-turn, multitask AI agent workflows with minimal coding. It reduces costs and complexity while enhancing reliability and speed for applications such as search, domain-expert copilots (e.g., coding, math, medicine). This approach was first proposed in a [post](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) by Matei Zaharia et al. from Berkeley Artificial Intelligence Research (BAIR).

Fireworks recently introduced a fundamental building block for compound AI systems: [FireFunction V2](https://fireworks.ai/blog/firefunction-v2-launch-post), an open weights function calling model. FireFunction serves as an orchestrator across multiple models and their multimodal capabilities, external data and knowledge sources, search, transcription, and other APIs, while preserving core LLM capabilities such as multi-turn chat.

Key features include:

- •**Open-weight model** that delivers high accuracy and fast performance out of the box
- •**Cloud and on-premise deployment** with low latency and high throughput inference
- •**Schema-based constrained generation** for improved error handling
- •**Customization capabilities** through fine-tuning and custom deployments
- •**Seamless integration** with popular AI frameworks and a wide range of external tools

Superhuman, an AI-powered email provider, used Fireworks to create Ask AI, a compound AI system that delivers rapid answers from your inbox. Customers simply ask questions without needing to remember senders, guess keywords, or search through messages. Ask AI uses function calling to interact with search and calendar tools, prompt LLMs, and generate rapid responses.

We are thrilled about this new chapter for Fireworks and the AI community, as it reduces the complexity and inefficiencies of productionizing AI applications. We started Fireworks to empower AI startups, digital-native companies, and Fortune 500 enterprises alike to disrupt the status quo with groundbreaking products, experiences, and increased productivity. We can’t wait to see what you disrupt.
