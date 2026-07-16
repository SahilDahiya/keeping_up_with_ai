---
title: How we chose the model behind Topics with Baseten - Blog - Braintrust
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- product-engineering/case-studies
summary: Details how Braintrust and Baseten chose and tuned a sub-10B model (Gemma
  4B, beating Qwen) to summarize every production trace for the Topics feature, built
  a 650-example benchmark across label correctness/factuality/issues-recall/false-positive-rate,
  and improved Issues recall from 0% to 32.8% through prompt iteration alone (no fine-tuning).
triage: null
skip_reason: null
source: braintrust
url: https://www.braintrust.dev/blog/model-behind-topics-baseten
author: Braintrust Team
published: '2026-07-15'
fetched: '2026-07-16T06:48:38Z'
classifier: claude
taxonomy_rev: 2
words: 1330
content_sha256: cc29575a15f1c72765664abf9eeb3bb44abbb4ccebe8911f36abc7fbbc908adc
---

# How we chose the model behind Topics with Baseten - Blog - Braintrust

15 July 2026Izzy Hurley8 min

If you run agents in production, the behavior worth knowing about is spread across more traces than anyone can read by hand. The failures, the shifts in what people are asking for, and the slow regressions are all in there.

[Topics](https://www.braintrust.dev/docs/observe/topics) reads production traces with an LLM, summarizes each one, and clusters the summaries, so you can see what your agents are doing across all of your traffic without reading logs one by one. It runs continuously in the background, on every trace. We call this [active observability](https://www.braintrust.dev/blog/active-observability). Braintrust works on your production data on its own, instead of waiting for you to write the right query.

Running that kind of intelligence on every trace is only affordable with a small model that is cheap to run and still good enough to read what is happening inside a trace. That balance took close work with Baseten. We started with an off-the-shelf Gemma 4B model, built a benchmark from real Topics traces, and iterated against the failure modes that mattered most.

Topics uses a model to do one job. It reads each trace and summarizes it in a sentence or two along a dimension like task, issues, or sentiment. Everything after that step works off the short summary rather than the raw trace. We embed and cluster the summary, then classify each new trace with a roughly 100-millisecond lookup and no LLM call. The summary is the only expensive step, and it runs once on every trace, so the cost of that model determines whether the whole feature is viable. We batch all of a trace's facets into a single call, so the trace tokens are paid once and running several facets costs about the same as running one.

That created three constraints:

- Topics is most useful at 100% coverage. Sampling can miss the long tail, where many interesting failures live.
- Frontier models are too expensive to run on every trace, so Topics relies on a smaller model that still meets the quality bar.
- Small models are cheap, but easy to get wrong. Without a rigorous benchmark, you are only guessing whether "good enough" is good enough.

The model behind Topics is a Braintrust-managed model served on Baseten. We partnered on both the model and the serving stack. Gemma 4B was the best small model in our initial exploration, and we limited the search to models under 10B parameters to stay within cost constraints.

Baseten owned the model and serving system, making a small model fast and cheap enough to run continuously. Braintrust owned the benchmark and the production data, which showed whether a change made Topics better. Both teams measured every serving change and prompt change against the same benchmark.

Most of the quality work was concentrated in the summarization step, where the prompt is designed to work with the model. The model behind Topics is not fine-tuned today. Our customers deploy agents in large, complex, and constantly changing environments, so they need to define and customize their own [facets](https://www.braintrust.dev/docs/observe/topics/custom-facets) in addition to the defaults we provide. In pilot tests, careful prompting and representative examples have been more useful than fine-tuning for that flexibility. We refer to this combination of a strong base model, prompts, and example traces as our **task-calibrated model**.

Serving mattered as much as raw quality, so we optimized latency and throughput together. Each summary call completes in about 10 seconds, with tail latency up to 60 seconds during traffic spikes because we batch requests asynchronously. That works for this background pipeline because every trace is still processed, and individual tail latency does not obscure the aggregate trends.

Baseten also handles the hosting posture, with zero data retention on inference payloads, US and EU regions, and HIPAA compliance.

We built the initial benchmark from 650 real Topics traces: 220 Issues rows, 215 Task rows, and 215 Sentiment rows. Each entry could be graded along several dimensions:

- Label correct: whether the predicted facet label matches the audited label.
- Factuality: whether the explanation is grounded in the trace.
- Issues recall: whether the model catches a real failure for Issues rows.
- False-positive rate: whether the model incorrectly flags normal rows as failures.

The off-the-shelf Gemma 4B model scored 81.1% label correctness overall, but had 0.0% Issues recall, meaning it almost never caught real issue cases. Qwen scored 76.5% label correctness with a 22.1% Issues false-positive rate, 26.2% Issues recall, and 58.8% subtype accuracy when it detected an issue.

Most of the iteration happened in the prompt and the examples the model sees. We shaped the Issues prompt and the example traces it reasons from while keeping the model weights and the scored comparison dataset fixed. The prompt changes covered retry handling, quoted-history handling, final-turn rules, and domain-specific "No response" examples. On the serving side, later runs tested a consolidated profile configuration and an FP8 Gemma serving endpoint.

One run with the adjusted prompt and configuration reached 78.3% label correctness and improved Issues recall to 32.8%. It also beat Qwen on the reduced Issues metrics we cared about most: lower false-positive rate, higher recall, and higher subtype accuracy when it detected an issue.

There was not a clean aggregate win over every frontier model in every run. GLM 5.2 reached 82.1% label correctness, and GPT-5.4 reached 81.5%. But the contextualized Gemma design beat Qwen, GLM 5.2, and GPT-5.4 mini on Issues recall, while costing **$244.50 per million examples**. That was about one-third of Qwen, one-quarter of GLM 5.2, one-fifth of GPT-5.4 mini, and roughly 4% of GPT-5.4.

The production setup built on those iterations and reached 82.2% label correctness, 41.5% Issues recall, and a 10.3% Issues false-positive rate. Reaching it took a sequence of small, measured improvements against the same benchmark.

Baseten and Braintrust owned different parts of the work and judged progress with the same benchmark.

That benchmark made every change measurable. The off-the-shelf model caught almost no Issues, and each change to the prompt and serving setup showed up in Issues recall. The setup we shipped recovered meaningful Issues recall at a fraction of the cost of frontier models.

A small model, shaped with the right prompt and examples and held to a real benchmark, can beat frontier models on the metric you care about while costing a fraction as much to run. Active observability is only affordable because of models like this. None of it is specific to Topics, though. Any product that runs an LLM over a lot of data faces the same cost and quality problem, and the same approach solves it.

You do not need to be building Topics to use this. If you are running a model over production data for your own product, whether that is classification, extraction, routing, or scoring, the path is the same one we used, and the same one Braintrust is built for.

- Build a real benchmark from your task. Turn the job into a labeled dataset with a clear metric and a holdout set, so "good enough" becomes a number you can move.
- Put candidate models side by side. Run each model against frontier baselines on the same data with the same scorers.
- Iterate with [evals](https://www.braintrust.dev/docs/evaluate)in the loop. Make a change, run the eval, and keep what moves the numbers you care about.
- Optimize your own facets. Use the [facet optimizer](https://github.com/braintrustdata/facet-optimizer)for custom facets, and run the same loop on your evals to improve them.
- Ship it and watch production. Trace the model, monitor for drift, and let production feed the next round.

For the full pipeline behind Topics, from preprocessing through clustering to classification, read [How we made continuous trace intelligence possible at scale](https://www.braintrust.dev/blog/topics-architecture).

Ready to understand what is happening across your traces? Open **Topics** in [Braintrust](https://www.braintrust.dev/), [enable it for your project](https://www.braintrust.dev/docs/observe/topics/enable), and turn large volumes of unstructured production data into clear, actionable patterns.

For a guided walkthrough, [book a demo](https://www.braintrust.dev/contact) to see how Topics can help you uncover insights faster.
