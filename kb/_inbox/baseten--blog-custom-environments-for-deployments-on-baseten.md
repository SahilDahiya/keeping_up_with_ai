---
title: Create custom environments for deployments on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/custom-environments-for-deployments-on-baseten
author: Samiksha Pal
published: '2024-11-14'
fetched: '2026-11-12T06:09:22Z'
classifier: null
taxonomy_rev: 2
words: 727
content_sha256: d536af630322e8ab98a116eef2972bffad00833fa5946f642467b74ed5a3f89b
---

# Create custom environments for deployments on Baseten

News
# Create custom environments for deployments on Baseten

Test and deploy ML models reliably with production-ready custom environments, persistent endpoints, and seamless CI/CD.


- Authors
- Date
- November 14, 2024

TLDR

Custom environments let you create production-ready environments for any model deployment and use case. Define custom auto-scaling and promotion settings (including canary deployments) for situations like staging and benchmarking, get a persistent environment endpoint, and seamlessly roll back to previous model versions. Join us at KubeCon to learn more about our product roadmap, or meet us and Lambda at our happy hour Thursday, November 14th!

We're making engineering best practices the standard for ML model deployments. After working with our customers to perfect custom environments, we’re thrilled to release them as GA!

Developers need the ability to test production workflows and workloads without the consequences of failing in production. Our custom environments address this need: they act as full production environments with all the same capabilities except one—they don’t receive your production traffic.

To test your production workflows, you could define environments for:

- Testing
- Staging
- Benchmarking
- The new interns
- Dan, that coworker who always wants their own setup

Baseten’s custom environments come with persistent URLs to ensure your next production release performs as expected. Rigorously test and tune your settings, knowing your model will behave identically in production—or flexibly define testing environments with cheaper hardware.

Check out the demo by [Samiksha Pal](https://www.linkedin.com/in/samiksha-pal/), one of the lead engineers behind custom environments:

Our custom environments stand out for their:

- **Production-readiness:** These are full-fledged environments, equipped with custom autoscaling settings and persistent endpoints for inference and management.
- **Streamlined model promotions:** Models move fluidly between environments, obviating build time and reducing errors.
- **CI/CD:** Promote any model to any environment, with seamless rollback and full deployment history.

Streamline your ML model CI/CD pipelines, save engineering time, and enhance the reliability of your models in production.

An environment encapsulates a single deployment, including all configurations for:

While environments have long been a part of our platform, custom environments give users more flexibility and control to test beyond development and production.

With other solutions, promotions from different environments are either unsupported or slow, because your model image needs to be rebuilt upon promotion. This can introduce unexpected behavior if anything in your model code (or dependencies) changed since the first time it was built and deployed.

Our environments provide safe testing spaces and smooth promotion through development stages (like going from development to staging, then to production). Since we don’t have to rebuild your model image between promotions:

- Promotions are faster
- You know your model will perform exactly as expected
- There’s less risk of breaking your pipeline or causing inconsistencies in model behavior

This enables:

- Cleaner model management
- Faster development cycles
- More reliable production systems

Our custom environments are built for deployment stability across the entire ML model lifecycle. While other solutions can be useful for basic workspace segmentation, they lack the fine-tuned control to ensure robust performance in production environments.

This level of customizability for environments plays a critical role in CI/CD workflows by:

- Creating persistent endpoints per environment
- Enabling rollbacks and version control
- Isolating testing and development
- Automating promotion flow

Just a few ways our custom environments stand out in the ML deployment landscape:

| Feature | Baseten | Other solutions | 
|---|---|---|
| CI/CD | Environments come with persistent URLs, custom configuration options (including autoscaling), canary deployments, and model rollbacks—ideal for CI/CD. | Typically built as sandboxes. Limited or no production-level settings (like autoscaling) and no model rollbacks. | 
| Promotion flow | We enable a seamless promotion flow between environments, including production. No redundant model builds, making it efficient for testing and validation cycles. | No built-in capability to promote deployments across environments, forcing additional model builds. Slower, and can introduce inconsistencies in model behavior. | 

Developer experience is at the heart of everything we build. Custom environments with persistent URLs help developers test, iterate, and release faster, ensuring that products are high-performing and reliable in production.

We’re thrilled to offer a uniquely developer-first experience, making engineering workflow best practices a standard in the field of ML model deployments. [Join us at KubeCon](https://www.baseten.co/resources/event/baseten-kubecon24/) to learn more about our product roadmap, or meet us and [Lambda](https://www.linkedin.com/company/lambda-cloud/posts/?feedView=all) at our [happy hour](https://lu.ma/qxfyykcz)!
