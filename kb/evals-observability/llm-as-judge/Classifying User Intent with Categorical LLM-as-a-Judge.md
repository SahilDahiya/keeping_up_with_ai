---
title: Classifying User Intent with Categorical LLM-as-a-Judge
topic: evals-observability
subtopic: llm-as-judge
secondary_topics:
- prompt-engineering/structured-output
summary: Shows how to classify user intent with categorical LLM-as-judge evaluators,
  including rubric design and structured scoring for production analysis.
source: langfuse
url: https://langfuse.com/blog/2026-04-14-categorical-llm-as-a-judge-user-intent
author: null
published: '2026-04-14'
fetched: '2026-07-11T04:36:26Z'
classifier: codex
taxonomy_rev: 1
words: 1065
content_sha256: 4396bd5e04b68e31a12e8ffca9b7b67876436f63d716ecc3a10d10a626ef1540
---

# Classifying User Intent with Categorical LLM-as-a-Judge

# Classifying User Intent with Categorical LLM-as-a-Judge

A guide on how to set up a categorical LLM-as-a-judge evaluator to classify user intent. Follow along with how we applied this to our demo application.

![Picture Lotte Verheyden](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Flotteverheyden.jpg&w=96&q=75) Lotte Verheyden

Lotte VerheydenWe recently shipped [categorical LLM-as-a-judge scores](https://github.com/orgs/langfuse/discussions/4965), a highly requested feature. Instead of only returning numeric scores, evaluators can now return category labels. To put this to use right away, we set it up on our own [support chatbot demo application](https://langfuse.com/demo) to classify the user's intent into a fixed set of categories.

New to LLM-as-a-judge? The

[docs page](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)covers the concept in detail.

[What you can do with intent labels](https://langfuse.com#what-you-can-do-with-intent-labels)

Once every trace has an intent label attached to it, a few things become possible:

- **Filter traces by intent.**Want to look at only self-hosting questions, or only implementation questions? Filter on the score value and review just those traces.
- **Build dashboards showing question distribution.**See at a glance how many users are asking conceptual questions vs. implementation questions vs. pricing questions, and track how the distribution changes over time.
- **Correlate intent with other scores**using- [Score Analytics](https://langfuse.com/docs/evaluation/evaluation-methods/score-analytics). For example, if you collect user feedback scores, you can check whether self-hosting questions consistently receive lower feedback scores than conceptual questions.

[The evaluator prompt](https://langfuse.com#the-evaluator-prompt)

We defined six intent categories that map to distinct user needs:

| Category | Description |
|---|---|
| `conceptual-question` | The user wants to understand what Langfuse is, how a feature or concept works, or wants a high-level explanation. |
| `implementation-question` | The user wants to build, integrate, or write code with Langfuse. This includes getting-started questions, framework-specific integration, debugging errors, and API usage. |
| `self-hosting` | The user wants to deploy or run Langfuse on their own infrastructure. Includes Docker, Kubernetes, local setup, and infrastructure questions. |
| `pricing-and-comparison` | The user asks about cost, pricing plans, or compares Langfuse to an alternative. |
| `ui-feedback` | The user gives feedback, reports a UI issue, or makes a product suggestion about the Langfuse application itself. |
| `irrelevant-to-langfuse` | Greetings with no question, test messages, gibberish, or requests completely unrelated to Langfuse. |

## Read the full evaluator prompt here.

You are a user intent classifier for a Langfuse support chatbot. You will be given the user's message. Classify it into exactly one of the following categories.

**Categories**

- **conceptual-question**: The user wants to understand what Langfuse is, how a feature or concept works, or wants a high-level explanation. The user is not trying to build or set up anything yet. Examples: "What is Langfuse?", "How does tracing work?", "Explain this to a product manager."
- **implementation-question**: The user wants to build, integrate, or write code with Langfuse. This includes getting-started questions, framework-specific integration, requests for code examples, debugging errors, and API usage. If the user is trying to- *do*something with Langfuse in their application, it belongs here.
- **self-hosting**: The user wants to deploy or run Langfuse on their own infrastructure. Includes Docker, Kubernetes, local setup, resource provisioning, and infrastructure questions. If the question is about running Langfuse itself rather than using it in an application, it belongs here.
- **pricing-and-comparison**: The user asks about cost, pricing plans, or compares Langfuse to an alternative (e.g. "How does Langfuse compare to X?"). A general "What can Langfuse do?" question is conceptual, not a comparison.
- **ui-feedback**: The user gives feedback, reports a UI issue, or makes a product suggestion about the Langfuse application itself. The user is commenting on their experience, not asking a question.
- **irrelevant-to-langfuse**: Greetings with no question, test messages, gibberish, or requests completely unrelated to Langfuse (e.g. shopping lists, weather, song lyrics).

**Rules**

- Classify based on the user's primary goal. A user asking "what are traces?" is **conceptual**; a user asking "how do I set up tracing in Python?" is**implementation**.
- When a message touches multiple categories, choose the one that best matches what the user is ultimately trying to achieve.
- If the message is in a non-English language, classify based on the translated intent, language does not affect the category.

**Input:** `{{input}}`

**Output:** Respond with only the category name, nothing else.

A few things worth noting about this prompt:

- **Each category has a clear boundary.**For example,- `conceptual-question`vs.- `implementation-question`comes down to whether the user is trying to understand something or build something.
- **The rules section resolves ambiguity.**When a message touches multiple categories, the judge picks the one matching the user's primary goal.
- **The categories are actionable.**Each one maps to something we can act on, whether that's improving docs, routing feedback, or filtering out noise.

You can see this evaluator live in our [public demo project](https://cloud.langfuse.com/project/clkpwwm0m000gmm094odg11gi/evals?peek=bd338e3a-dbe9-464d-8aed-cd3dc60ca623).

[Configuring the evaluator in Langfuse](https://langfuse.com#configuring-the-evaluator-in-langfuse)

After entering your prompt for the evaluator, select "Categorical" as the score type and define the category values.

![Score type selector showing Categorical selected](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-04-14-categorical-llm-as-a-judge-user-intent%2Fscore-type-dropdown.png&w=3840&q=75)


Then define the category values and enter the score reasoning and category selection prompts.

![Full evaluator configuration with categories and prompts](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-04-14-categorical-llm-as-a-judge-user-intent%2Fevaluator-config.png&w=3840&q=75)


Make sure the category names you enter here match the category names used in the evaluator prompt exactly.


There is also a checkbox to allow multiple matches. In our case, we left this unchecked since each user message should have exactly one intent.

After saving, you can configure the remaining settings as you normally would for any LLM-as-a-judge evaluator: filtering on the observations you want to run on, mapping the variables to the observation input, etc. See the [LLM-as-a-judge documentation](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge) for guidance on these steps.

[Intent scores in action](https://langfuse.com#intent-scores-in-action)

With the evaluator running, every new support chatbot trace gets an intent label automatically. Now we can set up a dashboard widget that shows us the distribution of user intent over conversations.

To create this widget, select "Scores Categorical" as the view, set the metric to "Count", filter by score name `user-intent`, and break down by "String Value". We chose a pie chart to visualize the distribution.

![Widget configuration for user intent distribution](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-04-14-categorical-llm-as-a-judge-user-intent%2Fwidget-configuration.png&w=3840&q=75)


The resulting widget shows the distribution of user intent across conversations.

![Dashboard widget showing user intent distribution](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-04-14-categorical-llm-as-a-judge-user-intent%2Fdashboard-widget.png&w=3840&q=75)


The [dashboard is publicly accessible](https://cloud.langfuse.com/project/clkpwwm0m000gmm094odg11gi/dashboards/cmk3to8l7014fad07soxj1c1m) if you want to explore the data yourself.

[Get started](https://langfuse.com#get-started)

Categorical LLM-as-a-judge scores are available on all Langfuse plans. To set up your own evaluator:

- Read the [LLM-as-a-judge documentation](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)for the full setup guide.
- Explore the [public demo project](https://cloud.langfuse.com/project/clkpwwm0m000gmm094odg11gi)to see this evaluator in action.
- Check out the [changelog entry](https://langfuse.com/changelog/2026-03-20-categorical-llm-as-a-judge-scores)for the feature announcement.
