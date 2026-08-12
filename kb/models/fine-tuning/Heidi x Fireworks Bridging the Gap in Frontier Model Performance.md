---
title: 'Heidi x Fireworks: Bridging the Gap in Frontier Model Performance'
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- inference/optimization
summary: Heidi's clinical-note scribe moved from closed frontier models to a two-stage
  pipeline (SFT to imitate style, then RFT/DPO for preference-based quality) on Fireworks,
  cutting latency from 25s to 7s and outperforming Gemini Flash/Pro tiers in side-by-side
  evals; success depended on high-quality filtered data and larger effective batch
  sizes.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/Heidi-Health
author: null
published: '2026-07-20'
fetched: '2026-08-12T06:29:51Z'
classifier: claude
taxonomy_rev: 2
words: 580
content_sha256: 8f011dbf2f593447c40e2c352760e880e6b6302d231aa2860726955de2e82683
---

# Heidi x Fireworks: Bridging the Gap in Frontier Model Performance

Heidi, a leader in ambient AI scribe technology, has partnered with Fireworks to achieve and surpass the quality of proprietary frontier models, delivering faster, more reliable, and cost-effective AI solutions for clinicians.

Heidi’s flagship product is an ambient AI scribe that transcribes clinician-patient encounters and generates professional clinical notes. This solution offers immense value, primarily saving clinicians up to 2 hours every working day, significantly boosting productivity and connection.

Heidi was looking for a partner to move from closed to open models to gain more control, better performance, and significant cost savings. Their top criteria for a partner were:

- •**Technical Capability and High-Quality Product:** A platform that could support their performance goals.
- •**Trustworthy & Transparent:** A clear and open relationship.
- •**Collaborative Teams:** A partner willing to work closely on the solution.

Fireworks' solution stood out due to its superior optimization on model [fine-tuning](https://fireworks.ai/training) and [inference](https://fireworks.ai/inference). The ability to take advantage of **specialized intelligence**, transforming general purpose models into AI tailored to Heidi’s usecase was a game-changer. It allowed Heidi to increase model performance and quality, reduce and control latency (dropping from 25 seconds to 7 seconds), and realize huge cost savings.

The path from Proof of Concept (POC) to production took just **4 weeks**, demonstrating the speed and utility of the solution.

The combined Heidi x Fireworks solution delivered two major breakthroughs in model quality, which was the most important factor for Heidi:

1. **Supervised Fine-Tuning (SFT):** The initial step, which "imitates" foundation model behavior to learn content style, resulted in a model that**outperformed the Gemini Flash tier of models*** .
2. **Reinforcement Fine-Tuning (RFT):** The recent breakthrough, which shifts the model from imitation to "deep thinking" by incorporating preference signals, resulted in a model**whose outputs were preferred over the Gemini Pro tier (frontier) models*** .

*In Heidi's internal side-by-side evaluation on its clinical note dataset

The technical study by Heidi revealed that simply adopting an advanced algorithm like Direct Preference Optimization (DPO) is not enough. Success hinged on two critical operational levers: **high quality data through rigorous filtering** and **larger effective batch sizes**.

Heidi’s experiments confirmed that raw Side-by-Side (SBS) preference data is noisy, with evaluators often choosing responses that still contain hallucinations. The successful filtering strategy involved:

- •**Synthetic Rewrites:** Using frontier models to generate high-quality synthetic target outputs, creating a "golden standard" target.
- •**LLM-as-a-Judge:** Employing an LLM to align with quality standards and strictly pre-evaluate datasets for safeguard metrics (like Template Adherence and Details Omission), further de-noising the feedback.

To overcome the noise that remains even after rigorous filtering, Heidi scaled their effective batch size to approximately **1.5 million tokens**. This strategy, directly enabled by Fireworks' support for gradient accumulation (up to 24 steps), ensures that every weight update is derived from a massive sample distribution. This process effectively de-noises the gradient signal by averaging out the contribution of any individual bad data point.

In a key experiment, increasing the effective batch size from a standard 64k to 768k tokens resulted in a direct win rate improvement from 48.0% to **51.3%** over proprietary models.

The experiments validate that open models can rival proprietary frontier models when subjected to rigorous DPO. The final blueprint for success is:

1. **Curate aggressively:** Use synthetic data and SBS signals filtered through LLM Judges to build DPO pairs. Don't trust raw SBS.
2. **Scale the Batch:** Aim for 1M+ token effective batch sizes using gradient accumulation.
3. **Evaluate:** Run pre-evaluations on datasets to catch regression risks before training.
