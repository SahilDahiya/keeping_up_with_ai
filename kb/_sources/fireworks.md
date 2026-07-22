# fireworks

65 articles.

- **2026-07-21** — [Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.](<../models/benchmarks/Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.md>) · `benchmarks` · fireworks
  Fireworks benchmarked open Kimi K3 against closed Fable 5 across ~1,030 agentic tasks (SWE-bench-style fixes, terminal ops, algorithmic problems, multi-language, legal), finding near-parity on quality (92.4% vs 92.6% on SWE) and that oracle routing between the two models hits 93% accuracy at up to 50x lower cost than running Fable alone.
- **2026-07-20** — [Heidi x Fireworks: Bridging the Gap in Frontier Model Performance](<../models/fine-tuning/Heidi x Fireworks Bridging the Gap in Frontier Model Performance.md>) · `fine-tuning` · fireworks
  Heidi's ambient clinical scribe moved from proprietary to fine-tuned open models on Fireworks: SFT beat Gemini Flash and RFT/DPO beat Gemini Pro on internal side-by-side evals, with the key levers being LLM-judge and synthetic-rewrite filtering of noisy preference data and scaling effective batch size from 64k to 768k tokens via gradient accumulation (win rate 48.0% to 51.3%).
- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<../inference/kernels/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `kernels` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-07** — [How I shipped a month of engineering work in four days with GLM 5.2 Fast](<../product-engineering/case-studies/How I shipped a month of engineering work in four days with GLM 5.2 Fast.md>) · `case-studies` · fireworks
  An engineer used glm-5p2-fast (via Fireworks' FireConnect router into Claude Code) to design, plan, and implement a GPU-scheduler reclaim feature test-first (34 tests, 4 PRs, ~3,000 lines) in four days for $218 in inference, arguing that 2-3x faster inference keeps human-AI design iteration a live back-and-forth instead of breaking into async context switches.
- **2026-06-24** — [Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.](<../agents/multi-agent/Frontier AI at a fraction of the cost open-source worker agents with a closed-source advisor.md>) · `multi-agent` · fireworks
  Explains a worker-advisor pattern that combines open-source worker agents with closed-source advisors for cost-quality tradeoffs.
- **2026-06-24** — [Frontier-lab training infrastructure, now as a service](<../infra-platform/gpu-clusters/Frontier-lab training infrastructure, now as a service.md>) · `gpu-clusters` · fireworks
  Describes training infrastructure as a service for frontier-lab workloads, including scale, orchestration, and reliability needs.
- **2026-06-03** — [How Harvey & Fireworks Beat Closed Source on Cost + Quality](<../agents/multi-agent/How Harvey & Fireworks Beat Closed Source on Cost + Quality.md>) · `multi-agent` · fireworks
  Case study of using open-source agents with frontier advisors to improve cost and quality versus closed-source baselines.
- **2026-05-20** — [The Agent Execution Tax](<../evals-observability/benchmark-design/The Agent Execution Tax.md>) · `benchmark-design` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-04-27** — [DeepSeek V4 Pro: Validating Frontier Models for Production](<../evals-observability/evaluation/DeepSeek V4 Pro Validating Frontier Models for Production.md>) · `evaluation` · fireworks
  Shows how to validate a frontier model for production using benchmark and workload-specific evaluation signals.
- **2026-04-24** — [How we fixed prompt injection for all models on Fireworks](<../product-engineering/security/How we fixed prompt injection for all models on Fireworks.md>) · `security` · fireworks
  Explains a tokenizer-level prompt-injection fix and the implications for securing model-serving systems.
- **2026-03-28** — [The Fine-Tuning Bottleneck Isn't the Algorithm](<../models/fine-tuning/The Fine-Tuning Bottleneck Isn't the Algorithm.md>) · `fine-tuning` · fireworks
  Explains why fine-tuning bottlenecks often come from data, evaluation, orchestration, and serving rather than algorithms alone.
- **2026-03-23** — [Frontier RL Is Cheaper Than You Think](<../models/reinforcement-learning/Frontier RL Is Cheaper Than You Think.md>) · `reinforcement-learning` · fireworks
  Argues that frontier reinforcement learning can be cost-effective with the right infrastructure and training-loop design.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<../inference/kernels/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `kernels` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<../models/reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2026-02-03** — [The Benchmark Gap: What It Takes to Ship Kimi K2.5](<../evals-observability/evaluation/The Benchmark Gap What It Takes to Ship Kimi K2.5.md>) · `evaluation` · fireworks
  Explains the benchmark and quality gaps involved in shipping Kimi K2.5 for production workloads.
- **2026-01-23** — [Turning production logs into evaluation datasets](<../evals-observability/evaluation/Turning production logs into evaluation datasets.md>) · `evaluation` · fireworks
  Describes converting production traces into compact evaluation datasets using embeddings, clustering, and representative sampling.
- **2025-12-31** — [DPO as reinforcement learning](<../models/reinforcement-learning/DPO as reinforcement learning.md>) · `reinforcement-learning` · fireworks
  Connects DPO and RL-style training loops, explaining preference optimization as part of continuous model improvement.
- **2025-12-17** — [Self-Improving Agents, Powered by Your Evals](<../agents/planning/Self-Improving Agents, Powered by Your Evals.md>) · `planning` · fireworks
  Describes self-improving agents powered by eval loops, using evaluation feedback to improve behavior.
- **2025-12-10** — [Best Practices for Multi-Turn RL](<../models/reinforcement-learning/Best Practices for Multi-Turn RL.md>) · `reinforcement-learning` · fireworks
  Covers best practices for multi-turn reinforcement learning, including environment design and reward structure.
- **2025-12-04** — [Fine-tuning LLMs as classifiers](<../models/fine-tuning/Fine-tuning LLMs as classifiers.md>) · `fine-tuning` · fireworks
  Shows how to adapt generative LLMs for classification tasks while preserving probability outputs and efficient serving.
- **2025-11-20** — [Eval Protocol: RL on your agents, in any environment](<../models/reinforcement-learning/Eval Protocol RL on your agents, in any environment.md>) · `reinforcement-learning` · fireworks
  Describes using Eval Protocol to run reinforcement learning on agents in task environments.
- **2025-11-19** — [50 Trillion Tokens Per Day: The State of Agent Environments](<../agents/computer-use/50 Trillion Tokens Per Day The State of Agent Environments.md>) · `computer-use` · fireworks
  Surveys the state of agent environments, emphasizing execution scale, sandboxing, and environment design.
- **2025-11-10** — [Fireworks RFT: Build AI agents with fine-tuned open models that outperform frontier closed models](<../models/reinforcement-learning/Fireworks RFT Build AI agents with fine-tuned open models that outperform frontier closed models.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement fine-tuning for building agent models that can outperform closed frontier models on target tasks.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models, speculative decoding, and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-31** — [Genspark deep research agent with Fireworks RFT](<../models/reinforcement-learning/Genspark deep research agent with Fireworks RFT.md>) · `reinforcement-learning` · fireworks
  Case study of reinforcement fine-tuning a deep research agent to improve quality, tool calls, and cost.
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
- **2025-08-01** — [Kimi K2: Architecture, Capabilities & Benchmarks](<../models/reasoning/Kimi K2 Architecture, Capabilities & Benchmarks.md>) · `reasoning` · fireworks
  Explains Kimi K2 architecture, capabilities, and benchmark behavior for agent and reasoning workloads.
- **2025-08-01** — [Qwen3 Instruct vs Thinking vs Coder: Model Selection Guide](<../models/reasoning/Qwen3 Instruct vs Thinking vs Coder Model Selection Guide.md>) · `reasoning` · fireworks
  Compares Qwen3 Instruct, Thinking, and Coder variants for model selection across reasoning and coding tasks.
- **2025-07-22** — [Kimi QK-Clip and multi-head latent attention](<../models/reasoning/Kimi QK-Clip and multi-head latent attention.md>) · `reasoning` · fireworks
  Explains Kimi QK-Clip, multi-head latent attention, and why training-inference key construction affects stability.
- **2025-07-15** — [MuonClip and Kimi K2 training stability](<../models/reasoning/MuonClip and Kimi K2 training stability.md>) · `reasoning` · fireworks
  Explains MuonClip as a stability technique for large-scale Kimi-style model training.
- **2025-07-11** — [Function calling for agentic AI systems](<../agents/tool-use/Function calling for agentic AI systems.md>) · `tool-use` · fireworks
  Explains function calling as the bridge between LLM outputs, external tools, and agentic execution loops.
- **2025-07-10** — [Using Model-as-a-Judge for Reward in Reinforcement Finetuning](<../evals-observability/llm-as-judge/Using Model-as-a-Judge for Reward in Reinforcement Finetuning.md>) · `llm-as-judge` · fireworks
  Explains using model-as-judge rewards for reinforcement fine-tuning and the evaluation risks involved.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<../inference/serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-09** — [Reinforcement Fine Tuning: Train expert open models to surpass closed frontier models](<../models/reinforcement-learning/Reinforcement Fine Tuning Train expert open models to surpass closed frontier models.md>) · `reinforcement-learning` · fireworks
  Introduces reinforcement fine-tuning for training expert open models beyond supervised baselines.
- **2025-06-04** — [Synthetic data pipeline for fine-tuning and evaluation](<../models/fine-tuning/Synthetic data pipeline for fine-tuning and evaluation.md>) · `fine-tuning` · fireworks
  Describes a synthetic-data pipeline that connects task definition, generation, SFT/RFT, evaluation, and cleanup.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<../inference/quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-05-21** — [Building an open-source Browser Agent on Fireworks AI](<../agents/computer-use/Building an open-source Browser Agent on Fireworks AI.md>) · `computer-use` · fireworks
  Walkthrough of building an open-source browser agent, including model choice, tool execution, and environment control.
- **2025-05-19** — [Agentic AI Systems](<../agents/planning/Agentic AI Systems.md>) · `planning` · fireworks
  Overview of agentic AI systems, covering planning, tool use, control loops, and production architecture concerns.
- **2025-05-12** — [Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI: Tutorial](<../models/fine-tuning/Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI Tutorial.md>) · `fine-tuning` · fireworks
  Tutorial for supervised fine-tuning with LoRA, including setup, training, and deployment workflow.
- **2025-03-12** — [Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost](<../models/fine-tuning/Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost.md>) · `fine-tuning` · fireworks
  Guide to fine-tuning DeepSeek V3 and R1 models while balancing quality, latency, and cost.
- **2025-02-07** — [DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical](<../models/reasoning/DeepSeek v3 and R1 Model Architecture Why it's powerful and economical.md>) · `reasoning` · fireworks
  Explains DeepSeek V3 and R1 architecture choices, including why the models are efficient for reasoning workloads.
- **2025-02-01** — [From text to task: Constrained generation for structured extraction in R1](<../prompt-engineering/structured-output/From text to task Constrained generation for structured extraction in R1.md>) · `structured-output` · fireworks
  Explains constrained generation for structured extraction with reasoning models and schema-bound outputs.
- **2025-01-31** — [Distillation with Reasoning: Can DeepSeek R1 Teach Better Than Humans?](<../models/fine-tuning/Distillation with Reasoning Can DeepSeek R1 Teach Better Than Humans.md>) · `fine-tuning` · fireworks
  Discusses distilling reasoning behavior from DeepSeek R1 and the limits of teacher-model supervision.
- **2025-01-27** — [Beyond Supervised Fine Tuning: How Reinforcement Learning Empowers AI with Minimal Labels](<../models/reinforcement-learning/Beyond Supervised Fine Tuning How Reinforcement Learning Empowers AI with Minimal Labels.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement learning with verifiable rewards as a way to improve models with minimal labels.
- **2024-12-09** — [20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds](<../models/multimodal/20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds.md>) · `multimodal` · fireworks
  Describes high-throughput Whisper transcription serving and the latency/cost tradeoffs in batch audio inference.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<../inference/hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<../inference/serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-29** — [Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction](<../agents/tool-use/Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction.md>) · `tool-use` · fireworks
  Tutorial for building a function-calling application with FastAPI, SerpAPI, and structured tool invocation.
- **2024-08-14** — [Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1](<../rag-retrieval/pipelines/Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1.md>) · `pipelines` · fireworks
  End-to-end RAG application example using Astro, FastAPI, SurrealDB, and Llama 3.1.
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
- **2024-02-20** — [Why do all LLMs need structured output modes?](<../prompt-engineering/structured-output/Why do all LLMs need structured output modes.md>) · `structured-output` · fireworks
  Explains why structured-output modes matter for reliable LLM applications and tool-calling systems.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<../inference/quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<../inference/serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<../inference/kernels/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `kernels` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
