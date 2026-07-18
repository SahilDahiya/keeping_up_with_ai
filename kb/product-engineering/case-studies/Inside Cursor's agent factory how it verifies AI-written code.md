---
title: 'Inside Cursor''s agent factory: how it verifies AI-written code'
kind: blog
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/evaluation
- agents/harness
summary: 'Details Cursor''s verification architecture for AI-written code: risk scoring
  routes ~30-40% of PRs to merge without human review, behavioral video artifacts
  let reviewers inspect agent-exercised changes before the diff, and human corrections
  become rules/eval cases for its review agent Bugbot, with failed evals triggering
  diagnosis workflows with trace context attached.'
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/inside-cursors-agent-factory-how-it-verifies-ai-written-code/
author: Sara Verdi
published: '2026-07-17'
fetched: '2026-07-18T06:38:35Z'
classifier: claude
taxonomy_rev: 2
words: 1860
content_sha256: 8595b75a178d0c04d815bd3d8bcb155ab150861c23282cb4f7fb74e9c0ebb16c
---

# Inside Cursor's agent factory: how it verifies AI-written code

**Key takeaways**

• Cursor treats verification as an integrated architecture across CI, security review, risk scoring, behavioral artifacts, and specialized review agents.

• Agents work inside developer-like environments so they can exercise a change and return evidence that shows how the product behaves.

• Risk scores route routine pull requests through an automated path while directing consequential changes to the right human reviewer.

• Human corrections become rules and evaluation cases for Bugbot, Cursor’s pull request review agent.

• Failed evals can trigger diagnosis workflows with trace and logging context already attached.

• Cursor prunes its skill library because sharper context matters more than a growing instruction count.

**When a screen recording becomes a unit of trust**

