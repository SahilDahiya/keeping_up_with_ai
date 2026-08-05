# baseten

74 articles.

- **2026-08-04** — [Introducing NVIDIA Nemotron 3.5 ASR Streaming](<../models/releases/Introducing NVIDIA Nemotron 3.5 ASR Streaming.md>) · `releases` · baseten
  Baseten benchmarks NVIDIA's Nemotron 3.5 ASR streaming models (a 600M-parameter cache-aware FastConformer-RNNT architecture) on H100s, sustaining 100 concurrent WebSocket streams with 98-138ms finalization latency, 8.84% average WER across 19 languages, and 2.32% WER on LibriSpeech Clean for the English-only variant.
- **2026-08-03** — [Laguna S 2.1 goes Greek: a repository-scale game transformation](<../agents/tool-use/Laguna S 2.1 goes Greek a repository-scale game transformation.md>) · `tool-use` · baseten
  Baseten case study: Poolside's Laguna S 2.1 (118B MoE, 8B active params, 1M context), running on Baseten Dedicated Inference, autonomously re-themed the 715-file Hypersomnia C++ codebase from cyberpunk to Ancient Greek in under 99 minutes, orchestrating Step 3.7 Flash, Krea 2 Turbo, and NVIDIA Cosmos 3 Nano as sub-models (modifying 954 sprites and 64 code/config files) while deliberately declining to use the video model when it added no value.
- **2026-07-31** — [Fine-tuning Qwen3-TTS for high-quality voice cloning](<../models/fine-tuning/Fine-tuning Qwen3-TTS for high-quality voice cloning.md>) · `fine-tuning` · baseten
  Baseten details a fine-tuning recipe for Qwen3-TTS voice cloning: an ASR-driven pipeline for building utterance-level (audio, text) pairs, talker/sub-talker cross-entropy loss over 12 RVQ codebook frames/sec, a centroid speaker embedding averaged over 64 clips, and warmup+cosine LR decay, trained in ~1 hour on a single H100 for 8 epochs on 1.5 hours of LJ Speech audio, reaching ~130ms TTFA (vs ~154ms for ICL cloning).
- **2026-07-30** — [22,580: GPT-2 to Kimi K3, explained](<../models/architectures/22,580 GPT-2 to Kimi K3, explained.md>) · `architectures` · baseten
  Worklog tracing the architectural path from GPT-2 (2019) to Kimi K3 (2026, 22,580x larger), walking through decoder-only attention code and then the successive changes -- RoPE, GQA/MQA, MoE routing, and other efficiency techniques -- that took models from dense transformers to today's sparse, trillion-parameter frontier models.
- **2026-07-27** — [Making Kimi K3 tokenization 18x faster for million-token agentic workloads](<../inference/optimization/Making Kimi K3 tokenization 18x faster for million-token agentic workloads.md>) · `optimization` · baseten
  Describes Baseten's Rust-based Basetenkenizer, built to replace a Python tiktoken implementation for Kimi K3's up-to-1M-token agentic inputs, correctly distinguishing literal control-token strings from structural chat-template tokens while running up to 18x faster than tiktoken with exact token-ID parity.
- **2026-07-27** — [How to build a day-0 API for Kimi K3](<../inference/serving/How to build a day-0 API for Kimi K3.md>) · `serving` · baseten
  Walks through Baseten's five milestones for standing up a day-0 inference API for the 2.8T-parameter Kimi K3 on NVIDIA GB300 NVL72 systems: bringing up vLLM/SGLang with native MXFP4 weights, validating fidelity with Moonshot's Kimi Vendor Verifier, sweeping TP/EP/ADP configs, applying speculation/disaggregation/caching, and scaling replicas with KV-aware routing for prefix cache hit rate.
- **2026-07-23** — [H100 vs. H200 GPUs](<../inference/hardware/H100 vs. H200 GPUs.md>) · `hardware` · baseten
  Compares H100 vs H200 SXM nodes for LLM serving: an 8x H100 node has 640GB VRAM versus 1,128GB for H200 (needed to fit models like GLM 5.2 at 744B params/~755GB FP8 on one node), and covers MIG partitioning for serving small models cheaply on fractional GPUs.
- **2026-07-23** — [How to optimize LLM inference speed and reduce costs in production](<../inference/optimization/How to optimize LLM inference speed and reduce costs in production.md>) · `optimization` · baseten
  Surveys production LLM inference optimization techniques -- continuous batching, speculative decoding, KV cache reuse, quantization, and smarter routing -- for cutting latency and cost when GPUs sit idle or repeat work.
