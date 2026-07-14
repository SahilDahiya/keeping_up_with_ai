# prompt-engineering

24 articles.

- **2026-06-26** — [Prompt Caching with Deep Agents](<context-engineering/Prompt Caching with Deep Agents.md>) · `context-engineering` · langchain
  Explains prompt caching for Deep Agents and how cache-aware context design reduces latency and cost for repeated agent work.
- **2026-05-12** — [Context engineering: the key to great agents](<context-engineering/Context engineering the key to great agents.md>) · `context-engineering` · sierra
  Explains context engineering for agents, including how the right knowledge, state, and instructions shape agent quality.
- **2026-04-30** — [Prompt templates as configs, not code](<context-engineering/Prompt templates as configs, not code.md>) · `context-engineering` · arize
  Argues for treating prompt templates as configuration, improving iteration, versioning, and deployment safety.
- **2026-03-20** — [Designing delightful frontends with GPT-5.4 | OpenAI Developers](<techniques/Designing delightful frontends with GPT-5.4 OpenAI Developers.md>) · `techniques` · openai-devs
  Prompting guide for steering GPT-5.4 toward non-generic frontend design: the model was trained for UI work, native image search/generation (e.g. prompt it to build mood boards first), and computer use for self-verification with tools like Playwright.
- **2026-02-16** — [Using Agent Skills to Automatically Improve your Prompts](<techniques/Using Agent Skills to Automatically Improve your Prompts.md>) · `techniques` · langfuse
  Shows how agent skills can automatically improve prompts, using evaluation feedback and reusable agent workflows to iterate on prompt quality.
- **2025-11-20** — [CLAUDE.md: Best Practices Learned from Optimizing Claude Code with Prompt Learning](<context-engineering/CLAUDE.md Best Practices Learned from Optimizing Claude Code with Prompt Learning.md>) · `context-engineering` · arize
  Extracts CLAUDE.md best practices from prompt-learning experiments that optimized Claude Code behavior through repository instructions.
- **2025-11-17** — [GEPA vs Prompt Learning: Benchmarking Different Prompt Optimization Approaches](<techniques/GEPA vs Prompt Learning Benchmarking Different Prompt Optimization Approaches.md>) · `techniques` · arize
  Benchmarks GEPA against prompt learning and frames prompt optimization as an eval-driven engineering loop.
- **2025-10-28** — [8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025)](<techniques/8 Top Prompt Testing and Optimization Tools for LLMs and Multiagent Systems (2025).md>) · `techniques` · arize
  Survey of prompt testing and optimization tools for LLM and multi-agent systems, focused on iteration workflows, evaluation support, and production prompt quality.
- **2025-09-29** — [Effective context engineering for AI agents](<context-engineering/Effective context engineering for AI agents.md>) · `context-engineering` · anthropic-engineering
  Strategies for managing agent context windows—compaction, structured note-taking, sub-agent architectures—and why context engineering supersedes prompt engineering.
- **2025-09-29** — [VibeGame: Exploring Vibe Coding Games](<context-engineering/VibeGame Exploring Vibe Coding Games.md>) · `context-engineering` · huggingface
  Case study on why vibe-coded games fall apart as they grow: the context window fills and model performance degrades. Compares Roblox MCP, Unity MCP and web stacks for LLM-friendliness, and introduces Shallot, a lightweight /peel + /nourish context-management system for Claude Code, arguing for high-level abstractions (ECS/declarative) that keep the codebase small enough to fit in context.
- **2025-08-20** — [Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain-of-Thought](<techniques/Evidence-Based Prompting Strategies for LLM-as-a-Judge Explanations and Chain-of-Thought.md>) · `techniques` · arize
  Examines prompting strategies for LLM-as-judge evaluators, including explanations and chain-of-thought design choices.
- **2025-07-18** — [Prompt Learning: Using English Feedback to Optimize LLM Systems](<techniques/Prompt Learning Using English Feedback to Optimize LLM Systems.md>) · `techniques` · arize
  Explains prompt learning driven by natural-language feedback as an optimization loop for LLM systems.
- **2025-03-17** — [Prompt Optimization Techniques](<techniques/Prompt Optimization Techniques.md>) · `techniques` · arize
  Covers few-shot prompting and prompt optimization techniques with an emphasis on measurable improvement.
