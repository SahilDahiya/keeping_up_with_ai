# together

80 articles.

- **2026-07-16** — [What does 99.9% uptime mean for inference?](<../inference/serving/What does 99.9% uptime mean for inference.md>) · `serving` · together
  Together breaks down what each reliability 'nine' actually requires for GPU inference serving, mapping failure domains (compute ECC errors, NIC/NVLink faults, storage, network, software/routing bugs) to the multi-region and AZ-redundancy architecture needed to survive them.
- **2026-07-15** — [Together AI brings Thinking Machines Lab’s new model Inkling on day 0](<../models/architectures/Together AI brings Thinking Machines Lab’s new model Inkling on day 0.md>) · `architectures` · together
  Details Inkling's architecture (975B/40B active MoE with a shared expert sink jointly normalized against routed experts, a learned query-conditioned relative attention bias instead of RoPE, and 'sconv' short causal convolutions on K/V and sublayer outputs) and Together's FlashAttention-4-based kernel adapted to serve its query-conditioned relative attention efficiently.
- **2026-07-15** — [New in Together GPU Clusters: Reliability and control for production GPU clusters](<../infra-platform/gpu-clusters/New in Together GPU Clusters Reliability and control for production GPU clusters.md>) · `gpu-clusters` · together
  Details operational upgrades to Together GPU Clusters: passive health checks that catch GPUs falling off the PCIe bus, Xid errors, and thermal throttling on live workloads; four automated-but-approved repair actions (reboot/reprovision/failover/remove); and a rebuilt Slurm-on-Kubernetes stack (Slinky fork) targeting crashing daemons and scheduler drift at scale.
