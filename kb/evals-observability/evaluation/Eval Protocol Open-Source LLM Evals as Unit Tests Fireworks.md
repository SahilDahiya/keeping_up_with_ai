---
title: 'Eval Protocol: Open-Source LLM Evals as Unit Tests | Fireworks'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Introduces Eval Protocol, an open-source spec for writing LLM evaluations
  as unit tests that travel from local prompt engineering through CI/CD regression
  checks to fine-tuning and RL.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/eval-protocol-llm-evaluation
author: null
published: '2025-08-04'
fetched: '2026-10-23T06:12:10Z'
classifier: claude
taxonomy_rev: 2
words: 586
content_sha256: 5925574d2144ce7b7a0dca6a0a532493e62574c0617ca22954deb546a0490b73
---

# Eval Protocol: Open-Source LLM Evals as Unit Tests | Fireworks

**Can I swap one model for another?** It is a simple question with no consistent method for answering confidently. Divergences of one for or another are hard to trap. So we set out to provide that method, and today launched [Eval Protocol](https://evalprotocol.io), an OSS library and SDK for making model evaluations work like unit tests, and through CI/CD automation.

## Introducing Eval Protocol (EP)

**EP is an open protocol that standardizes how developers author evaluations for large language model (LLM) applications**. EP provides a specification for writing evals and storing eval results that travel with developers from local model picking and prompt engineering, through production CI/CD, to automated fine-tuning and reinforcement learning for real-world use-cases- from simple markdown and JSON generation to complex customer service agents with tool calling.

EP bridges the gap between quick wins and long-term customization. Developers can start with immediate benefits like automated CI/CD checks to prevent regressions today, then scale to sophisticated multi-turn evaluations using Model Context Protocol (MCP) for agent optimization tomorrow.

![Evaluation Protocol Evaluation Protocol](https://fireworks.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fpv37i0yn%2Fhorizon%2F9858a893539ce3304bfa05c8e1793bce20256cf5-1536x1024.png%3Fauto%3Dformat&w=3840&q=75)

### Quickstart

EP can be installed with `pip install eval-protocol`

In this simple single-turn eval example, we run a mark for checking instruction-following test:

`pythonCopy`
12345678910111213141516171819202122232425262728293031

For a multi-turn example with MCP, check out our [τ²-bench implementation](https://evalprotocol.io/tutorial/multi-turn-eval-user-simulation).

### The Problem: LLM agents are software, but not developed with the same rigor

Building LLM apps involves juggling prompts, models, data, environments, and evals themselves. Today, developers face a fractured workflow: one-off scripts for model selection, disjointed tracing for production, and custom code for fine-tuning. Our opinion is that, if a developer wants to be confident with the quality of the LLM agent, we need to bring the same SDLC lifecycle back into LLM agents, with the familiar concepts of unit testing & CI/CD front and center. For example, you may have the following question around your application:

- Can I swap models without losing quality? (Manual swaps in API clients)
- Did my deployment cause a regression? Is my new prompt better or worse? (Ad-hoc scripts and console checks)
- Is my fine tuned model solving real problems?

### Three Core Workflows, One Protocol

EP is designed around your AI journey, with emphasis on getting quick value from CI/CD while paving the way for advanced customization.

1. **Local Evals & Model Picking:** Kick off in your notebook. Use the `eval-protocol` library to benchmark models on your use case. Answer “Can I switch from Claude to Kimi?” with reproducible results. Supports row-wise rewards for single-turn rollouts and test MCP for multi-turn simulations with user agents.
2. **Scale Up & CI/CD:** This is where EP shines for developers right now—no waiting for complex setups. Use the same eval suite on production logs for monitoring. Integrate into CI/CD via GitHub Actions: Run evals on PRs against golden datasets, get pass/fail comments with regression examples. Prevent issues before merge, ensuring “Did I break anything?” is answered automatically. Start simple with single-turn evals, then layer in MCP for multi-turn as your app grows.
3. **Customized model:** As things grow, EP helps you evaluate your own model and own your AI stack. Curate bad traces into datasets, and re-evaluate with your original suite for proven improvements. This carries you from basic quality gates on top of proprietary models to evaluating your customized models.

EP evolves with you.

### Resources:

- Get started with Installing Eval Protocol: `pip install eval-protocol`
- More Docs: [Introduction,](https://evalprotocol.io/introduction) [Single-turn Guide](https://evalprotocol.io/tutorial/single-turn-eval-static), [Multi-turn with τ²-bench](https://evalprotocol.io/tutorial/multi-turn-eval-user-simulation)
- GitHub Repository: [GitHub](https://github.com/eval-protocol/python-sdk)
- Join: [#eval-protocol](https://discord.com/channels/1137072072808472616/1400975572405850155) in our Discord for community support
