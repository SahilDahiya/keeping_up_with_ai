---
title: 'NVIDIA Nemotron 3 Nano Omni: Build multimodal agents on Baseten'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-3-nano-omni
author: Madison Kanna
published: '2026-04-28'
fetched: '2026-11-12T06:14:46Z'
classifier: null
taxonomy_rev: 2
words: 680
content_sha256: 7520b83b9a2e3f89b8646a50abcbee796bafe7ab9bebca1db4e303fcec97d708
---

# NVIDIA Nemotron 3 Nano Omni: Build multimodal agents on Baseten

AI models
# NVIDIA Nemotron 3 Nano Omni: Build multimodal agents on Baseten

NVIDIA Nemotron 3 Nano Omni is an open multimodal foundation model that unifies audio, images, and videos into a single context.


- Authors
- Date
- April 28, 2026

TLDR

NVIDIA Nemotron 3 Nano Omni is an open multimodal foundation model that unifies audio, images, video, and text into a single context. Built on the Nemotron 3 Nano backbone, Nemotron 3 Nano Omni powers sub-agents in agentic workflows with leading efficiency and accuracy. Today, Baseten is launching support for NVIDIA Nemotron 3 Nano Omni, an open unified multimodal model built for production agents.

NVIDIA Nemotron 3 Nano Omni is an open, efficient multimodal foundation model built to power sub-agents that understand and reason across video, audio, images, documents and text in enterprise agent systems.

Most agent systems today rely on separate models for speech, vision and language. When it comes to agentic workflows, this creates problems. Separate models mean repeated inference passes, increasing latency. Orchestration and error handling also become more complex and context fragments across modalities which reduces accuracy.

NVIDIA Nemotron 3 Nano Omni takes a different approach. It is a single multimodal reasoning model that enables agents to reason and perceive across modalities within a unified loop with complete deployment control and efficient performance.

Nemotron 3 Nano Omni combines audio and vision encoders into a unified multimodal architecture, which eliminates the need for separate perception models. This enables agents to complete tasks faster at scale, and simplifies agent development.

There are three architectural choices in particular that make Omni efficient:

- A latent MoE design used that improves memory and compute efficiency
- 3D convolutional layers let the model extract spatial and temporal features together, so it knows how visuals change over time
- Efficient video sampling selectively processes the most dynamic parts of long videos, instead of scanning entire frames

Nemotron 3 Nano Omni extends the efficiency and accuracy of Nemotron 3 Nano across different modalities.

Nemotron 3 Nano Omni’s open, lightweight 30B-A3B architecture supports deployments in local environments, such as NVIDIA DGX systems, as well as datacenters and cloud environments. It’s designed for computer use, complex document intelligence and audio and video reasoning.

Context matters in customer service, research and monitoring workflows, and Nemotron 3 Nano Omni preserves unified multimodal context across audio, video, and documents within a single reasoning loop.

At Baseten, as an AI infrastructure platform purpose-built for ultra-fast inference, we provide day-zero support for Nemotron 3 Nano Omni.

Our platform accelerates enterprise AI initiatives through:

- High performance inference: We run generative AI models with exceptionally low latency, including our top tier [<u>GPT-OSS API</u>](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/) powered by [<u>NVIDIA Dynamo</u>](https://www.nvidia.com/en-us/ai/dynamo/) and the [<u>NVIDIA Blackwell architecture</u>](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/).
- [<u>Multi-cloud Capacity Management</u>](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/%23what-is-mcm-isnt-it-just-another-multi-cloud-solution) (MCM): Our customers tap into autoscaling GPU resources spanning all major hyperscalers and neo-cloud providers, unified into a single compute layer. They benefit from active-active reliability, isolated workload planes and intelligent multi-cloud capacity management.
- Expert engineering support: Collaboration with the [<u>Baseten Forward Deployed Engineers</u>](https://www.baseten.co/blog/forward-deployed-engineering/%23how-do-you-establish-an-fde-function) (FDE) provides hands-on assistance from specialists in large scale inference.
- [<u>Robust enterprise security</u>](https://www.baseten.co/enterprise/): Baseten is SOC 2 Type II, SOC 3 and HIPAA compliant, offers self-hosting options as well as audit logging, SSO and other features essential for [<u>enterprise environments</u>](https://www.baseten.co/enterprise/).

[<u>The Baseten Inference</u>](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) stack is critical to achieve these results and under the hood it uses NVFP4, components of TensorRT-LLM, Dynamo and the Baseten Speculation Engine. All running on NVIDIA Blackwell GPUs.

If you’re building agents that need to see, hear, and reason across workflows—such as customer service, computer use or document intelligence - Nemotron 3 Nano Omni provides you with a production-ready, open foundation to do all of this with a single model.

The model processes multimodal inputs such as audio, video, images, and documents (e.g., recordings or files) and performs unified reasoning across them in a single pass.

You can deploy [Nemotron 3 Nano Omni on Baseten](https://www.baseten.co/library/nemotron-3-nano-omni/) for scalable multimodal inference, or [<u>get in touch with our engineers</u>](https://www.baseten.co/talk-to-us/) to learn more about the performance, scale, security, and flexibility we offer enterprises, including our [<u>self-hosting capabilities</u>](https://www.baseten.co/deployments/baseten-self-hosted/).
