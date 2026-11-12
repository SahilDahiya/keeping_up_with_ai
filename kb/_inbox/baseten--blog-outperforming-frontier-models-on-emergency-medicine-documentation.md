---
title: Outperforming frontier models on emergency medicine documentation
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/outperforming-frontier-models-on-emergency-medicine-documentation
author: Harry Partridge
published: '2026-03-03'
fetched: '2026-11-12T06:14:38Z'
classifier: null
taxonomy_rev: 2
words: 1921
content_sha256: 2bb4966b0ca04e27f911a2d8561fb3a9d3132c3db323837356b9adfb60fe0b9f
---

# Outperforming frontier models on emergency medicine documentation

AI engineering
# Outperforming frontier models on emergency medicine documentation

We trained a specialist model that beats frontier Gemini models on clinical documentation and runs 6–8x faster.


- Authors
- Date
- March 3, 2026

TLDR

A company that builds ambient scribes that convert emergency department (ED) conversations into structured clinical charts came to us with a specific challenge: build a model capable of handling the complexity of emergency medicine documentation while being fast enough for real-time use. The task involves two stages. First, convert (often messy) ED transcripts into structured JSON with 16 distinct sections. Second, merge that JSON with physical exam templates to produce the final chart. Each stage has dozens of interlocking rules that must be followed precisely. This is quite scary because getting things wrong means the model has introduced liability issues, as well as just generating a bad note. We built a model that achieves 84.8% accuracy on chart generation and 67.2% on summarization, compared to gemini-2.5-pro's 63.6% and 47.2%. It also runs 6-8x faster.

Emergency physicians spend 2-3 hours per shift on documentation. In addition, emergency department notes aren't like other medical documentation. Information comes from multiple sources simultaneously: the patient, EMS, family members, and prior records. The clinician must document not just what happened but also what didn't happen, in particular by explicitly ruling out dangerous diagnoses.

The system needed to handle:

- Complex routing logic where information is redistributed across sections based on priority
- Conditional inclusion rules (e.g., include transport mode only if not self-transport)
- Template modification that saves non-contradicted normal findings while adding new observations
- High-risk diagnosis detection that matches chief complaints to potential emergencies and tracks rule-out criteria

General-purpose LLMs consistently failed at these tasks. They'd hallucinate provider names, place physical exam findings in the history section, or worse, would miss critical diagnoses that hadn't been ruled out. And frontier models failed at emergency documentation.

And it’s true, frontier models actually do fail a lot at emergency documentation. They need to maintain multiple concurrent constraints while preserving information semantics, which in some sense is actually quite out of distribution for them. When `gemini-2.5-pro` sees “regular rate, regular rhythm, no murmurs” and needs to incorporate tachycardia, it faces a constraint satisfaction problem: preserve non-contradicted facts while surgically removing contradicted ones. This requires understanding medical relationships (rate ≠ murmurs) plus precise text manipulation. Most models do one or the other; few do both.

