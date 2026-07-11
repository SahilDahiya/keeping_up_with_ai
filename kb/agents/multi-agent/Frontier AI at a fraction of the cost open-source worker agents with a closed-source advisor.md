---
title: 'Frontier AI at a fraction of the cost: open-source worker agents with a closed-source
  advisor.'
topic: agents
subtopic: multi-agent
secondary_topics:
- models/reasoning
summary: Explains a worker-advisor pattern that combines open-source worker agents
  with closed-source advisors for cost-quality tradeoffs.
source: fireworks
url: https://fireworks.ai/blog/frontier-open-source-worker-with-closed-source-advisor
author: null
published: '2026-06-24'
fetched: '2026-07-11T04:17:52Z'
classifier: codex
taxonomy_rev: 1
words: 1423
content_sha256: 98fdbe8e80df9690769fee265fa599fd0cc4fcb0debc75b8d3c293006e31830e
triage: keep
skip_reason: null
---

# Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.

**A simple worker + advisor setup produces better outcomes at lower cost.**

An open-source worker (Kimi-K2.6 / GLM-5.2) that calls a closed-source frontier model (Claude Opus 4.8) once per task as an advisor, **raises the success rate in every cell** across three benchmarks studied, while doing so at a fraction of the cost.

- •**Consistent lift:**+4 (Kimi) / +7 (GLM) pp on SWE-bench Pro; +8 / +4pp Terminal-Bench 2.1; and +1 / +4 pp on Legal Agent Benchmark.
- •**Frontier quality or better, far cheaper.**GLM-5.2 + advisor matches Opus run as the worker on Terminal-Bench (≈80%) at ~half the cost ($3.50 vs $6.61/task), beats it on Legal Agent Bench at ~40% lower cost, and captures most of the frontier on SWE-bench Pro at ~3× lower cost.

Two roles, one tool.

The open-source worker runs the task end to end (implement → review → revise); at the single review step it consults a read-only frontier advisor, then produces the deliverables.

- •**Worker**— an open-source model (Kimi-K2.6 / GLM-5.2) drives the task end to end: reads the problem, edits files, runs commands, verifies its own work.
- •**Advisor**— a frontier model (Opus 4.8) exposed to the worker as a single**review**consult. It cannot edit files. It reads the worker’s trajectory-so-far plus the working diff and returns an assessment with concrete pass/fail checks.

There is no external router or orchestrator. **The worker decides when to consult the advisor, **after it has done the work and run its own verification. The advisor audits what was actually done — it sees the diff — and flags gaps the worker missed. The worker receives the feedback and does additional work if needed. The result is a pattern of **sparse advisor calls, denser worker activity upstream and downstream.** The advisor is **pure brain with no hands**. Everything expensive — writing, running, iterating — stays on the open-source worker.

Resolve rate over graded tasks (see Method notes). Worker baselines are the same model with no advisor; advisor = Opus 4.8, effort = medium. The Legal benchmark is harder where task resolved = all criteria pass, over all 100 tasks, so its absolute numbers run lower.

| Benchmark + worker | Baseline | with Advisor | Uplift |
|---|---|---|---|
| SWE-bench Pro + Kimi-2.6 | 55% | 59% | +4 pp |
| SWE-bench Pro + GLM-5.2 | 59% | 66% | +7 pp |
| Terminal-Bench 2.1 + Kimi-2.6 | 64% | 72% | +8 pp |
| Terminal-Bench 2.1 + GLM-5.2 | 76% | 80% | +4 pp |
| Legal Agent Bench + Kimi-2.6 | 8% | 9% | +1 pp |
| Legal Agent Bench + GLM-5.2 | 12% | 16% | +4 pp |

