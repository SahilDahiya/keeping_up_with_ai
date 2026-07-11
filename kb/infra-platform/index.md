# infra-platform

66 articles.

- **2026-07-09** — [Trace before you migrate: Measuring Kubernetes bottlenecks in AI agent sandboxes](<deployment/Trace before you migrate Measuring Kubernetes bottlenecks in AI agent sandboxes.md>) · `deployment` · arize
  Shows how tracing can diagnose Kubernetes bottlenecks in AI agent sandboxes before migration decisions.
- **2026-07-06** — [How to price serverless GPUs](<cost/How to price serverless GPUs.md>) · `cost` · modal
  Explains serverless GPU pricing from utilization, scheduling, and workload-shape constraints rather than simple hourly rates.
- **2026-07-02** — [Your coding agent bill doubled. Here’s how to fix it.](<cost/Your coding agent bill doubled. Here’s how to fix it.md>) · `cost` · langchain
  Practical guide to reducing coding-agent spend through model choice, caching, harness tuning, and workflow design.
- **2026-07-01** — [Model subsidies are ending. What do you do now?](<cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-24** — [Frontier-lab training infrastructure, now as a service](<gpu-clusters/Frontier-lab training infrastructure, now as a service.md>) · `gpu-clusters` · fireworks
  Describes training infrastructure as a service for frontier-lab workloads, including scale, orchestration, and reliability needs.
- **2026-06-19** — [Why AI token costs don't tell you if your AI is working](<cost/Why AI token costs don't tell you if your AI is working.md>) · `cost` · arize
  Explains why token cost alone is an incomplete production metric and how quality, latency, and outcomes must be measured together.
- **2026-06-19** — [Temporary Cloudflare Accounts for AI agents](<deployment/Temporary Cloudflare Accounts for AI agents.md>) · `deployment` · cloudflare-ai
  Temporary Cloudflare Accounts let agents run 'wrangler deploy --temporary' to ship a Worker with zero signup — a 60-minute claimable account with auto-provisioned API token — with Wrangler itself prompting agents about the flag, removing human-built OAuth/dashboard friction from the deploy loop.
- **2026-06-19** — [Unpacking sandbox startup latency: why started is not ready](<deployment/Unpacking sandbox startup latency why started is not ready.md>) · `deployment` · modal
  Breaks down sandbox startup latency and why ready-state semantics matter for agent and remote-execution workflows.
- **2026-06-17** — [How to test agent cost-efficiency with Braintrust](<cost/How to test agent cost-efficiency with Braintrust.md>) · `cost` · braintrust
  Explains how to test agent cost-efficiency by measuring task success against token, model, and tool-use costs.
- **2026-06-17** — [Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue](<deployment/Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue.md>) · `deployment` · cloudflare-ai
  Describes a three-layer production agent stack — framework (Flue, from the Astro team, built on the Pi harness), harness (Project Think, Pi), and runtime (Cloudflare Agents SDK) — with durable execution, dynamic code execution, and a durable filesystem exposed to any harness.
- **2026-06-15** — [How LangChain Made Coding Agent Spend Predictable](<cost/How LangChain Made Coding Agent Spend Predictable.md>) · `cost` · langchain
  Explains how LangChain made coding-agent spend more predictable using constraints, monitoring, and workflow-level cost controls.
- **2026-06-12** — [Rolling deployments for zero-downtime model updates](<deployment/Rolling deployments for zero-downtime model updates.md>) · `deployment` · baseten
  Explains rolling deployments for zero-downtime model updates in production serving systems.
- **2026-06-05** — [Your AI bill is out of control. Cloudflare can fix it now.](<cost/Your AI bill is out of control. Cloudflare can fix it now.md>) · `cost` · cloudflare-ai
  AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven budgets and model routing via Cloudflare Access, so enterprises can attribute LLM spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for interns) instead of one opaque shared API key.
- **2026-06-04** — [Model Neutrality: Why Avoiding AI Vendor Lock-In Matters](<deployment/Model Neutrality Why Avoiding AI Vendor Lock-In Matters.md>) · `deployment` · langchain
  Explains model neutrality and why avoiding AI vendor lock-in matters for provider routing, cost control, and long-term architecture.
- **2026-05-26** — [Mission Control for Self-Hosted LangSmith on Kubernetes](<deployment/Mission Control for Self-Hosted LangSmith on Kubernetes.md>) · `deployment` · langchain
  Guide to operating self-hosted LangSmith on Kubernetes, covering deployment, operations, and control-plane concerns.
- **2026-05-19** — [Announcing Claude Managed Agents on Cloudflare](<deployment/Announcing Claude Managed Agents on Cloudflare.md>) · `deployment` · cloudflare-ai
  Cloudflare-Anthropic integration running Claude Managed Agents against Cloudflare Sandboxes: the agent loop stays on the Claude Platform while Cloudflare provides microVM or isolate sandboxes, credential-injecting proxies, private service connectivity, browser session audit trails, and per-agent email.
- **2026-05-14** — [The Three Pillars of Voice Integration: Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure](<deployment/The Three Pillars of Voice Integration Building Hybrid AI Contact Centers That Work With Your Existing Infrastructure.md>) · `deployment` · cresta
  Covers hybrid voice-agent integration patterns for deploying AI into existing telephony and contact-center infrastructure.
- **2026-05-13** — [We built SmithDB, the data layer for agent observability](<deployment/We built SmithDB, the data layer for agent observability.md>) · `deployment` · langchain
  Introduces SmithDB as a data layer for agent observability, optimized for storing and querying trace-heavy workloads.
- **2026-05-12** — [Load testing: how Sierra scales for surges](<deployment/Load testing how Sierra scales for surges.md>) · `deployment` · sierra
  Explains load testing for agent systems so conversation serving can scale through traffic surges without quality or latency collapse.
