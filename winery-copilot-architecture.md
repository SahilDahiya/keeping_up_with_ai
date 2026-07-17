# Winery Ops Copilot — Constellation Architecture (one page)

> **Author:** Sahil Dahiya · *synthesized with Claude Code* · **Created:** 2026-07-15
> **Companion to:** [`PLAYBOOK.md`](PLAYBOOK.md). Original design work — lives outside `kb/`, never scraped.
>
> A concrete architecture for a **staff-facing** winery ops copilot layered on
> Commerce7 / WineDirect (chat, hosted models on **Claude/Bedrock**, on AWS; the agent
> both **answers and acts**). It composes two patterns from the KB:
> **[Sierra's constellation-of-models + supervisors](<kb/models/reasoning/Constellation of models the architecture powering Sierra's agents.md>)**
> as the skeleton, and **[Anthropic's orchestrator fan-out](<kb/agents/multi-agent/How we built our multi-agent research system.md>)**
> as one organ inside it (the read lane).

---

## The governing split: two lanes, decided by one question

> **Is the path knowable, and is a wrong step reversible?**
> **Yes/yes → the model orchestrates (READ lane).  No/no → code orchestrates (WRITE lane).**

```
Staff chat ("why did club signups drop in June?" | "enroll the Johnsons in the Reserve club")
   │
   ▼  ① INPUT SUPERVISOR  — injection / out-of-scope / pasted-untrusted-content   [Haiku 4.5]
   │
   ▼  ② INTENT ROUTER  — classify into a lane + skill                            [Haiku 4.5]
   │
   ├─ READ lane  (analytics / guest / churn — Anthropic fan-out, latency-tolerant)
   │     ORCHESTRATOR [Opus 4.8] decomposes, spawns parallel reads:
   │        ∥ text-to-SQL → read-only warehouse   ∥ guest_360 (Commerce7)
   │        ∥ inventory                            ∥ past campaigns
   │     → synthesize  →  ③ GROUNDING SUPERVISOR (is every claim in the rows?)   [Haiku 4.5]
   │     → typed answer (Pydantic model, e.g. ChurnReport / GuestBrief)
   │
   └─ WRITE lane  (transactional — deterministic state machine, code owns control flow)
         verify entity → build typed action (structured output)  [Sonnet 5]
         →  ④ ACTION SUPERVISOR  (policy + real-impact check)     [code + Haiku 4.5]
         →  ⑤ AUTONOMY GATE  (approval if the action class is Low — see dial)
         → execute with idempotency key → confirm
   │
   ▼  EVERY step traced to Logfire (OpenTelemetry).  Staff thumbs-down → tomorrow's eval case.
```

The READ lane is [Anthropic's mode](<kb/agents/multi-agent/How we built our multi-agent research system.md>):
one open question, too broad for one pass, so **replicate** across parallel reads and
synthesize — the win is coverage. The WRITE lane is the opposite discipline (Playbook
[IX/XI](PLAYBOOK.md)): the steps are **known and irreversible**, so a probabilistic LLM
must never own the sequencing — code does; the model only fills language *inside* a step.

---

## ① The constellation (model-per-task)

Sierra's rule: no single model is fast **and** precise **and** warm **and** long-context at
once, so route each job to the specialist that wins on its binding constraint. Every
assignment is **swappable** (that is the point — [adopt new models per task without touching
guardrails](<kb/models/reasoning/Constellation of models the architecture powering Sierra's agents.md>)).

| Task (job-to-be-done) | Binding constraint | Model (today) | Notes |
|---|---|---|---|
| Intent router / classifier | latency + precision, every turn | **Haiku 4.5** | cheap; fine-tune later on your traffic |
| Analytics orchestrator + synthesis | hardest reasoning | **Opus 4.8** | only fires on the read lane |
| Text-to-SQL generation | correctness, structured | **Sonnet 5** (structured output) | validated + **read-only** connection before run |
| Guest-360 summarization | grounding + typed output | **Sonnet 5** | emits a typed `GuestBrief` |
| Campaign / email drafting | tone, on-brand | **Sonnet 5** + brand voice in context | tone-tuned model later if needed |
| Action-argument extraction | precision, structured | **Sonnet 5** (structured output) | **Pydantic-validated** before any write |
| Offline eval judge | calibrated judgment | **Opus 4.8** | *not in the request path*; calibrated vs humans |

Cost stays sane because the models called *most often* (router, supervisors) are the
*cheapest*, and Opus only fires on genuinely hard reads — Playbook
[XIV](PLAYBOOK.md): [measure per outcome, cheap models where they suffice](<kb/infra-platform/cost/AI spend is the new headcount why cost control is an observability problem.md>).

---

## ② The supervisor set (Sierra's "Jiminy Crickets")

Separate agents that run *alongside* the copilot — each with a defined role, individually
tunable, [independently evaluable](<kb/product-engineering/architecture/From LLMs to enterprise-grade agents.md>).
Supervision doesn't just restrict autonomy — **it is what lets you safely grant more of it.**

| Supervisor | When | Does | Model |
|---|---|---|---|
| **Input** | before routing | detect injection / abuse / pasted untrusted guest content / out-of-scope | Haiku 4.5 |
| **Grounding** | before any answer is shown | reject claims not supported by retrieved rows (catch *fluent-but-wrong*) | Haiku 4.5 |
| **Action / policy** | before any write executes | deterministic allow-list + judge the action's **real impact**, not its surface text | **code** + Haiku 4.5 |

The deterministic boundary comes **first**, the model check second — Playbook
[VIII](PLAYBOOK.md): [contain at the code layer, then steer with classifiers](<kb/product-engineering/security/How we contain Claude across products.md>).
And the supervisors themselves get evaluated — [who monitors the monitors](<kb/evals-observability/monitoring/Who monitors the monitors.md>).

---

## ③ The autonomy dial (per-action, not global)

Sierra's core reframe: shift the goal from "perfect adherence" to **bounded error rates per
action class**, and give the agent the least autonomy exactly where a mistake costs most.

| Action class | Autonomy | Control | Winery example |
|---|---|---|---|
| Read analytics / guest info | **High** | runs freely | "revenue by varietal", "guest history" |
| Draft unsent content | **High** | agent drafts → human reviews before send | campaign copy, guest email |
| Reversible low-stakes write | **Medium** | act + log + easy undo | add a note, tag a guest, create a task |
| Irreversible / money / customer-facing send | **Low** | deterministic gate **+ human approval + idempotency key** | charge a card, enroll a club, **send** a campaign, issue a refund |
| Sensitive / adversarial / bulk-export | **Lowest** | supervisor intercepts → refuse or escalate | anything touching PCI/PII, mass data export, injected content |

*Reads run free; writes stop for a human where it matters* — and the write path is
idempotent so a retry never double-charges a club member (Playbook [IX](PLAYBOOK.md)).

---

## Why these choices (the through-line)

- **Decompose by your binding constraint.** Anthropic's is *coverage* → replicate (read
  lane). Sierra's is *conflicting per-task demands + brand safety* → specialize + supervise
  (the skeleton). Yours is **both**, so you use each where it fits.
- **Code owns control flow for anything irreversible.** The model is creative in the
  moments that don't matter and boxed in the moments that do.
- **The trace is the substrate.** Every step → Logfire; every staff thumbs-down becomes an
  eval case; no change ships without passing the suite (Playbook [I, IV, V](PLAYBOOK.md)).
- **Everything is swappable.** Bedrock + per-task model selection means you ride the model
  frontier down the cost curve without re-architecting.

---

## Thinnest first build (prove the shape before the constellation)

You do **not** build all of this at once. Minimum viable loop:

1. **One model** (Sonnet 5) + **intent router** (Haiku 4.5) — skip the full constellation.
2. **Three read tools** — `analytics_query` (read-only SQL), `guest_360`, `churn_risk`.
3. **One write tool behind the autonomy gate** — `draft_and_send_campaign` (drafts freely,
   *send* requires approval + idempotency).
4. **One grounding supervisor** + **Logfire tracing** from turn one.
5. **A handful of real-data evals + a calibrated judge**, gating deploys.

Then split models per task (the constellation), add the analytics **fan-out** orchestrator,
and add supervisors as the failure modes reveal themselves. *The LLM is the easy part; the
integration + eval loop is the product.*