We built comprehensive evaluation frameworks using Lumina for both stages of the pipeline. (Read more about our LLM-as-judge evaluation construction with Lumina [here](https://www.baseten.co/blog/purpose-built-llms-for-dental-note-taking/).) Our client provided 120 micro-checks they used for quality assurance, i.e., specific failure modes they'd identified over months of production use. We semantically partitioned these into our evaluator framework, ensuring complete coverage while organizing them into coherent evaluation dimensions, as well as supplementing them with additional errors and holistic checks for quality.

For each stage – summarization and chart generation – we created five evaluators. Each evaluator uses binary pass/fail scoring on specific criteria. A chart passes only if it satisfies all requirements.

| Summarization (Transcript → JSON) | Chart Generation (JSON + Template -> Chart) | 
|---|---|
| Groundedness: No hallucinated information, all facts traceable to source | Factual grounding: Demographics and findings match exactly | 
| Semantic categorization: Information placed in the correct sections | Template modification: Preserves non-contradicted normals, removes contradicted clauses | 
| Conditional logic: Exclusion/inclusion rules correctly applied | Structural integrity: Sections included/omitted based on content rules | 
| Formatting compliance: Age formats, temporal expressions, structural requirements | Information completeness: All required data present, mandatory defaults applied | 
| Clinical quality: Non-redundant, uses proper terminology, applies high-risk diagnosis logic | Formatting and style: Length limits, prefixes, capitalization, data transformations | 

We also needed to validate the evaluators themselves. We ran a meta-evaluation process where we generated “perfect” outputs according to our evaluators, and had our customer's clinical team review these outputs. When they found issues our evaluators missed, we refined the evaluation prompts. When evaluators flagged clinically acceptable outputs, we traced misalignment back to task specifications. We also provided questions about ambiguities surfaced by Lumina for the customer to answer. This iteration continued until our evaluators aligned with expert clinical judgment.

The original system used multiple prompts across different stages: separate prompts for each summarization section, another for PE template selection, and more for chart generation. This created compounding errors and latency.

We consolidated this into two stages:

- **Stage 1**: One prompt handles all 16 sections of summarization
- **Stage 2**: One prompt handles complete chart generation

For PE template selection, we noticed the LLM was essentially pattern-matching against rules. We replaced this with deterministic Python code, eliminating an unnecessary LLM call while improving accuracy to 100%.

This simplification was only possible because we made the first stage robust enough to produce consistent, well-structured outputs that the second stage could reliably process.

We used iterative SFT to train our model, which in this case is `qwen3-32b`, a dense model (we are also currently training an MoE model for the same task, `qwen3-next-80b-a3b`, which significantly speeds up inference at the cost of memory).

For each training example, we:

1. Generate initial output from base model
2. Run all evaluators to identify failures
3. Use `gemini-2.5-pro` to repair the output based on specific failure feedback
4. Repeat until all evaluators pass
5. Train on these perfect outputs

This process is more sample-efficient than standard SFT because we're training on outputs that score higher than what `gemini-2.5-pro` produces naturally. Each training example provides dense supervisory signal about what went wrong and how to fix it.

We also enhanced our training data through [prompt mutation](https://www.baseten.co/research/robust-sample-efficient-sft-with-prompt-mutations/), which is systematically varying the input format while preserving semantic content. This prevented overfitting to specific phrasings.

For the chart generation stage, we added robustness by training on both perfect JSON outputs and unrefined outputs from the summarization stage. This ensures the model handles imperfect inputs gracefully in production.

We include two examples of how [iterative SFT](https://www.baseten.co/research/iterative-sft/) (iSFT) allows us to bake in specific behaviors to the model (that are difficult to prompt for) below.

The most important component is the high-risk diagnosis detector. For each chief complaint, the model must identify dangerous conditions that haven't been ruled out.

For example, subarachnoid hemorrhage is ruled out only if thunderclap headache is absent AND CT within 6 hours is negative. Another example is that pulmonary embolism requires either low-risk Wells score plus negative PERC, or negative imaging.

We trained the model to apply these rule-out criteria exactly. If a dangerous diagnosis isn't explicitly ruled out, it appears in the output with specific next steps: what history to clarify, what exam findings to check, what tests to order.

Physical exam documentation presented a unique challenge. The system starts with standard templates, such as "Normal Adult," that include default findings. The model must surgically edit these templates based on new findings.

If the template says "regular rate, regular rhythm, no murmurs" and the exam found tachycardia, the model must delete only "regular rate, regular rhythm" while preserving "no murmurs". It then appends "tachycardic" to the remaining text.

Most models either replace everything or keep everything. Through iSFT with targeted feedback on template modification failures, we taught our model to make precise edits. Our model achieves 94% accuracy on template modification compared to `gemini-2.5-pro`'s 58%.

The headline result is that we outperform `gemini-2.5-pro` (the SOTA for this task prior to our training) on both summarization and chart generation by a significant margin. We also do so about 5-7x faster than `gemini-2.5-pro`, and just under 25x faster than `o4-mini`, which surprisingly was the second-best model we tested.

Our model scored 20% better than `gemini-2.5-pro` on the summarization task (which was the best of the closed-source models). Here, the pass rate is defined as the percentage of evaluators who passed (averaged across all types of evaluators and all notes).

We also include the scores from individual evaluators for completeness.

Similarly, we outperform `gemini-2.5-pro` by 33% on chart generation, and outperform `o4-mini` (the next closest model) by 18%.

Importantly, we achieve a score of 100% on structural integrity scoping and significantly outperform other models in information completeness evaluation.

However, performance is not the only axis a customer must optimize along; another key axis is latency. Our model is not only the most accurate, but also among the fastest by a significant margin. We use the [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack/) with its optimized [Speculation Engine](https://www.baseten.co/resources/guide/the-baseten-inference-stack/#baseten-speculation-engine) to minimize how long doctors wait for notes, which is critical in emergency settings.

Another way to view this is “percentage points achieved per second of thinking time” on the overall aggregated evaluations. Baseten's custom model comes out well ahead.

It's also worth noting that the true latency improvement over the previous system was actually much higher. The gains come not just from model speed but also from pipeline simplification (though all models above use the condensed pipeline for comparison). By consolidating multiple LLM calls into single stages and replacing pattern-matching tasks with code, we reduced the total number of inference calls from 5+ to 2. We were able to do this because, when we can change a model’s weights, we don’t have to break the task into individual steps to prompt it effectively; we can just teach it the mapping in one step.

Our model currently processes tens of thousands of emergency department notes weekly across our client’s customer base. This volume is expected to double by year-end as more emergency departments adopt the system.

**Example of what our model gets right:** One particular case we evaluated stood out to us, where a patient arrives by EMS with chest pain. The transcript mentions the patient has diabetes and takes metformin, but the family member states the patient stopped taking it last month. EMS noted hypotension en route. `gemini-2.5-pro` actually failed pretty miserably; it placed “stopped metformin” in current medications instead of past medications, included a family member as a healthcare provider, put EMS vital signs in the physical exam section, and missed that chest pain requires ACS rule-out documentation.

Our model, in contrast, correctly routed discontinued medication to the appropriate section; identified the family as a historian, not a provider; excluded EMS vitals from PE findings while preserving them in HPI, and generated a high-risk diagnosis section noting that ACS was not ruled out.

Three factors drove our success:

1. **Comprehensive evaluation before training**. We spent weeks with our client's clinical team cataloging every possible failure mode. This upfront investment in evaluation quality set the ceiling for model performance.
2. **Dense feedback through iSFT**. Rather than training on whatever gemini-2.5-pro generates, we train on outputs that have been iteratively refined to pass all evaluators. This produces training data of higher quality than any model can generate naturally.
3. **Multi-stage robustness**. We deliberately trained the chart generation model on both perfect and imperfect JSON inputs from the summarization stage. This ensures graceful handling of upstream errors and eliminates the brittleness of the original multi-prompt pipeline.

Emergency medicine documentation requires precise application of clinical rules while maintaining semantic understanding. By building calibrated evaluators and using iterative refinement to hillclimb these evaluators, we've created a model that outperforms general-purpose systems on both accuracy and speed.

This approach generalizes: build evaluators that capture domain expertise, use iterative refinement to create perfect training examples, then train a specialist model. For regulated industries where errors have consequences, this methodology delivers models that don't just approximate the task under fuzzy prompt instructions, but also execute it correctly.
