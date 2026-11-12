---
title: 'AI Infrastructure: Build vs. Buy | Baseten'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ai-infrastructure-build-vs-buy
author: The Baseten Team
published: '2023-07-28'
fetched: '2026-11-12T06:13:40Z'
classifier: null
taxonomy_rev: 2
words: 1032
content_sha256: 59cd8e6105078b0d37c2519059cffc0bd0e43db9f8374e660275b28b83e26134
---

# AI Infrastructure: Build vs. Buy | Baseten

Infrastructure
# AI infrastructure: Build vs. buy

Should you build or buy your ML infra? We break down the tradeoffs, technical considerations, and when each approach makes sense.


- Authors
- Date
- July 28, 2023

TLDR

If you're starting to productionize machine learning models, one of the first big decisions you need to make is whether to build or buy your deployment infrastructure. This post breaks down the pros and cons of each AI infrastructure approach, including key considerations around performance, scalability, and cost-efficiency. We also spoke with Chris Albon, Director of Machine Learning at the Wikimedia Foundation, and include his perspective throughout.

Your AI/ML infrastructure is critical to the success of your business and needs to be robust enough to handle dynamic traffic loads without breaking the bank. Docker and Kubernetes are fantastic tools, but as your business grows, you’ll be faced with competing interests for your time and talent. There are definite benefits to continuing to build out your own AI infrastructure, just as there are benefits to outsourcing your infrastructure needs to a platform like Baseten.

We recommend using three distinct but related factors when evaluating AI infrastructure: performance, scalability, and cost-efficiency.

With regards to AI infrastructure, performance relates to how well your model performs in both development and production environments. Transparent and informative model logs and health metrics can give you insights into model performance, and help spot any issues with high latency or low throughput.

Scalability refers to both horizontal scaling and vertical scaling. Horizontal scaling is when more replicas, or nodes, are added to your infrastructure system, while vertical scaling is the addition of more computing power.

Compute can be expensive, and there’s nothing worse than paying for idle GPUs. You also don’t want to be paying for the wrong type of compute—for instance, using A100 GPUs when your model would perform just as well with A10s.

Optimizing for the right setup isn’t just about performance. It can dramatically reduce costs.

For example, [Patreon saved nearly $600k per year](https://www.baseten.co/resources/customers/patreon/) on ML infrastructure by right-sizing compute and automating scale with Baseten.

If you’ve got the team, the talent, and the time, building your own AI/ML infrastructure is a great way to lay the groundwork for a system that grows with your company, particularly if infrastructure is a differentiator for you. One of the main advantages of building your own AI infrastructure is that you have full control over the tools you use and how everything is configured, and for some organizations, this is exactly what they need to be successful.

But one of the biggest drawbacks of building your own AI infrastructure is that you need to both find and finance the team that will continue to build, maintain, and optimize your infrastructure as your organization continues to grow. This can be both time-consuming and expensive, and it’s worth thinking through whether or not the cost and time spent are worth the investment.

Purchasing AI/ML infrastructure services can get you up and running with your project quickly, handing off the expertise needed to configure infrastructure to a dedicated team, and ultimately lower some of the barriers in getting your product to market. And as a new client, you’re in a position to negotiate competitive starter pricing along with a slew of free computing credits.

However, there can be some drawbacks to purchasing AI infrastructure, the first being that you have less control over the configuration of your infrastructure. Furthermore, you’re in the position of relying on someone else to handle any infrastructure issues as they arise.

"If there are areas that are truly unique to your organization, you should 100% invest in building there. But don’t try to build out everything."


At Baseten, we take AI/ML infrastructure seriously and do everything we can to ensure you can get started in minutes, without getting tangled in complex deployment processes. Our [model deployment features](https://docs.baseten.co/deployment/deployments) require zero infrastructure experience and include logs and health metrics, giving you visibility into what’s happening with your models and making it easy to debug issues. And whether or not you’re a Baseten customer, you can always take advantage of [Truss](https://truss.baseten.co/?utm_source=product&utm_medium=blog&utm_campaign=build_vs_buy), our open-source model packaging framework.

Our horizontally scalable AI infrastructure gets you from prototype to production as quickly as possible, and we couple that with blazingly fast inference times and autoscaling features that ensure all traffic to your model gets served, while giving you full control over scale-to-zero settings so that you’re not paying for idle GPUs. To get an idea of just how fast our cold starts are, for Stable Diffusion on an A10G, we reliably see cold start times of 15 seconds, from zero to ready for inference.

We also make sure that computing resource management is easy and straightforward so that you’re always clear on which GPUs you’re utilizing for a given model.

We enable a suite of customizable model infrastructure features, which, along with our GPU scaling, fast cold starts, and scale to zero functionality, mean that you only pay for the compute that you use. No more surprise bills for idle GPUs!

"If it’s just another brick in the infrastructure, don’t bother putting your most creative people on it. Just buy a solution that meets your needs and focus on whatever’s actually unique to your company."


Want to host models on your own cloud? Not a problem! [Self-hosting](https://www.baseten.co/deployments/baseten-self-hosted/) comes with all the features of [our Pro plan](https://www.baseten.co/pricing/), and includes multi-tenant architecture capabilities, data segregation, and live engineering support.

Speaking of support, Baseten Pro and Self-hosted customers have dedicated engineering support through our team of forward-deployed engineers. These engineers are well-versed in the capabilities of Baseten and are deeply invested in ensuring your success with our platform.

We’re also proud of the fact that we’ve received both [SOC II Type 2 certification](https://www.baseten.co/blog/soc-2-type-2/) as well as [HIPAA compliance](https://www.baseten.co/blog/baseten-announces-hipaa-compliance?utm_source=product&utm_medium=blog&utm_campaign=build_vs_buy), demonstrating our dedication to providing secure and reliable AI infrastructure for hosting ML models, along with our commitment to ensuring the confidentiality, integrity, and availability of sensitive health information.

We’d love to know what you’re working on and whether or not Baseten is a good fit for your project or startup. Reach out to us at [hi@baseten.co](mailto:hi@baseten.co) to talk to our engineers.
