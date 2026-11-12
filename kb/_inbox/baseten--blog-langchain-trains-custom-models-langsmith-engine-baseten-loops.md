---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/langchain-trains-custom-models-langsmith-engine-baseten-loops
author: null
published: '2026-01-01'
fetched: '2026-11-12T06:06:56Z'
classifier: null
taxonomy_rev: 2
words: 370
content_sha256: c212ea3b0dfcd5ca17a05f5c5c473704aeb9f4ec02735e9bf7a20425b7000db2
---

# The platform for inference, training, and execution | Baseten

LangChain trains custom models for LangSmith Engine with Loops

Baseten Loops provides managed infrastructure for fine-tuning models through an API, with support for supervised fine-tuning, reinforcement learning, and long-context workloads.

LangChain develops tools for building, evaluating, and deploying AI agents at scale. LangChain uses Baseten Loops to train custom models for LangSmith Engine, its in-platform agent that helps users debug and improve their agents autonomously.

Our collaboration with LangChain brings together their experience building AI agents and our infrastructure for model training and inference, allowing LangChain to own the intelligence that underpins their products.

Training custom models for agent-specific tasks

Custom model training lets teams shape agent behavior around a specific task. Fine-tuning a large open-weight model on agent traces specializes it for difficult tasks in LangSmith Engine, such as reading a connected GitHub repository to diagnose why an issue is happening, then drafting the prompt or code change that goes into the pull request.

For more specialized requirements, such as categorizing traces by failure mode and severity, or mapping them to existing open issues, LangChain easily changes models and trains a smaller open-weight model (like Qwen) tailored specifically to the task.

From training to production with Baseten Loops

Baseten Loops provides managed infrastructure for fine-tuning models through an API, with support for supervised fine-tuning, reinforcement learning, and long-context workloads.

Loops also connects training to Baseten’s inference platform. Checkpoints can be evaluated during training and deployed directly, giving teams an easy way to experiment and bring models into production, which drastically increases the speed of training.

Our engineers continue to work closely with their team as it develops its training workflows.

“Baseten is a key partner as we develop the models behind LangSmith Engine. Loops gives us the control and iteration speed we need while training, backed by a team that works closely with us. Having training and inference on the same platform gives us a clear path from model development to production.”

— Jake Broekhuizen, Applied Research Lead, LangChain Labs

Our collaboration reflects a shared focus on helping developers turn application data into improvements in agent behavior. LangChain brings the tools to understand and evaluate agents. Baseten provides the infrastructure to train custom models and bring them into production.
