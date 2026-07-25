# models

221 articles.

- **2026-07-23** — [Cost per successful task: Benchmarking Kimi K3, GPT-5.5, and 8 more AI models](<benchmarks/Cost per successful task Benchmarking Kimi K3, GPT-5.5, and 8 more AI models.md>) · `benchmarks` · arize
  Arize and Fireworks benchmark 10 models (Kimi K3, K2.6, GPT-5.5, GPT-5, Claude Sonnet 5, GLM-5.2, DeepSeek V4 Pro, gpt-oss-120b, two Gemini variants) across 40 agent tasks and 2,400 runs, arguing cost-per-successful-task (spend across all attempts / successes) is the metric that matters, not token price — gpt-oss-120b wins on cost-per-success despite a 33% pass rate.
- **2026-07-22** — [GLM 5.2 With Vision](<multimodal/GLM 5.2 With Vision.md>) · `multimodal` · baseten
  Baseten post-trained vision onto GLM 5.2 by training only a 50M-parameter, 2-layer MLP projector (reusing Kimi K2.6's vision tower) via SFT on 66k image-QA pairs, reaching MMMU-Pro scores equivalent to Claude 4.5 Haiku (55%) without touching GLM's text weights, and observed grokking plus strong generalization to entities never seen in the alignment dataset.
- **2026-07-21** — [Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.](<benchmarks/Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA.md>) · `benchmarks` · fireworks
  Fireworks benchmarked open Kimi K3 against closed Fable 5 across ~1,030 agentic tasks (SWE-bench-style fixes, terminal ops, algorithmic problems, multi-language, legal), finding near-parity on quality (92.4% vs 92.6% on SWE) and that oracle routing between the two models hits 93% accuracy at up to 50x lower cost than running Fable alone.
- **2026-07-20** — [Heidi x Fireworks: Bridging the Gap in Frontier Model Performance](<fine-tuning/Heidi x Fireworks Bridging the Gap in Frontier Model Performance.md>) · `fine-tuning` · fireworks
  Heidi's ambient clinical scribe moved from proprietary to fine-tuned open models on Fireworks: SFT beat Gemini Flash and RFT/DPO beat Gemini Pro on internal side-by-side evals, with the key levers being LLM-judge and synthetic-rewrite filtering of noisy preference data and scaling effective batch size from 64k to 768k tokens via gradient accumulation (win rate 48.0% to 51.3%).
- **2026-07-16** — [Inkling: Our open-weights model](<releases/Inkling Our open-weights model.md>) · `releases` · simon-willison
  Simon Willison covers Thinking Machines Lab's first open-weights release, Inkling: a 975B-parameter (41B active) Apache-2.0 MoE transformer trained on 45T multimodal tokens, positioned as a fine-tuning base for their Tinker platform rather than a frontier model, plus a promised smaller Inkling-Small variant.
- **2026-07-16** — [Kimi K3, and what we can still learn from the pelican benchmark](<releases/Kimi K3, and what we can still learn from the pelican benchmark.md>) · `releases` · simon-willison
  Simon Willison reviews Moonshot AI's Kimi K3 (2.8T parameters, open weights promised July 27, 2026), covering its Artificial Analysis benchmark standing (Elo 1547, +732 over K2.6), its $3/$15 per-million-token pricing, and revisits his informal 'pelican riding a bicycle' SVG test as an ad hoc capability check.
- **2026-07-15** — [Together AI brings Thinking Machines Lab’s new model Inkling on day 0](<architectures/Together AI brings Thinking Machines Lab’s new model Inkling on day 0.md>) · `architectures` · together
  Details Inkling's architecture (975B/40B active MoE with a shared expert sink jointly normalized against routed experts, a learned query-conditioned relative attention bias instead of RoPE, and 'sconv' short causal convolutions on K/V and sublayer outputs) and Together's FlashAttention-4-based kernel adapted to serve its query-conditioned relative attention efficiently.
- **2026-07-13** — [How do you make an LLM, anyway? Microsoft just published a textbook.](<training/How do you make an LLM, anyway Microsoft just published a textbook.md>) · `training` · arize
  Walks through Microsoft's 109-page MAI-Thinking-1 technical report: a 1.2-trillion-page proprietary crawl filtered down and mixed to 54.6% code, a 30-trillion-token pretrain on 8,192 GPUs, a mid-training context-stretching phase (16K to 262K tokens), and RL post-training with anti-reward-hacking measures like time-traveled repo snapshots and test-file resets.
- **2026-07-10** — [Evaluating the GPT-5.6 family](<benchmarks/Evaluating the GPT-5.6 family.md>) · `benchmarks` · braintrust
  Evaluates the GPT-5.6 model family and presents a decision map for choosing models based on quality, cost, and task requirements.
- **2026-07-09** — [Evaluating speech-to-text models](<multimodal/Evaluating speech-to-text models.md>) · `multimodal` · braintrust
  Evaluates speech-to-text models for voice AI workflows, covering datasets, scoring, and tradeoffs in transcription quality.
- **2026-07-09** — [The new GPT-5.6 family: Luna, Terra, Sol](<releases/The new GPT-5.6 family Luna, Terra, Sol.md>) · `releases` · simon-willison
  Notes on the GPT-5.6 Luna, Terra, and Sol release, including pricing, million-token context, agentic benchmark claims, SWE-Bench Pro caveats, programmatic tool calling, subagents, and prompt-cache breakpoints.
- **2026-06-30** — [GLM-5.2 vs. Opus 4.8 technical report](<benchmarks/GLM-5.2 vs. Opus 4.8 technical report.md>) · `benchmarks` · braintrust
  Technical report comparing GLM-5.2 and Opus 4.8, including benchmark methodology, long-context retrieval behavior, and model-performance tradeoffs.
- **2026-06-30** — [What’s new in Claude Sonnet 5](<releases/What’s new in Claude Sonnet 5.md>) · `releases` · simon-willison
  Developer-focused notes on Claude Sonnet 5 covering adaptive thinking defaults, removed sampling parameters, million-token context, pricing/tokenizer changes, and comparative tokenization cost across document types.
- **2026-06-25** — [Live draft model training for speculative decoding](<fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
- **2026-06-24** — [Long-horizon agent benchmarks are fragmenting: a field guide to what each one actually measures](<benchmarks/Long-horizon agent benchmarks are fragmenting a field guide to what each one actually measures.md>) · `benchmarks` · arize
  Field guide to long-horizon agent benchmarks and what each benchmark family reveals about agent performance.
- **2026-06-18** — [Beyond LoRA: Can you beat the most popular fine-tuning technique?](<fine-tuning/Beyond LoRA Can you beat the most popular fine-tuning technique.md>) · `fine-tuning` · huggingface
  Benchmarks PEFT methods beyond LoRA (LoHa, LoKr, OFT, BOFT, VeRA, FourierFT, prompt tuning, adapters) on a common task using the MetaMathQA benchmark suite in the PEFT repo, comparing accuracy, memory and checkpoint size to show when LoRA is and isn't the right default.
- **2026-06-17** — [Two labs started dreaming, and they built two different architectures](<reasoning/Two labs started dreaming, and they built two different architectures.md>) · `reasoning` · arize
  Compares two different AI architecture directions from research labs, focusing on design choices and implications.
- **2026-06-02** — [The end of fine-tuning: Why evals, context, and traces matter more](<fine-tuning/The end of fine-tuning Why evals, context, and traces matter more.md>) · `fine-tuning` · arize
  Argues that evals, context, and traces can reduce the need for fine-tuning in many production AI workflows.
- **2026-05-29** — [How Together AI built a fast speech-to-text stack](<multimodal/How Together AI built a fast speech-to-text stack.md>) · `multimodal` · together
  Engineering writeup on building a fast speech-to-text stack.
- **2026-05-29** — [Timestep distillation: 2.5x faster FLUX.2 image generation](<multimodal/Timestep distillation 2.5x faster FLUX.2 image generation.md>) · `multimodal` · baseten
  Explains timestep distillation for faster FLUX.2 image generation.
- **2026-05-28** — [Reinforcement learning is an infrastructure problem](<reinforcement-learning/Reinforcement learning is an infrastructure problem.md>) · `reinforcement-learning` · modal
  Argues that reinforcement learning progress depends heavily on infrastructure for scheduling, iteration, and scalable experiments.
- **2026-05-27** — [Shipping a Trillion Parameters With a Hub Bucket: Delta Weight Sync in TRL](<reinforcement-learning/Shipping a Trillion Parameters With a Hub Bucket Delta Weight Sync in TRL.md>) · `reinforcement-learning` · huggingface
  In async RL the trainer must ship the full model to the inference engine every step (14 GB for a 7B, ~1 TB for a frontier model); TRL exploits the fact that ~99% of bf16 weights are bit-identical between consecutive optimizer steps and syncs only a sparse safetensors delta via a Hub bucket, cutting Qwen3-0.6B's per-step payload from 1.2 GB to 20-35 MB and enabling fully disaggregated training with no shared cluster or RDMA.
- **2026-05-26** — [How to ship a local LLM that matches frontier LLMs with evals and prompt engineering](<fine-tuning/How to ship a local LLM that matches frontier LLMs with evals and prompt engineering.md>) · `fine-tuning` · arize
  Explains how evals and prompt engineering can make smaller local models viable substitutes for frontier models on constrained tasks.
- **2026-05-19** — [Scaling reinforcement learning at Applied Compute](<reinforcement-learning/Scaling reinforcement learning at Applied Compute.md>) · `reinforcement-learning` · modal
  Case study on scaling reinforcement learning workloads with elastic GPU infrastructure and faster experiment iteration.
- **2026-05-18** — [Voice AI is only as good as what it hears](<multimodal/Voice AI is only as good as what it hears.md>) · `multimodal` · sierra
  Explains why voice-agent quality depends on transcription accuracy and how hearing failures propagate into agent behavior.
- **2026-05-14** — [Cost-efficient, high-performance TTS with Qwen3-TTS](<multimodal/Cost-efficient, high-performance TTS with Qwen3-TTS.md>) · `multimodal` · baseten
  Describes cost-efficient high-performance Qwen3-TTS serving for text-to-speech workloads.
- **2026-05-12** — [Models got an order of magnitude better at following instructions in one year](<benchmarks/Models got an order of magnitude better at following instructions in one year.md>) · `benchmarks` · arize
  Analyzes instruction-following benchmark changes and what they imply for tracking model quality over time.
- **2026-05-12** — [Mu-Bench: an open multilingual transcription benchmark](<benchmarks/Mu-Bench an open multilingual transcription benchmark.md>) · `benchmarks` · sierra
  Introduces mu-Bench, an open multilingual transcription benchmark for evaluating speech recognition quality across languages.
- **2026-05-12** — [Improving voice performance with post-training](<fine-tuning/Improving voice performance with post-training.md>) · `fine-tuning` · sierra
  Describes post-training techniques for improving voice model performance and agent interaction quality.
- **2026-05-12** — [Building more human voice experiences](<multimodal/Building more human voice experiences.md>) · `multimodal` · sierra
  Explains design and engineering considerations for more human voice-agent experiences, including timing, emotion, and conversational flow.
- **2026-05-12** — [Multilingual voice: building agents that speak to everyone](<multimodal/Multilingual voice building agents that speak to everyone.md>) · `multimodal` · sierra
  Describes building multilingual voice agents, including speech recognition, language coverage, and user-experience considerations.
- **2026-05-12** — [Sierra speaks](<multimodal/Sierra speaks.md>) · `multimodal` · sierra
  Launch writeup for Sierra voice agents with useful architecture details on interruptions, latency, call-center integration, escalation, and multi-channel agent reuse.
- **2026-05-12** — [Visual Attachments: A new dimension for chat agents](<multimodal/Visual Attachments A new dimension for chat agents.md>) · `multimodal` · sierra
  Covers visual attachments in chat agents and how images expand support-agent context and user interaction patterns.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-04-24** — [DeepSeek-V4: a million-token context that agents can actually use](<architectures/DeepSeek-V4 a million-token context that agents can actually use.md>) · `architectures` · huggingface
  Breaks down how DeepSeek-V4's architecture makes 1M-token context cheap for agents: V4-Pro needs 27% of V3.2's single-token inference FLOPs and 10% of its KV cache (V4-Flash: 10% and 7%, roughly 2% of an 8-head GQA bf16 cache), plus the agent-specific post-training decisions that build on it.
- **2026-04-22** — [Flow generation through natural language: An agentic modeling approach (2026)](<fine-tuning/Flow generation through natural language An agentic modeling approach (2026).md>) · `fine-tuning` · shopify
  Shopify fine-tunes a model to generate Flow automations from natural language, arguing differentiation comes from proprietary merchant-interaction data and the training recipe rather than closed-model API access.
- **2026-04-20** — [Building an RL theorem-proving workflow on Modal](<reasoning/Building an RL theorem-proving workflow on Modal.md>) · `reasoning` · modal
  Walks through an RL theorem-proving workflow, connecting reasoning tasks, training loops, and scalable remote execution.
- **2026-04-16** — [Ecom-RLVE: Adaptive Verifiable Environments for E-Commerce Conversational Agents](<reinforcement-learning/Ecom-RLVE Adaptive Verifiable Environments for E-Commerce Conversational Agents.md>) · `reinforcement-learning` · huggingface
  Extends RLVE from single-turn puzzles to multi-turn tool-using e-commerce agents: 8 verifiable environments (search, substitution, cart, returns, policy QA...) with procedural problem generation, a 12-axis difficulty curriculum and algorithmic (non-LLM-judge) rewards; trains Qwen3-8B with DAPO for 300 steps.
- **2026-04-15** — [Parcae: Doing more with fewer parameters using stable looped models](<reasoning/Parcae Doing more with fewer parameters using stable looped models.md>) · `reasoning` · together
  Explains stable looped models for doing more with fewer parameters.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-02** — [Welcome Gemma 4: Frontier multimodal intelligence on device](<releases/Welcome Gemma 4 Frontier multimodal intelligence on device.md>) · `releases` · huggingface
  Gemma 4 (Apache 2.0, up to 256K context) mixes alternating local sliding-window and global attention layers, dual RoPE configs, MoE (26B total / 4B active, LMArena ~1441) alongside a 31B dense model at ~1452, plus a USM-style conformer audio encoder and a variable-aspect-ratio image encoder with configurable image-token budget.
- **2026-03-31** — [Baseten Training: an autoresearch substrate](<fine-tuning/Baseten Training an autoresearch substrate.md>) · `fine-tuning` · baseten
  Frames model training infrastructure as an autoresearch substrate for running iterative experiments and training jobs.
- **2026-03-31** — [Open-source LLM training is a mess. Here is how it all works.](<fine-tuning/Open-source LLM training is a mess. Here is how it all works.md>) · `fine-tuning` · baseten
  Explains the moving pieces of open-source LLM training, including data, trainers, infrastructure, and evaluation.
- **2026-03-28** — [The Fine-Tuning Bottleneck Isn't the Algorithm](<fine-tuning/The Fine-Tuning Bottleneck Isn't the Algorithm.md>) · `fine-tuning` · fireworks
  Explains why fine-tuning bottlenecks often come from data, evaluation, orchestration, and serving rather than algorithms alone.
- **2026-03-23** — [Frontier RL Is Cheaper Than You Think](<reinforcement-learning/Frontier RL Is Cheaper Than You Think.md>) · `reinforcement-learning` · fireworks
  Argues that frontier reinforcement learning can be cost-effective with the right infrastructure and training-loop design.
- **2026-03-17** — [Mamba-3](<reasoning/Mamba-3.md>) · `reasoning` · together
  Describes Mamba-3 and its implications for efficient sequence modeling.
- **2026-03-10** — [Keep the Tokens Flowing: Lessons from 16 Open-Source RL Libraries](<reinforcement-learning/Keep the Tokens Flowing Lessons from 16 Open-Source RL Libraries.md>) · `reinforcement-learning` · huggingface
  Surveys 16 open-source async RL libraries across 7 axes (orchestration, rollout buffers, weight-sync protocols, staleness handling, partial rollouts, LoRA, distributed backends); the shared pattern is disaggregating inference and training GPU pools so neither idles, with Ray dominating orchestration (8/16) and NCCL broadcast the default weight transfer.
- **2026-03-09** — [Ulysses Sequence Parallelism: Training with Million-Token Contexts](<training/Ulysses Sequence Parallelism Training with Million-Token Contexts.md>) · `training` · huggingface
  Ulysses Sequence Parallelism (from Snowflake's ALST) shards attention by heads across GPUs via all-to-all so context length scales with GPU count, enabling million-token training; explains the algorithm and its integration into Accelerate, Transformers Trainer and TRL SFTTrainer.
- **2026-03-05** — [When the Call Runs Too Long: Modeling Outcomes for Long Conversations](<reasoning/When the Call Runs Too Long Modeling Outcomes for Long Conversations.md>) · `reasoning` · cresta
  Discusses modeling outcomes for long conversations, including challenges around sequence length and delayed success signals.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2026-02-25** — [The generative recommender behind Shopify's commerce engine (2026)](<architectures/The generative recommender behind Shopify's commerce engine (2026).md>) · `architectures` · shopify
  Shopify's generative recommender treats a buyer's cross-storefront event history as a sequence and predicts the next action, a sequence-modeling approach to commerce recommendations over months-long journeys.
- **2026-02-23** — [How speech models fail where it matters the most and what to do about it](<multimodal/How speech models fail where it matters the most and what to do about it.md>) · `multimodal` · together
  Analyzes speech model failure modes that matter for production applications.
- **2026-02-02** — [Fine-tuning open LLM judges to outperform GPT-5.2](<reinforcement-learning/Fine-tuning open LLM judges to outperform GPT-5.2.md>) · `reinforcement-learning` · together
  Explains fine-tuning open LLM judges to outperform a frontier judge model.
- **2025-12-31** — [DPO as reinforcement learning](<reinforcement-learning/DPO as reinforcement learning.md>) · `reinforcement-learning` · fireworks
  Connects DPO and RL-style training loops, explaining preference optimization as part of continuous model improvement.
- **2025-12-19** — [Evaluating AI Voices – What Does It Mean to Sound “Good”?](<multimodal/Evaluating AI Voices – What Does It Mean to Sound “Good”.md>) · `multimodal` · cresta
  Explores how to evaluate AI voice quality beyond subjective preference, including production criteria for speech experiences.
- **2025-12-17** — [When Every Word Matters: Engineering Real-Time Multilingual Intelligence for Human Conversations](<multimodal/When Every Word Matters Engineering Real-Time Multilingual Intelligence for Human Conversations.md>) · `multimodal` · cresta
  Engineering guide to real-time multilingual intelligence for conversations, focusing on latency and speech-language quality.
- **2025-12-15** — [Updates for developers building with voice | OpenAI Developers](<releases/Updates for developers building with voice OpenAI Developers.md>) · `releases` · openai-devs
  Release notes for four December 2025 audio model snapshots (gpt-4o-mini-transcribe, gpt-4o-mini-tts, gpt-realtime-mini, gpt-audio-mini): lower word-error rates on noisy audio, fewer hallucinations during silence, better tool calling in the minis, and broader Custom Voices access at unchanged pricing.
- **2025-12-10** — [Best Practices for Multi-Turn RL](<reinforcement-learning/Best Practices for Multi-Turn RL.md>) · `reinforcement-learning` · fireworks
  Covers best practices for multi-turn reinforcement learning, including environment design and reward structure.
- **2025-12-05** — [DeepSeek V3.2's path to GPT-5-level performance: sparse attention, RL at scale, and context reuse](<reasoning/DeepSeek V3.2's path to GPT-5-level performance sparse attention, RL at scale, and context reuse.md>) · `reasoning` · baseten
  Explains DeepSeek V3.2 architecture and training choices including sparse attention, RL, and context reuse.
- **2025-12-04** — [Fine-tuning LLMs as classifiers](<fine-tuning/Fine-tuning LLMs as classifiers.md>) · `fine-tuning` · fireworks
  Shows how to adapt generative LLMs for classification tasks while preserving probability outputs and efficient serving.
- **2025-11-20** — [Eval Protocol: RL on your agents, in any environment](<reinforcement-learning/Eval Protocol RL on your agents, in any environment.md>) · `reinforcement-learning` · fireworks
  Describes using Eval Protocol to run reinforcement learning on agents in task environments.
- **2025-11-10** — [Fireworks RFT: Build AI agents with fine-tuned open models that outperform frontier closed models](<reinforcement-learning/Fireworks RFT Build AI agents with fine-tuned open models that outperform frontier closed models.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement fine-tuning for building agent models that can outperform closed frontier models on target tasks.
- **2025-10-31** — [Genspark deep research agent with Fireworks RFT](<reinforcement-learning/Genspark deep research agent with Fireworks RFT.md>) · `reinforcement-learning` · fireworks
  Case study of reinforcement fine-tuning a deep research agent to improve quality, tool calls, and cost.
- **2025-10-23** — [DeepSeek-OCR and the Unreasonable Usefulness of Compression](<multimodal/DeepSeek-OCR and the Unreasonable Usefulness of Compression.md>) · `multimodal` · baseten
  Explains DeepSeek-OCR and why compression can be useful for multimodal model workflows.
- **2025-10-06** — [LLM Fine-Tuning: Deep Dive & Best Practices](<fine-tuning/LLM Fine-Tuning Deep Dive & Best Practices.md>) · `fine-tuning` · fireworks
  Deep dive into LLM fine-tuning best practices, including data preparation, training strategy, and deployment concerns.
- **2025-09-29** — [Claude Sonnet 4.5 analysis](<benchmarks/Claude Sonnet 4.5 analysis.md>) · `benchmarks` · braintrust
  Analyzes Claude Sonnet 4.5 with aspirational evals, focusing on how harder task suites reveal model strengths and gaps beyond standard benchmarks.
- **2025-09-12** — [Developer notes on the Realtime API | OpenAI Developers](<releases/Developer notes on the Realtime API OpenAI Developers.md>) · `releases` · openai-devs
  Developer notes on the Realtime API GA and the gpt-realtime speech-to-speech model: beta-to-GA interface migration, new marin/cedar voices, and advice to rewrite prompts because instruction-following improved enough that literal instructions are now honored.
- **2025-09-09** — [mmBERT: ModernBERT goes Multilingual](<training/mmBERT ModernBERT goes Multilingual.md>) · `training` · huggingface
  mmBERT is a ModernBERT-style multilingual encoder trained on 3T+ tokens across 1,800+ languages using a three-phase schedule with an inverse masking-ratio decay and 'annealed language learning' that progressively adds low-resource languages late in training. Beats XLM-R and mGTE on multilingual retrieval and classification while running significantly faster.
- **2025-09-05** — [NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI](<reasoning/NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI.md>) · `reasoning` · arize
  Summarizes the argument for small language models in agentic AI and where they can replace larger models.
- **2025-08-19** — [How to fine-tune gpt-oss-120b with Baseten and Axolotl](<fine-tuning/How to fine-tune gpt-oss-120b with Baseten and Axolotl.md>) · `fine-tuning` · baseten
  Guide to fine-tuning GPT-OSS 120B with Axolotl and scalable training infrastructure.
- **2025-08-15** — [Fine-tuning small open-source LLMs for specialized tasks](<fine-tuning/Fine-tuning small open-source LLMs for specialized tasks.md>) · `fine-tuning` · together
  Case study fine-tuning small open-source LLMs to beat larger closed models on specialized tasks.
- **2025-08-15** — [Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks](<fine-tuning/Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks.md>) · `fine-tuning` · baseten
  Case study on fine-tuning small open-source LLMs to beat larger closed models on specialized tasks.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-08-08** — [GPT-5 vs. Claude Opus 4.1](<benchmarks/GPT-5 vs. Claude Opus 4.1.md>) · `benchmarks` · braintrust
  Compares GPT-5 and Claude Opus 4.1 with eval-driven analysis of strengths, weaknesses, and model-selection implications.
- **2025-08-08** — [Accelerate ND-Parallel: A guide to Efficient Multi-GPU Training](<training/Accelerate ND-Parallel A guide to Efficient Multi-GPU Training.md>) · `training` · huggingface
  Guide to combining FSDP/HSDP with tensor, context and pipeline parallelism (ND parallelism) in HF Accelerate, with config examples for Llama-3.1-8B and guidance on when each axis pays off.
- **2025-08-01** — [Kimi K2: Architecture, Capabilities & Benchmarks](<reasoning/Kimi K2 Architecture, Capabilities & Benchmarks.md>) · `reasoning` · fireworks
  Explains Kimi K2 architecture, capabilities, and benchmark behavior for agent and reasoning workloads.
- **2025-08-01** — [Qwen3 Instruct vs Thinking vs Coder: Model Selection Guide](<reasoning/Qwen3 Instruct vs Thinking vs Coder Model Selection Guide.md>) · `reasoning` · fireworks
  Compares Qwen3 Instruct, Thinking, and Coder variants for model selection across reasoning and coding tasks.
- **2025-07-28** — [Building Voice AI That Actually Works: Balancing Realistic Voices vs. Production-Ready Performance](<multimodal/Building Voice AI That Actually Works Balancing Realistic Voices vs. Production-Ready Performance.md>) · `multimodal` · cresta
  Explains tradeoffs in building production voice AI, balancing naturalness, latency, reliability, and operational constraints.
- **2025-07-23** — [Transcribe speech 100x faster and 100x cheaper with open models](<multimodal/Transcribe speech 100x faster and 100x cheaper with open models.md>) · `multimodal` · modal
  Shows how open speech models and batch execution can reduce transcription latency and cost at large scale.
- **2025-07-22** — [Kimi QK-Clip and multi-head latent attention](<reasoning/Kimi QK-Clip and multi-head latent attention.md>) · `reasoning` · fireworks
  Explains Kimi QK-Clip, multi-head latent attention, and why training-inference key construction affects stability.
- **2025-07-16** — [Leveraging multimodal LLMs for Shopify’s global catalogue: Recap of expo talk at ICLR 2025](<multimodal/Leveraging multimodal LLMs for Shopify’s global catalogue Recap of expo talk at ICLR 2025.md>) · `multimodal` · shopify
  Shopify uses multimodal LLMs to standardize product data across its global catalogue, producing the high-quality structured attributes that agent-driven shopping ('show me sustainable running shoes') depends on.
- **2025-07-16** — [Ettin Suite: SoTA Paired Encoders and Decoders](<training/Ettin Suite SoTA Paired Encoders and Decoders.md>) · `training` · huggingface
  Ettin is the first suite of paired encoder-only and decoder-only models (17M-1B params) trained on identical data (2T tokens), architecture and recipe, giving a true apples-to-apples MLM vs causal-LM comparison. The open ModernBERT-style recipe beats ModernBERT on encoder tasks and beats Llama 3.2 1B and SmolLM2 on decoder tasks; also tests cross-objective continued training.
- **2025-07-15** — [MuonClip and Kimi K2 training stability](<reasoning/MuonClip and Kimi K2 training stability.md>) · `reasoning` · fireworks
  Explains MuonClip as a stability technique for large-scale Kimi-style model training.
- **2025-07-11** — [Building with Grok 4](<releases/Building with Grok 4.md>) · `releases` · braintrust
  Notes on building with Grok 4, including model behavior, practical integration considerations, and evaluation needs for new model adoption.
- **2025-07-08** — [Efficient MultiModal Data Pipeline](<training/Efficient MultiModal Data Pipeline.md>) · `training` · huggingface
  Rebuilds nanoVLM's multimodal data pipeline in five stages to stop GPUs idling on padding: from naive padding to constrained batching and sequence packing with knapsack-style grouping, showing the padding-token waste eliminated at each step.
- **2025-07-08** — [SmolLM3: smol, multilingual, long-context reasoner](<training/SmolLM3 smol, multilingual, long-context reasoner.md>) · `training` · huggingface
  The full engineering blueprint for SmolLM3-3B: 11T tokens over a three-stage pretraining data mixture, NoPE + YaRN for 128k context, and a dual-mode (think / no_think) hybrid reasoning instruct model — beating Llama-3.2-3B and Qwen2.5-3B, with exact data mixes and the mid-training/APO alignment recipe published.
- **2025-06-26** — [Gemma 3n fully available in the open-source ecosystem!](<releases/Gemma 3n fully available in the open-source ecosystem!.md>) · `releases` · huggingface
  Gemma 3n E2B/E4B: models with 5B and 8B actual parameters that need only 2B/4B worth of VRAM (2-3 GB) thanks to per-layer embeddings and MatFormer nesting, paired with a MobileNet-V5-300 vision encoder (60 FPS on Pixel, beating ViT-Giant with 3x fewer params) and a USM-based audio encoder processing 160ms chunks.
- **2025-06-20** — [The Illusion of Thinking: What the Apple AI Paper Says About LLM Reasoning](<reasoning/The Illusion of Thinking What the Apple AI Paper Says About LLM Reasoning.md>) · `reasoning` · arize
  Analyzes the Apple reasoning paper and what it suggests about evaluating LLM reasoning limits.
- **2025-06-19** — [(LoRA) Fine-Tuning FLUX.1-dev on Consumer Hardware](<fine-tuning/(LoRA) Fine-Tuning FLUX.1-dev on Consumer Hardware.md>) · `fine-tuning` · huggingface
  Fine-tunes FLUX.1-dev with QLoRA under ~10GB of VRAM on a single RTX 4090 using bitsandbytes NF4, 8-bit optimizers and gradient checkpointing, and compares FP8 training with torchao for extra speed on compatible hardware.
- **2025-06-09** — [Reinforcement Fine Tuning: Train expert open models to surpass closed frontier models](<reinforcement-learning/Reinforcement Fine Tuning Train expert open models to surpass closed frontier models.md>) · `reinforcement-learning` · fireworks
  Introduces reinforcement fine-tuning for training expert open models beyond supervised baselines.
- **2025-06-04** — [Synthetic data pipeline for fine-tuning and evaluation](<fine-tuning/Synthetic data pipeline for fine-tuning and evaluation.md>) · `fine-tuning` · fireworks
  Describes a synthetic-data pipeline that connects task definition, generation, SFT/RFT, evaluation, and cleanup.
- **2025-06-03** — [No GPU left behind: Unlocking Efficiency with Co-located vLLM in TRL](<reinforcement-learning/No GPU left behind Unlocking Efficiency with Co-located vLLM in TRL.md>) · `reinforcement-learning` · huggingface
  In TRL's GRPO setup, running vLLM in server mode leaves generation and training GPUs idling in turn; co-locating vLLM in the same process/GPUs as the trainer (sharing memory via a gpu_memory_utilization split and sleep/wake between phases) removes the idle gap, with throughput and GPU-utilization numbers across model sizes and TP configs.
- **2025-05-28** — [Mixture-of-Agents Alignment for post-training](<fine-tuning/Mixture-of-Agents Alignment for post-training.md>) · `fine-tuning` · together
  Explains Mixture-of-Agents Alignment for improving post-training with collective model intelligence.
- **2025-05-22** — [Why Speech to Text Is the Hidden Engine Behind Contact Center AI Performance](<multimodal/Why Speech to Text Is the Hidden Engine Behind Contact Center AI Performance.md>) · `multimodal` · cresta
  Explains how speech-to-text quality drives downstream AI performance and why it should be treated as a system dependency.
- **2025-05-21** — [nanoVLM: The simplest repository to train your VLM in pure PyTorch](<multimodal/nanoVLM The simplest repository to train your VLM in pure PyTorch.md>) · `multimodal` · huggingface
  nanoVLM is a ~750-line pure-PyTorch VLM training repo (nanoGPT for vision): a SigLIP vision encoder plus a SmolLM2 language backbone joined by a pixel-shuffle modality-projection MLP, trainable to 35.3% on MMStar in ~6 hours on a single H100.
- **2025-05-16** — [Scalable Chain of Thoughts via Elastic Reasoning](<reasoning/Scalable Chain of Thoughts via Elastic Reasoning.md>) · `reasoning` · arize
  Summarizes elastic reasoning and scalable chain-of-thought ideas for allocating reasoning compute more flexibly.
- **2025-05-12** — [Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI: Tutorial](<fine-tuning/Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI Tutorial.md>) · `fine-tuning` · fireworks
  Tutorial for supervised fine-tuning with LoRA, including setup, training, and deployment workflow.
- **2025-05-12** — [Vision Language Models (Better, faster, stronger)](<multimodal/Vision Language Models (Better, faster, stronger).md>) · `multimodal` · huggingface
  A year-in-review of vision language models covering new model classes (any-to-any, reasoning VLMs, small on-device VLMs, MoE VLMs), multimodal RAG with ColPali-style late-interaction retrievers, VLM agents for GUI/computer use, video understanding, and how alignment/benchmarks for VLMs have evolved. Names the specific models and techniques behind each shift.
- **2025-04-29** — [Day zero benchmarks for Qwen 3 with SGLang on Baseten](<benchmarks/Day zero benchmarks for Qwen 3 with SGLang on Baseten.md>) · `benchmarks` · baseten
  Provides day-zero Qwen 3 benchmarks with SGLang and discusses serving-performance implications.
- **2025-04-18** — [Why Transcription Performance Is Holding Back Your AI Strategy](<multimodal/Why Transcription Performance Is Holding Back Your AI Strategy.md>) · `multimodal` · cresta
  Connects transcription performance to broader AI application quality, especially for voice-first systems.
- **2025-04-17** — [Continued Fine-tuning of LLMs: A Technical Deep Dive](<fine-tuning/Continued Fine-tuning of LLMs A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into continued fine-tuning of LLMs.
- **2025-04-17** — [Direct Preference Optimization: A Technical Deep Dive](<reinforcement-learning/Direct Preference Optimization A Technical Deep Dive.md>) · `reinforcement-learning` · together
  Technical deep dive into Direct Preference Optimization for aligning language models.
- **2025-04-11** — [40 Large Language Model Benchmarks and The Future of Model Evaluation](<benchmarks/40 Large Language Model Benchmarks and The Future of Model Evaluation.md>) · `benchmarks` · arize
  Surveys major LLM benchmarks and explains what different benchmark families measure for model evaluation.
- **2025-04-08** — [Arabic Leaderboards: Introducing Arabic Instruction Following, Updating AraGen, and More](<benchmarks/Arabic Leaderboards Introducing Arabic Instruction Following, Updating AraGen, and More.md>) · `benchmarks` · huggingface
  Updates the Arabic LLM evaluation stack: the 3C3H generative scoring metric (correctness, completeness, conciseness + helpfulness, honesty, harmlessness) behind AraGen-03-25, plus Arabic IFEval, the first public instruction-following benchmark for Arabic, consolidated in one Arabic-Leaderboards Space with MBZUAI.
- **2025-04-08** — [Tracing and Evaluating Gemini Audio with Arize](<multimodal/Tracing and Evaluating Gemini Audio with Arize.md>) · `multimodal` · arize
  Covers tracing and evaluation for Gemini audio applications, focusing on observability for multimodal systems.
- **2025-04-04** — [AI Benchmark Deep Dive: Gemini 2.5 and Humanity's Last Exam](<benchmarks/AI Benchmark Deep Dive Gemini 2.5 and Humanity's Last Exam.md>) · `benchmarks` · arize
  Paper-reading recap on Gemini 2.5 and Humanity's Last Exam, focusing on benchmark interpretation and what modern evaluation results do and do not show.
- **2025-03-12** — [Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost](<fine-tuning/Fine-Tuning DeepSeek v3 & R1 to optimize quality, latency, & cost.md>) · `fine-tuning` · fireworks
  Guide to fine-tuning DeepSeek V3 and R1 models while balancing quality, latency, and cost.
- **2025-03-12** — [Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM](<releases/Welcome Gemma 3 Google's all new multimodal, multilingual, long context open LLM.md>) · `releases` · huggingface
  Gemma 3 (1B-27B) adds a SigLIP vision encoder, 128k context (32k for 1B), 140+ languages, and interleaved local/global attention to keep long-context KV cache tractable; covers benchmarks and official QAT quantized checkpoints.
- **2025-03-04** — [Understanding Cresta’s Voice Platform - The Voice Stack](<multimodal/Understanding Cresta’s Voice Platform - The Voice Stack.md>) · `multimodal` · cresta
  Breaks down the components of a production voice AI stack, including telephony, speech, model, and orchestration layers.
- **2025-02-25** — [Minions: embracing small LMs, shifting compute on-device, and cutting cloud costs in the process](<reasoning/Minions embracing small LMs, shifting compute on-device, and cutting cloud costs in the process.md>) · `reasoning` · together
  Explores using small language models and on-device compute to reduce cloud inference costs.
- **2025-02-20** — [SmolVLM2: Bringing Video Understanding to Every Device](<multimodal/SmolVLM2 Bringing Video Understanding to Every Device.md>) · `multimodal` · huggingface
  SmolVLM2 brings video understanding to 2.2B, 500M and 256M parameter VLMs — the smallest video LMs released — with benchmark results on Video-MME/MLVU and demos running on an iPhone via MLX and in the browser. Covers the frame-sampling/visual-token budget that makes video feasible at these sizes and the transformers/MLX fine-tuning paths.
- **2025-02-07** — [DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical](<reasoning/DeepSeek v3 and R1 Model Architecture Why it's powerful and economical.md>) · `reasoning` · fireworks
  Explains DeepSeek V3 and R1 architecture choices, including why the models are efficient for reasoning workloads.
- **2025-01-31** — [Distillation with Reasoning: Can DeepSeek R1 Teach Better Than Humans?](<fine-tuning/Distillation with Reasoning Can DeepSeek R1 Teach Better Than Humans.md>) · `fine-tuning` · fireworks
  Discusses distilling reasoning behavior from DeepSeek R1 and the limits of teacher-model supervision.
- **2025-01-28** — [Open-R1: a fully open reproduction of DeepSeek-R1](<reinforcement-learning/Open-R1 a fully open reproduction of DeepSeek-R1.md>) · `reinforcement-learning` · huggingface
  Lays out the Open-R1 plan to fully reproduce DeepSeek-R1: distill reasoning traces from R1 to build an open SFT dataset, reimplement the pure-RL (GRPO) pipeline that produced R1-Zero without human supervision, and run the multi-stage RL+SFT recipe — naming the unknowns DeepSeek left out (data curation, hyperparameters, scaling trade-offs).
- **2025-01-27** — [Beyond Supervised Fine Tuning: How Reinforcement Learning Empowers AI with Minimal Labels](<reinforcement-learning/Beyond Supervised Fine Tuning How Reinforcement Learning Empowers AI with Minimal Labels.md>) · `reinforcement-learning` · fireworks
  Explains reinforcement learning with verifiable rewards as a way to improve models with minimal labels.
- **2025-01-22** — [Building Audio Support with OpenAI: Insights from our Journey](<multimodal/Building Audio Support with OpenAI Insights from our Journey.md>) · `multimodal` · arize
  Case study on adding audio support with OpenAI models, covering product and engineering lessons from building multimodal support.
- **2025-01-22** — [Evaluating and Monitoring Voice AI Agents](<multimodal/Evaluating and Monitoring Voice AI Agents.md>) · `multimodal` · langfuse
  Covers evaluation and monitoring for voice AI agents, including speech-specific quality signals and agent behavior beyond text-only evals.
- **2025-01-06** — [Claude SWE-Bench Performance](<benchmarks/Claude SWE-Bench Performance.md>) · `benchmarks` · anthropic-engineering
  How Anthropic scaffolded Claude 3.5 Sonnet to 49% on SWE-bench Verified with a minimal agent harness, detailing tool design and error analysis.
- **2024-12-19** — [Finally, a Replacement for BERT: Introducing ModernBERT](<architectures/Finally, a Replacement for BERT Introducing ModernBERT.md>) · `architectures` · huggingface
  ModernBERT (149M base / 395M large) modernizes the BERT encoder with 8192-token context, rotary embeddings, alternating global/local attention, GeGLU, unpadding and Flash Attention 2, trained on 2T tokens of web+code — a Pareto improvement over BERT/DeBERTa on both speed and accuracy and a slot-in replacement for retrieval and classification encoders.
- **2024-12-18** — [Bamba: Inference-Efficient Hybrid Mamba2 Model](<architectures/Bamba Inference-Efficient Hybrid Mamba2 Model.md>) · `architectures` · huggingface
  Bamba-9B is a hybrid Mamba2/transformer model trained by IBM, Princeton, CMU and UIUC on 2.2T tokens of fully open data, delivering 2.5x throughput and 2x lower latency than a comparable transformer in vLLM by shrinking the KV-cache memory-bandwidth bottleneck. Covers the hybrid architecture, training lineage, checkpoints and vLLM/transformers/llama.cpp enablement.
- **2024-12-17** — [Welcome to the Falcon 3 Family of Open Models!](<releases/Welcome to the Falcon 3 Family of Open Models!.md>) · `releases` · huggingface
  TII's Falcon 3 family (1B-10B, plus Mamba and quantized variants) trained with a single 14T-token pretraining run on 1024 H100s, then depth up-scaled from 7B to 10B by duplicating redundant layers and continuing pretraining on 2T more tokens. Reports SoTA zero/few-shot results for sub-13B models on math, code and science benchmarks.
- **2024-12-10** — [What is LLM fine-tuning?](<fine-tuning/What is LLM fine-tuning.md>) · `fine-tuning` · modal
  Overview of LLM fine-tuning concepts, when to fine-tune, and how training data and serving constraints affect the workflow.
- **2024-12-09** — [20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds](<multimodal/20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds.md>) · `multimodal` · fireworks
  Describes high-throughput Whisper transcription serving and the latency/cost tradeoffs in batch audio inference.
- **2024-12-05** — [Welcome PaliGemma 2 – New vision language models by Google](<multimodal/Welcome PaliGemma 2 – New vision language models by Google.md>) · `multimodal` · huggingface
  PaliGemma 2 pairs a SigLIP image encoder with Gemma 2 LLMs at 3B/10B/28B and 224/448/896px input resolutions, designed as pre-trained checkpoints intended to be fine-tuned per task rather than used zero-shot. Covers the resolution-vs-cost trade-off, DOCCI long-caption fine-tunes, and the transformers fine-tuning scripts/VQAv2 demo.
- **2024-11-26** — [SmolVLM - small yet mighty Vision Language Model](<multimodal/SmolVLM - small yet mighty Vision Language Model.md>) · `multimodal` · huggingface
  SmolVLM is a 2B VLM tuned for memory footprint: SigLIP vision encoder with aggressive pixel-shuffle visual-token compression (9x fewer tokens than Qwen2-VL), trained on the Cauldron and Docmatix, using ~5GB of GPU RAM at inference versus tens of GB for peers.
- **2024-11-25** — [You could have designed state of the art positional encoding](<architectures/You could have designed state of the art positional encoding.md>) · `architectures` · huggingface
  Derives RoPE from first principles by iteratively fixing naive positional-encoding schemes (integer positions, binary, sinusoidal) until arriving at rotary embeddings as used in Llama 3.2, then extends to 2D/context-length scaling.
- **2024-11-25** — [Fine-Tuning LLMs for Multi-Turn Conversations: A Technical Deep Dive](<fine-tuning/Fine-Tuning LLMs for Multi-Turn Conversations A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into fine-tuning LLMs for multi-turn conversations.
- **2024-11-25** — [Long Context Fine-Tuning: A Technical Deep Dive](<fine-tuning/Long Context Fine-Tuning A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into long-context fine-tuning.
- **2024-11-14** — [Evaluating Gemini models for vision](<multimodal/Evaluating Gemini models for vision.md>) · `multimodal` · braintrust
  Evaluates Gemini vision models and shows how multimodal evals can compare image-understanding behavior across model versions.
- **2024-11-04** — [Building serverless apps with the OpenAI Realtime API](<multimodal/Building serverless apps with the OpenAI Realtime API.md>) · `multimodal` · braintrust
  Guide to building serverless apps with the OpenAI Realtime API, focusing on real-time voice interaction architecture and deployment patterns.
- **2024-10-15** — [Google's NotebookLM and the Future of AI-Generated Audio](<multimodal/Google's NotebookLM and the Future of AI-Generated Audio.md>) · `multimodal` · arize
  Paper-reading style overview of Google NotebookLM and AI-generated audio as a multimodal product pattern.
- **2024-10-14** — [Linearizing LLMs with LoLCATs](<reasoning/Linearizing LLMs with LoLCATs.md>) · `reasoning` · together
  Explains LoLCATs for linearizing LLM attention while preserving useful behavior.
- **2024-10-01** — [🇨🇿 BenCzechMark - Can your LLM Understand Czech?](<benchmarks/🇨🇿 BenCzechMark - Can your LLM Understand Czech.md>) · `benchmarks` · huggingface
  Introduces BenCzechMark, a Czech LLM evaluation suite of 50 tasks across 9 categories (90% natively Czech, not translated) with a leaderboard covering 25+ open models, plus its statistical duel-based ranking methodology.
- **2024-09-27** — [Exploring OpenAI's o1-preview and o1-mini](<reasoning/Exploring OpenAI's o1-preview and o1-mini.md>) · `reasoning` · arize
  Analyzes OpenAI o1-preview and o1-mini from a reasoning-model perspective, including expected strengths, limits, and evaluation implications for production teams.
- **2024-09-25** — [Llama can now see and run on your device - welcome Llama 3.2](<releases/Llama can now see and run on your device - welcome Llama 3.2.md>) · `releases` · huggingface
  Llama 3.2 adds 11B/90B vision models (cross-attention adapter over a frozen text backbone, via the new MllamaForConditionalGeneration) and 1B/3B on-device text models, plus a vision-capable Llama Guard 3 and a 1B Llama Guard for input/output safety classification.
- **2024-09-19** — [Breaking Down Reflection Tuning: Enhancing LLM Performance with Self-Learning](<fine-tuning/Breaking Down Reflection Tuning Enhancing LLM Performance with Self-Learning.md>) · `fine-tuning` · arize
  Explains reflection tuning as a self-learning approach for improving LLM performance through critique and iterative refinement.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-09-11** — [Composable Interventions for Language Models](<reasoning/Composable Interventions for Language Models.md>) · `reasoning` · arize
  Deep dive on composable interventions for language models, covering techniques for steering or modifying model behavior.
- **2024-09-09** — [The Mamba in the Llama: Distilling and Accelerating Hybrid Models](<fine-tuning/The Mamba in the Llama Distilling and Accelerating Hybrid Models.md>) · `fine-tuning` · together
  Explains distilling and accelerating hybrid Mamba/Transformer models.
- **2024-08-12** — [Welcome Falcon Mamba: The first strong attention-free 7B model](<architectures/Welcome Falcon Mamba The first strong attention-free 7B model.md>) · `architectures` · huggingface
  Falcon Mamba 7B is a pure SSM (Mamba with extra RMSNorm for training stability) trained on 5.8T tokens: constant per-token generation time and flat memory regardless of context length, with throughput and benchmark comparisons against attention-based 7Bs.
- **2024-08-06** — [Breaking Down Meta's Llama 3 Herd of Models](<releases/Breaking Down Meta's Llama 3 Herd of Models.md>) · `releases` · arize
  Technical overview of Meta's Llama 3 model family, including architecture, capabilities, and benchmark interpretation.
- **2024-07-31** — [Google releases Gemma 2 2B, ShieldGemma and Gemma Scope](<releases/Google releases Gemma 2 2B, ShieldGemma and Gemma Scope.md>) · `releases` · huggingface
  Google's July 2024 Gemma drop: Gemma 2 2B distilled from larger models for on-device use, ShieldGemma safety classifiers for filtering app inputs/outputs, and Gemma Scope sparse autoencoders for interpretability.
- **2024-07-25** — [Deploying custom ComfyUI workflows as APIs](<multimodal/Deploying custom ComfyUI workflows as APIs.md>) · `multimodal` · baseten
  Shows how to deploy custom ComfyUI image-generation workflows behind API endpoints.
- **2024-07-23** — [Llama 3.1 - 405B, 70B & 8B with multilinguality and long context](<releases/Llama 3.1 - 405B, 70B & 8B with multilinguality and long context.md>) · `releases` · huggingface
  Llama 3.1 8B/70B/405B: 128k context via a new RoPE scaling recipe, 15T-token training, and the accompanying Llama Guard 3 safety classifier and Prompt Guard jailbreak/prompt-injection detector; covers FP8/AWQ/GPTQ quantization needed to actually serve 405B, TGI deployment, and using 405B for synthetic data and LLM-as-judge.
- **2024-07-18** — [Docmatix - a huge dataset for Document Visual Question Answering](<training/Docmatix - a huge dataset for Document Visual Question Answering.md>) · `training` · huggingface
  Builds Docmatix, a DocVQA dataset of 2.4M images / 9.5M Q&A pairs from 1.3M PDFs (240x prior scale) by prompting Phi-3-small over PDFA OCR transcriptions and filtering ~15% hallucinated pairs; fine-tuning Florence-2 on it shows the resulting gains.
- **2024-07-16** — [SmolLM - blazingly fast and remarkably powerful](<training/SmolLM - blazingly fast and remarkably powerful.md>) · `training` · huggingface
  SmolLM 135M/360M/1.7B and the SmolLM-Corpus behind them: Cosmopedia v2 synthetic textbooks generated with Mixtral (28B tokens), FineWeb-Edu (220B tokens) filtered by a Llama3-labeled educational classifier, plus the training recipe and benchmarks vs same-size models.
- **2024-07-12** — [Fine-tuning Llama-3 toward GPT-4 performance at lower cost](<fine-tuning/Fine-tuning Llama-3 toward GPT-4 performance at lower cost.md>) · `fine-tuning` · together
  Shows fine-tuning Llama 3 toward GPT-4-like task performance at lower cost.
- **2024-07-11** — [How NuminaMath Won the 1st AIMO Progress Prize](<reasoning/How NuminaMath Won the 1st AIMO Progress Prize.md>) · `reasoning` · huggingface
  How NuminaMath 7B won the first AIMO Progress Prize (29/50 on the private set): two-stage SFT of DeepSeekMath-Base — first on chain-of-thought math data, then on a tool-integrated reasoning dataset where the model writes and executes Python — plus self-consistency decoding over majority-voted candidates and vLLM + 8-bit quantization to fit the 2xT4 Kaggle time budget.
- **2024-07-10** — [Preference Optimization for Vision Language Models](<fine-tuning/Preference Optimization for Vision Language Models.md>) · `fine-tuning` · huggingface
  Walks through direct preference optimization (DPO) for vision language models using TRL's new VLM support, fine-tuning Idefics2-8B on the RLAIF-V preference dataset to reduce hallucination. Covers preference-data format, the reference-model/beta setup, LoRA + 4-bit config and the memory considerations for VLM DPO.
- **2024-06-27** — [Welcome Gemma 2 - Google’s new open LLM](<releases/Welcome Gemma 2 - Google’s new open LLM.md>) · `releases` · huggingface
  Google's Gemma 2 (9B/27B, 8K context, 13T/8T training tokens) introduces interleaved sliding-window and full attention, logit soft-capping, and knowledge distillation from a larger teacher for the 9B model, plus WARP-style model merging. Explains why soft-capping must be disabled to use Flash Attention 2, and covers transformers/TRL fine-tuning support.
- **2024-06-24** — [Fine-tuning Florence-2 - Microsoft's Cutting-edge Vision Language Models](<fine-tuning/Fine-tuning Florence-2 - Microsoft's Cutting-edge Vision Language Models.md>) · `fine-tuning` · huggingface
  Fine-tunes Microsoft's Florence-2 vision-language model on DocVQA, which the released checkpoints don't support: seq2seq task formulation, freezing the vision encoder, and a DDP training loop with batch collation for image+text pairs.
- **2024-06-14** — [Comparing few-step image generation models](<benchmarks/Comparing few-step image generation models.md>) · `benchmarks` · baseten
  Compares few-step image generation models and the tradeoffs between speed and output quality.
- **2024-06-14** — [LLM Interpretability and Sparse Autoencoders: Research from OpenAI and Anthropic](<reasoning/LLM Interpretability and Sparse Autoencoders Research from OpenAI and Anthropic.md>) · `reasoning` · arize
  Explains sparse autoencoders and interpretability research from OpenAI and Anthropic as tools for understanding model internals.
- **2024-06-13** — [From DeepSpeed to FSDP and Back Again with Hugging Face Accelerate](<training/From DeepSpeed to FSDP and Back Again with Hugging Face Accelerate.md>) · `training` · huggingface
  Debugs why Mistral-7B bf16 training converged under DeepSpeed but not FSDP: DeepSpeed silently upcasts master weights to fp32 while FSDP flattens in the model dtype; explains the mixed-precision differences and how Accelerate now aligns them.
- **2024-06-12** — [Putting RL back in RLHF](<reinforcement-learning/Putting RL back in RLHF.md>) · `reinforcement-learning` · huggingface
  Introduces TRL's RLOO (REINFORCE Leave-One-Out) trainer as a lighter alternative to PPO for online RLHF: it drops the value network and uses other samples in the batch as the baseline, cutting GPU memory and wall-clock time to convergence while matching PPO's GPT-4-judged win rate and beating offline DPO.
- **2024-06-06** — [Dragonfly: A large vision-language model with multi-resolution zoom](<multimodal/Dragonfly A large vision-language model with multi-resolution zoom.md>) · `multimodal` · together
  Introduces Dragonfly, a vision-language model with multi-resolution zoom.
- **2024-06-04** — [How latent consistency models work](<multimodal/How latent consistency models work.md>) · `multimodal` · baseten
  Explains latent consistency models and how they enable faster image generation.
- **2024-05-24** — [Falcon 2: An 11B parameter pretrained language model and VLM, trained on over 5000B tokens and 11 languages](<releases/Falcon 2 An 11B parameter pretrained language model and VLM, trained on over 5000B tokens and 11 languages.md>) · `releases` · huggingface
  Falcon2-11B: 11B params trained on 5,000B tokens of RefinedWeb in a four-stage curriculum that raises context length 2048 -> 4096 -> 8192 with a final high-quality-data stage, plus a VLM variant; benchmarked against Llama 3 8B and Gemma 7B.
- **2024-05-21** — [Create an infinite icon library by fine-tuning Stable Diffusion](<fine-tuning/Create an infinite icon library by fine-tuning Stable Diffusion.md>) · `fine-tuning` · modal
  Practical example of fine-tuning Stable Diffusion for a custom image-generation domain using Modal infrastructure.
- **2024-05-05** — [Introducing the Open Leaderboard for Hebrew LLMs!](<benchmarks/Introducing the Open Leaderboard for Hebrew LLMs!.md>) · `benchmarks` · huggingface
  An open leaderboard for Hebrew LLMs, motivated by Hebrew's root-and-pattern morphology breaking tokenization strategies designed for simpler languages; it evaluates on Hebrew-native tasks (Q&A, sentiment, winograd, translation) rather than translated English benchmarks.
- **2024-05-01** — [FAQ: Building LLMs with RedPajama-v2, a 30 trillion token web dataset](<fine-tuning/FAQ Building LLMs with RedPajama-v2, a 30 trillion token web dataset.md>) · `fine-tuning` · together
  FAQ-style technical explanation of building LLMs with the RedPajama-v2 dataset.
- **2024-04-29** — [How fine tuned LLMs power knowledge assist, summarization, and chat suggestions](<fine-tuning/How fine tuned LLMs power knowledge assist, summarization, and chat suggestions.md>) · `fine-tuning` · cresta
  Explains how fine-tuned LLMs support knowledge assist, summarization, and chat suggestions in production workflows.
- **2024-04-29** — [StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation](<fine-tuning/StarCoder2-Instruct Fully Transparent and Permissive Self-Alignment for Code Generation.md>) · `fine-tuning` · huggingface
  StarCoder2-15B-Instruct self-aligns with no GPT-4 distillation: it mines seed functions from The Stack v1, has the model generate its own code instructions and responses, then filters by executing the generated tests in a sandbox. Scores 72.6 on HumanEval (above CodeLlama-70B-Instruct's 72.0) and beats the same model trained on GPT-4-distilled data on LiveCodeBench.
- **2024-04-26** — [Beating proprietary models with a quick fine-tune](<fine-tuning/Beating proprietary models with a quick fine-tune.md>) · `fine-tuning` · modal
  Explains fine-tuning embedding models to beat proprietary baselines for a retrieval task with a compact training loop.
- **2024-04-23** — [Introducing the Open Chain of Thought Leaderboard](<reasoning/Introducing the Open Chain of Thought Leaderboard.md>) · `reasoning` · huggingface
  The Open CoT Leaderboard measures the *accuracy gain* a model gets from generating a chain-of-thought trace rather than raw accuracy, scoring several CoT prompting regimes across reasoning benchmarks to see which models actually benefit from thinking step by step.
- **2024-04-22** — [Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent](<reinforcement-learning/Jack of All Trades, Master of Some, a Multi-Purpose Transformer Agent.md>) · `reinforcement-learning` · huggingface
  JAT is an open reproduction of DeepMind's Gato: a multimodal transformer agent trained on hundreds of thousands of expert trajectories (Atari, BabyAI, Meta-World, MuJoCo) released as the JAT dataset, with architectural changes for handling sequential observations and continuous values.
- **2024-04-19** — [The Open Medical-LLM Leaderboard: Benchmarking Large Language Models in Healthcare](<benchmarks/The Open Medical-LLM Leaderboard Benchmarking Large Language Models in Healthcare.md>) · `benchmarks` · huggingface
  The Open Medical-LLM Leaderboard aggregates MedQA (USMLE), MedMCQA, PubMedQA and MMLU medical subsets into a standardized accuracy benchmark for clinical LLMs, motivated by failure cases like GPT-3 recommending tetracycline to a pregnant patient while correctly explaining its contraindication.
- **2024-04-18** — [Streaming real-time text to speech with XTTS V2](<multimodal/Streaming real-time text to speech with XTTS V2.md>) · `multimodal` · baseten
  Covers streaming real-time text-to-speech serving with XTTS v2.
- **2024-04-18** — [Welcome Llama 3 - Meta's new open LLM](<releases/Welcome Llama 3 - Meta's new open LLM.md>) · `releases` · huggingface
  Meta's Llama 3 (8B and 70B, base + instruct, 8K context) with a 128,256-token tokenizer (up from 32K), grouped-query attention on both sizes, and 15T pretraining tokens; also ships Llama Guard 2 for input/output safety classification. Explains the tokenizer/embedding-size trade-off and the KV-cache benefit of GQA at 8B.
- **2024-04-15** — [Introducing Idefics2: A Powerful 8B Vision-Language Model for the community](<multimodal/Introducing Idefics2 A Powerful 8B Vision-Language Model for the community.md>) · `multimodal` · huggingface
  Idefics2-8B vision-language model: native image resolution/aspect-ratio handling, a learned-pooling perceiver to cut image tokens to 64 per image, and its OBELICS/PDF-heavy training mix, benchmarked against DeepSeek-VL and LLaVA-NeXT.
- **2024-04-11** — [Vision Language Models Explained](<multimodal/Vision Language Models Explained.md>) · `multimodal` · huggingface
  Explainer on vision-language model internals: image encoder + projection into the LLM embedding space, contrastive (CLIP) vs generative pretraining, common open VLMs, and how to fine-tune them with TRL/SFT.
- **2024-04-09** — [CodeGemma - an official Google release for code LLMs](<releases/CodeGemma - an official Google release for code LLMs.md>) · `releases` · huggingface
  Google's CodeGemma ships 2B (infilling-specialized), 7B base and 7B instruct code models built on Gemma, trained with fill-in-the-middle (FIM) objectives on ~500B tokens of code. Details the FIM prompt formatting/tokens needed to actually use the base models plus HumanEval/MBPP/GSM8K results.
- **2024-04-04** — [Demystifying Amazon's Chronos: Learning the Language of Time Series](<releases/Demystifying Amazon's Chronos Learning the Language of Time Series.md>) · `releases` · arize
  Deep dive into Amazon Chronos for time-series modeling, including model behavior and evaluation context.
- **2024-03-26** — [Anthropic Claude 3](<releases/Anthropic Claude 3.md>) · `releases` · arize
  Overview of Anthropic Claude 3 model releases and capabilities, including model comparisons and implications for LLM application builders.
- **2024-03-20** — [Cosmopedia: how to create large-scale synthetic data for pre-training Large Language Models](<training/Cosmopedia how to create large-scale synthetic data for pre-training Large Language Models.md>) · `training` · huggingface
  How Cosmopedia was built: 30M synthetic textbooks/blogs/stories (25B tokens) generated with Mixtral-8x7B-Instruct to reproduce Phi-1.5's pretraining data, with most of the effort going into prompt curation for topic diversity — reaching <1% duplicate content — plus the clustering and generation stack used at scale.
- **2024-03-15** — [Reinforcement Learning in the Era of LLMs](<reinforcement-learning/Reinforcement Learning in the Era of LLMs.md>) · `reinforcement-learning` · arize
  Explains reinforcement learning concepts in the LLM era and how RL fits into model improvement workflows.
- **2024-03-04** — [BASED: Simple linear attention language models balance the recall-throughput tradeoff](<reasoning/BASED Simple linear attention language models balance the recall-throughput tradeoff.md>) · `reasoning` · together
  Explains BASED linear-attention language models and the recall-throughput tradeoff.
- **2024-02-28** — [StarCoder2 and The Stack v2](<releases/StarCoder2 and The Stack v2.md>) · `releases` · huggingface
  StarCoder2 (3B/7B/15B) code LLMs trained on 3-4T tokens of The Stack v2 (67.5 TB, 600+ languages, repository-grouped so models see repo context), using Grouped Query Attention, 16k context with 4k sliding-window attention and a Fill-in-the-Middle objective; the 15B matches 33B+ models on many evals.
- **2024-02-27** — [Evo: Long-context modeling from molecular to genome scale](<reasoning/Evo Long-context modeling from molecular to genome scale.md>) · `reasoning` · together
  Explains Evo and long-context modeling from molecular to genome-scale sequences.
- **2024-02-23** — [Fine-Tuning Gemma Models in Hugging Face](<fine-tuning/Fine-Tuning Gemma Models in Hugging Face.md>) · `fine-tuning` · huggingface
  How to LoRA/QLoRA fine-tune Gemma with Transformers + PEFT on both GPUs (bitsandbytes 4-bit on a free Colab) and Cloud TPUs via PyTorch/XLA with FSDP-through-SPMD, including which layers to attach adapters to.
- **2024-02-21** — [Welcome Gemma - Google’s new open LLM](<releases/Welcome Gemma - Google’s new open LLM.md>) · `releases` · huggingface
  Google's Gemma 2B/7B open LLMs: architecture notes (multi-query attention for 2B, GeGLU, RMSNorm, 8k context, 256k vocab), benchmark results, and the integration surface for fine-tuning with PEFT/TRL and serving with TGI.
- **2024-02-20** — [BitDelta: Your Fine-Tune May Only Be Worth One Bit](<fine-tuning/BitDelta Your Fine-Tune May Only Be Worth One Bit.md>) · `fine-tuning` · together
  Explains BitDelta and how small weight deltas can represent fine-tuned model changes.
- **2024-02-19** — [🤗 PEFT welcomes new merging methods](<fine-tuning/🤗 PEFT welcomes new merging methods.md>) · `fine-tuning` · huggingface
  Adds LoRA adapter merging to PEFT via add_weighted_adapter, supporting linear/cat/TIES/DARE (and their SVD variants) so multiple adapters from the same base model can be combined on the fly without downloading and merging full checkpoints. Explains when TIES/DARE's sign-election and drop-and-rescale steps beat naive weighted averaging.
- **2024-02-16** — [Synthetic data: save money, time and carbon with open source](<fine-tuning/Synthetic data save money, time and carbon with open source.md>) · `fine-tuning` · huggingface
  Uses Mixtral-8x7B to generate synthetic labels that train a small RoBERTa classifier for investor sentiment: matches GPT-4 accuracy (94%, 0.94 F1 macro) while costing ~$2.7 vs $3061 to label the corpus, at 0.13s latency and ~0.12kg CO2.
- **2024-02-01** — [Constitutional AI with Open LLMs](<reinforcement-learning/Constitutional AI with Open LLMs.md>) · `reinforcement-learning` · huggingface
  Reproduces Anthropic's Constitutional AI with open models: self-critique/revision against written principles produces an AI-feedback preference dataset used to DPO-align Mistral-7B, yielding the mistral-7b-anthropic model.
- **2024-01-31** — [Phi-2 Model](<releases/Phi-2 Model.md>) · `releases` · arize
  Technical overview of Phi-2, including model characteristics, benchmark behavior, and small-model implications.
- **2024-01-18** — [Preference Tuning LLMs with Direct Preference Optimization Methods](<fine-tuning/Preference Tuning LLMs with Direct Preference Optimization Methods.md>) · `fine-tuning` · huggingface
  Empirical head-to-head of DPO vs IPO vs KTO in TRL on two SFT'd 7B models (Zephyr and OpenHermes), sweeping the beta hyperparameter and scoring on MT-Bench; finds DPO/IPO roughly on par and beating KTO in the paired-preference setting, with beta mattering more than algorithm choice. Includes an errata where a summed-vs-averaged log-likelihood bug in TRL's IPO loss changed the results.
- **2024-01-16** — [Generation configurations: temperature, top-k, top-p, and test time compute](<reasoning/Generation configurations temperature, top-k, top-p, and test time compute.md>) · `reasoning` · chip-huyen
  Explains decoding parameters such as temperature, top-k, top-p, and test-time compute, connecting generation configuration to reliability, diversity, latency, and cost.
- **2023-12-27** — [Mistral AI (Mixtral-8x7B): Performance, Benchmarks](<releases/Mistral AI (Mixtral-8x7B) Performance, Benchmarks.md>) · `releases` · arize
  Technical overview of Mistral and Mixtral model behavior, performance, and benchmark positioning.
- **2023-12-08** — [How to serve your ComfyUI model behind an API endpoint](<multimodal/How to serve your ComfyUI model behind an API endpoint.md>) · `multimodal` · baseten
  Shows how to serve a ComfyUI model behind an API endpoint for production image workflows.
- **2023-12-08** — [StripedHyena-7B and efficient architectures beyond Transformers](<reasoning/StripedHyena-7B and efficient architectures beyond Transformers.md>) · `reasoning` · together
  Introduces StripedHyena-7B and efficient architectures beyond Transformers.
- **2023-12-05** — [Extraction Benchmarking](<benchmarks/Extraction Benchmarking.md>) · `benchmarks` · langchain
  Benchmarking post for extraction tasks, comparing structured-output performance and evaluation approaches for information extraction.
- **2023-11-22** — [Sharing LangSmith Benchmarks](<benchmarks/Sharing LangSmith Benchmarks.md>) · `benchmarks` · langchain
  Shares LangSmith benchmarks for evaluating models and chains, including methodology and public comparison workflows.
- **2023-11-14** — [The Geometry of Truth: Emergent Linear Structure in LLM Representation of True/False Datasets](<reasoning/The Geometry of Truth Emergent Linear Structure in LLM Representation of TrueFalse Datasets.md>) · `reasoning` · arize
  Summarizes research on linear structure in LLM representations of truth and falsehood, relevant to interpretability.
- **2023-11-02** — [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](<reasoning/Towards Monosemanticity Decomposing Language Models With Dictionary Learning.md>) · `reasoning` · arize
  Summarizes monosemanticity and dictionary learning work for decomposing language model internals.
- **2023-10-30** — [RedPajama-Data-v2: An open dataset with 30 trillion tokens for training large language models](<fine-tuning/RedPajama-Data-v2 An open dataset with 30 trillion tokens for training large language models.md>) · `fine-tuning` · together
  Introduces RedPajama-Data-v2, a large web dataset for training language models.
- **2023-10-16** — [Testing Fine Tuned Open Source Models in LangSmith](<fine-tuning/Testing Fine Tuned Open Source Models in LangSmith.md>) · `fine-tuning` · langchain
  Shows how to test fine-tuned open-source models in LangSmith using evaluations and comparison workflows.
- **2023-10-10** — [Multimodality and Large Multimodal Models (LMMs)](<multimodal/Multimodality and Large Multimodal Models (LMMs).md>) · `multimodal` · chip-huyen
  Explains large multimodal model architecture and training patterns, modality fusion, data challenges, and product capabilities unlocked by image, text, audio, and video models.
- **2023-10-06** — [Explaining Grokking Through Circuit Efficiency](<reasoning/Explaining Grokking Through Circuit Efficiency.md>) · `reasoning` · arize
  Paper-reading deep dive on grokking and circuit efficiency as a way to understand model generalization.
- **2023-08-24** — [Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading](<reasoning/Skeleton of Thought LLMs Can Do Parallel Decoding Paper Reading.md>) · `reasoning` · arize
  Summarizes Skeleton of Thought and how parallel decoding can speed structured reasoning.
- **2023-08-16** — [Open challenges in LLM research](<reasoning/Open challenges in LLM research.md>) · `reasoning` · chip-huyen
  Surveys open LLM research problems around hallucination, context length, efficiency, multimodality, agents, evaluation, and post-training behavior that shape engineering constraints.
- **2023-08-07** — [Extending the Context Window of LLaMA Models Paper Reading](<reasoning/Extending the Context Window of LLaMA Models Paper Reading.md>) · `reasoning` · arize
  Explains techniques for extending LLaMA context windows and the tradeoffs involved in long-context model behavior.
- **2023-08-04** — [Llama 2: Open Foundation and Fine-Tuned Chat Models Paper Reading](<releases/Llama 2 Open Foundation and Fine-Tuned Chat Models Paper Reading.md>) · `releases` · arize
  Technical paper-reading summary of Llama 2, including foundation and chat-tuned model behavior.
- **2023-07-25** — [Lost in the Middle: How Language Models Use Long Contexts Paper Reading](<reasoning/Lost in the Middle How Language Models Use Long Contexts Paper Reading.md>) · `reasoning` · arize
  Summarizes the Lost in the Middle findings on long-context model behavior and retrieval sensitivity.
- **2023-07-25** — [Monarch Mixer: A new model architecture for increased efficiency](<reasoning/Monarch Mixer A new model architecture for increased efficiency.md>) · `reasoning` · together
  Introduces Monarch Mixer as an efficient model architecture.
- **2023-07-14** — [Orca: Progressive Learning from Complex Explanation Traces of GPT-4 Paper Reading](<fine-tuning/Orca Progressive Learning from Complex Explanation Traces of GPT-4 Paper Reading.md>) · `fine-tuning` · arize
  Summarizes Orca and progressive learning from GPT-4 explanation traces as a post-training strategy.
- **2023-07-12** — [Multi-Query Attention is All You Need](<reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
- **2023-07-03** — [One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning](<fine-tuning/One-for-All Generalized LoRA for Parameter-Efficient Fine-tuning.md>) · `fine-tuning` · arize
  Summarizes Generalized LoRA as a parameter-efficient fine-tuning method and explains where it fits in adaptation workflows.
- **2023-06-15** — [Three techniques to adapt LLMs for any use case](<fine-tuning/Three techniques to adapt LLMs for any use case.md>) · `fine-tuning` · baseten
  Explains prompt engineering, fine-tuning, and related techniques for adapting LLMs to use cases.
- **2023-06-12** — [LoRA: Low-Rank Adaptation of Large Language Models Paper Reading and Discussion](<fine-tuning/LoRA Low-Rank Adaptation of Large Language Models Paper Reading and Discussion.md>) · `fine-tuning` · arize
  Paper-reading guide to LoRA and why low-rank adaptation is useful for efficient LLM fine-tuning.
- **2023-06-02** — [LIMA: Less Is More for Alignment - Paper Reading and Discussion](<fine-tuning/LIMA Less Is More for Alignment - Paper Reading and Discussion.md>) · `fine-tuning` · arize
  Summarizes LIMA and the idea that small high-quality instruction data can have outsized impact on alignment tuning.
- **2023-06-01** — [Drag Your GAN: Interactive Point-Based Manipulation on the Generative Image Manifold](<multimodal/Drag Your GAN Interactive Point-Based Manipulation on the Generative Image Manifold.md>) · `multimodal` · arize
  Paper-reading deep dive on DragGAN and interactive point-based image manipulation in generative model latent spaces.
- **2023-05-05** — [OpenAI on Reinforcement Learning With Human Feedback (RLHF)](<reinforcement-learning/OpenAI on Reinforcement Learning With Human Feedback (RLHF).md>) · `reinforcement-learning` · arize
  Summarizes RLHF concepts from OpenAI and how human feedback changes model behavior during post-training.
- **2023-05-02** — [RLHF: Reinforcement Learning from Human Feedback](<reinforcement-learning/RLHF Reinforcement Learning from Human Feedback.md>) · `reinforcement-learning` · chip-huyen
  Explains the RLHF pipeline from preference data through reward modeling and policy optimization, including why human feedback changes model behavior and where evaluation matters.
- **2023-03-29** — [Hungry Hungry Hippos (H3) and Language Modeling with State Space Models](<reasoning/Hungry Hungry Hippos (H3) and Language Modeling with State Space Models.md>) · `reasoning` · arize
  Explains H3/state-space model ideas as alternatives to standard attention and why they matter for sequence modeling efficiency.
- **2023-01-23** — [FlashConv: speeding up state space models](<reasoning/FlashConv speeding up state space models.md>) · `reasoning` · together
  Explains FlashConv and efficient state-space model execution.
- **2022-11-17** — [HELM: benchmarking large language models on the Together Research Computer](<benchmarks/HELM benchmarking large language models on the Together Research Computer.md>) · `benchmarks` · together
  Describes HELM benchmarking on the Together Research Computer.
- **2022-02-10** — [Why Transcription is Vital to Contact Center AI](<multimodal/Why Transcription is Vital to Contact Center AI.md>) · `multimodal` · cresta
  Explains why transcription quality is a core dependency for downstream AI systems that operate on spoken conversations.
- **2021-01-13** — [Action Directed GPT-2](<reasoning/Action Directed GPT-2.md>) · `reasoning` · cresta
  Explains Action Directed GPT-2 as an early pattern for steering language model behavior toward actions, relevant to tool-using and task-oriented agents.
- **2017-06-12** — **[Paper]** [Attention Is All You Need](<architectures/[Paper] Attention Is All You Need.md>) · `architectures` · arxiv
  Introduces the Transformer: a sequence model built purely on multi-head self-attention with no recurrence or convolution, hitting 28.4 BLEU on WMT14 EN-DE while training in 3.5 days on 8 GPUs. The architecture every modern LLM descends from.
- **2014-12-22** — **[Paper]** [Adam: A Method for Stochastic Optimization](<training/[Paper] Adam A Method for Stochastic Optimization.md>) · `training` · arxiv
  Introduces Adam, a first-order optimizer combining momentum with per-parameter adaptive learning rates from first and second gradient-moment estimates, with bias correction. Little memory overhead, robust to sparse gradients and non-stationary objectives; the default optimizer for training neural nets since.

## Also relevant (filed elsewhere)

- **2026-07-23** — [Bringing Nunchaku 4-bit Diffusion Inference to Diffusers](<../inference/quantization/Bringing Nunchaku 4-bit Diffusion Inference to Diffusers.md>) · `quantization` · huggingface
  Diffusers now natively loads Nunchaku's SVDQuant W4A4 checkpoints via from_pretrained() and the Hugging Face `kernels` package, requiring no local CUDA compilation; unlike weight-only quantization, SVDQuant runs transformer layers in 4-bit weights and activations, cutting both memory and denoising-loop latency.
- **2026-07-23** — [How to choose an AI model: lessons from Notion and Gamma](<../product-engineering/case-studies/How to choose an AI model lessons from Notion and Gamma.md>) · `case-studies` · baseten
  Panel takeaways from Notion and Gamma on production model selection: harnesses shouldn't be model-agnostic, model switching pays for itself via A/B testing against real users, pick models per-workflow using cost-per-capability-per-second, and open-weight models plus targeted RL now compete with closed frontier models on many workloads.
- **2026-07-16** — [Real-time video generation inference on Baseten](<../inference/optimization/Real-time video generation inference on Baseten.md>) · `optimization` · baseten
  Details Baseten's real-time video inference runtime for Wan 2.2, combining four-step timestep distillation (~20x), custom kernel fusion (~1.5x), and NVFP4 quantization (~1.5x) for a combined 53.6x speedup, cutting per-clip generation from over two minutes to 2.75 seconds and cost from 5 cents to under a sixth of a cent.
- **2026-07-15** — [Inkling by Thinking Machines now available on Modal | Modal Blog](<../inference/speculative-decoding/Inkling by Thinking Machines now available on Modal Modal Blog.md>) · `speculative-decoding` · modal
  Describes adapting Z Lab's DFlash block-diffusion speculator to Thinking Machines' Inkling (which uses five sliding-window attention layers per full-attention layer), making the drafter all-local-attention and causal for kernel support, reaching 250 tok/s/user at 2.5M TPM per GPU, 67% faster than Inkling's built-in MTP speculative path.
- **2026-07-15** — [Introducing Real World VoiceEQ: Measuring the human quality of voice AI](<../evals-observability/benchmark-design/Introducing Real World VoiceEQ Measuring the human quality of voice AI.md>) · `benchmark-design` · huggingface
  Hume AI's Real World VoiceEQ benchmark evaluates 40+ voice models across ASR, TTS, speech-to-speech, and speech understanding using 1M+ human ratings (785K TTS, 48K STS), finding no single model tops all 8 TTS capability groups and that speech-language-model judges disagree with human raters on subjective calls like emotional fit or identity consistency.
- **2026-07-08** — [Tuning the harness, not the model: a Nemotron 3 Ultra playbook](<../agents/harness/Tuning the harness, not the model a Nemotron 3 Ultra playbook.md>) · `harness` · langchain
  Nemotron 3 Ultra playbook arguing for harness tuning over model tuning, with practical agent-system design and eval implications.
- **2026-06-30** — [Multi-token Residual Prediction](<../inference/speculative-decoding/Multi-token Residual Prediction.md>) · `speculative-decoding` · modal
  Explains multi-token residual prediction as an inference acceleration technique for generating multiple tokens per step.
- **2026-06-30** — [Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval](<../rag-retrieval/search/Benchmarking GLM-5.2 vs Opus 4.8 for real-world long-context retrieval.md>) · `search` · braintrust
  Benchmarks GLM-5.2 against Opus 4.8 on real-world long-context retrieval, focusing on retrieval quality under large-context conditions.
- **2026-06-24** — [Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.](<../agents/multi-agent/Frontier AI at a fraction of the cost open-source worker agents with a closed-source advisor.md>) · `multi-agent` · fireworks
  Explains a worker-advisor pattern that combines open-source worker agents with closed-source advisors for cost-quality tradeoffs.
- **2026-06-24** — [Introducing the FFASR Leaderboard: Benchmarking ASR in the Real World](<../evals-observability/benchmark-design/Introducing the FFASR Leaderboard Benchmarking ASR in the Real World.md>) · `benchmark-design` · huggingface
  The FFASR leaderboard benchmarks far-field ASR (clean/noisy/reverberant) using hybrid wave-based room simulation with sim-to-real validation, held-out audio and standardized eval hardware; it plots a WER-vs-RTFx Pareto front and finds far-field WER at low SNR is several times worse than near-field on the same speech.
- **2026-06-24** — [Frontier-lab training infrastructure, now as a service](<../infra-platform/gpu-clusters/Frontier-lab training infrastructure, now as a service.md>) · `gpu-clusters` · fireworks
  Describes training infrastructure as a service for frontier-lab workloads, including scale, orchestration, and reliability needs.
- **2026-06-22** — [Achieve state-of-the-art inference latencies with speculative decoding](<../inference/speculative-decoding/Achieve state-of-the-art inference latencies with speculative decoding.md>) · `speculative-decoding` · modal
  Explains speculative decoding for lower inference latency, including draft-model tradeoffs and production serving considerations.
- **2026-06-19** — [Speculation Is All You Need](<../inference/speculative-decoding/Speculation Is All You Need.md>) · `speculative-decoding` · modal
  Deep dive into speculative decoding and related techniques for improving LLM inference latency and throughput.
- **2026-06-15** — [Teaching Sidekick to say no: automated data curation with LLM judge consensus (2026)](<../evals-observability/llm-as-judge/Teaching Sidekick to say no automated data curation with LLM judge consensus (2026).md>) · `llm-as-judge` · shopify
  Shopify curates Sidekick training data using LLM-judge consensus to automatically filter examples ('teaching Sidekick to say no'), replacing manual labeling with judge-based quality and coverage control.
- **2026-06-03** — [How Harvey & Fireworks Beat Closed Source on Cost + Quality](<../agents/multi-agent/How Harvey & Fireworks Beat Closed Source on Cost + Quality.md>) · `multi-agent` · fireworks
  Case study of using open-source agents with frontier advisors to improve cost and quality versus closed-source baselines.
- **2026-06-02** — [MiniMax-M3 efficient 1M-token multimodal serving](<../inference/serving/MiniMax-M3 efficient 1M-token multimodal serving.md>) · `serving` · together
  Covers efficient MiniMax-M3 serving for million-token context and multimodal workloads.
- **2026-05-29** — [Evaluating Speech-to-Text Quality: Beyond Word Error Rate](<../evals-observability/evaluation/Evaluating Speech-to-Text Quality Beyond Word Error Rate.md>) · `evaluation` · cresta
  Explains why word error rate is insufficient for speech-to-text evaluation and what production teams should measure instead.
- **2026-05-28** — [AI-native product localization](<../product-engineering/architecture/AI-native product localization.md>) · `architecture` · sierra
  Case study of AI-native product localization, covering workflows for translating and adapting product surfaces with model assistance.
- **2026-05-20** — [What we learned testing 7 models under the same agent harness](<../evals-observability/testing/What we learned testing 7 models under the same agent harness.md>) · `testing` · arize
  Compares seven models under a shared agent harness, showing how harness-controlled tests expose model behavior differences.
- **2026-05-19** — [Introducing the Ettin Reranker Family](<../rag-retrieval/search/Introducing the Ettin Reranker Family.md>) · `search` · huggingface
  Releases six CrossEncoder rerankers (17M-1B) built on Ettin ModernBERT encoders with the full training recipe: data selection, loss choice, hard-negative mining, and BEIR/NanoBEIR numbers showing SOTA at each size.
- **2026-05-18** — [Sub-second image generation with Flux.2 and Qwen-Image](<../inference/optimization/Sub-second image generation with Flux.2 and Qwen-Image.md>) · `optimization` · baseten
  Explains sub-second image generation with FLUX.2 and Qwen-Image serving optimizations.
- **2026-05-18** — [Project Glasswing: what Mythos showed us](<../product-engineering/security/Project Glasswing what Mythos showed us.md>) · `security` · cloudflare-ai
  Cloudflare's findings from running Anthropic's Mythos Preview (Project Glasswing) against 50+ of its own repos: the model constructs multi-primitive exploit chains and compiles/runs its own proofs-of-concept, but its organic refusals are inconsistent and false-positive rates spike in C/C++ codebases.
- **2026-05-14** — [The Three Pillars of Voice Integration: Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure](<../infra-platform/deployment/The Three Pillars of Voice Integration Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure.md>) · `deployment` · cresta
  Covers hybrid voice-agent integration patterns for deploying AI into existing telephony and contact-center infrastructure.
- **2026-05-12** — [Engineering low-latency voice agents](<../inference/optimization/Engineering low-latency voice agents.md>) · `optimization` · sierra
  Engineering note on low-latency voice agents, covering response-time constraints and optimization across speech and model serving.
- **2026-05-12** — [Meet Linnaeus and Darwin: Search models that drive higher resolution rates](<../rag-retrieval/search/Meet Linnaeus and Darwin Search models that drive higher resolution rates.md>) · `search` · sierra
  Introduces Sierra search models for improving support-agent resolution rates through better knowledge retrieval and answer grounding.
- **2026-05-12** — [Tau-Bench leaderboard: compare, explore, and understand agent performance](<../evals-observability/benchmark-design/Tau-Bench leaderboard compare, explore, and understand agent performance.md>) · `benchmark-design` · sierra
  Introduces a tau-Bench leaderboard for comparing and analyzing agent performance across benchmark tasks.
- **2026-05-12** — [Tau-Voice: benchmarking real-time voice agents](<../evals-observability/benchmark-design/Tau-Voice benchmarking real-time voice agents.md>) · `benchmark-design` · sierra
  Introduces tau-voice for benchmarking real-time voice agents on realistic tasks, including speech interaction and task-completion quality.
- **2026-05-12** — [Tau3-Bench: Advancing agent evaluation to knowledge and voice](<../evals-observability/benchmark-design/Tau3-Bench Advancing agent evaluation to knowledge and voice.md>) · `benchmark-design` · sierra
  Introduces tau3-Bench for extending agent evaluation to knowledge and voice tasks, expanding beyond text-only transactional benchmarks.
- **2026-05-12** — [How Voice Sims work](<../evals-observability/testing/How Voice Sims work.md>) · `testing` · sierra
  Explains how voice simulations test agents before production by generating realistic spoken interactions and edge cases.
- **2026-05-12** — [Voice Sims: testing real conversations before real customers](<../evals-observability/testing/Voice Sims testing real conversations before real customers.md>) · `testing` · sierra
  Explains voice simulations for testing agents under real-world speech conditions before production customer calls.
- **2026-05-12** — [Meet the Voice Sommelier](<../product-engineering/ux-patterns/Meet the Voice Sommelier.md>) · `ux-patterns` · sierra
  Explains voice-agent experience design, including brand voice selection, vocal cues, conversation design, and metrics for acceptance and satisfaction.
- **2026-05-08** — [DFlash: 3x faster LLM inference](<../inference/speculative-decoding/DFlash 3x faster LLM inference.md>) · `speculative-decoding` · baseten
  Explains DFlash as an optimization for faster LLM inference.
- **2026-05-06** — [Adding Benchmaxxer Repellant to the Open ASR Leaderboard](<../evals-observability/benchmark-design/Adding Benchmaxxer Repellant to the Open ASR Leaderboard.md>) · `benchmark-design` · huggingface
  Adds private held-out Appen/DataoceanAI accent and conversational splits to the Open ASR Leaderboard to blunt benchmaxxing and test-set contamination, keeping the public average WER separate behind a toggle, and discusses the text normalizer needed to standardize model outputs.
- **2026-04-27** — [DeepSeek V4 Pro: Validating Frontier Models for Production](<../evals-observability/evaluation/DeepSeek V4 Pro Validating Frontier Models for Production.md>) · `evaluation` · fireworks
  Shows how to validate a frontier model for production using benchmark and workload-specific evaluation signals.
- **2026-04-24** — [Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding](<../inference/speculative-decoding/Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding.md>) · `speculative-decoding` · together
  Explains distribution-aware speculative decoding for faster RL rollouts.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<../inference/optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-16** — [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](<../rag-retrieval/embeddings/Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Walks through finetuning Qwen3-VL-Embedding-2B for Visual Document Retrieval with Sentence Transformers' new multimodal support, showing a specialized 2B model beating much larger general-purpose embedders on NDCG. Covers multimodal dataset format, loss selection (cached MNRL), hard-negative mining and training a reranker on top.
- **2026-04-09** — [Multimodal Embedding & Reranker Models with Sentence Transformers](<../rag-retrieval/embeddings/Multimodal Embedding & Reranker Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Sentence Transformers v5+ adds multimodal embedding and reranker models (shared text/image embedding space, mixed-modality cross-encoder scoring) for visual document retrieval, cross-modal search and multimodal RAG; covers the API and model choices.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<../inference/optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<../inference/quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-03-25** — [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](<../product-engineering/case-studies/How Perplexity Brought Voice Search to Millions Using the Realtime API OpenAI Developers.md>) · `case-studies` · openai-devs
  Perplexity's production lessons running Realtime-1.5 voice across Comet and Computer: feed context in 2,000-token chunks to avoid all-or-nothing truncation, get system/user/assistant role semantics right, standardize audio via a Rust SDK (48 kHz mono, WebRTC APM), and a 'voice lock' pattern for user pauses.
- **2026-03-20** — [Designing delightful frontends with GPT-5.4 | OpenAI Developers](<../prompt-engineering/techniques/Designing delightful frontends with GPT-5.4 OpenAI Developers.md>) · `techniques` · openai-devs
  Prompting guide for steering GPT-5.4 toward non-generic frontend design: the model was trained for UI work, native image search/generation (e.g. prompt it to build mood boards first), and computer use for self-verification with tools like Playwright.
- **2026-03-19** — [Building a Magic Mirror: AI retail experiences with Remix (2026)](<../product-engineering/case-studies/Building a Magic Mirror AI retail experiences with Remix (2026).md>) · `case-studies` · shopify
  Shopify builds an in-store 'Magic Mirror' AI retail experience with Remix, using multimodal AI to turn physical shopping into an interactive experience for hype-driven brands.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<../inference/kernels/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `kernels` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-06** — [Eval awareness in Claude Opus 4.6’s BrowseComp performance](<../evals-observability/benchmark-design/Eval awareness in Claude Opus 4.6’s BrowseComp performance.md>) · `benchmark-design` · anthropic-engineering
  Investigates how Claude Opus 4.6 recognizing it was being evaluated affected BrowseComp scores, and what eval-awareness implies for benchmark validity.
- **2026-02-24** — [Optimizing Training Workloads for GPU Clusters](<../infra-platform/gpu-clusters/Optimizing Training Workloads for GPU Clusters.md>) · `gpu-clusters` · together
  Covers optimization patterns for training workloads on GPU clusters.
- **2026-02-23** — [Run long horizon tasks with Codex | OpenAI Developers](<../agents/planning/Run long horizon tasks with Codex OpenAI Developers.md>) · `planning` · openai-devs
  Stress test of long-horizon agentic coding: GPT-5.3-Codex at Extra High reasoning ran ~25 hours uninterrupted, consuming ~13M tokens and generating ~30k lines to build a design tool from a blank repo, framed by METR's ~7-month doubling time for agent task horizons.
- **2026-02-19** — [Consistency diffusion language models: Up to 14x faster inference without sacrificing quality](<../inference/optimization/Consistency diffusion language models Up to 14x faster inference without sacrificing quality.md>) · `optimization` · together
  Explains consistency diffusion language models for faster inference without large quality loss.
- **2026-02-12** — [The 5 pillars of AI model performance](<../evals-observability/benchmark-design/The 5 pillars of AI model performance.md>) · `benchmark-design` · braintrust
  Defines five pillars of AI model performance and how to measure quality beyond a single aggregate benchmark score.
- **2026-02-11** — [How we built the fastest Kimi K2.5 on Artificial Analysis](<../inference/optimization/How we built the fastest Kimi K2.5 on Artificial Analysis.md>) · `optimization` · baseten
  Explains optimizations behind fast Kimi K2.5 serving on Artificial Analysis.
- **2026-02-06** — [What do LLMs think when you don't tell them what to think about?](<../evals-observability/evaluation/What do LLMs think when you don't tell them what to think about.md>) · `evaluation` · together
  Investigates what LLMs do under underspecified prompting and how that affects evaluation.
- **2026-02-03** — [The Benchmark Gap: What It Takes to Ship Kimi K2.5](<../evals-observability/evaluation/The Benchmark Gap What It Takes to Ship Kimi K2.5.md>) · `evaluation` · fireworks
  Explains the benchmark and quality gaps involved in shipping Kimi K2.5 for production workloads.
- **2026-01-26** — [SkyPilot at Shopify: Multi-cloud GPUs without the pain (2026)](<../infra-platform/gpu-clusters/SkyPilot at Shopify Multi-cloud GPUs without the pain (2026).md>) · `gpu-clusters` · shopify
  How Shopify uses SkyPilot to run ML training across fragmented multi-cloud GPU capacity (H200s, L4s) behind one interface, avoiding per-provider API and configuration lock-in for scarce accelerators.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<../inference/speculative-decoding/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `speculative-decoding` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2026-01-12** — [Inside multi-node training: How to scale model training across GPU clusters](<../infra-platform/gpu-clusters/Inside multi-node training How to scale model training across GPU clusters.md>) · `gpu-clusters` · together
  Explains multi-node model training across GPU clusters and the coordination issues that appear at scale.
- **2026-01-08** — [How to choose the right open model for production](<../product-engineering/architecture/How to choose the right open model for production.md>) · `architecture` · together
  Guide to choosing open models for production based on workload, quality, and serving constraints.
- **2025-12-30** — [OpenAI for Developers in 2025](<../industry/trends/OpenAI for Developers in 2025.md>) · `trends` · openai-devs
  Year-in-review of OpenAI's 2025 developer platform: reasoning converging from separate o1/o3/o4-mini lines into unified flagship models, multimodal I/O becoming default, agent building blocks (Responses API, Agents SDK, AgentKit), and GPT-5.2-Codex for long-horizon coding.
- **2025-12-05** — [Tangle: An open-source ML experimentation platform built for scale (2025)](<../evals-observability/tracing/Tangle An open-source ML experimentation platform built for scale (2025).md>) · `tracing` · shopify
  Tangle: Shopify's open-source ML experimentation platform for reproducibility at scale, tracking notebook versions, data snapshots, and parameters so experiments can be reproduced without re-running from scratch.
- **2025-11-12** — [Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell](<../inference/optimization/Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell.md>) · `optimization` · baseten
  Explains Kimi K2 Thinking serving at high throughput on NVIDIA Blackwell hardware.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<../inference/optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-11-04** — [How to evaluate and benchmark Large Language Models (LLMs)](<../evals-observability/benchmark-design/How to evaluate and benchmark Large Language Models (LLMs).md>) · `benchmark-design` · together
  Guide to evaluating and benchmarking LLMs for production model selection.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models, speculative decoding, and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-22** — [Large Reasoning Models Fail to Follow Instructions During Reasoning: A Benchmark Study](<../evals-observability/benchmark-design/Large Reasoning Models Fail to Follow Instructions During Reasoning A Benchmark Study.md>) · `benchmark-design` · together
  Benchmark study showing instruction-following failures during reasoning.
- **2025-10-21** — [Engineering for Real-Time Voice Agent Latency](<../inference/serving/Engineering for Real-Time Voice Agent Latency.md>) · `serving` · cresta
  Technical discussion of latency in real-time voice agents and the engineering constraints behind responsive spoken interaction.
- **2025-10-13** — [State of LLMs on the Application Layer](<../industry/trends/State of LLMs on the Application Layer.md>) · `trends` · langfuse
  Application-layer snapshot of LLM usage and model trends, useful for understanding production model adoption and quality/cost tradeoffs.
- **2025-10-10** — [ATLAS runtime-learning accelerators for LLM inference](<../inference/speculative-decoding/ATLAS runtime-learning accelerators for LLM inference.md>) · `speculative-decoding` · together
  Introduces ATLAS, a runtime-learning accelerator for improving LLM inference.
- **2025-10-09** — [How AI Agents are Evolving Shopify's Product Taxonomy at Scale (2025)](<../agents/multi-agent/How AI Agents are Evolving Shopify's Product Taxonomy at Scale (2025).md>) · `multi-agent` · shopify
  Shopify uses AI agents to evolve its product taxonomy (10,000+ categories, 2,000+ attributes) that powers tens of millions of daily product classifications, keeping the taxonomy adapting without breaking the classifier.
- **2025-09-22** — [Why we built the Responses API | OpenAI Developers](<../agents/tool-use/Why we built the Responses API OpenAI Developers.md>) · `tool-use` · openai-devs
  OpenAI's design rationale for the Responses API as an agentic loop unifying Chat Completions and Assistants: it preserves reasoning state across turns (+5% on TAUBench, better cache utilization) and emits multiple output items — tool calls, structured outputs, intermediate steps — not just the final message.
- **2025-09-10** — [Jupyter Agents: training LLMs to reason with notebooks](<../agents/tool-use/Jupyter Agents training LLMs to reason with notebooks.md>) · `tool-use` · huggingface
  Builds a data-science agent that executes code inside a Jupyter notebook, then trains small models to do it: generates a synthetic notebook trajectory dataset from Kaggle notebooks, fine-tunes Qwen3-4B/32B on it, and measures the gain on the DABStep benchmark. Details the scaffolding (executor, context management) and the data-quality filtering that drove most of the improvement.
- **2025-09-04** — [Welcome EmbeddingGemma, Google's new efficient embedding model](<../rag-retrieval/embeddings/Welcome EmbeddingGemma, Google's new efficient embedding model.md>) · `embeddings` · huggingface
  EmbeddingGemma is a 308M-param multilingual embedding model: a Gemma3 backbone converted to bidirectional attention plus mean pooling and two dense layers, trained on ~320B tokens with Matryoshka Representation Learning so its 768-dim output can be truncated to 512/256/128; runs under 200 MB RAM quantized, tops MTEB under 500M, and the post shows a domain fine-tune on MIRIAD that beats models twice its size.
- **2025-08-26** — [Building production-ready agentic systems: Lessons from Shopify Sidekick (2025)](<../agents/harness/Building production-ready agentic systems Lessons from Shopify Sidekick (2025).md>) · `harness` · shopify
  ICML 2025 talk on building Shopify Sidekick as a production agentic system: architecture, LLM-based evaluation, and GRPO reinforcement-learning training for a merchant-facing AI assistant.
- **2025-08-21** — [Voice AI Agents for Customer Experience: Why Decentralized Agent Architectures Can Outperform Central Orchestrators](<../agents/multi-agent/Voice AI Agents for Customer Experience Why Decentralized Agent Architectures Can Outperform Central Orchestrators.md>) · `multi-agent` · cresta
  Argues for decentralized voice-agent architectures over central orchestration in some customer-experience workloads.
- **2025-08-15** — [Your AI Benchmark is Lying to You. Here's How We Caught It](<../evals-observability/benchmark-design/Your AI Benchmark is Lying to You. Here's How We Caught It.md>) · `benchmark-design` · fireworks
  Explains how benchmark methodology can mislead model selection and how to evaluate models against real workload constraints.
- **2025-07-30** — [A Watermark for Large Language Models](<../product-engineering/security/A Watermark for Large Language Models.md>) · `security` · arize
  Summary of a paper-reading session on watermarking generated text from large language models, including detection goals and implications for responsible deployment.
- **2025-07-23** — [Fast LoRA inference for Flux with Diffusers and PEFT](<../inference/optimization/Fast LoRA inference for Flux with Diffusers and PEFT.md>) · `optimization` · huggingface
  Gets ~2.3x faster LoRA inference for Flux.1-Dev by combining LoRA hotswapping with torch.compile without recompilation — using peft's hotswap_adapter, max-rank padding so shapes stay static, and flags to avoid recompiles when adapters have different ranks and target layers. Also covers fusing/unfusing and FP8 quantization on top.
- **2025-07-10** — [Using Model-as-a-Judge for Reward in Reinforcement Finetuning](<../evals-observability/llm-as-judge/Using Model-as-a-Judge for Reward in Reinforcement Finetuning.md>) · `llm-as-judge` · fireworks
  Explains using model-as-judge rewards for reinforcement fine-tuning and the evaluation risks involved.
- **2025-07-02** — [DeepSWE coding agent trained with scaled RL](<../agents/tool-use/DeepSWE coding agent trained with scaled RL.md>) · `tool-use` · together
  Explains DeepSWE, an open-source coding agent trained by scaling reinforcement learning.
- **2025-07-02** — [How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work](<../evals-observability/evaluation/How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work.md>) · `evaluation` · modal
  Case study using evals and inference-time compute scaling to generate QR codes that satisfy visual and functional constraints.
- **2025-07-01** — [Training and Finetuning Sparse Embedding Models with Sentence Transformers](<../rag-retrieval/embeddings/Training and Finetuning Sparse Embedding Models with Sentence Transformers.md>) · `embeddings` · huggingface
  End-to-end guide to training SPLADE-style sparse embedding models with Sentence Transformers: the model/loss/evaluator/trainer components, FLOPS regularization to control sparsity, distillation from a cross-encoder, and NanoBEIR results plus the retrieval-cost tradeoff versus dense vectors.
- **2025-06-18** — [Run FLUX.1-dev three times faster](<../inference/optimization/Run FLUX.1-dev three times faster.md>) · `optimization` · modal
  Explains optimizations for running FLUX.1-dev faster, including inference configuration and image-model serving tradeoffs.
- **2025-06-05** — [Model-Preserving Adaptive Rounding with YAQA](<../inference/quantization/Model-Preserving Adaptive Rounding with YAQA.md>) · `quantization` · together
  Explains YAQA, a model-preserving adaptive rounding approach for quantization.
- **2025-05-12** — [Boosting DeepSeek-R1 speed with customized speculative decoding](<../inference/speculative-decoding/Boosting DeepSeek-R1 speed with customized speculative decoding.md>) · `speculative-decoding` · together
  Shows customized speculative decoding for accelerating DeepSeek-R1 serving.
- **2025-04-21** — [Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas](<../inference/kernels/Chipmunk Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas.md>) · `kernels` · together
  Describes Chipmunk, a training-free acceleration method for diffusion transformers.
- **2025-04-16** — [Introducing HELMET: Holistically Evaluating Long-context Language Models](<../evals-observability/benchmark-design/Introducing HELMET Holistically Evaluating Long-context Language Models.md>) · `benchmark-design` · huggingface
  HELMET is a long-context benchmark spanning 7 application-centric categories (RAG, passage re-ranking, many-shot ICL, long-doc QA, summarization, cite/attribution) up to 128K tokens, built because synthetic probes like needle-in-a-haystack correlate poorly with real downstream long-context ability. Reports rankings that shift by category and shows open models lag closed ones most on tasks requiring full-context reasoning.
- **2025-04-08** — [DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level](<../agents/tool-use/DeepCoder A Fully Open-Source 14B Coder at O3-mini Level.md>) · `tool-use` · together
  Describes DeepCoder, an open-source coding model trained for O3-mini-level coding performance.
- **2025-03-26** — [Training and Finetuning Reranker Models with Sentence Transformers](<../rag-retrieval/search/Training and Finetuning Reranker Models with Sentence Transformers.md>) · `search` · huggingface
  Full guide to training cross-encoder reranker models with Sentence Transformers v4: dataset formats, losses (BinaryCrossEntropy, CachedMultipleNegativesRanking, ListNet), hard-negative mining, and evaluation, with a fine-tune that beats much larger general rerankers on the target domain.
- **2025-03-13** — [Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence](<../inference/serving/Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence.md>) · `serving` · cresta
  Explains ML services, inference graphs, and real-time intelligence components in a production voice platform.
- **2025-03-13** — [Hugging Face and Langfuse: 5 Ways to use them Together](<../infra-platform/deployment/Hugging Face and Langfuse 5 Ways to use them Together.md>) · `deployment` · langfuse
  Shows ways to combine Hugging Face workflows with Langfuse for model experimentation, tracing, evaluation, and deployment feedback loops.
- **2025-02-26** — [Evaluating Large Language Models With OpenEvals](<../evals-observability/llm-as-judge/Evaluating Large Language Models With OpenEvals.md>) · `llm-as-judge` · langchain
  Guide to evaluating large language models with OpenEvals, including reusable evaluators and model comparison workflows.
- **2025-02-25** — [Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains](<../infra-platform/deployment/Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains.md>) · `deployment` · cresta
  Architecture note on routing incoming voice traffic with customer-specific subdomains in a production voice platform.
- **2025-02-13** — [Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection](<../inference/hardware/Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection.md>) · `hardware` · together
  Describes Blackwell BF16 training acceleration with the Together Kernel Collection.
- **2025-02-10** — [The Open Arabic LLM Leaderboard 2](<../evals-observability/benchmark-design/The Open Arabic LLM Leaderboard 2.md>) · `benchmark-design` · huggingface
  The Open Arabic LLM Leaderboard 2 rebuilds Arabic LLM evaluation around native (not machine-translated) datasets and centralized, reproducible evaluation to fix the integrity problem of self-reported scores. Describes the new benchmark mix (including the Balsam Index and native Arabic tasks) and the leaderboard's verification pipeline.
- **2025-02-01** — [From text to task: Constrained generation for structured extraction in R1](<../prompt-engineering/structured-output/From text to task Constrained generation for structured extraction in R1.md>) · `structured-output` · fireworks
  Explains constrained generation for structured extraction with reasoning models and schema-bound outputs.
- **2025-01-10** — [Visual Document Retrieval Goes Multilingual](<../rag-retrieval/embeddings/Visual Document Retrieval Goes Multilingual.md>) · `embeddings` · huggingface
  vdr-2b-multi-v1 is a ColPali-style visual document retrieval embedding model trained on a new 500k multilingual query/page synthetic dataset across 5 languages, beating the English-only baseline on multilingual and cross-lingual document retrieval benchmarks.
- **2024-12-20** — [Evaluating Audio Reasoning with Big Bench Audio](<../evals-observability/benchmark-design/Evaluating Audio Reasoning with Big Bench Audio.md>) · `benchmark-design` · huggingface
  Introduces Big Bench Audio, 1,000 audio questions adapted from Big Bench Hard, and measures a 'speech reasoning gap': GPT-4o scores 92% text-to-text but only 66% speech-to-speech, with Gemini 1.5 compared across S2S/S2T/T2S/T2T pipelines.
- **2024-12-19** — [A quick introduction to speculative decoding](<../inference/speculative-decoding/A quick introduction to speculative decoding.md>) · `speculative-decoding` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-10** — [Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies](<../agents/multi-agent/Merge, Ensemble, and Cooperate! A Survey on Collaborative LLM Strategies.md>) · `multi-agent` · arize
  Summarizes collaborative LLM strategies such as merging, ensembling, and cooperation for multi-model or multi-agent systems.
- **2024-12-04** — [Rethinking LLM Evaluation with 3C3H: AraGen Benchmark and Leaderboard](<../evals-observability/benchmark-design/Rethinking LLM Evaluation with 3C3H AraGen Benchmark and Leaderboard.md>) · `benchmark-design` · huggingface
  AraGen's 3C3H measure scores an LLM response on Correctness, Completeness, Conciseness, Helpfulness, Honesty and Harmlessness via LLM-as-judge, combining them into one metric; the leaderboard also rotates a private Arabic eval set to resist contamination.
- **2024-12-04** — [What to do when a new AI model comes out](<../evals-observability/evaluation/What to do when a new AI model comes out.md>) · `evaluation` · braintrust
  Playbook for responding when a new AI model ships: run targeted evals, compare cost and quality, inspect regressions, and decide rollout strategy.
- **2024-12-03** — [Investing in Performance: Fine-tune small models with LLM insights - a CFM case study](<../product-engineering/case-studies/Investing in Performance Fine-tune small models with LLM insights - a CFM case study.md>) · `case-studies` · huggingface
  CFM (quant hedge fund) case study: use an LLM to label financial NER data, distill that into a compact fine-tuned model, and deploy it on Inference Endpoints — with an F1 and $/hour table showing the fine-tuned small model beating zero-shot LLM accuracy at a fraction of the inference cost.
- **2024-11-20** — [Faster Text Generation with Self-Speculative Decoding](<../inference/speculative-decoding/Faster Text Generation with Self-Speculative Decoding.md>) · `speculative-decoding` · huggingface
  LayerSkip self-speculative decoding: the same model drafts with early-exit at an intermediate layer and verifies with the remaining layers, reusing the KV cache so no separate draft model or extra memory is needed; includes speedups on Llama checkpoints trained with layer dropout + early-exit loss.
- **2024-11-20** — [Introducing the Open Leaderboard for Japanese LLMs!](<../evals-observability/benchmark-design/Introducing the Open Leaderboard for Japanese LLMs!.md>) · `benchmark-design` · huggingface
  The Open Japanese LLM Leaderboard evaluates models on 16+ llm-jp-eval tasks (NLI, translation, summarization, QA, code generation), motivated by Japanese-specific challenges like the three-script writing system and the absence of word boundaries for tokenization.
- **2024-11-19** — [Judge Arena: Benchmarking LLMs as Evaluators](<../evals-observability/llm-as-judge/Judge Arena Benchmarking LLMs as Evaluators.md>) · `llm-as-judge` · huggingface
  Launches Judge Arena, a crowdsourced side-by-side arena where humans vote between two LLM judges' scores and critiques, producing an ELO leaderboard of 18 open and proprietary LLM-as-a-judge models. Describes the judge-selection criteria and the prompt/scoring setup used for each battle.
- **2024-10-09** — [Scaling AI-based Data Processing with Hugging Face + Dask](<../infra-platform/gpu-clusters/Scaling AI-based Data Processing with Hugging Face + Dask.md>) · `gpu-clusters` · huggingface
  Uses Dask with hf.co/datasets and the fineweb-edu-classifier to run distributed, out-of-core AI data processing (Parquet chunking, GPU classifier inference) across a cloud cluster, showing how to scale a filtering/labeling pipeline past single-machine memory.
- **2024-10-08** — [Multimodal Document RAG with Llama 3.2 Vision and ColQwen2](<../rag-retrieval/pipelines/Multimodal Document RAG with Llama 3.2 Vision and ColQwen2.md>) · `pipelines` · together
  Builds a multimodal document RAG pipeline with Llama 3.2 Vision and ColQwen2.
- **2024-09-30** — [Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations](<../evals-observability/llm-as-judge/Best Practices for Selecting the Right Model for LLM-as-a-Judge Evaluations.md>) · `llm-as-judge` · arize
  Best practices for choosing an LLM-as-judge evaluation model, including tradeoffs in evaluator quality and fit for task.
- **2024-09-18** — [Fine-tuning LLMs to 1.58bit: extreme quantization made easy](<../inference/quantization/Fine-tuning LLMs to 1.58bit extreme quantization made easy.md>) · `quantization` · huggingface
  Shows how to fine-tune an existing Llama3-8B/SmolLM into BitNet's 1.58-bit ternary ({-1,0,1}) weight format instead of pre-training from scratch, using BitLinear layers, a lambda-scheduled quantization warmup and per-row/per-tensor scaling. Reports pre-training and fine-tuning results plus custom kernel benchmarks.
- **2024-09-16** — [Boost your throughput with dynamic batching](<../inference/optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-08-30** — [Evaluating an Image Classifier](<../evals-observability/evaluation/Evaluating an Image Classifier.md>) · `evaluation` · arize
  Tutorial on evaluating an image classifier with Phoenix, using multimodal experiment and tracing workflows.
- **2024-08-28** — [TEAL: Training-Free Activation Sparsity in Large Language Models](<../inference/optimization/TEAL Training-Free Activation Sparsity in Large Language Models.md>) · `optimization` · together
  Explains TEAL, a training-free activation sparsity method for large language models.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<../inference/speculative-decoding/How to double tokens per second for Llama 3 with Medusa.md>) · `speculative-decoding` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-13** — [A practitioner's guide to testing and running large GPU clusters for training generative AI models](<../infra-platform/gpu-clusters/A practitioner's guide to testing and running large GPU clusters for training generative AI models.md>) · `gpu-clusters` · together
  Practical guide to testing and operating large GPU clusters for generative model training.
- **2024-08-05** — [Beat GPT-4o at Python by searching with 100 dumb LLaMAs](<../evals-observability/evaluation/Beat GPT-4o at Python by searching with 100 dumb LLaMAs.md>) · `evaluation` · modal
  Explores using many small Llama runs and search to improve Python benchmark performance against GPT-4o baselines.
- **2024-07-31** — [Llama 3.1: Same model, different results. The impact of a percentage point.](<../evals-observability/benchmark-design/Llama 3.1 Same model, different results. The impact of a percentage point.md>) · `benchmark-design` · together
  Explains how small quality differences and deployment choices affect Llama 3.1 results.
- **2024-07-25** — [LAVE: Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning?](<../evals-observability/benchmark-design/LAVE Zero-shot VQA Evaluation on Docmatix with LLMs - Do We Still Need Fine-Tuning.md>) · `benchmark-design` · huggingface
  Shows that exact-match VQA metrics (VQA Accuracy, ANLS, CIDEr, BLEU) unfairly punish correct out-of-distribution answers, and applies LAVE — an LLM-as-judge metric where Llama-2-7B-chat rates answers 1-3 with a rationale from in-context demonstrations — to evaluate MPLUGDocOwl1.5 zero-shot on Docmatix, where its ANLS collapses despite 84% on DocVQA.
- **2024-07-23** — [How to serve 10,000 fine-tuned LLMs from a single GPU](<../inference/serving/How to serve 10,000 fine-tuned LLMs from a single GPU.md>) · `serving` · baseten
  Explains serving many fine-tuned LLM adapters from a single GPU with efficient multiplexing.
- **2024-07-18** — [TGI Multi-LoRA: Deploy Once, Serve 30 Models](<../inference/serving/TGI Multi-LoRA Deploy Once, Serve 30 Models.md>) · `serving` · huggingface
  Explains TGI's multi-LoRA serving: load one base model plus up to ~30 LoRA adapters in a single deployment, batching requests for different adapters together via a gathered/segmented matmul so per-adapter overhead is small. Argues the cost and ops case for many specialized adapters over many full deployments, with latency numbers vs single-adapter serving.
- **2024-07-16** — [How we leveraged distilabel to create an Argilla 2.0 Chatbot](<../rag-retrieval/pipelines/How we leveraged distilabel to create an Argilla 2.0 Chatbot.md>) · `pipelines` · huggingface
  End-to-end build of a docs chatbot: distilabel generates synthetic query/answer pairs from Argilla 2.0 documentation, which fine-tunes a bge-base Matryoshka embedding model used in a retrieval + Gradio chat pipeline.
- **2024-06-28** — [RAFT: Adapting Language Model to Domain Specific RAG](<../rag-retrieval/pipelines/RAFT Adapting Language Model to Domain Specific RAG.md>) · `pipelines` · arize
  Summarizes RAFT as a method for adapting language models to domain-specific RAG workflows.
- **2024-06-24** — [Building a personalized code assistant with open-source LLMs using RAG Fine-tuning](<../rag-retrieval/pipelines/Building a personalized code assistant with open-source LLMs using RAG Fine-tuning.md>) · `pipelines` · together
  Builds a personalized code assistant using RAG fine-tuning with open-source LLMs.
- **2024-06-18** — [SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices](<../inference/speculative-decoding/SpecExec Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices.md>) · `speculative-decoding` · together
  Introduces SpecExec for massively parallel speculative decoding on consumer devices.
- **2024-06-18** — [BigCodeBench: The Next Generation of HumanEval](<../evals-observability/benchmark-design/BigCodeBench The Next Generation of HumanEval.md>) · `benchmark-design` · huggingface
  BigCodeBench replaces HumanEval with 1,140 function-level tasks that force LLMs to compose calls across 139 libraries, with rich test harnesses (average 5.6 test cases, 99% branch coverage) and both Complete and Instruct splits. Reports that instruction-tuned models drop sharply on the Instruct split and that even top models are ~20 points behind human performance.
- **2024-06-11** — [Together MoA collective intelligence of open-source models](<../agents/multi-agent/Together MoA collective intelligence of open-source models.md>) · `multi-agent` · together
  Explains Mixture-of-Agents for improving model outputs through collective open-source model reasoning.
- **2024-05-29** — [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](<../evals-observability/benchmark-design/Trustworthy LLMs A Survey and Guideline for Evaluating Large Language Models' Alignment.md>) · `benchmark-design` · arize
  Survey-style guide to evaluating trustworthy and aligned LLM behavior across reliability, safety, and quality dimensions.
- **2024-05-28** — [Training and Finetuning Embedding Models with Sentence Transformers](<../rag-retrieval/embeddings/Training and Finetuning Embedding Models with Sentence Transformers.md>) · `embeddings` · huggingface
  Complete guide to finetuning embedding models with Sentence Transformers v3: choosing a loss for your dataset shape (MultipleNegativesRankingLoss for (anchor, positive) pairs, CoSENT, etc.), the SentenceTransformerTrainer API, training args (batch size matters a lot for in-batch negatives), and evaluators for measuring retrieval gains.
- **2024-05-15** — [Pairwise Evaluations with LangSmith](<../evals-observability/llm-as-judge/Pairwise Evaluations with LangSmith.md>) · `llm-as-judge` · langchain
  Explains pairwise evaluations with LangSmith for comparing model or prompt outputs using preference-style scoring.
- **2024-05-08** — [Code Generation with Large Language Models - Fireworks AI Take](<../agents/tool-use/Code Generation with Large Language Models - Fireworks AI Take.md>) · `tool-use` · fireworks
  Discusses code-generation copilots with LLMs, including model behavior, latency, and developer workflow considerations.
- **2024-04-26** — [Keys To Understanding ReAct: Synergizing Reasoning and Acting in Language Models](<../agents/tool-use/Keys To Understanding ReAct Synergizing Reasoning and Acting in Language Models.md>) · `tool-use` · arize
  Explains ReAct as a reasoning-plus-acting pattern for agents and how it structures tool use.
- **2024-04-16** — [Introducing the LiveCodeBench Leaderboard - Holistic and Contamination-Free Evaluation of Code LLMs](<../evals-observability/benchmark-design/Introducing the LiveCodeBench Leaderboard - Holistic and Contamination-Free Evaluation of Code LLMs.md>) · `benchmark-design` · huggingface
  LiveCodeBench continuously scrapes date-stamped problems from LeetCode, AtCoder and Codeforces so models can be evaluated only on problems released after their training cutoff, making contamination detectable. Evaluates four scenarios — code generation, self-repair from error feedback, code execution (output prediction) and test-output prediction.
- **2024-04-03** — [Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon](<../inference/quantization/Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon.md>) · `quantization` · huggingface
  Accelerates SetFit few-shot text classification inference by 7.8x on Intel Xeon (Sapphire Rapids) using Optimum Intel + OpenVINO post-training quantization to int8, with an accuracy-drop constraint; includes the few-shot accuracy context where SetFit beats 3-shot GPT-3.5/GPT-4 on Banking77.
- **2024-03-05** — [Introducing ConTextual: How well can your Multimodal model jointly reason over text and image in text-rich scenes?](<../evals-observability/benchmark-design/Introducing ConTextual How well can your Multimodal model jointly reason over text and image in text-rich scenes.md>) · `benchmark-design` · huggingface
  ConTextual is a benchmark and leaderboard for context-sensitive text-rich visual reasoning (reading text in images to answer instructions); uses GPT-4 as judge plus human evaluation, showing a large gap between GPT-4V and open LMMs.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<../evals-observability/benchmark-design/Predictive Human Preference From Model Ranking to Model Routing.md>) · `benchmark-design` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2024-02-22** — [40% faster Stable Diffusion XL inference with NVIDIA TensorRT](<../inference/optimization/40% faster Stable Diffusion XL inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains TensorRT optimization for Stable Diffusion XL inference, including latency and throughput gains.
- **2024-02-08** — [RAG vs Fine-Tuning](<../rag-retrieval/pipelines/RAG vs Fine-Tuning.md>) · `pipelines` · arize
  Compares RAG and fine-tuning as adaptation strategies, including when retrieval is preferable to model updates.
- **2024-02-02** — [NPHardEval Leaderboard: Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates](<../evals-observability/benchmark-design/NPHardEval Leaderboard Unveiling the Reasoning Abilities of Large Language Models through Complexity Classes and Dynamic Updates.md>) · `benchmark-design` · huggingface
  NPHardEval grounds LLM reasoning evaluation in computational complexity classes: 900 auto-generated algorithmic questions (3 P, 3 NP-complete, 3 NP-hard tasks x 10 difficulty levels), refreshed monthly to defeat overfitting, scored by weighted accuracy and failure rate.
- **2024-01-31** — [Introduction to quantizing ML models](<../inference/quantization/Introduction to quantizing ML models.md>) · `quantization` · baseten
  Introduces model quantization concepts and how they affect inference efficiency and model quality.
- **2024-01-31** — [How to benchmark image generation models like Stable Diffusion XL](<../evals-observability/benchmark-design/How to benchmark image generation models like Stable Diffusion XL.md>) · `benchmark-design` · baseten
  Explains how to benchmark image-generation models with attention to quality, latency, and reproducibility.
- **2023-11-13** — [FlashFFTConv: Efficient Convolutions for Long Sequences with Tensor Cores](<../inference/kernels/FlashFFTConv Efficient Convolutions for Long Sequences with Tensor Cores.md>) · `kernels` · together
  Explains FlashFFTConv for efficient long-sequence convolutions on tensor cores.
- **2023-10-17** — [RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models](<../rag-retrieval/search/RankVicuna Zero-Shot Listwise Document Reranking with Open-Source Large Language Models.md>) · `search` · arize
  Summarizes RankVicuna for zero-shot listwise reranking and its implications for LLM-powered search.
- **2023-09-11** — [Medusa: Simple framework for accelerating LLM generation with multiple decoding heads](<../inference/speculative-decoding/Medusa Simple framework for accelerating LLM generation with multiple decoding heads.md>) · `speculative-decoding` · together
  Introduces Medusa, a multi-decoding-head framework for accelerating LLM generation.
- **2023-08-30** — [SDXL inference in under 2 seconds](<../inference/optimization/SDXL inference in under 2 seconds.md>) · `optimization` · baseten
  Guide to Stable Diffusion XL inference optimization for sub-2-second image generation.
- **2023-03-21** — [Toolformer: Training LLMs To Use Tools](<../agents/tool-use/Toolformer Training LLMs To Use Tools.md>) · `tool-use` · arize
  Summarizes Toolformer and how language models can learn to use external tools.
- **2022-12-08** — [Accelerating model deployment: 100X faster dev loops with development deployments](<../infra-platform/deployment/Accelerating model deployment 100X faster dev loops with development deployments.md>) · `deployment` · baseten
  Explains development deployments and draft models as a way to shorten model deployment iteration loops.
- **2022-12-05** — [Overcoming communication bottlenecks for decentralized training, part 2](<../infra-platform/gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 2.md>) · `gpu-clusters` · together
  Continues the decentralized training discussion with techniques for communication-efficient optimization.
- **2022-11-30** — [Overcoming communication bottlenecks for decentralized training, part 1](<../infra-platform/gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 1.md>) · `gpu-clusters` · together
  Explains communication bottlenecks in decentralized foundation-model training.
- **2020-05-22** — **[Paper]** [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](<../rag-retrieval/pipelines/[Paper] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.md>) · `pipelines` · arxiv
  Introduces Retrieval-Augmented Generation: a seq2seq model coupled to a dense-vector Wikipedia index via DPR, with the retriever and generator fine-tuned end-to-end. Sets SOTA on three open-domain QA tasks and yields more factual, specific generations than a parametric-only BART baseline.
