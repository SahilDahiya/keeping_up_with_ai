---
title: How to measure human-LLM judge alignment
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/measuring-human-llm-judge-alignment/
author: Elizabeth Hutton
published: '2026-07-22'
fetched: '2026-07-23T06:50:14Z'
classifier: null
taxonomy_rev: 2
words: 3123
content_sha256: fe901141db67211f020ef03893d6efa1d0fa9aea71fb152e389c2598ecd7676c
---

# How to measure human-LLM judge alignment

LLM judges make it possible to evaluate large datasets quickly, but before relying on one, you need to know how closely its judgments match those of human experts.

No single number can tell you whether an LLM judge is trustworthy. Before you can trust the judge, you need to know whether the task itself is well-defined, whether the judge applies the rubric within the observed range of human judgments, and where exactly it goes wrong. Each of those is a separate question, and each calls for a different kind of measurement.

A complete measure of evaluation alignment can be broken down into three questions:

- How reliably do humans apply the evaluation criteria?
- Does the LLM agree with humans about as often as humans agree with one another?
- When the LLM disagrees with the reference judgment, what kinds of errors does it make?

This guide will help you answer each of these important questions and choose the right approach for your setup.

**TL;DR**

- Collect multiple human annotations on a representative subset. Use disagreements to identify problems with the criteria and create a more defensible reference.
- Report raw human–human agreement alongside a chance-adjusted metric such as Cohen’s kappa, Fleiss’ kappa, or Krippendorff’s alpha (depending on your annotation setup).
- Compare human–human and LLM–human agreement on the same examples using the same metric. Treat human agreement as context for the comparison, not as a hard performance ceiling.
- Create the reference through adjudication or a true majority vote. Preserve ties and low-consensus cases rather than assigning an arbitrary label.
- Against that reference, treat the LLM judge as a classifier. Report precision, recall, F1, class counts, and the confusion matrix.
- Ensure that each important class—not only the dataset overall—has enough examples, and report uncertainty around the main results.

**Step 1: Define the task before choosing a metric**

Start by writing down four things:

```
unit: span | trace | session
labels:
  type: nominal | ordinal | multilabel
  values: [pass, fail]  # or ordered list
positive_class: fail    # for precision/recall
reference_policy: majority | adjudicate | soft_label
cost_asymmetry: fp_worse | fn_worse | equal
```
**Unit:** What receives one judgment: an individual LLM call (span), a sequence of steps inside a turn (trace), or the whole conversation (session)?

**Label structure and measurement level:** Is the task single-label or multilabel? If it is multi-label, are the categories nominal or ordinal? Three nominal labels such as hallucination, irrelevant, and incomplete have no inherent order. Three ordinal labels such as fail, partial, and pass do.

**Positive class:** For precision and recall, which label represents the event you are trying to detect?

**Reference policy:** How will multiple human judgments become an operational reference—for example, majority vote or expert adjudication?

**Error cost:** Which is more consequential: a false positive or a false negative?

These decisions determine which metrics are meaningful.

**Step 2: Measure human-human agreement**

Before evaluating the LLM judge, look at the examples with multiple human annotations.

Agreement metrics tell you whether people can apply the rubric consistently. No person is designated as correct; their judgments are treated symmetrically.

A practical starting point is:

| Annotation setup | Good starting point | 
|---|---|
| Two annotators, categorical labels | Cohen’s kappa | 
| Two annotators, ordered labels | Weighted Cohen’s kappa | 
| Three or more annotators, same number per item | Fleiss’ kappa | 
| Missing annotations or varying annotator counts | Krippendorff’s alpha | 
| Ordered labels with missing or varying annotations | Ordinal Krippendorff’s alpha | 
| Any setup | Raw percent agreement as a descriptive companion is still useful. | 

Cohen’s kappa supports both binary and multiclass tasks; it is not limited to pass/fail.[ See Scikit-learn’s documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) for examples of how to configure this metric.

