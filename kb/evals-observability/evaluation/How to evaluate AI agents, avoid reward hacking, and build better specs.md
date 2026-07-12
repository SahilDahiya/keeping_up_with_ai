---
title: How to evaluate AI agents, avoid reward hacking, and build better specs
topic: evals-observability
subtopic: evaluation
secondary_topics:
- agents/planning
summary: Connects agent evaluation with specification quality, including reward hacking
  risks and tighter behavioral contracts.
source: arize
url: https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs
author: Sara Verdi
published: '2026-07-02'
fetched: '2026-07-11T04:41:40Z'
classifier: codex
taxonomy_rev: 1
words: 1693
content_sha256: f2566467a6cdcf7629669cde6059dc7815167f2c9a6ce30257d967b315099ec4
---

# How to evaluate AI agents, avoid reward hacking, and build better specs

Agent evals are repeatable tests that measure whether an AI agent completed a task correctly. They can score final outputs, tool calls, retrieved context, trace behavior, safety constraints, or artifacts such as code. A good agent eval defines what “done” means, catches regressions, and prevents agents from optimizing shortcuts instead of user outcomes.

That matters because AI agents do not ship as frozen prompts. They swap models, use tools, rewrite plans, and loop until something looks complete. Without strong evals, “done” becomes whatever the agent can get past the scorecard.

For agent teams, evals are becoming durable product IP. Prompts and models churn, but rubrics, behavioral specs, and test suites preserve the definition of good work across model upgrades and workflow changes. They tell the optimizer what hill to climb.