- **2025-03-07** — [Prompt Management from First Principles](<techniques/Prompt Management from First Principles.md>) · `techniques` · arize
  Frames prompt management from first principles, including versioning, ownership, and production workflow concerns.
- **2025-02-01** — [From text to task: Constrained generation for structured extraction in R1](<structured-output/From text to task Constrained generation for structured extraction in R1.md>) · `structured-output` · fireworks
  Explains constrained generation for structured extraction with reasoning models and schema-bound outputs.
- **2024-12-23** — [Controlling Language Model Generation with NVIDIA's LogitsProcessorZoo](<structured-output/Controlling Language Model Generation with NVIDIA's LogitsProcessorZoo.md>) · `structured-output` · huggingface
  Uses NVIDIA's LogitsProcessorZoo to steer generation by editing the logit distribution directly: GenLengthLogitsProcessor to control answer length, CiteFromPromptLogitsProcessor to bias tokens toward the source passage (useful for RAG), ForceLastPhraseLogitsProcessor and MultipleChoiceLogitsProcessor for constrained answers.
- **2024-11-13** — [Promptim: an experimental library for prompt optimization](<techniques/Promptim an experimental library for prompt optimization.md>) · `techniques` · langchain
  Introduces Promptim as an experimental prompt-optimization library that uses evaluation feedback to improve prompts.
- **2024-09-12** — [How to build function calling and JSON mode for open-source and fine-tuned LLMs](<structured-output/How to build function calling and JSON mode for open-source and fine-tuned LLMs.md>) · `structured-output` · baseten
  Shows how to build function calling and JSON mode for open-source and fine-tuned LLMs.
- **2024-07-24** — [DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](<techniques/DSPy Assertions Computational Constraints for Self-Refining Language Model Pipelines.md>) · `techniques` · arize
  Explains DSPy assertions as computational constraints for self-refining language-model pipelines.
- **2024-04-30** — [Improving Prompt Consistency with Structured Generations](<structured-output/Improving Prompt Consistency with Structured Generations.md>) · `structured-output` · huggingface
  HF's leaderboards team and dottxt show that eval scores swing wildly with tiny prompt-format changes, and that forcing structured generation (Outlines' regex/JSON-constrained decoding) sharply reduces that variance across prompt formats on GSM8K-style tasks.
- **2024-04-04** — [Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B](<structured-output/Text2SQL using Hugging Face Dataset Viewer API and Motherduck DuckDB-NSQL-7B.md>) · `structured-output` · huggingface
  Text-to-SQL walkthrough using MotherDuck's DuckDB-NSQL-7B (Llama-2-7B fine-tuned on DuckDB SQL pairs) with the HF Dataset Viewer parquet API: schema-in-prompt templating, generation, and executing the SQL against DuckDB.
- **2024-02-20** — [Why do all LLMs need structured output modes?](<structured-output/Why do all LLMs need structured output modes.md>) · `structured-output` · fireworks
  Explains why structured-output modes matter for reliable LLM applications and tool-calling systems.
- **2024-01-31** — [Function calling and JSON mode](<structured-output/Function calling and JSON mode.md>) · `structured-output` · together
  Explains function calling and JSON mode for structured LLM application outputs.
- **2023-12-18** — [How to Prompt LLMs for Text-to-SQL](<structured-output/How to Prompt LLMs for Text-to-SQL.md>) · `structured-output` · arize
  Practical guide to Text-to-SQL prompting, including schema context, output constraints, and evaluation considerations.

## Also relevant (filed elsewhere)

- **2026-06-22** — [We got local models to triage the OpenClaw repo for FREE!*](<../agents/tool-use/We got local models to triage the OpenClaw repo for FREE!.md>) · `tool-use` · huggingface
  Uses local Gemma/Qwen models inside an agent harness with structured outputs to triage hundreds of daily OpenClaw issues/PRs on a 128GB NVIDIA GB10, replacing a quota-limited GPT-5/Opus workflow; covers label schema design, prompt iteration and accuracy vs closed models.
- **2026-05-28** — [Claude Code: Best practices for agentic coding](<../agents/tool-use/Claude Code Best practices for agentic coding.md>) · `tool-use` · anthropic-engineering
  Practical workflows for agentic coding with Claude Code: CLAUDE.md setup, explore-plan-code loops, test-driven iteration, headless automation, and multi-Claude patterns.
