# langchain

85 articles.

- **2026-07-14** — [How to Debug Coding Agents with LangSmith Traces](<../evals-observability/tracing/How to Debug Coding Agents with LangSmith Traces.md>) · `tracing` · langchain
  Introduces LangSmith tracing support across coding agents (Claude Code, Codex, Cursor, Copilot Chat, Pi, OpenCode, dcode), normalizing each tool's fragmented session/tool-call/subagent-handoff formats into one standardized trace structure so failures like a subagent inheriting a stale offset-paging helper are visible instead of requiring a fresh restart.
- **2026-07-10** — [OpenWiki Brains: Proactive Memory for AI Agents](<../agents/memory-context/OpenWiki Brains Proactive Memory for AI Agents.md>) · `memory-context` · langchain
  Introduces OpenWiki Brains as proactive wiki memory for agents, focused on persistent context and retrieval over project knowledge.
- **2026-07-08** — [Tuning the harness, not the model: a Nemotron 3 Ultra playbook](<../agents/harness/Tuning the harness, not the model a Nemotron 3 Ultra playbook.md>) · `harness` · langchain
  Nemotron 3 Ultra playbook arguing for harness tuning over model tuning, with practical agent-system design and eval implications.
- **2026-07-08** — [Deep Agents Code on NVIDIA NemoClaw](<../agents/tool-use/Deep Agents Code on NVIDIA NemoClaw.md>) · `tool-use` · langchain
  Covers a governed Deep Agents code blueprint on NVIDIA NemoClaw for sensitive code workflows, emphasizing controls around agentic coding.
- **2026-07-07** — [Improving Agents is a Data Mining Problem](<../evals-observability/monitoring/Improving Agents is a Data Mining Problem.md>) · `monitoring` · langchain
  Argues that improving agents is a data-mining problem over traces, failures, feedback, and recurring behavioral patterns.
- **2026-07-07** — [How Schneider Electric Built Their LLMOps Foundations With LangSmith](<../product-engineering/case-studies/How Schneider Electric Built Their LLMOps Foundations With LangSmith.md>) · `case-studies` · langchain
  Schneider Electric case study on building enterprise LLMOps foundations with LangSmith at scale.
- **2026-07-02** — [Your coding agent bill doubled. Here’s how to fix it.](<../infra-platform/cost/Your coding agent bill doubled. Here’s how to fix it.md>) · `cost` · langchain
  Practical guide to reducing coding-agent spend through model choice, caching, harness tuning, and workflow design.
- **2026-07-01** — [How to Use RLMs in Deep Agents](<../agents/memory-context/How to Use RLMs in Deep Agents.md>) · `memory-context` · langchain
  Explains how to use retrieval language models in Deep Agents to improve context selection and long-running agent performance.
- **2026-07-01** — [OpenWiki: Open Source Repo Documentation for Coding Agents](<../agents/tool-use/OpenWiki Open Source Repo Documentation for Coding Agents.md>) · `tool-use` · langchain
  Introduces OpenWiki as an agent for repository documentation, combining code understanding, retrieval, and generated docs.
- **2026-07-01** — [How Pendo uses LangSmith to trace Novus from user behavior to code fixes](<../product-engineering/case-studies/How Pendo uses LangSmith to trace Novus from user behavior to code fixes.md>) · `case-studies` · langchain
  Pendo case study tracing Novus from user behavior to code fixes, showing how traces connect product signals to agent improvements.
- **2026-06-30** — [Wiki Memory](<../agents/memory-context/Wiki Memory.md>) · `memory-context` · langchain
  Explains wiki memory as a persistent knowledge layer for agents, supporting retrieval, documentation, and long-term project context.
- **2026-06-30** — [Harbor x LangChain: A Unified Stack for Evaluating Agents](<../evals-observability/evaluation/Harbor x LangChain A Unified Stack for Evaluating Agents.md>) · `evaluation` · langchain
  Describes a unified stack for evaluating agents, integrating agent execution, traces, datasets, and scoring workflows.
- **2026-06-30** — [How Deep Agents Run Untrusted Code Without a Sandbox](<../product-engineering/security/How Deep Agents Run Untrusted Code Without a Sandbox.md>) · `security` · langchain
  Explains how Deep Agents run untrusted code without a conventional sandbox and the security tradeoffs in agent execution design.