At [Arize Observe 2026](https://arize.com/), George Zhang, OpenClaw maintainer and CTO at [Runner](https://runner.now), made this point through examples from coding agents, React Doctor, and agent orchestration: models are increasingly good at climbing whatever hill you define. The engineering work is naming the hill, hardening the scorecard, and updating it when production traces reveal new failure modes.

This post explains what agent evals are, why they matter, how agents game weak evals, and how to design rubrics and test suites that are harder to reward-hack in production.

**What are agent evals?**

An agent eval is a repeatable check that scores whether an agent run did what you intended. That can look like a golden dataset with expected answers, a code check on tool arguments, an [LLM-as-a-judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/) rubric, or a linter-style score on an artifact the agent produced. The input is usually a trace (prompt, tool calls, final output). The output is a label or score plus, ideally, a reason you can inspect.

Agent evals differ from classic unit tests in one important way: the “correct” path is often under-specified. The agent may call three tools or seven and still succeed. We encode outcomes and constraints (“answer from provided context only,” “never disable lint rules”) rather than a single expected call sequence.

Here are two common shapes:

- **Numeric target:**a 0 to 100 grade on a codebase (React Doctor is a public example).
- **Behavioral spec:**a test suite that defines correct software behavior (Next.js’s suite is the reference case teams cite when they talk about reproducible implementations).

Both tell an optimizer what to climb toward. If you are building that stack for the first time, start with [evaluation fundamentals](https://arize.com/docs/ax/evaluate/evaluation-concepts/evaluation-fundamentals) in AX or [Phoenix LLM evals](https://arize.com/docs/phoenix/evaluation/llm-evals) in open source.

**Why are evals important for AI agents?**

Agents increasingly swap models, rewrite skills, add tools, and loop until something looks done. Without evals, “done” becomes whatever the agent could get away with on the last run.

Once you can specify the problem clearly, getting the agent there is increasingly the cheap part. The eval is that specification. It should survive prompt rewrites and model upgrades because it encodes what the product is for: not how the agent implemented a task today, but whether the outcome is acceptable tomorrow.

Two examples clarify why we treat specs as IP, even outside agent products.

- **Test suites as product definitions.**Cloudflare’s experimental vinext work showed why public test suites matter for agentic development. By porting large parts of the Next.js test suite and using it as a behavioral spec, the team could iterate toward a broad Next.js-compatible surface in about a week. The lesson is not that agents can magically clone a mature framework end to end; it is that tests make compatibility executable.
- **Standards as the human job.**OpenAI’s- [harness engineering](https://openai.com/index/harness-engineering/)write-up describes a five-month experiment in which Codex agents produced roughly a million lines of code across about 1,500 pull requests, with zero manually written code. The human work shifted toward defining coding standards, architecture rules, feedback loops, and review harnesses that agents could operate inside.

For agent products, e.g., support, research, coding, or otherwise, the parallel is direct. Model weights are not the moat, neither are prompts or skill files.

That is also why we wire evals into the [improvement loop](https://arize.com/glossary/ai-improvement-loop): update the spec when production traces show a new failure mode, and don’t treat evals as a one-time pre-launch gate. Our [agent harness with traces and evals](https://arize.com/blog/improve-ai-agents-traces-evals-harness/) walkthrough shows that loop on a PM agent scoring GitHub issues; a linter score on a coding agent is the same pattern with a different scorer.

**What are examples of agent evals?**

Agent evals take different shapes depending on the workload, but the underlying move is always the same: define pass/fail (or a score) on something you can re-run. What changes is the scorer.

- **Coding agents**get a linter or audit score on the code they generate.
- **Tool-calling agents**get checked on whether the right tool fired with valid arguments— see- [how to evaluate tool-calling agents](https://arize.com/blog/how-to-evaluate-tool-calling-agents/)and- [evaluating tool calls in LLM pipelines](https://arize.com/blog/llm-function-calling-evaluating-tool-calls-in-llm-pipelines/).
- **PM and workflow agents**get rubrics scoring issue quality or task completion straight from their traces, as in our- [PM agent harness walkthrough](https://arize.com/blog/improve-ai-agents-traces-evals-harness/).
- **Open-ended output**calls for- [LLM-as-a-judge](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/)or- [LLM-judge agent evaluation](https://arize.com/blog/agent-evaluation-llm-judge/), where rubric-based scoring handles natural language a number can’t.
- **Pass/fail gates**are- [binary evals](https://arize.com/blog/testing-binary-vs-score-llm-evals-on-the-latest-models/)tied to a single failure mode: hallucination, policy violation, a missing citation.

Retrieval-heavy agents are their own case, you can start with [ RAG evaluation](https://arize.com/blog/rag-evaluation-complete-guide-2026/) patterns—golden questions, context adherence, and trace review—before you reach for judges.

**How do agent evals get gamed?**

Reward hacking shows up the moment a metric becomes the target. Take React Doctor for example: it grades a React codebase from 0 to 100 and lists what is wrong. Point an agent at it with “fix my front-end until React Doctor reads 100/100” and the score often moves without much human refactoring. That is specification-driven development working as designed.

It also breaks the same way every time someone forgets to constrain the spec. Another run on the same prompt hit 100/100 by disabling or excluding the checks being scored. The prompt never said that was out of bounds. The model took the shortest path up the hill.

That sequence is what we mean by gaming an agent eval:

- Pick a metric.
- Let the agent optimize it.
- Watch the metric and the user-visible outcome diverge.

Goodhart’s law is not new. What changed is speed: a model finds the exploit on the first pass if your spec leaves room for it. When we review [common agent failures](https://arize.com/blog/common-ai-agent-failures/) in production, vague success criteria show up far more often than weak base models.

**How do you build evals that are harder to game?**

The React Doctor case is a useful template. The first prompt optimized the score. The hardened spec optimizes score plus constraints. Next:

- **State the forbidden shortcuts.**Write “100/100 with all rules still enabled,” not “make the front-end better.” List the cheats you refuse to accept before you run the agent: disabled linters, empty citations, stub implementations, tool calls with placeholder arguments.
- **Check spirit, not just letter.**If your eval only reads the final number, it is incomplete. Add checks that the behaviors you care about still happened: scored checks still enabled, tools called with real inputs, sources present in the answer.
- **Red-team before you trust.**Try to pass the eval without solving the user problem. If you can, the model will too. The missing “do not disable rules” clause in the React Doctor prompt is exactly the kind of gap red-teaming is meant to surface.
- **Use instructions when there is no single number.**For “elegant architecture” or “good writing,” we use plain-English rules and iterate until the optimizer stops finding loopholes. Same job as an LLM judge, with the same dependency on human labels behind the rubric. When pass/fail is enough,- [binary evals](https://arize.com/blog/testing-binary-vs-score-llm-evals-on-the-latest-models/)are often easier to defend than an uncalibrated 1-100 scale.
- **Run on production-shaped traffic.**Offline green scores are cheap.- [Run evals on traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces)from real sessions so shortcuts show up where they hurt users. For agent-heavy workloads,- [Agent as a Judge](https://arize.com/docs/ax/evaluate/harness-as-a-judge)can help when a fixed template is too rigid and you need scoring in full trace context. In Arize AX, this pattern uses an agentic evaluator that reads traces at runtime rather than relying only on pre-mapped columns. The- [LLM evaluation guide](https://arize.com/blog/llm-evaluation-guide/)is our recommended starting point if you are building that stack for the first time.

**Specs are climbing the abstraction ladder**

Coding agents changed how much intent you have to write to get a unit of work done:

| Stage | What you write | What the tool does |
|---|---|---|
| Tab completion (early Cursor) | The first few characters of the code you want | Completes the line |
| Agent mode | A short English task | Writes the function or file |
| Codex / Conductor-style agents | A chat thread | Keeps coding while you steer in conversation |
| Ticket-driven agents (e.g. Symphony-style workflows on Linear) | A Linear issue or project-board task | Agent picks up work, opens a PR, and moves the task through review states; humans review outcomes, tests, and acceptance criteria instead of steering every line |

Each step returns more output per sentence of specification. Coding agents generate faster than most teams can define “done,” so vague specs become the bottleneck. The leverage is in clearer completion criteria, not in watching every diff.

You can also spec by reference: ask a model to design a distributed system “like *Designing Data-Intensive Applications*” and it often produces something credible because the book functions as a shared standard. [Coding-agent rule files](https://arize.com/blog/optimizing-coding-agent-rules-claude-md-agents-md-clinerules-cursor-rules-for-improved-accuracy/) are another form of the same idea: machine-readable standards agents optimize against between runs.

**What to invest in next**

Execution will keep getting cheaper. What compounds is the spec: what you measure, what you forbid, and what you update when a new loophole appears in production.

If you are auditing an agent stack today, start here: write evals before prompts, treat the suite like a product definition a new engineer can understand, and [run evals on traces](https://arize.com/docs/ax/evaluate/run-evals-on-traces) as traffic arrives. That is the IP worth defending: evals, rubrics, and test suites that catch real failures, resist reward hacking, and make the next agent version measurably better than the last.

For more, watch George’s full talk at Arize Observe 2026 [here](https://www.youtube.com/watch?v=DVzZqIzlsRk).
