---
title: Automated Evaluations of LLM Applications
topic: evals-observability
subtopic: testing
secondary_topics:
- evals-observability/evaluation
summary: Guide to automated evaluations for LLM applications, including datasets,
  scorers, experiment runs, and continuous quality checks.
source: langfuse
url: https://langfuse.com/blog/2025-09-05-automated-evaluations
author: null
published: '2025-09-05'
fetched: '2026-07-11T04:35:37Z'
classifier: codex
taxonomy_rev: 1
words: 1111
content_sha256: 520dda171b6fd4f11a1c2ee3db76d6dbba15859d531b5ea0afdc52a808f9658d
---

# Automated Evaluations of LLM Applications

# Automated Evaluations of LLM Applications

A practical guide to setting up automated evaluations for LLM applications and AI agents using Langfuse.

![Picture Jannik Maierhöfer](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fjannikmaierhoefer.jpg&w=96&q=75) Jannik Maierhöfer

Jannik MaierhöferIn AI development, iterating quickly is important. Whether you're refining a prompt, swapping a model, or changing your application logic, you need to understand the impact of each change on performance. Manually annotating outputs after every modification is slow and expensive, especially when you want to integrate evaluations into a CI/CD pipeline.

**Automated evaluators** solve this problem by providing a scalable way to measure and monitor your application's failure modes, enabling a fast and effective development loop.

*The framework in this guide is adapted from Hamel Husain's  Eval FAQ.*

This guide describes a process to **build automated evaluators** for your application. This is a robust evaluator that you can scale for different tests and evolutions of your application:

I'll demonstrate this process using an [example chatbot in the Langfuse documentation](https://langfuse.com/docs/demo) that uses the Vercel AI SDK and has access to a RAG tool to retrieve documents from the Langfuse documentation. The example chat app logs traces into the Langfuse example project and has already answered 19k user queries in the past year.

Here's the chat interface (you can find the example chat app [here](https://langfuse.com/docs/demo)):

![Chat
Interface](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-29-error-analysis-to-evaluate-llm-applications%2Fdemo-chat.png&w=3840&q=75)