**The lift is positive  using a single setup with no per-model or per-benchmark tuning** — across three task types (software engineering vs. terminal/ops vs. legal work) and two open-source workers. This robustness to task type and to worker model makes the advisor setup deployable at scale. Notably, GLM-5.2 + advisor reaches **parity-or-better with Opus run as the worker on 2 of the 3 benchmarks. **It matches on Terminal-Bench and beats on Legal, both at a fraction of the cost. This confirms and extends the findings from our [previous research](https://fireworks.ai/blog/open-source-agents-frontier-advisors) shared in partnership with the team from Harvey AI.

A few disclosure caveats: with only 60–100 tasks per cell, a one-task swing is ~1–1.8 pp, so cell directions are solid and exact magnitudes are subset estimates. The Opus/GLM-5.2 Terminal-Bench tie (80.5 vs 79.5) is within sampling noise and should be read as parity, not a win. Additionally, the Legal Agent Benchmark with Kimi-K2.6 + advisor cell (+1 pp, one task) is likewise within noise and so should also be read as flat, not a lift.

We plot three operating points per benchmark: the open-source worker alone, the open-source worker + Opus advisor, and the frontier model run as the worker (Opus, no advisor).

Figures 1–3 Below: x = inference cost per task (USD), y = resolve rate.

For each worker, the dashed line goes base → + advisor; the red square is Opus run as the worker (4.8 on SWE/Terminal, 4.7 on Legal).

The detailed cost breakdown below. The lessons are clear:

- •**Open source + advisor reduces spend across the board**. Every cell undercuts Opus-as-worker — 19% to 67% cheaper.
- •**The win compounds with GLM quality.**GLM beats Kimi on quality, advisor spend, and savings all at once.

| Benchmark + worker | Opus 4.8 (frontier) | Open-source + advisor (worker + advisor) | Savings vs Opus |
|---|---|---|---|
| SWE-bench Pro + Kimi-2.6 | $18.28 | $6.13 ($4.02 + $2.11) | 66% |
| SWE-bench Pro + GLM-5.2 | $18.28 | $6.09 ($4.64 + $1.45) | 67% |
| Terminal-Bench 2.1 + Kimi-2.6 | $6.61 | $4.11 ($2.70 + $1.41) | 38% |
| Terminal-Bench 2.1 + GLM-5.2 | $6.61 | $3.50 ($2.20 + $1.30) | 47% |
| Legal Agent Bench + Kimi-2.6 | $9.54 | $7.73 ($5.35 + $2.38) | 19% |
| Legal Agent Bench + GLM-5.2 | $9.54 | $5.74 ($5.03 + $0.71) | 40% |

**Plan+review vs. review-only: is it better to call the advisor once or multiple times? **We tested a stronger version of the advisor harness, where we instruct the agent to consult the advisor twice: a plan call before building, plus the review call before finishing. The verdict: review-only is **as good or better in 5 of 6 (benchmark × worker) experiments. **It is distinctly better on Terminal-Bench (Kimi-K2.6 72% vs. 63%) at roughly **half the advisor calls** (≈1 vs. ≈2 per task). In short, the additional plan call doesn’t pay for itself.

**Does the reviewer have to be the frontier?** Run GLM-5.2 as both worker and reviewer: a same-model reviewer **reproduces the frontier advisor’s lift on neither benchmark** — flat on SWE-bench (58% vs. 59% base, vs. frontier-advised 66%) and worse on Terminal-Bench (72% vs. 76% base, vs. frontier-advised 80%). The judgment the frontier reviewer supplies is exactly what the open model can’t supply about its own work — so the reviewer has to be the frontier. The Legal benchmark sharpens it: GLM-5.2 self-review is again flat (12→12%), and a same-tier GLM-5.2 reviewer over a different open worker (Kimi-K2.6) actively **degrades** it (8→6%) where the frontier reviewer is neutral-to-positive (8→9%).

**Advisor effort: medium is the default.** Medium vs. high advisor effort lands within one task (SWE-bench: Kimi 34 vs. 35, GLM 36 vs. 35) — cheaper and faster at no quality cost.

This six-cell sweep is a snapshot. The natural next steps:

- •**More task types and models.**Code and ops are two regimes; further agentic domains (data analysis, web, longer workflows) and newer model tiers, to confirm the uplift holds as both the open and frontier tiers advance.

The advisor is open-sourced as a single self-contained file in the Fireworks cookbook: ** github.com/fw-ai/cookbook/tree/main/advisorbook/advisor**.

Two roles: an open-source (GLM-5.2) **worker on Fireworks** does the task; a **frontier reviewer (Claude)** reviews its diff before it finishes.

12345

Then add one line to your agent’s instructions (CLAUDE.md / AGENTS.md) so it consults the advisor before finishing.

Full walkthrough in the [README](https://github.com/fw-ai/cookbook/tree/main/advisor).

- •**Benchmarks.**SWE-bench Pro (cais/swebenchpro), a stratified 60-task subset over 11 repos (≈8% of the 731-task set);**Terminal-Bench 2.1**, 84 text tasks;**Legal Agent Benchmark**, 100 expert-authored legal tasks (Harvey), scored as**all-criteria-pass over all 100 tasks**(every sub-requirement must pass — a stricter bar than the SWE/TB resolve rate, hence the lower absolute numbers), judged by Kimi-K2.6. We also ran GLM 5.1 as judge model and got comparable results, ruling out same-family scoring bias. Opus as worker on Legal is 4.7 (4.8 scored lower on the subset); Legal per-task cost is uncached and scaled to a measured Kimi-K2.6 baseline.
- •What the review call actually says: The whole mechanism is one prompt, and the exact wording is the design. **The review call is a skeptic, not a cheerleader.**It is told to distrust the worker — both its framing and its prose. e.g.

“do NOT accept the agent’s framing, arithmetic, or boundaries … … Verify claimed edits against theworktree, not the agent’s prose… … Confidence: score each issue 0–100.”

Two choices do the work.

- **Calibrated confidence**(only ≥80 becomes “critical”) keeps the advisor from drowning a working solution in nitpicks the worker would waste turns chasing.
- And **auditing the diff, not the narrative**, means the worker cannot talk its way to “done”: the advisor reads git diff as ground truth and marks each check as`PASSING / FAILING / NOT IMPLEMENTED / DEVIATED`. The worker then fixes what’s flagged and finishes.
