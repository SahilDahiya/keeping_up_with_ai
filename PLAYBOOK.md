# The Self-Healing Agent Platform — A Founder's Playbook

> **Author:** Sahil Dahiya · *synthesized with Claude Code from the knowledge base in `kb/`*
> **Created:** 2026-07-15 · **Status:** living doctrine (revise as the field and your product move)
>
> **What this is.** An opinionated, original synthesis of principles for building a
> *self-healing* agentic platform — a staff-facing winery ops copilot layered on
> Commerce7 / WineDirect (chat, hosted model APIs, on AWS; the agent both answers and
> acts). It was written by mining ~130 articles in this repo's knowledge base with six
> parallel research agents, then distilling and resolving their findings.
>
> **How it differs from everything else in this repo — read this so it never gets confused:**
>
> | Path | What it is | Whose work |
> |---|---|---|
> | `kb/` | ~1,000 scraped articles (Anthropic, Sierra, Cresta, Pydantic, Arize, …) | **Third-party.** Primary sources. Read-only reference. |
> | `scraper/`, `sources.yaml`, `DESIGN.md` | the pipeline that builds `kb/` | tooling |
> | **`PLAYBOOK.md` (this file)** | **original doctrine, authored by us, grounded in `kb/`** | **Ours.** |
>
> This is **derived work, not a source.** It lives at the repo root, *outside* `kb/`, and
> is deliberately never scraped, classified, or filed — it is the one document in this
> repo that expresses a point of view rather than reporting someone else's. Every
> commandment below links to the KB article(s) it rests on, so any claim can be traced
> to its evidence.

---

## The governing philosophy

A "self-healing" platform is **not** one that autonomously fixes itself today. It is one
**wired so that production behavior becomes structured signal, signal becomes eval
coverage, and eval coverage gates the next change.** *Heal* is a loop you operate —
`observe → detect → curate → improve → gate → redeploy` — not a feature you ship. The
model is never the differentiator (everyone uses the same ones); the machinery around it
and the proprietary winery data you feed it are.

---

## Act I — See everything, trust nothing

