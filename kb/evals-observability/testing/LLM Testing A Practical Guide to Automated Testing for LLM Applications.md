---
title: 'LLM Testing: A Practical Guide to Automated Testing for LLM Applications'
topic: evals-observability
subtopic: testing
secondary_topics:
- product-engineering/architecture
summary: Practical guide to automated testing for LLM applications, covering test
  cases, regression checks, CI-style workflows, and quality gates.
source: langfuse
url: https://langfuse.com/blog/2025-10-21-testing-llm-applications
author: null
published: '2025-10-21'
fetched: '2026-07-11T04:35:45Z'
classifier: codex
taxonomy_rev: 1
words: 1536
content_sha256: 67c8a01e92e9add64c1f16f16f36e068ff7dc7504c44003c62cc2f3ffa6084f1
---

# LLM Testing: A Practical Guide to Automated Testing for LLM Applications

# LLM Testing: A Practical Guide to Automated Testing for LLM Applications

Learn how to test LLM applications with automated evaluation, datasets, and experiment runners. A practical guide to LLM testing strategies.

![Picture Abdallah Abedraba](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Faabedraba.jpeg&w=96&q=75) Abdallah Abedraba

Abdallah AbedrabaTesting LLM applications presents unique challenges. Unlike traditional software where outputs are deterministic, LLMs produce varied responses that can't be verified with simple equality checks. Yet the need for systematic testing remains critical—how do you ensure your AI application works reliably across deployments?

