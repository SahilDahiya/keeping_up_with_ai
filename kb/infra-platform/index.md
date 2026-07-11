# infra-platform

21 articles.

- **2026-07-01** — [Model subsidies are ending. What do you do now?](<cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-19** — [Temporary Cloudflare Accounts for AI agents](<deployment/Temporary Cloudflare Accounts for AI agents.md>) · `deployment` · cloudflare-ai
  Temporary Cloudflare Accounts let agents run 'wrangler deploy --temporary' to ship a Worker with zero signup — a 60-minute claimable account with auto-provisioned API token — with Wrangler itself prompting agents about the flag, removing human-built OAuth/dashboard friction from the deploy loop.
- **2026-06-17** — [How to test agent cost-efficiency with Braintrust](<cost/How to test agent cost-efficiency with Braintrust.md>) · `cost` · braintrust
  Explains how to test agent cost-efficiency by measuring task success against token, model, and tool-use costs.
- **2026-06-17** — [Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue](<deployment/Bringing more agent harnesses and frameworks to Cloudflare, starting with Flue.md>) · `deployment` · cloudflare-ai
  Describes a three-layer production agent stack — framework (Flue, from the Astro team, built on the Pi harness), harness (Project Think, Pi), and runtime (Cloudflare Agents SDK) — with durable execution, dynamic code execution, and a durable filesystem exposed to any harness.
- **2026-06-05** — [Your AI bill is out of control. Cloudflare can fix it now.](<cost/Your AI bill is out of control. Cloudflare can fix it now.md>) · `cost` · cloudflare-ai
  AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven budgets and model routing via Cloudflare Access, so enterprises can attribute LLM spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for interns) instead of one opaque shared API key.
- **2026-05-19** — [Announcing Claude Managed Agents on Cloudflare](<deployment/Announcing Claude Managed Agents on Cloudflare.md>) · `deployment` · cloudflare-ai
  Cloudflare-Anthropic integration running Claude Managed Agents against Cloudflare Sandboxes: the agent loop stays on the Claude Platform while Cloudflare provides microVM or isolate sandboxes, credential-injecting proxies, private service connectivity, browser session audit trails, and per-agent email.
- **2026-03-16** — [Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider](<deployment/Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider.md>) · `deployment` · arize
  Announces native NVIDIA NIM support in Arize AX so teams can connect hosted model providers into evaluation and observability workflows.
- **2025-09-17** — [adb Benchmarks](<deployment/adb Benchmarks.md>) · `deployment` · arize
  Benchmarks Arize database performance at the storage and application level for AI observability workloads powered by high-volume traces and model data.
- **2025-08-11** — [adb Database: Realtime Ingestion At Scale](<deployment/adb Database Realtime Ingestion At Scale.md>) · `deployment` · arize
  Describes realtime ingestion design for Arize database, including scale requirements for AI observability data and production trace ingestion.
- **2025-05-19** — [Arize AI Accelerates Enterprise AI Adoption On-Premises With NVIDIA](<deployment/Arize AI Accelerates Enterprise AI Adoption On-Premises With NVIDIA.md>) · `deployment` · arize
  Announcement of Arize and NVIDIA collaboration for on-prem enterprise AI deployment and observability infrastructure.
- **2025-03-03** — [Brainstore: the database designed for the AI engineering era](<deployment/Brainstore the database designed for the AI engineering era.md>) · `deployment` · braintrust
  Introduces Brainstore as a database for AI engineering workloads, optimized for traces, evals, logs, and large-scale observability queries.
- **2025-01-08** — [Our approach to hybrid deployment](<deployment/Our approach to hybrid deployment.md>) · `deployment` · braintrust
  Describes a hybrid deployment approach for AI observability, balancing managed services with customer-controlled data and infrastructure boundaries.
- **2024-05-21** — [Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog](<deployment/Arize AI Brings LLM Evaluation, Observability To Microsoft Azure AI Model Catalog.md>) · `deployment` · arize
  Describes Arize integration with Microsoft Azure AI Model Catalog for LLM evaluation and observability in Azure-hosted development workflows.
- **2023-11-27** — [Open sourcing the AI proxy](<deployment/Open sourcing the AI proxy.md>) · `deployment` · braintrust
  Open-source AI proxy notes focused on provider routing, logging, credentials, access control, and observability for model calls.
- **2023-11-20** — [AI proxy: fostering a more open ecosystem](<deployment/AI proxy fostering a more open ecosystem.md>) · `deployment` · braintrust
  Introduces an AI proxy pattern for routing model calls across providers while centralizing logging, credentials, access control, and production visibility.
