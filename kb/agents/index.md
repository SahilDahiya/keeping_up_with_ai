# agents

147 articles.

- **2026-07-10** — [OpenWiki Brains: Proactive Memory for AI Agents](<memory-context/OpenWiki Brains Proactive Memory for AI Agents.md>) · `memory-context` · langchain
  Introduces OpenWiki Brains as proactive wiki memory for agents, focused on persistent context and retrieval over project knowledge.
- **2026-07-10** — [3 production patterns for AI agents and how to evaluate each one](<planning/3 production patterns for AI agents and how to evaluate each one.md>) · `planning` · arize
  Breaks production agents into local coding agents, in-app assistants, and operational agents, then maps each pattern to different harness, rollout, and evaluation needs.
- **2026-07-10** — [What is a loop in AI engineering, anyway?](<planning/What is a loop in AI engineering, anyway.md>) · `planning` · arize
  Defines feedback loops in AI engineering and why loops are central to agent and eval system design.
- **2026-07-10** — **[Paper]** [Failure as a Process: An Anatomy of CLI Coding Agent Trajectories](<planning/[Paper] Failure as a Process An Anatomy of CLI Coding Agent Trajectories.md>) · `planning` · arxiv
  Empirical study of how CLI coding agents fail as a *process* rather than an outcome: 3,843 trajectories from 7 frontier models across 3 scaffolds (OpenHands, MiniSWE, Terminus2) on Terminal-Bench, with 1,794 valid ones hand-annotated over 63,000 execution steps. Finds failures are driven mainly by epistemic errors, begin within the first few steps, and stay hidden until recovery is impossible — arguing for early validation and intervention instead of final-outcome evaluation.
- **2026-07-08** — [Tuning the harness, not the model: a Nemotron 3 Ultra playbook](<planning/Tuning the harness, not the model a Nemotron 3 Ultra playbook.md>) · `planning` · langchain
  Nemotron 3 Ultra playbook arguing for harness tuning over model tuning, with practical agent-system design and eval implications.
- **2026-07-08** — [Deep Agents Code on NVIDIA NemoClaw](<tool-use/Deep Agents Code on NVIDIA NemoClaw.md>) · `tool-use` · langchain
  Covers a governed Deep Agents code blueprint on NVIDIA NemoClaw for sensitive code workflows, emphasizing controls around agentic coding.
- **2026-07-07** — **[Paper]** [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](<planning/[Paper] Beyond the Leaderboard A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents.md>) · `planning` · arxiv
  Synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026) across 19 benchmarks into a unified taxonomy of LLM-agent failure, with six clusters: tool-invocation/parameter errors, planning and constraint-satisfaction failures, long-horizon degradation from context accumulation, multi-agent coordination breakdown, safety failures under adversarial or underspecified conditions, and measurement-validity problems. Finds failures compound nonlinearly with task length, strong sub-task scores do not predict end-to-end success, and extra scaffolding does not reliably improve reliability.
- **2026-07-06** — [Own the loop: A field guide to agent harnesses](<planning/Own the loop A field guide to agent harnesses.md>) · `planning` · arize
  Field guide to owning the agent harness loop, from task control to measurement and iteration.
- **2026-07-06** — [Evaluating the USA vs Belgium World Cup matchup](<tool-use/Evaluating the USA vs Belgium World Cup matchup.md>) · `tool-use` · braintrust
  Uses a USA vs Belgium matchup example to evaluate web research agents, illustrating task design and judging for tool-using research workflows.
- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-04** — [Better Models: Worse Tools](<tool-use/Better Models Worse Tools.md>) · `tool-use` · simon-willison
  Short analysis of newer coding models producing malformed arguments for third-party edit tools, raising the issue that tool schemas and edit mechanisms may need model-specific evaluation and adaptation.
- **2026-07-03** — [Fable's judgement](<multi-agent/Fable's judgement.md>) · `multi-agent` · simon-willison
  Practical coding-agent pattern for delegating implementation work to cheaper subagents while reserving the main model for judgment, review, synthesis, and model-selection decisions.
- **2026-07-02** — [From World Cup matchups to research maps: evaluating Parallel's web research agents](<tool-use/From World Cup matchups to research maps evaluating Parallel's web research agents.md>) · `tool-use` · braintrust
  Evaluates Parallel web research agents using World Cup matchups and research-map tasks, connecting tool use, knowledge graphs, and answer quality.
- **2026-07-02** — [Release: llm-coding-agent 0.1a0](<tool-use/Release llm-coding-agent 0.1a0.md>) · `tool-use` · simon-willison
  Release and implementation notes for a Claude Code-style coding agent built on Simon Willison's LLM framework, including file-editing, command execution, search, read, and write tools plus approval modes.
- **2026-07-01** — [How to Use RLMs in Deep Agents](<memory-context/How to Use RLMs in Deep Agents.md>) · `memory-context` · langchain
  Explains how to use retrieval language models in Deep Agents to improve context selection and long-running agent performance.
- **2026-07-01** — [OpenWiki: Open Source Repo Documentation for Coding Agents](<tool-use/OpenWiki Open Source Repo Documentation for Coding Agents.md>) · `tool-use` · langchain
  Introduces OpenWiki as an agent for repository documentation, combining code understanding, retrieval, and generated docs.
- **2026-06-30** — [Wiki Memory](<memory-context/Wiki Memory.md>) · `memory-context` · langchain
  Explains wiki memory as a persistent knowledge layer for agents, supporting retrieval, documentation, and long-term project context.
- **2026-06-29** — [Introducing Dynamic Subagents in Deep Agents](<multi-agent/Introducing Dynamic Subagents in Deep Agents.md>) · `multi-agent` · langchain
  Introduces dynamic subagents in Deep Agents, covering delegation, specialized worker agents, and runtime coordination.
- **2026-06-26** — [Building an auditable VC research agent with the Perplexity Agent API and LangGraph](<tool-use/Building an auditable VC research agent with the Perplexity Agent API and LangGraph.md>) · `tool-use` · langchain
  Walkthrough for building an auditable VC research agent with Perplexity, LangGraph, and LangSmith, emphasizing traceability and review.
- **2026-06-24** — [How to Build Memory into AI Agents](<memory-context/How to Build Memory into AI Agents.md>) · `memory-context` · langchain
  Explains how to build memory into AI agents through state, retrieval, persistence, and context injection patterns.
- **2026-06-24** — [Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.](<multi-agent/Frontier AI at a fraction of the cost open-source worker agents with a closed-source advisor.md>) · `multi-agent` · fireworks
  Explains a worker-advisor pattern that combines open-source worker agents with closed-source advisors for cost-quality tradeoffs.
- **2026-06-24** — [Using Braintrust to eval agentic setups from large-scale Hugging Face data](<planning/Using Braintrust to eval agentic setups from large-scale Hugging Face data.md>) · `planning` · braintrust
  Uses large-scale Hugging Face agent traces to evaluate agentic setups, connecting trace analysis to agent behavior and reliability measurement.
- **2026-06-18** — [What is an agent harness? Why harnesses are replacing agent frameworks](<planning/What is an agent harness Why harnesses are replacing agent frameworks.md>) · `planning` · arize
  Explains why agent harnesses are replacing simple framework use as the unit of production agent engineering.
- **2026-06-16** — [The Art of Loop Engineering](<planning/The Art of Loop Engineering.md>) · `planning` · langchain
  Discusses loop engineering for agents, focusing on the control loops that govern planning, action, observation, and refinement.
- **2026-06-16** — [What is agent orchestration? Frameworks, runtimes, and observability explained](<planning/What is agent orchestration Frameworks, runtimes, and observability explained.md>) · `planning` · arize
  Explains agent orchestration across frameworks, runtimes, and observability concerns.
- **2026-06-12** — [How to Choose the Right Sandbox for AI Agents](<computer-use/How to Choose the Right Sandbox for AI Agents.md>) · `computer-use` · langchain
  Guide to choosing an agent sandbox based on isolation, tool access, persistence, security, and operational constraints.
- **2026-06-12** — [Memory is still a missing primitive: Cataloguing what the field is actually shipping](<memory-context/Memory is still a missing primitive Cataloguing what the field is actually shipping.md>) · `memory-context` · arize
  Catalogs memory approaches currently shipping in AI systems and frames memory as a missing primitive for agents.
- **2026-06-12** — [Agent Assist: What It Is, How It Works & How to Choose](<tool-use/Agent Assist What It Is, How It Works & How to Choose.md>) · `tool-use` · cresta
  Explains real-time agent assist as a tool-augmented workflow that surfaces guidance during live interactions.
- **2026-06-11** — [Cresta Conductor: The Agent for AI Agent Development](<planning/Cresta Conductor The Agent for AI Agent Development.md>) · `planning` · cresta
  Introduces an agent used to help develop other AI agents, with lessons around orchestration, testing, and iteration workflows.
- **2026-06-11** — [PostgresFS vs. SQL skills: should AI agents fake a filesystem?](<tool-use/PostgresFS vs. SQL skills should AI agents fake a filesystem.md>) · `tool-use` · arize
  Compares filesystem-like and SQL-backed skill interfaces for AI agents, focusing on state access and tool ergonomics.
- **2026-06-05** — [Give your agent its own computer](<computer-use/Give your agent its own computer.md>) · `computer-use` · langchain
  Argues for giving agents isolated computers or sandboxes so they can run tools while preserving control, safety, and reproducibility.
- **2026-06-04** — [Fault Tolerance in LangGraph: Retries, Timeouts and Error Handlers](<planning/Fault Tolerance in LangGraph Retries, Timeouts and Error Handlers.md>) · `planning` · langchain
  Explains fault tolerance in LangGraph with retries, timeouts, and error handlers for more reliable long-running agents.
- **2026-06-03** — [How Harvey & Fireworks Beat Closed Source on Cost + Quality](<multi-agent/How Harvey & Fireworks Beat Closed Source on Cost + Quality.md>) · `multi-agent` · fireworks
  Case study of using open-source agents with frontier advisors to improve cost and quality versus closed-source baselines.
- **2026-06-03** — [How to Build a Custom Agent Harness](<planning/How to Build a Custom Agent Harness.md>) · `planning` · langchain
  Guide to building a custom agent harness, covering control loop design, state, tools, observability, and evaluation hooks.
- **2026-06-01** — [How Hermes implements an open source agent harness architecture](<planning/How Hermes implements an open source agent harness architecture.md>) · `planning` · arize
  Breaks down Hermes as an open-source agent harness architecture, focusing on components, control flow, and implementation boundaries.
- **2026-05-29** — [How to build a better agent harness with traces and evals](<planning/How to build a better agent harness with traces and evals.md>) · `planning` · arize
  Shows how traces and evals combine inside an agent harness to make agent behavior easier to test and improve.