- **2026-05-12** — [How we achieved truly serverless GPUs](<gpu-clusters/How we achieved truly serverless GPUs.md>) · `gpu-clusters` · modal
  Explains Modal’s serverless GPU architecture, including scheduling, cold starts, isolation, and utilization constraints.
- **2026-04-21** — [Capacity without conflict: A guide to multi-tenant GPU cluster design for AI-native teams](<gpu-clusters/Capacity without conflict A guide to multi-tenant GPU cluster design for AI-native teams.md>) · `gpu-clusters` · together
  Guide to multi-tenant GPU cluster design for avoiding capacity conflicts in AI-native teams.
- **2026-04-09** — [How the Baseten Delivery Network (BDN) makes cold starts fast](<deployment/How the Baseten Delivery Network (BDN) makes cold starts fast.md>) · `deployment` · baseten
  Deep dive into how the Baseten Delivery Network reduces cold starts for model serving.
- **2026-03-19** — [Introducing the Baseten Delivery Network: Fast cold starts for big models](<deployment/Introducing the Baseten Delivery Network Fast cold starts for big models.md>) · `deployment` · baseten
  Introduces the Baseten Delivery Network for reducing cold starts when serving large models.
- **2026-03-16** — [Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider](<deployment/Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider.md>) · `deployment` · arize
  Announces native NVIDIA NIM support in Arize AX so teams can connect hosted model providers into evaluation and observability workflows.
- **2026-03-10** — [Simplifying Langfuse for Scale](<deployment/Simplifying Langfuse for Scale.md>) · `deployment` · langfuse
  Architecture case study on simplifying Langfuse for scale, covering operational complexity, storage and compute boundaries, and reliability improvements.
- **2026-02-24** — [Optimizing Training Workloads for GPU Clusters](<gpu-clusters/Optimizing Training Workloads for GPU Clusters.md>) · `gpu-clusters` · together
  Covers optimization patterns for training workloads on GPU clusters.
- **2026-02-23** — [Directory Snapshots: Resumable project state for Sandboxes](<deployment/Directory Snapshots Resumable project state for Sandboxes.md>) · `deployment` · modal
  Introduces directory snapshots for sandbox state, enabling resumable project files across agent and remote-execution sessions.
- **2026-01-12** — [Inside multi-node training: How to scale model training across GPU clusters](<gpu-clusters/Inside multi-node training How to scale model training across GPU clusters.md>) · `gpu-clusters` · together
  Explains multi-node model training across GPU clusters and the coordination issues that appear at scale.
- **2025-12-28** — [Keeping 20,000 GPUs healthy](<gpu-clusters/Keeping 20,000 GPUs healthy.md>) · `gpu-clusters` · modal
  Describes operational practices for keeping a large GPU fleet healthy, including failure detection and reliability management.
- **2025-11-20** — [Incident Report for Nov 18, 2025](<deployment/Incident Report for Nov 18, 2025.md>) · `deployment` · langfuse
  Incident report with reliability lessons for production observability infrastructure, including failure analysis and operational follow-up.
