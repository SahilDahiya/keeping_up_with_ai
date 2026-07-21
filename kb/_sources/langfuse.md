# langfuse

37 articles.

- **2026-07-15** — [Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse](<../evals-observability/evaluation/Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse.md>) · `evaluation` · langfuse
  Walks through a PASS/FAIL deployment-gate pipeline for LLM systems at a major bank, built on Langfuse datasets/experiments/prompt management/annotation queues: three golden datasets (FinanceBench, Financial PhraseBank, a custom adversarial advisory set) score models and agents, gate on thresholds like 85% numerical accuracy, and emit CI exit codes plus reviewable evidence for model risk management.
- **2026-06-22** — [Designing the runtime for Langfuse code evaluators](<../evals-observability/testing/Designing the runtime for Langfuse code evaluators.md>) · `testing` · langfuse
  Design deep dive on the runtime for Langfuse code evaluators, covering execution isolation, evaluator lifecycle, and safe scalable scoring infrastructure.
- **2026-06-09** — [AI is eating the AI engineering loop](<../industry/trends/AI is eating the AI engineering loop.md>) · `trends` · langfuse
  Argues that AI is reshaping the AI engineering loop itself, with agents increasingly participating in prompt, eval, observability, and product iteration workflows.
- **2026-06-05** — [How we use agents to review production infrastructure](<../product-engineering/case-studies/How we use agents to review production infrastructure.md>) · `case-studies` · langfuse
  Case study of using agents to review production infrastructure, including operational workflows, review boundaries, and human oversight.
- **2026-04-14** — [Classifying User Intent with Categorical LLM-as-a-Judge](<../evals-observability/llm-as-judge/Classifying User Intent with Categorical LLM-as-a-Judge.md>) · `llm-as-judge` · langfuse
  Shows how to classify user intent with categorical LLM-as-judge evaluators, including rubric design and structured scoring for production analysis.
- **2026-04-01** — [The Rage Clicks of LLM apps: High-Signal Production Monitoring for AI Customer Support Agents](<../evals-observability/monitoring/The Rage Clicks of LLM apps High-Signal Production Monitoring for AI Customer Support Agents.md>) · `monitoring` · langfuse
  Detailed production-monitoring pattern for AI customer-support agents using high-signal LLM-as-judge classifiers to detect rage-click-like failure modes.
- **2026-03-24** — [We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests](<../evals-observability/testing/We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests.md>) · `testing` · langfuse
  Case study of using Autoresearch to improve an AI skill, with emphasis on writing better tests and using research-agent output to harden behavior.
- **2026-03-13** — [How We Built an Agent Skill to Synthesize what Langfuse Users want](<../agents/tool-use/How We Built an Agent Skill to Synthesize what Langfuse Users want.md>) · `tool-use` · langfuse
  Case study of building an agent skill to synthesize user feedback and product needs, showing how agents can support operational product workflows.
- **2026-03-10** — [Simplifying Langfuse for Scale](<../infra-platform/deployment/Simplifying Langfuse for Scale.md>) · `deployment` · langfuse
  Architecture case study on simplifying Langfuse for scale, covering operational complexity, storage and compute boundaries, and reliability improvements.
- **2026-02-26** — [Evaluating AI Agent Skills](<../evals-observability/evaluation/Evaluating AI Agent Skills.md>) · `evaluation` · langfuse
  Explains how to evaluate AI agent skills, including task design, scoring, trace inspection, and regression testing for reusable agent capabilities.
- **2026-02-20** — [AI Agent Observability, Tracing & Evaluation with Langfuse](<../evals-observability/tracing/AI Agent Observability, Tracing & Evaluation with Langfuse.md>) · `tracing` · langfuse
  Guide to observability for AI agents, covering traces, spans, tool calls, evaluations, and debugging workflows for agentic systems.
