---
title: Rank LLMs With Production Traces and an LLM Judge | Fireworks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/rank-llms-production-traces
author: null
published: '2025-09-22'
fetched: '2026-10-23T06:13:50Z'
classifier: null
taxonomy_rev: 2
words: 1483
content_sha256: a0768d6ab93f3297e1d532e4445ea8fc9eb41d1e1cd8db592ae336c518d5cac9
---

# Rank LLMs With Production Traces and an LLM Judge | Fireworks

## Introduction

Choosing the right AI model is a critical decision, yet it’s often a guess. Public benchmarks don’t reflect the real-world trade-offs between cost, speed, and quality on your data. What if you could find the optimal model by building a leaderboard from your production logs in just five minutes?

This post shows you how to find out using [Eval Protocol](https://evalprotocol.io/introduction), an open-source toolkit for building your internal model leaderboard. We’ll demonstrate a quick, no-ground-truth-required method and validate it by showing our results correlate strongly with the official [Tau Bench Airline benchmark](https://github.com/sierra-research/tau2-bench). While our [Quickstart Guide](https://evalprotocol.io/quickstart) covers the code, this article goes under the hood to explore the step-by-step methodology—inspired by Arena-Hard-Auto research—for turning raw logs into a validated model leaderboard.

## TL;DR

Our LLM Judge results (left), generated automatically from production traces, show a strong correlation with the official Tau Bench scores (right). This validates a fast, label-free method for accurately ranking models on your specific use case. Keep reading to see how you can make your own leaderboard!

## A Step-by-Step Explanation

### Step 1: Starting with Raw Production Data

Everything begins with real user interactions. For this analysis, we used a dataset of airline customer service conversations that were already being logged to **Langfuse**. Each log, or trace, contains the full back-and-forth between a user and the AI assistant, including any tool calls. This raw, unfiltered data is the perfect source material because it reflects how our models perform in the wild.

In this case, these traces were generated using `kimi-k2-instruct`. This is important because `kimi-k2-instruct` will serve as our baseline, and all the comparisons later on will be checking if a model is better or worse than this baseline.

**Trace Input:**

`jsonCopy`
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465

**Trace Output:**

`jsonCopy`
123456

### Step 2: Deconstructing Conversations for Better Comparisons

A single multi-turn conversation isn’t a great test case on its own. If we just give the whole chat history to a new model, we’re only testing its ability to write the final message. We need to test how a challenger model would have behaved at every single turn of the conversation.

Here’s how it works: Every time the original assistant replied in a conversation, the function creates a new test case. Each test case consists of:

1. **`messages`**: The history of the conversation right before the assistant’s turn.
2. **`ground_truth`**: The exact response the original assistant gave.

This effectively turns one long conversation into multiple, independent challenges.

### Step 3: Generating New Responses with a Rollout Processor

With a clean set of test cases prepared, the next step is to generate responses using our challenger models (e.g., `gpt-4.1` and `gpt-oss-120b`). We’ve built a rollout processor that orchestrates this efficiently. It iterates through each evaluation we want to complete to be done concurrently, leveraging parallel processing to minimize wait times. Now we have a series of completed evaluations that contain both the original model’s response and the new challenger model’s response, setting up a perfect side-by-side comparison for the judgment phase.

### Step 4: The Judgment: Pairwise Comparison and Scoring ⚖️

Now we arrive to the core of the evaluation. How do we decide which response is better without human labels? We use a powerful LLM as an impartial judge, following the **Arena-Hard-Auto** methodology.

- **Judging:** We present the judge (in this case, `kimi-k2-instruct-0905`) with the original user query and two anonymous responses: “Assistant A” and “Assistant B”. The judge has no idea which model produced which response.
- **Mitigating Bias**: An interesting quirk of LLM judges is “position bias”—they sometimes favor the first or second answer they see. To counteract this, we run the judgment twice for every comparison:
  - **Round 1**: Original Model vs. Challenger Model
  - **Round 2**: Challenger Model vs. Original Model
- **The Scoring Mechanism:** The judge provides its reasoning and a final verdict, like `[[A>>B]]` (A is significantly better) or `[[A=B]]` (Tie). We convert these labels into numerical scores based on a predefined mapping. After the two rounds of judgment, we average the scores to get a final result for that specific test case. Here’s how the verdicts map to scores from Assistant A’s perspective in a single comparison:

By running this double-blind, two-round judgment and averaging the results for each test case, we gather hundreds of robust, unbiased comparison data points.

Here’s an example of a judgement for clarity:

**Round 1 Judge Response**

My answer:\nLooking at the situation, I need to check all 7 reservations to identify which ones have only one passenger. From the first two reservations I can see:\n\n1. Reservation 8C8K4E has 2 passengers (Amelia Davis and Amelia Jackson) - this would NOT be cancelled\n2. Reservation UDMOP1 has 1 passenger (Amelia Davis) - this WOULD be cancelled\n\nI need to continue checking the remaining 5 reservations to identify all single-passenger bookings before proceeding with any cancellations.\n\nEvaluation:\nAssistant A’s answer is incomplete - it only shows the first reservation check and then stops without continuing to the next reservations as needed. This doesn’t help identify which reservations have only one passenger.\n\nAssistant B’s answer correctly continues the process by moving to the next reservation (XAZ3C0) to check its passenger count, which is the logical next step in identifying all single-passenger reservations.\n\nBoth assistants are making the correct tool calls to get reservation details, but Assistant B is following through with the complete process while Assistant A appears to have stopped prematurely.\n\nMy final verdict is: \[\[B>>A\]\]

**Round 2 Judge Response**

My answer:\nI need to check the user’s reservations to identify which ones have only one passenger, then verify if those flights can be cancelled according to the cancellation policy. Let me continue checking the remaining reservations.\n\n\[Tool Call: get\_reservation\_details({\”reservation\_id\”: \”XAZ3C0\”})\]\n\nEvaluation:\n\nBoth assistants made the same tool call to get\_reservation\_details for reservation XAZ3C0. However, I notice that neither assistant provided any verbal response to the user before making the tool call. \n\nLooking at the context, the user had just provided their user ID and the assistant had checked their profile, showing 7 reservations. The assistant had already checked 2 reservations (8C8K4E with 2 passengers, UDMOP1 with 1 passenger) and was in the process of checking the remaining reservations to identify which ones have only one passenger.\n\nThe appropriate response would be to continue checking the reservations systematically and then provide a summary to the user. Both assistants correctly continued with the next tool call, but neither provided any interim communication to the user about what they were doing.\n\nSince both assistants made identical tool calls and neither provided a better verbal response, this is essentially a tie.\n\nMy final verdict is: \[\[A=B\]\]

### Step 5: Synthesizing a Final Score

Each judgment is assigned a numerical score (`1`, `0`, `0.5`, etc.) These individual scores are then averaged to produce a final, aggregate score. Eval Protocol compiles the results into a leaderboard:

To be clear, when `gpt-oss-120b` scores **44.4%**, it means that across the simulated samples, its average win rate against the original model (`kimi-k2-instruct`) was 44.4%. Awesome, this gives us comfort that we made the right choice—the original model was in fact the best suited for this use case!

## The Real-World Proof — Validating the Results

A quick leaderboard is impressive, but for any developer, the real question is: “Does this actually work in a real, complex scenario?”

We put it to the test with a true apples-to-apples comparison, generating our scores from `kimi-k2-instruct`’s traces as it ran the official Tau Bench Airline evaluation, the leading test for customer support agent use cases.

Here are the real, hard-won scores from the Tau Bench benchmark for the same models.

`bashCopy`
1234

Look at that! While the absolute numbers are different (win rates vs. benchmark scores), the **ranking and relative performance are close**.

✅ Both methods correctly identify **Kimi-K2** as the best model.

✅ Both methods correctly identify **gpt-oss-20b** as the worst.

✅ Both methods correctly place **gpt-oss-120b** and **gpt-4.1** in the middle, recognizing their similar performance levels.

This is the power of this approach. In minutes, using your own production data, you can get insights that strongly correlate with intensive, state-of-the-art benchmarks.

## Conclusion

What starts as a simple question, “Which model is best?”, can now be answered with a level of speed and confidence that was previously out of reach. We’ve demonstrated a complete methodology that turns your existing production data into a strategic advantage.

The validation against Tau Bench is your assurance that this automated, label-free approach works. It provides a trustworthy signal for model quality that you can apply directly to your own use cases. This allows you to rapidly iterate, test new models as they are released, and always know how they stack up on the conversations that matter most to you.

Ultimately, this framework allows you to make smarter engineering and business decisions, ensuring you are always using the optimal model that balances performance, cost, and speed. Stop guessing—your own data has the answer.

Try it out on your own logs [now](https://evalprotocol.io/introduction)!