- **2025-09-17** — [adb Benchmarks](<deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-09-16** — [Inside Modal Notebooks: How we built a cloud GPU notebook that boots in seconds](<deployment/Inside Modal Notebooks How we built a cloud GPU notebook that boots in seconds.md>) · `deployment` · modal
  Engineering writeup on cloud GPU notebooks that boot quickly, covering startup paths, state, and execution isolation.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-07-16** — [Dollars per token considered harmful](<cost/Dollars per token considered harmful.md>) · `cost` · modal
  Critiques dollars-per-token as an inference cost metric and explains why workload shape, latency, and utilization matter more.
- **2025-06-23** — [How we built Multi-cloud Capacity Management (MCM)](<gpu-clusters/How we built Multi-cloud Capacity Management (MCM).md>) · `gpu-clusters` · baseten
  Engineering writeup on building multi-cloud capacity management for inference infrastructure.
- **2025-06-09** — [How Baseten multi-cloud capacity management unifies deployments](<gpu-clusters/How Baseten multi-cloud capacity management unifies deployments.md>) · `gpu-clusters` · baseten
  Explains multi-cloud capacity management for unifying cloud, self-hosted, and hybrid inference deployments.
- **2025-05-19** — [Arize AI Accelerates Enterprise AI Adoption On-Premises With NVIDIA](<deployment/Arize AI Accelerates Enterprise AI Adoption On-Premises With NVIDIA.md>) · `deployment` · arize
  Announcement of Arize and NVIDIA collaboration for on-prem enterprise AI deployment and observability infrastructure.
- **2025-05-07** — [Linear programming for fun and profit](<cost/Linear programming for fun and profit.md>) · `cost` · modal
  Shows how linear programming can allocate compute resources under constraints, useful for GPU scheduling and cost control.
- **2025-03-13** — [Hugging Face and Langfuse: 5 Ways to use them Together](<deployment/Hugging Face and Langfuse 5 Ways to use them Together.md>) · `deployment` · langfuse
  Shows ways to combine Hugging Face workflows with Langfuse for model experimentation, tracing, evaluation, and deployment feedback loops.
- **2025-03-03** — [Brainstore: the database designed for the AI engineering era](<deployment/Brainstore the database designed for the AI engineering era.md>) · `deployment` · braintrust
  Introduces Brainstore as a database for AI engineering workloads, optimized for traces, evals, logs, and large-scale observability queries.
- **2025-02-25** — [Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains](<deployment/Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains.md>) · `deployment` · cresta
  Architecture note on routing incoming voice traffic with customer-specific subdomains in a production voice platform.
- **2025-01-28** — [How Cresta Scales Real-Time Insights with ClickHouse](<deployment/How Cresta Scales Real-Time Insights with ClickHouse.md>) · `deployment` · cresta
  Architecture case study on scaling real-time AI insights with ClickHouse for high-volume conversation analytics.
- **2025-01-28** — [Memory snapshots: Checkpoint and restore for sub-second startup](<deployment/Memory snapshots Checkpoint and restore for sub-second startup.md>) · `deployment` · modal
  Explains memory snapshots as checkpoint/restore infrastructure for faster startup in serverless AI workloads.
- **2025-01-08** — [Our approach to hybrid deployment](<deployment/Our approach to hybrid deployment.md>) · `deployment` · braintrust
  Describes a hybrid deployment approach for AI observability, balancing managed services with customer-controlled data and infrastructure boundaries.
- **2024-12-02** — [WireGuard at Modal: Static IPs for serverless containers](<deployment/WireGuard at Modal Static IPs for serverless containers.md>) · `deployment` · modal
  Explains static IP support for serverless containers using WireGuard, relevant to secure networked AI deployments.
- **2024-11-17** — [From Zero to Scale: Langfuse's Infrastructure Evolution](<deployment/From Zero to Scale Langfuse's Infrastructure Evolution.md>) · `deployment` · langfuse
  Case study of Langfuse infrastructure evolution from early product to scale, including data architecture, observability workloads, and operational tradeoffs.
- **2024-09-23** — [Should you use an LLM Proxy to Build your Application?](<deployment/Should you use an LLM Proxy to Build your Application.md>) · `deployment` · langfuse
  Explains the LLM proxy pattern for AI applications, including provider abstraction, centralized logging, key management, routing, and governance tradeoffs.
- **2024-08-13** — [A practitioner's guide to testing and running large GPU clusters for training generative AI models](<gpu-clusters/A practitioner's guide to testing and running large GPU clusters for training generative AI models.md>) · `gpu-clusters` · together
  Practical guide to testing and operating large GPU clusters for generative model training.
- **2024-06-20** — [Run GPU jobs from Airflow with Modal](<deployment/Run GPU jobs from Airflow with Modal.md>) · `deployment` · modal
  Shows how to run GPU jobs from Airflow, connecting existing orchestration systems to elastic AI compute.
- **2024-06-03** — [GPUs on-demand: Not serverless, not reserved, but some third thing](<gpu-clusters/GPUs on-demand Not serverless, not reserved, but some third thing.md>) · `gpu-clusters` · fireworks
  Explains on-demand GPU infrastructure as a middle ground between serverless and reserved capacity.
- **2024-05-30** — [Control plane vs workload plane in model serving infrastructure](<deployment/Control plane vs workload plane in model serving infrastructure.md>) · `deployment` · baseten
  Explains the control-plane/workload-plane split in model serving infrastructure.
- **2024-05-21** — [Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog](<deployment/Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog.md>) · `deployment` · arize
  Describes Arize integration with Microsoft Azure AI Model Catalog for LLM evaluation and observability in Azure-hosted development workflows.
- **2024-04-30** — [CI-CD for AI model deployments](<deployment/CI-CD for AI model deployments.md>) · `deployment` · baseten
  Covers CI/CD practices for AI model deployments, including versioning, release flow, and operational safety.
- **2024-03-14** — [Lambda on hard mode: Inside Modal's web infrastructure](<deployment/Lambda on hard mode Inside Modal's web infrastructure.md>) · `deployment` · modal
  Deep dive into Modal web infrastructure, including serverless HTTP routing, isolation, and platform architecture.
- **2023-11-27** — [Open sourcing the AI proxy](<deployment/Open sourcing the AI proxy.md>) · `deployment` · braintrust
  Open-source AI proxy notes focused on provider routing, logging, credentials, access control, and observability for model calls.
- **2023-11-20** — [AI proxy: fostering a more open ecosystem](<deployment/AI proxy fostering a more open ecosystem.md>) · `deployment` · braintrust
  Introduces an AI proxy pattern for routing model calls across providers while centralizing logging, credentials, access control, and production visibility.
- **2023-09-19** — [Arize AI Debuts Integration with Anyscale Endpoints](<deployment/Arize AI Debuts Integration with Anyscale Endpoints.md>) · `deployment` · arize
  Announcement and integration walkthrough for using Arize with Anyscale Endpoints to monitor hosted open-model inference.
- **2023-02-17** — [Technical deep dive: Truss live reload](<deployment/Technical deep dive Truss live reload.md>) · `deployment` · baseten
  Technical deep dive into Truss live reload and faster model-server development loops.
- **2023-01-08** — [Self-serve feature platforms: architectures and APIs](<deployment/Self-serve feature platforms architectures and APIs.md>) · `deployment` · chip-huyen
  Breaks down self-serve feature-platform architecture and APIs, covering feature definitions, pipelines, storage, discovery, and ergonomics for ML teams that need reusable production features.
- **2022-12-08** — [Accelerating model deployment: 100X faster dev loops with development deployments](<deployment/Accelerating model deployment 100X faster dev loops with development deployments.md>) · `deployment` · baseten
  Explains development deployments and draft models as a way to shorten model deployment iteration loops.
- **2022-12-05** — [Overcoming communication bottlenecks for decentralized training, part 2](<gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 2.md>) · `gpu-clusters` · together
  Continues the decentralized training discussion with techniques for communication-efficient optimization.
- **2022-11-30** — [Overcoming communication bottlenecks for decentralized training, part 1](<gpu-clusters/Overcoming communication bottlenecks for decentralized training, part 1.md>) · `gpu-clusters` · together
  Explains communication bottlenecks in decentralized foundation-model training.
- **2022-08-03** — [Introduction to streaming for data scientists](<deployment/Introduction to streaming for data scientists.md>) · `deployment` · chip-huyen
  Introduces stream processing for ML systems, comparing batch and streaming architectures, event-time semantics, joins, windows, and why streaming underpins real-time features.
- **2021-09-13** — [Why data scientists shouldn’t need to know Kubernetes](<deployment/Why data scientists shouldn’t need to know Kubernetes.md>) · `deployment` · chip-huyen
  Argues that data scientists should consume self-serve infrastructure abstractions rather than raw Kubernetes, outlining platform requirements for development, deployment, and operational ownership.
- **2021-06-07** — [Arize Partners with UbiOps to Accelerate Model Building & Deployment](<deployment/Arize Partners with UbiOps to Accelerate Model Building & Deployment.md>) · `deployment` · arize
  Partnership announcement with UbiOps focused on connecting model building, deployment, and observability workflows.
- **2020-06-22** — [What I learned from looking at 200 machine learning tools](<deployment/What I learned from looking at 200 machine learning tools.md>) · `deployment` · chip-huyen
  Analyzes 200 machine learning tools and maps the MLOps stack across data pipelines, training, deployment, monitoring, labeling, and orchestration for production ML systems.

## Also relevant (filed elsewhere)

- **2026-07-09** — [The new GPT-5.6 family: Luna, Terra, Sol](<../models/releases/The new GPT-5.6 family Luna, Terra, Sol.md>) · `releases` · simon-willison
  Notes on the GPT-5.6 Luna, Terra, and Sol release, including pricing, million-token context, agentic benchmark claims, SWE-Bench Pro caveats, programmatic tool calling, subagents, and prompt-cache breakpoints.
- **2026-07-07** — [How Schneider Electric Built Their LLMOps Foundations With LangSmith](<../product-engineering/case-studies/How Schneider Electric Built Their LLMOps Foundations With LangSmith.md>) · `case-studies` · langchain
  Schneider Electric case study on building enterprise LLMOps foundations with LangSmith at scale.
- **2026-07-03** — [Fable's judgement](<../agents/multi-agent/Fable's judgement.md>) · `multi-agent` · simon-willison
  Practical coding-agent pattern for delegating implementation work to cheaper subagents while reserving the main model for judgment, review, synthesis, and model-selection decisions.
- **2026-07-02** — [H100 vs. H200 vs. B200: which GPU should you use?](<../inference/hardware/H100 vs. H200 vs. B200 which GPU should you use.md>) · `hardware` · baseten
  Compares H100, H200, and B200 GPUs for choosing hardware for inference workloads.
- **2026-07-01** — [Announcing the Monetization Gateway: charge for any resource behind Cloudflare via x402](<../industry/business/Announcing the Monetization Gateway charge for any resource behind Cloudflare via x402.md>) · `business` · cloudflare-ai
  Announces the Monetization Gateway: charge agents for any Cloudflare-protected resource (pages, datasets, APIs, MCP tools) with payment verification enforced at the edge, settling sub-cent stablecoin micropayments over the x402 protocol now stewarded by a 25+ member Linux Foundation x402 Foundation.
- **2026-06-30** — [What’s new in Claude Sonnet 5](<../models/releases/What’s new in Claude Sonnet 5.md>) · `releases` · simon-willison
  Developer-focused notes on Claude Sonnet 5 covering adaptive thinking defaults, removed sampling parameters, million-token context, pricing/tokenizer changes, and comparative tokenization cost across document types.
- **2026-06-30** — [Using OSS models to save on inference costs without cutting quality](<../inference/serving/Using OSS models to save on inference costs without cutting quality.md>) · `serving` · braintrust
  Explains using open-source models to reduce inference cost without sacrificing quality, emphasizing eval-driven model selection and serving tradeoffs.
- **2026-06-26** — [Prompt Caching with Deep Agents](<../prompt-engineering/context-engineering/Prompt Caching with Deep Agents.md>) · `context-engineering` · langchain
  Explains prompt caching for Deep Agents and how cache-aware context design reduces latency and cost for repeated agent work.
- **2026-06-25** — [Proxying inference requests in 6ms with Pingora, Envoy, and Spanner](<../inference/serving/Proxying inference requests in 6ms with Pingora, Envoy, and Spanner.md>) · `serving` · modal
  Explains low-latency inference proxying with Pingora, Envoy, and Spanner, including request-routing architecture.
- **2026-06-25** — [How we built SmithDB’s inverted index for full-text search](<../rag-retrieval/search/How we built SmithDB’s inverted index for full-text search.md>) · `search` · langchain
  Deep dive on constructing and querying SmithDB's inverted index for full-text search over observability data.
- **2026-06-22** — [Introducing Modal Auto Endpoints: Optimized inference you actually own](<../inference/serving/Introducing Modal Auto Endpoints Optimized inference you actually own.md>) · `serving` · modal
  Describes auto endpoints for owned inference deployments, including optimized serving configuration and operational control.
- **2026-06-22** — [Designing the runtime for Langfuse code evaluators](<../evals-observability/testing/Designing the runtime for Langfuse code evaluators.md>) · `testing` · langfuse
  Design deep dive on the runtime for Langfuse code evaluators, covering execution isolation, evaluator lifecycle, and safe scalable scoring infrastructure.
- **2026-06-16** — [How to use Braintrust with any framework or provider](<../evals-observability/tracing/How to use Braintrust with any framework or provider.md>) · `tracing` · braintrust
  Integration guide for capturing Braintrust traces and evals across different AI frameworks and model providers without locking the application stack to one SDK.
- **2026-06-15** — [Building a 100x Cheaper Trace Judge with Fireworks](<../evals-observability/evaluation/Building a 100x Cheaper Trace Judge with Fireworks.md>) · `evaluation` · langchain
  Shows how to build a lower-cost trace judge with Fireworks, focusing on evaluator cost reduction while preserving useful scoring quality.
- **2026-06-15** — [One agent, two trace destinations: Arize AX + Databricks Unity Catalog](<../evals-observability/tracing/One agent, two trace destinations Arize AX + Databricks Unity Catalog.md>) · `tracing` · arize
  Shows how a single agent can emit traces to multiple destinations, highlighting interoperability concerns for observability stacks.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<../evals-observability/tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-10** — [Full Text Search in SmithDB: Designing an Inverted Index for Object Storage](<../rag-retrieval/search/Full Text Search in SmithDB Designing an Inverted Index for Object Storage.md>) · `search` · langchain
  Architecture writeup on designing an inverted index for object storage in SmithDB, motivated by full-text search over agent traces.
- **2026-06-05** — [How we use agents to review production infrastructure](<../product-engineering/case-studies/How we use agents to review production infrastructure.md>) · `case-studies` · langfuse
  Case study of using agents to review production infrastructure, including operational workflows, review boundaries, and human oversight.
- **2026-06-04** — [Fault Tolerance in LangGraph: Retries, Timeouts and Error Handlers](<../agents/planning/Fault Tolerance in LangGraph Retries, Timeouts and Error Handlers.md>) · `planning` · langchain
  Explains fault tolerance in LangGraph with retries, timeouts, and error handlers for more reliable long-running agents.
- **2026-06-04** — [How we made continuous trace intelligence possible at scale](<../evals-observability/tracing/How we made continuous trace intelligence possible at scale.md>) · `tracing` · braintrust
  Architecture deep dive on continuous trace intelligence at scale, including how production traces are clustered and surfaced for analysis.
- **2026-06-04** — [Model Neutrality: Why Avoiding AI Vendor Lock-In Matters](<deployment/Model Neutrality Why Avoiding AI Vendor Lock-In Matters.md>) · `deployment` · langchain
  Explains model neutrality and why avoiding AI vendor lock-in matters for provider routing, cost control, and long-term architecture.
- **2026-05-28** — [Reinforcement learning is an infrastructure problem](<../models/fine-tuning/Reinforcement learning is an infrastructure problem.md>) · `fine-tuning` · modal
  Argues that reinforcement learning progress depends heavily on infrastructure for scheduling, iteration, and scalable experiments.
- **2026-05-20** — [The Agent Execution Tax](<../evals-observability/evaluation/The Agent Execution Tax.md>) · `evaluation` · fireworks
  Analyzes browser-agent runs to show how reliability, latency, and cost compound into task-level execution tax.
- **2026-05-19** — [Scaling reinforcement learning at Applied Compute](<../models/fine-tuning/Scaling reinforcement learning at Applied Compute.md>) · `fine-tuning` · modal
  Case study on scaling reinforcement learning workloads with elastic GPU infrastructure and faster experiment iteration.
- **2026-05-18** — [Introducing Claude Managed Agents with Modal Sandboxes](<../agents/computer-use/Introducing Claude Managed Agents with Modal Sandboxes.md>) · `computer-use` · modal
  Shows how Claude managed agents can use Modal sandboxes for isolated execution, filesystem state, and scalable agent workloads.
- **2026-05-12** — [Delta Channels: How We’re Evolving our Runtime for Long-Running Agents](<../agents/planning/Delta Channels How We’re Evolving our Runtime for Long-Running Agents.md>) · `planning` · langchain
  Describes Delta Channels as an evolution of the LangGraph runtime for long-running agents, focused on durable state and runtime communication.
- **2026-05-12** — [Shipping and scaling AI agents](<../agents/planning/Shipping and scaling AI agents.md>) · `planning` · sierra
  Practical guide to shipping and scaling AI agents, including lifecycle, reliability, deployment, and continuous improvement concerns.
- **2026-05-12** — [A more reliable inference layer for foundation models](<../inference/serving/A more reliable inference layer for foundation models.md>) · `serving` · sierra
  Explains Sierra's inference-layer reliability strategy for foundation models, including routing, redundancy, and serving behavior preservation under provider failures.
- **2026-04-30** — [Agents can now create Cloudflare accounts, buy domains, and deploy](<../agents/tool-use/Agents can now create Cloudflare accounts, buy domains, and deploy.md>) · `tool-use` · cloudflare-ai
  Via a protocol co-designed with Stripe for Stripe Projects, coding agents can now provision a Cloudflare account, start a paid subscription, register a domain, and receive an API token to deploy — end-to-end with humans only approving payment and terms of service.
- **2026-04-30** — [Prompt templates as configs, not code](<../prompt-engineering/context-engineering/Prompt templates as configs, not code.md>) · `context-engineering` · arize
  Argues for treating prompt templates as configuration, improving iteration, versioning, and deployment safety.
- **2026-04-23** — [How we built RBAC that scales for the enterprise](<../product-engineering/security/How we built RBAC that scales for the enterprise.md>) · `security` · baseten
  Engineering writeup on building RBAC for enterprise AI infrastructure and balancing autonomy with control.
- **2026-04-21** — [Capacity without conflict: A guide to multi-tenant GPU cluster design for AI-native teams](<gpu-clusters/Capacity without conflict A guide to multi-tenant GPU cluster design for AI-native teams.md>) · `gpu-clusters` · together
  Guide to multi-tenant GPU cluster design for avoiding capacity conflicts in AI-native teams.
- **2026-04-20** — [Building an RL theorem-proving workflow on Modal](<../models/reasoning/Building an RL theorem-proving workflow on Modal.md>) · `reasoning` · modal
  Walks through an RL theorem-proving workflow, connecting reasoning tasks, training loops, and scalable remote execution.
- **2026-04-20** — [The AI engineering stack we built internally — on the platform we ship](<../product-engineering/case-studies/The AI engineering stack we built internally — on the platform we ship.md>) · `case-studies` · cloudflare-ai
  Eleven-month buildout of Cloudflare's internal AI engineering stack on its own products: 3,683 users (93% of R&D), 47.95M AI requests and 241B tokens/month through AI Gateway, an MCP Server Portal with single OAuth, and merge requests nearly doubling from ~5,600 to 10,952/week.
- **2026-04-20** — [Building the agentic cloud: everything we launched during Agents Week 2026](<../industry/announcements/Building the agentic cloud everything we launched during Agents Week 2026.md>) · `announcements` · cloudflare-ai
  Roundup of every Agents Week 2026 launch for Cloudflare's 'agentic cloud': Artifacts (Git-compatible versioned storage), Sandboxes with Outbound Workers for zero-trust egress, Durable Object Facets, and Workflows rearchitected to 50,000 concurrency for durable background agents.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<../evals-observability/tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-04-14** — [Autoscaling Autoresearch: Give your agents elastic GPUs on Modal](<../agents/tool-use/Autoscaling Autoresearch Give your agents elastic GPUs on Modal.md>) · `tool-use` · modal
  Shows how autoresearch agents can use elastic GPU compute for parallel experiments, background jobs, and scalable tool execution.
- **2026-04-14** — [Building with Modal and the OpenAI Agents SDK](<../agents/tool-use/Building with Modal and the OpenAI Agents SDK.md>) · `tool-use` · modal
  Guide to running OpenAI Agents SDK workflows on Modal, including tool execution, deployment, and scalable background compute.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<../product-engineering/architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-04-06** — [How Brainstore works: architecture for AI observability at scale](<../evals-observability/monitoring/How Brainstore works architecture for AI observability at scale.md>) · `monitoring` · braintrust
  Deep dive into Brainstore's architecture for AI observability at scale, covering storage, indexing, query patterns, and trace/log workloads.
- **2026-03-31** — [Baseten Training: an autoresearch substrate](<../models/fine-tuning/Baseten Training an autoresearch substrate.md>) · `fine-tuning` · baseten
  Frames model training infrastructure as an autoresearch substrate for running iterative experiments and training jobs.
- **2026-03-31** — [Open-source LLM training is a mess. Here is how it all works.](<../models/fine-tuning/Open-source LLM training is a mess. Here is how it all works.md>) · `fine-tuning` · baseten
  Explains the moving pieces of open-source LLM training, including data, trainers, infrastructure, and evaluation.
- **2026-03-28** — [The Fine-Tuning Bottleneck Isn't the Algorithm](<../models/fine-tuning/The Fine-Tuning Bottleneck Isn't the Algorithm.md>) · `fine-tuning` · fireworks
  Explains why fine-tuning bottlenecks often come from data, evaluation, orchestration, and serving rather than algorithms alone.
- **2026-03-23** — [Frontier RL Is Cheaper Than You Think](<../models/fine-tuning/Frontier RL Is Cheaper Than You Think.md>) · `fine-tuning` · fireworks
  Argues that frontier reinforcement learning can be cost-effective with the right infrastructure and training-loop design.
- **2026-03-12** — [Supporting privacy and compliance for EU teams](<../product-engineering/security/Supporting privacy and compliance for EU teams.md>) · `security` · braintrust
  Covers privacy and compliance requirements for EU AI teams, including data residency, controls, and deployment choices for observability data.
- **2026-03-06** — [Inference providers vs. API routers](<../inference/serving/Inference providers vs. API routers.md>) · `serving` · fireworks
  Explains the operational difference between inference providers and API routers, including routing, control, and token provenance.
- **2026-02-25** — [Accelerating AI research that accelerates AI research](<../product-engineering/case-studies/Accelerating AI research that accelerates AI research.md>) · `case-studies` · modal
  Case study on using elastic compute to accelerate AI research workflows, including experiment throughput and infrastructure offload.
- **2026-02-18** — [How Ramp built a full context background coding agent on Modal](<../agents/computer-use/How Ramp built a full context background coding agent on Modal.md>) · `computer-use` · modal
  Case study of a background coding agent architecture that gives agents full project context through remote sandboxes.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<../evals-observability/evaluation/Quantifying infrastructure noise in agentic coding evals.md>) · `evaluation` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-22** — [Optimizing inference speed and costs: Lessons learned from large-scale deployments](<../inference/optimization/Optimizing inference speed and costs Lessons learned from large-scale deployments.md>) · `optimization` · together
  Lessons from optimizing inference speed and cost in large-scale deployments.