- **2026-05-29** — [Interpreter Skills: Building Workflows for Agents](<tool-use/Interpreter Skills Building Workflows for Agents.md>) · `tool-use` · langchain
  Introduces interpreter skills as reusable workflows for agents that need to execute code, inspect outputs, and compose tools.
- **2026-05-28** — [Claude Code: Best practices for agentic coding](<tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-05-21** — [The six generations of AI agents and how to eval them](<planning/The six generations of AI agents and how to eval them.md>) · `planning` · braintrust
  Taxonomy of six generations of AI agents and guidance for evaluating each generation's capabilities, failure modes, and production readiness.
- **2026-05-20** — [EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API](<tool-use/EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.md>) · `tool-use` · langchain
  Case study building a financial research agent for EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.
- **2026-05-19** — [Building a self-improving agent on a context graph of human disagreement](<memory-context/Building a self-improving agent on a context graph of human disagreement.md>) · `memory-context` · arize
  Shows how a context graph of human disagreement can support a self-improving agent loop.
- **2026-05-19** — [How We Built LangSmith Engine, Our Agent for Improving Agents](<planning/How We Built LangSmith Engine, Our Agent for Improving Agents.md>) · `planning` · langchain
  Explains LangSmith Engine, an agent for improving agents through trace analysis, feedback, evals, and iterative changes.
- **2026-05-18** — [Introducing Claude Managed Agents with Modal Sandboxes](<computer-use/Introducing Claude Managed Agents with Modal Sandboxes.md>) · `computer-use` · modal
  Shows how Claude managed agents can use Modal sandboxes for isolated execution, filesystem state, and scalable agent workloads.
- **2026-05-13** — [LangSmith Sandboxes are Generally Available](<computer-use/LangSmith Sandboxes are Generally Available.md>) · `computer-use` · langchain
  Covers LangSmith Sandboxes for safely running agent code and tools in isolated execution environments.
- **2026-05-12** — [Sierra Agent OS 2.0: from answers to memory and action](<memory-context/Sierra Agent OS 2.0 from answers to memory and action.md>) · `memory-context` · sierra
  Describes Agent OS 2.0 moving agents from answers to memory and action, covering persistent context, tool use, and stateful behavior.
- **2026-05-12** — [Delta Channels: How We’re Evolving our Runtime for Long-Running Agents](<planning/Delta Channels How We’re Evolving our Runtime for Long-Running Agents.md>) · `planning` · langchain
  Describes Delta Channels as an evolution of the LangGraph runtime for long-running agents, focused on durable state and runtime communication.
- **2026-05-12** — [Explorer: The agent-optimizing agent](<planning/Explorer The agent-optimizing agent.md>) · `planning` · sierra
  Introduces Explorer as an agent-optimizing agent that analyzes conversations and identifies improvement opportunities for deployed agents.
- **2026-05-12** — [Shipping and scaling AI agents](<planning/Shipping and scaling AI agents.md>) · `planning` · sierra
  Practical guide to shipping and scaling AI agents, including lifecycle, reliability, deployment, and continuous improvement concerns.
- **2026-05-12** — [The Agent Development Life Cycle](<planning/The Agent Development Life Cycle.md>) · `planning` · sierra
  Defines an agent development lifecycle from design and simulation through evaluation, deployment, monitoring, and continuous improvement.
- **2026-05-09** — [The Agent Development Lifecycle: Build, Test, Deploy & Monitor AI Agents](<planning/The Agent Development Lifecycle Build, Test, Deploy & Monitor AI Agents.md>) · `planning` · langchain
  Defines the agent development lifecycle from build and test through deployment, monitoring, and iterative improvement.
- **2026-05-07** — [Agent harnesses have an expiration date](<planning/Agent harnesses have an expiration date.md>) · `planning` · arize
  Argues that agent harnesses need lifecycle management as tools, models, and objectives drift, with implications for ongoing evaluation.
- **2026-05-04** — [Swarm management in agent harnesses: owning long-running agents](<multi-agent/Swarm management in agent harnesses owning long-running agents.md>) · `multi-agent` · arize
  Explains swarm management patterns for long-running agent harnesses and how ownership/control should be structured.
- **2026-05-01** — [MCP vs. CLI Skills for agents: what our eval found (and which you should use)](<tool-use/MCP vs. CLI Skills for agents what our eval found (and which you should use).md>) · `tool-use` · arize
  Compares MCP and CLI skills for agents using evaluation results, focusing on reliability and tool interface design.
- **2026-04-30** — [Agents can now create Cloudflare accounts, buy domains, and deploy](<tool-use/Agents can now create Cloudflare accounts, buy domains, and deploy.md>) · `tool-use` · cloudflare-ai
  Via a protocol co-designed with Stripe for Stripe Projects, coding agents can now provision a Cloudflare account, start a paid subscription, register a domain, and receive an API token to deploy — end-to-end with humans only approving payment and terms of service.
- **2026-04-29** — [Using context graphs: build a data moat like Google's using your enterprise data](<memory-context/Using context graphs build a data moat like Google's using your enterprise data.md>) · `memory-context` · arize
  Explains context graphs as an enterprise memory layer for agents and retrieval-heavy AI systems.
- **2026-04-28** — [Context management in agent harnesses: memory, files, and subagents](<memory-context/Context management in agent harnesses memory, files, and subagents.md>) · `memory-context` · arize
  Detailed guide to context management in agent harnesses, including memory, files, subagents, and strategies for working within context limits.
- **2026-04-24** — [What is an agent harness?](<planning/What is an agent harness.md>) · `planning` · arize
  Defines an agent harness and the responsibilities it carries for control flow, state, tools, and testing.
- **2026-04-21** — [AI to Human Agent Handoff Best Practices](<planning/AI to Human Agent Handoff Best Practices.md>) · `planning` · cresta
  Covers best practices for AI-to-human handoffs, including when agents should escalate and how handoff context should be preserved.
- **2026-04-20** — [Orchestrating AI Code Review at scale](<multi-agent/Orchestrating AI Code Review at scale.md>) · `multi-agent` · cloudflare-ai
  Deep dive into Cloudflare's CI-native AI code review built on OpenCode: up to seven specialized reviewer agents (security, performance, quality, docs, compliance) plus a coordinator that deduplicates findings and posts one structured review, run across tens of thousands of GitLab merge requests via a plugin architecture.
- **2026-04-17** — [Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering](<multi-agent/Agentic Engineering How Swarms of AI Agents Are Redefining Software Engineering.md>) · `multi-agent` · langchain
  Discusses how swarms of agents change software engineering workflows, including orchestration, delegation, review, and human oversight.
- **2026-04-16** — [Harnesses are everything. Here's how to optimize yours.](<planning/Harnesses are everything. Here's how to optimize yours.md>) · `planning` · baseten
  Explains why agent harness design matters and how to optimize harnesses for reliable agent behavior.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-04-14** — [Autoscaling Autoresearch: Give your agents elastic GPUs on Modal](<tool-use/Autoscaling Autoresearch Give your agents elastic GPUs on Modal.md>) · `tool-use` · modal
  Shows how autoresearch agents can use elastic GPU compute for parallel experiments, background jobs, and scalable tool execution.
- **2026-04-14** — [Building with Modal and the OpenAI Agents SDK](<tool-use/Building with Modal and the OpenAI Agents SDK.md>) · `tool-use` · modal
  Guide to running OpenAI Agents SDK workflows on Modal, including tool execution, deployment, and scalable background compute.
- **2026-04-13** — [EinsteinArena: Harnessing the collective intelligence of agents in the wild to advance science](<multi-agent/EinsteinArena Harnessing the collective intelligence of agents in the wild to advance science.md>) · `multi-agent` · together
  Explains EinsteinArena for using collective agent intelligence to advance scientific tasks.
- **2026-03-24** — [Harness design for long-running application development](<planning/Harness design for long-running application development.md>) · `planning` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-03-19** — [Managing Memory in AI Agents: Beyond the Context Window](<memory-context/Managing Memory in AI Agents Beyond the Context Window.md>) · `memory-context` · arize
  Covers memory and context-window management patterns for agents that need to preserve useful state over long tasks.
- **2026-03-13** — [How We Built an Agent Skill to Synthesize what Langfuse Users want](<tool-use/How We Built an Agent Skill to Synthesize what Langfuse Users want.md>) · `tool-use` · langfuse
  Case study of building an agent skill to synthesize user feedback and product needs, showing how agents can support operational product workflows.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-03-05** — [How to Build Planning Into Your Agent (The Architecture That Actually Works)](<planning/How to Build Planning Into Your Agent (The Architecture That Actually Works).md>) · `planning` · arize
  Explains planning architectures for agents and how explicit planning changes control flow, reliability, and debugging.
- **2026-03-04** — [From UI to Terminal: Bringing Alyx's Superpowers Into Your Coding Agent](<tool-use/From UI to Terminal Bringing Alyx's Superpowers Into Your Coding Agent.md>) · `tool-use` · arize
  Introduces an AX CLI preview that brings Alyx-style trace and eval workflows into terminal-based coding-agent loops.
- **2026-02-26** — [Building frontend UIs with Codex and Figma | OpenAI Developers](<tool-use/Building frontend UIs with Codex and Figma OpenAI Developers.md>) · `tool-use` · openai-devs
  Announces bidirectional Codex-Figma integration via the Figma MCP server: get_design_context extracts layouts/styles/components from Figma frames for code generation, and generate_figma_design turns a running UI back into editable Figma frames.
- **2026-02-24** — [Alyx 2.0: The AI Agent That Actually Plans](<planning/Alyx 2.0 The AI Agent That Actually Plans.md>) · `planning` · arize
  Introduces Alyx 2.0 as an agent that plans over observability workflows, covering product design lessons from building a more capable AI analyst.
- **2026-02-23** — [How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System (MAS)](<multi-agent/How Cresta Scales Data Annotation With a Human-Supervised Multi-Agent System (MAS).md>) · `multi-agent` · cresta
  Case study on scaling data annotation with a human-supervised multi-agent system, including review and quality-control loops.
- **2026-02-23** — [Run long horizon tasks with Codex | OpenAI Developers](<planning/Run long horizon tasks with Codex OpenAI Developers.md>) · `planning` · openai-devs
  Stress test of long-horizon agentic coding: GPT-5.3-Codex at Extra High reasoning ran ~25 hours uninterrupted, consuming ~13M tokens and generating ~30k lines to build a design tool from a blank repo, framed by METR's ~7-month doubling time for agent task horizons.
- **2026-02-18** — [How Ramp built a full context background coding agent on Modal](<computer-use/How Ramp built a full context background coding agent on Modal.md>) · `computer-use` · modal
  Case study of a background coding agent architecture that gives agents full project context through remote sandboxes.
- **2026-02-13** — [On Agent Frameworks and Agent Observability](<planning/On Agent Frameworks and Agent Observability.md>) · `planning` · langchain
  Connects agent-framework design with observability requirements, arguing that runtime structure determines what teams can debug and evaluate.
- **2026-02-11** — [CUGA Agent: From Benchmarks to Business Impact of IBM's Generalist Agent](<planning/CUGA Agent From Benchmarks to Business Impact of IBM's Generalist Agent.md>) · `planning` · arize
  Brief paper-reading note on IBM's CUGA generalist agent, connecting benchmark performance to business impact.
- **2026-02-11** — [Shell + Skills + Compaction: Tips for long-running agents that do real work | OpenAI Developers](<tool-use/Shell + Skills + Compaction Tips for long-running agents that do real work OpenAI Developers.md>) · `tool-use` · openai-devs
  Nonobvious patterns for three new Responses API primitives for long-running agents — skills (on-demand SKILL.md playbooks), the hosted/local shell tool, and server-side compaction that auto-compresses conversation history — drawn from Codex internals and Glean's production use.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2026-01-29** — [Hierarchical Memory Management In Agent Harnesses](<memory-context/Hierarchical Memory Management In Agent Harnesses.md>) · `memory-context` · arize
  Explains hierarchical memory management patterns for agent harnesses, including how state is organized across short and long horizons.
- **2026-01-28** — [Context Management for Deep Agents](<memory-context/Context Management for Deep Agents.md>) · `memory-context` · langchain
  Explains context management for Deep Agents, including what information to retain, retrieve, summarize, or isolate during long-running tasks.
- **2026-01-22** — [Testing if "bash is all you need"](<tool-use/Testing if bash is all you need.md>) · `tool-use` · braintrust
  Tests whether bash-oriented agents can solve realistic tasks, using evals to measure command-line tool use and agent reliability.
- **2026-01-21** — [AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)](<tool-use/AI Agent interfaces In 2026 Filesystem vs API vs Database (What Actually Works).md>) · `tool-use` · arize
  Compares filesystem, API, and database interfaces for agents, using memory benchmarks and practical interface tradeoffs to evaluate what works in production.
