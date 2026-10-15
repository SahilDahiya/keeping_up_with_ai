---
title: Deploy Runway’s video models on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deploy-runway-video-models-dedicated-inference/
author: Albert Lee
published: '2026-10-14'
fetched: '2026-10-15T06:10:46Z'
classifier: null
taxonomy_rev: 2
words: 475
content_sha256: a1b5f0fe851285c33c4dd519560c8680d2f045e54018d757f962065e22bf0ec6
---

# Deploy Runway’s video models on Baseten

### Published

![Baseten Runway Partnership](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791578046-black-logo-4x.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

We’ve partnered with Runway to bring its video models to enterprises on Baseten. You can deploy Runway’s [Gen-4.5](https://www.baseten.co/library/gen-45/) and [Aleph 2.0](https://www.baseten.co/library/aleph-2/), including fine-tuned versions, in single-tenant environments through [Baseten Dedicated Inference](https://www.baseten.co/products/dedicated-inference/).

Runway builds models that generate and edit cinematic video using text, images, audio, and existing footage. Runway’s frontier video generation and editing models, Gen-4.5 and Aleph 2.0, are now available directly through Baseten.

## **Runway’s video models: Gen-4.5 and Aleph 2.0**

Gen-4.5 turns text and image inputs into video, with support for detailed scene direction, camera movement, and a range of visual styles. You can use it to visualize a storyboard, animate a product image, create cinematic B-roll, or adapt a campaign concept into multiple variations.

Aleph 2.0 complements Gen-4.5 by letting you modify generated or real footage you already have. Starting with a prompt or edited keyframe, you can change a specific element or restyle a scene, then carry that edit across relevant shots while preserving the surrounding details. The model supports multi-scene videos up to 30 seconds at 1080p.

![Video](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2FDiNxmcYp7MMjKOo4s38pwdK5rTERwVHT%2Fthumbnail.jpg%3Ftime%3D0.609&w=3840&q=75)

Runway offers these models through Runway Creative, its platform for generating and editing video, images and audio, and Runway Dev, its API platform for developers. Through this partnership, Runway is also making its proprietary video models available for dedicated deployment on Baseten.

## **Deploy Runway models on Baseten**

You can license Runway model weights directly from Runway and deploy them in a secure, single-tenant environment on Baseten. Each deployment runs in an isolated workload plane with dedicated GPU resources, while Baseten manages the control plane and underlying infrastructure. Runway and Baseten support each deployment together, from model customization through production serving.

- **Security and compliance**: Compute and scheduling are isolated to your organization. Baseten’s access to Runway’s model weights is governed by a distribution agreement, and your deployment runs on infrastructure covered by Baseten’s SOC 2 Type II and HIPAA compliance programs.
- **Fine-tuning:** You can fine-tune Runway models on your own data so their outputs reflect your brand, canon, and content guidelines. Your direct license with Runway governs this work, while Baseten provides the infrastructure to run the fine-tuning and deploy the resulting model in a dedicated environment.
- **Dedicated capacity**: You get reserved GPU capacity for video-generation workloads, with autoscaling to handle spikes in demand.

![Your Runway deployment runs in an isolated workload plane with dedicated GPU nodes, while Baseten manages the control plane.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1791578183-hosting-options-single-tenant.avif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Your Runway deployment runs in an isolated workload plane with dedicated GPU nodes, while Baseten manages the control plane.

*Source: Baseten single-tenant documentation.*

## **Runway in the enterprise**

Amazon, Robinhood, Dolce & Gabbana, and Microsoft are among the enterprise creative teams already using Runway in production. Baseten backs dedicated deployments with a 99.99% uptime SLA.

Ready to join them? Learn more and deploy [Gen-4.5](https://www.baseten.co/library/gen-45/) and [Aleph 2.0](https://www.baseten.co/library/aleph-2/) on Baseten dedicated inference.