- **2026-02-16** — [Using Agent Skills to Automatically Improve your Prompts](<../prompt-engineering/techniques/Using Agent Skills to Automatically Improve your Prompts.md>) · `techniques` · langfuse
  Shows how agent skills can automatically improve prompts, using evaluation feedback and reusable agent workflows to iterate on prompt quality.
- **2025-12-09** — [Building Langfuse's MCP Server: Code Reuse and Developer Experience](<../agents/tool-use/Building Langfuse's MCP Server Code Reuse and Developer Experience.md>) · `tool-use` · langfuse
  Engineering writeup on building the Langfuse MCP server, focusing on code reuse, developer experience, and exposing observability workflows to agents.
- **2025-11-25** — [Vibe Coding a Custom Annotation UI](<../product-engineering/ux-patterns/Vibe Coding a Custom Annotation UI.md>) · `ux-patterns` · langfuse
  Case study of building a custom annotation UI for eval workflows with AI-assisted coding, highlighting review ergonomics and human feedback collection.
- **2025-11-20** — [Incident Report for Nov 18, 2025](<../infra-platform/deployment/Incident Report for Nov 18, 2025.md>) · `deployment` · langfuse
  Incident report with reliability lessons for production observability infrastructure, including failure analysis and operational follow-up.
- **2025-11-12** — [Evaluating LLM Applications: A Comprehensive Roadmap](<../evals-observability/evaluation/Evaluating LLM Applications A Comprehensive Roadmap.md>) · `evaluation` · langfuse
  Roadmap for evaluating LLM applications, from defining quality criteria and datasets to running automated and human-assisted eval workflows.
- **2025-11-06** — [Systematic Evaluation of AI Agents](<../evals-observability/evaluation/Systematic Evaluation of AI Agents.md>) · `evaluation` · langfuse
  Covers systematic evaluation of AI agents, focusing on experiment interpretation, failure analysis, and how to compare agent variants.
- **2025-10-28** — [RAG Observability and Evals](<../rag-retrieval/pipelines/RAG Observability and Evals.md>) · `pipelines` · langfuse
  Explains observability and evaluation for RAG systems, including tracing retrieval/generation steps and measuring answer and context quality.
- **2025-10-21** — [LLM Testing: A Practical Guide to Automated Testing for LLM Applications](<../evals-observability/testing/LLM Testing A Practical Guide to Automated Testing for LLM Applications.md>) · `testing` · langfuse
  Practical guide to automated testing for LLM applications, covering test cases, regression checks, CI-style workflows, and quality gates.
- **2025-10-13** — [State of LLMs on the Application Layer](<../industry/trends/State of LLMs on the Application Layer.md>) · `trends` · langfuse
  Application-layer snapshot of LLM usage and model trends, useful for understanding production model adoption and quality/cost tradeoffs.
- **2025-10-09** — [Evaluating Multi-Turn Conversations](<../evals-observability/evaluation/Evaluating Multi-Turn Conversations.md>) · `evaluation` · langfuse
  Explains how to evaluate multi-turn conversations, including context retention, conversation-level scoring, and stateful failure modes.
- **2025-09-05** — [Automated Evaluations of LLM Applications](<../evals-observability/testing/Automated Evaluations of LLM Applications.md>) · `testing` · langfuse
  Guide to automated evaluations for LLM applications, including datasets, scorers, experiment runs, and continuous quality checks.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-05-21** — [How we Built Scalable & Customizable Dashboards](<../evals-observability/monitoring/How we Built Scalable & Customizable Dashboards.md>) · `monitoring` · langfuse
  Engineering writeup on building scalable customizable dashboards for observability data, covering query, rendering, and product architecture concerns.
- **2025-04-24** — [How we use LLMs to build and scale Langfuse](<../product-engineering/case-studies/How we use LLMs to build and scale Langfuse.md>) · `case-studies` · langfuse
  Case study of how Langfuse uses LLMs internally to build and scale the product, including practical workflows for AI-assisted engineering and operations.