- **2023-09-19** — [Arize AI Debuts Integration with Anyscale Endpoints](<deployment/Arize AI Debuts Integration with Anyscale Endpoints.md>) · `deployment` · arize
  Announcement and integration walkthrough for using Arize with Anyscale Endpoints to monitor hosted open-model inference.
- **2023-01-08** — [Self-serve feature platforms: architectures and APIs](<deployment/Self-serve feature platforms architectures and APIs.md>) · `deployment` · chip-huyen
  Breaks down self-serve feature-platform architecture and APIs, covering feature definitions, pipelines, storage, discovery, and ergonomics for ML teams that need reusable production features.
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
- **2026-07-03** — [Fable's judgement](<../agents/multi-agent/Fable's judgement.md>) · `multi-agent` · simon-willison
  Practical coding-agent pattern for delegating implementation work to cheaper subagents while reserving the main model for judgment, review, synthesis, and model-selection decisions.
- **2026-07-01** — [Announcing the Monetization Gateway: charge for any resource behind Cloudflare via x402](<../industry/business/Announcing the Monetization Gateway charge for any resource behind Cloudflare via x402.md>) · `business` · cloudflare-ai
  Announces the Monetization Gateway: charge agents for any Cloudflare-protected resource (pages, datasets, APIs, MCP tools) with payment verification enforced at the edge, settling sub-cent stablecoin micropayments over the x402 protocol now stewarded by a 25+ member Linux Foundation x402 Foundation.
- **2026-06-30** — [What’s new in Claude Sonnet 5](<../models/releases/What’s new in Claude Sonnet 5.md>) · `releases` · simon-willison
  Developer-focused notes on Claude Sonnet 5 covering adaptive thinking defaults, removed sampling parameters, million-token context, pricing/tokenizer changes, and comparative tokenization cost across document types.
- **2026-06-30** — [Using OSS models to save on inference costs without cutting quality](<../inference/serving/Using OSS models to save on inference costs without cutting quality.md>) · `serving` · braintrust
  Explains using open-source models to reduce inference cost without sacrificing quality, emphasizing eval-driven model selection and serving tradeoffs.
- **2026-06-16** — [How to use Braintrust with any framework or provider](<../evals-observability/tracing/How to use Braintrust with any framework or provider.md>) · `tracing` · braintrust
  Integration guide for capturing Braintrust traces and evals across different AI frameworks and model providers without locking the application stack to one SDK.
- **2026-06-11** — [Bring production agent traces from Arize into Databricks Unity Catalog](<../evals-observability/tracing/Bring production agent traces from Arize into Databricks Unity Catalog.md>) · `tracing` · arize
  Explains how to bring production agent traces, evaluations, and annotations from Arize into Databricks Unity Catalog for queryable analysis.
- **2026-06-04** — [How we made continuous trace intelligence possible at scale](<../evals-observability/tracing/How we made continuous trace intelligence possible at scale.md>) · `tracing` · braintrust
  Architecture deep dive on continuous trace intelligence at scale, including how production traces are clustered and surfaced for analysis.
- **2026-04-30** — [Agents can now create Cloudflare accounts, buy domains, and deploy](<../agents/tool-use/Agents can now create Cloudflare accounts, buy domains, and deploy.md>) · `tool-use` · cloudflare-ai
  Via a protocol co-designed with Stripe for Stripe Projects, coding agents can now provision a Cloudflare account, start a paid subscription, register a domain, and receive an API token to deploy — end-to-end with humans only approving payment and terms of service.
- **2026-04-20** — [The AI engineering stack we built internally — on the platform we ship](<../product-engineering/case-studies/The AI engineering stack we built internally — on the platform we ship.md>) · `case-studies` · cloudflare-ai
  Eleven-month buildout of Cloudflare's internal AI engineering stack on its own products: 3,683 users (93% of R&D), 47.95M AI requests and 241B tokens/month through AI Gateway, an MCP Server Portal with single OAuth, and merge requests nearly doubling from ~5,600 to 10,952/week.
- **2026-04-20** — [Building the agentic cloud: everything we launched during Agents Week 2026](<../industry/announcements/Building the agentic cloud everything we launched during Agents Week 2026.md>) · `announcements` · cloudflare-ai
  Roundup of every Agents Week 2026 launch for Cloudflare's 'agentic cloud': Artifacts (Git-compatible versioned storage), Sandboxes with Outbound Workers for zero-trust egress, Durable Object Facets, and Workflows rearchitected to 50,000 concurrency for durable background agents.