- **2026-06-29** — [Introducing Dynamic Subagents in Deep Agents](<../agents/multi-agent/Introducing Dynamic Subagents in Deep Agents.md>) · `multi-agent` · langchain
  Introduces dynamic subagents in Deep Agents, covering delegation, specialized worker agents, and runtime coordination.
- **2026-06-29** — [How Candidly Built State-Aware Agent Harnesses with LangSmith](<../product-engineering/case-studies/How Candidly Built State-Aware Agent Harnesses with LangSmith.md>) · `case-studies` · langchain
  Candidly case study on building state-aware agent harnesses with LangSmith for production agent workflows.
- **2026-06-26** — [Building an auditable VC research agent with the Perplexity Agent API and LangGraph](<../agents/tool-use/Building an auditable VC research agent with the Perplexity Agent API and LangGraph.md>) · `tool-use` · langchain
  Walkthrough for building an auditable VC research agent with Perplexity, LangGraph, and LangSmith, emphasizing traceability and review.
- **2026-06-26** — [Prompt Caching with Deep Agents](<../prompt-engineering/context-engineering/Prompt Caching with Deep Agents.md>) · `context-engineering` · langchain
  Explains prompt caching for Deep Agents and how cache-aware context design reduces latency and cost for repeated agent work.
- **2026-06-25** — [How we built SmithDB’s inverted index for full-text search](<../rag-retrieval/search/How we built SmithDB’s inverted index for full-text search.md>) · `search` · langchain
  Deep dive on constructing and querying SmithDB's inverted index for full-text search over observability data.
- **2026-06-24** — [How to Build Memory into AI Agents](<../agents/memory-context/How to Build Memory into AI Agents.md>) · `memory-context` · langchain
  Explains how to build memory into AI agents through state, retrieval, persistence, and context injection patterns.
- **2026-06-16** — [The Art of Loop Engineering](<../agents/harness/The Art of Loop Engineering.md>) · `harness` · langchain
  Discusses loop engineering for agents, focusing on the control loops that govern planning, action, observation, and refinement.
- **2026-06-16** — [Why Fleet Has General Purpose Chat and Specialized Agents](<../product-engineering/architecture/Why Fleet Has General Purpose Chat and Specialized Agents.md>) · `architecture` · langchain
  Fleet case study explaining why a product needs both general-purpose chat and specialized agents for different user workflows.
- **2026-06-15** — [Building a 100x Cheaper Trace Judge with Fireworks](<../evals-observability/llm-as-judge/Building a 100x Cheaper Trace Judge with Fireworks.md>) · `llm-as-judge` · langchain
  Shows how to build a lower-cost trace judge with Fireworks, focusing on evaluator cost reduction while preserving useful scoring quality.
- **2026-06-15** — [How LangChain Made Coding Agent Spend Predictable](<../infra-platform/cost/How LangChain Made Coding Agent Spend Predictable.md>) · `cost` · langchain
  Explains how LangChain made coding-agent spend more predictable using constraints, monitoring, and workflow-level cost controls.
- **2026-06-12** — [How to Choose the Right Sandbox for AI Agents](<../agents/computer-use/How to Choose the Right Sandbox for AI Agents.md>) · `computer-use` · langchain
  Guide to choosing an agent sandbox based on isolation, tool access, persistence, security, and operational constraints.
- **2026-06-12** — [How Box AI built enterprise content agents with Deep Agents](<../product-engineering/case-studies/How Box AI built enterprise content agents with Deep Agents.md>) · `case-studies` · langchain
  Case study of Box AI moving enterprise content workflows to Deep Agents, covering agent architecture and production constraints.
- **2026-06-11** — [How Benchling builds agents when the smartest AI isn't smart enough](<../product-engineering/case-studies/How Benchling builds agents when the smartest AI isn't smart enough.md>) · `case-studies` · langchain
  Case-study notes on how Benchling builds agents when model capability is insufficient on its own, emphasizing workflow design and product constraints.
