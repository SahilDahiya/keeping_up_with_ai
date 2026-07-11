# inference

74 articles.

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
- **2026-06-22** — [Introducing Modal Auto Endpoints: Optimized inference you actually own](<serving/Introducing Modal Auto Endpoints Optimized inference you actually own.md>) · `serving` · modal
  Describes auto endpoints for owned inference deployments, including optimized serving configuration and operational control.
- **2026-06-19** — [Speculation Is All You Need](<optimization/Speculation Is All You Need.md>) · `optimization` · modal
  Deep dive into speculative decoding and related techniques for improving LLM inference latency and throughput.
- **2026-05-18** — [Sub-second image generation with Flux.2 and Qwen-Image](<optimization/Sub-second image generation with Flux.2 and Qwen-Image.md>) · `optimization` · baseten
  Explains sub-second image generation with FLUX.2 and Qwen-Image serving optimizations.
- **2026-05-12** — [Engineering low-latency voice agents](<optimization/Engineering low-latency voice agents.md>) · `optimization` · sierra
  Engineering note on low-latency voice agents, covering response-time constraints and optimization across speech and model serving.
- **2026-05-12** — [A more reliable inference layer for foundation models](<serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-05-12** — [Preserving agent behavior while serving LLMs reliably](<serving/Preserving agent behavior while serving LLMs reliably.md>) · `serving` · sierra
  Covers model failover for preserving agent behavior while serving LLMs reliably across model/provider disruptions.
- **2026-05-08** — [DFlash: 3x faster LLM inference](<optimization/DFlash 3x faster LLM inference.md>) · `optimization` · baseten
  Explains DFlash as an optimization for faster LLM inference.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-03-10** — [Training-Inference Parity in MoE Models: Where Numerics Drift](<optimization/Training-Inference Parity in MoE Models Where Numerics Drift.md>) · `optimization` · fireworks
  Explains training-inference parity issues in MoE models and how numeric drift can affect production behavior.
- **2026-03-06** — [How we built the fastest GLM 5 API](<optimization/How we built the fastest GLM 5 API.md>) · `optimization` · baseten
  Explains serving optimizations used to build a fast GLM 5 API.
- **2026-03-06** — [Inference providers vs. API routers](<serving/Inference providers vs. API routers.md>) · `serving` · fireworks
  Explains the operational difference between inference providers and API routers, including routing, control, and token provenance.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-02-11** — [How we built the fastest Kimi K2.5 on Artificial Analysis](<optimization/How we built the fastest Kimi K2.5 on Artificial Analysis.md>) · `optimization` · baseten
  Explains optimizations behind fast Kimi K2.5 serving on Artificial Analysis.
- **2026-02-03** — [The Baseten Inference Stack at NVIDIA Dynamo Day](<serving/The Baseten Inference Stack at NVIDIA Dynamo Day.md>) · `serving` · baseten
  Describes Baseten inference-stack ideas presented around NVIDIA Dynamo and production serving.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<optimization/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `optimization` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-11-12** — [Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell](<optimization/Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell.md>) · `optimization` · baseten
  Explains Kimi K2 Thinking serving at high throughput on NVIDIA Blackwell hardware.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-10-24** — [How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster](<optimization/How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster.md>) · `optimization` · baseten
  Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-17** — [A postmortem of three recent issues](<serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-08-07** — [How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs](<optimization/How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs.md>) · `optimization` · baseten
  Explains how to run GPT-OSS 120B at high token throughput on NVIDIA GPUs.
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
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2025-01-09** — [Driving model performance optimization: 2024 highlights](<optimization/Driving model performance optimization 2024 highlights.md>) · `optimization` · baseten
  Summarizes concrete model-performance optimization work across inference serving, batching, and hardware.
- **2024-12-19** — [A quick introduction to speculative decoding](<optimization/A quick introduction to speculative decoding.md>) · `optimization` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<optimization/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `optimization` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-16** — [Boost your throughput with dynamic batching](<optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<optimization/How to double tokens per second for Llama 3 with Medusa.md>) · `optimization` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-01** — [Introducing automatic LLM optimization with TensorRT-LLM Engine Builder](<optimization/Introducing automatic LLM optimization with TensorRT-LLM Engine Builder.md>) · `optimization` · baseten
  Describes automatic LLM optimization with TensorRT-LLM Engine Builder for production serving.
- **2024-08-01** — [How Fireworks evaluates quantization precisely and interpretably](<quantization/How Fireworks evaluates quantization precisely and interpretably.md>) · `quantization` · fireworks
  Details precise and interpretable quantization evaluation for understanding quality and performance tradeoffs.
- **2024-07-23** — [How to serve 10,000 fine-tuned LLMs from a single GPU](<serving/How to serve 10,000 fine-tuned LLMs from a single GPU.md>) · `serving` · baseten
  Explains serving many fine-tuned LLM adapters from a single GPU with efficient multiplexing.
- **2024-07-11** — [Using asynchronous inference in production](<serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-06-23** — [How Cursor built Fast Apply using the Speculative Decoding API](<optimization/How Cursor built Fast Apply using the Speculative Decoding API.md>) · `optimization` · fireworks
  Case study of Cursor Fast Apply using speculative decoding to reduce coding-assistant latency.
- **2024-06-20** — [FireAttention V2: 12x faster to make Long Contexts practical for Online Inference](<optimization/FireAttention V2 12x faster to make Long Contexts practical for Online Inference.md>) · `optimization` · fireworks
  Explains FireAttention V2 and the serving optimizations that make long-context inference more practical.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-03-28** — [Using fractional H100 GPUs for efficient model serving](<serving/Using fractional H100 GPUs for efficient model serving.md>) · `serving` · baseten
  Explains fractional H100 usage for efficient model serving and better GPU utilization.
- **2024-03-14** — [33% faster LLM inference with FP8 quantization](<quantization/33% faster LLM inference with FP8 quantization.md>) · `quantization` · baseten
  Shows how FP8 quantization improves LLM inference throughput while managing accuracy and hardware constraints.
- **2024-03-12** — [High performance ML inference with NVIDIA TensorRT](<optimization/High performance ML inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains high-performance model inference with NVIDIA TensorRT and related deployment considerations.
- **2024-03-07** — [FP8: Efficient model inference with 8-bit floating point numbers](<quantization/FP8 Efficient model inference with 8-bit floating point numbers.md>) · `quantization` · baseten
  Explains FP8 numeric formats and why 8-bit floating point can improve efficient model inference.
- **2024-02-22** — [40% faster Stable Diffusion XL inference with NVIDIA TensorRT](<optimization/40% faster Stable Diffusion XL inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains TensorRT optimization for Stable Diffusion XL inference, including latency and throughput gains.
- **2024-02-20** — [Why GPU utilization matters for model inference](<hardware/Why GPU utilization matters for model inference.md>) · `hardware` · baseten
  Explains why GPU utilization is central to inference cost and performance.
- **2024-02-06** — [Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT](<optimization/Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT.md>) · `optimization` · baseten
  Shows how TensorRT unlocks H100 performance for model inference.
- **2024-01-31** — [Introduction to quantizing ML models](<quantization/Introduction to quantizing ML models.md>) · `quantization` · baseten
  Introduces model quantization concepts and how they affect inference efficiency and model quality.
- **2024-01-08** — [FireAttention: serving open models faster with quantization](<quantization/FireAttention serving open models faster with quantization.md>) · `quantization` · fireworks
  Introduces FireAttention for serving open models faster through quantization with minimal quality tradeoff.
- **2023-12-22** — [Faster Mixtral inference with TensorRT-LLM and quantization](<quantization/Faster Mixtral inference with TensorRT-LLM and quantization.md>) · `quantization` · baseten
  Shows how TensorRT-LLM and quantization improve Mixtral inference performance.
- **2023-11-28** — [NVIDIA A10 vs A10G for ML model inference](<hardware/NVIDIA A10 vs A10G for ML model inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A10G GPUs for model inference performance and cost.
- **2023-11-17** — [A guide to LLM inference and performance](<serving/A guide to LLM inference and performance.md>) · `serving` · baseten
  Comprehensive guide to LLM inference, transformer serving, latency, and throughput performance.
- **2023-11-03** — [LLM Inference Performance Benchmarking (Part 1)](<serving/LLM Inference Performance Benchmarking (Part 1).md>) · `serving` · fireworks
  Introduces LLM inference performance benchmarking and the metrics needed to compare serving systems.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-08-30** — [SDXL inference in under 2 seconds](<optimization/SDXL inference in under 2 seconds.md>) · `optimization` · baseten
  Guide to Stable Diffusion XL inference optimization for sub-2-second image generation.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.

## Also relevant (filed elsewhere)

- **2026-07-10** — [Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell](<optimization/Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell.md>) · `optimization` · fireworks
  Deep dive into sparse-attention kernel optimization for MiniMax M3 on NVIDIA Blackwell hardware.
- **2026-07-06** — [How to price serverless GPUs](<../infra-platform/cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-07-01** — [Model subsidies are ending. What do you do now?](<../infra-platform/cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-25** — [Live draft model training for speculative decoding](<../models/fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
- **2026-06-23** — [How we built the world’s fastest API for GLM-5.2](<optimization/How we built the world’s fastest API for GLM-5.2.md>) · `optimization` · baseten
  Engineering writeup on building a high-speed GLM-5.2 API.
- **2026-06-15** — [Growing the Cloudflare AI team with talent from Ensemble AI](<../industry/announcements/Growing the Cloudflare AI team with talent from Ensemble AI.md>) · `announcements` · cloudflare-ai
  Ensemble AI's team joins Cloudflare's Workers AI to improve inference economics, bringing NdLinear — a drop-in linear-layer replacement operating on multidimensional activations to cut parameters and compute — and NdLinear-LoRA for parameter-efficient fine-tuning, complementing Infire and Unweight.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<../infra-platform/deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-05-29** — [Timestep distillation: 2.5x faster FLUX.2 image generation](<../models/multimodal/Timestep distillation 2.5x faster FLUX.2 image generation.md>) · `multimodal` · baseten
  Explains timestep distillation for faster FLUX.2 image generation.
- **2026-05-14** — [Cost-efficient, high-performance TTS with Qwen3-TTS](<../models/multimodal/Cost-efficient, high-performance TTS with Qwen3-TTS.md>) · `multimodal` · baseten
  Describes cost-efficient high-performance Qwen3-TTS serving for text-to-speech workloads.
- **2026-05-12** — [Constellation of models: the architecture powering Sierra's agents](<../models/reasoning/Constellation of models the architecture powering Sierra's agents.md>) · `reasoning` · sierra
  Describes a constellation-of-models architecture for powering agents, combining multiple models and routing behavior around task needs.
- **2026-05-12** — [How we achieved truly serverless GPUs](<../infra-platform/gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<../models/fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<../infra-platform/deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-03-19** — [Introducing the Baseten Delivery Network: Fast cold starts for big models](<../infra-platform/deployment/Introducing the Baseten Delivery Network Fast cold starts for big models.md>) · `deployment` · baseten
  Introduces the Baseten Delivery Network for reducing cold starts when serving large models.
- **2026-03-16** — [Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider](<../infra-platform/deployment/Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider.md>) · `deployment` · arize
  Announces native NVIDIA NIM support in Arize AX so teams can connect hosted model providers into evaluation and observability workflows.
- **2026-03-06** — [How we built the fastest GLM 5 API](<optimization/How we built the fastest GLM 5 API.md>) · `optimization` · baseten
  Explains serving optimizations used to build a fast GLM 5 API.
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
- **2025-11-03** — [Vercel code fixing with open models, speculative decoding, and RFT](<../product-engineering/case-studies/Vercel code fixing with open models speculative decoding and RFT.md>) · `case-studies` · fireworks
  Case study of improving Vercel code-fixing outputs with open models, speculative decoding, and reinforcement fine-tuning.
- **2025-10-24** — [How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster](<optimization/How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster.md>) · `optimization` · baseten
  Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-08-07** — [How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs](<optimization/How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs.md>) · `optimization` · baseten
  Explains how to run GPT-OSS 120B at high token throughput on NVIDIA GPUs.
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
- **2024-12-09** — [20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds](<../models/multimodal/20x faster Whisper than OpenAI - Fireworks audio transcribes 1 hour in 4 seconds.md>) · `multimodal` · fireworks
  Describes high-throughput Whisper transcription serving and the latency/cost tradeoffs in batch audio inference.
- **2024-10-15** — [FireAttention V3: Enabling AMD as a viable alternative for GPU inference](<hardware/FireAttention V3 Enabling AMD as a viable alternative for GPU inference.md>) · `hardware` · fireworks
  Describes FireAttention V3 and optimizations that make AMD GPUs more viable for inference workloads.
- **2024-09-18** — [Multi-LoRA: Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency](<../models/fine-tuning/Multi-LoRA Personalize AI at scale and deliver the best experience for each customer and use case, with 100x cost-efficiency.md>) · `fine-tuning` · fireworks
  Explains Multi-LoRA serving for personalized models at scale with better cost efficiency.
- **2024-08-30** — [FireOptimizer: Customizing latency and quality for your production inference workload](<serving/FireOptimizer Customizing latency and quality for your production inference workload.md>) · `serving` · fireworks
  Explains FireOptimizer for tuning production inference workloads across latency, quality, and cost objectives.
- **2024-08-01** — [Introducing automatic LLM optimization with TensorRT-LLM Engine Builder](<optimization/Introducing automatic LLM optimization with TensorRT-LLM Engine Builder.md>) · `optimization` · baseten
  Describes automatic LLM optimization with TensorRT-LLM Engine Builder for production serving.
- **2024-06-04** — [How latent consistency models work](<../models/multimodal/How latent consistency models work.md>) · `multimodal` · baseten
  Explains latent consistency models and how they enable faster image generation.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<../infra-platform/deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-04-18** — [Streaming real-time text to speech with XTTS V2](<../models/multimodal/Streaming real-time text to speech with XTTS V2.md>) · `multimodal` · baseten
  Covers streaming real-time text-to-speech serving with XTTS v2.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-03-14** — [33% faster LLM inference with FP8 quantization](<quantization/33% faster LLM inference with FP8 quantization.md>) · `quantization` · baseten
  Shows how FP8 quantization improves LLM inference throughput while managing accuracy and hardware constraints.
- **2024-03-14** — [Benchmarking fast Mistral 7B inference](<../evals-observability/evaluation/Benchmarking fast Mistral 7B inference.md>) · `evaluation` · baseten
  Benchmarks Mistral 7B inference performance and the serving choices that affect throughput and latency.
- **2024-03-12** — [High performance ML inference with NVIDIA TensorRT](<optimization/High performance ML inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains high-performance model inference with NVIDIA TensorRT and related deployment considerations.
- **2024-03-07** — [FP8: Efficient model inference with 8-bit floating point numbers](<quantization/FP8 Efficient model inference with 8-bit floating point numbers.md>) · `quantization` · baseten
  Explains FP8 numeric formats and why 8-bit floating point can improve efficient model inference.
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
- **2023-11-17** — [A guide to LLM inference and performance](<serving/A guide to LLM inference and performance.md>) · `serving` · baseten
  Comprehensive guide to LLM inference, transformer serving, latency, and throughput performance.
- **2023-11-02** — [Deployment and inference for open source text embedding models](<../rag-retrieval/embeddings/Deployment and inference for open source text embedding models.md>) · `embeddings` · baseten
  Covers deployment and inference patterns for open-source text embedding models.
- **2023-09-19** — [Arize AI Debuts Integration with Anyscale Endpoints](<../infra-platform/deployment/Arize AI Debuts Integration with Anyscale Endpoints.md>) · `deployment` · arize
  Announcement and integration walkthrough for using Arize with Anyscale Endpoints to monitor hosted open-model inference.
- **2023-08-29** — [Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning](<optimization/Speed, Python Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning.md>) · `optimization` · fireworks
  Explains how CUDA Graphs reduce Python overhead for fast deep-learning execution.
- **2023-07-12** — [Multi-Query Attention is All You Need](<../models/reasoning/Multi-Query Attention is All You Need.md>) · `reasoning` · fireworks
  Explains multi-query attention and why attention variants matter for efficient LLM inference.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.
