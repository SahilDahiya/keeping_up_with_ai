# product-engineering

121 articles.

- **2026-07-20** — [Building Governed Agents: A Framework for Cost, Control, and Compliance](<security/Building Governed Agents A Framework for Cost, Control, and Compliance.md>) · `security` · langchain
  Framework for governing production agents through an LLM gateway: a five-part govern/decide/protect/observe/assure operating model, pattern-based vs model-based guardrail detection for PII and prompt injection, fail-open/fail-closed fallback design, and layered spend controls (org/team/key limits) for controlling agent token cost.
- **2026-07-17** — [Inside Cursor's agent factory: how it verifies AI-written code](<case-studies/Inside Cursor's agent factory how it verifies AI-written code.md>) · `case-studies` · arize
  Details Cursor's verification architecture for AI-written code: risk scoring routes ~30-40% of PRs to merge without human review, behavioral video artifacts let reviewers inspect agent-exercised changes before the diff, and human corrections become rules/eval cases for its review agent Bugbot, with failed evals triggering diagnosis workflows with trace context attached.
- **2026-07-15** — [AI gateway with data loss prevention, failover, and spend caps in Pydantic Logfire](<security/AI gateway with data loss prevention, failover, and spend caps in Pydantic Logfire.md>) · `security` · pydantic
  Makes the case for an LLM gateway as the single choke point for governance: one key across OpenAI/Anthropic/Google/Bedrock/etc., data-loss-prevention scanning of prompts and completions for secrets/PII (observe, flag, redact, or block), priority and weighted routing for failover/load-balancing, and hard per-key spend caps that block the request rather than alert after the budget is gone.
- **2026-07-15** — [How I tricked Claude into leaking your deepest, darkest secrets](<security/How I tricked Claude into leaking your deepest, darkest secrets.md>) · `security` · simon-willison
  Explains how researcher Ayush Paul bypassed Claude's web_fetch exfiltration protections (which restrict navigation to user- or search-provided URLs) by having a honeypot site serve nested links that the tool would follow, letting an attacker exfiltrate a user's name, city, and employer letter-by-letter; Anthropic closed the hole by disallowing navigation to links found within fetched content.
- **2026-07-13** — [Introducing Precursor: detecting agentic behavior with continuous client-side signals](<security/Introducing Precursor detecting agentic behavior with continuous client-side signals.md>) · `security` · cloudflare-ai
  Details Cloudflare's Precursor system, which injects client-side JS to continuously score session-level behavioral signals (mouse-movement physics like wrist-pivot arcs and hand tremor, keystroke rhythm) at the edge to distinguish humans from bots and agentic automation across an entire user journey, not just at a single challenge checkpoint.
- **2026-07-10** — [AI-pilling our company: lessons learned](<case-studies/AI-pilling our company lessons learned.md>) · `case-studies` · sierra
  Internal adoption case study on spreading AI workflows through a company, including practical lessons for using agents and tools in day-to-day work.
