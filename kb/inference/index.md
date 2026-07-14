# inference

130 articles.

- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<optimization/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `optimization` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-06-30** — [Multi-token Residual Prediction](<optimization/Multi-token Residual Prediction.md>) · `optimization` · modal
  Explains multi-token residual prediction as an inference acceleration technique for generating multiple tokens per step.
- **2026-06-30** — [Using OSS models to save on inference costs without cutting quality](<serving/Using OSS models to save on inference costs without cutting quality.md>) · `serving` · braintrust
  Explains using open-source models to reduce inference cost without sacrificing quality, emphasizing eval-driven model selection and serving tradeoffs.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-06-23** — [How we built the world’s fastest API for GLM-5.2](<optimization/How we built the world’s fastest API for GLM-5.2.md>) · `optimization` · baseten
  Engineering writeup on building a high-speed GLM-5.2 API.
- **2026-06-22** — [Achieve state-of-the-art inference latencies with speculative decoding](<optimization/Achieve state-of-the-art inference latencies with speculative decoding.md>) · `optimization` · modal
  Explains speculative decoding for lower inference latency, including draft-model tradeoffs and production serving considerations.
- **2026-06-22** — [Best practices to accelerate inference for large-scale production workloads](<optimization/Best practices to accelerate inference for large-scale production workloads.md>) · `optimization` · together
  Best practices for accelerating inference in large-scale production workloads.
- **2026-06-22** — [Introducing Modal Auto Endpoints: Optimized inference you actually own](<serving/Introducing Modal Auto Endpoints Optimized inference you actually own.md>) · `serving` · modal
  Describes auto endpoints for owned inference deployments, including optimized serving configuration and operational control.
- **2026-06-19** — [Speculation Is All You Need](<optimization/Speculation Is All You Need.md>) · `optimization` · modal
  Deep dive into speculative decoding and related techniques for improving LLM inference latency and throughput.
- **2026-06-02** — [MiniMax-M3 efficient 1M-token multimodal serving](<serving/MiniMax-M3 efficient 1M-token multimodal serving.md>) · `serving` · together
  Covers efficient MiniMax-M3 serving for million-token context and multimodal workloads.
- **2026-05-18** — [Sub-second image generation with Flux.2 and Qwen-Image](<optimization/Sub-second image generation with Flux.2 and Qwen-Image.md>) · `optimization` · baseten
  Explains sub-second image generation with FLUX.2 and Qwen-Image serving optimizations.
- **2026-05-12** — [Engineering low-latency voice agents](<optimization/Engineering low-latency voice agents.md>) · `optimization` · sierra
  Engineering note on low-latency voice agents, covering response-time constraints and optimization across speech and model serving.
