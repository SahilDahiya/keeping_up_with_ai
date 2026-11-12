---
title: Inference Infrastructure for AI Labs | Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-frontier-gateway
author: Bola Malek
published: '2026-05-06'
fetched: '2026-11-12T06:14:48Z'
classifier: null
taxonomy_rev: 2
words: 1166
content_sha256: 074defd51d268c1a00d37f43cb39eaedeae03f2c1b44b2901e1c8bcb7360799a
---

# Inference Infrastructure for AI Labs | Baseten

Product
# Introducing the Baseten Frontier Gateway

Production-grade Inference Infrastructure for AI Labs


- Authors
- Date
- May 6, 2026

TLDR

Starting today, labs can launch a production-grade, multi-tenant inference API on Baseten without having to build or buy a separate gateway. The Baseten Frontier Gateway is a managed API gateway built on top of Baseten Dedicated Inference. It lets labs serve Baseten hosted models under their own domain and gives them everything they need to service models through production-grade AI inference infrastructure to multiple customers.

Over the past few months, we have witnessed a striking evolution of the AI Frontier. It has moved from evolving in a smooth and expanding line to a jagged and uneven boundary that outlines the irregular shape of AI capabilities across different tasks.

Today, we believe that the frontier is better understood as a “capability silhouette”: irregular, shifting unevenly and defined by its gaps as much as its peaks. It means that Frontier models can’t be good at all tasks on their own and specialization is necessary. In addition, the barrier to training frontier-quality models has collapsed.

The tools, techniques, and talent that once lived exclusively inside a handful of well-capitalized labs are now more broadly available. It has resulted in a Cambrian explosion of new model labs coming online and we see new ones emerging every week. They cover the frontier across modalities and use-cases – image generation, video, speech, code, reasoning, RL agents and a growing list of vertical-specific research directions.

*“When we set out to make our Laguna family of models available to the world, we knew the inference layer would make or break the developer experience at launch.”* 


These model labs excel because they have research at their core, not infrastructure. Their competitive advantage lives in their research and the products that research unlocks and not in auth, billing systems or GPU capacity management. But before today, when a model lab was ready to offer API access to its model, it had a narrow set of options:

**Build it in-house:** hire a team of engineers to build authentication & authorization, API key management, rate limiting, usage metering and a billing integration. While building in-house can be attractive, it comes with the following challenges:

1. Each piece of this complex puzzle requires deep expertise in each area and together they represent months of engineering time and ongoing maintenance burden.
2. There are serious security risks when using open source libraries like LiteLLM which was compromised only a few weeks ago during a fairly long 3 hour time window and exposed a large number of cloud providers.
3. There is a real operational risk if any part of the solution fails under load: if the model is successful and the usage is growing, chances are that they will have to rebuild it at each stage of growth because auth and metering become really hard at scale.

**Buy a third-party gateway:** There are many tools out there that can handle some of this but they were not designed for inference. The various conversations we have had with model labs interested in working with us highlight the following challenges they have ran into:

1. Latency/performance concerns: a third-party gateway runs in a centralized location that is often decoupled from their inference. This can add hundreds of milliseconds of overhead which is a significant problem for performance-optimized workloads.
2. Model orchestration: These external gateways do not offer a clean way to chain calls to other models before hitting the main inference endpoint. It presents an architectural challenge to model labs who need to deliver complex workflows.
3. Billing complexity: Depending on the model and type of billing parameters, there is often a need to write custom code to deliver more flexibility to their GTM teams.

Neither path is fast or cheap. In both cases, they have to sacrifice inference performance for network routing latency because it is not coupled enough to the inference infrastructure. In addition, both divert engineering attention away from the research that actually differentiates the lab. With its deep expertise in inference and its proven platform, Baseten is uniquely positioned to address this challenge for model labs and that’s why we are excited to introduce the Baseten Frontier Gateway today.

With the Frontier Gateway, labs can launch a production-grade, multi-tenant inference API on Baseten without having to build or buy a separate gateway.

Baseten Frontier Gateway is a managed routing layer that sits natively on top of Baseten Dedicated Inference. And because the gateway is co-located with the inference infrastructure, labs get everything without latency or integration overhead.

Key features of the gateway:

- **Authentication & authorization**: Every incoming request is validated before it reaches the model. Baseten handles authn/authz at scale, across clouds. A problem that is deceptively hard to do correctly and reliably under load and at scale.
- **Federated API key management:** Baseten provides you with an API to generate access tokens and manage access, rate limits, and usage limits across your hosted models. You issue keys to your downstream users while we handle the lifecycle.
- **Per-user rate and usage limits:** Enforce token or request-based limits per API key to prevent abuse and protect other users from noisy neighbor effects.
- **Billing and metering:** Token or character consumption is tracked per API key. Usage data is sent out-of-band to allow you to plug directly into your billing provider, without affecting inference performance.
- **White label branding:** Requests are served from a lab-branded URL (e.g.: <u>api.yourlabname.ai</u>) while routing under the hood to Baseten's inference infrastructure.

**Built on Baseten Inference:**

Labs using the gateway also inherit Baseten powerful inference platform capabilities:

- **Scalability and reliability:** 99.99% uptime backed by Baseten Cloud and its global, elastic GPU pool.
- **Performance:** Years of runtime optimization delivered through the Baseten Inference Stack including significant latency and throughput improvements over baseline serving frameworks.
- **Compliance:** SOC 2 Type 2, SOC 3, HIPAA, CCPA, PCI DSS, GDPR out of the box and zero data retention. More details can be found in our [<u>Trust Center</u>](https://trust.baseten.co/).

If you are building a model and want to monetize it, the Baseten Frontier Gateway is the fastest path from trained weights to production API.

Poolside is one of the first labs using the Frontier Gateway and the partnership delivered results that exceeded their expectations on every dimension: Performance, speed of execution and relationship quality.

*“Baseten exceeded our quality and performance bar. The speed from conversion to production-grade, whitelabeled API was unlike anything we had seen from an infrastructure partner.”* 


Baseten’s engineering team achieved a breakthrough by leveraging Triton MoE backend for Laguna inference. Some key results include:

- **P50 TTFT:** 146ms for Laguna XS.2 and 605ms for Laguna M.1
- **P90 TTFT:** 1.5s for Laguna XS.2 and 3.9s for Laguna M.1

The Baseten Frontier Gateway is available with [full documentation](https://docs.baseten.co/frontier-gateway/overview). We are onboarding new labs starting today so if you are interested, submit an application [here](https://www.baseten.co/products/frontier-gateway/) and our team will reach out to you promptly.
