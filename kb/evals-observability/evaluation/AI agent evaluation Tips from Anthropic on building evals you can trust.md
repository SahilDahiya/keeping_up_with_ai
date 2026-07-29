---
title: 'AI agent evaluation: Tips from Anthropic on building evals you can trust'
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/harness
summary: Anthropic's Marius Buleandra explains why agent evals need trajectory-level
  scrutiny, not just pass rates, using a case where a harness bug (missing SQL LIMIT
  clause) inflated a model's eval score by 9 points; covers regression vs. capability
  evals and building eval datasets from production traces.
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/ai-agent-evaluation-how-to-build-evals-you-can-trust/
author: Sara Verdi
published: '2026-07-28'
fetched: '2026-07-29T06:53:26Z'
classifier: claude
taxonomy_rev: 2
words: 3258
content_sha256: 5799b8fe9bc170747443be2d86ccce8cd7e424693b94189bd81c6a3429a4b608
---

# AI agent evaluation: Tips from Anthropic on building evals you can trust

*This piece builds on a talk Marius Buleandra, a member of  Anthropic’s technical staff, gave at Arize Observe on building agent evals that hold up in production.*

When [Marius Buleandra](https://www.linkedin.com/in/mariusbuleandra/) tested a newer model on an AI data analyst eval, it appeared to beat its predecessor by nine points. The improvement looked substantial enough to share with Anthropic’s research team as evidence of a meaningful capability gain.

Before sending the result, however, Buleandra opened the transcripts, where the victory began to unravel. The newer model had developed a habit of adding LIMIT clauses to its SQL queries.

Under ordinary circumstances, that would be a defensible way to keep a query manageable. Inside this particular evaluation, it allowed the model to sidestep a defect in the harness. Once Buleandra repaired the harness, much of the apparent improvement disappeared. The score had detected a difference, but it had misidentified the cause.

Buleandra works on Anthropic’s Applied AI team, which sits between product research and customers and helps teams improve their agents, evals, and harnesses. That position has given him a close view of a problem increasingly familiar to software developers: [agent benchmarks](https://arize.com/blog/agents-too-smart-for-benchmarks/) can produce precise numbers while concealing messy causal stories.

A model, prompt, tool, grader, or environment may have changed. The system may also have stumbled into a favorable path by chance. Reliable agent evaluation depends on knowing which explanation fits the evidence.

**What are AI agent evals?**

AI agent evals are structured tests that measure whether an agent completes a task successfully, how it reaches the result, and whether its behavior remains reliable as the surrounding system changes.

A conventional unit test usually evaluates a bounded function with a known input and an inspectable output. A bounded function is one whose behavior is self-contained and predictable: it takes a defined set of inputs and returns a defined output without depending on external state, accumulated history, or intermediate decisions.

An agent operates across a trajectory. It interprets a request, chooses an action, calls a tool, reads the result, revises its plan, and carries the accumulating history into every later decision. That means an agent eval may need to examine several layers at once:

- The final outcome
- The sequence of decisions and tool calls
- The model and system instructions
- [The agent harness](https://arize.com/blog/what-is-an-agent-harness/)
- The state of external tools and services
- The grader used to determine success

A passing result can emerge from durable capability, a flawed test, or a fortunate accident. A useful eval must provide enough evidence to distinguish among them.

**Why are AI agents so difficult to evaluate?**

Agents are difficult to evaluate because their behavior unfolds over time, their instructions are frequently incomplete, and their interfaces allow users to ask for almost anything.

Three characteristics make that behavior especially difficult to measure:

- **Errors compound across the trajectory.**An incorrect assumption or malformed tool call near the beginning can influence every action that follows. Because earlier observations remain in context, a small mistake can become part of the agent’s working model of the task.
- **Tasks arrive underspecified.**Users rarely provide a complete definition of success. They type a sentence into a text box and expect the system to infer the goal, constraints, tradeoffs, and stopping conditions.
- **Open-ended interfaces create unknown unknowns.**A general-purpose input field invites requests the product team may never have anticipated, including tasks the agent cannot safely or reliably complete.

These problems become more severe as agents run for longer periods. A multi-hour trajectory may contain hundreds of decisions, any one of which can redirect the rest of the run.

The surrounding environment introduces another source of uncertainty. Agents can reach into databases, code repositories, Slack workspaces, ticketing systems, CI pipelines, and third-party APIs. Those systems change independently, which makes it difficult to reproduce the exact conditions behind a success or failure.

The cost of avoiding this work is substantial. Without evals, regressions can remain hidden until a user encounters them. Model upgrades can also become slow and subjective because the team has no reliable way to compare versions. New capabilities may arrive without anyone realizing that the product can finally support them.

An agent can also feel similar after an upgrade while behaving much better on a narrow class of valuable tasks. Capability evals give those improvements somewhere to appear.

**Regression evals vs. capability evals: What’s the difference?**

Regression evals verify that previously working behavior continues to work. Capability evals measure how far the agent’s abilities can extend.

Production teams need both because they support different engineering and product decisions.

| Dimension | Regression evals | Capability evals | 
|---|---|---|
| Primary question | Did this change break known behavior? | What can the agent accomplish now? | 
| Main purpose | Prevent fixed failures from returning | Reveal new capabilities and remaining headroom | 
| Expected performance | A high pass rate that approaches saturation | A challenging baseline with meaningful room to improve | 
| Typical data sources | Customer incidents, reported failures, and repaired bugs | Frontier workflows, benchmark-inspired tasks, and stress cases | 
| When to refresh | When the product, harness, or user distribution changes | When models, tools, or the agent’s scope improve | 
| Decision supported | Is this release safe? | What should we build next? | 

Most teams begin with regression cases because the source material is already available. A customer reports a failure, the engineering team fixes it, and the corresponding example enters the suite so the same problem cannot quietly return.

A mature regression suite should achieve a high pass rate. It may still require maintenance as user behavior, prompts, tools, and external systems change, although its central purpose remains stable: protect capabilities the product already depends on.

[Capability evals occupy the frontier](https://arize.com/blog/3-production-patterns-ai-agents-how-to-evaluate-each-one/). Buleandra describes the process as hill climbing. The team begins with tasks that the agent can complete only some of the time, then changes the model, prompt, tools, or harness and measures whether the frontier moves.

These evals can influence product strategy as much as model selection. An agent that becomes better at recovering from failed tool calls, preserving coherence across long workflows, or interpreting ambiguous instructions may unlock features that previously required constant human supervision.

The strongest agent teams invest heavily in capability evals because the results reveal more than whether a release is safe. They show what the product may be ready to become.

**How do you build an AI agent eval dataset?**

A useful agent eval dataset combines the structure of established benchmarks with the substance of real production behavior.

The first case often feels harder than the hundredth because every decision remains open: task format, data source, success criteria, environment, and grader.

Buleandra’s advice is practical: “Just copy the shape of the eval.”

A workable data pipeline looks like this:

- **Study a relevant public benchmark.**Examine how it frames tasks, samples inputs, defines success, captures evidence, and grades the result.
- [Mine production traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces)for real behavior.
- **Create a small expert-labeled reference set.**Ask people with deep domain knowledge to identify successful behavior, acceptable alternatives, and meaningful failure modes.
- **Calibrate a capable model against those labels.**Once its judgments align with the expert reference set, use it to extend the labeling process across a larger dataset.
- **Repeat the pipeline as the system changes.**Revisit production traces periodically to account for data drift, model upgrades, new tools, and changing user behavior.

[Public benchmarks provide a starting structure](https://arize.com/blog/long-horizon-agent-benchmarks-field-guide/). A team building a coding agent might study repository-level software engineering benchmarks, while a team building an operational agent could examine tasks involving stateful tools and multi-step recovery.

The benchmark’s shape is more transferable than its exact cases. Developers can borrow the task format, evidence requirements, and grading logic, then replace the content with examples that reflect their own product. Production transcripts supply that content.

Customer complaints offer an obvious starting point, although they often only capture the failures visible enough to provoke a report. The larger opportunity lies inside the hundreds of thousands, or millions, of agent trajectories that nobody has read.

A smaller, inexpensive model can help mine this archive by:

- Clustering similar trajectories
- Tagging recurring failure modes
- Surfacing unusual tool sequences
- Identifying examples that resemble known incidents
- Finding cases in which the agent succeeded through a suspicious path

This process turns [observability data into evaluation data](https://arize.com/blog/ai-evals-are-a-data-science-problem-what-most-teams-get-wrong/). Instead of allowing traces to accumulate as an inert archive, the team uses them to discover which behaviors deserve a permanent place in the test suite.

Human experts remain essential when the domain requires specialized judgment. A medical, legal, financial, or deeply technical workflow needs labelers who can distinguish a convincing answer from a correct one.

Those experts do not need to review the entire dataset. A small, carefully labeled reference set can anchor a model-assisted labeling process, provided that the team continues checking where the model and experts disagree.

The pipeline should run repeatedly. Each model release, prompt change, tool update, and new user cohort can alter the production distribution. An eval set that never changes will eventually describe a version of the product that no longer exists.

**Agent outcomes vs. trajectories: what should you evaluate?**

Agent evals should measure both the final outcome and the trajectory that produced it.

- **Outcome evaluation**asks whether the agent reached the required end state. Depending on the product, success might mean producing a correct analysis, repairing an infrastructure problem, merging a valid patch, updating a database, or resolving a support case.
- **Trajectory evaluation**examines how the agent reached that state, including the tools it selected, the parameters it supplied, the evidence it used, the errors it encountered, and the point at which it chose to stop.

Both views are necessary because the same outcome can conceal very different behavior.

An agent might complete a task after issuing risky commands, exploiting a harness defect, or retrying until it stumbles into the answer. The final result may pass even though the process remains too brittle for production.

A failed task can also contain encouraging evidence. The agent may have formed the correct plan and used the appropriate tools before an external service timed out. Treating that run as an undifferentiated failure would hide the distinction between agent behavior and infrastructure behavior.

Trajectory analysis also exposes weak patterns before they become incidents. An agent may be succeeding today while relying on redundant calls, unsupported assumptions, or a recovery path that will collapse under a slightly different input.

[Tracing connects the aggregate score](https://arize.com/docs/ax/evaluate/run-evals-on-traces) to those individual decisions. A developer should be able to move from a metric to the exact tool call, observation, or grader decision that influenced it.

Without that connection, an eval can announce that the agent failed while offering little guidance about what the engineering team should change.

**How do you calibrate an LLM-as-a-Judge for agent evals?**

[An LLM-as-a-judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) should be calibrated against human-labeled examples before its scores are trusted. An LLM-as-a-judge is simply a language model asked to grade another model’s output—scoring a response, ranking two trajectories, or checking work against a rubric in place of a human reviewer.

Some agent outcomes can be verified with deterministic checks. A database row either changed or it did not. A test suite either passed or it failed. Many consequential tasks contain enough ambiguity that teams rely on another model to assess the output or trajectory.

The judge might evaluate whether a report addressed the user’s actual question, whether a patch fixed the root cause, or whether the agent followed an acceptable process. That flexibility creates another model-dependent layer whose errors can distort the benchmark.

Before relying on an LLM judge, the team should:

- [Compare its verdicts with expert-labeled examples](https://arize.com/blog/measuring-human-llm-judge-alignment/).
- **Inspect disagreement cases rather than tracking agreement alone.**
- **Rewrite ambiguous rubric language that produces inconsistent decisions.**
- **Require the judge to identify the evidence behind its verdict.**
- **Version the judge prompt, model, rubric, and output format together.**
- **Recalibrate whenever the judge model or task distribution changes.**

Disagreement analysis is particularly valuable because it often reveals weaknesses in the specification itself. The judge may be missing context. The rubric may leave an important preference undefined. Human reviewers may also disagree because the team has never established a shared definition of success.

Resolving those cases improves the judge and clarifies the product requirements.

Judge prompts should be treated as production code. A small wording change can alter results across the entire suite, while switching to a newer judge model can make a benchmark appear to improve or regress even when the evaluated agent remains unchanged.

A trustworthy judge should also return inspectable evidence. Rather than producing only a score, it should point to the section of the output, tool call, or transcript passage that supports its conclusion.

That evidence allows a human reviewer to verify the verdict without reconstructing the entire run from scratch.

**Why do the agent harness and evaluation harness matter?**

The agent harness and evaluation harness influence what the agent can observe, which actions it can take, and whether the resulting score can be reproduced.

Buleandra recalled working with a startup building an AI site reliability engineer. The agent connected to Kubernetes clusters, CI pipelines, and other operational systems, where it was expected to diagnose and repair infrastructure problems.

The team wanted to know whether there was a clever shortcut for building the eval environment. The practical answer involved constructing a simulated cluster, filling it with realistic data, reproducing operational incidents, and making the system rewindable to a known point in time.

“Everybody is doing the hard thing,” Buleandra said. For developers, that hard thing usually includes:

- **Resettable state**so every run can begin from a known baseline
- **Versioned tool schemas**so the agent receives consistent interfaces
- **Seeded data and failure scenarios**that reproduce meaningful conditions
- **Controlled credentials and permissions**that limit unsafe actions
- **Detailed environment logs**that separate infrastructure faults from agent mistakes

The environment becomes part of the test fixture. When an agent can mutate files, databases, tickets, deployments, or clusters, each run must return the system to a reproducible state before the next one begins.

Perfect simulation may remain impossible, especially when the product depends on live third-party services. The evaluation should make those limitations visible.

An API timeout, an expired credential, a stale database snapshot, and a bad tool decision should not collapse into the same generic failure label. When those causes remain indistinguishable, the score blends model quality with infrastructure reliability and becomes difficult to interpret.

This work resembles distributed systems engineering and test infrastructure more than prompt experimentation. That is precisely why production agent evaluation requires a harness playbook.

The model forms only one layer of the product. The tools, prompts, memory, context management, retry logic, environment, and graders collectively determine what the agent can accomplish.

**How does human transcript review expose false improvements?**

Human transcript review reveals whether a benchmark improvement reflects genuine capability, a favorable accident, or a defect in the evaluation system.

The SQL LIMIT example captures the gap between measurement and understanding. Buleandra could see the nine-point improvement immediately, although only a side-by-side review showed that the newer model had discovered a lucky route around the harness bug.

Other apparent gains can arise from changed latency, different tool ordering, random variation, or a grader that rewards the wrong behavior. A model may even get lucky consistently, which makes the effect look like a durable capability until someone examines the mechanism behind it.

“There’s no replacement for this,” Buleandra said of reading transcripts. Manual review becomes difficult as trajectories stretch from minutes to hours. The answer is to build tooling that directs human attention toward the decisive parts of the run.

Teams can scale transcript review with three kinds of tools:

- **Task-specific transcript viewers**that support search, filtering, annotation, and questions over long trajectories
- **Side-by-side comparison tools**that align two runs around tool calls, state transitions, errors, or other consequential moments
- **Grader-decision views**that surface low-confidence verdicts, model-human disagreements, and the examples responsible for a score change

The goal is efficient inspection rather than fully automated interpretation. A model can summarize long trajectories, group similar failures, identify unusual behavior, and rank the cases most likely to explain a metric shift.

A human who understands the task, harness, and product still needs to decide whether the behavior represents a meaningful capability gain.

That workflow should begin with the aggregate metric and end at the underlying evidence. When a benchmark moves, the developer should be able to answer:

- Which cases changed?
- Where did the trajectories diverge?
- Which tool calls or observations caused that divergence?
- Did the grader evaluate both runs consistently?
- Did the agent improve, or did the surrounding system change?

A score identifies where performance moved. Transcript review helps explain why.

**How does evaluation-driven development improve AI agents?**

[Evaluation-driven development](https://arize.com/blog/own-the-loop-field-guide-agent-harnesses/) places evals inside the engineering loop so every model, prompt, tool, or harness change can be measured against known failures and frontier capabilities.

Without a maintained eval system, each change creates uncertainty. A prompt revision may repair one workflow while damaging another. A tool update may alter behavior in ways that a handful of manually tested examples never expose. A more capable model may ship while the product team lacks the evidence needed to use its new abilities.

A mature evaluation loop connects several components:

- Production traces reveal failures and unusual behavior.
- Human experts convert the most important cases into labeled examples.
- Regression evals protect customer-critical behavior.
- Capability evals measure the frontier.
- LLM judges extend review after being calibrated against human labels.
- Transcript inspection explains why the score changed.
- The resulting evidence guides the next engineering decision.

Each release then produces information that can improve the next one.

This feedback loop also provides the foundation for [self-improving agents](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/). An agent system cannot reliably improve itself unless it can observe failures, identify meaningful examples, propose a change, test the new behavior, and verify that the improvement did not create regressions elsewhere.

**What developers should take away**

- **Evaluate the outcome and the trajectory.**Task completion alone cannot reveal whether the agent used a safe, reliable, and repeatable process.
- **Maintain separate regression and capability suites.**One protects established behavior while the other exposes new product possibilities.
- **Treat the harness and environment as part of the evaluated system.**Tools, state, permissions, data, and external services can all influence the result.
- **Build eval datasets from production traces and expert judgment.**Public benchmarks can provide the structure, while real user behavior supplies the cases that matter.
- **Calibrate every model-based grader.**A judge needs its own reference set, version history, and disagreement analysis.
- **Read the transcripts before declaring victory.**Aggregate scores show that something changed, while the underlying trajectories reveal whether the change deserves to be called progress.

Buleandra’s nine-point gain looked like evidence of a stronger model until the transcript revealed a more complicated truth. The model had behaved differently, the harness had rewarded that difference, and the benchmark had compressed the entire interaction into a flattering number.

That compression is useful only when developers can reverse it. Trustworthy AI agent evaluation gives teams a path from the score back to the decision, tool call, environmental condition, or grader judgment that produced it. With that evidence, developers can fix the correct layer of the system, adopt new models with confidence, and recognize when an emerging capability is ready to become a product feature.

Until then, the most reliable instruction remains the least glamorous one: read the transcripts.