- **2026-01-20** — [Building observable AI agents with Temporal](<tool-use/Building observable AI agents with Temporal.md>) · `tool-use` · braintrust
  Shows how Temporal workflows can make AI agents observable, connecting durable execution with traces, evals, and debugging data.
- **2026-01-08** — [How Context Graphs Turn Agent Traces Into Durable Business Assets](<memory-context/How Context Graphs Turn Agent Traces Into Durable Business Assets.md>) · `memory-context` · arize
  Describes context graphs as a way to transform agent traces into durable memory and operational knowledge assets.
- **2025-12-17** — [Self-Improving Agents, Powered by Your Evals](<planning/Self-Improving Agents, Powered by Your Evals.md>) · `planning` · fireworks
  Describes self-improving agents powered by eval loops, using evaluation feedback to improve behavior.
- **2025-12-09** — [Agent Engineering: A New Discipline](<planning/Agent Engineering A New Discipline.md>) · `planning` · langchain
  Defines agent engineering as a discipline around designing, evaluating, observing, and iterating on production agents rather than treating them as prompt-only systems.
- **2025-12-09** — [Building Langfuse's MCP Server: Code Reuse and Developer Experience](<tool-use/Building Langfuse's MCP Server Code Reuse and Developer Experience.md>) · `tool-use` · langfuse
  Engineering writeup on building the Langfuse MCP server, focusing on code reuse, developer experience, and exposing observability workflows to agents.
- **2025-12-04** — [How We Built a State-of-the-Art Research Agent for Call Center Conversation Analytics](<planning/How We Built a State-of-the-Art Research Agent for Call Center Conversation Analytics.md>) · `planning` · cresta
  Detailed build story for a research agent over conversation analytics, covering agent design and domain-specific workflow constraints.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-25** — [Building and Deploying Production‑Grade AI Agents: Cresta’s End‑to‑End Approach](<planning/Building and Deploying Production‑Grade AI Agents Cresta’s End‑to‑End Approach.md>) · `planning` · cresta
  End-to-end guide to production AI agent deployment, including design, launch, monitoring, and operational controls.
- **2025-11-24** — [Introducing advanced tool use on the Claude Developer Platform](<tool-use/Introducing advanced tool use on the Claude Developer Platform.md>) · `tool-use` · anthropic-engineering
  Introduces tool search, programmatic tool calling, and tool-use examples on the Claude Developer Platform to scale agents past context-window limits on large tool sets.
- **2025-11-19** — [50 Trillion Tokens Per Day: The State of Agent Environments](<computer-use/50 Trillion Tokens Per Day The State of Agent Environments.md>) · `computer-use` · fireworks
  Surveys the state of agent environments, emphasizing execution scale, sandboxing, and environment design.
- **2025-11-05** — [Tool Calling in Inference](<tool-use/Tool Calling in Inference.md>) · `tool-use` · baseten
  Explains tool calling in inference and how model servers support structured external actions.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-10-14** — [Optimizing Coding Agent Rules (./clinerules) for Improved Accuracy](<computer-use/Optimizing Coding Agent Rules (.clinerules) for Improved Accuracy.md>) · `computer-use` · arize
  Explains how coding-agent rule files affect accuracy and how to optimize them for better agent behavior.
- **2025-09-22** — [Build an AI coding platform that scales to millions of monthly sessions](<computer-use/Build an AI coding platform that scales to millions of monthly sessions.md>) · `computer-use` · modal
  Describes architecture concerns for AI coding platforms that need to scale sandboxed coding sessions to large user volumes.
- **2025-09-22** — [Why we built the Responses API | OpenAI Developers](<tool-use/Why we built the Responses API OpenAI Developers.md>) · `tool-use` · openai-devs
  OpenAI's design rationale for the Responses API as an agentic loop unifying Chat Completions and Assistants: it preserves reasoning state across turns (+5% on TAUBench, better cache utilization) and emits multiple output items — tool calls, structured outputs, intermediate steps — not just the final message.
- **2025-09-11** — [How to turn Claude Code into a domain specific coding agent](<tool-use/How to turn Claude Code into a domain specific coding agent.md>) · `tool-use` · langchain
  Shows how to turn Claude Code into a domain-specific coding agent using instructions, tools, context, and workflow constraints.
- **2025-09-11** — [Writing effective tools for AI agents—using AI agents](<tool-use/Writing effective tools for AI agents—using AI agents.md>) · `tool-use` · anthropic-engineering
  Guidance on designing tool interfaces agents use reliably—consolidating workflows, namespacing, returning meaningful context—and using Claude to optimize its own tools.
- **2025-09-09** — [Orchestrator-Worker Agents: A Practical Comparison of Common Agent Frameworks](<multi-agent/Orchestrator-Worker Agents A Practical Comparison of Common Agent Frameworks.md>) · `multi-agent` · arize
  Compares orchestrator-worker agent frameworks and clarifies when this multi-agent pattern is useful.
- **2025-09-09** — [AI that knows your data](<tool-use/AI that knows your data.md>) · `tool-use` · braintrust
  Discusses MCP-style access to data and tools so AI systems can retrieve context and act against application-specific resources.
- **2025-09-04** — [Building LangGraph: Designing an Agent Runtime from first principles](<planning/Building LangGraph Designing an Agent Runtime from first principles.md>) · `planning` · langchain
  Design history of LangGraph as an agent runtime from first principles, covering control flow, state, durability, and production requirements.
- **2025-08-28** — [Claude Code vs Cursor: A Power-User’s Playbook](<tool-use/Claude Code vs Cursor A Power-User’s Playbook.md>) · `tool-use` · arize
  Compares Claude Code and Cursor from a power-user workflow perspective, focusing on coding-agent interfaces and usage patterns.
- **2025-08-21** — [Voice AI Agents for Customer Experience: Why Decentralized Agent Architectures Can Outperform Central Orchestrators](<multi-agent/Voice AI Agents for Customer Experience Why Decentralized Agent Architectures Can Outperform Central Orchestrators.md>) · `multi-agent` · cresta
  Argues for decentralized voice-agent architectures over central orchestration in some customer-experience workloads.
- **2025-08-21** — [AI agents for efficient LLM inference engineering](<tool-use/AI agents for efficient LLM inference engineering.md>) · `tool-use` · together
  Case study of using AI agents to automate engineering tasks while developing efficient inference systems.
- **2025-08-07** — [The canonical agent architecture: A while loop with tools](<planning/The canonical agent architecture A while loop with tools.md>) · `planning` · braintrust
  Frames the canonical agent architecture as a while loop around model calls, tool use, state updates, and termination criteria for controllable agent behavior.
- **2025-08-06** — [Introducing Open SWE: An Open-Source Asynchronous Coding Agent](<tool-use/Introducing Open SWE An Open-Source Asynchronous Coding Agent.md>) · `tool-use` · langchain
  Introduces Open SWE as an open-source asynchronous coding agent and discusses its architecture for long-running coding tasks.
- **2025-07-24** — [What is an AI code sandbox?](<computer-use/What is an AI code sandbox.md>) · `computer-use` · modal
  Explains AI code sandboxes as isolated execution environments for coding agents, including safety and state considerations.
- **2025-07-15** — [Building reliable AI agents](<planning/Building reliable AI agents.md>) · `planning` · baseten
  Covers practical design patterns for building more reliable AI agents.
- **2025-07-11** — [Function calling for agentic AI systems](<tool-use/Function calling for agentic AI systems.md>) · `tool-use` · fireworks
  Explains function calling as the bridge between LLM outputs, external tools, and agentic execution loops.
- **2025-07-02** — [DeepSWE coding agent trained with scaled RL](<tool-use/DeepSWE coding agent trained with scaled RL.md>) · `tool-use` · together
  Explains DeepSWE, an open-source coding agent trained by scaling reinforcement learning.
- **2025-06-16** — [How and when to build multi-agent systems](<multi-agent/How and when to build multi-agent systems.md>) · `multi-agent` · langchain
  Guidance on when multi-agent systems are warranted and how to design agent roles, coordination, and boundaries.
