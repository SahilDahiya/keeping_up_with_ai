---
title: How Harvey & Fireworks Beat Closed Source on Cost + Quality
topic: agents
subtopic: multi-agent
secondary_topics:
- models/fine-tuning
summary: Case study of using open-source agents with frontier advisors to improve
  cost and quality versus closed-source baselines.
source: fireworks
url: https://fireworks.ai/blog/open-source-agents-frontier-advisors
author: null
published: '2026-06-03'
fetched: '2026-07-11T04:18:26Z'
classifier: codex
taxonomy_rev: 1
words: 1997
content_sha256: 52183babd0b87d240e254b3c26ef001f13e6a1628feb994fb7f0c32764803409
triage: keep
skip_reason: null
---

# How Harvey & Fireworks Beat Closed Source on Cost + Quality

- Combining an open-source agent harness, frontier tool use, and Fireworks-native post-training lifts performance through system-level orchestration.
- The Test
- Open source is competitive on quality, dominant on cost
- A hybrid harness: open-source worker, frontier advisor as a callable tool
- Post-training on Fireworks
- Legal Agent Benchmark
- How LAB scores a model
- Our first step with Harvey in post-training a frontier-scale model

**TL;DR.** We explore two system-level techniques on Harvey’s Legal Agent Benchmark that reduce reliance on single frontier model calls while reaching the frontier-level performance at lower cost.

**Harness engineering**: an open-source GLM 5.1 worker self-triggers Claude Opus 4.7 as a callable advisor on sub-tasks where it improves outcomes, reaching 18 / 100 all-pass at $368 versus 14 / 100 for Opus end-to-end at $954.

**Post-training on Fireworks**: supervised fine-tuning (SFT) of Kimi K2.6 on LAB trajectories reaches 15 / 100 all-pass at $84, while reinforcement fine-tuning (RFT) improves mean score from 0.863 to 0.886 across 46 rollout steps.

Both approaches run on the Fireworks platform used for training and serving, removing the traditional gap between experimentation and production.

“On Fireworks, combining open-source worker models with frontier tool use and post-training closes much of the gap to frontier performance on Legal Agent Benchmark, while improving cost efficiency and system controllability.” — Niko Grupen, Head of Applied Research at Harvey

As a Harvey LAB research partner, Fireworks took an initial 100-task slice and ran it across the most capable open-source and closed-source models, then layered in the two interventions we think the field has been under-investing in: a hybrid harness with an open-source worker and frontier advisor, and Fireworks-native post-training capabilities.

The 100-task slice is a distribution-mirrored subset of the 1,250-task LAB release, preserving the practice-area mix of the full benchmark. This mirrors the sampling approach Harvey used for the Initial Results in the [launch post](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark).

The exercise was necessary because intelligence is jagged: a model that nails frontier mathematics or competitive code generation can still struggle with structured legal drafting, and there is no shortcut around domain-specific evaluation. LAB is the cleanest public lab we know of for the question the industry has been arguing about for two years:

can open-source models do frontier-quality legal AI?

The joint team’s setup runs both halves of the answer on one platform: Fireworks trains, evaluates, and serves on the same infrastructure, so a model fine-tuned against LAB is the same model, bit-for-bit, that serves production traffic. No research-to-production gap to cross.

On LAB’s continuous mean-score metric, GLM 5.1 ranks highest among the open-source models we evaluated, at **0.8921 mean score** putting it directly alongside frontier: Claude Opus 4.7 at 0.911, GPT-5.5 at 0.892. Kimi K2.6 (0.863) and DeepSeek V4 Pro (0.871) come in just below, both still clearly viable for production legal workloads.

On the LAB all-pass metric, the production-readiness measure, the closed frontier holds a small lead: **Opus 4.7 at 14 / 100, GPT-5.5 at 11 / 100, GLM 5.1 at 12 / 100**. That gap is where the rest of this post lives; the two interventions we describe below close most of it.

Cost is the headline. GLM 5.1 reaches its 0.8921 mean for **$121 across the 100-task run**. GPT-5.5’s nearly identical 0.892 costs $560. Claude Opus 4.7’s 0.911 mean and 14 / 100 all-pass runs **$954, roughly 8× any open-source candidate**.

