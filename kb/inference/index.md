# inference

130 articles.

- **2026-08-29** — [Agentic kernels in production](<kernels/Agentic kernels in production.md>) · `kernels` · baseten
  Baseten built a self-improving agentic framework that profiles production diffusion-model serving (Qwen-Image, FLUX.2 on B300 GPUs with SGLang), then generates, benchmarks, and ships GPU kernel optimizations like pre-packed FP8 scales directly into the serving stack, cutting end-to-end latency 42.3% on Qwen-Image, 15.2% on FLUX.2, and lifting throughput 5.5% on MiniMax M3.
- **2026-08-19** — [Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost (2026)](<optimization/Gisting Compressing LLM Agent context to ↑ throughput and ↓ cost (2026).md>) · `optimization` · shopify
  Shopify's Sidekick GraphQL agent uses gisting -- training special 'gist' token embeddings via knowledge distillation -- to compress its ~6,000-token system prompt to ~1,500 gist tokens (4:1), cutting median TTFT from 438ms to 354ms and end-to-end latency from 6.8s to 4.2s while raising throughput from 20.2 to 23.4 QPS at 350 RPM, reducing the GPUs needed to serve the agent.
- **2026-08-14** — [Inference engineering for DeepSeek V4 Pro 0813](<optimization/Inference engineering for DeepSeek V4 Pro 0813.md>) · `optimization` · baseten
  Baseten details the inference engineering behind serving DeepSeek V4 Pro 0813 (1.7T params, MXFP4 weights) day-zero: retuned parallelism, KV cache allocation, and prefill-decode worker ratios for longer agentic-coding sequences, plus speculative decoding via the model's built-in DSpark speculator for higher throughput.
- **2026-08-04** — [Bringing serverless functions closer to the speed of wire | Modal Blog](<optimization/Bringing serverless functions closer to the speed of wire Modal Blog.md>) · `optimization` · modal
  Modal rewrote its Function I/O plane in Go and deployed it across 4+ regions with a routing_region flag, cutting p50 end-to-end Function Call latency by ~80ms; also covers async offloading of non-critical work, JWT-based auth refresh, and sticking with Redis 7.1 over Valkey/Redis 7.2 after observing CPU spikes under load.
- **2026-07-31** — [Autoscaling endpoints for LLM inference](<optimization/Autoscaling endpoints for LLM inference.md>) · `optimization` · together
  Together AI details its dedicated-inference autoscaler (proportional control loop, asymmetric scale-up/scale-down windows) and compares 8 scaling metrics; an experiment replaying sine-wave + spike traffic under inflight_requests, ttft-p95, and gpu_utilization policies shows only the concurrency-based inflight_requests metric caught saturation, since continuous batching hid the problem from both TTFT and GPU-utilization signals.
- **2026-07-29** — [ThunderAgent: 2x Faster Agentic Inference for Synthetic Data Generation at Scale](<optimization/ThunderAgent 2x Faster Agentic Inference for Synthetic Data Generation at Scale.md>) · `optimization` · together
  Together AI's ThunderAgent (ICML 2026 Spotlight) fixes KV cache thrashing in high-concurrency agentic inference by scheduling at the program level instead of per-request: it pauses low-priority agent workflows under memory pressure and resumes them via a global waiting queue, achieving 803 vs 390 tok/s single-node throughput over SGLang and near-linear scaling to 2.4x speedup across 8 H100 nodes.
- **2026-07-27** — [Making Kimi K3 tokenization 18x faster for million-token agentic workloads](<optimization/Making Kimi K3 tokenization 18x faster for million-token agentic workloads.md>) · `optimization` · baseten
  Describes Baseten's Rust-based Basetenkenizer, built to replace a Python tiktoken implementation for Kimi K3's up-to-1M-token agentic inputs, correctly distinguishing literal control-token strings from structural chat-template tokens while running up to 18x faster than tiktoken with exact token-ID parity.
- **2026-07-27** — [How to build a day-0 API for Kimi K3](<serving/How to build a day-0 API for Kimi K3.md>) · `serving` · baseten
  Walks through Baseten's five milestones for standing up a day-0 inference API for the 2.8T-parameter Kimi K3 on NVIDIA GB300 NVL72 systems: bringing up vLLM/SGLang with native MXFP4 weights, validating fidelity with Moonshot's Kimi Vendor Verifier, sweeping TP/EP/ADP configs, applying speculation/disaggregation/caching, and scaling replicas with KV-aware routing for prefix cache hit rate.
- **2026-07-27** — [Kimi K3 by Moonshot now available on Modal | Modal Blog](<speculative-decoding/Kimi K3 by Moonshot now available on Modal Modal Blog.md>) · `speculative-decoding` · modal
  Modal details Day-0 serving of Kimi K3 with a custom DFlash speculator tuned to K3's architecture, trained on hidden states from 28 B300 nodes running K3 at TP8 against 4 training nodes, yielding 360% faster interactivity (100 to 460 tok/s) and 88% higher throughput; also notes Moonshot's MXFP4/MXFP8 quantization-aware training and a new KDA-compatible prefix-caching implementation contributed to vLLM.
- **2026-07-23** — [H100 vs. H200 GPUs](<hardware/H100 vs. H200 GPUs.md>) · `hardware` · baseten
  Compares H100 vs H200 SXM nodes for LLM serving: an 8x H100 node has 640GB VRAM versus 1,128GB for H200 (needed to fit models like GLM 5.2 at 744B params/~755GB FP8 on one node), and covers MIG partitioning for serving small models cheaply on fractional GPUs.
- **2026-07-23** — [How to optimize LLM inference speed and reduce costs in production](<optimization/How to optimize LLM inference speed and reduce costs in production.md>) · `optimization` · baseten
  Surveys production LLM inference optimization techniques -- continuous batching, speculative decoding, KV cache reuse, quantization, and smarter routing -- for cutting latency and cost when GPUs sit idle or repeat work.
- **2026-07-23** — [Bringing Nunchaku 4-bit Diffusion Inference to Diffusers](<quantization/Bringing Nunchaku 4-bit Diffusion Inference to Diffusers.md>) · `quantization` · huggingface
  Diffusers now natively loads Nunchaku's SVDQuant W4A4 checkpoints via from_pretrained() and the Hugging Face `kernels` package, requiring no local CUDA compilation; unlike weight-only quantization, SVDQuant runs transformer layers in 4-bit weights and activations, cutting both memory and denoising-loop latency.
- **2026-07-16** — [Real-time video generation inference on Baseten](<optimization/Real-time video generation inference on Baseten.md>) · `optimization` · baseten
  Details Baseten's real-time video inference runtime for Wan 2.2, combining four-step timestep distillation (~20x), custom kernel fusion (~1.5x), and NVFP4 quantization (~1.5x) for a combined 53.6x speedup, cutting per-clip generation from over two minutes to 2.75 seconds and cost from 5 cents to under a sixth of a cent.