- **2026-06-10** — [Full Text Search in SmithDB: Designing an Inverted Index for Object Storage](<../rag-retrieval/search/Full Text Search in SmithDB Designing an Inverted Index for Object Storage.md>) · `search` · langchain
  Architecture writeup on designing an inverted index for object storage in SmithDB, motivated by full-text search over agent traces.
- **2026-06-10** — [The Missing Link Between Agents and Applications](<../product-engineering/architecture/The Missing Link Between Agents and Applications.md>) · `architecture` · langchain
  Explains the missing application-layer pieces around agents, connecting agent runtimes to product interfaces, state, and deployment workflows.
- **2026-06-05** — [Give your agent its own computer](<../agents/computer-use/Give your agent its own computer.md>) · `computer-use` · langchain
  Argues for giving agents isolated computers or sandboxes so they can run tools while preserving control, safety, and reproducibility.
- **2026-06-04** — [Fault Tolerance in LangGraph: Retries, Timeouts and Error Handlers](<../agents/harness/Fault Tolerance in LangGraph Retries, Timeouts and Error Handlers.md>) · `harness` · langchain
  Explains fault tolerance in LangGraph with retries, timeouts, and error handlers for more reliable long-running agents.
- **2026-06-04** — [Model Neutrality: Why Avoiding AI Vendor Lock-In Matters](<../infra-platform/deployment/Model Neutrality Why Avoiding AI Vendor Lock-In Matters.md>) · `deployment` · langchain
  Explains model neutrality and why avoiding AI vendor lock-in matters for provider routing, cost control, and long-term architecture.
- **2026-06-03** — [How to Build a Custom Agent Harness](<../agents/harness/How to Build a Custom Agent Harness.md>) · `harness` · langchain
  Guide to building a custom agent harness, covering control loop design, state, tools, observability, and evaluation hooks.
- **2026-06-03** — [How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith](<../product-engineering/case-studies/How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith.md>) · `case-studies` · langchain
  Harmonic case study on rebuilding Scout with Deep Agents and LangSmith, linking agent architecture to retention and evaluation.
- **2026-06-02** — [Designing Efficient Verifiers for Legal Agents](<../evals-observability/llm-as-judge/Designing Efficient Verifiers for Legal Agents.md>) · `llm-as-judge` · langchain
  Explains how to design efficient verifiers for legal agents so domain-specific correctness can be checked without excessive cost.
- **2026-06-02** — [Introducing Rubrics: Build Agents that Evaluate and Correct Their Work](<../evals-observability/llm-as-judge/Introducing Rubrics Build Agents that Evaluate and Correct Their Work.md>) · `llm-as-judge` · langchain
  Introduces rubrics for Deep Agents so agents can evaluate and correct their own work against explicit criteria.
- **2026-06-01** — [How Rippling built production AI in 6 months with Deep Agents and LangSmith](<../product-engineering/case-studies/How Rippling built production AI in 6 months with Deep Agents and LangSmith.md>) · `case-studies` · langchain
  Rippling case study on rolling production AI across products with Deep Agents and LangSmith in a six-month buildout.
- **2026-05-29** — [Interpreter Skills: Building Workflows for Agents](<../agents/tool-use/Interpreter Skills Building Workflows for Agents.md>) · `tool-use` · langchain
  Introduces interpreter skills as reusable workflows for agents that need to execute code, inspect outputs, and compose tools.
