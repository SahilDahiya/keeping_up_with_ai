---
title: Airbnb's three-layer eval workflow with Pydantic AI and Logfire
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/three-layer-evals-logfire
author: Bill Easton
published: '2026-08-06'
fetched: '2026-08-07T06:29:22Z'
classifier: null
taxonomy_rev: 2
words: 2830
content_sha256: 3254366e143323cadbc556b72fda8de34f4b59f65b820921364894308aafb26e
---

# Airbnb's three-layer eval workflow with Pydantic AI and Logfire

Airbnb recently published [its playbook for evaluating generative AI at scale](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788). Start by reading roughly 100 outputs and traces, then build evaluators for the failures you actually find. Its framework has three layers:

1. Programmatic checks for failures code can identify exactly.
2. LLM judges for qualities that require interpretation.
3. Human review for ground truth, disputed cases, and judge calibration.

The layers are a division of labor. Code answers objective questions, judges handle interpretation, and humans define and calibrate what good means. Confirmed production failures become new test cases.

Yesterday, we showed how to send existing Braintrust evals to [Logfire](https://pydantic.dev/logfire) without rewriting them. Today, we will build Airbnb's workflow end to end with Pydantic AI and Logfire: evaluate a support agent, inspect failures in the Evals workspace, calibrate the judge with human review, and use Logfire's optimizer to propose the next prompt improvement.

## 

- **Programmatic checks:** Did the system obey an objective contract? Use Pydantic output validation, custom evaluators, and agentic trajectory checks on every offline case, and in production when the check is cheap enough.
- **LLM judges:** Is the answer faithful to the evidence? Use`LLMJudge` with one narrow rubric and a recorded reason on every offline case, then sample production traffic.
- **Human review:** Does the rubric match expert judgment? Use run annotations, annotation queues, and hosted datasets to calibrate a gold set, resolve disagreements, and review a production sample.

Airbnb recommends running roughly 100 examples and reading the outputs and traces before writing evaluators. A generic "helpfulness" score written before anyone has seen the failures mostly measures the author's imagination.

Start the same way:

1. Instrument the prototype and run 50 to 100 representative inputs.
2. Read the complete traces, including retrieval and tool calls.
3. Classify the recurring failure modes.
4. Write one evaluator for each failure worth preventing.

Keep the set small. Airbnb's rule of thumb is three to five well-calibrated judges rather than 20 noisy ones.

## 

Install the agent, evaluation, and observability packages:

```
pip install logfire pydantic-evals "pydantic-ai-slim[openai]"
```
Set `OPENAI_API_KEY`, then create `support_agent.py`:

```
from dataclasses import dataclass, field
from typing import Literal
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
logfire.configure()
logfire.instrument_pydantic_ai()
POLICIES = {
    'returns': 'Unused items can be returned within 30 days. Refunds take 5 to 7 business days.',
    'cancellations': 'An order can be cancelled before it ships. Shipped orders must use the return process.',
}
class SupportAnswer(BaseModel):
    text: str
    cited_policy_ids: list[str]
    action: Literal['answer', 'escalate']
class SupportResult(BaseModel):
    answer: SupportAnswer
    evidence: dict[str, str]
@dataclass
class SupportDeps:
    evidence: dict[str, str] = field(default_factory=dict)
support_agent = Agent(
    'openai:gpt-5-mini',
    deps_type=SupportDeps,
    output_type=SupportAnswer,
    system_prompt=(
        'Before answering, call `lookup_policy` with the customer question. '
        'Answer only from the policies it returns and cite every policy used by ID. '
        'Escalate when the returned policies do not answer the question.'
    ),
)
@support_agent.tool
def lookup_policy(ctx: RunContext[SupportDeps], question: str) -> dict[str, str]:
    """Return support policies relevant to the customer's question."""
    words = question.lower()
    evidence: dict[str, str] = {}
    if 'cancel' in words or 'ship' in words:
        evidence['cancellations'] = POLICIES['cancellations']
    if 'return' in words or 'refund' in words:
        evidence['returns'] = POLICIES['returns']
    ctx.deps.evidence.update(evidence)
    return evidence
async def answer_support_question(question: str) -> SupportResult:
    deps = SupportDeps()
    result = await support_agent.run(question, deps=deps)
    return SupportResult(answer=result.output, evidence=deps.evidence)
```
This code gives the evaluation two contracts to enforce before adding a judge. Pydantic AI validates `SupportAnswer` before returning it and retries or raises an error if the model cannot produce valid output. Logfire records the agent's policy-tool call and model call in the same trace. Neither establishes that the prose is faithful, but both rule out entire classes of failure without asking another model.

## 

Create `quality.py`. The first evaluator verifies that answers cite retrieved evidence and that the agent escalates when no policy is found. The second verifies from the trace, rather than the final prose, that the policy lookup ran.

```
from dataclasses import dataclass
from pydantic_evals.evaluators import (
    EvaluationReason,
    Evaluator,
    EvaluatorContext,
    LLMJudge,
    ToolCorrectness,
)
from support_agent import SupportResult
@dataclass
class EvidenceContract(Evaluator[object, SupportResult, object]):
    def evaluate(
        self, ctx: EvaluatorContext[object, SupportResult, object]
    ) -> EvaluationReason:
        cited = set(ctx.output.answer.cited_policy_ids)
        available = set(ctx.output.evidence)
        missing = sorted(cited - available)
        if missing:
            return EvaluationReason(
                value=False,
                reason=f'Unknown policy IDs: {", ".join(missing)}',
            )
        if ctx.output.answer.action == 'escalate':
            if available:
                return EvaluationReason(
                    value=False,
                    reason='The agent escalated when relevant policies were available.',
                )
            return EvaluationReason(value=True)
        if not available:
            return EvaluationReason(
                value=False,
                reason='The answer did not escalate when no policy was found.',
            )
        if not cited:
            return EvaluationReason(
                value=False,
                reason='The answer used evidence without citing it.',
            )
        return EvaluationReason(value=True)
used_policy_lookup = ToolCorrectness(
    expected_tools=['lookup_policy'],
    evaluation_name='used_policy_lookup',
)
```
These checks are fast, deterministic, and make no model calls. Run them on every offline case. In production, run them in the background and apply them to all eligible traffic when practical. An LLM should never adjudicate whether `cited_policy_ids` contains an unknown string.

The `used_policy_lookup` check proves one required step: the agent called the policy lookup tool exactly once and called no unexpected tools. It does not prove that the entire trajectory was correct or efficient. Add separate agentic evaluators for other observed failure modes, such as wrong tool arguments, calls in the wrong order, or unnecessary retries. [`ToolCorrectness`](https://pydantic.dev/docs/ai/evals/evaluators/agentic/) evaluates the same OpenTelemetry trace you inspect in Logfire.

## 

A deterministic check can verify that a citation exists, but it cannot establish whether the answer follows from the cited policy. Add one judge to answer only that question:

```
FAITHFULNESS_RUBRIC = """
Pass only when every factual claim in `answer.text` is supported by an
`evidence` entry named in `answer.cited_policy_ids`. Accurate paraphrases pass.
Added deadlines, eligibility rules, guarantees, or exceptions fail.
"""
faithfulness_judge = LLMJudge(
    rubric=FAITHFULNESS_RUBRIC,
    model='openai:gpt-5.2',
    assertion={
        'evaluation_name': 'faithful_to_policy',
        'include_reason': True,
    },
)
```
The judge returns a pass/fail assertion and a reason. For this rubric, a binary result has a clearer decision boundary than a 1-to-10 score, and the reason makes a surprising result debuggable.

Airbnb recommends a separate evaluator and judge prompt for each dimension. Give faithfulness and concision their own judges so you can debug and calibrate each rubric independently.

## 

Create `eval_support.py`:

```
import asyncio
import logfire
from pydantic_evals import Case, Dataset
from quality import EvidenceContract, faithfulness_judge, used_policy_lookup
from support_agent import SupportResult, answer_support_question
dataset = Dataset[str, SupportResult, None](
    name='support-policy-agent',
    cases=[
        Case(name='return_window', inputs='Can I return an unused item after 20 days?'),
        Case(name='refund_timing', inputs='How quickly will my refund arrive?'),
        Case(name='cancel_unshipped', inputs='Can I cancel an order that has not shipped?'),
        Case(name='return_after_shipping', inputs='Can I return an unused item after it ships?'),
        Case(name='unknown_policy', inputs='Do you offer price matching?'),
    ],
    evaluators=[
        EvidenceContract(),
        used_policy_lookup,
        faithfulness_judge,
    ],
)
def pass_rate(report, evaluation_name: str) -> float:
    values = [
        case.assertions[evaluation_name].value
        for case in report.cases
        if evaluation_name in case.assertions
    ]
    if not values:
        raise RuntimeError(f'No results found for {evaluation_name!r}.')
    return sum(values) / len(values)
async def main() -> None:
    report = await dataset.evaluate(
        answer_support_question,
        name='baseline',
    )
    report.print(include_reasons=True)
    assert pass_rate(report, 'EvidenceContract') == 1.0
    assert pass_rate(report, 'used_policy_lookup') == 1.0
    assert pass_rate(report, 'faithful_to_policy') == 1.0
    print(logfire.url_from_eval(report))
if __name__ == '__main__':
    asyncio.run(main())
```
These five cases confirm that the evaluation pipeline runs and records useful results. They are too small to establish the agent's quality. Replace them with the failures you found while reading the first 100 traces, then add real regressions as they appear.

The run now appears as an experiment in the Evals workspace. You can compare it with the next prompt or model version, open the cases behind a changed score, and follow any result into its complete trace. Set a threshold for each evaluator rather than averaging unrelated checks into one number. The assertions make the script usable as a continuous integration (CI) gate.

Open **AI Evaluations** > **Experiments**, find `baseline`, and select **Review results**. Start on **Overview**: confirm that every case completed, check the assertion and task-error totals, then scan each evaluator. Assertion bars show the balance of passes and failures. If you also record numeric scores, histograms show whether an average hides a weak tail or several distinct clusters. The aggregate tells you where to look, not what to change.

![A focused Logfire experiment overview showing completion, assertions, task errors, score distributions, and operational metrics.](https://pydantic.dev/assets/blog/three-layer-evals-logfire/experiment-overview.webp)


Select **Review cases** beside `faithful_to_policy`, then filter to **Needs review** or **Failed**. Read the evidence in this order:

1. Confirm the input the task received.
2. Inspect the output it returned.
3. Read the selected evaluator's result and reason.
4. Open the trace in Live view when the output alone does not explain the result.

![A failed evaluation case in Logfire with its input, output, evaluator results, and trace link.](https://pydantic.dev/assets/blog/three-layer-evals-logfire/case-review.webp)


A bad answer paired with an accurate evaluation points to the agent. A reasonable answer paired with a surprising score points to the rubric or evaluator. Diagnose that boundary before editing the system prompt.

## 

An uncalibrated judge is another model output, not ground truth. Airbnb recommends a gold set of 50 to 100 examples containing both good and bad outputs, and reaching agreement in the high 80s or 90s before using a judge at scale. [Google's evaluator guidance recommends the same loop](https://developers.google.com/stax/evaluators): rate a sample yourself, run the judge on the same sample, compare, and refine the rubric.

You can create those labels in Logfire while looking at the complete interaction. First, agree on one criterion, such as "The answer resolves the customer's question without inventing policy details." A verdict becomes reusable calibration data only when reviewers apply the same rule.

For individual runs:

1. Open **AI Evaluations** >**Annotations** .
2. Choose the support agent and select **Proceed to annotate** .
3. Open a run and inspect its input, final output, model calls, tool calls, and trace.
4. Select **Annotate** , choose**Pass** ,**Neutral** , or**Fail** , and classify the failure when a category applies. Add the corrected response in**Expected output** when you know what the agent should have returned.
5. Explain the verdict in **Comment** , add tags such as`unsupported-claim` or`missing-escalation` , then select**Save** . Logfire advances to the next queued run; on the final run, the button reads**Save and close** .

![A focused Logfire annotation form showing a failed verdict, failure category, expected output, reviewer comment, and tags.](https://pydantic.dev/assets/blog/three-layer-evals-logfire/agent-run-annotation-form.png)


For a systematic calibration pass, put 50 to 100 runs in an annotation queue. Run annotations are in beta, and annotation queues are available on the Logfire Design Partner plan.

Each annotation becomes a score attached to the interaction alongside the automated evaluator results. When a reviewer confirms a new failure, add its trace to a hosted dataset from Live view so the next offline experiment tests it again. The [human review guide](https://pydantic.dev/docs/logfire/evaluate/human-review/) covers run annotations, annotation queues, and end-user feedback in more depth.

Once an expert has labeled a set, keep each reviewed output and label in a local or hosted dataset. Replay those saved results without rerunning the support agent, apply the judge, and measure how often it agrees with the reviewer:

```
from pydantic_evals import Case, Dataset
from quality import faithfulness_judge
from support_agent import SupportAnswer, SupportResult
def saved_result(answer: str, evidence: str) -> SupportResult:
    return SupportResult(
        answer=SupportAnswer(
            text=answer,
            cited_policy_ids=['returns'],
            action='answer',
        ),
        evidence={'returns': evidence},
    )
gold_set = Dataset(
    name='faithfulness-judge-gold-set',
    cases=[
        Case(
            name='accurate_paraphrase',
            inputs=saved_result(
                'You can return an unused item within 30 days.',
                'Unused items can be returned within 30 days.',
            ),
            metadata={'human_faithful': True},
        ),
        Case(
            name='invented_window',
            inputs=saved_result(
                'You can return an unused item within 60 days.',
                'Unused items can be returned within 30 days.',
            ),
            metadata={'human_faithful': False},
        ),
        # Add 48 to 98 reviewed examples, including difficult failures.
    ],
    evaluators=[faithfulness_judge],
)
report = gold_set.evaluate_sync(lambda result: result, name='judge-calibration')
agreement = sum(
    case.metadata['human_faithful'] == case.assertions['faithful_to_policy'].value
    for case in report.cases
) / len(report.cases)
print(f'Agreement: {agreement:.1%}')
```
The two cases keep the snippet short. Build the real gold set from 50 to 100 balanced examples with good answers, clear failures, and difficult boundaries. Track a confusion matrix or [Cohen's kappa](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) as the set grows. If experts disagree, resolve the disagreement or narrow the rubric before automating it.

When the judge disagrees with a reviewer, read the reason and classify the cause:

- **The rubric is ambiguous:** make the rule observable and add examples.
- **The judge lacks context:** include the source material it needs.
- **The human label is wrong:** correct the gold set and record why.
- **The case is genuinely subjective:** keep it with humans instead of forcing automation.

Re-run this calibration when the domain changes, a new failure mode appears, or you switch judge models.

## 

The three layers establish what failed and whether the diagnosis is trustworthy. Logfire's optimizer shortens the next step: deciding what to change.

Because the support agent is instrumented, both its offline eval executions and its production traffic appear as agent runs. Open **Agents**, select the support agent, and open **Optimize**. The optimizer reviews recent runs, prioritizes runs that raised exceptions, proposes one prompt edit, and cites the traces behind it. It does not apply the edit automatically.

![A focused Logfire optimization proposal that routes paid-plan billing tickets to a human, with the current and proposed prompts shown side by side.](https://pydantic.dev/assets/blog/three-layer-evals-logfire/optimizer-proposal.png)


Use it as part of the same review loop:

1. Use evaluator failures and human annotations to identify the behavior that needs work.
2. Generate an optimization proposal for the agent.
3. Read the prompt diff and open the cited runs. Reject the proposal if the evidence points to a bad evaluator, missing context, or an infrastructure failure instead of the prompt.
4. Apply the accepted edit to a candidate version, rerun the same dataset, and compare it with the baseline in the Evals workspace.

The optimizer turns the three layers into a change proposal, but the decision stays with the reviewer. Read the cited evidence and make sure the edit addresses a real agent failure rather than teaching the prompt to satisfy a flawed evaluator. The [prompt optimization walkthrough](https://pydantic.dev/articles/logfire-prompt-optimization) shows the proposal and review flow in more detail.

## 

Offline experiments ask, "Is this change safe to ship?" Online evaluations score live traces and ask, "Does it hold up on real traffic?"

Pydantic Evals can attach the same evaluators to a live function. This example adapts Airbnb's 5% production sample to the model judge while applying cheap checks to all eligible traffic. Online evaluation runs in the background; the callback records any work dropped when a concurrency limit is full.

```
import logfire
from pydantic_evals.evaluators import EvaluatorContext
from pydantic_evals.online import OnlineEvaluator, evaluate
from quality import EvidenceContract, faithfulness_judge, used_policy_lookup
from support_agent import answer_support_question
def record_evaluation_drop(_: EvaluatorContext) -> None:
    logfire.warning('Online evaluation dropped because its concurrency limit was reached')
evaluated_answer_support_question = evaluate(
    OnlineEvaluator(
        evaluator=EvidenceContract(),
        sample_rate=1.0,
        max_concurrency=100,
        on_max_concurrency=record_evaluation_drop,
    ),
    OnlineEvaluator(
        evaluator=used_policy_lookup,
        sample_rate=1.0,
        max_concurrency=100,
        on_max_concurrency=record_evaluation_drop,
    ),
    OnlineEvaluator(
        evaluator=faithfulness_judge,
        sample_rate=0.05,
        max_concurrency=5,
        on_max_concurrency=record_evaluation_drop,
    ),
    target='support-policy-agent',
    extract_args=True,
    record_return=True,
)(answer_support_question)
```
The evaluator results are emitted as OpenTelemetry `gen_ai.evaluation.result` events. Open **AI Evaluations** > **Live Monitoring** in Logfire. Each result stays linked to the production trace that produced it. That creates an operating loop:

1. Watch pass rates and evaluator errors in Live Monitoring.
2. Open a failed result and inspect its trace.
3. Send failures, disagreements, and a random sample to human review.
4. Add confirmed new failure modes to the offline dataset.
5. Update the system, rerun the experiment, and compare it with the baseline.

Logfire does not charge per score, so sampling is about judge-model spend and review capacity rather than an evaluation meter. Load-test the concurrency limits against your traffic before deploying the wrapper.

## 

For this support agent, a reasonable starting cadence is:

- **Every pull request:** Run all programmatic checks and a small calibrated judge set. Review only surprising changes.
- **Nightly or before release:** Run the full regression and challenge sets with every calibrated judge. Resolve disagreements and approve gates.
- **Production:** Run programmatic checks at a 100% sample rate and sample the judges. Review failures, uncertain cases, and a random sample.
- **Periodically:** Calibrate judges against the gold set, then update labels, rubrics, and examples.

The human layer should improve the automated layers, not become a queue that grows forever. Every repeated, objective human decision is a candidate for code. Every repeated, nuanced decision is a candidate for a calibrated judge. Some decisions should remain human.

## 

Airbnb's three-layer pattern sends each decision to the least expensive method that can answer it reliably. Logfire keeps the programmatic check, judge result, human score, and full system trace attached to the same interaction.

A falling average becomes the start of the investigation, not the end. Open the cases that changed, read the judge's reason, check the human label, and inspect the retrieval and tool calls that produced the answer.

Start with traces and let real failures determine the evaluators. Calibrate judges against human labels. Use confirmed failures to review the optimizer's proposal, add them to the dataset, and rerun the experiment.

We do not know what Airbnb uses for evals. If it happens to be Braintrust, [two environment variables can point the same SDK at Logfire](https://pydantic.dev/articles/switching-from-braintrust). Given the [per-score math](https://pydantic.dev/articles/braintrust-week), the savings might cover their next vacation, and then some.

For the Logfire workflow, read the guides to [datasets and experiments](https://pydantic.dev/docs/logfire/evaluate/datasets-and-experiments/), [human review](https://pydantic.dev/docs/logfire/evaluate/human-review/), [live evaluations](https://pydantic.dev/docs/logfire/evaluate/live-evals/), and the [prompt optimizer](https://pydantic.dev/articles/logfire-prompt-optimization). For evaluator design, read the Pydantic Evals guide to [LLM judges](https://pydantic.dev/docs/ai/evals/evaluators/llm-judge/).