- **2026-05-25** — [Harness, Scaffold, and the AI Agent Terms Worth Getting Right](<../agents/tool-use/Harness, Scaffold, and the AI Agent Terms Worth Getting Right.md>) · `tool-use` · huggingface
  A working glossary that disentangles the overloaded agent vocabulary — model vs scaffolding vs harness vs agent, plus context engineering, policy, tool use, skills, sub-agents and orchestrators — using Claude Code, Codex and RL-environment framing as reference points. Defines 'harness engineering' (stop conditions, error handling, guardrails) and the eval-harness variant.
- **2026-05-11** — [Serving DeepSeek-V4: why million-token context is an inference systems problem](<../inference/serving/Serving DeepSeek-V4 why million-token context is an inference systems problem.md>) · `serving` · together
  Explains why million-token context serving is primarily an inference-systems problem.
- **2026-04-24** — [How we fixed prompt injection for all models on Fireworks](<../product-engineering/security/How we fixed prompt injection for all models on Fireworks.md>) · `security` · fireworks
  Explains a tokenizer-level prompt-injection fix and the implications for securing model-serving systems.
- **2026-04-14** — [Classifying User Intent with Categorical LLM-as-a-Judge](<../evals-observability/llm-as-judge/Classifying User Intent with Categorical LLM-as-a-Judge.md>) · `llm-as-judge` · langfuse
  Shows how to classify user intent with categorical LLM-as-judge evaluators, including rubric design and structured scoring for production analysis.
- **2026-03-25** — [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](<../product-engineering/case-studies/How Perplexity Brought Voice Search to Millions Using the Realtime API OpenAI Developers.md>) · `case-studies` · openai-devs
  Perplexity's production lessons running Realtime-1.5 voice across Comet and Computer: feed context in 2,000-token chunks to avoid all-or-nothing truncation, get system/user/assistant role semantics right, standardize audio via a Rust SDK (48 kHz mono, WebRTC APM), and a 'voice lock' pattern for user pauses.
- **2026-03-19** — [Managing Memory in AI Agents: Beyond the Context Window](<../agents/memory-context/Managing Memory in AI Agents Beyond the Context Window.md>) · `memory-context` · arize
  Covers memory and context-window management patterns for agents that need to preserve useful state over long tasks.
- **2026-03-09** — [Using skills to accelerate OSS maintenance | OpenAI Developers](<../agents/tool-use/Using skills to accelerate OSS maintenance OpenAI Developers.md>) · `tool-use` · openai-devs
  How OpenAI maintains the Agents SDK repos with repo-local Codex skills, AGENTS.md policy, and the Codex GitHub Action — turning verification, release prep, and PR review into repeatable progressive-disclosure workflows; merged PRs rose from 316 to 457 quarter-over-quarter.
- **2026-02-04** — [15 lessons learned building ChatGPT Apps | OpenAI Developers](<../product-engineering/ux-patterns/15 lessons learned building ChatGPT Apps OpenAI Developers.md>) · `ux-patterns` · openai-devs
  Alpic distills 15 lessons from building two dozen ChatGPT Apps on the Apps SDK, centered on 'context asymmetry' between user, UI widget, and model — deciding which tool-output fields each party sees — and packaged into their open-source Skybridge framework.
- **2025-12-04** — [Fine-tuning LLMs as classifiers](<../models/fine-tuning/Fine-tuning LLMs as classifiers.md>) · `fine-tuning` · fireworks
  Shows how to adapt generative LLMs for classification tasks while preserving probability outputs and efficient serving.
- **2025-11-05** — [Tool Calling in Inference](<../agents/tool-use/Tool Calling in Inference.md>) · `tool-use` · baseten
  Explains tool calling in inference and how model servers support structured external actions.
- **2025-11-04** — [Code execution with MCP: building more efficient AI agents](<../agents/tool-use/Code execution with MCP building more efficient AI agents.md>) · `tool-use` · anthropic-engineering
  Argues agents should write code that calls MCP tools rather than invoking tools directly, cutting token usage and enabling control flow over intermediate results.
