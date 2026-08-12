# fireworks

84 articles.

- **2026-08-10** — [Fireworks AI](<../models/architectures/Fireworks AI.md>) · `architectures` · fireworks
  Meta's Muse Glimmer is a 30B dense agentic model (52 layers, GQA with 32 query/2 KV heads, SwiGLU) using sliding-window attention over 2,048 tokens with a global attention layer every fourth layer, keeping the KV cache small enough to serve long-context, multi-step tool-calling agents economically at high concurrency.
- **2026-07-30** — [Three Tests to Run Before You Switch from LoRA to FullFT](<../models/fine-tuning/Three Tests to Run Before You Switch from LoRA to FullFT.md>) · `fine-tuning` · fireworks
  Controlled experiments on Qwen3.5-9B isolate which lever actually closes the LoRA-to-FullFT quality gap -- rank, learning-rate tuning, and training-data coverage -- finding that recipe/learning-rate tuning erases much of a naive fixed-recipe FullFT advantage, rank hits a ceiling on supported behaviors, and broader curriculum coverage is what moves results beyond it.
- **2026-07-29** — [Fine-Tune Your Own Embedding Model from an LLM — for the Price of a Coffee](<../rag-retrieval/embeddings/Fine-Tune Your Own Embedding Model from an LLM — for the Price of a Coffee.md>) · `embeddings` · fireworks
  Shows a sub-$10 recipe for contrastive fine-tuning of Qwen3-Embedding-8B (in-batch negatives, InfoNCE) on the Fireworks platform, lifting retrieval quality on domain tasks like legal citation retrieval (LegalBench, +36% nDCG@10), clinical trial matching, and EU case-law retrieval, while preserving general-purpose performance.
- **2026-07-26** — [Fireworks AI](<../models/fine-tuning/Fireworks AI.md>) · `fine-tuning` · fireworks
  Demonstrates LoRA post-training of Kimi K3 via Fireworks Serverless Training on two RL tasks, Countdown and Frozen Lake, showing how dense partial-credit rewards produce fast smooth learning curves versus sparse goal-only rewards, with a small RL run (~20 steps, 860K tokens) costing about $65.
- **2026-07-20** — [Heidi x Fireworks: Bridging the Gap in Frontier Model Performance](<../models/fine-tuning/Heidi x Fireworks Bridging the Gap in Frontier Model Performance.md>) · `fine-tuning` · fireworks
  Heidi's clinical-note scribe moved from closed frontier models to a two-stage pipeline (SFT to imitate style, then RFT/DPO for preference-based quality) on Fireworks, cutting latency from 25s to 7s and outperforming Gemini Flash/Pro tiers in side-by-side evals; success depended on high-quality filtered data and larger effective batch sizes.
- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<../inference/kernels/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `kernels` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-08** — [Best Open Source LLMs in 2026: We Reviewed 7 Models](<../models/benchmarks/Best Open Source LLMs in 2026 We Reviewed 7 Models.md>) · `benchmarks` · fireworks
  July 2026 snapshot comparing GLM 5.2, Kimi K3, Kimi K2.7 Code, DeepSeek-V4-Pro/Flash on benchmark quality, context window (up to 1,040k tokens), modality, and license terms for production model selection.
- **2026-06-26** — [How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks](<../agents/harness/How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks.md>) · `harness` · fireworks
  Factory's Droids run any coding model (frontier or open-weight) behind one harness that absorbs per-model differences in reasoning/tracing formats, tool schemas, and git-state handling; open-weight share of Factory's usage grew 2-3x in six months as models closed the capability gap at a fraction of frontier cost.
- **2026-06-26** — [Fireworks AI](<../models/reinforcement-learning/Fireworks AI.md>) · `reinforcement-learning` · fireworks
  Cursor's Composer 2, built on Kimi 2.5, is trained via continual pretraining and large-scale RL on long-horizon software engineering tasks; Fireworks provides distributed rollout/inference infra across 3-4 clusters with compressed weight sync, hitting 61.3 CursorBench and 6-10x lower inference cost than comparable frontier coding models.