“The customer ask is no longer ‘how do we get the smartest model on every query.’ It is ‘how do we get frontier-quality outputs on the queries that need them, and a model we control on the queries that don’t.’”

A single LLM call is the wrong unit of work for a legal task: reasoning chains run long, citation discipline is unforgiving, and under all-pass grading any missed criterion costs the entire task. To solve the problem, the team built a small, opinionated multi-agent harness with the open-source worker at its core. The configuration is straightforward: open weights at the core, orchestration the team can inspect and tune, and the frontier model invoked as a callable tool rather than a load-bearing dependency.

**A frontier advisor as a callable tool.** Treating Opus 4.7 as an advisor the worker can call on hard sub-tasks unlocked the cost savings on the harness. The GLM 5.1 worker does the bulk of the reasoning, drafting, and tool calls. There is no external router or orchestrator. The worker pulls the advisor in itself, wherever it needs a second opinion: retrieval, drafting, validation. Across the run, the advisor is invoked **just 0.83 times per task on average** — sparse-but-targeted use. That captures most of the quality lift of running the frontier end-to-end, at a small fraction of per-query cost, and it gives us a tunable cost/performance knob: dial advisor calls up on complex matters, down on routine ones.

The harness traces show a recognizable pattern. The worker’s turn count rises meaningfully versus a GLM 5.1-only run: the model reaches an uncertain step (typically during validation, occasionally mid-draft), calls the advisor for guidance or review, then resumes the trajectory with additional turns informed by the response. The advisor is doing less of the writing and more of the steering; the worker is doing the rest of the work it would not have known to do on its own. Sparse advisor calls, denser worker activity downstream of them.

The harness moves GLM 5.1 from **12 / 100 all-pass to 18 / 100 — higher than Claude Opus 4.7’s 14 / 100** — at $368 across the 100 tasks, roughly 39% of Opus’s $954 standalone cost (Figure 1). Against Opus the comparison is clean on both axes: **−$586, +4 tasks all-pass**. Against the GLM-only baseline, the advisor adds **+6 tasks all-pass for +$246** — the cost increase is real, but it is the cost of beating Opus while still running the open-source worker at the core.

