---
title: How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System
  (MAS)
topic: agents
subtopic: multi-agent
secondary_topics:
- evals-observability/evaluation
summary: Case study on scaling data annotation with a human-supervised multi-agent
  system, including review and quality-control loops.
source: cresta
url: https://cresta.com/blog/how-cresta-scales-data-annotation-with-a-human-supervised-multi-agent-system-mas
author: Hagyeong Shin
published: '2026-02-23'
fetched: '2026-07-11T03:58:51Z'
classifier: codex
taxonomy_rev: 1
words: 1543
content_sha256: 5ac5f17ce9dfb1bc3cedd200bf6586a7188447af2fd3f68534facb36bbad5022
---

# How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System (MAS)

**Summary**

Our multi-agent design preserves the core mechanisms that make high-quality human annotation effective. High-quality labeling is inherently rigorous: independent labeling, adjudication, discussion, and final resolution are essential to producing reliable ground truth—especially for enterprise domain data. The challenge is scaling this rigor across thousands of data points without cutting corners. Our multi-agent annotation system addresses that challenge by modeling the human workflow with multiple LLM annotators, structured deliberation, and human oversight and adjudication, delivering scalability while preserving the quality controls that make the dataset dependable.

Constructing a high-quality, human-annotated dataset requires a rigorous process. To get a single label that is credible, the process typically requires a multi-stage workflow:

- Recruit domain experts as annotators
- Train annotators using the established guidelines
- Annotators label data points while adhering to the guidelines
- Identify and adjudicate disagreements, then consolidate labels into a final judgment
- Update the guidelines to incorporate any edge cases and adjudication discussions

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/699cb00a445f306d9b731fc1_blog-scales-data-annotation-figure-1-1.avif)

Many annotation pipelines attempt to scale by using only one annotator or limiting adjudication. That may increase speed, but it often introduces silent failure modes. Limiting the adjudication step often yields incomplete guidelines because the individual annotators often make decisions based on their own implicit understanding not grounded in the guidelines.

These noisy labels across similar cases result in a dataset that stakeholders cannot confidently treat as ground truth. We do not want to skip any steps that ensure the quality of the dataset, because each step in the workflow is essential to make the dataset consistent and trustworthy in the first place.

At the same time, human annotators with domain expertise are often not readily available within the organization. For example, to evaluate the machine-translation layer in Cresta’s [Real-Time Translation](https://cresta.com/blog/when-every-word-matters-engineering-real-time-multilingual-intelligence-for-human-conversations) with human annotators, we’d need to have annotators who are multilingual and skilled at evaluating the translation quality. It is not always feasible to expect readily available internal staff who happen to be fluent in each new language we deploy for Real-Time Translation. Outsourcing the data annotation is not an option either at Cresta, since it goes against our data privacy policy. This is why we leverage LLMs.

To scale data annotation while maintaining quality, we use a **Multi-Agent System (MAS) with human-in-the-loop (HITL) supervision**. The idea is to mirror the human workflow with LLMs, while keeping humans as the final authority. Let’s walk through how we use the MAS to automate some steps of the dataset construction.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/699cafb6bbbf4388a3ebad5b_blog-scales-data-annotation-figure-2-1.avif)

**1. LLMs as annotators**

As mentioned above, staffing human annotators is costly and not always feasible. In our MAS + HITL approach, this step is replaced by selecting multiple LLMs to emulate gathering different perspectives, reducing the need for recruiting and staffing while preserving the benefits of multi-annotator coverage.

We use different frontier reasoning models to mimic diverse opinions and reasoning styles we obtain from human annotators. Each LLM receives the same inputs (data point + guidelines) and produces a label (and rationale) without access to other LLMs’ outputs. This preserves the benefits of multi-annotator labeling: it surfaces ambiguity, reduces single-model bias, and surfaces disagreements.

**2. Human supervision of LLM annotators**

A human oversees the LLM annotators by monitoring common failure patterns, updating instructions in prompts, and running calibration checks. This mirrors the human workflow, where the supervisor verifies that the guidelines are applied consistently and edge cases are handled correctly. We enforce the LLMs to follow instructions in the prompt accurately.

**3. Disagreement detection and adjudication setup**

A single data point often needs labels from multiple annotators, especially for subjective tasks, which are common in Cresta’s high-volume prediction workflows. For example, when labeling an agent’s performance as “good” or “bad,” disagreement is expected. Different annotators may interpret the guidelines differently, weigh evidence differently, or notice different details in the same conversation. These disagreements are not noise; they are signals. Observing and resolving them is essential to ensure the final labels reflect more than one annotator’s judgment.