- **2026-01-21** — [Security is a choice: how Braintrust lets you decide where your AI data lives](<../product-engineering/security/Security is a choice how Braintrust lets you decide where your AI data lives.md>) · `security` · braintrust
  Explains data-control choices for AI observability, including where data lives, how security boundaries are enforced, and deployment implications.
- **2025-12-18** — [Brainstore makes AI observability at scale possible](<../evals-observability/monitoring/Brainstore makes AI observability at scale possible.md>) · `monitoring` · braintrust
  Benchmark-oriented note on Brainstore performance and why purpose-built storage is needed for high-volume AI observability workloads.
- **2025-11-25** — [Building and Deploying Production‑Grade AI Agents: Cresta’s End‑to‑End Approach](<../agents/planning/Building and Deploying Production‑Grade AI Agents Cresta’s End‑to‑End Approach.md>) · `planning` · cresta
  End-to-end guide to production AI agent deployment, including design, launch, monitoring, and operational controls.
- **2025-11-19** — [50 Trillion Tokens Per Day: The State of Agent Environments](<../agents/computer-use/50 Trillion Tokens Per Day The State of Agent Environments.md>) · `computer-use` · fireworks
  Surveys the state of agent environments, emphasizing execution scale, sandboxing, and environment design.
- **2025-11-18** — [Host overhead is killing your inference efficiency](<../inference/optimization/Host overhead is killing your inference efficiency.md>) · `optimization` · modal
  Analyzes host overhead as an inference bottleneck and shows why CPU-side orchestration can dominate model-serving efficiency.
