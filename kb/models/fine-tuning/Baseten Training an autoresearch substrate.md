---
title: 'Baseten Training: an autoresearch substrate'
topic: models
subtopic: fine-tuning
secondary_topics:
- agents/tool-use
- infra-platform/gpu-clusters
summary: Frames model training infrastructure as an autoresearch substrate for running
  iterative experiments and training jobs.
source: baseten
url: https://www.baseten.co/blog/baseten-training-an-autoresearch-substrate/
author: Raymond Cano
published: '2026-03-31'
fetched: '2026-07-11T04:05:49Z'
classifier: codex
taxonomy_rev: 1
words: 1104
content_sha256: ab366aee39319465bb377a1205d54abc5edffa883d1bae6309d321177cd932fb
triage: keep
skip_reason: null
---

# Baseten Training: an autoresearch substrate

![autoresearch](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774921840-baseten-training-blog-autoresearch.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

When Andrej Karpathy released [autoresearch](https://github.com/karpathy/autoresearch), it formalized something our researchers were already doing informally: humans define the research program, and an AI agent runs the experiments.

We've been running this loop internally for the past few months, pointed at [Baseten Training](https://docs.baseten.co/training/overview), and it has become a core part of how we work. That loop has driven our [KV cache compaction research](https://www.baseten.co/research/repeated-kv-cache-for-long-running-agents/), our work rightsizing [Qwen3 Coder](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-80b-msswift/training) for long sequence lengths, and several experiments we'll be sharing soon. The prompts are simple and experimentation is easily parallelized, giving us a substrate for autoresearch.**Why autoresearch works better on Baseten Training**

Standard training infrastructure gives agents too much surface area. An agent with SSH access to a GPU node can edit any file, install packages, change system state, and create the kind of drift that makes experiments unreproducible. Baseten Training naturally avoids these pitfalls:

- [Baseten Training](https://docs.baseten.co/training/overview)is CLI-first and agents are pretty darn good with CLI tools. Additionally, we provide an mcp for easier access to documentation.
- The training jobs themselves are containerized - meaning that side effects from one job won’t impact the next. Local code is zipped up, so each experiment implicitly has its own copy of code. Layering on git is easy, but also optional.
- You can run multiple training jobs at once. Baseten’s on-demand compute allows you to fan out your experiments
- Results are easily observable. Logs and metrics are retrievable by CLI, and our execution harness makes job results easily understandable
- The workflow is inherently a - **single entrypoint**. The agent submits a self-contained configuration via- `truss train push`rather than SSH-ing into a node. This seems like a small distinction, but it creates focus for the agent to avoid degenerating into messy, scattered changes when given free reign across too many files.

**The result is that the product itself is bootstrapped for agentic iteration, creating a prompt-minimal ****experiment loop**** out of the box.**

![autoresearch](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774921047-autoresearch-karpathy.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## Try it yourself

Getting started takes a Baseten account with GPU access, the Truss CLI, and a CLI agent like Claude Code. If you don't have H100 access or need a higher GPU quota, [reach out to us](mailto:support@baseten.co).

- Install the Baseten MCP server:

`claude mcp add --transport http baseten-docs https://docs.baseten.co/mcp`This helps your agent have enough context to use the truss CLI. Alternatively, you can prompt it to use the `--non-interactive` flag and `--help` when stuck.

2. Then, install the Truss CLI and clone the cookbook:

```
pip install -U truss && truss login
git clone https://github.com/basetenlabs/ml-cookbook.git
cd ml-cookbook/recipes/autoresearch-finetune/training
```
3. Open up your agent and prompt away:

```
Optimize val_loss by fine-tuning Qwen3-8B on pirate-ultrachat-10k.
Edit run.sh only and avoid modifying train_iters.
You can run a total of 10 experiments and run experiments 2 at a time.
```
The default configuration fine-tunes Qwen3-8B on [pirate-ultrachat-10k](https://huggingface.co/datasets/winglian/pirate-ultrachat-10k) using 2 H100s with [MS-Swift](https://github.com/modelscope/ms-swift)/Megatron, though Baseten Training is framework-agnostic. The same pattern works with Hugging Face TRL, Axolotl, or plain PyTorch.

A cap on parallel jobs and a total experiment budget keeps the process focused, and it forces the agent to spend its tries where they matter.

While the agent runs, you can monitor progress in several ways. The CLI agent's own output shows each submission and result in real time. Job logs are available through `truss train logs` or the Baseten UI. And if you store a `wandb_api_key` secret on Baseten, experiment metrics can be logged to Weights & Biases.

![autoresearch](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774920779-autoresearch-2-16-9.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Validation loss across nine autoresearch experiments, from an untuned baseline (1.39) to 13.3% lower after automated hyperparameter search on 2×H100s.

Validation loss across nine autoresearch experiments, from an untuned baseline (1.39) to 13.3% lower after automated hyperparameter search on 2×H100s.## Decomposing autoresearch

At a high level, an autoresearch prompt needs to communicate three things: what the objective is (e.g. metric to optimize), what the agent can change, and what the agent can’t change.

When we were rightsizing Qwen3 Coder for long sequence lengths, we used this prompt:

Let's figure out how to run Qwen3-coder-next at sequence lengths of 32, 64, and 128k using the existing GLM 4.7 script as a starting point. Each experiment should train for 4 steps, eval every 2 steps, and write a checkpoint. Install flash linear attention to $BT_PROJECT_CACHE_DIR. Start with expert_parallelism=num_gpus. You can use a maximum of 4 nodes concurrently and you can run a total of 8 experiments. Modify training-related parameters in the run.sh file only.

The agent proceeded to diagnose OOM bottlenecks, adjust `recompute_num_layers`, and iterate toward working parallelism configurations by toggling expert, pipeline, and tensor parallelism. It did the tedious work of searching through configurations that a human would find mind-numbing, and it did so while managing concurrent experiments.

## Where autoresearch works, and where it doesn't

Once you have a clearly defined metric and a way to normalize experiments (usually wall-clock time, not steps or FLOPs), every experiment becomes directly comparable regardless of what the agent changed. This is where autoresearch shines: methodical, bounded optimization within a well-defined search space.

As Charlie O'Neill put it on our internal Slack:

I think it's having a really clear, constrained setup to hill-climb, and not allowing it to edit the "test harness" once you're confident in your metric.

That's the key insight. The human researcher's role shifts from running experiments to curating the search space. In practice, we've found it useful to maintain two running lists: specific optimizations to try (targeting a known metric) and broader hypotheses to test (mapping the contours of the problem). The first list is where autoresearch excels. The second is where a researcher's judgment remains essential.

Without periodic intervention, agents tend to degenerate. They collapse into increasingly narrow, incremental changes: adjusting the learning rate by 0.001, toggling a single flag, or rerunning the same configuration with a different seed. Even in Karpathy's own runs, this pattern emerges. The agent's implicit value function is, for lack of a better term, too vanilla to sustain genuine novelty over extended runs. The best results come from a researcher periodically injecting new directions and letting the agent optimize within those bounds.

Autoresearch is a tool for accelerating the experimental grind, not for replacing research taste. The human decides what questions are worth asking. The agent finds out the answers faster than you could alone.

## Conclusion

The setup is minimal: a single repo directory with a training script, a config file, and a three-line prompt. The iteration is fast: edit, submit, monitor, and evaluate. And the infrastructure stays out of the way, which turns out to be the most important feature of all.

Clone the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook), navigate to `recipes/autoresearch-finetune/training`, write your prompt, and start autoresearching.
