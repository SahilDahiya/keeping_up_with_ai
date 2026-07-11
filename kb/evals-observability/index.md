# evals-observability

5 articles.

- **2026-04-23** — [An update on recent Claude Code quality reports](<monitoring/An update on recent Claude Code quality reports.md>) · `monitoring` · anthropic-engineering
  Follow-up on Claude Code quality regression reports: how the issues were traced, what infrastructure changes caused them, and monitoring added to catch recurrence.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<evaluation/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `evaluation` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<evaluation/Quantifying infrastructure noise in agentic coding evals.md>) · `evaluation` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-21** — [Designing AI resistant technical evaluations](<testing/Designing AI resistant technical evaluations.md>) · `testing` · anthropic-engineering
  How Anthropic designs technical hiring evaluations that stay meaningful when candidates have AI assistance, favoring debugging and judgment over greenfield coding.
- **2026-01-09** — [Demystifying evals for AI agents](<evaluation/Demystifying evals for AI agents.md>) · `evaluation` · anthropic-engineering
  A practical framework for building agent evals: grader design, task suites, pass@k metrics, and evolving evals as agent capabilities improve.

## Also relevant (filed elsewhere)

- **2025-09-17** — [A postmortem of three recent issues](<../inference/serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-06-13** — [How we built our multi-agent research system](<../agents/multi-agent/How we built our multi-agent research system.md>) · `multi-agent` · anthropic-engineering
  How Anthropic built Claude's Research feature on an orchestrator-worker multi-agent architecture, with prompting lessons, token economics, and eval methodology.