- **2025-06-13** — [How we built our multi-agent research system](<multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-06-12** — [From Zero to One: Building An Autonomous and Open Data Scientist Agent from Scratch](<planning/From Zero to One Building An Autonomous and Open Data Scientist Agent from Scratch.md>) · `planning` · together
  Walkthrough of building an autonomous open data-scientist agent from scratch.
- **2025-05-21** — [Building an open-source Browser Agent on Fireworks AI](<computer-use/Building an open-source Browser Agent on Fireworks AI.md>) · `computer-use` · fireworks
  Walkthrough of building an open-source browser agent, including model choice, tool execution, and environment control.
- **2025-05-19** — [Agentic AI Systems](<planning/Agentic AI Systems.md>) · `planning` · fireworks
  Overview of agentic AI systems, covering planning, tool use, control loops, and production architecture concerns.
- **2025-04-20** — [How to think about agent frameworks](<planning/How to think about agent frameworks.md>) · `planning` · langchain
  Framework for evaluating agent frameworks by abstraction level, control, durability, observability, and fit to production workflows.
- **2025-04-16** — [Open Deep Research](<tool-use/Open Deep Research.md>) · `tool-use` · together
  Describes an open deep research system combining retrieval, planning, and tool use.
- **2025-04-09** — [Embracing Google's Agent-To-Agent (A2A) Protocol](<multi-agent/Embracing Google's Agent-To-Agent (A2A) Protocol.md>) · `multi-agent` · arize
  Discusses Google's Agent-to-Agent protocol and why interoperability standards matter for multi-agent systems and production agent ecosystems.
- **2025-04-08** — [DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level](<tool-use/DeepCoder A Fully Open-Source 14B Coder at O3-mini Level.md>) · `tool-use` · together
  Describes DeepCoder, an open-source coding model trained for O3-mini-level coding performance.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2025-03-19** — [Comparing Open-Source AI Agent Frameworks](<planning/Comparing Open-Source AI Agent Frameworks.md>) · `planning` · langfuse
  Compares open-source AI agent frameworks and their architecture tradeoffs around orchestration, tools, memory, extensibility, and production readiness.
- **2025-02-26** — [Memory and State in LLM Applications](<memory-context/Memory and State in LLM Applications.md>) · `memory-context` · arize
  Explains memory and state patterns in LLM applications and how they affect reliability across interactions.
- **2025-02-20** — [The Agent Deep Dive: David Zhang’s Open Deep Research](<planning/The Agent Deep Dive David Zhang’s Open Deep Research.md>) · `planning` · langfuse
  Deep dive on Open Deep Research as an agentic system, covering planning, tool use, research workflows, and trace-based inspection.
- **2025-02-18** — [How to Build An AI Agent](<planning/How to Build An AI Agent.md>) · `planning` · arize
  Practical guide to building an AI agent, covering planning, tools, state, and reliability considerations.
- **2025-02-10** — [Benchmarking Single Agent Performance](<planning/Benchmarking Single Agent Performance.md>) · `planning` · langchain
  Benchmarks single-agent ReAct-style performance and discusses evaluation methodology for agent reasoning/tool-use loops.
- **2025-01-31** — [Best Practices for Building an Agent Router](<planning/Best Practices for Building an Agent Router.md>) · `planning` · arize
  Explains agent-router design as a decision layer that routes user requests to the right tools, services, or actions in larger agent systems.
- **2025-01-22** — [Evaluating agents](<planning/Evaluating agents.md>) · `planning` · braintrust
  Detailed guide to evaluating agents, including task design, tool-use traces, intermediate-step analysis, and failure modes unique to multi-step systems.
- **2025-01-07** — [Agents](<planning/Agents.md>) · `planning` · chip-huyen
  Framework for foundation-model agents covering environments, tools, planning, action selection, failure modes, and evaluation for multi-step agentic applications.
- **2024-12-19** — [Building Effective AI Agents](<planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
- **2024-12-10** — [Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies](<multi-agent/Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies.md>) · `multi-agent` · arize
  Summarizes collaborative LLM strategies such as merging, ensembling, and cooperation for multi-model or multi-agent systems.
- **2024-12-04** — [AI Agent Workflows and Architectures Masterclass](<planning/AI Agent Workflows and Architectures Masterclass.md>) · `planning` · arize
  Introduces practical agent workflow and architecture patterns, emphasizing simple tool-calling loops and design choices over vague autonomy claims.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-10-16** — [Comparing OpenAI Swarm with other Multi Agent Frameworks](<multi-agent/Comparing OpenAI Swarm with other Multi Agent Frameworks.md>) · `multi-agent` · arize
  Compares OpenAI Swarm with other multi-agent frameworks, highlighting orchestration patterns and framework tradeoffs.
- **2024-10-08** — [Functions: flexible AI engineering primitives](<tool-use/Functions flexible AI engineering primitives.md>) · `tool-use` · braintrust
  Introduces functions as flexible AI engineering primitives for tool calling, structured behavior, and reusable evaluation or workflow components.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.
- **2024-08-29** — [Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction](<tool-use/Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction.md>) · `tool-use` · fireworks
  Tutorial for building a function-calling application with FastAPI, SerpAPI, and structured tool invocation.
- **2024-08-08** — [LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents](<planning/LlamaIndex Workflows Navigating a New Way To Build Cyclical Agents.md>) · `planning` · arize
  Explains LlamaIndex Workflows as a pattern for building cyclical agents with explicit control flow.
- **2024-06-11** — [Together MoA collective intelligence of open-source models](<multi-agent/Together MoA collective intelligence of open-source models.md>) · `multi-agent` · together
  Explains Mixture-of-Agents for improving model outputs through collective open-source model reasoning.
- **2024-05-08** — [Code Generation with Large Language Models - Fireworks AI Take](<tool-use/Code Generation with Large Language Models - Fireworks AI Take.md>) · `tool-use` · fireworks
  Discusses code-generation copilots with LLMs, including model behavior, latency, and developer workflow considerations.
- **2024-04-26** — [Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models](<tool-use/Keys To Understanding ReAct Synergizing Reasoning and Acting in Language Models.md>) · `tool-use` · arize
  Explains ReAct as a reasoning-plus-acting pattern for agents and how it structures tool use.
- **2023-12-20** — [Benchmarking Agent Tool Use](<tool-use/Benchmarking Agent Tool Use.md>) · `tool-use` · langchain
  Benchmarking study for agent tool use, focused on measuring whether agents choose and invoke tools correctly across tasks.
- **2023-06-20** — [Voyager: An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion](<planning/Voyager An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion.md>) · `planning` · arize
  Paper-reading summary of Voyager as an open-ended embodied agent using LLM-driven skills and exploration.
- **2023-03-21** — [Toolformer: Training LLMs To Use Tools](<tool-use/Toolformer Training LLMs To Use Tools.md>) · `tool-use` · arize
  Summarizes Toolformer and how language models can learn to use external tools.

## Also relevant (filed elsewhere)

- **2026-07-13** — [Introducing Precursor: detecting agentic behavior with continuous client-side signals](<../product-engineering/security/Introducing Precursor detecting agentic behavior with continuous client-side signals.md>) · `security` · cloudflare-ai
  Cloudflare's Precursor injects client-side JS to continuously collect session-level behavioral signals (mouse-movement physics, keystroke rhythm, focus changes) and feeds them into an edge-side evaluator/dispatcher to distinguish human from agentic/bot traffic in real time, feeding Cloudflare's bot score without exposing raw signals to customers.
- **2026-07-10** — [AI-pilling our company: lessons learned](<../product-engineering/case-studies/AI-pilling our company lessons learned.md>) · `case-studies` · sierra
  Internal adoption case study on spreading AI workflows through a company, including practical lessons for using agents and tools in day-to-day work.
- **2026-07-09** — [The new GPT-5.6 family: Luna, Terra, Sol](<../models/releases/The new GPT-5.6 family Luna, Terra, Sol.md>) · `releases` · simon-willison
  Notes on the GPT-5.6 Luna, Terra, and Sol release, including pricing, million-token context, agentic benchmark claims, SWE-Bench Pro caveats, programmatic tool calling, subagents, and prompt-cache breakpoints.
- **2026-07-08** — [Rewriting Bun in Rust](<../product-engineering/case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-08** — [The agent is the user now: lessons from the founder of WorkOS](<../product-engineering/security/The agent is the user now lessons from the founder of WorkOS.md>) · `security` · arize
  Interview-driven discussion of agents as users, covering identity, permissions, memory, evals, and feedback loops as core production-agent infrastructure.
- **2026-07-07** — [Improving Agents is a Data Mining Problem](<../evals-observability/monitoring/Improving Agents is a Data Mining Problem.md>) · `monitoring` · langchain
  Argues that improving agents is a data-mining problem over traces, failures, feedback, and recurring behavioral patterns.
- **2026-07-07** — [How I shipped a month of engineering work in four days with GLM 5.2 Fast](<../product-engineering/case-studies/How I shipped a month of engineering work in four days with GLM 5.2 Fast.md>) · `case-studies` · fireworks
  A senior engineer used GLM 5.2 Fast (via Fireworks' FireConnect with Claude Code) to design, spec, and implement a GPU-scheduler 'reclaim' feature in four days for $218 in inference cost — 4 PRs, ~3,000 LOC, 34 passing tests — crediting the model's ~400 tok/s speed for sustaining a real-time design/test/implement loop instead of async, tab-switching workflows.
- **2026-07-02** — [How to evaluate AI agents, avoid reward hacking, and build better specs](<../evals-observability/evaluation/How to evaluate AI agents, avoid reward hacking, and build better specs.md>) · `evaluation` · arize
  Connects agent evaluation with specification quality, including reward hacking risks and tighter behavioral contracts.
- **2026-07-02** — [Your coding agent bill doubled. Here’s how to fix it.](<../infra-platform/cost/Your coding agent bill doubled. Here’s how to fix it.md>) · `cost` · langchain
  Practical guide to reducing coding-agent spend through model choice, caching, harness tuning, and workflow design.
- **2026-07-01** — [How Pendo uses LangSmith to trace Novus from user behavior to code fixes](<../product-engineering/case-studies/How Pendo uses LangSmith to trace Novus from user behavior to code fixes.md>) · `case-studies` · langchain
  Pendo case study tracing Novus from user behavior to code fixes, showing how traces connect product signals to agent improvements.
- **2026-06-30** — [Harbor x LangChain: A Unified Stack for Evaluating Agents](<../evals-observability/evaluation/Harbor x LangChain A Unified Stack for Evaluating Agents.md>) · `evaluation` · langchain
  Describes a unified stack for evaluating agents, integrating agent execution, traces, datasets, and scoring workflows.
- **2026-06-30** — [How Deep Agents Run Untrusted Code Without a Sandbox](<../product-engineering/security/How Deep Agents Run Untrusted Code Without a Sandbox.md>) · `security` · langchain
  Explains how Deep Agents run untrusted code without a conventional sandbox and the security tradeoffs in agent execution design.
- **2026-06-29** — [Introducing Dynamic Subagents in Deep Agents](<multi-agent/Introducing Dynamic Subagents in Deep Agents.md>) · `multi-agent` · langchain
  Introduces dynamic subagents in Deep Agents, covering delegation, specialized worker agents, and runtime coordination.
- **2026-06-29** — [How Candidly Built State-Aware Agent Harnesses with LangSmith](<../product-engineering/case-studies/How Candidly Built State-Aware Agent Harnesses with LangSmith.md>) · `case-studies` · langchain
  Candidly case study on building state-aware agent harnesses with LangSmith for production agent workflows.
- **2026-06-26** — [Prompt Caching with Deep Agents](<../prompt-engineering/context-engineering/Prompt Caching with Deep Agents.md>) · `context-engineering` · langchain
  Explains prompt caching for Deep Agents and how cache-aware context design reduces latency and cost for repeated agent work.
- **2026-06-26** — [How to eval stateful agents](<../evals-observability/evaluation/How to eval stateful agents.md>) · `evaluation` · braintrust
  Guide to evaluating stateful agents, including memory, conversation state, trace review, and tests for behavior that depends on previous interactions.
- **2026-06-26** — [Making private MCP servers reachable without making them public | OpenAI Developers](<../product-engineering/security/Making private MCP servers reachable without making them public OpenAI Developers.md>) · `security` · openai-devs
  Engineering design of OpenAI's Secure MCP Tunnel: a customer-run open-source client beside a private MCP server opens outbound-only HTTPS to OpenAI, forwarding MCP requests (including streaming and auth flows) so ChatGPT/Codex can reach the server without public endpoints, VPNs, or third-party tunnels.
- **2026-06-24** — [Long-horizon agent benchmarks are fragmenting: a field guide to what each one actually measures](<../models/benchmarks/Long-horizon agent benchmarks are fragmenting a field guide to what each one actually measures.md>) · `benchmarks` · arize
  Field guide to long-horizon agent benchmarks and what each benchmark family reveals about agent performance.
- **2026-06-22** — [Project Rosetta Stone: a reference implementation for instrumenting agents in any framework](<../evals-observability/tracing/Project Rosetta Stone a reference implementation for instrumenting agents in any framework.md>) · `tracing` · arize
  Describes a reference implementation for instrumenting agents across frameworks, useful for standardizing trace capture.
- **2026-06-19** — [Temporary Cloudflare Accounts for AI agents](<../infra-platform/deployment/Temporary Cloudflare Accounts for AI agents.md>) · `deployment` · cloudflare-ai
  Temporary Cloudflare Accounts let agents run 'wrangler deploy --temporary' to ship a Worker with zero signup — a 60-minute claimable account with auto-provisioned API token — with Wrangler itself prompting agents about the flag, removing human-built OAuth/dashboard friction from the deploy loop.
- **2026-06-19** — [Unpacking sandbox startup latency: why started is not ready](<../infra-platform/deployment/Unpacking sandbox startup latency why started is not ready.md>) · `deployment` · modal
  Breaks down sandbox startup latency and why ready-state semantics matter for agent and remote-execution workflows.
- **2026-06-18** — [Build your own vulnerability harness](<../product-engineering/security/Build your own vulnerability harness.md>) · `security` · cloudflare-ai
  How Cloudflare grew a ~450-line security-audit skill into a model-agnostic, fleet-wide vulnerability-scanning harness: parallel recon agents, per-attack-class Hunter agents, adversarial validators, schema-checked findings.json, and independent re-verification, with different models cross-testing discovery vs. validation.
- **2026-06-17** — [Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue](<../infra-platform/deployment/Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue.md>) · `deployment` · cloudflare-ai
  Describes a three-layer production agent stack — framework (Flue, from the Astro team, built on the Pi harness), harness (Project Think, Pi), and runtime (Cloudflare Agents SDK) — with durable execution, dynamic code execution, and a durable filesystem exposed to any harness.
- **2026-06-16** — [Why Fleet Has General Purpose Chat and Specialized Agents](<../product-engineering/architecture/Why Fleet Has General Purpose Chat and Specialized Agents.md>) · `architecture` · langchain
  Fleet case study explaining why a product needs both general-purpose chat and specialized agents for different user workflows.
- **2026-06-15** — [How LangChain Made Coding Agent Spend Predictable](<../infra-platform/cost/How LangChain Made Coding Agent Spend Predictable.md>) · `cost` · langchain
  Explains how LangChain made coding-agent spend more predictable using constraints, monitoring, and workflow-level cost controls.
- **2026-06-12** — [How Box AI built enterprise content agents with Deep Agents](<../product-engineering/case-studies/How Box AI built enterprise content agents with Deep Agents.md>) · `case-studies` · langchain
  Case study of Box AI moving enterprise content workflows to Deep Agents, covering agent architecture and production constraints.
- **2026-06-11** — [PostgresFS vs. SQL skills: should AI agents fake a filesystem?](<tool-use/PostgresFS vs. SQL skills should AI agents fake a filesystem.md>) · `tool-use` · arize
  Compares filesystem-like and SQL-backed skill interfaces for AI agents, focusing on state access and tool ergonomics.
- **2026-06-11** — [How Benchling builds agents when the smartest AI isn't smart enough](<../product-engineering/case-studies/How Benchling builds agents when the smartest AI isn't smart enough.md>) · `case-studies` · langchain
  Case-study notes on how Benchling builds agents when model capability is insufficient on its own, emphasizing workflow design and product constraints.
- **2026-06-10** — [The Missing Link Between Agents and Applications](<../product-engineering/architecture/The Missing Link Between Agents and Applications.md>) · `architecture` · langchain
  Explains the missing application-layer pieces around agents, connecting agent runtimes to product interfaces, state, and deployment workflows.
- **2026-06-09** — [The Data Comes First: Mining Real Conversations for Test Coverage](<../evals-observability/testing/The Data Comes First Mining Real Conversations for Test Coverage.md>) · `testing` · cresta
  Explains how real conversation data can be mined to create better test coverage for AI agents.
- **2026-06-09** — [AI is eating the AI engineering loop](<../industry/trends/AI is eating the AI engineering loop.md>) · `trends` · langfuse
  Argues that AI is reshaping the AI engineering loop itself, with agents increasingly participating in prompt, eval, observability, and product iteration workflows.
- **2026-06-05** — [How we use agents to review production infrastructure](<../product-engineering/case-studies/How we use agents to review production infrastructure.md>) · `case-studies` · langfuse
  Case study of using agents to review production infrastructure, including operational workflows, review boundaries, and human oversight.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<../evals-observability/monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-06-03** — [How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith](<../product-engineering/case-studies/How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith.md>) · `case-studies` · langchain
  Harmonic case study on rebuilding Scout with Deep Agents and LangSmith, linking agent architecture to retention and evaluation.
- **2026-06-02** — [Designing Efficient Verifiers for Legal Agents](<../evals-observability/evaluation/Designing Efficient Verifiers for Legal Agents.md>) · `evaluation` · langchain
  Explains how to design efficient verifiers for legal agents so domain-specific correctness can be checked without excessive cost.
- **2026-06-02** — [Introducing Rubrics: Build Agents that Evaluate and Correct Their Work](<../evals-observability/evaluation/Introducing Rubrics Build Agents that Evaluate and Correct Their Work.md>) · `evaluation` · langchain
  Introduces rubrics for Deep Agents so agents can evaluate and correct their own work against explicit criteria.
- **2026-06-01** — [The best eval harness for production AI and agents: A comparison](<../evals-observability/testing/The best eval harness for production AI and agents A comparison.md>) · `testing` · arize
  Compares production AI eval harnesses and highlights the design dimensions that matter for agents and applications.
- **2026-06-01** — [How Rippling built production AI in 6 months with Deep Agents and LangSmith](<../product-engineering/case-studies/How Rippling built production AI in 6 months with Deep Agents and LangSmith.md>) · `case-studies` · langchain
  Rippling case study on rolling production AI across products with Deep Agents and LangSmith in a six-month buildout.
- **2026-05-29** — [Interpreter Skills: Building Workflows for Agents](<tool-use/Interpreter Skills Building Workflows for Agents.md>) · `tool-use` · langchain
  Introduces interpreter skills as reusable workflows for agents that need to execute code, inspect outputs, and compose tools.
- **2026-05-28** — [How we built Cloudflare's data platform and an AI agent on top of it](<../product-engineering/architecture/How we built Cloudflare's data platform and an AI agent on top of it.md>) · `architecture` · cloudflare-ai
  How Cloudflare built Town Lake, a single-SQL-interface data platform on R2/Workers/Workflows unifying Postgres, ClickHouse, Kafka, and BigQuery sprawl (1B+ events/sec), and Skipper, an AI agent on top that answers plain-English questions with auditable queries and PII-aware governance.
- **2026-05-27** — [How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith](<../product-engineering/case-studies/How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Lyft case study on building a self-serve AI agent platform for customer support with LangGraph and LangSmith.
- **2026-05-25** — [How we contain Claude across products](<../product-engineering/security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-05-20** — [The Agent Execution Tax](<../evals-observability/evaluation/The Agent Execution Tax.md>) · `evaluation` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-05-19** — [Benchmarking inference at scale: coding agents](<../evals-observability/evaluation/Benchmarking inference at scale coding agents.md>) · `evaluation` · together
  Benchmarks inference at scale for coding-agent workloads.
- **2026-05-18** — [Coding agent tracing and evaluation: An open source tool to improve AI coding workflows](<../evals-observability/tracing/Coding agent tracing and evaluation An open source tool to improve AI coding workflows.md>) · `tracing` · arize
  Introduces open-source tracing and evaluation for coding agents, focusing on visibility into tool use and code-edit behavior.
- **2026-05-14** — [How to evaluate multi-turn conversations](<../evals-observability/evaluation/How to evaluate multi-turn conversations.md>) · `evaluation` · braintrust
  Guide to evaluating multi-turn conversations, including state, conversation-level criteria, turn-level scoring, and agent-like interaction failures.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<../evals-observability/monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-12** — [Sierra Agent OS 2.0: from answers to memory and action](<memory-context/Sierra Agent OS 2.0 from answers to memory and action.md>) · `memory-context` · sierra
  Describes Agent OS 2.0 moving agents from answers to memory and action, covering persistent context, tool use, and stateful behavior.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [Preserving agent behavior while serving LLMs reliably](<../inference/serving/Preserving agent behavior while serving LLMs reliably.md>) · `serving` · sierra
  Covers model failover for preserving agent behavior while serving LLMs reliably across model/provider disruptions.
- **2026-05-12** — [Context engineering: the key to great agents](<../prompt-engineering/context-engineering/Context engineering the key to great agents.md>) · `context-engineering` · sierra
  Explains context engineering for agents, including how the right knowledge, state, and instructions shape agent quality.
- **2026-05-12** — [Expert Answers: Turn everyday support conversations into compounding knowledge](<../rag-retrieval/pipelines/Expert Answers Turn everyday support conversations into compounding knowledge.md>) · `pipelines` · sierra
  Describes turning everyday support conversations into compounding knowledge, using agent interactions to improve knowledge bases and answers.
- **2026-05-12** — [Tau-Bench: Benchmarking AI agents for the real-world](<../evals-observability/evaluation/Tau-Bench Benchmarking AI agents for the real-world.md>) · `evaluation` · sierra
  Introduces tau-Bench as a benchmark for real-world AI agents, focusing on task completion, tool use, and operational realism.
- **2026-05-12** — [Tau-Bench shaping development and evaluation agents](<../evals-observability/evaluation/Tau-Bench shaping development and evaluation agents.md>) · `evaluation` · sierra
  Explains how tau-bench shapes agent development and evaluation by providing realistic tasks and measurable behavior.
- **2026-05-12** — [Tau2-Bench](<../evals-observability/evaluation/Tau2-Bench.md>) · `evaluation` · sierra
  Introduces tau2-bench for evaluating agents in collaborative real-world scenarios where task success depends on interaction dynamics.
- **2026-05-12** — [Tau3-Bench: Advancing agent evaluation to knowledge and voice](<../evals-observability/evaluation/Tau3-Bench Advancing agent evaluation to knowledge and voice.md>) · `evaluation` · sierra
  Introduces tau3-Bench for extending agent evaluation to knowledge and voice tasks, expanding beyond text-only transactional benchmarks.
- **2026-05-12** — [Insights 2.0: AI that improves your AI](<../evals-observability/monitoring/Insights 2.0 AI that improves your AI.md>) · `monitoring` · sierra
  Describes using AI-generated insights from production conversations to improve deployed agents and surface recurring issues.
- **2026-05-12** — [Who monitors the monitors?](<../evals-observability/monitoring/Who monitors the monitors.md>) · `monitoring` · sierra
  Discusses monitoring AI agents and the meta-problem of monitoring the monitors, with emphasis on operational feedback and quality controls.
- **2026-05-12** — [Simulations: the secret behind every great agent](<../evals-observability/testing/Simulations the secret behind every great agent.md>) · `testing` · sierra
  Explains simulation as a testing strategy for agents, using realistic scenarios to validate behavior before customer deployment.
- **2026-05-12** — [Agent Traces: getting to the fix, fast](<../evals-observability/tracing/Agent Traces getting to the fix, fast.md>) · `tracing` · sierra
  Introduces agent traces as a debugging workflow for finding failures quickly across conversations, tools, and agent decisions.
- **2026-05-12** — [From LLMs to enterprise-grade agents](<../product-engineering/architecture/From LLMs to enterprise-grade agents.md>) · `architecture` · sierra
  Explains what distinguishes enterprise-grade agents from raw LLMs, including integrations, policy controls, reliability, and operational lifecycle.
- **2026-05-12** — [Industry first: PCI-compliant agents](<../product-engineering/security/Industry first PCI-compliant agents.md>) · `security` · sierra
  Explains PCI-compliant payment workflows for agents, focusing on secure action-taking and sensitive-data handling.
- **2026-05-11** — [From observability to context: What’s next for Arize Phoenix](<../evals-observability/tracing/From observability to context What’s next for Arize Phoenix.md>) · `tracing` · arize
  Connects LLM observability with context management, showing how traces and application state can become reusable context for better agents.
- **2026-05-05** — [Agent observability needs feedback to power learning](<../evals-observability/monitoring/Agent observability needs feedback to power learning.md>) · `monitoring` · langchain
  Explains why agent observability needs feedback loops from users, evaluators, and production traces to power ongoing agent learning and improvement.
- **2026-05-05** — [AI agent evaluation: How to test, debug, and improve agents in production](<../evals-observability/testing/AI agent evaluation How to test, debug, and improve agents in production.md>) · `testing` · arize
  Explains how to test, debug, and improve AI agents in production with structured evaluation and observability.
- **2026-05-04** — [Swarm management in agent harnesses: owning long-running agents](<multi-agent/Swarm management in agent harnesses owning long-running agents.md>) · `multi-agent` · arize
  Explains swarm management patterns for long-running agent harnesses and how ownership/control should be structured.
- **2026-05-01** — [Why agent telemetry needs standards](<../evals-observability/tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-05-01** — [Designing the AI Agent Supervision Experience](<../product-engineering/ux-patterns/Designing the AI Agent Supervision Experience.md>) · `ux-patterns` · cresta
  Discusses UX and workflow design for supervising AI agents, including human oversight and intervention surfaces.
- **2026-04-28** — [Context management in agent harnesses: memory, files, and subagents](<memory-context/Context management in agent harnesses memory, files, and subagents.md>) · `memory-context` · arize
  Detailed guide to context management in agent harnesses, including memory, files, subagents, and strategies for working within context limits.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<../evals-observability/evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-04-22** — [How to add an evaluation harness to your Gemini CLI coding agent](<../evals-observability/testing/How to add an evaluation harness to your Gemini CLI coding agent.md>) · `testing` · arize
  Walks through adding an evaluation harness to a Gemini CLI coding agent, including how to measure and compare agent behavior.
- **2026-04-09** — [Human judgment in the agent improvement loop](<../evals-observability/evaluation/Human judgment in the agent improvement loop.md>) · `evaluation` · langchain
  Explains where human judgment fits into the agent improvement loop, including review, labeling, feedback, and evaluator calibration.
- **2026-04-08** — [Agentic eval development with the Braintrust CLI](<../evals-observability/testing/Agentic eval development with the Braintrust CLI.md>) · `testing` · braintrust
  Shows how to use the Braintrust CLI for agentic eval development, turning local experiments into repeatable tests for agent behavior.
- **2026-04-03** — [From First Eval to Autonomous AI Ops: A Maturity Model for AI Evaluation](<../evals-observability/evaluation/From First Eval to Autonomous AI Ops A Maturity Model for AI Evaluation.md>) · `evaluation` · arize
  Defines a maturity model for moving from first evaluations to automated AI operations, with emphasis on eval loops and production governance.
- **2026-04-03** — [AI for Systems: Using LLMs to Optimize Database Query Execution](<../product-engineering/architecture/AI for Systems Using LLMs to Optimize Database Query Execution.md>) · `architecture` · together
  Explores using LLMs to optimize database query execution as an AI-for-systems pattern.
- **2026-03-31** — [Baseten Training: an autoresearch substrate](<../models/fine-tuning/Baseten Training an autoresearch substrate.md>) · `fine-tuning` · baseten
  Frames model training infrastructure as an autoresearch substrate for running iterative experiments and training jobs.
- **2026-03-27** — [Agent Evaluation Readiness Checklist](<../evals-observability/evaluation/Agent Evaluation Readiness Checklist.md>) · `evaluation` · langchain
  Checklist for agent-evaluation readiness covering task definitions, datasets, traces, scoring, human review, and rollout criteria.
- **2026-03-26** — [How we build evals for Deep Agents](<../evals-observability/evaluation/How we build evals for Deep Agents.md>) · `evaluation` · langchain
  Describes how LangChain builds evals for Deep Agents, including datasets, task realism, scorers, and iteration loops.
- **2026-03-26** — [Observability for AI Agents: Tracing Multi-Service LLM Pipelines with Langfuse](<../evals-observability/tracing/Observability for AI Agents Tracing Multi-Service LLM Pipelines with Langfuse.md>) · `tracing` · cresta
  Shows how to trace multi-service LLM pipelines for AI agents with Langfuse, including cross-service visibility concerns.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<../product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-03-24** — [We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests](<../evals-observability/testing/We Used Autoresearch on Our AI Skill, It Taught Us to Write Better Tests.md>) · `testing` · langfuse
  Case study of using Autoresearch to improve an AI skill, with emphasis on writing better tests and using research-agent output to harden behavior.
- **2026-03-22** — [100 AI Agents Per Employee: The Enterprise Governance Gap](<../product-engineering/security/100 AI Agents Per Employee The Enterprise Governance Gap.md>) · `security` · arize
  Argues that enterprises adopting large populations of AI agents need governance for permissions, ownership, auditability, and lifecycle management before agent scale outpaces human oversight.
- **2026-03-11** — [From prompts to products: One year of Responses | OpenAI Developers](<../product-engineering/case-studies/From prompts to products One year of Responses OpenAI Developers.md>) · `case-studies` · openai-devs
  One-year retrospective on the Responses API told through five developer stories, including Raindrop AI's production agent-monitoring platform (failure detection and debugging on GPT-5.2 via the Vercel AI SDK) built on its hosted-tool and background-analysis primitives.
- **2026-03-10** — [How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator](<../evals-observability/evaluation/How We Used Evals (and an AI Agent) to Iteratively Improve an AI Newsletter Generator.md>) · `evaluation` · arize
  Case study on using evals plus an agentic workflow to iteratively improve a newsletter-generation system.
- **2026-03-09** — [How we built LangChain’s GTM Agent](<../product-engineering/case-studies/How we built LangChain’s GTM Agent.md>) · `case-studies` · langchain
  Case study of building LangChain's GTM agent, covering workflow design, tool use, and production iteration.
- **2026-03-05** — [Evaluating Skills](<../evals-observability/evaluation/Evaluating Skills.md>) · `evaluation` · langchain
  Explains how to evaluate agent skills as reusable capabilities, with tests that isolate skill behavior from the full agent loop.
- **2026-03-02** — [How to Evaluate Tool-Calling Agents](<../evals-observability/evaluation/How to Evaluate Tool-Calling Agents.md>) · `evaluation` · arize
  Covers evaluation methods for tool-calling agents, including how to assess action selection and tool-use correctness.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<../evals-observability/monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<../evals-observability/tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-26** — [Evaluating AI Agent Skills](<../evals-observability/evaluation/Evaluating AI Agent Skills.md>) · `evaluation` · langfuse
  Explains how to evaluate AI agent skills, including task design, scoring, trace inspection, and regression testing for reusable agent capabilities.
- **2026-02-26** — [Agent Observability: How to Monitor and Evaluate LLM Agents in Production](<../evals-observability/monitoring/Agent Observability How to Monitor and Evaluate LLM Agents in Production.md>) · `monitoring` · langchain
  Guide to monitoring and evaluating LLM agents in production, including traces, feedback, evals, and alerting signals.
- **2026-02-23** — [Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems](<../rag-retrieval/pipelines/Mastering Production RAG with Google ADK and Arize AX for Enterprise Knowledge Systems.md>) · `pipelines` · arize
  Explains production RAG architecture with Google ADK and Arize AX, including agentic retrieval and evaluation concerns.
- **2026-02-23** — [Directory Snapshots: Resumable project state for Sandboxes](<../infra-platform/deployment/Directory Snapshots Resumable project state for Sandboxes.md>) · `deployment` · modal
  Introduces directory snapshots for sandbox state, enabling resumable project files across agent and remote-execution sessions.
- **2026-02-20** — [AI Agent Observability, Tracing & Evaluation with Langfuse](<../evals-observability/tracing/AI Agent Observability, Tracing & Evaluation with Langfuse.md>) · `tracing` · langfuse
  Guide to observability for AI agents, covering traces, spans, tool calls, evaluations, and debugging workflows for agentic systems.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<../evals-observability/tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-17** — [Inside Typeform’s AI Agent Stack](<../product-engineering/case-studies/Inside Typeform’s AI Agent Stack.md>) · `case-studies` · arize
  Case study of Typeform’s AI agent stack, useful for understanding production architecture choices in agent applications.
- **2026-02-16** — [Using Agent Skills to Automatically Improve your Prompts](<../prompt-engineering/techniques/Using Agent Skills to Automatically Improve your Prompts.md>) · `techniques` · langfuse
  Shows how agent skills can automatically improve prompts, using evaluation feedback and reusable agent workflows to iterate on prompt quality.
- **2026-02-11** — [Shell + Skills + Compaction: Tips for long-running agents that do real work | OpenAI Developers](<tool-use/Shell + Skills + Compaction Tips for long-running agents that do real work OpenAI Developers.md>) · `tool-use` · openai-devs
  Nonobvious patterns for three new Responses API primitives for long-running agents — skills (on-demand SKILL.md playbooks), the hosted/local shell tool, and server-side compaction that auto-compresses conversation history — drawn from Codex internals and Glean's production use.
- **2026-01-29** — [Hierarchical Memory Management In Agent Harnesses](<memory-context/Hierarchical Memory Management In Agent Harnesses.md>) · `memory-context` · arize
  Explains hierarchical memory management patterns for agent harnesses, including how state is organized across short and long horizons.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<../evals-observability/monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-29** — [OWASP Top 10 for Agentic Applications: Compliance Guide](<../product-engineering/security/OWASP Top 10 for Agentic Applications Compliance Guide.md>) · `security` · arize
  Maps OWASP risks to agentic applications and explains compliance-oriented controls for agent systems.
- **2026-01-28** — [Context Management for Deep Agents](<memory-context/Context Management for Deep Agents.md>) · `memory-context` · langchain
  Explains context management for Deep Agents, including what information to retain, retrieve, summarize, or isolate during long-running tasks.
- **2026-01-28** — [How to Debug & Evaluate AI Agents with Observability — LangChain Guide](<../evals-observability/tracing/How to Debug & Evaluate AI Agents with Observability — LangChain Guide.md>) · `tracing` · langchain
  Guide to debugging and evaluating AI agents with observability, using traces to inspect tool calls, intermediate steps, and failure modes.
- **2026-01-26** — [DSGym: A holistic framework for evaluating and training data science agents](<../evals-observability/evaluation/DSGym A holistic framework for evaluating and training data science agents.md>) · `evaluation` · together
  Introduces DSGym for evaluating and training data science agents.
- **2026-01-22** — [Testing Agent Skills Systematically with Evals | OpenAI Developers](<../evals-observability/evaluation/Testing Agent Skills Systematically with Evals OpenAI Developers.md>) · `evaluation` · openai-devs
  Pattern for evaluating Codex agent skills like lightweight end-to-end tests: define outcome/process/style/efficiency success criteria first, capture run traces and artifacts, then combine deterministic checks (did it run npm install, create package.json) with rubric-based grading to catch regressions.
- **2026-01-22** — [How Observability-Driven Sandboxing Secures AI Agents](<../product-engineering/security/How Observability-Driven Sandboxing Secures AI Agents.md>) · `security` · arize
  Explains how sandbox telemetry and observability can harden AI agents that execute code or use external tools.
- **2026-01-21** — [AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)](<tool-use/AI Agent interfaces In 2026 Filesystem vs API vs Database (What Actually Works).md>) · `tool-use` · arize
  Compares filesystem, API, and database interfaces for agents, using memory benchmarks and practical interface tradeoffs to evaluate what works in production.
- **2026-01-11** — [Supercharging Codex with JetBrains MCP at Skyscanner | OpenAI Developers](<../product-engineering/case-studies/Supercharging Codex with JetBrains MCP at Skyscanner OpenAI Developers.md>) · `case-studies` · openai-devs
  Skyscanner wires Codex CLI to the JetBrains MCP server so the agent gets IDE feedback loops: get_file_problems surfaced a non-compiling Databricks SDK NotFound constructor immediately instead of after a test run, cutting iteration time.
- **2026-01-09** — [Demystifying evals for AI agents](<../evals-observability/evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2026-01-01** — [How Graphite builds reliable AI code review at scale](<../product-engineering/case-studies/How Graphite builds reliable AI code review at scale.md>) · `case-studies` · braintrust
  Case study of Graphite building reliable AI code review at scale, with evaluation and workflow design for production developer tooling.
- **2025-12-10** — [Best Practices for Multi-Turn RL](<../models/reinforcement-learning/Best Practices for Multi-Turn RL.md>) · `reinforcement-learning` · fireworks
  Covers best practices for multi-turn reinforcement learning, including environment design and reward structure.
- **2025-12-03** — [Evaluating Deep Agents: Our Learnings](<../evals-observability/evaluation/Evaluating Deep Agents Our Learnings.md>) · `evaluation` · langchain
  Shares lessons from evaluating Deep Agents, including task design, traces, scoring, and how agent architectures change eval needs.
- **2025-12-01** — [AWS Bedrock AgentCore Observability with Arize AX: Operationalizing AI Agents At Scale](<../evals-observability/tracing/AWS Bedrock AgentCore Observability with Arize AX Operationalizing AI Agents At Scale.md>) · `tracing` · arize
  Walks through operationalizing AWS Bedrock AgentCore agents with Arize AX observability, focusing on traces, evaluation, and production-scale monitoring.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-25** — [Vibe Coding a Custom Annotation UI](<../product-engineering/ux-patterns/Vibe Coding a Custom Annotation UI.md>) · `ux-patterns` · langfuse
  Case study of building a custom annotation UI for eval workflows with AI-assisted coding, highlighting review ergonomics and human feedback collection.
- **2025-11-20** — [Eval Protocol: RL on your agents, in any environment](<../models/reinforcement-learning/Eval Protocol RL on your agents, in any environment.md>) · `reinforcement-learning` · fireworks
  Describes using Eval Protocol to run reinforcement learning on agents in task environments.
- **2025-11-20** — [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](<../prompt-engineering/context-engineering/CLAUDE.md Best Practices Learned from Optimizing Claude Code with Prompt Learning.md>) · `context-engineering` · arize
  Extracts CLAUDE.md best practices from prompt-learning experiments that optimized Claude Code behavior through repository instructions.
- **2025-11-20** — [Agents need good developer experience too](<../product-engineering/architecture/Agents need good developer experience too.md>) · `architecture` · modal
  Argues that agent systems need strong developer experience, covering observability, iteration loops, deployment ergonomics, and tool surfaces.
- **2025-11-18** — [Evaluating and Improving AI Agents at Scale with Microsoft Foundry](<../evals-observability/evaluation/Evaluating and Improving AI Agents at Scale with Microsoft Foundry.md>) · `evaluation` · arize
  Guide to evaluating and improving production AI agents at scale with Microsoft Foundry and Arize workflows.
- **2025-11-14** — [Tracing, Evaluation, and Observability for Google ADK (How To)](<../evals-observability/tracing/Tracing, Evaluation, and Observability for Google ADK (How To).md>) · `tracing` · arize
  How-to guide for tracing, evaluating, and observing Google ADK agents in production-style workflows.
- **2025-11-10** — [Fireworks RFT: Build AI agents with fine-tuned open models that outperform frontier closed models](<../models/reinforcement-learning/Fireworks RFT Build AI agents with fine-tuned open models that outperform frontier closed models.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement fine-tuning for building agent models that can outperform closed frontier models on target tasks.
- **2025-11-06** — [Systematic Evaluation of AI Agents](<../evals-observability/evaluation/Systematic Evaluation of AI Agents.md>) · `evaluation` · langfuse
  Covers systematic evaluation of AI agents, focusing on experiment interpretation, failure analysis, and how to compare agent variants.
- **2025-10-31** — [Genspark deep research agent with Fireworks RFT](<../models/reinforcement-learning/Genspark deep research agent with Fireworks RFT.md>) · `reinforcement-learning` · fireworks
  Case study of reinforcement fine-tuning a deep research agent to improve quality, tool calls, and cost.
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<../evals-observability/monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<../product-engineering/security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-10-17** — [When to Use What: A Practical Guide to AI Agent Testing and Evaluation](<../evals-observability/testing/When to Use What A Practical Guide to AI Agent Testing and Evaluation.md>) · `testing` · cresta
  Practical guide for choosing AI agent testing and evaluation methods based on deployment stage and risk.
- **2025-10-10** — [How Codex ran OpenAI DevDay 2025](<../product-engineering/case-studies/How Codex ran OpenAI DevDay 2025.md>) · `case-studies` · openai-devs
  Behind-the-scenes account of OpenAI using Codex to build DevDay 2025: it implemented the 1990s VISCA protocol to control venue cameras, built an MCP server for stage lighting, and used Codex Cloud best-of-N to iterate Apps SDK demos like a beat pad in parallel.
- **2025-10-09** — [Evaluating Multi-Turn Conversations](<../evals-observability/evaluation/Evaluating Multi-Turn Conversations.md>) · `evaluation` · langfuse
  Explains how to evaluate multi-turn conversations, including context retention, conversation-level scoring, and stateful failure modes.
- **2025-10-07** — [AI-Ready Knowledge for Contact Centers: Closing the Gap Between the Knowledge Base and AI](<../rag-retrieval/pipelines/AI-Ready Knowledge for Contact Centers Closing the Gap Between the Knowledge Base and AI.md>) · `pipelines` · cresta
  Explains how operational knowledge bases need to be structured for AI agents, with emphasis on grounding and retrieval readiness.
- **2025-09-29** — [Effective context engineering for AI agents](<../prompt-engineering/context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-09-11** — [Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith](<../product-engineering/case-studies/Monte Carlo Building Data + AI Observability Agents with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Monte Carlo case study on building data and AI observability agents with LangGraph and LangSmith.
- **2025-09-09** — [Orchestrator-Worker Agents: A Practical Comparison of Common Agent Frameworks](<multi-agent/Orchestrator-Worker Agents A Practical Comparison of Common Agent Frameworks.md>) · `multi-agent` · arize
  Compares orchestrator-worker agent frameworks and clarifies when this multi-agent pattern is useful.
- **2025-08-25** — [LLM Eval Driven Development with Claude Code](<../evals-observability/evaluation/LLM Eval Driven Development with Claude Code.md>) · `evaluation` · fireworks
  Explains eval-driven development with Claude Code, using tests and feedback loops to improve coding-agent behavior.
- **2025-08-19** — [The rise of async programming](<../product-engineering/architecture/The rise of async programming.md>) · `architecture` · braintrust
  Explains why asynchronous programming patterns matter for long-running AI workflows, background jobs, agent tasks, and responsive product experiences.
- **2025-08-14** — [Test-driven agent development](<../evals-observability/testing/Test-driven agent development.md>) · `testing` · fireworks
  Shows a TDD-style workflow for building agents with concrete acceptance tests, red teaming, and regression checks.
- **2025-08-07** — [The canonical agent architecture: A while loop with tools](<planning/The canonical agent architecture A while loop with tools.md>) · `planning` · braintrust
  Frames the canonical agent architecture as a while loop around model calls, tool use, state updates, and termination criteria for controllable agent behavior.
- **2025-07-17** — [Back to The Future: Evaluating AI Agents on Predicting Future Events](<../evals-observability/evaluation/Back to The Future Evaluating AI Agents on Predicting Future Events.md>) · `evaluation` · together
  Introduces FutureBench for evaluating agents on predicting future events.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<../product-engineering/ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-06-16** — [How and when to build multi-agent systems](<multi-agent/How and when to build multi-agent systems.md>) · `multi-agent` · langchain
  Guidance on when multi-agent systems are warranted and how to design agent roles, coordination, and boundaries.
- **2025-06-12** — [From Zero to One: Building An Autonomous and Open Data Scientist Agent from Scratch](<planning/From Zero to One Building An Autonomous and Open Data Scientist Agent from Scratch.md>) · `planning` · together
  Walkthrough of building an autonomous open data-scientist agent from scratch.
- **2025-05-28** — [Mixture-of-Agents Alignment for post-training](<../models/fine-tuning/Mixture-of-Agents Alignment for post-training.md>) · `fine-tuning` · together
  Explains Mixture-of-Agents Alignment for improving post-training with collective model intelligence.
- **2025-05-21** — [Building an open-source Browser Agent on Fireworks AI](<computer-use/Building an open-source Browser Agent on Fireworks AI.md>) · `computer-use` · fireworks
  Walkthrough of building an open-source browser agent, including model choice, tool execution, and environment control.
- **2025-05-19** — [Agentic AI Systems](<planning/Agentic AI Systems.md>) · `planning` · fireworks
  Overview of agentic AI systems, covering planning, tool use, control loops, and production architecture concerns.
- **2025-04-24** — [How we use LLMs to build and scale Langfuse](<../product-engineering/case-studies/How we use LLMs to build and scale Langfuse.md>) · `case-studies` · langfuse
  Case study of how Langfuse uses LLMs internally to build and scale the product, including practical workflows for AI-assisted engineering and operations.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<../evals-observability/tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-04-09** — [Embracing Google's Agent-To-Agent (A2A) Protocol](<multi-agent/Embracing Google's Agent-To-Agent (A2A) Protocol.md>) · `multi-agent` · arize
  Discusses Google's Agent-to-Agent protocol and why interoperability standards matter for multi-agent systems and production agent ecosystems.
- **2025-03-19** — [Comparing Open-Source AI Agent Frameworks](<planning/Comparing Open-Source AI Agent Frameworks.md>) · `planning` · langfuse
  Compares open-source AI agent frameworks and their architecture tradeoffs around orchestration, tools, memory, extensibility, and production readiness.
- **2025-03-18** — [Our Own Zero to One: Lessons Learned in Building The Brinks Home AI Agent](<../product-engineering/case-studies/Our Own Zero to One Lessons Learned in Building The Brinks Home AI Agent.md>) · `case-studies` · cresta
  Production case study on building an AI agent from zero to one, with lessons about scope, rollout, and operational constraints.
- **2025-02-20** — [The Agent Deep Dive: David Zhang’s Open Deep Research](<planning/The Agent Deep Dive David Zhang’s Open Deep Research.md>) · `planning` · langfuse
  Deep dive on Open Deep Research as an agentic system, covering planning, tool use, research workflows, and trace-based inspection.
- **2025-02-18** — [How to Build An AI Agent](<planning/How to Build An AI Agent.md>) · `planning` · arize
  Practical guide to building an AI agent, covering planning, tools, state, and reliability considerations.
- **2025-02-05** — [Understanding Agentic RAG](<../rag-retrieval/pipelines/Understanding Agentic RAG.md>) · `pipelines` · arize
  Explains agentic RAG and how agents change retrieval planning, tool use, and synthesis workflows.
- **2025-01-31** — [Best Practices for Building an Agent Router](<planning/Best Practices for Building an Agent Router.md>) · `planning` · arize
  Explains agent-router design as a decision layer that routes user requests to the right tools, services, or actions in larger agent systems.
- **2025-01-22** — [Evaluating and Monitoring Voice AI Agents](<../models/multimodal/Evaluating and Monitoring Voice AI Agents.md>) · `multimodal` · langfuse
  Covers evaluation and monitoring for voice AI agents, including speech-specific quality signals and agent behavior beyond text-only evals.
- **2025-01-07** — [Agents](<planning/Agents.md>) · `planning` · chip-huyen
  Framework for foundation-model agents covering environments, tools, planning, action selection, failure modes, and evaluation for multi-step agentic applications.
- **2025-01-06** — [Claude SWE-Bench Performance](<../models/benchmarks/Claude SWE-Bench Performance.md>) · `benchmarks` · anthropic-engineering
  How Anthropic scaffolded Claude 3.5 Sonnet to 49% on SWE-bench Verified with a minimal agent harness, detailing tool design and error analysis.
- **2024-11-25** — [Fine-Tuning LLMs for Multi-Turn Conversations: A Technical Deep Dive](<../models/fine-tuning/Fine-Tuning LLMs for Multi-Turn Conversations A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into fine-tuning LLMs for multi-turn conversations.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<../evals-observability/evaluation/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `evaluation` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-10-16** — [Comparing OpenAI Swarm with other Multi Agent Frameworks](<multi-agent/Comparing OpenAI Swarm with other Multi Agent Frameworks.md>) · `multi-agent` · arize
  Compares OpenAI Swarm with other multi-agent frameworks, highlighting orchestration patterns and framework tradeoffs.
- **2024-10-16** — [Tracing and Evaluating LangGraph Agents](<../evals-observability/tracing/Tracing and Evaluating LangGraph Agents.md>) · `tracing` · arize
  Covers tracing and evaluation patterns for LangGraph agents, linking graph-based control flow with observability.
- **2024-10-07** — [Observability in Multi-Step LLM Systems](<../evals-observability/tracing/Observability in Multi-Step LLM Systems.md>) · `tracing` · langfuse
  Explains observability needs for multi-step LLM systems, including tracing chains, tools, intermediate state, and failure points across complex application flows.
- **2024-10-03** — [Building AI Assistants with Vectara-agentic and Arize](<../rag-retrieval/pipelines/Building AI Assistants with Vectara-agentic and Arize.md>) · `pipelines` · arize
  Shows how to build AI assistants with Vectara-agentic and Arize, tying retrieval, agent tools, and observability together.
- **2024-09-26** — [Pushing LangSmith to new limits with Replit Agent's complex workflows](<../product-engineering/case-studies/Pushing LangSmith to new limits with Replit Agent's complex workflows.md>) · `case-studies` · langchain
  Replit Agent case study on tracing and managing complex agent workflows with LangSmith.
- **2024-09-12** — [How to build function calling and JSON mode for open-source and fine-tuned LLMs](<../prompt-engineering/structured-output/How to build function calling and JSON mode for open-source and fine-tuned LLMs.md>) · `structured-output` · baseten
  Shows how to build function calling and JSON mode for open-source and fine-tuned LLMs.
- **2024-08-08** — [LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents](<planning/LlamaIndex Workflows Navigating a New Way To Build Cyclical Agents.md>) · `planning` · arize
  Explains LlamaIndex Workflows as a pattern for building cyclical agents with explicit control flow.
- **2024-08-06** — [Compound AI systems explained](<../product-engineering/architecture/Compound AI systems explained.md>) · `architecture` · baseten
  Explains compound AI systems and how multiple models, tools, and control logic combine into applications.
- **2024-07-30** — [Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant](<../product-engineering/case-studies/Developing Copilot What AI Engineers Can Learn from Our Experience Building An AI Assistant.md>) · `case-studies` · arize
  Arize Copilot case study covering lessons from building an AI assistant for data scientists and AI engineers.
- **2024-07-02** — [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](<../rag-retrieval/search/Improving Memory Retrieval How New Computer achieved 50% higher recall with LangSmith.md>) · `search` · langchain
  New Computer case study on improving memory retrieval recall with LangSmith-backed evaluation and debugging.
- **2024-07-02** — [Building multi-component AI workflows at scale with Chains](<../product-engineering/architecture/Building multi-component AI workflows at scale with Chains.md>) · `architecture` · baseten
  Explains multi-component AI workflows with Chains, including orchestration across model and application steps.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<../inference/optimization/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `optimization` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-03-14** — [What I learned from looking at 900 most popular open source AI tools](<../industry/trends/What I learned from looking at 900 most popular open source AI tools.md>) · `trends` · chip-huyen
  Maps 900 open-source AI tools into infrastructure, model-development, and application-development layers, highlighting growth in agents, prompt engineering, vector search, evaluation, and inference tooling.
- **2024-02-20** — [Why do all LLMs need structured output modes?](<../prompt-engineering/structured-output/Why do all LLMs need structured output modes.md>) · `structured-output` · fireworks
  Explains why structured-output modes matter for reliable LLM applications and tool-calling systems.
- **2024-02-18** — [The Shift from Models to Compound AI Systems](<../product-engineering/architecture/The Shift from Models to Compound AI Systems.md>) · `architecture` · arize
  Explains the shift from standalone models to compound AI systems that combine models, retrieval, tools, orchestration, and evaluation into production applications.
- **2024-01-31** — [Function calling and JSON mode](<../prompt-engineering/structured-output/Function calling and JSON mode.md>) · `structured-output` · together
  Explains function calling and JSON mode for structured LLM application outputs.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<../evals-observability/evaluation/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `evaluation` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-06-20** — [Voyager: An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion](<planning/Voyager An Open-Ended Embodied Agent with LLMs Paper Reading and Discussion.md>) · `planning` · arize
  Paper-reading summary of Voyager as an open-ended embodied agent using LLM-driven skills and exploration.
- **2023-04-28** — [Lessons From Building an Early ChatGPT Plugin In Under 24 Hours](<../product-engineering/case-studies/Lessons From Building an Early ChatGPT Plugin In Under 24 Hours.md>) · `case-studies` · arize
  Retrospective on building an early ChatGPT plugin quickly, including product workflow lessons and integration constraints from the plugin ecosystem.
- **2021-01-13** — [Action Directed GPT-2](<../models/reasoning/Action Directed GPT-2.md>) · `reasoning` · cresta
  Explains Action Directed GPT-2 as an early pattern for steering language model behavior toward actions, relevant to tool-using and task-oriented agents.
- **2017-06-12** — **[Paper]** [Attention Is All You Need](<../models/architectures/[Paper] Attention Is All You Need.md>) · `architectures` · arxiv
  Introduces the Transformer: a sequence model built purely on multi-head self-attention with no recurrence or convolution, hitting 28.4 BLEU on WMT14 EN-DE while training in 3.5 days on 8 GPUs. The architecture every modern LLM descends from.