- **2026-06-23** — [ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet)](<../evals-observability/benchmark-design/ParallelKernelBench Frontier LLMs can't write fast multi-GPU kernels (yet).md>) · `benchmark-design` · together
  Introduces ParallelKernelBench for measuring whether frontier LLMs can write fast multi-GPU kernels.
- **2026-06-22** — [Best practices to accelerate inference for large-scale production workloads](<../inference/optimization/Best practices to accelerate inference for large-scale production workloads.md>) · `optimization` · together
  Best practices for accelerating inference in large-scale production workloads.
- **2026-06-02** — [MiniMax-M3 efficient 1M-token multimodal serving](<../inference/serving/MiniMax-M3 efficient 1M-token multimodal serving.md>) · `serving` · together
  Covers efficient MiniMax-M3 serving for million-token context and multimodal workloads.
- **2026-05-29** — [How Together AI built a fast speech-to-text stack](<../models/multimodal/How Together AI built a fast speech-to-text stack.md>) · `multimodal` · together
  Engineering writeup on building a fast speech-to-text stack.
- **2026-05-19** — [Benchmarking inference at scale: coding agents](<../evals-observability/benchmark-design/Benchmarking inference at scale coding agents.md>) · `benchmark-design` · together
  Benchmarks inference at scale for coding-agent workloads.
- **2026-05-11** — [Serving DeepSeek-V4: why million-token context is an inference systems problem](<../inference/serving/Serving DeepSeek-V4 why million-token context is an inference systems problem.md>) · `serving` · together
  Explains why million-token context serving is primarily an inference-systems problem.
- **2026-05-04** — [Foundational research powering efficient inference at scale](<../inference/optimization/Foundational research powering efficient inference at scale.md>) · `optimization` · together
  Summarizes research lines behind efficient inference at production scale.
- **2026-04-24** — [Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding](<../inference/speculative-decoding/Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding.md>) · `speculative-decoding` · together
  Explains distribution-aware speculative decoding for faster RL rollouts.
- **2026-04-21** — [Capacity without conflict: A guide to multi-tenant GPU cluster design for AI-native teams](<../infra-platform/gpu-clusters/Capacity without conflict A guide to multi-tenant GPU cluster design for AI-native teams.md>) · `gpu-clusters` · together
  Guide to multi-tenant GPU cluster design for avoiding capacity conflicts in AI-native teams.
- **2026-04-15** — [Parcae: Doing more with fewer parameters using stable looped models](<../models/reasoning/Parcae Doing more with fewer parameters using stable looped models.md>) · `reasoning` · together
  Explains stable looped models for doing more with fewer parameters.
- **2026-04-13** — [EinsteinArena: Harnessing the collective intelligence of agents in the wild to advance science](<../agents/multi-agent/EinsteinArena Harnessing the collective intelligence of agents in the wild to advance science.md>) · `multi-agent` · together
  Explains EinsteinArena for using collective agent intelligence to advance scientific tasks.
- **2026-04-03** — [AI for Systems: Using LLMs to Optimize Database Query Execution](<../product-engineering/architecture/AI for Systems Using LLMs to Optimize Database Query Execution.md>) · `architecture` · together
  Explores using LLMs to optimize database query execution as an AI-for-systems pattern.
- **2026-04-01** — [Inside the Together AI kernels team](<../inference/hardware/Inside the Together AI kernels team.md>) · `hardware` · together
  Looks inside a kernel team’s workflow for optimizing AI inference and training performance.
- **2026-03-17** — [Mamba-3](<../models/reasoning/Mamba-3.md>) · `reasoning` · together
  Describes Mamba-3 and its implications for efficient sequence modeling.
- **2026-03-05** — [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](<../inference/kernels/FlashAttention-4 Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling.md>) · `kernels` · together
  Covers FlashAttention-4 algorithm and kernel co-design for asymmetric hardware scaling.
- **2026-03-04** — [Cache-aware prefill-decode disaggregation for long-context LLM serving](<../inference/serving/Cache-aware prefill-decode disaggregation for long-context LLM serving.md>) · `serving` · together
  Explains cache-aware prefill/decode disaggregation for faster long-context LLM serving.
- **2026-02-24** — [Optimizing Training Workloads for GPU Clusters](<../infra-platform/gpu-clusters/Optimizing Training Workloads for GPU Clusters.md>) · `gpu-clusters` · together
  Covers optimization patterns for training workloads on GPU clusters.
- **2026-02-23** — [How speech models fail where it matters the most and what to do about it](<../models/multimodal/How speech models fail where it matters the most and what to do about it.md>) · `multimodal` · together
  Analyzes speech model failure modes that matter for production applications.
- **2026-02-19** — [Consistency diffusion language models: Up to 14x faster inference without sacrificing quality](<../inference/optimization/Consistency diffusion language models Up to 14x faster inference without sacrificing quality.md>) · `optimization` · together
  Explains consistency diffusion language models for faster inference without large quality loss.
- **2026-02-06** — [What do LLMs think when you don't tell them what to think about?](<../evals-observability/evaluation/What do LLMs think when you don't tell them what to think about.md>) · `evaluation` · together
  Investigates what LLMs do under underspecified prompting and how that affects evaluation.
- **2026-02-02** — [Fine-tuning open LLM judges to outperform GPT-5.2](<../models/reinforcement-learning/Fine-tuning open LLM judges to outperform GPT-5.2.md>) · `reinforcement-learning` · together
  Explains fine-tuning open LLM judges to outperform a frontier judge model.
- **2026-01-26** — [DSGym: A holistic framework for evaluating and training data science agents](<../evals-observability/benchmark-design/DSGym A holistic framework for evaluating and training data science agents.md>) · `benchmark-design` · together
  Introduces DSGym for evaluating and training data science agents.
- **2026-01-22** — [Optimizing inference speed and costs: Lessons learned from large-scale deployments](<../inference/optimization/Optimizing inference speed and costs Lessons learned from large-scale deployments.md>) · `optimization` · together
  Lessons from optimizing inference speed and cost in large-scale deployments.
- **2026-01-12** — [Inside multi-node training: How to scale model training across GPU clusters](<../infra-platform/gpu-clusters/Inside multi-node training How to scale model training across GPU clusters.md>) · `gpu-clusters` · together
  Explains multi-node model training across GPU clusters and the coordination issues that appear at scale.
- **2026-01-08** — [How to choose the right open model for production](<../product-engineering/architecture/How to choose the right open model for production.md>) · `architecture` · together
  Guide to choosing open models for production based on workload, quality, and serving constraints.
- **2025-11-04** — [How to evaluate and benchmark Large Language Models (LLMs)](<../evals-observability/benchmark-design/How to evaluate and benchmark Large Language Models (LLMs).md>) · `benchmark-design` · together
  Guide to evaluating and benchmarking LLMs for production model selection.
- **2025-10-22** — [Large Reasoning Models Fail to Follow Instructions During Reasoning: A Benchmark Study](<../evals-observability/benchmark-design/Large Reasoning Models Fail to Follow Instructions During Reasoning A Benchmark Study.md>) · `benchmark-design` · together
  Benchmark study showing instruction-following failures during reasoning.
- **2025-10-10** — [ATLAS runtime-learning accelerators for LLM inference](<../inference/speculative-decoding/ATLAS runtime-learning accelerators for LLM inference.md>) · `speculative-decoding` · together
  Introduces ATLAS, a runtime-learning accelerator for improving LLM inference.
- **2025-08-21** — [AI agents for efficient LLM inference engineering](<../agents/tool-use/AI agents for efficient LLM inference engineering.md>) · `tool-use` · together
  Case study of using AI agents to automate engineering tasks while developing efficient inference systems.
- **2025-08-15** — [Fine-tuning small open-source LLMs for specialized tasks](<../models/fine-tuning/Fine-tuning small open-source LLMs for specialized tasks.md>) · `fine-tuning` · together
  Case study fine-tuning small open-source LLMs to beat larger closed models on specialized tasks.
- **2025-07-02** — [DeepSWE coding agent trained with scaled RL](<../agents/tool-use/DeepSWE coding agent trained with scaled RL.md>) · `tool-use` · together
  Explains DeepSWE, an open-source coding agent trained by scaling reinforcement learning.
- **2025-06-12** — [From Zero to One: Building An Autonomous and Open Data Scientist Agent from Scratch](<../agents/planning/From Zero to One Building An Autonomous and Open Data Scientist Agent from Scratch.md>) · `planning` · together
  Walkthrough of building an autonomous open data-scientist agent from scratch.
- **2025-06-05** — [Model-Preserving Adaptive Rounding with YAQA](<../inference/quantization/Model-Preserving Adaptive Rounding with YAQA.md>) · `quantization` · together
  Explains YAQA, a model-preserving adaptive rounding approach for quantization.
- **2025-05-28** — [Mixture-of-Agents Alignment for post-training](<../models/fine-tuning/Mixture-of-Agents Alignment for post-training.md>) · `fine-tuning` · together
  Explains Mixture-of-Agents Alignment for improving post-training with collective model intelligence.
- **2025-05-12** — [Boosting DeepSeek-R1 speed with customized speculative decoding](<../inference/speculative-decoding/Boosting DeepSeek-R1 speed with customized speculative decoding.md>) · `speculative-decoding` · together
  Shows customized speculative decoding for accelerating DeepSeek-R1 serving.
- **2025-04-21** — [Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas](<../inference/kernels/Chipmunk Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas.md>) · `kernels` · together
  Describes Chipmunk, a training-free acceleration method for diffusion transformers.
- **2025-04-17** — [Continued Fine-tuning of LLMs: A Technical Deep Dive](<../models/fine-tuning/Continued Fine-tuning of LLMs A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into continued fine-tuning of LLMs.
- **2025-04-17** — [Direct Preference Optimization: A Technical Deep Dive](<../models/reinforcement-learning/Direct Preference Optimization A Technical Deep Dive.md>) · `reinforcement-learning` · together
  Technical deep dive into Direct Preference Optimization for aligning language models.
- **2025-04-16** — [Open Deep Research](<../agents/tool-use/Open Deep Research.md>) · `tool-use` · together
  Describes an open deep research system combining retrieval, planning, and tool use.
- **2025-04-08** — [DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level](<../agents/tool-use/DeepCoder A Fully Open-Source 14B Coder at O3-mini Level.md>) · `tool-use` · together
  Describes DeepCoder, an open-source coding model trained for O3-mini-level coding performance.
- **2025-03-15** — [ThunderKittens Now Optimized for NVIDIA Blackwell GPUs](<../inference/hardware/ThunderKittens Now Optimized for NVIDIA Blackwell GPUs.md>) · `hardware` · together
  Describes ThunderKittens optimizations for NVIDIA Blackwell GPUs.
- **2025-02-25** — [Minions: embracing small LMs, shifting compute on-device, and cutting cloud costs in the process](<../models/reasoning/Minions embracing small LMs, shifting compute on-device, and cutting cloud costs in the process.md>) · `reasoning` · together
  Explores using small language models and on-device compute to reduce cloud inference costs.
- **2025-02-13** — [Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection](<../inference/hardware/Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection.md>) · `hardware` · together
  Describes Blackwell BF16 training acceleration with the Together Kernel Collection.
- **2024-11-25** — [Fine-Tuning LLMs for Multi-Turn Conversations: A Technical Deep Dive](<../models/fine-tuning/Fine-Tuning LLMs for Multi-Turn Conversations A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into fine-tuning LLMs for multi-turn conversations.
- **2024-11-25** — [Long Context Fine-Tuning: A Technical Deep Dive](<../models/fine-tuning/Long Context Fine-Tuning A Technical Deep Dive.md>) · `fine-tuning` · together
  Technical deep dive into long-context fine-tuning.
- **2024-10-30** — [Even Better, Even Faster Quantized LLMs with QTIP](<../inference/quantization/Even Better, Even Faster Quantized LLMs with QTIP.md>) · `quantization` · together
  Explains QTIP quantization for faster LLM inference with improved quality preservation.
- **2024-10-14** — [Linearizing LLMs with LoLCATs](<../models/reasoning/Linearizing LLMs with LoLCATs.md>) · `reasoning` · together
  Explains LoLCATs for linearizing LLM attention while preserving useful behavior.
- **2024-10-08** — [Multimodal Document RAG with Llama 3.2 Vision and ColQwen2](<../rag-retrieval/pipelines/Multimodal Document RAG with Llama 3.2 Vision and ColQwen2.md>) · `pipelines` · together
  Builds a multimodal document RAG pipeline with Llama 3.2 Vision and ColQwen2.
- **2024-09-09** — [The Mamba in the Llama: Distilling and Accelerating Hybrid Models](<../models/fine-tuning/The Mamba in the Llama Distilling and Accelerating Hybrid Models.md>) · `fine-tuning` · together
  Explains distilling and accelerating hybrid Mamba/Transformer models.
- **2024-09-05** — [Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection](<../inference/hardware/Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection.md>) · `hardware` · together
  Shows how kernel work improves H200 and H100 GPU cluster performance.
- **2024-09-05** — [Speculative decoding for high-throughput long-context inference](<../inference/speculative-decoding/Speculative decoding for high-throughput long-context inference.md>) · `speculative-decoding` · together
  Explains speculative decoding for high-throughput long-context inference.
- **2024-08-28** — [TEAL: Training-Free Activation Sparsity in Large Language Models](<../inference/optimization/TEAL Training-Free Activation Sparsity in Large Language Models.md>) · `optimization` · together
  Explains TEAL, a training-free activation sparsity method for large language models.
- **2024-08-13** — [A practitioner's guide to testing and running large GPU clusters for training generative AI models](<../infra-platform/gpu-clusters/A practitioner's guide to testing and running large GPU clusters for training generative AI models.md>) · `gpu-clusters` · together
  Practical guide to testing and operating large GPU clusters for generative model training.
- **2024-07-31** — [Llama 3.1: Same model, different results. The impact of a percentage point.](<../evals-observability/benchmark-design/Llama 3.1 Same model, different results. The impact of a percentage point.md>) · `benchmark-design` · together
  Explains how small quality differences and deployment choices affect Llama 3.1 results.
- **2024-07-12** — [Fine-tuning Llama-3 toward GPT-4 performance at lower cost](<../models/fine-tuning/Fine-tuning Llama-3 toward GPT-4 performance at lower cost.md>) · `fine-tuning` · together
  Shows fine-tuning Llama 3 toward GPT-4-like task performance at lower cost.
- **2024-07-11** — [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](<../inference/kernels/FlashAttention-3 Fast and Accurate Attention with Asynchrony and Low-precision.md>) · `kernels` · together
  Explains FlashAttention-3 and its asynchronous low-precision attention optimizations.
- **2024-06-24** — [Building a personalized code assistant with open-source LLMs using RAG Fine-tuning](<../rag-retrieval/pipelines/Building a personalized code assistant with open-source LLMs using RAG Fine-tuning.md>) · `pipelines` · together
  Builds a personalized code assistant using RAG fine-tuning with open-source LLMs.
- **2024-06-18** — [SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices](<../inference/speculative-decoding/SpecExec Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices.md>) · `speculative-decoding` · together
  Introduces SpecExec for massively parallel speculative decoding on consumer devices.
- **2024-06-11** — [Together MoA collective intelligence of open-source models](<../agents/multi-agent/Together MoA collective intelligence of open-source models.md>) · `multi-agent` · together
  Explains Mixture-of-Agents for improving model outputs through collective open-source model reasoning.
- **2024-06-06** — [Dragonfly: A large vision-language model with multi-resolution zoom](<../models/multimodal/Dragonfly A large vision-language model with multi-resolution zoom.md>) · `multimodal` · together
  Introduces Dragonfly, a vision-language model with multi-resolution zoom.
- **2024-05-01** — [FAQ: Building LLMs with RedPajama-v2, a 30 trillion token web dataset](<../models/fine-tuning/FAQ Building LLMs with RedPajama-v2, a 30 trillion token web dataset.md>) · `fine-tuning` · together
  FAQ-style technical explanation of building LLMs with the RedPajama-v2 dataset.
- **2024-03-04** — [BASED: Simple linear attention language models balance the recall-throughput tradeoff](<../models/reasoning/BASED Simple linear attention language models balance the recall-throughput tradeoff.md>) · `reasoning` · together
  Explains BASED linear-attention language models and the recall-throughput tradeoff.
- **2024-02-27** — [Evo: Long-context modeling from molecular to genome scale](<../models/reasoning/Evo Long-context modeling from molecular to genome scale.md>) · `reasoning` · together
  Explains Evo and long-context modeling from molecular to genome-scale sequences.
- **2024-02-20** — [BitDelta: Your Fine-Tune May Only Be Worth One Bit](<../models/fine-tuning/BitDelta Your Fine-Tune May Only Be Worth One Bit.md>) · `fine-tuning` · together
  Explains BitDelta and how small weight deltas can represent fine-tuned model changes.
- **2024-01-31** — [Function calling and JSON mode](<../prompt-engineering/structured-output/Function calling and JSON mode.md>) · `structured-output` · together
  Explains function calling and JSON mode for structured LLM application outputs.
- **2024-01-11** — [Long context retrieval models with Monarch Mixer](<../rag-retrieval/search/Long context retrieval models with Monarch Mixer.md>) · `search` · together
  Explains long-context retrieval models using Monarch Mixer.
- **2023-12-08** — [StripedHyena-7B and efficient architectures beyond Transformers](<../models/reasoning/StripedHyena-7B and efficient architectures beyond Transformers.md>) · `reasoning` · together
  Introduces StripedHyena-7B and efficient architectures beyond Transformers.
- **2023-11-13** — [FlashFFTConv: Efficient Convolutions for Long Sequences with Tensor Cores](<../inference/kernels/FlashFFTConv Efficient Convolutions for Long Sequences with Tensor Cores.md>) · `kernels` · together
  Explains FlashFFTConv for efficient long-sequence convolutions on tensor cores.
- **2023-10-30** — [RedPajama-Data-v2: An open dataset with 30 trillion tokens for training large language models](<../models/fine-tuning/RedPajama-Data-v2 An open dataset with 30 trillion tokens for training large language models.md>) · `fine-tuning` · together
  Introduces RedPajama-Data-v2, a large web dataset for training language models.
- **2023-10-12** — [Flash-Decoding for long-context inference](<../inference/kernels/Flash-Decoding for long-context inference.md>) · `kernels` · together
  Introduces Flash-Decoding for efficient long-context inference.
- **2023-09-11** — [Medusa: Simple framework for accelerating LLM generation with multiple decoding heads](<../inference/speculative-decoding/Medusa Simple framework for accelerating LLM generation with multiple decoding heads.md>) · `speculative-decoding` · together
  Introduces Medusa, a multi-decoding-head framework for accelerating LLM generation.
- **2023-07-25** — [Monarch Mixer: A new model architecture for increased efficiency](<../models/reasoning/Monarch Mixer A new model architecture for increased efficiency.md>) · `reasoning` · together
  Introduces Monarch Mixer as an efficient model architecture.
- **2023-07-17** — [FlashAttention-2 for faster training and inference](<../inference/kernels/FlashAttention-2 for faster training and inference.md>) · `kernels` · together
  Introduces FlashAttention-2 and its impact on training and inference speed.
- **2023-01-23** — [FlashConv: speeding up state space models](<../models/reasoning/FlashConv speeding up state space models.md>) · `reasoning` · together
  Explains FlashConv and efficient state-space model execution.
- **2022-12-05** — [Overcoming communication bottlenecks for decentralized training, part 2](<../infra-platform/gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 2.md>) · `gpu-clusters` · together
  Continues the decentralized training discussion with techniques for communication-efficient optimization.
- **2022-11-30** — [Overcoming communication bottlenecks for decentralized training, part 1](<../infra-platform/gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 1.md>) · `gpu-clusters` · together
  Explains communication bottlenecks in decentralized foundation-model training.
- **2022-11-17** — [HELM: benchmarking large language models on the Together Research Computer](<../models/benchmarks/HELM benchmarking large language models on the Together Research Computer.md>) · `benchmarks` · together
  Describes HELM benchmarking on the Together Research Computer.
