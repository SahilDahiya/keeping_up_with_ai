---
title: AI Agent Observability, Tracing & Evaluation with Langfuse
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/planning
summary: Guide to observability for AI agents, covering traces, spans, tool calls,
  evaluations, and debugging workflows for agentic systems.
source: langfuse
url: https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse
author: null
published: '2026-02-20'
fetched: '2026-07-11T04:34:39Z'
classifier: codex
taxonomy_rev: 1
words: 2259
content_sha256: 5711d62293f3edec32d24b80d4d4b0d896f60bc98a529e92342779201cc29fe3
---

# AI Agent Observability, Tracing & Evaluation with Langfuse

# AI Agent Observability, Tracing & Evaluation with Langfuse

Trace, monitor, evaluate, and test AI agents in production. Learn about agent observability strategies, evaluation techniques, and how to use Langfuse with LangGraph, OpenAI Agents, Pydantic AI, CrewAI, n8n, and more.

![Picture Jannik Maierhöfer](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fjannikmaierhoefer.jpg&w=96&q=75) Jannik Maierhöfer

Jannik Maierhöfer[What are AI Agents?](https://langfuse.com#what-are-ai-agents)

An AI agent is a system that autonomously performs tasks by planning its task execution and utilizing available tools. AI Agents leverage large language models (LLMs) to understand and respond to user inputs step-by-step and decide when to call external tools.

**To solve tasks, agents use:**

- **planning**by devising step-by-step actions from the given task
- **tools**to extend their capabilities like RAG, external APIs, or code interpretation/execution
- **memory**to store and recall past interactions for additional contextual information

[What are Agents Used For?](https://langfuse.com#what-are-agents-used-for)

**Common use cases include:**

- **Customer Support:**AI agents use RAG to automate responses, autonomously take action and efficiently handle inquiries with accurate information.
- **Market Research**: Agents collect and synthesize information from various sources, delivering accurate and concise summaries to users.
- **Software Development:**AI agents break coding tasks into smaller sub-tasks and then recombine them to create a complete solution.

[Design Patterns of AI Agents](https://langfuse.com#design-patterns-of-ai-agents)

An AI agent usually consists of 5 parts: A language model with general-purpose capabilities that serves as the main brain or **coordinator**, and four sub-modules: a **planning module** to divide the task into smaller steps, an **action module** that enables the agent to use external tools, a **memory module** to store and recall past interactions and a **profile module**, to describe the behavior of the agent.

![AI Agent Design](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Fagent-design.png&w=3840&q=75)


In **single-agent setups**, one agent is responsible for solving the entire task autonomously. In **multi-agent setups**, multiple specialized agents collaborate, each handling different aspects of the task to achieve a common goal more efficiently. These agents are also often referred to as state-based or stateful agents as they route the task through different states.

![Single and Multi Agent
Designs](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Fmulti-agent.png&w=3840&q=75)


[What is AI Agent Observability?](https://langfuse.com#what-is-ai-agent-observability)

Observing agents means tracking and analyzing the performance, behavior, and interactions of AI agents. This includes real-time monitoring of multiple LLM calls, control flows, decision-making processes, and outputs to ensure agents operate efficiently and accurately.

[Langfuse](https://langfuse.com/) is an open-source AI engineering platform that provides deep insights into metrics such as latency, cost, and error rates, enabling developers to debug, optimize, and enhance their LLM systems. Using Langfuse observability, teams can identify and resolve issues, streamline workflows, and maintain high-quality outputs by evaluating agent responses in complex, multi-step AI agents.

[Industry Trends in Agent Observability](https://langfuse.com#industry-trends-in-agent-observability)

As AI agents become more prevalent in production, the observability landscape is evolving rapidly. The industry is converging on **OpenTelemetry (OTEL)** as a standard for collecting agent telemetry data, preventing vendor lock-in and enabling interoperability across frameworks. Many agent frameworks — including Pydantic AI, smolagents, and Strands Agents — now emit traces via OpenTelemetry, which [Langfuse natively supports](https://langfuse.com/docs/observability/sdk/instrumentation).

There is also a shift from reactive log-based monitoring to **proactive, structured tracing** with typed observation data. Rather than parsing unstructured logs after failures, teams now instrument agents with rich semantic types (tool calls, retriever steps, guardrail checks) for real-time insight into agent behavior.

Additionally, **cost optimization** is becoming critical as agent workloads scale. Agents that autonomously chain multiple LLM and API calls can incur unpredictable costs, making real-time cost tracking and per-trace cost attribution essential for production deployments.

[Why AI Agent Observability is Important](https://langfuse.com#why-ai-agent-observability-is-important)

[Debugging and Edge Cases](https://langfuse.com#debugging-and-edge-cases)

Agents use multiple steps to solve complex tasks, and inaccurate intermediary results can cause failures of the entire system. [Tracing](https://langfuse.com/docs/observability/overview) these intermediate steps and testing your application on known edge cases is essential.

When deploying LLMs, some edge cases will always slip through in initial testing. A proper analytics set-up helps identify these cases, allowing you to add them to future test sets for more robust agent evaluations. With [Datasets](https://langfuse.com/docs/evaluation/experiments/datasets), Langfuse allows you to collect examples of inputs and expected outputs to benchmark new releases before deployment. Datasets can be incrementally updated with new edge cases found in production and integrated with existing [CI/CD pipelines](https://langfuse.com/blog/2025-10-21-testing-llm-applications).

[Tradeoff of Accuracy and Costs](https://langfuse.com#tradeoff-of-accuracy-and-costs)

LLMs are stochastic by nature, meaning they are a statistical process that can produce errors or hallucinations. Calling language models multiple times while selecting the best or most common answer can increase accuracy. This can be a major advantage of using agentic workflows.

However, this comes with a cost. The tradeoff between accuracy and costs in LLM-based agents is crucial, as higher accuracy often leads to increased operational expenses. Often, the agent decides autonomously how many LLM calls or paid external API calls it needs to make to solve a task, potentially leading to high costs for single-task executions. Therefore, it is important to monitor model usage and costs in real-time.

Langfuse monitors both [costs](https://langfuse.com/docs/observability/features/token-and-cost-tracking) and [accuracy](https://langfuse.com/docs/evaluation/overview), enabling you to optimize your application for production.

[Understanding User Interactions](https://langfuse.com#understanding-user-interactions)

AI agents analytics allows you to capture how users interact with your LLM applications. This information is crucial for refining your AI application and tailoring responses to better meet user needs.

[Langfuse Analytics](https://langfuse.com/docs/metrics/overview) derives insights from production data, helping you measure quality through user feedback and model-based [scoring](https://langfuse.com/docs/evaluation/overview) over time and across different versions. It also allows you to monitor cost and latency metrics in real-time, broken down by user, session, geography, and model version, enabling precise optimizations for your LLM application.

[Tools to build AI Agents](https://langfuse.com#tools-to-build-ai-agents)

You do not need any specific tools to build AI agents. However, there are several open-source frameworks that can help you build complex, stateful, multi-agent applications.

[Application Frameworks](https://langfuse.com#application-frameworks)

[LangGraph](https://langfuse.com#langgraph)

LangGraph ([GitHub](https://github.com/langchain-ai/langgraph)) is an open-source framework by the LangChain team for building complex, stateful, multi-agent applications. LangGraph includes built-in persistence to save and resume state, which enables error recovery and human-in-the-loop workflows.

LangGraph agents can be [monitored with Langfuse](https://langfuse.com/guides/cookbook/integration_langgraph) to observe and debug the steps of an agent.

[Llama Agents](https://langfuse.com#llama-agents)

Llama Agents ([GitHub](https://github.com/run-llama/llama-agents)) is an open-source framework designed to simplify the process of building, iterating, and deploying multi-agent AI systems and turn your agents into production microservices.

Langfuse offers a simple [integration](https://langfuse.com/integrations/frameworks/llamaindex) for automatic capture of traces and metrics generated in LlamaIndex applications.

![Llama Agents Example trace in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Fllama-agents.png&w=3840&q=75)


[OpenAI Agents SDK](https://langfuse.com#openai-agents-sdk)

OpenAI Agents SDK provides a simple yet powerful framework for building and orchestrating AI agents. By instrumenting the SDK with Langfuse, you can capture detailed traces of agent execution, including planning, function calls, and multi-agent handoffs. This integration enables you to monitor performance metrics, trace issues in real time, and optimize your workflows effectively.

For a comprehensive guide on setting up this integration, please refer to our [Trace the OpenAI Agents SDK with Langfuse](https://langfuse.com/integrations/frameworks/openai-agents) notebook.

[Hugging Face smolagents](https://langfuse.com#hugging-face-smolagents)

Hugging Face smolagents is a minimalist framework for building AI agents. With the Langfuse integration, you can effortlessly capture and visualize telemetry data from your agents. By initializing the SmolagentsInstrumentor, your agent interactions are traced using OpenTelemetry and displayed in Langfuse, enabling you to debug and optimize decision-making processes.

For a comprehensive, step-by-step guide, see our integration notebook: [Observability for smolagents with Langfuse](https://langfuse.com/integrations/frameworks/smolagents).

![Smolagents Example trace in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fintegration-smolagents%2Fsmolagent_example_trace.png&w=3840&q=75)


[Pydantic AI](https://langfuse.com#pydantic-ai)

[Pydantic AI](https://ai.pydantic.dev/) brings Pydantic's type safety and ergonomic developer experience to agent development. You define your agent's inputs, tool signatures, and outputs as Python types, and the framework handles validation plus OpenTelemetry instrumentation under the hood. The result is a FastAPI-style developer experience for building production-ready agents.

For a step-by-step guide, see our integration notebook: [Trace Pydantic AI agents with Langfuse](https://langfuse.com/integrations/frameworks/pydantic-ai).

![Pydantic AI trace visualization in Langfuse](https://langfuse.com/_next/image?url=https%3A%2F%2Flangfuse.com%2Fimages%2Fcookbook%2Fotel-integration-pydantic-ai%2Fpydanticai-openai-trace-tree.png&w=3840&q=75)


[CrewAI](https://langfuse.com#crewai)

[CrewAI](https://github.com/crewAIInc/crewAI) is all about role-based collaboration among multiple agents. You assign each agent a distinct skillset or role, then let them cooperate to solve a problem. The framework offers a higher-level abstraction called a "Crew" that coordinates workflows, allowing agents to share context and build upon one another's contributions. It is well-suited for tasks requiring multiple specialists working in parallel.

For setup instructions, see our integration guide: [Trace CrewAI agents with Langfuse](https://langfuse.com/integrations/frameworks/crewai).

![CrewAI trace visualization in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-03-19-ai-agent-comparison%2Fcrewai-trace.png&w=3840&q=75)


[AutoGen](https://langfuse.com#autogen)

[AutoGen](https://github.com/microsoft/autogen), from Microsoft Research, frames agent interactions as asynchronous conversations among specialized agents. Each agent can be a ChatGPT-style assistant or a tool executor, and you orchestrate how they pass messages back and forth. This event-driven approach reduces blocking and is well-suited for longer tasks or scenarios requiring real-time concurrency.

For tracing setup, see: [Trace AutoGen agents with Langfuse](https://langfuse.com/integrations/frameworks/autogen).

![AutoGen trace visualization in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-03-19-ai-agent-comparison%2Fautogen-trace.png&w=3840&q=75)


[Strands Agents](https://langfuse.com#strands-agents)

[Strands Agents SDK](https://strandsagents.com) is a model-agnostic agent framework that runs anywhere and supports multiple model providers including Amazon Bedrock, Anthropic, OpenAI, and Ollama via LiteLLM. It emphasizes production readiness with first-class OpenTelemetry tracing, giving you end-to-end observability with a clean, declarative API for defining agent behavior.

For setup instructions, see: [Trace Strands Agents with Langfuse](https://langfuse.com/integrations/frameworks/strands-agents).

![Strands Agents trace visualization in Langfuse](https://langfuse.com/_next/image?url=https%3A%2F%2Flangfuse.com%2Fimages%2Fcookbook%2Fintegration_aws_strands_agents%2Fstrands-agents-trace.png&w=3840&q=75)


[Semantic Kernel](https://langfuse.com#semantic-kernel)

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) is Microsoft's approach to orchestrating AI "skills" and combining them into workflows. It supports multiple programming languages (C#, Python, Java) and focuses on enterprise readiness, including security, compliance, and Azure integration. You can create a range of skills — some powered by AI, others by pure code — and compose them into multi-step plans.

For tracing setup, see: [Trace Semantic Kernel with Langfuse](https://langfuse.com/integrations/frameworks/semantic-kernel).

![Semantic Kernel trace visualization in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-03-19-ai-agent-comparison%2Fsemantic-kernel-trace.png&w=3840&q=75)


[No-code Agent Builders](https://langfuse.com#no-code-agent-builders)

For prototypes and development by non-developers, no-code builders can be a great starting point.

[Flowise](https://langfuse.com#flowise)

Flowise ([GitHub](https://github.com/FlowiseAI/Flowise)) is a no-code builder. It lets you build customized LLM flows with a drag-and-drop editor. With the native Langfuse [integration](https://langfuse.com/integrations/no-code/flowise), you can use Flowise to quickly create complex LLM applications in no-code and then use Langfuse to analyze and improve them.

![Flowise Example](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Fflowise.jpg&w=3840&q=75)


*Example of a catalog chatbot created in Flowise to answer any questions
related to shop products.*

[Langflow](https://langfuse.com#langflow)

Langflow ([GitHub](https://github.com/logspace-ai/langflow)) is a UI for LangChain, designed with react-flow to provide an effortless way to experiment and prototype flows.

With the native [integration](https://langfuse.com/integrations/no-code/langflow), you can use Langflow to quickly create complex LLM applications in no code and then use Langfuse to monitor and debug them.

![Langflow Example](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Flangflow.jpg&w=3840&q=75)


*Example of a chat agent with chain-of-thought reasoning built in Langflow by
 Cobus Greyling.*

[Dify](https://langfuse.com#dify)

Dify ([GitHub](https://github.com/langgenius/dify)) is an open-source LLM app development platform. Using their Agent Builder nd variety of templates, you can easily build an AI agent and then grow it into a more complex system via Dify workflows.

With the native Langfuse [integration](https://langfuse.com/integrations/no-code/dify), you can use Dify to quickly create complex LLM applications and then use Langfuse to monitor and improve them.

![Dify Example](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fai-agent-observability%2Fdify.jpg&w=3840&q=75)


*Example of a Dify Agent that summarizes meetings.*

[Agent Evaluation and Testing](https://langfuse.com#agent-evaluation-and-testing)

Building an agent is only the first step. Agents can fail in nuanced ways — selecting the wrong tool, entering reasoning loops, or hallucinating in intermediate steps that produce a plausible-looking but incorrect final answer. To ship agents with confidence, you need a systematic approach to evaluation and testing.

[Why Evaluate Agents?](https://langfuse.com#why-evaluate-agents)

When working with agents, three problems show up again and again: **understanding**, **specification**, and **generalization**. You often lack understanding of what the agent actually does on real traffic because you are not systematically inspecting traces. The task is frequently underspecified — prompts and examples don't clearly encode what "good" behavior is, so the agent improvises in unpredictable ways. And even once you have tightened the spec, the agent may still struggle to generalize, performing well on handpicked examples but failing on slightly different real-world queries.

[Three Evaluation Strategies](https://langfuse.com#three-evaluation-strategies)

Langfuse supports three complementary strategies for evaluating agents:

-
**Final Response (Black-Box):**This method only looks at the user's input and the agent's final answer, ignoring the intermediate steps. It is flexible and easy to set up, but does not tell you*why*an agent failed.
-
**Trajectory (Glass-Box):**This strategy evaluates the full sequence of tool calls, reasoning steps, and decisions an agent made. You compare the actual trajectory against an expected one, catching issues like unnecessary tool calls, skipped steps, or inefficient reasoning paths.
-
**Single Step (White-Box):**This zooms in on individual steps within the agent's execution, evaluating whether each tool call returned the right result or each reasoning step was sound. It provides the most granular feedback for debugging specific failures.

[Three Phases of Evaluation](https://langfuse.com#three-phases-of-evaluation)

The evaluation process follows a natural progression as your application matures:

- **Phase 1 — Manual Tracing:**During early development, the most valuable activity is simply inspecting traces in Langfuse to understand your agent's reasoning.
- **Phase 2 — Online Evaluation:**As you get your first users, implement- [user feedback](https://langfuse.com/docs/observability/features/user-feedback)mechanisms and automated- [LLM-as-a-Judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)evaluators to flag problematic traces in real-time.
- **Phase 3 — Offline Evaluation:**At scale, create benchmark- [datasets](https://langfuse.com/docs/evaluation/experiments/datasets)of inputs and expected outputs, then run automated- [experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk)to test your agent before each release, preventing regressions and enabling confident iteration.

[Agent Evaluation Guides](https://langfuse.com#agent-evaluation-guides)

To dive deeper, explore these hands-on guides:

- [Agent Evaluation Guide](https://langfuse.com/guides/cookbook/example_pydantic_ai_mcp_agent_evaluation)— End-to-end walkthrough of all three evaluation strategies using Pydantic AI agents
- [Evaluating OpenAI Agents](https://langfuse.com/guides/cookbook/example_evaluating_openai_agents)— Online and offline evaluation for OpenAI Agents SDK
- [LangGraph Agent Evaluation](https://langfuse.com/guides/cookbook/example_langgraph_agents)— Monitoring and evaluating LangGraph agents
- [Synthetic Dataset Generation](https://langfuse.com/guides/cookbook/example_synthetic_datasets)— Scale test coverage with LLM-generated data for agent evaluation
- [Testing LLM Applications](https://langfuse.com/blog/2025-10-21-testing-llm-applications)— Build a testing foundation with deterministic checks and LLM judges

[Get Started](https://langfuse.com#get-started)

If you want to get started with building AI agents and monitoring them with Langfuse, here are the best places to begin:

- **Build and trace an agent:**Follow our- [end-to-end example](https://langfuse.com/guides/cookbook/integration_langgraph)of building a simple agent with LangGraph and tracking it with Langfuse.
- **Compare agent frameworks:**Read our- [AI Agent Comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison)blog post for an in-depth guide on when to use which framework.
- **Evaluate your agents:**Start with the- [Agent Evaluation Guide](https://langfuse.com/guides/cookbook/example_pydantic_ai_mcp_agent_evaluation)to set up black-box, trajectory, and step-level evaluations.
- **Explore all integrations:**Browse the full list of- [supported integrations](https://langfuse.com/integrations)to find the right setup for your stack.