- **2026-06-24** — [Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.](<../agents/multi-agent/Frontier AI at a fraction of the cost open-source worker agents with a closed-source advisor.md>) · `multi-agent` · fireworks
  Explains a worker-advisor pattern that combines open-source worker agents with closed-source advisors for cost-quality tradeoffs.
- **2026-06-12** — [MiniMax M3 is live: long context + native multimodality at 1/20th the price](<../models/architectures/MiniMax M3 is live long context + native multimodality at 120th the price.md>) · `architectures` · fireworks
  MiniMax M3's extended context comes from MSA (MiniMax Sparse Attention), which pre-filters and blocks KV caches with a 'KV outer gather Q' operator ordering that fetches each block once, delivering >4x speedup over Flash-Sparse-Attention/flash-moba, 95% lower per-token compute, and 9x/15x faster prefill/decode at 1M-token context versus M2.7.
- **2026-06-12** — [Kimi K2.7 Code on Fireworks: Better Agents, Lower Cost per Task, Available Day-0 | Fireworks](<../models/reasoning/Kimi K2.7 Code on Fireworks Better Agents, Lower Cost per Task, Available Day-0 Fireworks.md>) · `reasoning` · fireworks
  Kimi K2.7 Code uses roughly 30% fewer reasoning tokens than K2.6 while scoring higher on coding evals (+21.8% Kimi Code Bench v2, +11% Program Bench), illustrating that reasoning-token economy, not just raw benchmark score, matters for agentic coding workloads that fire off dozens of model calls per task.
- **2026-05-20** — [The Agent Execution Tax](<../evals-observability/benchmark-design/The Agent Execution Tax.md>) · `benchmark-design` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-05-19** — [Best Open Source LLMs of May 2026: We Reviewed 7 Models](<../models/benchmarks/Best Open Source LLMs of May 2026 We Reviewed 7 Models.md>) · `benchmarks` · fireworks
  May 2026 snapshot comparing seven open-source LLMs (MiniMax-M2.5, GLM-5, Kimi K2.5, DeepSeek v3.2, Kimi K2 Thinking, Qwen3 VL 235B) on parameters, context window, and best-fit use case, all available for serverless inference on Fireworks.
- **2026-04-27** — [DeepSeek V4 Pro: Validating Frontier Models for Production](<../evals-observability/evaluation/DeepSeek V4 Pro Validating Frontier Models for Production.md>) · `evaluation` · fireworks
  Shows how to validate a frontier model for production using benchmark and workload-specific evaluation signals.
- **2026-04-24** — [How we fixed prompt injection for all models on Fireworks](<../product-engineering/security/How we fixed prompt injection for all models on Fireworks.md>) · `security` · fireworks
  Explains a tokenizer-level prompt-injection fix and the implications for securing model-serving systems.
- **2026-04-23** — [Claude Code pricing: plans, API costs, and how to lower your bill](<../infra-platform/cost/Claude Code pricing plans, API costs, and how to lower your bill.md>) · `cost` · fireworks
  Breaks down Claude Code cost paths (Pro $17/mo, Max 5x/20x, Team Standard/Premium, Enterprise, API) and describes routing Claude Code through Fireworks-hosted open-weight models (GLM 5.2, Kimi K2.7 Code, MiniMax M3) via FireConnect or an OpenAI-compatible harness, recommending evaluation on completion rate and repair time rather than token price alone.
- **2026-03-28** — [The Fine-Tuning Bottleneck Isn't the Algorithm](<../models/fine-tuning/The Fine-Tuning Bottleneck Isn't the Algorithm.md>) · `fine-tuning` · fireworks
  Explains why fine-tuning bottlenecks often come from data, evaluation, orchestration, and serving rather than algorithms alone.
