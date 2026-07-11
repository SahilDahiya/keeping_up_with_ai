# agents

11 articles.

- **2026-05-28** — [Claude Code: Best practices for agentic coding](<tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-03-24** — [Harness design for long-running application development](<planning/Harness design for long-running application development.md>) · `planning` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-11-24** — [Introducing advanced tool use on the Claude Developer Platform](<tool-use/Introducing advanced tool use on the Claude Developer Platform.md>) · `tool-use` · anthropic-engineering
  Introduces tool search, programmatic tool calling, and tool-use examples on the Claude Developer Platform to scale agents past context-window limits on large tool sets.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-09-11** — [Writing effective tools for AI agents—using AI agents](<tool-use/Writing effective tools for AI agents—using AI agents.md>) · `tool-use` · anthropic-engineering
  Guidance on designing tool interfaces agents use reliably—consolidating workflows, namespacing, returning meaningful context—and using Claude to optimize its own tools.
- **2025-06-13** — [How we built our multi-agent research system](<multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2024-12-19** — [Building Effective AI Agents](<planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.

## Also relevant (filed elsewhere)

- **2026-05-25** — [How we contain Claude across products](<../product-engineering/security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<../product-engineering/security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2026-01-09** — [Demystifying evals for AI agents](<../evals-observability/evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.
- **2025-11-26** — [Effective harnesses for long-running agents](<planning/Effective harnesses for long-running agents.md>) · `planning` · anthropic-engineering
  Harness patterns for agents that work over hours or days: initializer/coder agent split, checkpointing progress to files, and recovering from failure mid-run.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<../product-engineering/security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-09-29** — [Effective context engineering for AI agents](<../prompt-engineering/context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<../product-engineering/ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.
- **2025-01-06** — [Claude SWE-Bench Performance](<../models/benchmarks/Claude SWE-Bench Performance.md>) · `benchmarks` · anthropic-engineering
  How Anthropic scaffolded Claude 3.5 Sonnet to 49% on SWE-bench Verified with a minimal agent harness, detailing tool design and error analysis.
