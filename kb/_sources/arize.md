# arize

183 articles.

- **2026-07-13** — [How do you make an LLM, anyway? Microsoft just published a textbook.](<../models/reinforcement-learning/How do you make an LLM, anyway Microsoft just published a textbook.md>) · `reinforcement-learning` · arize
  Breaks down Microsoft's 109-page MAI-Thinking-1 technical report: 30-trillion-token pretraining on 8,192 GPUs with a 54.6%-code data mix, mid-training context extension from 16K to 262K tokens, and RL post-training with reward-hacking countermeasures like network-isolated coding environments and time-traveled repo snapshots with future commits scrubbed.
- **2026-07-10** — [What is a loop in AI engineering, anyway?](<../agents/harness/What is a loop in AI engineering, anyway.md>) · `harness` · arize
  Defines feedback loops in AI engineering and why loops are central to agent and eval system design.
- **2026-07-10** — [3 production patterns for AI agents and how to evaluate each one](<../agents/planning/3 production patterns for AI agents and how to evaluate each one.md>) · `planning` · arize
  Breaks production agents into local coding agents, in-app assistants, and operational agents, then maps each pattern to different harness, rollout, and evaluation needs.
- **2026-07-09** — [Trace before you migrate: Measuring Kubernetes bottlenecks in AI agent sandboxes](<../infra-platform/deployment/Trace before you migrate Measuring Kubernetes bottlenecks in AI agent sandboxes.md>) · `deployment` · arize
  Shows how tracing can diagnose Kubernetes bottlenecks in AI agent sandboxes before migration decisions.
- **2026-07-08** — [The agent is the user now: lessons from the founder of WorkOS](<../product-engineering/security/The agent is the user now lessons from the founder of WorkOS.md>) · `security` · arize
  Interview-driven discussion of agents as users, covering identity, permissions, memory, evals, and feedback loops as core production-agent infrastructure.
- **2026-07-07** — [Evals in CI: How to write your LLM evals as tests with Arize Phoenix](<../evals-observability/testing/Evals in CI How to write your LLM evals as tests with Arize Phoenix.md>) · `testing` · arize
  Practical guide to writing LLM evals as CI tests with Arize Phoenix, including how to start with executable checks.
- **2026-07-06** — [Own the loop: A field guide to agent harnesses](<../agents/harness/Own the loop A field guide to agent harnesses.md>) · `harness` · arize
  Field guide to owning the agent harness loop, from task control to measurement and iteration.
- **2026-07-02** — [How to evaluate AI agents, avoid reward hacking, and build better specs](<../evals-observability/evaluation/How to evaluate AI agents, avoid reward hacking, and build better specs.md>) · `evaluation` · arize
  Connects agent evaluation with specification quality, including reward hacking risks and tighter behavioral contracts.