- **2026-03-23** — [Frontier RL Is Cheaper Than You Think](<../models/reinforcement-learning/Frontier RL Is Cheaper Than You Think.md>) · `reinforcement-learning` · fireworks
  Argues that frontier reinforcement learning can be cost-effective with the right infrastructure and training-loop design.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<../inference/kernels/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `kernels` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-06** — [Inference Providers vs. API Routers: where do tokens come from?](<../infra-platform/deployment/Inference Providers vs. API Routers where do tokens come from.md>) · `deployment` · fireworks
  Distinguishes inference providers (control the GPUs serving a model) from API routers like OpenRouter (forward requests upstream), explaining that routers can improve tail latency/reliability via failover but cannot beat direct-provider median latency, and have no visibility into KV cache, batch scheduling, or kernel decisions that determine quality.
- **2026-03-04** — [Best LLM API Providers in 2026: We Reviewed 8 Options](<../infra-platform/deployment/Best LLM API Providers in 2026 We Reviewed 8 Options.md>) · `deployment` · fireworks
  Comparison of 8 LLM inference providers (Fireworks, Groq, Together, OpenRouter, Cerebras, Hugging Face, Baseten, Modal) on criteria beyond price/token: fine-tuning support, model deprecation risk, rate limits, and billing complexity, with per-provider recommendations by use case.
- **2026-03-02** — [Best LLMs for coding: 2026 roundup](<../models/benchmarks/Best LLMs for coding 2026 roundup.md>) · `benchmarks` · fireworks
  2026 coding-model roundup comparing GPT-5.5, Claude Opus 4.7, Kimi K2.6, DeepSeek V4-Pro/Flash, gpt-oss-120B and others on AA Coding Index, SWE-Bench Verified, context window, price, and license, with guidance on open vs closed model tradeoffs for production coding workloads.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<../models/reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2026-02-03** — [The Benchmark Gap: What It Takes to Ship Kimi K2.5](<../evals-observability/evaluation/The Benchmark Gap What It Takes to Ship Kimi K2.5.md>) · `evaluation` · fireworks
  Explains the benchmark and quality gaps involved in shipping Kimi K2.5 for production workloads.
- **2026-01-26** — [Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT](<../models/reinforcement-learning/Kimi K2.5 Is Live on Fireworks Vibe Coding, Agents, and Full-Parameter RFT.md>) · `reinforcement-learning` · fireworks
  Fireworks' full-parameter RL tuning preview for Kimi K2.5 exposes Tinker-API-compatible low-level primitives (forward, forward_backward, optimizer_step) while handling distributed training, cross-region trainer/sampler deployment with seamless weight transfer, and customizable GRPO/reward-shaping loss.
- **2026-01-23** — [Turning production logs into evaluation datasets](<../evals-observability/evaluation/Turning production logs into evaluation datasets.md>) · `evaluation` · fireworks
  Describes converting production traces into compact evaluation datasets using embeddings, clustering, and representative sampling.
- **2025-12-31** — [DPO as reinforcement learning](<../models/reinforcement-learning/DPO as reinforcement learning.md>) · `reinforcement-learning` · fireworks
  Connects DPO and RL-style training loops, explaining preference optimization as part of continuous model improvement.
- **2025-12-17** — [Self-Improving Agents, Powered by Your Evals](<../agents/planning/Self-Improving Agents, Powered by Your Evals.md>) · `planning` · fireworks
  Describes self-improving agents powered by eval loops, using evaluation feedback to improve behavior.
- **2025-12-15** — [NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents](<../models/architectures/NVIDIA Nemotron 3 Nano on Fireworks The Engine for Next-Generation AI Agents.md>) · `architectures` · fireworks
  NVIDIA Nemotron 3 Nano is a 30B MoE (3B active) hybrid Mamba-Transformer with 23 Mamba-2/MoE layers, 6 attention layers, 128 experts (5 active) plus a shared expert, and a token 'thinking budget' to cap reasoning-token generation; a cookbook demonstrates a chunk-then-synthesize strategy for summarizing large source files.
- **2025-12-10** — [Best Practices for Multi-Turn RL](<../models/reinforcement-learning/Best Practices for Multi-Turn RL.md>) · `reinforcement-learning` · fireworks
  Covers best practices for multi-turn reinforcement learning, including environment design and reward structure.
