# industry

3 articles.

- **2025-12-30** — [OpenAI for Developers in 2025](<trends/OpenAI for Developers in 2025.md>) · `trends` · openai-devs
  Year-in-review of OpenAI's 2025 developer platform: reasoning converging from separate o1/o3/o4-mini lines into unified flagship models, multimodal I/O becoming default, agent building blocks (Responses API, Agents SDK, AgentKit), and GPT-5.2-Codex for long-horizon coding.
- **2025-07-04** — [Augmented commerce: Machine learning at Shopify (2025)](<trends/Augmented commerce Machine learning at Shopify (2025).md>) · `trends` · shopify
  Overview of how ML is applied across Shopify's commerce platform ('augmented commerce'), framing the merchant ecosystem as the problem space for recommendation, search, and classification systems.
- **2024-12-02** — [Open Source Developers Guide to the EU AI Act](<trends/Open Source Developers Guide to the EU AI Act.md>) · `trends` · huggingface
  Practical guide to EU AI Act obligations for open-source model and system developers: the GPAI vs system distinction, the 10^25 FLOP systemic-risk threshold, and the documentation, transparency, watermarking and opt-out steps that satisfy limited-risk duties.

## Also relevant (filed elsewhere)

- **2026-04-23** — [Claude Code pricing: plans, API costs, and how to lower your bill](<../infra-platform/cost/Claude Code pricing plans, API costs, and how to lower your bill.md>) · `cost` · fireworks
  Breaks down Claude Code cost paths (Pro $17/mo, Max 5x/20x, Team Standard/Premium, Enterprise, API) and describes routing Claude Code through Fireworks-hosted open-weight models (GLM 5.2, Kimi K2.7 Code, MiniMax M3) via FireConnect or an OpenAI-compatible harness, recommending evaluation on completion rate and repair time rather than token price alone.
- **2026-03-06** — [Inference Providers vs. API Routers: where do tokens come from?](<../infra-platform/deployment/Inference Providers vs. API Routers where do tokens come from.md>) · `deployment` · fireworks
  Distinguishes inference providers (control the GPUs serving a model) from API routers like OpenRouter (forward requests upstream), explaining that routers can improve tail latency/reliability via failover but cannot beat direct-provider median latency, and have no visibility into KV cache, batch scheduling, or kernel decisions that determine quality.
- **2026-03-04** — [Best LLM API Providers in 2026: We Reviewed 8 Options](<../infra-platform/deployment/Best LLM API Providers in 2026 We Reviewed 8 Options.md>) · `deployment` · fireworks
  Comparison of 8 LLM inference providers (Fireworks, Groq, Together, OpenRouter, Cerebras, Hugging Face, Baseten, Modal) on criteria beyond price/token: fine-tuning support, model deprecation risk, rate limits, and billing complexity, with per-provider recommendations by use case.
- **2025-05-12** — [Vision Language Models (Better, faster, stronger)](<../models/multimodal/Vision Language Models (Better, faster, stronger).md>) · `multimodal` · huggingface
  A year-in-review of vision language models covering new model classes (any-to-any, reasoning VLMs, small on-device VLMs, MoE VLMs), multimodal RAG with ColPali-style late-interaction retrievers, VLM agents for GUI/computer use, video understanding, and how alignment/benchmarks for VLMs have evolved. Names the specific models and techniques behind each shift.
