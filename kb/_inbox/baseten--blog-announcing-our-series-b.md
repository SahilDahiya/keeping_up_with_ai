---
title: Announcing our Series B
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/announcing-our-series-b
author: Tuhin Srivastava
published: '2024-03-04'
fetched: '2026-11-12T06:12:00Z'
classifier: null
taxonomy_rev: 2
words: 668
content_sha256: eba16656881503ece59a8655e67b36cb8b95088a9cc1bdbe0df89af9bb9ab94e
---

# Announcing our Series B

News
# Announcing our Series B

We’ve spent the last four and a half years building Baseten to be the most performant, scalable, and reliable way to run your machine learning workloads.


- Authors
- Date
- March 4, 2024

We founded Baseten in 2019 to accelerate the impact of machine learning. To state the obvious, a lot has changed since then: large models have gone mainstream, with large-scale consumer adoption of tools like ChatGPT and Midjourney. At the same time, open-source models (Stable Diffusion, the Llamas, Mistral) are getting attention as customizable, widely available alternatives. Developers are actively reimagining what technology can achieve with AI at its core.

But for most businesses, it is still very challenging to run large models in production. Every part of the problem is difficult, cumbersome, and expensive: acquiring compute, getting models to run fast, scaling to meet demand, observability, CI/CD, cost optimization — the list goes on. When handling it all on their own, most teams spend as much time running models in production as they do focusing on the core product experiences they are building. This doesn’t make sense. Just as we saw new categories of tools emerge to support the transitions to cloud and mobile, we need new solutions built for the problem at hand.

This is where Baseten comes in. We’ve spent the last four and a half years building Baseten to be the most performant, scalable, and reliable way to run your machine learning workloads – in our cloud or yours. We’ve created beautiful, clean abstractions to scaffold out production services, paired with a workflow that seamlessly spans development and production ([meet Truss](https://truss.baseten.co/welcome), our open-source standard for serving models in production!). Our autoscaling and cold starts are world class, which keeps cost under control. Our native workflows serve large models in production so users don’t need to think about version management, roll-out, and observability. And we’ve done it all in a secure (SOC, HIPAA) way.

In 2023, we scaled inference loads hundreds of times over without a minute of downtime. Companies like Descript, Picnic Health, Writer, Patreon, Loop, and Robust Intelligence rely on us to power core machine learning workloads. Every day, thousands of developers use Baseten to deliver AI-enabled products without having to think about building any of the infrastructure powering their models.

We’re constantly launching new features. We’ve recently added:

- [Multi-cloud support](https://www.baseten.co/blog/the-benefits-of-globally-distributed-infrastructure-for-ml-model-serving/) so that customer workloads can span across multiple clouds and regions.
- Integrations with [best in-class runtimes like TensorRT](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/).
- Partnerships with AWS and GCP, so our customers [can access the best hardware](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/) and don’t need to spend months negotiating for compute from cloud providers.

In the next quarter, we’ll be adding more clouds (more GPUs!), a brand new orchestration layer (think build pipelines, queues, etc.), and an optimization engine to make sure workloads are running as performantly as possible. Customers tell us that they want us to go beyond inference, so we also have some exciting updates around fine-tuning, evals, and training coming soon.

Lastly, the money! We’re excited to announce that we’ve raised an additional $40M. [You can read more about it here](https://www.forbes.com/sites/kenrickcai/2024/03/04/baseten-series-b-making-ai-useful-inference/) but the long and short of it is that we’ve brought on some great new folks to help us further accelerate the adoption of machine learning. IVP and Spark led the round, and our existing investors Greylock, South Park Commons, Lachy Groom, and Base Case also participated. We also want to shout out the continued support of Sarah Guo at Conviction. This new round of funding gives us the room to move even faster on building the thing that we have always wanted and know needs to exist.

We’re always on the lookout for smart, fun, and humble people to [join us](https://www.baseten.co/careers/), so please get in touch if you think you might be a fit. And if you’re a developer who wants to build with Baseten, browse our [model library](https://www.baseten.co/library/) and [documentation](https://docs.baseten.co/welcome) to get started — or reach out to us if you want a personalized tour.
