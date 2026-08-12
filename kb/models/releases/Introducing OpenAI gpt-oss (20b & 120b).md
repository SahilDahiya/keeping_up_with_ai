---
title: Introducing OpenAI gpt-oss (20b & 120b)
kind: blog
topic: models
subtopic: releases
secondary_topics:
- agents/tool-use
summary: 'Deep dive on OpenAI''s first open-weight release since GPT-2 (gpt-oss-20b/120b):
  standard MoE transformer architecture with adjustable low/mid/high reasoning levels
  and built-in tool support, with gpt-oss-120b surpassing o3-mini and approaching
  o4-mini on benchmarks despite being 6x smaller than typical frontier scale, driven
  mainly by post-training data and RL rather than architecture.'
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/openai-gpt-oss
author: null
published: '2025-08-05'
fetched: '2026-08-12T06:31:02Z'
classifier: claude
taxonomy_rev: 2
words: 659
content_sha256: c2a6b20b5262989f6909a1419d920b81c21e5f9acaacfb254ceed7463e3871b4
---

# Introducing OpenAI gpt-oss (20b & 120b)

This is a deep dive analysis of gpt-oss (20b & 120b), released by OpenAI on 5th Aug 2025. This blog explores its capabilities, technical architecture, benchmarks, and practical applications for developers.

OpenAI is finally back to living up to its name of building “open models”. After GPT-2, this is the first set of open-source LLMs coming from OpenAI.

OpenAI's new open-source models, gpt-oss-20b and gpt-oss-120b, are very strong reasoning models that excel at problem solving and tool calling. Both models support long context windows and adjustable reasoning levels. That makes them a great choice for agentic use cases.

- •The models performance is at the level of o3 and o4-mini (see section 2.1 for benchmarks)
- •The models support both built-in (code interpreter, browser) and user-provided tools and are able to generate consistent trajectories over doesn’t of turns
- •The models allow for selecting low/mid/high reasoning level (as in o4-mini-high)
- •The model architecture is quite standard mixture-of-experts transformer. The performance upgrades are primarily because of the training data & reinforcement learning tuning

Try out the new OpenAI [gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b) & [gpt-oss-20b](https://fireworks.ai/models/fireworks/gpt-oss-20b) on Fireworks!

The following table is an evaluation across multiple benchmarks and reasoning levels for both the gpt-oss-20b and gpt-oss-120b

The following table showcases the Main capabilities evaluations, where gpt-oss models are compared at reasoning level with other OpenAI closed-models including - high to OpenAI’s o3, o3-mini, and o4-mini on canonical benchmarks.

The gpt-oss-120b model surpasses OpenAI o3-mini and approaches OpenAI o4-mini accuracy. The smaller gpt-oss-20b model is also surprisingly competitive, despite being 6 times smaller than gpt-oss-120b.

A fair comparison of gpt-oss against leading commercial models including Kimi, GLM, Qwen and DeepSeek, highlighting areas where it excels and areas for improvement.

After pre-training on massive text data, thegpt-oss models go through a dedicated post-training phase to refine their reasoning abilities and tool usage, drawing from similar Chain-of-Thought (CoT) reinforcement learning techniques used in OpenAI's o3 models.

This phase trains the models on complex, multi-step tasks across coding, math, and science, helping them develop structured problem-solving capabilities and a personality similar to ChatGPT.

OpenAI introduced a new format called the Harmony Chat Format- a flexible, role-aware, message-based structure for interactive conversations.

- •It uses labeled roles like System, Developer, User, Assistant, and Tool to enforce a hierarchy when resolving conflicting instructions.
- •Special “channels” like analysis, commentary, and final help guide how reasoning traces, tool calls, and final answers are shown to the user.
- •This structure enables the model to perform more advanced agentic tasks, like embedding tool calls directly within reasoning steps or sharing step-by-step action plans.

💡 If you're deploying gpt-oss models, using Harmony Format correctly is essential for unlocking their full capabilities, especially in multi-turn chats.

The models are trained to support **three reasoning levels**- low, medium, and high, configured in the system prompt (e.g., Reasoning: high).

As you increase the reasoning level, the model produces longer and more structured CoT traces, allowing it to think through problems with greater depth.

**4.3 Agentic Tool Use**gpt-oss models are also trained to work with a range of tools in agentic workflows:

- •**Web browsing** , to fetch real-time information and increase factual grounding
- •**Python execution** , in a stateful notebook-style environment for live code reasoning
- •**Custom developer functions** , defined in-system using schemas (similar to OpenAI’s function calling)

These tools can be turned on or off using system prompts, and OpenAI provides basic harnesses and an open-source implementation to help developers integrate them into real-world apps.

You can run both the gpt-oss models ([gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b) & [gpt-oss-20b](https://fireworks.ai/models/fireworks/gpt-oss-20b)) on Fireworks Model Library via UI.

1234567891011121314

We’re also excited to announce a joint effort between Fireworks and AMD to bring OpenAI models to AMD’s latest MI355 GPUs. This collaboration will make powerful AI models more accessible and cost-efficient, coming soon to the Fireworks platform.

Try out the new OpenAI gpt-oss models now!

- •gpt-oss-120b: [https://fireworks.ai/models/fireworks/gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b)
- •gpt-oss-20b: [https://fireworks.ai/models/fireworks/gpt-oss-20b](https://fireworks.ai/models/fireworks/gpt-oss-20b)

- •Official model documentation: [https://openai.com/index/introducing-gpt-oss/](https://openai.com/index/introducing-gpt-oss/)
- •Model card: [https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf](https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf)