Krippendorff’s alpha is the flexible choice when annotation coverage is uneven. It supports multiple measurement levels, varying numbers of annotators, and missing judgments.[ The R Journal overview](https://journal.r-project.org/articles/RJ-2021-046/) provides a detailed explanation.

**Why collect multiple human annotations?**

Multiple annotations serve three purposes.

First, they give you more evidence for constructing a reference label. One annotation may reflect a mistake, an unusual interpretation, or an individual bias. Multiple judgments make it possible to identify consensus, adjudicate disagreements, or preserve the distribution of opinions.

They do not automatically create ground truth. They create a more defensible basis for an operational reference. Earlier Arize coverage of judge alignment, including [Judging the Judges](https://arize.com/blog/judging-the-judges-llm-as-a-judge/), covers related failure modes; [building on a context graph of human disagreement](https://arize.com/blog/self-improving-agent-with-context-graph) shows how to put those disagreements to work.

Second, disagreement helps you improve the evaluation criteria. Low agreement may indicate that:

- The rubric is ambiguous.
- Annotators need better examples.
- Relevant context is missing.
- A single label combines several concepts.
- The task contains legitimate subjectivity.

The agreement score identifies that a problem exists. The disagreements themselves help you understand what to change.

Third, human agreement provides context for interpreting the judge. When qualified people regularly interpret the same examples differently, perfect human-LLM agreement may be neither realistic nor desirable.

**Use annotation as part of eval development**

A practical development loop looks like this:

- Have multiple humans label a representative calibration set.
- Calculate agreement and inspect the disagreements.
- Revise the criteria, examples, or annotation process.
- Run another calibration round.
- Once the criteria are stable, lock the final test set.

This is why I treat annotation as part of *developing* the eval, not just grading it. Teams that already collect human feedback at scale can also borrow patterns from [how OpenAI turns user feedback into product improvements](https://arize.com/blog/how-openai-turns-user-feedback-into-product-improvements/).

**Should you report raw percent agreement?**

Yes—raw percent agreement is easy to understand, but it doesn’t account for random chance, individual annotator distributions, or class imbalance, so report it alongside a chance-adjusted metric.

Suppose you have 100 examples and 95 are pass. One annotator identifies the five failures; another labels everything pass. They still agree on 95% of the dataset, even though the second annotator never detects a failure.

Chance-adjusted metrics such as kappa consider the annotators’ label distributions. But kappa has quirks too: severe class imbalance can produce surprisingly low kappa despite high raw agreement, a well-documented phenomenon sometimes called the kappa prevalence paradox.[ Feinstein and Cicchetti](https://pubmed.ncbi.nlm.nih.gov/2348207/) describe this behavior.

The practical solution is to report several pieces of evidence together:

- Raw agreement
- Kappa or alpha
- Label counts or percentages
- The confusion matrix or major disagreement patterns

Avoid relying on universal thresholds such as “0.6 is good” or “0.8 is acceptable.” Whether an agreement level is sufficient depends on the ambiguity of the task, the risk of an incorrect decision, and how the judge will be used.

**Step 3: Use human agreement as a baseline for the LLM**

If humans don’t agree perfectly, we shouldn’t expect perfect human-LLM agreement either.

To make a clean comparison, calculate pairwise agreement between the LLM and each individual human annotator.

Suppose humans A, B, and C and an LLM label the same examples.

First calculate human-human agreement:

- A ↔ B
- A ↔ C
- B ↔ C

Then calculate LLM-human agreement:

- LLM ↔ A
- LLM ↔ B
- LLM ↔ C

Report the individual pairwise results along with their mean or range.

For example:

Pairwise human-human agreement ranged from 69% to 75%, with a mean of 72%. LLM-human agreement ranged from 68% to 71%, with a mean of 70%.

That tells you the LLM is operating close to the observed range of human reproducibility.

Be careful **not** to add the LLM to the annotation pool and report one combined human+LLM alpha or Fleiss’ kappa. That answers the less useful question, “How reliable is this mixed panel?” It doesn’t directly compare the LLM with the human baseline.

Also note that human agreement is a baseline, not a hard performance ceiling. A model can agree with a stable consensus reference more often than individual annotators agree with one another, particularly when individual annotations contain noise.[Simulation research has shown](https://aclanthology.org/2022.bionlp-1.26/) that inter-annotator agreement is not necessarily an upper bound on model performance.

**Measure the judge’s self-consistency**

If the judge is nondeterministic, run it more than once on the same examples.

A judge that agrees with humans on average but changes its own answer across runs may be difficult to use reliably in monitoring, experimentation, or release gates.

Report both:

- Agreement between the judge and the human reference
- Agreement between repeated runs of the judge

Also record the model version, evaluator prompt, inference settings, and evaluation date. A score is difficult to reproduce when the underlying judge configuration is not versioned. Prompt design also affects judge reliability—see [evidence-based prompting strategies for LLM-as-a-Judge](https://arize.com/blog/evidence-based-prompting-strategies-for-llm-as-a-judge-explanations-and-chain-of-thought/).

**Step 4: Turn the human judgments into a reference**

The next step is to create one reference outcome per example.

This changes the evaluation relationship. Human-human agreement is symmetric, but once you define an operational reference, the comparison becomes asymmetric:

- Human aggregate or adjudicated label = reference
- LLM judgment = prediction

Possible reference policies include:

- Expert adjudication
- Majority vote
- A predefined tie-breaking process
- A consensus meeting
- Preserving a distribution rather than forcing a hard label

**Binary tasks**

With three complete pass/fail annotations, majority vote always produces a result.

With two annotators, every disagreement is a tie. Use a third annotator or adjudication rather than silently choosing one person’s label.

**Multiclass tasks**

With three labels and three annotators, each annotator can choose a different class. That is not a meaningful majority.

Consider adjudicating these cases or marking them as ambiguous. If you force a hard label, preserve the vote counts so you can distinguish:

- 3-0: strong consensus
- 2-1: weak consensus
- 1-1-1: no consensus

You may also want to report LLM performance separately on high- and low-consensus examples. That can reveal whether the judge is failing on clear cases or merely participating in legitimate ambiguity.

**Step 5: Treat the LLM judge like a classifier**

Once you have a reference label, the relationship becomes asymmetric:

- Human aggregate = reference label
- LLM judgment = prediction

Now report classification metrics. For a hands-on comparison of label formats in practice, see [testing binary vs. score evals](https://arize.com/blog/testing-binary-vs-score-llm-evals-on-the-latest-models/).

**For binary tasks**

Choose the important positive class—often fail—and report:

- Precision
- Recall
- F1
- Confusion matrix
- Support, meaning the number of examples in each class

**For multiclass tasks**

Report:

- Precision, recall, and F1 for every class
- Macro F1
- Weighted F1, if useful
- The full confusion matrix

Macro F1 gives every class equal weight, which helps surface poor performance on rare but important labels. Weighted F1 gives common labels more influence and can therefore hide failures on rare classes. In ordinary single-label multiclass classification, micro F1 is equivalent to accuracy, so it often adds little.[ Scikit-learn explains the averaging options here](https://scikit-learn.org/stable/modules/model_evaluation.html#multiclass-and-multilabel-classification).

Interpretation:

- **Low precision:**too many false positives; the judge may be overly sensitive.
- **Low recall:**too many false negatives; the judge is missing real failures.
- **F1:**summarizes the precision-recall tradeoff.

For ordinal labels, also consider weighted kappa or a measure of error distance. Confusing pass with partial may be less serious than confusing pass with fail.

You can still report LLM-reference percent agreement and kappa. They provide continuity with the human baseline. Precision, recall, and F1 provide the error diagnosis.

**Interpreting classification metrics**

These metrics reveal different failure modes in your judge.

Precision asks: Of the examples the judge labeled as failures, how many were failures according to the reference? Low precision means the judge is producing too many false positives. It may be overly sensitive or applying the rubric too broadly.

Recall asks: Of the reference failures, how many did the judge detect? Low recall means the judge is missing real failures.

F1 combines precision and recall into one score, giving them equal weight by default. It is often more informative than accuracy when failures are rare. It is useful for comparing overall performance, but it should not replace the confusion matrix or an explicit discussion of error costs.

If false negatives are more costly, prioritize recall or use an F-score that gives recall more weight, such as F2. If false positives are more costly, prioritize precision or use an F-score that gives precision more weight, such as F0.5.

The metric should reflect the operational decision the judge will support.

**How many examples do you need?**

There is no universal minimum. The required sample size depends on:

- Expected performance
- Class balance
- Number of labels
- Number of annotators
- Desired precision
- Whether you are estimating a metric or testing a claim

For a simple proportion such as raw agreement, a useful worst-case approximation at 95% confidence is:

- About 100 independent examples for a margin of error near ±10 percentage points
- About 400 for a margin near ±5 percentage points

These figures come from the standard sample-size calculation for a proportion.[ NIST provides the underlying formula](https://itl.nist.gov/div898/handbook/ppc/section3/ppc333.htm).

Treat those as intuition, not a guarantee. Kappa and F1 have more complicated uncertainty, and rare classes are usually the real constraint.

**Count examples per class, not only total examples**

Suppose failures make up 5% of your data. A test set of 200 examples contains only about ten failures on average. Your recall estimate will be extremely unstable, no matter how impressive the total sample size sounds.

Precision depends on the number of predicted positives. Recall depends on the number of actual positives. Make sure both denominators contain enough examples to support the conclusions you want to draw.

A reasonable workflow heuristic is:

- Use 30-50 representative examples with multiple annotations for early rubric iteration.
- Treat results from roughly 100 examples as directional.
- For a stable benchmark, plan around the desired confidence-interval width and the expected count of each important class.

If you enrich the dataset with failures to get better class coverage, say so. Precision measured on an artificially balanced set may not represent production precision because production prevalence is different. You can maintain a natural-distribution test set and a separate failure-focused challenge set.

**Report uncertainty**

A score of 0.78 from 40 examples does not mean the same thing as 0.78 from 4,000.

Report 95% confidence intervals around your main metrics. For kappa, alpha, and F1, bootstrapping over examples is a practical option. If multiple spans come from the same trace or conversation, resample entire traces—not individual spans—so correlated examples stay together.

When comparing two judges on the same examples, use a paired bootstrap: resample examples once and recalculate both judges’ scores and their difference.

**Ready-to-use recipes**

**Depending on the annotation setup:**

| Annotation setup | Recommended approach | 
|---|---|
| One human label per example | Measure LLM–reference precision, recall, and F1, but note that reference-label reliability is unknown. If possible, double-annotate a representative subset. | 
| Two human annotators | Report raw agreement and Cohen’s kappa. Adjudicate disagreements, compare the LLM with each annotator separately, and calculate classifier metrics against the adjudicated reference. | 
| Three or more complete annotations | Report raw agreement and Fleiss’ kappa or Krippendorff’s alpha. Calculate pairwise human–human and LLM–human agreement for a matched comparison. Use majority vote only when a true majority exists; adjudicate ties and no-consensus cases. | 
| Annotation counts vary by example | Use Krippendorff’s alpha for overall human reliability. For the matched LLM baseline, calculate pairwise agreement wherever a human and the LLM labeled the same example. Check whether missing annotations are concentrated among difficult examples. | 

**Depending on the label structure:**

| Label structure | Additional analysis | 
|---|---|
| Multiclass | Report per-class metrics, macro F1, class counts, and the confusion matrix. Inspect which classes are commonly confused. | 
| Ordinal | Use weighted Cohen’s kappa for two raters or ordinal Krippendorff’s alpha for multiple raters. Use an analysis that preserves the severity of disagreements. | 

**What to include in your final report**

At minimum, document:

- The unit being judged
- Label definitions and whether they are nominal or ordinal
- Number of examples and label distribution
- Number of annotators per example
- Human-human raw agreement and kappa or alpha, with uncertainty
- Pairwise LLM-human agreement on the same subset
- How human labels were aggregated or adjudicated
- LLM-reference precision, recall, F1, and confusion matrix
- Performance by class and human-consensus level
- Important disagreement patterns and rubric changes

If the LLM judge is nondeterministic, also repeat the evaluation to measure whether it agrees with itself across runs.

**Putting the workflow into practice in Arize AX**

A practical human-LLM judge validation workflow has four parts:

- Collect representative examples.
- Calibrate the human annotation process.
- Run the judge on a held-out dataset.
- Analyze the disagreements and version the resulting evaluator.

[Arize AX](https://arize.com/ax/) supports [human annotations](https://arize.com/docs/ax/evaluate/human-review) on application data and experiment results, and [LLM-as-a-Judge evaluators](https://arize.com/docs/ax/evaluate/evaluators/llm-as-a-judge) for automated scoring. Labeling queues can distribute a defined dataset and annotation criteria to subject-matter experts, making it easier to collect structured human feedback and identify examples where automated evaluations and humans disagree.

Start with a representative calibration set. Ask multiple annotators to apply the draft rubric, calculate agreement, and inspect recurring disagreements. Revise the criteria and examples until the rubric is sufficiently reproducible.

Then freeze the rubric and annotate the full dataset and adjudicate disagreements. Run the LLM judge against that dataset and compare its labels with the individual human judgments and the aggregated reference.

In Arize AX, an evaluator can return structured labels, scores, and explanations at the span, trace, session, or experiment level. Evaluators are versioned, allowing teams to track changes to the rubric, prompt, judge model, and configuration over time.

Use that versioning to preserve a clean record of:

- Which evaluator produced each result
- Which prompt and model configuration it used
- Which dataset version it ran against
- What changed between evaluator versions
- Whether the change improved performance on the held-out benchmark

The aggregate score is only the beginning. Review the disagreements, filter by class and consensus level, and determine whether the judge is failing because of an unclear rubric, missing context, an overly broad prompt, or a genuine model limitation.

**The takeaway**

Agreement metrics and classification metrics are complementary:

- **Human-human agreement**tells you whether the evaluation criteria are reproducible.
- **LLM-human agreement**tells you whether the judge operates within the range of human variation.
- **LLM-reference classification metrics**tell you what the judge gets wrong.

Or, more simply:

Use human disagreement to harden the eval. Use agreement metrics to contextualize the judge. Use classification metrics to diagnose it.

None of these metrics, by itself, proves that the rubric measures the right thing. That still requires representative data, domain expertise, careful review of disagreements, and a clear understanding of how the judge’s outputs will be used.
