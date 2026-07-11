---
title: 'Tau-Bench: Benchmarking AI agents for the real-world'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/planning
summary: Introduces tau-Bench as a benchmark for real-world AI agents, focusing on
  task completion, tool use, and operational realism.
source: sierra
url: https://sierra.ai/blog/benchmarking-ai-agents
author: Karthik Narasimhan
published: '2026-05-12'
fetched: '2026-07-11T03:53:53Z'
classifier: codex
taxonomy_rev: 1
words: 1485
content_sha256: 019fb80ccdbafd69de803268ccfc35a4de57bad867749c1a894a5edf661a7b20
---

# Tau-Bench: Benchmarking AI agents for the real-world

# Tau-Bench: Benchmarking AI agents for the real-world

## TL;DR

- Sierra’s AI research team is on a mission to advance the frontier of conversational AI agents. In our [new research paper,](https://arxiv.org/abs/2406.12045)we present a new benchmark, 𝜏-bench, for evaluating AI agents' performance and reliability in real-world settings with dynamic user and tool interaction.
- There is a dearth of good benchmarks to measure the reliability of agents in dynamic real-world scenarios with humans in the loop. 𝜏-bench tests agents on completing complex tasks while interacting with (LLM-simulated) users and tools to gather required information.
- Results show that agents built with simple LLM constructs (like function calling or [ReAct](https://arxiv.org/abs/2210.03629)) perform poorly on even relatively simple tasks, highlighting the need for more sophisticated agent architectures.

## Background

[AI agents](https://sierra.ai/blog/ai-agents-guide) are autonomous software systems that are powered by LLMs, enabling them to reason, make decisions, and pursue goals with creativity and flexibility, all while staying within the bounds that have been set for them. Agents have incredible applications across a wide range of tasks, from handling simple information exchanges and question answering, to complex troubleshooting and problem solving. At Sierra, our experience in enabling real-world user-facing conversational agents has made one thing extremely clear: a robust measurement of agent performance and reliability is critical to their successful deployment. Before companies deploy an AI agent, they need to measure how well it is working in as realistic a scenario as possible.

The research community has built several benchmarks for AI agents in the last few years ([WebArena](https://arxiv.org/abs/2307.13854), [SWE-bench](https://arxiv.org/abs/2310.06770), [Agentbench](https://arxiv.org/abs/2308.03688) to name a few), but they all fall short in a number of critical areas. While these benchmarks are useful for revealing an agent’s high-level capabilities, they only evaluate a single round of human-agent interaction in which all necessary information is exchanged at once. This is in stark contrast to real-life scenarios where agents gather information over multiple, dynamic exchanges. Moreover, these benchmarks typically focus their evaluation on first-order statistics like average performance and do not provide measures of reliability or adaptability.

We built 𝜏-bench to address this gap. Drawing on our experience with live agents in production, we distilled the requirements for a realistic agent benchmark to three key points. First and foremost, most real-world settings require agents to interact seamlessly with **both** humans and programmatic APIs over long horizons, in order to incrementally gather information and solve complex problems. Second, agents must be able to accurately follow complex policies or rules specific to the task or domain. This is critical to ensure the agent does not violate company policies or produce unwanted behavior. Third, agents must maintain consistency and reliability at scale, across millions of interactions. This ensures predictable agent behavior, and peace of mind for the company deploying it.

𝜏-bench incorporates all of these elements into a single modular framework for evaluating and developing agents for real-world use cases.

## TAU (𝜏)-Bench: A tool-agent-user benchmark

At a high level, 𝜏-bench measures an agent’s ability to interact with (simulated) human users and programmatic APIs while following domain-specific policies in a consistent manner. The benchmark contains several tasks for testing agents built using a modular framework with (1) realistic databases and tool APIs, (2) domain-specific policy documents dictating the behavior required of the agent, and (3) an LLM-based user simulator guided by instructions for diverse scenarios to produce realistic user utterances with the agent.

Each task in 𝜏-bench tests an agent's ability to follow rules, reason, remember information over long and complex contexts, and communicate effectively in realistic conversations. We used a stateful evaluation scheme that compares the database state after each task completion with the expected outcome, allowing us to objectively measure the agent's decision-making. This method also provides room for variations in conversation responses. Additionally, we introduce a new metric, pass^k, which measures the agent's reliability and determines if it can successfully complete the same task multiple times (k representing the number of different trials).

Here are the key features of 𝜏-bench:

- Realistic dialog and tool use: Thanks to the advances in generative modeling for language, 𝜏-bench features complex databases and realistic user simulation. Notably, prompting LLMs allows us to create interesting and varied user scenarios specified in natural language as opposed to writing complex rules.
- Open-ended and diverse tasks: 𝜏-bench’s data schemas, APIs and policy documents are rich enough to support the creation of diverse, open-ended and creative tasks for the agent.
- Faithful objective evaluation: 𝜏-bench’s focus on evaluating agents on goal database state (as opposed to evaluating the conversation itself) allows for fast and faithful assessment of agent capabilities, alleviating the need for any human or LLM-based evaluation.
- Modular framework: 𝜏-bench is built to be modular and allow for easy addition of new domains, database entries, rules, APIs, tasks and evaluation metrics.

We constructed 𝜏-bench in three stages:

- Stage 1: We manually designed the database schema, APIs and policies, inspired by real-world use cases in customer support.
- Stage 2: Once the data schema was set up, we leveraged LLMs (GPT-4) to generate code snippets that can generate data entries at scale.
- Stage 3: We manually generated scenarios for user simulation for each task along with the target goal state, and verified the correctness of the task before adding it to the benchmark.

Using the above procedures, we constructed two domains – 𝜏-retail and 𝜏-airline, dealing with common use cases in the corresponding sectors. We chose these domains since they provide a nice balance between ease of data synthesis and policy specification, and potential for diverse, realistic applications. You can read more about the methodology for the benchmark construction in [the paper](https://arxiv.org/abs/2406.12045).

## Key findings

Most AI agents are relatively simple, predominantly built using function calling or the ReAct framework, which involves the LLM generating API-calls to take actions. As a first use of 𝜏-bench, we evaluated these types of AI agents as powered by 12 popular LLMs, both proprietary and open models. We find that all 12 of these agents we tested have difficulties solving tasks in 𝜏-bench, with even the best performing GPT-4o agent achieving <50% average success rate across the two domains.

What’s even more interesting is that all the tested agents perform extremely poorly on the reliability test and are unable to consistently solve the exact same task when the episode is re-run (note that since the user is simulated, we can generate a variety of lexical variations in the utterances while keeping the underlying task semantics unchanged simply by re-running the task). For instance, the agent powered by GPT-4o drops to ~25% on pass^8 in 𝜏-retail, which is a staggering 60% drop compared to its corresponding pass^1 score. Practically, this means that there is only a 25% chance that the agent will resolve 8 cases of the same issue with different customers – a number that is far behind the expectation of a real-world user-facing agent.

We further analyze the failure cases manually and break them down into four quadrants, which provide actionable insights into improving agent capabilities. The key challenges lie around improving their ability to follow rules consistently, plan over long horizons and focus on the right pieces of information in the conversation, especially when there may be conflicting facts present. In particular, we find that function calling agents are not great at following rules provided in the policy documents.

## Towards more reliable agents in the real world

Sierra agents have a broader set of capabilities than those described in the findings, above. First, Sierra’s Agent SDK enables developers to declaratively specify agent behavior, orchestrating them to accurately execute complex tasks. Sierra agents are also governed by supervisory LM models which ensure that agent performance is consistent and predictable, while also adapting easily to unique dialogue and infinite user scenarios. As we deploy and evaluate agents, our [Agent Development Life Cycle](https://sierra.ai/blog/agent-development-life-cycle) allows for rapid iteration to improve agent quality and ensure compliance with domain-specific policies. We plan to use 𝜏-bench to help compile, tailor, and fine-tune our constellation of models for superior performance. Additionally, our research team is working on new specification frameworks and cognitive architectures to enable more reliable and consistent agents.

While 𝜏-bench provides a new take on dynamic agent evaluation, there are still several directions for future improvement of the benchmark. First, we can improve the fidelity of user simulation through more advanced LLMs that can improve reasoning and planning, along with creating more complex scenarios. Second, we can build new methods to reduce the difficulty of annotation through the use of automated tools. Finally, we can develop more fine-grained evaluation metrics that test other aspects of the agent’s behavior in the conversation (e.g. use of appropriate tone and style). We hope the AI research community will find 𝜏-bench useful in developing more capable and reliable AI agents and build on the benchmark for more advanced evaluation.

You can find the code and data for 𝜏-bench [here](https://github.com/sierra-research/tau-bench).
