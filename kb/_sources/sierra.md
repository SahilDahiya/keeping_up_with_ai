# sierra

41 articles.

- **2026-07-22** — [Building Sierra’s MCP Gateway: An engineering iceberg](<../product-engineering/security/Building Sierra’s MCP Gateway An engineering iceberg.md>) · `security` · sierra
  Lessons from building Sierra's internal MCP gateway: a 'grab the lock' single-owner model for coordination, coding agents that cheat verification (reading tokens directly, falling back to curl) requiring weaker consumer agents for smoke tests, and a three-pass deterministic-plus-two-model pipeline that blocks cross-customer data access with an audit log.
- **2026-07-15** — [Pinecone: Harnessing the wisdom of the workforce](<../agents/harness/Pinecone Harnessing the wisdom of the workforce.md>) · `harness` · sierra
  Describes Sierra's internal cloud-agent platform Pinecone: an app server plus 'Agency' control plane that reconciles Kubernetes pods and Redis Streams for durable, resumable sessions, a Go runner supervising Codex/Claude Code, network-proxy credential injection so the agent never sees real tokens, and copy-on-write session forking/branching for multiplayer collaboration.
- **2026-07-10** — [AI-pilling our company: lessons learned](<../product-engineering/case-studies/AI-pilling our company lessons learned.md>) · `case-studies` · sierra
  Internal adoption case study on spreading AI workflows through a company, including practical lessons for using agents and tools in day-to-day work.
- **2026-06-30** — [Let your customers shape your agents](<../evals-observability/evaluation/Let your customers shape your agents.md>) · `evaluation` · sierra
  Explains experimentation loops for agent improvement, using customer behavior, A/B tests, and statistical confidence to shape agent changes.
- **2026-05-28** — [AI-native product localization](<../product-engineering/architecture/AI-native product localization.md>) · `architecture` · sierra
  Case study of AI-native product localization, covering workflows for translating and adapting product surfaces with model assistance.
- **2026-05-18** — [Voice AI is only as good as what it hears](<../models/multimodal/Voice AI is only as good as what it hears.md>) · `multimodal` · sierra
  Explains why voice-agent quality depends on transcription accuracy and how hearing failures propagate into agent behavior.
- **2026-05-13** — [Tau-Knowledge: benchmarking agents on realistic knowledge](<../evals-observability/benchmark-design/Tau-Knowledge benchmarking agents on realistic knowledge.md>) · `benchmark-design` · sierra
  Introduces tau-knowledge for benchmarking agents on realistic knowledge tasks that require grounded retrieval and use of external information.
- **2026-05-12** — [Sierra Agent OS 2.0: from answers to memory and action](<../agents/memory-context/Sierra Agent OS 2.0 from answers to memory and action.md>) · `memory-context` · sierra
  Describes Agent OS 2.0 moving agents from answers to memory and action, covering persistent context, tool use, and stateful behavior.
- **2026-05-12** — [Explorer: The agent-optimizing agent](<../agents/planning/Explorer The agent-optimizing agent.md>) · `planning` · sierra
  Introduces Explorer as an agent-optimizing agent that analyzes conversations and identifies improvement opportunities for deployed agents.
- **2026-05-12** — [Shipping and scaling AI agents](<../agents/planning/Shipping and scaling AI agents.md>) · `planning` · sierra
  Practical guide to shipping and scaling AI agents, including lifecycle, reliability, deployment, and continuous improvement concerns.
- **2026-05-12** — [The Agent Development Life Cycle](<../agents/planning/The Agent Development Life Cycle.md>) · `planning` · sierra
  Defines an agent development lifecycle from design and simulation through evaluation, deployment, monitoring, and continuous improvement.
- **2026-05-12** — [Mu-Bench: an open multilingual transcription benchmark](<../models/benchmarks/Mu-Bench an open multilingual transcription benchmark.md>) · `benchmarks` · sierra
  Introduces mu-Bench, an open multilingual transcription benchmark for evaluating speech recognition quality across languages.
