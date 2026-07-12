---
title: Synthetic data pipeline for fine-tuning and evaluation
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/evaluation
summary: Describes a synthetic-data pipeline that connects task definition, generation,
  SFT/RFT, evaluation, and cleanup.
source: fireworks
url: https://fireworks.ai/blog/synthetic-data-pipeline
author: null
published: '2025-06-04'
fetched: '2026-07-11T04:13:44Z'
classifier: codex
taxonomy_rev: 1
words: 942
content_sha256: fb720f6f6aa05f4a2f309a9f15d27dff35437f763d3ebbe26beaac17817960a1
triage: keep
skip_reason: null
---

# Synthetic data pipeline for fine-tuning and evaluation

In modern AI workflows, access to large, well‑curated datasets is often the bottleneck for achieving production‑grade model performance. To address this, we developed an end‑to‑end system that **automates** synthetic data generation, quality control, and iterative fine‑tuning, delivering in hours what traditionally takes weeks. Below, we dive into the technical architecture, key components, and performance gains of this workflow.

The pipeline is composed of five interlinked stages:

- Task Definition and Config Generation
- Dataset Customization and Synthetic Generation
- Automated Fine-Tuning (SFT/RFT) and Evaluation
- Data Cleaning and Feedback Integration
- Model Fine-Tuning and Accuracy Benchmarking

At its core, the pipeline leverages large language models (LLMs) to orchestrate generation logic, apply dynamic constraints, and drive intelligent iteration through automated evaluation loops.

- •**Task Input**- •User provides a high‑level task description (e.g., “Classify support tickets by urgency”).
- •The orchestrator invokes the LLM to **generate a base YAML config**, specifying:- •Dataset type (classification, extraction, summarization)
- •Input/label schema
- •Sampling parameters (size, class balance)
- •Example prompts and edge‑case scenarios


- •**Config Enhancement**- •Automated routines enrich the base config with:- •**Contextual prompts**(e.g., domain definitions, style guidelines)
- •**Quality controls**(min/max length, profanity filters)
- •**Diversity controls**(ensuring coverage across entity types, sentiment)
- •**Evaluation metrics**to be tracked

- •

- •Automated routines enrich the base config with:
- •**YAML Formatting & Export**- •The enriched config is serialized into a clean, documented YAML file which you can edit within the same dashboard.
- •Inline comments, section headers, and logical grouping facilitate human review.


**Smart Defaults**

- •Technical tasks: temperature → 0.1–0.3 for deterministic outputs
- •Creative tasks: temperature → 0.7–1.0 for richer variation

Once the YAML config is reviewed and optionally modified by the user, it is uploaded to the generation dashboard. This interface provides operational transparency into data generation progress, including:

- •Throughput metrics (TPS, TTFB)
- •Model version and parameters in use
- •Per‑job views showing aggregate statistics; per‑row views showing generated text + raw metrics.

Generated data is streamed in JSON format, where each entry includes:

- •Prompt (as specified by the config)
- •Model-generated response
- •Metadata (token count, latency, generation seed)

Each row is stored with associated quality metrics, facilitating downstream filtering and inspection. The platform supports row-level and job-level visualization, allowing for granular validation and debugging. Planned enhancements include a "model jury" mechanism, where multiple models independently generate candidate responses for each prompt and vote on the most reliable output, as well as live data retrieval via APIs (e.g., SerpAPI) to inject fresh and topical content into synthetic examples.

After initial generation, the dataset is used for multiple rounds of automated fine-tuning and evaluation loops.

We first define an **Evaluation Criteria** using “[deepseek r1](https://fireworks.ai/blog/deepseek-r1-deepdive)”. We create an LLM-as-judge evaluation flow to score responses. It is also beneficial to expose single-shot examples of real data to the evaluator prompt to guide the evaluation process.

We then run multiple rounds of **Reinforcement‑Fine‑Tuning (RFT)**, using the scores from the LLM-as-judge evaluator to guide the model.** **Throughout this loop, the system clusters low-performing outputs (e.g., incorrectly classified samples, incoherent responses) to surface latent knowledge gaps. These gaps could potentially be used to update the original YAML configuration, e.g., adding more diverse samples, expanding label definitions, or including domain-specific instructions, thus driving continuous improvement in the next iteration.

The RFT loop simultaneously trains a model that performs better on the target task, while also guiding the dataset generation process to create more challenging examples, all without training on any real-world data examples.

This significantly improves the accuracy of the model on the target task, making it comparable to a model fine-tuned on real-world datasets.

| Model | Accuracy | Data |
|---|---|---|
| Baseline (no tuning) | 52% | NA |
| SFT on curated data | 79% | Requires client data and curation effort |
| RFT on synthetic data | 73% | No requirement for client data |

- •**Intelligent Automation**Orchestrates LLM prompts, job scaling, and evaluation in a single pipeline.
- •**Smart Defaults**Context‑aware temperature and top‑p settings ensure precision vs. creativity trade‑offs.
- •**Quality Control**Built‑in validators enforce length, diversity, and accuracy constraints before data rolls out.
- •**Domain Flexibility**Easily switch between use cases,classification, extraction, summarization, dialogue.
- •**Dataset Quality Loop**Automatic SFT/RFT + clustering drives continuous improvement in synthetic data.

- •**Demo fine‑tuned models in hours**, not weeks,no need for client proprietary data.
- •Synthetic data preserves compliance: **no PII**,**no GDPR exposure**.
- •Fine‑tuned models from this pipeline **outperform base models**, matching or exceeding traditional workflows.

The pipeline incorporates multiple automation and orchestration features:

- •End-to-end coordination of prompt design, config validation, job execution, and evaluation
- •Smart defaults and templates for different use cases and model types
- •Built-in validation layers to enforce length, diversity, and quality constraints
- •Dynamic YAML re-configuration based on evaluation feedback

Planned upgrades include:

- •An interactive YAML builder with a chat-based interface for schema population and sample previews
- •Model jury consensus mechanism for more reliable generations
- •Batch APIs for massively parallel throughput
- •Real-time gap-driven re-generation workflows

The synthetic data pipeline developed by Fireworks AI provides an efficient, scalable, and compliant approach to dataset generation and model fine-tuning. By combining LLM orchestration, rigorous evaluation loops, and intelligent feedback mechanisms, the pipeline enables ML practitioners to build production-ready models in hours instead of weeks.

With ongoing advancements in retrieval augmentation, reward modeling, and orchestration logic, this system is poised to become a foundational layer in future AI model development stacks.

Explore the full implementation and try it out: [https://github.com/aisrini/synthetic-data-generation/tree/main/synthetic-data-generation ](https://github.com/aisrini/synthetic-data-generation/tree/main/synthetic-data-generation)

If you are getting started with Supervised Fine tuning, check out this step-by-step guide: [https://fireworks.ai/blog/supervised-fine-tuning-tutorial](https://fireworks.ai/blog/supervised-fine-tuning-tutorial)

Detailed docs on Supervised Fine-tuning can be found here: [https://docs.fireworks.ai/fine-tuning/fine-tuning-models](https://docs.fireworks.ai/fine-tuning/fine-tuning-models)
