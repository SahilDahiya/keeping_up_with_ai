---
title: 'pydantic-deep: Production Deep Agents for Pydantic AI | Vstorm'
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- product-engineering/architecture
summary: 'Guest post from Vstorm introducing pydantic-deep, a ''deep agents'' framework
  on Pydantic AI (an alternative to LangChain''s deepagents) covering the production
  patterns: planning/progress tracking, filesystem as a first-class abstraction, sub-agent
  task delegation, sandboxed code execution in Docker, context summarization, and
  human-in-the-loop approval, with a full example app using per-user containers and
  WebSocket streaming.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/pydantic-deep-agents
author: Antoni Kozelski
published: '2026-03-18'
fetched: '2026-07-16T22:04:13Z'
classifier: claude
taxonomy_rev: 2
words: 1147
content_sha256: 8edc86f6c89a3f181c37f758dced2d0b85f575e6172a36f49adf560617a3a5af
---

# pydantic-deep: Production Deep Agents for Pydantic AI | Vstorm

*This piece is a guest post from Vstorm.*

If you take a moment to evaluate existing deep agents solutions, you will find a large gap. And for teams already invested in the Pydantic ecosystem, switching frameworks for Langchain's deepagents is not attractive.

Now [ pydantic-deep](https://github.com/vstorm-co/pydantic-deep?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents) bridges the gap, a heavy-duty extension framework for building "deep agents" that can plan, operate on files, delegate tasks, and execute code in isolated environments. Built on top of 

[Pydantic AI](https://github.com/pydantic/pydantic-ai?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents), it provides the same capabilities as LangChain's

[deepagents](https://github.com/langchain-ai/deepagents), but with the type safety, developer experience, and simplicity Pydantic users expect.

`pydantic-deep`

The call was to create deep agent capabilities with:

- **Type safety**throughout the entire codebase
- **Async-first design**for modern Python applications
- **Pydantic models**for structured inputs and outputs
- **Simpler mental models**than graph-based state machines
- **100% test coverage**for production confidence

The answer was to build [ pydantic-deep](https://github.com/vstorm-co/pydantic-deep?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents) on 

[pydantic-ai](https://github.com/pydantic/pydantic-ai?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents), Pydantic's official AI agent framework. By extending

[Pydantic AI](https://pydantic.dev/pydantic-ai?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents)with deep agent patterns, we deliver production-grade capabilities while maintaining the developer experience Pydantic users love.


Anyone who has deployed an AI agent to production knows the pattern: the demo works beautifully and the proof of concept impresses stakeholders. Then reality hits.

Real-world tasks are not single-step operations. When a user asks an agent to "analyze this CSV file and create a visualization," the agent needs to:

- **Plan**the approach and break down the task
- **Read**the file from storage
- **Write**analysis code
- **Execute**the code in a safe environment
- **Handle errors**and retry if something fails
- **Track progress**so users know what is happening

Simple agents with a handful of tools cannot handle this complexity reliably. They lose track of multi-step tasks, cannot recover from errors gracefully, and provide no visibility into their reasoning process.

Production agents need architecture patterns that address these challenges systematically.


Deep agents represent a maturation of AI agent design. The term, popularized by LangChain's research into production systems, describes agents with specific architectural capabilities:

- **Planning and Progress Tracking**- Deep agents break complex tasks into steps and track their progress. Users can see what the agent is working on, what it has completed, and what remains.
- **File System Operations**- Real work requires reading, writing, and editing files. Deep agents treat the file system as a first-class citizen, with proper abstraction layers that work across in-memory storage, real file systems, and sandboxed containers.
- **Task Delegation**- Some tasks benefit from specialized sub-agents. A coding agent might delegate documentation writing to a specialized sub-agent with different instructions and capabilities.
- **Sandboxed Execution**- Running code that an AI generates is inherently risky. Deep agents execute code in isolated environments, typically Docker containers, preventing accidents from affecting the host system.
- **Context Management**- Long conversations exceed token limits. Deep agents automatically summarize older context while preserving essential information, enabling sessions that span hours or days.
- **Human-in-the-Loop**- Certain operations require human approval before execution. Deep agents support approval workflows for dangerous operations like code execution or file deletion.

These patterns emerged from teams building production agents and discovering what actually works at scale.


To demonstrate pydantic-deep's capabilities in a production-like environment, here is a [full example application](https://github.com/vstorm-co/pydantic-deep/tree/main/examples/full_app?utm_source=pydantic&utm_medium=blog&utm_campaign=pydantic-deep-agents) that showcases every feature working together. You can watch the [demo video below](https://youtu.be/AhV5DqiHn7E) to see it in action.


- **Multi-User Session Management**- Each user receives an isolated Docker container. Sessions persist across page refreshes and clean up automatically after idle timeout.
- **WebSocket Streaming**- Real-time streaming of agent responses, including text generation, thinking content (for reasoning models), tool calls, and tool results.
- **File Upload and Processing**- Users upload CSV, PDF, or text files. The agent accesses these files in its sandbox and can analyze, transform, or reference them.
- **Custom Tools**- Mock GitHub tools demonstrate how to extend pydantic-deep with domain-specific capabilities. The pattern works identically for real API integrations.
- **Human-in-the-Loop**- Code execution requires user approval. The frontend displays the proposed command and waits for confirmation before proceeding.
- **Skills in Action**- A data analysis skill provides the agent with pandas expertise, visualization templates, and best practices for working with CSV data.
- **Sub-Agent Delegation**- A joke generator sub-agent demonstrates task delegation. When users ask for humor, the main agent delegates to the specialized sub-agent.
- **Todo Progress Tracking**- The frontend displays the agent's todo list in real-time, showing users exactly what the agent is working on.


The application demonstrates several production patterns:

- **Stateless Agent, Stateful Sessions**- The agent itself is stateless and shared across all users. Per-user state lives in session objects that hold the Docker sandbox, message history, and todo list.
- **Backend Injection at Runtime**- The agent is configured without a backend. Each session provides its own DockerSandbox, enabling per-user isolation without creating multiple agent instances.
- **Approval Flow**- When the agent calls a tool requiring approval, it returns a DeferredToolRequests object. The application presents this to the user, collects their decision, and resumes the agent with DeferredToolResults.

Deep agents represent the current state of the art in production AI systems. The patterns; planning, file operations, task delegation, sandboxed execution, context management, and human oversight; all emerged from teams solving real problems at scale.

With pydantic-deep, these patterns are now available in the Pydantic ecosystem. Whether you are building a coding assistant, data analysis tool, or any AI application that needs to interact with the world, pydantic-deep provides a solid, type-safe foundation.

The framework reflects Vstorm's experience building production AI systems for clients across industries. We have seen what works and what fails, and we have encoded those lessons into a library that handles the hard parts so you can focus on your application's unique value.


**What is pydantic-deep and how does it relate to deep agents?**

Deep agents are production-grade AI agents that go beyond simple tool calling: they plan multi-step tasks, operate on files, delegate work to sub-agents, execute code in sandboxed containers, and support human-in-the-loop approval. pydantic-deep is an open-source framework that brings these capabilities to the Pydantic ecosystem, built on top of Pydantic AI.

**How does pydantic-deep compare to LangChain's deepagents?**

pydantic-deep provides the same deep agent capabilities as LangChain's deepagents but is built on Pydantic AI. It offers full type safety, async-first design, Pydantic models for structured inputs and outputs, and simpler mental models than graph-based state machines.

**Does pydantic-deep support sandboxed code execution?**

Yes. pydantic-deep executes AI-generated code in isolated Docker containers, preventing accidents from affecting the host system. Each user receives an isolated container with sessions that persist across page refreshes and clean up automatically after idle timeout.

**Does pydantic-deep support human-in-the-loop workflows?**

Yes. When the agent calls a tool requiring approval, it returns a DeferredToolRequests object. The application presents this to the user, collects their decision, and resumes the agent with DeferredToolResults. This enables approval workflows for dangerous operations like code execution or file deletion.


Ready to build deep agents with Pydantic AI? Check out the resources below:
