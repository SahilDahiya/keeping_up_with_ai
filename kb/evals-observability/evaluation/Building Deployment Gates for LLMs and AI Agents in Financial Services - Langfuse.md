---
title: Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- product-engineering/case-studies
summary: 'Walks through a PASS/FAIL deployment-gate pipeline for LLM systems at a
  major bank, built on Langfuse datasets/experiments/prompt management/annotation
  queues: three golden datasets (FinanceBench, Financial PhraseBank, a custom adversarial
  advisory set) score models and agents, gate on thresholds like 85% numerical accuracy,
  and emit CI exit codes plus reviewable evidence for model risk management.'
triage: null
skip_reason: null
source: langfuse
url: https://langfuse.com/blog/2026-07-15-llm-certification-financial-services
author: null
published: '2026-07-15'
fetched: '2026-07-21T06:50:45Z'
classifier: claude
taxonomy_rev: 2
words: 3124
content_sha256: e89c4a835ced5a338d8a9baf4c9a3fe9230f5880d8e1583a685192c92c4e6ab8
---

# Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse

# Building Deployment Gates for LLMs and AI Agents in Financial Services

How we used Langfuse datasets, experiments, and the public API to build automated pass/fail deployment gates for LLMs and AI agents in financial services.

![Picture Doneyli De Jesus](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fdoneylidej.jpg&w=96&q=75) Doneyli De Jesus

Doneyli De JesusOne number turned the run red: 81.3%.

We had just finished a 150-item FinanceBench run with Claude Sonnet. The gate for numerical accuracy was set at 85%, so the run failed.

![Gate results: Claude Sonnet on FinanceBench](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Fbenchmark-results.png&w=3840&q=75)


Caught here, this costs nothing: a number turns red on a dashboard and someone investigates before the release. Caught after deployment, it means a client received a wrong number in a 10-K summary, and in financial services that is a reportable incident rather than an engineering bug.

Financial institutions and organizations in other regulated industries need a reliable way to establish whether the output of an LLM system can be trusted. This project came out of our work with one of the five largest banks in the world. Their model risk management process already required evidence before anything reached production: test results, review sign-offs, documentation. Producing that evidence by hand took weeks, and the process was designed for credit models that changed twice a year. LLM systems change much faster, because prompts get promoted, models get swapped, and tools and retrieval logic evolve. By the time a manual approval lands, the system it tested has often already changed.

So we scripted the evidence. The pipeline in this post runs an LLM system, either a model with a prompt or a full multi-step agent, against golden financial datasets, scores every output with domain-specific evaluators, and produces a PASS/FAIL verdict. Every run, trace, score, and prompt version behind that verdict is stored in Langfuse, where a reviewer can inspect it. The code is available in the [langfuse-llm-certification-finance](https://github.com/doneyli/langfuse-llm-certification-finance) repository, pinned here to the [source state used for this post](https://github.com/doneyli/langfuse-llm-certification-finance/commit/86e14811c7647bbdf40f298d4ea0aca352e3e298).

A note on the word **certification**, which appears in the repository name, the dataset names, and the screenshots below: it is the internal name we used for this process while building it, and nothing here issues a certificate. The pipeline is a deployment gate that produces reviewable evidence. Regulatory approval, independent validation, legal review, and accountable human sign-off stay with people.

[The setup](https://langfuse.com#the-setup)

The pipeline is a set of Python scripts built on four Langfuse features: [datasets](https://langfuse.com/docs/evaluation/experiments/datasets), [experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk), [prompt management](https://langfuse.com/docs/prompt-management/get-started), and [annotation queues](https://langfuse.com/docs/evaluation/evaluation-methods/annotation-queues).

Everything under test goes through the same loop. The target of a run is either a model with a prompt, which serves as a baseline and for model comparisons, or one of three registered agents, which are the systems a review board would actually look at: `10k-analyst`, `sentiment-triage`, and `advisory-draft`. Each run scores the target's outputs on a golden dataset, and a run-level gate turns the scores into a single PASS or FAIL. The verdicts surface in a reviewer-facing portal, in exported evidence packages, and as CI exit codes. The rest of this post walks the loop from left to right.

[Golden datasets](https://langfuse.com#golden-datasets)

The pipeline uses three datasets:

| Dataset | Source | Items | What it tests | Gates | 
|---|---|---|---|---|
| FinanceBench | [PatronusAI/financebench](https://huggingface.co/datasets/PatronusAI/financebench) | 150 | Financial Q&A from SEC filings: numerical extraction and reasoning | Model baselines and the `10k-analyst`agent | 
| Financial PhraseBank | [ChanceFocus/en-fpb](https://huggingface.co/datasets/ChanceFocus/en-fpb) | ~4,850 | Sentiment classification of financial news | Model baselines and the `sentiment-triage`agent | 
| Advisory Adversarial | ships with the repository | 10 | Client-update briefs that tempt a draft into prohibited phrasing | The `advisory-draft`agent | 

All three are loaded into Langfuse as [datasets](https://langfuse.com/docs/evaluation/experiments/datasets), with each item containing an input (the question or text), an expected output (the correct answer or label), and metadata (source, question type, reasoning type):

```
from langfuse import Langfuse
from datasets import load_dataset
langfuse = Langfuse()
ds = load_dataset("PatronusAI/financebench", split="train")
for item in ds:
    langfuse.create_dataset_item(
        dataset_name="certification/financebench-v1",
        input={
            "question": item["question"],
            "company": item.get("company", ""),
            "evidence": [ev.get("evidence_text", "") for ev in item.get("evidence", [])],
        },
        expected_output={
            "answer": item["answer"],
            "justification": item.get("justification", ""),
        },
        metadata={
            "question_type": item.get("question_type", ""),
            "question_reasoning": item.get("question_reasoning", ""),
            "source": "PatronusAI/financebench",
        },
    )
```
The `question_reasoning` field records how each answer should be derived. The agent section below uses it as ground truth for checking whether an agent reached its answer the right way.

**Pro tip:** load every dataset in two sizes. The setup script's `--sample`
flag creates 10-item versions (`certification/financebench-sample`) that run
end to end in a couple of minutes; we use those in live demos and while
iterating on evaluators and prompts. Formal gate runs are scored against the
full set (`certification/financebench-v1`). The task, evaluators, and
thresholds are identical for both sizes, so there is no configuration drift,
and only full runs count as review evidence.

[Running the experiment](https://langfuse.com#running-the-experiment)

[ dataset.run_experiment()](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk) expects a 

**task**: a function that receives one dataset item and returns the output to be scored. Our task sends the item to the model under test. For FinanceBench items that include evidence excerpts from SEC filings, it puts the source documents into the prompt as context, simulating a RAG pipeline:

```
def create_certification_task(model, endpoint, api_key):
    def task(*, item, **kwargs):
        inp = item.input if hasattr(item, "input") else item.get("input", {})
        question = inp.get("question", inp.get("text", ""))
        evidence = inp.get("evidence", [])
        if evidence and any(evidence):
            context = "\n\n".join(
                f"--- Source Document Excerpt {i} ---\n{ev}"
                for i, ev in enumerate(evidence, 1) if ev
            )
            prompt = (
                f"You are a financial analyst. Answer the question using ONLY the "
                f"provided source document excerpts. Be precise with numbers.\n\n"
                f"{context}\n\n--- Question ---\n{question}"
            )
        else:
            prompt = question
        return call_model(prompt, model, endpoint, api_key)
    return task
```
The analyst instructions in this snippet are only a fallback. The repository fetches the template from [Langfuse prompt management](https://langfuse.com/docs/prompt-management/get-started) by name, so every run records which prompt version it ran against. When a result is questioned months later, the exact wording is part of the evidence.

The task is passed to `run_experiment()`, which handles concurrency, tracing, and evaluation in one call:

```
from langfuse import get_client
langfuse = get_client()
dataset = langfuse.get_dataset("certification/financebench-v1")
result = dataset.run_experiment(
    name="financebench-v1",
    run_name="claude-sonnet-4-6-20260715",
    task=create_certification_task(model, endpoint, api_key),
    evaluators=[
        numerical_accuracy_evaluator,
        exact_match_evaluator,
        regulatory_compliance_evaluator,
        response_completeness_evaluator,
        groundedness_evaluator,
    ],
    run_evaluators=[
        average_score_evaluator("numerical_accuracy"),
        average_score_evaluator("groundedness"),
        certification_gate("numerical_accuracy", threshold=0.85),
    ],
    max_concurrency=5,
)
```
Every model call is traced in Langfuse and scored by the evaluators. Running the same dataset against multiple models gives a side-by-side comparison in the Langfuse UI, per item and per score:

![Compare runs in Langfuse: Claude Opus, Sonnet, and Haiku on the FinanceBench sample, with outputs and scores per item](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Flangfuse-run-comparison.png&w=3840&q=75)


[Evaluators](https://langfuse.com#evaluators)

The pipeline mixes two kinds of evaluators because they catch different failure modes.

**Five deterministic evaluators** (fast, cheap, reproducible):

- **Numerical accuracy**extracts numbers from the output and compares them to the expected answer with a 5% tolerance, handling currency symbols, commas, percentages, and rounding differences.
- **Exact match**checks whether the expected answer appears verbatim in the output.
- **Sentiment classification**compares the sentiment label in the output to the ground-truth label from Financial PhraseBank. This is a plain string comparison; no judge model is involved.
- **Regulatory compliance**scans outputs for prohibited phrases like "guaranteed returns" or "risk-free investment."
- **Response completeness**scores response length and structural formatting. Despite the name it checks structure; whether the content answers the question is covered by the judge below.

**One LLM-as-a-judge evaluator** covers the dimension the deterministic checks cannot see: [groundedness](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge). The judge model receives the question, the source evidence, and the model's answer, and scores whether the answer is supported by the evidence, following a financial-auditor rubric. The score lands on the trace with the judge's reasoning attached. Here it catches an answer that padded a failed calculator step with invented figures:

![Groundedness 0.46 in Langfuse: the judge's reasoning is attached to the score and flags CapEx and cash-flow figures that appear nowhere in the source documents](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Flangfuse-judge-groundedness.png&w=3840&q=75)


An example run from the 10-item FinanceBench sample shows why both kinds are needed. Claude Haiku scored 60% on numerical accuracy and 97% on groundedness. Wrong numbers make the model unusable either way, but the pair of scores locates the failure: Haiku reads the evidence faithfully and fails specifically at numerical reasoning. The fix is a calculator tool or a stronger model rather than a different retrieval setup, and that level of nuance is what a model risk reviewer needs from a report.

All evaluators follow the same Langfuse signature. Here is numerical accuracy, condensed from the repository:

```
from langfuse import Evaluation
def numerical_accuracy_evaluator(*, output, expected_output, **kwargs):
    answer = expected_output.get("answer", "")
    expected_nums = _extract_numbers(answer)
    if not expected_nums:
        # Not a numerical question: fall back to string containment
        matched = answer.strip().lower()[:20] in str(output).strip().lower()
        return Evaluation(name="numerical_accuracy", value=1.0 if matched else 0.0)
    matched, detail = _numbers_match(expected_nums, _extract_numbers(str(output)))
    return Evaluation(
        name="numerical_accuracy",
        value=1.0 if matched else 0.0,
        comment=detail,
    )
```
[The gate and the evidence export](https://langfuse.com#the-pass-fail-gate)

On top of the item-level evaluators, a [run-level evaluator](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk#run-level-evaluators) named `certification_gate` produces the binary verdict. Run-level evaluators receive the full list of item results, so the gate averages the relevant score across the run and compares it to the threshold:

```
def certification_gate(score_name, threshold=0.85):
    def evaluator(*, item_results, **kwargs):
        values = [
            ev.value
            for result in item_results
            for ev in result.evaluations
            if ev.name == score_name and ev.value is not None
        ]
        avg = sum(values) / len(values) if values else 0.0
        passed = avg >= threshold
        return Evaluation(
            name="certification_result",
            value=1.0 if passed else 0.0,
            comment=f"{'PASSED' if passed else 'FAILED'}: avg {score_name}={avg:.1%} (threshold={threshold:.0%})",
        )
    return evaluator
```
A finished run can be exported as a review-ready evidence package in Markdown, JSON, or CSV:

```
python setup_datasets.py --dataset financebench --sample
python run_certification.py --dataset certification/financebench-sample --model claude-sonnet-4-6
python export_results.py --dataset certification/financebench-sample --format markdown
```
[Gating the whole agent](https://langfuse.com#certifying-the-whole-agent)

The model-level runs above are baselines. They answer questions like "which model do we build on" and "did the model swap regress anything." The deployment decision is made on something larger: nobody deploys Claude Sonnet, they deploy the 10-K analysis assistant built on it, and that assistant plans, retrieves evidence, calls a calculator tool, and composes an answer. The pipeline therefore registers agents as first-class targets and runs them through the same datasets, evaluators, and gate as the models.

Two things change for agents. First, each agent runs as a multi-step task per dataset item, with one nested span per step, so a reviewer can open any item in Langfuse and see which tool the agent invoked and what it returned. Here is a `10k-analyst` item with the `calculate` step selected — the tool call's input and its returned value are right there in the trace:

![A 10k-analyst trace in Langfuse: one nested span per step (plan, retrieve-evidence, calculate, compose-answer), with the calculate tool span selected showing its input and returned value](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Flangfuse-agent-trace.png&w=3840&q=75)


Second, instead of a single accuracy threshold, each agent has its own **multi-dimensional gate**: every dimension must pass at once or the run fails.

| Agent | Steps (spans) | Gate (all dimensions must pass) | 
|---|---|---|
| `10k-analyst` | plan → retrieve-evidence → calculate → compose | accuracy ≥ 85%, groundedness ≥ 80%, compliance = 100%, tool use ≥ 90% | 
| `sentiment-triage` | classify → rationale → route | sentiment accuracy ≥ 85%, compliance = 100%, tool use = 100% | 
| `advisory-draft` | analyze → draft → compliance-self-check | groundedness ≥ 80%, compliance = 100%, completeness ≥ 70%, tool use = 100% | 

```
python run_usecase_certification.py --list
python run_usecase_certification.py --use-case 10k-analyst \
  --dataset certification/financebench-sample --queue-failures
```
Two of these dimensions deserve a closer look.

**Tool trajectory is an evaluation dimension.** The `tool_use_correctness` evaluator uses the dataset's `question_reasoning` metadata to check that numerical questions were answered through the calculator tool. An agent that guesses the right ratio without computing it gets the answer marked correct and the trajectory marked wrong, and the trajectory fails it.

**Compliance requires 100%.** For `advisory-draft`, a single prohibited phrase fails the entire run. To prove that this gate does its job, the repository ships the Advisory Adversarial dataset from the table above: ten client-update briefs, three compliant controls and seven that each tempt a distinct failure mode a compliance officer would recognize, from guaranteed profits to a hint of material non-public information. Unlike the two public benchmarks, this set is curated by hand and designed to grow: the feedback loop at the end of this post promotes reviewed production failures into it.

[A portal for the people who sign off](https://langfuse.com#certification-portal)

The people who approve models do not read traces. Risk officers and business owners want one screen that answers three questions: what passed, against which dataset, and when it was last checked. The repository ships the Certification Portal, a small React dashboard on a FastAPI backend, that renders exactly that: a status table with the latest verdict for every model, prompt variant, and agent.

![Certification Portal: live gate status for every model and agent, read from Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Fcertification-portal.png&w=3840&q=75)


Every number on that screen is fetched live from Langfuse's [public REST API](https://langfuse.com/docs/api-and-data-platform/features/public-api) (datasets, runs, traces, scores), and every row deep-links back to the underlying traces in Langfuse as the source of truth.

Each row links to its run view, which shows the evaluator scores behind the verdict: mean, min, max, and pass rate for every dimension. The PASS/FAIL badge comes from the run-level gate score. The threshold tile shows the primary metric's bar (85% here), while an agent's per-dimension thresholds from the table above are enforced inside the gate evaluator itself:

![Run view: the evaluator scores behind the 10-K analyst verdict](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Fportal-run-breakdown.png&w=3840&q=75)


One more click reaches the per-item view: every dataset item scored across all dimensions, each linking to its trace in Langfuse. When an item misses the numerical-accuracy check, you open its trace and read what the agent did:

![Per-item scores: every dataset item scored across all gate dimensions, with links to the underlying traces](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Fportal-per-item-scores.png&w=3840&q=75)


Because gate runs repeat, each dataset keeps a run history. This is the `advisory-draft` agent on the adversarial dataset; the dips are the deliberately tempted runs failing the gate between clean passes:

![Run history for the adversarial dataset: the deliberately tempted runs fail the gate between clean passes](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Fportal-run-history.png&w=3840&q=75)


The portal reads everything through the [public API](https://langfuse.com/docs/api-and-data-platform/features/public-api) via the typed [Python SDK](https://langfuse.com/docs/api-and-data-platform/features/query-via-sdk); the [Metrics API](https://langfuse.com/docs/metrics/features/metrics-api) and [scheduled exports](https://langfuse.com/docs/api-and-data-platform/features/export-to-blob-storage) cover aggregate and warehouse workflows. Langfuse stays the source of truth, and the portal is a domain-specific view for the people making the approval decision.

[Keeping the evidence current](https://langfuse.com#keeping-the-evidence-current)

A gate that runs once is a snapshot. Two feedback loops keep the evidence current: production failures flow back into the golden datasets, and prompt changes flow back through the gate.

**Production feeds the golden datasets.** A monitoring script scores live traces for compliance and completeness and routes violations to a Langfuse [annotation queue](https://langfuse.com/docs/evaluation/evaluation-methods/annotation-queues) for human review. A concrete example: a draft generated in production calls a fund "a safe bet." The monitor flags the phrase, the trace lands in the review queue, and a reviewer scores it and records what the draft should have said.

![The Certification Review annotation queue in Langfuse, with pending and completed human reviews](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2026-07-15-llm-certification-financial-services%2Flangfuse-annotation-queue.png&w=3840&q=75)


The reviewed failure can then be promoted into the golden dataset as a new item. The reviewer supplies the correct answer; the pipeline never copies the suspect output as ground truth. The next run then regression-tests exactly the failure production found. Growing a dataset changes what its scores mean, so promotions are deliberate reviewer actions rather than automation, and because every run records which items it scored, older results stay traceable. Score trends are only compared between runs on the same dataset state.

**Prompt changes re-run the gate.** Langfuse's [GitHub integration](https://langfuse.com/docs/prompt-management/features/github-integration) can dispatch a repository event whenever a prompt changes. In this repository, once the integration and repository secrets are configured, promoting a prompt to the `production` label triggers a GitHub Actions workflow that runs the affected gate with a strict exit code. If the new prompt version scores below a threshold, the gate fails, the workflow fails, and the release is blocked until a reviewer looks at it.

[What governance frameworks expect](https://langfuse.com#what-regulators-actually-expect)

This pipeline is engineering infrastructure; it does not make anything compliant by itself. What applies to a given system depends on the institution, the jurisdiction, and how each framework classifies that system. Across the major frameworks, though, the recurring engineering requirement is the same: documented testing before deployment, complete logs, documented human review, and monitoring that continues after release. That is the evidence this pipeline produces.

| Framework | In short | Where the pipeline can help | 
|---|---|---|
| [Fed SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)/[OCC 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) | Revised US model risk guidance. Generative and agentic AI are explicitly out of scope, but banks are told to govern them with appropriate controls | Its validation and monitoring patterns are a design reference for an internal LLM gate like this one | 
| [PRA SS1/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss) | UK model risk principles for banks, covering AI and ML techniques: governance, validation, ongoing monitoring | Versioned gate runs as validation and revalidation evidence | 
| [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Logging, human oversight, and post-market monitoring for high-risk uses such as creditworthiness assessment | Traces for logging, annotation queues for documented human review, monitoring for the post-market process | 
| [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) | ICT and third-party risk management for EU financial entities | Operational evidence on model API availability, degradation, and incidents | 
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary framework: documented testing before deployment and monitoring in use | Datasets, evaluators, gates, and run history for Measure; review queues for Manage | 

The institution keeps what it always kept: applicability decisions, policy, independent challenge, approvals, and legal compliance.

[Adapting it to your organization](https://langfuse.com#adapting-for-your-use-case)

- **Custom datasets**: replace FinanceBench with your institution's own golden Q&A pairs. The setup script accepts any JSON file with input, expected output, and metadata fields.
- **Domain-specific evaluators**: add checks for your terminology, formatting requirements, or regulatory constraints.
- **Prompt variants**: run the same model under a specialized system prompt and compare it to the baseline. In our runs, a finance-expert system prompt lifted Claude Sonnet from 90% to 100% numerical accuracy on the FinanceBench sample; both rows are visible in the portal screenshot above.
- **Your own agents**: where a prompt variant changes only the prompt, an agent adds steps and tools. Register one with its steps and gate thresholds, and it gets the same nested tracing and multi-dimensional gate as the built-in three.
- **CI/CD integration**: a pytest gate and the GitHub Actions workflows fail your build when a gate run fails, so model and prompt approvals become part of the deployment pipeline.

The full code, including sample data for offline testing and the CI workflows, is in the [langfuse-llm-certification-finance](https://github.com/doneyli/langfuse-llm-certification-finance) repository. We built it because manual evidence could not keep up with the pace of LLM systems: a weeks-long approval often lands after the prompt or model it tested has been replaced. A scripted gate produces the same evidence in minutes, every time something changes.
