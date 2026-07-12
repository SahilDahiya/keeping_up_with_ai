---
title: 3 production patterns for AI agents and how to evaluate each one
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/evaluation
summary: Breaks production agents into local coding agents, in-app assistants, and
  operational agents, then maps each pattern to different harness, rollout, and evaluation
  needs.
source: arize
url: https://arize.com/blog/3-production-patterns-ai-agents-how-to-evaluate-each-one/
author: Sara Verdi
published: '2026-07-10'
fetched: '2026-07-11T04:41:26Z'
classifier: codex
taxonomy_rev: 1
words: 1857
content_sha256: 88fea30c8a52d68cf8378380b968a21c2c2bbd18e9a2c0edfda1151ff34fdd1f
---

# 3 production patterns for AI agents and how to evaluate each one

You have probably built an agent, but shipping one is a different job.

A local coding agent, an in-app customer assistant, and an AI SRE triaging production logs may all use the same model class. But they don’t have the same harness, eval plan, rollout risk, or failure modes. The useful distinction is not “agent vs. no agent”—it’s which kind of production agent you are building.

That framing comes from a talk by [Sam Bhagwat](https://www.linkedin.com/in/sambhagwat/), CEO and founder of [Mastra](https://mastra.ai/), at [Arize Observe 2026](https://www.youtube.com/watch?v=m0mS7lLLDaw). Drawing on thousands of teams moving from prototype to production, Sam’s point was simple: everybody’s talking about agents—the real question is what kind. This post walks through Mastra’s view of a production agent stack, the three patterns that most often make it into production, and the practical risks each one tends to hit first.

## Mastra’s view of a production agent stack

Before we jump into the pattern table, it helps to name what Mastra thinks production work actually is.

According to Sam, when you build an agent, you are solving two problems at once. One is the primitives—the agent loop, workflows, harness, sandboxes. The other is the features you need to ship to users. Teams that reinvent the primitives on every project move slower. Mastra’s view is to give you those primitives out of the box so you can spend the cycle on product:

| Layer | What Mastra means by it in production |
|---|---|
| Agents | Typed agents with instructions, models, tools, and runtime behavior in one place |
| Workflows | Multi-step orchestration with branching, parallelism, and human-in-the-loop pauses |
| Memory | Conversation history plus retrieval from APIs, databases, and files |
| Harness | Tools, permissions, sandboxes, and guardrails that keep runs bounded |
| Evals | Scorers and repeatable checks on agent runs before and after changes ship |
| Observability | Traces, metrics, token use, and datasets on each run |
| Deployment | Standalone server, embedded app, or Mastra Server as a production API |

## Pick your production pattern

Before you write another prompt, decide which bucket you’re in. Your harness, eval plan, and rollout strategy all depend on it.

| Production agent pattern | Who builds it | Typical use cases | First production risks |
|---|---|---|---|
| Customer-facing | Product teams | In-app assistants, copilots, support agents | Inference cost at scale, incomplete pre-launch evals |
| Internal enterprise | Platform or ops teams in large orgs | Enterprise search, process automation | Org friction, fragmented data systems |
| Developer platform | Infra / platform engineering | AI SREs, blessed internal agent platforms | Governance, standardizing harness primitives |

**Tip:** Not sure which category you fall under? You can ask these questions:

- **Are real users (not employees) the customer?**Customer-facing
- **Are you automating internal workflows at org scale?**Internal enterprise
- **Are you building the stack other developers will ship agents on?**Developer platform

## If you are building a customer-facing agent

From Mastra’s side of the room, this pattern is context engineering more than model shopping. Your users want an in-app agent that understands their account, their data, their workflow. Frontier models are increasingly good at general reasoning, but they do not automatically know your product state, customer permissions, account history, or workflow constraints. Sam’s line from Observe: consumer models go off the rails not because they’re bad at reasoning, but because they don’t have access to the right context. So your job isn’t picking a smarter model—it’s feeding the model everything it needs to know about your users.

### Design for context, not model swaps

[Factorial](https://factorialhr.com/) (14,000 HR customers) watched users export CSV dumps and paste them into Claude or ChatGPT for salary analysis. [Indeed](https://www.indeed.com/) built a career counselor agent on Mastra the other way: users bring resumes, the platform brings jobs and salary data. In both cases, the value is model plus data. If you swap in a newer model and quality flatlines, you likely have a context engineering problem.

Before launch, make sure the agent can reach the account-scoped data users expect it to know, the policy docs and guardrails generic chatbots lack, and retrieval paths you can actually inspect in traces.

### Plan for two production failures

Mastra sees customer-facing teams hit the same two walls after internal testing:

**Cost.** Staging hides usage intensity. A few power users can burn hundreds—or in some cases thousands—of dollars in inference before finance notices. Watch token burn in [production observability](https://arize.com/blog/agent-observability-controllability/) dashboards from day one.

**Accuracy.** Yes, you write evals before launch. But as Sam put it, before you’ve shown the agent to any users, you don’t know the full breadth of questions they’ll ask—so your eval suite is not complete. How can it be? [Evaluation fundamentals](https://arize.com/docs/ax/evaluate/evaluation-concepts/evaluation-fundamentals) matter before launch. [Evals on traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces) matter more after.

### Rollout checklist

- Ship to 1% or 5% of users, or run invite-only early access, before general availability
- Route simpler query classes to cheaper models once you see real traffic patterns
- Put someone who has shipped an agent before on the critical path if you can
- Expand eval coverage from production failures, not from guesswork

## If you are building an internal enterprise agent

This pattern shows up in healthcare, finance, banks, and other orgs north of 1,000 employees. Internal data volume rivals customer scale. Your agent needs tool access across fragmented systems, not a single clean API—which is why Mastra’s stack leans on workflows, memory across connectors, and a harness security will approve.

### Start with one high-volume workflow

- Enterprise search across wikis, drives, and ticketing systems
- Process automation for paperwork, approvals, and compliance

[Brex](https://www.brex.com/) built an internal agent framework first, then consolidated on Mastra after learning what they actually needed. Prototype on one painful workflow. Standardize once the harness is real.

Expect org friction, too. Leadership may push agent projects without a crisp use case, you may spot high-impact workflows that aren’t on the roadmap, and the domain experts and builders who should be talking early often aren’t in the same room.

If the official project is stuck, find one partner team and one workflow you can instrument end to end. Pair domain experts with engineers who understand what an [agent harness](https://arize.com/blog/what-is-an-agent-harness/) and [evaluation harness](https://arize.com/blog/what-is-an-evaluation-harness/) need before anyone promises ROI upstairs.

## If you are building a developer platform agent

You are building agents for other engineers, or agents that multiply how fast your org ships agents. In Mastra’s framing, this is where the primitives matter most: a blessed way to build agents so every team isn’t reinventing auth, tracing, and deployment.

### Pick a shape

- **AI SRE:**ingest logs and telemetry at scale (some teams run agents over 10 TB of logs for triage and anomaly detection)
- **Internal agent platform:**a blessed stack with approved connectors, like MongoDB’s Sage on Mastra, so hundreds of developers can spin up domain agents without reinventing auth, tracing, and deployment

Your advantage, from Sam’s talk: you are often your own customer. You can look at your own workload and say you reduced MTTR because you built an agent to triage the page. Pick a metric you own (MTTR, triage time, deploy frequency) and iterate against it.

### Run the improvement loop from day one

- Trace the run
- Evaluate the failure
- Change the harness
- Rerun

That is the [improvement loop](https://arize.com/glossary/ai-improvement-loop) in practice. Platform teams that skip it rebuild the same agent three times with different names.

## Production checklist (all three patterns)

Local agents lie to you. A demo on a curated set does not prove your eval suite is complete or your cost model works at user scale. Before you call an agent “production,” check:

- **Observability:**Can you see tool calls, latency, token use, and failures on real sessions?
- **Evals:**Do you score behavior on traces, not just final answers in a notebook?
- **Harness:**When evals fail, do you know whether to change prompts, tools, context, or rubrics?
- **Failure modes:**Have you read- [common agent failures](https://arize.com/blog/common-ai-agent-failures/)against your own traces? Tool misuse and missing context beat weak base models most days.

If you need a reference implementation for the loop, start with [improving the agent harness with traces and evals](https://arize.com/blog/improve-ai-agents-traces-evals-harness/).

## How to evaluate production agents

Mastra’s stack names evals and observability as separate layers for a reason. Observability tells you what happened on a run. Evaluation tells you whether that run was good enough—and where to change the harness when it was not.

An agent eval is a repeatable check on a **trace**: the prompt, tool calls, workflow steps, and final output. Agent evals are not unit tests. The correct path is often under-specified—the agent may call three tools or seven and still succeed—so you encode **outcomes and constraints** (answer grounded in retrieved docs, approval ticket created before status flips to complete) rather than a single expected call sequence.

**Where to attach evals:**

| Level | What you score | When it matters |
|---|---|---|
| Span | One tool call, retrieval step, or model turn | Debugging wherea run broke |
| Trace | Full run from input to final answer | Ship gates, regression checks, LLM-as-judge rubrics |
| Session | Multi-turn visit across a user | Customer-facing agents, cost over a session |

Once you know which level you’re scoring at, the next choice is how you score it.

**Evaluator types teams use most:**

- **Code evaluators**: deterministic checks on tool arguments, JSON shape, or workflow state
- **Binary evaluators**: pass/fail on one failure mode; see- [binary vs. score evals](https://arize.com/blog/testing-binary-vs-score-llm-evals-on-the-latest-models/)
- **LLM-as-a-judge**: rubric scoring on open-ended output; calibrate against human labels first (- [production judge guide](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/))
- **Harness-as-a-Judge**: when a fixed template is too rigid, an agent scores inside full trace context (- [docs](https://arize.com/docs/ax/evaluate/harness-as-a-judge))

**The loop that actually sticks** ([evaluation fundamentals](https://arize.com/docs/ax/evaluate/evaluation-concepts/evaluation-fundamentals)):

- **Instrument**. Traces flowing from Mastra into Arize AX or Phoenix. The- **@mastra/arize**package exports OpenTelemetry spans; see- [Mastra tracing docs](https://arize.com/docs/ax/integrations/ts-js-agent-frameworks/mastra/mastra-tracing)
- **Error analysis**. Cluster failed or flagged traces; name the failure mode in plain language
- **Label**. Domain experts or engineers annotate a sample in a labeling UI, not raw JSON in a spreadsheet
- **Build evaluators**. One evaluator per failure mode; prefer binary over uncalibrated 1–100 scales
- **Golden set**. Hold out a test partition; do not tune rubrics on the same traces you judge against
- **Online evals**.- [Run evals on production traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces)after staged rollout; expand the suite from new failures

## What to focus on for your next sprint

| If you are building… | Do this first |
|---|---|
| Customer-facing agent | Wire proprietary context paths, then stage rollout to 1-5% of users |
| Internal enterprise agent | Pick one high-volume workflow and one domain partner team |
| Developer platform agent | Pick one metric (MTTR, triage time) and one blessed stack for the next ten agents |

The demos were never the hard part. Naming which pattern you are in, and building the evals and traces to know when you have shipped, is the real work.

Watch Mastra’s full talk from Arize Observe 2026: [What Production AI Agent Teams Are Building Today](https://www.youtube.com/watch?v=m0mS7lLLDaw).
