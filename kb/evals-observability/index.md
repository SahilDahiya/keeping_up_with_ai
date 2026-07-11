# evals-observability

54 articles.

- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-06-30** — [AI evals are a data science problem: What most teams get wrong](<evaluation/AI evals are a data science problem What most teams get wrong.md>) · `evaluation` · arize
  Argues that AI evaluation is a data science workflow requiring careful labeling, slices, standards, and failure analysis rather than a simple dashboard metric.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<evaluation/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `evaluation` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-01** — [Why agent telemetry needs standards](<tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-04-23** — [An update on recent Claude Code quality reports](<monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<evaluation/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `evaluation` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<evaluation/Quantifying infrastructure noise in agentic coding evals.md>) · `evaluation` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-22** — [Testing Agent Skills Systematically with Evals | OpenAI Developers](<evaluation/Testing Agent Skills Systematically with Evals OpenAI Developers.md>) · `evaluation` · openai-devs
  Pattern for evaluating Codex agent skills like lightweight end-to-end tests: define outcome/process/style/efficiency success criteria first, capture run traces and artifacts, then combine deterministic checks (did it run npm install, create package.json) with rubric-based grading to catch regressions.
- **2026-01-21** — [Designing AI resistant technical evaluations](<testing/Designing AI resistant technical evaluations.md>) · `testing` · anthropic-engineering
  How Anthropic designs technical hiring evaluations that stay meaningful when candidates have AI assistance, favoring debugging and judgment over greenfield coding.
- **2026-01-09** — [Demystifying evals for AI agents](<evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-12-01** — [AWS Bedrock AgentCore Observability with Arize AX: Operationalizing AI Agents At Scale](<tracing/AWS Bedrock AgentCore Observability with Arize AX Operationalizing AI Agents At Scale.md>) · `tracing` · arize
  Walks through operationalizing AWS Bedrock AgentCore agents with Arize AX observability, focusing on traces, evaluation, and production-scale monitoring.
- **2025-11-18** — [Evaluating and Improving AI Agents at Scale with Microsoft Foundry](<evaluation/Evaluating and Improving AI Agents at Scale with Microsoft Foundry.md>) · `evaluation` · arize
  Guide to evaluating and improving production AI agents at scale with Microsoft Foundry and Arize workflows.
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-09-19** — [Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary: A Framework and Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies](<evaluation/Atropos Health’s Arjun Mukerji, PhD, Explains RWESummary A Framework and Test for Choosing LLMs to Summarize Real-World Evidence (RWE) Studies.md>) · `evaluation` · arize
  Summarizes RWESummary, a healthcare-focused framework for choosing LLMs to summarize real-world evidence studies safely and reliably.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-08-21** — [Annotation for Strong AI Evaluation Pipelines](<evaluation/Annotation for Strong AI Evaluation Pipelines.md>) · `evaluation` · arize
  Explains how human annotations support strong AI evaluation pipelines and how annotation data can be combined with evals in Phoenix workflows.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-03-18** — [Self-Improving Agents: Automating LLM Performance Optimization using Arize and NVIDIA NeMo](<monitoring/Self-Improving Agents Automating LLM Performance Optimization using Arize and NVIDIA NeMo.md>) · `monitoring` · arize
  Describes using Arize with NVIDIA NeMo to automate LLM performance optimization and support self-improving agent workflows.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<evaluation/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `evaluation` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-09-30** — [Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations](<evaluation/Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations.md>) · `evaluation` · arize
  Best practices for choosing an LLM-as-judge evaluation model, including tradeoffs in evaluator quality and fit for task.
- **2024-09-05** — [Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation](<evaluation/Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation.md>) · `evaluation` · arize
  Explains how to create and validate synthetic datasets for LLM evaluation and experimentation workflows.
- **2024-08-30** — [Evaluating an Image Classifier](<evaluation/Evaluating an Image Classifier.md>) · `evaluation` · arize
  Tutorial on evaluating an image classifier with Phoenix, using multimodal experiment and tracing workflows.
- **2024-07-25** — [Different Ways to Instrument Your LLM Application](<tracing/Different Ways to Instrument Your LLM Application.md>) · `tracing` · arize
  Survey of instrumentation approaches for LLM applications, focused on tracing and observability setup choices.
- **2024-05-13** — [Breaking Down EvalGen: Who Validates the Validators?](<evaluation/Breaking Down EvalGen Who Validates the Validators.md>) · `evaluation` · arize
  Deep dive on EvalGen and the problem of validating LLM-generated evaluators, including human review limitations and evaluator reliability.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<evaluation/Predictive Human Preference From Model Ranking to Model Routing.md>) · `evaluation` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<evaluation/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `evaluation` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
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
- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-06-05** — [Your AI bill is out of control. Cloudflare can fix it now.](<../infra-platform/cost/Your AI bill is out of control. Cloudflare can fix it now.md>) · `cost` · cloudflare-ai
  AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven budgets and model routing via Cloudflare Access, so enterprises can attribute LLM spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for interns) instead of one opaque shared API key.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<evaluation/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `evaluation` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-04-20** — [Code is free, technical debt isn’t: Notes from AI Engineer Europe](<../industry/trends/Code is free, technical debt isn’t Notes from AI Engineer Europe.md>) · `trends` · arize
  AI Engineer Europe notes arguing that faster code generation increases the need for verification, standards, and technical-debt management.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<../agents/planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-03-10** — [Arize Skills: Coding Agent Workflows for Traces, Evals, and Instrumentation](<../agents/tool-use/Arize Skills Coding Agent Workflows for Traces, Evals, and Instrumentation.md>) · `tool-use` · arize
  Introduces Arize Skills for coding agents, enabling workflows around trace extraction, evals, and instrumentation from agentic development environments.
- **2026-03-04** — [From UI to Terminal: Bringing Alyx's Superpowers Into Your Coding Agent](<../agents/tool-use/From UI to Terminal Bringing Alyx's Superpowers Into Your Coding Agent.md>) · `tool-use` · arize
  Introduces an AX CLI preview that brings Alyx-style trace and eval workflows into terminal-based coding-agent loops.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<../product-engineering/security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<../prompt-engineering/techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-09-17** — [A postmortem of three recent issues](<../inference/serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-17** — [adb Benchmarks](<../infra-platform/deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<../prompt-engineering/techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<../infra-platform/deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-06-13** — [How we built our multi-agent research system](<../agents/multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-04-04** — [AI Benchmark Deep Dive: Gemini 2.5 and Humanity's Last Exam](<../models/benchmarks/AI Benchmark Deep Dive Gemini 2.5 and Humanity's Last Exam.md>) · `benchmarks` · arize
  Paper-reading recap on Gemini 2.5 and Humanity's Last Exam, focusing on benchmark interpretation and what modern evaluation results do and do not show.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<../product-engineering/architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2025-01-07** — [Agents](<../agents/planning/Agents.md>) · `planning` · chip-huyen
  Framework for foundation-model agents covering environments, tools, planning, action selection, failure modes, and evaluation for multi-step agentic applications.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<../agents/planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<../agents/memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<../prompt-engineering/techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.
- **2024-05-21** — [Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog](<../infra-platform/deployment/Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog.md>) · `deployment` · arize
  Describes Arize integration with Microsoft Azure AI Model Catalog for LLM evaluation and observability in Azure-hosted development workflows.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<../product-engineering/case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<../rag-retrieval/pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-01-01** — [Evaluate RAG with LLM Evals and Benchmarking](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarking.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarking.
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
