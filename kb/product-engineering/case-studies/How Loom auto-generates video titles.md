---
title: How Loom auto-generates video titles
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/evaluation
summary: Case study of Loom auto-generating video titles and using evals to improve
  a production AI feature's usefulness and quality.
source: braintrust
url: https://www.braintrust.dev/blog/loom
author: null
published: '2026-01-01'
fetched: '2026-07-11T04:32:53Z'
classifier: codex
taxonomy_rev: 1
words: 1029
content_sha256: 61277224af8235897d1a7c6952fb8ee18bf6e9f33684ed5aeb8c286895cc5f39
---

# How Loom auto-generates video titles

With [Matt Granmoe](https://www.linkedin.com/in/mattgranmoe/), Senior Software Engineer

10-15

Examples to start iterating

6

Common quality measures

![Loom AI](https://www.braintrust.dev/customers/stories/loom/loom-ai.jpg)


[Loom](https://www.loom.com/) is a video communication platform used by millions of professionals worldwide. With the rise of generative AI, the Loom team saw an opportunity to make video communication more accessible and efficient with [new features powered by LLMs](https://www.loom.com/ai), like automatically generated video titles.

Behind the scenes, developing these AI features came with its own set of challenges. The team at Loom recognized that building great AI features requires a robust method for evaluating quality. How do they know if their auto-generated titles are any good? To answer that question, they started running evals on Braintrust with their own custom scoring functions.

In this post, we'll share how Loom's software engineering team conceptualizes and builds scoring functions. By defining clear, actionable criteria and iterating quickly, Loom has found a sweet spot between innovation and reliability.

Loom’s philosophy is that all AI-driven features should be built around how real users evaluate the generated output: to write great scorers, you need to understand the feature first. Instead of asking, “Is the model doing what I want?,” which optimizes for the model following instructions, Loom focuses on the feature itself by evaluating whether the output is ideal, regardless of how it’s generated. This approach allows for higher-level improvements to the feature. By replacing a generic notion of “quality” with a structured, four-step process, Loom iterates on scoring functions, making sure that each AI feature meets its intended goals and delights users.

Identify the traits of great video titles

Check for common measures of quality

Create initial scores and iterate

Implement objective code measures

When kicking off a new feature, their team looks at:

**The input**: what data or prompt is the model receiving?

**The output**: what is the model supposed to generate?

They then ask, “How do humans evaluate the quality of this output?” and “What do great examples of this output look like?”

For example, in the case of auto-generating video titles, they first identify what makes a great video title:

- Conveys the main idea
- Concise yet descriptive
- Engaging to readers
- Readable (no grammar or spelling issues)
- Doesn’t contain hallucinations
- Ends with a single relevant emoji (for a bit of fun!)

By identifying these traits, the team can begin to outline how they’ll measure each aspect of a great output, even before writing any actual scoring code or prompts.

There are a handful of quality measures that apply across a broad range of LLM use cases. They won’t necessarily be useful for every use case, but it’s worth doing a quick check to see if any of them apply:

- Relevance (also known as faithfulness or hallucinations): does the output accurately reflect the source material (for example, video transcripts)?
- Readability: is it written in clear, understandable language?
- Structure/formatting: does it follow a desired format, like a JSON schema or specific text layout, like a title with multiple subheadings?
- Factuality: if the output is supposed to be factual, like when drawing from a RAG system, is it accurate?
- Bias/toxicity/brand safety: is it safe to show the output to users, without offensive or biased language?
- Correct language: is the output in the requested language?

These general checks are powerful, but Loom also customizes them to the specific feature by building small, [custom scorers](https://www.braintrust.dev/docs/evaluate/write-scorers). By tailoring each scorer to the task, they remove unnecessary noise in prompts and get more reliable results.

Whenever possible, Loom automates these quality checks with deterministic, [code-based scorers](https://www.braintrust.dev/docs/evaluate/custom-code). Objective checks like “Does the output text contain exactly one emoji at the end?” or “Does the JSON response contain all required keys?” can be validated without an LLM.

This approach saves time and money, as code-based scorers are low-cost and fast, even at scale, and eliminate the variablilty of LLM responses.

Using their feature-specific criteria and any relevant common measures as a starting point, the team at Loom sets up an initial round of scorers in Braintrust. Here are some examples of scorers they ended up building for auto-generated video titles:

- Relevance, focusing on the main topic of the video
- Conciseness
- Engagement potential
- Clarity
- Correct language

From there, they continue iterating by feeding in around 10-15 test examples to get a feel for how the scorers are performing, inspecting the results, and refining as needed. After they're satisfied that the scorers are dialed in, they begin running evals at scale by configuring [online evaluations](https://www.braintrust.dev/docs/evaluate#online-evaluation-production-scoring).

Here are a few best practices they've picked up along the way:

- When using [LLM-as-a-judge scorers](https://www.braintrust.dev/docs/evaluate/llm-as-a-judge), it's crucial to enable the chain-of-thought option. This gives you back a “rationale” in the score where the LLM explains why it gave the score it did. Use this to calibrate the scorer.
- Each scorer should focus on a distinct aspect of the output (e.g., factual correctness vs. style vs. presence of an emoji).
- When some aspects matter more (e.g., factual accuracy over style), they configure [weighted averages](https://www.braintrust.dev/docs/evaluate/interpret-results)to combine scores.
- Sometimes a binary (yes/no) score is enough. Other times, a 3- or 5-point scale is necessary for more nuance.

Through multiple iterations of prompt tuning, scorer adjustment, and dataset honing, Loom tailors each feature's scoring process unil they're sure it captures all the essential qualities.

This cycle of define → implement → evaluate → refine gives Loom a strategic advantage. By integrating both objective and subjective measures into their scorers, the team can quickly identify what’s working and where improvements are needed. They also avoid “analysis paralysis” by starting small and iterating quickly.

At Loom, they've established a repeatable, reliable system for shipping features faster and more confidently using Braintrust evals. By systematically scoring AI outputs, they can run large-scale evaluations more quickly, make sure features reliably meet users' needs, and ship improvements with the knowledge they've been thoroughly tested.

Whether you're building auto-generated titles, chat-based assistants, or something entirely different, Loom's guide to scoring functions is an excellent blueprint to follow.

Learn how Loom uses Braintrust to identify quality traits, implement objective checks with code, and iterate on LLM-as-a-judge scorers with chain-of-thought rationale.