- **2026-05-27** — [How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith](<../product-engineering/case-studies/How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Lyft case study on building a self-serve AI agent platform for customer support with LangGraph and LangSmith.
- **2026-05-26** — [Mission Control for Self-Hosted LangSmith on Kubernetes](<../infra-platform/deployment/Mission Control for Self-Hosted LangSmith on Kubernetes.md>) · `deployment` · langchain
  Guide to operating self-hosted LangSmith on Kubernetes, covering deployment, operations, and control-plane concerns.
- **2026-05-20** — [EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API](<../agents/tool-use/EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.md>) · `tool-use` · langchain
  Case study building a financial research agent for EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.
- **2026-05-19** — [How We Built LangSmith Engine, Our Agent for Improving Agents](<../agents/planning/How We Built LangSmith Engine, Our Agent for Improving Agents.md>) · `planning` · langchain
  Explains LangSmith Engine, an agent for improving agents through trace analysis, feedback, evals, and iterative changes.
- **2026-05-13** — [LangSmith Sandboxes are Generally Available](<../agents/computer-use/LangSmith Sandboxes are Generally Available.md>) · `computer-use` · langchain
  Covers LangSmith Sandboxes for safely running agent code and tools in isolated execution environments.
- **2026-05-13** — [We built SmithDB, the data layer for agent observability](<../infra-platform/deployment/We built SmithDB, the data layer for agent observability.md>) · `deployment` · langchain
  Introduces SmithDB as a data layer for agent observability, optimized for storing and querying trace-heavy workloads.
- **2026-05-12** — [Delta Channels: How We’re Evolving our Runtime for Long-Running Agents](<../agents/harness/Delta Channels How We’re Evolving our Runtime for Long-Running Agents.md>) · `harness` · langchain
  Describes Delta Channels as an evolution of the LangGraph runtime for long-running agents, focused on durable state and runtime communication.
- **2026-05-09** — [The Agent Development Lifecycle: Build, Test, Deploy & Monitor AI Agents](<../agents/planning/The Agent Development Lifecycle Build, Test, Deploy & Monitor AI Agents.md>) · `planning` · langchain
  Defines the agent development lifecycle from build and test through deployment, monitoring, and iterative improvement.
- **2026-05-05** — [Agent observability needs feedback to power learning](<../evals-observability/monitoring/Agent observability needs feedback to power learning.md>) · `monitoring` · langchain
  Explains why agent observability needs feedback loops from users, evaluators, and production traces to power ongoing agent learning and improvement.
- **2026-04-27** — [How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements](<../product-engineering/security/How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements.md>) · `security` · langchain
  Connects LangSmith and LangChain OSS workflows to EU AI Act readiness, including observability, evaluation, governance, and auditability.
- **2026-04-17** — [Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering](<../agents/multi-agent/Agentic Engineering How Swarms of AI Agents Are Redefining Software Engineering.md>) · `multi-agent` · langchain
  Discusses how swarms of agents change software engineering workflows, including orchestration, delegation, review, and human oversight.
- **2026-04-16** — [Reusable Evaluators and Evaluator Templates in LangSmith](<../evals-observability/llm-as-judge/Reusable Evaluators and Evaluator Templates in LangSmith.md>) · `llm-as-judge` · langchain
  Covers reusable evaluator templates in LangSmith for standardizing scoring logic across teams and experiments.
- **2026-04-09** — [Human judgment in the agent improvement loop](<../evals-observability/evaluation/Human judgment in the agent improvement loop.md>) · `evaluation` · langchain
  Explains where human judgment fits into the agent improvement loop, including review, labeling, feedback, and evaluator calibration.
- **2026-03-27** — [Agent Evaluation Readiness Checklist](<../evals-observability/evaluation/Agent Evaluation Readiness Checklist.md>) · `evaluation` · langchain
  Checklist for agent-evaluation readiness covering task definitions, datasets, traces, scoring, human review, and rollout criteria.
- **2026-03-26** — [How we build evals for Deep Agents](<../evals-observability/evaluation/How we build evals for Deep Agents.md>) · `evaluation` · langchain
  Describes how LangChain builds evals for Deep Agents, including datasets, task realism, scorers, and iteration loops.
- **2026-03-09** — [How we built LangChain’s GTM Agent](<../product-engineering/case-studies/How we built LangChain’s GTM Agent.md>) · `case-studies` · langchain
  Case study of building LangChain's GTM agent, covering workflow design, tool use, and production iteration.
- **2026-03-05** — [Evaluating Skills](<../evals-observability/evaluation/Evaluating Skills.md>) · `evaluation` · langchain
  Explains how to evaluate agent skills as reusable capabilities, with tests that isolate skill behavior from the full agent loop.
- **2026-02-26** — [Agent Observability: How to Monitor and Evaluate LLM Agents in Production](<../evals-observability/monitoring/Agent Observability How to Monitor and Evaluate LLM Agents in Production.md>) · `monitoring` · langchain
  Guide to monitoring and evaluating LLM agents in production, including traces, feedback, evals, and alerting signals.
- **2026-02-18** — [monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1](<../product-engineering/case-studies/monday Service + LangSmith Building a Code-First Evaluation Strategy from Day 1.md>) · `case-studies` · langchain
  monday Service case study on building a code-first evaluation strategy for AI product quality from day one.
- **2026-02-13** — [On Agent Frameworks and Agent Observability](<../agents/harness/On Agent Frameworks and Agent Observability.md>) · `harness` · langchain
  Connects agent-framework design with observability requirements, arguing that runtime structure determines what teams can debug and evaluate.
- **2026-01-28** — [Context Management for Deep Agents](<../agents/memory-context/Context Management for Deep Agents.md>) · `memory-context` · langchain
  Explains context management for Deep Agents, including what information to retain, retrieve, summarize, or isolate during long-running tasks.
- **2026-01-28** — [How to Debug & Evaluate AI Agents with Observability — LangChain Guide](<../evals-observability/tracing/How to Debug & Evaluate AI Agents with Observability — LangChain Guide.md>) · `tracing` · langchain
  Guide to debugging and evaluating AI agents with observability, using traces to inspect tool calls, intermediate steps, and failure modes.
- **2025-12-09** — [Agent Engineering: A New Discipline](<../agents/planning/Agent Engineering A New Discipline.md>) · `planning` · langchain
  Defines agent engineering as a discipline around designing, evaluating, observing, and iterating on production agents rather than treating them as prompt-only systems.
- **2025-12-03** — [Evaluating Deep Agents: Our Learnings](<../evals-observability/evaluation/Evaluating Deep Agents Our Learnings.md>) · `evaluation` · langchain
  Shares lessons from evaluating Deep Agents, including task design, traces, scoring, and how agent architectures change eval needs.
- **2025-09-11** — [How to turn Claude Code into a domain specific coding agent](<../agents/tool-use/How to turn Claude Code into a domain specific coding agent.md>) · `tool-use` · langchain
  Shows how to turn Claude Code into a domain-specific coding agent using instructions, tools, context, and workflow constraints.
- **2025-09-11** — [Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith](<../product-engineering/case-studies/Monte Carlo Building Data + AI Observability Agents with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Monte Carlo case study on building data and AI observability agents with LangGraph and LangSmith.
- **2025-09-04** — [Building LangGraph: Designing an Agent Runtime from first principles](<../agents/harness/Building LangGraph Designing an Agent Runtime from first principles.md>) · `harness` · langchain
  Design history of LangGraph as an agent runtime from first principles, covering control flow, state, durability, and production requirements.
- **2025-08-06** — [Introducing Open SWE: An Open-Source Asynchronous Coding Agent](<../agents/tool-use/Introducing Open SWE An Open-Source Asynchronous Coding Agent.md>) · `tool-use` · langchain
  Introduces Open SWE as an open-source asynchronous coding agent and discusses its architecture for long-running coding tasks.
- **2025-06-16** — [How and when to build multi-agent systems](<../agents/multi-agent/How and when to build multi-agent systems.md>) · `multi-agent` · langchain
  Guidance on when multi-agent systems are warranted and how to design agent roles, coordination, and boundaries.
- **2025-04-20** — [How to think about agent frameworks](<../agents/harness/How to think about agent frameworks.md>) · `harness` · langchain
  Framework for evaluating agent frameworks by abstraction level, control, durability, observability, and fit to production workflows.
- **2025-03-27** — [Introducing End-to-End OpenTelemetry Support in LangSmith](<../evals-observability/tracing/Introducing End-to-End OpenTelemetry Support in LangSmith.md>) · `tracing` · langchain
  Introduces end-to-end OpenTelemetry support in LangSmith for standardizing traces across AI application components.
- **2025-02-26** — [Evaluating Large Language Models With OpenEvals](<../evals-observability/llm-as-judge/Evaluating Large Language Models With OpenEvals.md>) · `llm-as-judge` · langchain
  Guide to evaluating large language models with OpenEvals, including reusable evaluators and model comparison workflows.
- **2025-02-10** — [Benchmarking Single Agent Performance](<../agents/planning/Benchmarking Single Agent Performance.md>) · `planning` · langchain
  Benchmarks single-agent ReAct-style performance and discusses evaluation methodology for agent reasoning/tool-use loops.
- **2024-11-13** — [Promptim: an experimental library for prompt optimization](<../prompt-engineering/techniques/Promptim an experimental library for prompt optimization.md>) · `techniques` · langchain
  Introduces Promptim as an experimental prompt-optimization library that uses evaluation feedback to improve prompts.
- **2024-09-26** — [Pushing LangSmith to new limits with Replit Agent's complex workflows](<../product-engineering/case-studies/Pushing LangSmith to new limits with Replit Agent's complex workflows.md>) · `case-studies` · langchain
  Replit Agent case study on tracing and managing complex agent workflows with LangSmith.
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<../rag-retrieval/search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-06-26** — [Aligning LLM-as-a-Judge with Human Preferences](<../evals-observability/llm-as-judge/Aligning LLM-as-a-Judge with Human Preferences.md>) · `llm-as-judge` · langchain
  Covers aligning LLM-as-judge evaluators with human preferences through calibration, examples, and evaluation design.
- **2024-06-19** — [How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x](<../product-engineering/case-studies/How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x.md>) · `case-studies` · langchain
  Factory case study on automating feedback loops with LangSmith to improve iteration speed and production agent quality.
- **2024-05-15** — [Pairwise Evaluations with LangSmith](<../evals-observability/llm-as-judge/Pairwise Evaluations with LangSmith.md>) · `llm-as-judge` · langchain
  Explains pairwise evaluations with LangSmith for comparing model or prompt outputs using preference-style scoring.
- **2024-05-01** — [Regression Testing with LangSmith](<../evals-observability/testing/Regression Testing with LangSmith.md>) · `testing` · langchain
  Explains regression testing with LangSmith for preventing LLM application quality regressions during prompt, model, or code changes.
- **2024-03-15** — [Benchmarking Query Analysis in High Cardinality Situations](<../rag-retrieval/search/Benchmarking Query Analysis in High Cardinality Situations.md>) · `search` · langchain
  Benchmarks query analysis in high-cardinality situations, relevant to retrieval, search, and observability filtering workloads.
- **2024-03-11** — [Iterating Towards LLM Reliability with Evaluation Driven Development](<../evals-observability/testing/Iterating Towards LLM Reliability with Evaluation Driven Development.md>) · `testing` · langchain
  Explains evaluation-driven development for LLM reliability using regression tests, examples, and iterative quality gates.
- **2024-01-16** — [Build and deploy a RAG app with Pinecone Serverless](<../rag-retrieval/pipelines/Build and deploy a RAG app with Pinecone Serverless.md>) · `pipelines` · langchain
  Walkthrough for building and deploying a RAG application with Pinecone Serverless and LangChain components.
- **2023-12-20** — [Benchmarking Agent Tool Use](<../agents/tool-use/Benchmarking Agent Tool Use.md>) · `tool-use` · langchain
  Benchmarking study for agent tool use, focused on measuring whether agents choose and invoke tools correctly across tasks.
- **2023-12-05** — [Extraction Benchmarking](<../models/benchmarks/Extraction Benchmarking.md>) · `benchmarks` · langchain
  Benchmarking post for extraction tasks, comparing structured-output performance and evaluation approaches for information extraction.
- **2023-11-22** — [Sharing LangSmith Benchmarks](<../models/benchmarks/Sharing LangSmith Benchmarks.md>) · `benchmarks` · langchain
  Shares LangSmith benchmarks for evaluating models and chains, including methodology and public comparison workflows.
- **2023-10-17** — [Test Run Comparisons](<../evals-observability/testing/Test Run Comparisons.md>) · `testing` · langchain
  Explains test-run comparisons for evaluating changes across LLM application versions and identifying regressions.
- **2023-10-16** — [Testing Fine Tuned Open Source Models in LangSmith](<../models/fine-tuning/Testing Fine Tuned Open Source Models in LangSmith.md>) · `fine-tuning` · langchain
  Shows how to test fine-tuned open-source models in LangSmith using evaluations and comparison workflows.
