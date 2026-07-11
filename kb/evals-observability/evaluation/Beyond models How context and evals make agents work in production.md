---
title: 'Beyond models: How context and evals make agents work in production'
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/memory-context
summary: Explains why production agents depend on context quality and eval loops,
  not just model choice, and outlines how to evaluate behavior on real workflows.
source: arize
url: https://arize.com/blog/ai-agents-in-production-context-evaluation
author: Patrick Kelly
published: '2026-04-23'
fetched: '2026-07-11T04:55:33Z'
classifier: codex
taxonomy_rev: 1
words: 1610
content_sha256: 3bf6b0cce680b30a64b32dd85ff54de0cb49d962ec288e4b38539b4f1bfa3422
---

# Beyond models: How context and evals make agents work in production

Building an AI agent has never been easier. But getting one into production that’s reliable is still hard.

Most teams can ship a working demo in a day. The agent can answer questions, call tools, and even complete multi-step tasks. Then it hits production data, real users, and real constraints. That is where things break.

In a conversation with [Tobias Leong](https://www.linkedin.com/in/tobiasleong/), the CTO and cofounder of [Axium Industries](https://axium-industries.com/), a company building AI agents for supply chain and industrial operations, one idea came up again and again: The problem isn’t the model, but everything around it.

“We swapped [a new model] in, and it actually does nothing,” Leong says. “It just raises your costs, but it doesn’t actually do anything more, because of insufficient context.”

This is the shift happening right now. Model quality is improving quickly but production reliability isn’t. The teams that succeed are the ones investing in context, evaluation, and system design—not the ones chasing the latest model.

*Are you a visual learner? Check out the full interview with Tobias Leong. 👇*

**The gap between demos and production**

There’s a reason most agent demos look impressive. They run in controlled environments with curated inputs and limited scope.

Production systems are different. They rely on messy data, legacy infrastructure, and workflows that have evolved over years. At Axium Industries, Tobias and his team build agents for industrial environments across manufacturing, logistics, oil and gas, and retail. These are systems where decisions carry real operational consequences.

The difficulty isn’t generating an answer, but generating the right answer consistently and under uncertainty.

“You need to be very certain that a certain event should be happening,” Leong says. “In an example of an inventory replenishment, you need to ensure that you don’t have SKUs in the warehouse. You have to really get it right.”

This is where most agent systems fail when the underlying model lacks the context required to reason correctly and consistently.

**The rise of the agent engineer**

This shift has created a new kind of role. Leong describes the agent engineer as someone who combines software engineering, infrastructure, and applied AI.

The work involves understanding systems, data, and human workflows, not just prompts and model APIs.

At Axium, that meant going into the field.

Leong explains: “We have been on offshore supply bases, we have been on ships, we have been in warehouses, to really understand what the processes are, what are the humans actually doing today.”

That level of context is what allows agents to operate effectively. Without it, you are building in the dark.

**Context is the real source of intelligence**

A common instinct when agents underperform is to upgrade the model. Leong has seen this pattern repeatedly, and the outcome is usually the same.

“We swapped in a new model, and it actually did nothing … because of insufficient context,” he says.

The underlying issue is missing information.

Tobias described a failure mode that shows up often in production systems: “The models sometimes answer the question that you wish to ask, but not the one you actually asked. And it sounds really confident.”

This is a context problem, not a model problem.

**What “context” actually means in production**

In real systems, context is more than just the system prompt. It includes:

- Structured data from systems of record
- Retrieval pipelines for relevant documents
- Memory and state across interactions
- Tool access for real-world actions
- Domain-specific constraints and logic

At Axium, agents operate on top of ERP systems, telemetry data, and operational workflows. That context is what enables useful decisions in the industrial context.

**Separating retrieval from reasoning in your architecture**

A reliable pattern is to separate retrieval from reasoning.

```
```
```
def plan_inventory_restock(sku_id: str) -> str:
    # Retrieve facts from source systems
    inventory = warehouse_db.get_inventory_level(sku_id)
    forecast = forecasting_service.get_weekly_forecast(sku_id)
    # Let the model reason over grounded data
    prompt = f"""
    Current inventory: {inventory}
    Forecasted demand: {forecast}
    Should we restock this SKU? Explain your reasoning.
    """
    return llm.generate(prompt)
```
			This code example above reflects how Leong describes his mental model: “One thing that has worked out well for us is this mental model of using LLMs not as data sources, but as reasoning engines.”

Once you make this separation, a large class of errors disappears. The model is no longer responsible for recalling facts. It is responsible for properly retrieving data and context, then interpreting them.

**Evaluations are what make agents real**

Context gets you closer to the right answer. Evaluation tells you whether you are actually getting it.

Leong draws a clear line between demos and production: “Evaluation … transcends something that seems to be working into something that actually works.”

Most public benchmarks do not reflect real workloads. In supply chain systems, there are no standard datasets that capture the complexity of real decisions. That means teams need to build their own.

At Axium, this takes the form of golden datasets created with domain experts. These datasets represent real scenarios and expected outcomes.

**What to evaluate**

A practical evaluation loop should include:

- Task success
- Tool call correctness
- Consistency across variations
- Behavior under edge cases
- Business outcomes

Evaluation isn’t a one-time step. It’s a continuous loop that enables:

- Regression detection
- Model comparison
- Safe iteration

**Making evaluation operational**

Axium initially built its own tooling for evaluation and observability. As their systems matured, they also evaluated third-party options, including Braintrust, but found it was not sufficient for the production requirements they were solving around tracing, observability, and operating complex agent workflows at scale. They ultimately shifted to using Arize Phoenix and the broader Arize platform to support evaluation and production-grade monitoring.

The reason was focus. Building infrastructure slowed down work on actual customer problems.

The broader lesson is simple. Evaluation needs to be treated as infrastructure, not an afterthought.

**Common failure modes in production agents**

The patterns Leong described map closely to what many teams see in production.

Here are a few to watch for:

**Confident irrelevance**

“The models sometimes answer the question that you wish to ask, but not the one you actually asked.”

**Over reliance on model upgrades**

“It just raises your costs, but it doesn’t actually do anything more meaningful for that particular situation.”

**Missing or incomplete context**

Agents cannot make correct decisions without access to the right data.

**Lack of evaluation**

Without a way to measure performance, systems degrade silently.

**Domain expertise is a force multiplier**

One of the most overlooked parts of building agents is domain knowledge.

At Axium, forward deployed engineers (FDEs) work directly with customers to understand how decisions are made. That includes observing real-world behavior and identifying edge cases that would not appear in synthetic data.

“You need to really understand the industry, the use cases, what work happens around that for you to be able to design the best possible agent for that workload,” Leong says.

Domain experts also play a key role in evaluation by defining what “correct” looks like. Axium does this by working closely with the customer, and also having a bench of industry experts in their respective industries across key industrial sectors in the region including aviation, maritime, energy, logistics, and manufacturing.

**Building vs. buying an AI observability platform**

Axium’s early approach included building internal tools for tracing and evaluation. That worked for a while, but created a new problem.

Too much precious engineering time was spent maintaining infrastructure instead of solving customer problems.

The shift to using Arize tools allowed the team to move faster and focus on what mattered. That included Alyx, Arize’s AI engineering agent, which helps developers investigate traces, run evaluations, generate datasets, and fix issues in agent behavior. In practice, it gives teams an agentic interface for AI engineering workflows, similar to how coding agents accelerate software development.

This is a common tradeoff. Building everything yourself gives control. It also slows you down.

**A practical playbook for developers**

If you are building agents today, here are the patterns that matter most:

**Before upgrading your model**

- Are you grounding responses in real data?
- Do you have clear tool interfaces?
- Is your context complete and relevant?

**For evaluation**

- Do you have a golden dataset?
- Can you measure task success?
- Are you tracking regressions?

**For system design**

- Are retrieval and reasoning separated?
- Can you trace what the agent did?
- Can you explain why it made a decision?

**Quick agent maturity model**

| Stage | Focus |
|---|---|
| Prototype | Prompting |
| Contextualized | Data and tools |
| Evaluated | Measurement |
| Observable | Tracing |
| Production-ready | Reliability and iteration |

**What to try next**

If you want to improve your agent today:

- Replace one prompt-only flow with a retrieval-backed workflow
- Create a small golden dataset with 20 real examples
- Run two models against the same evaluation set
- Add tracing to understand failures
- Measure task success instead of relying on intuition

**Stop chasing models**

The industry narrative is still centered on model progress. Bigger models, better reasoning, higher benchmarks.

That progress is real, and it’s not the bottleneck.

The bottleneck is building systems that can use that intelligence effectively.

The teams that succeed will not be the ones with the best model. They will be the ones with the best systems around it.

So, stop chasing models and start building context and evaluation into everything.

**Make this real in your own system**

Take one workflow and:

- Add retrieval-backed context
- Build a small evaluation set
- Trace what your agent is actually doing

[Arize AX](https://arize.com/generative-ai/) makes this loop fast: trace, evaluate, fix.