- **2026-07-01** — [Model subsidies are ending. What do you do now?](<../infra-platform/cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-30** — [AI evals are a data science problem: What most teams get wrong](<../evals-observability/evaluation/AI evals are a data science problem What most teams get wrong.md>) · `evaluation` · arize
  Argues that AI evaluation is a data science workflow requiring careful labeling, slices, standards, and failure analysis rather than a simple dashboard metric.
- **2026-06-24** — [Long-horizon agent benchmarks are fragmenting: a field guide to what each one actually measures](<../models/benchmarks/Long-horizon agent benchmarks are fragmenting a field guide to what each one actually measures.md>) · `benchmarks` · arize
  Field guide to long-horizon agent benchmarks and what each benchmark family reveals about agent performance.
- **2026-06-22** — [Project Rosetta Stone: a reference implementation for instrumenting agents in any framework](<../evals-observability/tracing/Project Rosetta Stone a reference implementation for instrumenting agents in any framework.md>) · `tracing` · arize
  Describes a reference implementation for instrumenting agents across frameworks, useful for standardizing trace capture.
- **2026-06-19** — [Why AI token costs don't tell you if your AI is working](<../infra-platform/cost/Why AI token costs don't tell you if your AI is working.md>) · `cost` · arize
  Explains why token cost alone is an incomplete production metric and how quality, latency, and outcomes must be measured together.
- **2026-06-18** — [What is an agent harness? Why harnesses are replacing agent frameworks](<../agents/harness/What is an agent harness Why harnesses are replacing agent frameworks.md>) · `harness` · arize
  Explains why agent harnesses are replacing simple framework use as the unit of production agent engineering.
- **2026-06-17** — [Two labs started dreaming, and they built two different architectures](<../models/reasoning/Two labs started dreaming, and they built two different architectures.md>) · `reasoning` · arize
  Compares two different AI architecture directions from research labs, focusing on design choices and implications.
- **2026-06-16** — [What is agent orchestration? Frameworks, runtimes, and observability explained](<../agents/harness/What is agent orchestration Frameworks, runtimes, and observability explained.md>) · `harness` · arize
  Explains agent orchestration across frameworks, runtimes, and observability concerns.
- **2026-06-15** — [One agent, two trace destinations: Arize AX + Databricks Unity Catalog](<../evals-observability/tracing/One agent, two trace destinations Arize AX + Databricks Unity Catalog.md>) · `tracing` · arize
  Shows how a single agent can emit traces to multiple destinations, highlighting interoperability concerns for observability stacks.
- **2026-06-12** — [Memory is still a missing primitive: Cataloguing what the field is actually shipping](<../agents/memory-context/Memory is still a missing primitive Cataloguing what the field is actually shipping.md>) · `memory-context` · arize
  Catalogs memory approaches currently shipping in AI systems and frames memory as a missing primitive for agents.
- **2026-06-11** — [PostgresFS vs. SQL skills: should AI agents fake a filesystem?](<../agents/tool-use/PostgresFS vs. SQL skills should AI agents fake a filesystem.md>) · `tool-use` · arize
  Compares filesystem-like and SQL-backed skill interfaces for AI agents, focusing on state access and tool ergonomics.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<../evals-observability/tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-09** — [How to detect credential theft in AI agent harness traces](<../product-engineering/security/How to detect credential theft in AI agent harness traces.md>) · `security` · arize
  Shows how agent harness traces can expose credential theft and other security failures during tool use.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<../evals-observability/monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-06-02** — [The end of fine-tuning: Why evals, context, and traces matter more](<../models/fine-tuning/The end of fine-tuning Why evals, context, and traces matter more.md>) · `fine-tuning` · arize
  Argues that evals, context, and traces can reduce the need for fine-tuning in many production AI workflows.
- **2026-06-02** — [AI benchmarks are breaking. Trace analysis is what comes next.](<../evals-observability/benchmark-design/AI benchmarks are breaking. Trace analysis is what comes next.md>) · `benchmark-design` · arize
  Explains why outcome-only agent benchmarks are losing resolution as agents exploit tests, and argues for trace analysis to distinguish real solving from benchmark gaming.
- **2026-06-01** — [How Hermes implements an open source agent harness architecture](<../agents/harness/How Hermes implements an open source agent harness architecture.md>) · `harness` · arize
  Breaks down Hermes as an open-source agent harness architecture, focusing on components, control flow, and implementation boundaries.
- **2026-06-01** — [The best eval harness for production AI and agents: A comparison](<../evals-observability/testing/The best eval harness for production AI and agents A comparison.md>) · `testing` · arize
  Compares production AI eval harnesses and highlights the design dimensions that matter for agents and applications.
- **2026-05-29** — [How to build a better agent harness with traces and evals](<../agents/planning/How to build a better agent harness with traces and evals.md>) · `planning` · arize
  Shows how traces and evals combine inside an agent harness to make agent behavior easier to test and improve.
- **2026-05-27** — [From production traces to better AI agents: Automating the LLMOps feedback loop](<../evals-observability/tracing/From production traces to better AI agents Automating the LLMOps feedback loop.md>) · `tracing` · arize
  Shows how production traces can feed evaluation and improvement loops for AI agents rather than remaining passive monitoring data.
- **2026-05-26** — [How to ship a local LLM that matches frontier LLMs with evals and prompt engineering](<../models/fine-tuning/How to ship a local LLM that matches frontier LLMs with evals and prompt engineering.md>) · `fine-tuning` · arize
  Explains how evals and prompt engineering can make smaller local models viable substitutes for frontier models on constrained tasks.
- **2026-05-21** — [How to build LLM-as-a-Judge evaluators that hold up in production](<../evals-observability/llm-as-judge/How to build LLM-as-a-Judge evaluators that hold up in production.md>) · `llm-as-judge` · arize
  Details how to design LLM-as-judge evaluators that remain useful in production, including calibration and failure modes.
- **2026-05-20** — [What we learned testing 7 models under the same agent harness](<../evals-observability/testing/What we learned testing 7 models under the same agent harness.md>) · `testing` · arize
  Compares seven models under a shared agent harness, showing how harness-controlled tests expose model behavior differences.
- **2026-05-19** — [Building a self-improving agent on a context graph of human disagreement](<../agents/memory-context/Building a self-improving agent on a context graph of human disagreement.md>) · `memory-context` · arize
  Shows how a context graph of human disagreement can support a self-improving agent loop.
- **2026-05-18** — [Coding agent tracing and evaluation: An open source tool to improve AI coding workflows](<../evals-observability/tracing/Coding agent tracing and evaluation An open source tool to improve AI coding workflows.md>) · `tracing` · arize
  Introduces open-source tracing and evaluation for coding agents, focusing on visibility into tool use and code-edit behavior.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<../evals-observability/monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-12** — [Models got an order of magnitude better at following instructions in one year](<../models/benchmarks/Models got an order of magnitude better at following instructions in one year.md>) · `benchmarks` · arize
  Analyzes instruction-following benchmark changes and what they imply for tracking model quality over time.
- **2026-05-11** — [From observability to context: What’s next for Arize Phoenix](<../evals-observability/tracing/From observability to context What’s next for Arize Phoenix.md>) · `tracing` · arize
  Connects LLM observability with context management, showing how traces and application state can become reusable context for better agents.
- **2026-05-07** — [Agent harnesses have an expiration date](<../agents/harness/Agent harnesses have an expiration date.md>) · `harness` · arize
  Argues that agent harnesses need lifecycle management as tools, models, and objectives drift, with implications for ongoing evaluation.
- **2026-05-05** — [AI agent evaluation: How to test, debug, and improve agents in production](<../evals-observability/testing/AI agent evaluation How to test, debug, and improve agents in production.md>) · `testing` · arize
  Explains how to test, debug, and improve AI agents in production with structured evaluation and observability.
- **2026-05-04** — [Swarm management in agent harnesses: owning long-running agents](<../agents/multi-agent/Swarm management in agent harnesses owning long-running agents.md>) · `multi-agent` · arize
  Explains swarm management patterns for long-running agent harnesses and how ownership/control should be structured.
- **2026-05-04** — [What is an evaluation harness?](<../evals-observability/testing/What is an evaluation harness.md>) · `testing` · arize
  Defines evaluation harnesses and how they structure repeatable measurement for AI applications and agents.
- **2026-05-01** — [MCP vs. CLI Skills for agents: what our eval found (and which you should use)](<../agents/tool-use/MCP vs. CLI Skills for agents what our eval found (and which you should use).md>) · `tool-use` · arize
  Compares MCP and CLI skills for agents using evaluation results, focusing on reliability and tool interface design.
- **2026-05-01** — [Why agent telemetry needs standards](<../evals-observability/tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-04-30** — [Prompt templates as configs, not code](<../prompt-engineering/context-engineering/Prompt templates as configs, not code.md>) · `context-engineering` · arize
  Argues for treating prompt templates as configuration, improving iteration, versioning, and deployment safety.
- **2026-04-29** — [Using context graphs: build a data moat like Google's using your enterprise data](<../agents/memory-context/Using context graphs build a data moat like Google's using your enterprise data.md>) · `memory-context` · arize
  Explains context graphs as an enterprise memory layer for agents and retrieval-heavy AI systems.
- **2026-04-28** — [Context management in agent harnesses: memory, files, and subagents](<../agents/memory-context/Context management in agent harnesses memory, files, and subagents.md>) · `memory-context` · arize
  Detailed guide to context management in agent harnesses, including memory, files, subagents, and strategies for working within context limits.
- **2026-04-24** — [What is an agent harness?](<../agents/harness/What is an agent harness.md>) · `harness` · arize
  Defines an agent harness and the responsibilities it carries for control flow, state, tools, and testing.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<../evals-observability/evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-04-22** — [How to add an evaluation harness to your Gemini CLI coding agent](<../evals-observability/testing/How to add an evaluation harness to your Gemini CLI coding agent.md>) · `testing` · arize
  Walks through adding an evaluation harness to a Gemini CLI coding agent, including how to measure and compare agent behavior.
- **2026-04-20** — [Code is free, technical debt isn’t: Notes from AI Engineer Europe](<../industry/trends/Code is free, technical debt isn’t Notes from AI Engineer Europe.md>) · `trends` · arize
  AI Engineer Europe notes arguing that faster code generation increases the need for verification, standards, and technical-debt management.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<../evals-observability/tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<../agents/planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-04-04** — [How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours](<../rag-retrieval/pipelines/How Arize Skills Improved RAG Recall from 39% to 75% in 8 Hours.md>) · `pipelines` · arize
  Uses an eval-guided RAG improvement loop to show how retrieval recall can be diagnosed and improved quickly.
- **2026-04-03** — [From First Eval to Autonomous AI Ops: A Maturity Model for AI Evaluation](<../evals-observability/evaluation/From First Eval to Autonomous AI Ops A Maturity Model for AI Evaluation.md>) · `evaluation` · arize
  Defines a maturity model for moving from first evaluations to automated AI operations, with emphasis on eval loops and production governance.
- **2026-03-22** — [100 AI Agents Per Employee: The Enterprise Governance Gap](<../product-engineering/security/100 AI Agents Per Employee The Enterprise Governance Gap.md>) · `security` · arize
  Argues that enterprises adopting large populations of AI agents need governance for permissions, ownership, auditability, and lifecycle management before agent scale outpaces human oversight.
- **2026-03-19** — [Managing Memory in AI Agents: Beyond the Context Window](<../agents/memory-context/Managing Memory in AI Agents Beyond the Context Window.md>) · `memory-context` · arize
  Covers memory and context-window management patterns for agents that need to preserve useful state over long tasks.
- **2026-03-10** — [How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator](<../evals-observability/evaluation/How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator.md>) · `evaluation` · arize
  Case study on using evals plus an agentic workflow to iteratively improve a newsletter-generation system.
- **2026-03-05** — [How to Build Planning Into Your Agent (The Architecture That Actually Works)](<../agents/planning/How to Build Planning Into Your Agent (The Architecture That Actually Works).md>) · `planning` · arize
  Explains planning architectures for agents and how explicit planning changes control flow, reliability, and debugging.
- **2026-03-02** — [How to Evaluate Tool-Calling Agents](<../evals-observability/evaluation/How to Evaluate Tool-Calling Agents.md>) · `evaluation` · arize
  Covers evaluation methods for tool-calling agents, including how to assess action selection and tool-use correctness.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<../evals-observability/monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<../evals-observability/tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<../evals-observability/tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-24** — [Alyx 2.0: The AI Agent That Actually Plans](<../agents/planning/Alyx 2.0 The AI Agent That Actually Plans.md>) · `planning` · arize
  Introduces Alyx 2.0 as an agent that plans over observability workflows, covering product design lessons from building a more capable AI analyst.
- **2026-02-23** — [Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems](<../rag-retrieval/pipelines/Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems.md>) · `pipelines` · arize
  Explains production RAG architecture with Google ADK and Arize AX, including agentic retrieval and evaluation concerns.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<../evals-observability/tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-17** — [Inside Typeform’s AI Agent Stack](<../product-engineering/case-studies/Inside Typeform’s AI Agent Stack.md>) · `case-studies` · arize
  Case study of Typeform’s AI agent stack, useful for understanding production architecture choices in agent applications.
- **2026-01-29** — [Hierarchical Memory Management In Agent Harnesses](<../agents/memory-context/Hierarchical Memory Management In Agent Harnesses.md>) · `memory-context` · arize
  Explains hierarchical memory management patterns for agent harnesses, including how state is organized across short and long horizons.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<../evals-observability/monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-29** — [OWASP Top 10 for Agentic Applications: Compliance Guide](<../product-engineering/security/OWASP Top 10 for Agentic Applications Compliance Guide.md>) · `security` · arize
  Maps OWASP risks to agentic applications and explains compliance-oriented controls for agent systems.
- **2026-01-22** — [How Observability-Driven Sandboxing Secures AI Agents](<../product-engineering/security/How Observability-Driven Sandboxing Secures AI Agents.md>) · `security` · arize
  Explains how sandbox telemetry and observability can harden AI agents that execute code or use external tools.
- **2026-01-21** — [AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)](<../agents/tool-use/AI Agent interfaces In 2026 Filesystem vs API vs Database (What Actually Works).md>) · `tool-use` · arize
  Compares filesystem, API, and database interfaces for agents, using memory benchmarks and practical interface tradeoffs to evaluate what works in production.
- **2026-01-08** — [How Context Graphs Turn Agent Traces Into Durable Business Assets](<../agents/memory-context/How Context Graphs Turn Agent Traces Into Durable Business Assets.md>) · `memory-context` · arize
  Describes context graphs as a way to transform agent traces into durable memory and operational knowledge assets.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<../product-engineering/security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-12-01** — [AWS Bedrock AgentCore Observability with Arize AX: Operationalizing AI Agents At Scale](<../evals-observability/tracing/AWS Bedrock AgentCore Observability with Arize AX Operationalizing AI Agents At Scale.md>) · `tracing` · arize
  Walks through operationalizing AWS Bedrock AgentCore agents with Arize AX observability, focusing on traces, evaluation, and production-scale monitoring.
- **2025-11-20** — [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](<../prompt-engineering/context-engineering/CLAUDE.md Best Practices Learned from Optimizing Claude Code with Prompt Learning.md>) · `context-engineering` · arize
  Extracts CLAUDE.md best practices from prompt-learning experiments that optimized Claude Code behavior through repository instructions.
- **2025-11-19** — [How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry](<../product-engineering/security/How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry.md>) · `security` · arize
  Explains how red-team agents can be used to find and test security weaknesses in agentic applications.
- **2025-11-18** — [Evaluating and Improving AI Agents at Scale with Microsoft Foundry](<../evals-observability/evaluation/Evaluating and Improving AI Agents at Scale with Microsoft Foundry.md>) · `evaluation` · arize
  Guide to evaluating and improving production AI agents at scale with Microsoft Foundry and Arize workflows.
- **2025-11-17** — [GEPA vs Prompt Learning: Benchmarking Different Prompt Optimization Approaches](<../prompt-engineering/techniques/GEPA vs Prompt Learning Benchmarking Different Prompt Optimization Approaches.md>) · `techniques` · arize
  Benchmarks GEPA against prompt learning and frames prompt optimization as an eval-driven engineering loop.
- **2025-11-14** — [Tracing, Evaluation, and Observability for Google ADK (How To)](<../evals-observability/tracing/Tracing, Evaluation, and Observability for Google ADK (How To).md>) · `tracing` · arize
  How-to guide for tracing, evaluating, and observing Google ADK agents in production-style workflows.
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<../evals-observability/monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<../prompt-engineering/techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-10-14** — [Optimizing Coding Agent Rules (./clinerules) for Improved Accuracy](<../agents/computer-use/Optimizing Coding Agent Rules (.clinerules) for Improved Accuracy.md>) · `computer-use` · arize
  Explains how coding-agent rule files affect accuracy and how to optimize them for better agent behavior.
- **2025-10-08** — [Should I Use the Same LLM for My Eval as My Agent? Testing Self-Evaluation Bias](<../evals-observability/llm-as-judge/Should I Use the Same LLM for My Eval as My Agent Testing Self-Evaluation Bias.md>) · `llm-as-judge` · arize
  Tests self-evaluation bias when using the same model for agent behavior and evaluation, with guidance for eval design.
- **2025-09-24** — [Testing Binary vs Score Evals on the Latest Models](<../evals-observability/testing/Testing Binary vs Score Evals on the Latest Models.md>) · `testing` · arize
  Compares binary and score-based LLM evals across models to clarify tradeoffs in evaluator design.
- **2025-09-17** — [adb Benchmarks](<../infra-platform/deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-09-09** — [Orchestrator-Worker Agents: A Practical Comparison of Common Agent Frameworks](<../agents/multi-agent/Orchestrator-Worker Agents A Practical Comparison of Common Agent Frameworks.md>) · `multi-agent` · arize
  Compares orchestrator-worker agent frameworks and clarifies when this multi-agent pattern is useful.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<../evals-observability/evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-05** — [NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI](<../models/reasoning/NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI.md>) · `reasoning` · arize
  Summarizes the argument for small language models in agentic AI and where they can replace larger models.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<../evals-observability/evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-08-28** — [Claude Code vs Cursor: A Power-User’s Playbook](<../agents/tool-use/Claude Code vs Cursor A Power-User’s Playbook.md>) · `tool-use` · arize
  Compares Claude Code and Cursor from a power-user workflow perspective, focusing on coding-agent interfaces and usage patterns.
- **2025-08-21** — [Annotation for Strong AI Evaluation Pipelines](<../evals-observability/evaluation/Annotation for Strong AI Evaluation Pipelines.md>) · `evaluation` · arize
  Explains how human annotations support strong AI evaluation pipelines and how annotation data can be combined with evals in Phoenix workflows.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<../prompt-engineering/techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<../infra-platform/deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-07-30** — [A Watermark for Large Language Models](<../product-engineering/security/A Watermark for Large Language Models.md>) · `security` · arize
  Summary of a paper-reading session on watermarking generated text from large language models, including detection goals and implications for responsible deployment.
- **2025-07-18** — [Prompt Learning: Using English Feedback to Optimize LLM Systems](<../prompt-engineering/techniques/Prompt Learning Using English Feedback to Optimize LLM Systems.md>) · `techniques` · arize
  Explains prompt learning driven by natural-language feedback as an optimization loop for LLM systems.
- **2025-07-18** — [LLM Observability for AI Agents and Applications](<../evals-observability/monitoring/LLM Observability for AI Agents and Applications.md>) · `monitoring` · arize
  Introduces observability practices for LLM applications and agents, including monitoring signals beyond traditional metrics.
- **2025-06-20** — [The Illusion of Thinking: What the Apple AI Paper Says About LLM Reasoning](<../models/reasoning/The Illusion of Thinking What the Apple AI Paper Says About LLM Reasoning.md>) · `reasoning` · arize
  Analyzes the Apple reasoning paper and what it suggests about evaluating LLM reasoning limits.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<../inference/quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2025-05-16** — [Scalable Chain of Thoughts via Elastic Reasoning](<../models/reasoning/Scalable Chain of Thoughts via Elastic Reasoning.md>) · `reasoning` · arize
  Summarizes elastic reasoning and scalable chain-of-thought ideas for allocating reasoning compute more flexibly.
- **2025-04-11** — [40 Large Language Model Benchmarks and The Future of Model Evaluation](<../models/benchmarks/40 Large Language Model Benchmarks and The Future of Model Evaluation.md>) · `benchmarks` · arize
  Surveys major LLM benchmarks and explains what different benchmark families measure for model evaluation.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<../evals-observability/tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-04-09** — [Embracing Google's Agent-To-Agent (A2A) Protocol](<../agents/multi-agent/Embracing Google's Agent-To-Agent (A2A) Protocol.md>) · `multi-agent` · arize
  Discusses Google's Agent-to-Agent protocol and why interoperability standards matter for multi-agent systems and production agent ecosystems.
- **2025-04-08** — [Tracing and Evaluating Gemini Audio with Arize](<../models/multimodal/Tracing and Evaluating Gemini Audio with Arize.md>) · `multimodal` · arize
  Covers tracing and evaluation for Gemini audio applications, focusing on observability for multimodal systems.
- **2025-04-04** — [AI Benchmark Deep Dive: Gemini 2.5 and Humanity's Last Exam](<../models/benchmarks/AI Benchmark Deep Dive Gemini 2.5 and Humanity's Last Exam.md>) · `benchmarks` · arize
  Paper-reading recap on Gemini 2.5 and Humanity's Last Exam, focusing on benchmark interpretation and what modern evaluation results do and do not show.
- **2025-03-17** — [Prompt Optimization Techniques](<../prompt-engineering/techniques/Prompt Optimization Techniques.md>) · `techniques` · arize
  Covers few-shot prompting and prompt optimization techniques with an emphasis on measurable improvement.
- **2025-03-07** — [Prompt Management from First Principles](<../prompt-engineering/techniques/Prompt Management from First Principles.md>) · `techniques` · arize
  Frames prompt management from first principles, including versioning, ownership, and production workflow concerns.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<../evals-observability/evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2025-02-26** — [Memory and State in LLM Applications](<../agents/memory-context/Memory and State in LLM Applications.md>) · `memory-context` · arize
  Explains memory and state patterns in LLM applications and how they affect reliability across interactions.
- **2025-02-18** — [How to Build An AI Agent](<../agents/planning/How to Build An AI Agent.md>) · `planning` · arize
  Practical guide to building an AI agent, covering planning, tools, state, and reliability considerations.
- **2025-02-12** — [How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting](<../product-engineering/case-studies/How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting.md>) · `case-studies` · arize
  Case study on using Phoenix traces and observability to improve AI-driven troubleshooting workflows in production.
- **2025-02-05** — [Understanding Agentic RAG](<../rag-retrieval/pipelines/Understanding Agentic RAG.md>) · `pipelines` · arize
  Explains agentic RAG and how agents change retrieval planning, tool use, and synthesis workflows.
- **2025-01-31** — [Best Practices for Building an Agent Router](<../agents/planning/Best Practices for Building an Agent Router.md>) · `planning` · arize
  Explains agent-router design as a decision layer that routes user requests to the right tools, services, or actions in larger agent systems.
- **2025-01-22** — [Building Audio Support with OpenAI: Insights from our Journey](<../models/multimodal/Building Audio Support with OpenAI Insights from our Journey.md>) · `multimodal` · arize
  Case study on adding audio support with OpenAI models, covering product and engineering lessons from building multimodal support.
- **2024-12-10** — [Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies](<../agents/multi-agent/Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies.md>) · `multi-agent` · arize
  Summarizes collaborative LLM strategies such as merging, ensembling, and cooperation for multi-model or multi-agent systems.
- **2024-12-04** — [AI Agent Workflows and Architectures Masterclass](<../agents/harness/AI Agent Workflows and Architectures Masterclass.md>) · `harness` · arize
  Introduces practical agent workflow and architecture patterns, emphasizing simple tool-calling loops and design choices over vague autonomy claims.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<../agents/planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<../evals-observability/llm-as-judge/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `llm-as-judge` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-11-19** — [Instrumenting Your LLM Application: Arize Phoenix and Vercel AI SDK](<../evals-observability/tracing/Instrumenting Your LLM Application Arize Phoenix and Vercel AI SDK.md>) · `tracing` · arize
  Shows how to instrument an LLM application with Phoenix and Vercel AI SDK so traces are available for debugging and evaluation.
- **2024-11-11** — [How to Improve LLM Safety and Reliability](<../evals-observability/testing/How to Improve LLM Safety and Reliability.md>) · `testing` · arize
  Covers testing and monitoring practices for improving LLM application safety and reliability in production.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<../evals-observability/evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-10-23** — [Techniques for Self-Improving LLM Evals](<../evals-observability/llm-as-judge/Techniques for Self-Improving LLM Evals.md>) · `llm-as-judge` · arize
  Covers techniques for making LLM evals self-improving through feedback, iteration, and evaluator refinement.
- **2024-10-16** — [Comparing OpenAI Swarm with other Multi Agent Frameworks](<../agents/multi-agent/Comparing OpenAI Swarm with other Multi Agent Frameworks.md>) · `multi-agent` · arize
  Compares OpenAI Swarm with other multi-agent frameworks, highlighting orchestration patterns and framework tradeoffs.
- **2024-10-16** — [Tracing and Evaluating LangGraph Agents](<../evals-observability/tracing/Tracing and Evaluating LangGraph Agents.md>) · `tracing` · arize
  Covers tracing and evaluation patterns for LangGraph agents, linking graph-based control flow with observability.
- **2024-10-15** — [Google's NotebookLM and the Future of AI-Generated Audio](<../models/multimodal/Google's NotebookLM and the Future of AI-Generated Audio.md>) · `multimodal` · arize
  Paper-reading style overview of Google NotebookLM and AI-generated audio as a multimodal product pattern.
- **2024-10-08** — [The Role of OpenTelemetry (OTEL) in LLM Observability](<../evals-observability/tracing/The Role of OpenTelemetry (OTEL) in LLM Observability.md>) · `tracing` · arize
  Explains OpenTelemetry’s role in LLM observability and why standard traces matter for production systems.
- **2024-10-03** — [Building AI Assistants with Vectara-agentic and Arize](<../rag-retrieval/pipelines/Building AI Assistants with Vectara-agentic and Arize.md>) · `pipelines` · arize
  Shows how to build AI assistants with Vectara-agentic and Arize, tying retrieval, agent tools, and observability together.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<../agents/memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.
- **2024-09-30** — [Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations](<../evals-observability/llm-as-judge/Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations.md>) · `llm-as-judge` · arize
  Best practices for choosing an LLM-as-judge evaluation model, including tradeoffs in evaluator quality and fit for task.
- **2024-09-27** — [Exploring OpenAI's o1-preview and o1-mini](<../models/reasoning/Exploring OpenAI's o1-preview and o1-mini.md>) · `reasoning` · arize
  Analyzes OpenAI o1-preview and o1-mini from a reasoning-model perspective, including expected strengths, limits, and evaluation implications for production teams.
- **2024-09-19** — [Breaking Down Reflection Tuning: Enhancing LLM Performance with Self-Learning](<../models/fine-tuning/Breaking Down Reflection Tuning Enhancing LLM Performance with Self-Learning.md>) · `fine-tuning` · arize
  Explains reflection tuning as a self-learning approach for improving LLM performance through critique and iterative refinement.
- **2024-09-11** — [Composable Interventions for Language Models](<../models/reasoning/Composable Interventions for Language Models.md>) · `reasoning` · arize
  Deep dive on composable interventions for language models, covering techniques for steering or modifying model behavior.
- **2024-09-05** — [Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation](<../evals-observability/evaluation/Creating and Validating Synthetic Datasets for LLM Evaluation & Experimentation.md>) · `evaluation` · arize
  Explains how to create and validate synthetic datasets for LLM evaluation and experimentation workflows.
- **2024-08-30** — [Evaluating an Image Classifier](<../evals-observability/evaluation/Evaluating an Image Classifier.md>) · `evaluation` · arize
  Tutorial on evaluating an image classifier with Phoenix, using multimodal experiment and tracing workflows.
- **2024-08-16** — [Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges](<../evals-observability/llm-as-judge/Judging the Judges Evaluating Alignment and Vulnerabilities in LLMs-as-Judges.md>) · `llm-as-judge` · arize
  Analyzes vulnerabilities and alignment issues in LLM-as-judge systems, with implications for production evaluator design.
- **2024-08-08** — [LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents](<../agents/harness/LlamaIndex Workflows Navigating a New Way To Build Cyclical Agents.md>) · `harness` · arize
  Explains LlamaIndex Workflows as a pattern for building cyclical agents with explicit control flow.
- **2024-08-06** — [Breaking Down Meta's Llama 3 Herd of Models](<../models/releases/Breaking Down Meta's Llama 3 Herd of Models.md>) · `releases` · arize
  Technical overview of Meta's Llama 3 model family, including architecture, capabilities, and benchmark interpretation.
- **2024-07-30** — [Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant](<../product-engineering/case-studies/Developing Copilot What AI Engineers Can Learn from Our Experience Building An AI Assistant.md>) · `case-studies` · arize
  Arize Copilot case study covering lessons from building an AI assistant for data scientists and AI engineers.
- **2024-07-25** — [Different Ways to Instrument Your LLM Application](<../evals-observability/tracing/Different Ways to Instrument Your LLM Application.md>) · `tracing` · arize
  Survey of instrumentation approaches for LLM applications, focused on tracing and observability setup choices.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<../prompt-engineering/techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.
- **2024-06-28** — [RAFT: Adapting Language Model to Domain Specific RAG](<../rag-retrieval/pipelines/RAFT Adapting Language Model to Domain Specific RAG.md>) · `pipelines` · arize
  Summarizes RAFT as a method for adapting language models to domain-specific RAG workflows.
- **2024-06-20** — [Managing and Monitoring Your Open Source LLM Applications](<../evals-observability/monitoring/Managing and Monitoring Your Open Source LLM Applications.md>) · `monitoring` · arize
  Covers practical monitoring needs for open-source LLM applications, including operational metrics and deployment feedback.
- **2024-06-14** — [LLM Interpretability and Sparse Autoencoders: Research from OpenAI and Anthropic](<../models/reasoning/LLM Interpretability and Sparse Autoencoders Research from OpenAI and Anthropic.md>) · `reasoning` · arize
  Explains sparse autoencoders and interpretability research from OpenAI and Anthropic as tools for understanding model internals.
- **2024-05-30** — [LLM Summarization: Getting To Production](<../product-engineering/architecture/LLM Summarization Getting To Production.md>) · `architecture` · arize
  Covers production considerations for LLM summarization systems, including quality controls and deployment pitfalls.
- **2024-05-29** — [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](<../evals-observability/benchmark-design/Trustworthy LLMs A Survey and Guideline for Evaluating Large Language Models' Alignment.md>) · `benchmark-design` · arize
  Survey-style guide to evaluating trustworthy and aligned LLM behavior across reliability, safety, and quality dimensions.
- **2024-05-13** — [Breaking Down EvalGen: Who Validates the Validators?](<../evals-observability/llm-as-judge/Breaking Down EvalGen Who Validates the Validators.md>) · `llm-as-judge` · arize
  Deep dive on EvalGen and the problem of validating LLM-generated evaluators, including human review limitations and evaluator reliability.
- **2024-04-26** — [Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models](<../agents/tool-use/Keys To Understanding ReAct Synergizing Reasoning and Acting in Language Models.md>) · `tool-use` · arize
  Explains ReAct as a reasoning-plus-acting pattern for agents and how it structures tool use.
- **2024-04-04** — [Demystifying Amazon's Chronos: Learning the Language of Time Series](<../models/releases/Demystifying Amazon's Chronos Learning the Language of Time Series.md>) · `releases` · arize
  Deep dive into Amazon Chronos for time-series modeling, including model behavior and evaluation context.
- **2024-03-26** — [Anthropic Claude 3](<../models/releases/Anthropic Claude 3.md>) · `releases` · arize
  Overview of Anthropic Claude 3 model releases and capabilities, including model comparisons and implications for LLM application builders.
- **2024-03-15** — [Reinforcement Learning in the Era of LLMs](<../models/reinforcement-learning/Reinforcement Learning in the Era of LLMs.md>) · `reinforcement-learning` · arize
  Explains reinforcement learning concepts in the LLM era and how RL fits into model improvement workflows.
- **2024-03-06** — [Evaluate RAG with LLM Evals and Benchmarks](<../rag-retrieval/pipelines/Evaluate RAG with LLM Evals and Benchmarks.md>) · `pipelines` · arize
  Workshop recap on evaluating RAG systems with LLM evals and benchmarks.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<../product-engineering/case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-20** — [Evaluating and Analyzing Your RAG Pipeline with Ragas](<../evals-observability/evaluation/Evaluating and Analyzing Your RAG Pipeline with Ragas.md>) · `evaluation` · arize
  Explains how to evaluate RAG pipelines with Ragas and Phoenix, including retrieval and generation quality dimensions.
- **2024-02-18** — [The Shift from Models to Compound AI Systems](<../product-engineering/architecture/The Shift from Models to Compound AI Systems.md>) · `architecture` · arize
  Explains the shift from standalone models to compound AI systems that combine models, retrieval, tools, orchestration, and evaluation into production applications.
- **2024-02-16** — [Evaluating the Generation Stage in RAG](<../rag-retrieval/pipelines/Evaluating the Generation Stage in RAG.md>) · `pipelines` · arize
  Focuses on evaluating the generation stage in RAG pipelines, complementing retrieval-focused evaluation.
- **2024-02-08** — [RAG vs Fine-Tuning](<../rag-retrieval/pipelines/RAG vs Fine-Tuning.md>) · `pipelines` · arize
  Compares RAG and fine-tuning as adaptation strategies, including when retrieval is preferable to model updates.
- **2024-01-31** — [Phi-2 Model](<../models/releases/Phi-2 Model.md>) · `releases` · arize
  Technical overview of Phi-2, including model characteristics, benchmark behavior, and small-model implications.
- **2023-12-27** — [Mistral AI (Mixtral-8x7B): Performance, Benchmarks](<../models/releases/Mistral AI (Mixtral-8x7B) Performance, Benchmarks.md>) · `releases` · arize
  Technical overview of Mistral and Mixtral model behavior, performance, and benchmark positioning.
- **2023-12-18** — [How to Prompt LLMs for Text-to-SQL](<../prompt-engineering/structured-output/How to Prompt LLMs for Text-to-SQL.md>) · `structured-output` · arize
  Practical guide to Text-to-SQL prompting, including schema context, output constraints, and evaluation considerations.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<../evals-observability/benchmark-design/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `benchmark-design` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-11-14** — [The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets](<../models/reasoning/The Geometry of Truth Emergent Linear Structure in LLM Representation of TrueFalse Datasets.md>) · `reasoning` · arize
  Summarizes research on linear structure in LLM representations of truth and falsehood, relevant to interpretability.
- **2023-11-08** — [Ingesting Data for Semantic Searches in a Production-Ready Way](<../rag-retrieval/pipelines/Ingesting Data for Semantic Searches in a Production-Ready Way.md>) · `pipelines` · arize
  Explains production ingestion concerns for semantic search, including data preparation and retrieval pipeline reliability.
- **2023-11-02** — [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](<../models/reasoning/Towards Monosemanticity Decomposing Language Models With Dictionary Learning.md>) · `reasoning` · arize
  Summarizes monosemanticity and dictionary learning work for decomposing language model internals.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<../evals-observability/monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
- **2023-10-17** — [RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models](<../rag-retrieval/search/RankVicuna Zero-Shot Listwise Document Reranking with Open-Source Large Language Models.md>) · `search` · arize
  Summarizes RankVicuna for zero-shot listwise reranking and its implications for LLM-powered search.
- **2023-10-06** — [Explaining Grokking Through Circuit Efficiency](<../models/reasoning/Explaining Grokking Through Circuit Efficiency.md>) · `reasoning` · arize
  Paper-reading deep dive on grokking and circuit efficiency as a way to understand model generalization.
- **2023-10-02** — [LLM Tracing and Observability](<../evals-observability/tracing/LLM Tracing and Observability.md>) · `tracing` · arize
  Explains LLM tracing and observability concepts using Phoenix as the concrete implementation context.
- **2023-08-24** — [Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading](<../models/reasoning/Skeleton of Thought LLMs Can Do Parallel Decoding Paper Reading.md>) · `reasoning` · arize
  Summarizes Skeleton of Thought and how parallel decoding can speed structured reasoning.
- **2023-08-07** — [Extending the Context Window of LLaMA Models Paper Reading](<../models/reasoning/Extending the Context Window of LLaMA Models Paper Reading.md>) · `reasoning` · arize
  Explains techniques for extending LLaMA context windows and the tradeoffs involved in long-context model behavior.
- **2023-08-04** — [Llama 2: Open Foundation and Fine-Tuned Chat Models Paper Reading](<../models/releases/Llama 2 Open Foundation and Fine-Tuned Chat Models Paper Reading.md>) · `releases` · arize
  Technical paper-reading summary of Llama 2, including foundation and chat-tuned model behavior.
- **2023-07-25** — [Lost in the Middle: How Language Models Use Long Contexts Paper Reading](<../models/reasoning/Lost in the Middle How Language Models Use Long Contexts Paper Reading.md>) · `reasoning` · arize
  Summarizes the Lost in the Middle findings on long-context model behavior and retrieval sensitivity.
- **2023-07-14** — [Orca: Progressive Learning from Complex Explanation Traces of GPT-4 Paper Reading](<../models/fine-tuning/Orca Progressive Learning from Complex Explanation Traces of GPT-4 Paper Reading.md>) · `fine-tuning` · arize
  Summarizes Orca and progressive learning from GPT-4 explanation traces as a post-training strategy.
- **2023-07-03** — [One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning](<../models/fine-tuning/One-for-All Generalized LoRA for Parameter-Efficient Fine-tuning.md>) · `fine-tuning` · arize
  Summarizes Generalized LoRA as a parameter-efficient fine-tuning method and explains where it fits in adaptation workflows.
- **2023-06-27** — [HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels](<../rag-retrieval/search/HyDE Precise Zero-Shot Dense Retrieval without Relevance Labels.md>) · `search` · arize
  Summarizes HyDE for zero-shot dense retrieval and how hypothetical document generation can improve semantic search.
- **2023-06-20** — [Voyager: An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion](<../agents/planning/Voyager An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion.md>) · `planning` · arize
  Paper-reading summary of Voyager as an open-ended embodied agent using LLM-driven skills and exploration.
- **2023-06-12** — [LoRA: Low-Rank Adaptation of Large Language Models Paper Reading and Discussion](<../models/fine-tuning/LoRA Low-Rank Adaptation of Large Language Models Paper Reading and Discussion.md>) · `fine-tuning` · arize
  Paper-reading guide to LoRA and why low-rank adaptation is useful for efficient LLM fine-tuning.
- **2023-06-09** — [Retrieval-Augmented Generation - Paper Reading and Discussion](<../rag-retrieval/pipelines/Retrieval-Augmented Generation - Paper Reading and Discussion.md>) · `pipelines` · arize
  Paper-reading summary of retrieval-augmented generation and the architecture behind combining retrieval with generation.
- **2023-06-02** — [LIMA: Less Is More for Alignment - Paper Reading and Discussion](<../models/fine-tuning/LIMA Less Is More for Alignment - Paper Reading and Discussion.md>) · `fine-tuning` · arize
  Summarizes LIMA and the idea that small high-quality instruction data can have outsized impact on alignment tuning.
- **2023-06-01** — [Drag Your GAN: Interactive Point-Based Manipulation on the Generative Image Manifold](<../models/multimodal/Drag Your GAN Interactive Point-Based Manipulation on the Generative Image Manifold.md>) · `multimodal` · arize
  Paper-reading deep dive on DragGAN and interactive point-based image manipulation in generative model latent spaces.
- **2023-05-25** — [Cross Validation: What You Need To Know, From the Basics To LLMs](<../evals-observability/evaluation/Cross Validation What You Need To Know, From the Basics To LLMs.md>) · `evaluation` · arize
  Overview of cross-validation from classic ML through LLM applications, focused on evaluation methodology.
- **2023-05-17** — [Evaluating Model Fairness](<../evals-observability/evaluation/Evaluating Model Fairness.md>) · `evaluation` · arize
  Explains model fairness evaluation and how to assess bias and fairness risks in production systems.
- **2023-05-05** — [OpenAI on Reinforcement Learning With Human Feedback (RLHF)](<../models/reinforcement-learning/OpenAI on Reinforcement Learning With Human Feedback (RLHF).md>) · `reinforcement-learning` · arize
  Summarizes RLHF concepts from OpenAI and how human feedback changes model behavior during post-training.
- **2023-04-28** — [Lessons From Building an Early ChatGPT Plugin In Under 24 Hours](<../product-engineering/case-studies/Lessons From Building an Early ChatGPT Plugin In Under 24 Hours.md>) · `case-studies` · arize
  Retrospective on building an early ChatGPT plugin quickly, including product workflow lessons and integration constraints from the plugin ecosystem.
- **2023-03-29** — [Hungry Hungry Hippos (H3) and Language Modeling with State Space Models](<../models/reasoning/Hungry Hungry Hippos (H3) and Language Modeling with State Space Models.md>) · `reasoning` · arize
  Explains H3/state-space model ideas as alternatives to standard attention and why they matter for sequence modeling efficiency.
- **2023-03-21** — [Toolformer: Training LLMs To Use Tools](<../agents/tool-use/Toolformer Training LLMs To Use Tools.md>) · `tool-use` · arize
  Summarizes Toolformer and how language models can learn to use external tools.
