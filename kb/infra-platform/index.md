# infra-platform

45 articles.

- **2026-08-20** — [Release governance: guardrails for agents at scale](<deployment/Release governance guardrails for agents at scale.md>) · `deployment` · sierra
  Sierra describes release governance for its agent platform: Agent Checks (a linter flagging missing tools, conflicting instructions, and weak authentication on sensitive lookups), Simulations as pre-production quality gates, merge approval workflows with a dedicated Reviewer role, and split-traffic canary releases backed by immutable, instantly rollback-able snapshots.
- **2026-08-18** — [Feature flags for production AI](<deployment/Feature flags for production AI.md>) · `deployment` · pydantic
  Shows how to use Pydantic Logfire's typed managed variables as feature flags for production AI systems, letting teams target and A/B test models, prompts, and tool policies (with UsageLimits caps) without redeploying, and tying each resolved variant to OpenTelemetry traces and dashboards.
- **2026-08-17** — [A/B test models in production](<deployment/AB test models in production.md>) · `deployment` · together
  Explains Together AI's endpoint-level A/B testing for production model traffic: one control plus up to 20 variants with fixed percentage splits independent of replica autoscaling, etag-guarded ramping, sampling-key-based cohort stickiness, and promote-then-delete rollout to end an experiment. Walks through a live run ramping 95/5 to 80/20 to 50/50 and shows observed traffic shares matching the configured percents.
- **2026-07-21** — [Devin Outposts on Modal | Modal Blog](<deployment/Devin Outposts on Modal Modal Blog.md>) · `deployment` · modal
  Modal's open-source modal-devin library lets Cognition's Devin coding agent execute in user-controlled Modal Sandboxes (GPU-backed, custom images, snapshot suspend/resume) while its reasoning stays in Cognition's cloud, splitting the agent's control-plane queue from a self-hosted data-plane orchestrator and worker.
- **2026-07-15** — [Scaling to 1 million concurrent sandboxes in seconds | Modal Blog](<deployment/Scaling to 1 million concurrent sandboxes in seconds Modal Blog.md>) · `deployment` · modal
  Modal rebuilt its sandbox scheduling platform to remove central coordination (no Postgres/etcd-style datastore in the critical path), using horizontally scaled scheduling servers and worker state published to Redis streams, enabling 1 million concurrent sandboxes created in under a minute with sub-second median start latency.
- **2026-07-15** — [New in Together GPU Clusters: Reliability and control for production GPU clusters](<gpu-clusters/New in Together GPU Clusters Reliability and control for production GPU clusters.md>) · `gpu-clusters` · together
  Details operational upgrades to Together GPU Clusters: passive health checks that catch GPUs falling off the PCIe bus, Xid errors, and thermal throttling on live workloads; four automated-but-approved repair actions (reboot/reprovision/failover/remove); and a rebuilt Slurm-on-Kubernetes stack (Slinky fork) targeting crashing daemons and scheduler drift at scale.
