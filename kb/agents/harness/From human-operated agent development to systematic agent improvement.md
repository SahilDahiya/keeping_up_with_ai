---
title: From human-operated agent development to systematic agent improvement
kind: blog
topic: agents
subtopic: harness
secondary_topics:
- evals-observability/evaluation
- evals-observability/tracing
summary: 'Translates an Arize Observe 2026 keynote into an architecture for automated
  agent improvement loops: managed reader/fixer/reviewer workers triage failures from
  OpenInference traces, harness-as-a-judge evaluates fixes, and fleet controls catch
  runaway or stuck sessions instead of a human pasting traces into a coding agent
  by hand.'
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/
author: Sara Verdi
published: '2026-07-14'
fetched: '2026-07-15T06:44:28Z'
classifier: claude
taxonomy_rev: 2
words: 1948
content_sha256: 91c1cc01fdec2ade0e5268a4c0e3d50a0e2864fbbe0e134932b6b9913bf48fb0
---

# From human-operated agent development to systematic agent improvement

Over the past year, agents moved from occasional demos into everyday development workflows. Tools like Claude Code, OpenClaw, and open-source agent harnesses became daily drivers, while “harness” went from niche terminology to an architectural choice teams debate in design reviews.

The uncomfortable part is what that usefulness still looks like in practice. The agent runs on your laptop, but you are still in the loop. You pull [traces](https://arize.com/docs/ax/observe/tracing), spot the bad tool call, paste context into a coding agent, review the diff, and ship. That is real engineering work. And it is also a workflow that collapses the moment you have more failures than afternoons.

At [Arize Observe 2026](https://arize.com/observe/), Arize cofounders [Jason Lopatecki](https://www.linkedin.com/in/jason-lopatecki-9509941/) and [Aparna Dhinakaran](https://www.linkedin.com/in/aparnadhinakaran/) delivered a keynote about that shift: from human-operated agent development to systematic, automated agent improvement. This post translates that vision into an engineering architecture: how traces, failure discovery, managed workers, evaluations, and fleet controls fit into a repeatable improvement loop. Let’s jump in.

**The loop you already run**

If you ship agents in production, last year probably looked like this:

- Traces land in a platform
- You write or tweak manual evals
- You find a wrong tool call, missing context, or a skipped step
- You give representative traces and repository context to a coding agent
- You replay the affected cases, run regression evals, review the diff, and decide whether to ship

Teams have already started automating pieces of that path. Assistants help draft evals. Skills help turn a failure into a patch. The human is still the orchestrator. You decide which issue matters, which trace is representative, and whether the fix is safe to merge.

That model works when volume is low and the number of agents, tools, and failure modes is small. It breaks when production generates more failures than engineers can inspect, cluster, reproduce, and validate manually, whether that means thousands of traces or millions.

**What breaks when improvement stays human-operated**

At Arize, our bet is straightforward: useful agents become long-running processes you operate as a system, not one-off sessions you nurse by hand. You already see early versions of this. Kick off a worker per issue. Spin up a reviewer for the proposed fix. Run an eval agent on a schedule. Those workers are not only fixing your product agent. They start touching backend workflows and internal enterprise processes too.

That creates a different engineering job:

| Human-operated development | Systematic agent improvement | 
|---|---|
| Debug one broken session | Triage patterns across millions of traces | 
| Pair with one coding agent | Orchestrate readers, fixers, and reviewers | 
| Optimize a prompt or tool | Operate a [harness](https://arize.com/blog/what-is-an-agent-harness/): loop, tools, memory, permissions | 
| Ask “did this run succeed?” | Ask “is this fleet solving the right problems safely and cheaply?” | 

Aparna put the org shift bluntly: you stop being the person who reads a handful of traces and become the person who owns a fleet. Agents review other agents’ work. Context has to move between them. The hard questions stop being isolated model-selection questions and start looking like systems questions:

- Are workers picking the right failures, or just the loud ones?
- Did the fix address the actual trajectory bug?
- What happens when a worker has the wrong permissions?
- Which sessions are burning tokens without producing outcomes?

If you have lived through one bad agent loop that retries an expensive tool call until the budget evaporates, that last question is not theoretical. [Token spend is not proof the system is working](https://arize.com/blog/why-ai-token-costs-dont-tell-you-if-your-ai-is-working/).

**Traces are the input to the loop, not a dashboard hobby**

Continual improvement does not start with a prettier chart. It starts with a trace: the blueprint of what happened.

A useful trace for agent work usually needs:

- LLM calls and messages
- Tool calls and arguments
- Retrieval or context assembly steps
- The observable trajectory the harness took, including routing decisions, retries, handoffs, and state transitions

That is why [OpenInference](https://github.com/Arize-ai/openinference) mattered early. Without shared semantic conventions, every team invents its own names for the same spans, and your coding agent inherits a mess. If you need a concrete instrumentation reference across frameworks, [Project Rosetta Stone](https://arize.com/blog/project-rosetta-stone-instrumenting-agents-any-framework/) is built for that.

Two changes make the “paste traces into Claude” workflow obsolete:

- **Scale.**Humans cannot inspect millions of traces individually. Automated systems can query, filter, cluster, and summarize them, provided the spans use consistent semantics and retain enough context to reconstruct the failure.
- **Managed workers.**Once coding agents can run as managed processes, the reader, fixer, and reviewer can run as separate managed workers: one queries and clusters failures, one proposes a code or configuration change, and one evaluates the candidate against regression cases and policy checks.

The [AI improvement loop](https://arize.com/glossary/ai-improvement-loop/) is just that idea named: observe, find failures, change the system, evaluate, repeat. For a clearer map of how overloaded the word “loop” has become, see [what is a loop in AI engineering, anyway?](https://arize.com/blog/what-is-a-loop-in-ai-engineering-anyway/).

**The four jobs developers actually need covered**

You can ignore the product names and still use the architecture. An automated improvement loop needs four capabilities: **failure discovery, change generation, runtime operation, and regression evaluation**. Most teams have one or two, but the value comes from connecting all four with explicit handoffs and approval gates.

| Job | Developer question | What “good” looks like | 
|---|---|---|
| Discover | What is failing repeatedly? | Clusters of repeated failures rather than a handful of memorable traces | 
| Fix | Can a worker turn an issue into a reviewable change? | Same harness/skills/sandbox you trust in day-to-day development, running against real production telemetry | 
| Operate | What is the fleet doing right now? | Visibility into stuck loops, dead workers, redirected sessions, and runaway sessions, retry storms, and workers consuming resources without completing useful work | 
| Evaluate / experiment | Did the change help, and did it break something else? | Evals that survive harness churn, plus a way to compare real agent trajectories before you ship | 

In the Observe keynote those jobs mapped to Signal, managed agents, fleet observability, harness-as-a-judge, and agent experimentation. The product write-up is in [Building the AI factory for self-improving agents](https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/). The useful takeaway for builders is the dependency order: discovery without fix workers just makes a prettier backlog; fix workers without fleet controls become an unsupervised cost and security problem; evals that do not remain aligned with the harness’s tools, prompts, policies, and execution flow the week after your PM writes them.

A few details from the talk that matter if you are designing this yourself:

- **Bring your own harness.**Automated fix workers only help if they match the debug setup you already trust. Claude, Cursor, Codex, your skills, your sandbox.
- **Trace the harnesses you already use.**If Claude Code, Cursor, and Codex sessions are invisible, you are operating half-blind. See also- [own the loop: a field guide to agent harnesses](https://arize.com/blog/own-the-loop-field-guide-agent-harnesses/).
- **Cost is a first-class failure mode.**Find the session with the runaway query or the “rebuild the database” spiral before finance finds it.

**Evals have to match the thing you shipped**

[LLM-as-a-judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) remains useful when correctness is difficult to express as a deterministic check, especially for criteria such as relevance, completeness, groundedness, or policy adherence. The recurring failure mode is a static judge prompt that no longer matches the system being evaluated.

That is the practical argument for harness-as-a-judge. Instead of placing the entire evaluation procedure in one prompt, define the evaluation goal and give an evaluation harness the tools, context, execution steps, and stopping conditions needed to investigate the result. This is most useful when evaluation requires inspecting multiple spans, executing code, retrieving external evidence, or combining deterministic checks with model judgment. Related reading: [what is an evaluation harness?](https://arize.com/blog/what-is-an-evaluation-harness/) and [how to build a better agent harness with traces and evals](https://arize.com/blog/improve-ai-agents-traces-evals-harness/).

Experimentation has the same shape problem. You are not A/B testing one prompt string. You are comparing harness variants with different trajectories. Anyone who has changed one tool description and watched the whole agent take a new path knows why you need to evaluate the complete harness in a production-like environment, using representative inputs, tool implementations, permissions, and state. Pair that with evals on traces and you get a regression loop you can actually rerun.

Menu metrics are not enough either. Complex harness failures need sandboxes where you bring your own packages, multi-model checks, grounding logic, or judge agents, then write structured annotations back. Investigating and reproducing failures usually consumes more engineering time than calculating another score. [PXI](https://arize.com/blog/meet-pxi/) is Phoenix’s bet on an open-source AI engineering agent that lives next to that telemetry: harness, filesystem, bash, skills, aimed at investigation first, not full autonomy on day one.

Use the cheapest reliable evaluator for each failure mode: deterministic assertions for schema and tool constraints, execution-based checks for code and state changes, model judges for semantic criteria, and agentic evaluators only when the task requires multi-step investigation.

**Own the telemetry layer**

If traces are the fuel for improvement, lost or inconsistent telemetry is an upstream bug no coding agent can invent away. For teams that want portable telemetry, OpenTelemetry plus OpenInference provides a practical foundation: standard transport and collection infrastructure paired with GenAI-specific semantic conventions. Arize donated OpenInference source to the Linux Foundation for the same reason you want shared span conventions in any other observability stack: one vendor should not own the vocabulary.

[Phoenix](https://arize.com/docs/phoenix/) stays relevant here for a practical reason, not a brand one. Critical agent infrastructure needs to run locally, air-gapped, or in your VPC, and it needs to be forkable when the default evaluator menu is wrong for your failure modes. That is the builder test. If you cannot inspect and customize the loop, you do not really own it.

**What to change in your stack this month**

If your improvement loop is still mostly human-operated, that is normal. Most teams are there. Do not jump straight to “fleet of fix agents.” Sequence the work:

- **Make traces agent-readable.**Instrument with stable GenAI conventions. If a coding agent cannot reconstruct the trajectory from spans, nothing downstream will either.
- **Name your top failure modes.**Wrong tool, bad context, infinite retry, silent wrong answer. Build evals against those, not against a generic quality score. See- [common AI agent failures](https://arize.com/blog/common-ai-agent-failures/).
- **Define the acceptance test for each failure mode.**Decide what evidence would prove a fix worked, which regression set it must pass, and which cost, latency, or safety thresholds it cannot violate.
- **Automate discovery before you automate merges.**Cluster repeated failures first. Unsupervised PR bots on noisy telemetry create review debt.
- **Stand up one managed worker.**Start with a read-only discovery worker or a fixer that can open a draft PR but cannot merge. Give it scoped credentials, bounded runtime and spend, and the same reproducible environment you use during manual debugging.
- **Add cost and stuck-loop visibility before you scale concurrency.**A fleet can exceed its budget before it produces a conventional availability incident

The past year’s breakthrough was agents that could perform useful work. The next engineering problem is making their improvement loop repeatable: discover recurring failures, generate a candidate change, evaluate it against representative trajectories, and operate the workers within explicit cost, permission, and deployment boundaries.

Start by making traces reconstructable and evaluations reproducible. Then automate the parts of the loop where the evidence is strong, while keeping consequential changes behind review gates. In that architecture, observability is more than a record of what happened. It is the structured input that makes systematic improvement possible.

Watch the keynote on [YouTube](https://www.youtube.com/watch?v=errTnC59gVM). For the AX-side implementation details, see the [factory launch post](https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/). For hands-on eval patterns, check out the [AI agent handbook](https://arize.com/ai-agents/).