- **2025-12-04** — [Fine-tuning LLMs as classifiers](<../models/fine-tuning/Fine-tuning LLMs as classifiers.md>) · `fine-tuning` · fireworks
  Shows how to adapt generative LLMs for classification tasks while preserving probability outputs and efficient serving.
- **2025-12-02** — [Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks](<../models/architectures/Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks.md>) · `architectures` · fireworks
  NVIDIA Nemotron Nano 2 uses a hybrid Mamba-Transformer design where only ~8% of layers use quadratic-cost self-attention (placed where long-range links matter) and the rest use constant-cost Mamba-2/FFN blocks, giving transformer-level accuracy with much lower compute and stable memory for long-context reasoning.
- **2025-11-20** — [Eval Protocol: RL on your agents, in any environment](<../models/reinforcement-learning/Eval Protocol RL on your agents, in any environment.md>) · `reinforcement-learning` · fireworks
  Describes using Eval Protocol to run reinforcement learning on agents in task environments.
- **2025-11-19** — [50 Trillion Tokens Per Day: The State of Agent Environments](<../agents/computer-use/50 Trillion Tokens Per Day The State of Agent Environments.md>) · `computer-use` · fireworks
  Surveys the state of agent environments, emphasizing execution scale, sandboxing, and environment design.
- **2025-11-09** — [Modernizing Healthcare with AI: How RADPAIR and Fireworks Unlock Smarter Radiology Workflows](<../product-engineering/case-studies/Modernizing Healthcare with AI How RADPAIR and Fireworks Unlock Smarter Radiology Workflows.md>) · `case-studies` · fireworks
  RADPAIR built an open-source AI orchestration standard for radiology (Report Document Schema + Actions and Event Protocol) running fine-tuned models and multi-agent pipelines on Fireworks, cutting report turnaround from 15-20s to 2-5s and reporting ~12% fewer errors across 1,000+ concurrent users.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models, speculative decoding, and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-31** — [Genspark’s Deep Research Agent Outperforms a Frontier Closed Model in Quality and Tool Calls using Fireworks RFT, Achieving a 50% Cost Reduction](<../models/reinforcement-learning/Genspark’s Deep Research Agent Outperforms a Frontier Closed Model in Quality and Tool Calls using Fireworks RFT, Achieving a 50% Cost Reduction.md>) · `reinforcement-learning` · fireworks
  Genspark used Fireworks' Reinforcement Fine-Tuning on a 1T-parameter Kimi K2 Mixture-of-Agents deep-research system, achieving 12% better quality and 33% more tool calls than a SOTA closed model at 50% lower cost within one month, moving beyond what prompt engineering on a proprietary model could achieve.
- **2025-10-27** — [Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks](<../models/multimodal/Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks.md>) · `multimodal` · fireworks
  NVIDIA Nemotron Nano2 VL combines the hybrid Mamba-Transformer Nemotron LLM with a CRADIOH-V2 vision encoder and video token compression; in an invoice-processing benchmark on Fireworks it hit 90%+ extraction accuracy on fields like invoice number and date via semantic (not pure-OCR) document understanding.
- **2025-10-06** — [LLM Fine-Tuning: Deep Dive & Best Practices](<../models/fine-tuning/LLM Fine-Tuning Deep Dive & Best Practices.md>) · `fine-tuning` · fireworks
  Deep dive into LLM fine-tuning best practices, including data preparation, training strategy, and deployment concerns.
- **2025-09-22** — [Traces are all you need](<../evals-observability/evaluation/Traces are all you need.md>) · `evaluation` · fireworks
  Shows how to turn production traces into an internal model leaderboard with rollout processors and judge comparisons.
- **2025-09-12** — [Understanding embeddings and reranking at scale](<../rag-retrieval/search/Understanding embeddings and reranking at scale.md>) · `search` · fireworks
  Explains embeddings, reranking, and retrieval architecture patterns for production RAG systems.
- **2025-08-25** — [LLM Eval Driven Development with Claude Code](<../evals-observability/evaluation/LLM Eval Driven Development with Claude Code.md>) · `evaluation` · fireworks
  Explains eval-driven development with Claude Code, using tests and feedback loops to improve coding-agent behavior.
