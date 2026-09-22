---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/viberl
author: null
published: '2025-07-22'
fetched: '2026-09-22T06:10:30Z'
classifier: null
taxonomy_rev: 2
words: 667
content_sha256: 96cb6a6ff2fa7f4455a179c52c9b7ccc6bf114611cfb4906208c34b9739949d4
---

# Fireworks AI

- •We introduce the concept of VibeRL, an AI agent that automates complex Reinforcement Learning (RL) fine-tuning. Instead of wrestling with intricate setups, you simply provide a dataset and a prompt, and the agent handles the rest.
- •Preliminary validation on diverse tasks like math and coding shows VibeRL automatically selects optimal strategies and delivers significant results.

Reinforcement Learning (RL) isn't new. Think about it like training a pet - you give a command, your pet performs an action, and if it's correct, it gets a treat. Over time, your pet learns exactly what you want.

The same idea has been quietly revolutionizing AI. Techniques like Proximal Policy Optimization (PPO) played a huge role in early successes such as ChatGPT. But honestly, these early methods weren’t easy. You had to juggle multiple models, tweak countless hyperparameters, and sometimes even then, things would just break.

Things got simpler with methods like Group Relative Policy Optimization (GRPO), which reduced some complexity. But even then, RL remained tricky - designing reward functions and fine-tuning was more art than science. (We previously discussed how models can judge each other in our post, ["Model as a Judge"](https://fireworks.ai/blog/model-as-judge)).

Recently, "Vibe Coding" - AI translating simple human instructions into working code - has changed the game for software developers. It made coding easier, faster, and more accessible.

We thought: why not bring this vibe to RL?

RL’s complexity actually makes it ideal for automation. So we built VibeRL - an AI agent designed to handle all the difficult parts of RL for you. Here’s how easy it is:

- •Give VibeRL your dataset.
- •Write a simple prompt describing your goal.

That’s it. From there, VibeRL analyzes your task, picks the best strategy, and runs the entire fine-tuning process on its own. We're still actively developing it, but early results have been pretty exciting.

We tested VibeRL with a variety of problems to see how it stacked up against traditional methods.

- •**Base Model:** Qwen2.5-3B
- •**Task:** Improve math reasoning with GSM8K data.
- •**User prompt:** You are given a datase GSM8k about grade school math problem solving in`{dataset_path}` . You are tasked to improve the math problem solving ability of the base model on this dataset by performing funetuning on it. The final solution of the finetuned model should be concise, mathematically correct, and closely follow the desired format.
- •**Result:** In just 40 epochs, accuracy jumped from 52% to 85%.

- •**Base Model:** Qwen2.5-7B
- •**Task:** Solve LeetCode programming problems without direct answers—just a pass/fail test environment.
- •**User prompt:** You are given a datase consist of leetcode coding problems in`{dataset_path}` . You are tasked to improve the coding problem solving ability of the base model on this dataset by performing funetuning on it. The final solution of the finetuned model should be able to give the correct answer to the leetcode coding problems, which passes all of the test cases. The solution should also be concise and easy to understand
- •**Result:** Accuracy improved from 34% to 63%. Interestingly, we noticed performance fluctuating slightly near the end, giving us insight into future improvements.

We tackled a real client problem, improving the model’s ability to correctly call functions based on user inputs.

- •**Base Model:** Qwen3-32B
- •**Task:** Function calling accuracy from client dataset.
- •**Result:** Using a two-step approach (SFT followed by RFT), accuracy rose dramatically from 50% to 87.3%.
- •**Prompt:** <hidden to avoid revealing customer-specific details>

|  | Baseline | SFT | RFT | 
|---|---|---|---|
| Function calling accuracy | 50.0% | 85.8% | 87.3% | 

These early tests confirm that AI agents like VibeRL can genuinely simplify RL workflows, making powerful model customization accessible even without deep expertise.

Next up, we’re turning VibeRL into a product. We're also exploring ways to make it smarter, like automatically choosing base models, tuning hyperparameters on-the-fly, and even drafting reward functions with minimal human effort.

Ultimately, we want everyone to easily harness their data and build models - less engineering, more intuition.
