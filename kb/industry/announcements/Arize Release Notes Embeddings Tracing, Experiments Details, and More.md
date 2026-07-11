---
title: 'Arize Release Notes: Embeddings Tracing, Experiments Details, and More.'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/tracing
summary: Arize release notes covering embeddings, tracing, experiment details, and
  observability workflow improvements.
source: arize
url: https://arize.com/blog/arize-release-notes-embeddings-tracing-experiments-details-and-more/
author: Sarah Welsh
published: '2024-10-03'
fetched: '2026-07-11T04:50:14Z'
classifier: codex
taxonomy_rev: 1
words: 606
content_sha256: 2ddd3b3dd1eba96e3d7fc6920de369ea6261f835f6d99a19c5d2a21ad6c07a47
---

# Arize Release Notes: Embeddings Tracing, Experiments Details, and More.

![Release notes 10-3 Release Notes October 3, 2024](https://arize.com/wp-content/uploads/2024/10/Release-notes-10-3-1021x560.jpg)

              # Arize Release Notes: Embeddings Tracing, Experiments Details, and More.

Welcome to our regular update on new releases, enhancements, and changes.

## What’s New

## Embeddings Tracing

With Embeddings Tracing, you can effortlessly select embedding spans and dive straight into the UMAP visualizer, simplifying troubleshooting for your genAI applications. How this works:

- Users can now select embedding spans and go to the embedding visualizer (also available on project level nav for all generative models)
- All embedding spans get pulled over for UMAP + clustering
- Users can select an individual point/cluster and the embedding span attributes get pulled over
- “Color by” span attributes is also available, and whichever attribute users “color by” can also be viewed as a column in the table

*Note: this functionality is only viewable for embedding spans after October 2, 2024.*

[Learn more about our embeddings visualizer here](https://docs.arize.com/arize/computer-vision-cv/how-to-cv/embedding-and-cluster-analyzer).

## Experiments Details Visualization

Users can now view a detailed breakdown of labels for their experiments on the Experiments Details page.

Note: this feature is currently only available for label-based evaluations. Support for score-exclusive evaluations will be coming in a future update.

![Compare Experiments](https://arize.com/wp-content/uploads/2024/10/Compare-Experiments.avif)

## Enhancements

### Prompt Playground Improvements

- **Full OpenAI Models Support:**We’ve added full support for all available OpenAI models in the playground including the o1-mini and o1-preview.
- **OpenAI Function/Tool Calls:**With OpenAI’s addition of function calling in their models, we have added support in Arize starting from the trace all the way to the playground. View function/tool calls in your traces, and open the playground to further experiment and test.
- **Full-screen Data Mode:**Enter full screen mode to view your data more easily.
- **Features For Datasets:**- **Prompt Overriding:**When using a dataset to test out different prompts, users can now replace the prompt template with the dataset.
- **Pop Up Windows for Long Outputs & Variables:**Viewing longer outputs is now easier with pop up windows.


Along with these features, we’ve added improvements such as better input variable behavior, autocompletion enhancements, support for mustache/f-string input variables, and more.

![prompt playground](https://arize.com/wp-content/uploads/2024/10/Playground-1024x1024.png)


## Filters Updates

- **Filter History:**We now store the last three filters used by a user! Users can easily access their filter history in the query filters dropdown, making it simpler to reuse filters for future queries.

![filter history](https://arize.com/wp-content/uploads/2024/10/Filter-histroy-1024x424.png) Traces Page Updates

Traces Page Updates

- **Parent Spans:**We’ve enhanced the Traces page to give users a better experience when filtering spans. Now, even if the filter doesn’t match the parent span, users will still see the the parent span with the relevant spans nested under it.
- **Quick Filters:**We’ve introduced quick filters, allowing users to apply filters directly from the table by hovering over the text to reveal the filter icon.

![Spans](https://arize.com/wp-content/uploads/2024/10/Spans.png)


## New Arize-Otel Package for LLM App Tracing

We heard you, and we made it much simpler to add automatic tracing to your applications! It’s now just a few lines of code to use OpenTelemetry to trace your LLM application. [Check out our new quickstart guide which uses our arize-otel package](https://docs.arize.com/arize/llm-tracing/quickstart-llm).

## Workflow Improvements

- Support for new line creation while reviewing prompts.
- Easily add spans to a dataset from the Traces page using the “Add to Dataset” button.
- Quickly create an evaluation task within a trace if no evaluations currently exist using the “Setup Task” button.

![trace details](https://arize.com/wp-content/uploads/2024/10/Trace-details.png)


## 📚 New Content

The latest video tutorials, paper readings, ebooks, self-guided learning modules, and technical posts:

🧑⚖️ [Selecting the Right Model for LLM-as-a-Judge Evaluations](https://arize.com/blog/choosing-the-best-llm-evaluation-model/)

🤖 [Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems ](https://arize.com/blog/arize-ai-mongodb-agentic-systems/)

🔭 [Exploring OpenAI’s o1 Models ](https://arize.com/blog/exploring-openai-o1-preview-and-o1-mini/)

🪞[Breaking Down Reflection Tuning](https://arize.com/blog/breaking-down-reflection-tuning-enhancing-llm-performance-with-self-learning/)
