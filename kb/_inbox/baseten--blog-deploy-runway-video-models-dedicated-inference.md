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
url: https://www.baseten.co/blog/deploy-runway-video-models-dedicated-inference
author: Albert Lee
published: '2026-10-14'
fetched: '2026-11-12T06:08:54Z'
classifier: null
taxonomy_rev: 2
words: 398
content_sha256: fcbb3ddb294eb20175692d17eaadcbf9d93f49e2de621afa4d6f2eb83f78a75a
---

# Deploy Runway’s video models on Baseten

AI models
# Deploy Runway’s video models on Baseten

You can now deploy Runway’s Gen-4.5 and Aleph 2.0 on secure, single-tenant environments on Baseten.


- Authors
- Date
- October 14, 2026

TLDR

We’ve partnered with Runway to bring its video models to enterprises on Baseten. You can deploy Runway’s Gen-4.5 and Aleph 2.0, including fine-tuned versions, in single-tenant environments through Baseten Dedicated Inference.

Runway builds models that generate and edit cinematic video using text, images, audio, and existing footage. Runway’s frontier video generation and editing models, Gen-4.5 and Aleph 2.0, are now available directly through Baseten.

Gen-4.5 turns text and image inputs into video, with support for detailed scene direction, camera movement, and a range of visual styles. You can use it to visualize a storyboard, animate a product image, create cinematic B-roll, or adapt a campaign concept into multiple variations.

Aleph 2.0 complements Gen-4.5 by letting you modify generated or real footage you already have. Starting with a prompt or edited keyframe, you can change a specific element or restyle a scene, then carry that edit across relevant shots while preserving the surrounding details. The model supports multi-scene videos up to 30 seconds at 1080p.

Runway offers these models through Runway Creative, its platform for generating and editing video, images and audio, and Runway Dev, its API platform for developers. Through this partnership, Runway is also making its proprietary video models available for dedicated deployment on Baseten.

You can license Runway model weights directly from Runway and deploy them in a secure, single-tenant environment on Baseten. Each deployment runs in an isolated workload plane with dedicated GPU resources, while Baseten manages the control plane and underlying infrastructure. Runway and Baseten support each deployment together, from model customization through production serving.

- **Security and compliance**: Compute and scheduling are isolated to your organization. Baseten’s access to Runway’s model weights is governed by a distribution agreement, and your deployment runs on infrastructure covered by Baseten’s SOC 2 Type II and HIPAA compliance programs.
- **Fine-tuning:** You can fine-tune Runway models on your own data so their outputs reflect your brand, canon, and content guidelines. Your direct license with Runway governs this work, while Baseten provides the infrastructure to run the fine-tuning and deploy the resulting model in a dedicated environment.
- **Dedicated capacity**: You get reserved GPU capacity for video-generation workloads, with autoscaling to handle spikes in demand.
