---
title: 'Arize Release Notes: Prompt Hub, Managed Code Evaluators and More'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/evaluation
summary: Arize release notes covering Prompt Hub, managed code evaluators, and evaluation
  workflow improvements.
source: arize
url: https://arize.com/blog/arize-release-notes-prompt-hub-managed-code-evaluators-and-more/
author: Sarah Welsh
published: '2024-12-19'
fetched: '2026-07-11T04:51:04Z'
classifier: codex
taxonomy_rev: 1
words: 520
content_sha256: ea0e176d12653f8b31c4971a317b289a043e44853f587aca237b131fcdd2ede2
---

# Arize Release Notes: Prompt Hub, Managed Code Evaluators and More

![Release notes 12-19 Text reads: Release Notes, December 19, 2024 with the Arize logo.](https://arize.com/wp-content/uploads/2024/12/Release-notes-12-19-1021x560.jpg)

              # Arize Release Notes: Prompt Hub, Managed Code Evaluators and More

Welcome to our regular update on new releases, enhancements, and changes.

## What’s New

### Prompt Hub

[The Prompt Hub](https://docs.arize.com/arize/prompt-engineering/prompt-hub) is a centralized repository for managing, iterating, and deploying prompt templates within the Arize platform. It serves as a collaborative workspace for users to refine and store templates for various use cases, including production applications and experimentation.

Key features of the Prompt Hub include:

- **Template Management**: Users can save templates directly from the Prompt Playground along with associated LLM parameters, function definitions, and metadata required to reproduce specific LLM calls.
- **Version Control**: Every saved template supports versioning, enabling users to track updates, experiment with variations, and revert to previous versions if needed.
- **Collaboration and Reusability**: Saved templates can be shared across teams, facilitating collaboration and consistency in production workflows. Templates can also be reloaded into the Prompt Playground or accessed via APIs for seamless integration into codebases and online tasks.
- **Evaluation and Optimization**: By saving outputs as experiments, users can compare templates, compute evaluation metrics, and analyze performance both quantitatively and qualitatively.

### Managed Code Evaluators

We recently launched [a set of pre-built, off-the-shelf evaluators](https://docs.arize.com/arize/llm-evaluation-and-annotations/catching-hallucinations/code-evaluations) to enable users to evaluate their spans without requiring requests to an LLM-as-a-Judge.

Evaluators available:

- **Matches Regex**: Checks if text matches a specific regular expression pattern.
- **JSON Parseable**: Validate JSON output from LLMs.
- **Contains Any Keyword**: Check if any keywords appear in the text.
- **Contains All Keywords**: Validate that all specified keywords are present.


## Enhancements

### Experiment Creation From Playground

We just released a [ new flow for creating experiments](https://docs.arize.com/arize/prompt-engineering/prompt-playground#save-outputs-as-experiment) from outputs generated with the Prompt Playground. What’s new?

**Quickly Experiment**: After running the playground successfully on a dataset, click the “Save as Experiment” button.

- **Debug**: In addition to the newly outputted response, we save the LLM invocation parameters & prompt template message structure for greater replay functionality.
- **Compare**: Just like our existing experiments, you can compare the playground outputs as well.

### New Monitor Visualization

We’ve rolled out the first part of our monitor improvements! Here’s what’s new:

- **Alert Status Graph**: Maps directly to the alerts users see, giving them a transparent and seamless way to line up alerts with the real-time metric visualization.
- **Cleaner UX**: Updates include removing “last run monitor time,” aligning card titles and Y-axis with metric names, and simplifying by removing granularity.


*Note: Alert ticks are limited—users may need to zoom into specific dates to see all alerts.*

![Screenshot of monitor visualization in Arize](https://arize.com/wp-content/uploads/2024/12/AI-Search-errors-1024x594.png)


### LangChain Instrumentation

Support for sessions via LangChain native thread tracking in TypeScript is now available. Easily track multi-turn conversations / threads using LangChain.js.

## 📚 New Content

The latest video tutorials, paper readings, ebooks, self-guided learning modules, and technical posts:

✈️ [How ](https://arize.com/blog/how-booking-com-enhances-travel-planning-with-ai-trip-planner-and-arize-ai/)[Booking.com](http://booking.com/)[ Personalizes Travel Planning with AI Trip Planner and Arize AI](https://arize.com/blog/how-booking-com-enhances-travel-planning-with-ai-trip-planner-and-arize-ai/)

♾️ [How to Add LLM Evaluations to CI/CD Pipelines](https://arize.com/blog/how-to-add-llm-evaluations-to-ci-cd-pipelines/)

📛 [2025 AI Conferences](https://arize.com/blog/2025-ai-conferences/)

🤝 [Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies](https://arize.com/blog/merge-ensemble-and-cooperate-a-survey-on-collaborative-llm-strategies/)
