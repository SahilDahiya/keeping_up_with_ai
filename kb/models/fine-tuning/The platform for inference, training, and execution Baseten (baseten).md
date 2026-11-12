---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: A sweep across Qwen3 and Llama dense/MoE models up to 235B parameters measures
  how optimal learning rate and batch size shift with scale and data for LoRA versus
  full fine-tuning, and whether validation loss reliably predicts downstream LLM-judge
  quality.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/post-training-science-for-supervised-fine-tuning
author: Charles O'Neill
published: '2026-06-18'
fetched: '2026-11-12T06:16:04Z'
classifier: claude
taxonomy_rev: 2
words: 291
content_sha256: 4eae002f66a3c485e02c53712f8966a1e44ca0edf3c08201ae0ddaef34e97bca
---

# The platform for inference, training, and execution | Baseten

Research
# Post-Training Science for Supervised Fine-Tuning

How the optimal learning rate and batch size move with model scale, family, and data, and whether one selection rule transfers across them.


- Authors
- Date
- June 18, 2026

**Summary:** Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset.

Here we measure them under one instrument: a sweep that varies one lever at a time, and spans dense and mixture-of-experts models in two families (Qwen3 and Llama), on four real-world customer SFT datasets, for both LoRA and full fine-tuning. These datasets give a controlled testbed: each task carries an evaluation built with the customer, and its training data is produced by iterative supervised fine-tuning that refines model outputs until they pass that evaluation, so the supervised target is internally consistent and the task judge we report against is the criterion the data was built to satisfy.

We ask how the optimal learning rate and batch size move with model scale, family, and data, and whether one selection rule transfers across them; what LoRA trades against full fine-tuning, and how its rank and α set what the adapter can learn; whether validation loss (or other metrics, such as loss landscape flatness) faithfully ranks downstream quality; whether post-training gains scale with model size and data volume, on a model ladder extended through mixtures-of-experts to 235B parameters; how many epochs to train before general instruction-following erodes; and whether a geometry-aware optimiser improves on AdamW. Each recommendation is paired with a measure of its uncertainty.

Read the paper [here](https://www.datocms-assets.com/104802/1781805778-baseten-research-sft.pdf).
