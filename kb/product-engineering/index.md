# product-engineering

5 articles.

- **2026-05-25** — [How we contain Claude across products](<security/How we contain Claude across products.md>) · `security` · anthropic-engineering
  Anthropic's layered containment architecture for Claude's code execution and browsing across products: sandboxes, egress control, and per-surface trust boundaries.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-03-25** — [How we built Claude Code auto mode: a safer way to skip permissions](<security/How we built Claude Code auto mode a safer way to skip permissions.md>) · `security` · anthropic-engineering
  Design of Claude Code auto mode: sandboxing plus permission heuristics that let the agent act without per-action approval while bounding blast radius.
- **2025-10-20** — [Making Claude Code more secure and autonomous with sandboxing](<security/Making Claude Code more secure and autonomous with sandboxing.md>) · `security` · anthropic-engineering
  Introduces sandboxed bash execution and filesystem/network isolation in Claude Code, reducing permission prompts while containing what the agent can touch.
- **2025-06-26** — [Claude Desktop Extensions: One-click MCP server installation for Claude Desktop](<ux-patterns/Claude Desktop Extensions One-click MCP server installation for Claude Desktop.md>) · `ux-patterns` · anthropic-engineering
  Introduces Desktop Extensions (.dxt): a packaging format for one-click installation of local MCP servers in Claude Desktop, with manifest spec and distribution details.

## Also relevant (filed elsewhere)

- **2026-04-23** — [An update on recent Claude Code quality reports](<../evals-observability/monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-03-24** — [Harness design for long-running application development](<../agents/planning/Harness design for long-running application development.md>) · `planning` · anthropic-engineering
  Deep dive on harness design for multi-day application builds: state management, verification loops, task queues, and recovery when the agent goes off track.
- **2026-02-05** — [Building a C compiler with a team of parallel Claudes](<../agents/multi-agent/Building a C compiler with a team of parallel Claudes.md>) · `multi-agent` · anthropic-engineering
  Case study orchestrating a team of parallel Claude instances to build a working C compiler, covering task decomposition, shared state, and verification loops.
- **2024-12-19** — [Building Effective AI Agents](<../agents/planning/Building Effective AI Agents.md>) · `planning` · anthropic-engineering
  Anthropic's canonical guide to agent design patterns: when to use workflows (prompt chaining, routing, orchestrator-workers) versus autonomous agents, and why simple composable patterns beat frameworks.
