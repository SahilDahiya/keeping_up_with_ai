---
title: The platform for inference, training, and execution
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/benchmark-design
summary: Baseten post-trained four US open-weight models (Meta Muse Spark Open, NVIDIA
  Nemotron 3.5 Super VL, Reflection Beam 1.0, Thinking Machines Inkling 2 Small) with
  Harvey on the Legal Agent Benchmark, pushing all-pass rate from a best of 19.2%
  to 30.3% and beating closed models like GPT-6.2 Astra and Claude Fable 5.2, with
  gains holding on unrelated benchmarks like SWE-bench Pro's HARD-51 subset.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/open-weight-models-beat-the-closed-frontier-on-legal-tasks-with-harvey/
author: Jonathon Liu; Xavier Morris; Will Rankin; Aaron Ellis-Bloor; Matthew Blau;
  Albert Lee
published: '2026-11-24'
fetched: '2026-11-25T06:07:45Z'
classifier: claude
taxonomy_rev: 2
words: 656
content_sha256: 694c000b7316ddcc6e0373edf9ba2241f31f13c2cd4febc59e37e3bf637a451a
---

# The platform for inference, training, and execution

News
# Open-weight models beat the closed frontier on legal tasks with Harvey

Results from training Muse Spark Open, Nemotron 3.5 Super VL, Beam 1.0, and Inkling 2 Small on agentic legal work


- Authors
- Published

It’s been a big year for American open-source intelligence. Teams from Meta, NVIDIA, Reflection, Thinking Machines, and others have released frontier models of varying sizes and capabilities, giving enterprises many more ways to control their intelligence. Post-training is a big part of that: customizing model weights on your specific task or domain is a relatively low-cost way to outperform the frontier. Today we’re releasing our results with the Harvey team on how much post-training can improve success rate on complex, multi-step legal tasks, **showing that post-trained US open-weight models can outperform closed frontier models.**

We post-trained four recently released open-weight models from US labs, covering different sizes and architectures. Before this study, no model—closed or open—had reached a 30% all-pass rate (satisfying every rubric criterion on a task) on the [Legal Agent Benchmark](https://github.com/harveyai/harvey-labs) (LAB). After post-training, Muse Spark Open reached 30.3%, and all four US open-weight models scored higher than GPT-6.2 Astra and Claude Fable 5.2.

We also found that post-training provides improvement over each base model at *every* reasoning effort so the gains come from training rather than simply letting the model think longer.

In addition to evaluating each model on LAB, we also benchmarked each model on [LAB Contracts](https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting), which evaluates each model's capacity to draft, review, and negotiate routine business contracts. We saw generalization despite no tasks of this nature being present in the training set.

We also evaluated each post-trained model on the hard subset of SWE-bench Pro ([HARD-51](https://github.com/scaleapi/SWE-bench_Pro-os)) to check for regressions on a largely unrelated agentic benchmark. Compared with each original model across all of its reasoning levels, every post-trained model sits on or above the original model's Pareto frontier. This shows that this increased performance on agentic legal tasks **does not** come at the cost of performance across other domains, such as coding.

Every US open-weight model showed significant uplift that indicated they can be effectively post-trained to achieve high performance in specific tasks and in other domains, even when baseline benchmark scores are low. For instance, despite low initial scores on LAB, both Beam 1.0 and Nemotron 3.5 Super VL achieved performance competitive with closed frontier models following post-training.

We and our enterprise customers are excited about the potential of US open-weight models, as these results demonstrate that you can start from a base model, post-train on your own unique data, and surpass the performance of a closed-source model.

Beyond legal, we also evaluated the models on agent benchmarks covering consulting, banking, business automation, and software engineering, avoiding regression and even showing uplift across different domains that the model was never trained on.

Our applied research team can partner with you to post-train open models for your specific use cases, giving you full ownership of the resulting weights. With [built-in security](https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/) on Baseten, you stay in control of where your model runs and who can use it.

[Connect with Baseten Applied Research](https://www.baseten.co/talk-to-us/research-support/) to learn more.

| Model | Type | All-pass % before | All-pass % after | 
|---|---|---|---|
| Meta Muse Spark Open | US open-weight | 19.2% | 30.3% | 
| Google Gemini 4 Argon | US closed-weight | 27.1% | - | 
| Thinking Machines Lab Inkling 2 Small | US open-weight | 11.7% | 23.3% | 
| NVIDIA Nemotron 3.5 Super VL | US open-weight | 1.3% | 21.8% | 
| Reflection Beam 1.0 | US open-weight | 0.0% | 20.8% | 
| OpenAI GPT-6.2 Astra | US closed-weight | 16.3% | - | 
| Anthropic Claude Fable 5.2 | US closed-weight | 5.0% | - | 

*Note: Closed-source model all-pass rates on HLAB-Vals were conducted on a slightly different harness. We have reproduced the Gemini 4 Argon HLAB-Vals results on our harness within 1 percentage point.*