- **2026-05-12** — [Improving voice performance with post-training](<../models/fine-tuning/Improving voice performance with post-training.md>) · `fine-tuning` · sierra
  Describes post-training techniques for improving voice model performance and agent interaction quality.
- **2026-05-12** — [Building more human voice experiences](<../models/multimodal/Building more human voice experiences.md>) · `multimodal` · sierra
  Explains design and engineering considerations for more human voice-agent experiences, including timing, emotion, and conversational flow.
- **2026-05-12** — [Multilingual voice: building agents that speak to everyone](<../models/multimodal/Multilingual voice building agents that speak to everyone.md>) · `multimodal` · sierra
  Describes building multilingual voice agents, including speech recognition, language coverage, and user-experience considerations.
- **2026-05-12** — [Sierra speaks](<../models/multimodal/Sierra speaks.md>) · `multimodal` · sierra
  Launch writeup for Sierra voice agents with useful architecture details on interruptions, latency, call-center integration, escalation, and multi-channel agent reuse.
- **2026-05-12** — [Visual Attachments: A new dimension for chat agents](<../models/multimodal/Visual Attachments A new dimension for chat agents.md>) · `multimodal` · sierra
  Covers visual attachments in chat agents and how images expand support-agent context and user interaction patterns.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [Engineering low-latency voice agents](<../inference/optimization/Engineering low-latency voice agents.md>) · `optimization` · sierra
  Engineering note on low-latency voice agents, covering response-time constraints and optimization across speech and model serving.
