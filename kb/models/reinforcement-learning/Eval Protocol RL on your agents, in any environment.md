---
title: 'Eval Protocol: RL on your agents, in any environment'
topic: models
subtopic: reinforcement-learning
secondary_topics:
- evals-observability/evaluation
- agents/planning
summary: Describes using Eval Protocol to run reinforcement learning on agents in
  task environments.
source: fireworks
url: https://fireworks.ai/blog/eval-protocol-rl-on-your-agents
author: null
published: '2025-11-20'
fetched: '2026-07-11T04:14:53Z'
classifier: codex
taxonomy_rev: 1
words: 1306
content_sha256: 56c18ab458afc89fa1db9014f942ddbd34c9619246efeb5a34f2bf9d5cb92646
triage: keep
skip_reason: null
---

# Eval Protocol: RL on your agents, in any environment

- Announcing Eval Protocol for RL
- Why Eval Protocol
- Why RL today feels so detached from production
- Eval Protocol’s growing integration ecosystem
- Agents in the Real World: The Challenges of Production RL
- Why tracing has to come first
- Why RL feels more accessible now (and how EP leans into that)
- From messy traces to reliable feedback—and back into the loop

Eval Protocol (EP) is an open-source, language-agnostic framework that makes it easy to do reinforcement fine-tuning on agents, across any framework, environment, or trainer.