- **2025-08-15** — [Your AI Benchmark is Lying to You. Here's How We Caught It](<../evals-observability/benchmark-design/Your AI Benchmark is Lying to You. Here's How We Caught It.md>) · `benchmark-design` · fireworks
  Explains how benchmark methodology can mislead model selection and how to evaluate models against real workload constraints.
- **2025-08-14** — [Test-driven agent development](<../evals-observability/testing/Test-driven agent development.md>) · `testing` · fireworks
  Shows a TDD-style workflow for building agents with concrete acceptance tests, red teaming, and regression checks.
- **2025-08-05** — [Introducing OpenAI gpt-oss (20b & 120b)](<../models/releases/Introducing OpenAI gpt-oss (20b & 120b).md>) · `releases` · fireworks
  Deep dive on OpenAI's first open-weight release since GPT-2 (gpt-oss-20b/120b): standard MoE transformer architecture with adjustable low/mid/high reasoning levels and built-in tool support, with gpt-oss-120b surpassing o3-mini and approaching o4-mini on benchmarks despite being 6x smaller than typical frontier scale, driven mainly by post-training data and RL rather than architecture.
- **2025-08-01** — [Kimi K2: Architecture, Capabilities & Benchmarks](<../models/reasoning/Kimi K2 Architecture, Capabilities & Benchmarks.md>) · `reasoning` · fireworks
  Explains Kimi K2 architecture, capabilities, and benchmark behavior for agent and reasoning workloads.
- **2025-08-01** — [Qwen3 Instruct vs Thinking vs Coder: Model Selection Guide](<../models/reasoning/Qwen3 Instruct vs Thinking vs Coder Model Selection Guide.md>) · `reasoning` · fireworks
  Compares Qwen3 Instruct, Thinking, and Coder variants for model selection across reasoning and coding tasks.
- **2025-07-30** — [Fireworks AI](<../evals-observability/benchmark-design/Fireworks AI.md>) · `benchmark-design` · fireworks
  Fireworks' Real-World Leaderboard evaluates models on vertical, production-mirroring tasks (ticket classification, e-commerce search, agentic workflows) rather than academic benchmarks, finding Qwen3 Instruct strongest on knowledge-heavy tasks, Qwen3 Coder strong on simple tool-use, and Claude Sonnet 4 still leading complex multi-step agentic work.
- **2025-07-22** — [Kimi QK-Clip and multi-head latent attention](<../models/reasoning/Kimi QK-Clip and multi-head latent attention.md>) · `reasoning` · fireworks
  Explains Kimi QK-Clip, multi-head latent attention, and why training-inference key construction affects stability.
- **2025-07-15** — [MuonClip and Kimi K2 training stability](<../models/reasoning/MuonClip and Kimi K2 training stability.md>) · `reasoning` · fireworks
  Explains MuonClip as a stability technique for large-scale Kimi-style model training.
- **2025-07-11** — [Function calling for agentic AI systems](<../agents/tool-use/Function calling for agentic AI systems.md>) · `tool-use` · fireworks
  Explains function calling as the bridge between LLM outputs, external tools, and agentic execution loops.
- **2025-07-10** — [Using Model-as-a-Judge for Reward in Reinforcement Finetuning](<../evals-observability/llm-as-judge/Using Model-as-a-Judge for Reward in Reinforcement Finetuning.md>) · `llm-as-judge` · fireworks
  Explains using model-as-judge rewards for reinforcement fine-tuning and the evaluation risks involved.
