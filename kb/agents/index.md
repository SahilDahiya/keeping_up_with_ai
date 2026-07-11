# agents

33 articles.

- **2026-07-10** — [3 production patterns for AI agents and how to evaluate each one](<planning/3 production patterns for AI agents and how to evaluate each one.md>) · `planning` · arize
  Breaks production agents into local coding agents, in-app assistants, and operational agents, then maps each pattern to different harness, rollout, and evaluation needs.
- **2026-05-28** — [Claude Code: Best practices for agentic coding](<tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-04-30** — [Agents can now create Cloudflare accounts, buy domains, and deploy](<tool-use/Agents can now create Cloudflare accounts, buy domains, and deploy.md>) · `tool-use` · cloudflare-ai
  Via a protocol co-designed with Stripe for Stripe Projects, coding agents can now provision a Cloudflare account, start a paid subscription, register a domain, and receive an API token to deploy — end-to-end with humans only approving payment and terms of service.
- **2026-04-28** — [Context management in agent harnesses: memory, files, and subagents](<memory-context/Context management in agent harnesses memory, files, and subagents.md>) · `memory-context` · arize
  Detailed guide to context management in agent harnesses, including memory, files, subagents, and strategies for working within context limits.
- **2026-04-20** — [Orchestrating AI Code Review at scale](<multi-agent/Orchestrating AI Code Review at scale.md>) · `multi-agent` · cloudflare-ai
  Deep dive into Cloudflare's CI-native AI code review built on OpenCode: up to seven specialized reviewer agents (security, performance, quality, docs, compliance) plus a coordinator that deduplicates findings and posts one structured review, run across tens of thousands of GitLab merge requests via a plugin architecture.
- **2026-04-14** — [Building smarter AI agents: architecture, evals, and lessons from the field](<planning/Building smarter AI agents architecture, evals, and lessons from the field.md>) · `planning` · arize
  Summarizes field lessons on production agent architecture, evaluation, and reliability from AI Builders events.
- **2026-03-24** — [Harness design for long-running application development](<planning/Harness design for long-running application development.md>) · `planning` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-03-10** — [Arize Skills: Coding Agent Workflows for Traces, Evals, and Instrumentation](<tool-use/Arize Skills Coding Agent Workflows for Traces, Evals, and Instrumentation.md>) · `tool-use` · arize
  Introduces Arize Skills for coding agents, enabling workflows around trace extraction, evals, and instrumentation from agentic development environments.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-03-04** — [From UI to Terminal: Bringing Alyx's Superpowers Into Your Coding Agent](<tool-use/From UI to Terminal Bringing Alyx's Superpowers Into Your Coding Agent.md>) · `tool-use` · arize
  Introduces an AX CLI preview that brings Alyx-style trace and eval workflows into terminal-based coding-agent loops.
- **2026-02-26** — [Building frontend UIs with Codex and Figma | OpenAI Developers](<tool-use/Building frontend UIs with Codex and Figma OpenAI Developers.md>) · `tool-use` · openai-devs
  Announces bidirectional Codex-Figma integration via the Figma MCP server: get_design_context extracts layouts/styles/components from Figma frames for code generation, and generate_figma_design turns a running UI back into editable Figma frames.
- **2026-02-24** — [Alyx 2.0: The AI Agent That Actually Plans](<planning/Alyx 2.0 The AI Agent That Actually Plans.md>) · `planning` · arize
  Introduces Alyx 2.0 as an agent that plans over observability workflows, covering product design lessons from building a more capable AI analyst.
- **2026-02-23** — [Run long horizon tasks with Codex | OpenAI Developers](<planning/Run long horizon tasks with Codex OpenAI Developers.md>) · `planning` · openai-devs
  Stress test of long-horizon agentic coding: GPT-5.3-Codex at Extra High reasoning ran ~25 hours uninterrupted, consuming ~13M tokens and generating ~30k lines to build a design tool from a blank repo, framed by METR's ~7-month doubling time for agent task horizons.
- **2026-02-11** — [CUGA Agent: From Benchmarks to Business Impact of IBM's Generalist Agent](<planning/CUGA Agent From Benchmarks to Business Impact of IBM's Generalist Agent.md>) · `planning` · arize
  Brief paper-reading note on IBM's CUGA generalist agent, connecting benchmark performance to business impact.
- **2026-02-11** — [Shell + Skills + Compaction: Tips for long-running agents that do real work | OpenAI Developers](<tool-use/Shell + Skills + Compaction Tips for long-running agents that do real work OpenAI Developers.md>) · `tool-use` · openai-devs
  Nonobvious patterns for three new Responses API primitives for long-running agents — skills (on-demand SKILL.md playbooks), the hosted/local shell tool, and server-side compaction that auto-compresses conversation history — drawn from Codex internals and Glean's production use.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2026-01-21** — [AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)](<tool-use/AI Agent interfaces In 2026 Filesystem vs API vs Database (What Actually Works).md>) · `tool-use` · arize
  Compares filesystem, API, and database interfaces for agents, using memory benchmarks and practical interface tradeoffs to evaluate what works in production.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-24** — [Introducing advanced tool use on the Claude Developer Platform](<tool-use/Introducing advanced tool use on the Claude Developer Platform.md>) · `tool-use` · anthropic-engineering
  Introduces tool search, programmatic tool calling, and tool-use examples on the Claude Developer Platform to scale agents past context-window limits on large tool sets.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-09-22** — [Why we built the Responses API | OpenAI Developers](<tool-use/Why we built the Responses API OpenAI Developers.md>) · `tool-use` · openai-devs
  OpenAI's design rationale for the Responses API as an agentic loop unifying Chat Completions and Assistants: it preserves reasoning state across turns (+5% on TAUBench, better cache utilization) and emits multiple output items — tool calls, structured outputs, intermediate steps — not just the final message.
- **2025-09-11** — [Writing effective tools for AI agents—using AI agents](<tool-use/Writing effective tools for AI agents—using AI agents.md>) · `tool-use` · anthropic-engineering
  Guidance on designing tool interfaces agents use reliably—consolidating workflows, namespacing, returning meaningful context—and using Claude to optimize its own tools.
- **2025-08-28** — [Claude Code vs Cursor: A Power-User’s Playbook](<tool-use/Claude Code vs Cursor A Power-User’s Playbook.md>) · `tool-use` · arize
  Compares Claude Code and Cursor from a power-user workflow perspective, focusing on coding-agent interfaces and usage patterns.
- **2025-06-13** — [How we built our multi-agent research system](<multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-04-09** — [Embracing Google's Agent-To-Agent (A2A) Protocol](<multi-agent/Embracing Google's Agent-To-Agent (A2A) Protocol.md>) · `multi-agent` · arize
  Discusses Google's Agent-to-Agent protocol and why interoperability standards matter for multi-agent systems and production agent ecosystems.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2025-01-31** — [Best Practices for Building an Agent Router](<planning/Best Practices for Building an Agent Router.md>) · `planning` · arize
  Explains agent-router design as a decision layer that routes user requests to the right tools, services, or actions in larger agent systems.
- **2024-12-19** — [Building Effective AI Agents](<planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
- **2024-12-04** — [AI Agent Workflows and Architectures Masterclass](<planning/AI Agent Workflows and Architectures Masterclass.md>) · `planning` · arize
  Introduces practical agent workflow and architecture patterns, emphasizing simple tool-calling loops and design choices over vague autonomy claims.
- **2024-12-03** — [Building an AI Agent that Thrives in the Real World](<planning/Building an AI Agent that Thrives in the Real World.md>) · `planning` · arize
  Practical guidance for building production AI agents that survive real-world failures through monitoring, iteration, and reliability practices.
- **2024-10-16** — [Comparing OpenAI Swarm with other Multi Agent Frameworks](<multi-agent/Comparing OpenAI Swarm with other Multi Agent Frameworks.md>) · `multi-agent` · arize
  Compares OpenAI Swarm with other multi-agent frameworks, highlighting orchestration patterns and framework tradeoffs.
- **2024-09-30** — [Arize AI + MongoDB: Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems](<memory-context/Arize AI + MongoDB Leveraging Agent Evaluation and Memory to Build Robust Agentic Systems.md>) · `memory-context` · arize
  Explains how Arize and MongoDB combine agent evaluation and memory patterns for more robust agentic systems.

## Also relevant (filed elsewhere)

- **2026-07-08** — [The agent is the user now: lessons from the founder of WorkOS](<../product-engineering/security/The agent is the user now lessons from the founder of WorkOS.md>) · `security` · arize
  Interview-driven discussion of agents as users, covering identity, permissions, memory, evals, and feedback loops as core production-agent infrastructure.
- **2026-06-26** — [Making private MCP servers reachable without making them public | OpenAI Developers](<../product-engineering/security/Making private MCP servers reachable without making them public OpenAI Developers.md>) · `security` · openai-devs
  Engineering design of OpenAI's Secure MCP Tunnel: a customer-run open-source client beside a private MCP server opens outbound-only HTTPS to OpenAI, forwarding MCP requests (including streaming and auth flows) so ChatGPT/Codex can reach the server without public endpoints, VPNs, or third-party tunnels.
- **2026-06-19** — [Temporary Cloudflare Accounts for AI agents](<../infra-platform/deployment/Temporary Cloudflare Accounts for AI agents.md>) · `deployment` · cloudflare-ai
  Temporary Cloudflare Accounts let agents run 'wrangler deploy --temporary' to ship a Worker with zero signup — a 60-minute claimable account with auto-provisioned API token — with Wrangler itself prompting agents about the flag, removing human-built OAuth/dashboard friction from the deploy loop.
- **2026-06-18** — [Build your own vulnerability harness](<../product-engineering/security/Build your own vulnerability harness.md>) · `security` · cloudflare-ai
  How Cloudflare grew a ~450-line security-audit skill into a model-agnostic, fleet-wide vulnerability-scanning harness: parallel recon agents, per-attack-class Hunter agents, adversarial validators, schema-checked findings.json, and independent re-verification, with different models cross-testing discovery vs. validation.
- **2026-06-17** — [Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue](<../infra-platform/deployment/Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue.md>) · `deployment` · cloudflare-ai
  Describes a three-layer production agent stack — framework (Flue, from the Astro team, built on the Pi harness), harness (Project Think, Pi), and runtime (Cloudflare Agents SDK) — with durable execution, dynamic code execution, and a durable filesystem exposed to any harness.
- **2026-06-04** — [Building the AI factory for self-improving agents: What’s new in Arize AX](<../evals-observability/monitoring/Building the AI factory for self-improving agents What’s new in Arize AX.md>) · `monitoring` · arize
  Introduces Arize AX updates aimed at building an AI factory for self-improving agents through traces, evals, and feedback loops.
- **2026-05-28** — [How we built Cloudflare's data platform and an AI agent on top of it](<../product-engineering/architecture/How we built Cloudflare's data platform and an AI agent on top of it.md>) · `architecture` · cloudflare-ai
  How Cloudflare built Town Lake, a single-SQL-interface data platform on R2/Workers/Workflows unifying Postgres, ClickHouse, Kafka, and BigQuery sprawl (1B+ events/sec), and Skipper, an AI agent on top that answers plain-English questions with auditable queries and PII-aware governance.
- **2026-05-25** — [How we contain Claude across products](<../product-engineering/security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-05-13** — [How we use Alyx to build Alyx: How to build an AI agent feedback loop](<../evals-observability/monitoring/How we use Alyx to build Alyx How to build an AI agent feedback loop.md>) · `monitoring` · arize
  Describes how Arize uses Alyx to improve Alyx through a feedback loop that captures failures, analyzes traces, and routes product improvements back into the agent.
- **2026-05-01** — [Why agent telemetry needs standards](<../evals-observability/tracing/Why agent telemetry needs standards.md>) · `tracing` · arize
  Argues for standard agent telemetry schemas so teams can reconstruct tool calls, model hops, context use, and handoffs across production agent systems.
- **2026-04-28** — [Context management in agent harnesses: memory, files, and subagents](<memory-context/Context management in agent harnesses memory, files, and subagents.md>) · `memory-context` · arize
  Detailed guide to context management in agent harnesses, including memory, files, subagents, and strategies for working within context limits.
- **2026-04-23** — [Beyond models: How context and evals make agents work in production](<../evals-observability/evaluation/Beyond models How context and evals make agents work in production.md>) · `evaluation` · arize
  Explains why production agents depend on context quality and eval loops, not just model choice, and outlines how to evaluate behavior on real workflows.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<../product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-03-22** — [100 AI Agents Per Employee: The Enterprise Governance Gap](<../product-engineering/security/100 AI Agents Per Employee The Enterprise Governance Gap.md>) · `security` · arize
  Argues that enterprises adopting large populations of AI agents need governance for permissions, ownership, auditability, and lifecycle management before agent scale outpaces human oversight.
- **2026-03-11** — [From prompts to products: One year of Responses | OpenAI Developers](<../product-engineering/case-studies/From prompts to products One year of Responses OpenAI Developers.md>) · `case-studies` · openai-devs
  One-year retrospective on the Responses API told through five developer stories, including Raindrop AI's production agent-monitoring platform (failure detection and debugging on GPT-5.2 via the Vercel AI SDK) built on its hosted-tool and background-analysis primitives.
- **2026-02-27** — [Best AI Observability Tools for Autonomous Agents in 2026](<../evals-observability/monitoring/Best AI Observability Tools for Autonomous Agents in 2026.md>) · `monitoring` · arize
  Survey of AI observability tools for autonomous agents, emphasizing monitoring failure modes specific to tool use, autonomy, and production traces.
- **2026-02-27** — [Add Observability to Your Open Agent Spec Agents with Arize Phoenix](<../evals-observability/tracing/Add Observability to Your Open Agent Spec Agents with Arize Phoenix.md>) · `tracing` · arize
  Shows how to add Phoenix tracing and observability to Open Agent Specification agents so portable agent runtimes can still be debugged in production.
- **2026-02-17** — [Closing the Loop: Coding Agents, Telemetry, and the Path to Self-Improving Software](<../evals-observability/tracing/Closing the Loop Coding Agents, Telemetry, and the Path to Self-Improving Software.md>) · `tracing` · arize
  Argues that coding-agent telemetry can close the loop toward self-improving software by capturing agent behavior, failures, and feedback.
- **2026-02-11** — [Shell + Skills + Compaction: Tips for long-running agents that do real work | OpenAI Developers](<tool-use/Shell + Skills + Compaction Tips for long-running agents that do real work OpenAI Developers.md>) · `tool-use` · openai-devs
  Nonobvious patterns for three new Responses API primitives for long-running agents — skills (on-demand SKILL.md playbooks), the hosted/local shell tool, and server-side compaction that auto-compresses conversation history — drawn from Codex internals and Glean's production use.
- **2026-01-29** — [Why AI Agents Break: A Field Analysis of Production Failures](<../evals-observability/monitoring/Why AI Agents Break A Field Analysis of Production Failures.md>) · `monitoring` · arize
  Field analysis of production AI-agent failures, covering common operational failure modes and why fluent outputs can hide broken behavior.
- **2026-01-22** — [Testing Agent Skills Systematically with Evals | OpenAI Developers](<../evals-observability/evaluation/Testing Agent Skills Systematically with Evals OpenAI Developers.md>) · `evaluation` · openai-devs
  Pattern for evaluating Codex agent skills like lightweight end-to-end tests: define outcome/process/style/efficiency success criteria first, capture run traces and artifacts, then combine deterministic checks (did it run npm install, create package.json) with rubric-based grading to catch regressions.
- **2026-01-21** — [AI Agent interfaces In 2026: Filesystem vs API vs Database (What Actually Works)](<tool-use/AI Agent interfaces In 2026 Filesystem vs API vs Database (What Actually Works).md>) · `tool-use` · arize
  Compares filesystem, API, and database interfaces for agents, using memory benchmarks and practical interface tradeoffs to evaluate what works in production.
- **2026-01-11** — [Supercharging Codex with JetBrains MCP at Skyscanner | OpenAI Developers](<../product-engineering/case-studies/Supercharging Codex with JetBrains MCP at Skyscanner OpenAI Developers.md>) · `case-studies` · openai-devs
  Skyscanner wires Codex CLI to the JetBrains MCP server so the agent gets IDE feedback loops: get_file_problems surfaced a non-compiling Databricks SDK NotFound constructor immediately instead of after a test run, cutting iteration time.
- **2026-01-09** — [Demystifying evals for AI agents](<../evals-observability/evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-12-01** — [AWS Bedrock AgentCore Observability with Arize AX: Operationalizing AI Agents At Scale](<../evals-observability/tracing/AWS Bedrock AgentCore Observability with Arize AX Operationalizing AI Agents At Scale.md>) · `tracing` · arize
  Walks through operationalizing AWS Bedrock AgentCore agents with Arize AX observability, focusing on traces, evaluation, and production-scale monitoring.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-20** — [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](<../prompt-engineering/context-engineering/CLAUDE.md Best Practices Learned from Optimizing Claude Code with Prompt Learning.md>) · `context-engineering` · arize
  Extracts CLAUDE.md best practices from prompt-learning experiments that optimized Claude Code behavior through repository instructions.
- **2025-11-18** — [Evaluating and Improving AI Agents at Scale with Microsoft Foundry](<../evals-observability/evaluation/Evaluating and Improving AI Agents at Scale with Microsoft Foundry.md>) · `evaluation` · arize
  Guide to evaluating and improving production AI agents at scale with Microsoft Foundry and Arize workflows.
- **2025-10-30** — [Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo](<../evals-observability/monitoring/Building the Data Flywheel for Smarter AI Systems with Arize AX and NVIDIA NeMo.md>) · `monitoring` · arize
  Explains a data-flywheel approach for improving AI systems with Arize AX and NVIDIA NeMo, using production feedback to drive model and agent improvements.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<../product-engineering/security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-10-10** — [How Codex ran OpenAI DevDay 2025](<../product-engineering/case-studies/How Codex ran OpenAI DevDay 2025.md>) · `case-studies` · openai-devs
  Behind-the-scenes account of OpenAI using Codex to build DevDay 2025: it implemented the 1990s VISCA protocol to control venue cameras, built an MCP server for stage lighting, and used Codex Cloud best-of-N to iterate Apps SDK demos like a beat pad in parallel.
- **2025-09-29** — [Effective context engineering for AI agents](<../prompt-engineering/context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<../product-engineering/ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-04-10** — [Building and Deploying Observable AI Agents with Google Agent Framework and Arize](<../evals-observability/tracing/Building and Deploying Observable AI Agents with Google Agent Framework and Arize.md>) · `tracing` · arize
  Guide to building and deploying observable agents with Google Agent Framework and Arize, emphasizing traces for multi-agent and agentic workflows.
- **2025-04-09** — [Embracing Google's Agent-To-Agent (A2A) Protocol](<multi-agent/Embracing Google's Agent-To-Agent (A2A) Protocol.md>) · `multi-agent` · arize
  Discusses Google's Agent-to-Agent protocol and why interoperability standards matter for multi-agent systems and production agent ecosystems.
- **2025-03-18** — [Self-Improving Agents: Automating LLM Performance Optimization using Arize and NVIDIA NeMo](<../evals-observability/monitoring/Self-Improving Agents Automating LLM Performance Optimization using Arize and NVIDIA NeMo.md>) · `monitoring` · arize
  Describes using Arize with NVIDIA NeMo to automate LLM performance optimization and support self-improving agent workflows.
- **2025-01-31** — [Best Practices for Building an Agent Router](<planning/Best Practices for Building an Agent Router.md>) · `planning` · arize
  Explains agent-router design as a decision layer that routes user requests to the right tools, services, or actions in larger agent systems.
- **2025-01-06** — [Claude SWE-Bench Performance](<../models/benchmarks/Claude SWE-Bench Performance.md>) · `benchmarks` · anthropic-engineering
  How Anthropic scaffolded Claude 3.5 Sonnet to 49% on SWE-bench Verified with a minimal agent harness, detailing tool design and error analysis.
- **2024-11-22** — [Agent-as-a-Judge: Evaluate Agents with Agents](<../evals-observability/evaluation/Agent-as-a-Judge Evaluate Agents with Agents.md>) · `evaluation` · arize
  Summarizes Agent-as-a-Judge, an evaluation pattern where agent systems critique other agent systems instead of relying only on final outcomes or manual review.
- **2024-10-16** — [Comparing OpenAI Swarm with other Multi Agent Frameworks](<multi-agent/Comparing OpenAI Swarm with other Multi Agent Frameworks.md>) · `multi-agent` · arize
  Compares OpenAI Swarm with other multi-agent frameworks, highlighting orchestration patterns and framework tradeoffs.
- **2024-07-30** — [Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant](<../product-engineering/case-studies/Developing Copilot What AI Engineers Can Learn from Our Experience Building An AI Assistant.md>) · `case-studies` · arize
  Arize Copilot case study covering lessons from building an AI assistant for data scientists and AI engineers.
- **2024-02-18** — [The Shift from Models to Compound AI Systems](<../product-engineering/architecture/The Shift from Models to Compound AI Systems.md>) · `architecture` · arize
  Explains the shift from standalone models to compound AI systems that combine models, retrieval, tools, orchestration, and evaluation into production applications.
- **2023-12-07** — [Calling All Functions: Benchmarking OpenAI Function Calling and Explanations](<../evals-observability/evaluation/Calling All Functions Benchmarking OpenAI Function Calling and Explanations.md>) · `evaluation` · arize
  Benchmarks OpenAI function calling and explanation quality, using evaluations to understand third-party LLM tool behavior.
- **2023-04-28** — [Lessons From Building an Early ChatGPT Plugin In Under 24 Hours](<../product-engineering/case-studies/Lessons From Building an Early ChatGPT Plugin In Under 24 Hours.md>) · `case-studies` · arize
  Retrospective on building an early ChatGPT plugin quickly, including product workflow lessons and integration constraints from the plugin ecosystem.
