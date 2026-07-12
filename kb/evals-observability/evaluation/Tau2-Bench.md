---
title: Tau2-Bench
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/multi-agent
summary: Introduces tau2-bench for evaluating agents in collaborative real-world scenarios
  where task success depends on interaction dynamics.
source: sierra
url: https://sierra.ai/blog/benchmarking-agents-in-collaborative-real-world-scenarios
author: Victor Barres; Honghua Dong; Soham Ray; Karthik Narasimhan
published: '2026-05-12'
fetched: '2026-07-11T03:53:11Z'
classifier: codex
taxonomy_rev: 1
words: 1235
content_sha256: fd50a89156c8d08bcdd5e6c49a69c7dc855de1f0f2edfece6d4e2c47a406f2fb
---

# Tau2-Bench

# 𝜏²-bench: benchmarking agents in collaborative real-world scenarios

One year ago, we introduced [𝜏-bench](https://sierra.ai/blog/benchmarking-ai-agents): a new kind of benchmark that challenges AI agents to complete realistic, multi-turn tasks while following domain-specific policies and using tools programmatically. It showed that while LLMs can look impressive on paper, they often falter when it comes to reliably solving the same task multiple times.

And a few months ago, we showed [how 𝜏-bench has rapidly influenced academic research and industrial evaluation pipelines](https://sierra.ai/blog/tau-bench-shaping-development-evaluation-agents), and how the reliability metric pass^k is reshaping how agent performance is measured. But we also noted a key limitation: all these tasks assumed the agent had full control over its environment.

However, that assumption rarely holds true. Take tech support. The agent can look up your account or reset a backend flag, but you still need to reboot your phone or change a setting. The success of the interaction depends on both participants working together to solve the problem.

This is the world of dual control, and it's where 𝜏²-bench comes in.

𝜏²-bench challenges AI agents not just to reason and act, but to coordinate, guide, and assist a user in achieving a shared objective. This leap from solo operation to co-ownership of a task pushes agents into a much more demanding space. And, critically, it reflects the kinds of tasks AI agents are increasingly being asked to perform in the real world.

## A dual-control benchmark for collaborative agents

𝜏²-bench builds on the 𝜏-bench foundation but adds a new dimension of complexity: the shared action space between agent and user. It introduces a telecom troubleshooting domain designed around real-world scenarios where the user must actively perform steps while the agent assists remotely.

This distinction is crucial for real-world applications, where users aren't passive observers. They're part of the loop. The design of 𝜏²-bench acknowledges this critical reality by evaluating how well an agent can collaborate, communicate, and coordinate in environments where agency is shared. Agents are now required to explicitly model the user as an actor, reason about their abilities and likely actions, and ensure that guidance is both timely and accurate.

In 𝜏²-bench, the environment is co-owned by the agent and the user. The agent may toggle backend features or query network settings, while the user is responsible for verifying on-device status, rebooting hardware, or changing configurations. 𝜏²-bench supports two distinct operating modes:

- **Solo mode:**The agent has full control and performs all actions on behalf of the user.
- **Interactive mode:**The agent guides the user through their responsibilities while simultaneously managing its own tools.

These scenarios were inspired by the kinds of issues real users encounter when dealing with telecom support, such as fixing broken data connections, resolving issues with Multimedia Messaging Service (MMS), or switching mobile network modes. To complete each task, the agent must correctly follow telecom policy documents, communicate instructions, wait for user feedback, and update its strategy accordingly. Errors in any of these steps can derail task completion.

## Collaboration is hard

We evaluated multiple LLM-based agents using 𝜏²-bench, comparing performance across solo and interactive modes. The result? A drop of up to 25 points in task success rate when agents moved from solo to interactive mode, even those built on top-tier LLMs, such as GPT‑4.1 and o4-mini. While these agents might appear intelligent in a single-exchange chat, their ability to manage complex, unfolding collaborative tasks is limited.

This dramatic falloff in task performance highlights the steep difficulty gradient introduced by dual-control environments: effective collaboration is not trivial. In interactive settings, agents must not only issue precise, understandable instructions but must also model the user's context and cognitive load. It’s not enough to say, "Turn on data roaming"—the agent must ensure the user understands how to navigate their device settings, verify when the action is done, and adapt if something goes wrong.

This type of interaction is fragile, as miscommunication and unexpected user behavior complicate the agent's task. 𝜏²-bench exposes these pain points with clinical clarity, forcing developers to grapple with what it really means for an agent to be helpful.

## A new kind of task generation engine

Beyond the shift to dual control, 𝜏²-bench also includes foundational improvements to benchmark construction itself. Rather than relying on manually authored scenarios, 𝜏²-bench uses a compositional task generator.

Tasks are built from a library of smaller, verifiable atomic actions. These components allow researchers to mix and match steps like "toggle mobile data," "check data limit," or "adjust network mode" into new and increasingly complex workflows. This not only ensures better domain coverage but also allows for systematic control of task complexity, enabling precise experiments on model performance.

This task generator eliminates the need for laborious manual scenario writing while ensuring that each task can be automatically verified for correctness. Every completed task leaves a measurable footprint on the simulated environment: a change in system state, a flag update, or a resolved error. This allows researchers to assess agent behavior objectively, without relying on subjective grading or LLM-based evaluation.

## Upgraded simulators for consistent evaluation

𝜏²-bench also introduces substantial improvements to user simulation reliability. In many benchmarks, user simulators are error-prone or unpredictable, making it difficult to disentangle agent mistakes from simulation noise. To address this, 𝜏²-bench tightly couples the user simulator to the environment across the telecom domain, constraining user behavior through available tools and observable states.

Each simulated user is constrained by the available tools and observable state. For instance, the simulator won’t invent device settings that don’t exist or make contradictory statements about network status. Instead, it generates responses based on the real configuration of the environment, which the agent can also observe or query.

We also performed a full audit of simulators across all domains, including the earlier Airline and Retail domains introduced in the original 𝜏-bench. This verification process surfaced common failure modes—such as premature conversation termination or missing constraints—and allowed us to patch simulation logic for better reliability and realism.

## Expanding the frontier of agent evaluation

𝜏²-bench is a step forward in the pursuit of robust, user-centered AI. It opens up several promising directions for future work.

One is expanding to multi-user collaboration: scenarios where agents must navigate conversations involving several participants, such as family account setups, enterprise tech support, or shared financial decision-making.

Another is developing interaction-sensitive reward functions that reward agents not just for completing a task, but for doing so smoothly, politely, and efficiently. This would allow researchers to begin optimizing for quality of interaction, not just success rates.

We also see room for integration with human-in-the-loop training, where real users guide model improvement by identifying where collaborative behaviors break down. And finally, 𝜏²-bench paves the way for future domains—healthcare, legal services, education—where shared control and guided instruction are the norm.

## Benchmarks that reflect the real world

𝜏²-bench challenges agents to thrive in the messy, collaborative environments where real work gets done. It's not enough to act autonomously. The next generation of AI must learn to act with us. If you build or evaluate conversational agents, we encourage you to integrate 𝜏²-bench into your development loop. Benchmarks like 𝜏²-bench help the field converge on what matters: not just correctness, but cooperation.

We’re excited to continue refining the benchmark, expanding to new domains, and learning from the community’s contributions. Explore 𝜏²-bench on [GitHub](https://github.com/sierra-research/tau2-bench ), read the paper on [arXiv](https://arxiv.org/abs/2506.07982), and let us know what you'd like to see next at [research@sierra.ai](mailto:research@sierra.ai.).