- **2025-10-27** — [Using Codex for education at Dagster Labs | OpenAI Developers](<../product-engineering/case-studies/Using Codex for education at Dagster Labs OpenAI Developers.md>) · `case-studies` · openai-devs
  Dagster Labs describes using Codex to accelerate documentation work — writing docs, translating content across mediums, and measuring doc completeness — and finds a well-structured CONTRIBUTING.md doubles as high-leverage scaffolding for the agent.
- **2025-10-16** — [Equipping agents for the real world with Agent Skills](<../agents/tool-use/Equipping agents for the real world with Agent Skills.md>) · `tool-use` · anthropic-engineering
  Introduces Agent Skills: folder-based packages of instructions, scripts, and resources that agents load progressively to gain domain expertise on demand.
- **2025-10-14** — [Optimizing Coding Agent Rules (./clinerules) for Improved Accuracy](<../agents/computer-use/Optimizing Coding Agent Rules (.clinerules) for Improved Accuracy.md>) · `computer-use` · arize
  Explains how coding-agent rule files affect accuracy and how to optimize them for better agent behavior.
- **2025-09-11** — [How to turn Claude Code into a domain specific coding agent](<../agents/tool-use/How to turn Claude Code into a domain specific coding agent.md>) · `tool-use` · langchain
  Shows how to turn Claude Code into a domain-specific coding agent using instructions, tools, context, and workflow constraints.
- **2025-09-09** — [Building a Multilingual Cypher Query Evaluation Pipeline](<../evals-observability/evaluation/Building a Multilingual Cypher Query Evaluation Pipeline.md>) · `evaluation` · arize
  Walks through building a multilingual Cypher query evaluation pipeline for testing whether LLMs generate correct database queries across languages.
- **2025-09-03** — [AI Evals Maven Course Homework: the Recipe Bot Workflow](<../evals-observability/evaluation/AI Evals Maven Course Homework the Recipe Bot Workflow.md>) · `evaluation` · arize
  Walks through a recipe-bot homework workflow from an AI evals course, showing how to design tests and iterate on an LLM application.
- **2025-07-11** — [Function calling for agentic AI systems](<../agents/tool-use/Function calling for agentic AI systems.md>) · `tool-use` · fireworks
  Explains function calling as the bridge between LLM outputs, external tools, and agentic execution loops.
- **2025-05-28** — [CodeAgents + Structure: A Better Way to Execute Actions](<../agents/tool-use/CodeAgents + Structure A Better Way to Execute Actions.md>) · `tool-use` · huggingface
  Shows that making a CodeAgent emit its thoughts and code as structured JSON (rather than free-form markdown code blocks) beats both plain CodeAgents and JSON ToolCallingAgents on SmolBench (GAIA, MATH, SimpleQA, Frames), with the gain concentrated in larger models; smaller models can be hurt by the added format constraint.
- **2025-03-20** — [The "think" tool: Enabling Claude to stop and think](<../agents/tool-use/The think tool Enabling Claude to stop and think.md>) · `tool-use` · anthropic-engineering
  Adding a no-op 'think' tool gives Claude space for intermediate reasoning mid-task, significantly improving policy-heavy agentic benchmarks like tau-bench.
- **2025-02-26** — [Memory and State in LLM Applications](<../agents/memory-context/Memory and State in LLM Applications.md>) · `memory-context` · arize
  Explains memory and state patterns in LLM applications and how they affect reliability across interactions.
- **2025-01-16** — [Common pitfalls when building generative AI applications](<../product-engineering/architecture/Common pitfalls when building generative AI applications.md>) · `architecture` · chip-huyen
  Covers common generative-AI application pitfalls, including overusing LLMs, confusing product problems with model failures, premature framework complexity, and weak evaluation/product iteration.