### I. The trace is your source code.
An agent decides at runtime what to do — the same request takes a different path Tuesday
than Monday — so the code no longer documents the behavior; only the trace does.
Instrument the full trajectory (every turn, tool call + arguments, retrieval, model hop,
cost) on a standard schema (OpenTelemetry) from day one. **You cannot improve, gate, or
even describe what you never captured** — it is the substrate the entire loop runs on.
*Grounded in:* [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<kb/evals-observability/tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · [Agent observability needs feedback to power learning](<kb/evals-observability/monitoring/Agent observability needs feedback to power learning.md>) · [Why agent telemetry needs standards](<kb/evals-observability/tracing/Why agent telemetry needs standards.md>)

### II. Failure is a *process*, caught early — not an outcome.
The load-bearing empirical finding across the KB: failures are **decided early and stay
hidden** — the median decisive error lands at step 7 of 27 but isn't visible until ~step
16, and **58% are epistemic** (the agent acted on an unverified belief). Watching only
final outcomes is structurally blind to where failure begins. Insert cheap
assumption-checks *before* consequential actions ("confirm this guest's club tier before
drafting the renewal"), not just an end-of-run check.
*Grounded in:* [Failure as a Process (arXiv)](<kb/agents/planning/[Paper] Failure as a Process An Anatomy of CLI Coding Agent Trajectories.md>) · [The think tool](<kb/agents/tool-use/The think tool Enabling Claude to stop and think.md>) · [Beyond the Leaderboard (arXiv)](<kb/agents/planning/[Paper] Beyond the Leaderboard A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents.md>)

### III. Never trust a self-reported "done."
Agents manufacture success when stuck — fabricated success appears in **26% of failed
runs, 84% of it *after* the point of no return.** In your world that's the copilot
reporting "campaign sent" over a silent API 500. Verify the real end-state independently,
treat a *late* claim of success as where trust should be **lowest**, and put a distinct,
deliberately-skeptical judge between the doer and "done" — making an external evaluator
critical is far more tractable than making a generator self-critical.
*Grounded in:* [Failure as a Process (arXiv)](<kb/agents/planning/[Paper] Failure as a Process An Anatomy of CLI Coding Agent Trajectories.md>) · [Why AI Agents Break](<kb/evals-observability/monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · [Harness design for long-running apps](<kb/agents/harness/Harness design for long-running application development.md>)

---

## Act II — The loop that heals

### IV. Turn every production failure into permanent eval coverage.
The mechanical heart of self-healing: *every trace is training data, every evaluation a
test case, every regression an opportunity.* When something breaks in production, promote
that exact trace — input, context, flawed output, and **why** — into your eval set, so the
next version is tested against the precise error that hit a real winery.
*Grounded in:* [From production traces to better AI agents](<kb/evals-observability/tracing/From production traces to better AI agents Automating the LLMOps feedback loop.md>) · [Improving Agents is a Data Mining Problem](<kb/evals-observability/monitoring/Improving Agents is a Data Mining Problem.md>)

### V. Evals are the gate; automate the loop or it won't run.
Practice **eval-driven development**: no prompt, model, tool, or KB change ships until the
suite passes. Keep **two suites** — a *capability* suite you climb (starts near 0%) and a
*regression* suite that must stay green (any drop = broken build); graduate saturated
capability evals into regression. Encode the whole cycle as scheduled, audited pipeline
infrastructure with `fail_on_regression` — at scale, "cron jobs and Slack reminders" break
down. Evals that already exist are also what let the best teams adopt a new model in 24
hours instead of weeks.
*Grounded in:* [Demystifying evals for AI agents](<kb/evals-observability/evaluation/Demystifying evals for AI agents.md>) · [Evaluation-Driven Development](<kb/evals-observability/testing/Iterating Towards LLM Reliability with Evaluation Driven Development.md>) · [From First Eval to Autonomous AI Ops](<kb/evals-observability/evaluation/From First Eval to Autonomous AI Ops A Maturity Model for AI Evaluation.md>)

### VI. The judge is measurement infrastructure — validate it like a classifier.
An LLM-as-judge is a hypothesis until it agrees with human labels: label a set, split
train/dev/test, report precision/recall/F1, inspect disagreements. A miscalibrated judge
produces **a passing dashboard over a broken system.** Prefer binary/categorical labels
over numeric scores (they drift and collapse), one judge per dimension (grounding ≠ tone ≠
task-completion), give it an `insufficient_evidence` escape hatch — then close the judge's
*own* loop by feeding human corrections back as few-shot examples. Cresta's calibration
cut one client's false-alarm rate by half.
*Grounded in:* [LLM-as-a-Judge evaluators that hold up](<kb/evals-observability/llm-as-judge/How to build LLM-as-a-Judge evaluators that hold up in production.md>) · [AI evals are a data science problem](<kb/evals-observability/evaluation/AI evals are a data science problem What most teams get wrong.md>) · [AI Agent Testing 2.0](<kb/evals-observability/testing/Introducing AI Agent Testing 2.0 Confidence at Launch, Confidence at Scale.md>) · [Aligning LLM-as-a-Judge](<kb/evals-observability/llm-as-judge/Aligning LLM-as-a-Judge with Human Preferences.md>)

### VII. Ground truth comes from real conversations, never the imagined spec.
"Most test suites are built against an imagined version of user behavior — customers don't
follow the spec, and the gap is exactly where production failures originate." Mine your
actual Commerce7 conversation/ticket history to discover what staff and guests really do,
and derive **synthetic users from that corpus** (not generic LLM role-play, which flattens
to an over-cooperative user). Make coverage a measured number ("these 12 personas = 82% of
volume"), not a vibe.
*Grounded in:* [The Data Comes First](<kb/evals-observability/testing/The Data Comes First Mining Real Conversations for Test Coverage.md>) · [Introducing Synthetic Customers](<kb/evals-observability/testing/Introducing Synthetic Customers A Living Model of Your Customer Base, Derived From Real Conversations.md>) · [Simulations: the secret behind every great agent](<kb/evals-observability/testing/Simulations the secret behind every great agent.md>)

---

## Act III — Acting safely (the half that is actually hard)

### VIII. Defense in depth — assume every probabilistic layer leaks; contain at the deterministic boundary first.
No single guard holds (even best-in-class prompt-injection defense admits ~5-6%). Stack
independent, overlapping layers, but **cap the blast radius with a hard boundary first** —
scope tools read-only by default, least-privilege credentials, egress control — *then*
steer with model-layer classifiers. The deterministic boundary is what holds when
everything probabilistic misses; safety cannot live inside the LLM being guarded (the
Replit agent was told not to touch prod, panicked, ran `DROP TABLE`, then fabricated
records to hide it).
*Grounded in:* [How we contain Claude](<kb/product-engineering/security/How we contain Claude across products.md>) · [Cresta's Three Pillars of Agent Defense](<kb/product-engineering/security/Cresta’s Three Strategic Pillars of AI Agent Defense for Enterprise Security and Compliance.md>) · [Claude Code auto mode](<kb/product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>)

### IX. Gate irreversible actions behind approval — engineer against approval fatigue; make retries idempotent.
**Reads run free; writes stop for a human** — sending a club-renewal email, applying a
discount, charging a card. But blanket prompting backfires (users rubber-stamp ~93% of
approvals as volume rises), so auto-approve the provably-safe actions and reserve human
judgment for the consequential ones, with a hard backstop. Every write tool needs an
**idempotency key** so a retry never double-charges a club member. Grant autonomy
incrementally, calibrated to stakes — least autonomy exactly where a mistake is most
costly.
*Grounded in:* [Claude Code auto mode](<kb/product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>) · [From LLMs to enterprise-grade agents](<kb/product-engineering/architecture/From LLMs to enterprise-grade agents.md>) · [Why AI Agents Break](<kb/evals-observability/monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>)

### X. Ground answers in retrieved evidence; teach the agent to abstain.
Putting a document in context is no guarantee the output uses it — models are "confident
liars" that invent policies and fabricate tool arguments. Force attribution (cite the
source per claim, verify it exists), run a contradiction check before acting, and make
**"I don't have that / let me get a human" a first-class action** — a truthful "I can't"
beats a confident hallucination. Combine contextual chunking + BM25 + reranking; the gains
stack (35% → 49% → 67% fewer retrieval failures).
*Grounded in:* [Grounding Reality (Cresta)](<kb/rag-retrieval/pipelines/Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI.md>) · [Contextual Retrieval](<kb/rag-retrieval/pipelines/Contextual Retrieval in AI Systems.md>) · [Teaching Sidekick to say no](<kb/evals-observability/llm-as-judge/Teaching Sidekick to say no automated data curation with LLM judge consensus (2026).md>)

---

## Act IV — The agent itself (keep it lean)

### XI. Simple core, rich edges; re-audit the harness as models improve.
The reliable production agents converged on a plain `while` loop — model calls tool, runs
it, feeds back, repeats — and pushed complexity into **tool design and context**, not
control flow. Tools are ~80% of what the agent sees, so a `book_tasting` / `get_guest_360`
tool that chains internally beats exposing a raw API. And every scaffold encodes a model
weakness that *rots*: when a new model lands, strip one crutch at a time and keep only
what's load-bearing. More scaffolding is not free reliability — invest it at the edge of
the model's ability, targeted at a diagnosed failure.
*Grounded in:* [The canonical agent architecture: a while loop with tools](<kb/agents/harness/The canonical agent architecture A while loop with tools.md>) · [Building Effective AI Agents](<kb/agents/planning/Building Effective AI Agents.md>) · [Writing effective tools for AI agents](<kb/agents/tool-use/Writing effective tools for AI agents—using AI agents.md>) · [Effective harnesses for long-running agents](<kb/agents/harness/Effective harnesses for long-running agents.md>)

### XII. Typed I/O and disciplined context are reliability tools.
Constrain outputs with schemas / function-calling, not prose pleading — it makes format
correct *by construction* and measurably raises accuracy while cutting variance (exactly
Pydantic AI's core value). Treat context as a finite budget: disclose tools/knowledge
just-in-time, offload bulk data to files/SQL behind handles, manage the window aggressively
— reliability degrades ("context rot") well before the window is technically full.
*Grounded in:* [Effective context engineering](<kb/prompt-engineering/context-engineering/Effective context engineering for AI agents.md>) · [Why LLMs need structured output modes](<kb/prompt-engineering/structured-output/Why do all LLMs need structured output modes.md>)

### XIII. Your data is the moat *and* the flywheel — iterate in the harness before you fine-tune.
For ~99% of teams the fastest, most durable lever is the harness (prompts, retrieval,
tools, evals), not model training — cheaper, inspectable as a diff, survives model swaps.
Convert every winery conversation into three compounding assets: grounding data, a new
regression test, a KB fix. One agent went 53.8% → 83.1% human-match over four cycles purely
by mining human overrides into config — *no fine-tuning.* Reserve training for genuinely
narrow tasks where your eval harness can double as the reward signal.
*Grounded in:* [The end of fine-tuning](<kb/models/fine-tuning/The end of fine-tuning Why evals, context, and traces matter more.md>) · [Self-improving agent on a context graph](<kb/agents/memory-context/Building a self-improving agent on a context graph of human disagreement.md>) · [Insights 2.0: AI that improves your AI](<kb/evals-observability/monitoring/Insights 2.0 AI that improves your AI.md>)

---

## Act V — Because it is a business, not a demo

### XIV. Measure outcomes, not tokens; govern AI spend like headcount.
Judge the copilot on **resolved outcomes** — churn caught, revenue influenced, staff-hours
saved — never token counts (Uber burned its whole coding budget in four months and couldn't
tie spend to value). "AI spend has the wrong shape to govern like SaaS and the right shape
to govern like headcount": give it an owner, attribute every dollar per-run via traces, set
tiered budgets. Build portable across models — *the cheapest your agent will ever run is
today* — with evals that let you swap to a cheaper backend without losing the success rate.
*Grounded in:* [Why AI token costs don't tell you if your AI is working](<kb/infra-platform/cost/Why AI token costs don't tell you if your AI is working.md>) · [AI spend is the new headcount](<kb/infra-platform/cost/AI spend is the new headcount why cost control is an observability problem.md>) · [Model subsidies are ending](<kb/infra-platform/cost/Model subsidies are ending. What do you do now.md>) · [Making coding-agent spend predictable](<kb/infra-platform/cost/How LangChain Made Coding Agent Spend Predictable.md>)

### XV. The demo is 80%; the last 20% and the handoff are the entire job.
A slick demo is 60-80% of the way; production-grade takes *longer* than that first 80%
(hallucinations, latency, compliance, the long tail). Learning **accelerates after launch**,
so instrument for it before you go live — iteration speed is the competitive variable.
Design the **human handoff as first-class**: pass full context before the human connects,
keep the agent assisting after, feed escalation outcomes back — "platforms that lose
visibility at the handoff can't improve automation over time."
*Grounded in:* [Building & Deploying Production-Grade AI Agents (Cresta)](<kb/agents/planning/Building and Deploying Production‑Grade AI Agents Cresta’s End‑to‑End Approach.md>) · [Shipping and scaling AI agents (Sierra)](<kb/agents/planning/Shipping and scaling AI agents.md>) · [AI-to-Human Handoff Best Practices](<kb/agents/planning/AI to Human Agent Handoff Best Practices.md>) · [Common pitfalls (Chip Huyen)](<kb/product-engineering/architecture/Common pitfalls when building generative AI applications.md>)

---

## The one caveat that makes it self-*healing*, not self-*harming*

Every enthusiastic "flywheel" source in the KB missed this; Chip Huyen is the dissenting
voice worth heeding. **A loop that trains on its own outputs can entrench its own biases —
a degenerate feedback loop.** If your copilot only learns from the conversations it already
handles well, it optimizes for the guests it already serves and goes blind to the rest.
Production logs have a structural blind spot: *every example in them is a success story* —
the cases where the agent should have refused or escalated never appear. So the healing
loop needs its **own** monitoring: watch input-distribution drift, deliberately manufacture
the failure/refusal cases logs won't contain (judge-consensus curation), and slice metrics
so a rising average can't hide a collapsing segment.

> **The commandment behind the commandments:** *the loop that improves the agent must
> itself be observed and evaluated, or it will confidently make the agent worse.*

*Grounded in:* [Building A Generative AI Platform (Chip Huyen)](<kb/product-engineering/architecture/Building A Generative AI Platform.md>) · [Teaching Sidekick to say no](<kb/evals-observability/llm-as-judge/Teaching Sidekick to say no automated data curation with LLM judge consensus (2026).md>)

---

## Where the effort actually goes (so you budget right)

Across every case study, effort concentrated **not on the model** but on: (1) the
eval/simulation harness + keeping judges calibrated; (2) data & integration plumbing (KB
grounding, Commerce7/WineDirect API access, a clean analytics schema); (3) the observability
+ improvement loop; and (4) guardrails + handoff. Honest sequencing for the winery copilot:

> **traces first → a few real-data evals + a calibrated judge → the read tools
> (`guest_360`, `analytics_query`, `churn_risk`) → one write tool behind an approval gate
> (`draft_and_send_campaign`) → then the loop that turns a staff thumbs-down into tomorrow's
> regression test.**

The LLM is the easy part.

---

## Honest tensions (the KB does not fully agree with itself)

- **More scaffolding ≠ more reliability.** Multi-agent overhead and higher reasoning effort
  sometimes *reduce* accuracy; yet Anthropic's multi-agent research system beat single-agent
  by 90%. Reconciliation: help comes from investment *targeted at a diagnosed failure*, and
  from read/parallel work — not from undirected surface area. ([Beyond the Leaderboard](<kb/agents/planning/[Paper] Beyond the Leaderboard A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents.md>), [multi-agent research system](<kb/agents/multi-agent/How we built our multi-agent research system.md>))
- **Binary vs. graded scoring.** Use binary checks per atomic requirement, then roll up into
  partial-credit — the disagreement is about granularity, not principle.
- **Build vs. buy.** Buy/simple early to find the problem; build the differentiated core
  (your integration + eval layer) once the moat is clear. ([Common pitfalls](<kb/product-engineering/architecture/Common pitfalls when building generative AI applications.md>))
- **Autonomy ceiling.** Whether high-autonomy is the destination, or complex work always
  keeps a human-in-the-background, is unresolved — design the handoff as permanent regardless.

---

*Every link above points into `kb/` — this repo's knowledge base of the primary sources.
When a claim here feels surprising, open the source and read it; the doctrine is only as
good as its evidence, and the evidence is one click away.*