- **2025-09-22** — [Build an AI coding platform that scales to millions of monthly sessions](<../agents/computer-use/Build an AI coding platform that scales to millions of monthly sessions.md>) · `computer-use` · modal
  Describes architecture concerns for AI coding platforms that need to scale sandboxed coding sessions to large user volumes.
- **2025-09-04** — [Building LangGraph: Designing an Agent Runtime from first principles](<../agents/planning/Building LangGraph Designing an Agent Runtime from first principles.md>) · `planning` · langchain
  Design history of LangGraph as an agent runtime from first principles, covering control flow, state, durability, and production requirements.
- **2025-08-19** — [How to fine-tune gpt-oss-120b with Baseten and Axolotl](<../models/fine-tuning/How to fine-tune gpt-oss-120b with Baseten and Axolotl.md>) · `fine-tuning` · baseten
  Guide to fine-tuning GPT-OSS 120B with Axolotl and scalable training infrastructure.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-07-30** — [GPU Memory Snapshots: Supercharging sub-second startup](<../inference/optimization/GPU Memory Snapshots Supercharging sub-second startup.md>) · `optimization` · modal
  Explains GPU memory snapshots for reducing cold-start latency and preserving loaded model state across invocations.
- **2025-06-23** — [How we built Multi-cloud Capacity Management (MCM)](<gpu-clusters/How we built Multi-cloud Capacity Management (MCM).md>) · `gpu-clusters` · baseten
  Engineering writeup on building multi-cloud capacity management for inference infrastructure.
