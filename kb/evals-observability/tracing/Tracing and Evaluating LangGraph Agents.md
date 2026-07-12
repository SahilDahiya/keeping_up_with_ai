---
title: Tracing and Evaluating LangGraph Agents
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/planning
summary: Covers tracing and evaluation patterns for LangGraph agents, linking graph-based
  control flow with observability.
source: arize
url: https://arize.com/blog/langgraph/
author: Greg Chase
published: '2024-10-16'
fetched: '2026-07-11T04:50:16Z'
classifier: codex
taxonomy_rev: 1
words: 1028
content_sha256: ad1af67b8989279b5af14a3dfeb8a46bbd343d3826a1e557e1e0477a61b1d245
---

# Tracing and Evaluating LangGraph Agents

[LangGraph](https://langchain-ai.github.io/langgraph/) is a powerful library designed for building stateful, multi-actor applications within large language models (LLMs). In this post, we’ll discuss how LangGraph’s traces can be ingested into Arize, and how to leverage LLMs as a judge to evaluate LangGraph agent performance.

## What is LangGraph?

LangGraph is a flexible, low-level framework that allows developers to build agents and multi-agent workflows. Unlike Directed Acyclic Graph (DAG)-based solutions, LangGraph supports cycles, which are crucial for creating agents. The framework also provides greater control over the flow and state of an application, making it easier to manage complex agent interactions. A key feature is its built-in persistence, enabling advanced memory and cumulative loop functions.

LangGraph is also one of the most popular agent frameworks, which means there are a ton of example projects and tutorials to work from. LangGraph is a great option for anyone to build agents, regardless of skill level.

## LangGraph Structure

LangGraph provides a few abstractions that make building agents much easier. These core abstractions include **nodes**, **edges**, and **conditional edges**, all of which play a vital role in structuring agent workflows.

- **Nodes**: In LangGraph, nodes represent individual units of work or tasks that an agent performs. Each node can encapsulate any specific function, such as fetching data from a database, invoking an external API, or processing a computation. Nodes are the building blocks of the agent’s workflow, and they are responsible for both the action taken and updating the internal state of the agent as the workflow progresses. Nodes in LangGraph can also interact with Langchain abstractions, such as tools, prompts, or memory buffers, allowing them to leverage pre-built capabilities of the Langchain ecosystem.
- **Edges**: Edges define the relationships and flow between nodes. They indicate how data and state are transferred from one node to another, allowing for the seamless progression of tasks. These edges essentially map the order of execution, guiding the agent from one task to the next. When a node completes its task, the edge determines where the result flows and which node is triggered next in the sequence.
- **Conditional Edges**: Conditional edges are specialized edges that introduce decision-making logic into the workflow. Rather than simply following a linear path, conditional edges enable agents to evaluate criteria before choosing the next node. For example, after processing some data, the agent may take one path if a condition is met (e.g., if a query returns a valid result) and a different path if the condition is not met (e.g., retrying the task or invoking error-handling logic). This makes workflows highly flexible, as agents can dynamically adapt based on real-time information or results.

It also goes without saying that the framework also works seamlessly with Langchain abstractions. The combination of these two libraries can significantly streamline the agent construction process.

## The Importance of State in LangGraph

State is central to how LangGraph operates. Each execution of the graph creates a state that is passed between the nodes, with each node updating the internal state as it executes. This process allows the graph to maintain context and memory, critical for stateful applications. The state can be customized based on the graph type or custom functions, ensuring flexibility and adaptability for different agent workflows.

## SQL Agent Example

- See here for the [full notebook](https://colab.research.google.com/github/Arize-ai/tutorials_python/blob/main/Arize_Tutorials/Tracing/Arize_Tutorial_LangGraph_SQL_Agent.ipynb)

Now let’s look at an example. We’ve built an SQL agent that answers queries from a SQL database. The process is broken down into several key steps, represented as nodes in LangGraph:

- Fetch available tables – Retrieve all available tables from the database.
- Identify relevant tables – Determine which tables are relevant to the question being asked.
- Fetch Data Definition Language (DDL) – Gather the DDL for the relevant tables.
- Generate the SQL query – Formulate the SQL query based on the question and the table information.
- Validate the query – Use an LLM to check for common SQL mistakes.
- Execute the query – Run the SQL query and return the results.
- Error handling – Correct any errors surfaced by the database until the query succeeds.
- Formulate a response – Generate a response based on the SQL results.

![](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-04-at-1.49.00 PM-474x1024.png)

## Ingesting Traces into Arize

Arize provides an auto-instrumentor for Langchain, which works with LangGraph as well. Enabling this auto-instrumentor will automatically capture and trace any calls made to the framework. These traces are then ingested into Arize, where each unit of work within the agent—such as chains or tools—appears as individual spans in the trace. This level of traceability is crucial for monitoring agent performance and identifying bottlenecks.

*Note: The same auto-instrumentor will work for Arize Phoenix, our OSS platform, as well.*

![](https://arize.com/wp-content/uploads/2024/10/langgraph_arize_perf_tracing_20241003-1024x404.png)

![](https://arize.com/wp-content/uploads/2024/10/langgraph_arize_trace_20241003-1024x555.png)

## Evaluating SQL Agents with LLMs as Judges

Once the agent traces are ingested, we’ll run two evaluations to measure the agent’s effectiveness:

- SQL generation accuracy – This evaluation checks whether the SQL queries generated by the agent are correct based on the questions asked.
- AI vs. Human Ground Truth Evaluation – This test compares the agent’s answers to a human-provided ground truth. By evaluating the agent’s responses against a golden dataset, we can measure the agent’s accuracy in answering questions.

Both of these evaluations use an LLM-as-a-Judge approach, meaning we are passing the relevant input and output fields to a separate LLM to judge their correctness or accuracy. You can [read more about LLM-as-a-Judge here](https://arize.com/blog-course/llm-evaluation-the-definitive-guide#llm-as-judge).

Once these traces have been labeled by the corresponding evaluations, we can visualize those metrics within the Arize dashboard.

![](https://arize.com/wp-content/uploads/2024/10/langgraph_arize_trace_evals_20241003-1024x554.png)

## Harnessing the Power of LangGraph and Arize

LangGraph offers a robust framework for building stateful agents with advanced memory and persistence features. Coupled with Arize’s trace ingestion and LLM-based evaluations, it provides a comprehensive solution for monitoring and improving agent performance. By tracking agent behavior over time, developers can ensure their agents remain reliable and effective in a variety of tasks.

Ready to improve your agent workflows? Start using [ LangGraph](https://langchain-ai.github.io/langgraph/) to build robust, stateful agents today and integrate it with

[to monitor and enhance performance. You can also try](https://arize.com/)

**Arize**[, our open-source LLM observability tool, and star its](https://phoenix.arize.com)

**Phoenix**[GitHub repository](https://github.com/Arize-ai/phoenix)if you find it useful!