- **2026-07-16** — [What does 99.9% uptime mean for inference?](<serving/What does 99.9% uptime mean for inference.md>) · `serving` · together
  Together breaks down what each reliability 'nine' actually requires for GPU inference serving, mapping failure domains (compute ECC errors, NIC/NVLink faults, storage, network, software/routing bugs) to the multi-region and AZ-redundancy architecture needed to survive them.
- **2026-07-15** — [Inkling by Thinking Machines now available on Modal | Modal Blog](<speculative-decoding/Inkling by Thinking Machines now available on Modal Modal Blog.md>) · `speculative-decoding` · modal
  Describes adapting Z Lab's DFlash block-diffusion speculator to Thinking Machines' Inkling (which uses five sliding-window attention layers per full-attention layer), making the drafter all-local-attention and causal for kernel support, reaching 250 tok/s/user at 2.5M TPM per GPU, 67% faster than Inkling's built-in MTP speculative path.
- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<kernels/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `kernels` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-06-30** — [Multi-token Residual Prediction](<speculative-decoding/Multi-token Residual Prediction.md>) · `speculative-decoding` · modal
  Explains multi-token residual prediction as an inference acceleration technique for generating multiple tokens per step.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-06-22** — [Best practices to accelerate inference for large-scale production workloads](<optimization/Best practices to accelerate inference for large-scale production workloads.md>) · `optimization` · together
  Best practices for accelerating inference in large-scale production workloads.
- **2026-06-22** — [Achieve state-of-the-art inference latencies with speculative decoding](<speculative-decoding/Achieve state-of-the-art inference latencies with speculative decoding.md>) · `speculative-decoding` · modal
  Explains speculative decoding for lower inference latency, including draft-model tradeoffs and production serving considerations.
- **2026-06-19** — [Speculation Is All You Need](<speculative-decoding/Speculation Is All You Need.md>) · `speculative-decoding` · modal
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
- **2026-05-08** — [DFlash: 3x faster LLM inference](<speculative-decoding/DFlash 3x faster LLM inference.md>) · `speculative-decoding` · baseten
  Explains DFlash as an optimization for faster LLM inference.
- **2026-05-04** — [Foundational research powering efficient inference at scale](<optimization/Foundational research powering efficient inference at scale.md>) · `optimization` · together
  Summarizes research lines behind efficient inference at production scale.
- **2026-04-24** — [Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding](<speculative-decoding/Accelerate RL rollouts by up to 50% with distribution-aware speculative decoding.md>) · `speculative-decoding` · together
  Explains distribution-aware speculative decoding for faster RL rollouts.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<kernels/Making FlashAttention-4 faster for inference.md>) · `kernels` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<kernels/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `kernels` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-05** — [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](<kernels/FlashAttention-4 Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling.md>) · `kernels` · together
  Covers FlashAttention-4 algorithm and kernel co-design for asymmetric hardware scaling.
- **2026-03-04** — [Cache-aware prefill-decode disaggregation for long-context LLM serving](<serving/Cache-aware prefill-decode disaggregation for long-context LLM serving.md>) · `serving` · together
  Explains cache-aware prefill/decode disaggregation for faster long-context LLM serving.
- **2026-02-19** — [Consistency diffusion language models: Up to 14x faster inference without sacrificing quality](<optimization/Consistency diffusion language models Up to 14x faster inference without sacrificing quality.md>) · `optimization` · together
  Explains consistency diffusion language models for faster inference without large quality loss.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<speculative-decoding/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `speculative-decoding` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2026-01-22** — [Optimizing inference speed and costs: Lessons learned from large-scale deployments](<optimization/Optimizing inference speed and costs Lessons learned from large-scale deployments.md>) · `optimization` · together
  Lessons from optimizing inference speed and cost in large-scale deployments.
- **2026-01-15** — [Open Responses: What you need to know](<serving/Open Responses What you need to know.md>) · `serving` · huggingface
  Argues Chat Completions is a poor fit for agentic workloads and proposes Open Responses, an open version of OpenAI's Responses API: stateless by default with encrypted reasoning, standardized model params, and provider-side agentic loops that execute tool calls before returning.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-11-12** — [Building world-class product search at Shopify: Where C++ excellence meets ML innovation (2025)](<serving/Building world-class product search at Shopify Where C++ excellence meets ML innovation (2025).md>) · `serving` · shopify
  How Shopify runs transformers, neural rankers, and gradient-boosted models (LightGBM, CatBoost) at native C++ speed for product search, meeting millisecond-latency-at-scale while keeping fast ML iteration.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-10-21** — [Engineering for Real-Time Voice Agent Latency](<serving/Engineering for Real-Time Voice Agent Latency.md>) · `serving` · cresta
  Technical discussion of latency in real-time voice agents and the engineering constraints behind responsive spoken interaction.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-10-10** — [ATLAS runtime-learning accelerators for LLM inference](<speculative-decoding/ATLAS runtime-learning accelerators for LLM inference.md>) · `speculative-decoding` · together
  Introduces ATLAS, a runtime-learning accelerator for improving LLM inference.