- **2025-06-09** — [How Baseten multi-cloud capacity management unifies deployments](<gpu-clusters/How Baseten multi-cloud capacity management unifies deployments.md>) · `gpu-clusters` · baseten
  Explains multi-cloud capacity management for unifying cloud, self-hosted, and hybrid inference deployments.
- **2025-05-21** — [How we Built Scalable & Customizable Dashboards](<../evals-observability/monitoring/How we Built Scalable & Customizable Dashboards.md>) · `monitoring` · langfuse
  Engineering writeup on building scalable customizable dashboards for observability data, covering query, rendering, and product architecture concerns.
- **2025-05-07** — [Linear programming for fun and profit](<cost/Linear programming for fun and profit.md>) · `cost` · modal
  Shows how linear programming can allocate compute resources under constraints, useful for GPU scheduling and cost control.
- **2025-04-03** — [Resilient observability by design](<../evals-observability/monitoring/Resilient observability by design.md>) · `monitoring` · braintrust
  Describes resilient observability design for AI systems, including reliability considerations for storing, querying, and using production traces.
- **2025-03-27** — [Introducing End-to-End OpenTelemetry Support in LangSmith](<../evals-observability/tracing/Introducing End-to-End OpenTelemetry Support in LangSmith.md>) · `tracing` · langchain
  Introduces end-to-end OpenTelemetry support in LangSmith for standardizing traces across AI application components.
