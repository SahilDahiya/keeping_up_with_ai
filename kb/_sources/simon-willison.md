# simon-willison

12 articles.

- **2026-07-21** — [A Fireside Chat with Cat and Thariq from the Claude Code team](<../agents/harness/A Fireside Chat with Cat and Thariq from the Claude Code team.md>) · `harness` · simon-willison
  Transcript of a fireside chat with Anthropic's Claude Code team covering Claude Tag's proactive multiplayer Slack agent with team memory (65% of product-eng PRs), a six-month migration to letting Claude fully review PRs at the 'outer layers' backed by incident-driven eval sets, an 80% system-prompt size cut for Fable/Opus 4.8 (fewer examples and hard constraints, more context), and how auto mode was red-teamed against prompt injection before becoming Claude Tag's foundation.
- **2026-07-16** — [Inkling: Our open-weights model](<../models/releases/Inkling Our open-weights model.md>) · `releases` · simon-willison
  Simon Willison covers Thinking Machines Lab's first open-weights release, Inkling: a 975B-parameter (41B active) Apache-2.0 MoE transformer trained on 45T multimodal tokens, positioned as a fine-tuning base for their Tinker platform rather than a frontier model, plus a promised smaller Inkling-Small variant.
- **2026-07-16** — [Kimi K3, and what we can still learn from the pelican benchmark](<../models/releases/Kimi K3, and what we can still learn from the pelican benchmark.md>) · `releases` · simon-willison
  Simon Willison reviews Moonshot AI's Kimi K3 (2.8T parameters, open weights promised July 27, 2026), covering its Artificial Analysis benchmark standing (Elo 1547, +732 over K2.6), its $3/$15 per-million-token pricing, and revisits his informal 'pelican riding a bicycle' SVG test as an ad hoc capability check.
- **2026-07-15** — [xai-org/grok-build, now open source](<../agents/harness/xai-orggrok-build, now open source.md>) · `harness` · simon-willison
  Covers xAI open-sourcing its 844K-line Rust 'Grok Build' coding-agent CLI after backlash over it silently uploading users' entire home directories to Google Cloud; digs into the released source for its system/subagent prompts and tool implementations that were ported from Codex (apply_patch, grep_files) and OpenCode (bash, edit, glob).
- **2026-07-15** — [How I tricked Claude into leaking your deepest, darkest secrets](<../product-engineering/security/How I tricked Claude into leaking your deepest, darkest secrets.md>) · `security` · simon-willison
  Explains how researcher Ayush Paul bypassed Claude's web_fetch exfiltration protections (which restrict navigation to user- or search-provided URLs) by having a honeypot site serve nested links that the tool would follow, letting an attacker exfiltrate a user's name, city, and employer letter-by-letter; Anthropic closed the hole by disallowing navigation to links found within fetched content.
- **2026-07-09** — [The new GPT-5.6 family: Luna, Terra, Sol](<../models/releases/The new GPT-5.6 family Luna, Terra, Sol.md>) · `releases` · simon-willison
  Notes on the GPT-5.6 Luna, Terra, and Sol release, including pricing, million-token context, agentic benchmark claims, SWE-Bench Pro caveats, programmatic tool calling, subagents, and prompt-cache breakpoints.
- **2026-07-08** — [Rewriting Bun in Rust](<../product-engineering/case-studies/Rewriting Bun in Rust.md>) · `case-studies` · simon-willison
  Case study of an agent-assisted Bun rewrite from Zig to Rust using a large conformance test suite, dynamic workflows, adversarial review, and process-level fixes to build confidence in LLM-authored code.
- **2026-07-05** — [sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)](<../agents/tool-use/sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25).md>) · `tool-use` · simon-willison
  Case study of using Claude Fable and GPT-5.5 to review and harden a sqlite-utils release, including release-blocking bug discovery, cross-model review, subagent cost accounting, and agent-written release notes.
- **2026-07-04** — [Better Models: Worse Tools](<../agents/tool-use/Better Models Worse Tools.md>) · `tool-use` · simon-willison
  Short analysis of newer coding models producing malformed arguments for third-party edit tools, raising the issue that tool schemas and edit mechanisms may need model-specific evaluation and adaptation.
- **2026-07-03** — [Fable's judgement](<../agents/multi-agent/Fable's judgement.md>) · `multi-agent` · simon-willison
  Practical coding-agent pattern for delegating implementation work to cheaper subagents while reserving the main model for judgment, review, synthesis, and model-selection decisions.
- **2026-07-02** — [Release: llm-coding-agent 0.1a0](<../agents/tool-use/Release llm-coding-agent 0.1a0.md>) · `tool-use` · simon-willison
  Release and implementation notes for a Claude Code-style coding agent built on Simon Willison's LLM framework, including file-editing, command execution, search, read, and write tools plus approval modes.
- **2026-06-30** — [What’s new in Claude Sonnet 5](<../models/releases/What’s new in Claude Sonnet 5.md>) · `releases` · simon-willison
  Developer-focused notes on Claude Sonnet 5 covering adaptive thinking defaults, removed sampling parameters, million-token context, pricing/tokenizer changes, and comparative tokenization cost across document types.
