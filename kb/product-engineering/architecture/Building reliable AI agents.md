---
title: Building reliable AI agents
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/multi-agent
- evals-observability/monitoring
summary: Breaks the agent stack into cognitive, tool-interaction, oversight, and orchestration
  layers, and describes using Patronus AI's Percival debugger to catch 20+ production
  agent error types.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-to-build-reliable-ai-agents
author: Chinmayee Kulkarni
published: '2025-07-15'
fetched: '2026-11-12T06:10:10Z'
classifier: claude
taxonomy_rev: 2
words: 1062
content_sha256: 05bf1d27cdbd53499166b48667fc3e26730ca694a503339fbb74ecfd4218a4b8
---

# Building reliable AI agents

AI engineering
# Building reliable AI agents

Agentic AI workflows are compound AI systems. This blog breaks down the models, infra, and orchestration needed to build and run them in production.


- Authors
- Date
- July 15, 2025

TLDR

AI agents are complex systems that go beyond simple LLM query-response patterns. The agent stack consists of four layers spanning reasoning, tool use, oversight, and orchestration, powered by different platforms and AI models. Baseten enables modular deployment for agentic workloads with independent scaling per component, while Patronus AI's Percival debugger catches failures across 20+ error types for agents in production.

Agents are more complex than traditional AI workloads. While LLMs operate on a query → response basis (a 1:1 relationship), agents take in a query, decompose it into subtasks, and take action on the user’s behalf (a 1:many relationship).

In other words, while LLMs fetch information from a variety of data sources to produce an answer, agents both fetch information and perform actions on behalf of the user to produce an answer.

This means that agentic workflows must coordinate multiple moving parts: reasoning over the user's intent, deciding which tools to use, executing calls to those tools, and integrating the results. Supporting this added complexity requires a unique tech stack.

In this blog, we outline what the stack is: the architecture, tools, and infrastructure needed to build and deploy reliable AI agents. We’ll start with the models and platforms you can use to build reliable agents, then explain how to link those components together, deploy them to production, and evaluate performance in terms of both quality and responsiveness.

The agentic stack has four layers:

1. **The cognitive layer**: This layer is powered by LLMs. It’s where user intent is parsed, the course of action is determined, and decisions are made regarding action coordination.
2. **Tool interaction**: Agents must use different tools, such as databases, APIs, and other models to satisfy user intent. This layer interacts closely with the cognitive layer to determine which tools to access for various subtasks.
3. **Oversight**: This layer is responsible for agent safety and alignment. It consists of grounding, guardrails, and tracing.
4. **Orchestration**: Finally, your agent may have to interact with other agents; in this case, an orchestration layer coordinates across multiple specialized agents, managing communication, delegation, and review.

Building these layers requires combining different models, tools, and platforms. Let’s look at the agentic tech stack.

To power the cognitive layer of agents, builders typically leverage state-of-the-art LLMs. Popular model families include:

- **Llama**: A good all-rounder, with support for long context windows with [Llama 4 Scout](https://www.baseten.co/library/llama-4-scout/) (10M token context) and [Maverick](https://www.baseten.co/library/llama-4-maverick/) (1M token context).
- **Qwen**: A popular choice for coding tasks; typically lighter-weight to run due to the smaller size of many models in the Qwen family.
- **DeepSeek**: Powerful for many applications with good built-in structured outputs and tool usage for both [DeepSeek V3](https://www.baseten.co/library/deepseek-v3/) and [R1 0528](https://www.baseten.co/library/deepseek-r1/).
- **Kimi K3**: A strong choice for long-horizon agentic coding, with sustained multi-hour autonomous sessions, native multimodality, and a 1M-token context window.

Once you’ve selected your models and tools, you’ll need to link them together into a coherent workflow.

Modern agent systems require sophisticated orchestration that goes beyond simple request-response patterns. They need modular, scalable workflows, where each component can run on optimal hardware while maintaining frictionless communication.

Without proper orchestration, you can run into:

- Cumbersome, inefficient scripts to coordinate between models
- Inefficient hardware utilization or processing bottlenecks
- Complex error handling and retry logic

For these reasons, building modular deployments—where each model or processing step in an agentic workflow is deployed as an independent unit—is a best practice for agentic systems. Each component can be deployed on optimal hardware (like using CPUs for less-intensive tasks vs. more powerful GPUs for more compute-intensive models), and ideally scale independently as needed. (These capabilities are what frameworks like [Baseten Chains](https://www.baseten.co/products/chains/) aim to solve.)

Building your agent is half the battle—deploying it to production is the other half.

Deploying agents involves serving and scaling multiple interdependent components such as planners, retrievers, and model backends. This requires infrastructure that goes beyond basic model hosting, with support for:

- **Component-specific autoscaling**: Different parts of the agent pipeline experience distinct load patterns. Inference infrastructure should allow independent scaling (e.g., scale retrievers separately from LLMs) to avoid under- or overprovisioning, performance bottlenecks, or wasted money on idle GPUs.
- **Heterogeneous hardware support**: Components should run on optimal hardware for their role—e.g., orchestration logic on CPU, embedding models on lighter-weight GPUs, and large generative models on more powerful GPU instances. This improves both performance and cost-efficiency.
- **Fault isolation**: Since agents span multiple services, a failure in one component (e.g., a vector database or router) can take down the entire pipeline. Use active-active topologies, retry logic, and circuit breakers to support reliability.
- **Latency-aware routing and orchestration**: Especially for interactive agents, infrastructure should support prioritizing low-latency paths, as well as intelligent or geo-aware routing.
- **Observability and evaluation**: Fine-grained logs, traces, and evaluation tooling (e.g., Patronus AI) are essential to debug, monitor, and improve agent performance in production settings.

Once deployed, the challenge shifts from getting agents to run to making sure they behave reliably and effectively in real-world conditions.

That’s where evaluation comes in.

Determining success is difficult with agents due to their increased complexity. While traditional evaluation methods like [LLMs-as-a-Judge](https://www.patronus.ai/llm-testing) score individual outputs, evaluating agents requires analyzing the full trajectory of their behavior; their actions need to be contextualized in a dynamic environment to uncover systemic patterns and failure modes that will otherwise propagate.

Points of failure—such as miscommunication, accessing improper data sources, or delegation errors—can occur in any layer. Additionally, many agent benchmarks do not adequately capture real-world context, nuances, or performance.

To provide a more realistic alternative, Patronus AI developed [TRAIL](https://www.patronus.ai/blog/introducing-trail-a-benchmark-for-agentic-evaluation), a benchmark designed to debug and identify errors in complex AI agent workflows. Built on top of that is [Percival](https://www.patronus.ai/percival), an AI agent debugger that evaluates across all major agent failure types with [integrations](https://docs.patronus.ai/docs/percival/percival) with various platforms like Langchain, Pydantic, and smolagents.

As agents grow in complexity and capability, building and evaluating them requires a new stack—spanning models, infrastructure, orchestration, and oversight.

If you're building and shipping production AI agents, you can [reach out to Baseten's engineers](https://www.baseten.co/talk-to-us/) for help deploying agentic workflows in production, and [Patronus AI](https://www.patronus.ai/book-a-call) for support evaluating and improving their performance for real users.