- **2025-03-20** — [Build vs. Buy: How Cresta Engineered Its Own Customer Data Access Solution](<../product-engineering/architecture/Build vs. Buy How Cresta Engineered Its Own Customer Data Access Solution.md>) · `architecture` · cresta
  Engineering case study on building a customer data access layer, useful for understanding integration tradeoffs in enterprise AI products.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<../evals-observability/evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2025-03-04** — [Understanding Cresta’s Voice Platform - The Voice Stack](<../models/multimodal/Understanding Cresta’s Voice Platform - The Voice Stack.md>) · `multimodal` · cresta
  Breaks down the components of a production voice AI stack, including telephony, speech, model, and orchestration layers.
- **2025-02-25** — [Minions: embracing small LMs, shifting compute on-device, and cutting cloud costs in the process](<../models/reasoning/Minions embracing small LMs, shifting compute on-device, and cutting cloud costs in the process.md>) · `reasoning` · together
  Explores using small language models and on-device compute to reduce cloud inference costs.
- **2025-02-24** — ['I paid for the whole GPU, I am going to use the whole GPU': A high-level guide to GPU utilization](<../inference/hardware/'I paid for the whole GPU, I am going to use the whole GPU' A high-level guide to GPU utilization.md>) · `hardware` · modal
  Guide to GPU utilization for AI workloads, covering bottlenecks, throughput, batching, and cost-aware usage.
- **2025-02-13** — [How multi-node inference works for massive LLMs like DeepSeek-R1](<../inference/serving/How multi-node inference works for massive LLMs like DeepSeek-R1.md>) · `serving` · baseten
  Explains multi-node inference for very large LLMs such as DeepSeek-R1.
- **2024-11-19** — [Instrumenting Your LLM Application: Arize Phoenix and Vercel AI SDK](<../evals-observability/tracing/Instrumenting Your LLM Application Arize Phoenix and Vercel AI SDK.md>) · `tracing` · arize
  Shows how to instrument an LLM application with Phoenix and Vercel AI SDK so traces are available for debugging and evaluation.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<../evals-observability/evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-10-14** — [OpenTelemetry (OTel) for LLM Observability](<../evals-observability/tracing/OpenTelemetry (OTel) for LLM Observability.md>) · `tracing` · langfuse
  Introduces OpenTelemetry for LLM observability and how OTel-style traces can standardize spans, metadata, and interoperability across AI systems.
- **2024-10-08** — [The Role of OpenTelemetry (OTEL) in LLM Observability](<../evals-observability/tracing/The Role of OpenTelemetry (OTEL) in LLM Observability.md>) · `tracing` · arize
  Explains OpenTelemetry’s role in LLM observability and why standard traces matter for production systems.
