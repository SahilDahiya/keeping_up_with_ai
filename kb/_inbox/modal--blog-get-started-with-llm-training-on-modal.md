---
title: Get started with LLM training on Modal
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/get-started-with-llm-training-on-modal
author: Joy Liu; Andrew Hinh
published: '2026-10-21'
fetched: '2026-10-22T06:09:42Z'
classifier: null
taxonomy_rev: 2
words: 1024
content_sha256: 94d46afbcdabbb377fd88af1c5c1153ee949e322f0a9ea6ef540a98498f241a0
---

# Get started with LLM training on Modal

We’ve written about how [reinforcement learning (RL) is an infrastructure problem](https://modal.com/blog/reinforcement-learning-infrastructure-problem),
and how the [last five years](https://modal.com/blog/truly-serverless-gpus) of
work we’ve done provides [performant](https://modal.com/blog/bringing-serverless-functions-closer-to-the-speed-of-wire), [available](https://modal.com/blog/modal-clusters-generally-available), and [scalable](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds) infrastructure you can rely on to train your models. Even without the concerns
of infrastructure, RL is still hard! There are many higher-level components in
the system that control your outcome: you need appropriate base models,
high-fidelity environments, clear and robust reward functions, and tuned
training recipes that actually work.

But if you have an agent harness deployed in production, with evals and agent traces collected from that deployment, you’re already 80% of the way there. You just need an easy way to start training on your data.

That’s why we built [Modal Dojo](http://dojo.modal.dev): a library that gives
you the building blocks, tuned defaults, and observability you need for easy,
production-grade LLM training.

It’s available now. All it takes is a prompt:

```
Use Modal Dojo to train [X model] on [Y proprietary dataset]
to replace [Z agent].
```
Read on to learn more about how we built it and why.

## Betting on open-source

Companies build differentiated value when they own their intelligence. Post-training enables you to effectively compete on task-intelligence per dollar — in particular, by training on proprietary data and iterating quickly on training recipes. Doing this effectively requires full control over your training stack, down to the source code. And this is exactly what Modal is designed for. We build reliable and scalable abstractions that expose their inner workings to grow with our users’ needs.

Our training library builds on multiple battle-tested open source frameworks
like [Miles](https://www.lmsys.org/blog/2026-08-18-miles-v0-1/) and [Slime](https://github.com/THUDM/slime). They give you the foundation to build
robust post-training without relying on closed source providers or having to
reinvent the wheel from scratch. We’ve even [patched](https://github.com/sgl-project/sglang/pull/33593) and [upstreamed](https://github.com/radixark/miles/pull/3354) a [few PRs](https://github.com/sgl-project/sglang/pull/34319) [ourselves](https://github.com/sgl-project/sglang/pull/40986).

When you own the full stack, you can customize to your heart’s content. We’ve
designed the library to allow you to tune recipes for maximum performance, build
complex environments, patch the underlying frameworks, and even [reshape the observability dashboard](https://www.inkandswitch.com/essay/malleable-software/) that comes out of the box.

## Production LLM training in \<100 LOC

Using our training library is as easy as:

```
import re
from modal_dojo import (
    HuggingFaceDataset,
    Qwen3_8_27B,
    Qwen3_8_27B_Recipe,
    TrainConfig,
)
model = Qwen3_8_27B()
```
## async def gsm8k_rm(args, sample, **kwargs) -> float:

BOXED_RE = re.compile(r"\\boxed\{([^}]+)\}")
    NUMBER_RE = re.compile(r"-?[\d,]+(?:\.\d+)?")
    text = model.parse_response(sample.response or "").content
    boxed = BOXED_RE.findall(text)
    pred = boxed[-1] if boxed else (NUMBER_RE.findall(text) or [""])[-1]
    try:
        return float(float(pred.replace(",", "")) == float(sample.label))
    except ValueError:
        return 0.0
config = TrainConfig(
    model=model,
    dataset=HuggingFaceDataset(
        hf_repo="skrishna/gsm8k_only_answer",
        hf_split="train[:120]",
        input_column="text",
        output_column="label",
        input_format="text",
    ),
    recipe=Qwen3_8_27B_Recipe(
        custom_rm_function=gsm8k_rm,
    ),
)
run = config.launch()
print(run.training_run_id)
Let’s break this down.

1. First, you have to [choose a model to train](https://dojo.modal.dev/guides/model). This training
library has been validated on everything from [a half billion to multi-trillion parameter models](https://dojo.modal.dev/#supported-models) with support for bringing your own. All it takes is running evals for these
models to determine the right fit.
2. Then, you’ll need [data to train your model on](https://dojo.modal.dev/guides/dataset). It’s
easy to load one from Hugging Face, ingest a Harbor environment, or use your
harness and evals to create one yourself. Using production traces, you can
generate tasks for that environment to form your training and test split.
3. [Lastly, you need a recipe before you can start cooking.](https://dojo.modal.dev/guides/recipe) While the model and dataset dictate *what* will be trained, the recipe
dictates *how* training will occur by specifying parameters for the hardware,
parallelism, total rollout size, environment, and more. We provide
auto-optimized recipes for all supported models, developed through our
experience with teams training models for exceptionally frontier performance
in their respective fields. But when you need to extend these recipes for
your specific use case, it’s as simple as [changing a few parameters](https://dojo.modal.dev/reference/sdk).

Then, you’re ready to [start training](https://dojo.modal.dev/guides/training)!

## Metric observability

To catch reward hacking in the act, debug stalling runs, and track the progress of many concurrent runs, you need observability of key metrics for training stability and substep timing.

Modal’s training library comes out of the box with an [observability dashboard](https://dojo.modal.dev/guides/dashboard). Backing it
is a robust metric collector we built to show you everything you need to track
your run’s progress: loss and reward curves, framework-emitted metrics, the
agent’s trajectory for each rollout during training, granular profiling down to
the substep, and container logs to easily identify bottlenecks and debug runs.

## It’s so easy, even your agent can do it!

Agents are particularly useful when you need to validate hypotheses or run many experiments in parallel. However, they are less effective when forced to create and sift through thousands of lines of configuration files and source code, or reason through how to fix bugs in training without guidance from seasoned experts.

Everything you might need to train a model is readily available to your agents.
As shown above, the API is intuitive and minimal. Through the [CLI](https://dojo.modal.dev/reference/cli), agents can get a run’s status,
metadata, logs, and agent traces with ease. And the [skills](https://dojo.modal.dev/reference/cli/skills) we’ve crafted helps guide
them in a predictable and directed manner. With all that in place, RL becomes a
problem that your agent can one-shot a baseline for.

[Here’s an example of what a single prompt can do](https://dojo.modal.dev/guides/agent):

If you’re doing something more advanced and need guidance, [reach out](https://modal.com/slack).

## Customers are moving faster than ever

We’re seeing post-training happen at unprecedented speeds on top of Modal Dojo.

### Axiom Bio trains models to reduce **unexpected drug toxicity**

[Axiom Bio](https://www.axi.om/) trains large open models to identify molecules
from mass spectrometry data. With Modal Dojo, they were able to quickly conduct
large-scale, long-context RL experiments.

### Afterquery curates expert data across a variety of domains

[Afterquery](https://www.afterquery.com/) curates data from domain experts for
models to be trained on. Using Modal Dojo, they were able to kick off [autoresearch](https://modal.com/blog/autoscaling-autoresearch) on their
existing datasets for performance hillclimbing.

## Get started now

At Modal, our goal is to help you own your intelligence. So far, we’ve
productionized LLM inference with [Endpoints](https://modal.com/blog/introducing-auto-endpoints), enabled the
testing of alternative deployments with [Endpoint Candidates](https://modal.com/blog/endpoint-candidates), and sped up
trillion-parameter model inference with [speculative decoding](https://modal.com/blog/trillion-tokens-trillion-parameters).
Now, we are giving you the ability to train toward your own Pareto frontier.
