---
title: Evaluating Multi-Turn Conversations
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/memory-context
summary: Explains how to evaluate multi-turn conversations, including context retention,
  conversation-level scoring, and stateful failure modes.
source: langfuse
url: https://langfuse.com/blog/2025-10-09-evaluating-multi-turn-conversations
author: null
published: '2025-10-09'
fetched: '2026-07-11T04:35:41Z'
classifier: codex
taxonomy_rev: 1
words: 1082
content_sha256: 6a6d848dd311f511ecd81ece3ef2e6843e9554b5057999acd84e117bc0609302
---

# Evaluating Multi-Turn Conversations

# Evaluating Multi-Turn Conversations

A practical guide of the different ways to evaluate multi-turn conversation agents (a.k.a. chatbots)

![Picture Abdallah Abedraba](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Faabedraba.jpeg&w=96&q=75) Abdallah Abedraba

Abdallah AbedrabaIf you're building a chatbot, you've probably experienced this: everything works great in testing, users start trying it, and then... chaos. Your agent forgets what someone said three messages ago. It hallucinates confidently. It gives unsafe recipe advice to someone with allergies.

The problem? You're flying blind. You need evaluation systems, and you need them yesterday.

We've created two notevbooks on evaluating multi-turn conversations that tackle this from different angles. This post will help you understand when to use each approach, and why you probably need both.

(If you're new to evals, check out our [intro to LLM evaluation](https://langfuse.com/docs/evaluation) for foundational concepts. And if code's your thing, both methods include Jupyter notebooks to get you started.)

[The Problem](https://langfuse.com#the-problem)

Multi-turn conversations are deceptively hard. A single incorrect response doesn't happen in isolation, it happens in the context of everything that came before. Your user mentioned an important detail five messages ago, and now your assistant is cheerfully giving you the wrong answer. Oops.

There are two ways to systematically address this:

- [N+1 Evaluations](https://langfuse.com/guides/cookbook/example_evaluating_multi_turn_conversations): Debug specific failure points in real conversations
- [Simulated Conversations](https://langfuse.com/guides/cookbook/example_simulated_multi_turn_conversations): Proactively test scenarios before users hit them

[Method 1: N+1 Evaluations](https://langfuse.com#method-1-n1-evaluations)

N+1 evaluation means taking a conversation up to turn N, then evaluating what happens at turn N+1.

**Use this when:**

- You have production traffic, traces, and real user conversations
- You've identified a specific recurring problem
- You're making targeted fixes and want to verify they work

[Process](https://langfuse.com#process)

Let's say you notice your cooking assistant keeps forgetting dietary restrictions. Here's how you debug it systematically:

-
**Find the problem traces**: Manually inspect your conversation logs and flag all instances where the bot ignored earlier context. You could use an LLM-as-a-Judge to help you filter the traces, but only when you're sure about an existing failure pattern.
-
**Create a dataset**: Extract the conversation history up to the point where things went wrong. This becomes your test set.
-
**Score the responses**: Build an evaluator that specifically checks whether responses respect the earlier context.
-
**Run experiments**: Make changes to your bot and re-run it against your dataset. Track scores over time.

The beauty of this approach is that you're working with real user data. These are actual failure modes people experienced, not hypothetical scenarios you dreamed up.

[Example](https://langfuse.com#example)

Here's what this looks like in practice:

```
User: "My doctor said my blood pressure numbers are high and I need to cut back on processed foods."
Bot: "Well that must be concerning to hear. Did your doctor give you specific guidance?"
User: "It went over my head... Anyway, I'm stressed and just want some good comfort food. Can you give me a recipe for loaded nachos?"
Bot: [cheerfully provides loaded nachos recipe] ❌
```
You extract this conversation history (minus the bot's final response), add it to your dataset, and create a scoring function that checks: "Does the response acknowledge the user's implied dietary restrictions?". Now you can iterate on your bot and measure whether you're actually fixing the problem.

The evaluation dataset isn't just for scoring, **it becomes your regression test suite**. Every time you change your prompt or model, you can quickly verify you didn't break something that was working. If you've ever played whack-a-mole with prompt engineering (fix one thing, break another), you know how valuable this is.

See the [N+1 Evaluations](https://langfuse.com/guides/cookbook/example_evaluating_multi_turn_conversations) cookbook for a detailed step-by-step example.

[Method 2: Simulated Conversations](https://langfuse.com#method-2-simulated-conversations)

Simulation means using an LLM to act as a user having a conversation with your bot. You define personas and scenarios, then let them talk.

**Use this when:**

- You want to test specific scenarios systematically
- You're building something new without much production data yet
- You need to explore edge cases that rarely happen naturally

[The Process](https://langfuse.com#the-process)

- **Define your test dimensions**: What contexts matter? Maybe you care about:

- Frustrated user providing invalid data to the bot
- User query returns multiple results
- User query returns no results

-
**Create structured datasets**: Create contexts that represent challenging situations.
-
**Run simulations**: Use a framework like[OpenEvals](https://github.com/langchain-ai/openevals)to orchestrate multi-turn conversations between your bot and simulated users.
-
**Evaluate the outputs**: Score the complete conversations using LLM-as-a-Judge.

The downside? Simulated conversations are synthetic. They're only as good as your context design.

[Example](https://langfuse.com#example-1)

Here's a scenario:

```
{
  "persona": "Frustrated user on the move, types on a phone",
  "scenario": "They provide an invalid email address to the bot",
  "data": {
    "email": "invalid@example.com"
  }
}
```
You let this simulated user talk to your bot for several turns and see how well your bot handles the invalid data, urgency, and frustration.

See the [Simulated Conversations](https://langfuse.com/guides/cookbook/example_simulated_multi_turn_conversations) cookbook for a detailed step-by-step example.

[Some Practical Advice](https://langfuse.com#some-practical-advice)

From building both systems, here's what I've learned:

**Remove ALL friction from  looking at data**: You cannot outsource this to tooling alone. Build custom views that show you everything you need on one screen. If you're context-switching between tools to understand what happened, you're doing it wrong.

**Start simple**: Don't build elaborate scoring systems with multiple metrics immediately. Binary pass/fail is often enough to start.

**Your datasets will evolve**: The test cases you create today will be outdated in three months. That's fine. Keep updating them based on what you learn.

**LLMs can help create eval systems**: Use them to generate test scenarios, as judge, and create scoring rubrics. They're not just the thing you're evaluating, they're tools for building the evaluation system itself.

**Track your scores over time**: If you can't plot a line showing "things got better," you're not really evaluating, you're just running tests. Use whatever analytics tool you have (even a spreadsheet works) to track progress.

[The Real Insight](https://langfuse.com#the-real-insight)

You can't build a good chatbot without a good evaluation system. Period. The teams that win are the ones who invest early in systematic evaluation. They can iterate 10x faster because they know immediately when they've made things better or worse.

The difference is where you start:

- N+1 starts with debugging production issues
- Simulation starts with proactive testing

But both create datasets, run experiments, score results, and iterate. You're creating a flywheel for improvement.

Now go build your evaluation system. Your users (and your future self) will thank you.

[Further Reading:](https://langfuse.com#further-reading)

- [Evaluating Multi-Turn Conversations (N+1 Method)](https://langfuse.com/guides/cookbook/example_evaluating_multi_turn_conversations)
- [Simulating Multi-Turn Conversations](https://langfuse.com/guides/cookbook/example_simulated_multi_turn_conversations)
- [Hamel's Eval Systems Post](https://hamel.dev/blog/posts/evals/)
- [CI/CD for LLM Applications](https://langfuse.com/blog/2025-10-21-testing-llm-applications)
