---
title: 'How to write effective AI agent skills: 6 data-backed practices'
kind: blog
topic: prompt-engineering
subtopic: context-engineering
secondary_topics:
- agents/harness
- evals-observability/evaluation
summary: 'Synthesizes three 2026 studies (SkillsBench, SkillComposer, a generative
  skill-composition paper) into six data-backed rules for writing AI agent skills:
  curated skills added 18.2-24.8 points over baseline on Claude Code/Codex/Gemini
  CLI while self-generated skills scored 8.1-11.5 points below baseline, and loading
  only 1-3 skills outperformed larger, comprehensive sets.'
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/how-to-write-effective-ai-agent-skills/
author: Laurie Voss
published: '2026-07-24'
fetched: '2026-07-25T06:46:14Z'
classifier: claude
taxonomy_rev: 2
words: 1977
content_sha256: 66d96d584f933b0cfe43f5fa2fe70285857a9f4765271e0f4838f3c65d45f7e0
---

# How to write effective AI agent skills: 6 data-backed practices

Skills are now a shipping product surface, from [Anthropic](https://github.com/anthropics/skills) to [ GitHub](https://www.a16z.news/p/impeccable-by-design). Yet for most AI engineers, the practice of writing them well remains poorly codified. Three recent studies change that, though. The headline finding: a good skill isn’t the longest SKILL.md or the cleverest prompt. It’s a compact package of procedural expertise that fixes a repeatable failure, loads only when relevant, and earns its place against a matched evaluation. The work is no longer adding skills—it’s designing, routing, and evaluating them as one system.

This piece distills that new data into six practical rules for writing skills that measurably improve your agent and shows how to prove each one with an eval.

**TL;DR: What makes an effective AI agent skill?**

The research points to six practical rules:

- Ground it in real human procedural expertise. Let models draft or refine only behind an evaluation gate.
- Keep it focused. Compact or standard-length guidance outperformed comprehensive documentation.
- Load the smallest relevant set. One to three skills performed best; flooding context wasted tokens and accuracy.
- Test every model-harness pair. A portable file format does not guarantee portable behavior.
- Aim at repeated knowledge gaps: internal conventions, regulated workflows, brittle APIs, and specialized procedures.
- Accept each change only when a matched with-skill versus without-skill evaluation shows meaningful lift.

**What is an AI agent skill?**

An AI agent skill is a reusable, file-system-based package of procedural knowledge for a class of tasks. It typically includes a required SKILL.md file and can add scripts, templates, examples, or reference material. A skill tells the agent how to perform a workflow; it should not contain the answer to one specific task.

That makes a skill different from a prompt, a tool, or retrieval. A prompt is an instruction in the current context. A tool exposes an action the agent can invoke. Retrieval brings in changing factual context. A skill packages reusable judgment, sequence, constraints, and resources.

Some practitioners use the term *recipe* for the larger system that wraps a skill with evals, judges, and feedback signals.

![Figure 1. Prompts, tools, skills, and recipes package increasing amounts of human expertise inside the <a href=](https://arize.com/wp-content/uploads/2026/07/skills-figure-0-opt.jpg)

**What did the research measure?**

Three recent studies move skill design from opinion to experiment. [SkillsBench](https://arxiv.org/abs/2602.12670) compares matched runs with no skills and curated skills. [SkillComposer for skill evolution](https://arxiv.org/abs/2606.06079) tests whether models can create, improve, and merge skills under explicit quality control. A separate [generative skill composition study](https://arxiv.org/abs/2606.32025) asks which skills a large library should load, how many it should load, and in what order.

**Study**

**Question**

**Practical signal**

**1. Start with human expertise, not a blank model**

Treat the model as an editor or implementer, not the source of domain truth. In SkillsBench, self-generated skills landed 8.1 to 11.5 points below the no-skill baseline across [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Codex, and [Gemini CLI](https://github.com/google-gemini/gemini-cli) configurations. Curated skills on the same configurations added 18.2 to 24.8 points.

The failure modes matter more than the headline. Generated packs sometimes went unused, consumed effort that should have gone toward solving the task, or encoded a confident but wrong assumption that the solver then followed. A polished-looking SKILL.md can still make the agent less reliable.

That does not mean model assistance is useless. The skill-evolution study shows a narrower, more defensible pattern: let a model propose a skill or revision, then retain it only when it improves a held-out task suite by a defined pass-rate margin. The source of truth is the domain expert plus the eval, not the model’s confidence.

[Paul Bakaus’s Impeccable design skill](https://github.com/pbakaus/impeccable) is a useful example. An unassisted model may interpret “make this page bolder” as gradients and neon. A design expert can define boldness through hierarchy, scale, contrast, and decisive typography. As Bakaus put it, “You really have to tell the agent what you mean.”

**What belongs in the skill?**

- The expert vocabulary and decision criteria that separate good work from plausible work.
- The canonical workflow, including branches, prerequisites, and stop conditions.
- Calibrated defaults, constraints, invariants, and sanity checks.
- API quirks, file-format requirements, parsing rules, and other details the model repeatedly misses.
- Executable scripts, worked examples, or templates when they reduce repeated reasoning.
- Known failure modes and the recovery procedure for each one.

**2. Keep the skill compact and procedural**

Do not turn SKILL.md into a manual. In the latest SkillsBench analysis, compact and standard-length skills improved pass rate by 19.0 and 21.5 points. Detailed skills improved it by 14.5 points. Comprehensive documentation was almost flat at a 0.7-point lift.

The model has a finite attention budget. Every paragraph competes with the task, tool outputs, and the rest of the harness. Extra prose can bury the actual decision rule or introduce conflicting instructions.

Put the minimum viable procedure in SKILL.md: when to use the skill, the ordered steps, the critical branches, and the definition of done. Move bulky references, examples, and scripts into separate files that the agent can open only when needed. This progressive-disclosure pattern preserves detail without paying the full context cost on every run.

**A focused skill should answer five questions**

- When should the agent load this skill?
- What sequence and decision points should it follow?
- Which constraints or invariants must never be violated?
- What does a correct result look like?
- Which resource should it open or run when the main path is not enough?

**3. Route only the skills the task needs**

A skill library creates a second engineering problem: selection. The system has to decide which skills to load, how many to load, and in what order. Loading everything is not a safe default.

The generative composition study tested a library of 196 human-curated skills. On GPT-5.2-Codex, loading all skills reached a 29.3% pass rate. A task-conditioned composer reached 45.3%. The all-skills condition also used about 23% more input tokens than the composer: 1.27 million versus 1.03 million. All-skills was still better than no skills, but it left most of the available gain on the table and paid more to do it.

SkillsBench found the same pattern from a different angle: tasks with one skill gained 18.0 points, tasks with two or three gained 19.0 points, and larger bundles gained only 10.1 points. The best default is the smallest relevant set, not the whole catalog.

**Make routing part of the harness**

- Write specific skill names and descriptions that mirror the language of the tasks they solve.
- Select the minimum subset that covers the required procedure.
- Order prerequisites before execution skills when one depends on another.
- Trace whether the agent actually discovered, read, and used the selected skill.
- Evaluate routing errors separately from execution errors. A perfect skill cannot help if it is never loaded.

**4. Test every model-harness combination you support**

Skills are portable as files, not automatically portable as behavior. The harness controls discovery, context injection, tools, permissions, subagents, workspace state, and execution. Those choices determine whether the skill is seen and whether its procedure can be followed.

SkillsBench measured the same models under different harnesses. Gemini 3.1 Pro reached 60.8% with skills in Gemini CLI and 52.8% in [OpenHands](https://github.com/All-Hands-AI/OpenHands). Claude Opus 4.7 reached 61.2% in Claude Code and 53.1% in OpenHands. A compatibility claim should therefore name the complete stack, not just the model.

For each target, test skill discovery, tool and permission compatibility, successful execution, token cost, latency, and regressions. Where harnesses expose materially different capabilities, ship a shared core plus target-specific instructions rather than pretending one file behaves identically everywhere.

This is the same reason Arize frames the agent harness as the full control layer around the model, not a thin prompt wrapper. The harness includes the tools the model can call, the context it receives, the traces it emits, the evals it runs, and the review gates that determine what changes safely ship.

**5. Aim at gaps the base model cannot reliably fill**

The best skill candidates are repeated failures that require specialized procedure. Skills are most valuable when they encode judgment or workflow the model is unlikely to recover from general pretraining alone.

Look for internal conventions, regulated review steps, scientific or manufacturing workflows, brittle APIs, uncommon file formats, incident-response playbooks, and any process where a small missed detail causes a large downstream failure. Those are high-leverage places to package expertise.

By contrast, a generic skill that restates familiar coding advice may add little and can displace a stronger default strategy. Before writing a skill, ask whether the problem is really reusable procedure.

**Need**

**Best-fit mechanism**

**6. Treat every skill change as an experiment**

A skill is not done when the Markdown looks polished. It is done when it wins a controlled comparison.

SkillsBench found negative deltas on 13 of 87 tasks, often because a skill prescribed an unnecessarily heavy pipeline, displaced a better default, or pointed the agent toward a solver it could not debug.

The practical method is [paired evaluation](https://arize.com/blog/evals-in-ci-how-to-write-llm-evals-as-tests/): hold the task, model, harness, tools, budget, and scorer constant; run a no-skill baseline; run the skill condition; then compare.

For deterministic work, use automated verifiers. For subjective work, use explicit rubrics, [calibrated judges](https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs), and human review where ambiguity remains. [Inspect traces](https://arize.com/blog/own-the-loop-field-guide-agent-harnesses/) in both conditions so you can separate routing, reasoning, tool-use, and output failures.

**A practical skill evaluation loop**

- Build a representative task set, including expected successes, edge cases, and likely regressions.
- Freeze the model, harness, tools, permissions, time limit, and token budget.
- Run the baseline without the skill and store the full traces.
- Run the same tasks with the skill available and the same scorer.
- Compare task success, skill utilization, trajectory quality, cost, latency, and regression rate.
- Inspect failures, revise one hypothesis at a time, and rerun the full suite.
- Ship only when the improvement is meaningful and holds on a separate validation set.

That loop is [evaluation-driven development](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/): trace what the agent did, evaluate the behavior, inspect the failure, refine the harness or skill, and rerun. It is also the foundation for [self-improving agents](https://arize.com/blog/from-human-operated-agent-development-to-systematic-agent-improvement/). Feedback becomes useful only when changes are measured against a stable scorecard.

**What should you measure?**

**Metric**

**Question it answers**

**How do you evaluate subjective skills?**

Not every skill produces an output that can be checked with pytest. Design quality, writing quality, investigation quality, and other judgment-heavy outcomes need a different scorecard. The core principle is still the same: compare matched conditions, but make the evaluation multidimensional.

- Define a rubric with independent dimensions such as correctness, clarity, brand fit, originality, and constraint adherence.
- Calibrate LLM judges against expert-labeled examples and use blinded human review for close or high-stakes cases.
- Evaluate the trajectory as well as the final artifact. A good-looking answer can hide a brittle or unsafe process.
- Measure diversity across a batch, not only quality one output at a time. A design skill that makes every site look the same is creating a corpus-level regression.
- Keep a holdout set and periodically refresh it so the skill does not overfit to a static benchmark.

The field does not yet have one standard for these subjective and population-level failures. That is a reason to make the scorecard explicit, not a reason to fall back to vibes.

**The eval is the skill**

The emerging rulebook is clear: start with human expertise, keep the skill focused, route only what the task needs, test every supported stack, target real procedural gaps, and gate every change with an eval.

The hard part is no longer writing convincing Markdown, it is proving that the skill makes the agent better.

For a practical starting point, use [Arize Skills](https://arize.com/docs/ax/set-up-with-ai-assistants#arize-skills-and-mcp) to add tracing and evaluation workflows to coding agents, instrument the full agent loop, and compare skill or harness versions with [agent experiments in Arize AX](https://arize.com/docs/ax/evaluate/). The standard is simple: keep what measurably helps, and discard what does not.