This guide shows you how to implement automated tests for LLM applications using datasets and experiment runners, inspired by [Hamel Husain's testing framework](https://hamel.dev/blog/posts/evals/#level-1-unit-tests).

[Testing vs. Evaluation in LLM Applications](https://langfuse.com#testing-vs-evaluation-in-llm-applications)

Before diving in, let's clarify some terminology that often causes confusion:

**Testing** typically means running automated checks that produce pass/fail results. You write assertions like `assert result == expected` and your test suite tells you if something broke.

**Evaluation** is about measuring quality. How accurate is your model? How helpful are the responses? These are scored on continuous scales rather than binary pass/fail.

Traditional testing relies on predictable outputs. You assert that `add(2, 3)` returns `5`. But when you ask an LLM "What is the capital of France?", you might get "Paris", "The capital is Paris", "Paris, France", or a longer explanation. All are correct, but none match exactly.

This variability doesn't mean we can't test LLM applications—it means we need different testing strategies. In LLM applications, these concepts blend together. You "test" your application by "evaluating" its outputs with scoring functions. A test passes if the evaluation score meets your threshold.

[Unit Tests vs What We're Building](https://langfuse.com#unit-tests-vs-what-were-building)

Hamel Husain calls this approach "Level 1: Unit Tests" in his framework, and we'll use similar terminology. However, it's worth noting that these aren't traditional unit tests:

**Traditional unit tests**:

- Test isolated code units
- Deterministic (same input = same output)
- Fast, no external dependencies

**LLM application tests**:

- Test application behavior
- Non-deterministic (same input can produce different outputs)
- Slower execution

Think of these as **automated regression tests** that verify your LLM application maintains acceptable quality as you make changes. The "unit" being tested is your application's behavior on specific inputs.

[The Solution: Datasets + Experiment Runners + Evaluators](https://langfuse.com#the-solution-datasets--experiment-runners--evaluators)

The approach combines three components:

- **Datasets**: Collections of input/output pairs that represent your test cases
- **Experiment Runners**: Execute your LLM application against the dataset
- **Evaluators**: Score the outputs programmatically instead of checking exact matches

Let's see how this works in practice.

[Example: Testing a Geography Question Answering System](https://langfuse.com#example-testing-a-geography-question-answering-system)

Here's a complete example testing an LLM application that answers geography questions, using Langfuse's Experiment Runner SDK and local test data.

First, setup the environment variables:

```
# .env file
OPENAI_API_KEY=your_openai_api_key
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```
You can export the environment variables to your shell:

`export $(grep -v '^#' .env)`Now create the test file:

```
# test_geography_experiment.py
import pytest
from langfuse import get_client, Evaluation, Langfuse
from langfuse.openai import OpenAI
# Each test case includes both the input and expected output. The expected output
# serves as a reference for evaluation, not as an exact string match.
test_data = [
    {"input": "What is the capital of France?", "expected_output": "Paris"},
    {"input": "What is the capital of Germany?", "expected_output": "Berlin"},
    {"input": "What is the capital of Spain?", "expected_output": "Madrid"},
]
# The task function wraps your LLM application logic. It receives each test item and
# returns the LLM's response. This should be your full LLM application logic.
def geography_task(*, item, **kwargs):
    """Task function that answers geography questions"""
    question = item["input"]
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content
# This evaluator checks if the expected answer appears anywhere in the output, accounting
# for LLM verbosity. You could also use more sophisticated evaluators, including LLM-as-a-judge
# for semantic similarity.
def accuracy_evaluator(*, input, output, expected_output, **kwargs):
    """Evaluator that checks if the expected answer is in the output"""
    if expected_output and expected_output.lower() in output.lower():
        return Evaluation(name="accuracy", value=1.0)
    return Evaluation(name="accuracy", value=0.0)
# Run-level evaluators aggregate scores across all test items, giving you a single
# metric to assert against.
def average_accuracy_evaluator(*, item_results, **kwargs):
    """Run evaluator that calculates average accuracy across all items"""
    accuracies = [
        eval.value for result in item_results
        for eval in result.evaluations if eval.name == "accuracy"
    ]
    if not accuracies:
        return Evaluation(name="avg_accuracy", value=None)
    avg = sum(accuracies) / len(accuracies)
    return Evaluation(name="avg_accuracy", value=avg, comment=f"Average accuracy: {avg:.2%}")
@pytest.fixture
def langfuse_client() -> Langfuse:
    """Initialize Langfuse client for testing"""
    return get_client()
def test_geography_accuracy_passes(langfuse_client: Langfuse):
    """Test that passes when accuracy is above threshold"""
    result = langfuse_client.run_experiment(
        name="Geography Test - Should Pass",
        data=test_data,
        task=geography_task,
        evaluators=[accuracy_evaluator],
        run_evaluators=[average_accuracy_evaluator]
    )
    # Access the run evaluator result directly
    avg_accuracy = next(
        eval.value for eval in result.run_evaluations
        if eval.name == "avg_accuracy"
    )
    # Assert minimum accuracy threshold
    assert avg_accuracy >= 0.8, f"Average accuracy {avg_accuracy:.2f} below threshold 0.8"
```
**Set Appropriate Thresholds**: Not all tests need 100% accuracy. Set realistic thresholds based on your application's requirements:

```
# Strict threshold for critical functionality
assert avg_accuracy >= 0.95, "Critical tests must have 95%+ accuracy"
# Relaxed threshold for experimental features
assert avg_accuracy >= 0.70, "Experimental feature needs improvement"
```
You can run the test with:

```
pip install pytest langfuse openai
pytest test_geography_experiment.py -v
```
[Running Tests in CI/CD](https://langfuse.com#running-tests-in-cicd)

You can integrate these tests into your continuous integration pipeline.

[GitHub Actions Example](https://langfuse.com#github-actions-example)

First, setup the environment variables in your Github Actions secrets:

![Github Actions secrets](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-10-21-testing-llm-applications%2Fgithub-actions-secrets.png&w=3840&q=75)


```
name: LLM Application Tests
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install pytest langfuse openai
    - name: Run LLM unit tests
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        LANGFUSE_PUBLIC_KEY: ${{ secrets.LANGFUSE_PUBLIC_KEY }}
        LANGFUSE_SECRET_KEY: ${{ secrets.LANGFUSE_SECRET_KEY }}
        LANGFUSE_BASE_URL: ${{ secrets.LANGFUSE_BASE_URL }}
      run: |
        pytest test_geography_experiment.py -v
```
[Using Remote Datasets with LLM-as-a-Judge](https://langfuse.com#using-remote-datasets-with-llm-as-a-judge)

For more advanced testing, you can use [remote datasets](https://langfuse.com/docs/evaluation/experiments/datasets) stored in Langfuse:

```
import pytest
from langfuse import get_client, Langfuse
@pytest.fixture
def langfuse_client() -> Langfuse:
    return get_client()
def test_with_remote_dataset(langfuse_client: Langfuse):
    """Test using a dataset stored in Langfuse with LLM-as-a-judge evaluation"""
    # Fetch dataset from Langfuse
    dataset = langfuse_client.get_dataset("geography-questions")
    def task(*, item, **kwargs):
        question = item.input
        response = OpenAI().chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
    # Run experiment - Langfuse automatically applies configured evaluators
    result = dataset.run_experiment(
        name="Geography Test with Remote Dataset",
        description="Testing geography QA with LLM-as-a-judge",
        task=task
    )
    # The LLM-as-a-judge evaluator runs automatically in Langfuse
    # Results are visible in the Langfuse UI
    langfuse_client.flush()
```
You can then see the result of LLM-as-a-judge evaluation and the aggregated score in the Langfuse UI:

![LLM-as-a-judge evaluation and aggregated score](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-10-21-testing-llm-applications%2Fllm-as-a-judge-results.png&w=3840&q=75)


[Benefits of Remote Datasets](https://langfuse.com#benefits-of-remote-datasets)

- **Centralized test management**: Update test cases without code changes
- **LLM-as-a-judge evaluators**: Configure semantic evaluation in the Langfuse UI (see- [LLM-as-a-judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge))
- **Historical tracking**: Compare results across runs to detect regressions
- **Team collaboration**: Share datasets across team members

When using remote datasets, all experiment results are tracked in Langfuse:

- View individual test case results with scores and reasoning
- Compare experiment runs over time
- Track which code changes improved or degraded performance
- Share results with team members through the Langfuse dashboard

We published two guides covering how to test chatbots and conversational applications with remote datasets and LLM-as-a-judge evaluators:

- [Evaluating Multi-Turn Conversations](https://langfuse.com/guides/cookbook/example_evaluating_multi_turn_conversations)
- [Simulating Multi-Turn Conversations](https://langfuse.com/guides/cookbook/example_simulated_multi_turn_conversations)

[Next Steps](https://langfuse.com#next-steps)

Ready to implement automated testing for your LLM application? Start by [identifying 3-5 critical functionalities](https://langfuse.com/academy/monitoring/error-analysis), create a small dataset with expected behaviors, and run your first experiment. We'd love to hear about your testing approach—join the conversation in our [GitHub Discussion](https://github.com/langfuse/langfuse/discussions), and explore our learning resources below.

[Learn More](https://langfuse.com#learn-more)


### Datasets Documentation


### Experiment Runner SDK


### Evaluating Multi-Turn Conversations


### Simulating Multi-Turn Conversations

[FAQ](https://langfuse.com#faq)

## How do you test LLM applications?

Testing LLM applications requires a different approach than traditional software testing. Instead of checking exact output matches, you use **evaluation functions** that score outputs on continuous scales. The typical approach combines three components: (1) **Datasets** — collections of input/output pairs representing test cases, (2) **Experiment runners** — tools that execute your LLM application against the dataset, and (3) **Evaluators** — scoring functions that assess output quality using LLM-as-a-Judge, semantic similarity, or custom logic. A test passes when evaluation scores meet your defined thresholds.

## What is the difference between LLM testing and LLM evaluation?

**Testing** produces binary pass/fail results — your test suite tells you whether something broke. **Evaluation** measures quality on continuous scales — how accurate, helpful, or relevant are the responses. In practice, LLM testing and evaluation blend together: you "test" your application by "evaluating" its outputs with scoring functions, and a test passes if the evaluation score meets your threshold. Both are essential for building reliable LLM applications.

## How do I automate LLM testing in CI/CD?

You can integrate LLM testing into your CI/CD pipeline using Langfuse's experiment runner SDK. Create a test script that: (1) loads your dataset (locally or from Langfuse), (2) runs your application against each test case, (3) scores the outputs with evaluator functions, and (4) asserts that scores meet minimum thresholds. Run this script as part of your CI pipeline using `pytest` or your preferred test runner. See the [experiments via SDK guide](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk) for implementation details.