[Cursor](https://cursor.com/home) gave an unsupervised coding agent a modest assignment: add pinned chats to the web app. The agent implemented the feature, launched the interface, exercised the interaction, and returned a video that showed the result.

For Cursor’s Regional Director of Field Engineering [John Gilhuly](https://www.linkedin.com/in/johngilhuly/), speaking at [Arize Observe 2026](https://arize.com/observe/), that artifact marked “one of the turning points” in Cursor’s internal use of agents. A reviewer could inspect the behavior before parsing the diff, which gave the team a faster way to decide whether the change deserved deeper attention. Gilhuly estimated that roughly 30 to 40 percent of pull requests in Cursor’s ecosystem now merge without human review, which makes the quality of that evidence consequential.

The demo also reveals the engineering problem that arrives after code generation gets fast. Agents can now plan work, modify a monorepo, open pull requests, respond to CI, and continue in the background while a developer moves elsewhere. As that capacity grows, teams need a reliable way to gather evidence, allocate human review, and improve the system whenever an issue escapes.

Cursor’s answer is a verification architecture that spans the whole development loop. It combines reusable skills, realistic execution environments, CI and security checks, risk scoring, behavioral artifacts, and review agents whose mistakes become future evaluation cases.

**The bottleneck moves downstream**

A growing share of Cursor’s product comes from background agents that continue after the developer has moved on, Gilhuly said. Inside the company, the software development lifecycle has compressed into four connected phases: an agent prepares a plan, a human reviews the approach, the agent implements the change and returns a demo, and the team ships while running a continuous retrospective on the system.

Each phase can have a specialized agent, which shifts engineering effort toward the [harness](https://arize.com/blog/what-is-an-agent-harness/) around the models: context, tools, policies, evaluations, and the plumbing that turns failures into [better future behavior](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/). Cursor’s internal diagram placed Anthropic, OpenAI, Gemini, and its own models in a baseline intelligence layer, while the custom engineering sat above them in the agent system. Gilhuly described this work as sharpening the axe.

When that harness is weak, [agents lose relevant context](https://arize.com/blog/common-ai-agent-failures/), narrow the task prematurely, misjudge their capabilities, or finish without proving that the result works. Those failures often look like isolated model mistakes in a trace, although the deeper cause lives in system design.

**A merge decision becomes a policy**

That level of autonomy depends on several gates working together, because no single check can carry the full decision.

A simplified policy might look like this:

```
```
```
evidence = collect(ci, security_review, demo_artifact)
 risk = score_change(pr, evidence)
 if evidence.passed and risk <= auto_merge_threshold:
     merge(pr)
 else:
     request_review(pr, owner=route_by_change(pr))
```
This is a conceptual sketch based on the talk; Cursor’s production implementation is proprietary. The architecture will still look familiar to a platform team: collect signals, apply a policy, and route exceptions to the person most capable of judging them.

CI and clean-code checks establish a baseline, while security-specific agents add another source of evidence. Risk scoring then determines where scarce human attention should go. A low-risk change with complete evidence can follow an automated path, while a high-risk change can summon the appropriate owner.

Teams adopting this pattern should treat the auto-merge threshold as an operating parameter. Escaped defects, rollback frequency, human overrides, and time-to-merge reveal whether the policy has become too permissive or too cautious.

**The developer environment becomes part of the eval harness**

A traditional coding agent can report that it changed a button. Treating the runtime as an [evaluation harness](https://arize.com/glossary/evaluation-harness/) changes what evidence an agent can return. Cursor gives its agents machines preconfigured with local developer tooling, which lets them boot the product and exercise the change. The resulting artifact can be a video, screenshot, test run, or another form of evidence that maps the diff to visible behavior.

One attempt at developer fidelity became comically literal. A skill told an agent to behave like a real engineer, and the agent installed Spotify because the application lived in that developer’s setup. The anecdote exposes a serious design boundary: the environment needs enough fidelity to reproduce the workflow, while the harness still needs to distinguish useful context from incidental personal setup.

With computer-use capabilities, an agent can navigate the interface it just modified, record the outcome, and attach the recording to the pull request. A diff describes the implementation, while a demo exposes the behavior that users will encounter. Video evidence still covers an exercised path, so tests and static checks carry the wider state space. Cursor can also retain those artifacts as data for future evaluations.

**How Cursor’s Bugbot learns from the comment thread**

Code review is another specialized agent inside Cursor’s system. [Bugbot](https://cursor.com/bugbot), the company’s pull request review agent, consumes reactions, replies, and review comments as signals for learned rules and evaluation cases.

If a human has to step in and say, “This is something that you missed,” Gilhuly said, the correction is incorporated into future reviews. The comment therefore has a second life beyond the current pull request, because it can become a regression case that tests whether Bugbot catches the same class of issue again.

This design turns review quality into a maintained product surface. Teams need a corpus of misses, expected findings, and difficult examples, alongside metrics for precision, recall, override rate, and downstream escapes. They also need curation because review comments mix correctness, style, and local preference. Without a measured corpus, a review agent can sound increasingly polished while its actual coverage remains unclear.

**Skills give the monorepo a memory**

Cursor’s monorepo contains about 150 skills, according to Gilhuly. A skill packages repeated knowledge or a workflow so an agent can reuse it across tasks. One “how” skill teaches an agent how to discover how a system works; a companion “why” skill searches Slack, Notion, git history, and related records for the reasoning behind a decision.

Cursor measures the skill system by its signal quality, which often improves as redundant material disappears. Gilhuly described the questions his team asks: “Can we reduce the number of skills? Can we streamline those?”

That pruning discipline matters because every additional instruction competes for context and attention. A useful skill has a clear trigger, required inputs, expected artifact, success signal, and owner. Mature skills can graduate into automations that run when an event occurs. Gilhuly said some projects, including build-process optimization, are coordinated through Slack channels that trigger those workflows.

**An eval failure can start the diagnosis**

Consider a documentation help agent that returns a bad answer. In the workflow Gilhuly described, [an eval failure](https://arize.com/docs/ax/evaluate/run-evals-on-traces) can emit a trigger through Arize or Phoenix, launch a diagnosis skill, and pass the relevant logging context into the new run. The system begins investigating at the moment of detection.

That pattern gives evals an operational role. A score feeds the next control decision, while traces supply the evidence the diagnosis agent needs. Viewed as a control loop, the sequence becomes observe, evaluate, diagnose, improve, and deploy. This is a concrete form of [agent-native evaluation](https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs), because the eval result becomes a machine-consumable signal inside the workflow. A human can remain responsible for policy, escalation, and deployment approval even as the investigative loop becomes automatic.

Cursor applies a similar model to longer-running optimization jobs. [Self-improving agents](https://arize.com/glossary/self-improving-agents/) can [hill-climb](https://arize.com/glossary/ai-improvement-loop/) against measurable product signals such as build time or success rate for hours or days, and Gilhuly said one run lasted about five days. He also called Cursor’s usage “the extreme end of the spectrum,” a useful warning for teams whose latency, cost, or security constraints require tighter bounds.

Long-running autonomy earns its keep when the objective is measurable, the tools are scoped, the system can checkpoint progress, and the stop conditions are explicit. Improvement comes from the objective and the feedback signal; extra token volume only extends the search.

**What agent automation looks like in daily engineering**

Cursor has applied this pattern across a broad set of maintenance and review tasks — the kind of specialized workflows that also show up in [production patterns for AI agents](https://arize.com/blog/3-production-patterns-ai-agents-how-to-evaluate-each-one/):

• Security review on individual pull requests and recurring scans

• Detection and repair of CI failures

• Automatic fixes for issues found during code review

• Test coverage maintenance and dependency updates

• Continuous checks for documentation

• Vulnerability confirmation and remediation workflows

When CI fails, an agent can detect the break, make a repair, and keep the branch current, creating what Gilhuly called a “self-driving PR.” Security offers another revealing example: once agents took on more of the review surface, Cursor began finding dramatically more vulnerabilities. The number can look alarming on a slide; it also suggests that the detection surface expanded.

These workflows share the same architecture: a specialized agent owns a bounded task, verification tools measure the outcome, and feedback updates the rules, skills, or eval set. The value accumulates because each incident can make the next run more reliable.

**A practical adoption path**

Most teams can begin with one workflow where success is easy to measure.

1. **Start with a bounded task.** CI repair, dependency updates, documentation verification, and narrow security checks have clear outputs and existing signals.

2. **Define an evidence contract.** Decide which tests, artifacts, security checks, and risk signals must be present before any automated merge — the same discipline behind writing [LLM evals as CI tests](https://arize.com/blog/evals-in-ci-how-to-write-llm-evals-as-tests/).

3. **Make the environment reproducible.** Package the developer tooling, credentials policy, fixtures, and service dependencies required to exercise the change.

4. **Route by risk.** Begin with recommendations, then graduate low-risk changes to auto-merge after measuring escaped defects, rollbacks, and human overrides.

5. **Turn corrections into regression cases.** Every missed review comment should update the eval set, skill, or rule that governs future runs.

6. **Wire detection to action.** Let a failed eval launch a diagnosis workflow with trace context, while policy controls which fixes can reach production.

**The factory runs on evidence**

Cursor’s experience suggests that the [durable advantage in ](https://arize.com/docs/ax/observe/tracing)[coding agents](https://arize.com/blog/own-the-loop-field-guide-agent-harnesses/) will come from the verification layer around them. Models can produce more code each quarter, while teams still carry responsibility for deciding what deserves trust.

That responsibility becomes manageable when agents return evidence, risk policies allocate human attention, and every correction strengthens the next evaluation. Under that architecture, autonomy grows because the system can explain what happened, show why a change passed, and reveal which signal will improve the next run.

**Watch the full Arize Observe 2026 session: ***How Cursor Uses AI Agents to Build Cursor**.*