**4. LLMs as self-adjudicators to generate structured deliberation between LLMs**

When disagreement exists, we orchestrate a separate set of LLMs to deliberate and resolve it. The original annotator models are not used in this step. Self-adjudicator LLMs receive the labels produced during the initial annotation step, but the labels are anonymized—models do not know which annotator model produced which label. We then give the adjudicators a fixed turn budget to converge on a resolution. One adjudicator is randomly selected to initiate the discussion, and the others respond in a round-robin sequence, building on the prior turns.

Self-adjudicator LLMs deliberately use the same inputs human annotators would use: the guidelines and the specific evidence in the data point. These discussions reveal gaps in the guidelines or confusing edge cases that should be clarified. Prioritizing the human supervisor’s review on these highly informative samples means that the human effort is efficiently used for the component that maintains the data quality.

**5. Final verdict by human supervisor**

If disagreement remains after deliberation—or if the case exposes guidelines’ ambiguity—the human supervisor makes the final decision. This ensures the dataset remains coherent and that unresolved ambiguity is handled consistently without preferring any single LLM’s biases.

**6. Spot checks**

The human supervisor runs spot checks on samples of data where LLMs agreed and samples where they disagreed to verify the sanity of the process. If many cases resolve in ways that conflict with human judgments, we run another iteration to improve alignment. A small number of errors can be chalked up to noise in the dataset. Some amount of noise in the dataset is acceptable: a generally clean, large dataset paired with the application of uncertainty estimation can help verify that the results we see are still significant and can be trusted.

**Use case: Translation evaluation with MAS + HITL**

Translation evaluation is a perfect use case of the MAS + HITL workflow described above: it’s subjective enough that multi-annotator coverage and adjudication matter, and it requires language expertise that isn’t always available internally. It’s also a domain where “faster” labeling quickly becomes unreliable; subtle meaning discrepancies can change intent, tone and register shifts can go unnoticed, and omissions or hallucinations can slip through unless the process is built for rigor rather than speed.

To make judgments consistent across languages and annotators, we anchor the workflow in guidelines that define a compact rubric across four preference metrics: keyword fidelity, meaning preservation, grammatical correctness, and tone appropriateness. For each language pair, we select a small panel of frontier reasoning models chosen for strong target-language performance. Each model labels every metric independently and provides a rationale without seeing other models’ outputs.

From there, we follow the same escalation path as the general pipeline: we automatically detect disagreements, route those items into a structured deliberation round run by a separate set of models, and produce proposed final labels grounded in the rubric. Human supervision remains the final authority. The human supervisor audits both agreement and disagreement cases, monitors recurring failure patterns, maps decisions back to rubric criteria, and issues the final verdict, updating the guidelines when needed to improve consistency in future rounds.

The result is scalable, dependable ground truth with end-to-end auditability. For every item, we record the independent labels, disagreement triggers, deliberation output, final decision, and rubric references. This traceability makes it easier for stakeholders to understand why a label was assigned and improves the process over time. It also supports downstream ML iteration: we can distill this knowledge into smaller models, reduce iteration overhead, and validate labels with limited domain expertise.

In a traditional human-only workflow, human effort grows roughly with the full annotation surface area: the number of languages (Z) × the number of rubric metrics (W) × the number of data points per language (N). In practice, doubling languages, metrics, or dataset size roughly doubles the human hours, because every (language × metric × data point) combination needs labeling and often adjudication.

In our experience, even a compact four-metric rubric is expensive to label from scratch. For a single data point, keyword fidelity took 2 minutes, grammatical correctness 3 minutes, meaning preservation 10 minutes, and tone appropriateness (including formality) 2 minutes, adding up to 17 minutes per data point before accounting for adjudication. Multiply that by N items per language and Z languages, and total human hours quickly becomes the bottleneck as you scale. In comparison, the dual LLM annotator approach can label the same data point across all 4 metrics in parallel in a matter of seconds. The overall time savings are even higher due to the parallel nature of the LLM annotation process.

MAS + HITL changes the slope. After an upfront phase to define and calibrate the rubric, humans no longer need to label every item. Human time concentrates on the subset of items that require escalation (disagreements or ambiguous cases) plus a small spot-check rate, while LLMs handle the bulk of per-item labeling and deliberation. As a result, scaling to more data points or more language pairs primarily increases model compute, and human review grows with a much smaller “review rate” than the full dataset size, so you can scale breadth (many language pairs) and depth (multi-metric rigor) without cutting corners on quality.

*In other words, humans focus on the hardest cases, and the system scales everywhere else.*