- **2026-07-06** — [How to price serverless GPUs](<cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-06-19** — [Unpacking sandbox startup latency: why started is not ready](<deployment/Unpacking sandbox startup latency why started is not ready.md>) · `deployment` · modal
  Breaks down sandbox startup latency and why ready-state semantics matter for agent and remote-execution workflows.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-06-09** — [AI spend is the new headcount: why cost control is an observability problem](<cost/AI spend is the new headcount why cost control is an observability problem.md>) · `cost` · pydantic
  Frames LLM/agent spend as headcount-shaped (usage-scaled, salary-magnitude) rather than SaaS-shaped, arguing cost governance is really an observability problem: attribute spend per agent, per user, per session from traces (via the genai-prices dataset) and ask 'was this run worth what it cost?'.
- **2026-05-27** — [Reachy Mini goes fully local](<edge/Reachy Mini goes fully local.md>) · `edge` · huggingface
  Runs a full cascaded voice stack (VAD -> STT -> LLM -> TTS) locally on-device behind an OpenAI-Realtime-API-compatible /v1/realtime WebSocket, replacing the cloud backend for the Reachy Mini robot; argues cascades beat end-to-end S2S models on flexibility and latency and shows which local components to swap in.
- **2026-05-14** — [The Three Pillars of Voice Integration: Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure](<deployment/The Three Pillars of Voice Integration Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure.md>) · `deployment` · cresta
  Covers hybrid voice-agent integration patterns for deploying AI into existing telephony and contact-center infrastructure.
- **2026-05-12** — [Load testing: how Sierra scales for surges](<deployment/Load testing how Sierra scales for surges.md>) · `deployment` · sierra
  Explains load testing for agent systems so conversation serving can scale through traffic surges without quality or latency collapse.
- **2026-05-12** — [How we achieved truly serverless GPUs](<gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-23** — [Claude Code pricing: plans, API costs, and how to lower your bill](<cost/Claude Code pricing plans, API costs, and how to lower your bill.md>) · `cost` · fireworks
  Breaks down Claude Code cost paths (Pro $17/mo, Max 5x/20x, Team Standard/Premium, Enterprise, API) and describes routing Claude Code through Fireworks-hosted open-weight models (GLM 5.2, Kimi K2.7 Code, MiniMax M3) via FireConnect or an OpenAI-compatible harness, recommending evaluation on completion rate and repair time rather than token price alone.
- **2026-04-23** — [How to Use Transformers.js in a Chrome Extension](<edge/How to Use Transformers.js in a Chrome Extension.md>) · `edge` · huggingface
  Practical guide to running Transformers.js models inside a Chrome Manifest V3 extension: a background service worker hosts the model, a side panel provides the chat UI, and a content script handles page-level actions, with message passing between them. Covers the MV3 gotchas — service-worker lifecycle/termination, model loading and caching, and streaming tokens across the messaging boundary.
- **2026-04-21** — [Capacity without conflict: A guide to multi-tenant GPU cluster design for AI-native teams](<gpu-clusters/Capacity without conflict A guide to multi-tenant GPU cluster design for AI-native teams.md>) · `gpu-clusters` · together
  Guide to multi-tenant GPU cluster design for avoiding capacity conflicts in AI-native teams.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-03-06** — [Inference Providers vs. API Routers: where do tokens come from?](<deployment/Inference Providers vs. API Routers where do tokens come from.md>) · `deployment` · fireworks
  Distinguishes inference providers (control the GPUs serving a model) from API routers like OpenRouter (forward requests upstream), explaining that routers can improve tail latency/reliability via failover but cannot beat direct-provider median latency, and have no visibility into KV cache, batch scheduling, or kernel decisions that determine quality.
- **2026-03-04** — [Best LLM API Providers in 2026: We Reviewed 8 Options](<deployment/Best LLM API Providers in 2026 We Reviewed 8 Options.md>) · `deployment` · fireworks
  Comparison of 8 LLM inference providers (Fireworks, Groq, Together, OpenRouter, Cerebras, Hugging Face, Baseten, Modal) on criteria beyond price/token: fine-tuning support, model deprecation risk, rate limits, and billing complexity, with per-provider recommendations by use case.
- **2026-02-24** — [Optimizing Training Workloads for GPU Clusters](<gpu-clusters/Optimizing Training Workloads for GPU Clusters.md>) · `gpu-clusters` · together
  Covers optimization patterns for training workloads on GPU clusters.
- **2026-02-23** — [Directory Snapshots: Resumable project state for Sandboxes](<deployment/Directory Snapshots Resumable project state for Sandboxes.md>) · `deployment` · modal
  Introduces directory snapshots for sandbox state, enabling resumable project files across agent and remote-execution sessions.
- **2026-01-26** — [SkyPilot at Shopify: Multi-cloud GPUs without the pain (2026)](<gpu-clusters/SkyPilot at Shopify Multi-cloud GPUs without the pain (2026).md>) · `gpu-clusters` · shopify
  How Shopify uses SkyPilot to run ML training across fragmented multi-cloud GPU capacity (H200s, L4s) behind one interface, avoiding per-provider API and configuration lock-in for scarce accelerators.
- **2026-01-12** — [Inside multi-node training: How to scale model training across GPU clusters](<gpu-clusters/Inside multi-node training How to scale model training across GPU clusters.md>) · `gpu-clusters` · together
  Explains multi-node model training across GPU clusters and the coordination issues that appear at scale.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-09-16** — [Inside Modal Notebooks: How we built a cloud GPU notebook that boots in seconds](<deployment/Inside Modal Notebooks How we built a cloud GPU notebook that boots in seconds.md>) · `deployment` · modal
  Engineering writeup on cloud GPU notebooks that boot quickly, covering startup paths, state, and execution isolation.
- **2025-07-16** — [Dollars per token considered harmful](<cost/Dollars per token considered harmful.md>) · `cost` · modal
  Critiques dollars-per-token as an inference cost metric and explains why workload shape, latency, and utilization matter more.
- **2025-05-07** — [Linear programming for fun and profit](<cost/Linear programming for fun and profit.md>) · `cost` · modal
  Shows how linear programming can allocate compute resources under constraints, useful for GPU scheduling and cost control.
- **2025-03-07** — [LLM Inference on Edge: A Fun and Easy Guide to run LLMs via React Native on your Phone!](<edge/LLM Inference on Edge A Fun and Easy Guide to run LLMs via React Native on your Phone!.md>) · `edge` · huggingface
  End-to-end guide to building a React Native chat app that runs LLMs fully on-device via llama.rn/llama.cpp, covering how to pick mobile-viable models, what the GGUF quantization suffixes (Q2_K, Q4_K_M, Q8_0) actually trade off in size vs quality, and the Expo/native build plumbing.
- **2025-02-25** — [Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains](<deployment/Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains.md>) · `deployment` · cresta
  Architecture note on routing incoming voice traffic with customer-specific subdomains in a production voice platform.
- **2025-02-13** — [1 Billion Classifications](<cost/1 Billion Classifications.md>) · `cost` · huggingface
  Works through the actual cost and latency math of running 1 billion text classifications with encoder models (gte-modernbert-base), comparing batch inference vs heavy-usage serving across hardware and optimizations (ONNX, TensorRT, quantization). Includes a reproducible encoder-analysis repo and per-configuration cost tables.
- **2025-01-28** — [How Cresta Scales Real-Time Insights with ClickHouse](<deployment/How Cresta Scales Real-Time Insights with ClickHouse.md>) · `deployment` · cresta
  Architecture case study on scaling real-time AI insights with ClickHouse for high-volume conversation analytics.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2024-12-02** — [WireGuard at Modal: Static IPs for serverless containers](<deployment/WireGuard at Modal Static IPs for serverless containers.md>) · `deployment` · modal
  Explains static IP support for serverless containers using WireGuard, relevant to secure networked AI deployments.
- **2024-10-22** — [Deploying Speech-to-Speech on Hugging Face](<deployment/Deploying Speech-to-Speech on Hugging Face.md>) · `deployment` · huggingface
  Deploys HF's cascaded speech-to-speech pipeline (VAD -> STT -> LLM -> TTS, 6 languages with auto-detect) as a custom Inference Endpoint, covering the handler and websocket/streaming plumbing needed to keep an interactive voice loop responsive.
- **2024-10-09** — [Scaling AI-based Data Processing with Hugging Face + Dask](<gpu-clusters/Scaling AI-based Data Processing with Hugging Face + Dask.md>) · `gpu-clusters` · huggingface
  Uses Dask with hf.co/datasets and the fineweb-edu-classifier to run distributed, out-of-core AI data processing (Parquet chunking, GPU classifier inference) across a cloud cluster, showing how to scale a filtering/labeling pipeline past single-machine memory.
- **2024-08-19** — [Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI](<deployment/Deploy Meta Llama 3.1 405B on Google Cloud Vertex AI.md>) · `deployment` · huggingface
  Step-by-step deployment of Llama 3.1 405B (FP8 quantized) on Google Cloud Vertex AI with Hugging Face TGI on an A3 8xH100 node: registering the model, endpoint config, and running online inference with 128k context.
- **2024-08-13** — [A practitioner's guide to testing and running large GPU clusters for training generative AI models](<gpu-clusters/A practitioner's guide to testing and running large GPU clusters for training generative AI models.md>) · `gpu-clusters` · together
  Practical guide to testing and operating large GPU clusters for generative model training.
- **2024-07-22** — [WWDC 24: Running Mistral 7B with Core ML](<edge/WWDC 24 Running Mistral 7B with Core ML.md>) · `edge` · huggingface
  Reproduces Apple's WWDC'24 Mistral-7B Core ML demo: exporting a Swift-Transformers model, stateful KV cache, multifunction models for prefill vs extend, INT4 block-wise weight quantization, and running across CPU/GPU/ANE on Apple Silicon.
- **2024-06-03** — [GPUs on-demand: Not serverless, not reserved, but some third thing](<gpu-clusters/GPUs on-demand Not serverless, not reserved, but some third thing.md>) · `gpu-clusters` · fireworks
  Explains on-demand GPU infrastructure as a middle ground between serverless and reserved capacity.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-04-30** — [CI-CD for AI model deployments](<deployment/CI-CD for AI model deployments.md>) · `deployment` · baseten
  Covers CI/CD practices for AI model deployments, including versioning, release flow, and operational safety.
- **2024-03-14** — [Lambda on hard mode: Inside Modal's web infrastructure](<deployment/Lambda on hard mode Inside Modal's web infrastructure.md>) · `deployment` · modal
  Deep dive into Modal web infrastructure, including serverless HTTP routing, isolation, and platform architecture.
- **2022-12-05** — [Overcoming communication bottlenecks for decentralized training, part 2](<gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 2.md>) · `gpu-clusters` · together
  Continues the decentralized training discussion with techniques for communication-efficient optimization.
- **2022-11-30** — [Overcoming communication bottlenecks for decentralized training, part 1](<gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 1.md>) · `gpu-clusters` · together
  Explains communication bottlenecks in decentralized foundation-model training.

## Also relevant (filed elsewhere)

- **2026-08-31** — [Training API now generally available | Fireworks](<../models/reinforcement-learning/Training API now generally available Fireworks.md>) · `reinforcement-learning` · fireworks
  Fireworks details the infrastructure behind its now-GA Training API and Fireworks Lab: aligning numerical formats (BF16, block-wise FP8, NVFP4) and kernels between trainer and rollout engines, Router Replay to keep MoE expert selection consistent across rollout and backward pass, asynchronous RL that overlaps rollout generation with training, and XOR-diff plus zstd weight compression that cuts hot-load transmission bandwidth up to 10x.
- **2026-08-26** — [Best Prompt Management Tools 2026 | Pydantic Logfire](<../prompt-engineering/techniques/Best Prompt Management Tools 2026 Pydantic Logfire.md>) · `techniques` · pydantic
  Compares prompt management tools (Langfuse, LangSmith, Braintrust, PromptLayer, Agenta, Helicone, Pydantic Logfire) on how a saved prompt version reaches production: server-side vs. application-code A/B splitting, percentage rollout and targeting, and whether the serving version is recorded on the run's trace.
- **2026-08-26** — [Best Langfuse Alternatives in 2026 | Pydantic Logfire](<../evals-observability/tracing/Best Langfuse Alternatives in 2026 Pydantic Logfire.md>) · `tracing` · pydantic
  Compares Langfuse against LangSmith, Braintrust, Arize Phoenix, Helicone, Laminar, and Confident AI for LLM tracing, detailing concrete gaps: Langfuse's OTLP endpoint accepts traces but not logs/metrics, its billing meters traces/observations/scores together, and nine governance features (RBAC, audit logs, data masking) require an enterprise license key.
- **2026-08-26** — [Best OpenTelemetry Backends in 2026 | Pydantic Logfire](<../evals-observability/tracing/Best OpenTelemetry Backends in 2026 Pydantic Logfire.md>) · `tracing` · pydantic
  Compares OTLP-native observability backends (including Pydantic Logfire) on cross-signal querying, high-cardinality tolerance, self-hosting, and how each handles OpenTelemetry's still-evolving GenAI semantic conventions for model names, token counts, and tool calls in LLM/agent request paths.
- **2026-08-25** — [The two AI gateway patterns in production inference](<../product-engineering/architecture/The two AI gateway patterns in production inference.md>) · `architecture` · baseten
  Distinguishes two AI gateway architectures — access gateways for application-side multi-provider routing vs. serving gateways for model owners exposing their own models to customers — and traces how a serving gateway handles identity, routing, tenant protection, metering, and auditable request logs.
- **2026-08-21** — [GLM-5.3 vs. Claude Fable 5 on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/GLM-5.3 vs. Claude Fable 5 on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  On 113 DeepSWE coding tasks (904 rollouts), GLM-5.3 and Claude Fable 5 tie on pass@1 (69.0% vs 69.7%) but GLM-5.3 wins pass@2 (81.1% vs 77.1%) and pass@4 (87.6% vs 84.1%) while costing 5.4x less per rollout ($3.99 vs $21.63), yielding 17 vs 3 solves per $100 spent.
- **2026-08-21** — [GLM-5.3 vs. GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/GLM-5.3 vs. GPT-5.6 Sol on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  On 113 DeepSWE tasks, GPT-5.6 Sol edges GLM-5.3 on pass@1 (72.7% vs 69.0%) but GLM-5.3 ties or leads at pass@2/pass@4 (87.6% vs 85.8%) at 2.1x lower cost ($3.99 vs $8.37/rollout); cascading GLM-5.3 first and escalating to Sol on test failure solves 85.9% of tasks at $6.61 each, beating either model alone.
- **2026-08-04** — [Bringing serverless functions closer to the speed of wire | Modal Blog](<../inference/optimization/Bringing serverless functions closer to the speed of wire Modal Blog.md>) · `optimization` · modal
  Modal rewrote its Function I/O plane in Go and deployed it across 4+ regions with a routing_region flag, cutting p50 end-to-end Function Call latency by ~80ms; also covers async offloading of non-critical work, JWT-based auth refresh, and sticking with Redis 7.1 over Valkey/Redis 7.2 after observing CPU spikes under load.
- **2026-07-31** — [Autoscaling endpoints for LLM inference](<../inference/optimization/Autoscaling endpoints for LLM inference.md>) · `optimization` · together
  Together AI details its dedicated-inference autoscaler (proportional control loop, asymmetric scale-up/scale-down windows) and compares 8 scaling metrics; an experiment replaying sine-wave + spike traffic under inflight_requests, ttft-p95, and gpu_utilization policies shows only the concurrency-based inflight_requests metric caught saturation, since continuous batching hid the problem from both TTFT and GPU-utilization signals.
- **2026-07-30** — [Best AI platform for building agents on Kubernetes in 2026 | Pydantic Logfire](<../evals-observability/monitoring/Best AI platform for building agents on Kubernetes in 2026 Pydantic Logfire.md>) · `monitoring` · pydantic
  Surveys the observability landscape for AI agents running on Kubernetes, contrasting AI-native eval tools (Langfuse, LangSmith, Arize, Braintrust) that are blind to pod/node health with infra incumbents (Datadog, Grafana, New Relic, Elastic) whose LLM tracing is a bolted-on, separately-priced product; details Groundcover's eBPF zero-instrumentation approach versus Pydantic Logfire's OpenTelemetry Collector + k8sattributes processor for correlating OOMKills and CPU throttling with agent traces in one view.
- **2026-07-29** — [Agency: Secure, scalable sandboxes for agents](<../product-engineering/architecture/Agency Secure, scalable sandboxes for agents.md>) · `architecture` · sierra
  Sierra describes Agency, its Kubernetes-based agent-sandbox orchestration layer powering Pinecone and Ghostwriter: a stateless control plane provisioning per-runner pods with dedicated IAM roles and an LLM proxy for just-in-time key injection, plus a hibernation design that models each runner as a finite state machine restorable from an append-only checkpoint/event log (p50 8ms, p99 40ms round trips) to reclaim compute from the 2-4 orders of magnitude of idle agents.
- **2026-07-26** — [Kimi K3 vs GPT-5.6 Sol on DeepSWE: Cost, Coding, and Routing](<../models/benchmarks/Kimi K3 vs GPT-5.6 Sol on DeepSWE Cost, Coding, and Routing.md>) · `benchmarks` · together
  Analyzes 904 graded DeepSWE rollouts comparing Kimi K3 and GPT-5.6 Sol: Sol leads pass@1 72.7% to 68.5%, but Kimi K3 wins pass@4 (89.4% vs 85.8%) at 64% lower cost ($4.65 vs $8.37 per rollout). With only 0.46 task-level correlation between the two models, a Kimi-first cascade that escalates to Sol on test failure covers 108/113 tasks (~85.6%), beating both single models and a perfect one-shot router.
- **2026-07-14** — [Agent and LLM views in Pydantic Logfire](<../evals-observability/monitoring/Agent and LLM views in Pydantic Logfire.md>) · `monitoring` · pydantic
  Argues that non-deterministic agent workloads should be monitored on turns-per-run and tool-calling-turns-per-run at p90, not the mean, because a rare runaway retry loop (e.g. 40 tool calls, $12) hides in the average; built from the gen_ai.* spans agents already emit.
- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<../inference/hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-06-26** — [How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks](<../agents/harness/How Factory Grew Open Model Usage 2-3x in Six Months on Fireworks.md>) · `harness` · fireworks
  Factory's Droids run any coding model (frontier or open-weight) behind one harness that absorbs per-model differences in reasoning/tracing formats, tool schemas, and git-state handling; open-weight share of Factory's usage grew 2-3x in six months as models closed the capability gap at a fraction of frontier cost.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<../inference/serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-05-28** — [Reinforcement learning is an infrastructure problem](<../models/reinforcement-learning/Reinforcement learning is an infrastructure problem.md>) · `reinforcement-learning` · modal
  Argues that reinforcement learning progress depends heavily on infrastructure for scheduling, iteration, and scalable experiments.
- **2026-05-27** — [Shipping a Trillion Parameters With a Hub Bucket: Delta Weight Sync in TRL](<../models/reinforcement-learning/Shipping a Trillion Parameters With a Hub Bucket Delta Weight Sync in TRL.md>) · `reinforcement-learning` · huggingface
  In async RL the trainer must ship the full model to the inference engine every step (14 GB for a 7B, ~1 TB for a frontier model); TRL exploits the fact that ~99% of bf16 weights are bit-identical between consecutive optimizer steps and syncs only a sparse safetensors delta via a Hub bucket, cutting Qwen3-0.6B's per-step payload from 1.2 GB to 20-35 MB and enabling fully disaggregated training with no shared cluster or RDMA.
- **2026-05-25** — [Durable Runtime for Pydantic AI Agents](<../agents/harness/Durable Runtime for Pydantic AI Agents.md>) · `harness` · pydantic
  Guest post on adding a durable execution runtime to Pydantic AI agents so a harnessed run survives production failures (pod evictions, tool timeouts, crashes after expensive model calls) by persisting intermediate decisions and supporting pause/resume for offline human approval, rather than losing agent state to terminal output.
- **2026-05-20** — [The Agent Execution Tax](<../evals-observability/benchmark-design/The Agent Execution Tax.md>) · `benchmark-design` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-05-12** — [Shipping and scaling AI agents](<../agents/planning/Shipping and scaling AI agents.md>) · `planning` · sierra
  Practical guide to shipping and scaling AI agents, including lifecycle, reliability, deployment, and continuous improvement concerns.
- **2026-05-12** — [A more reliable inference layer for foundation models](<../inference/serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-04-16** — [How to Optimize MCP Tool Schemas to Reduce Token Usage](<../agents/tool-use/How to Optimize MCP Tool Schemas to Reduce Token Usage.md>) · `tool-use` · pydantic
  Shows how MCP tool definitions consume context tokens and how to engineer them for efficiency, using a Rust weather MCP server (Open-Meteo, built on the sans-IO 'mercutio' library) as the worked example for tightening the tool schemas and descriptions that Claude and other agents ingest on every request.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<../product-engineering/architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-04-02** — [Welcome Gemma 4: Frontier multimodal intelligence on device](<../models/releases/Welcome Gemma 4 Frontier multimodal intelligence on device.md>) · `releases` · huggingface
  Gemma 4 (Apache 2.0, up to 256K context) mixes alternating local sliding-window and global attention layers, dual RoPE configs, MoE (26B total / 4B active, LMArena ~1441) alongside a 31B dense model at ~1452, plus a USM-style conformer audio encoder and a variable-aspect-ratio image encoder with configurable image-token budget.
- **2026-03-31** — [Open-source LLM training is a mess. Here is how it all works.](<../models/fine-tuning/Open-source LLM training is a mess. Here is how it all works.md>) · `fine-tuning` · baseten
  Explains the moving pieces of open-source LLM training, including data, trainers, infrastructure, and evaluation.
- **2026-03-28** — [The Fine-Tuning Bottleneck Isn't the Algorithm](<../models/fine-tuning/The Fine-Tuning Bottleneck Isn't the Algorithm.md>) · `fine-tuning` · fireworks
  Explains why fine-tuning bottlenecks often come from data, evaluation, orchestration, and serving rather than algorithms alone.
- **2026-03-23** — [Frontier RL Is Cheaper Than You Think](<../models/reinforcement-learning/Frontier RL Is Cheaper Than You Think.md>) · `reinforcement-learning` · fireworks
  Argues that frontier reinforcement learning can be cost-effective with the right infrastructure and training-loop design.
- **2026-03-10** — [Keep the Tokens Flowing: Lessons from 16 Open-Source RL Libraries](<../models/reinforcement-learning/Keep the Tokens Flowing Lessons from 16 Open-Source RL Libraries.md>) · `reinforcement-learning` · huggingface
  Surveys 16 open-source async RL libraries across 7 axes (orchestration, rollout buffers, weight-sync protocols, staleness handling, partial rollouts, LoRA, distributed backends); the shared pattern is disaggregating inference and training GPU pools so neither idles, with Ray dominating orchestration (8/16) and NCCL broadcast the default weight transfer.
- **2026-03-09** — [Ulysses Sequence Parallelism: Training with Million-Token Contexts](<../models/training/Ulysses Sequence Parallelism Training with Million-Token Contexts.md>) · `training` · huggingface
  Ulysses Sequence Parallelism (from Snowflake's ALST) shards attention by heads across GPUs via all-to-all so context length scales with GPU count, enabling million-token training; explains the algorithm and its integration into Accelerate, Transformers Trainer and TRL SFTTrainer.
- **2026-02-10** — [Zero Code Instrumentation with eBPF and Logfire](<../evals-observability/tracing/Zero Code Instrumentation with eBPF and Logfire.md>) · `tracing` · pydantic
  Instrumenting services that can't take an OpenTelemetry SDK—legacy apps, compiled binaries, third-party containers—using the OpenTelemetry eBPF instrumentation agent to emit traces to Logfire with zero code changes.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<../evals-observability/benchmark-design/Quantifying infrastructure noise in agentic coding evals.md>) · `benchmark-design` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-22** — [Optimizing inference speed and costs: Lessons learned from large-scale deployments](<../inference/optimization/Optimizing inference speed and costs Lessons learned from large-scale deployments.md>) · `optimization` · together
  Lessons from optimizing inference speed and cost in large-scale deployments.
- **2025-11-25** — [Building and Deploying Production‑Grade AI Agents: Cresta’s End‑to‑End Approach](<../agents/planning/Building and Deploying Production‑Grade AI Agents Cresta’s End‑to‑End Approach.md>) · `planning` · cresta
  End-to-end guide to production AI agent deployment, including design, launch, monitoring, and operational controls.
- **2025-11-19** — [50 Trillion Tokens Per Day: The State of Agent Environments](<../agents/computer-use/50 Trillion Tokens Per Day The State of Agent Environments.md>) · `computer-use` · fireworks
  Surveys the state of agent environments, emphasizing execution scale, sandboxing, and environment design.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<../inference/optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-09-29** — [Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models](<../inference/speculative-decoding/Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models.md>) · `speculative-decoding` · huggingface
  Accelerates a Qwen3-8B agent on Intel Core Ultra by ~1.3x using speculative decoding with a depth-pruned Qwen3-0.6B int8 draft model in OpenVINO GenAI, showing how draft-model depth pruning raises acceptance rate per unit of draft cost on client hardware.
- **2025-09-04** — [Welcome EmbeddingGemma, Google's new efficient embedding model](<../rag-retrieval/embeddings/Welcome EmbeddingGemma, Google's new efficient embedding model.md>) · `embeddings` · huggingface
  EmbeddingGemma is a 308M-param multilingual embedding model: a Gemma3 backbone converted to bidirectional attention plus mean pooling and two dense layers, trained on ~320B tokens with Matryoshka Representation Learning so its 768-dim output can be truncated to 512/256/128; runs under 200 MB RAM quantized, tops MTEB under 500M, and the post shows a domain fine-tune on MIRIAD that beats models twice its size.
- **2025-09-02** — [Make your ZeroGPU Spaces go brrr with ahead-of-time compilation](<../inference/kernels/Make your ZeroGPU Spaces go brrr with ahead-of-time compilation.md>) · `kernels` · huggingface
  Uses PyTorch ahead-of-time compilation (torch.export + AOTInductor) instead of just-in-time torch.compile so short-lived ZeroGPU processes keep the compiled artifact, giving 1.3x-1.8x speedups on Flux, Wan and LTX; also covers FP8 quantization, dynamic shapes and multi-compile for varying resolutions.
- **2025-08-18** — [From Zero to GPU: A Guide to Building and Scaling Production-Ready CUDA Kernels](<../inference/hardware/From Zero to GPU A Guide to Building and Scaling Production-Ready CUDA Kernels.md>) · `hardware` · huggingface
  End-to-end guide to writing a custom CUDA kernel and shipping it with HF's kernel-builder: Nix-based reproducible builds across multiple GPU architectures and torch ABIs, PyTorch op registration and torch.compile compatibility, and distribution via `get_kernel()` from the Hub instead of compiling at install time.
- **2025-08-08** — [Accelerate ND-Parallel: A guide to Efficient Multi-GPU Training](<../models/training/Accelerate ND-Parallel A guide to Efficient Multi-GPU Training.md>) · `training` · huggingface
  Guide to combining FSDP/HSDP with tensor, context and pipeline parallelism (ND parallelism) in HF Accelerate, with config examples for Llama-3.1-8B and guidance on when each axis pays off.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<../inference/optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-06-26** — [Gemma 3n fully available in the open-source ecosystem!](<../models/releases/Gemma 3n fully available in the open-source ecosystem!.md>) · `releases` · huggingface
  Gemma 3n E2B/E4B: models with 5B and 8B actual parameters that need only 2B/4B worth of VRAM (2-3 GB) thanks to per-layer embeddings and MatFormer nesting, paired with a MobileNet-V5-300 vision encoder (60 FPS on Pixel, beating ViT-Giant with 3x fewer params) and a USM-based audio encoder processing 160ms chunks.
- **2025-06-03** — [No GPU left behind: Unlocking Efficiency with Co-located vLLM in TRL](<../models/reinforcement-learning/No GPU left behind Unlocking Efficiency with Co-located vLLM in TRL.md>) · `reinforcement-learning` · huggingface
  In TRL's GRPO setup, running vLLM in server mode leaves generation and training GPUs idling in turn; co-locating vLLM in the same process/GPUs as the trainer (sharing memory via a gpu_memory_utilization split and sleep/wake between phases) removes the idle gap, with throughput and GPU-utilization numbers across model sizes and TP configs.
- **2025-05-13** — [Blazingly fast whisper transcriptions with Inference Endpoints](<../inference/optimization/Blazingly fast whisper transcriptions with Inference Endpoints.md>) · `optimization` · huggingface
  An optimized Whisper deployment on Inference Endpoints built on vLLM, targeting Ada Lovelace GPUs (L4/L40s) to unlock torch.compile JIT kernels, CUDA graphs and a float8 KV cache — with the resulting latency/throughput gains for transcription workloads.
- **2025-03-20** — [Build vs. Buy: How Cresta Engineered Its Own Customer Data Access Solution](<../product-engineering/architecture/Build vs. Buy How Cresta Engineered Its Own Customer Data Access Solution.md>) · `architecture` · cresta
  Engineering case study on building a customer data access layer, useful for understanding integration tradeoffs in enterprise AI products.
- **2025-03-04** — [Understanding Cresta’s Voice Platform - The Voice Stack](<../models/multimodal/Understanding Cresta’s Voice Platform - The Voice Stack.md>) · `multimodal` · cresta
  Breaks down the components of a production voice AI stack, including telephony, speech, model, and orchestration layers.
- **2025-02-25** — [Minions: embracing small LMs, shifting compute on-device, and cutting cloud costs in the process](<../models/reasoning/Minions embracing small LMs, shifting compute on-device, and cutting cloud costs in the process.md>) · `reasoning` · together
  Explores using small language models and on-device compute to reduce cloud inference costs.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<../inference/hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-02-20** — [SmolVLM2: Bringing Video Understanding to Every Device](<../models/multimodal/SmolVLM2 Bringing Video Understanding to Every Device.md>) · `multimodal` · huggingface
  SmolVLM2 brings video understanding to 2.2B, 500M and 256M parameter VLMs — the smallest video LMs released — with benchmark results on Video-MME/MLVU and demos running on an iPhone via MLX and in the browser. Covers the frame-sampling/visual-token budget that makes video feasible at these sizes and the transformers/MLX fine-tuning paths.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<../inference/serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2024-12-03** — [Investing in Performance: Fine-tune small models with LLM insights - a CFM case study](<../product-engineering/case-studies/Investing in Performance Fine-tune small models with LLM insights - a CFM case study.md>) · `case-studies` · huggingface
  CFM (quant hedge fund) case study: use an LLM to label financial NER data, distill that into a compact fine-tuned model, and deploy it on Inference Endpoints — with an F1 and $/hour table showing the fine-tuned small model beating zero-shot LLM accuracy at a fraction of the inference cost.
- **2024-11-26** — [SmolVLM - small yet mighty Vision Language Model](<../models/multimodal/SmolVLM - small yet mighty Vision Language Model.md>) · `multimodal` · huggingface
  SmolVLM is a 2B VLM tuned for memory footprint: SigLIP vision encoder with aggressive pixel-shuffle visual-token compression (9x fewer tokens than Qwen2-VL), trained on the Cauldron and Docmatix, using ~5GB of GPU RAM at inference versus tens of GB for peers.
- **2024-09-25** — [Llama can now see and run on your device - welcome Llama 3.2](<../models/releases/Llama can now see and run on your device - welcome Llama 3.2.md>) · `releases` · huggingface
  Llama 3.2 adds 11B/90B vision models (cross-attention adapter over a frozen text backbone, via the new MllamaForConditionalGeneration) and 1B/3B on-device text models, plus a vision-capable Llama Guard 3 and a 1B Llama Guard for input/output safety classification.
- **2024-08-13** — [Introduction to ggml](<../inference/kernels/Introduction to ggml.md>) · `kernels` · huggingface
  A hands-on introduction to ggml — the C/C++ tensor library behind llama.cpp, whisper.cpp, ollama and LM Studio — covering its context/graph memory model, GGUF file format, quantized tensor types, and backend dispatch (CPU/CUDA/Metal) via a worked matrix-multiplication example.
- **2024-07-11** — [Using asynchronous inference in production](<../inference/serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-06-13** — [From DeepSpeed to FSDP and Back Again with Hugging Face Accelerate](<../models/training/From DeepSpeed to FSDP and Back Again with Hugging Face Accelerate.md>) · `training` · huggingface
  Debugs why Mistral-7B bf16 training converged under DeepSpeed but not FSDP: DeepSpeed silently upcasts master weights to fp32 while FSDP flattens in the model dtype; explains the mixed-precision differences and how Accelerate now aligns them.
- **2024-06-06** — [How to catch crypto miners using syscall signatures](<../product-engineering/security/How to catch crypto miners using syscall signatures.md>) · `security` · modal
  Explains detecting abusive GPU workloads with syscall signatures, a useful pattern for securing shared AI infrastructure.
- **2024-05-01** — [Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints](<../inference/serving/Powerful ASR + diarization + speculative decoding with Hugging Face Inference Endpoints.md>) · `serving` · huggingface
  Walks through a custom Inference Endpoints handler that chains Whisper-large-v3 ASR, Pyannote diarization and speculative decoding (with a distil-whisper assistant model and SDPA/Flash Attention 2) into one deployable pipeline, including the pre/post-processing needed to align transcript timestamps with speaker turns.
- **2024-03-28** — [Using fractional H100 GPUs for efficient model serving](<../inference/serving/Using fractional H100 GPUs for efficient model serving.md>) · `serving` · baseten
  Explains fractional H100 usage for efficient model serving and better GPU utilization.
- **2024-02-20** — [Why GPU utilization matters for model inference](<../inference/hardware/Why GPU utilization matters for model inference.md>) · `hardware` · baseten
  Explains why GPU utilization is central to inference cost and performance.
- **2024-02-16** — [Synthetic data: save money, time and carbon with open source](<../models/fine-tuning/Synthetic data save money, time and carbon with open source.md>) · `fine-tuning` · huggingface
  Uses Mixtral-8x7B to generate synthetic labels that train a small RoBERTa classifier for investor sentiment: matches GPT-4 accuracy (94%, 0.94 F1 macro) while costing ~$2.7 vs $3061 to label the corpus, at 0.13s latency and ~0.12kg CO2.
- **2024-02-01** — [Hugging Face Text Generation Inference available for AWS Inferentia2](<../inference/hardware/Hugging Face Text Generation Inference available for AWS Inferentia2.md>) · `hardware` · huggingface
  Deploys Zephyr-7B with TGI on AWS Inferentia2 via SageMaker as a GPU alternative, covering the Neuronx TGI image, the ahead-of-time model compilation/tracing step that Neuron requires (fixed batch size and sequence length), and how tensor parallelism plus continuous batching carry over.
- **2024-01-23** — [Embedding English Wikipedia in under 15 minutes](<../rag-retrieval/embeddings/Embedding English Wikipedia in under 15 minutes.md>) · `embeddings` · modal
  Walkthrough of embedding English Wikipedia quickly, covering large-scale embedding jobs, batching, and storage workflow.
- **2023-11-28** — [NVIDIA A10 vs A10G for ML model inference](<../inference/hardware/NVIDIA A10 vs A10G for ML model inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A10G GPUs for model inference performance and cost.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<../inference/hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<../inference/hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.
- **2021-06-25** — [Inside Cresta's Platform: Auth, APIs, and Scaling](<../product-engineering/architecture/Inside Cresta's Platform Auth, APIs, and Scaling.md>) · `architecture` · cresta
  Cresta's platform re-architecture into four layers (client, edge orchestration, service/platform including ML services, and infra), motivated by supporting third-party API consumers alongside the first-party web app. Covers microservice scaffolding that unifies logging, config, CI/CD and testing, plus migrating auth and config off Netlify lambdas into dedicated services.
