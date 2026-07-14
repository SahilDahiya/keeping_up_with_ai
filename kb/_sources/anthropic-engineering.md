# anthropic-engineering

25 articles.

- **2026-05-28** — [Claude Code: Best practices for agentic coding](<../agents/tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-05-25** — [How we contain Claude across products](<../product-engineering/security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-04-23** — [An update on recent Claude Code quality reports](<../evals-observability/monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<../product-engineering/architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<../product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-03-24** — [Harness design for long-running application development](<../agents/harness/Harness design for long-running application development.md>) · `harness` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<../evals-observability/benchmark-design/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `benchmark-design` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<../agents/multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<../evals-observability/benchmark-design/Quantifying infrastructure noise in agentic coding evals.md>) · `benchmark-design` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-21** — [Designing AI resistant technical evaluations](<../evals-observability/testing/Designing AI resistant technical evaluations.md>) · `testing` · anthropic-engineering
  How Anthropic designs technical hiring evaluations that stay meaningful when candidates have AI assistance, favoring debugging and judgment over greenfield coding.
- **2026-01-09** — [Demystifying evals for AI agents](<../evals-observability/evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-11-26** — [Effective harnesses for long-running agents](<../agents/harness/Effective harnesses for long-running agents.md>) · `harness` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-24** — [Introducing advanced tool use on the Claude Developer Platform](<../agents/tool-use/Introducing advanced tool use on the Claude Developer Platform.md>) · `tool-use` · anthropic-engineering
  Introduces tool search, programmatic tool calling, and tool-use examples on the Claude Developer Platform to scale agents past context-window limits on large tool sets.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<../agents/tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<../product-engineering/security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<../agents/tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-09-29** — [Effective context engineering for AI agents](<../prompt-engineering/context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-09-17** — [A postmortem of three recent issues](<../inference/serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-11** — [Writing effective tools for AI agents—using AI agents](<../agents/tool-use/Writing effective tools for AI agents—using AI agents.md>) · `tool-use` · anthropic-engineering
  Guidance on designing tool interfaces agents use reliably—consolidating workflows, namespacing, returning meaningful context—and using Claude to optimize its own tools.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<../product-engineering/ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-06-13** — [How we built our multi-agent research system](<../agents/multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<../agents/tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2025-01-06** — [Claude SWE-Bench Performance](<../models/benchmarks/Claude SWE-Bench Performance.md>) · `benchmarks` · anthropic-engineering
  How Anthropic scaffolded Claude 3.5 Sonnet to 49% on SWE-bench Verified with a minimal agent harness, detailing tool design and error analysis.
- **2024-12-19** — [Building Effective AI Agents](<../agents/planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
- **2024-09-19** — [Contextual Retrieval in AI Systems](<../rag-retrieval/pipelines/Contextual Retrieval in AI Systems.md>) · `pipelines` · anthropic-engineering
  Introduces contextual retrieval: prepending chunk-situating context before embedding and BM25 indexing, cutting retrieval failure rates by 49% (67% with reranking).
