---
title: How to improve your evaluations
topic: evals-observability
subtopic: evaluation
secondary_topics: []
summary: Practical guide to improving evals through better examples, rubrics, scorers,
  slices, and investigation of failure cases.
source: braintrust
url: https://www.braintrust.dev/blog/improve-evals
author: Braintrust Team
published: '2024-06-20'
fetched: '2026-07-11T04:32:47Z'
classifier: codex
taxonomy_rev: 1
words: 955
content_sha256: 0164e2eb3845e9673a3b083adbab7f139bd3cd1e683fc63ede1d7dd050e32be5
---

# How to improve your evaluations

20 June 2024Albert Zhang6 min

This post will cover what evaluations are, what you should work towards, and some actionable approaches to improving your evals.

![How to improve your evals (Header Image)](https://www.braintrust.dev/blog/meta/improve-evals/improve-evals-og-image.png)


To effectively build production-grade AI products, you need great evaluations. Evals measure the performance of your AI application and help establish an effective feedback loop for you and your team. Evals consist of 3 parts:

- __Data__: a test set of examples
- __Task__: the AI function you want to test
- __Scores__: a set of scoring functions that take an- `input`,- `output`, and optional- `expected`value and compute a score

With these 3 pieces, you can run your __task__ on your test __data__ and compute __scores__ for each example. These scores measure how well your application performed and can be aggregated or inspected individually.

If you are new to evals, check out our [overview of evals]([https://www.braintrust.dev/docs/evaluate](https://www.braintrust.dev/docs/evaluate) and our [guide to getting started with automated evals](https://www.braintrust.dev/blog/getting-started-evals).

While evals are quick to get started with, they take time and iteration to get right. In particular, there are two key goals to work toward:

- Taking your understanding of what a good response looks like and codifying it into a set of scoring functions
- Gathering a set of test examples that is 1. broad and 2. representative of real-world usage

Working towards these goals is time well-spent, as you will also be crystallizing your own understanding of the application you’re building.

Here are 3 great approaches you can leverage to improve your evals:

- Identify new and useful evaluators
- Improve your existing scorers
- Add new test cases to your dataset

For you (or any human) to determine whether a subjective LLM response is good or bad, you will intuitively evaluate it on multiple, often unrelated axes. This same principle should apply to your evaluation functions. While you can sometimes rely on a single scorer, it’s almost always worthwhile to leverage multiple. This is especially true for more complex or unstructured use cases.

For example, many of our customers use [factuality](https://github.com/braintrustdata/autoevals/blob/main/templates/factuality.yaml) to identify hallucinations successfully. However, hallucinations are only part of the puzzle (i.e. no hallucinations != great response). Your outputs might still be too wordy, or unhelpful, or include the word “sorry” (which users hate). In these cases, you can improve your evals by adding additional scorers to measure these attributes; for example, a scorer that penalizes long responses.

To improve your existing scoring functions, dig into specific examples and inspect the inputs, outputs, and scores. As you go through, you should think through whether the scores are accurate and how they could be more informative. You can then take action with one of these two approaches:

- **Add more company- or use-case-specific context**- you have a uniquely deep level of context on your users, the product you’re building, and what good/bad looks like. The more of this context you can codify into your scoring functions, the more useful they will be
- **Be more precise about what you’re testing for**- great scoring functions provide high-fidelity signal on a clearly defined axis. For each of your scoring functions, think through what exactly you want to test for, and then update your scorer to test for that as precisely as possible. It’s almost always better to have multiple tightly defined scoring functions vs. a single vaguely defined one, so don’t be afraid to split scoring functions up

For example, [closedQA](https://github.com/braintrustdata/autoevals/blob/main/templates/closed_q_a.yaml) is a very open-ended scorer. If you set the criteria to something vague like “Output should be helpful”, you may find yourself frequently disagreeing with how helpfulness is being scored. In these situations, you will have a lot more success if you:

- Define what helpful means more clearly
- Narrow the scope of your scorer, e.g. specifically test whether outputs respond to all parts of their respective inputs

[closedQA](https://github.com/braintrustdata/autoevals/blob/main/templates/closed_q_a.yaml) scoring function:

yaml

```
prompt: |-
  You are assessing a submitted answer on a given task based on a criterion. Here is the data:
  [BEGIN DATA]
  ***
  [Task]: {{{input}}}
  ***
  [Submission]: {{{output}}}
  ***
  [Criterion]: {{{criteria}}}
  ***
  [END DATA]
  Does the submission meet the criterion?
choice_scores:
  "Y": 1.0
  "N": 0.0
```
Because the input/output space of AI applications is so wide, adding more test cases will almost always increase the coverage of your evals and provide additional useful signal. As a result, great AI teams are constantly adding to and updating their set of test cases.

For example, you may find that your application is performing well on your existing test set. However, when you ship your product to internal users, you see that your application is failing in a specific way; e.g. it fails to use the calculator tool when it should have. This is an important failure, but only 1 of your current test cases requires calculator use. In this situation, you should improve your test case coverage by sourcing 5-10 targeted examples that require calculator use and adding them to your datasets going forward. You might then add an evaluator to test tool usage (or even specifically to test calculator usage).

This pattern is especially powerful once you start [logging](https://www.braintrust.dev/docs/instrument) real user interactions. Learn more about how to establish a logging -> evals feedback loop [here](https://www.braintrust.dev/blog/eval-feedback-loops)!

If you can’t trust your evals (or don’t have them at all), it often feels like you are developing in the dark. Great evals solve this problem by helping you understand the impact of the changes you make. As a result, spending time iterating on your evals is a critical step towards building great AI products.

We hope these methods are helpful as you work towards improving your evals. Happy eval’ing 🙂.

*Check out our [docs]( https://www.braintrust.dev/docs/evaluate or get in touch to learn more about Braintrust.*
