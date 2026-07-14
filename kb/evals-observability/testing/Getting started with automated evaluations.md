---
title: Getting started with automated evaluations
topic: evals-observability
subtopic: testing
secondary_topics: []
summary: Introductory guide to automated evaluations, covering datasets, scorers,
  experiments, and how to start measuring AI application quality.
source: braintrust
url: https://www.braintrust.dev/blog/getting-started-evals
author: Braintrust Team
published: '2024-04-24'
fetched: '2026-07-11T04:32:27Z'
classifier: codex
taxonomy_rev: 1
words: 827
content_sha256: d6585006998730fc14e55917057dc6e50752fdf41b5fa8e201202355b45254ff
---

# Getting started with automated evaluations

![Getting started with automated evaluations (Header Image): An image of a rocketship taking off into AI enlightenment](https://www.braintrust.dev/blog/meta/getting-started/new-opengraph-image.png)


24 April 2024Albert Zhang5 min

At Braintrust, when we chat with engineers building AI applications, one of the most common questions we hear is “How do we get started with automated evaluations?”

In this post, we will discuss the state of evals today and lay out some high-leverage ways to quickly get started with automated evaluations.

Prior to Braintrust, we see AI teams leverage a few common approaches to evals:

- **Vibes-based**: engineers and PMs remember some interesting test cases and eyeball the results
- **Benchmarks and/or black box**: MMLU for general tasks, HellaSwag for common sense, TruthfulQA for truthfulness, HumanEval for code generation, many more
- **Stitched together manual review**: a combination of examples saved in spreadsheets, a script to run through test cases, and humans (engineers/PMs/SMEs) manually checking examples

While the above approaches are all helpful, we find that all three fall short in important ways. Vibes and manual review do not scale, and general benchmarks are not sufficiently application-specific and are hard to customize. This means engineering teams struggle to understand product performance, resulting in a very slow dev loop and frustrating behavior like:

- Making updates without having a good sense of how they impact end users
- Playing whack-a-mole to identify regressions
- Manually scoring responses one by one
- Manually tracking experiments and examples over time (or worse, not tracking them)

Automated evaluations are straightforward to set up and can make an immediate impact on AI development speed. In this section, we will walk through 3 great approaches: LLM evaluators, heuristics, and comparative evals.

LLMs are incredibly useful for evaluating responses out-of-the-box, even with minimal prompting. Anything you can ask a human to evaluate, you can (at least partially) encode into an LLM evaluator. Here are some examples:

- **Comparing a generated output vs. an expected output**- instead of having an engineer scroll through an Excel spreadsheet and manually compare generated responses vs expected responses, you can use a- [factuality](https://github.com/braintrustdata/autoevals/blob/main/templates/factuality.yaml)prompt to compare the two. Many of our customers use this type of test to detect and prevent hallucinations
- **Checking whether an output fully addresses a question**- if you provide a task and a response, LLMs do a great job of scoring whether the response is relevant and addresses all parts of the task

The above two methods are great places to start, and we’ve seen customers successfully configure LLMs to score many other subjective characteristics - conciseness, tone, helpfulness, writing quality, and many more.

Heuristics are a valuable objective way to score responses. We’ve found that the best heuristics fall into one of two buckets:

- **Functional**- ensuring the output fulfills a specific functional criteria- Examples: testing if an output is valid markdown, if generated code is executable, if the model selected a valid option from a list, Levenshtein distance

- **Subjective**- using objective heuristics as a proxy for subjective factors- Examples: checking if an output exceeds a certain number of words (conciseness), checking if an output contains the word “sorry” (usefulness/tone)


Importantly - to make heuristic scoring as valuable as possible, engineering teams should be able to see updated scores after every change, quickly drill down into interesting examples, and add/tweak heuristics.

Comparative evals compare an updated set of responses vs. a previous iteration. This is particularly helpful in understanding whether your application is improving as you make changes. Comparative evals also do not require expected responses, so they can be a great option for very subjective tasks. Here are a few examples:

- Testing whether summarization is improving ([example](https://github.com/braintrustdata/autoevals/blob/main/templates/summary.yaml))
- Comparing cost, token usage, duration (especially when switching between models)
- Starting with a standard template like [battle](https://github.com/braintrustdata/autoevals/blob/main/templates/battle.yaml)and tweaking the questions and scores over time to be use-case specific

Braintrust natively supports [hill climbing](https://www.braintrustdata.com/docs/evaluate/compare-experiments), which allows you to iteratively compare new outputs to previous ones.

While there is no replacement for human review, setting up basic structure around automated evals unlocks the ability for developers to start iterating quickly. The ideal AI dev loop enables teams to **immediately understand performance, track experiments over time, identify and drill down into interesting examples, and codify what “good” looks like**. This also makes human review time much higher leverage as you can point reviewers to useful examples and continuously utilize their scores.

Getting this foundation in place does not require a big time investment up front. A single [scoring function](https://www.braintrustdata.com/docs/evaluate/write-scorers) with 10-30 examples is enough to enable teams to start iterating. We’ve seen teams start from that foundation and very quickly scale into making **50+ updates per day across their AI applications, evaluation methods, and test data**.

At Braintrust, we obsess over making the AI development process as smooth and iterative as possible. Setting up evaluations in Braintrust takes less than 1 hour and makes a huge difference. If you want to learn more, [sign up](https://braintrust.auth.us-east-1.amazoncognito.com/signup?client_id=3jrssgukm2k5hso93j4t1acplm&scope=openid&response_type=code&redirect_uri=https%3A%2F%2Fwww.braintrust.dev%2Fapi%2Fauth%2Fcallback%2Fcognito&nonce=UXM6nP3Q4OIlAoE4hh-LXkS6RDoNI4v80UU_rWAfOPk), [check out our docs](https://www.braintrust.dev/docs) or [get in touch](https://www.braintrust.dev/contact)!