- **2024-09-05** — [Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection](<../inference/hardware/Supercharging NVIDIA H200 and H100 GPU Cluster Performance With Together Kernel Collection.md>) · `hardware` · together
  Shows how kernel work improves H200 and H100 GPU cluster performance.
- **2024-07-25** — [Deploying custom ComfyUI workflows as APIs](<../models/multimodal/Deploying custom ComfyUI workflows as APIs.md>) · `multimodal` · baseten
  Shows how to deploy custom ComfyUI image-generation workflows behind API endpoints.
- **2024-07-25** — [Building A Generative AI Platform](<../product-engineering/architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-07-11** — [Using asynchronous inference in production](<../inference/serving/Using asynchronous inference in production.md>) · `serving` · baseten
  Explains asynchronous inference patterns for production model-serving workloads.
- **2024-06-20** — [Managing and Monitoring Your Open Source LLM Applications](<../evals-observability/monitoring/Managing and Monitoring Your Open Source LLM Applications.md>) · `monitoring` · arize
  Covers practical monitoring needs for open-source LLM applications, including operational metrics and deployment feedback.
- **2024-06-06** — [How to catch crypto miners using syscall signatures](<../product-engineering/security/How to catch crypto miners using syscall signatures.md>) · `security` · modal
  Explains detecting abusive GPU workloads with syscall signatures, a useful pattern for securing shared AI infrastructure.
- **2024-06-03** — [GPUs on-demand: Not serverless, not reserved, but some third thing](<gpu-clusters/GPUs on-demand Not serverless, not reserved, but some third thing.md>) · `gpu-clusters` · fireworks
  Explains on-demand GPU infrastructure as a middle ground between serverless and reserved capacity.
- **2024-03-28** — [Using fractional H100 GPUs for efficient model serving](<../inference/serving/Using fractional H100 GPUs for efficient model serving.md>) · `serving` · baseten
  Explains fractional H100 usage for efficient model serving and better GPU utilization.
- **2024-03-14** — [What I learned from looking at 900 most popular open source AI tools](<../industry/trends/What I learned from looking at 900 most popular open source AI tools.md>) · `trends` · chip-huyen
  Maps 900 open-source AI tools into infrastructure, model-development, and application-development layers, highlighting growth in agents, prompt engineering, vector search, evaluation, and inference tooling.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<../evals-observability/evaluation/Predictive Human Preference From Model Ranking to Model Routing.md>) · `evaluation` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2024-02-20** — [Why GPU utilization matters for model inference](<../inference/hardware/Why GPU utilization matters for model inference.md>) · `hardware` · baseten
  Explains why GPU utilization is central to inference cost and performance.
- **2024-01-23** — [Embedding English Wikipedia in under 15 minutes](<../rag-retrieval/embeddings/Embedding English Wikipedia in under 15 minutes.md>) · `embeddings` · modal
  Walkthrough of embedding English Wikipedia quickly, covering large-scale embedding jobs, batching, and storage workflow.
- **2023-12-08** — [How to serve your ComfyUI model behind an API endpoint](<../models/multimodal/How to serve your ComfyUI model behind an API endpoint.md>) · `multimodal` · baseten
  Shows how to serve a ComfyUI model behind an API endpoint for production image workflows.
- **2023-11-28** — [NVIDIA A10 vs A10G for ML model inference](<../inference/hardware/NVIDIA A10 vs A10G for ML model inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A10G GPUs for model inference performance and cost.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<../evals-observability/monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
- **2023-09-15** — [NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference](<../inference/hardware/NVIDIA A10 vs A100 GPUs for LLM and Stable Diffusion inference.md>) · `hardware` · baseten
  Compares NVIDIA A10 and A100 GPUs for LLM and Stable Diffusion inference workloads.
- **2023-04-27** — [Comparing NVIDIA GPUs for AI: T4 vs A10](<../inference/hardware/Comparing NVIDIA GPUs for AI T4 vs A10.md>) · `hardware` · baseten
  Compares NVIDIA T4 and A10 GPUs for AI inference workloads and cost-performance tradeoffs.
- **2022-12-22** — [Hugging Face + Arize: Partnership and Code Example](<../evals-observability/monitoring/Hugging Face + Arize Partnership and Code Example.md>) · `monitoring` · arize
  Partnership and code example showing how to monitor Hugging Face model workflows with Arize observability.
- **2022-12-16** — [Calculate Real-Time AI ROI With Custom Metrics](<../evals-observability/monitoring/Calculate Real-Time AI ROI With Custom Metrics.md>) · `monitoring` · arize
  Shows how custom metrics can connect AI observability data to real-time ROI analysis and business impact.
- **2022-01-02** — [Real-time machine learning: challenges and solutions](<../product-engineering/architecture/Real-time machine learning challenges and solutions.md>) · `architecture` · chip-huyen
  Deep dive on real-time ML systems covering online prediction, feature freshness, stream processing, monitoring, feedback delays, and the tradeoffs needed to serve adaptive models in production.
- **2020-12-30** — [Machine Learning Tools Landscape v2 (+84 new tools)](<../industry/trends/Machine Learning Tools Landscape v2 (+84 new tools).md>) · `trends` · chip-huyen
  Updates the MLOps tooling landscape to 284 tools and identifies deployment, monitoring, serving hardware, and regional infrastructure divergence as major production-ML trends.
- **2020-12-27** — [Machine learning is going real-time](<../product-engineering/architecture/Machine learning is going real-time.md>) · `architecture` · chip-huyen
  Explains the shift from batch prediction to online ML, covering streaming features, low-latency inference, fresh feedback loops, and the architectural constraints behind real-time applications.
