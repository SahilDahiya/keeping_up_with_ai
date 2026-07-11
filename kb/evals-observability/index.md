# evals-observability

85 articles.

- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-06-30** — [AI evals are a data science problem: What most teams get wrong](<evaluation/AI evals are a data science problem What most teams get wrong.md>) · `evaluation` · arize
  Argues that AI evaluation is a data science workflow requiring careful labeling, slices, standards, and failure analysis rather than a simple dashboard metric.
- **2026-06-26** — [How to eval stateful agents](<evaluation/How to eval stateful agents.md>) · `evaluation` · braintrust
  Guide to evaluating stateful agents, including memory, conversation state, trace review, and tests for behavior that depends on previous interactions.
- **2026-06-16** — [How to use Braintrust with any framework or provider](<tracing/How to use Braintrust with any framework or provider.md>) · `tracing` · braintrust
  Integration guide for capturing Braintrust traces and evals across different AI frameworks and model providers without locking the application stack to one SDK.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-06-04** — [How we made continuous trace intelligence possible at scale](<tracing/How we made continuous trace intelligence possible at scale.md>) · `tracing` · braintrust
  Architecture deep dive on continuous trace intelligence at scale, including how production traces are clustered and surfaced for analysis.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<evaluation/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `evaluation` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-06-01** — [AI observability is active observability](<monitoring/AI observability is active observability.md>) · `monitoring` · braintrust
  Defines active AI observability as systems that analyze traces, surface patterns, and drive improvements rather than passively storing production logs.
- **2026-05-21** — [How to improve your golden datasets with human review](<testing/How to improve your golden datasets with human review.md>) · `testing` · braintrust
  Explains how human review improves golden datasets for evals by correcting labels, surfacing ambiguity, and tightening quality standards.
- **2026-05-14** — [How to evaluate multi-turn conversations](<evaluation/How to evaluate multi-turn conversations.md>) · `evaluation` · braintrust
  Guide to evaluating multi-turn conversations, including state, conversation-level criteria, turn-level scoring, and agent-like interaction failures.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-11** — [Why your traces and evals belong in the same place](<tracing/Why your traces and evals belong in the same place.md>) · `tracing` · braintrust
  Argues that traces and evals should live together so teams can connect production behavior, offline experiments, and failure analysis.