- **2024-11-25** — [Long Context Fine-Tuning: A Technical Deep Dive](<../models/fine-tuning/Long Context Fine-Tuning A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into long-context fine-tuning.
- **2024-10-08** — [Functions: flexible AI engineering primitives](<../agents/tool-use/Functions flexible AI engineering primitives.md>) · `tool-use` · braintrust
  Introduces functions as flexible AI engineering primitives for tool calling, structured behavior, and reusable evaluation or workflow components.
- **2024-09-11** — [Composable Interventions for Language Models](<../models/reasoning/Composable Interventions for Language Models.md>) · `reasoning` · arize
  Deep dive on composable interventions for language models, covering techniques for steering or modifying model behavior.
- **2024-09-05** — [Speculative decoding for high-throughput long-context inference](<../inference/speculative-decoding/Speculative decoding for high-throughput long-context inference.md>) · `speculative-decoding` · together
  Explains speculative decoding for high-throughput long-context inference.
- **2024-08-29** — [Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction](<../agents/tool-use/Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction.md>) · `tool-use` · fireworks
  Tutorial for building a function-calling application with FastAPI, SerpAPI, and structured tool invocation.
- **2024-08-12** — [Tool Use, Unified](<../agents/tool-use/Tool Use, Unified.md>) · `tool-use` · huggingface
  Explains the unified tool-use API in Transformers chat templates: pass plain Python functions with typed signatures and docstrings and they are auto-converted to JSON schema, then rendered per-model by the model's Jinja chat template — plus the conventions chosen for tool-call and tool-result messages so tool-calling chats are portable across models that disagree on formats.
- **2024-06-26** — [Aligning LLM-as-a-Judge with Human Preferences](<../evals-observability/llm-as-judge/Aligning LLM-as-a-Judge with Human Preferences.md>) · `llm-as-judge` · langchain
  Covers aligning LLM-as-judge evaluators with human preferences through calibration, examples, and evaluation design.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<../inference/kernels/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `kernels` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-05-13** — [License to Call: Introducing Transformers Agents 2.0](<../agents/tool-use/License to Call Introducing Transformers Agents 2.0.md>) · `tool-use` · huggingface
  Transformers Agents 2.0 introduces ReAct-style CodeAgent and JsonAgent that iterate on past observations, with a code-writing action format, tool definitions and system prompts, benchmarked against LangChain agents.
- **2024-03-20** — [Cosmopedia: how to create large-scale synthetic data for pre-training Large Language Models](<../models/training/Cosmopedia how to create large-scale synthetic data for pre-training Large Language Models.md>) · `training` · huggingface
  How Cosmopedia was built: 30M synthetic textbooks/blogs/stories (25B tokens) generated with Mixtral-8x7B-Instruct to reproduce Phi-1.5's pretraining data, with most of the effort going into prompt curation for topic diversity — reaching <1% duplicate content — plus the clustering and generation stack used at scale.
- **2024-02-27** — [Evo: Long-context modeling from molecular to genome scale](<../models/reasoning/Evo Long-context modeling from molecular to genome scale.md>) · `reasoning` · together
  Explains Evo and long-context modeling from molecular to genome-scale sequences.
- **2024-01-11** — [Long context retrieval models with Monarch Mixer](<../rag-retrieval/search/Long context retrieval models with Monarch Mixer.md>) · `search` · together
  Explains long-context retrieval models using Monarch Mixer.
- **2023-12-05** — [Extraction Benchmarking](<../models/benchmarks/Extraction Benchmarking.md>) · `benchmarks` · langchain
  Benchmarking post for extraction tasks, comparing structured-output performance and evaluation approaches for information extraction.
- **2023-10-12** — [Flash-Decoding for long-context inference](<../inference/kernels/Flash-Decoding for long-context inference.md>) · `kernels` · together
  Introduces Flash-Decoding for efficient long-context inference.
- **2023-08-07** — [Extending the Context Window of LLaMA Models Paper Reading](<../models/reasoning/Extending the Context Window of LLaMA Models Paper Reading.md>) · `reasoning` · arize
  Explains techniques for extending LLaMA context windows and the tradeoffs involved in long-context model behavior.
- **2023-07-25** — [Lost in the Middle: How Language Models Use Long Contexts Paper Reading](<../models/reasoning/Lost in the Middle How Language Models Use Long Contexts Paper Reading.md>) · `reasoning` · arize
  Summarizes the Lost in the Middle findings on long-context model behavior and retrieval sensitivity.
- **2023-06-15** — [Three techniques to adapt LLMs for any use case](<../models/fine-tuning/Three techniques to adapt LLMs for any use case.md>) · `fine-tuning` · baseten
  Explains prompt engineering, fine-tuning, and related techniques for adapting LLMs to use cases.
