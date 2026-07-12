---
title: Scalable Chain of Thoughts via Elastic Reasoning
topic: models
subtopic: reasoning
secondary_topics: []
summary: Summarizes elastic reasoning and scalable chain-of-thought ideas for allocating
  reasoning compute more flexibly.
source: arize
url: https://arize.com/blog/scalable-chain-of-thoughts-via-elastic-reasoning/
author: Sarah Welsh
published: '2025-05-16'
fetched: '2026-07-11T04:52:17Z'
classifier: codex
taxonomy_rev: 1
words: 959
content_sha256: f3875426b16523193bf3487e9ed14668fa5e180fc3be9ddadb735909821ea562
---

# Scalable Chain of Thoughts via Elastic Reasoning

This paper introduces Elastic Reasoning, a novel framework designed to enhance the efficiency and scalability of large reasoning models (LRMs) by explicitly separating the reasoning process into two distinct phases: thinking and solution. This separation allows for independent allocation of computational budgets, addressing challenges related to uncontrolled output lengths in real-world deployments with strict resource constraints.

This discussion will explore how Elastic Reasoning contributes to more concise and efficient reasoning, even in unconstrained settings, and its implications for deploying LRMs in resource-limited environments.

## Watch

## Listen

## Dive in

- Read [Scalable Chain of Thoughts via Elastic Reasoning](https://arxiv.org/abs/2505.05315)
- Sign up for[future paper readings](https://arxiv.org/pdf/2505.05315)

## Summary: Scalable Chain of Thoughts via Elastic Reasoning

Large Language Models (LLMs) have become incredibly powerful, especially when using Chain-of-Thought (CoT) prompting to break down complex problems step-by-step. This structured reasoning process enables Large Reasoning Models (LRMs) to achieve state-of-the-art results on tasks like math and programming. However, there’s a catch: these CoT outputs can be excessively long and unpredictable. This leads to high test-time compute costs—more tokens, longer latency, and greater GPU usage. For real-world, user-facing applications, high latency can cause user drop-off, while higher compute costs hurt providers.

## The Challenge of Length Control

Previous attempts to manage CoT output length have had notable limitations. The S1 method, which forces the model to emit a “Final Answer” token, often sacrifices accuracy by ignoring nuanced conclusions. L1 uses reinforcement learning (RL) to impose length constraints but demands heavy training resources and still results in performance degradation. Naively truncating output is risky—the model might never reach its final answer.

## The Core Idea: Separate Thinking and Solution

The paper “Scalable Chain of Thoughts via Elastic Reasoning” introduces a novel solution: explicitly separating the reasoning process into two distinct stages—thinking and solution—each with its own token budget. This separation is a game-changer.

Why split? Having a dedicated thinking phase allows the model to explore options, much like a rough draft, while the solution phase summarizes and finalizes the answer. This structured split not only improves performance but also ensures that the final answer is not lost due to token limits. While the process mimics human drafting, the transition is an abrupt shift to summarization—a trade-off that boosts interpretability and guarantees output completeness.

## How Elastic Reasoning Works

Elastic Reasoning implements this split through two key mechanisms: Separate Budgeting for Inference, and Budget-Constrained Rollout.

### Separate Budgeting for Inference

- The total token budget c is divided into a thinking budget t and a solution budget s, where c = t + s.
- The model generates reasoning within a block.
- If it emits before reaching the t-token limit, it smoothly transitions to the solution phase.
- If it doesn’t, the model is forced to stop reasoning by appending and immediately starts the solution phase.
- This guarantees both reasoning and a final answer are included. The solution phase always receives its token allocation, making this method more reliable than S1 or naive truncation.

### Budget-Constrained Rollout (Training Strategy)

- An RL fine-tuning strategy using the GRPO algorithm trains the model to handle truncated reasoning.
- Training simulates the budgeting setup, using fixed budget pairs (e.g., 1K thinking, 1K solution).
- The model learns to front-load useful information and reason adaptively within constraints.
- This training approach requires 75% fewer RL steps than L1 and generalizes well to new budget configurations at test time.
- Strong Results Across the Board

Elastic Reasoning achieves impressive results on benchmark tasks…

- **Accuracy Under Tight Budgets:**The E1-Math-1.5B model maintains high accuracy even with reduced token budgets, outperforming S1 and L1-Exact across varying conditions.
- **Significant Cost Savings:**Token usage drops by over 30% on AIME2024 and 37% on LiveCodeBench, leading to substantial inference cost reductions.
- **Concise Reasoning:**E1 models produce shorter, more efficient reasoning trajectories without sacrificing performance—even when unconstrained.
- **Budget Generalization:**Training with fixed budgets (like 1K/1K) enables effective generalization to new budget splits, without retraining.
- **Code Task Performance:**The E1-Code-14B model shows scalable improvements as token budgets increase and performs strongly on Codeforces and
- HumanEval Plus, while reducing token usage.
- **Improved Components:**Both the thinking and solution segments improve through training, with especially strong gains in the solution phase under constrained thinking.
- **Practical Insights:**Hallucinations, Evals, and Applications

The paper also offers deeper insights into real-world applications:

- **Hallucination Handling:**Forcibly cutting the thinking phase doesn’t eliminate hallucinations, but the structure helps with debugging. You can inspect the reasoning to trace where things went wrong.
- **Evaluation Considerations:**CoT models require evaluating reasoning alongside answers. In some tasks, reasoning might not help and could even hurt performance. Elastic Reasoning lets teams dial down reasoning depth for simpler problems.
- **Extending to Multi-Tool Agents:**The concept of budgeted components could expand to agents using external tools, assigning budgets for “tool call” tokens alongside thinking and solution. This will require further research.
- **Best-Fit Use Cases:**Elastic Reasoning shines in latency-sensitive and token-constrained environments—like chatbots and math/code assistants—where every millisecond and token counts.
- **Where It Falls Short:**Applications that need untruncated reasoning (e.g., for auditing, research, or writing) may not benefit as much.
- **Toward Lightweight LLMs:**Elastic Reasoning may pave the way for more efficient, edge-friendly LLMs. Many current models are overkill for typical tasks. By reducing waste, Elastic Reasoning helps reduce environmental costs too—though there’s always a risk of increased demand offsetting those gains.

## Conclusion

Elastic Reasoning offers a principled and scalable approach to deploying powerful reasoning models in production. By separating the reasoning process into distinct thinking and solution phases and training the model to adapt under strict token budgets, it provides reliable performance, lower costs, and improved efficiency. It’s a critical step forward in making LLMs not just smarter, but more practical and sustainable for real-world use.
