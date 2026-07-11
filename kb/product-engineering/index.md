# product-engineering

38 articles.

- **2026-07-08** — [Rewriting Bun in Rust](<case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-08** — [The agent is the user now: lessons from the founder of WorkOS](<security/The agent is the user now lessons from the founder of WorkOS.md>) · `security` · arize
  Interview-driven discussion of agents as users, covering identity, permissions, memory, evals, and feedback loops as core production-agent infrastructure.
- **2026-07-01** — [Your site, your rules: new AI traffic options for all customers](<security/Your site, your rules new AI traffic options for all customers.md>) · `security` · cloudflare-ai
  Cloudflare replaces the binary 'Block AI Bots' toggle with per-use-case controls — Search, Agent, and Training crawlers — for all customers including Free tier, and pushes bot operators to split multi-purpose crawlers so site owners can allow discovery without donating training data.
- **2026-06-26** — [Making private MCP servers reachable without making them public | OpenAI Developers](<security/Making private MCP servers reachable without making them public OpenAI Developers.md>) · `security` · openai-devs
  Engineering design of OpenAI's Secure MCP Tunnel: a customer-run open-source client beside a private MCP server opens outbound-only HTTPS to OpenAI, forwarding MCP requests (including streaming and auth flows) so ChatGPT/Codex can reach the server without public endpoints, VPNs, or third-party tunnels.
- **2026-06-23** — [Mastering remote engineering work from your phone | OpenAI Developers](<ux-patterns/Mastering remote engineering work from your phone OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Power-user field guide to Codex Remote in the ChatGPT mobile app, framing the phone as a control plane for agents running on your own machines: worktrees, goals, side chats, inline code review, queued vs. steering prompts, and command-approval security controls.
- **2026-06-18** — [Build your own vulnerability harness](<security/Build your own vulnerability harness.md>) · `security` · cloudflare-ai
  How Cloudflare grew a ~450-line security-audit skill into a model-agnostic, fleet-wide vulnerability-scanning harness: parallel recon agents, per-attack-class Hunter agents, adversarial validators, schema-checked findings.json, and independent re-verification, with different models cross-testing discovery vs. validation.
- **2026-06-09** — [Defend against frontier cyber models: Cloudflare's architecture as customer zero](<security/Defend against frontier cyber models Cloudflare's architecture as customer zero.md>) · `security` · cloudflare-ai
  Follow-up to Project Glasswing detailing Cloudflare's customer-zero defense architecture against frontier cyber models — which compress discovery, exploit-chain construction, and PoC generation — using Cloudforce One threat intel feeding WAF rules deployed network-wide in under 30 seconds (e.g. React2Shell pre-advisory).
- **2026-05-28** — [How we built Cloudflare's data platform and an AI agent on top of it](<architecture/How we built Cloudflare's data platform and an AI agent on top of it.md>) · `architecture` · cloudflare-ai
  How Cloudflare built Town Lake, a single-SQL-interface data platform on R2/Workers/Workflows unifying Postgres, ClickHouse, Kafka, and BigQuery sprawl (1B+ events/sec), and Skipper, an AI agent on top that answers plain-English questions with auditable queries and PII-aware governance.
- **2026-05-25** — [How we contain Claude across products](<security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-05-18** — [Project Glasswing: what Mythos showed us](<security/Project Glasswing what Mythos showed us.md>) · `security` · cloudflare-ai
  Cloudflare's findings from running Anthropic's Mythos Preview (Project Glasswing) against 50+ of its own repos: the model constructs multi-primitive exploit chains and compiles/runs its own proofs-of-concept, but its organic refusals are inconsistent and false-positive rates spike in C/C++ codebases.
- **2026-04-21** — [Moving past bots vs. humans](<security/Moving past bots vs. humans.md>) · `security` · cloudflare-ai
  Argues bot detection must move from 'bots vs. humans' to intent and behavior as AI agents fetch raw content without rendering pages: covers Web Bot Auth (HTTP message signatures) for crawler identification and private rate limiting for clients that no longer behave like browsers.
- **2026-04-20** — [The AI engineering stack we built internally — on the platform we ship](<case-studies/The AI engineering stack we built internally — on the platform we ship.md>) · `case-studies` · cloudflare-ai
  Eleven-month buildout of Cloudflare's internal AI engineering stack on its own products: 3,683 users (93% of R&D), 47.95M AI requests and 241B tokens/month through AI Gateway, an MCP Server Portal with single OAuth, and merge requests nearly doubling from ~5,600 to 10,952/week.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-03-25** — [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](<case-studies/How Perplexity Brought Voice Search to Millions Using the Realtime API OpenAI Developers.md>) · `case-studies` · openai-devs
  Perplexity's production lessons running Realtime-1.5 voice across Comet and Computer: feed context in 2,000-token chunks to avoid all-or-nothing truncation, get system/user/assistant role semantics right, standardize audio via a Rust SDK (48 kHz mono, WebRTC APM), and a 'voice lock' pattern for user pauses.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-03-22** — [100 AI Agents Per Employee: The Enterprise Governance Gap](<security/100 AI Agents Per Employee The Enterprise Governance Gap.md>) · `security` · arize
  Argues that enterprises adopting large populations of AI agents need governance for permissions, ownership, auditability, and lifecycle management before agent scale outpaces human oversight.
- **2026-03-11** — [From prompts to products: One year of Responses | OpenAI Developers](<case-studies/From prompts to products One year of Responses OpenAI Developers.md>) · `case-studies` · openai-devs
  One-year retrospective on the Responses API told through five developer stories, including Raindrop AI's production agent-monitoring platform (failure detection and debugging on GPT-5.2 via the Vercel AI SDK) built on its hosted-tool and background-analysis primitives.
- **2026-02-04** — [15 lessons learned building ChatGPT Apps | OpenAI Developers](<ux-patterns/15 lessons learned building ChatGPT Apps OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Alpic distills 15 lessons from building two dozen ChatGPT Apps on the Apps SDK, centered on 'context asymmetry' between user, UI widget, and model — deciding which tool-output fields each party sees — and packaged into their open-source Skybridge framework.
- **2026-01-11** — [Supercharging Codex with JetBrains MCP at Skyscanner | OpenAI Developers](<case-studies/Supercharging Codex with JetBrains MCP at Skyscanner OpenAI Developers.md>) · `case-studies` · openai-devs
  Skyscanner wires Codex CLI to the JetBrains MCP server so the agent gets IDE feedback loops: get_file_problems surfaced a non-compiling Databricks SDK NotFound constructor immediately instead of after a test run, cutting iteration time.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-11-24** — [What makes a great ChatGPT app | OpenAI Developers](<ux-patterns/What makes a great ChatGPT app OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Design guidance for ChatGPT Apps: instead of porting an existing app's screens and navigation, expose a few narrow 'specific powers' the model can invoke mid-conversation, design for conversational entry points and discovery, and measure whether the app actually improves conversations.
- **2025-10-27** — [Using Codex for education at Dagster Labs | OpenAI Developers](<case-studies/Using Codex for education at Dagster Labs OpenAI Developers.md>) · `case-studies` · openai-devs
  Dagster Labs describes using Codex to accelerate documentation work — writing docs, translating content across mediums, and measuring doc completeness — and finds a well-structured CONTRIBUTING.md doubles as high-leverage scaffolding for the agent.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-10-10** — [How Codex ran OpenAI DevDay 2025](<case-studies/How Codex ran OpenAI DevDay 2025.md>) · `case-studies` · openai-devs
  Behind-the-scenes account of OpenAI using Codex to build DevDay 2025: it implemented the 1990s VISCA protocol to control venue cameras, built an MCP server for stage lighting, and used Codex Cloud best-of-N to iterate Apps SDK demos like a beat pad in parallel.
- **2025-07-30** — [A Watermark for Large Language Models](<security/A Watermark for Large Language Models.md>) · `security` · arize
  Summary of a paper-reading session on watermarking generated text from large language models, including detection goals and implications for responsible deployment.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2024-07-30** — [Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant](<case-studies/Developing Copilot What AI Engineers Can Learn from Our Experience Building An AI Assistant.md>) · `case-studies` · arize
  Arize Copilot case study covering lessons from building an AI assistant for data scientists and AI engineers.
- **2024-07-25** — [Building A Generative AI Platform](<architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-18** — [The Shift from Models to Compound AI Systems](<architecture/The Shift from Models to Compound AI Systems.md>) · `architecture` · arize
  Explains the shift from standalone models to compound AI systems that combine models, retrieval, tools, orchestration, and evaluation into production applications.
- **2023-07-19** — [Streamline and Centralize AI Analytics With Snowflake and Arize AI](<case-studies/Streamline and Centralize AI Analytics With Snowflake and Arize AI.md>) · `case-studies` · arize
  Describes using Snowflake with Arize to centralize AI analytics and observability data for model performance analysis.
- **2023-04-28** — [Lessons From Building an Early ChatGPT Plugin In Under 24 Hours](<case-studies/Lessons From Building an Early ChatGPT Plugin In Under 24 Hours.md>) · `case-studies` · arize
  Retrospective on building an early ChatGPT plugin quickly, including product workflow lessons and integration constraints from the plugin ecosystem.
- **2023-04-11** — [Building LLM applications for production](<architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
- **2022-06-22** — [Deploying Models In An Evolving Housing Market](<case-studies/Deploying Models In An Evolving Housing Market.md>) · `case-studies` · arize
  Case discussion on deploying models in a changing housing market and monitoring model behavior under shifting real-world conditions.
- **2022-01-02** — [Real-time machine learning: challenges and solutions](<architecture/Real-time machine learning challenges and solutions.md>) · `architecture` · chip-huyen
  Deep dive on real-time ML systems covering online prediction, feature freshness, stream processing, monitoring, feedback delays, and the tradeoffs needed to serve adaptive models in production.
- **2021-10-21** — [Rise of the ML Engineer: Chick-fil-A's Korri Jones](<case-studies/Rise of the ML Engineer Chick-fil-A's Korri Jones.md>) · `case-studies` · arize
  Interview with Chick-fil-A ML engineer Korri Jones on production ML work and applied model operations in a large business.
- **2020-12-27** — [Machine learning is going real-time](<architecture/Machine learning is going real-time.md>) · `architecture` · chip-huyen
  Explains the shift from batch prediction to online ML, covering streaming features, low-latency inference, fresh feedback loops, and the architectural constraints behind real-time applications.

## Also relevant (filed elsewhere)

- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<../agents/tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-02** — [Release: llm-coding-agent 0.1a0](<../agents/tool-use/Release llm-coding-agent 0.1a0.md>) · `tool-use` · simon-willison
  Release and implementation notes for a Claude Code-style coding agent built on Simon Willison's LLM framework, including file-editing, command execution, search, read, and write tools plus approval modes.
- **2026-07-01** — [Unmasking the crawls with Attribution Business Insights](<../industry/business/Unmasking the crawls with Attribution Business Insights.md>) · `business` · cloudflare-ai
  Announces the Attribution Business Insights dashboard for Bot Management customers: per-operator crawl-to-referral ratios (observed from 118:1 to ~50,000:1 for AI crawlers), bot-vs-human traffic breakdowns, and crawler classification into Training, Search, and Agent purposes.
- **2026-05-19** — [Announcing Claude Managed Agents on Cloudflare](<../infra-platform/deployment/Announcing Claude Managed Agents on Cloudflare.md>) · `deployment` · cloudflare-ai
  Cloudflare-Anthropic integration running Claude Managed Agents against Cloudflare Sandboxes: the agent loop stays on the Claude Platform while Cloudflare provides microVM or isolate sandboxes, credential-injecting proxies, private service connectivity, browser session audit trails, and per-agent email.
- **2026-04-23** — [An update on recent Claude Code quality reports](<../evals-observability/monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-20** — [Orchestrating AI Code Review at scale](<../agents/multi-agent/Orchestrating AI Code Review at scale.md>) · `multi-agent` · cloudflare-ai
  Deep dive into Cloudflare's CI-native AI code review built on OpenCode: up to seven specialized reviewer agents (security, performance, quality, docs, compliance) plus a coordinator that deduplicates findings and posts one structured review, run across tens of thousands of GitLab merge requests via a plugin architecture.
- **2026-03-24** — [Harness design for long-running application development](<../agents/planning/Harness design for long-running application development.md>) · `planning` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<../agents/tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-02-26** — [Building frontend UIs with Codex and Figma | OpenAI Developers](<../agents/tool-use/Building frontend UIs with Codex and Figma OpenAI Developers.md>) · `tool-use` · openai-devs
  Announces bidirectional Codex-Figma integration via the Figma MCP server: get_design_context extracts layouts/styles/components from Figma frames for code generation, and generate_figma_design turns a running UI back into editable Figma frames.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<../evals-observability/tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-24** — [Alyx 2.0: The AI Agent That Actually Plans](<../agents/planning/Alyx 2.0 The AI Agent That Actually Plans.md>) · `planning` · arize
  Introduces Alyx 2.0 as an agent that plans over observability workflows, covering product design lessons from building a more capable AI analyst.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<../agents/multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2025-09-22** — [Why we built the Responses API | OpenAI Developers](<../agents/tool-use/Why we built the Responses API OpenAI Developers.md>) · `tool-use` · openai-devs
  OpenAI's design rationale for the Responses API as an agentic loop unifying Chat Completions and Assistants: it preserves reasoning state across turns (+5% on TAUBench, better cache utilization) and emits multiple output items — tool calls, structured outputs, intermediate steps — not just the final message.
- **2025-08-28** — [Claude Code vs Cursor: A Power-User’s Playbook](<../agents/tool-use/Claude Code vs Cursor A Power-User’s Playbook.md>) · `tool-use` · arize
  Compares Claude Code and Cursor from a power-user workflow perspective, focusing on coding-agent interfaces and usage patterns.
- **2025-01-22** — [Building Audio Support with OpenAI: Insights from our Journey](<../models/multimodal/Building Audio Support with OpenAI Insights from our Journey.md>) · `multimodal` · arize
  Case study on adding audio support with OpenAI models, covering product and engineering lessons from building multimodal support.
- **2024-12-19** — [Building Effective AI Agents](<../agents/planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
- **2024-12-04** — [AI Agent Workflows and Architectures Masterclass](<../agents/planning/AI Agent Workflows and Architectures Masterclass.md>) · `planning` · arize
  Introduces practical agent workflow and architecture patterns, emphasizing simple tool-calling loops and design choices over vague autonomy claims.
- **2023-10-10** — [Multimodality and Large Multimodal Models (LMMs)](<../models/multimodal/Multimodality and Large Multimodal Models (LMMs).md>) · `multimodal` · chip-huyen
  Explains large multimodal model architecture and training patterns, modality fusion, data challenges, and product capabilities unlocked by image, text, audio, and video models.
- **2023-05-17** — [Evaluating Model Fairness](<../evals-observability/evaluation/Evaluating Model Fairness.md>) · `evaluation` · arize
  Explains model fairness evaluation and how to assess bias and fairness risks in production systems.
- **2023-01-08** — [Self-serve feature platforms: architectures and APIs](<../infra-platform/deployment/Self-serve feature platforms architectures and APIs.md>) · `deployment` · chip-huyen
  Breaks down self-serve feature-platform architecture and APIs, covering feature definitions, pipelines, storage, discovery, and ergonomics for ML teams that need reusable production features.
- **2022-09-22** — [The Death of Central ML Is Greatly Exaggerated](<../industry/trends/The Death of Central ML Is Greatly Exaggerated.md>) · `trends` · arize
  Argues that centralized ML teams remain important as organizations mature, covering organizational patterns for production ML work.
- **2022-08-03** — [Introduction to streaming for data scientists](<../infra-platform/deployment/Introduction to streaming for data scientists.md>) · `deployment` · chip-huyen
  Introduces stream processing for ML systems, comparing batch and streaming architectures, event-time semantics, joins, windows, and why streaming underpins real-time features.
- **2022-02-07** — [Data Distribution Shifts and Monitoring](<../evals-observability/monitoring/Data Distribution Shifts and Monitoring.md>) · `monitoring` · chip-huyen
  Taxonomy of covariate, label, and concept shifts with production monitoring strategies, data-quality checks, slice analysis, alerting tradeoffs, and examples of real-world ML failure modes.
- **2021-10-27** — [Best Practices In ML Observability for Monitoring, Mitigating and Preventing Fraud](<../evals-observability/monitoring/Best Practices In ML Observability for Monitoring, Mitigating and Preventing Fraud.md>) · `monitoring` · arize
  Best practices for fraud-model observability, covering monitoring, mitigation, and prevention workflows for production risk systems.
- **2021-09-13** — [Why data scientists shouldn’t need to know Kubernetes](<../infra-platform/deployment/Why data scientists shouldn’t need to know Kubernetes.md>) · `deployment` · chip-huyen
  Argues that data scientists should consume self-serve infrastructure abstractions rather than raw Kubernetes, outlining platform requirements for development, deployment, and operational ownership.
- **2021-09-11** — [Overcoming AI's Transparency Paradox](<../evals-observability/monitoring/Overcoming AI's Transparency Paradox.md>) · `monitoring` · arize
  Discusses AI transparency and explainability challenges, positioning observability as a way to understand opaque model behavior in production.
