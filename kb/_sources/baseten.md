# baseten

84 articles.

- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<../inference/hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-06-25** — [Live draft model training for speculative decoding](<../models/fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
- **2026-06-23** — [How we built the world’s fastest API for GLM-5.2](<../inference/optimization/How we built the world’s fastest API for GLM-5.2.md>) · `optimization` · baseten
  Engineering writeup on building a high-speed GLM-5.2 API.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<../infra-platform/deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-05-29** — [Timestep distillation: 2.5x faster FLUX.2 image generation](<../models/multimodal/Timestep distillation 2.5x faster FLUX.2 image generation.md>) · `multimodal` · baseten
  Explains timestep distillation for faster FLUX.2 image generation.
- **2026-05-18** — [Sub-second image generation with Flux.2 and Qwen-Image](<../inference/optimization/Sub-second image generation with Flux.2 and Qwen-Image.md>) · `optimization` · baseten
  Explains sub-second image generation with FLUX.2 and Qwen-Image serving optimizations.
- **2026-05-14** — [Cost-efficient, high-performance TTS with Qwen3-TTS](<../models/multimodal/Cost-efficient, high-performance TTS with Qwen3-TTS.md>) · `multimodal` · baseten
  Describes cost-efficient high-performance Qwen3-TTS serving for text-to-speech workloads.
- **2026-05-08** — [DFlash: 3x faster LLM inference](<../inference/speculative-decoding/DFlash 3x faster LLM inference.md>) · `speculative-decoding` · baseten
  Explains DFlash as an optimization for faster LLM inference.
- **2026-04-23** — [How we built RBAC that scales for the enterprise](<../product-engineering/security/How we built RBAC that scales for the enterprise.md>) · `security` · baseten
  Engineering writeup on building RBAC for enterprise AI infrastructure and balancing autonomy with control.
- **2026-04-16** — [Harnesses are everything. Here's how to optimize yours.](<../agents/harness/Harnesses are everything. Here's how to optimize yours.md>) · `harness` · baseten
  Explains why agent harness design matters and how to optimize harnesses for reliable agent behavior.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<../models/fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<../infra-platform/deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<../inference/optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-03-31** — [Baseten Training: an autoresearch substrate](<../models/fine-tuning/Baseten Training an autoresearch substrate.md>) · `fine-tuning` · baseten
  Frames model training infrastructure as an autoresearch substrate for running iterative experiments and training jobs.
- **2026-03-31** — [Open-source LLM training is a mess. Here is how it all works.](<../models/fine-tuning/Open-source LLM training is a mess. Here is how it all works.md>) · `fine-tuning` · baseten
  Explains the moving pieces of open-source LLM training, including data, trainers, infrastructure, and evaluation.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<../inference/quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-03-19** — [Introducing the Baseten Delivery Network: Fast cold starts for big models](<../infra-platform/deployment/Introducing the Baseten Delivery Network Fast cold starts for big models.md>) · `deployment` · baseten
  Introduces the Baseten Delivery Network for reducing cold starts when serving large models.
- **2026-03-06** — [How we built the fastest GLM 5 API](<../inference/optimization/How we built the fastest GLM 5 API.md>) · `optimization` · baseten
  Explains serving optimizations used to build a fast GLM 5 API.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<../inference/quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-02-11** — [How we built the fastest Kimi K2.5 on Artificial Analysis](<../inference/optimization/How we built the fastest Kimi K2.5 on Artificial Analysis.md>) · `optimization` · baseten
  Explains optimizations behind fast Kimi K2.5 serving on Artificial Analysis.
- **2026-02-09** — [AI Model Performance Metrics Explained](<../evals-observability/monitoring/AI Model Performance Metrics Explained.md>) · `monitoring` · baseten
  Explains model performance metrics used in production inference, including latency, throughput, and quality signals.
- **2026-02-05** — [How to run LLM performance benchmarks (and why you should)](<../evals-observability/benchmark-design/How to run LLM performance benchmarks (and why you should).md>) · `benchmark-design` · baseten
  Explains how to run LLM performance benchmarks and which serving metrics matter.
- **2026-02-03** — [The Baseten Inference Stack at NVIDIA Dynamo Day](<../inference/serving/The Baseten Inference Stack at NVIDIA Dynamo Day.md>) · `serving` · baseten
  Describes Baseten inference-stack ideas presented around NVIDIA Dynamo and production serving.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<../inference/speculative-decoding/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `speculative-decoding` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2025-12-05** — [DeepSeek V3.2's path to GPT-5-level performance: sparse attention, RL at scale, and context reuse](<../models/reasoning/DeepSeek V3.2's path to GPT-5-level performance sparse attention, RL at scale, and context reuse.md>) · `reasoning` · baseten
  Explains DeepSeek V3.2 architecture and training choices including sparse attention, RL, and context reuse.
- **2025-11-12** — [Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell](<../inference/optimization/Kimi K2 Thinking at 140+ TPS on NVIDIA Blackwell.md>) · `optimization` · baseten
  Explains Kimi K2 Thinking serving at high throughput on NVIDIA Blackwell hardware.
- **2025-11-05** — [Tool Calling in Inference](<../agents/tool-use/Tool Calling in Inference.md>) · `tool-use` · baseten
  Explains tool calling in inference and how model servers support structured external actions.
- **2025-10-24** — [How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster](<../inference/optimization/How we made the fastest GPT-OSS on NVIDIA GPUs 60% faster.md>) · `optimization` · baseten
  Explains optimization work that made GPT-OSS inference faster on NVIDIA GPUs.
- **2025-10-23** — [DeepSeek-OCR and the Unreasonable Usefulness of Compression](<../models/multimodal/DeepSeek-OCR and the Unreasonable Usefulness of Compression.md>) · `multimodal` · baseten
  Explains DeepSeek-OCR and why compression can be useful for multimodal model workflows.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<../inference/optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-08-19** — [How to fine-tune gpt-oss-120b with Baseten and Axolotl](<../models/fine-tuning/How to fine-tune gpt-oss-120b with Baseten and Axolotl.md>) · `fine-tuning` · baseten
  Guide to fine-tuning GPT-OSS 120B with Axolotl and scalable training infrastructure.
- **2025-08-15** — [Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks](<../models/fine-tuning/Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks.md>) · `fine-tuning` · baseten
  Case study on fine-tuning small open-source LLMs to beat larger closed models on specialized tasks.
- **2025-08-07** — [How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs](<../inference/optimization/How we run GPT OSS 120B at 500+ tokens per second on NVIDIA GPUs.md>) · `optimization` · baseten
  Explains how to run GPT-OSS 120B at high token throughput on NVIDIA GPUs.
- **2025-07-15** — [Building reliable AI agents](<../agents/planning/Building reliable AI agents.md>) · `planning` · baseten
  Covers practical design patterns for building more reliable AI agents.
- **2025-06-23** — [How we built Multi-cloud Capacity Management (MCM)](<../infra-platform/gpu-clusters/How we built Multi-cloud Capacity Management (MCM).md>) · `gpu-clusters` · baseten
  Engineering writeup on building multi-cloud capacity management for inference infrastructure.
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<../rag-retrieval/embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-06-09** — [How Baseten multi-cloud capacity management unifies deployments](<../infra-platform/gpu-clusters/How Baseten multi-cloud capacity management unifies deployments.md>) · `gpu-clusters` · baseten
  Explains multi-cloud capacity management for unifying cloud, self-hosted, and hybrid inference deployments.
- **2025-04-29** — [Day zero benchmarks for Qwen 3 with SGLang on Baseten](<../models/benchmarks/Day zero benchmarks for Qwen 3 with SGLang on Baseten.md>) · `benchmarks` · baseten
  Provides day-zero Qwen 3 benchmarks with SGLang and discusses serving-performance implications.
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<../inference/hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<../rag-retrieval/embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<../inference/serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2025-02-07** — [Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud](<../evals-observability/benchmark-design/Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud.md>) · `benchmark-design` · baseten
  Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark results.
- **2025-01-09** — [Driving model performance optimization: 2024 highlights](<../inference/optimization/Driving model performance optimization 2024 highlights.md>) · `optimization` · baseten
  Summarizes concrete model-performance optimization work across inference serving, batching, and hardware.
- **2024-12-19** — [A quick introduction to speculative decoding](<../inference/speculative-decoding/A quick introduction to speculative decoding.md>) · `speculative-decoding` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<../inference/speculative-decoding/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `speculative-decoding` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<../inference/hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-09-17** — [Building high-performance compound AI applications with MongoDB Atlas and Baseten](<../rag-retrieval/pipelines/Building high-performance compound AI applications with MongoDB Atlas and Baseten.md>) · `pipelines` · baseten
  Shows how to build high-performance compound AI applications with retrieval, orchestration, and model serving.
- **2024-09-12** — [How to build function calling and JSON mode for open-source and fine-tuned LLMs](<../prompt-engineering/structured-output/How to build function calling and JSON mode for open-source and fine-tuned LLMs.md>) · `structured-output` · baseten
  Shows how to build function calling and JSON mode for open-source and fine-tuned LLMs.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<../inference/speculative-decoding/How to double tokens per second for Llama 3 with Medusa.md>) · `speculative-decoding` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-06** — [Compound AI systems explained](<../product-engineering/architecture/Compound AI systems explained.md>) · `architecture` · baseten
  Explains compound AI systems and how multiple models, tools, and control logic combine into applications.
