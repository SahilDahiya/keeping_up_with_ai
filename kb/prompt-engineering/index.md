# prompt-engineering

9 articles.

- **2026-06-26** — [Prompt Caching with Deep Agents](<context-engineering/Prompt Caching with Deep Agents.md>) · `context-engineering` · langchain
  Explains prompt caching for Deep Agents and how cache-aware context design reduces latency and cost for repeated agent work.
- **2026-03-20** — [Designing delightful frontends with GPT-5.4 | OpenAI Developers](<techniques/Designing delightful frontends with GPT-5.4 OpenAI Developers.md>) · `techniques` · openai-devs
  Prompting guide for steering GPT-5.4 toward non-generic frontend design: the model was trained for UI work, native image search/generation (e.g. prompt it to build mood boards first), and computer use for self-verification with tools like Playwright.
- **2026-02-16** — [Using Agent Skills to Automatically Improve your Prompts](<techniques/Using Agent Skills to Automatically Improve your Prompts.md>) · `techniques` · langfuse
  Shows how agent skills can automatically improve prompts, using evaluation feedback and reusable agent workflows to iterate on prompt quality.
- **2025-11-20** — [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](<context-engineering/CLAUDE.md Best Practices Learned from Optimizing Claude Code with Prompt Learning.md>) · `context-engineering` · arize
  Extracts CLAUDE.md best practices from prompt-learning experiments that optimized Claude Code behavior through repository instructions.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-09-29** — [Effective context engineering for AI agents](<context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2024-11-13** — [Promptim: an experimental library for prompt optimization](<techniques/Promptim an experimental library for prompt optimization.md>) · `techniques` · langchain
  Introduces Promptim as an experimental prompt-optimization library that uses evaluation feedback to improve prompts.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.

## Also relevant (filed elsewhere)

- **2026-05-28** — [Claude Code: Best practices for agentic coding](<../agents/tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-04-14** — [Classifying User Intent with Categorical LLM-as-a-Judge](<../evals-observability/evaluation/Classifying User Intent with Categorical LLM-as-a-Judge.md>) · `evaluation` · langfuse
  Shows how to classify user intent with categorical LLM-as-judge evaluators, including rubric design and structured scoring for production analysis.
- **2026-03-25** — [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](<../product-engineering/case-studies/How Perplexity Brought Voice Search to Millions Using the Realtime API OpenAI Developers.md>) · `case-studies` · openai-devs
  Perplexity's production lessons running Realtime-1.5 voice across Comet and Computer: feed context in 2,000-token chunks to avoid all-or-nothing truncation, get system/user/assistant role semantics right, standardize audio via a Rust SDK (48 kHz mono, WebRTC APM), and a 'voice lock' pattern for user pauses.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<../agents/tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-02-04** — [15 lessons learned building ChatGPT Apps | OpenAI Developers](<../product-engineering/ux-patterns/15 lessons learned building ChatGPT Apps OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Alpic distills 15 lessons from building two dozen ChatGPT Apps on the Apps SDK, centered on 'context asymmetry' between user, UI widget, and model — deciding which tool-output fields each party sees — and packaged into their open-source Skybridge framework.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<../agents/tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-27** — [Using Codex for education at Dagster Labs | OpenAI Developers](<../product-engineering/case-studies/Using Codex for education at Dagster Labs OpenAI Developers.md>) · `case-studies` · openai-devs
  Dagster Labs describes using Codex to accelerate documentation work — writing docs, translating content across mediums, and measuring doc completeness — and finds a well-structured CONTRIBUTING.md doubles as high-leverage scaffolding for the agent.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<../agents/tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-09-11** — [How to turn Claude Code into a domain specific coding agent](<../agents/tool-use/How to turn Claude Code into a domain specific coding agent.md>) · `tool-use` · langchain
  Shows how to turn Claude Code into a domain-specific coding agent using instructions, tools, context, and workflow constraints.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<../evals-observability/evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<../evals-observability/evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<../agents/tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<../product-engineering/architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2024-10-08** — [Functions: flexible AI engineering primitives](<../agents/tool-use/Functions flexible AI engineering primitives.md>) · `tool-use` · braintrust
  Introduces functions as flexible AI engineering primitives for tool calling, structured behavior, and reusable evaluation or workflow components.
- **2024-09-11** — [Composable Interventions for Language Models](<../models/reasoning/Composable Interventions for Language Models.md>) · `reasoning` · arize
  Deep dive on composable interventions for language models, covering techniques for steering or modifying model behavior.
- **2024-06-26** — [Aligning LLM-as-a-Judge with Human Preferences](<../evals-observability/evaluation/Aligning LLM-as-a-Judge with Human Preferences.md>) · `evaluation` · langchain
  Covers aligning LLM-as-judge evaluators with human preferences through calibration, examples, and evaluation design.
- **2023-12-05** — [Extraction Benchmarking](<../models/benchmarks/Extraction Benchmarking.md>) · `benchmarks` · langchain
  Benchmarking post for extraction tasks, comparing structured-output performance and evaluation approaches for information extraction.
