# modal

46 articles.

- **2026-07-06** — [How to price serverless GPUs](<../infra-platform/cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-06-30** — [Multi-token Residual Prediction](<../inference/optimization/Multi-token Residual Prediction.md>) · `optimization` · modal
  Explains multi-token residual prediction as an inference acceleration technique for generating multiple tokens per step.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<../inference/serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-06-22** — [Achieve state-of-the-art inference latencies with speculative decoding](<../inference/optimization/Achieve state-of-the-art inference latencies with speculative decoding.md>) · `optimization` · modal
  Explains speculative decoding for lower inference latency, including draft-model tradeoffs and production serving considerations.
- **2026-06-22** — [Introducing Modal Auto Endpoints: Optimized inference you actually own](<../inference/serving/Introducing Modal Auto Endpoints Optimized inference you actually own.md>) · `serving` · modal
  Describes auto endpoints for owned inference deployments, including optimized serving configuration and operational control.
- **2026-06-19** — [Speculation Is All You Need](<../inference/optimization/Speculation Is All You Need.md>) · `optimization` · modal
  Deep dive into speculative decoding and related techniques for improving LLM inference latency and throughput.
- **2026-06-19** — [Unpacking sandbox startup latency: why started is not ready](<../infra-platform/deployment/Unpacking sandbox startup latency why started is not ready.md>) · `deployment` · modal
  Breaks down sandbox startup latency and why ready-state semantics matter for agent and remote-execution workflows.
- **2026-05-28** — [Reinforcement learning is an infrastructure problem](<../models/fine-tuning/Reinforcement learning is an infrastructure problem.md>) · `fine-tuning` · modal
  Argues that reinforcement learning progress depends heavily on infrastructure for scheduling, iteration, and scalable experiments.
- **2026-05-19** — [Scaling reinforcement learning at Applied Compute](<../models/fine-tuning/Scaling reinforcement learning at Applied Compute.md>) · `fine-tuning` · modal
  Case study on scaling reinforcement learning workloads with elastic GPU infrastructure and faster experiment iteration.
- **2026-05-18** — [Introducing Claude Managed Agents with Modal Sandboxes](<../agents/computer-use/Introducing Claude Managed Agents with Modal Sandboxes.md>) · `computer-use` · modal
  Shows how Claude managed agents can use Modal sandboxes for isolated execution, filesystem state, and scalable agent workloads.
- **2026-05-12** — [How we achieved truly serverless GPUs](<../infra-platform/gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-21** — [Boosting multimodal inference performance by >10% with a single Python dictionary](<../inference/optimization/Boosting multimodal inference performance by 10% with a single Python dictionary.md>) · `optimization` · modal
  Describes a small configuration change that improves multimodal inference performance, with attention to batching and serving settings.
- **2026-04-20** — [Building an RL theorem-proving workflow on Modal](<../models/reasoning/Building an RL theorem-proving workflow on Modal.md>) · `reasoning` · modal
  Walks through an RL theorem-proving workflow, connecting reasoning tasks, training loops, and scalable remote execution.
- **2026-04-17** — [Making FlashAttention-4 faster for inference](<../inference/optimization/Making FlashAttention-4 faster for inference.md>) · `optimization` · modal
  Deep dive on making FlashAttention-4 faster for inference, including kernel-level and serving-performance considerations.
- **2026-04-14** — [Autoscaling Autoresearch: Give your agents elastic GPUs on Modal](<../agents/tool-use/Autoscaling Autoresearch Give your agents elastic GPUs on Modal.md>) · `tool-use` · modal
  Shows how autoresearch agents can use elastic GPU compute for parallel experiments, background jobs, and scalable tool execution.
- **2026-04-14** — [Building with Modal and the OpenAI Agents SDK](<../agents/tool-use/Building with Modal and the OpenAI Agents SDK.md>) · `tool-use` · modal
  Guide to running OpenAI Agents SDK workflows on Modal, including tool execution, deployment, and scalable background compute.
- **2026-02-25** — [Accelerating AI research that accelerates AI research](<../product-engineering/case-studies/Accelerating AI research that accelerates AI research.md>) · `case-studies` · modal
  Case study on using elastic compute to accelerate AI research workflows, including experiment throughput and infrastructure offload.
- **2026-02-23** — [Directory Snapshots: Resumable project state for Sandboxes](<../infra-platform/deployment/Directory Snapshots Resumable project state for Sandboxes.md>) · `deployment` · modal
  Introduces directory snapshots for sandbox state, enabling resumable project files across agent and remote-execution sessions.
- **2026-02-18** — [How Ramp built a full context background coding agent on Modal](<../agents/computer-use/How Ramp built a full context background coding agent on Modal.md>) · `computer-use` · modal
  Case study of a background coding agent architecture that gives agents full project context through remote sandboxes.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<../infra-platform/gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-11-20** — [Agents need good developer experience too](<../product-engineering/architecture/Agents need good developer experience too.md>) · `architecture` · modal
  Argues that agent systems need strong developer experience, covering observability, iteration loops, deployment ergonomics, and tool surfaces.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<../inference/optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-11-04** — [One-second voice-to-voice latency with Modal, Pipecat, and open models](<../inference/optimization/One-second voice-to-voice latency with Modal, Pipecat, and open models.md>) · `optimization` · modal
  Builds a low-latency voice-to-voice system with open models, covering speech pipeline latency and serving architecture.
- **2025-09-26** — [We reverse-engineered Flash Attention 4](<../inference/optimization/We reverse-engineered Flash Attention 4.md>) · `optimization` · modal
  Reverse-engineering writeup for FlashAttention-4, explaining how kernel design choices affect attention performance.
- **2025-09-22** — [Build an AI coding platform that scales to millions of monthly sessions](<../agents/computer-use/Build an AI coding platform that scales to millions of monthly sessions.md>) · `computer-use` · modal
  Describes architecture concerns for AI coding platforms that need to scale sandboxed coding sessions to large user volumes.
- **2025-09-16** — [Inside Modal Notebooks: How we built a cloud GPU notebook that boots in seconds](<../infra-platform/deployment/Inside Modal Notebooks How we built a cloud GPU notebook that boots in seconds.md>) · `deployment` · modal
  Engineering writeup on cloud GPU notebooks that boot quickly, covering startup paths, state, and execution isolation.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<../inference/optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-07-24** — [What is an AI code sandbox?](<../agents/computer-use/What is an AI code sandbox.md>) · `computer-use` · modal
  Explains AI code sandboxes as isolated execution environments for coding agents, including safety and state considerations.
- **2025-07-23** — [Transcribe speech 100x faster and 100x cheaper with open models](<../models/multimodal/Transcribe speech 100x faster and 100x cheaper with open models.md>) · `multimodal` · modal
  Shows how open speech models and batch execution can reduce transcription latency and cost at large scale.
- **2025-07-16** — [Dollars per token considered harmful](<../infra-platform/cost/Dollars per token considered harmful.md>) · `cost` · modal
  Critiques dollars-per-token as an inference cost metric and explains why workload shape, latency, and utilization matter more.
- **2025-07-02** — [How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work](<../evals-observability/evaluation/How we used evals and inference-time compute scaling to generate beautiful QR codes that actually work.md>) · `evaluation` · modal
  Case study using evals and inference-time compute scaling to generate QR codes that satisfy visual and functional constraints.
- **2025-06-18** — [Run FLUX.1-dev three times faster](<../inference/optimization/Run FLUX.1-dev three times faster.md>) · `optimization` · modal
  Explains optimizations for running FLUX.1-dev faster, including inference configuration and image-model serving tradeoffs.
- **2025-05-07** — [Linear programming for fun and profit](<../infra-platform/cost/Linear programming for fun and profit.md>) · `cost` · modal
  Shows how linear programming can allocate compute resources under constraints, useful for GPU scheduling and cost control.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<../inference/hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<../infra-platform/deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2024-12-10** — [What is LLM fine-tuning?](<../models/fine-tuning/What is LLM fine-tuning.md>) · `fine-tuning` · modal
  Overview of LLM fine-tuning concepts, when to fine-tune, and how training data and serving constraints affect the workflow.
- **2024-12-02** — [WireGuard at Modal: Static IPs for serverless containers](<../infra-platform/deployment/WireGuard at Modal Static IPs for serverless containers.md>) · `deployment` · modal
  Explains static IP support for serverless containers using WireGuard, relevant to secure networked AI deployments.
- **2024-09-24** — [Hybrid search over California embeddings with Modal, MongoDB, and Clay](<../rag-retrieval/search/Hybrid search over California embeddings with Modal, MongoDB, and Clay.md>) · `search` · modal
  Example of hybrid search over embeddings, combining vector retrieval with MongoDB and a geospatial dataset.
- **2024-09-16** — [Boost your throughput with dynamic batching](<../inference/optimization/Boost your throughput with dynamic batching.md>) · `optimization` · modal
  Explains dynamic batching for Whisper transcription workloads and how batching improves throughput without changing model behavior.
- **2024-08-05** — [Beat GPT-4o at Python by searching with 100 dumb LLaMAs](<../evals-observability/evaluation/Beat GPT-4o at Python by searching with 100 dumb LLaMAs.md>) · `evaluation` · modal
  Explores using many small Llama runs and search to improve Python benchmark performance against GPT-4o baselines.
- **2024-06-20** — [Run GPU jobs from Airflow with Modal](<../infra-platform/deployment/Run GPU jobs from Airflow with Modal.md>) · `deployment` · modal
  Shows how to run GPU jobs from Airflow, connecting existing orchestration systems to elastic AI compute.
- **2024-06-06** — [How to catch crypto miners using syscall signatures](<../product-engineering/security/How to catch crypto miners using syscall signatures.md>) · `security` · modal
  Explains detecting abusive GPU workloads with syscall signatures, a useful pattern for securing shared AI infrastructure.
- **2024-05-21** — [Create an infinite icon library by fine-tuning Stable Diffusion](<../models/fine-tuning/Create an infinite icon library by fine-tuning Stable Diffusion.md>) · `fine-tuning` · modal
  Practical example of fine-tuning Stable Diffusion for a custom image-generation domain using Modal infrastructure.
- **2024-04-26** — [Beating proprietary models with a quick fine-tune](<../models/fine-tuning/Beating proprietary models with a quick fine-tune.md>) · `fine-tuning` · modal
  Explains fine-tuning embedding models to beat proprietary baselines for a retrieval task with a compact training loop.
- **2024-03-14** — [Lambda on hard mode: Inside Modal's web infrastructure](<../infra-platform/deployment/Lambda on hard mode Inside Modal's web infrastructure.md>) · `deployment` · modal
  Deep dive into Modal web infrastructure, including serverless HTTP routing, isolation, and platform architecture.
- **2024-01-23** — [Embedding English Wikipedia in under 15 minutes](<../rag-retrieval/embeddings/Embedding English Wikipedia in under 15 minutes.md>) · `embeddings` · modal
  Walkthrough of embedding English Wikipedia quickly, covering large-scale embedding jobs, batching, and storage workflow.