- **2026-07-08** — [Rewriting Bun in Rust](<case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-08** — [The agent is the user now: lessons from the founder of WorkOS](<security/The agent is the user now lessons from the founder of WorkOS.md>) · `security` · arize
  Interview-driven discussion of agents as users, covering identity, permissions, memory, evals, and feedback loops as core production-agent infrastructure.
- **2026-07-07** — [How I shipped a month of engineering work in four days with GLM 5.2 Fast](<case-studies/How I shipped a month of engineering work in four days with GLM 5.2 Fast.md>) · `case-studies` · fireworks
  An engineer used glm-5p2-fast (via Fireworks' FireConnect router into Claude Code) to design, plan, and implement a GPU-scheduler reclaim feature test-first (34 tests, 4 PRs, ~3,000 lines) in four days for $218 in inference, arguing that 2-3x faster inference keeps human-AI design iteration a live back-and-forth instead of breaking into async context switches.
- **2026-07-07** — [How Schneider Electric Built Their LLMOps Foundations With LangSmith](<case-studies/How Schneider Electric Built Their LLMOps Foundations With LangSmith.md>) · `case-studies` · langchain
  Schneider Electric case study on building enterprise LLMOps foundations with LangSmith at scale.
- **2026-07-01** — [How Pendo uses LangSmith to trace Novus from user behavior to code fixes](<case-studies/How Pendo uses LangSmith to trace Novus from user behavior to code fixes.md>) · `case-studies` · langchain
  Pendo case study tracing Novus from user behavior to code fixes, showing how traces connect product signals to agent improvements.
- **2026-07-01** — [Your site, your rules: new AI traffic options for all customers](<security/Your site, your rules new AI traffic options for all customers.md>) · `security` · cloudflare-ai
  Cloudflare replaces the binary 'Block AI Bots' toggle with per-use-case controls — Search, Agent, and Training crawlers — for all customers including Free tier, and pushes bot operators to split multi-purpose crawlers so site owners can allow discovery without donating training data.
- **2026-06-30** — [How Deep Agents Run Untrusted Code Without a Sandbox](<security/How Deep Agents Run Untrusted Code Without a Sandbox.md>) · `security` · langchain
  Explains how Deep Agents run untrusted code without a conventional sandbox and the security tradeoffs in agent execution design.
- **2026-06-29** — [How Candidly Built State-Aware Agent Harnesses with LangSmith](<case-studies/How Candidly Built State-Aware Agent Harnesses with LangSmith.md>) · `case-studies` · langchain
  Candidly case study on building state-aware agent harnesses with LangSmith for production agent workflows.
- **2026-06-26** — [Making private MCP servers reachable without making them public | OpenAI Developers](<security/Making private MCP servers reachable without making them public OpenAI Developers.md>) · `security` · openai-devs
  Engineering design of OpenAI's Secure MCP Tunnel: a customer-run open-source client beside a private MCP server opens outbound-only HTTPS to OpenAI, forwarding MCP requests (including streaming and auth flows) so ChatGPT/Codex can reach the server without public endpoints, VPNs, or third-party tunnels.
- **2026-06-23** — [Mastering remote engineering work from your phone | OpenAI Developers](<ux-patterns/Mastering remote engineering work from your phone OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Power-user field guide to Codex Remote in the ChatGPT mobile app, framing the phone as a control plane for agents running on your own machines: worktrees, goals, side chats, inline code review, queued vs. steering prompts, and command-approval security controls.
- **2026-06-18** — [Build your own vulnerability harness](<security/Build your own vulnerability harness.md>) · `security` · cloudflare-ai
  How Cloudflare grew a ~450-line security-audit skill into a model-agnostic, fleet-wide vulnerability-scanning harness: parallel recon agents, per-attack-class Hunter agents, adversarial validators, schema-checked findings.json, and independent re-verification, with different models cross-testing discovery vs. validation.
- **2026-06-17** — [Clustering billions of products for agentic commerce with Catalog API (2026)](<case-studies/Clustering billions of products for agentic commerce with Catalog API (2026).md>) · `case-studies` · shopify
  How Shopify clusters billions of product listings across millions of stores into canonical entities via embeddings for its agentic-commerce Catalog API, reconciling inconsistent merchant listing structures.
- **2026-06-16** — [Why Fleet Has General Purpose Chat and Specialized Agents](<architecture/Why Fleet Has General Purpose Chat and Specialized Agents.md>) · `architecture` · langchain
  Fleet case study explaining why a product needs both general-purpose chat and specialized agents for different user workflows.
- **2026-06-12** — [How Box AI built enterprise content agents with Deep Agents](<case-studies/How Box AI built enterprise content agents with Deep Agents.md>) · `case-studies` · langchain
  Case study of Box AI moving enterprise content workflows to Deep Agents, covering agent architecture and production constraints.
- **2026-06-11** — [How Benchling builds agents when the smartest AI isn't smart enough](<case-studies/How Benchling builds agents when the smartest AI isn't smart enough.md>) · `case-studies` · langchain
  Case-study notes on how Benchling builds agents when model capability is insufficient on its own, emphasizing workflow design and product constraints.
- **2026-06-10** — [The Missing Link Between Agents and Applications](<architecture/The Missing Link Between Agents and Applications.md>) · `architecture` · langchain
  Explains the missing application-layer pieces around agents, connecting agent runtimes to product interfaces, state, and deployment workflows.
- **2026-06-09** — [Defend against frontier cyber models: Cloudflare's architecture as customer zero](<security/Defend against frontier cyber models Cloudflare's architecture as customer zero.md>) · `security` · cloudflare-ai
  Follow-up to Project Glasswing detailing Cloudflare's customer-zero defense architecture against frontier cyber models — which compress discovery, exploit-chain construction, and PoC generation — using Cloudforce One threat intel feeding WAF rules deployed network-wide in under 30 seconds (e.g. React2Shell pre-advisory).
- **2026-06-09** — [How to detect credential theft in AI agent harness traces](<security/How to detect credential theft in AI agent harness traces.md>) · `security` · arize
  Shows how agent harness traces can expose credential theft and other security failures during tool use.
- **2026-06-05** — [How we use agents to review production infrastructure](<case-studies/How we use agents to review production infrastructure.md>) · `case-studies` · langfuse
  Case study of using agents to review production infrastructure, including operational workflows, review boundaries, and human oversight.
- **2026-06-03** — [How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith](<case-studies/How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith.md>) · `case-studies` · langchain
  Harmonic case study on rebuilding Scout with Deep Agents and LangSmith, linking agent architecture to retention and evaluation.
- **2026-06-01** — [How Rippling built production AI in 6 months with Deep Agents and LangSmith](<case-studies/How Rippling built production AI in 6 months with Deep Agents and LangSmith.md>) · `case-studies` · langchain
  Rippling case study on rolling production AI across products with Deep Agents and LangSmith in a six-month buildout.
- **2026-05-28** — [AI-native product localization](<architecture/AI-native product localization.md>) · `architecture` · sierra
  Case study of AI-native product localization, covering workflows for translating and adapting product surfaces with model assistance.
- **2026-05-28** — [How we built Cloudflare's data platform and an AI agent on top of it](<architecture/How we built Cloudflare's data platform and an AI agent on top of it.md>) · `architecture` · cloudflare-ai
  How Cloudflare built Town Lake, a single-SQL-interface data platform on R2/Workers/Workflows unifying Postgres, ClickHouse, Kafka, and BigQuery sprawl (1B+ events/sec), and Skipper, an AI agent on top that answers plain-English questions with auditable queries and PII-aware governance.
- **2026-05-27** — [How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith](<case-studies/How Lyft Built a Self-Serve AI Agent Platform with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Lyft case study on building a self-serve AI agent platform for customer support with LangGraph and LangSmith.
- **2026-05-25** — [How we contain Claude across products](<security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-05-18** — [Project Glasswing: what Mythos showed us](<security/Project Glasswing what Mythos showed us.md>) · `security` · cloudflare-ai
  Cloudflare's findings from running Anthropic's Mythos Preview (Project Glasswing) against 50+ of its own repos: the model constructs multi-primitive exploit chains and compiles/runs its own proofs-of-concept, but its organic refusals are inconsistent and false-positive rates spike in C/C++ codebases.
- **2026-05-12** — [From LLMs to enterprise-grade agents](<architecture/From LLMs to enterprise-grade agents.md>) · `architecture` · sierra
  Explains what distinguishes enterprise-grade agents from raw LLMs, including integrations, policy controls, reliability, and operational lifecycle.
- **2026-05-12** — [Industry first: PCI-compliant agents](<security/Industry first PCI-compliant agents.md>) · `security` · sierra
  Explains PCI-compliant payment workflows for agents, focusing on secure action-taking and sensitive-data handling.
- **2026-05-12** — [Meet the Voice Sommelier](<ux-patterns/Meet the Voice Sommelier.md>) · `ux-patterns` · sierra
  Explains voice-agent experience design, including brand voice selection, vocal cues, conversation design, and metrics for acceptance and satisfaction.
- **2026-05-05** — [PostgreSQL Triggers vs Async Audit Logs: A Pydantic Logfire Migration](<architecture/PostgreSQL Triggers vs Async Audit Logs A Pydantic Logfire Migration.md>) · `architecture` · pydantic
  Migrating Logfire's audit logging from synchronous PostgreSQL triggers to async event-based logs, covering reliability, write-path performance, and capturing who-did-what context without blocking the request.
- **2026-05-01** — [Designing the AI Agent Supervision Experience](<ux-patterns/Designing the AI Agent Supervision Experience.md>) · `ux-patterns` · cresta
  Discusses UX and workflow design for supervising AI agents, including human oversight and intervention surfaces.
- **2026-04-27** — [How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements](<security/How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements.md>) · `security` · langchain
  Connects LangSmith and LangChain OSS workflows to EU AI Act readiness, including observability, evaluation, governance, and auditability.
- **2026-04-24** — [How we fixed prompt injection for all models on Fireworks](<security/How we fixed prompt injection for all models on Fireworks.md>) · `security` · fireworks
  Explains a tokenizer-level prompt-injection fix and the implications for securing model-serving systems.
- **2026-04-23** — [How we built RBAC that scales for the enterprise](<security/How we built RBAC that scales for the enterprise.md>) · `security` · baseten
  Engineering writeup on building RBAC for enterprise AI infrastructure and balancing autonomy with control.
- **2026-04-21** — [Moving past bots vs. humans](<security/Moving past bots vs. humans.md>) · `security` · cloudflare-ai
  Argues bot detection must move from 'bots vs. humans' to intent and behavior as AI agents fetch raw content without rendering pages: covers Web Bot Auth (HTTP message signatures) for crawler identification and private rate limiting for clients that no longer behave like browsers.
- **2026-04-20** — [The AI engineering stack we built internally — on the platform we ship](<case-studies/The AI engineering stack we built internally — on the platform we ship.md>) · `case-studies` · cloudflare-ai
  Eleven-month buildout of Cloudflare's internal AI engineering stack on its own products: 3,683 users (93% of R&D), 47.95M AI requests and 241B tokens/month through AI Gateway, an MCP Server Portal with single OAuth, and merge requests nearly doubling from ~5,600 to 10,952/week.
- **2026-04-15** — [Automation Discovery: Designing Systems to Extract Blueprints from Conversation Data](<architecture/Automation Discovery Designing Systems to Extract Blueprints from Conversation Data.md>) · `architecture` · cresta
  Describes systems that mine conversation data to discover automation opportunities and generate process blueprints.
- **2026-04-13** — [How to prepare for AI compliance and governance](<security/How to prepare for AI compliance and governance.md>) · `security` · braintrust
  Connects AI compliance and governance to engineering controls such as observability, audit trails, data boundaries, review workflows, and policy enforcement.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-04-03** — [AI for Systems: Using LLMs to Optimize Database Query Execution](<architecture/AI for Systems Using LLMs to Optimize Database Query Execution.md>) · `architecture` · together
  Explores using LLMs to optimize database query execution as an AI-for-systems pattern.
- **2026-03-27** — [Evals are the new PRD](<architecture/Evals are the new PRD.md>) · `architecture` · braintrust
  Argues that evals can act as executable product requirements for AI systems, aligning teams around expected behavior and measurable quality.
- **2026-03-25** — [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](<case-studies/How Perplexity Brought Voice Search to Millions Using the Realtime API OpenAI Developers.md>) · `case-studies` · openai-devs
  Perplexity's production lessons running Realtime-1.5 voice across Comet and Computer: feed context in 2,000-token chunks to avoid all-or-nothing truncation, get system/user/assistant role semantics right, standardize audio via a Rust SDK (48 kHz mono, WebRTC APM), and a 'voice lock' pattern for user pauses.
- **2026-03-25** — [Full-Stack Agent Observability with AgentSH + Pydantic Logfire | Pydantic](<security/Full-Stack Agent Observability with AgentSH + Pydantic Logfire Pydantic.md>) · `security` · pydantic
  Pairs LLM-level tracing (model calls, tool invocations) with AgentSH's OS-boundary auditing of what an agent actually did on the machine (file access, network connections, process execution) plus policy enforcement, both emitted as OpenTelemetry into one timeline to catch failures in the 'seams'.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-03-22** — [100 AI Agents Per Employee: The Enterprise Governance Gap](<security/100 AI Agents Per Employee The Enterprise Governance Gap.md>) · `security` · arize
  Argues that enterprises adopting large populations of AI agents need governance for permissions, ownership, auditability, and lifecycle management before agent scale outpaces human oversight.
- **2026-03-19** — [Building a Magic Mirror: AI retail experiences with Remix (2026)](<case-studies/Building a Magic Mirror AI retail experiences with Remix (2026).md>) · `case-studies` · shopify
  Shopify builds an in-store 'Magic Mirror' AI retail experience with Remix, using multimodal AI to turn physical shopping into an interactive experience for hype-driven brands.
- **2026-03-17** — [Evals for PMs: A practical guide to AI product quality](<ux-patterns/Evals for PMs A practical guide to AI product quality.md>) · `ux-patterns` · braintrust
  Practical guide for product managers defining AI product quality with evals, user-centered criteria, examples, and iteration loops.
- **2026-03-12** — [Supporting privacy and compliance for EU teams](<security/Supporting privacy and compliance for EU teams.md>) · `security` · braintrust
  Covers privacy and compliance requirements for EU AI teams, including data residency, controls, and deployment choices for observability data.
- **2026-03-11** — [From prompts to products: One year of Responses | OpenAI Developers](<case-studies/From prompts to products One year of Responses OpenAI Developers.md>) · `case-studies` · openai-devs
  One-year retrospective on the Responses API told through five developer stories, including Raindrop AI's production agent-monitoring platform (failure detection and debugging on GPT-5.2 via the Vercel AI SDK) built on its hosted-tool and background-analysis primitives.
- **2026-03-09** — [How we built LangChain’s GTM Agent](<case-studies/How we built LangChain’s GTM Agent.md>) · `case-studies` · langchain
  Case study of building LangChain's GTM agent, covering workflow design, tool use, and production iteration.
- **2026-03-03** — [Scaling Open Source Code Review With AI | Pydantic](<case-studies/Scaling Open Source Code Review With AI Pydantic.md>) · `case-studies` · pydantic
  The Pydantic AI lead maintainer distills 4,668 historical PR review comments into ~150 AGENTS.md rules to build an automated AI code reviewer, a response to the AI-generated PR flood that inverted the old effort asymmetry between creating and reviewing a PR.
- **2026-02-25** — [Accelerating AI research that accelerates AI research](<case-studies/Accelerating AI research that accelerates AI research.md>) · `case-studies` · modal
  Case study on using elastic compute to accelerate AI research workflows, including experiment throughput and infrastructure offload.
- **2026-02-18** — [monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1](<case-studies/monday Service + LangSmith Building a Code-First Evaluation Strategy from Day 1.md>) · `case-studies` · langchain
  monday Service case study on building a code-first evaluation strategy for AI product quality from day one.
- **2026-02-17** — [Is Your Python Web Framework Really the Performance Bottleneck? | Pydantic Logfire](<architecture/Is Your Python Web Framework Really the Performance Bottleneck Pydantic Logfire.md>) · `architecture` · pydantic
  Argues Python web-framework micro-benchmarks mislead: within a real request, database calls, serialization, and downstream I/O usually dominate, so framework choice is rarely the actual latency bottleneck—use tracing to find the real one.
- **2026-02-17** — [Inside Typeform’s AI Agent Stack](<case-studies/Inside Typeform’s AI Agent Stack.md>) · `case-studies` · arize
  Case study of Typeform’s AI agent stack, useful for understanding production architecture choices in agent applications.
- **2026-02-04** — [15 lessons learned building ChatGPT Apps | OpenAI Developers](<ux-patterns/15 lessons learned building ChatGPT Apps OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Alpic distills 15 lessons from building two dozen ChatGPT Apps on the Apps SDK, centered on 'context asymmetry' between user, UI widget, and model — deciding which tool-output fields each party sees — and packaged into their open-source Skybridge framework.
- **2026-02-03** — [How to build a production agentic app, the Pydantic Way](<architecture/How to build a production agentic app, the Pydantic Way.md>) · `architecture` · pydantic
  End-to-end guide to structuring a production agentic app on the Pydantic stack: FastAPI to expose the agent, Pydantic AI for the agent loop, Logfire for observability, and Pydantic Evals for evaluation, with reasoning on when to use an agent framework vs. the raw LLM SDK.
- **2026-01-29** — [OWASP Top 10 for Agentic Applications: Compliance Guide](<security/OWASP Top 10 for Agentic Applications Compliance Guide.md>) · `security` · arize
  Maps OWASP risks to agentic applications and explains compliance-oriented controls for agent systems.
- **2026-01-26** — [How shredding JSON is giving Logfire 1000x query speedups](<architecture/How shredding JSON is giving Logfire 1000x query speedups.md>) · `architecture` · pydantic
  How Logfire 'shreds' nested JSON attributes into typed columns in its columnar store for up to 1000x query speedups—turning 30s-timeout queries into sub-second—covering schema inference and dynamic column materialization.
- **2026-01-22** — [How Observability-Driven Sandboxing Secures AI Agents](<security/How Observability-Driven Sandboxing Secures AI Agents.md>) · `security` · arize
  Explains how sandbox telemetry and observability can harden AI agents that execute code or use external tools.
- **2026-01-11** — [Supercharging Codex with JetBrains MCP at Skyscanner | OpenAI Developers](<case-studies/Supercharging Codex with JetBrains MCP at Skyscanner OpenAI Developers.md>) · `case-studies` · openai-devs
  Skyscanner wires Codex CLI to the JetBrains MCP server so the agent gets IDE feedback loops: get_file_problems surfaced a non-compiling Databricks SDK NotFound constructor immediately instead of after a test run, cutting iteration time.
- **2026-01-08** — [How to choose the right open model for production](<architecture/How to choose the right open model for production.md>) · `architecture` · together
  Guide to choosing open models for production based on workload, quality, and serving constraints.
- **2026-01-01** — [How Coursera builds next-generation learning tools](<case-studies/How Coursera builds next-generation learning tools.md>) · `case-studies` · braintrust
  Customer case study on Coursera's next-generation learning tools and how evaluation workflows support quality for education-focused AI features.
- **2026-01-01** — [How Fintool generates millions of financial insights](<case-studies/How Fintool generates millions of financial insights.md>) · `case-studies` · braintrust
  Case study of Fintool generating financial insights at scale, using evaluation and observability to manage quality in high-volume AI workflows.
- **2026-01-01** — [How Graphite builds reliable AI code review at scale](<case-studies/How Graphite builds reliable AI code review at scale.md>) · `case-studies` · braintrust
  Case study of Graphite building reliable AI code review at scale, with evaluation and workflow design for production developer tooling.
- **2026-01-01** — [How Loom auto-generates video titles](<case-studies/How Loom auto-generates video titles.md>) · `case-studies` · braintrust
  Case study of Loom auto-generating video titles and using evals to improve a production AI feature's usefulness and quality.
- **2026-01-01** — [How Portola empowers subject matter experts to improve AI quality](<case-studies/How Portola empowers subject matter experts to improve AI quality.md>) · `case-studies` · braintrust
  Case study of Portola using subject-matter experts to improve AI quality through review workflows, datasets, and eval-driven iteration.
- **2026-01-01** — [How Retool uses Loop to turn logs into AI roadmap decisions](<case-studies/How Retool uses Loop to turn logs into AI roadmap decisions.md>) · `case-studies` · braintrust
  Case study of Retool using production logs and Loop-style review to turn AI usage data into roadmap and quality decisions.
- **2026-01-01** — [How Zapier builds production-ready AI products](<case-studies/How Zapier builds production-ready AI products.md>) · `case-studies` · braintrust
  Case study of Zapier building production-ready AI products with observability, evals, and feedback loops across real customer workflows.
- **2025-12-22** — [EU AI Act Compliance: What AI Engineering Teams Should Monitor](<security/EU AI Act Compliance What AI Engineering Teams Should Monitor.md>) · `security` · arize
  Explains what AI engineering teams should monitor for EU AI Act compliance, connecting regulation to observability and operational controls.
- **2025-12-17** — [How Tiger Data Built a Production AI Slack Bot with Pydantic AI and Logfire](<case-studies/How Tiger Data Built a Production AI Slack Bot with Pydantic AI and Logfire.md>) · `case-studies` · pydantic
  Case study of Tiger Data's production Slack bot on Pydantic AI + Logfire, integrating eight MCP servers (Slack search, customer docs, Salesforce, GitHub, Linear, meeting transcripts, user memory, progress reports) with per-user memory/context, retry logic, provider switching, and Agent-Run trace visualization, scaled to thousands of concurrent conversations.
- **2025-11-25** — [Vibe Coding a Custom Annotation UI](<ux-patterns/Vibe Coding a Custom Annotation UI.md>) · `ux-patterns` · langfuse
  Case study of building a custom annotation UI for eval workflows with AI-assisted coding, highlighting review ergonomics and human feedback collection.
- **2025-11-24** — [What makes a great ChatGPT app | OpenAI Developers](<ux-patterns/What makes a great ChatGPT app OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Design guidance for ChatGPT Apps: instead of porting an existing app's screens and navigation, expose a few narrow 'specific powers' the model can invoke mid-conversation, design for conversational entry points and discovery, and measure whether the app actually improves conversations.
- **2025-11-20** — [Agents need good developer experience too](<architecture/Agents need good developer experience too.md>) · `architecture` · modal
  Argues that agent systems need strong developer experience, covering observability, iteration loops, deployment ergonomics, and tool surfaces.
- **2025-11-19** — [How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry](<security/How To Improve AI Agent Security with Microsoft’s AI Red Teaming Agent in Microsoft Foundry.md>) · `security` · arize
  Explains how red-team agents can be used to find and test security weaknesses in agentic applications.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<case-studies/Vercel code fixing with open models, speculative decoding, and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-28** — [Voice Cloning with Consent](<security/Voice Cloning with Consent.md>) · `security` · huggingface
  Proposes a 'voice consent gate': before any voice cloning runs, the speaker must record a spoken consent phrase, which is verified with ASR (and speaker verification) against the same audio used for cloning — a concrete, implementable design pattern (with a demo Space and code) for making consent a hard gate rather than a checkbox.
- **2025-10-27** — [Using Codex for education at Dagster Labs | OpenAI Developers](<case-studies/Using Codex for education at Dagster Labs OpenAI Developers.md>) · `case-studies` · openai-devs
  Dagster Labs describes using Codex to accelerate documentation work — writing docs, translating content across mediums, and measuring doc completeness — and finds a well-structured CONTRIBUTING.md doubles as high-leverage scaffolding for the agent.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-10-10** — [How Codex ran OpenAI DevDay 2025](<case-studies/How Codex ran OpenAI DevDay 2025.md>) · `case-studies` · openai-devs
  Behind-the-scenes account of OpenAI using Codex to build DevDay 2025: it implemented the 1990s VISCA protocol to control venue cameras, built an MCP server for stage lighting, and used Codex Cloud best-of-N to iterate Apps SDK demos like a beat pad in parallel.
- **2025-09-11** — [Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith](<case-studies/Monte Carlo Building Data + AI Observability Agents with LangGraph and LangSmith.md>) · `case-studies` · langchain
  Monte Carlo case study on building data and AI observability agents with LangGraph and LangSmith.
- **2025-09-08** — [Cresta’s Three Strategic Pillars of AI Agent Defense for Enterprise Security and Compliance](<security/Cresta’s Three Strategic Pillars of AI Agent Defense for Enterprise Security and Compliance.md>) · `security` · cresta
  Frames AI agent defense around enterprise security, compliance, testing, and operational safeguards.
- **2025-08-19** — [The rise of async programming](<architecture/The rise of async programming.md>) · `architecture` · braintrust
  Explains why asynchronous programming patterns matter for long-running AI workflows, background jobs, agent tasks, and responsive product experiences.
- **2025-07-30** — [A Watermark for Large Language Models](<security/A Watermark for Large Language Models.md>) · `security` · arize
  Summary of a paper-reading session on watermarking generated text from large language models, including detection goals and implications for responsible deployment.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-04-24** — [How we use LLMs to build and scale Langfuse](<case-studies/How we use LLMs to build and scale Langfuse.md>) · `case-studies` · langfuse
  Case study of how Langfuse uses LLMs internally to build and scale the product, including practical workflows for AI-assisted engineering and operations.
- **2025-03-20** — [Build vs. Buy: How Cresta Engineered Its Own Customer Data Access Solution](<architecture/Build vs. Buy How Cresta Engineered Its Own Customer Data Access Solution.md>) · `architecture` · cresta
  Engineering case study on building a customer data access layer, useful for understanding integration tradeoffs in enterprise AI products.
- **2025-03-18** — [Our Own Zero to One: Lessons Learned in Building The Brinks Home AI Agent](<case-studies/Our Own Zero to One Lessons Learned in Building The Brinks Home AI Agent.md>) · `case-studies` · cresta
  Production case study on building an AI agent from zero to one, with lessons about scope, rollout, and operational constraints.
- **2025-02-25** — [FastRTC: The Real-Time Communication Library for Python](<architecture/FastRTC The Real-Time Communication Library for Python.md>) · `architecture` · huggingface
  FastRTC builds real-time voice/video AI apps in Python over WebRTC or WebSockets: built-in voice activity detection and turn-taking (ReplyOnPause), automatic Gradio UI, phone-call ingress, and mounting streams onto FastAPI.
- **2025-02-12** — [How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting](<case-studies/How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting.md>) · `case-studies` · arize
  Case study on using Phoenix traces and observability to improve AI-driven troubleshooting workflows in production.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2024-12-03** — [Investing in Performance: Fine-tune small models with LLM insights - a CFM case study](<case-studies/Investing in Performance Fine-tune small models with LLM insights - a CFM case study.md>) · `case-studies` · huggingface
  CFM (quant hedge fund) case study: use an LLM to label financial NER data, distill that into a compact fine-tuned model, and deploy it on Inference Endpoints — with an F1 and $/hour table showing the fine-tuned small model beating zero-shot LLM accuracy at a fraction of the inference cost.
- **2024-11-13** — [LLM Product Development for Product Managers](<ux-patterns/LLM Product Development for Product Managers.md>) · `ux-patterns` · langfuse
  Product-management guide for LLM applications, connecting user workflows, quality criteria, feedback, and evals to AI product development decisions.
- **2024-09-26** — [Pushing LangSmith to new limits with Replit Agent's complex workflows](<case-studies/Pushing LangSmith to new limits with Replit Agent's complex workflows.md>) · `case-studies` · langchain
  Replit Agent case study on tracing and managing complex agent workflows with LangSmith.
- **2024-08-06** — [Compound AI systems explained](<architecture/Compound AI systems explained.md>) · `architecture` · baseten
  Explains compound AI systems and how multiple models, tools, and control logic combine into applications.
- **2024-07-30** — [Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant](<case-studies/Developing Copilot What AI Engineers Can Learn from Our Experience Building An AI Assistant.md>) · `case-studies` · arize
  Arize Copilot case study covering lessons from building an AI assistant for data scientists and AI engineers.
- **2024-07-25** — [Building A Generative AI Platform](<architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-07-09** — [Banque des Territoires (CDC Group) x Polyconseil x Hugging Face: Enhancing a Major French Environmental Program with a Sovereign Data Solution](<case-studies/Banque des Territoires (CDC Group) x Polyconseil x Hugging Face Enhancing a Major French Environmental Program with a Sovereign Data Solution.md>) · `case-studies` · huggingface
  Banque des Territoires (CDC) x Polyconseil build a sovereign, on-prem RAG assistant for the EduRénov program using open models (Mistral-7B-Instruct, Sentence Transformers, TGI): retriever/reader architecture, data-sovereignty constraints, and production lessons.
- **2024-07-02** — [Building multi-component AI workflows at scale with Chains](<architecture/Building multi-component AI workflows at scale with Chains.md>) · `architecture` · baseten
  Explains multi-component AI workflows with Chains, including orchestration across model and application steps.
- **2024-06-25** — [XLSCOUT Unveils ParaEmbed 2.0: a Powerful Embedding Model Tailored for Patents and IP with Expert Support from Hugging Face](<case-studies/XLSCOUT Unveils ParaEmbed 2.0 a Powerful Embedding Model Tailored for Patents and IP with Expert Support from Hugging Face.md>) · `case-studies` · huggingface
  XLSCOUT fine-tunes BGE-base into ParaEmbed 2.0 on expert-curated patent data, gaining 23% accuracy over its predecessor and beating GPT-4/text-embedding-ada-002 on patent prior-art retrieval — a case for domain-specific open embeddings over closed APIs.
- **2024-06-19** — [How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x](<case-studies/How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x.md>) · `case-studies` · langchain
  Factory case study on automating feedback loops with LangSmith to improve iteration speed and production agent quality.
- **2024-06-06** — [How to catch crypto miners using syscall signatures](<security/How to catch crypto miners using syscall signatures.md>) · `security` · modal
  Explains detecting abusive GPU workloads with syscall signatures, a useful pattern for securing shared AI infrastructure.
- **2024-05-30** — [LLM Summarization: Getting To Production](<architecture/LLM Summarization Getting To Production.md>) · `architecture` · arize
  Covers production considerations for LLM summarization systems, including quality controls and deployment pitfalls.
- **2024-05-14** — [Monitoring LLM Security & Reducing LLM Risks](<security/Monitoring LLM Security & Reducing LLM Risks.md>) · `security` · langfuse
  Covers monitoring patterns for LLM security risks such as prompt injection, data leakage, and unsafe outputs, with observability as part of the mitigation loop.
- **2024-05-06** — [AI development loops](<architecture/AI development loops.md>) · `architecture` · braintrust
  Describes AI development loops where logs, evals, human review, and product iteration form the core workflow for improving AI applications.
- **2024-04-16** — [Running Privacy-Preserving Inferences on Hugging Face Endpoints](<security/Running Privacy-Preserving Inferences on Hugging Face Endpoints.md>) · `security` · huggingface
  Shows how to serve Zama Concrete ML models under Fully Homomorphic Encryption on HF Inference Endpoints via custom inference handlers, so a spam classifier runs on ciphertext without ever seeing the plaintext message; also covers compiling your own FHE-friendly model.
- **2024-02-26** — [AI Watermarking 101: Tools and Techniques](<security/AI Watermarking 101 Tools and Techniques.md>) · `security` · huggingface
  Surveys watermarking for AI-generated content: for images, in-generation methods (Stable Signature) vs post-hoc (Truepic/Imatag, C2PA metadata); for LLM text, logit-biasing green/red token lists at sampling time and the detection statistics behind them, plus SynthID-Text in transformers. Discusses robustness to editing and the short-text detection confidence limit.
- **2024-02-21** — [What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?](<case-studies/What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences.md>) · `case-studies` · arize
  Healthcare and life-sciences case discussion on what it takes to build successful LLM applications, including domain constraints and evaluation needs.
- **2024-02-18** — [The Shift from Models to Compound AI Systems](<architecture/The Shift from Models to Compound AI Systems.md>) · `architecture` · arize
  Explains the shift from standalone models to compound AI systems that combine models, retrieval, tools, orchestration, and evaluation into production applications.
- **2023-11-13** — [The AI product development journey](<architecture/The AI product development journey.md>) · `architecture` · braintrust
  Frames the AI product development journey around iterative prototyping, evaluation, logging, feedback, and production-quality improvement loops.
- **2023-04-28** — [Lessons From Building an Early ChatGPT Plugin In Under 24 Hours](<case-studies/Lessons From Building an Early ChatGPT Plugin In Under 24 Hours.md>) · `case-studies` · arize
  Retrospective on building an early ChatGPT plugin quickly, including product workflow lessons and integration constraints from the plugin ecosystem.
- **2023-04-11** — [Building LLM applications for production](<architecture/Building LLM applications for production.md>) · `architecture` · chip-huyen
  Practical guide to production LLM applications covering task decomposition, retrieval, prompt construction, evaluation, monitoring, and latency/cost tradeoffs.
- **2022-01-02** — [Real-time machine learning: challenges and solutions](<architecture/Real-time machine learning challenges and solutions.md>) · `architecture` · chip-huyen
  Deep dive on real-time ML systems covering online prediction, feature freshness, stream processing, monitoring, feedback delays, and the tradeoffs needed to serve adaptive models in production.
- **2020-12-27** — [Machine learning is going real-time](<architecture/Machine learning is going real-time.md>) · `architecture` · chip-huyen
  Explains the shift from batch prediction to online ML, covering streaming features, low-latency inference, fresh feedback loops, and the architectural constraints behind real-time applications.
- **2020-06-30** — [3 Key Concepts for Creating AI Product Experiences](<ux-patterns/3 Key Concepts for Creating AI Product Experiences.md>) · `ux-patterns` · cresta
  Covers product-design principles for understandable AI experiences, including how users form trust and interpret system behavior.

## Also relevant (filed elsewhere)

- **2026-07-20** — [Harness Week: Pydantic AI Harness, the capability library for agents](<../agents/harness/Harness Week Pydantic AI Harness, the capability library for agents.md>) · `harness` · pydantic
  Introduces Pydantic AI Harness, an official capability library of ~40 pluggable agent capabilities (file/shell access with path-traversal checks, memory, sub-agent delegation, context compaction, CodeMode's code-execution sandbox) that plug in without framework changes, plus community packages like pydantic-ai-shields, which layers a heuristic PromptInjection filter with a deterministic ToolGuard approval gate on sensitive tool calls.
- **2026-07-15** — [Agents need their own computer. Here's how to give them one safely.](<../agents/harness/Agents need their own computer. Here's how to give them one safely.md>) · `harness` · langchain
  Argues agent execution environments need machine-level isolation (hardware-virtualized microVMs, not shared-kernel containers) citing a 2025 npm supply-chain worm and a 2026 Linux kernel CVE, then lays out four requirements (safe execution, control via credential-proxying, observability, fast reproducible provisioning) that LangSmith Sandboxes implements with sub-second boot and copy-on-write forking.
- **2026-07-15** — [Pinecone: Harnessing the wisdom of the workforce](<../agents/harness/Pinecone Harnessing the wisdom of the workforce.md>) · `harness` · sierra
  Describes Sierra's internal cloud-agent platform Pinecone: an app server plus 'Agency' control plane that reconciles Kubernetes pods and Redis Streams for durable, resumable sessions, a Go runner supervising Codex/Claude Code, network-proxy credential injection so the agent never sees real tokens, and copy-on-write session forking/branching for multiplayer collaboration.
- **2026-07-15** — [xai-org/grok-build, now open source](<../agents/harness/xai-orggrok-build, now open source.md>) · `harness` · simon-willison
  Covers xAI open-sourcing its 844K-line Rust 'Grok Build' coding-agent CLI after backlash over it silently uploading users' entire home directories to Google Cloud; digs into the released source for its system/subagent prompts and tool implementations that were ported from Codex (apply_patch, grep_files) and OpenCode (bash, edit, glob).
- **2026-07-15** — [Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse](<../evals-observability/evaluation/Building Deployment Gates for LLMs and AI Agents in Financial Services - Langfuse.md>) · `evaluation` · langfuse
  Walks through a PASS/FAIL deployment-gate pipeline for LLM systems at a major bank, built on Langfuse datasets/experiments/prompt management/annotation queues: three golden datasets (FinanceBench, Financial PhraseBank, a custom adversarial advisory set) score models and agents, gate on thresholds like 85% numerical accuracy, and emit CI exit codes plus reviewable evidence for model risk management.
- **2026-07-15** — [How we chose the model behind Topics with Baseten - Blog - Braintrust](<../evals-observability/evaluation/How we chose the model behind Topics with Baseten - Blog - Braintrust.md>) · `evaluation` · braintrust
  Details how Braintrust and Baseten chose and tuned a sub-10B model (Gemma 4B, beating Qwen) to summarize every production trace for the Topics feature, built a 650-example benchmark across label correctness/factuality/issues-recall/false-positive-rate, and improved Issues recall from 0% to 32.8% through prompt iteration alone (no fine-tuning).
- **2026-07-08** — [Deep Agents Code on NVIDIA NemoClaw](<../agents/tool-use/Deep Agents Code on NVIDIA NemoClaw.md>) · `tool-use` · langchain
  Covers a governed Deep Agents code blueprint on NVIDIA NemoClaw for sensitive code workflows, emphasizing controls around agentic coding.
- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<../agents/tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-02** — [Release: llm-coding-agent 0.1a0](<../agents/tool-use/Release llm-coding-agent 0.1a0.md>) · `tool-use` · simon-willison
  Release and implementation notes for a Claude Code-style coding agent built on Simon Willison's LLM framework, including file-editing, command execution, search, read, and write tools plus approval modes.
- **2026-07-01** — [Unmasking the crawls with Attribution Business Insights](<../industry/business/Unmasking the crawls with Attribution Business Insights.md>) · `business` · cloudflare-ai
  Announces the Attribution Business Insights dashboard for Bot Management customers: per-operator crawl-to-referral ratios (observed from 118:1 to ~50,000:1 for AI crawlers), bot-vs-human traffic breakdowns, and crawler classification into Training, Search, and Agent purposes.
- **2026-06-30** — [Let your customers shape your agents](<../evals-observability/evaluation/Let your customers shape your agents.md>) · `evaluation` · sierra
  Explains experimentation loops for agent improvement, using customer behavior, A/B tests, and statistical confidence to shape agent changes.
- **2026-06-18** — [What is an agent harness? Why harnesses are replacing agent frameworks](<../agents/harness/What is an agent harness Why harnesses are replacing agent frameworks.md>) · `harness` · arize
  Explains why agent harnesses are replacing simple framework use as the unit of production agent engineering.
- **2026-06-16** — [The Art of Loop Engineering](<../agents/harness/The Art of Loop Engineering.md>) · `harness` · langchain
  Discusses loop engineering for agents, focusing on the control loops that govern planning, action, observation, and refinement.
- **2026-06-12** — [How to Choose the Right Sandbox for AI Agents](<../agents/computer-use/How to Choose the Right Sandbox for AI Agents.md>) · `computer-use` · langchain
  Guide to choosing an agent sandbox based on isolation, tool access, persistence, security, and operational constraints.
- **2026-06-12** — [Agent Assist: What It Is, How It Works & How to Choose](<../agents/tool-use/Agent Assist What It Is, How It Works & How to Choose.md>) · `tool-use` · cresta
  Explains real-time agent assist as a tool-augmented workflow that surfaces guidance during live interactions.
- **2026-06-05** — [Give your agent its own computer](<../agents/computer-use/Give your agent its own computer.md>) · `computer-use` · langchain
  Argues for giving agents isolated computers or sandboxes so they can run tools while preserving control, safety, and reproducibility.
- **2026-06-03** — [How to Build a Custom Agent Harness](<../agents/harness/How to Build a Custom Agent Harness.md>) · `harness` · langchain
  Guide to building a custom agent harness, covering control loop design, state, tools, observability, and evaluation hooks.
- **2026-06-03** — [Why long-running AI agents need a harness, not a model](<../agents/harness/Why long-running AI agents need a harness, not a model.md>) · `harness` · pydantic
  Foundational argument that a capable model is not a reliable agent: long-running agents need a 'harness' — the layer of tools, coordination, context, orchestration, safety checks, fallbacks, and memory around the model that turns intent into durable work legible to humans and systems.
- **2026-06-02** — [AI observability for agent products: how Atlas uses Logfire](<../evals-observability/tracing/AI observability for agent products how Atlas uses Logfire.md>) · `tracing` · pydantic
  Atlas (8 engineers, 1000 DAU) instruments every span with user/project/workspace identity via X-Context-* headers so a coding agent can query production traces in plain English; the takeaway is that identity-carrying spans, not the AI, are what make trace data answerable.
- **2026-06-01** — [How Hermes implements an open source agent harness architecture](<../agents/harness/How Hermes implements an open source agent harness architecture.md>) · `harness` · arize
  Breaks down Hermes as an open-source agent harness architecture, focusing on components, control flow, and implementation boundaries.
- **2026-05-20** — [EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API](<../agents/tool-use/EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.md>) · `tool-use` · langchain
  Case study building a financial research agent for EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API.
- **2026-05-19** — [Announcing Claude Managed Agents on Cloudflare](<../infra-platform/deployment/Announcing Claude Managed Agents on Cloudflare.md>) · `deployment` · cloudflare-ai
  Cloudflare-Anthropic integration running Claude Managed Agents against Cloudflare Sandboxes: the agent loop stays on the Claude Platform while Cloudflare provides microVM or isolate sandboxes, credential-injecting proxies, private service connectivity, browser session audit trails, and per-agent email.
- **2026-05-13** — [LangSmith Sandboxes are Generally Available](<../agents/computer-use/LangSmith Sandboxes are Generally Available.md>) · `computer-use` · langchain
  Covers LangSmith Sandboxes for safely running agent code and tools in isolated execution environments.
- **2026-05-12** — [Build durable agents with Restate and Pydantic AI](<../agents/harness/Build durable agents with Restate and Pydantic AI.md>) · `harness` · pydantic
  Integrates Restate to give Pydantic AI agents durable execution (journaled steps with retry/recovery), durable sessions keyed by user/conversation, human-in-the-loop pauses that survive crashes for minutes to months, and durable multi-agent orchestration (RPC, fan-out, timeouts).
- **2026-05-12** — [Building more human voice experiences](<../models/multimodal/Building more human voice experiences.md>) · `multimodal` · sierra
  Explains design and engineering considerations for more human voice-agent experiences, including timing, emotion, and conversational flow.
- **2026-05-12** — [Multilingual voice: building agents that speak to everyone](<../models/multimodal/Multilingual voice building agents that speak to everyone.md>) · `multimodal` · sierra
  Describes building multilingual voice agents, including speech recognition, language coverage, and user-experience considerations.
- **2026-05-12** — [Sierra speaks](<../models/multimodal/Sierra speaks.md>) · `multimodal` · sierra
  Launch writeup for Sierra voice agents with useful architecture details on interruptions, latency, call-center integration, escalation, and multi-channel agent reuse.
- **2026-05-12** — [Visual Attachments: A new dimension for chat agents](<../models/multimodal/Visual Attachments A new dimension for chat agents.md>) · `multimodal` · sierra
  Covers visual attachments in chat agents and how images expand support-agent context and user interaction patterns.
- **2026-04-28** — [How to earn stakeholder trust with evals and observability](<../evals-observability/monitoring/How to earn stakeholder trust with evals and observability.md>) · `monitoring` · braintrust
  Explains how evals and observability help build stakeholder trust by making AI product quality measurable, reviewable, and improvable.
- **2026-04-23** — [An update on recent Claude Code quality reports](<../evals-observability/monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-23** — [How to Use Transformers.js in a Chrome Extension](<../infra-platform/edge/How to Use Transformers.js in a Chrome Extension.md>) · `edge` · huggingface
  Practical guide to running Transformers.js models inside a Chrome Manifest V3 extension: a background service worker hosts the model, a side panel provides the chat UI, and a content script handles page-level actions, with message passing between them. Covers the MV3 gotchas — service-worker lifecycle/termination, model loading and caching, and streaming tokens across the messaging boundary.
- **2026-04-21** — [AI to Human Agent Handoff Best Practices](<../agents/planning/AI to Human Agent Handoff Best Practices.md>) · `planning` · cresta
  Covers best practices for AI-to-human handoffs, including when agents should escalate and how handoff context should be preserved.
- **2026-04-20** — [Orchestrating AI Code Review at scale](<../agents/multi-agent/Orchestrating AI Code Review at scale.md>) · `multi-agent` · cloudflare-ai
  Deep dive into Cloudflare's CI-native AI code review built on OpenCode: up to seven specialized reviewer agents (security, performance, quality, docs, compliance) plus a coordinator that deduplicates findings and posts one structured review, run across tens of thousands of GitLab merge requests via a plugin architecture.
- **2026-04-15** — [Autoresearch isn’t just for training models (2026)](<../agents/harness/Autoresearch isn’t just for training models (2026).md>) · `harness` · shopify
  Shopify's internal 'autoresearch' harness: an agentic loop that runs experiments, evaluates results, and iterates autonomously on ML side-projects and dev-productivity problems, framed around a real CI-fixing story.
- **2026-04-01** — [The Rage Clicks of LLM apps: High-Signal Production Monitoring for AI Customer Support Agents](<../evals-observability/monitoring/The Rage Clicks of LLM apps High-Signal Production Monitoring for AI Customer Support Agents.md>) · `monitoring` · langfuse
  Detailed production-monitoring pattern for AI customer-support agents using high-signal LLM-as-judge classifiers to detect rage-click-like failure modes.
- **2026-03-24** — [Harness design for long-running application development](<../agents/harness/Harness design for long-running application development.md>) · `harness` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-03-20** — [Debugging Python memory issues in production with memray and AI](<../evals-observability/monitoring/Debugging Python memory issues in production with memray and AI.md>) · `monitoring` · pydantic
  Debugging recurring Kubernetes OOM kills on a production Python service using memray heap profiling plus AI-assisted analysis to trace the leak to specific request patterns.
- **2026-03-18** — [pydantic-deep: Production Deep Agents for Pydantic AI | Vstorm](<../agents/harness/pydantic-deep Production Deep Agents for Pydantic AI Vstorm.md>) · `harness` · pydantic
  Guest post from Vstorm introducing pydantic-deep, a 'deep agents' framework on Pydantic AI (an alternative to LangChain's deepagents) covering the production patterns: planning/progress tracking, filesystem as a first-class abstraction, sub-agent task delegation, sandboxed code execution in Docker, context summarization, and human-in-the-loop approval, with a full example app using per-user containers and WebSocket streaming.
- **2026-03-13** — [How We Built an Agent Skill to Synthesize what Langfuse Users want](<../agents/tool-use/How We Built an Agent Skill to Synthesize what Langfuse Users want.md>) · `tool-use` · langfuse
  Case study of building an agent skill to synthesize user feedback and product needs, showing how agents can support operational product workflows.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<../agents/tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-02-26** — [Building frontend UIs with Codex and Figma | OpenAI Developers](<../agents/tool-use/Building frontend UIs with Codex and Figma OpenAI Developers.md>) · `tool-use` · openai-devs
  Announces bidirectional Codex-Figma integration via the Figma MCP server: get_design_context extracts layouts/styles/components from Figma frames for code generation, and generate_figma_design turns a running UI back into editable Figma frames.
- **2026-02-25** — [AI Agent Debugging: Four Lessons from Shipping Alyx to Production](<../evals-observability/tracing/AI Agent Debugging Four Lessons from Shipping Alyx to Production.md>) · `tracing` · arize
  Case study from shipping Arize Alyx that distills debugging lessons around traces, failure analysis, context inspection, and production agent iteration.
- **2026-02-24** — [Alyx 2.0: The AI Agent That Actually Plans](<../agents/planning/Alyx 2.0 The AI Agent That Actually Plans.md>) · `planning` · arize
  Introduces Alyx 2.0 as an agent that plans over observability workflows, covering product design lessons from building a more capable AI analyst.
- **2026-02-19** — [Build Reliable AI Agents with Durable Execution | Pydantic AI + DBOS](<../agents/harness/Build Reliable AI Agents with Durable Execution Pydantic AI + DBOS.md>) · `harness` · pydantic
  Adds durable execution to Pydantic AI agents by layering DBOS (a lightweight Postgres-backed library) under the agent loop: workflow/step checkpointing resumes from the last completed step after crashes instead of restarting and re-burning tokens, plus database-backed durable queues; demoed on a deep-research agent.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<../agents/multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2026-01-22** — [E2E Test Debugging with Distributed Tracing | Pydantic Logfire](<../evals-observability/tracing/E2E Test Debugging with Distributed Tracing Pydantic Logfire.md>) · `tracing` · pydantic
  Using distributed tracing to debug failing E2E tests: propagating trace context through the system so a CI failure (e.g. a 500) can be localized to the API, database, or a downstream service instead of guessing from logs.
- **2025-12-09** — [Building Langfuse's MCP Server: Code Reuse and Developer Experience](<../agents/tool-use/Building Langfuse's MCP Server Code Reuse and Developer Experience.md>) · `tool-use` · langfuse
  Engineering writeup on building the Langfuse MCP server, focusing on code reuse, developer experience, and exposing observability workflows to agents.
- **2025-12-04** — [How We Built a State-of-the-Art Research Agent for Call Center Conversation Analytics](<../agents/planning/How We Built a State-of-the-Art Research Agent for Call Center Conversation Analytics.md>) · `planning` · cresta
  Detailed build story for a research agent over conversation analytics, covering agent design and domain-specific workflow constraints.
- **2025-11-25** — [Evals are a team sport: How we built Loop](<../evals-observability/testing/Evals are a team sport How we built Loop.md>) · `testing` · braintrust
  Describes collaborative eval workflows for teams, including feedback loops that turn production examples, review, and datasets into better AI behavior.
- **2025-11-24** — [Turn production data into better AI with Loop](<../evals-observability/monitoring/Turn production data into better AI with Loop.md>) · `monitoring` · braintrust
  Explains Loop as a way to turn production data into AI improvements through review, labeling, datasets, and feedback-driven iteration.
- **2025-10-21** — [LLM Testing: A Practical Guide to Automated Testing for LLM Applications](<../evals-observability/testing/LLM Testing A Practical Guide to Automated Testing for LLM Applications.md>) · `testing` · langfuse
  Practical guide to automated testing for LLM applications, covering test cases, regression checks, CI-style workflows, and quality gates.
- **2025-09-29** — [VibeGame: Exploring Vibe Coding Games](<../prompt-engineering/context-engineering/VibeGame Exploring Vibe Coding Games.md>) · `context-engineering` · huggingface
  Case study on why vibe-coded games fall apart as they grow: the context window fills and model performance degrades. Compares Roblox MCP, Unity MCP and web stacks for LLM-friendliness, and introduces Shallot, a lightweight /peel + /nourish context-management system for Claude Code, arguing for high-level abstractions (ECS/declarative) that keep the codebase small enough to fit in context.
- **2025-09-22** — [Why we built the Responses API | OpenAI Developers](<../agents/tool-use/Why we built the Responses API OpenAI Developers.md>) · `tool-use` · openai-devs
  OpenAI's design rationale for the Responses API as an agentic loop unifying Chat Completions and Assistants: it preserves reasoning state across turns (+5% on TAUBench, better cache utilization) and emits multiple output items — tool calls, structured outputs, intermediate steps — not just the final message.
- **2025-09-16** — [Inside Modal Notebooks: How we built a cloud GPU notebook that boots in seconds](<../infra-platform/deployment/Inside Modal Notebooks How we built a cloud GPU notebook that boots in seconds.md>) · `deployment` · modal
  Engineering writeup on cloud GPU notebooks that boot quickly, covering startup paths, state, and execution isolation.
- **2025-09-03** — [A/B testing can't keep up with AI](<../evals-observability/evaluation/AB testing can't keep up with AI.md>) · `evaluation` · braintrust
  Explains why traditional A/B testing is too slow for AI products and argues for eval-driven experimentation loops that compare model, prompt, and product changes before rollout.
- **2025-08-28** — [Claude Code vs Cursor: A Power-User’s Playbook](<../agents/tool-use/Claude Code vs Cursor A Power-User’s Playbook.md>) · `tool-use` · arize
  Compares Claude Code and Cursor from a power-user workflow perspective, focusing on coding-agent interfaces and usage patterns.
- **2025-08-14** — [More than Just a Model: How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency](<../inference/serving/More than Just a Model How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency.md>) · `serving` · cresta
  Explains production summarization architecture focused on low latency, adaptability, and precision rather than model choice alone.
- **2025-08-06** — [Introducing Open SWE: An Open-Source Asynchronous Coding Agent](<../agents/tool-use/Introducing Open SWE An Open-Source Asynchronous Coding Agent.md>) · `tool-use` · langchain
  Introduces Open SWE as an open-source asynchronous coding agent and discusses its architecture for long-running coding tasks.
- **2025-07-24** — [What is an AI code sandbox?](<../agents/computer-use/What is an AI code sandbox.md>) · `computer-use` · modal
  Explains AI code sandboxes as isolated execution environments for coding agents, including safety and state considerations.
- **2025-07-16** — [Leveraging multimodal LLMs for Shopify’s global catalogue: Recap of expo talk at ICLR 2025](<../models/multimodal/Leveraging multimodal LLMs for Shopify’s global catalogue Recap of expo talk at ICLR 2025.md>) · `multimodal` · shopify
  Shopify uses multimodal LLMs to standardize product data across its global catalogue, producing the high-quality structured attributes that agent-driven shopping ('show me sustainable running shoes') depends on.
- **2025-07-04** — [Augmented commerce: Machine learning at Shopify (2025)](<../industry/trends/Augmented commerce Machine learning at Shopify (2025).md>) · `trends` · shopify
  Overview of how ML is applied across Shopify's commerce platform ('augmented commerce'), framing the merchant ecosystem as the problem space for recommendation, search, and classification systems.
- **2025-05-28** — [How to Built an Elite Data Team Leveraging Pydantic AI](<../agents/multi-agent/How to Built an Elite Data Team Leveraging Pydantic AI.md>) · `multi-agent` · pydantic
  Guest post from Definite on building 'Fi', a data-engineering agent on Pydantic AI: uses multi-agent processes, per-run and per-instantiation model hot-swapping, tool whitelisting via 'prepare' functions to eliminate model distraction, query validation and error correction, with Logfire tracing latency and the agent's thought process.
- **2025-04-20** — [How to think about agent frameworks](<../agents/harness/How to think about agent frameworks.md>) · `harness` · langchain
  Framework for evaluating agent frameworks by abstraction level, control, durability, observability, and fit to production workflows.
- **2025-03-07** — [Prompt Management from First Principles](<../prompt-engineering/techniques/Prompt Management from First Principles.md>) · `techniques` · arize
  Frames prompt management from first principles, including versioning, ownership, and production workflow concerns.
- **2025-01-22** — [Building Audio Support with OpenAI: Insights from our Journey](<../models/multimodal/Building Audio Support with OpenAI Insights from our Journey.md>) · `multimodal` · arize
  Case study on adding audio support with OpenAI models, covering product and engineering lessons from building multimodal support.
- **2024-12-19** — [Building Effective AI Agents](<../agents/planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
- **2024-12-04** — [AI Agent Workflows and Architectures Masterclass](<../agents/harness/AI Agent Workflows and Architectures Masterclass.md>) · `harness` · arize
  Introduces practical agent workflow and architecture patterns, emphasizing simple tool-calling loops and design choices over vague autonomy claims.
- **2024-12-02** — [WireGuard at Modal: Static IPs for serverless containers](<../infra-platform/deployment/WireGuard at Modal Static IPs for serverless containers.md>) · `deployment` · modal
  Explains static IP support for serverless containers using WireGuard, relevant to secure networked AI deployments.
- **2024-11-11** — [How to Improve LLM Safety and Reliability](<../evals-observability/testing/How to Improve LLM Safety and Reliability.md>) · `testing` · arize
  Covers testing and monitoring practices for improving LLM application safety and reliability in production.
- **2024-11-04** — [Building serverless apps with the OpenAI Realtime API](<../models/multimodal/Building serverless apps with the OpenAI Realtime API.md>) · `multimodal` · braintrust
  Guide to building serverless apps with the OpenAI Realtime API, focusing on real-time voice interaction architecture and deployment patterns.
- **2024-09-23** — [Should you use an LLM Proxy to Build your Application?](<../infra-platform/deployment/Should you use an LLM Proxy to Build your Application.md>) · `deployment` · langfuse
  Explains the LLM proxy pattern for AI applications, including provider abstraction, centralized logging, key management, routing, and governance tradeoffs.
- **2024-09-17** — [Building high-performance compound AI applications with MongoDB Atlas and Baseten](<../rag-retrieval/pipelines/Building high-performance compound AI applications with MongoDB Atlas and Baseten.md>) · `pipelines` · baseten
  Shows how to build high-performance compound AI applications with retrieval, orchestration, and model serving.
- **2024-08-16** — [Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges](<../evals-observability/llm-as-judge/Judging the Judges Evaluating Alignment and Vulnerabilities in LLMs-as-Judges.md>) · `llm-as-judge` · arize
  Analyzes vulnerabilities and alignment issues in LLM-as-judge systems, with implications for production evaluator design.
- **2024-08-14** — [Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1](<../rag-retrieval/pipelines/Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1.md>) · `pipelines` · fireworks
  End-to-end RAG application example using Astro, FastAPI, SurrealDB, and Llama 3.1.
- **2024-07-31** — [Google releases Gemma 2 2B, ShieldGemma and Gemma Scope](<../models/releases/Google releases Gemma 2 2B, ShieldGemma and Gemma Scope.md>) · `releases` · huggingface
  Google's July 2024 Gemma drop: Gemma 2 2B distilled from larger models for on-device use, ShieldGemma safety classifiers for filtering app inputs/outputs, and Gemma Scope sparse autoencoders for interpretability.
- **2024-05-24** — [CyberSecEval 2 - A Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models](<../evals-observability/benchmark-design/CyberSecEval 2 - A Comprehensive Evaluation Framework for Cybersecurity Risks and Capabilities of Large Language Models.md>) · `benchmark-design` · huggingface
  CyberSecEval 2 evaluates LLM cybersecurity risk: prompt injection, code interpreter abuse, offensive-security capability and insecure-code generation, plus a false-refusal-rate metric that quantifies the safety/helpfulness tradeoff.
- **2024-05-01** — [Regression Testing with LangSmith](<../evals-observability/testing/Regression Testing with LangSmith.md>) · `testing` · langchain
  Explains regression testing with LangSmith for preventing LLM application quality regressions during prompt, model, or code changes.
- **2024-04-30** — [CI-CD for AI model deployments](<../infra-platform/deployment/CI-CD for AI model deployments.md>) · `deployment` · baseten
  Covers CI/CD practices for AI model deployments, including versioning, release flow, and operational safety.
- **2024-04-17** — [Eval feedback loops](<../evals-observability/evaluation/Eval feedback loops.md>) · `evaluation` · braintrust
  Explains eval feedback loops where production observations and human review continuously improve prompts, datasets, and model behavior.
- **2024-03-24** — [Trace complex LLM applications with the Langfuse decorator (Python)](<../evals-observability/tracing/Trace complex LLM applications with the Langfuse decorator (Python).md>) · `tracing` · langfuse
  Shows how to trace complex Python LLM applications with the Langfuse decorator, including nested calls, metadata, and observability patterns for multi-step workflows.
- **2024-03-14** — [Lambda on hard mode: Inside Modal's web infrastructure](<../infra-platform/deployment/Lambda on hard mode Inside Modal's web infrastructure.md>) · `deployment` · modal
  Deep dive into Modal web infrastructure, including serverless HTTP routing, isolation, and platform architecture.
- **2024-03-11** — [Iterating Towards LLM Reliability with Evaluation Driven Development](<../evals-observability/testing/Iterating Towards LLM Reliability with Evaluation Driven Development.md>) · `testing` · langchain
  Explains evaluation-driven development for LLM reliability using regression tests, examples, and iterative quality gates.
- **2024-02-23** — [Introducing the Red-Teaming Resistance Leaderboard](<../evals-observability/benchmark-design/Introducing the Red-Teaming Resistance Leaderboard.md>) · `benchmark-design` · huggingface
  The Red-Teaming Resistance Leaderboard scores frontier LLMs on robustness against adversarial prompts drawn from real red-teaming datasets (AdvBench, AART, HarmBench, Beavertails, plus Haize's own attacks), reporting attack success rates per harm category rather than a single safety number.
- **2024-02-08** — [From OpenAI to Open LLMs with Messages API on Hugging Face](<../inference/serving/From OpenAI to Open LLMs with Messages API on Hugging Face.md>) · `serving` · huggingface
  TGI 1.4 adds an OpenAI Chat Completions-compatible Messages API, so open models on Inference Endpoints become a drop-in swap for GPT-4 by only changing base_url and api_key — shown with the OpenAI Python/JS clients, LangChain and LlamaIndex, and a Nous-Hermes-2-Mixtral migration.
- **2024-01-26** — [An Introduction to AI Secure LLM Safety Leaderboard](<../evals-observability/benchmark-design/An Introduction to AI Secure LLM Safety Leaderboard.md>) · `benchmark-design` · huggingface
  The AI Secure LLM Safety Leaderboard runs the DecodingTrust benchmark, scoring models across eight trustworthiness axes (toxicity, stereotype bias, adversarial and out-of-distribution robustness, privacy leakage, machine ethics, fairness) rather than capability alone.
- **2023-11-27** — [Open sourcing the AI proxy](<../infra-platform/deployment/Open sourcing the AI proxy.md>) · `deployment` · braintrust
  Open-source AI proxy notes focused on provider routing, logging, credentials, access control, and observability for model calls.
- **2023-11-20** — [AI proxy: fostering a more open ecosystem](<../infra-platform/deployment/AI proxy fostering a more open ecosystem.md>) · `deployment` · braintrust
  Introduces an AI proxy pattern for routing model calls across providers while centralizing logging, credentials, access control, and production visibility.
- **2023-10-10** — [Multimodality and Large Multimodal Models (LMMs)](<../models/multimodal/Multimodality and Large Multimodal Models (LMMs).md>) · `multimodal` · chip-huyen
  Explains large multimodal model architecture and training patterns, modality fusion, data challenges, and product capabilities unlocked by image, text, audio, and video models.
- **2023-09-12** — [It's time to build reliable AI](<../evals-observability/evaluation/It's time to build reliable AI.md>) · `evaluation` · braintrust
  Early argument for reliable AI systems built around evals, logging, feedback loops, and engineering practices rather than ad hoc demos.
- **2023-05-17** — [Evaluating Model Fairness](<../evals-observability/evaluation/Evaluating Model Fairness.md>) · `evaluation` · arize
  Explains model fairness evaluation and how to assess bias and fairness risks in production systems.
- **2023-02-17** — [Technical deep dive: Truss live reload](<../infra-platform/deployment/Technical deep dive Truss live reload.md>) · `deployment` · baseten
  Technical deep dive into Truss live reload and faster model-server development loops.
- **2023-01-08** — [Self-serve feature platforms: architectures and APIs](<../infra-platform/deployment/Self-serve feature platforms architectures and APIs.md>) · `deployment` · chip-huyen
  Breaks down self-serve feature-platform architecture and APIs, covering feature definitions, pipelines, storage, discovery, and ergonomics for ML teams that need reusable production features.
- **2022-08-03** — [Introduction to streaming for data scientists](<../infra-platform/deployment/Introduction to streaming for data scientists.md>) · `deployment` · chip-huyen
  Introduces stream processing for ML systems, comparing batch and streaming architectures, event-time semantics, joins, windows, and why streaming underpins real-time features.
- **2022-02-07** — [Data Distribution Shifts and Monitoring](<../evals-observability/monitoring/Data Distribution Shifts and Monitoring.md>) · `monitoring` · chip-huyen
  Taxonomy of covariate, label, and concept shifts with production monitoring strategies, data-quality checks, slice analysis, alerting tradeoffs, and examples of real-world ML failure modes.
- **2021-09-13** — [Why data scientists shouldn’t need to know Kubernetes](<../infra-platform/deployment/Why data scientists shouldn’t need to know Kubernetes.md>) · `deployment` · chip-huyen
  Argues that data scientists should consume self-serve infrastructure abstractions rather than raw Kubernetes, outlining platform requirements for development, deployment, and operational ownership.
- **2021-01-29** — [How We Reduced Our Labeling Cost by 10x](<../evals-observability/evaluation/How We Reduced Our Labeling Cost by 10x.md>) · `evaluation` · cresta
  Explains how labeling costs were reduced through process and model-assisted annotation changes, relevant to eval dataset operations.
