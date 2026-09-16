---
title: LangChain trains custom models for LangSmith Engine with Baseten Loops
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/langchain-trains-custom-models-langsmith-engine-baseten-loops/
author: Aaron Ellis-Bloor; Mudith Jayasekara; Jake Broekhuizen; Vivek Trivedy
published: '2026-09-15'
fetched: '2026-09-16T06:10:13Z'
classifier: null
taxonomy_rev: 2
words: 335
content_sha256: fa391b16c008f3c062cbd02ec61b7e79ccae4cfe941619805996a6db2c9c5ae4
---

# LangChain trains custom models for LangSmith Engine with Baseten Loops

![langchain](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1789478376-b10-langchain-blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

LangChain develops tools for building, evaluating, and deploying AI agents at scale. LangChain uses Baseten Loops to train custom models for LangSmith Engine, its in-platform agent that helps users debug and improve their agents autonomously.

Our collaboration with LangChain brings together their experience building AI agents and our infrastructure for model training and inference, allowing LangChain to own the intelligence that underpins their products.

## Training custom models for agent-specific tasks

Custom model training lets teams shape agent behavior around a specific task. Fine-tuning a large open-weight model on agent traces specializes it for difficult tasks in LangSmith Engine, such as reading a connected GitHub repository to diagnose why an issue is happening, then drafting the prompt or code change that goes into the pull request.

For more specialized requirements, such as categorizing traces by failure mode and severity, or mapping them to existing open issues, LangChain easily changes models and trains a smaller open-weight model (like Qwen) tailored specifically to the task.

## From training to production with Baseten Loops

[Baseten Loops](https://docs.baseten.co/loops/overview#loops) provides managed infrastructure for fine-tuning models through an API, with support for supervised fine-tuning, reinforcement learning, and long-context workloads. 

Loops also connects training to Baseten’s inference platform. Checkpoints can be evaluated during training and deployed directly, giving teams an easy way to experiment and bring models into production, which drastically increases the speed of training.

Our engineers continue to work closely with their team as it develops its training workflows.

“Baseten is a key partner as we develop the models behind LangSmith Engine. Loops gives us the control and iteration speed we need while training, backed by a team that works closely with us. Having training and inference on the same platform gives us a clear path from model development to production.”

Our collaboration reflects a shared focus on helping developers turn application data into improvements in agent behavior. LangChain brings the tools to understand and evaluate agents. Baseten provides the infrastructure to train custom models and bring them into production.