- **2026-05-12** — [A more reliable inference layer for foundation models](<serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-05-12** — [Preserving agent behavior while serving LLMs reliably](<serving/Preserving agent behavior while serving LLMs reliably.md>) · `serving` · sierra
  Covers model failover for preserving agent behavior while serving LLMs reliably across model/provider disruptions.
- **2026-05-11** — [Serving DeepSeek-V4: why million-token context is an inference systems problem](<serving/Serving DeepSeek-V4 why million-token context is an inference systems problem.md>) · `serving` · together
  Explains why million-token context serving is primarily an inference-systems problem.
- **2026-05-08** — [DFlash: 3x faster LLM inference](<optimization/DFlash 3x faster LLM inference.md>) · `optimization` · baseten
  Explains DFlash as an optimization for faster LLM inference.
- **2026-05-04** — [Foundational research powering efficient inference at scale](<optimization/Foundational research powering efficient inference at scale.md>) · `optimization` · together
  Summarizes research lines behind efficient inference at production scale.
- **2026-04-24** — [Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding](<optimization/Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding.md>) · `optimization` · together
  Explains distribution-aware speculative decoding for faster RL rollouts.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-04-01** — [Inside the Together AI kernels team](<hardware/Inside the Together AI kernels team.md>) · `hardware` · together
  Looks inside a kernel team’s workflow for optimizing AI inference and training performance.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<optimization/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `optimization` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-06** — [How we built the fastest GLM 5 API](<optimization/How we built the fastest GLM 5 API.md>) · `optimization` · baseten
  Explains serving optimizations used to build a fast GLM 5 API.
- **2026-03-06** — [Inference providers vs. API routers](<serving/Inference providers vs. API routers.md>) · `serving` · fireworks
  Explains the operational difference between inference providers and API routers, including routing, control, and token provenance.
- **2026-03-05** — [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](<optimization/FlashAttention-4 Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling.md>) · `optimization` · together
  Covers FlashAttention-4 algorithm and kernel co-design for asymmetric hardware scaling.
- **2026-03-04** — [Cache-aware prefill-decode disaggregation for long-context LLM serving](<serving/Cache-aware prefill-decode disaggregation for long-context LLM serving.md>) · `serving` · together
  Explains cache-aware prefill/decode disaggregation for faster long-context LLM serving.
- **2026-02-19** — [Consistency diffusion language models: Up to 14x faster inference without sacrificing quality](<optimization/Consistency diffusion language models Up to 14x faster inference without sacrificing quality.md>) · `optimization` · together
  Explains consistency diffusion language models for faster inference without large quality loss.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-02-11** — [How we built the fastest Kimi K2.5 on Artificial Analysis](<optimization/How we built the fastest Kimi K2.5 on Artificial Analysis.md>) · `optimization` · baseten
  Explains optimizations behind fast Kimi K2.5 serving on Artificial Analysis.
- **2026-02-03** — [The Baseten Inference Stack at NVIDIA Dynamo Day](<serving/The Baseten Inference Stack at NVIDIA Dynamo Day.md>) · `serving` · baseten
  Describes Baseten inference-stack ideas presented around NVIDIA Dynamo and production serving.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<optimization/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `optimization` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2026-01-22** — [Optimizing inference speed and costs: Lessons learned from large-scale deployments](<optimization/Optimizing inference speed and costs Lessons learned from large-scale deployments.md>) · `optimization` · together
  Lessons from optimizing inference speed and cost in large-scale deployments.
- **2026-01-15** — [Open Responses: What you need to know](<serving/Open Responses What you need to know.md>) · `serving` · huggingface
  Argues Chat Completions is a poor fit for agentic workloads and proposes Open Responses, an open version of OpenAI's Responses API: stateless by default with encrypted reasoning, standardized model params, and provider-side agentic loops that execute tool calls before returning.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-11-12** — [Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell](<optimization/Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell.md>) · `optimization` · baseten
  Explains Kimi K2 Thinking serving at high throughput on NVIDIA Blackwell hardware.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-10-24** — [How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster](<optimization/How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster.md>) · `optimization` · baseten
  Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
- **2025-10-21** — [Engineering for Real-Time Voice Agent Latency](<serving/Engineering for Real-Time Voice Agent Latency.md>) · `serving` · cresta
  Technical discussion of latency in real-time voice agents and the engineering constraints behind responsive spoken interaction.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-10-10** — [ATLAS runtime-learning accelerators for LLM inference](<optimization/ATLAS runtime-learning accelerators for LLM inference.md>) · `optimization` · together
  Introduces ATLAS, a runtime-learning accelerator for improving LLM inference.
- **2025-09-29** — [Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models](<optimization/Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models.md>) · `optimization` · huggingface
  Accelerates a Qwen3-8B agent on Intel Core Ultra by ~1.3x using speculative decoding with a depth-pruned Qwen3-0.6B int8 draft model in OpenVINO GenAI, showing how draft-model depth pruning raises acceptance rate per unit of draft cost on client hardware.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-17** — [A postmortem of three recent issues](<serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-11** — [Tricks from OpenAI gpt-oss YOU 🫵 can use with transformers](<optimization/Tricks from OpenAI gpt-oss YOU 🫵 can use with transformers.md>) · `optimization` · huggingface
  Unpacks the optimizations shipped in transformers for OpenAI's gpt-oss and reusable by any model: zero-build kernels pulled from the Hub, MXFP4 quantization, tensor parallelism, expert parallelism, continuous batching and dynamic sliding-window caches.
- **2025-09-02** — [Make your ZeroGPU Spaces go brrr with ahead-of-time compilation](<optimization/Make your ZeroGPU Spaces go brrr with ahead-of-time compilation.md>) · `optimization` · huggingface
  Uses PyTorch ahead-of-time compilation (torch.export + AOTInductor) instead of just-in-time torch.compile so short-lived ZeroGPU processes keep the compiled artifact, giving 1.3x-1.8x speedups on Flux, Wan and LTX; also covers FP8 quantization, dynamic shapes and multi-compile for varying resolutions.
- **2025-08-18** — [From Zero to GPU: A Guide to Building and Scaling Production-Ready CUDA Kernels](<hardware/From Zero to GPU A Guide to Building and Scaling Production-Ready CUDA Kernels.md>) · `hardware` · huggingface
  End-to-end guide to writing a custom CUDA kernel and shipping it with HF's kernel-builder: Nix-based reproducible builds across multiple GPU architectures and torch ABIs, PyTorch op registration and torch.compile compatibility, and distribution via `get_kernel()` from the Hub instead of compiling at install time.
- **2025-08-14** — [More than Just a Model: How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency](<serving/More than Just a Model How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency.md>) · `serving` · cresta
  Explains production summarization architecture focused on low latency, adaptability, and precision rather than model choice alone.
- **2025-08-07** — [How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs](<optimization/How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs.md>) · `optimization` · baseten
  Explains how to run GPT-OSS 120B at high token throughput on NVIDIA GPUs.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-07-23** — [Fast LoRA inference for Flux with Diffusers and PEFT](<optimization/Fast LoRA inference for Flux with Diffusers and PEFT.md>) · `optimization` · huggingface
  Gets ~2.3x faster LoRA inference for Flux.1-Dev by combining LoRA hotswapping with torch.compile without recompilation — using peft's hotswap_adapter, max-rank padding so shapes stay static, and flags to avoid recompiles when adapters have different ranks and target layers. Also covers fusing/unfusing and FP8 quantization on top.
- **2025-06-18** — [Run FLUX.1-dev three times faster](<optimization/Run FLUX.1-dev three times faster.md>) · `optimization` · modal
  Explains optimizations for running FLUX.1-dev faster, including inference configuration and image-model serving tradeoffs.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-12** — [Learn the Hugging Face Kernel Hub in 5 Minutes](<optimization/Learn the Hugging Face Kernel Hub in 5 Minutes.md>) · `optimization` · huggingface
  Introduces the Kernel Hub: `get_kernel("kernels-community/activation")` downloads precompiled optimized CUDA kernels at runtime with no local build system, and the post benchmarks the drop-in kernels (activation, RMSNorm, Flash Attention) against native PyTorch.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2025-06-05** — [Model-Preserving Adaptive Rounding with YAQA](<quantization/Model-Preserving Adaptive Rounding with YAQA.md>) · `quantization` · together
  Explains YAQA, a model-preserving adaptive rounding approach for quantization.
- **2025-06-04** — [KV Cache from scratch in nanoVLM](<optimization/KV Cache from scratch in nanoVLM.md>) · `optimization` · huggingface
  Implements KV caching from scratch in nanoVLM, explaining prefill vs decode, how cached keys/values remove redundant attention recomputation, and the code changes to the attention block and generation loop; yields a 38% generation speedup.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-05-21** — [Exploring Quantization Backends in Diffusers](<quantization/Exploring Quantization Backends in Diffusers.md>) · `quantization` · huggingface
  Compares the quantization backends integrated in Diffusers — bitsandbytes (4-bit/8-bit/NF4), GGUF, torchao, Quanto and native FP8 — on Flux.1-dev, with memory-savings and quality trade-offs plus a blind test showing 8-bit differences are usually imperceptible. Includes code for combining quantization with torch.compile and CPU offloading.
- **2025-05-13** — [Blazingly fast whisper transcriptions with Inference Endpoints](<optimization/Blazingly fast whisper transcriptions with Inference Endpoints.md>) · `optimization` · huggingface
  An optimized Whisper deployment on Inference Endpoints built on vLLM, targeting Ada Lovelace GPUs (L4/L40s) to unlock torch.compile JIT kernels, CUDA graphs and a float8 KV cache — with the resulting latency/throughput gains for transcription workloads.
- **2025-05-12** — [Boosting DeepSeek-R1 speed with customized speculative decoding](<optimization/Boosting DeepSeek-R1 speed with customized speculative decoding.md>) · `optimization` · together
  Shows customized speculative decoding for accelerating DeepSeek-R1 serving.
- **2025-04-21** — [Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas](<optimization/Chipmunk Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas.md>) · `optimization` · together
  Describes Chipmunk, a training-free acceleration method for diffusion transformers.
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-03-15** — [ThunderKittens Now Optimized for NVIDIA Blackwell GPUs](<hardware/ThunderKittens Now Optimized for NVIDIA Blackwell GPUs.md>) · `hardware` · together
  Describes ThunderKittens optimizations for NVIDIA Blackwell GPUs.
- **2025-03-13** — [Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence](<serving/Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence.md>) · `serving` · cresta
  Explains ML services, inference graphs, and real-time intelligence components in a production voice platform.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-02-13** — [Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection](<hardware/Together AI Achieves 90% Faster BF16 Training with NVIDIA Blackwell Platform and Together Kernel Collection.md>) · `hardware` · together
  Describes Blackwell BF16 training acceleration with the Together Kernel Collection.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2025-01-09** — [Driving model performance optimization: 2024 highlights](<optimization/Driving model performance optimization 2024 highlights.md>) · `optimization` · baseten
  Summarizes concrete model-performance optimization work across inference serving, batching, and hardware.
- **2024-12-19** — [A quick introduction to speculative decoding](<optimization/A quick introduction to speculative decoding.md>) · `optimization` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<optimization/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `optimization` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-11-20** — [Faster Text Generation with Self-Speculative Decoding](<optimization/Faster Text Generation with Self-Speculative Decoding.md>) · `optimization` · huggingface
  LayerSkip self-speculative decoding: the same model drafts with early-exit at an intermediate layer and verifies with the remaining layers, reusing the KV cache so no separate draft model or extra memory is needed; includes speedups on Llama checkpoints trained with layer dropout + early-exit loss.
- **2024-10-30** — [Even Better, Even Faster Quantized LLMs with QTIP](<quantization/Even Better, Even Faster Quantized LLMs with QTIP.md>) · `quantization` · together
  Explains QTIP quantization for faster LLM inference with improved quality preservation.
- **2024-10-29** — [Universal Assisted Generation: Faster Decoding with Any Assistant Model](<optimization/Universal Assisted Generation Faster Decoding with Any Assistant Model.md>) · `optimization` · huggingface
  Universal Assisted Generation (Intel Labs + HF) lifts speculative decoding's requirement that the draft model share the target's tokenizer by re-encoding draft tokens between vocabularies, giving 1.5x-2x speedups for models like gemma-2-9b and Mixtral-8x22B that have no small same-family draft model.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-10-08** — [Faster Assisted Generation with Dynamic Speculation](<optimization/Faster Assisted Generation with Dynamic Speculation.md>) · `optimization` · huggingface
  Dynamic speculative decoding (Intel Labs + HF, default in Transformers 4.45) adapts the speculation lookahead per iteration instead of using a fixed number of draft tokens, giving up to 2.7x faster assisted generation depending on task while preserving the target model's output.
- **2024-09-18** — [Fine-tuning LLMs to 1.58bit: extreme quantization made easy](<quantization/Fine-tuning LLMs to 1.58bit extreme quantization made easy.md>) · `quantization` · huggingface
  Shows how to fine-tune an existing Llama3-8B/SmolLM into BitNet's 1.58-bit ternary ({-1,0,1}) weight format instead of pre-training from scratch, using BitLinear layers, a lambda-scheduled quantization warmup and per-row/per-tensor scaling. Reports pre-training and fine-tuning results plus custom kernel benchmarks.
- **2024-09-16** — [Boost your throughput with dynamic batching](<optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-09-05** — [Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection](<hardware/Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection.md>) · `hardware` · together
  Shows how kernel work improves H200 and H100 GPU cluster performance.
- **2024-09-05** — [Speculative decoding for high-throughput long-context inference](<optimization/Speculative decoding for high-throughput long-context inference.md>) · `optimization` · together
  Explains speculative decoding for high-throughput long-context inference.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-28** — [TEAL: Training-Free Activation Sparsity in Large Language Models](<optimization/TEAL Training-Free Activation Sparsity in Large Language Models.md>) · `optimization` · together
  Explains TEAL, a training-free activation sparsity method for large language models.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<optimization/How to double tokens per second for Llama 3 with Medusa.md>) · `optimization` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-13** — [Introduction to ggml](<optimization/Introduction to ggml.md>) · `optimization` · huggingface
  A hands-on introduction to ggml — the C/C++ tensor library behind llama.cpp, whisper.cpp, ollama and LM Studio — covering its context/graph memory model, GGUF file format, quantized tensor types, and backend dispatch (CPU/CUDA/Metal) via a worked matrix-multiplication example.
- **2024-08-01** — [Introducing automatic LLM optimization with TensorRT-LLM Engine Builder](<optimization/Introducing automatic LLM optimization with TensorRT-LLM Engine Builder.md>) · `optimization` · baseten
  Describes automatic LLM optimization with TensorRT-LLM Engine Builder for production serving.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-07-30** — [Memory-efficient Diffusion Transformers with Quanto and Diffusers](<quantization/Memory-efficient Diffusion Transformers with Quanto and Diffusers.md>) · `quantization` · huggingface
  Quantizes diffusion-transformer pipelines (PixArt-Sigma, SD3, Flux) with Quanto: int8/fp8/int4 on the transformer and T5 text encoders cuts SD3 inference memory from 18.8GB FP16 toward consumer-GPU range, with per-component memory/latency/quality tradeoffs and gotchas.
- **2024-07-23** — [How to serve 10,000 fine-tuned LLMs from a single GPU](<serving/How to serve 10,000 fine-tuned LLMs from a single GPU.md>) · `serving` · baseten
  Explains serving many fine-tuned LLM adapters from a single GPU with efficient multiplexing.
- **2024-07-18** — [TGI Multi-LoRA: Deploy Once, Serve 30 Models](<serving/TGI Multi-LoRA Deploy Once, Serve 30 Models.md>) · `serving` · huggingface
  Explains TGI's multi-LoRA serving: load one base model plus up to ~30 LoRA adapters in a single deployment, batching requests for different adapters together via a gathered/segmented matmul so per-adapter overhead is small. Argues the cost and ops case for many specialized adapters over many full deployments, with latency numbers vs single-adapter serving.
- **2024-07-11** — [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](<optimization/FlashAttention-3 Fast and Accurate Attention with Asynchrony and Low-precision.md>) · `optimization` · together
  Explains FlashAttention-3 and its asynchronous low-precision attention optimizations.
- **2024-07-11** — [Using asynchronous inference in production](<serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<optimization/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `optimization` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<optimization/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `optimization` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-06-18** — [SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices](<optimization/SpecExec Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices.md>) · `optimization` · together
  Introduces SpecExec for massively parallel speculative decoding on consumer devices.
- **2024-05-29** — [Benchmarking Text Generation Inference](<serving/Benchmarking Text Generation Inference.md>) · `serving` · huggingface
  How to use the TGI benchmarking tool to profile LLM serving: separating prefill from decode, reading latency vs throughput curves under different batch sizes, and choosing the batch size that meets your latency SLO.
- **2024-05-03** — [Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face](<serving/Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face.md>) · `serving` · huggingface
  The Artificial Analysis LLM Performance Leaderboard benchmarks hosted inference endpoints (not model quality) on throughput tokens/s, time-to-first-token, and price per token across providers, arguing latency is the limiting factor for agentic/tool-use systems where sequential LLM calls compound.
- **2024-05-01** — [Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints](<serving/Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints.md>) · `serving` · huggingface
  Walks through a custom Inference Endpoints handler that chains Whisper-large-v3 ASR, Pyannote diarization and speculative decoding (with a distil-whisper assistant model and SDPA/Flash Attention 2) into one deployable pipeline, including the pre/post-processing needed to align transcript timestamps with speaker turns.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-04-03** — [Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon](<optimization/Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon.md>) · `optimization` · huggingface
  Accelerates SetFit few-shot text classification inference by 7.8x on Intel Xeon (Sapphire Rapids) using Optimum Intel + OpenVINO post-training quantization to int8, with an accuracy-drop constraint; includes the few-shot accuracy context where SetFit beats 3-shot GPT-3.5/GPT-4 on Banking77.
- **2024-03-28** — [Using fractional H100 GPUs for efficient model serving](<serving/Using fractional H100 GPUs for efficient model serving.md>) · `serving` · baseten
  Explains fractional H100 usage for efficient model serving and better GPU utilization.
- **2024-03-18** — [Quanto: a PyTorch quantization backend for Optimum](<quantization/Quanto a PyTorch quantization backend for Optimum.md>) · `quantization` · huggingface
  Introduces quanto, a PyTorch quantization backend for Optimum with a device-agnostic design: int8/float8 weights and activations, eager-mode quantized tensor subclass, calibration and QAT support, working across CUDA/MPS/CPU where most quantization libraries are locked to specific model or device configurations.
- **2024-03-14** — [33% faster LLM inference with FP8 quantization](<quantization/33% faster LLM inference with FP8 quantization.md>) · `quantization` · baseten
  Shows how FP8 quantization improves LLM inference throughput while managing accuracy and hardware constraints.
- **2024-03-12** — [High performance ML inference with NVIDIA TensorRT](<optimization/High performance ML inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains high-performance model inference with NVIDIA TensorRT and related deployment considerations.
- **2024-03-07** — [FP8: Efficient model inference with 8-bit floating point numbers](<quantization/FP8 Efficient model inference with 8-bit floating point numbers.md>) · `quantization` · baseten
  Explains FP8 numeric formats and why 8-bit floating point can improve efficient model inference.
- **2024-02-29** — [Text-Generation Pipeline on Intel® Gaudi® 2 AI Accelerator](<hardware/Text-Generation Pipeline on Intel® Gaudi® 2 AI Accelerator.md>) · `hardware` · huggingface
  Runs a custom text-generation pipeline for Llama-2-7b on Intel Gaudi 2 via Optimum Habana, covering HPU graph warmup, bf16, batching and static shapes, and plugging the pipeline into LangChain for a RAG-style prompt template.
- **2024-02-22** — [40% faster Stable Diffusion XL inference with NVIDIA TensorRT](<optimization/40% faster Stable Diffusion XL inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains TensorRT optimization for Stable Diffusion XL inference, including latency and throughput gains.
- **2024-02-20** — [Why GPU utilization matters for model inference](<hardware/Why GPU utilization matters for model inference.md>) · `hardware` · baseten
  Explains why GPU utilization is central to inference cost and performance.
- **2024-02-08** — [From OpenAI to Open LLMs with Messages API on Hugging Face](<serving/From OpenAI to Open LLMs with Messages API on Hugging Face.md>) · `serving` · huggingface
  TGI 1.4 adds an OpenAI Chat Completions-compatible Messages API, so open models on Inference Endpoints become a drop-in swap for GPT-4 by only changing base_url and api_key — shown with the OpenAI Python/JS clients, LangChain and LlamaIndex, and a Nous-Hermes-2-Mixtral migration.
- **2024-02-06** — [Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT](<optimization/Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT.md>) · `optimization` · baseten
  Shows how TensorRT unlocks H100 performance for model inference.
- **2024-02-01** — [Hugging Face Text Generation Inference available for AWS Inferentia2](<hardware/Hugging Face Text Generation Inference available for AWS Inferentia2.md>) · `hardware` · huggingface
  Deploys Zephyr-7B with TGI on AWS Inferentia2 via SageMaker as a GPU alternative, covering the Neuronx TGI image, the ahead-of-time model compilation/tracing step that Neuron requires (fixed batch size and sequence length), and how tensor parallelism plus continuous batching carry over.
- **2024-01-31** — [Introduction to quantizing ML models](<quantization/Introduction to quantizing ML models.md>) · `quantization` · baseten
  Introduces model quantization concepts and how they affect inference efficiency and model quality.
- **2024-01-30** — [Accelerate StarCoder with 🤗 Optimum Intel on Xeon: Q8/Q4 and Speculative Decoding](<quantization/Accelerate StarCoder with 🤗 Optimum Intel on Xeon Q8Q4 and Speculative Decoding.md>) · `quantization` · huggingface
  Over 7x inference speedup for StarCoder-15B on 4th-gen Intel Xeon (AMX) by combining INT8/INT4 weight-only quantization with assisted/speculative decoding using a small draft model, with latency and accuracy tables per configuration.
- **2024-01-15** — [Accelerating SD Turbo and SDXL Turbo Inference with ONNX Runtime and Olive](<optimization/Accelerating SD Turbo and SDXL Turbo Inference with ONNX Runtime and Olive.md>) · `optimization` · huggingface
  Benchmarks ONNX Runtime CUDA and TensorRT execution providers against PyTorch for SD Turbo and SDXL Turbo one-step generation on NVIDIA GPUs, reporting throughput gains up to 229% (SDXL Turbo) and 120% (SD Turbo). Covers graph fusions, static vs dynamic shapes, and Olive-based optimization/quantization of the pipeline.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-12-22** — [Faster Mixtral inference with TensorRT-LLM and quantization](<quantization/Faster Mixtral inference with TensorRT-LLM and quantization.md>) · `quantization` · baseten
  Shows how TensorRT-LLM and quantization improve Mixtral inference performance.
- **2023-11-28** — [NVIDIA A10 vs A10G for ML model inference](<hardware/NVIDIA A10 vs A10G for ML model inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A10G GPUs for model inference performance and cost.
- **2023-11-17** — [A guide to LLM inference and performance](<serving/A guide to LLM inference and performance.md>) · `serving` · baseten
  Comprehensive guide to LLM inference, transformer serving, latency, and throughput performance.
- **2023-11-13** — [FlashFFTConv: Efficient Convolutions for Long Sequences with Tensor Cores](<optimization/FlashFFTConv Efficient Convolutions for Long Sequences with Tensor Cores.md>) · `optimization` · together
  Explains FlashFFTConv for efficient long-sequence convolutions on tensor cores.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-10-12** — [Flash-Decoding for long-context inference](<optimization/Flash-Decoding for long-context inference.md>) · `optimization` · together
  Introduces Flash-Decoding for efficient long-context inference.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-09-11** — [Medusa: Simple framework for accelerating LLM generation with multiple decoding heads](<optimization/Medusa Simple framework for accelerating LLM generation with multiple decoding heads.md>) · `optimization` · together
  Introduces Medusa, a multi-decoding-head framework for accelerating LLM generation.
- **2023-08-30** — [SDXL inference in under 2 seconds](<optimization/SDXL inference in under 2 seconds.md>) · `optimization` · baseten
  Guide to Stable Diffusion XL inference optimization for sub-2-second image generation.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-17** — [FlashAttention-2 for faster training and inference](<optimization/FlashAttention-2 for faster training and inference.md>) · `optimization` · together
  Introduces FlashAttention-2 and its impact on training and inference speed.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.

## Also relevant (filed elsewhere)

- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<optimization/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `optimization` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-07** — [How I shipped a month of engineering work in four days with GLM 5.2 Fast](<../product-engineering/case-studies/How I shipped a month of engineering work in four days with GLM 5.2 Fast.md>) · `case-studies` · fireworks
  A senior engineer used GLM 5.2 Fast (via Fireworks' FireConnect with Claude Code) to design, spec, and implement a GPU-scheduler 'reclaim' feature in four days for $218 in inference cost — 4 PRs, ~3,000 LOC, 34 passing tests — crediting the model's ~400 tok/s speed for sustaining a real-time design/test/implement loop instead of async, tab-switching workflows.
- **2026-07-06** — [How to price serverless GPUs](<../infra-platform/cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-07-01** — [Model subsidies are ending. What do you do now?](<../infra-platform/cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-25** — [Live draft model training for speculative decoding](<../models/fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
- **2026-06-23** — [How we built the world’s fastest API for GLM-5.2](<optimization/How we built the world’s fastest API for GLM-5.2.md>) · `optimization` · baseten
  Engineering writeup on building a high-speed GLM-5.2 API.
- **2026-06-23** — [ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet)](<../evals-observability/evaluation/ParallelKernelBench Frontier LLMs can't write fast multi-GPU kernels (yet).md>) · `evaluation` · together
  Introduces ParallelKernelBench for measuring whether frontier LLMs can write fast multi-GPU kernels.
- **2026-06-22** — [Best practices to accelerate inference for large-scale production workloads](<optimization/Best practices to accelerate inference for large-scale production workloads.md>) · `optimization` · together
  Best practices for accelerating inference in large-scale production workloads.
- **2026-06-15** — [Growing the Cloudflare AI team with talent from Ensemble AI](<../industry/announcements/Growing the Cloudflare AI team with talent from Ensemble AI.md>) · `announcements` · cloudflare-ai
  Ensemble AI's team joins Cloudflare's Workers AI to improve inference economics, bringing NdLinear — a drop-in linear-layer replacement operating on multidimensional activations to cut parameters and compute — and NdLinear-LoRA for parameter-efficient fine-tuning, complementing Infire and Unweight.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<../infra-platform/deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-05-29** — [How Together AI built a fast speech-to-text stack](<../models/multimodal/How Together AI built a fast speech-to-text stack.md>) · `multimodal` · together
  Engineering writeup on building a fast speech-to-text stack.
- **2026-05-29** — [Timestep distillation: 2.5x faster FLUX.2 image generation](<../models/multimodal/Timestep distillation 2.5x faster FLUX.2 image generation.md>) · `multimodal` · baseten
  Explains timestep distillation for faster FLUX.2 image generation.
- **2026-05-27** — [Reachy Mini goes fully local](<../infra-platform/edge/Reachy Mini goes fully local.md>) · `edge` · huggingface
  Runs a full cascaded voice stack (VAD -> STT -> LLM -> TTS) locally on-device behind an OpenAI-Realtime-API-compatible /v1/realtime WebSocket, replacing the cloud backend for the Reachy Mini robot; argues cascades beat end-to-end S2S models on flexibility and latency and shows which local components to swap in.
- **2026-05-19** — [Benchmarking inference at scale: coding agents](<../evals-observability/evaluation/Benchmarking inference at scale coding agents.md>) · `evaluation` · together
  Benchmarks inference at scale for coding-agent workloads.
- **2026-05-14** — [Cost-efficient, high-performance TTS with Qwen3-TTS](<../models/multimodal/Cost-efficient, high-performance TTS with Qwen3-TTS.md>) · `multimodal` · baseten
  Describes cost-efficient high-performance Qwen3-TTS serving for text-to-speech workloads.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [How we achieved truly serverless GPUs](<../infra-platform/gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-05-04** — [Foundational research powering efficient inference at scale](<optimization/Foundational research powering efficient inference at scale.md>) · `optimization` · together
  Summarizes research lines behind efficient inference at production scale.
- **2026-04-24** — [DeepSeek-V4: a million-token context that agents can actually use](<../models/architectures/DeepSeek-V4 a million-token context that agents can actually use.md>) · `architectures` · huggingface
  Breaks down how DeepSeek-V4's architecture makes 1M-token context cheap for agents: V4-Pro needs 27% of V3.2's single-token inference FLOPs and 10% of its KV cache (V4-Flash: 10% and 7%, roughly 2% of an 8-head GQA bf16 cache), plus the agent-specific post-training decisions that build on it.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-15** — [Parcae: Doing more with fewer parameters using stable looped models](<../models/reasoning/Parcae Doing more with fewer parameters using stable looped models.md>) · `reasoning` · together
  Explains stable looped models for doing more with fewer parameters.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<../models/fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<../infra-platform/deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-04-01** — [Inside the Together AI kernels team](<hardware/Inside the Together AI kernels team.md>) · `hardware` · together
  Looks inside a kernel team’s workflow for optimizing AI inference and training performance.
- **2026-03-19** — [Introducing the Baseten Delivery Network: Fast cold starts for big models](<../infra-platform/deployment/Introducing the Baseten Delivery Network Fast cold starts for big models.md>) · `deployment` · baseten
  Introduces the Baseten Delivery Network for reducing cold starts when serving large models.
- **2026-03-17** — [Mamba-3](<../models/reasoning/Mamba-3.md>) · `reasoning` · together
  Describes Mamba-3 and its implications for efficient sequence modeling.
- **2026-03-06** — [How we built the fastest GLM 5 API](<optimization/How we built the fastest GLM 5 API.md>) · `optimization` · baseten
  Explains serving optimizations used to build a fast GLM 5 API.
- **2026-03-05** — [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](<optimization/FlashAttention-4 Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling.md>) · `optimization` · together
  Covers FlashAttention-4 algorithm and kernel co-design for asymmetric hardware scaling.
- **2026-03-04** — [Cache-aware prefill-decode disaggregation for long-context LLM serving](<serving/Cache-aware prefill-decode disaggregation for long-context LLM serving.md>) · `serving` · together
  Explains cache-aware prefill/decode disaggregation for faster long-context LLM serving.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<../models/reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-02-09** — [AI Model Performance Metrics Explained](<../evals-observability/monitoring/AI Model Performance Metrics Explained.md>) · `monitoring` · baseten
  Explains model performance metrics used in production inference, including latency, throughput, and quality signals.
- **2026-02-05** — [How to run LLM performance benchmarks (and why you should)](<../evals-observability/evaluation/How to run LLM performance benchmarks (and why you should).md>) · `evaluation` · baseten
  Explains how to run LLM performance benchmarks and which serving metrics matter.
- **2026-02-03** — [The Baseten Inference Stack at NVIDIA Dynamo Day](<serving/The Baseten Inference Stack at NVIDIA Dynamo Day.md>) · `serving` · baseten
  Describes Baseten inference-stack ideas presented around NVIDIA Dynamo and production serving.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<../infra-platform/gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-12-17** — [When Every Word Matters: Engineering Real-Time Multilingual Intelligence for Human Conversations](<../models/multimodal/When Every Word Matters Engineering Real-Time Multilingual Intelligence for Human Conversations.md>) · `multimodal` · cresta
  Engineering guide to real-time multilingual intelligence for conversations, focusing on latency and speech-language quality.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models speculative decoding and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-24** — [How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster](<optimization/How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster.md>) · `optimization` · baseten
  Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-05** — [NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI](<../models/reasoning/NVIDIA's Peter Belcak Distills Why Small Language Models are the Future of Agentic AI.md>) · `reasoning` · arize
  Summarizes the argument for small language models in agentic AI and where they can replace larger models.
- **2025-08-21** — [AI agents for efficient LLM inference engineering](<../agents/tool-use/AI agents for efficient LLM inference engineering.md>) · `tool-use` · together
  Case study of using AI agents to automate engineering tasks while developing efficient inference systems.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-08-07** — [How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs](<optimization/How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs.md>) · `optimization` · baseten
  Explains how to run GPT-OSS 120B at high token throughput on NVIDIA GPUs.
- **2025-07-28** — [Building Voice AI That Actually Works: Balancing Realistic Voices vs. Production-Ready Performance](<../models/multimodal/Building Voice AI That Actually Works Balancing Realistic Voices vs. Production-Ready Performance.md>) · `multimodal` · cresta
  Explains tradeoffs in building production voice AI, balancing naturalness, latency, reliability, and operational constraints.
- **2025-07-23** — [Transcribe speech 100x faster and 100x cheaper with open models](<../models/multimodal/Transcribe speech 100x faster and 100x cheaper with open models.md>) · `multimodal` · modal
  Shows how open speech models and batch execution can reduce transcription latency and cost at large scale.
- **2025-07-22** — [Kimi QK-Clip and multi-head latent attention](<../models/reasoning/Kimi QK-Clip and multi-head latent attention.md>) · `reasoning` · fireworks
  Explains Kimi QK-Clip, multi-head latent attention, and why training-inference key construction affects stability.
- **2025-07-16** — [Dollars per token considered harmful](<../infra-platform/cost/Dollars per token considered harmful.md>) · `cost` · modal
  Critiques dollars-per-token as an inference cost metric and explains why workload shape, latency, and utilization matter more.
- **2025-07-02** — [How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work](<../evals-observability/evaluation/How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work.md>) · `evaluation` · modal
  Case study using evals and inference-time compute scaling to generate QR codes that satisfy visual and functional constraints.
- **2025-06-19** — [(LoRA) Fine-Tuning FLUX.1-dev on Consumer Hardware](<../models/fine-tuning/(LoRA) Fine-Tuning FLUX.1-dev on Consumer Hardware.md>) · `fine-tuning` · huggingface
  Fine-tunes FLUX.1-dev with QLoRA under ~10GB of VRAM on a single RTX 4090 using bitsandbytes NF4, 8-bit optimizers and gradient checkpointing, and compares FP8 training with torchao for extra speed on compatible hardware.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<../rag-retrieval/embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-04-29** — [Day zero benchmarks for Qwen 3 with SGLang on Baseten](<../models/benchmarks/Day zero benchmarks for Qwen 3 with SGLang on Baseten.md>) · `benchmarks` · baseten
  Provides day-zero Qwen 3 benchmarks with SGLang and discusses serving-performance implications.
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<../rag-retrieval/embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
- **2025-03-15** — [ThunderKittens Now Optimized for NVIDIA Blackwell GPUs](<hardware/ThunderKittens Now Optimized for NVIDIA Blackwell GPUs.md>) · `hardware` · together
  Describes ThunderKittens optimizations for NVIDIA Blackwell GPUs.
- **2025-03-12** — [Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM](<../models/releases/Welcome Gemma 3 Google's all new multimodal, multilingual, long context open LLM.md>) · `releases` · huggingface
  Gemma 3 (1B-27B) adds a SigLIP vision encoder, 128k context (32k for 1B), 140+ languages, and interleaved local/global attention to keep long-context KV cache tractable; covers benchmarks and official QAT quantized checkpoints.
- **2025-03-07** — [LLM Inference on Edge: A Fun and Easy Guide to run LLMs via React Native on your Phone!](<../infra-platform/edge/LLM Inference on Edge A Fun and Easy Guide to run LLMs via React Native on your Phone!.md>) · `edge` · huggingface
  End-to-end guide to building a React Native chat app that runs LLMs fully on-device via llama.rn/llama.cpp, covering how to pick mobile-viable models, what the GGUF quantization suffixes (Q2_K, Q4_K_M, Q8_0) actually trade off in size vs quality, and the Expo/native build plumbing.
- **2025-02-25** — [FastRTC: The Real-Time Communication Library for Python](<../product-engineering/architecture/FastRTC The Real-Time Communication Library for Python.md>) · `architecture` · huggingface
  FastRTC builds real-time voice/video AI apps in Python over WebRTC or WebSockets: built-in voice activity detection and turn-taking (ReplyOnPause), automatic Gradio UI, phone-call ingress, and mounting streams onto FastAPI.
- **2025-02-13** — [1 Billion Classifications](<../infra-platform/cost/1 Billion Classifications.md>) · `cost` · huggingface
  Works through the actual cost and latency math of running 1 billion text classifications with encoder models (gte-modernbert-base), comparing batch inference vs heavy-usage serving across hardware and optimizations (ONNX, TensorRT, quantization). Includes a reproducible encoder-analysis repo and per-configuration cost tables.
- **2025-02-07** — [DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical](<../models/reasoning/DeepSeek v3 and R1 Model Architecture Why it's powerful and economical.md>) · `reasoning` · fireworks
  Explains DeepSeek V3 and R1 architecture choices, including why the models are efficient for reasoning workloads.
- **2025-02-07** — [Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud](<../evals-observability/evaluation/Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud.md>) · `evaluation` · baseten
  Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark results.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<../infra-platform/deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2025-01-09** — [Driving model performance optimization: 2024 highlights](<optimization/Driving model performance optimization 2024 highlights.md>) · `optimization` · baseten
  Summarizes concrete model-performance optimization work across inference serving, batching, and hardware.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<optimization/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `optimization` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-12-18** — [Bamba: Inference-Efficient Hybrid Mamba2 Model](<../models/architectures/Bamba Inference-Efficient Hybrid Mamba2 Model.md>) · `architectures` · huggingface
  Bamba-9B is a hybrid Mamba2/transformer model trained by IBM, Princeton, CMU and UIUC on 2.2T tokens of fully open data, delivering 2.5x throughput and 2x lower latency than a comparable transformer in vLLM by shrinking the KV-cache memory-bandwidth bottleneck. Covers the hybrid architecture, training lineage, checkpoints and vLLM/transformers/llama.cpp enablement.
- **2024-12-09** — [20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds](<../models/multimodal/20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds.md>) · `multimodal` · fireworks
  Describes high-throughput Whisper transcription serving and the latency/cost tradeoffs in batch audio inference.
- **2024-10-30** — [Even Better, Even Faster Quantized LLMs with QTIP](<quantization/Even Better, Even Faster Quantized LLMs with QTIP.md>) · `quantization` · together
  Explains QTIP quantization for faster LLM inference with improved quality preservation.
- **2024-10-22** — [Deploying Speech-to-Speech on Hugging Face](<../infra-platform/deployment/Deploying Speech-to-Speech on Hugging Face.md>) · `deployment` · huggingface
  Deploys HF's cascaded speech-to-speech pipeline (VAD -> STT -> LLM -> TTS, 6 languages with auto-detect) as a custom Inference Endpoint, covering the handler and websocket/streaming plumbing needed to keep an interactive voice loop responsive.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-10-14** — [Linearizing LLMs with LoLCATs](<../models/reasoning/Linearizing LLMs with LoLCATs.md>) · `reasoning` · together
  Explains LoLCATs for linearizing LLM attention while preserving useful behavior.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-19** — [Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI](<../infra-platform/deployment/Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI.md>) · `deployment` · huggingface
  Step-by-step deployment of Llama 3.1 405B (FP8 quantized) on Google Cloud Vertex AI with Hugging Face TGI on an A3 8xH100 node: registering the model, endpoint config, and running online inference with 128k context.
- **2024-08-01** — [Introducing automatic LLM optimization with TensorRT-LLM Engine Builder](<optimization/Introducing automatic LLM optimization with TensorRT-LLM Engine Builder.md>) · `optimization` · baseten
  Describes automatic LLM optimization with TensorRT-LLM Engine Builder for production serving.
- **2024-07-23** — [Llama 3.1 - 405B, 70B & 8B with multilinguality and long context](<../models/releases/Llama 3.1 - 405B, 70B & 8B with multilinguality and long context.md>) · `releases` · huggingface
  Llama 3.1 8B/70B/405B: 128k context via a new RoPE scaling recipe, 15T-token training, and the accompanying Llama Guard 3 safety classifier and Prompt Guard jailbreak/prompt-injection detector; covers FP8/AWQ/GPTQ quantization needed to actually serve 405B, TGI deployment, and using 405B for synthetic data and LLM-as-judge.
- **2024-07-22** — [WWDC 24: Running Mistral 7B with Core ML](<../infra-platform/edge/WWDC 24 Running Mistral 7B with Core ML.md>) · `edge` · huggingface
  Reproduces Apple's WWDC'24 Mistral-7B Core ML demo: exporting a Swift-Transformers model, stateful KV cache, multifunction models for prefill vs extend, INT4 block-wise weight quantization, and running across CPU/GPU/ANE on Apple Silicon.
- **2024-07-11** — [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](<optimization/FlashAttention-3 Fast and Accurate Attention with Asynchrony and Low-precision.md>) · `optimization` · together
  Explains FlashAttention-3 and its asynchronous low-precision attention optimizations.
- **2024-06-04** — [How latent consistency models work](<../models/multimodal/How latent consistency models work.md>) · `multimodal` · baseten
  Explains latent consistency models and how they enable faster image generation.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<../infra-platform/deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-04-18** — [Streaming real-time text to speech with XTTS V2](<../models/multimodal/Streaming real-time text to speech with XTTS V2.md>) · `multimodal` · baseten
  Covers streaming real-time text-to-speech serving with XTTS v2.
- **2024-04-16** — [Running Privacy-Preserving Inferences on Hugging Face Endpoints](<../product-engineering/security/Running Privacy-Preserving Inferences on Hugging Face Endpoints.md>) · `security` · huggingface
  Shows how to serve Zama Concrete ML models under Fully Homomorphic Encryption on HF Inference Endpoints via custom inference handlers, so a spam classifier runs on ciphertext without ever seeing the plaintext message; also covers compiling your own FHE-friendly model.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-03-22** — [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](<../rag-retrieval/embeddings/Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval.md>) · `embeddings` · huggingface
  Binary (1-bit) and int8 scalar quantization of embeddings cuts retrieval memory/cost ~32x and ~4x while retaining ~92-96% of performance; covers rescoring with float embeddings and combining binary search + int8 rescoring in FAISS/usearch.
- **2024-03-15** — [CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG](<../rag-retrieval/embeddings/CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG.md>) · `embeddings` · huggingface
  Speeds up bge-base embeddings on Xeon CPUs by quantizing to int8 with Optimum Intel / IPEX, reporting latency and MTEB retrieval-quality deltas, then wires the optimized encoder into a fastRAG retrieval pipeline.
- **2024-03-14** — [33% faster LLM inference with FP8 quantization](<quantization/33% faster LLM inference with FP8 quantization.md>) · `quantization` · baseten
  Shows how FP8 quantization improves LLM inference throughput while managing accuracy and hardware constraints.
- **2024-03-14** — [Benchmarking fast Mistral 7B inference](<../evals-observability/evaluation/Benchmarking fast Mistral 7B inference.md>) · `evaluation` · baseten
  Benchmarks Mistral 7B inference performance and the serving choices that affect throughput and latency.
- **2024-03-12** — [High performance ML inference with NVIDIA TensorRT](<optimization/High performance ML inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains high-performance model inference with NVIDIA TensorRT and related deployment considerations.
- **2024-03-07** — [FP8: Efficient model inference with 8-bit floating point numbers](<quantization/FP8 Efficient model inference with 8-bit floating point numbers.md>) · `quantization` · baseten
  Explains FP8 numeric formats and why 8-bit floating point can improve efficient model inference.
- **2024-03-04** — [BASED: Simple linear attention language models balance the recall-throughput tradeoff](<../models/reasoning/BASED Simple linear attention language models balance the recall-throughput tradeoff.md>) · `reasoning` · together
  Explains BASED linear-attention language models and the recall-throughput tradeoff.
- **2024-02-20** — [BitDelta: Your Fine-Tune May Only Be Worth One Bit](<../models/fine-tuning/BitDelta Your Fine-Tune May Only Be Worth One Bit.md>) · `fine-tuning` · together
  Explains BitDelta and how small weight deltas can represent fine-tuned model changes.
- **2024-02-06** — [Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT](<optimization/Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT.md>) · `optimization` · baseten
  Shows how TensorRT unlocks H100 performance for model inference.
- **2024-01-16** — [Generation configurations: temperature, top-k, top-p, and test time compute](<../models/reasoning/Generation configurations temperature, top-k, top-p, and test time compute.md>) · `reasoning` · chip-huyen
  Explains decoding parameters such as temperature, top-k, top-p, and test-time compute, connecting generation configuration to reliability, diversity, latency, and cost.
- **2024-01-12** — [Understanding performance benchmarks for LLM inference](<../evals-observability/evaluation/Understanding performance benchmarks for LLM inference.md>) · `evaluation` · baseten
  Explains LLM inference performance benchmarks and how to interpret serving metrics.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-12-22** — [Faster Mixtral inference with TensorRT-LLM and quantization](<quantization/Faster Mixtral inference with TensorRT-LLM and quantization.md>) · `quantization` · baseten
  Shows how TensorRT-LLM and quantization improve Mixtral inference performance.
- **2023-12-08** — [StripedHyena-7B and efficient architectures beyond Transformers](<../models/reasoning/StripedHyena-7B and efficient architectures beyond Transformers.md>) · `reasoning` · together
  Introduces StripedHyena-7B and efficient architectures beyond Transformers.
- **2023-11-17** — [A guide to LLM inference and performance](<serving/A guide to LLM inference and performance.md>) · `serving` · baseten
  Comprehensive guide to LLM inference, transformer serving, latency, and throughput performance.
- **2023-11-02** — [Deployment and inference for open source text embedding models](<../rag-retrieval/embeddings/Deployment and inference for open source text embedding models.md>) · `embeddings` · baseten
  Covers deployment and inference patterns for open-source text embedding models.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-08-24** — [Skeleton of Thought: LLMs Can Do Parallel Decoding Paper Reading](<../models/reasoning/Skeleton of Thought LLMs Can Do Parallel Decoding Paper Reading.md>) · `reasoning` · arize
  Summarizes Skeleton of Thought and how parallel decoding can speed structured reasoning.
- **2023-07-25** — [Monarch Mixer: A new model architecture for increased efficiency](<../models/reasoning/Monarch Mixer A new model architecture for increased efficiency.md>) · `reasoning` · together
  Introduces Monarch Mixer as an efficient model architecture.
- **2023-07-17** — [FlashAttention-2 for faster training and inference](<optimization/FlashAttention-2 for faster training and inference.md>) · `optimization` · together
  Introduces FlashAttention-2 and its impact on training and inference speed.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
- **2023-03-29** — [Hungry Hungry Hippos (H3) and Language Modeling with State Space Models](<../models/reasoning/Hungry Hungry Hippos (H3) and Language Modeling with State Space Models.md>) · `reasoning` · arize
  Explains H3/state-space model ideas as alternatives to standard attention and why they matter for sequence modeling efficiency.
- **2023-01-23** — [FlashConv: speeding up state space models](<../models/reasoning/FlashConv speeding up state space models.md>) · `reasoning` · together
  Explains FlashConv and efficient state-space model execution.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.
