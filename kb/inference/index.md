# inference

34 articles.

- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<optimization/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `optimization` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-06-30** — [Multi-token Residual Prediction](<optimization/Multi-token Residual Prediction.md>) · `optimization` · modal
  Explains multi-token residual prediction as an inference acceleration technique for generating multiple tokens per step.
- **2026-06-30** — [Using OSS models to save on inference costs without cutting quality](<serving/Using OSS models to save on inference costs without cutting quality.md>) · `serving` · braintrust
  Explains using open-source models to reduce inference cost without sacrificing quality, emphasizing eval-driven model selection and serving tradeoffs.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-06-22** — [Achieve state-of-the-art inference latencies with speculative decoding](<optimization/Achieve state-of-the-art inference latencies with speculative decoding.md>) · `optimization` · modal
  Explains speculative decoding for lower inference latency, including draft-model tradeoffs and production serving considerations.
- **2026-06-22** — [Introducing Modal Auto Endpoints: Optimized inference you actually own](<serving/Introducing Modal Auto Endpoints Optimized inference you actually own.md>) · `serving` · modal
  Describes auto endpoints for owned inference deployments, including optimized serving configuration and operational control.
- **2026-06-19** — [Speculation Is All You Need](<optimization/Speculation Is All You Need.md>) · `optimization` · modal
  Deep dive into speculative decoding and related techniques for improving LLM inference latency and throughput.
- **2026-05-12** — [Engineering low-latency voice agents](<optimization/Engineering low-latency voice agents.md>) · `optimization` · sierra
  Engineering note on low-latency voice agents, covering response-time constraints and optimization across speech and model serving.
- **2026-05-12** — [A more reliable inference layer for foundation models](<serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-05-12** — [Preserving agent behavior while serving LLMs reliably](<serving/Preserving agent behavior while serving LLMs reliably.md>) · `serving` · sierra
  Covers model failover for preserving agent behavior while serving LLMs reliably across model/provider disruptions.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<optimization/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `optimization` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-06** — [Inference providers vs. API routers](<serving/Inference providers vs. API routers.md>) · `serving` · fireworks
  Explains the operational difference between inference providers and API routers, including routing, control, and token provenance.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-17** — [A postmortem of three recent issues](<serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-06-18** — [Run FLUX.1-dev three times faster](<optimization/Run FLUX.1-dev three times faster.md>) · `optimization` · modal
  Explains optimizations for running FLUX.1-dev faster, including inference configuration and image-model serving tradeoffs.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-16** — [Boost your throughput with dynamic batching](<optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<optimization/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `optimization` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<optimization/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `optimization` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.

## Also relevant (filed elsewhere)

- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<optimization/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `optimization` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-06** — [How to price serverless GPUs](<../infra-platform/cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-07-01** — [Model subsidies are ending. What do you do now?](<../infra-platform/cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-15** — [Growing the Cloudflare AI team with talent from Ensemble AI](<../industry/announcements/Growing the Cloudflare AI team with talent from Ensemble AI.md>) · `announcements` · cloudflare-ai
  Ensemble AI's team joins Cloudflare's Workers AI to improve inference economics, bringing NdLinear — a drop-in linear-layer replacement operating on multidimensional activations to cut parameters and compute — and NdLinear-LoRA for parameter-efficient fine-tuning, complementing Infire and Unweight.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [How we achieved truly serverless GPUs](<../infra-platform/gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-03-16** — [Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider](<../infra-platform/deployment/Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider.md>) · `deployment` · arize
  Announces native NVIDIA NIM support in Arize AX so teams can connect hosted model providers into evaluation and observability workflows.
- **2026-02-27** — [DeepSeek Models: V3.2, R1, Distills, and Production Caveats](<../models/reasoning/DeepSeek Models V3.2, R1, Distills, and Production Caveats.md>) · `reasoning` · fireworks
  Surveys DeepSeek model variants with production caveats around serving, reasoning behavior, and deployment tradeoffs.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<../infra-platform/gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models speculative decoding and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-07-23** — [Transcribe speech 100x faster and 100x cheaper with open models](<../models/multimodal/Transcribe speech 100x faster and 100x cheaper with open models.md>) · `multimodal` · modal
  Shows how open speech models and batch execution can reduce transcription latency and cost at large scale.
- **2025-07-22** — [Kimi QK-Clip and multi-head latent attention](<../models/reasoning/Kimi QK-Clip and multi-head latent attention.md>) · `reasoning` · fireworks
  Explains Kimi QK-Clip, multi-head latent attention, and why training-inference key construction affects stability.
- **2025-07-16** — [Dollars per token considered harmful](<../infra-platform/cost/Dollars per token considered harmful.md>) · `cost` · modal
  Critiques dollars-per-token as an inference cost metric and explains why workload shape, latency, and utilization matter more.
- **2025-07-02** — [How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work](<../evals-observability/evaluation/How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work.md>) · `evaluation` · modal
  Case study using evals and inference-time compute scaling to generate QR codes that satisfy visual and functional constraints.
- **2025-06-14** — [3D FireOptimizer: Automating the Multi-Dimensional Tradeoffs in LLM Serving](<serving/3D FireOptimizer Automating the Multi-Dimensional Tradeoffs in LLM Serving.md>) · `serving` · fireworks
  Explains multi-dimensional optimization for LLM serving, balancing latency, cost, throughput, and quality tradeoffs.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2025-05-28** — [FireAttention V4: Industry-Leading Latency and Cost Efficiency with FP4](<quantization/FireAttention V4 Industry-Leading Latency and Cost Efficiency with FP4.md>) · `quantization` · fireworks
  Covers FP4 and B200-focused FireAttention V4 optimizations for latency and cost-efficient serving.
- **2025-02-07** — [DeepSeek v3 and R1 Model Architecture: Why it's powerful and economical](<../models/reasoning/DeepSeek v3 and R1 Model Architecture Why it's powerful and economical.md>) · `reasoning` · fireworks
  Explains DeepSeek V3 and R1 architecture choices, including why the models are efficient for reasoning workloads.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<../infra-platform/deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2024-12-09** — [20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds](<../models/multimodal/20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds.md>) · `multimodal` · fireworks
  Describes high-throughput Whisper transcription serving and the latency/cost tradeoffs in batch audio inference.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-01-16** — [Generation configurations: temperature, top-k, top-p, and test time compute](<../models/reasoning/Generation configurations temperature, top-k, top-p, and test time compute.md>) · `reasoning` · chip-huyen
  Explains decoding parameters such as temperature, top-k, top-p, and test-time compute, connecting generation configuration to reliability, diversity, latency, and cost.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-09-19** — [Arize AI Debuts Integration with Anyscale Endpoints](<../infra-platform/deployment/Arize AI Debuts Integration with Anyscale Endpoints.md>) · `deployment` · arize
  Announcement and integration walkthrough for using Arize with Anyscale Endpoints to monitor hosted open-model inference.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.