[What to Measure](https://langfuse.com#what-to-measure)

In the [Error Analysis Academy page](https://langfuse.com/academy/monitoring/error-analysis), we cover how to perform **error analysis** and identify failure modes in your application. Now we will focus on building automated evaluators to measure these failure modes.

Before building an evaluator, it's important to differentiate between two types of failures to prioritize your efforts:

**Missing Instructions:** The first type are errors caused by vague or incomplete instructions in your prompt. For instance if your agent uses too many bullet points or doesn't ask follow-up questions, and you never instructed it to do so, the first step is to fix the prompt. Creating an evaluator for a failure that a simple prompt tweak can solve is often unnecessary effort.

**Model Limitations:** The second type occur when the LLM fails to perform correctly despite receiving clear and precise instructions. These are the ideal candidates for automated evaluation because they represent the model's inherent limitations, not a misunderstanding of your intent.

Let's apply this to the [Langfuse Example App](https://langfuse.com/docs/demo). First, we fix some obvious issues by clarifying the prompt: "use a maximum of three bullet points" and "ask for more context when the user's query is ambiguous." With those fixed, we can focus on measuring the more complex model limitation failures we identified during [error analysis](https://langfuse.com/academy/monitoring/error-analysis):

- **Out of Scope**: The agent answers a question not related to Langfuse or the LLM/AI space.
- **Generic Responses**: The answer is technically correct but doesn't resolve the user's issue. The metric is to assess if the agent's final answer is helpful and directly addresses the user's question.
- **Context Retrieval / RAG Issues**: The agent uses the wrong retrieval tool. The metric needs to judge if the correct tool was chosen based on the user's query.

For this guide, we will set up an evaluator for the "Out of Scope" failure mode.

[How to Measure](https://langfuse.com#how-to-measure)

In Langfuse, all evaluations are tracked as **Scores**, which [can be attached to traces, observations, sessions or dataset runs](https://langfuse.com/docs/evaluation/scores/overview). Evaluations in Langfuse can be set up in two main ways:

**In the Langfuse UI:** In Langfuse, you can set up **LLM-as-a-Judge Evaluators** that use another LLM to evaluate your application's output on subjective and nuanced criteria. These are easily configured directly in Langfuse. For a guide on setting them up in the UI, check the documentation on ** LLM-as-a-Judge evaluators**.

**External Evaluators:** In your code, you can set up **Custom Evaluators** and use the Langfuse SDKs to send the scores back to the evaluated traces. This allows you to set up code-based evaluators or any other custom evaluation logic. For an example of a custom pipeline, see the guide on ** setting up an external evaluation pipelines**.

In this guide, we will set up an LLM-as-a-Judge evaluator in the Langfuse UI.

[Drafting your LLM-as-a-Judge Prompt](https://langfuse.com#draft-prompt)

A good LLM-as-a-Judge prompt is narrowly focused and well-structured:

- **Pick one Failure Mode**: Focus on one specific failure mode. Do not try to cover multiple failure modes at once.
- **Pass/Fail Definitions**: Clearly define what constitutes a "Pass" (failure is absent) and a "Fail" (failure is present).
- **Examples**: Include clear examples of both "Pass" and "Fail" cases.

Here is an example prompt I use in our Example App to check if the agent's answer is within its scope:

![LLM-as-a-Judge Prompt](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-09-05-automated-evaluations%2Fprompt.png&w=3840&q=75)


Once you drafted your prompt, you can set up the LLM-as-a-Judge evaluator in the Langfuse UI. You can find a guide on how to set them up in the UI [here](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge).

![Evaluator Setup](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-09-05-automated-evaluations%2Fsetup-evaluator.png&w=3840&q=75)


[Validating Your Evaluator](https://langfuse.com#validate-evaluator)

To build an evaluator you can trust, you must validate its performance against human judgment, a process similar to testing a machine learning classifier.

First, split a set of human-labeled traces into a **development set** and a **test set**. In Langfuse, you can use tags to manage these sets. The **development set** is used to iteratively refine your judge's prompt. Run the evaluator on this set, compare its scores to the human labels, analyze the disagreements, and adjust the prompt's definitions or examples until its judgments closely align with yours:

![Evaluator Tuning](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-09-05-automated-evaluations%2Fevaluator-tuning.png&w=3840&q=75)


Additionally, you can measure the judge's alignment with human labels. The best metrics for this are **True Positive Rate (TPR)** and **True Negative Rate (TNR)**. TPR measures what fraction of actual "Passes" your judge correctly identifies, while TNR measures what fraction of actual "Fails" it correctly identifies.

You can calculate these metrics by querying the data from the trace table (via [UI export](https://langfuse.com/docs/api-and-data-platform/features/export-from-ui) or [SDKs](https://langfuse.com/docs/api-and-data-platform/features/query-via-sdk)) and calculating the metrics.

Once your judge performs well on the dev set (e.g., TPR and TNR >90%), run it a final time on the held-out **test set** to get an unbiased measure of its real-world performance. A validated evaluator with high TPR and TNR gives you confidence that your automated metrics are meaningful.

You can now repeat this process for both your Evaluators in the Langfuse UI and your custom evaluators as part of an [external evaluation pipeline](https://langfuse.com/guides/cookbook/example_external_evaluation_pipelines).

[Next Steps](https://langfuse.com#operationalize-evaluator)

With good automated evaluators in place, the next step is to operationalize your workflow. The goal is to create a CI/CD pipeline where every code change (to a prompt, model, or tool) automatically triggers an evaluation run on a **golden  Langfuse Dataset**.

Your automated evaluators will score these runs, providing immediate feedback on how your changes impacted key failure modes. This continuous monitoring loop helps you develop faster while maintaining a high quality bar for your application.
