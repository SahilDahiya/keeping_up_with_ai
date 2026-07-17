---
title: Langfuse Update — September 2023 - Langfuse
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: langfuse
url: https://langfuse.com/blog/update-2023-09
author: null
published: '2023-10-02'
fetched: '2026-07-17T06:46:58Z'
classifier: null
taxonomy_rev: 2
words: 813
content_sha256: 82da995c25c945f329938c3f9d0b1f4294feb824563d9a54f379c3f078f71449
---

# Langfuse Update — September 2023 - Langfuse

# Langfuse Update — September 2023

Model-based evals, datasets, core improvements (query engine, complex filters, exports, sharing) and new integrations (Flowise, Langflow, LiteLLM)

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc Klingen

Marc KlingenHi everyone 👋, here's a quick overview of all the most notable new features we shipped in September:

- 
**Model-based evaluations**
- 
**Datasets (beta)**
- 
**In-app analytics**
- 
**New integrations**
- 
**Improvements**- [Complex filters](https://langfuse.com#filters)for all tables
- [Share traces](https://langfuse.com#link-sharing)via public link
- [Export generations](https://langfuse.com#export-generations)as CSV, JSON or JSONL (e.g. for fine-tuning)
 

... and many small improvements and bug fixes.

The details 👇

[🚦 Model-based evaluations via Python SDK](https://langfuse.com#model-based-eval)

We've added an [example implementation](https://langfuse.com/docs/scores/model-based-evals) on how to run model-based evaluations on production data in Langfuse using the Python SDK.

The new `get_generations` method allows you to fetch all generations based on a filter (e.g. name). You can then run your eval function on each generation and add the scores to Langfuse for exploration.

With this, you can run your favorite eval library (e.g. OpenAI evals, Langkit, Langchain) on all generations in Langfuse.

```
from langfuse import Langfuse
langfuse = Langfuse(LF_PUBLIC_KEY, LF_SECRET_KEY)
generations = langfuse.get_generations(name="my_generation_name").data
for generation in generations:
    # import function from an eval library, see docs for details
    eval = hallucination_eval(
      generation.prompt,
      generation.completion
    )
    langfuse.score(
      name="hallucination",
      traceId=generation.trace_id,
      observationId=generation.id,
      value=eval["score"],
      comment=eval['reasoning']
    )
```
→ [Docs](https://langfuse.com/docs/scores/model-based-evals)

[🗂️ Datasets (beta)](https://langfuse.com#datasets)

Systematically test new iterations of your LLM app with `datasets`.

Datasets are collections of inputs and expected outputs that you can manage in Langfuse. Upload an existing dataset or create one based on production data (e.g. when discovering new edge cases).

When combined with automated evals, Datasets in Langfuse make it easy to systematically evaluate new iterations of your LLM app.

*Overview of dataset runs on a demo dataset*

![Dataset runs](https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Fdataset_runs_table.png&w=3840&q=75)

*Run experiment on dataset*

```
dataset = langfuse.get_dataset("<dataset_name>")
for item in dataset.items:
    # execute application function and get Langfuse parent observation (span/generation/event, and other observation types: see /docs/observability/features/observation-types)
    # output also returned as it is used to evaluate the run
    generation, output = my_llm_application.run(item.input)
    # link the execution trace to the dataset item and give it a run_name
    item.link(generation, "<run_name>")
    # optionally, evaluate the output to compare different runs more easily
    generation.score(
      name="<example_eval>",
      # any float value
      value=my_eval_fn(
          item.input,
          output,
          item.expected_output
      )
    )
```
```
const dataset = await langfuse.getDataset("<dataset_name>");
for (const item of dataset.items) {
  // execute application function and get Langfuse parent observation (span/generation/event, and other observation types: see /docs/observability/features/observation-types)
  // output also returned as it is used to evaluate the run
  const [generation, output] = await myLlmApplication.run(item.input);
  // link the execution trace to the dataset item and give it a run_name
  await item.link(generation, "<run_name>");
  // optionally, evaluate the output to compare different runs more easily
  generation.score({
    name: "<score_name>",
    value: myEvalFunction(item.input, output, item.expectedOutput),
  });
}
```
```
dataset = langfuse.get_dataset("<dataset_name>")
for item in dataset.items:
    # Langchain callback handler that automatically links the execution trace to the dataset item
    handler = item.get_langchain_handler(run_name="<run_name>")
    # Execute application and pass custom handler
    my_langchain_chain.run(item.input, callbacks=[handler])
```
Datasets are currently in beta on Langfuse Cloud as the API might still slightly change. If you'd like to try it, let us know via the in-app chat.

→ [Dataset docs](https://langfuse.com/docs/datasets/overview)
→ [Python Cookbook](https://langfuse.com/docs/datasets/python-cookbook)

[📊 In-app dashboards](https://langfuse.com#analytics)

Over the last weeks, [analytics features](https://langfuse.com/docs/analytics/overview) were in public alpha on Langfuse Cloud. We've now shipped a new *query engine* as an underlying abstraction for the native in-app dashboards. This is a major step towards bringing all analytics features into the Langfuse core project and helps us move much faster on these.

Over the next days, you'll see more and more dashboards popping up in the app. If there is a specific analysis you'd like to see, suggest it on [Discord](https://langfuse.com/discord).

[🔄 New integrations](https://langfuse.com#integrations)

The new integrations make it easier to get started with Langfuse. Thanks to the teams behind Langflow, Flowise and LiteLLM for building/collaborating on these integrations.

See integrations docs for details:

- [Langflow](https://langfuse.com/docs/langflow): No-code LLM app builder in Python
- [Flowise](https://langfuse.com/docs/flowise): No-code LLM app builder in JS
- [LiteLLM](https://langfuse.com/integrations/gateways/litellm): Python library to use any LLM model as drop in replacement of OpenAI API

[🔎 Complex filters for all tables](https://langfuse.com#filters)

You can now filter all tables in Langfuse by multiple columns.

[🌐 Share traces via public link](https://langfuse.com#link-sharing)

Share traces with anyone via public links. The other person doesn't need a Langfuse account to view the trace.

[💾 Export generations (for fine-tuning)](https://langfuse.com#export-generations)

In addition to the GET API, you can now directly export generations from the Langfuse UI. Supported formats: CSV, JSON, OpenAI-JSONL.

Use Langfuse to capture high-quality production examples (e.g. from a larger model) and export them for fine-tuning.

![Export generations from
Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fupdate-september-2023%2Fexport_generations.gif&w=3840&q=75)


[🚢 What's Next?](https://langfuse.com#-whats-next)

There is more coming in October. Stay tuned! Based on the new query engine we'll ship extensive dashboards over the next weeks. Anything you'd like to see? Join us on [Discord](https://langfuse.com/discord) and share your thoughts.

Subscribe to get monthly updates via email:

Follow along on Twitter ([@Langfuse](https://twitter.com/langfuse), [@marcklingen](https://twitter.com/marcklingen))