- **2026-04-15** — [Data Fabric: Querying agent traces in BigQuery](<../evals-observability/tracing/Data Fabric Querying agent traces in BigQuery.md>) · `tracing` · arize
  Shows how to query production agent traces in BigQuery by connecting observability data with warehouse analysis workflows.
- **2026-04-08** — [Scaling Managed Agents: Decoupling the brain from the hands](<../product-engineering/architecture/Scaling Managed Agents Decoupling the brain from the hands.md>) · `architecture` · anthropic-engineering
  Architecture of Claude Managed Agents: decoupling the agent loop (the brain) from sandboxed tool execution (the hands) to scale hosted long-running sessions.
- **2026-04-06** — [How Brainstore works: architecture for AI observability at scale](<../evals-observability/monitoring/How Brainstore works architecture for AI observability at scale.md>) · `monitoring` · braintrust
  Deep dive into Brainstore's architecture for AI observability at scale, covering storage, indexing, query patterns, and trace/log workloads.
- **2026-03-12** — [Supporting privacy and compliance for EU teams](<../product-engineering/security/Supporting privacy and compliance for EU teams.md>) · `security` · braintrust
  Covers privacy and compliance requirements for EU AI teams, including data residency, controls, and deployment choices for observability data.
- **2026-02-05** — [Quantifying infrastructure noise in agentic coding evals](<../evals-observability/evaluation/Quantifying infrastructure noise in agentic coding evals.md>) · `evaluation` · anthropic-engineering
  Quantifies how infrastructure flakiness (timeouts, container variance) injects noise into agentic coding evals, and methods to measure and control for it.
- **2026-01-21** — [Security is a choice: how Braintrust lets you decide where your AI data lives](<../product-engineering/security/Security is a choice how Braintrust lets you decide where your AI data lives.md>) · `security` · braintrust
  Explains data-control choices for AI observability, including where data lives, how security boundaries are enforced, and deployment implications.
- **2025-12-18** — [Brainstore makes AI observability at scale possible](<../evals-observability/monitoring/Brainstore makes AI observability at scale possible.md>) · `monitoring` · braintrust
  Benchmark-oriented note on Brainstore performance and why purpose-built storage is needed for high-volume AI observability workloads.
- **2025-04-03** — [Resilient observability by design](<../evals-observability/monitoring/Resilient observability by design.md>) · `monitoring` · braintrust
  Describes resilient observability design for AI systems, including reliability considerations for storing, querying, and using production traces.
- **2025-03-05** — [Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA](<../evals-observability/evaluation/Build More Accurate AI Apps Through Fast Experimentation with Arize Phoenix, Langflow, and NVIDIA.md>) · `evaluation` · arize
  Shows how Arize Phoenix, Langflow, and NVIDIA can support fast experimentation loops for improving AI application accuracy.
- **2024-11-01** — [Arize, Vertex AI API: Evaluation Workflows to Accelerate Generative App Development and AI ROI](<../evals-observability/evaluation/Arize, Vertex AI API Evaluation Workflows to Accelerate Generative App Development and AI ROI.md>) · `evaluation` · arize
  Describes Arize and Vertex AI API evaluation workflows for accelerating generative application development and measuring AI ROI.
- **2024-07-25** — [Building A Generative AI Platform](<../product-engineering/architecture/Building A Generative AI Platform.md>) · `architecture` · chip-huyen
  Reference architecture for generative AI platforms covering context construction and RAG, guardrails, gateways and routers, caching, observability, orchestration, and tool/action layers.
- **2024-03-14** — [What I learned from looking at 900 most popular open source AI tools](<../industry/trends/What I learned from looking at 900 most popular open source AI tools.md>) · `trends` · chip-huyen
  Maps 900 open-source AI tools into infrastructure, model-development, and application-development layers, highlighting growth in agents, prompt engineering, vector search, evaluation, and inference tooling.
- **2024-02-28** — [Predictive Human Preference: From Model Ranking to Model Routing](<../evals-observability/evaluation/Predictive Human Preference From Model Ranking to Model Routing.md>) · `evaluation` · chip-huyen
  Describes predictive human preference for model ranking and model routing, using preference models and evaluations to choose among LLMs by quality, cost, and latency.
- **2023-10-26** — [AI ROI: Guide To Observability Value Statistics](<../evals-observability/monitoring/AI ROI Guide To Observability Value Statistics.md>) · `monitoring` · arize
  Frames AI observability value through ROI statistics, linking monitoring and model performance visibility to business outcomes.
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
