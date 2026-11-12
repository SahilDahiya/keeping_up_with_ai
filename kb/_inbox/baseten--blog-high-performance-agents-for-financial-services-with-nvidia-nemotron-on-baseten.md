---
title: High-performance agents for financial services with NVIDIA Nemotron on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/high-performance-agents-for-financial-services-with-nvidia-nemotron-on-baseten
author: Philip Kiely
published: '2025-10-28'
fetched: '2026-11-12T06:10:42Z'
classifier: null
taxonomy_rev: 2
words: 832
content_sha256: 50f020320e2013ecf464d9cdfff68ec2d2bd961f14c2b2d6fe0925e0b4e31002
---

# High-performance agents for financial services with NVIDIA Nemotron on Baseten

AI engineering
# High-performance agents for financial services with NVIDIA Nemotron on Baseten

Day-zero support for NVIDIA Nemotron Nano V2 VL, a powerful vision language model with use cases for document processing and more in financial services


- Authors
- Date
- October 28, 2025

TLDR

NVIDIA Nemotron Nano 2 VL is the new best-in-class open-source vision language model by NVIDIA. Based on a Nemotron Nano 2 LLM backbone, this 12 billion parameter model offers leading accuracy for efficiency for everything from video understanding to document processing. Enterprises in financial services and beyond can leverage Nemotron Nano 2 VL on Baseten for performant, scalable inference.

Baseten is excited to offer [day-zero support for NVIDIA Nemotron Nano 2 VL](https://developer.nvidia.com/blog/develop-specialized-ai-agents-with-new-nvidia-nemotron-vision-rag-and-guardrail-models/), a highly accurate and efficient vision language model, alongside other models in the Nemotron family.

NVIDIA Nemotron provides open weights and data, making these models an excellent choice for enterprises who want to build specialized AI agents. The Nemotron Nano 2 VL is a 12 billion parameter model built on [NVIDIA Nemotron Nano 2](https://research.nvidia.com/labs/adlr/files/NVIDIA-Nemotron-Nano-2-Technical-Report.pdf), a 9 billion parameter foundation model with a hybrid Mamba-Transformer architecture and reasoning capabilities.

[Nemotron Nano 2 VL](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16) replaces the [Llama Nemotron Nano VL](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1) with a larger, more capable, more scalable model with better performance across both vision language benchmarks and real-world testing.

Nemotron Nano 2 VL is [available to deploy today on Baseten](https://www.baseten.co/library/nvidia-nemotron-nano-12b-v2-vl/) and leverages NVIDIA NIM microservices for high-throughput, low-latency out-of-the-box performance.

While every industry, from healthcare to media to manufacturing, benefits from high-quality open vision language models, the financial services industry has a number of particularly compelling use cases.

Great applications of vision language models include:

- **KYC and Identity Verification:** know-your-customer compliance requires securely extracting PII from documents like drivers licenses and passports.
- **Intelligent Document Processing:** run OCR on everything from receipts and invoices to mortgage documents and SEC filings to extract structured information.
- **Fraud Detection:** scan customer interactions for unusual patterns across images and videos, not just textual records.

As enterprises in the financial services space build out differentiated agentic capabilities, adding vision agents for these kinds of use cases requires both highly accurate models and secure, scalable infrastructure.

Nemotron Nano 2 VL is a general-purpose vision language model that supports a wide range of tasks, including extracting and summarizing images, tables, charts, formulas, and other diagrams from documents.

Additionally, this expansion to the Nemotron family includes a smaller, faster, less expensive model that is particularly well-suited for straightforward optical character recognition (OCR) tasks: Nemotron Parse 1.1.

This one-billion-parameter vision language model provides accurate and efficient information parsing in a 10x-smaller footprint. Nemotron Parse 1.1 runs faster and with higher throughput than Nemotron Nano 2 VL, making it an ideal choice for simple, high-volume, cost-sensitive OCR tasks.

Financial services enterprises from banks to insurance companies to investment firms need secure, reliable AI models to power their agents. Nemotron models are built with open data and offer recipes for developers to create trustworthy custom AI for their specific needs.

Reliability is a function of model quality; models should provide accurate outputs. Nemotron Nano 2 VL offers best-in-class accuracy for a 12B model. The model was trained using NVIDIA-curated synthetics data to ensure high quality.

But reliability is also a function of inference infrastructure. Models need to be fast and scalable to support demanding enterprise workloads.

At Baseten, a leading AI infrastructure company focused on high-performance inference, we have day-zero support for Nemotron Nano 2 VL.

Baseten’s platform as a whole accelerates enterprise AI with:

- **Model performance:** run generative AI models with the lowest latencies, like our [industry-best GPT-OSS API built with NVIDIA Dynamo and NVIDIA Blackwell](https://www.baseten.co/blog/how-we-made-the-fastest-gpt-oss-on-nvidia-gpus-60-percent-faster/).
- **Multi-cloud infrastructure:** access autoscaling GPUs from across every hyperscaler and neocloud as a single unified compute layer with active-active reliability and independent workload planes with [multi-cloud capacity management](https://www.baseten.co/blog/how-we-built-multi-cloud-capacity-management/).
- **Forward-deployed engineers:** build alongside inference experts with hands-on technical support from [Baseten’s forward-deployed engineers](https://www.baseten.co/blog/forward-deployed-engineering/).
- **Enterprise-grade security:** SOC 2 Type II and HIPAA compliance, self-hosting, audit logs, SSO, and more for a complete [enterprise platform](https://www.baseten.co/enterprise/).

Baseten leverages a large number of NVIDIA technologies including [NVIDIA Dynamo](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/), [NVIDIA TensorRT-LLM](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), [NVIDIA TensorRT](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/), custom CUDA kernels, and more in the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/).

Our inference stack lets developers swap in and out components as needed. One way to run Nemotron models on Baseten is with [NVIDIA NIM](https://developer.nvidia.com/nim), NVIDIA’s pre-packaged model serving containers. NIM microservices bundle runtime, dependencies, and performance optimizations together.

Caption: NVIDIA NIM microservices package open-source models and runtime technologies together in a portable, easy-to-deploy container.

Baseten offers out-of-the-box support for NVIDIA NIM (or any other model container) for convenient deployments of Nemotron.

Whether you’re building agents for KYC, document processing, fraud detection, or another mission-critical workflow, give them an intelligence upgrade with Nemotron Nano 2 VL.

You can deploy [Nemotron Nano 2 VL on Baseten today](https://www.baseten.co/library/nvidia-nemotron-nano-12b-v2-vl/) for scalable inference on NVIDIA’s latest vision model, or [get in touch with our engineers](https://www.baseten.co/talk-to-us/) to learn more about the performance, scale, security, and flexibility we offer enterprises, including our [self-hosting capabilities](https://www.baseten.co/deployments/baseten-self-hosted/).