- **2025-06-22** — [Unlock Your Tools: Fireworks Adds OpenAI-Response API with MCP Support (Beta)](<../agents/tool-use/Unlock Your Tools Fireworks Adds OpenAI-Response API with MCP Support (Beta).md>) · `tool-use` · fireworks
  Fireworks' OpenAI-compatible Responses API adds first-class Model Context Protocol (MCP) support, moving the agentic loop (reasoning, tool selection, execution) server-side so any MCP-speaking tool integration is portable across models rather than locked into one vendor's tool-calling format.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<../inference/serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-04** — [Synthetic data pipeline for fine-tuning and evaluation](<../models/fine-tuning/Synthetic data pipeline for fine-tuning and evaluation.md>) · `fine-tuning` · fireworks
  Describes a synthetic-data pipeline that connects task definition, generation, SFT/RFT, evaluation, and cleanup.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<../inference/quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-05-21** — [Building an open-source Browser Agent on Fireworks](<../agents/computer-use/Building an open-source Browser Agent on Fireworks.md>) · `computer-use` · fireworks
  Technical breakdown of Fireworks BrowserUse: gives an LLM web-browsing ability by combining DOM extraction (interactive element structure), base64 screenshot capture for visual context, viewport/scroll position tracking, and unique indexing of interactive elements so the model can unambiguously reference what to click.
- **2025-05-19** — [Agentic AI Systems](<../agents/planning/Agentic AI Systems.md>) · `planning` · fireworks
  Overview of agentic AI systems, covering planning, tool use, control loops, and production architecture concerns.
- **2025-05-12** — [Supervised Fine-Tuning (SFT) with LoRA on Fireworks: Tutorial](<../models/fine-tuning/Supervised Fine-Tuning (SFT) with LoRA on Fireworks Tutorial.md>) · `fine-tuning` · fireworks
  Step-by-step tutorial for LoRA/qLoRA supervised fine-tuning on Fireworks, covering 4-bit/8-bit quantized-model tuning for reduced memory, JSONL dataset formatting, and running up to 100 LoRA adapters concurrently on one dedicated deployment at no extra serving cost.
- **2025-05-06** — [Qwen 3 on Fireworks: Controllable Chain-of-Thought and Tool Calling at Frontier Scale](<../models/reasoning/Qwen 3 on Fireworks Controllable Chain-of-Thought and Tool Calling at Frontier Scale.md>) · `reasoning` · fireworks
  Qwen 3 235B-A22B (128-expert MoE, 22B active) streams an explicit chain-of-thought trace alongside a structured tool call in the same completion, toggleable via reasoning_effort or /think //no_think tags, with recommended sampling params differing between thinking and non-thinking modes.
- **2025-04-28** — [Optimizing Llama 4 Maverick on Fireworks](<../inference/optimization/Optimizing Llama 4 Maverick on Fireworks.md>) · `optimization` · fireworks
  Details how Fireworks served Llama 4 Maverick within minutes of weight release using FireOptimizer-tuned FP8 quantization, tensor+expert parallelism, a custom FireAttention kernel extended for Maverick's chunked local attention, and a trained speculative-decoding drafter, reaching 145 tok/s on H200 (10-20% faster than the nearest competitor per Artificial Analysis).
- **2025-03-12** — [Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost](<../models/fine-tuning/Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost.md>) · `fine-tuning` · fireworks
  Guide to fine-tuning DeepSeek V3 and R1 models while balancing quality, latency, and cost.