- **2026-05-12** — [A more reliable inference layer for foundation models](<../inference/serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-05-12** — [Preserving agent behavior while serving LLMs reliably](<../inference/serving/Preserving agent behavior while serving LLMs reliably.md>) · `serving` · sierra
  Covers model failover for preserving agent behavior while serving LLMs reliably across model/provider disruptions.
- **2026-05-12** — [Context engineering: the key to great agents](<../prompt-engineering/context-engineering/Context engineering the key to great agents.md>) · `context-engineering` · sierra
  Explains context engineering for agents, including how the right knowledge, state, and instructions shape agent quality.
- **2026-05-12** — [Expert Answers: Turn everyday support conversations into compounding knowledge](<../rag-retrieval/pipelines/Expert Answers Turn everyday support conversations into compounding knowledge.md>) · `pipelines` · sierra
  Describes turning everyday support conversations into compounding knowledge, using agent interactions to improve knowledge bases and answers.
- **2026-05-12** — [Golden articles: Evaluating and improving search](<../rag-retrieval/search/Golden articles Evaluating and improving search.md>) · `search` · sierra
  Covers golden-article evaluation for search quality and how retrieval systems can be measured and improved for support agents.
- **2026-05-12** — [Meet Linnaeus and Darwin: Search models that drive higher resolution rates](<../rag-retrieval/search/Meet Linnaeus and Darwin Search models that drive higher resolution rates.md>) · `search` · sierra
  Introduces Sierra search models for improving support-agent resolution rates through better knowledge retrieval and answer grounding.
- **2026-05-12** — [Tau-Bench: Benchmarking AI agents for the real-world](<../evals-observability/benchmark-design/Tau-Bench Benchmarking AI agents for the real-world.md>) · `benchmark-design` · sierra
  Introduces tau-Bench as a benchmark for real-world AI agents, focusing on task completion, tool use, and operational realism.
- **2026-05-12** — [Tau-Bench leaderboard: compare, explore, and understand agent performance](<../evals-observability/benchmark-design/Tau-Bench leaderboard compare, explore, and understand agent performance.md>) · `benchmark-design` · sierra
  Introduces a tau-Bench leaderboard for comparing and analyzing agent performance across benchmark tasks.
- **2026-05-12** — [Tau-Bench shaping development and evaluation agents](<../evals-observability/benchmark-design/Tau-Bench shaping development and evaluation agents.md>) · `benchmark-design` · sierra
  Explains how tau-bench shapes agent development and evaluation by providing realistic tasks and measurable behavior.
- **2026-05-12** — [Tau-Voice: benchmarking real-time voice agents](<../evals-observability/benchmark-design/Tau-Voice benchmarking real-time voice agents.md>) · `benchmark-design` · sierra
  Introduces tau-voice for benchmarking real-time voice agents on realistic tasks, including speech interaction and task-completion quality.
- **2026-05-12** — [Tau2-Bench](<../evals-observability/benchmark-design/Tau2-Bench.md>) · `benchmark-design` · sierra
  Introduces tau2-bench for evaluating agents in collaborative real-world scenarios where task success depends on interaction dynamics.
- **2026-05-12** — [Tau3-Bench: Advancing agent evaluation to knowledge and voice](<../evals-observability/benchmark-design/Tau3-Bench Advancing agent evaluation to knowledge and voice.md>) · `benchmark-design` · sierra
  Introduces tau3-Bench for extending agent evaluation to knowledge and voice tasks, expanding beyond text-only transactional benchmarks.
- **2026-05-12** — [Insights 2.0: AI that improves your AI](<../evals-observability/monitoring/Insights 2.0 AI that improves your AI.md>) · `monitoring` · sierra
  Describes using AI-generated insights from production conversations to improve deployed agents and surface recurring issues.
- **2026-05-12** — [Who monitors the monitors?](<../evals-observability/monitoring/Who monitors the monitors.md>) · `monitoring` · sierra
  Discusses monitoring AI agents and the meta-problem of monitoring the monitors, with emphasis on operational feedback and quality controls.
- **2026-05-12** — [How Voice Sims work](<../evals-observability/testing/How Voice Sims work.md>) · `testing` · sierra
  Explains how voice simulations test agents before production by generating realistic spoken interactions and edge cases.
- **2026-05-12** — [Simulations: the secret behind every great agent](<../evals-observability/testing/Simulations the secret behind every great agent.md>) · `testing` · sierra
  Explains simulation as a testing strategy for agents, using realistic scenarios to validate behavior before customer deployment.
- **2026-05-12** — [Voice Sims: testing real conversations before real customers](<../evals-observability/testing/Voice Sims testing real conversations before real customers.md>) · `testing` · sierra
  Explains voice simulations for testing agents under real-world speech conditions before production customer calls.
- **2026-05-12** — [Agent Traces: getting to the fix, fast](<../evals-observability/tracing/Agent Traces getting to the fix, fast.md>) · `tracing` · sierra
  Introduces agent traces as a debugging workflow for finding failures quickly across conversations, tools, and agent decisions.
- **2026-05-12** — [Load testing: how Sierra scales for surges](<../infra-platform/deployment/Load testing how Sierra scales for surges.md>) · `deployment` · sierra
  Explains load testing for agent systems so conversation serving can scale through traffic surges without quality or latency collapse.
- **2026-05-12** — [From LLMs to enterprise-grade agents](<../product-engineering/architecture/From LLMs to enterprise-grade agents.md>) · `architecture` · sierra
  Explains what distinguishes enterprise-grade agents from raw LLMs, including integrations, policy controls, reliability, and operational lifecycle.
- **2026-05-12** — [Industry first: PCI-compliant agents](<../product-engineering/security/Industry first PCI-compliant agents.md>) · `security` · sierra
  Explains PCI-compliant payment workflows for agents, focusing on secure action-taking and sensitive-data handling.
- **2026-05-12** — [Meet the Voice Sommelier](<../product-engineering/ux-patterns/Meet the Voice Sommelier.md>) · `ux-patterns` · sierra
  Explains voice-agent experience design, including brand voice selection, vocal cues, conversation design, and metrics for acceptance and satisfaction.