Post-training on Fireworks is the model-side counterpart to harness engineering. Where the harness restructures how the model is called at inference time, post-training restructures the model itself, turning a strong open-source base into a domain-specific one. Both experiments we ran on Kimi K2.6 lifted its hold-out scores on the 100-task slice: mean score climbed from a **0.863 base to 0.876 with supervised fine-tuning (SFT) and 0.886 with reinforcement fine-tuning (RFT)**. The Fireworks platform supports the full stack: SFT, [RFT](https://fireworks.ai/blog/frontier-rl-is-cheaper-than-you-think), full-parameter or LoRA, custom loss functions, and dedicated infrastructure, all on the same endpoint the model is served from. (For why that matters in practice — and where most fine-tuning runs actually break — see Fireworks’ [fine-tuning bottlenecks](https://fireworks.ai/blog/fine-tuning-bottlenecks) writeup.) We picked Kimi K2.6 deliberately because at its trillion-parameter mixture-of-experts scale it forces the platform to handle the kind of training we’d actually want to run in production; the engineering required to make that tractable is the subject of Fireworks’ [scaling and optimizing frontier model training](https://fireworks.ai/blog/scaling-optimizing-frontier-model-training) post.

**Supervised fine-tuning (SFT).** The recipe is the simplest one we could think of, partly because the LAB trajectory data was already clean enough to use as-is and partly because we wanted a clean illustration of how much headroom is left on the table when teams stop at prompting. Run Kimi K2.6 through LAB, keep the completions that pass LAB’s rubric criteria (the high-quality trajectories), and drop them into a [Fireworks SFT job](https://docs.fireworks.ai/fine-tuning/fine-tuning-models). No reward model, no human relabeling, no architecture changes. All-pass moved from **11 / 100 to 15 / 100** and mean score from 0.863 to 0.876, at essentially unchanged inference cost ($84 vs. $75 across the 100-task run). Four extra tasks fully passing, with no other change in the stack — Figure 1 plots that SFT shift alongside the harness configurations and the closed-source baseline.

**Reinforcement fine-tuning (RFT).** RFT trains against the LAB evaluators directly, with per-criterion rewards instead of just imitating passing trajectories. It is the natural follow-on when SFT starts to plateau. We ran RFT on a different sample of the training set than the SFT run, with the same Kimi K2.6 base. The signal at each rollout step is the 100-task mean score on the LAB eval set, evaluated continuously during training. Across 46 rollout steps the smoothed mean score climbs from **0.82 at the start to 0.886 at the final step**, jumping from 0.864 to 0.882 between steps 43 and 44 to clear both the Kimi K2.6 base (0.863) and the SFT checkpoint (0.876) in a single step. RFT is noisier and more compute-intensive than SFT, but by step 46 it picks up exactly the criteria SFT alone leaves on the table.

The two experiments together demonstrate something more important than either result alone. Fireworks handles full post-training at the parameter scale of Kimi K2.6 on dedicated infrastructure, with a [bit-for-bit handoff](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) to the serving endpoint, on the same platform from prompt to checkpoint to production. The model that ships is the model that came off the training run — no numeric drift between training and serving, no second deployment pipeline, no research-to-production gap. The numeric-alignment work behind that handoff (where most platforms quietly lose accuracy) is detailed in Fireworks’ [MoE numerics post](https://fireworks.ai/blog/when-faster-not-identical-moe-numerics).

“The frontier model shows up as a callable tool, not as the dependency the product is built on top of.”

Harvey recently open-sourced [Legal Agent Benchmark (LAB)](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark), a suite of 1,250 tasks across 24 practice areas with 75,000+ expert-written rubric criteria. Each task is a partner-style instruction over a client-matter environment with a required deliverable and a rubric. LAB builds on Harvey’s earlier [BigLaw Bench](https://www.harvey.ai/blog/introducing-biglaw-bench) work and extends it from short-horizon Q&A into the long-horizon, multi-document, citation-disciplined tasks that legal practice actually looks like.

LAB uses two metrics. **Mean score** is the share of rubric criteria a model passes, averaged across the suite. A 0.90 mean means the model is hitting roughly nine out of every ten criteria. [ All-pass](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark#evaluating-a-task) is strict: a task counts only when every criterion in its rubric passes. It is LAB’s grading metric for production-readiness, because a deal-team report that catches eight of ten risks is not 80% useful, it is materially incomplete.

“A deal-team report that catches eight of ten risks is not 80% useful, it is materially incomplete.”

The two tell different stories about the same model. A high mean with low all-pass is a generally strong model that fails the long tail of strict criteria. A small mean lift with a large all-pass jump is a model that learned to close tasks out cleanly. We report both throughout, because each lever we pulled moves them differently.


The 100-task slice is a snapshot. The joint team is already scoping the next set of experiments:

- •**Improved post-training on the best open-weights models**— we’re exploring ways to further improve the post-training of the leading open-weights models (Kimi K2.6, GLM 5.1, DeepSeek V4 Pro) on LAB via more informative reward modeling and enhanced training techniques.
- •**Harness engineering**— extending the advisor mechanic to more practice areas, and studying whether the worker’s turn-count expansion (the behavioral pattern above) is the right lever to tune, or whether smaller specialized open-source models can sit alongside the worker for sub-tasks the advisor is currently absorbing. We’re also looking at context compaction between turns as a cost-and-quality lever at LAB trajectory lengths.

The shared thread is the platform. Both efforts, like the training and harness in this post, run on the same Fireworks endpoint that serves the model in production. That bit-for-bit handoff is what makes the loop tractable: a model team can fine-tune, evaluate against LAB, and ship the result without crossing a research-to-production gap. Everything we ship next will run through the same loop.

The pattern that won on LAB is straightforward: open weights at the core, frontier intelligence called in only where it changes the answer.

Note: Cost figures throughout are estimates based on current serverless rates — Fireworks for open-source models (GLM 5.1, Kimi K2.6, DeepSeek V4 Pro), and published API rates from Anthropic (Claude) and OpenAI (GPT). Numbers reflect total inference cost on the 100-task slice and will move with token mix and rate changes.