Your agents, infrastructure, and training needs will evolve as you scale. Eval Protocol is designed to grow with you: migrate from local experiments to remote training, try different environments, support more agent types, or extend to multiple use cases with the same training setup. Eval Protocol lets you set up a lightweight interface between your agent environment and trainer; your agent stays unchanged, and the training setup plugs in seamlessly. [Get set up for RL with your agent today.](https://evalprotocol.io/introduction)

Fireworks is open-sourcing Eval Protocol because standardizing agent evaluation for RL benefits the entire ecosystem. The most valuable AI infrastructure has historically been open source—from our team’s roots at PyTorch to Transformers to RL frameworks. We believe that making agent training accessible and portable across environments will accelerate the maturity of production AI, benefiting researchers, developers, and end users alike.

Real world agent environments are messy, and instrumenting for RL often means figuring out a way to slot in arbitrary trainer-specific code into your production agent. If you’ve felt that most RL tooling assumes an academic “gym” while your agents live in a messy production world, EP is designed for you. We make it easy to:

- **Keep your code where it is.**Wrap it with a remote or CI runner if needed; point EP at your agent so we can observe calls.
- **Write your reward function any way you want.**Use any eval that reflects what success means in your app, from LLM-as-judge to deterministic output.
- **Run, observe, iterate.**Use the local UI to inspect live rollouts and the pivot view to compare models, prompts, and datasets.

That’s “Production RL”: connect the systems you already have, make the environment contract explicit, and let the trace be your ground truth. EP won’t sanitize your world—it meets it as it is and gives you the levers to evaluate and improve agents where they actually live.

Most RL frameworks grew up in “idealistic” settings: sanitized sandboxes with mocked tools, deterministic seeds, and tight reward channels. They look great on paper and make for excellent leaderboards—but they behave more like benchmarks than like the real agentic systems we ship. In production, the world is tangled. The “environment” is a swarm of services; tools call other tools (and sometimes other agents), logs live in a tracing system, and the same piece of code can be both policy and environment depending on where you stand. Untangling agent code from environment code from production scaffolding is hard; even pulling a single truthful trace of what happened can be non‑trivial. That’s the position Eval Protocol (EP) starts from.

We think “Production RL” is the right mental model: less about inventing a new algorithm on a toy gym, more about connecting your existing code and data to reinforcement learning and evaluation with minimal friction. You bring your agents and your realistic environment; EP gives you the contract to run, observe, and score—reliably and repeatably.

Eval Protocol addresses these concerns by offering Day 0 support out-of-the-box with multiple trainers (open- and closed-source) and environment providers. Go from local testing to remote training with the same evaluators and environment, with the flexibility to use the same trainer on future agent use cases.

As part of this launch, we are releasing a set of integrations and examples with various API providers, environment frameworks, and trainers.

- •Frameworks and API Providers - •Any remote server: for example, your agent built on [Vercel](https://github.com/eval-protocol/quickstart/blob/main/vercel_svg_server_ts/api/init.ts)
- •[OpenEnv](https://evalprotocol.io/integrations/openenv-rollout-processor): for running rollouts using environments built with OpenEnv
- •[GitHub Actions](https://evalprotocol.io/tutorial/github-actions-rollout): for running isolated rollouts using your familiar CI platform
- •[Klavis](https://evalprotocol.io/integrations/klavis-mcp): for training agents with reliable MCP servers on Strata

- •Any remote server: for example, your agent built on
- •Trainers:  - •[rLLM](https://evalprotocol.io/integrations/rllm-trainer): a framework for easily training agents with[verl](https://github.com/volcengine/verl)
- •[TRL](https://evalprotocol.io/integrations/trl-trainer): for using the latest post-training techniques like GRPO implemented by HuggingFace
- •[Tinker](https://github.com/eval-protocol/python-sdk/tree/main/eval_protocol/integrations/tinker_cookbook.py): for using Thinking Machine’s distributed training infrastructure
- •[Unsloth](https://evalprotocol.io/integrations/unsloth): for training LLMs with less VRAM
- •[OpenAI RFT](https://evalprotocol.io/integrations/openai-rft-trainer): for training on OpenAI’s closed source models
- •[Fireworks RFT](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models): for easily training and deploying the latest big open source models on the fastest inference engine

- •

In production, an “environment” isn’t a toy gym—it’s the surface your agent actually touches, with all the seams, rate limits, flaky APIs, and human expectations that come with it. From code generation to browser RPA to text-to-SQL, the [range of environments](https://fireworks.ai/blog/state-of-agent-environments) these agents operate in is large, varied, and growing by the day.

Once you can name your environment, you can make a clean promise: how a rollout starts, what counts as an observation, and exactly how success and termination are decided. Everything else—evaluation, learning, iteration—becomes a matter of tightening that contract. The common thread with EP is plug-and-play: bring your environment shape; EP helps you capture the trace and kicks off the scoring loop.

In multi‑turn, tool‑using agents, the only honest source of truth is the **trace**: which model was called, with what messages/tools, what came back, which tool was invoked next, and how it all ended. EP’s magic is in our “trace-first” rollout processors. With the **RemoteRolloutProcessor** and a simple `/init `endpoint, you keep your agent code where it already lives, stream structured logs to tracing, and EP correlates a finished rollout back to the full trace for scoring. EP handles the dotted‑box orchestration and you focus on your business logic. ([evalprotocol.io](https://evalprotocol.io/tutorial/remote-rollout-processor)).

EP tracing also lets you track nested behavior—e.g., when a tool call internally invokes another agent. Because correlation happens through rollout identifiers carried through logs and completions, EP can later reconstruct what actually happened and evaluate that, not a best‑effort re‑simulation.

The early "reward hacking" stories—token repetition ([as discussed by Dwarkesh Patel & Andrej Karpathy](https://www.dwarkesh.com/p/andrej-karpathy)), brittle judges breaking on degenerate strings—left many thinking RL is a minefield of exploits. But today's stronger judge models and better prompts have made cartoonish hacks rare. What's more common now is subtler "doing-the-minimum" behavior where models learn your rubric's edges. The lesson isn't "RL is unworkable," but "treat your evaluators like production code" ([ACL Anthology](https://aclanthology.org/2025.acl-short.20.pdf?utm_source=chatgpt.com)).

EP is designed around that reality. Instead of forcing you into toy environments, it lets your real system be the environment and makes traces the ground truth. You point your agent at EP's blessed URL, keep everything else where it runs, and EP handles orchestration. When finished, you're scoring the same interaction your users experienced—no translation between "eval world" and "product world."

Because the data plane is the trace stream, feedback is not an afterthought. EP writes scores and per‑step signals back onto trace data you see in the local UI (just run `ep logs`). The loop is tight: you watch a rollout live, you notice “lazy” behavior against your rubric, you refine the evaluator prompt or add a structured metric, and you re‑run.

When it’s worth scaling, you keep the contract and change only the where and how—Remote server, GitHub Actions, or a training backend. What matters most over time isn’t a clever trick in the reward model; it’s your **product insight**, encoded as evaluators that capture what “good” means for your users. Write once, run everywhere, so you invest energy in refining rubrics rather than re-plumbing environments.

Get started today [here](https://evalprotocol.io/introduction), and check out our starter video that walks through iterating on the evals inside Eval Protocol with the output from your local agent code.