- **2025-03-19** — [Comparing Open-Source AI Agent Frameworks](<../agents/harness/Comparing Open-Source AI Agent Frameworks.md>) · `harness` · langfuse
  Compares open-source AI agent frameworks and their architecture tradeoffs around orchestration, tools, memory, extensibility, and production readiness.
- **2025-03-13** — [Hugging Face and Langfuse: 5 Ways to use them Together](<../infra-platform/deployment/Hugging Face and Langfuse 5 Ways to use them Together.md>) · `deployment` · langfuse
  Shows ways to combine Hugging Face workflows with Langfuse for model experimentation, tracing, evaluation, and deployment feedback loops.
- **2025-03-04** — [LLM Evaluation 101: Best Practices, Challenges & Proven Techniques](<../evals-observability/evaluation/LLM Evaluation 101 Best Practices, Challenges & Proven Techniques.md>) · `evaluation` · langfuse
  Practical overview of LLM evaluation best practices, common challenges, scorer choices, datasets, and proven techniques for measuring application quality.
- **2025-02-20** — [The Agent Deep Dive: David Zhang’s Open Deep Research](<../agents/planning/The Agent Deep Dive David Zhang’s Open Deep Research.md>) · `planning` · langfuse
  Deep dive on Open Deep Research as an agentic system, covering planning, tool use, research workflows, and trace-based inspection.
- **2025-01-22** — [Evaluating and Monitoring Voice AI Agents](<../models/multimodal/Evaluating and Monitoring Voice AI Agents.md>) · `multimodal` · langfuse
  Covers evaluation and monitoring for voice AI agents, including speech-specific quality signals and agent behavior beyond text-only evals.
- **2024-11-17** — [From Zero to Scale: Langfuse's Infrastructure Evolution](<../infra-platform/deployment/From Zero to Scale Langfuse's Infrastructure Evolution.md>) · `deployment` · langfuse
  Case study of Langfuse infrastructure evolution from early product to scale, including data architecture, observability workloads, and operational tradeoffs.
- **2024-11-13** — [LLM Product Development for Product Managers](<../product-engineering/ux-patterns/LLM Product Development for Product Managers.md>) · `ux-patterns` · langfuse
  Product-management guide for LLM applications, connecting user workflows, quality criteria, feedback, and evals to AI product development decisions.
- **2024-10-14** — [OpenTelemetry (OTel) for LLM Observability](<../evals-observability/tracing/OpenTelemetry (OTel) for LLM Observability.md>) · `tracing` · langfuse
  Introduces OpenTelemetry for LLM observability and how OTel-style traces can standardize spans, metadata, and interoperability across AI systems.
- **2024-10-07** — [Observability in Multi-Step LLM Systems](<../evals-observability/tracing/Observability in Multi-Step LLM Systems.md>) · `tracing` · langfuse
  Explains observability needs for multi-step LLM systems, including tracing chains, tools, intermediate state, and failure points across complex application flows.
- **2024-09-23** — [Should you use an LLM Proxy to Build your Application?](<../infra-platform/deployment/Should you use an LLM Proxy to Build your Application.md>) · `deployment` · langfuse
  Explains the LLM proxy pattern for AI applications, including provider abstraction, centralized logging, key management, routing, and governance tradeoffs.
- **2024-05-14** — [Monitoring LLM Security & Reducing LLM Risks](<../product-engineering/security/Monitoring LLM Security & Reducing LLM Risks.md>) · `security` · langfuse
  Covers monitoring patterns for LLM security risks such as prompt injection, data leakage, and unsafe outputs, with observability as part of the mitigation loop.
- **2024-03-24** — [Trace complex LLM applications with the Langfuse decorator (Python)](<../evals-observability/tracing/Trace complex LLM applications with the Langfuse decorator (Python).md>) · `tracing` · langfuse
  Shows how to trace complex Python LLM applications with the Langfuse decorator, including nested calls, metadata, and observability patterns for multi-step workflows.
