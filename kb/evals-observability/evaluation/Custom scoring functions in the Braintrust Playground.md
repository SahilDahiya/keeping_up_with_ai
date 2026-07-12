---
title: Custom scoring functions in the Braintrust Playground
topic: evals-observability
subtopic: evaluation
secondary_topics:
- evals-observability/testing
summary: Explains custom scoring functions for evaluating AI outputs, including how
  domain-specific metrics can be added to an eval workflow.
source: braintrust
url: https://www.braintrust.dev/blog/custom-scorers
author: Braintrust Team
published: '2024-09-16'
fetched: '2026-07-11T04:31:59Z'
classifier: codex
taxonomy_rev: 1
words: 496
content_sha256: 752e62ea26a0c6dd02dde03efcbdb287d84f25cba86201be35273a9132263ce0
---

# Custom scoring functions in the Braintrust Playground

16 September 2024Ankur Goyal3 min

![Hero](https://www.braintrust.dev/blog/meta/custom-scorers/custom-scorers.png)


Testing and iterating on prompts in a traditional IDE is difficult because AI evaluation is an inherently dynamic and collaborative process. As a result, developers and non-technical builders tend to spend a lot of time using tools like the [Braintrust Playground](https://www.braintrust.dev/docs/evaluate/playgrounds) to move faster, run more experiments, and ultimately build better AI products.

Today, I’m excited to announce that you can now create custom scorers and access them via the Braintrust UI and API. Scoring is the foundation of AI evaluation – a scoring function allows you to assess the output of an LLM, usually against an expected output, and assign a score of 0 to 100%. In the Braintrust Playground, we have long provided several scorers that work out of the box through our open-source [autoevals](https://github.com/braintrustdata/autoevals) library. But once you begin running evaluations, you’ll often need custom scorers for your specific use cases to get a well-rounded view of your application’s performance. Until today, that required jumping back to your codebase to run full evals.

The new custom scoring functionality allows you to run sophisticated, multi-model comparisons across multiple prompts and scoring functions, defined as LLM-as-a-judge, TypeScript, Python, or HTTP endpoints. After you create a custom scoring function, you can even use Braintrust for server-side online evaluations that run asynchronously.

Let’s dig into how to use this feature, and what new capabilities it unlocks.

Scorers tend to be a combination of heuristics (best expressed as code) and LLM-as-a-judge (best expressed as a prompt).

To create a prompt-based scorer, define a prompt that classifies the output and a mapping from choices to scores. You can also specify whether or not to use chain-of-thought (CoT). This is the same technique used by the `LLMClassifier` class in [autoevals](https://github.com/braintrustdata/autoevals).

![Prompt scorer in UI](https://www.braintrust.dev/blog/img/custom-scorers/prompt-scorer.png)


To create a code-based scorer, write a TypeScript or Python handler function that returns a score between 0 and 1.

![Code-based scorer in UI](https://www.braintrust.dev/blog/img/custom-scorers/code-scorer.png)


You can also use any of the evaluators in [autoevals](https://github.com/braintrustdata/autoevals) as a starting point for your custom scorers.

In addition to creating custom scorers from the UI, you can also upload task and scorer functions to Braintrust from the command line, and use them in the Playground. To bundle and upload the functions to Braintrust, and update the bundled scorers in your project, run:

`npx braintrust eval —-push`

Creating custom scorers unlocks several workflows in Braintrust. You can:

- Use custom scorers in the playground as you iterate on your prompts, and kick off experiments
- Access custom scorers through the API
- Run server-side online evaluations asynchronously on specific logs

Once you compute scores on your logs, you can monitor performance over time, find anomalous cases, and add logs to a dataset to use in additional evaluations.

If you already have a Braintrust account, you can get started with custom scorers today. If you don’t, [sign up for free](https://www.braintrust.dev/signup) and give it a try. For more information, check out [our docs](https://www.braintrust.dev/docs) or [chat with us](https://www.braintrust.dev/contact).