- **2026-07-23** — [How to choose an AI model: lessons from Notion and Gamma](<../product-engineering/case-studies/How to choose an AI model lessons from Notion and Gamma.md>) · `case-studies` · baseten
  Panel takeaways from Notion and Gamma on production model selection: harnesses shouldn't be model-agnostic, model switching pays for itself via A/B testing against real users, pick models per-workflow using cost-per-capability-per-second, and open-weight models plus targeted RL now compete with closed frontier models on many workloads.
- **2026-07-22** — [GLM 5.2 With Vision](<../models/multimodal/GLM 5.2 With Vision.md>) · `multimodal` · baseten
  Baseten post-trained vision onto GLM 5.2 by training only a 50M-parameter, 2-layer MLP projector (reusing Kimi K2.6's vision tower) via SFT on 66k image-QA pairs, reaching MMMU-Pro scores equivalent to Claude 4.5 Haiku (55%) without touching GLM's text weights, and observed grokking plus strong generalization to entities never seen in the alignment dataset.
- **2026-07-16** — [Real-time video generation inference on Baseten](<../inference/optimization/Real-time video generation inference on Baseten.md>) · `optimization` · baseten
  Details Baseten's real-time video inference runtime for Wan 2.2, combining four-step timestep distillation (~20x), custom kernel fusion (~1.5x), and NVFP4 quantization (~1.5x) for a combined 53.6x speedup, cutting per-clip generation from over two minutes to 2.75 seconds and cost from 5 cents to under a sixth of a cent.
- **2026-07-16** — [Fast, accurate retrieval with NVIDIA Nemotron 3 Embed](<../rag-retrieval/embeddings/Fast, accurate retrieval with NVIDIA Nemotron 3 Embed.md>) · `embeddings` · baseten
  Compares NVIDIA's Nemotron 3 Embed 8B and 1B embedding models available on Baseten: the 1B model uses pruning, distillation, and NVFP4 quantization to retain 95% of the 8B's retrieval accuracy (99% in NVFP4 on Blackwell, 2x throughput) while cutting indexing latency and serving cost; also covers a fine-tuning recipe yielding ~10% accuracy gains in 5 hours.
- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<../inference/hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-06-25** — [Live draft model training for speculative decoding](<../models/fine-tuning/Live draft model training for speculative decoding.md>) · `fine-tuning` · baseten
  Describes live draft-model training for speculative decoding systems.
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
- **2026-04-16** — [Harnesses are everything. Here's how to optimize yours.](<../agents/harness/Harnesses are everything. Here's how to optimize yours.md>) · `harness` · baseten
  Explains why agent harness design matters and how to optimize harnesses for reliable agent behavior.
- **2026-04-13** — [How to train custom EAGLE-3 heads for speculative decoding](<../models/fine-tuning/How to train custom EAGLE-3 heads for speculative decoding.md>) · `fine-tuning` · baseten
  Explains training custom EAGLE-3 heads for speculative decoding acceleration.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<../infra-platform/deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-04-06** — [Sub-3 millisecond named entity recognition (NER) inference](<../inference/optimization/Sub-3 millisecond named entity recognition (NER) inference.md>) · `optimization` · baseten
  Shows how to achieve sub-3-millisecond NER inference with optimized serving.
- **2026-03-31** — [Open-source LLM training is a mess. Here is how it all works.](<../models/fine-tuning/Open-source LLM training is a mess. Here is how it all works.md>) · `fine-tuning` · baseten
  Explains the moving pieces of open-source LLM training, including data, trainers, infrastructure, and evaluation.
- **2026-03-27** — [I spent 31 hours on the math behind TurboQuant so you don't have to](<../inference/quantization/I spent 31 hours on the math behind TurboQuant so you don't have to.md>) · `quantization` · baseten
  Mathematical deep dive into TurboQuant and its quantization behavior for LLM inference.
- **2026-02-18** — [4-Bit Quantization for Inference Optimization](<../inference/quantization/4-Bit Quantization for Inference Optimization.md>) · `quantization` · baseten
  Deep dive into 4-bit quantization for inference, covering math, tradeoffs, and production optimization.
- **2026-02-09** — [AI Model Performance Metrics Explained](<../evals-observability/monitoring/AI Model Performance Metrics Explained.md>) · `monitoring` · baseten
  Explains model performance metrics used in production inference, including latency, throughput, and quality signals.
- **2026-02-05** — [How to run LLM performance benchmarks (and why you should)](<../evals-observability/benchmark-design/How to run LLM performance benchmarks (and why you should).md>) · `benchmark-design` · baseten
  Explains how to run LLM performance benchmarks and which serving metrics matter.
- **2026-01-23** — [Open-sourcing Baseten’s suffix automaton MTP accelerator](<../inference/speculative-decoding/Open-sourcing Baseten’s suffix automaton MTP accelerator.md>) · `speculative-decoding` · baseten
  Explains a suffix-automaton MTP accelerator for improving speculative decoding acceptance rates.
- **2025-12-05** — [DeepSeek V3.2's path to GPT-5-level performance: sparse attention, RL at scale, and context reuse](<../models/reasoning/DeepSeek V3.2's path to GPT-5-level performance sparse attention, RL at scale, and context reuse.md>) · `reasoning` · baseten
  Explains DeepSeek V3.2 architecture and training choices including sparse attention, RL, and context reuse.
- **2025-11-05** — [Tool Calling in Inference](<../agents/tool-use/Tool Calling in Inference.md>) · `tool-use` · baseten
  Explains tool calling in inference and how model servers support structured external actions.
- **2025-10-23** — [DeepSeek-OCR and the Unreasonable Usefulness of Compression](<../models/multimodal/DeepSeek-OCR and the Unreasonable Usefulness of Compression.md>) · `multimodal` · baseten
  Explains DeepSeek-OCR and why compression can be useful for multimodal model workflows.
- **2025-10-16** — [2x faster inference with KV cache-aware routing](<../inference/optimization/2x faster inference with KV cache-aware routing.md>) · `optimization` · baseten
  Describes 2x faster inference through KV-cache-aware routing with NVIDIA Dynamo.
- **2025-08-15** — [Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks](<../models/fine-tuning/Fine-tuning small open-source LLMs to outperform large closed-source models by 60% on specialized tasks.md>) · `fine-tuning` · baseten
  Case study on fine-tuning small open-source LLMs to beat larger closed models on specialized tasks.
- **2025-07-15** — [Building reliable AI agents](<../agents/planning/Building reliable AI agents.md>) · `planning` · baseten
  Covers practical design patterns for building more reliable AI agents.
- **2025-06-12** — [Your client code matters: 12x higher embedding throughput with Python and Rust](<../rag-retrieval/embeddings/Your client code matters 12x higher embedding throughput with Python and Rust.md>) · `embeddings` · baseten
  Shows how client implementation choices in Python and Rust affect embedding throughput.
- **2025-04-18** — [Accelerating inference with NVIDIA B200 GPUs](<../inference/hardware/Accelerating inference with NVIDIA B200 GPUs.md>) · `hardware` · baseten
  Covers inference acceleration on NVIDIA B200 GPUs and the hardware features relevant to model serving.
- **2025-03-27** — [How we built BEI: high-throughput embedding, reranker, and classifier inference](<../rag-retrieval/embeddings/How we built BEI high-throughput embedding, reranker, and classifier inference.md>) · `embeddings` · baseten
  Deep dive into BEI, a high-throughput embedding, reranker, and classifier inference system.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<../inference/serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2025-02-07** — [Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud](<../evals-observability/benchmark-design/Testing Llama 3.3 70B inference performance on NVIDIA GH200 in Lambda Cloud.md>) · `benchmark-design` · baseten
  Tests Llama 3.3 70B inference performance on NVIDIA GH200 and discusses benchmark results.
- **2024-12-19** — [A quick introduction to speculative decoding](<../inference/speculative-decoding/A quick introduction to speculative decoding.md>) · `speculative-decoding` · baseten
  Introduces speculative decoding and the draft-target model pattern for lower LLM inference latency.
- **2024-12-19** — [How we built production-ready speculative decoding with TensorRT-LLM](<../inference/speculative-decoding/How we built production-ready speculative decoding with TensorRT-LLM.md>) · `speculative-decoding` · baseten
  Deep dive into production-ready speculative decoding with TensorRT-LLM.
- **2024-10-22** — [Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference](<../inference/hardware/Evaluating NVIDIA H200 Tensor Core GPUs for LLM inference.md>) · `hardware` · baseten
  Evaluates NVIDIA H200 GPUs for LLM inference and compares their serving performance characteristics.
- **2024-09-12** — [How to build function calling and JSON mode for open-source and fine-tuned LLMs](<../prompt-engineering/structured-output/How to build function calling and JSON mode for open-source and fine-tuned LLMs.md>) · `structured-output` · baseten
  Shows how to build function calling and JSON mode for open-source and fine-tuned LLMs.
- **2024-08-20** — [How to double tokens per second for Llama 3 with Medusa](<../inference/speculative-decoding/How to double tokens per second for Llama 3 with Medusa.md>) · `speculative-decoding` · baseten
  Explains Medusa-style speculative heads for increasing Llama 3 tokens per second.
- **2024-08-06** — [Compound AI systems explained](<../product-engineering/architecture/Compound AI systems explained.md>) · `architecture` · baseten
  Explains compound AI systems and how multiple models, tools, and control logic combine into applications.
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