- **2025-02-07** — [DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical](<../models/reasoning/DeepSeek v3 and R1 Model Architecture Why it's powerful and economical.md>) · `reasoning` · fireworks
  Explains DeepSeek V3 and R1 architecture choices, including why the models are efficient for reasoning workloads.
- **2025-02-01** — [From text to task: Constrained generation for structured extraction in R1](<../prompt-engineering/structured-output/From text to task Constrained generation for structured extraction in R1.md>) · `structured-output` · fireworks
  Explains constrained generation for structured extraction with reasoning models and schema-bound outputs.
- **2025-01-31** — [Distillation with Reasoning: Can DeepSeek R1 Teach Better Than Humans?](<../models/fine-tuning/Distillation with Reasoning Can DeepSeek R1 Teach Better Than Humans.md>) · `fine-tuning` · fireworks
  Discusses distilling reasoning behavior from DeepSeek R1 and the limits of teacher-model supervision.
- **2025-01-27** — [Beyond Supervised Fine Tuning: How Reinforcement Learning Empowers AI with Minimal Labels](<../models/reinforcement-learning/Beyond Supervised Fine Tuning How Reinforcement Learning Empowers AI with Minimal Labels.md>) · `reinforcement-learning` · fireworks
  Explains GRPO (used in DeepSeek R1-Zero) versus PPO: GRPO removes the co-trained Value Model by using normalized reward across multiple generations of the same prompt as the advantage baseline, cutting compute/memory overhead and easing implementation, with reward-model choice left open to the practitioner.
- **2024-11-15** — [Fireworks f1: A breakthrough in complex reasoning with Compound AI](<../agents/harness/Fireworks f1 A breakthrough in complex reasoning with Compound AI.md>) · `harness` · fireworks
  Fireworks' f1 is a 'compound AI' model that interleaves generation from multiple open models at the inference layer to handle complex reasoning via declarative prompting, aiming to match or exceed closed frontier models on coding, math, and reasoning benchmarks.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<../inference/hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<../inference/quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<../inference/speculative-decoding/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `speculative-decoding` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<../inference/kernels/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `kernels` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-06-03** — [GPUs on-demand: Not serverless, not reserved, but some third thing](<../infra-platform/gpu-clusters/GPUs on-demand Not serverless, not reserved, but some third thing.md>) · `gpu-clusters` · fireworks
  Explains on-demand GPU infrastructure as a middle ground between serverless and reserved capacity.
- **2024-05-08** — [Code Generation with Large Language Models - Fireworks AI Take](<../agents/tool-use/Code Generation with Large Language Models - Fireworks AI Take.md>) · `tool-use` · fireworks
  Discusses code-generation copilots with LLMs, including model behavior, latency, and developer workflow considerations.
- **2024-05-06** — [Doomed to Code: How we Teamed Up with Fireworks at MistralAI Hackathon to Conquer the Shores of Hell](<../agents/computer-use/Doomed to Code How we Teamed Up with Fireworks at MistralAI Hackathon to Conquer the Shores of Hell.md>) · `computer-use` · fireworks
  Hackathon writeup on getting text-only Mistral-7B to play Doom by representing the game screen as text (bounding boxes of detected objects) rather than using vision models, working around the lack of native multimodal input to give a text LLM real-time game-state awareness.
- **2024-02-20** — [Why do all LLMs need structured output modes?](<../prompt-engineering/structured-output/Why do all LLMs need structured output modes.md>) · `structured-output` · fireworks
  Explains why structured-output modes matter for reliable LLM applications and tool-calling systems.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<../inference/quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-12-20** — [Fireworks Raises the Quality Bar with Function Calling Model and API Release](<../agents/tool-use/Fireworks Raises the Quality Bar with Function Calling Model and API Release.md>) · `tool-use` · fireworks
  Analyzes the core challenges of function calling at scale: intent detection (when to call vs. answer directly), handling large function sets like the full Stripe SDK, structuring nested/enum parameter values, and using multi-turn conversational context, ahead of Fireworks' alpha function-calling model release.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<../inference/serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-10-11** — [Accelerating Code Completion with Fireworks Fast LLM Inference](<../inference/optimization/Accelerating Code Completion with Fireworks Fast LLM Inference.md>) · `optimization` · fireworks
  Sourcegraph's Cody code-completion integrated Fireworks-served StarCoder, raising Completion Acceptance Rate from 15% to 30% and cutting multi-line latency from 3.4s to 2.4s; Fireworks reports 3.5x+ lower latency than vLLM across batch sizes on 8xA100 via multi-query attention and PyTorch runtime optimizations.
- **2023-09-12** — [Simplifying Code Infilling with Code Llama and Fireworks.ai](<../prompt-engineering/techniques/Simplifying Code Infilling with Code Llama and Fireworks.ai.md>) · `techniques` · fireworks
  Documents the specific prompt format required for Code Llama infilling (<PRE>{pre}<SUF>{suf}<MID>, sensitive to trailing whitespace) and notes base models outperform instruction-tuned variants for precise infilling control, a common source of silent failures when building code-completion features.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<../inference/kernels/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `kernels` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