- **2024-08-01** — [Introducing automatic LLM optimization with TensorRT-LLM Engine Builder](<../inference/optimization/Introducing automatic LLM optimization with TensorRT-LLM Engine Builder.md>) · `optimization` · baseten
  Describes automatic LLM optimization with TensorRT-LLM Engine Builder for production serving.
- **2024-07-25** — [Deploying custom ComfyUI workflows as APIs](<../models/multimodal/Deploying custom ComfyUI workflows as APIs.md>) · `multimodal` · baseten
  Shows how to deploy custom ComfyUI image-generation workflows behind API endpoints.
- **2024-07-23** — [How to serve 10,000 fine-tuned LLMs from a single GPU](<../inference/serving/How to serve 10,000 fine-tuned LLMs from a single GPU.md>) · `serving` · baseten
  Explains serving many fine-tuned LLM adapters from a single GPU with efficient multiplexing.
- **2024-07-11** — [Using asynchronous inference in production](<../inference/serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-07-02** — [Building multi-component AI workflows at scale with Chains](<../product-engineering/architecture/Building multi-component AI workflows at scale with Chains.md>) · `architecture` · baseten
  Explains multi-component AI workflows with Chains, including orchestration across model and application steps.
- **2024-06-14** — [Comparing few-step image generation models](<../models/benchmarks/Comparing few-step image generation models.md>) · `benchmarks` · baseten
  Compares few-step image generation models and the tradeoffs between speed and output quality.
- **2024-06-04** — [How latent consistency models work](<../models/multimodal/How latent consistency models work.md>) · `multimodal` · baseten
  Explains latent consistency models and how they enable faster image generation.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<../infra-platform/deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-04-30** — [CI-CD for AI model deployments](<../infra-platform/deployment/CI-CD for AI model deployments.md>) · `deployment` · baseten
  Covers CI/CD practices for AI model deployments, including versioning, release flow, and operational safety.
- **2024-04-18** — [Streaming real-time text to speech with XTTS V2](<../models/multimodal/Streaming real-time text to speech with XTTS V2.md>) · `multimodal` · baseten
  Covers streaming real-time text-to-speech serving with XTTS v2.
- **2024-04-05** — [Continuous vs dynamic batching for AI inference](<../inference/optimization/Continuous vs dynamic batching for AI inference.md>) · `optimization` · baseten
  Compares continuous and dynamic batching for inference serving and their latency-throughput tradeoffs.
- **2024-03-28** — [Using fractional H100 GPUs for efficient model serving](<../inference/serving/Using fractional H100 GPUs for efficient model serving.md>) · `serving` · baseten
  Explains fractional H100 usage for efficient model serving and better GPU utilization.
- **2024-03-14** — [33% faster LLM inference with FP8 quantization](<../inference/quantization/33% faster LLM inference with FP8 quantization.md>) · `quantization` · baseten
  Shows how FP8 quantization improves LLM inference throughput while managing accuracy and hardware constraints.
- **2024-03-14** — [Benchmarking fast Mistral 7B inference](<../evals-observability/benchmark-design/Benchmarking fast Mistral 7B inference.md>) · `benchmark-design` · baseten
  Benchmarks Mistral 7B inference performance and the serving choices that affect throughput and latency.
- **2024-03-12** — [High performance ML inference with NVIDIA TensorRT](<../inference/optimization/High performance ML inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains high-performance model inference with NVIDIA TensorRT and related deployment considerations.
- **2024-03-07** — [FP8: Efficient model inference with 8-bit floating point numbers](<../inference/quantization/FP8 Efficient model inference with 8-bit floating point numbers.md>) · `quantization` · baseten
  Explains FP8 numeric formats and why 8-bit floating point can improve efficient model inference.
- **2024-02-22** — [40% faster Stable Diffusion XL inference with NVIDIA TensorRT](<../inference/optimization/40% faster Stable Diffusion XL inference with NVIDIA TensorRT.md>) · `optimization` · baseten
  Explains TensorRT optimization for Stable Diffusion XL inference, including latency and throughput gains.
- **2024-02-20** — [Why GPU utilization matters for model inference](<../inference/hardware/Why GPU utilization matters for model inference.md>) · `hardware` · baseten
  Explains why GPU utilization is central to inference cost and performance.
- **2024-02-06** — [Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT](<../inference/optimization/Unlocking the full power of NVIDIA H100 GPUs for ML inference with TensorRT.md>) · `optimization` · baseten
  Shows how TensorRT unlocks H100 performance for model inference.
- **2024-01-31** — [Introduction to quantizing ML models](<../inference/quantization/Introduction to quantizing ML models.md>) · `quantization` · baseten
  Introduces model quantization concepts and how they affect inference efficiency and model quality.
- **2024-01-31** — [How to benchmark image generation models like Stable Diffusion XL](<../evals-observability/benchmark-design/How to benchmark image generation models like Stable Diffusion XL.md>) · `benchmark-design` · baseten
  Explains how to benchmark image-generation models with attention to quality, latency, and reproducibility.
- **2024-01-12** — [Understanding performance benchmarks for LLM inference](<../evals-observability/benchmark-design/Understanding performance benchmarks for LLM inference.md>) · `benchmark-design` · baseten
  Explains LLM inference performance benchmarks and how to interpret serving metrics.
- **2023-12-22** — [Faster Mixtral inference with TensorRT-LLM and quantization](<../inference/quantization/Faster Mixtral inference with TensorRT-LLM and quantization.md>) · `quantization` · baseten
  Shows how TensorRT-LLM and quantization improve Mixtral inference performance.
- **2023-12-13** — [Playground v2 vs Stable Diffusion XL 1.0 for text-to-image generation](<../models/benchmarks/Playground v2 vs Stable Diffusion XL 1.0 for text-to-image generation.md>) · `benchmarks` · baseten
  Compares Playground v2 and Stable Diffusion XL for text-to-image generation quality and serving use cases.
- **2023-12-08** — [How to serve your ComfyUI model behind an API endpoint](<../models/multimodal/How to serve your ComfyUI model behind an API endpoint.md>) · `multimodal` · baseten
  Shows how to serve a ComfyUI model behind an API endpoint for production image workflows.
- **2023-11-28** — [NVIDIA A10 vs A10G for ML model inference](<../inference/hardware/NVIDIA A10 vs A10G for ML model inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A10G GPUs for model inference performance and cost.
- **2023-11-17** — [A guide to LLM inference and performance](<../inference/serving/A guide to LLM inference and performance.md>) · `serving` · baseten
  Comprehensive guide to LLM inference, transformer serving, latency, and throughput performance.
- **2023-11-02** — [Deployment and inference for open source text embedding models](<../rag-retrieval/embeddings/Deployment and inference for open source text embedding models.md>) · `embeddings` · baseten
  Covers deployment and inference patterns for open-source text embedding models.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<../inference/hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-08-30** — [SDXL inference in under 2 seconds](<../inference/optimization/SDXL inference in under 2 seconds.md>) · `optimization` · baseten
  Guide to Stable Diffusion XL inference optimization for sub-2-second image generation.
- **2023-06-15** — [Three techniques to adapt LLMs for any use case](<../models/fine-tuning/Three techniques to adapt LLMs for any use case.md>) · `fine-tuning` · baseten
  Explains prompt engineering, fine-tuning, and related techniques for adapting LLMs to use cases.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<../inference/hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.
- **2023-02-17** — [Technical deep dive: Truss live reload](<../infra-platform/deployment/Technical deep dive Truss live reload.md>) · `deployment` · baseten
  Technical deep dive into Truss live reload and faster model-server development loops.
- **2022-12-08** — [Accelerating model deployment: 100X faster dev loops with development deployments](<../infra-platform/deployment/Accelerating model deployment 100X faster dev loops with development deployments.md>) · `deployment` · baseten
  Explains development deployments and draft models as a way to shorten model deployment iteration loops.