- **2026-05-01** — [Why agent telemetry needs standards](<tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-04-28** — [How to earn stakeholder trust with evals and observability](<monitoring/How to earn stakeholder trust with evals and observability.md>) · `monitoring` · braintrust
  Explains how evals and observability help build stakeholder trust by making AI product quality measurable, reviewable, and improvable.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-04-23** — [An update on recent Claude Code quality reports](<monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-04-08** — [Agentic eval development with the Braintrust CLI](<testing/Agentic eval development with the Braintrust CLI.md>) · `testing` · braintrust
  Shows how to use the Braintrust CLI for agentic eval development, turning local experiments into repeatable tests for agent behavior.
- **2026-04-06** — [How Brainstore works: architecture for AI observability at scale](<monitoring/How Brainstore works architecture for AI observability at scale.md>) · `monitoring` · braintrust
  Deep dive into Brainstore's architecture for AI observability at scale, covering storage, indexing, query patterns, and trace/log workloads.
- **2026-03-19** — [What is AI observability?](<monitoring/What is AI observability.md>) · `monitoring` · braintrust
  Explains AI observability concepts for production systems, including traces, evals, logs, monitoring, and feedback loops.
- **2026-03-10** — [How to build your first offline eval](<testing/How to build your first offline eval.md>) · `testing` · braintrust
  Step-by-step guide to building a first offline eval, including dataset setup, task definition, scorers, experiment runs, and failure review.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<evaluation/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `evaluation` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-25** — [Automatically discover what matters in your production traces with Topics](<tracing/Automatically discover what matters in your production traces with Topics.md>) · `tracing` · braintrust
  Introduces automatic topic discovery over production traces as a way to find recurring behavior patterns and quality issues.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-12** — [The 5 pillars of AI model performance](<evaluation/The 5 pillars of AI model performance.md>) · `evaluation` · braintrust
  Defines five pillars of AI model performance and how to measure quality beyond a single aggregate benchmark score.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<evaluation/Quantifying infrastructure noise in agentic coding evals.md>) · `evaluation` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-22** — [Testing Agent Skills Systematically with Evals | OpenAI Developers](<evaluation/Testing Agent Skills Systematically with Evals OpenAI Developers.md>) · `evaluation` · openai-devs
  Pattern for evaluating Codex agent skills like lightweight end-to-end tests: define outcome/process/style/efficiency success criteria first, capture run traces and artifacts, then combine deterministic checks (did it run npm install, create package.json) with rubric-based grading to catch regressions.
- **2026-01-21** — [Designing AI resistant technical evaluations](<testing/Designing AI resistant technical evaluations.md>) · `testing` · anthropic-engineering
  How Anthropic designs technical hiring evaluations that stay meaningful when candidates have AI assistance, favoring debugging and judgment over greenfield coding.
- **2026-01-13** — [Debugging Ralph Wiggum with Braintrust Logs](<tracing/Debugging Ralph Wiggum with Braintrust Logs.md>) · `tracing` · braintrust
  Debugging walkthrough using Braintrust logs to inspect AI application behavior, identify failure causes, and close the loop with improvements.
- **2026-01-09** — [Demystifying evals for AI agents](<evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-12-18** — [Brainstore makes AI observability at scale possible](<monitoring/Brainstore makes AI observability at scale possible.md>) · `monitoring` · braintrust
  Benchmark-oriented note on Brainstore performance and why purpose-built storage is needed for high-volume AI observability workloads.
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
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-10-10** — [Measuring what matters: An intro to AI evals](<evaluation/Measuring what matters An intro to AI evals.md>) · `evaluation` · braintrust
  Intro to AI evals focused on choosing metrics that reflect product quality, building datasets, and measuring what matters for users.
- **2025-09-19** — [Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary: A Framework and Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies](<evaluation/Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary A Framework and Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies.md>) · `evaluation` · arize
  Summarizes RWESummary, a healthcare-focused framework for choosing LLMs to summarize real-world evidence studies safely and reliably.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-03** — [A/B testing can't keep up with AI](<evaluation/AB testing can't keep up with AI.md>) · `evaluation` · braintrust
  Explains why traditional A/B testing is too slow for AI products and argues for eval-driven experimentation loops that compare model, prompt, and product changes before rollout.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-08-21** — [Annotation for Strong AI Evaluation Pipelines](<evaluation/Annotation for Strong AI Evaluation Pipelines.md>) · `evaluation` · arize
  Explains how human annotations support strong AI evaluation pipelines and how annotation data can be combined with evals in Phoenix workflows.
- **2025-07-17** — [Five hard-learned lessons about AI evals](<evaluation/Five hard-learned lessons about AI evals.md>) · `evaluation` · braintrust
  Five practical lessons for building AI evals, emphasizing dataset quality, scorer design, failure analysis, and iteration over dashboard theater.
- **2025-07-14** — [Braintrust is not an eval framework](<monitoring/Braintrust is not an eval framework.md>) · `monitoring` · braintrust
  Argues that production AI quality needs a full observability and iteration system around evals, not only an isolated evaluation framework.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-04-03** — [Resilient observability by design](<monitoring/Resilient observability by design.md>) · `monitoring` · braintrust
  Describes resilient observability design for AI systems, including reliability considerations for storing, querying, and using production traces.
- **2025-03-18** — [Self-Improving Agents: Automating LLM Performance Optimization using Arize and NVIDIA NeMo](<monitoring/Self-Improving Agents Automating LLM Performance Optimization using Arize and NVIDIA NeMo.md>) · `monitoring` · arize
  Describes using Arize with NVIDIA NeMo to automate LLM performance optimization and support self-improving agent workflows.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2024-12-04** — [What to do when a new AI model comes out](<evaluation/What to do when a new AI model comes out.md>) · `evaluation` · braintrust
  Playbook for responding when a new AI model ships: run targeted evals, compare cost and quality, inspect regressions, and decide rollout strategy.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<evaluation/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `evaluation` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-10-17** — [I ran an eval. Now what?](<evaluation/I ran an eval. Now what.md>) · `evaluation` · braintrust
  Walks through what to do after an eval run: inspect failures, slice results, improve datasets and scorers, and turn findings into product or prompt changes.
- **2024-09-30** — [Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations](<evaluation/Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations.md>) · `evaluation` · arize
  Best practices for choosing an LLM-as-judge evaluation model, including tradeoffs in evaluator quality and fit for task.
- **2024-09-16** — [Custom scoring functions in the Braintrust Playground](<evaluation/Custom scoring functions in the Braintrust Playground.md>) · `evaluation` · braintrust
  Explains custom scoring functions for evaluating AI outputs, including how domain-specific metrics can be added to an eval workflow.
- **2024-09-05** — [Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation](<evaluation/Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation.md>) · `evaluation` · arize
  Explains how to create and validate synthetic datasets for LLM evaluation and experimentation workflows.
- **2024-08-30** — [Evaluating an Image Classifier](<evaluation/Evaluating an Image Classifier.md>) · `evaluation` · arize
  Tutorial on evaluating an image classifier with Phoenix, using multimodal experiment and tracing workflows.
- **2024-07-25** — [Different Ways to Instrument Your LLM Application](<tracing/Different Ways to Instrument Your LLM Application.md>) · `tracing` · arize
  Survey of instrumentation approaches for LLM applications, focused on tracing and observability setup choices.
- **2024-06-20** — [How to improve your evaluations](<evaluation/How to improve your evaluations.md>) · `evaluation` · braintrust
  Practical guide to improving evals through better examples, rubrics, scorers, slices, and investigation of failure cases.
- **2024-05-13** — [Breaking Down EvalGen: Who Validates the Validators?](<evaluation/Breaking Down EvalGen Who Validates the Validators.md>) · `evaluation` · arize
  Deep dive on EvalGen and the problem of validating LLM-generated evaluators, including human review limitations and evaluator reliability.
- **2024-04-24** — [Getting started with automated evaluations](<testing/Getting started with automated evaluations.md>) · `testing` · braintrust
  Introductory guide to automated evaluations, covering datasets, scorers, experiments, and how to start measuring AI application quality.
- **2024-04-17** — [Eval feedback loops](<evaluation/Eval feedback loops.md>) · `evaluation` · braintrust
  Explains eval feedback loops where production observations and human review continuously improve prompts, datasets, and model behavior.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<evaluation/Predictive Human Preference From Model Ranking to Model Routing.md>) · `evaluation` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<evaluation/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `evaluation` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
- **2023-09-12** — [It's time to build reliable AI](<evaluation/It's time to build reliable AI.md>) · `evaluation` · braintrust
  Early argument for reliable AI systems built around evals, logging, feedback loops, and engineering practices rather than ad hoc demos.
- **2023-05-25** — [Cross Validation: What You Need To Know, From the Basics To LLMs](<evaluation/Cross Validation What You Need To Know, From the Basics To LLMs.md>) · `evaluation` · arize
  Overview of cross-validation from classic ML through LLM applications, focused on evaluation methodology.
- **2023-05-17** — [Evaluating Model Fairness](<evaluation/Evaluating Model Fairness.md>) · `evaluation` · arize
  Explains model fairness evaluation and how to assess bias and fairness risks in production systems.
- **2022-12-22** — [Hugging Face + Arize: Partnership and Code Example](<monitoring/Hugging Face + Arize Partnership and Code Example.md>) · `monitoring` · arize
  Partnership and code example showing how to monitor Hugging Face model workflows with Arize observability.
- **2022-12-16** — [Calculate Real-Time AI ROI With Custom Metrics](<monitoring/Calculate Real-Time AI ROI With Custom Metrics.md>) · `monitoring` · arize
  Shows how custom metrics can connect AI observability data to real-time ROI analysis and business impact.
- **2022-09-30** — [Arize AI + OpenAI](<monitoring/Arize AI + OpenAI.md>) · `monitoring` · arize
  Introduces Arize support for monitoring OpenAI-powered applications, connecting hosted LLM usage with observability and performance analysis.
- **2022-02-07** — [Data Distribution Shifts and Monitoring](<monitoring/Data Distribution Shifts and Monitoring.md>) · `monitoring` · chip-huyen
  Taxonomy of covariate, label, and concept shifts with production monitoring strategies, data-quality checks, slice analysis, alerting tradeoffs, and examples of real-world ML failure modes.
- **2022-01-05** — [Best Practices In ML Observability for Customer Lifetime Value (LTV) Models](<monitoring/Best Practices In ML Observability for Customer Lifetime Value (LTV) Models.md>) · `monitoring` · arize
  Best practices for monitoring customer lifetime value models in production using ML observability techniques.
- **2021-12-18** — [Best Practices In ML Observability for Click-Through Rate Models](<monitoring/Best Practices In ML Observability for Click-Through Rate Models.md>) · `monitoring` · arize
  Best practices for monitoring click-through-rate models, with attention to production metrics, drift, and model performance debugging.
- **2021-11-22** — [Best Practices for ML Monitoring and Observability of Demand Forecasting Models](<monitoring/Best Practices for ML Monitoring and Observability of Demand Forecasting Models.md>) · `monitoring` · arize
  Best practices for monitoring demand forecasting models, including drift, performance slices, and production observability needs.
- **2021-10-27** — [Best Practices In ML Observability for Monitoring, Mitigating and Preventing Fraud](<monitoring/Best Practices In ML Observability for Monitoring, Mitigating and Preventing Fraud.md>) · `monitoring` · arize
  Best practices for fraud-model observability, covering monitoring, mitigation, and prevention workflows for production risk systems.
- **2021-09-11** — [Overcoming AI's Transparency Paradox](<monitoring/Overcoming AI's Transparency Paradox.md>) · `monitoring` · arize
  Discusses AI transparency and explainability challenges, positioning observability as a way to understand opaque model behavior in production.
- **2021-08-06** — [Why Best-Of-Breed ML Monitoring and Observability Solutions Are The Way Forward](<monitoring/Why Best-Of-Breed ML Monitoring and Observability Solutions Are The Way Forward.md>) · `monitoring` · arize
  Argues for specialized ML monitoring and observability tools over broad platform bundles for production model operations.
- **2021-08-02** — [A Quick Start To Data Quality Monitoring For Machine Learning](<monitoring/A Quick Start To Data Quality Monitoring For Machine Learning.md>) · `monitoring` · arize
  Quick-start guide to data quality monitoring for machine learning systems.
- **2021-05-19** — [Beyond Monitoring: The Rise of Observability](<monitoring/Beyond Monitoring The Rise of Observability.md>) · `monitoring` · arize
  Explains the distinction between basic monitoring and deeper observability for diagnosing production ML model behavior.

## Also relevant (filed elsewhere)

- **2026-07-10** — [3 production patterns for AI agents and how to evaluate each one](<../agents/planning/3 production patterns for AI agents and how to evaluate each one.md>) · `planning` · arize
  Breaks production agents into local coding agents, in-app assistants, and operational agents, then maps each pattern to different harness, rollout, and evaluation needs.
- **2026-07-10** — [Evaluating the GPT-5.6 family](<../models/benchmarks/Evaluating the GPT-5.6 family.md>) · `benchmarks` · braintrust
  Evaluates the GPT-5.6 model family and presents a decision map for choosing models based on quality, cost, and task requirements.
- **2026-07-09** — [Evaluating speech-to-text models](<../models/multimodal/Evaluating speech-to-text models.md>) · `multimodal` · braintrust
  Evaluates speech-to-text models for voice AI workflows, covering datasets, scoring, and tradeoffs in transcription quality.
- **2026-07-08** — [Rewriting Bun in Rust](<../product-engineering/case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-07** — [Faster phrase search with shingled bloom filters in Brainstore](<../rag-retrieval/search/Faster phrase search with shingled bloom filters in Brainstore.md>) · `search` · braintrust
  Explains faster phrase search over Brainstore data using shingled bloom filters, aimed at efficient trace and log search for AI observability.
- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-07-06** — [Evaluating the USA vs Belgium World Cup matchup](<../agents/tool-use/Evaluating the USA vs Belgium World Cup matchup.md>) · `tool-use` · braintrust
  Uses a USA vs Belgium matchup example to evaluate web research agents, illustrating task design and judging for tool-using research workflows.
- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<../agents/tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-04** — [Better Models: Worse Tools](<../agents/tool-use/Better Models Worse Tools.md>) · `tool-use` · simon-willison
  Short analysis of newer coding models producing malformed arguments for third-party edit tools, raising the issue that tool schemas and edit mechanisms may need model-specific evaluation and adaptation.
- **2026-07-02** — [From World Cup matchups to research maps: evaluating Parallel's web research agents](<../agents/tool-use/From World Cup matchups to research maps evaluating Parallel's web research agents.md>) · `tool-use` · braintrust
  Evaluates Parallel web research agents using World Cup matchups and research-map tasks, connecting tool use, knowledge graphs, and answer quality.
- **2026-06-24** — [Using Braintrust to eval agentic setups from large-scale Hugging Face data](<../agents/planning/Using Braintrust to eval agentic setups from large-scale Hugging Face data.md>) · `planning` · braintrust
  Uses large-scale Hugging Face agent traces to evaluate agentic setups, connecting trace analysis to agent behavior and reliability measurement.
- **2026-06-17** — [How to test agent cost-efficiency with Braintrust](<../infra-platform/cost/How to test agent cost-efficiency with Braintrust.md>) · `cost` · braintrust
  Explains how to test agent cost-efficiency by measuring task success against token, model, and tool-use costs.
- **2026-06-05** — [Your AI bill is out of control. Cloudflare can fix it now.](<../infra-platform/cost/Your AI bill is out of control. Cloudflare can fix it now.md>) · `cost` · cloudflare-ai
  AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven budgets and model routing via Cloudflare Access, so enterprises can attribute LLM spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for interns) instead of one opaque shared API key.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<evaluation/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `evaluation` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-06-01** — [AI observability is active observability](<monitoring/AI observability is active observability.md>) · `monitoring` · braintrust
  Defines active AI observability as systems that analyze traces, surface patterns, and drive improvements rather than passively storing production logs.
- **2026-05-21** — [The six generations of AI agents and how to eval them](<../agents/planning/The six generations of AI agents and how to eval them.md>) · `planning` · braintrust
  Taxonomy of six generations of AI agents and guidance for evaluating each generation's capabilities, failure modes, and production readiness.
- **2026-05-21** — [How to improve your golden datasets with human review](<testing/How to improve your golden datasets with human review.md>) · `testing` · braintrust
  Explains how human review improves golden datasets for evals by correcting labels, surfacing ambiguity, and tightening quality standards.
- **2026-05-11** — [Why your traces and evals belong in the same place](<tracing/Why your traces and evals belong in the same place.md>) · `tracing` · braintrust
  Argues that traces and evals should live together so teams can connect production behavior, offline experiments, and failure analysis.
- **2026-04-20** — [Code is free, technical debt isn’t: Notes from AI Engineer Europe](<../industry/trends/Code is free, technical debt isn’t Notes from AI Engineer Europe.md>) · `trends` · arize
  AI Engineer Europe notes arguing that faster code generation increases the need for verification, standards, and technical-debt management.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<../agents/planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-04-13** — [How to prepare for AI compliance and governance](<../product-engineering/security/How to prepare for AI compliance and governance.md>) · `security` · braintrust
  Connects AI compliance and governance to engineering controls such as observability, audit trails, data boundaries, review workflows, and policy enforcement.
- **2026-04-03** — [Braintrust CLI and MCP](<../agents/tool-use/Braintrust CLI and MCP.md>) · `tool-use` · braintrust
  Covers Braintrust CLI and MCP support for connecting agent tools, local workflows, and observability/eval data into AI development loops.
- **2026-03-27** — [Evals are the new PRD](<../product-engineering/architecture/Evals are the new PRD.md>) · `architecture` · braintrust
  Argues that evals can act as executable product requirements for AI systems, aligning teams around expected behavior and measurable quality.
- **2026-03-19** — [What is AI observability?](<monitoring/What is AI observability.md>) · `monitoring` · braintrust
  Explains AI observability concepts for production systems, including traces, evals, logs, monitoring, and feedback loops.
- **2026-03-17** — [Evals for PMs: A practical guide to AI product quality](<../product-engineering/ux-patterns/Evals for PMs A practical guide to AI product quality.md>) · `ux-patterns` · braintrust
  Practical guide for product managers defining AI product quality with evals, user-centered criteria, examples, and iteration loops.
- **2026-03-10** — [Arize Skills: Coding Agent Workflows for Traces, Evals, and Instrumentation](<../agents/tool-use/Arize Skills Coding Agent Workflows for Traces, Evals, and Instrumentation.md>) · `tool-use` · arize
  Introduces Arize Skills for coding agents, enabling workflows around trace extraction, evals, and instrumentation from agentic development environments.
- **2026-03-10** — [How to build your first offline eval](<testing/How to build your first offline eval.md>) · `testing` · braintrust
  Step-by-step guide to building a first offline eval, including dataset setup, task definition, scorers, experiment runs, and failure review.
- **2026-03-04** — [From UI to Terminal: Bringing Alyx's Superpowers Into Your Coding Agent](<../agents/tool-use/From UI to Terminal Bringing Alyx's Superpowers Into Your Coding Agent.md>) · `tool-use` · arize
  Introduces an AX CLI preview that brings Alyx-style trace and eval workflows into terminal-based coding-agent loops.
- **2026-02-25** — [Automatically discover what matters in your production traces with Topics](<tracing/Automatically discover what matters in your production traces with Topics.md>) · `tracing` · braintrust
  Introduces automatic topic discovery over production traces as a way to find recurring behavior patterns and quality issues.
- **2026-01-22** — [Testing if "bash is all you need"](<../agents/tool-use/Testing if bash is all you need.md>) · `tool-use` · braintrust
  Tests whether bash-oriented agents can solve realistic tasks, using evals to measure command-line tool use and agent reliability.
- **2026-01-20** — [Building observable AI agents with Temporal](<../agents/tool-use/Building observable AI agents with Temporal.md>) · `tool-use` · braintrust
  Shows how Temporal workflows can make AI agents observable, connecting durable execution with traces, evals, and debugging data.
- **2026-01-13** — [Debugging Ralph Wiggum with Braintrust Logs](<tracing/Debugging Ralph Wiggum with Braintrust Logs.md>) · `tracing` · braintrust
  Debugging walkthrough using Braintrust logs to inspect AI application behavior, identify failure causes, and close the loop with improvements.
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
- **2025-12-23** — [Claude Code meets Braintrust](<../agents/tool-use/Claude Code meets Braintrust.md>) · `tool-use` · braintrust
  Shows how Claude Code workflows can connect to Braintrust so coding-agent traces, experiments, and eval data are captured for review.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<../product-engineering/security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-11-18** — [The three pillars of AI observability](<monitoring/The three pillars of AI observability.md>) · `monitoring` · braintrust
  Defines three pillars of AI observability and how traces, evals, and production feedback combine to improve AI systems.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<../prompt-engineering/techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-10-10** — [Measuring what matters: An intro to AI evals](<evaluation/Measuring what matters An intro to AI evals.md>) · `evaluation` · braintrust
  Intro to AI evals focused on choosing metrics that reflect product quality, building datasets, and measuring what matters for users.
- **2025-09-29** — [Claude Sonnet 4.5 analysis](<../models/benchmarks/Claude Sonnet 4.5 analysis.md>) · `benchmarks` · braintrust
  Analyzes Claude Sonnet 4.5 with aspirational evals, focusing on how harder task suites reveal model strengths and gaps beyond standard benchmarks.
- **2025-09-17** — [A postmortem of three recent issues](<../inference/serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-17** — [adb Benchmarks](<../infra-platform/deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<../prompt-engineering/techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<../infra-platform/deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-08-08** — [GPT-5 vs. Claude Opus 4.1](<../models/benchmarks/GPT-5 vs. Claude Opus 4.1.md>) · `benchmarks` · braintrust
  Compares GPT-5 and Claude Opus 4.1 with eval-driven analysis of strengths, weaknesses, and model-selection implications.
- **2025-07-17** — [Five hard-learned lessons about AI evals](<evaluation/Five hard-learned lessons about AI evals.md>) · `evaluation` · braintrust
  Five practical lessons for building AI evals, emphasizing dataset quality, scorer design, failure analysis, and iteration over dashboard theater.
- **2025-07-14** — [Braintrust is not an eval framework](<monitoring/Braintrust is not an eval framework.md>) · `monitoring` · braintrust
  Argues that production AI quality needs a full observability and iteration system around evals, not only an isolated evaluation framework.
- **2025-06-13** — [How we built our multi-agent research system](<../agents/multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-04-04** — [AI Benchmark Deep Dive: Gemini 2.5 and Humanity's Last Exam](<../models/benchmarks/AI Benchmark Deep Dive Gemini 2.5 and Humanity's Last Exam.md>) · `benchmarks` · arize
  Paper-reading recap on Gemini 2.5 and Humanity's Last Exam, focusing on benchmark interpretation and what modern evaluation results do and do not show.
- **2025-03-03** — [Brainstore: the database designed for the AI engineering era](<../infra-platform/deployment/Brainstore the database designed for the AI engineering era.md>) · `deployment` · braintrust
  Introduces Brainstore as a database for AI engineering workloads, optimized for traces, evals, logs, and large-scale observability queries.
- **2025-01-22** — [Evaluating agents](<../agents/planning/Evaluating agents.md>) · `planning` · braintrust
  Detailed guide to evaluating agents, including task design, tool-use traces, intermediate-step analysis, and failure modes unique to multi-step systems.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<../product-engineering/architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2025-01-07** — [Agents](<../agents/planning/Agents.md>) · `planning` · chip-huyen
  Framework for foundation-model agents covering environments, tools, planning, action selection, failure modes, and evaluation for multi-step agentic applications.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<../agents/planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-11-14** — [Evaluating Gemini models for vision](<../models/multimodal/Evaluating Gemini models for vision.md>) · `multimodal` · braintrust
  Evaluates Gemini vision models and shows how multimodal evals can compare image-understanding behavior across model versions.
- **2024-10-17** — [I ran an eval. Now what?](<evaluation/I ran an eval. Now what.md>) · `evaluation` · braintrust
  Walks through what to do after an eval run: inspect failures, slice results, improve datasets and scorers, and turn findings into product or prompt changes.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<../agents/memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.
- **2024-09-16** — [Custom scoring functions in the Braintrust Playground](<evaluation/Custom scoring functions in the Braintrust Playground.md>) · `evaluation` · braintrust
  Explains custom scoring functions for evaluating AI outputs, including how domain-specific metrics can be added to an eval workflow.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<../prompt-engineering/techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.
- **2024-06-20** — [How to improve your evaluations](<evaluation/How to improve your evaluations.md>) · `evaluation` · braintrust
  Practical guide to improving evals through better examples, rubrics, scorers, slices, and investigation of failure cases.
- **2024-05-21** — [Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog](<../infra-platform/deployment/Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog.md>) · `deployment` · arize
  Describes Arize integration with Microsoft Azure AI Model Catalog for LLM evaluation and observability in Azure-hosted development workflows.
- **2024-05-06** — [AI development loops](<../product-engineering/architecture/AI development loops.md>) · `architecture` · braintrust
  Describes AI development loops where logs, evals, human review, and product iteration form the core workflow for improving AI applications.
- **2024-04-24** — [Getting started with automated evaluations](<testing/Getting started with automated evaluations.md>) · `testing` · braintrust
  Introductory guide to automated evaluations, covering datasets, scorers, experiments, and how to start measuring AI application quality.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<../product-engineering/case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<../rag-retrieval/pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-01-01** — [Evaluate RAG with LLM Evals and Benchmarking](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarking.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarking.
- **2023-11-13** — [The AI product development journey](<../product-engineering/architecture/The AI product development journey.md>) · `architecture` · braintrust
  Frames the AI product development journey around iterative prototyping, evaluation, logging, feedback, and production-quality improvement loops.
- **2023-08-16** — [Open challenges in LLM research](<../models/reasoning/Open challenges in LLM research.md>) · `reasoning` · chip-huyen
  Surveys open LLM research problems around hallucination, context length, efficiency, multimodality, agents, evaluation, and post-training behavior that shape engineering constraints.
- **2023-07-19** — [Streamline and Centralize AI Analytics With Snowflake and Arize AI](<../product-engineering/case-studies/Streamline and Centralize AI Analytics With Snowflake and Arize AI.md>) · `case-studies` · arize
  Describes using Snowflake with Arize to centralize AI analytics and observability data for model performance analysis.
- **2023-05-02** — [RLHF: Reinforcement Learning from Human Feedback](<../models/fine-tuning/RLHF Reinforcement Learning from Human Feedback.md>) · `fine-tuning` · chip-huyen
  Explains the RLHF pipeline from preference data through reward modeling and policy optimization, including why human feedback changes model behavior and where evaluation matters.
- **2023-04-11** — [Building LLM applications for production](<../product-engineering/architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
- **2022-12-31** — [Measuring Embedding Drift](<../rag-retrieval/embeddings/Measuring Embedding Drift.md>) · `embeddings` · arize
  Explains embedding drift and how teams can measure changes in embedding distributions over time.
- **2022-06-22** — [Deploying Models In An Evolving Housing Market](<../product-engineering/case-studies/Deploying Models In An Evolving Housing Market.md>) · `case-studies` · arize
  Case discussion on deploying models in a changing housing market and monitoring model behavior under shifting real-world conditions.
- **2022-01-02** — [Real-time machine learning: challenges and solutions](<../product-engineering/architecture/Real-time machine learning challenges and solutions.md>) · `architecture` · chip-huyen
  Deep dive on real-time ML systems covering online prediction, feature freshness, stream processing, monitoring, feedback delays, and the tradeoffs needed to serve adaptive models in production.
- **2020-06-22** — [What I learned from looking at 200 machine learning tools](<../infra-platform/deployment/What I learned from looking at 200 machine learning tools.md>) · `deployment` · chip-huyen
  Analyzes 200 machine learning tools and maps the MLOps stack across data pipelines, training, deployment, monitoring, labeling, and orchestration for production ML systems.