- **2025-09-29** — [Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models](<speculative-decoding/Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models.md>) · `speculative-decoding` · huggingface
  Accelerates a Qwen3-8B agent on Intel Core Ultra by ~1.3x using speculative decoding with a depth-pruned Qwen3-0.6B int8 draft model in OpenVINO GenAI, showing how draft-model depth pruning raises acceptance rate per unit of draft cost on client hardware.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<kernels/We reverse-engineered Flash Attention 4.md>) · `kernels` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-17** — [A postmortem of three recent issues](<serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-09-11** — [Tricks from OpenAI gpt-oss YOU 🫵 can use with transformers](<optimization/Tricks from OpenAI gpt-oss YOU 🫵 can use with transformers.md>) · `optimization` · huggingface
  Unpacks the optimizations shipped in transformers for OpenAI's gpt-oss and reusable by any model: zero-build kernels pulled from the Hub, MXFP4 quantization, tensor parallelism, expert parallelism, continuous batching and dynamic sliding-window caches.
- **2025-09-02** — [Make your ZeroGPU Spaces go brrr with ahead-of-time compilation](<kernels/Make your ZeroGPU Spaces go brrr with ahead-of-time compilation.md>) · `kernels` · huggingface
  Uses PyTorch ahead-of-time compilation (torch.export + AOTInductor) instead of just-in-time torch.compile so short-lived ZeroGPU processes keep the compiled artifact, giving 1.3x-1.8x speedups on Flux, Wan and LTX; also covers FP8 quantization, dynamic shapes and multi-compile for varying resolutions.
- **2025-08-18** — [From Zero to GPU: A Guide to Building and Scaling Production-Ready CUDA Kernels](<hardware/From Zero to GPU A Guide to Building and Scaling Production-Ready CUDA Kernels.md>) · `hardware` · huggingface
  End-to-end guide to writing a custom CUDA kernel and shipping it with HF's kernel-builder: Nix-based reproducible builds across multiple GPU architectures and torch ABIs, PyTorch op registration and torch.compile compatibility, and distribution via `get_kernel()` from the Hub instead of compiling at install time.
- **2025-08-14** — [More than Just a Model: How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency](<serving/More than Just a Model How Cresta Delivers Precise, Adaptable Summaries with Ultra-Low Latency.md>) · `serving` · cresta
  Explains production summarization architecture focused on low latency, adaptability, and precision rather than model choice alone.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-07-23** — [Fast LoRA inference for Flux with Diffusers and PEFT](<optimization/Fast LoRA inference for Flux with Diffusers and PEFT.md>) · `optimization` · huggingface
  Gets ~2.3x faster LoRA inference for Flux.1-Dev by combining LoRA hotswapping with torch.compile without recompilation — using peft's hotswap_adapter, max-rank padding so shapes stay static, and flags to avoid recompiles when adapters have different ranks and target layers. Also covers fusing/unfusing and FP8 quantization on top.
- **2025-06-18** — [Run FLUX.1-dev three times faster](<optimization/Run FLUX.1-dev three times faster.md>) · `optimization` · modal
  Explains optimizations for running FLUX.1-dev faster, including inference configuration and image-model serving tradeoffs.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-12** — [Learn the Hugging Face Kernel Hub in 5 Minutes](<kernels/Learn the Hugging Face Kernel Hub in 5 Minutes.md>) · `kernels` · huggingface
  Introduces the Kernel Hub: `get_kernel("kernels-community/activation")` downloads precompiled optimized CUDA kernels at runtime with no local build system, and the post benchmarks the drop-in kernels (activation, RMSNorm, Flash Attention) against native PyTorch.
- **2025-06-05** — [Model-Preserving Adaptive Rounding with YAQA](<quantization/Model-Preserving Adaptive Rounding with YAQA.md>) · `quantization` · together
  Explains YAQA, a model-preserving adaptive rounding approach for quantization.
- **2025-06-04** — [KV Cache from scratch in nanoVLM](<kernels/KV Cache from scratch in nanoVLM.md>) · `kernels` · huggingface
  Implements KV caching from scratch in nanoVLM, explaining prefill vs decode, how cached keys/values remove redundant attention recomputation, and the code changes to the attention block and generation loop; yields a 38% generation speedup.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-05-21** — [Exploring Quantization Backends in Diffusers](<quantization/Exploring Quantization Backends in Diffusers.md>) · `quantization` · huggingface
  Compares the quantization backends integrated in Diffusers — bitsandbytes (4-bit/8-bit/NF4), GGUF, torchao, Quanto and native FP8 — on Flux.1-dev, with memory-savings and quality trade-offs plus a blind test showing 8-bit differences are usually imperceptible. Includes code for combining quantization with torch.compile and CPU offloading.
- **2025-05-13** — [Blazingly fast whisper transcriptions with Inference Endpoints](<optimization/Blazingly fast whisper transcriptions with Inference Endpoints.md>) · `optimization` · huggingface
  An optimized Whisper deployment on Inference Endpoints built on vLLM, targeting Ada Lovelace GPUs (L4/L40s) to unlock torch.compile JIT kernels, CUDA graphs and a float8 KV cache — with the resulting latency/throughput gains for transcription workloads.
- **2025-05-12** — [Boosting DeepSeek-R1 speed with customized speculative decoding](<speculative-decoding/Boosting DeepSeek-R1 speed with customized speculative decoding.md>) · `speculative-decoding` · together
  Shows customized speculative decoding for accelerating DeepSeek-R1 serving.
- **2025-04-28** — [Optimizing Llama 4 Maverick on Fireworks](<optimization/Optimizing Llama 4 Maverick on Fireworks.md>) · `optimization` · fireworks
  Details how Fireworks served Llama 4 Maverick within minutes of weight release using FireOptimizer-tuned FP8 quantization, tensor+expert parallelism, a custom FireAttention kernel extended for Maverick's chunked local attention, and a trained speculative-decoding drafter, reaching 145 tok/s on H200 (10-20% faster than the nearest competitor per Artificial Analysis).
- **2025-04-21** — [Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas](<kernels/Chipmunk Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas.md>) · `kernels` · together
  Describes Chipmunk, a training-free acceleration method for diffusion transformers.
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-03-15** — [ThunderKittens Now Optimized for NVIDIA Blackwell GPUs](<hardware/ThunderKittens Now Optimized for NVIDIA Blackwell GPUs.md>) · `hardware` · together
  Describes ThunderKittens optimizations for NVIDIA Blackwell GPUs.
- **2025-03-13** — [Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence](<serving/Understanding Cresta’s Voice Platform - ML Services, Inference Graphs, and Real-Time Intelligence.md>) · `serving` · cresta
  Explains ML services, inference graphs, and real-time intelligence components in a production voice platform.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2024-12-19** — [A quick introduction to speculative decoding](<speculative-decoding/A quick introduction to speculative decoding.md>) · `speculative-decoding` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<speculative-decoding/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `speculative-decoding` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-11-20** — [Faster Text Generation with Self-Speculative Decoding](<speculative-decoding/Faster Text Generation with Self-Speculative Decoding.md>) · `speculative-decoding` · huggingface
  LayerSkip self-speculative decoding: the same model drafts with early-exit at an intermediate layer and verifies with the remaining layers, reusing the KV cache so no separate draft model or extra memory is needed; includes speedups on Llama checkpoints trained with layer dropout + early-exit loss.
- **2024-10-30** — [Even Better, Even Faster Quantized LLMs with QTIP](<quantization/Even Better, Even Faster Quantized LLMs with QTIP.md>) · `quantization` · together
  Explains QTIP quantization for faster LLM inference with improved quality preservation.
- **2024-10-29** — [Universal Assisted Generation: Faster Decoding with Any Assistant Model](<speculative-decoding/Universal Assisted Generation Faster Decoding with Any Assistant Model.md>) · `speculative-decoding` · huggingface
  Universal Assisted Generation (Intel Labs + HF) lifts speculative decoding's requirement that the draft model share the target's tokenizer by re-encoding draft tokens between vocabularies, giving 1.5x-2x speedups for models like gemma-2-9b and Mixtral-8x22B that have no small same-family draft model.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-10-08** — [Faster Assisted Generation with Dynamic Speculation](<speculative-decoding/Faster Assisted Generation with Dynamic Speculation.md>) · `speculative-decoding` · huggingface
  Dynamic speculative decoding (Intel Labs + HF, default in Transformers 4.45) adapts the speculation lookahead per iteration instead of using a fixed number of draft tokens, giving up to 2.7x faster assisted generation depending on task while preserving the target model's output.
- **2024-09-18** — [Fine-tuning LLMs to 1.58bit: extreme quantization made easy](<quantization/Fine-tuning LLMs to 1.58bit extreme quantization made easy.md>) · `quantization` · huggingface
  Shows how to fine-tune an existing Llama3-8B/SmolLM into BitNet's 1.58-bit ternary ({-1,0,1}) weight format instead of pre-training from scratch, using BitLinear layers, a lambda-scheduled quantization warmup and per-row/per-tensor scaling. Reports pre-training and fine-tuning results plus custom kernel benchmarks.
- **2024-09-16** — [Boost your throughput with dynamic batching](<optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-09-05** — [Speculative decoding for high-throughput long-context inference](<speculative-decoding/Speculative decoding for high-throughput long-context inference.md>) · `speculative-decoding` · together
  Explains speculative decoding for high-throughput long-context inference.
- **2024-08-28** — [TEAL: Training-Free Activation Sparsity in Large Language Models](<optimization/TEAL Training-Free Activation Sparsity in Large Language Models.md>) · `optimization` · together
  Explains TEAL, a training-free activation sparsity method for large language models.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<speculative-decoding/How to double tokens per second for Llama 3 with Medusa.md>) · `speculative-decoding` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-13** — [Introduction to ggml](<kernels/Introduction to ggml.md>) · `kernels` · huggingface
  A hands-on introduction to ggml — the C/C++ tensor library behind llama.cpp, whisper.cpp, ollama and LM Studio — covering its context/graph memory model, GGUF file format, quantized tensor types, and backend dispatch (CPU/CUDA/Metal) via a worked matrix-multiplication example.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-07-30** — [Memory-efficient Diffusion Transformers with Quanto and Diffusers](<quantization/Memory-efficient Diffusion Transformers with Quanto and Diffusers.md>) · `quantization` · huggingface
  Quantizes diffusion-transformer pipelines (PixArt-Sigma, SD3, Flux) with Quanto: int8/fp8/int4 on the transformer and T5 text encoders cuts SD3 inference memory from 18.8GB FP16 toward consumer-GPU range, with per-component memory/latency/quality tradeoffs and gotchas.
- **2024-07-23** — [How to serve 10,000 fine-tuned LLMs from a single GPU](<serving/How to serve 10,000 fine-tuned LLMs from a single GPU.md>) · `serving` · baseten
  Explains serving many fine-tuned LLM adapters from a single GPU with efficient multiplexing.
- **2024-07-18** — [TGI Multi-LoRA: Deploy Once, Serve 30 Models](<serving/TGI Multi-LoRA Deploy Once, Serve 30 Models.md>) · `serving` · huggingface
  Explains TGI's multi-LoRA serving: load one base model plus up to ~30 LoRA adapters in a single deployment, batching requests for different adapters together via a gathered/segmented matmul so per-adapter overhead is small. Argues the cost and ops case for many specialized adapters over many full deployments, with latency numbers vs single-adapter serving.
- **2024-07-11** — [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](<kernels/FlashAttention-3 Fast and Accurate Attention with Asynchrony and Low-precision.md>) · `kernels` · together
  Explains FlashAttention-3 and its asynchronous low-precision attention optimizations.
- **2024-07-11** — [Using asynchronous inference in production](<serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<speculative-decoding/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `speculative-decoding` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<kernels/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `kernels` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-06-18** — [SpecExec: Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices](<speculative-decoding/SpecExec Massively Parallel Speculative Decoding for Interactive LLM Inference on Consumer Devices.md>) · `speculative-decoding` · together
  Introduces SpecExec for massively parallel speculative decoding on consumer devices.
- **2024-05-29** — [Benchmarking Text Generation Inference](<serving/Benchmarking Text Generation Inference.md>) · `serving` · huggingface
  How to use the TGI benchmarking tool to profile LLM serving: separating prefill from decode, reading latency vs throughput curves under different batch sizes, and choosing the batch size that meets your latency SLO.
- **2024-05-03** — [Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face](<serving/Bringing the Artificial Analysis LLM Performance Leaderboard to Hugging Face.md>) · `serving` · huggingface
  The Artificial Analysis LLM Performance Leaderboard benchmarks hosted inference endpoints (not model quality) on throughput tokens/s, time-to-first-token, and price per token across providers, arguing latency is the limiting factor for agentic/tool-use systems where sequential LLM calls compound.
- **2024-05-01** — [Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints](<serving/Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints.md>) · `serving` · huggingface
  Walks through a custom Inference Endpoints handler that chains Whisper-large-v3 ASR, Pyannote diarization and speculative decoding (with a distil-whisper assistant model and SDPA/Flash Attention 2) into one deployable pipeline, including the pre/post-processing needed to align transcript timestamps with speaker turns.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-04-03** — [Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon](<quantization/Blazing Fast SetFit Inference with 🤗 Optimum Intel on Xeon.md>) · `quantization` · huggingface
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
- **2023-11-13** — [FlashFFTConv: Efficient Convolutions for Long Sequences with Tensor Cores](<kernels/FlashFFTConv Efficient Convolutions for Long Sequences with Tensor Cores.md>) · `kernels` · together
  Explains FlashFFTConv for efficient long-sequence convolutions on tensor cores.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-10-12** — [Flash-Decoding for long-context inference](<kernels/Flash-Decoding for long-context inference.md>) · `kernels` · together
  Introduces Flash-Decoding for efficient long-context inference.
- **2023-10-11** — [Accelerating Code Completion with Fireworks Fast LLM Inference](<optimization/Accelerating Code Completion with Fireworks Fast LLM Inference.md>) · `optimization` · fireworks
  Sourcegraph's Cody code-completion integrated Fireworks-served StarCoder, raising Completion Acceptance Rate from 15% to 30% and cutting multi-line latency from 3.4s to 2.4s; Fireworks reports 3.5x+ lower latency than vLLM across batch sizes on 8xA100 via multi-query attention and PyTorch runtime optimizations.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-09-11** — [Medusa: Simple framework for accelerating LLM generation with multiple decoding heads](<speculative-decoding/Medusa Simple framework for accelerating LLM generation with multiple decoding heads.md>) · `speculative-decoding` · together
  Introduces Medusa, a multi-decoding-head framework for accelerating LLM generation.
- **2023-08-30** — [SDXL inference in under 2 seconds](<optimization/SDXL inference in under 2 seconds.md>) · `optimization` · baseten
  Guide to Stable Diffusion XL inference optimization for sub-2-second image generation.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<kernels/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `kernels` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-17** — [FlashAttention-2 for faster training and inference](<kernels/FlashAttention-2 for faster training and inference.md>) · `kernels` · together
  Introduces FlashAttention-2 and its impact on training and inference speed.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.

## Also relevant (filed elsewhere)

- **2026-08-28** — [GLM-5.3 vs. GLM-5.3 Flash on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/GLM-5.3 vs. GLM-5.3 Flash on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  Benchmarks GLM-5.3 against its distilled GLM-5.3 Flash sibling on 900 DeepSWE rollouts: a Flash-first, escalate-on-test-failure cascade solves 80.9% of tasks at $1.70 vs. the full model's 69.0% at $3.99, showing distillation mainly cost first-try reliability (recoverable via retries) rather than ceiling capability, at 17x lower per-rollout price.
- **2026-08-28** — [GLM 5.3: Scaling with post-training, intuitively explained](<../models/reinforcement-learning/GLM 5.3 Scaling with post-training, intuitively explained.md>) · `reinforcement-learning` · baseten
  Explains how GLM-5.3 improved over 50% on the identical GLM-5.2 base purely through scaled RL post-training: agent-generated environments verified by reward-hacking-resistant checks, SAO (Single-Rollout Asynchronous Optimization) with trajectory compaction for stable long-horizon RL, and a slime-based pipeline pairing SGLang rollout generation with Megatron training; also covers GLM 5.2's Multi-head Latent Attention, DeepSeek Sparse Attention, MTP speculative decoding, and the IndexShare optimization that cuts indexer FLOPs 2.9x.
- **2026-08-26** — [DeepSeek V4 Pro: Tops SWE-Bench & Cuts Cost per Task by 3x vs. Fable 5](<../models/benchmarks/DeepSeek V4 Pro Tops SWE-Bench & Cuts Cost per Task by 3x vs. Fable 5.md>) · `benchmarks` · fireworks
  Benchmarks DeepSeek V4 Pro 0813 against Kimi K3 and Fable 5 on SWE-Bench Verified, LiveCodeBench v6, Aider Polyglot, and Terminal-Bench 2.1, finding it tops two of four families at roughly a third of Fable 5's per-task cost, though it trails badly on Java (48.9% vs 74.5%), arguing for dynamic routing across specialist models.
- **2026-08-26** — [Post-training Kimi K3 with Harvey for long-horizon legal work](<../models/reinforcement-learning/Post-training Kimi K3 with Harvey for long-horizon legal work.md>) · `reinforcement-learning` · fireworks
  Harvey and Fireworks post-trained a Kimi K3 base into "Tenet" using asynchronous reinforcement learning on the Fireworks Training API, nearly doubling all-pass rate on the Legal Agent Benchmark (19.7% vs 10.8% for base Kimi K3) at roughly flat cost ($5.92 vs $5.62/task); gains transferred to unseen agentic benchmarks (Mercor Apex Agents, Crosby Redline Bench) with no regression on legal-knowledge benchmarks like LegalBench, CUAD, and MAUD.
- **2026-08-25** — [How to run any open model inside DeepSeek Harness](<../agents/harness/How to run any open model inside DeepSeek Harness.md>) · `harness` · baseten
  Describes DeepSeek Harness (DSH) as a plugin-based meta-harness where models, tools, sandboxes, and sub-agent harnesses (Claude Code, Codex) are swappable components with an append-only, fork-and-replay event log, and walks through wiring open models like Kimi K3, GLM 5.2, and DeepSeek V4 Pro into it via Baseten Model APIs.
- **2026-08-25** — [The two AI gateway patterns in production inference](<../product-engineering/architecture/The two AI gateway patterns in production inference.md>) · `architecture` · baseten
  Distinguishes two AI gateway architectures — access gateways for application-side multi-provider routing vs. serving gateways for model owners exposing their own models to customers — and traces how a serving gateway handles identity, routing, tenant protection, metering, and auditable request logs.
- **2026-08-24** — [How leading platforms ensure observability for LLM inference](<../evals-observability/monitoring/How leading platforms ensure observability for LLM inference.md>) · `monitoring` · baseten
  Explains LLM inference observability through three lenses: metrics (TTFT, TPOT, TPS, end-to-end latency, KV cache hit rate), build/deploy/serving logs keyed by request_id, and distributed traces that break a single request into API Gateway, Service Mesh, Activator, Queue, and Server stages to pinpoint cold-start and queue-backup latency.
- **2026-08-21** — [How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers with Code](<../rag-retrieval/search/How Hugging Face Inference Endpoints, Jobs, and Buckets Power Search on Papers with Code.md>) · `search` · huggingface
  Details the hybrid search architecture behind Papers with Code: an offline Jobs pipeline embeds papers with Qwen3-Embedding into a versioned pgvector contract (HNSW, 0.9955 Recall@20 at 256 dims), while online queries fuse lexical and semantic branches via weighted RRF and fall back to full-text search if the Inference Endpoint is cold or unhealthy.
- **2026-08-18** — [DeepSeek V4 Pro 0813 vs GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/DeepSeek V4 Pro 0813 vs GPT-5.6 Sol on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  Benchmarks DeepSeek V4 Pro 0813 against GPT-5.6 Sol on 113 DeepSWE coding tasks (904 rollouts): Sol wins pass@1 (72.7% vs 62.8%) but Pro's pass@4 (88.5% vs 85.8%) overtakes it at 1/35th the per-rollout cost, and a Pro-first-escalate-to-Sol cascade solves 83.0% of tasks at $3.35 each versus Sol alone at 72.7% for $8.37, though Sol's failures regress passing tests more often (20% vs 11%).
- **2026-08-17** — [DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  Benchmarks DeepSeek V4 Pro 0813 against Claude Fable 5 on 113 DeepSWE coding tasks (904 rollouts): Fable leads pass@1 (69.7% vs 62.8%) but Pro catches up by pass@4 (88.5% vs 84.1%) at 1/90th the per-rollout cost, and a Pro-first-escalate-to-Fable cascade solves 82.7% of tasks at $8.28 each, beating Fable alone (69.7% at $21.63) and even a perfect oracle router (78.8%).
- **2026-08-17** — [A/B test models in production](<../infra-platform/deployment/AB test models in production.md>) · `deployment` · together
  Explains Together AI's endpoint-level A/B testing for production model traffic: one control plus up to 20 variants with fixed percentage splits independent of replica autoscaling, etag-guarded ramping, sampling-key-based cohort stickiness, and promote-then-delete rollout to end an experiment. Walks through a live run ramping 95/5 to 80/20 to 50/50 and shows observed traffic shares matching the configured percents.
- **2026-08-11** — [Introducing NVIDIA Nemotron 3.5 Lightning](<../models/releases/Introducing NVIDIA Nemotron 3.5 Lightning.md>) · `releases` · baseten
  NVIDIA Nemotron 3.5 Lightning is a 30B MoE model (3B active) distilled from Nemotron 3 Ultra for agentic workloads, achieving ~4x higher throughput and 30% lower task completion time than comparable open models, now available on Baseten Dedicated Inference.
- **2026-08-06** — [DeepSeek-V4 Flash 0731 vs GPT-5.6 Luna on DeepSWE: Cost and Coding](<../models/benchmarks/DeepSeek-V4 Flash 0731 vs GPT-5.6 Luna on DeepSWE Cost and Coding.md>) · `benchmarks` · together
  Benchmarks DeepSeek-V4 Flash 0731 against GPT-5.6 Luna on all 113 DeepSWE coding tasks (900 rollouts): Luna leads pass@1 67.2% vs 53.3% but costs 6x more ($0.61 vs $0.10/rollout); shows a DeepSeek-first cascade that escalates to Luna only on failure solves 78.9% of tasks at $0.385 each, beating Luna alone on both accuracy and cost.
- **2026-08-04** — [Introducing NVIDIA Nemotron 3.5 ASR Streaming](<../models/releases/Introducing NVIDIA Nemotron 3.5 ASR Streaming.md>) · `releases` · baseten
  Baseten benchmarks NVIDIA's Nemotron 3.5 ASR streaming models (a 600M-parameter cache-aware FastConformer-RNNT architecture) on H100s, sustaining 100 concurrent WebSocket streams with 98-138ms finalization latency, 8.84% average WER across 19 languages, and 2.32% WER on LibriSpeech Clean for the English-only variant.
- **2026-07-31** — [Fine-tuning Qwen3-TTS for high-quality voice cloning](<../models/fine-tuning/Fine-tuning Qwen3-TTS for high-quality voice cloning.md>) · `fine-tuning` · baseten
  Baseten details a fine-tuning recipe for Qwen3-TTS voice cloning: an ASR-driven pipeline for building utterance-level (audio, text) pairs, talker/sub-talker cross-entropy loss over 12 RVQ codebook frames/sec, a centroid speaker embedding averaged over 64 clips, and warmup+cosine LR decay, trained in ~1 hour on a single H100 for 8 epochs on 1.5 hours of LJ Speech audio, reaching ~130ms TTFA (vs ~154ms for ICL cloning).
- **2026-07-26** — [Kimi K3 vs GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/Kimi K3 vs GPT-5.6 Sol on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  Analyzes 904 graded DeepSWE rollouts comparing Kimi K3 and GPT-5.6 Sol: Sol leads pass@1 72.7% to 68.5%, but Kimi K3 wins pass@4 (89.4% vs 85.8%) at 64% lower cost ($4.65 vs $8.37 per rollout). With only 0.46 task-level correlation between the two models, a Kimi-first cascade that escalates to Sol on test failure covers 108/113 tasks (~85.6%), beating both single models and a perfect one-shot router.
- **2026-07-20** — [Heidi x Fireworks: Bridging the Gap in Frontier Model Performance](<../models/fine-tuning/Heidi x Fireworks Bridging the Gap in Frontier Model Performance.md>) · `fine-tuning` · fireworks
  Heidi's clinical-note scribe moved from closed frontier models to a two-stage pipeline (SFT to imitate style, then RFT/DPO for preference-based quality) on Fireworks, cutting latency from 25s to 7s and outperforming Gemini Flash/Pro tiers in side-by-side evals; success depended on high-quality filtered data and larger effective batch sizes.
- **2026-07-16** — [Fast, accurate retrieval with NVIDIA Nemotron 3 Embed](<../rag-retrieval/embeddings/Fast, accurate retrieval with NVIDIA Nemotron 3 Embed.md>) · `embeddings` · baseten
  Compares NVIDIA's Nemotron 3 Embed 8B and 1B embedding models available on Baseten: the 1B model uses pruning, distillation, and NVFP4 quantization to retain 95% of the 8B's retrieval accuracy (99% in NVFP4 on Blackwell, 2x throughput) while cutting indexing latency and serving cost; also covers a fine-tuning recipe yielding ~10% accuracy gains in 5 hours.
- **2026-07-15** — [Together AI brings Thinking Machines Lab’s new model Inkling on day 0](<../models/architectures/Together AI brings Thinking Machines Lab’s new model Inkling on day 0.md>) · `architectures` · together
  Details Inkling's architecture (975B/40B active MoE with a shared expert sink jointly normalized against routed experts, a learned query-conditioned relative attention bias instead of RoPE, and 'sconv' short causal convolutions on K/V and sublayer outputs) and Together's FlashAttention-4-based kernel adapted to serve its query-conditioned relative attention efficiently.
- **2026-07-06** — [How to price serverless GPUs](<../infra-platform/cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-06-26** — [Fireworks AI](<../models/reinforcement-learning/Fireworks AI.md>) · `reinforcement-learning` · fireworks
  Cursor's Composer 2, built on Kimi 2.5, is trained via continual pretraining and large-scale RL on long-horizon software engineering tasks; Fireworks provides distributed rollout/inference infra across 3-4 clusters with compressed weight sync, hitting 61.3 CursorBench and 6-10x lower inference cost than comparable frontier coding models.
- **2026-06-25** — [Live draft model training for speculative decoding](<../models/fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
- **2026-06-23** — [ParallelKernelBench: Frontier LLMs can't write fast multi-GPU kernels (yet)](<../evals-observability/benchmark-design/ParallelKernelBench Frontier LLMs can't write fast multi-GPU kernels (yet).md>) · `benchmark-design` · together
  Introduces ParallelKernelBench for measuring whether frontier LLMs can write fast multi-GPU kernels.
- **2026-06-12** — [MiniMax M3 is live: long context + native multimodality at 1/20th the price](<../models/architectures/MiniMax M3 is live long context + native multimodality at 120th the price.md>) · `architectures` · fireworks
  MiniMax M3's extended context comes from MSA (MiniMax Sparse Attention), which pre-filters and blocks KV caches with a 'KV outer gather Q' operator ordering that fetches each block once, delivering >4x speedup over Flash-Sparse-Attention/flash-moba, 95% lower per-token compute, and 9x/15x faster prefill/decode at 1M-token context versus M2.7.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<../infra-platform/deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-05-29** — [How Together AI built a fast speech-to-text stack](<../models/multimodal/How Together AI built a fast speech-to-text stack.md>) · `multimodal` · together
  Engineering writeup on building a fast speech-to-text stack.
- **2026-05-29** — [Timestep distillation: 2.5x faster FLUX.2 image generation](<../models/multimodal/Timestep distillation 2.5x faster FLUX.2 image generation.md>) · `multimodal` · baseten
  Explains timestep distillation for faster FLUX.2 image generation.
- **2026-05-27** — [Reachy Mini goes fully local](<../infra-platform/edge/Reachy Mini goes fully local.md>) · `edge` · huggingface
  Runs a full cascaded voice stack (VAD -> STT -> LLM -> TTS) locally on-device behind an OpenAI-Realtime-API-compatible /v1/realtime WebSocket, replacing the cloud backend for the Reachy Mini robot; argues cascades beat end-to-end S2S models on flexibility and latency and shows which local components to swap in.
- **2026-05-19** — [Benchmarking inference at scale: coding agents](<../evals-observability/benchmark-design/Benchmarking inference at scale coding agents.md>) · `benchmark-design` · together
  Benchmarks inference at scale for coding-agent workloads.
- **2026-05-14** — [Cost-efficient, high-performance TTS with Qwen3-TTS](<../models/multimodal/Cost-efficient, high-performance TTS with Qwen3-TTS.md>) · `multimodal` · baseten
  Describes cost-efficient high-performance Qwen3-TTS serving for text-to-speech workloads.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [How we achieved truly serverless GPUs](<../infra-platform/gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-24** — [DeepSeek-V4: a million-token context that agents can actually use](<../models/architectures/DeepSeek-V4 a million-token context that agents can actually use.md>) · `architectures` · huggingface
  Breaks down how DeepSeek-V4's architecture makes 1M-token context cheap for agents: V4-Pro needs 27% of V3.2's single-token inference FLOPs and 10% of its KV cache (V4-Flash: 10% and 7%, roughly 2% of an 8-head GQA bf16 cache), plus the agent-specific post-training decisions that build on it.
- **2026-04-15** — [Parcae: Doing more with fewer parameters using stable looped models](<../models/reasoning/Parcae Doing more with fewer parameters using stable looped models.md>) · `reasoning` · together
  Explains stable looped models for doing more with fewer parameters.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<../models/fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<../infra-platform/deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-03-17** — [Mamba-3](<../models/reasoning/Mamba-3.md>) · `reasoning` · together
  Describes Mamba-3 and its implications for efficient sequence modeling.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<../models/reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2026-02-17** — [Is Your Python Web Framework Really the Performance Bottleneck? | Pydantic Logfire](<../product-engineering/architecture/Is Your Python Web Framework Really the Performance Bottleneck Pydantic Logfire.md>) · `architecture` · pydantic
  Argues Python web-framework micro-benchmarks mislead: within a real request, database calls, serialization, and downstream I/O usually dominate, so framework choice is rarely the actual latency bottleneck—use tracing to find the real one.
- **2026-02-09** — [AI Model Performance Metrics Explained](<../evals-observability/monitoring/AI Model Performance Metrics Explained.md>) · `monitoring` · baseten
  Explains model performance metrics used in production inference, including latency, throughput, and quality signals.
- **2026-02-05** — [How to run LLM performance benchmarks (and why you should)](<../evals-observability/benchmark-design/How to run LLM performance benchmarks (and why you should).md>) · `benchmark-design` · baseten
  Explains how to run LLM performance benchmarks and which serving metrics matter.
- **2026-01-26** — [Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT](<../models/reinforcement-learning/Kimi K2.5 Is Live on Fireworks Vibe Coding, Agents, and Full-Parameter RFT.md>) · `reinforcement-learning` · fireworks
  Fireworks' full-parameter RL tuning preview for Kimi K2.5 exposes Tinker-API-compatible low-level primitives (forward, forward_backward, optimizer_step) while handling distributed training, cross-region trainer/sampler deployment with seamless weight transfer, and customizable GRPO/reward-shaping loss.
- **2026-01-26** — [How shredding JSON is giving Logfire 1000x query speedups](<../product-engineering/architecture/How shredding JSON is giving Logfire 1000x query speedups.md>) · `architecture` · pydantic
  How Logfire 'shreds' nested JSON attributes into typed columns in its columnar store for up to 1000x query speedups—turning 30s-timeout queries into sub-second—covering schema inference and dynamic column materialization.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<../infra-platform/gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-12-17** — [When Every Word Matters: Engineering Real-Time Multilingual Intelligence for Human Conversations](<../models/multimodal/When Every Word Matters Engineering Real-Time Multilingual Intelligence for Human Conversations.md>) · `multimodal` · cresta
  Engineering guide to real-time multilingual intelligence for conversations, focusing on latency and speech-language quality.
- **2025-12-15** — [NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents](<../models/architectures/NVIDIA Nemotron 3 Nano on Fireworks The Engine for Next-Generation AI Agents.md>) · `architectures` · fireworks
  NVIDIA Nemotron 3 Nano is a 30B MoE (3B active) hybrid Mamba-Transformer with 23 Mamba-2/MoE layers, 6 attention layers, 128 experts (5 active) plus a shared expert, and a token 'thinking budget' to cap reasoning-token generation; a cookbook demonstrates a chunk-then-synthesize strategy for summarizing large source files.
- **2025-12-02** — [Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks](<../models/architectures/Unlock Advanced Reasoning with NVIDIA Nemotron Nano 2 Models on Fireworks.md>) · `architectures` · fireworks
  NVIDIA Nemotron Nano 2 uses a hybrid Mamba-Transformer design where only ~8% of layers use quadratic-cost self-attention (placed where long-range links matter) and the rest use constant-cost Mamba-2/FFN blocks, giving transformer-level accuracy with much lower compute and stable memory for long-context reasoning.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models, speculative decoding, and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-27** — [Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks](<../models/multimodal/Accelerate your Vision Pipelines with the new NVIDIA Nemotron Nano 2 VL Model on Fireworks.md>) · `multimodal` · fireworks
  NVIDIA Nemotron Nano2 VL combines the hybrid Mamba-Transformer Nemotron LLM with a CRADIOH-V2 vision encoder and video token compression; in an invoice-processing benchmark on Fireworks it hit 90%+ extraction accuracy on fields like invoice number and date via semantic (not pure-OCR) document understanding.
- **2025-08-21** — [AI agents for efficient LLM inference engineering](<../agents/tool-use/AI agents for efficient LLM inference engineering.md>) · `tool-use` · together
  Case study of using AI agents to automate engineering tasks while developing efficient inference systems.
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
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<../rag-retrieval/embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<../rag-retrieval/embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
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
- **2025-02-07** — [Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud](<../evals-observability/benchmark-design/Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud.md>) · `benchmark-design` · baseten
  Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark results.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<../infra-platform/deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2024-12-18** — [Bamba: Inference-Efficient Hybrid Mamba2 Model](<../models/architectures/Bamba Inference-Efficient Hybrid Mamba2 Model.md>) · `architectures` · huggingface
  Bamba-9B is a hybrid Mamba2/transformer model trained by IBM, Princeton, CMU and UIUC on 2.2T tokens of fully open data, delivering 2.5x throughput and 2x lower latency than a comparable transformer in vLLM by shrinking the KV-cache memory-bandwidth bottleneck. Covers the hybrid architecture, training lineage, checkpoints and vLLM/transformers/llama.cpp enablement.
- **2024-10-22** — [Deploying Speech-to-Speech on Hugging Face](<../infra-platform/deployment/Deploying Speech-to-Speech on Hugging Face.md>) · `deployment` · huggingface
  Deploys HF's cascaded speech-to-speech pipeline (VAD -> STT -> LLM -> TTS, 6 languages with auto-detect) as a custom Inference Endpoint, covering the handler and websocket/streaming plumbing needed to keep an interactive voice loop responsive.
- **2024-10-14** — [Linearizing LLMs with LoLCATs](<../models/reasoning/Linearizing LLMs with LoLCATs.md>) · `reasoning` · together
  Explains LoLCATs for linearizing LLM attention while preserving useful behavior.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-19** — [Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI](<../infra-platform/deployment/Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI.md>) · `deployment` · huggingface
  Step-by-step deployment of Llama 3.1 405B (FP8 quantized) on Google Cloud Vertex AI with Hugging Face TGI on an A3 8xH100 node: registering the model, endpoint config, and running online inference with 128k context.
- **2024-07-23** — [Llama 3.1 - 405B, 70B & 8B with multilinguality and long context](<../models/releases/Llama 3.1 - 405B, 70B & 8B with multilinguality and long context.md>) · `releases` · huggingface
  Llama 3.1 8B/70B/405B: 128k context via a new RoPE scaling recipe, 15T-token training, and the accompanying Llama Guard 3 safety classifier and Prompt Guard jailbreak/prompt-injection detector; covers FP8/AWQ/GPTQ quantization needed to actually serve 405B, TGI deployment, and using 405B for synthetic data and LLM-as-judge.
- **2024-07-22** — [WWDC 24: Running Mistral 7B with Core ML](<../infra-platform/edge/WWDC 24 Running Mistral 7B with Core ML.md>) · `edge` · huggingface
  Reproduces Apple's WWDC'24 Mistral-7B Core ML demo: exporting a Swift-Transformers model, stateful KV cache, multifunction models for prefill vs extend, INT4 block-wise weight quantization, and running across CPU/GPU/ANE on Apple Silicon.
- **2024-06-04** — [How latent consistency models work](<../models/multimodal/How latent consistency models work.md>) · `multimodal` · baseten
  Explains latent consistency models and how they enable faster image generation.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<../infra-platform/deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-04-18** — [Streaming real-time text to speech with XTTS V2](<../models/multimodal/Streaming real-time text to speech with XTTS V2.md>) · `multimodal` · baseten
  Covers streaming real-time text-to-speech serving with XTTS v2.
- **2024-04-16** — [Running Privacy-Preserving Inferences on Hugging Face Endpoints](<../product-engineering/security/Running Privacy-Preserving Inferences on Hugging Face Endpoints.md>) · `security` · huggingface
  Shows how to serve Zama Concrete ML models under Fully Homomorphic Encryption on HF Inference Endpoints via custom inference handlers, so a spam classifier runs on ciphertext without ever seeing the plaintext message; also covers compiling your own FHE-friendly model.
- **2024-03-22** — [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](<../rag-retrieval/embeddings/Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval.md>) · `embeddings` · huggingface
  Binary (1-bit) and int8 scalar quantization of embeddings cuts retrieval memory/cost ~32x and ~4x while retaining ~92-96% of performance; covers rescoring with float embeddings and combining binary search + int8 rescoring in FAISS/usearch.
- **2024-03-15** — [CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG](<../rag-retrieval/embeddings/CPU Optimized Embeddings with 🤗 Optimum Intel and fastRAG.md>) · `embeddings` · huggingface
  Speeds up bge-base embeddings on Xeon CPUs by quantizing to int8 with Optimum Intel / IPEX, reporting latency and MTEB retrieval-quality deltas, then wires the optimized encoder into a fastRAG retrieval pipeline.
- **2024-03-14** — [Benchmarking fast Mistral 7B inference](<../evals-observability/benchmark-design/Benchmarking fast Mistral 7B inference.md>) · `benchmark-design` · baseten
  Benchmarks Mistral 7B inference performance and the serving choices that affect throughput and latency.
- **2024-03-04** — [BASED: Simple linear attention language models balance the recall-throughput tradeoff](<../models/reasoning/BASED Simple linear attention language models balance the recall-throughput tradeoff.md>) · `reasoning` · together
  Explains BASED linear-attention language models and the recall-throughput tradeoff.
- **2024-02-20** — [BitDelta: Your Fine-Tune May Only Be Worth One Bit](<../models/fine-tuning/BitDelta Your Fine-Tune May Only Be Worth One Bit.md>) · `fine-tuning` · together
  Explains BitDelta and how small weight deltas can represent fine-tuned model changes.
- **2024-01-12** — [Understanding performance benchmarks for LLM inference](<../evals-observability/benchmark-design/Understanding performance benchmarks for LLM inference.md>) · `benchmark-design` · baseten
  Explains LLM inference performance benchmarks and how to interpret serving metrics.
- **2023-12-08** — [StripedHyena-7B and efficient architectures beyond Transformers](<../models/reasoning/StripedHyena-7B and efficient architectures beyond Transformers.md>) · `reasoning` · together
  Introduces StripedHyena-7B and efficient architectures beyond Transformers.
- **2023-11-10** — [How Custom Summarization Saves Hours of After-Call Work](<../models/fine-tuning/How Custom Summarization Saves Hours of After-Call Work.md>) · `fine-tuning` · cresta
  Argues prompting alone cannot control output topics, style, or domain terminology for call summarization, so Cresta fine-tunes smaller domain models (Ocean-1 based) with supervised fine-tuning plus RLHF fed by agent edits. Reports 5x or better latency improvement over a gpt-3.5-turbo baseline at comparable quality, with ACW down to ~30 seconds.
- **2023-11-02** — [Deployment and inference for open source text embedding models](<../rag-retrieval/embeddings/Deployment and inference for open source text embedding models.md>) · `embeddings` · baseten
  Covers deployment and inference patterns for open-source text embedding models.
- **2023-07-25** — [Monarch Mixer: A new model architecture for increased efficiency](<../models/reasoning/Monarch Mixer A new model architecture for increased efficiency.md>) · `reasoning` · together
  Introduces Monarch Mixer as an efficient model architecture.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
- **2023-01-23** — [FlashConv: speeding up state space models](<../models/reasoning/FlashConv speeding up state space models.md>) · `reasoning` · together
  Explains FlashConv and efficient state-space model execution.
- **2021-03-16** — [Scaling Behavior Change Across 1,000 People](<../product-engineering/architecture/Scaling Behavior Change Across 1,000 People.md>) · `architecture` · cresta
  Cresta's Behavioral Engine runs BERT, GPT-2 and T5 models over 40,000 live chats a day to detect decision points (price objections, package questions) and fire real-time coaching hints. Reports scaling hint volume 5x while cutting cost per hint, over 2 million hints delivered, and per-chat rather than sampled analytics.
