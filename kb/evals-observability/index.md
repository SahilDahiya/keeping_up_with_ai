# evals-observability

238 articles.

- **2026-07-21** — [How OpenAI uses human feedback to evaluate and improve LLMs](<evaluation/How OpenAI uses human feedback to evaluate and improve LLMs.md>) · `evaluation` · arize
  OpenAI aggregates explicit and implicit user feedback into a shared data layer, using an LLM-derived pipeline to recover in-conversation corrections (2-3x more actionable signal) and embedding-based KNN clustering to surface failure patterns beyond a hierarchical taxonomy, with MCP/skills letting Codex turn a raw bug report into a root-caused pull request.
- **2026-07-21** — [What I Learned by Dogfooding Our Own AI Agent, Signal](<evaluation/What I Learned by Dogfooding Our Own AI Agent, Signal.md>) · `evaluation` · cresta
  Cresta dogfooded its Synthetic Customers tool (personas built from real conversation data) against its own website AI agent, Signal, to test the agent against realistic non-happy-path visitors (impatient, adversarial, or channel-switching) instead of idealized test cases.
- **2026-07-21** — [Trace voice agents in LangSmith](<tracing/Trace voice agents in LangSmith.md>) · `tracing` · langchain
  LangSmith adds Python tracing integrations for four voice agent frameworks (Pipecat, LiveKit, OpenAI Realtime, Gemini Live/ADK), covering both 'sandwich' (STT to LLM to TTS) and speech-to-speech architectures with audio recording, per-component latency breakdown, and interruption tracking.
- **2026-07-20** — [IssueBench - How We Evaluate Engine](<benchmark-design/IssueBench - How We Evaluate Engine.md>) · `benchmark-design` · langchain
  Describes IssueBench, LangChain's internal benchmark for LangSmith Engine (an agent that finds/clusters/fixes issues in other agents' traces): 15 tasks with synthetically injected, ground-truth-labeled failures across SRE, software engineering, and customer support domains, run on Harbor and scored on classification, categorization, issue-attachment, and new-issue-grouping accuracy.
- **2026-07-16** — [Human annotations for agent runs in Pydantic Logfire](<evaluation/Human annotations for agent runs in Pydantic Logfire.md>) · `evaluation` · pydantic
  Human-in-the-loop annotation of agent runs in Logfire to catch cases automated LLM judges miss—an agent that is fluent, polite, and wrong—by letting domain experts label traces the judge scored as good.
- **2026-07-15** — [Introducing Real World VoiceEQ: Measuring the human quality of voice AI](<benchmark-design/Introducing Real World VoiceEQ Measuring the human quality of voice AI.md>) · `benchmark-design` · huggingface
  Hume AI's Real World VoiceEQ benchmark evaluates 40+ voice models across ASR, TTS, speech-to-speech, and speech understanding using 1M+ human ratings (785K TTS, 48K STS), finding no single model tops all 8 TTS capability groups and that speech-language-model judges disagree with human raters on subjective calls like emotional fit or identity consistency.
- **2026-07-15** — [Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse](<evaluation/Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse.md>) · `evaluation` · langfuse
  Walks through a PASS/FAIL deployment-gate pipeline for LLM systems at a major bank, built on Langfuse datasets/experiments/prompt management/annotation queues: three golden datasets (FinanceBench, Financial PhraseBank, a custom adversarial advisory set) score models and agents, gate on thresholds like 85% numerical accuracy, and emit CI exit codes plus reviewable evidence for model risk management.
- **2026-07-15** — [How we chose the model behind Topics with Baseten - Blog - Braintrust](<evaluation/How we chose the model behind Topics with Baseten - Blog - Braintrust.md>) · `evaluation` · braintrust
  Details how Braintrust and Baseten chose and tuned a sub-10B model (Gemma 4B, beating Qwen) to summarize every production trace for the Topics feature, built a 650-example benchmark across label correctness/factuality/issues-recall/false-positive-rate, and improved Issues recall from 0% to 32.8% through prompt iteration alone (no fine-tuning).
- **2026-07-15** — [Kiro CLI observability: trace and evaluate agent changes with Arize Skills](<evaluation/Kiro CLI observability trace and evaluate agent changes with Arize Skills.md>) · `evaluation` · arize
  Walks through pairing Amazon's Kiro CLI coding agent with Arize Skills to build a validation loop: instrument an app, export traces, build a regression dataset from production failures, and run an experiment comparing the current implementation against an agent-proposed revision before merging.
- **2026-07-14** — [How to measure AI productivity: From LLM token costs to business value with Arize AX](<evaluation/How to measure AI productivity From LLM token costs to business value with Arize AX.md>) · `evaluation` · arize
  Argues token/prompt/LOC counts don't measure AI productivity (citing METR's finding that developers were 19% slower with AI while feeling 20% faster) and proposes a five-dimension framework, built on a shared correlation_id tagging contract, that joins traced AI work to outcomes like merged non-reverted PRs via Arize AX.
- **2026-07-14** — [Agent and LLM views in Pydantic Logfire](<monitoring/Agent and LLM views in Pydantic Logfire.md>) · `monitoring` · pydantic
  Argues that non-deterministic agent workloads should be monitored on turns-per-run and tool-calling-turns-per-run at p90, not the mean, because a rare runaway retry loop (e.g. 40 tool calls, $12) hides in the average; built from the gen_ai.* spans agents already emit.
- **2026-07-14** — [How to Debug Coding Agents with LangSmith Traces](<tracing/How to Debug Coding Agents with LangSmith Traces.md>) · `tracing` · langchain
  Introduces LangSmith tracing support across coding agents (Claude Code, Codex, Cursor, Copilot Chat, Pi, OpenCode, dcode), normalizing each tool's fragmented session/tool-call/subagent-handoff formats into one standardized trace structure so failures like a subagent inheriting a stale offset-paging helper are visible instead of requiring a fresh restart.
- **2026-07-13** — [Agents Week: ship real agents and fix them from production traces | Pydantic Logfire](<monitoring/Agents Week ship real agents and fix them from production traces Pydantic Logfire.md>) · `monitoring` · pydantic
  Argues that agent quality is learned from production traces rather than pre-ship eval suites ('evals are a steering wheel, not a destination; it's a trace, not a test'), and that at scale you observe a 'herd' of agents over OpenTelemetry rather than hand-tuning each one.
- **2026-07-07** — [Improving Agents is a Data Mining Problem](<monitoring/Improving Agents is a Data Mining Problem.md>) · `monitoring` · langchain
  Argues that improving agents is a data-mining problem over traces, failures, feedback, and recurring behavioral patterns.
- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-07-02** — [How to evaluate AI agents, avoid reward hacking, and build better specs](<evaluation/How to evaluate AI agents, avoid reward hacking, and build better specs.md>) · `evaluation` · arize
  Connects agent evaluation with specification quality, including reward hacking risks and tighter behavioral contracts.
- **2026-06-30** — [AI evals are a data science problem: What most teams get wrong](<evaluation/AI evals are a data science problem What most teams get wrong.md>) · `evaluation` · arize
  Argues that AI evaluation is a data science workflow requiring careful labeling, slices, standards, and failure analysis rather than a simple dashboard metric.
- **2026-06-30** — [Harbor x LangChain: A Unified Stack for Evaluating Agents](<evaluation/Harbor x LangChain A Unified Stack for Evaluating Agents.md>) · `evaluation` · langchain
  Describes a unified stack for evaluating agents, integrating agent execution, traces, datasets, and scoring workflows.
- **2026-06-30** — [Let your customers shape your agents](<evaluation/Let your customers shape your agents.md>) · `evaluation` · sierra
  Explains experimentation loops for agent improvement, using customer behavior, A/B tests, and statistical confidence to shape agent changes.
- **2026-06-26** — [How to eval stateful agents](<evaluation/How to eval stateful agents.md>) · `evaluation` · braintrust
  Guide to evaluating stateful agents, including memory, conversation state, trace review, and tests for behavior that depends on previous interactions.
- **2026-06-24** — [Introducing the FFASR Leaderboard: Benchmarking ASR in the Real World](<benchmark-design/Introducing the FFASR Leaderboard Benchmarking ASR in the Real World.md>) · `benchmark-design` · huggingface
  The FFASR leaderboard benchmarks far-field ASR (clean/noisy/reverberant) using hybrid wave-based room simulation with sim-to-real validation, held-out audio and standardized eval hardware; it plots a WER-vs-RTFx Pareto front and finds far-field WER at low SNR is several times worse than near-field on the same speech.
- **2026-06-23** — [ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet)](<benchmark-design/ParallelKernelBench Frontier LLMs can't write fast multi-GPU kernels (yet).md>) · `benchmark-design` · together
  Introduces ParallelKernelBench for measuring whether frontier LLMs can write fast multi-GPU kernels.
- **2026-06-22** — [Designing the runtime for Langfuse code evaluators](<testing/Designing the runtime for Langfuse code evaluators.md>) · `testing` · langfuse
  Design deep dive on the runtime for Langfuse code evaluators, covering execution isolation, evaluator lifecycle, and safe scalable scoring infrastructure.
- **2026-06-22** — [Project Rosetta Stone: a reference implementation for instrumenting agents in any framework](<tracing/Project Rosetta Stone a reference implementation for instrumenting agents in any framework.md>) · `tracing` · arize
  Describes a reference implementation for instrumenting agents across frameworks, useful for standardizing trace capture.
- **2026-06-16** — [How to use Braintrust with any framework or provider](<tracing/How to use Braintrust with any framework or provider.md>) · `tracing` · braintrust
  Integration guide for capturing Braintrust traces and evals across different AI frameworks and model providers without locking the application stack to one SDK.
- **2026-06-15** — [Building a 100x Cheaper Trace Judge with Fireworks](<llm-as-judge/Building a 100x Cheaper Trace Judge with Fireworks.md>) · `llm-as-judge` · langchain
  Shows how to build a lower-cost trace judge with Fireworks, focusing on evaluator cost reduction while preserving useful scoring quality.
- **2026-06-15** — [Teaching Sidekick to say no: automated data curation with LLM judge consensus (2026)](<llm-as-judge/Teaching Sidekick to say no automated data curation with LLM judge consensus (2026).md>) · `llm-as-judge` · shopify
  Shopify curates Sidekick training data using LLM-judge consensus to automatically filter examples ('teaching Sidekick to say no'), replacing manual labeling with judge-based quality and coverage control.
- **2026-06-15** — [Agents are the new services in Pydantic Logfire](<monitoring/Agents are the new services in Pydantic Logfire.md>) · `monitoring` · pydantic
  Argues agents need service-style observability reinvented for their shape: non-deterministic execution paths, per-request token cost, models silently swapped or throttled under you, and a data plane that is now a compliance plane (user-typed PII in prompts). Contrasts AI-observability vendors (LangSmith, Langfuse, Arize) with infra vendors (Datadog, Grafana) and pitches a unified RED-metrics/topology/SLO view over a single trace ID.
- **2026-06-15** — [One agent, two trace destinations: Arize AX + Databricks Unity Catalog](<tracing/One agent, two trace destinations Arize AX + Databricks Unity Catalog.md>) · `tracing` · arize
  Shows how a single agent can emit traces to multiple destinations, highlighting interoperability concerns for observability stacks.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-09** — [The Data Comes First: Mining Real Conversations for Test Coverage](<testing/The Data Comes First Mining Real Conversations for Test Coverage.md>) · `testing` · cresta
  Explains how real conversation data can be mined to create better test coverage for AI agents.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-06-04** — [Introducing AI Agent Testing 2.0: Confidence at Launch, Confidence at Scale](<testing/Introducing AI Agent Testing 2.0 Confidence at Launch, Confidence at Scale.md>) · `testing` · cresta
  Describes AI agent testing at launch and scale, including confidence-building practices for production deployments.
- **2026-06-04** — [How we made continuous trace intelligence possible at scale](<tracing/How we made continuous trace intelligence possible at scale.md>) · `tracing` · braintrust
  Architecture deep dive on continuous trace intelligence at scale, including how production traces are clustered and surfaced for analysis.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<benchmark-design/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `benchmark-design` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-06-02** — [Designing Efficient Verifiers for Legal Agents](<llm-as-judge/Designing Efficient Verifiers for Legal Agents.md>) · `llm-as-judge` · langchain
  Explains how to design efficient verifiers for legal agents so domain-specific correctness can be checked without excessive cost.
- **2026-06-02** — [Introducing Rubrics: Build Agents that Evaluate and Correct Their Work](<llm-as-judge/Introducing Rubrics Build Agents that Evaluate and Correct Their Work.md>) · `llm-as-judge` · langchain
  Introduces rubrics for Deep Agents so agents can evaluate and correct their own work against explicit criteria.
- **2026-06-02** — [AI observability for agent products: how Atlas uses Logfire](<tracing/AI observability for agent products how Atlas uses Logfire.md>) · `tracing` · pydantic
  Atlas (8 engineers, 1000 DAU) instruments every span with user/project/workspace identity via X-Context-* headers so a coding agent can query production traces in plain English; the takeaway is that identity-carrying spans, not the AI, are what make trace data answerable.
- **2026-06-01** — [The best eval harness for production AI and agents: A comparison](<testing/The best eval harness for production AI and agents A comparison.md>) · `testing` · arize
  Compares production AI eval harnesses and highlights the design dimensions that matter for agents and applications.
- **2026-05-29** — [Evaluating Speech-to-Text Quality: Beyond Word Error Rate](<evaluation/Evaluating Speech-to-Text Quality Beyond Word Error Rate.md>) · `evaluation` · cresta
  Explains why word error rate is insufficient for speech-to-text evaluation and what production teams should measure instead.
- **2026-05-28** — [Introducing Synthetic Customers: A Living Model of Your Customer Base, Derived From Real Conversations](<testing/Introducing Synthetic Customers A Living Model of Your Customer Base, Derived From Real Conversations.md>) · `testing` · cresta
  Introduces synthetic customers as test fixtures for agent behavior, useful for scenario coverage and launch readiness.
- **2026-05-27** — [SLO monitoring in Logfire](<monitoring/SLO monitoring in Logfire.md>) · `monitoring` · pydantic
  Implementing SLO monitoring in Logfire: turning implicit reliability targets into explicit SLIs, error budgets, and burn-rate alerts to decide when to roll back a deploy or page on-call.
- **2026-05-27** — [From production traces to better AI agents: Automating the LLMOps feedback loop](<tracing/From production traces to better AI agents Automating the LLMOps feedback loop.md>) · `tracing` · arize
  Shows how production traces can feed evaluation and improvement loops for AI agents rather than remaining passive monitoring data.
- **2026-05-21** — [How to build LLM-as-a-Judge evaluators that hold up in production](<llm-as-judge/How to build LLM-as-a-Judge evaluators that hold up in production.md>) · `llm-as-judge` · arize
  Details how to design LLM-as-judge evaluators that remain useful in production, including calibration and failure modes.
- **2026-05-21** — [How to improve your golden datasets with human review](<testing/How to improve your golden datasets with human review.md>) · `testing` · braintrust
  Explains how human review improves golden datasets for evals by correcting labels, surfacing ambiguity, and tightening quality standards.
- **2026-05-20** — [The Agent Execution Tax](<benchmark-design/The Agent Execution Tax.md>) · `benchmark-design` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-05-20** — [What we learned testing 7 models under the same agent harness](<testing/What we learned testing 7 models under the same agent harness.md>) · `testing` · arize
  Compares seven models under a shared agent harness, showing how harness-controlled tests expose model behavior differences.
- **2026-05-19** — [Benchmarking inference at scale: coding agents](<benchmark-design/Benchmarking inference at scale coding agents.md>) · `benchmark-design` · together
  Benchmarks inference at scale for coding-agent workloads.
- **2026-05-18** — [Coding agent tracing and evaluation: An open source tool to improve AI coding workflows](<tracing/Coding agent tracing and evaluation An open source tool to improve AI coding workflows.md>) · `tracing` · arize
  Introduces open-source tracing and evaluation for coding agents, focusing on visibility into tool use and code-edit behavior.
- **2026-05-14** — [How to evaluate multi-turn conversations](<evaluation/How to evaluate multi-turn conversations.md>) · `evaluation` · braintrust
  Guide to evaluating multi-turn conversations, including state, conversation-level criteria, turn-level scoring, and agent-like interaction failures.
- **2026-05-13** — [Tau-Knowledge: benchmarking agents on realistic knowledge](<benchmark-design/Tau-Knowledge benchmarking agents on realistic knowledge.md>) · `benchmark-design` · sierra
  Introduces tau-knowledge for benchmarking agents on realistic knowledge tasks that require grounded retrieval and use of external information.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-12** — [Tau-Bench: Benchmarking AI agents for the real-world](<benchmark-design/Tau-Bench Benchmarking AI agents for the real-world.md>) · `benchmark-design` · sierra
  Introduces tau-Bench as a benchmark for real-world AI agents, focusing on task completion, tool use, and operational realism.
- **2026-05-12** — [Tau-Bench leaderboard: compare, explore, and understand agent performance](<benchmark-design/Tau-Bench leaderboard compare, explore, and understand agent performance.md>) · `benchmark-design` · sierra
  Introduces a tau-Bench leaderboard for comparing and analyzing agent performance across benchmark tasks.
- **2026-05-12** — [Tau-Bench shaping development and evaluation agents](<benchmark-design/Tau-Bench shaping development and evaluation agents.md>) · `benchmark-design` · sierra
  Explains how tau-bench shapes agent development and evaluation by providing realistic tasks and measurable behavior.
- **2026-05-12** — [Tau-Voice: benchmarking real-time voice agents](<benchmark-design/Tau-Voice benchmarking real-time voice agents.md>) · `benchmark-design` · sierra
  Introduces tau-voice for benchmarking real-time voice agents on realistic tasks, including speech interaction and task-completion quality.
- **2026-05-12** — [Tau2-Bench](<benchmark-design/Tau2-Bench.md>) · `benchmark-design` · sierra
  Introduces tau2-bench for evaluating agents in collaborative real-world scenarios where task success depends on interaction dynamics.
- **2026-05-12** — [Tau3-Bench: Advancing agent evaluation to knowledge and voice](<benchmark-design/Tau3-Bench Advancing agent evaluation to knowledge and voice.md>) · `benchmark-design` · sierra
  Introduces tau3-Bench for extending agent evaluation to knowledge and voice tasks, expanding beyond text-only transactional benchmarks.
- **2026-05-12** — [Insights 2.0: AI that improves your AI](<monitoring/Insights 2.0 AI that improves your AI.md>) · `monitoring` · sierra
  Describes using AI-generated insights from production conversations to improve deployed agents and surface recurring issues.
- **2026-05-12** — [Who monitors the monitors?](<monitoring/Who monitors the monitors.md>) · `monitoring` · sierra
  Discusses monitoring AI agents and the meta-problem of monitoring the monitors, with emphasis on operational feedback and quality controls.
- **2026-05-12** — [How Voice Sims work](<testing/How Voice Sims work.md>) · `testing` · sierra
  Explains how voice simulations test agents before production by generating realistic spoken interactions and edge cases.
- **2026-05-12** — [Simulations: the secret behind every great agent](<testing/Simulations the secret behind every great agent.md>) · `testing` · sierra
  Explains simulation as a testing strategy for agents, using realistic scenarios to validate behavior before customer deployment.
- **2026-05-12** — [Voice Sims: testing real conversations before real customers](<testing/Voice Sims testing real conversations before real customers.md>) · `testing` · sierra
  Explains voice simulations for testing agents under real-world speech conditions before production customer calls.
- **2026-05-12** — [Agent Traces: getting to the fix, fast](<tracing/Agent Traces getting to the fix, fast.md>) · `tracing` · sierra
  Introduces agent traces as a debugging workflow for finding failures quickly across conversations, tools, and agent decisions.
- **2026-05-11** — [From observability to context: What’s next for Arize Phoenix](<tracing/From observability to context What’s next for Arize Phoenix.md>) · `tracing` · arize
  Connects LLM observability with context management, showing how traces and application state can become reusable context for better agents.
- **2026-05-11** — [Why your traces and evals belong in the same place](<tracing/Why your traces and evals belong in the same place.md>) · `tracing` · braintrust
  Argues that traces and evals should live together so teams can connect production behavior, offline experiments, and failure analysis.
- **2026-05-06** — [Adding Benchmaxxer Repellant to the Open ASR Leaderboard](<benchmark-design/Adding Benchmaxxer Repellant to the Open ASR Leaderboard.md>) · `benchmark-design` · huggingface
  Adds private held-out Appen/DataoceanAI accent and conversational splits to the Open ASR Leaderboard to blunt benchmaxxing and test-set contamination, keeping the public average WER separate behind a toggle, and discusses the text normalizer needed to standardize model outputs.
- **2026-05-05** — [Agent observability needs feedback to power learning](<monitoring/Agent observability needs feedback to power learning.md>) · `monitoring` · langchain
  Explains why agent observability needs feedback loops from users, evaluators, and production traces to power ongoing agent learning and improvement.
- **2026-05-05** — [AI agent evaluation: How to test, debug, and improve agents in production](<testing/AI agent evaluation How to test, debug, and improve agents in production.md>) · `testing` · arize
  Explains how to test, debug, and improve AI agents in production with structured evaluation and observability.
- **2026-05-04** — [What is an evaluation harness?](<testing/What is an evaluation harness.md>) · `testing` · arize
  Defines evaluation harnesses and how they structure repeatable measurement for AI applications and agents.
- **2026-05-01** — [Why agent telemetry needs standards](<tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-04-30** — [Online evals in Pydantic Logfire to monitor production AI](<evaluation/Online evals in Pydantic Logfire to monitor production AI.md>) · `evaluation` · pydantic
  Explains online (production) evals: attach the same Evaluator classes used offline to live agent traffic, sample as much as you want (a cheap heuristic on every call, an expensive LLM judge on ~1%), score hallucination rate/tool-use accuracy/response quality on real inputs, and feed each regression back into the offline test suite anchored to the trace that produced it.
- **2026-04-28** — [How to earn stakeholder trust with evals and observability](<monitoring/How to earn stakeholder trust with evals and observability.md>) · `monitoring` · braintrust
  Explains how evals and observability help build stakeholder trust by making AI product quality measurable, reviewable, and improvable.
- **2026-04-27** — [DeepSeek V4 Pro: Validating Frontier Models for Production](<evaluation/DeepSeek V4 Pro Validating Frontier Models for Production.md>) · `evaluation` · fireworks
  Shows how to validate a frontier model for production using benchmark and workload-specific evaluation signals.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-04-23** — [An update on recent Claude Code quality reports](<monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-22** — [Why AI Agent Evaluations Fail — and How the Swiss-Cheese Model Prevails](<evaluation/Why AI Agent Evaluations Fail — and How the Swiss-Cheese Model Prevails.md>) · `evaluation` · cresta
  Explains common AI agent evaluation failure modes and uses a layered Swiss-cheese model for more robust coverage.
- **2026-04-22** — [How to add an evaluation harness to your Gemini CLI coding agent](<testing/How to add an evaluation harness to your Gemini CLI coding agent.md>) · `testing` · arize
  Walks through adding an evaluation harness to a Gemini CLI coding agent, including how to measure and compare agent behavior.
- **2026-04-16** — [Reusable Evaluators and Evaluator Templates in LangSmith](<llm-as-judge/Reusable Evaluators and Evaluator Templates in LangSmith.md>) · `llm-as-judge` · langchain
  Covers reusable evaluator templates in LangSmith for standardizing scoring logic across teams and experiments.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-04-14** — [Classifying User Intent with Categorical LLM-as-a-Judge](<llm-as-judge/Classifying User Intent with Categorical LLM-as-a-Judge.md>) · `llm-as-judge` · langfuse
  Shows how to classify user intent with categorical LLM-as-judge evaluators, including rubric design and structured scoring for production analysis.
- **2026-04-14** — [OpenTelemetry LLM Tracing with Vercel AI SDK and Pydantic Logfire](<tracing/OpenTelemetry LLM Tracing with Vercel AI SDK and Pydantic Logfire.md>) · `tracing` · pydantic
  Shows how enabling experimental_telemetry on Vercel AI SDK generateText/streamText calls emits rich OpenTelemetry spans (full prompt, response, token counts, streaming latency, tool calls) following the OTel GenAI semantic conventions (gen_ai.* / ai.*), which any OTel backend can render as readable conversations.
- **2026-04-09** — [Human judgment in the agent improvement loop](<evaluation/Human judgment in the agent improvement loop.md>) · `evaluation` · langchain
  Explains where human judgment fits into the agent improvement loop, including review, labeling, feedback, and evaluator calibration.
- **2026-04-08** — [Agentic eval development with the Braintrust CLI](<testing/Agentic eval development with the Braintrust CLI.md>) · `testing` · braintrust
  Shows how to use the Braintrust CLI for agentic eval development, turning local experiments into repeatable tests for agent behavior.
- **2026-04-06** — [How Brainstore works: architecture for AI observability at scale](<monitoring/How Brainstore works architecture for AI observability at scale.md>) · `monitoring` · braintrust
  Deep dive into Brainstore's architecture for AI observability at scale, covering storage, indexing, query patterns, and trace/log workloads.
- **2026-04-03** — [From First Eval to Autonomous AI Ops: A Maturity Model for AI Evaluation](<evaluation/From First Eval to Autonomous AI Ops A Maturity Model for AI Evaluation.md>) · `evaluation` · arize
  Defines a maturity model for moving from first evaluations to automated AI operations, with emphasis on eval loops and production governance.
- **2026-04-01** — [The Rage Clicks of LLM apps: High-Signal Production Monitoring for AI Customer Support Agents](<monitoring/The Rage Clicks of LLM apps High-Signal Production Monitoring for AI Customer Support Agents.md>) · `monitoring` · langfuse
  Detailed production-monitoring pattern for AI customer-support agents using high-signal LLM-as-judge classifiers to detect rage-click-like failure modes.
- **2026-03-27** — [Agent Evaluation Readiness Checklist](<evaluation/Agent Evaluation Readiness Checklist.md>) · `evaluation` · langchain
  Checklist for agent-evaluation readiness covering task definitions, datasets, traces, scoring, human review, and rollout criteria.
- **2026-03-26** — [How we build evals for Deep Agents](<evaluation/How we build evals for Deep Agents.md>) · `evaluation` · langchain
  Describes how LangChain builds evals for Deep Agents, including datasets, task realism, scorers, and iteration loops.
- **2026-03-26** — [Observability for AI Agents: Tracing Multi-Service LLM Pipelines with Langfuse](<tracing/Observability for AI Agents Tracing Multi-Service LLM Pipelines with Langfuse.md>) · `tracing` · cresta
  Shows how to trace multi-service LLM pipelines for AI agents with Langfuse, including cross-service visibility concerns.
- **2026-03-24** — [We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests](<testing/We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests.md>) · `testing` · langfuse
  Case study of using Autoresearch to improve an AI skill, with emphasis on writing better tests and using research-agent output to harden behavior.
- **2026-03-20** — [Debugging Python memory issues in production with memray and AI](<monitoring/Debugging Python memory issues in production with memray and AI.md>) · `monitoring` · pydantic
  Debugging recurring Kubernetes OOM kills on a production Python service using memray heap profiling plus AI-assisted analysis to trace the leak to specific request patterns.
- **2026-03-19** — [What is AI observability?](<monitoring/What is AI observability.md>) · `monitoring` · braintrust
  Explains AI observability concepts for production systems, including traces, evals, logs, monitoring, and feedback loops.
- **2026-03-10** — [How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator](<evaluation/How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator.md>) · `evaluation` · arize
  Case study on using evals plus an agentic workflow to iteratively improve a newsletter-generation system.
- **2026-03-10** — [How to build your first offline eval](<testing/How to build your first offline eval.md>) · `testing` · braintrust
  Step-by-step guide to building a first offline eval, including dataset setup, task definition, scorers, experiment runs, and failure review.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<benchmark-design/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `benchmark-design` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-03-05** — [Evaluating Skills](<evaluation/Evaluating Skills.md>) · `evaluation` · langchain
  Explains how to evaluate agent skills as reusable capabilities, with tests that isolate skill behavior from the full agent loop.
- **2026-03-02** — [How to Evaluate Tool-Calling Agents](<evaluation/How to Evaluate Tool-Calling Agents.md>) · `evaluation` · arize
  Covers evaluation methods for tool-calling agents, including how to assess action selection and tool-use correctness.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [2,000 robots walk into a shop: Simulated A/B testing (2026)](<testing/2,000 robots walk into a shop Simulated AB testing (2026).md>) · `testing` · shopify
  SimGym: Shopify's simulated A/B testing environment where thousands of LLM-driven shopper agents exercise storefronts, letting teams test changes against synthetic-but-realistic buyer behavior before real traffic.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-26** — [Evaluating AI Agent Skills](<evaluation/Evaluating AI Agent Skills.md>) · `evaluation` · langfuse
  Explains how to evaluate AI agent skills, including task design, scoring, trace inspection, and regression testing for reusable agent capabilities.
- **2026-02-26** — [Agent Observability: How to Monitor and Evaluate LLM Agents in Production](<monitoring/Agent Observability How to Monitor and Evaluate LLM Agents in Production.md>) · `monitoring` · langchain
  Guide to monitoring and evaluating LLM agents in production, including traces, feedback, evals, and alerting signals.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-25** — [Automatically discover what matters in your production traces with Topics](<tracing/Automatically discover what matters in your production traces with Topics.md>) · `tracing` · braintrust
  Introduces automatic topic discovery over production traces as a way to find recurring behavior patterns and quality issues.
- **2026-02-20** — [AI Agent Observability, Tracing & Evaluation with Langfuse](<tracing/AI Agent Observability, Tracing & Evaluation with Langfuse.md>) · `tracing` · langfuse
  Guide to observability for AI agents, covering traces, spans, tool calls, evaluations, and debugging workflows for agentic systems.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-12** — [The 5 pillars of AI model performance](<benchmark-design/The 5 pillars of AI model performance.md>) · `benchmark-design` · braintrust
  Defines five pillars of AI model performance and how to measure quality beyond a single aggregate benchmark score.
- **2026-02-11** — [LLM-as-a-Judge: A Practical Guide with Pydantic Evals](<llm-as-judge/LLM-as-a-Judge A Practical Guide with Pydantic Evals.md>) · `llm-as-judge` · pydantic
  Practical guide to LLM-as-a-judge with pydantic-evals: argues evaluation is a narrower task than generation, that case-specific evaluators outperform generic ones for test suites, to run deterministic type/format checks before the LLM judge, to always request the judge's reasoning for debugging rubrics, and to turn every user complaint into an evaluation case.
- **2026-02-10** — [Zero Code Instrumentation with eBPF and Logfire](<tracing/Zero Code Instrumentation with eBPF and Logfire.md>) · `tracing` · pydantic
  Instrumenting services that can't take an OpenTelemetry SDK—legacy apps, compiled binaries, third-party containers—using the OpenTelemetry eBPF instrumentation agent to emit traces to Logfire with zero code changes.
- **2026-02-09** — [AI Model Performance Metrics Explained](<monitoring/AI Model Performance Metrics Explained.md>) · `monitoring` · baseten
  Explains model performance metrics used in production inference, including latency, throughput, and quality signals.
- **2026-02-06** — [What do LLMs think when you don't tell them what to think about?](<evaluation/What do LLMs think when you don't tell them what to think about.md>) · `evaluation` · together
  Investigates what LLMs do under underspecified prompting and how that affects evaluation.
- **2026-02-05** — [How to run LLM performance benchmarks (and why you should)](<benchmark-design/How to run LLM performance benchmarks (and why you should).md>) · `benchmark-design` · baseten
  Explains how to run LLM performance benchmarks and which serving metrics matter.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<benchmark-design/Quantifying infrastructure noise in agentic coding evals.md>) · `benchmark-design` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-02-05** — [The logs I never read](<tracing/The logs I never read.md>) · `tracing` · pydantic
  A dogfooding walkthrough of tracking down a customer bug in a distributed system through Logfire traces rather than reading all the logs, framed by how large context windows and tool use have made coding agents productive but also more prolific bug generators.
- **2026-02-03** — [The Benchmark Gap: What It Takes to Ship Kimi K2.5](<evaluation/The Benchmark Gap What It Takes to Ship Kimi K2.5.md>) · `evaluation` · fireworks
  Explains the benchmark and quality gaps involved in shipping Kimi K2.5 for production workloads.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-28** — [How to Debug & Evaluate AI Agents with Observability — LangChain Guide](<tracing/How to Debug & Evaluate AI Agents with Observability — LangChain Guide.md>) · `tracing` · langchain
  Guide to debugging and evaluating AI agents with observability, using traces to inspect tool calls, intermediate steps, and failure modes.
- **2026-01-26** — [DSGym: A holistic framework for evaluating and training data science agents](<benchmark-design/DSGym A holistic framework for evaluating and training data science agents.md>) · `benchmark-design` · together
  Introduces DSGym for evaluating and training data science agents.
- **2026-01-23** — [Turning production logs into evaluation datasets](<evaluation/Turning production logs into evaluation datasets.md>) · `evaluation` · fireworks
  Describes converting production traces into compact evaluation datasets using embeddings, clustering, and representative sampling.
- **2026-01-22** — [Testing Agent Skills Systematically with Evals | OpenAI Developers](<evaluation/Testing Agent Skills Systematically with Evals OpenAI Developers.md>) · `evaluation` · openai-devs
  Pattern for evaluating Codex agent skills like lightweight end-to-end tests: define outcome/process/style/efficiency success criteria first, capture run traces and artifacts, then combine deterministic checks (did it run npm install, create package.json) with rubric-based grading to catch regressions.
- **2026-01-22** — [E2E Test Debugging with Distributed Tracing | Pydantic Logfire](<tracing/E2E Test Debugging with Distributed Tracing Pydantic Logfire.md>) · `tracing` · pydantic
  Using distributed tracing to debug failing E2E tests: propagating trace context through the system so a CI failure (e.g. a 500) can be localized to the API, database, or a downstream service instead of guessing from logs.
- **2026-01-21** — [Designing AI resistant technical evaluations](<testing/Designing AI resistant technical evaluations.md>) · `testing` · anthropic-engineering
  How Anthropic designs technical hiring evaluations that stay meaningful when candidates have AI assistance, favoring debugging and judgment over greenfield coding.
- **2026-01-13** — [Debugging Ralph Wiggum with Braintrust Logs](<tracing/Debugging Ralph Wiggum with Braintrust Logs.md>) · `tracing` · braintrust
  Debugging walkthrough using Braintrust logs to inspect AI application behavior, identify failure causes, and close the loop with improvements.
- **2026-01-09** — [Demystifying evals for AI agents](<evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-12-18** — [Brainstore makes AI observability at scale possible](<monitoring/Brainstore makes AI observability at scale possible.md>) · `monitoring` · braintrust
  Benchmark-oriented note on Brainstore performance and why purpose-built storage is needed for high-volume AI observability workloads.
- **2025-12-05** — [Tangle: An open-source ML experimentation platform built for scale (2025)](<tracing/Tangle An open-source ML experimentation platform built for scale (2025).md>) · `tracing` · shopify
  Tangle: Shopify's open-source ML experimentation platform for reproducibility at scale, tracking notebook versions, data snapshots, and parameters so experiments can be reproduced without re-running from scratch.
- **2025-12-03** — [Evaluating Deep Agents: Our Learnings](<evaluation/Evaluating Deep Agents Our Learnings.md>) · `evaluation` · langchain
  Shares lessons from evaluating Deep Agents, including task design, traces, scoring, and how agent architectures change eval needs.
- **2025-12-01** — [AWS Bedrock AgentCore Observability with Arize AX: Operationalizing AI Agents At Scale](<tracing/AWS Bedrock AgentCore Observability with Arize AX Operationalizing AI Agents At Scale.md>) · `tracing` · arize
  Walks through operationalizing AWS Bedrock AgentCore agents with Arize AX observability, focusing on traces, evaluation, and production-scale monitoring.
- **2025-11-25** — [Evals are a team sport: How we built Loop](<testing/Evals are a team sport How we built Loop.md>) · `testing` · braintrust
  Describes collaborative eval workflows for teams, including feedback loops that turn production examples, review, and datasets into better AI behavior.
- **2025-11-24** — [Turn production data into better AI with Loop](<monitoring/Turn production data into better AI with Loop.md>) · `monitoring` · braintrust
  Explains Loop as a way to turn production data into AI improvements through review, labeling, datasets, and feedback-driven iteration.
- **2025-11-18** — [Evaluating and Improving AI Agents at Scale with Microsoft Foundry](<evaluation/Evaluating and Improving AI Agents at Scale with Microsoft Foundry.md>) · `evaluation` · arize
  Guide to evaluating and improving production AI agents at scale with Microsoft Foundry and Arize workflows.
- **2025-11-18** — [The three pillars of AI observability](<monitoring/The three pillars of AI observability.md>) · `monitoring` · braintrust
  Defines three pillars of AI observability and how traces, evals, and production feedback combine to improve AI systems.
- **2025-11-14** — [Tracing, Evaluation, and Observability for Google ADK (How To)](<tracing/Tracing, Evaluation, and Observability for Google ADK (How To).md>) · `tracing` · arize
  How-to guide for tracing, evaluating, and observing Google ADK agents in production-style workflows.
- **2025-11-12** — [Evaluating LLM Applications: A Comprehensive Roadmap](<evaluation/Evaluating LLM Applications A Comprehensive Roadmap.md>) · `evaluation` · langfuse
  Roadmap for evaluating LLM applications, from defining quality criteria and datasets to running automated and human-assisted eval workflows.
- **2025-11-06** — [Systematic Evaluation of AI Agents](<evaluation/Systematic Evaluation of AI Agents.md>) · `evaluation` · langfuse
  Covers systematic evaluation of AI agents, focusing on experiment interpretation, failure analysis, and how to compare agent variants.
- **2025-11-04** — [How to evaluate and benchmark Large Language Models (LLMs)](<benchmark-design/How to evaluate and benchmark Large Language Models (LLMs).md>) · `benchmark-design` · together
  Guide to evaluating and benchmarking LLMs for production model selection.
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-10-27** — [Why You Can’t Trust Out-of-the-Box Evaluators](<llm-as-judge/Why You Can’t Trust Out-of-the-Box Evaluators.md>) · `llm-as-judge` · cresta
  Explains why generic evaluators often fail in production and why domain-specific calibration is needed.
- **2025-10-22** — [Large Reasoning Models Fail to Follow Instructions During Reasoning: A Benchmark Study](<benchmark-design/Large Reasoning Models Fail to Follow Instructions During Reasoning A Benchmark Study.md>) · `benchmark-design` · together
  Benchmark study showing instruction-following failures during reasoning.
- **2025-10-21** — [LLM Testing: A Practical Guide to Automated Testing for LLM Applications](<testing/LLM Testing A Practical Guide to Automated Testing for LLM Applications.md>) · `testing` · langfuse
  Practical guide to automated testing for LLM applications, covering test cases, regression checks, CI-style workflows, and quality gates.
- **2025-10-17** — [When to Use What: A Practical Guide to AI Agent Testing and Evaluation](<testing/When to Use What A Practical Guide to AI Agent Testing and Evaluation.md>) · `testing` · cresta
  Practical guide for choosing AI agent testing and evaluation methods based on deployment stage and risk.
- **2025-10-10** — [Measuring what matters: An intro to AI evals](<evaluation/Measuring what matters An intro to AI evals.md>) · `evaluation` · braintrust
  Intro to AI evals focused on choosing metrics that reflect product quality, building datasets, and measuring what matters for users.
- **2025-10-09** — [Evaluating Multi-Turn Conversations](<evaluation/Evaluating Multi-Turn Conversations.md>) · `evaluation` · langfuse
  Explains how to evaluate multi-turn conversations, including context retention, conversation-level scoring, and stateful failure modes.
- **2025-10-09** — [The New World of Non-Deterministic Testing and Evaluation](<testing/The New World of Non-Deterministic Testing and Evaluation.md>) · `testing` · cresta
  Explains why non-deterministic AI systems require different testing and evaluation methods than traditional software.
- **2025-10-08** — [Should I Use the Same LLM for My Eval as My Agent? Testing Self-Evaluation Bias](<llm-as-judge/Should I Use the Same LLM for My Eval as My Agent Testing Self-Evaluation Bias.md>) · `llm-as-judge` · arize
  Tests self-evaluation bias when using the same model for agent behavior and evaluation, with guidance for eval design.
- **2025-09-24** — [Testing Binary vs Score Evals on the Latest Models](<testing/Testing Binary vs Score Evals on the Latest Models.md>) · `testing` · arize
  Compares binary and score-based LLM evals across models to clarify tradeoffs in evaluator design.
- **2025-09-22** — [Traces are all you need](<evaluation/Traces are all you need.md>) · `evaluation` · fireworks
  Shows how to turn production traces into an internal model leaderboard with rollout processors and judge comparisons.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-05** — [Automated Evaluations of LLM Applications](<testing/Automated Evaluations of LLM Applications.md>) · `testing` · langfuse
  Guide to automated evaluations for LLM applications, including datasets, scorers, experiment runs, and continuous quality checks.
- **2025-09-03** — [A/B testing can't keep up with AI](<evaluation/AB testing can't keep up with AI.md>) · `evaluation` · braintrust
  Explains why traditional A/B testing is too slow for AI products and argues for eval-driven experimentation loops that compare model, prompt, and product changes before rollout.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-08-25** — [LLM Eval Driven Development with Claude Code](<evaluation/LLM Eval Driven Development with Claude Code.md>) · `evaluation` · fireworks
  Explains eval-driven development with Claude Code, using tests and feedback loops to improve coding-agent behavior.
- **2025-08-21** — [Annotation for Strong AI Evaluation Pipelines](<evaluation/Annotation for Strong AI Evaluation Pipelines.md>) · `evaluation` · arize
  Explains how human annotations support strong AI evaluation pipelines and how annotation data can be combined with evals in Phoenix workflows.
- **2025-08-15** — [Your AI Benchmark is Lying to You. Here's How We Caught It](<benchmark-design/Your AI Benchmark is Lying to You. Here's How We Caught It.md>) · `benchmark-design` · fireworks
  Explains how benchmark methodology can mislead model selection and how to evaluate models against real workload constraints.
- **2025-08-14** — [Test-driven agent development](<testing/Test-driven agent development.md>) · `testing` · fireworks
  Shows a TDD-style workflow for building agents with concrete acceptance tests, red teaming, and regression checks.
- **2025-08-12** — [TextQuests: How Good are LLMs at Text-Based Video Games?](<benchmark-design/TextQuests How Good are LLMs at Text-Based Video Games.md>) · `benchmark-design` · huggingface
  TextQuests evaluates LLM agents on 25 classic Infocom interactive-fiction games that need hundreds of precise actions over 30+ hours of play, testing long-horizon planning and long-context reasoning with no external tools. Scores both game progress and 'harm' (irreversible mistakes), and finds frontier models still struggle with sustained exploratory reasoning.
- **2025-07-18** — [LLM Observability for AI Agents and Applications](<monitoring/LLM Observability for AI Agents and Applications.md>) · `monitoring` · arize
  Introduces observability practices for LLM applications and agents, including monitoring signals beyond traditional metrics.
- **2025-07-17** — [Back to The Future: Evaluating AI Agents on Predicting Future Events](<benchmark-design/Back to The Future Evaluating AI Agents on Predicting Future Events (together).md>) · `benchmark-design` · together
  Introduces FutureBench for evaluating agents on predicting future events.
- **2025-07-17** — [Back to The Future: Evaluating AI Agents on Predicting Future Events](<benchmark-design/Back to The Future Evaluating AI Agents on Predicting Future Events.md>) · `benchmark-design` · huggingface
  FutureBench evaluates agents on predicting events that have not happened yet (news outcomes, prediction-market style questions), which makes benchmark contamination impossible by construction and makes results objectively verifiable once the future arrives. Describes the automated question-generation pipeline and rolling scoring of agents with web search.
- **2025-07-17** — [Five hard-learned lessons about AI evals](<evaluation/Five hard-learned lessons about AI evals.md>) · `evaluation` · braintrust
  Five practical lessons for building AI evals, emphasizing dataset quality, scorer design, failure analysis, and iteration over dashboard theater.
- **2025-07-14** — [Braintrust is not an eval framework](<monitoring/Braintrust is not an eval framework.md>) · `monitoring` · braintrust
  Argues that production AI quality needs a full observability and iteration system around evals, not only an isolated evaluation framework.
- **2025-07-10** — [Using Model-as-a-Judge for Reward in Reinforcement Finetuning](<llm-as-judge/Using Model-as-a-Judge for Reward in Reinforcement Finetuning.md>) · `llm-as-judge` · fireworks
  Explains using model-as-judge rewards for reinforcement fine-tuning and the evaluation risks involved.
- **2025-07-02** — [How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work](<evaluation/How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work.md>) · `evaluation` · modal
  Case study using evals and inference-time compute scaling to generate QR codes that satisfy visual and functional constraints.
- **2025-05-21** — [How we Built Scalable & Customizable Dashboards](<monitoring/How we Built Scalable & Customizable Dashboards.md>) · `monitoring` · langfuse
  Engineering writeup on building scalable customizable dashboards for observability data, covering query, rendering, and product architecture concerns.
- **2025-04-16** — [Introducing HELMET: Holistically Evaluating Long-context Language Models](<benchmark-design/Introducing HELMET Holistically Evaluating Long-context Language Models.md>) · `benchmark-design` · huggingface
  HELMET is a long-context benchmark spanning 7 application-centric categories (RAG, passage re-ranking, many-shot ICL, long-doc QA, summarization, cite/attribution) up to 128K tokens, built because synthetic probes like needle-in-a-haystack correlate poorly with real downstream long-context ability. Reports rankings that shift by category and shows open models lag closed ones most on tasks requiring full-context reasoning.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-04-03** — [Resilient observability by design](<monitoring/Resilient observability by design.md>) · `monitoring` · braintrust
  Describes resilient observability design for AI systems, including reliability considerations for storing, querying, and using production traces.
- **2025-03-27** — [Introducing End-to-End OpenTelemetry Support in LangSmith](<tracing/Introducing End-to-End OpenTelemetry Support in LangSmith.md>) · `tracing` · langchain
  Introduces end-to-end OpenTelemetry support in LangSmith for standardizing traces across AI application components.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2025-03-04** — [LLM Evaluation 101: Best Practices, Challenges & Proven Techniques](<evaluation/LLM Evaluation 101 Best Practices, Challenges & Proven Techniques.md>) · `evaluation` · langfuse
  Practical overview of LLM evaluation best practices, common challenges, scorer choices, datasets, and proven techniques for measuring application quality.
- **2025-02-26** — [Evaluating Large Language Models With OpenEvals](<llm-as-judge/Evaluating Large Language Models With OpenEvals.md>) · `llm-as-judge` · langchain
  Guide to evaluating large language models with OpenEvals, including reusable evaluators and model comparison workflows.
- **2025-02-10** — [The Open Arabic LLM Leaderboard 2](<benchmark-design/The Open Arabic LLM Leaderboard 2.md>) · `benchmark-design` · huggingface
  The Open Arabic LLM Leaderboard 2 rebuilds Arabic LLM evaluation around native (not machine-translated) datasets and centralized, reproducible evaluation to fix the integrity problem of self-reported scores. Describes the new benchmark mix (including the Balsam Index and native Arabic tasks) and the leaderboard's verification pipeline.
- **2025-02-07** — [Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud](<benchmark-design/Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud.md>) · `benchmark-design` · baseten
  Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark results.
- **2025-02-04** — [DABStep: Data Agent Benchmark for Multi-step Reasoning](<benchmark-design/DABStep Data Agent Benchmark for Multi-step Reasoning.md>) · `benchmark-design` · huggingface
  DABStep, built by Adyen and Hugging Face, is a benchmark of 450+ real multi-step data-analysis tasks over messy payments data that requires agents to write and execute code across heterogeneous files. Reports that frontier models solve only a small fraction of the hard split, and describes the easy/hard split and leak-resistant submission design.
- **2024-12-20** — [Evaluating Audio Reasoning with Big Bench Audio](<benchmark-design/Evaluating Audio Reasoning with Big Bench Audio.md>) · `benchmark-design` · huggingface
  Introduces Big Bench Audio, 1,000 audio questions adapted from Big Bench Hard, and measures a 'speech reasoning gap': GPT-4o scores 92% text-to-text but only 66% speech-to-speech, with Gemini 1.5 compared across S2S/S2T/T2S/T2T pipelines.
- **2024-12-04** — [Rethinking LLM Evaluation with 3C3H: AraGen Benchmark and Leaderboard](<benchmark-design/Rethinking LLM Evaluation with 3C3H AraGen Benchmark and Leaderboard.md>) · `benchmark-design` · huggingface
  AraGen's 3C3H measure scores an LLM response on Correctness, Completeness, Conciseness, Helpfulness, Honesty and Harmlessness via LLM-as-judge, combining them into one metric; the leaderboard also rotates a private Arabic eval set to resist contamination.
- **2024-12-04** — [What to do when a new AI model comes out](<evaluation/What to do when a new AI model comes out.md>) · `evaluation` · braintrust
  Playbook for responding when a new AI model ships: run targeted evals, compare cost and quality, inspect regressions, and decide rollout strategy.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<llm-as-judge/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `llm-as-judge` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-11-20** — [Introducing the Open Leaderboard for Japanese LLMs!](<benchmark-design/Introducing the Open Leaderboard for Japanese LLMs!.md>) · `benchmark-design` · huggingface
  The Open Japanese LLM Leaderboard evaluates models on 16+ llm-jp-eval tasks (NLI, translation, summarization, QA, code generation), motivated by Japanese-specific challenges like the three-script writing system and the absence of word boundaries for tokenization.
- **2024-11-20** — [Letting Large Models Debate: The First Multilingual LLM Debate Competition](<benchmark-design/Letting Large Models Debate The First Multilingual LLM Debate Competition.md>) · `benchmark-design` · huggingface
  BAAI's FlagEval Debate makes LLMs argue against each other as a dynamic eval, arguing that Chatbot-Arena-style setups lack discriminative power, never let models actually interact, and let style bias votes; uses a dual expert-plus-user scoring system across Chinese, English, Korean and Arabic.
- **2024-11-19** — [Judge Arena: Benchmarking LLMs as Evaluators](<llm-as-judge/Judge Arena Benchmarking LLMs as Evaluators.md>) · `llm-as-judge` · huggingface
  Launches Judge Arena, a crowdsourced side-by-side arena where humans vote between two LLM judges' scores and critiques, producing an ELO leaderboard of 18 open and proprietary LLM-as-a-judge models. Describes the judge-selection criteria and the prompt/scoring setup used for each battle.
- **2024-11-19** — [Instrumenting Your LLM Application: Arize Phoenix and Vercel AI SDK](<tracing/Instrumenting Your LLM Application Arize Phoenix and Vercel AI SDK.md>) · `tracing` · arize
  Shows how to instrument an LLM application with Phoenix and Vercel AI SDK so traces are available for debugging and evaluation.
- **2024-11-11** — [How to Improve LLM Safety and Reliability](<testing/How to Improve LLM Safety and Reliability.md>) · `testing` · arize
  Covers testing and monitoring practices for improving LLM application safety and reliability in production.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-10-28** — [Expert Support case study: Bolstering a RAG app with LLM-as-a-Judge](<llm-as-judge/Expert Support case study Bolstering a RAG app with LLM-as-a-Judge.md>) · `llm-as-judge` · huggingface
  Digital Green's agricultural advisory RAG chatbot for smallholder farmers adds an LLM-as-a-Judge evaluation loop, with judge prompt/criteria design and human-alignment checks used to iterate on retrieval and answer quality.
- **2024-10-23** — [Techniques for Self-Improving LLM Evals](<llm-as-judge/Techniques for Self-Improving LLM Evals.md>) · `llm-as-judge` · arize
  Covers techniques for making LLM evals self-improving through feedback, iteration, and evaluator refinement.
- **2024-10-17** — [I ran an eval. Now what?](<evaluation/I ran an eval. Now what.md>) · `evaluation` · braintrust
  Walks through what to do after an eval run: inspect failures, slice results, improve datasets and scorers, and turn findings into product or prompt changes.
- **2024-10-16** — [Tracing and Evaluating LangGraph Agents](<tracing/Tracing and Evaluating LangGraph Agents.md>) · `tracing` · arize
  Covers tracing and evaluation patterns for LangGraph agents, linking graph-based control flow with observability.
- **2024-10-14** — [OpenTelemetry (OTel) for LLM Observability](<tracing/OpenTelemetry (OTel) for LLM Observability.md>) · `tracing` · langfuse
  Introduces OpenTelemetry for LLM observability and how OTel-style traces can standardize spans, metadata, and interoperability across AI systems.
- **2024-10-08** — [The Role of OpenTelemetry (OTEL) in LLM Observability](<tracing/The Role of OpenTelemetry (OTEL) in LLM Observability.md>) · `tracing` · arize
  Explains OpenTelemetry’s role in LLM observability and why standard traces matter for production systems.
- **2024-10-07** — [Observability in Multi-Step LLM Systems](<tracing/Observability in Multi-Step LLM Systems.md>) · `tracing` · langfuse
  Explains observability needs for multi-step LLM systems, including tracing chains, tools, intermediate state, and failure points across complex application flows.
- **2024-09-30** — [Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations](<llm-as-judge/Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations.md>) · `llm-as-judge` · arize
  Best practices for choosing an LLM-as-judge evaluation model, including tradeoffs in evaluator quality and fit for task.
- **2024-09-16** — [Custom scoring functions in the Braintrust Playground](<llm-as-judge/Custom scoring functions in the Braintrust Playground.md>) · `llm-as-judge` · braintrust
  Explains custom scoring functions for evaluating AI outputs, including how domain-specific metrics can be added to an eval workflow.
- **2024-09-05** — [Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation](<evaluation/Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation.md>) · `evaluation` · arize
  Explains how to create and validate synthetic datasets for LLM evaluation and experimentation workflows.
- **2024-08-30** — [Evaluating an Image Classifier](<evaluation/Evaluating an Image Classifier.md>) · `evaluation` · arize
  Tutorial on evaluating an image classifier with Phoenix, using multimodal experiment and tracing workflows.
- **2024-08-16** — [Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges](<llm-as-judge/Judging the Judges Evaluating Alignment and Vulnerabilities in LLMs-as-Judges.md>) · `llm-as-judge` · arize
  Analyzes vulnerabilities and alignment issues in LLM-as-judge systems, with implications for production evaluator design.
- **2024-08-05** — [Beat GPT-4o at Python by searching with 100 dumb LLaMAs](<evaluation/Beat GPT-4o at Python by searching with 100 dumb LLaMAs.md>) · `evaluation` · modal
  Explores using many small Llama runs and search to improve Python benchmark performance against GPT-4o baselines.
- **2024-07-31** — [Llama 3.1: Same model, different results. The impact of a percentage point.](<benchmark-design/Llama 3.1 Same model, different results. The impact of a percentage point.md>) · `benchmark-design` · together
  Explains how small quality differences and deployment choices affect Llama 3.1 results.
- **2024-07-25** — [LAVE: Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning?](<benchmark-design/LAVE Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning.md>) · `benchmark-design` · huggingface
  Shows that exact-match VQA metrics (VQA Accuracy, ANLS, CIDEr, BLEU) unfairly punish correct out-of-distribution answers, and applies LAVE — an LLM-as-judge metric where Llama-2-7B-chat rates answers 1-3 with a rationale from in-context demonstrations — to evaluate MPLUGDocOwl1.5 zero-shot on Docmatix, where its ANLS collapses despite 84% on DocVQA.
- **2024-07-25** — [Different Ways to Instrument Your LLM Application](<tracing/Different Ways to Instrument Your LLM Application.md>) · `tracing` · arize
  Survey of instrumentation approaches for LLM applications, focused on tracing and observability setup choices.
- **2024-06-26** — [Aligning LLM-as-a-Judge with Human Preferences](<llm-as-judge/Aligning LLM-as-a-Judge with Human Preferences.md>) · `llm-as-judge` · langchain
  Covers aligning LLM-as-judge evaluators with human preferences through calibration, examples, and evaluation design.
- **2024-06-20** — [How to improve your evaluations](<evaluation/How to improve your evaluations.md>) · `evaluation` · braintrust
  Practical guide to improving evals through better examples, rubrics, scorers, slices, and investigation of failure cases.
- **2024-06-20** — [Managing and Monitoring Your Open Source LLM Applications](<monitoring/Managing and Monitoring Your Open Source LLM Applications.md>) · `monitoring` · arize
  Covers practical monitoring needs for open-source LLM applications, including operational metrics and deployment feedback.
- **2024-06-18** — [BigCodeBench: The Next Generation of HumanEval](<benchmark-design/BigCodeBench The Next Generation of HumanEval.md>) · `benchmark-design` · huggingface
  BigCodeBench replaces HumanEval with 1,140 function-level tasks that force LLMs to compose calls across 139 libraries, with rich test harnesses (average 5.6 test cases, 99% branch coverage) and both Complete and Instruct splits. Reports that instruction-tuned models drop sharply on the Instruct split and that even top models are ~20 points behind human performance.
- **2024-05-29** — [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](<benchmark-design/Trustworthy LLMs A Survey and Guideline for Evaluating Large Language Models' Alignment.md>) · `benchmark-design` · arize
  Survey-style guide to evaluating trustworthy and aligned LLM behavior across reliability, safety, and quality dimensions.
- **2024-05-24** — [CyberSecEval 2 - A Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models](<benchmark-design/CyberSecEval 2 - A Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models.md>) · `benchmark-design` · huggingface
  CyberSecEval 2 evaluates LLM cybersecurity risk: prompt injection, code interpreter abuse, offensive-security capability and insecure-code generation, plus a false-refusal-rate metric that quantifies the safety/helpfulness tradeoff.
- **2024-05-15** — [Pairwise Evaluations with LangSmith](<llm-as-judge/Pairwise Evaluations with LangSmith.md>) · `llm-as-judge` · langchain
  Explains pairwise evaluations with LangSmith for comparing model or prompt outputs using preference-style scoring.
- **2024-05-14** — [Introducing the Open Arabic LLM Leaderboard](<benchmark-design/Introducing the Open Arabic LLM Leaderboard.md>) · `benchmark-design` · huggingface
  The Open Arabic LLM Leaderboard evaluates models on native and human-verified translated Arabic benchmarks (AlGhafa, Arabic MMLU/EXAMS/ARC/HellaSwag), covering translation quality control and the dialect/culture gaps English benchmarks miss.
- **2024-05-13** — [Breaking Down EvalGen: Who Validates the Validators?](<llm-as-judge/Breaking Down EvalGen Who Validates the Validators.md>) · `llm-as-judge` · arize
  Deep dive on EvalGen and the problem of validating LLM-generated evaluators, including human review limitations and evaluator reliability.
- **2024-05-01** — [Regression Testing with LangSmith](<testing/Regression Testing with LangSmith.md>) · `testing` · langchain
  Explains regression testing with LangSmith for preventing LLM application quality regressions during prompt, model, or code changes.
- **2024-04-24** — [Getting started with automated evaluations](<testing/Getting started with automated evaluations.md>) · `testing` · braintrust
  Introductory guide to automated evaluations, covering datasets, scorers, experiments, and how to start measuring AI application quality.
- **2024-04-17** — [Eval feedback loops](<evaluation/Eval feedback loops.md>) · `evaluation` · braintrust
  Explains eval feedback loops where production observations and human review continuously improve prompts, datasets, and model behavior.
- **2024-04-16** — [Introducing the LiveCodeBench Leaderboard - Holistic and Contamination-Free Evaluation of Code LLMs](<benchmark-design/Introducing the LiveCodeBench Leaderboard - Holistic and Contamination-Free Evaluation of Code LLMs.md>) · `benchmark-design` · huggingface
  LiveCodeBench continuously scrapes date-stamped problems from LeetCode, AtCoder and Codeforces so models can be evaluated only on problems released after their training cutoff, making contamination detectable. Evaluates four scenarios — code generation, self-repair from error feedback, code execution (output prediction) and test-output prediction.
- **2024-03-24** — [Trace complex LLM applications with the Langfuse decorator (Python)](<tracing/Trace complex LLM applications with the Langfuse decorator (Python).md>) · `tracing` · langfuse
  Shows how to trace complex Python LLM applications with the Langfuse decorator, including nested calls, metadata, and observability patterns for multi-step workflows.
- **2024-03-14** — [Benchmarking fast Mistral 7B inference](<benchmark-design/Benchmarking fast Mistral 7B inference.md>) · `benchmark-design` · baseten
  Benchmarks Mistral 7B inference performance and the serving choices that affect throughput and latency.
- **2024-03-11** — [Iterating Towards LLM Reliability with Evaluation Driven Development](<testing/Iterating Towards LLM Reliability with Evaluation Driven Development.md>) · `testing` · langchain
  Explains evaluation-driven development for LLM reliability using regression tests, examples, and iterative quality gates.
- **2024-03-05** — [Introducing ConTextual: How well can your Multimodal model jointly reason over text and image in text-rich scenes?](<benchmark-design/Introducing ConTextual How well can your Multimodal model jointly reason over text and image in text-rich scenes.md>) · `benchmark-design` · huggingface
  ConTextual is a benchmark and leaderboard for context-sensitive text-rich visual reasoning (reading text in images to answer instructions); uses GPT-4 as judge plus human evaluation, showing a large gap between GPT-4V and open LMMs.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<benchmark-design/Predictive Human Preference From Model Ranking to Model Routing.md>) · `benchmark-design` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2024-02-23** — [Introducing the Red-Teaming Resistance Leaderboard](<benchmark-design/Introducing the Red-Teaming Resistance Leaderboard.md>) · `benchmark-design` · huggingface
  The Red-Teaming Resistance Leaderboard scores frontier LLMs on robustness against adversarial prompts drawn from real red-teaming datasets (AdvBench, AART, HarmBench, Beavertails, plus Haize's own attacks), reporting attack success rates per harm category rather than a single safety number.
- **2024-02-20** — [Introducing the Open Ko-LLM Leaderboard: Leading the Korean LLM Evaluation Ecosystem](<benchmark-design/Introducing the Open Ko-LLM Leaderboard Leading the Korean LLM Evaluation Ecosystem.md>) · `benchmark-design` · huggingface
  Upstage's Open Ko-LLM Leaderboard evaluates Korean LLMs on Ko-ARC/HellaSwag/MMLU/TruthfulQA plus a Korean commonsense benchmark, deliberately keeping test sets private to prevent contamination — a design lesson for any leaderboard.
- **2024-02-20** — [Evaluating and Analyzing Your RAG Pipeline with Ragas](<evaluation/Evaluating and Analyzing Your RAG Pipeline with Ragas.md>) · `evaluation` · arize
  Explains how to evaluate RAG pipelines with Ragas and Phoenix, including retrieval and generation quality dimensions.
- **2024-02-02** — [NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates](<benchmark-design/NPHardEval Leaderboard Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates.md>) · `benchmark-design` · huggingface
  NPHardEval grounds LLM reasoning evaluation in computational complexity classes: 900 auto-generated algorithmic questions (3 P, 3 NP-complete, 3 NP-hard tasks x 10 difficulty levels), refreshed monthly to defeat overfitting, scored by weighted accuracy and failure rate.
- **2024-01-31** — [How to benchmark image generation models like Stable Diffusion XL](<benchmark-design/How to benchmark image generation models like Stable Diffusion XL.md>) · `benchmark-design` · baseten
  Explains how to benchmark image-generation models with attention to quality, latency, and reproducibility.
- **2024-01-31** — [Introducing the Enterprise Scenarios Leaderboard: a Leaderboard for Real World Use Cases](<benchmark-design/Introducing the Enterprise Scenarios Leaderboard a Leaderboard for Real World Use Cases.md>) · `benchmark-design` · huggingface
  Patronus AI's Enterprise Scenarios Leaderboard evaluates LLMs on six real-world enterprise tasks — FinanceBench, Legal Confidentiality, Creative Writing, Customer Support Dialogue, Toxicity and Enterprise PII — with metrics like accuracy, engagingness, toxicity and PII leakage, arguing academic benchmarks miss enterprise failure modes.
- **2024-01-29** — [The Hallucinations Leaderboard, an Open Effort to Measure Hallucinations in Large Language Models](<benchmark-design/The Hallucinations Leaderboard, an Open Effort to Measure Hallucinations in Large Language Models.md>) · `benchmark-design` · huggingface
  The Hallucinations Leaderboard scores LLMs across in-context-learning tasks split into factuality (contradicting real-world facts) and faithfulness (contradicting the given context/instruction) hallucinations, spanning QA, summarization, fact-checking and self-consistency tasks.
- **2024-01-26** — [An Introduction to AI Secure LLM Safety Leaderboard](<benchmark-design/An Introduction to AI Secure LLM Safety Leaderboard.md>) · `benchmark-design` · huggingface
  The AI Secure LLM Safety Leaderboard runs the DecodingTrust benchmark, scoring models across eight trustworthiness axes (toxicity, stereotype bias, adversarial and out-of-distribution robustness, privacy leakage, machine ethics, fairness) rather than capability alone.
- **2024-01-12** — [A guide to setting up your own Hugging Face leaderboard: an end-to-end example with Vectara's hallucination leaderboard](<benchmark-design/A guide to setting up your own Hugging Face leaderboard an end-to-end example with Vectara's hallucination leaderboard.md>) · `benchmark-design` · huggingface
  End-to-end walkthrough of building a custom leaderboard on the HF leaderboard template (front-end Space + backend eval Space), using Vectara's HHEM hallucination-detection model to rank GPT-4/Gemini/Llama-2/Mistral by how often their summaries are unfaithful to the source document.
- **2024-01-12** — [Understanding performance benchmarks for LLM inference](<benchmark-design/Understanding performance benchmarks for LLM inference.md>) · `benchmark-design` · baseten
  Explains LLM inference performance benchmarks and how to interpret serving metrics.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<benchmark-design/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `benchmark-design` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
- **2023-10-17** — [Test Run Comparisons](<testing/Test Run Comparisons.md>) · `testing` · langchain
  Explains test-run comparisons for evaluating changes across LLM application versions and identifying regressions.
- **2023-10-02** — [LLM Tracing and Observability](<tracing/LLM Tracing and Observability.md>) · `tracing` · arize
  Explains LLM tracing and observability concepts using Phoenix as the concrete implementation context.
- **2023-09-12** — [It's time to build reliable AI](<evaluation/It's time to build reliable AI.md>) · `evaluation` · braintrust
  Early argument for reliable AI systems built around evals, logging, feedback loops, and engineering practices rather than ad hoc demos.
- **2023-05-25** — [Cross Validation: What You Need To Know, From the Basics To LLMs](<evaluation/Cross Validation What You Need To Know, From the Basics To LLMs.md>) · `evaluation` · arize
  Overview of cross-validation from classic ML through LLM applications, focused on evaluation methodology.
- **2023-05-17** — [Evaluating Model Fairness](<evaluation/Evaluating Model Fairness.md>) · `evaluation` · arize
  Explains model fairness evaluation and how to assess bias and fairness risks in production systems.
- **2022-02-07** — [Data Distribution Shifts and Monitoring](<monitoring/Data Distribution Shifts and Monitoring.md>) · `monitoring` · chip-huyen
  Taxonomy of covariate, label, and concept shifts with production monitoring strategies, data-quality checks, slice analysis, alerting tradeoffs, and examples of real-world ML failure modes.
- **2021-01-29** — [How We Reduced Our Labeling Cost by 10x](<evaluation/How We Reduced Our Labeling Cost by 10x.md>) · `evaluation` · cresta
  Explains how labeling costs were reduced through process and model-assisted annotation changes, relevant to eval dataset operations.

## Also relevant (filed elsewhere)

- **2026-07-21** — [A Fireside Chat with Cat and Thariq from the Claude Code team](<../agents/harness/A Fireside Chat with Cat and Thariq from the Claude Code team.md>) · `harness` · simon-willison
  Transcript of a fireside chat with Anthropic's Claude Code team covering Claude Tag's proactive multiplayer Slack agent with team memory (65% of product-eng PRs), a six-month migration to letting Claude fully review PRs at the 'outer layers' backed by incident-driven eval sets, an 80% system-prompt size cut for Fable/Opus 4.8 (fewer examples and hard constraints, more context), and how auto mode was red-teamed against prompt injection before becoming Claude Tag's foundation.
- **2026-07-20** — [Paper MCP vs Figma MCP for frontend agents - Blog - Braintrust](<../agents/tool-use/Paper MCP vs Figma MCP for frontend agents - Blog - Braintrust.md>) · `tool-use` · braintrust
  Independent eval of Paper MCP vs Figma MCP for coding-agent frontend generation across 40 Design2Code pages and 27 hand-picked complex designs: the two tie on visual similarity (0.741 vs 0.744 on simple pages), but Figma's run-to-run variance is 1.9x Paper's and it costs 32% more per point of visual quality ($3.73 vs $2.82) while running 42% longer.
- **2026-07-20** — [Heidi x Fireworks: Bridging the Gap in Frontier Model Performance](<../models/fine-tuning/Heidi x Fireworks Bridging the Gap in Frontier Model Performance.md>) · `fine-tuning` · fireworks
  Heidi's ambient clinical scribe moved from proprietary to fine-tuned open models on Fireworks: SFT beat Gemini Flash and RFT/DPO beat Gemini Pro on internal side-by-side evals, with the key levers being LLM-judge and synthetic-rewrite filtering of noisy preference data and scaling effective batch size from 64k to 768k tokens via gradient accumulation (win rate 48.0% to 51.3%).
- **2026-07-17** — [Prompt optimization and managed prompts in Pydantic Logfire](<../prompt-engineering/techniques/Prompt optimization and managed prompts in Pydantic Logfire.md>) · `techniques` · pydantic
  Describes Pydantic Logfire's prompt optimizer, which reads up to 100 recent production traces (failures weighted highest) via OpenTelemetry gen_ai spans, proposes a single evidence-cited prompt edit with a confidence ladder (prefer/always/never), rejects ungrounded claims via a validator, and separates prompt fixes from non-prompt issues like flaky providers or broken tools.
- **2026-07-17** — [Inside Cursor's agent factory: how it verifies AI-written code](<../product-engineering/case-studies/Inside Cursor's agent factory how it verifies AI-written code.md>) · `case-studies` · arize
  Details Cursor's verification architecture for AI-written code: risk scoring routes ~30-40% of PRs to merge without human review, behavioral video artifacts let reviewers inspect agent-exercised changes before the diff, and human corrections become rules/eval cases for its review agent Bugbot, with failed evals triggering diagnosis workflows with trace context attached.
- **2026-07-16** — [What does 99.9% uptime mean for inference?](<../inference/serving/What does 99.9% uptime mean for inference.md>) · `serving` · together
  Together breaks down what each reliability 'nine' actually requires for GPU inference serving, mapping failure domains (compute ECC errors, NIC/NVLink faults, storage, network, software/routing bugs) to the multi-region and AZ-redundancy architecture needed to survive them.
- **2026-07-14** — [From human-operated agent development to systematic agent improvement](<../agents/harness/From human-operated agent development to systematic agent improvement.md>) · `harness` · arize
  Translates an Arize Observe 2026 keynote into an architecture for automated agent improvement loops: managed reader/fixer/reviewer workers triage failures from OpenInference traces, harness-as-a-judge evaluates fixes, and fleet controls catch runaway or stuck sessions instead of a human pasting traces into a coding agent by hand.
- **2026-07-13** — [How do you make an LLM, anyway? Microsoft just published a textbook.](<../models/training/How do you make an LLM, anyway Microsoft just published a textbook.md>) · `training` · arize
  Walks through Microsoft's 109-page MAI-Thinking-1 technical report: a 1.2-trillion-page proprietary crawl filtered down and mixed to 54.6% code, a 30-trillion-token pretrain on 8,192 GPUs, a mid-training context-stretching phase (16K to 262K tokens), and RL post-training with anti-reward-hacking measures like time-traveled repo snapshots and test-file resets.
- **2026-07-10** — [What is a loop in AI engineering, anyway?](<../agents/harness/What is a loop in AI engineering, anyway.md>) · `harness` · arize
  Defines feedback loops in AI engineering and why loops are central to agent and eval system design.
- **2026-07-10** — [3 production patterns for AI agents and how to evaluate each one](<../agents/planning/3 production patterns for AI agents and how to evaluate each one.md>) · `planning` · arize
  Breaks production agents into local coding agents, in-app assistants, and operational agents, then maps each pattern to different harness, rollout, and evaluation needs.
- **2026-07-10** — **[Paper]** [Failure as a Process: An Anatomy of CLI Coding Agent Trajectories](<../agents/planning/[Paper] Failure as a Process An Anatomy of CLI Coding Agent Trajectories.md>) · `planning` · arxiv
  Empirical study of how CLI coding agents fail as a *process* rather than an outcome: 3,843 trajectories from 7 frontier models across 3 scaffolds (OpenHands, MiniSWE, Terminus2) on Terminal-Bench, with 1,794 valid ones hand-annotated over 63,000 execution steps. Finds failures are driven mainly by epistemic errors, begin within the first few steps, and stay hidden until recovery is impossible — arguing for early validation and intervention instead of final-outcome evaluation.
- **2026-07-10** — [Evaluating the GPT-5.6 family](<../models/benchmarks/Evaluating the GPT-5.6 family.md>) · `benchmarks` · braintrust
  Evaluates the GPT-5.6 model family and presents a decision map for choosing models based on quality, cost, and task requirements.
- **2026-07-09** — [Evaluating speech-to-text models](<../models/multimodal/Evaluating speech-to-text models.md>) · `multimodal` · braintrust
  Evaluates speech-to-text models for voice AI workflows, covering datasets, scoring, and tradeoffs in transcription quality.
- **2026-07-09** — [Trace before you migrate: Measuring Kubernetes bottlenecks in AI agent sandboxes](<../infra-platform/deployment/Trace before you migrate Measuring Kubernetes bottlenecks in AI agent sandboxes.md>) · `deployment` · arize
  Shows how tracing can diagnose Kubernetes bottlenecks in AI agent sandboxes before migration decisions.
- **2026-07-08** — [Tuning the harness, not the model: a Nemotron 3 Ultra playbook](<../agents/harness/Tuning the harness, not the model a Nemotron 3 Ultra playbook.md>) · `harness` · langchain
  Nemotron 3 Ultra playbook arguing for harness tuning over model tuning, with practical agent-system design and eval implications.
- **2026-07-08** — [Rewriting Bun in Rust](<../product-engineering/case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-07** — **[Paper]** [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](<../agents/planning/[Paper] Beyond the Leaderboard A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents.md>) · `planning` · arxiv
  Synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026) across 19 benchmarks into a unified taxonomy of LLM-agent failure, with six clusters: tool-invocation/parameter errors, planning and constraint-satisfaction failures, long-horizon degradation from context accumulation, multi-agent coordination breakdown, safety failures under adversarial or underspecified conditions, and measurement-validity problems. Finds failures compound nonlinearly with task length, strong sub-task scores do not predict end-to-end success, and extra scaffolding does not reliably improve reliability.
- **2026-07-07** — [Faster phrase search with shingled bloom filters in Brainstore](<../rag-retrieval/search/Faster phrase search with shingled bloom filters in Brainstore.md>) · `search` · braintrust
  Explains faster phrase search over Brainstore data using shingled bloom filters, aimed at efficient trace and log search for AI observability.
- **2026-07-07** — [How Schneider Electric Built Their LLMOps Foundations With LangSmith](<../product-engineering/case-studies/How Schneider Electric Built Their LLMOps Foundations With LangSmith.md>) · `case-studies` · langchain
  Schneider Electric case study on building enterprise LLMOps foundations with LangSmith at scale.
- **2026-07-06** — [Own the loop: A field guide to agent harnesses](<../agents/harness/Own the loop A field guide to agent harnesses.md>) · `harness` · arize
  Field guide to owning the agent harness loop, from task control to measurement and iteration.
- **2026-07-06** — [Evaluating the USA vs Belgium World Cup matchup](<../agents/tool-use/Evaluating the USA vs Belgium World Cup matchup.md>) · `tool-use` · braintrust
  Uses a USA vs Belgium matchup example to evaluate web research agents, illustrating task design and judging for tool-using research workflows.
- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<../agents/tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-04** — [Better Models: Worse Tools](<../agents/tool-use/Better Models Worse Tools.md>) · `tool-use` · simon-willison
  Short analysis of newer coding models producing malformed arguments for third-party edit tools, raising the issue that tool schemas and edit mechanisms may need model-specific evaluation and adaptation.
- **2026-07-02** — [From World Cup matchups to research maps: evaluating Parallel's web research agents](<../agents/tool-use/From World Cup matchups to research maps evaluating Parallel's web research agents.md>) · `tool-use` · braintrust
  Evaluates Parallel web research agents using World Cup matchups and research-map tasks, connecting tool use, knowledge graphs, and answer quality.
- **2026-07-02** — [Observability MCP comparison: Pydantic Logfire, ClickStack, LangSmith, Braintrust, Galileo, Phoenix, and Langfuse](<../agents/tool-use/Observability MCP comparison Pydantic Logfire, ClickStack, LangSmith, Braintrust, Galileo, Phoenix, and Langfuse.md>) · `tool-use` · pydantic
  Compares the MCP servers of seven observability platforms (Logfire, ClickStack, LangSmith, Braintrust, Galileo, Phoenix, Langfuse) on whether an agent can ask a debugging question directly and get bounded, verifiable evidence, arguing MCP tool design should return compact aggregates rather than pages of raw trace objects that burn the context window.
- **2026-07-01** — [How Pendo uses LangSmith to trace Novus from user behavior to code fixes](<../product-engineering/case-studies/How Pendo uses LangSmith to trace Novus from user behavior to code fixes.md>) · `case-studies` · langchain
  Pendo case study tracing Novus from user behavior to code fixes, showing how traces connect product signals to agent improvements.
- **2026-06-29** — [How Candidly Built State-Aware Agent Harnesses with LangSmith](<../product-engineering/case-studies/How Candidly Built State-Aware Agent Harnesses with LangSmith.md>) · `case-studies` · langchain
  Candidly case study on building state-aware agent harnesses with LangSmith for production agent workflows.
- **2026-06-26** — [Building an auditable VC research agent with the Perplexity Agent API and LangGraph](<../agents/tool-use/Building an auditable VC research agent with the Perplexity Agent API and LangGraph.md>) · `tool-use` · langchain
  Walkthrough for building an auditable VC research agent with Perplexity, LangGraph, and LangSmith, emphasizing traceability and review.
- **2026-06-24** — [Using Braintrust to eval agentic setups from large-scale Hugging Face data](<../agents/planning/Using Braintrust to eval agentic setups from large-scale Hugging Face data.md>) · `planning` · braintrust
  Uses large-scale Hugging Face agent traces to evaluate agentic setups, connecting trace analysis to agent behavior and reliability measurement.
- **2026-06-19** — [Why AI token costs don't tell you if your AI is working](<../infra-platform/cost/Why AI token costs don't tell you if your AI is working.md>) · `cost` · arize
  Explains why token cost alone is an incomplete production metric and how quality, latency, and outcomes must be measured together.
- **2026-06-17** — [How to test agent cost-efficiency with Braintrust](<../infra-platform/cost/How to test agent cost-efficiency with Braintrust.md>) · `cost` · braintrust
  Explains how to test agent cost-efficiency by measuring task success against token, model, and tool-use costs.
- **2026-06-16** — [What is agent orchestration? Frameworks, runtimes, and observability explained](<../agents/harness/What is agent orchestration Frameworks, runtimes, and observability explained.md>) · `harness` · arize
  Explains agent orchestration across frameworks, runtimes, and observability concerns.
- **2026-06-11** — [Cresta Conductor: The Agent for AI Agent Development](<../agents/planning/Cresta Conductor The Agent for AI Agent Development.md>) · `planning` · cresta
  Introduces an agent used to help develop other AI agents, with lessons around orchestration, testing, and iteration workflows.
- **2026-06-09** — [AI spend is the new headcount: why cost control is an observability problem](<../infra-platform/cost/AI spend is the new headcount why cost control is an observability problem.md>) · `cost` · pydantic
  Frames LLM/agent spend as headcount-shaped (usage-scaled, salary-magnitude) rather than SaaS-shaped, arguing cost governance is really an observability problem: attribute spend per agent, per user, per session from traces (via the genai-prices dataset) and ask 'was this run worth what it cost?'.
- **2026-06-09** — [How to detect credential theft in AI agent harness traces](<../product-engineering/security/How to detect credential theft in AI agent harness traces.md>) · `security` · arize
  Shows how agent harness traces can expose credential theft and other security failures during tool use.
- **2026-06-09** — [AI is eating the AI engineering loop](<../industry/trends/AI is eating the AI engineering loop.md>) · `trends` · langfuse
  Argues that AI is reshaping the AI engineering loop itself, with agents increasingly participating in prompt, eval, observability, and product iteration workflows.
- **2026-06-05** — [Your AI bill is out of control. Cloudflare can fix it now.](<../infra-platform/cost/Your AI bill is out of control. Cloudflare can fix it now.md>) · `cost` · cloudflare-ai
  AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven budgets and model routing via Cloudflare Access, so enterprises can attribute LLM spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for interns) instead of one opaque shared API key.
- **2026-06-03** — [How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith](<../product-engineering/case-studies/How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith.md>) · `case-studies` · langchain
  Harmonic case study on rebuilding Scout with Deep Agents and LangSmith, linking agent architecture to retention and evaluation.
- **2026-06-02** — [The end of fine-tuning: Why evals, context, and traces matter more](<../models/fine-tuning/The end of fine-tuning Why evals, context, and traces matter more.md>) · `fine-tuning` · arize
  Argues that evals, context, and traces can reduce the need for fine-tuning in many production AI workflows.
- **2026-05-29** — [How to build a better agent harness with traces and evals](<../agents/planning/How to build a better agent harness with traces and evals.md>) · `planning` · arize
  Shows how traces and evals combine inside an agent harness to make agent behavior easier to test and improve.
- **2026-05-27** — [How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith](<../product-engineering/case-studies/How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Lyft case study on building a self-serve AI agent platform for customer support with LangGraph and LangSmith.
- **2026-05-26** — [How to ship a local LLM that matches frontier LLMs with evals and prompt engineering](<../models/fine-tuning/How to ship a local LLM that matches frontier LLMs with evals and prompt engineering.md>) · `fine-tuning` · arize
  Explains how evals and prompt engineering can make smaller local models viable substitutes for frontier models on constrained tasks.
- **2026-05-26** — [Mission Control for Self-Hosted LangSmith on Kubernetes](<../infra-platform/deployment/Mission Control for Self-Hosted LangSmith on Kubernetes.md>) · `deployment` · langchain
  Guide to operating self-hosted LangSmith on Kubernetes, covering deployment, operations, and control-plane concerns.
- **2026-05-21** — [The six generations of AI agents and how to eval them](<../agents/planning/The six generations of AI agents and how to eval them.md>) · `planning` · braintrust
  Taxonomy of six generations of AI agents and guidance for evaluating each generation's capabilities, failure modes, and production readiness.
- **2026-05-19** — [Building a self-improving agent on a context graph of human disagreement](<../agents/memory-context/Building a self-improving agent on a context graph of human disagreement.md>) · `memory-context` · arize
  Shows how a context graph of human disagreement can support a self-improving agent loop.
- **2026-05-19** — [How We Built LangSmith Engine, Our Agent for Improving Agents](<../agents/planning/How We Built LangSmith Engine, Our Agent for Improving Agents.md>) · `planning` · langchain
  Explains LangSmith Engine, an agent for improving agents through trace analysis, feedback, evals, and iterative changes.
- **2026-05-18** — [Voice AI is only as good as what it hears](<../models/multimodal/Voice AI is only as good as what it hears.md>) · `multimodal` · sierra
  Explains why voice-agent quality depends on transcription accuracy and how hearing failures propagate into agent behavior.
- **2026-05-13** — [We built SmithDB, the data layer for agent observability](<../infra-platform/deployment/We built SmithDB, the data layer for agent observability.md>) · `deployment` · langchain
  Introduces SmithDB as a data layer for agent observability, optimized for storing and querying trace-heavy workloads.
- **2026-05-12** — [Explorer: The agent-optimizing agent](<../agents/planning/Explorer The agent-optimizing agent.md>) · `planning` · sierra
  Introduces Explorer as an agent-optimizing agent that analyzes conversations and identifies improvement opportunities for deployed agents.
- **2026-05-12** — [The Agent Development Life Cycle](<../agents/planning/The Agent Development Life Cycle.md>) · `planning` · sierra
  Defines an agent development lifecycle from design and simulation through evaluation, deployment, monitoring, and continuous improvement.
- **2026-05-12** — [Models got an order of magnitude better at following instructions in one year](<../models/benchmarks/Models got an order of magnitude better at following instructions in one year.md>) · `benchmarks` · arize
  Analyzes instruction-following benchmark changes and what they imply for tracking model quality over time.
- **2026-05-12** — [Golden articles: Evaluating and improving search](<../rag-retrieval/search/Golden articles Evaluating and improving search.md>) · `search` · sierra
  Covers golden-article evaluation for search quality and how retrieval systems can be measured and improved for support agents.
- **2026-05-12** — [Load testing: how Sierra scales for surges](<../infra-platform/deployment/Load testing how Sierra scales for surges.md>) · `deployment` · sierra
  Explains load testing for agent systems so conversation serving can scale through traffic surges without quality or latency collapse.
- **2026-05-09** — [The Agent Development Lifecycle: Build, Test, Deploy & Monitor AI Agents](<../agents/planning/The Agent Development Lifecycle Build, Test, Deploy & Monitor AI Agents.md>) · `planning` · langchain
  Defines the agent development lifecycle from build and test through deployment, monitoring, and iterative improvement.
- **2026-05-07** — [Agent harnesses have an expiration date](<../agents/harness/Agent harnesses have an expiration date.md>) · `harness` · arize
  Argues that agent harnesses need lifecycle management as tools, models, and objectives drift, with implications for ongoing evaluation.
- **2026-05-05** — [PostgreSQL Triggers vs Async Audit Logs: A Pydantic Logfire Migration](<../product-engineering/architecture/PostgreSQL Triggers vs Async Audit Logs A Pydantic Logfire Migration.md>) · `architecture` · pydantic
  Migrating Logfire's audit logging from synchronous PostgreSQL triggers to async event-based logs, covering reliability, write-path performance, and capturing who-did-what context without blocking the request.
- **2026-05-01** — [MCP vs. CLI Skills for agents: what our eval found (and which you should use)](<../agents/tool-use/MCP vs. CLI Skills for agents what our eval found (and which you should use).md>) · `tool-use` · arize
  Compares MCP and CLI skills for agents using evaluation results, focusing on reliability and tool interface design.
- **2026-04-27** — [How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements](<../product-engineering/security/How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements.md>) · `security` · langchain
  Connects LangSmith and LangChain OSS workflows to EU AI Act readiness, including observability, evaluation, governance, and auditability.
- **2026-04-24** — [What is an agent harness?](<../agents/harness/What is an agent harness.md>) · `harness` · arize
  Defines an agent harness and the responsibilities it carries for control flow, state, tools, and testing.
- **2026-04-20** — [Code is free, technical debt isn’t: Notes from AI Engineer Europe](<../industry/trends/Code is free, technical debt isn’t Notes from AI Engineer Europe.md>) · `trends` · arize
  AI Engineer Europe notes arguing that faster code generation increases the need for verification, standards, and technical-debt management.
- **2026-04-16** — [Harnesses are everything. Here's how to optimize yours.](<../agents/harness/Harnesses are everything. Here's how to optimize yours.md>) · `harness` · baseten
  Explains why agent harness design matters and how to optimize harnesses for reliable agent behavior.
- **2026-04-15** — [Automation Discovery: Designing Systems to Extract Blueprints from Conversation Data](<../product-engineering/architecture/Automation Discovery Designing Systems to Extract Blueprints from Conversation Data.md>) · `architecture` · cresta
  Describes systems that mine conversation data to discover automation opportunities and generate process blueprints.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<../agents/planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-04-13** — [EinsteinArena: Harnessing the collective intelligence of agents in the wild to advance science](<../agents/multi-agent/EinsteinArena Harnessing the collective intelligence of agents in the wild to advance science.md>) · `multi-agent` · together
  Explains EinsteinArena for using collective agent intelligence to advance scientific tasks.
- **2026-04-13** — [How to prepare for AI compliance and governance](<../product-engineering/security/How to prepare for AI compliance and governance.md>) · `security` · braintrust
  Connects AI compliance and governance to engineering controls such as observability, audit trails, data boundaries, review workflows, and policy enforcement.
- **2026-04-04** — [How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours](<../rag-retrieval/pipelines/How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours.md>) · `pipelines` · arize
  Uses an eval-guided RAG improvement loop to show how retrieval recall can be diagnosed and improved quickly.
- **2026-03-31** — [Logfire vs LangSmith vs Langfuse vs Arize: AI Observability Pricing Compared](<../infra-platform/cost/Logfire vs LangSmith vs Langfuse vs Arize AI Observability Pricing Compared.md>) · `cost` · pydantic
  Breaks down how AI-observability billing units (spans, traces, GB ingested, Langfuse-style billable units) interact with agentic/RAG workloads, noting LLM spans carry tens of KB payloads (system prompts, retrieved chunks, completions) versus sub-KB REST spans. Compares Logfire, LangSmith, Langfuse, and Arize pricing to show the billing unit, not the headline fee, drives real cost.
- **2026-03-30** — [Building IaC providers for Logfire: design decisions that mattered](<../infra-platform/deployment/Building IaC providers for Logfire design decisions that mattered.md>) · `deployment` · pydantic
  Design decisions in building Terraform/IaC providers for Logfire so customers manage alerts, dashboards, projects, and tokens as code, including how to model observability resources for declarative provisioning.
- **2026-03-27** — [Evals are the new PRD](<../product-engineering/architecture/Evals are the new PRD.md>) · `architecture` · braintrust
  Argues that evals can act as executable product requirements for AI systems, aligning teams around expected behavior and measurable quality.
- **2026-03-25** — [Full-Stack Agent Observability with AgentSH + Pydantic Logfire | Pydantic](<../product-engineering/security/Full-Stack Agent Observability with AgentSH + Pydantic Logfire Pydantic.md>) · `security` · pydantic
  Pairs LLM-level tracing (model calls, tool invocations) with AgentSH's OS-boundary auditing of what an agent actually did on the machine (file access, network connections, process execution) plus policy enforcement, both emitted as OpenTelemetry into one timeline to catch failures in the 'seams'.
- **2026-03-17** — [Evals for PMs: A practical guide to AI product quality](<../product-engineering/ux-patterns/Evals for PMs A practical guide to AI product quality.md>) · `ux-patterns` · braintrust
  Practical guide for product managers defining AI product quality with evals, user-centered criteria, examples, and iteration loops.
- **2026-03-10** — [Simplifying Langfuse for Scale](<../infra-platform/deployment/Simplifying Langfuse for Scale.md>) · `deployment` · langfuse
  Architecture case study on simplifying Langfuse for scale, covering operational complexity, storage and compute boundaries, and reliability improvements.
- **2026-03-05** — [When the Call Runs Too Long: Modeling Outcomes for Long Conversations](<../models/reasoning/When the Call Runs Too Long Modeling Outcomes for Long Conversations.md>) · `reasoning` · cresta
  Discusses modeling outcomes for long conversations, including challenges around sequence length and delayed success signals.
- **2026-02-23** — [How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System (MAS)](<../agents/multi-agent/How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System (MAS).md>) · `multi-agent` · cresta
  Case study on scaling data annotation with a human-supervised multi-agent system, including review and quality-control loops.
- **2026-02-23** — [How speech models fail where it matters the most and what to do about it](<../models/multimodal/How speech models fail where it matters the most and what to do about it.md>) · `multimodal` · together
  Analyzes speech model failure modes that matter for production applications.
- **2026-02-18** — [monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1](<../product-engineering/case-studies/monday Service + LangSmith Building a Code-First Evaluation Strategy from Day 1.md>) · `case-studies` · langchain
  monday Service case study on building a code-first evaluation strategy for AI product quality from day one.
- **2026-02-16** — [Using Agent Skills to Automatically Improve your Prompts](<../prompt-engineering/techniques/Using Agent Skills to Automatically Improve your Prompts.md>) · `techniques` · langfuse
  Shows how agent skills can automatically improve prompts, using evaluation feedback and reusable agent workflows to iterate on prompt quality.
- **2026-02-13** — [On Agent Frameworks and Agent Observability](<../agents/harness/On Agent Frameworks and Agent Observability.md>) · `harness` · langchain
  Connects agent-framework design with observability requirements, arguing that runtime structure determines what teams can debug and evaluate.
- **2026-02-12** — [OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments](<../agents/tool-use/OpenEnv in Practice Evaluating Tool-Using Agents in Real-World Environments.md>) · `tool-use` · huggingface
  Turing's Calendar Gym on Meta/HF's OpenEnv: a gym-style (reset/step/action/observation) environment exposing real calendar tools over MCP, with ACL-based access control, partial visibility and multi-step dependencies, used to evaluate tool-using agents against real systems rather than simulations — and reporting where current agents fail (permission errors, wrong action ordering).
- **2026-02-03** — [How to build a production agentic app, the Pydantic Way](<../product-engineering/architecture/How to build a production agentic app, the Pydantic Way.md>) · `architecture` · pydantic
  End-to-end guide to structuring a production agentic app on the Pydantic stack: FastAPI to expose the agent, Pydantic AI for the agent loop, Logfire for observability, and Pydantic Evals for evaluation, with reasoning on when to use an agent framework vs. the raw LLM SDK.
- **2026-02-02** — [Fine-tuning open LLM judges to outperform GPT-5.2](<../models/reinforcement-learning/Fine-tuning open LLM judges to outperform GPT-5.2.md>) · `reinforcement-learning` · together
  Explains fine-tuning open LLM judges to outperform a frontier judge model.
- **2026-02-02** — [Automated Prompt Optimization with GEPA, Pydantic AI, and Pydantic Evals](<../prompt-engineering/techniques/Automated Prompt Optimization with GEPA, Pydantic AI, and Pydantic Evals.md>) · `techniques` · pydantic
  Walks through automated prompt optimization with GEPA's evolutionary/reflective algorithm driven by Pydantic Evals as the scoring harness, using Agent.override() to inject candidate prompts without modifying agent definitions, turning manual prompt iteration into a systematic search of the prompt space against defined success criteria.
- **2026-01-22** — [Testing if "bash is all you need"](<../agents/tool-use/Testing if bash is all you need.md>) · `tool-use` · braintrust
  Tests whether bash-oriented agents can solve realistic tasks, using evals to measure command-line tool use and agent reliability.
- **2026-01-20** — [Building observable AI agents with Temporal](<../agents/tool-use/Building observable AI agents with Temporal.md>) · `tool-use` · braintrust
  Shows how Temporal workflows can make AI agents observable, connecting durable execution with traces, evals, and debugging data.
- **2026-01-08** — [How Context Graphs Turn Agent Traces Into Durable Business Assets](<../agents/memory-context/How Context Graphs Turn Agent Traces Into Durable Business Assets.md>) · `memory-context` · arize
  Describes context graphs as a way to transform agent traces into durable memory and operational knowledge assets.
- **2026-01-01** — [How Dropbox built an evaluation pipeline for AI search](<../rag-retrieval/search/How Dropbox built an evaluation pipeline for AI search.md>) · `search` · braintrust
  Case study of Dropbox's evaluation pipeline for AI search, focused on measuring retrieval and answer quality for production search experiences.
- **2026-01-01** — [How Coursera builds next-generation learning tools](<../product-engineering/case-studies/How Coursera builds next-generation learning tools.md>) · `case-studies` · braintrust
  Customer case study on Coursera's next-generation learning tools and how evaluation workflows support quality for education-focused AI features.
- **2026-01-01** — [How Fintool generates millions of financial insights](<../product-engineering/case-studies/How Fintool generates millions of financial insights.md>) · `case-studies` · braintrust
  Case study of Fintool generating financial insights at scale, using evaluation and observability to manage quality in high-volume AI workflows.
- **2026-01-01** — [How Loom auto-generates video titles](<../product-engineering/case-studies/How Loom auto-generates video titles.md>) · `case-studies` · braintrust
  Case study of Loom auto-generating video titles and using evals to improve a production AI feature's usefulness and quality.
- **2026-01-01** — [How Portola empowers subject matter experts to improve AI quality](<../product-engineering/case-studies/How Portola empowers subject matter experts to improve AI quality.md>) · `case-studies` · braintrust
  Case study of Portola using subject-matter experts to improve AI quality through review workflows, datasets, and eval-driven iteration.
- **2026-01-01** — [How Retool uses Loop to turn logs into AI roadmap decisions](<../product-engineering/case-studies/How Retool uses Loop to turn logs into AI roadmap decisions.md>) · `case-studies` · braintrust
  Case study of Retool using production logs and Loop-style review to turn AI usage data into roadmap and quality decisions.
- **2026-01-01** — [How Zapier builds production-ready AI products](<../product-engineering/case-studies/How Zapier builds production-ready AI products.md>) · `case-studies` · braintrust
  Case study of Zapier building production-ready AI products with observability, evals, and feedback loops across real customer workflows.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<../product-engineering/security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-12-19** — [Evaluating AI Voices – What Does It Mean to Sound “Good”?](<../models/multimodal/Evaluating AI Voices – What Does It Mean to Sound “Good”.md>) · `multimodal` · cresta
  Explores how to evaluate AI voice quality beyond subjective preference, including production criteria for speech experiences.
- **2025-12-17** — [Self-Improving Agents, Powered by Your Evals](<../agents/planning/Self-Improving Agents, Powered by Your Evals.md>) · `planning` · fireworks
  Describes self-improving agents powered by eval loops, using evaluation feedback to improve behavior.
- **2025-11-25** — [Vibe Coding a Custom Annotation UI](<../product-engineering/ux-patterns/Vibe Coding a Custom Annotation UI.md>) · `ux-patterns` · langfuse
  Case study of building a custom annotation UI for eval workflows with AI-assisted coding, highlighting review ergonomics and human feedback collection.
- **2025-11-20** — [Eval Protocol: RL on your agents, in any environment](<../models/reinforcement-learning/Eval Protocol RL on your agents, in any environment.md>) · `reinforcement-learning` · fireworks
  Describes using Eval Protocol to run reinforcement learning on agents in task environments.
- **2025-11-20** — [Incident Report for Nov 18, 2025](<../infra-platform/deployment/Incident Report for Nov 18, 2025.md>) · `deployment` · langfuse
  Incident report with reliability lessons for production observability infrastructure, including failure analysis and operational follow-up.
- **2025-11-19** — [How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry](<../product-engineering/security/How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry.md>) · `security` · arize
  Explains how red-team agents can be used to find and test security weaknesses in agentic applications.
- **2025-11-17** — [GEPA vs Prompt Learning: Benchmarking Different Prompt Optimization Approaches](<../prompt-engineering/techniques/GEPA vs Prompt Learning Benchmarking Different Prompt Optimization Approaches.md>) · `techniques` · arize
  Benchmarks GEPA against prompt learning and frames prompt optimization as an eval-driven engineering loop.
- **2025-10-31** — [Genspark deep research agent with Fireworks RFT](<../models/reinforcement-learning/Genspark deep research agent with Fireworks RFT.md>) · `reinforcement-learning` · fireworks
  Case study of reinforcement fine-tuning a deep research agent to improve quality, tool calls, and cost.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<../prompt-engineering/techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-10-28** — [RAG Observability and Evals](<../rag-retrieval/pipelines/RAG Observability and Evals.md>) · `pipelines` · langfuse
  Explains observability and evaluation for RAG systems, including tracing retrieval/generation steps and measuring answer and context quality.
- **2025-10-01** — [Introducing RTEB: A New Standard for Retrieval Evaluation](<../rag-retrieval/embeddings/Introducing RTEB A New Standard for Retrieval Evaluation.md>) · `embeddings` · huggingface
  RTEB is a retrieval benchmark that mixes open and permanently-private held-out datasets, so a model's gap between public and private scores exposes overfitting to MTEB-style public leaderboards. Covers the dataset selection across domains/languages, the private-eval protocol, and evidence that several leaderboard-topping embedding models generalize worse than their public scores suggest.
- **2025-09-29** — [Claude Sonnet 4.5 analysis](<../models/benchmarks/Claude Sonnet 4.5 analysis.md>) · `benchmarks` · braintrust
  Analyzes Claude Sonnet 4.5 with aspirational evals, focusing on how harder task suites reveal model strengths and gaps beyond standard benchmarks.
- **2025-09-17** — [A postmortem of three recent issues](<../inference/serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-17** — [adb Benchmarks](<../infra-platform/deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-09-11** — [Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith](<../product-engineering/case-studies/Monte Carlo Building Data + AI Observability Agents with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Monte Carlo case study on building data and AI observability agents with LangGraph and LangSmith.
- **2025-09-08** — [Cresta’s Three Strategic Pillars of AI Agent Defense for Enterprise Security and Compliance](<../product-engineering/security/Cresta’s Three Strategic Pillars of AI Agent Defense for Enterprise Security and Compliance.md>) · `security` · cresta
  Frames AI agent defense around enterprise security, compliance, testing, and operational safeguards.
- **2025-08-26** — [Building production-ready agentic systems: Lessons from Shopify Sidekick (2025)](<../agents/harness/Building production-ready agentic systems Lessons from Shopify Sidekick (2025).md>) · `harness` · shopify
  ICML 2025 talk on building Shopify Sidekick as a production agentic system: architecture, LLM-based evaluation, and GRPO reinforcement-learning training for a merchant-facing AI assistant.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<../prompt-engineering/techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<../infra-platform/deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-08-08** — [GPT-5 vs. Claude Opus 4.1](<../models/benchmarks/GPT-5 vs. Claude Opus 4.1.md>) · `benchmarks` · braintrust
  Compares GPT-5 and Claude Opus 4.1 with eval-driven analysis of strengths, weaknesses, and model-selection implications.
- **2025-08-06** — [Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI](<../rag-retrieval/pipelines/Grounding Reality – How Cresta Tackles LLM Hallucinations in Enterprise AI.md>) · `pipelines` · cresta
  Explains grounding strategies for reducing hallucinations in enterprise AI systems, with emphasis on knowledge and evaluation loops.
- **2025-07-18** — [Prompt Learning: Using English Feedback to Optimize LLM Systems](<../prompt-engineering/techniques/Prompt Learning Using English Feedback to Optimize LLM Systems.md>) · `techniques` · arize
  Explains prompt learning driven by natural-language feedback as an optimization loop for LLM systems.
- **2025-07-15** — [Building reliable AI agents](<../agents/planning/Building reliable AI agents.md>) · `planning` · baseten
  Covers practical design patterns for building more reliable AI agents.
- **2025-06-18** — [Introducing Roast: Structured AI workflows made easy (2025)](<../agents/harness/Introducing Roast Structured AI workflows made easy (2025).md>) · `harness` · shopify
  Shopify open-sources Roast, a framework for structured AI workflows, built to grade and optimize unit tests at scale with minimal human intervention after finding ad-hoc AI workflows hard to maintain.
- **2025-06-13** — [How we built our multi-agent research system](<../agents/multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-06-04** — [Synthetic data pipeline for fine-tuning and evaluation](<../models/fine-tuning/Synthetic data pipeline for fine-tuning and evaluation.md>) · `fine-tuning` · fireworks
  Describes a synthetic-data pipeline that connects task definition, generation, SFT/RFT, evaluation, and cleanup.
- **2025-05-22** — [Why Speech to Text Is the Hidden Engine Behind Contact Center AI Performance](<../models/multimodal/Why Speech to Text Is the Hidden Engine Behind Contact Center AI Performance.md>) · `multimodal` · cresta
  Explains how speech-to-text quality drives downstream AI performance and why it should be treated as a system dependency.
- **2025-04-18** — [Why Transcription Performance Is Holding Back Your AI Strategy](<../models/multimodal/Why Transcription Performance Is Holding Back Your AI Strategy.md>) · `multimodal` · cresta
  Connects transcription performance to broader AI application quality, especially for voice-first systems.
- **2025-04-11** — [40 Large Language Model Benchmarks and The Future of Model Evaluation](<../models/benchmarks/40 Large Language Model Benchmarks and The Future of Model Evaluation.md>) · `benchmarks` · arize
  Surveys major LLM benchmarks and explains what different benchmark families measure for model evaluation.
- **2025-04-08** — [Arabic Leaderboards: Introducing Arabic Instruction Following, Updating AraGen, and More](<../models/benchmarks/Arabic Leaderboards Introducing Arabic Instruction Following, Updating AraGen, and More.md>) · `benchmarks` · huggingface
  Updates the Arabic LLM evaluation stack: the 3C3H generative scoring metric (correctness, completeness, conciseness + helpfulness, honesty, harmlessness) behind AraGen-03-25, plus Arabic IFEval, the first public instruction-following benchmark for Arabic, consolidated in one Arabic-Leaderboards Space with MBZUAI.
- **2025-04-08** — [Tracing and Evaluating Gemini Audio with Arize](<../models/multimodal/Tracing and Evaluating Gemini Audio with Arize.md>) · `multimodal` · arize
  Covers tracing and evaluation for Gemini audio applications, focusing on observability for multimodal systems.
- **2025-04-04** — [AI Benchmark Deep Dive: Gemini 2.5 and Humanity's Last Exam](<../models/benchmarks/AI Benchmark Deep Dive Gemini 2.5 and Humanity's Last Exam.md>) · `benchmarks` · arize
  Paper-reading recap on Gemini 2.5 and Humanity's Last Exam, focusing on benchmark interpretation and what modern evaluation results do and do not show.
- **2025-03-17** — [Prompt Optimization Techniques](<../prompt-engineering/techniques/Prompt Optimization Techniques.md>) · `techniques` · arize
  Covers few-shot prompting and prompt optimization techniques with an emphasis on measurable improvement.
- **2025-03-13** — [Hugging Face and Langfuse: 5 Ways to use them Together](<../infra-platform/deployment/Hugging Face and Langfuse 5 Ways to use them Together.md>) · `deployment` · langfuse
  Shows ways to combine Hugging Face workflows with Langfuse for model experimentation, tracing, evaluation, and deployment feedback loops.
- **2025-03-03** — [Brainstore: the database designed for the AI engineering era](<../infra-platform/deployment/Brainstore the database designed for the AI engineering era.md>) · `deployment` · braintrust
  Introduces Brainstore as a database for AI engineering workloads, optimized for traces, evals, logs, and large-scale observability queries.
- **2025-02-20** — [The Agent Deep Dive: David Zhang’s Open Deep Research](<../agents/planning/The Agent Deep Dive David Zhang’s Open Deep Research.md>) · `planning` · langfuse
  Deep dive on Open Deep Research as an agentic system, covering planning, tool use, research workflows, and trace-based inspection.
- **2025-02-12** — [How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting](<../product-engineering/case-studies/How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting.md>) · `case-studies` · arize
  Case study on using Phoenix traces and observability to improve AI-driven troubleshooting workflows in production.
- **2025-02-10** — [Benchmarking Single Agent Performance](<../agents/planning/Benchmarking Single Agent Performance.md>) · `planning` · langchain
  Benchmarks single-agent ReAct-style performance and discusses evaluation methodology for agent reasoning/tool-use loops.
- **2025-02-04** — [Open-source DeepResearch – Freeing our search agents](<../agents/tool-use/Open-source DeepResearch – Freeing our search agents.md>) · `tool-use` · huggingface
  Open reproduction of OpenAI's Deep Research: a smolagents CodeAgent (Python-action instead of JSON tool calls) with a text web browser and file inspector reaches 55% on GAIA validation vs OpenAI's ~67%, with analysis of where browser interaction is the bottleneck.
- **2025-01-28** — [How Cresta Scales Real-Time Insights with ClickHouse](<../infra-platform/deployment/How Cresta Scales Real-Time Insights with ClickHouse.md>) · `deployment` · cresta
  Architecture case study on scaling real-time AI insights with ClickHouse for high-volume conversation analytics.
- **2025-01-27** — [Beyond Supervised Fine Tuning: How Reinforcement Learning Empowers AI with Minimal Labels](<../models/reinforcement-learning/Beyond Supervised Fine Tuning How Reinforcement Learning Empowers AI with Minimal Labels.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement learning with verifiable rewards as a way to improve models with minimal labels.
- **2025-01-22** — [Evaluating agents](<../agents/planning/Evaluating agents.md>) · `planning` · braintrust
  Detailed guide to evaluating agents, including task design, tool-use traces, intermediate-step analysis, and failure modes unique to multi-step systems.
- **2025-01-22** — [Evaluating and Monitoring Voice AI Agents](<../models/multimodal/Evaluating and Monitoring Voice AI Agents.md>) · `multimodal` · langfuse
  Covers evaluation and monitoring for voice AI agents, including speech-specific quality signals and agent behavior beyond text-only evals.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<../product-engineering/architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2025-01-07** — [Agents](<../agents/planning/Agents.md>) · `planning` · chip-huyen
  Framework for foundation-model agents covering environments, tools, planning, action selection, failure modes, and evaluation for multi-step agentic applications.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<../agents/planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-11-17** — [From Zero to Scale: Langfuse's Infrastructure Evolution](<../infra-platform/deployment/From Zero to Scale Langfuse's Infrastructure Evolution.md>) · `deployment` · langfuse
  Case study of Langfuse infrastructure evolution from early product to scale, including data architecture, observability workloads, and operational tradeoffs.
- **2024-11-14** — [Evaluating Gemini models for vision](<../models/multimodal/Evaluating Gemini models for vision.md>) · `multimodal` · braintrust
  Evaluates Gemini vision models and shows how multimodal evals can compare image-understanding behavior across model versions.
- **2024-11-13** — [Promptim: an experimental library for prompt optimization](<../prompt-engineering/techniques/Promptim an experimental library for prompt optimization.md>) · `techniques` · langchain
  Introduces Promptim as an experimental prompt-optimization library that uses evaluation feedback to improve prompts.
- **2024-11-13** — [LLM Product Development for Product Managers](<../product-engineering/ux-patterns/LLM Product Development for Product Managers.md>) · `ux-patterns` · langfuse
  Product-management guide for LLM applications, connecting user workflows, quality criteria, feedback, and evals to AI product development decisions.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<../inference/hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-10-01** — [🇨🇿 BenCzechMark - Can your LLM Understand Czech?](<../models/benchmarks/🇨🇿 BenCzechMark - Can your LLM Understand Czech.md>) · `benchmarks` · huggingface
  Introduces BenCzechMark, a Czech LLM evaluation suite of 50 tasks across 9 categories (90% natively Czech, not translated) with a leaderboard covering 25+ open models, plus its statistical duel-based ranking methodology.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<../agents/memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.
- **2024-09-26** — [Pushing LangSmith to new limits with Replit Agent's complex workflows](<../product-engineering/case-studies/Pushing LangSmith to new limits with Replit Agent's complex workflows.md>) · `case-studies` · langchain
  Replit Agent case study on tracing and managing complex agent workflows with LangSmith.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<../inference/quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<../prompt-engineering/techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<../rag-retrieval/search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-07-01** — [Our Transformers Code Agent beats the GAIA benchmark 🏅](<../agents/tool-use/Our Transformers Code Agent beats the GAIA benchmark 🏅.md>) · `tool-use` · huggingface
  How a Transformers CodeAgent (LLM writes Python actions rather than JSON) topped the GAIA agent benchmark: multi-agent web-browser delegation, tool design, and error analysis of GAIA failure modes.
- **2024-06-19** — [How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x](<../product-engineering/case-studies/How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x.md>) · `case-studies` · langchain
  Factory case study on automating feedback loops with LangSmith to improve iteration speed and production agent quality.
- **2024-05-30** — [LLM Summarization: Getting To Production](<../product-engineering/architecture/LLM Summarization Getting To Production.md>) · `architecture` · arize
  Covers production considerations for LLM summarization systems, including quality controls and deployment pitfalls.
- **2024-05-29** — [Benchmarking Text Generation Inference](<../inference/serving/Benchmarking Text Generation Inference.md>) · `serving` · huggingface
  How to use the TGI benchmarking tool to profile LLM serving: separating prefill from decode, reading latency vs throughput curves under different batch sizes, and choosing the batch size that meets your latency SLO.
- **2024-05-14** — [Monitoring LLM Security & Reducing LLM Risks](<../product-engineering/security/Monitoring LLM Security & Reducing LLM Risks.md>) · `security` · langfuse
  Covers monitoring patterns for LLM security risks such as prompt injection, data leakage, and unsafe outputs, with observability as part of the mitigation loop.
- **2024-05-06** — [AI development loops](<../product-engineering/architecture/AI development loops.md>) · `architecture` · braintrust
  Describes AI development loops where logs, evals, human review, and product iteration form the core workflow for improving AI applications.
- **2024-05-05** — [Introducing the Open Leaderboard for Hebrew LLMs!](<../models/benchmarks/Introducing the Open Leaderboard for Hebrew LLMs!.md>) · `benchmarks` · huggingface
  An open leaderboard for Hebrew LLMs, motivated by Hebrew's root-and-pattern morphology breaking tokenization strategies designed for simpler languages; it evaluates on Hebrew-native tasks (Q&A, sentiment, winograd, translation) rather than translated English benchmarks.
- **2024-05-03** — [Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face](<../inference/serving/Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face.md>) · `serving` · huggingface
  The Artificial Analysis LLM Performance Leaderboard benchmarks hosted inference endpoints (not model quality) on throughput tokens/s, time-to-first-token, and price per token across providers, arguing latency is the limiting factor for agentic/tool-use systems where sequential LLM calls compound.
- **2024-04-30** — [Improving Prompt Consistency with Structured Generations](<../prompt-engineering/structured-output/Improving Prompt Consistency with Structured Generations.md>) · `structured-output` · huggingface
  HF's leaderboards team and dottxt show that eval scores swing wildly with tiny prompt-format changes, and that forcing structured generation (Outlines' regex/JSON-constrained decoding) sharply reduces that variance across prompt formats on GSM8K-style tasks.
- **2024-04-23** — [Introducing the Open Chain of Thought Leaderboard](<../models/reasoning/Introducing the Open Chain of Thought Leaderboard.md>) · `reasoning` · huggingface
  The Open CoT Leaderboard measures the *accuracy gain* a model gets from generating a chain-of-thought trace rather than raw accuracy, scoring several CoT prompting regimes across reasoning benchmarks to see which models actually benefit from thinking step by step.
- **2024-04-19** — [The Open Medical-LLM Leaderboard: Benchmarking Large Language Models in Healthcare](<../models/benchmarks/The Open Medical-LLM Leaderboard Benchmarking Large Language Models in Healthcare.md>) · `benchmarks` · huggingface
  The Open Medical-LLM Leaderboard aggregates MedQA (USMLE), MedMCQA, PubMedQA and MMLU medical subsets into a standardized accuracy benchmark for clinical LLMs, motivated by failure cases like GPT-3 recommending tetracycline to a pregnant patient while correctly explaining its contraindication.
- **2024-03-15** — [Benchmarking Query Analysis in High Cardinality Situations](<../rag-retrieval/search/Benchmarking Query Analysis in High Cardinality Situations.md>) · `search` · langchain
  Benchmarks query analysis in high-cardinality situations, relevant to retrieval, search, and observability filtering workloads.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<../product-engineering/case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<../rag-retrieval/pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-01-24** — [Open-source LLMs as LangChain Agents](<../agents/tool-use/Open-source LLMs as LangChain Agents.md>) · `tool-use` · huggingface
  Explains the ReAct loop mechanics (thought/action/observation, stopping, error handling) and builds such agents with LangChain's ChatHuggingFace, then benchmarks open LLMs on a custom agent evaluation set against GPT-3.5/GPT-4. Mixtral-8x7B comes out ahead of GPT-3.5 on the agentic tasks; also covers the JSON-parsing failure modes that dominate agent errors.
- **2024-01-18** — [Preference Tuning LLMs with Direct Preference Optimization Methods](<../models/fine-tuning/Preference Tuning LLMs with Direct Preference Optimization Methods.md>) · `fine-tuning` · huggingface
  Empirical head-to-head of DPO vs IPO vs KTO in TRL on two SFT'd 7B models (Zephyr and OpenHermes), sweeping the beta hyperparameter and scoring on MT-Bench; finds DPO/IPO roughly on par and beating KTO in the paired-preference setting, with beta mattering more than algorithm choice. Includes an errata where a summed-vs-averaged log-likelihood bug in TRL's IPO loss changed the results.
- **2023-12-20** — [Benchmarking Agent Tool Use](<../agents/tool-use/Benchmarking Agent Tool Use.md>) · `tool-use` · langchain
  Benchmarking study for agent tool use, focused on measuring whether agents choose and invoke tools correctly across tasks.
- **2023-12-18** — [How to Prompt LLMs for Text-to-SQL](<../prompt-engineering/structured-output/How to Prompt LLMs for Text-to-SQL.md>) · `structured-output` · arize
  Practical guide to Text-to-SQL prompting, including schema context, output constraints, and evaluation considerations.
- **2023-11-22** — [Sharing LangSmith Benchmarks](<../models/benchmarks/Sharing LangSmith Benchmarks.md>) · `benchmarks` · langchain
  Shares LangSmith benchmarks for evaluating models and chains, including methodology and public comparison workflows.
- **2023-11-13** — [The AI product development journey](<../product-engineering/architecture/The AI product development journey.md>) · `architecture` · braintrust
  Frames the AI product development journey around iterative prototyping, evaluation, logging, feedback, and production-quality improvement loops.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<../inference/serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-10-16** — [Testing Fine Tuned Open Source Models in LangSmith](<../models/fine-tuning/Testing Fine Tuned Open Source Models in LangSmith.md>) · `fine-tuning` · langchain
  Shows how to test fine-tuned open-source models in LangSmith using evaluations and comparison workflows.
- **2023-08-16** — [Open challenges in LLM research](<../models/reasoning/Open challenges in LLM research.md>) · `reasoning` · chip-huyen
  Surveys open LLM research problems around hallucination, context length, efficiency, multimodality, agents, evaluation, and post-training behavior that shape engineering constraints.
- **2023-05-02** — [RLHF: Reinforcement Learning from Human Feedback](<../models/reinforcement-learning/RLHF Reinforcement Learning from Human Feedback.md>) · `reinforcement-learning` · chip-huyen
  Explains the RLHF pipeline from preference data through reward modeling and policy optimization, including why human feedback changes model behavior and where evaluation matters.
- **2023-04-11** — [Building LLM applications for production](<../product-engineering/architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
- **2022-11-17** — [HELM: benchmarking large language models on the Together Research Computer](<../models/benchmarks/HELM benchmarking large language models on the Together Research Computer.md>) · `benchmarks` · together
  Describes HELM benchmarking on the Together Research Computer.
- **2022-02-10** — [Why Transcription is Vital to Contact Center AI](<../models/multimodal/Why Transcription is Vital to Contact Center AI.md>) · `multimodal` · cresta
  Explains why transcription quality is a core dependency for downstream AI systems that operate on spoken conversations.
- **2022-01-02** — [Real-time machine learning: challenges and solutions](<../product-engineering/architecture/Real-time machine learning challenges and solutions.md>) · `architecture` · chip-huyen
  Deep dive on real-time ML systems covering online prediction, feature freshness, stream processing, monitoring, feedback delays, and the tradeoffs needed to serve adaptive models in production.
- **2020-06-22** — [What I learned from looking at 200 machine learning tools](<../infra-platform/deployment/What I learned from looking at 200 machine learning tools.md>) · `deployment` · chip-huyen
  Analyzes 200 machine learning tools and maps the MLOps stack across data pipelines, training, deployment, monitoring, labeling, and orchestration for production ML systems.
