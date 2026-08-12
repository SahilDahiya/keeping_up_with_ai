---
title: 'Best LLM API Providers in 2026: We Reviewed 8 Options'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/best-llm-api-providers
author: null
published: '2026-03-04'
fetched: '2026-08-12T06:31:03Z'
classifier: null
taxonomy_rev: 2
words: 10264
content_sha256: 8867d6274c9250bfaadebcf376481f0dc1156b500a3ee1d7d3029ed9767a8f9d
---

# Best LLM API Providers in 2026: We Reviewed 8 Options

**Last update:** this post was originally created in March 2026 and updated in May 2026.

Most LLM API provider comparisons rank platforms by price per million tokens, as if inference were a commodity with price as the only thing that matters. Inference is not a commodity: a provider that saves 40% on token costs often costs far more in engineering time when models deprecate without warning, rate limits throttle an agent mid-run, or a fine-tuning workflow requires a second vendor entirely.

Even when providers look comparable on a feature matrix, they often diverge sharply once production pressure surfaces the gaps between advertised throughput and real-world performance. Likewise, some providers have attractive free-tier ceilings that quickly become cost-inefficient at scale. Others provide terrific inference-only service, but have little or no support for model customization via post-training, thereby constraining teams to rely solely on prompt engineering to adapt model behavior, or to use a completely separate platform for model customization. This post summarizes the current landscape of API inference providers and seeks to transparently review the pros and cons of each platform so that AI builders can make informed decisions about investing in their inference stack.

A quick note before we dive in: writing an unbiased vendor comparison when your own platform is one of the vendors is inherently awkward. We're not going to pretend otherwise. What we can tell you is that building a good evaluation framework is itself a uniquely human activity. The same rigor that goes into designing evals for an effective RFT training run applies here as well. We've attempted to apply a consistent, bias-free lens across providers, scoring on criteria that matter to production engineering teams regardless of which platform they choose. Please take the Fireworks entries with appropriate skepticism, verify what matters, and use this as a starting point for your own due diligence.

- •Choose **Fireworks** if you need production-grade open-source inference and the ability to fine-tune and evaluate models without stitching together multiple vendors. 200+ models, Day-0 support for frontier model releases, and the only full post-training stack (SFT, LoRA, RFT, RL) in this list.
- •Choose **Groq** if the lowest possible time-to-first-token is your primary constraint and you can work within a narrow model catalog. Best for real-time chat and voice agents.
- •Choose **Together AI** if you need broad open-weight model selection with built-in fine-tuning and can tolerate billing complexity. Strong for research-stage workloads.
- •Choose **OpenRouter** if you want a single API key for 300+ models across providers and don't need fine-tuning or on-premise hosting.
- •Choose **Cerebras** if raw throughput on a few models matters more than catalog breadth, and you're comfortable with a platform still maturing around its hardware advantage.
- •Choose **Hugging Face** if you're prototyping or evaluating models. Graduate to a dedicated inference provider before shipping to production.
- •Choose **Baseten** if you have an ML engineering team that needs maximum control over deployment infrastructure — private dedicated endpoints, multi-node fine-tuning, and advanced observability are all available; expect a more ops-heavy setup than managed serverless platforms.
- •Choose **Modal** if you're a Python-native team that wants serverless GPU infrastructure with sub-second cold starts, full code control, and consumption-based billing. Best for custom model deployments, batch workloads, and teams that want to own their inference stack without managing Kubernetes.

The cheapest per-token rate often comes with hidden costs: rate-limit traps, model deprecation cycles, billing tier gates, and fine-tuning workflows that require a second vendor entirely. For most production teams, the answer is a provider that covers inference, customization, and scaling without adding operational overhead. If you prefer tinkering to reading, you can sign up and get started with free credits immediately. Below you will find a comprehensive guide to each of these eight inference providers.

This comparison article covers eight providers and is admittedly non-exhaustive. The inference API landscape moves quickly and new entrants emerge regularly. We plan to refresh this page as the market evolves. Last updated: May 2026.

| Provider | Models | Key Endpoints | Pricing | Limitation | 
|---|---|---|---|---|
| Fireworks | 200+ models with Day-0 support for new open-source releases | Chat, vision, audio, image generation, embeddings, full post-training stack | Per-token serverless and per-second GPU hourly rates | Higher unit costs compared to specialized discount providers | 
| OpenRouter | 300+ models from 60+ providers including proprietary models | Chat, vision, and multi-provider routing with automatic failover | Per-token rates with a 5.5% credit purchase fee | No fine-tuning; 5.5% credit purchase fee on prepaid credits (BYOK users pay 5% after 1M free requests/month) | 
| Together AI | 200+ models across text, image, video, and audio | Chat, vision, image generation, embeddings, fine-tuning (SFT, DPO, LoRA) | Per-token with 50% batch discounts and $5 minimum | Complex billing tiers and lifetime spend gates for models | 
| Groq | Narrow selection of Llama, GPT-OSS, and Qwen production models | Chat and vision | Per-token with free tier and batch discounts | Limited model variety and aggressive model deprecation patterns | 
| Cerebras | 4 models including Llama, GPT-OSS, Qwen, and GLM | Chat | Per-token with 1M free tokens per day | Constrained context windows and immature platform ecosystem | 
| Hugging Face | 2M+ open-source models via Hub and inference partners | Chat, vision, image, audio, and dedicated endpoints | Subscription tiers plus hourly compute and credit usage | Legacy serverless backend has reliability issues; Inference Providers system now routes to production-grade third-party backends | 
| Baseten | Open-source models (Llama, DeepSeek, Qwen, Kimi, etc.) plus custom models via Truss framework | Chat, embeddings, multi-step pipelines via Chains SDK, fine-tuning/training | Pay-as-you-go GPU compute (per minute); Model API per-token pricing; enterprise volume discounts | MLOps-heavy setup; requires more engineering investment than fully managed providers; no public per-token catalog for most models | 
| Modal | Any open-source or custom model deployable via Python | Chat, batch inference, fine-tuning, sandboxes, notebooks | Consumption-based per-second GPU compute; $30/month free credits on Starter plan | No managed model catalog; requires writing your own inference code; higher setup effort than turn-key API providers | 

Four dimensions separate the providers that look identical on a feature matrix from the ones that actually hold up in production:

- •**Model catalog and freshness:** Total model count, modality coverage (text-only LLMs vs. VLMs (vision), audio, embeddings, etc.), and how quickly new open-weight releases appear. A provider that takes weeks to add new frontier models forces you to stay on older models while competitors are faster to market.
- •**Inference speed and reliability:** Real-world throughput in tokens per second, time-to-first-token, and whether advertised speeds hold under production load. Artificial Analysis is the closest thing to an apples-to-apples benchmark source across providers. Note that benchmark conditions differ from production workloads with long contexts and tool calls.
- •**Post-training and customization:** Whether the provider offers fine-tuning (SFT, LoRA, RFT, RL pipelines) or is inference-only. This is the sharpest differentiator between providers that look similar on paper.
- •**Pricing transparency and total cost of ownership:** Not just per-token rates, but credit purchase fees, tier gating, batch discounts, and what happens to your bill at $10K per month. Small ~5% platform fees look great at the development stage on a pay-as-you-go tier but can become very material at production scale.

We reviewed official documentation, pricing pages, and endpoint specifications for each provider. We analyzed benchmark data from [Artificial Analysis](https://artificialanalysis.ai/), which measures throughput and latency under controlled conditions across hosted inference providers. For production reliability and real-world performance gaps, we compared developer-reported findings from community forums, technical reviews, and published case studies.

For this analysis, note that we did not conduct hands-on testing. Where community-reported performance diverges from vendor-published benchmarks (Cerebras is the clearest case in this roundup), we surface both data points and let you calibrate. Please also note that prices do change frequently in the API provider space. For example, [SemiAnalysis documented the ~40% price increase](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity) on Nvidia H100 GPUs that has been observed from October 2025 through March 2026. It is always worth verifying current pricing at each provider's site before committing to an architecture decision.

Choosing an LLM API provider comes down to four variables that rarely optimize together:

1. model breadth
2. inference speed and latency
3. pricing and transparency of costs
4. post-training ability to customize models

Fireworks and Together AI lead on catalog depth; Groq and Cerebras are specialists with narrow but fast options. OpenRouter's 300+ figure reflects routing to other providers' models, not hosted inventory. Baseten and Modal both support open-source models but are differentiated by their deployment model rather than catalog breadth.

| Provider | Proprietary Models | Open-Source Models | Total Model Count | 
|---|---|---|---|
| Fireworks | None | DeepSeek, Qwen, Kimi, Mistral, GLM, Minimax, Whisper, FLUX, Llama, and more | 200+ hosted models | 
| OpenRouter | None (routing layer only) | Llama, DeepSeek, Qwen, Mistral, Phi, Gemma, Kimi, and 60+ provider catalogs | 300+ routed models | 
| Hugging Face | None | 2M+ on Hub; hundreds via Inference Providers API across 18+ partners | 2M+ on Hub; hundreds via API | 
| Together AI | None | Llama 4, DeepSeek-V3.1/R1, Qwen3, Kimi K2, GLM-5, Mistral, FLUX family, Google Veo 3.0, Whisper, and more | 200+ across text, image, video, audio, embeddings | 
| Groq | Groq Compound, Groq Compound Mini (agentic orchestration) | Llama 3.1/3.3, Llama 4 Scout, GPT-OSS 20B/120B, Qwen3 32B, Whisper, Orpheus TTS | ~10 production + preview models | 
| Cerebras | None | GPT-OSS 120B, Llama 3.1 8B, Qwen 3 235B Instruct, and GLM 4.7 | 4 active models | 
| Baseten | None (Frontier Gateway white-label option for AI labs) | DeepSeek V3/V4, Llama 4 Scout/Maverick, Llama 3.3, Kimi K2.6, GLM 5, Gemma 3, Qwen, Whisper, custom models via Truss | No fixed catalog — deploys any model on your own GPU allocation | 
| Modal | None | Any Hugging Face or custom model; examples include Llama 3, Qwen3, Flux Kontext, Whisper, vision-language models, protein folding models | No fixed catalog — you bring your own model code | 

All providers in this comparison claim OpenAI compatibility, but the gaps matter in production. Cerebras drops `frequency_penalty`, `logit_bias`, and `presence_penalty`, returning a 400 error if supplied. Groq doesn't support `n > 1`, which blocks best-of-N sampling patterns. Hugging Face's OpenAI-compatible client covers chat completions only; image generation and embeddings require the native HF SDK. Baseten's Model APIs expose an OpenAI-compatible endpoint for supported models; custom Truss deployments follow your own API contract. Modal requires you to implement your own endpoint; OpenAI compatibility is achievable but not automatic.

| Provider | OpenAI-Compatible | Chat | Vision | Embeddings | Fine-tuning | Audio | Image Generation | Function Calling | 
|---|---|---|---|---|---|---|---|---|
| Fireworks | Yes | ✅ | ✅ | ✅ | ✅ Full stack (SFT, LoRA, RFT, RL) | ✅ | ✅ | ✅ | 
| OpenRouter | Yes (base URL swap) | ✅ | ✅ | ✅ | ❌ | ✅ Input only | ✅ | ✅ | 
| Hugging Face | Partial (chat only via OpenAI client) | ✅ | ✅ | ✅ (native SDK only) | ✅ Via TRL, Axolotl, or transformers (separate products) | ✅ | ✅ (native SDK only) | ✅ | 
| Together AI | Yes | ✅ | ✅ | ✅ | ✅ SFT + DPO, LoRA + Full | ✅ TTS + transcription | ✅ | ✅ | 
| Groq | Yes (with gaps) | ✅ | ✅ | ❌ | ❌ Enterprise only | ✅ STT + TTS | ❌ | ✅ | 
| Cerebras | Yes (with gaps) | ✅ | ❌ | ❌ | ❌ Enterprise only | ❌ | ❌ | ✅ | 
| Baseten | Yes (Model APIs); custom (Dedicated Deployments) | ✅ | ✅ | ✅ (Baseten Embeddings Inference) | ✅ Multi-node fine-tuning and pre-training | ✅ (via Whisper and custom models) | ✅ (custom deployment) | ✅ | 
| Modal | Achievable (must implement) | ✅ | ✅ | ✅ | ✅ Single- and multi-node via torchtune, Unsloth, GRPO | ✅ | ✅ | ✅ (must implement) | 

OpenRouter's per-token rates pass through at provider parity, but the Pay-as-you-go tier carries a 5.5% platform fee on credit purchases. Enterprise accounts get bulk discounts, so the fee primarily impacts mid-scale users between the free tier and an enterprise commitment. Together AI's $5 minimum purchase and Build Tier gating (FLUX Pro requires $50 lifetime spend) create friction that surfaces mid-build rather than at signup. Baseten and Modal both charge for GPU compute rather than tokens, making cost modeling different — you pay for time on hardware, not per inference call.

| Provider | Pricing Model | Flagship Model Price (per 1M tokens) | Free Tier | 
|---|---|---|---|
| Fireworks | Per-token (Serverless), per-GPU-second (On-Demand), custom (Enterprise Reserved) | DeepSeek-V4 Pro: $1.74 input / $3.48 output; from $0.10/1M (sub-4B models) | Yes, $1 in free credits | 
| OpenRouter | Pay-as-you-go credits + 5.5% purchase fee (5% for BYOK) | Pass-through at provider rates | Yes, 50 req/day; 1,000 req/day with ≥$10 credits | 
| Hugging Face | Subscription + pay-as-you-go inference credits + hourly endpoints (three separate billing models) | Pass-through at provider rates; hf-inference billed by compute-time × hardware cost | Yes, $0.10/month inference credits (Free tier); $2/month credits on PRO ($9/month) | 
| Together AI | Pay-as-you-go per token; 50% batch discount | DeepSeek-V4 Pro: $2.10 input / $4.40 output | No, $5 minimum purchase required | 
| Groq | Pay-as-you-go per token; 50% batch discount; 50% prompt cache discount | Llama 3.3 70B: $0.59 input / $0.79 output; GPT-OSS 120B: $0.15 / $0.60 | Yes, free tier with lower rate limits | 
| Cerebras | Pay-as-you-go per token; flat subscription (Code Pro/Max); enterprise custom | Llama 3.1 8B: $0.10/1M (combined); GPT-OSS 120B: see [cerebras.ai/pricing](http://cerebras.ai/pricing) | Yes, 1M tokens/day free across active models | 
| Baseten | Pay-as-you-go GPU compute (per minute); Model API per-token for supported models; enterprise volume discounts | DeepSeek V4: $1.74 input / $3.48 output (Model API); H100 dedicated: $0.10833/min ($6.50/hr equivalent) | Yes, free experimentation credits for new accounts | 
| Modal | Consumption-based per-second GPU compute; no idle charges | GPU-dependent: H100 ~$0.001097/sec ($3.95/hr equivalent); A100 80GB ~$0.000694/sec | Yes, $30/month in free compute credits (Starter plan) | 

- •**Fireworks is the only provider in this list with a full post-training stack available self-serve.** Together AI offers SFT, DPO, and LoRA. Baseten offers multi-node fine-tuning and pre-training jobs but requires more infrastructure setup. Modal supports fine-tuning through frameworks like torchtune and Unsloth but requires you to implement it yourself. Every other provider is inference-only or gates fine-tuning behind an enterprise sales process.
- •**OpenAI compatibility is table stakes, but the gaps are where production breaks.** All eight providers advertise drop-in compatibility. In practice, Cerebras's missing`frequency_penalty` support, Groq's`n=1` constraint, and Hugging Face's split SDK requirements mean that migrating an existing OpenAI-based application requires an audit pass before any provider switch goes live. Baseten's Model APIs offer OpenAI-compatible endpoints; Modal requires you to build your own.
- •**Breadth and speed are in direct tension.** Groq and Cerebras deliver the fastest raw throughput, but each supports fewer than 10 production models. Fireworks and Together AI cover hundreds of unique models respectively across five modalities, with the tradeoff being that neither matches Groq's peak speed on its supported models. Baseten and Modal both achieve low latency through infrastructure-level optimization rather than specialized hardware, with Baseten citing sub-400ms latency for production voice AI workloads and Modal's Rust-based container stack spinning up GPUs in under 1 second.
- •**Hidden costs compound at scale.** OpenRouter's 5.5% Pay-as-you-go platform fee, Together AI's tier-gated model access, and Hugging Face's three-layer billing structure all create costs that don't appear in the headline per-token rates. Groq and Cerebras both publish transparent per-token pricing with no purchase fees, making cost modeling more predictable for teams running volume workloads. Baseten and Modal charge for GPU time rather than tokens, which can be more cost-efficient for high-throughput workloads but requires careful capacity planning.
- •**Groq and Cerebras carry catalog risk for production systems.** Groq deprecated multiple models in 2026 with short notice; Cerebras currently offers a narrow catalog of 4 models, some of which may still carry preview status and can be discontinued without warning. Teams building on either platform should architect for model substitution from day one.
- •**Baseten and Modal are infrastructure-first platforms, not turn-key API services.** Both are powerful choices for teams with ML engineering capacity, but they require meaningfully more setup than managed API providers. If you want to call an endpoint and get a response with no infrastructure work, Baseten's Model APIs are the closest to managed — but Baseten's real value proposition is dedicated deployments with custom GPU selection, autoscaling, and observability. Modal's value proposition is maximum Python-native flexibility with serverless GPU economics.

Pricing and feature data gathered from official provider documentation as of mid-2026. Rates change frequently: verify current pricing on each provider's site before committing to a workload allocation.

Fireworks is the inference and adaptation platform engineering teams move to when they've validated their product on OpenAI or Anthropic and need production-grade open-source inference, model customization, and reliability at scale.

It serves open-source models at up to 90% lower cost than closed-source providers like GPT-5, Gemini 3 Pro, or Claude Opus 4.5, without trading away the speed or reliability that production workloads require. At [15+ trillion tokens per day](https://www.businessinsider.com/fireworks-ai-surge-ceo-lin-qiao-2026-4) and 99.9% uptime, the platform operates at a scale that makes it a credible default for teams past the prototyping stage.

What separates Fireworks from every other provider in this comparison is the combination: optimized inference through FireAttention, plus a complete post-training stack through FireOptimizer, all under one API. FireAttention delivers 3 to 12x lower latency and up to 5.6x higher throughput compared to a self-hosted vLLM deployment. FireOptimizer covers supervised fine-tuning, LoRA adapters, reinforcement fine-tuning, and full RL pipelines, all self-serve. No other provider in this roundup offers inference, fine-tuning, and evaluation under one API without an enterprise sales call.

**Platform details:**

- •**Models:** over 200 models including all frontier-capable open-source models such as DeepSeek-V4 Pro, Qwen 3.6 Plus, Kimi K2.5 and Kimi K2.6, GLM 5.1, MiniMax M2.7, Whisper, FLUX, Llama 4 Maverick, Llama 4 Scout, Llama 3.3, and many more open-source models across text, vision, audio, image generation, and[embeddings](https://fireworks.ai/models)
- •**Compatibility:** OpenAI-compatible API; most chat, embedding, and function calling code migrates without changes beyond the endpoint and key.
- •**Endpoints:** Chat completions, vision, embeddings, image generation, speech-to-text, function calling, fine-tuning via FireOptimizer
- •**Pricing:** Serverless from $0.10/1M tokens; On-Demand from $7.00/GPU hour (billed per second); Enterprise Reserved at custom rates; fine-tuning from $0.50/1M training tokens
- •**Limitation:** Fireworks is not always the lowest per-token price in the market. Other specialized discount providers can undercut on specific models. The value case is speed, reliability, and the post-training stack together, not cheapest unit cost alone.

Fireworks is the default for engineering teams that have found product-market fit on a closed-source API and are now watching their inference bill compound. It serves teams that need more than raw API access: fine-tuning on proprietary data, hundreds of LoRA adapters in production simultaneously, and a published 99.9% uptime SLA. If your roadmap includes any model customization, Fireworks is the only provider in this list where inference and post-training live under the same API.

- •**Full post-training stack, self-serve:** SFT, LoRA, reinforcement fine-tuning, and RL pipelines through FireOptimizer, available without an enterprise contract.
- •**Day-0 Model Support:** New open-source weights go live within 24 hours of public release, so your stack tracks the frontier automatically.
- •**FireAttention inference engine:** Handwritten CUDA kernels and adaptive speculative decoding purpose-built for open-source model architectures, delivering 3–12x lower latency and up to 5.6x higher throughput than self-hosted vLLM.

| Pros | Cons | 
|---|---|
| Only provider in this comparison with a full self-serve post-training stack under one API | Not always the cheapest per-token option; raw price can be undercut on specific models by other specialized providers | 
| 200+ models across five modalities with Day-0 support for new open-source releases | Model count reflects open-source catalog only; no proprietary foundation models if your workload requires a closed-source option | 
| 99.9% uptime SLA and 15T tokens/day operational scale, with no cold boots on Serverless | On-Demand GPU pricing starts at $7.00/hour for H100/H200s, which adds up quickly for always-on deployments that don't scale to zero | 
| FireAttention performance validated by Artificial Analysis across multiple model families | New accounts receive only $1 in free credits, which limits free-tier evaluation depth compared to providers like Cerebras (1M tokens/day free) | 

Fireworks offers three deployment tiers and a fine-tuning pricing track.

**Serverless** starts at $0.10 per 1M tokens for text and vision models under 4B parameters. You pay per token, skip cold boots, and face no GPU provisioning overhead. This is the right entry point for most teams evaluating the platform.

**On-Demand** starts at $7.00 per GPU hour for H100 and H200 GPUs, billed per second with auto-scaling to zero. This tier delivers up to 350% higher capacity and 60% lower latency than a self-hosted vLLM deployment on identical H100 hardware, per [Fireworks benchmarks](https://fireworks.ai/blog/custom-models-h100s-on-demand-deployments), and carries no rate limits.

**Enterprise Reserved** is custom-priced dedicated infrastructure with SLAs, priority support, and bring-your-own-cloud options. Contact the team at [fireworks.ai/contact](https://fireworks.ai/contact) for current rates.

**Fine-tuning** via FireOptimizer starts at $0.50 per 1M training tokens for LoRA fine-tuning on models up to 16B parameters (full-parameter SFT starts at $1.00/1M). Image generation starts at $0.00013 per step for non-FLUX models (FLUX.1 models from $0.00035/step). Embeddings start at $0.008 per 1M input tokens. Speech-to-text starts at $0.0009 per audio minute (Whisper Large v3 Turbo; base Whisper v3-large is $0.0015/minute).

New accounts receive $1 in free credits. Current model-specific rates are at [fireworks.ai/pricing](https://fireworks.ai/pricing).

**Can I Migrate from OpenAI's API Without Rewriting My Application?**

For most applications, yes. Fireworks uses an [OpenAI-compatible API](https://docs.fireworks.ai/docs/quickstart), so updating the endpoint and API key covers the majority of chat completion and embedding calls. Function calling, vision, and audio endpoints follow the same schema. The main audit step is confirming that any OpenAI-specific parameters your application passes are supported on the Fireworks model you're switching to.

**What Does "Day-0 Model Support" Actually Mean in Practice?**

When a new open-source model's weights are publicly released, Fireworks targets availability within 24 hours. This means teams tracking models like Llama 4 Maverick or [DeepSeek-R1](https://fireworks.ai/models/fireworks/deepseek-r1) don't need to wait weeks for a provider to onboard the model. For teams building on the open-source frontier, this removes the lag between "weights dropped" and "I can test this in production."

**Do I Need a Sales Conversation to Access Fine-Tuning?**

No. SFT, LoRA fine-tuning, reinforcement fine-tuning, and RL pipelines are all available self-serve through [FireOptimizer](https://docs.fireworks.ai/docs/fine-tuning-introduction). You can run your first fine-tuning job without speaking to anyone. Enterprise Reserved GPU capacity and custom SLAs do involve the sales team, but the full post-training stack is accessible from the moment you sign up at [app.fireworks.ai/signup](http://app.fireworks.ai/signup).

[Get started with Fireworks](https://app.fireworks.ai/signup) | [See Fireworks Plans](https://fireworks.ai/pricing)

OpenRouter routes requests to over 300 models across 60+ providers through a single OpenAI-compatible endpoint. The platform adds no per-token markup on inference costs: what you pay is what the underlying provider charges. The value proposition is consolidation, not optimization. You get one API key, one billing account, and automatic failover when a provider goes down or rate-limits your request.

The routing layer adds latency overhead on top of underlying provider response times. That overhead buys you intelligent routing variants: append `:nitro` to a model ID for maximum throughput, `:floor` for lowest cost, or `:exacto` for quality-first routing tuned for tool-calling reliability. OpenRouter identified that output quality differs measurably across providers running identical weights, and `:exacto` routes to the sub-group with the best tool-use success rates across billions of monthly requests.

- •**Models:** 300+ models across 60+ providers, including frontier proprietary models (OpenAI GPT series, Anthropic Claude, Google Gemini) and open-weight families (Meta Llama, Mistral, DeepSeek, Qwen). No proprietary models hosted directly.
- •**Compatibility:** Drop-in compatible with the OpenAI Python and Node.js SDKs; point to`https://openrouter.ai/api/v1` . Integrates with Vercel AI SDK, LangChain, Langfuse, and Mastra.
- •**Endpoints:** Chat/completions, vision, code generation, audio/speech, image generation, embeddings, function calling.
- •**Pricing:** Pass-through inference pricing with a 5.5% fee on credit purchases ($0.80 minimum). BYOK usage incurs a 5% fee after the first 1M free requests per month. Free accounts receive 50 free-model API requests per day; purchasing $10+ in credits raises the free-model daily limit to 1,000 requests per day.
- •**Limitation:** No fine-tuning capability, forcing teams that need model customization to maintain a separate provider relationship.

OpenRouter fits developers who need access to multiple model families without managing separate API keys, billing accounts, and SDK integrations for each. It is the lowest-friction path to testing frontier proprietary models alongside open-weight alternatives in the same codebase. Teams prototyping multi-model applications, building model comparison tools, or wanting automatic provider failover without writing custom routing logic use it as a gateway layer.

- •**Intelligent routing variants:** Append`:nitro` ,`:floor` , or`:exacto` to any model ID to optimize for speed, cost, or tool-calling quality without changing application logic.
- •**Automatic failover:** The platform tracks provider failures in real time and routes around unavailable providers, billing only for successful completions.
- •**Zero-markup inference pricing:** Costs match the underlying provider's published rates exactly, with no per-token surcharge added by the routing layer.

| Pros | Cons | 
|---|---|
| Single API key for 300+ models across 60+ providers eliminates SDK sprawl | 5.5% platform fee on Pay-as-you-go tier; enterprise accounts get bulk discounts and BYOK users pay 5% after 1M free requests/month | 
| Drop-in OpenAI SDK compatibility requires only a base URL change | Enterprise SLAs and SOC 2 compliance available but require contacting sales; no self-serve SLA tier | 
| Automatic failover and load balancing across providers with zero-completion insurance | Free-tier 429 errors can surface as silent failures in routing frameworks rather than standard rate-limit exceptions | 
| No per-token markup on inference costs | No fine-tuning capability; teams needing model customization require a separate provider | 

Inference costs pass through at the underlying provider's published rates with no per-token markup. OpenRouter charges a 5.5% fee (minimum $0.80) on prepaid credit purchases. BYOK users pay a lower 5% fee on usage after the first 1M free requests per month, making it the more cost-effective path at scale. Enterprise accounts can negotiate custom rates. Free accounts are capped at 50 API requests per day; purchasing at least $10 in credits raises the daily limit to 1,000 requests. No volume discounts are available through standard accounts, though high-volume cases can be raised via email. For current model-specific rates, see [openrouter.ai/pricing](http://openrouter.ai/pricing).

**Does OpenRouter Add Latency to My Requests?**

Yes. OpenRouter adds routing overhead on top of underlying provider response times. These are vendor-published figures; independent benchmarks at scale are limited. If consistent minimum latency is a hard requirement, pinning a specific model and region directly with the underlying provider removes the routing layer entirely.

**Does OpenRouter Offer Compliance Certifications and SLAs?**

OpenRouter is SOC 2 compliant and offers enterprise SLAs through its sales team. A public Trust Center is available at [trust.openrouter.ai](http://trust.openrouter.ai). For workloads in regulated industries, contact OpenRouter's enterprise team to confirm that specific compliance requirements are met before committing production traffic.

Hugging Face is the starting point for most open-source model evaluation. The platform hosts over 2 million models across text, vision, audio, embeddings, and image generation, and its Inference Providers API routes requests to 18 compute partners at zero markup on underlying provider rates. Developers use the Inference Playground to compare model outputs interactively before writing a single line of integration code.

Hugging Face overhauled its inference stack in 2025 with the Inference Providers system, which routes requests to third-party providers like Fireworks, Together, Groq, and Cerebras rather than relying on HF-hosted serverless infrastructure. The current docs describe the platform as "production-ready" and "built for enterprise workloads." That said, some users have reported reliability issues on the legacy HF-hosted inference backend: corrupted responses on large models, models dropping off the API without warning, and cold starts that can exceed three minutes on models not served by a third-party provider. The platform's strongest value is still in discovery and prototyping, though the Inference Providers layer has narrowed the gap with dedicated inference platforms.

- •**Models:** Meta Llama (3, 3.1, 3.3), DeepSeek (V3.2, R1), Mistral, Qwen, FLUX.1 and Stable Diffusion for image generation, OpenAI Whisper for speech-to-text, Sentence Transformers for embeddings
- •**Compatibility:** Python (`huggingface_hub` ), JavaScript/TypeScript (`@huggingface/inference` ); OpenAI-compatible via`https://router.huggingface.co/v1` for chat completions; image generation, embeddings, and speech tasks require the native SDK
- •**Endpoints:** Chat/completions, vision, code generation, embeddings, fine-tuning, audio/speech, image generation, function calling
- •**Pricing:** Free tier ($0.10/month in inference credits); PRO at $9/user/month; Team at $20/user/month; pay-as-you-go inference credits billed at underlying partner rates with no markup; dedicated Inference Endpoints billed hourly from $0.03/hr (CPU) to $80/hr (NVIDIA H100 x8 GPU cluster)
- •**Limitation:** Legacy HF-hosted serverless inference has documented reliability issues; the newer Inference Providers system routes to third-party backends with better uptime

Developers evaluating open-source models before committing to an inference provider. The Inference Playground lets you test dozens of model families against your actual prompts in minutes, and the zero-markup routing means you pay exactly what the underlying compute partner charges. Teams building RAG pipelines, multimodal applications, or audio workflows will find the endpoint breadth useful during the scoping phase. The migration path is clear: prototype here, then move to a dedicated inference provider before shipping to users.

- •**Zero-markup inference routing:** Hugging Face passes through partner compute costs directly, with no per-token margin added on top.
- •**Inference Playground:** Compare model outputs interactively across families before writing integration code or committing to a provider.
- •**Broadest open-source catalog available:** 2 million+ models spanning text, vision, audio, embeddings, and image generation under one API surface.

| Pros | Cons | 
|---|---|
| Largest open-source model catalog available, covering five modalities | Legacy HF-hosted inference backend (not Inference Providers) has documented reliability issues on large models | 
| Zero markup on inference: you pay the underlying provider rate directly | Cold starts on the legacy backend can last minutes, with timeouts at 7 minutes under parallel load | 
| OpenAI-compatible chat completions endpoint lowers migration friction | Models on the legacy backend can drop off without warning, breaking production implementations | 
| Free tier and Inference Playground enable fast model evaluation at no cost | Rate limit thresholds for Free and PRO tiers are undocumented, leaving developers without reliable planning data | 

The free tier includes $0.10/month in inference credits. PRO costs $9/user/month and unlocks pay-as-you-go inference billed at partner rates with no Hugging Face markup. The Team plan runs $20/user/month. Dedicated Inference Endpoints are billed hourly: $0.03/hr for an AWS CPU instance up to $80/hr for an NVIDIA H100 x8 GPU cluster. The three-layer structure (subscription plus inference credits plus endpoint hours) is a documented source of surprise charges; individual accounts have no built-in spending caps or automated cost warnings (Team and Enterprise orgs can set spending limits).

**Is the Hugging Face Serverless API Suitable for Production Traffic?**

The legacy HF-hosted serverless backend has documented reliability issues. However, the Inference Providers system now routes requests to production-grade backends like Fireworks, Together, Groq, and Cerebras. Teams running production traffic through Inference Providers get the reliability of those underlying platforms. For workloads requiring guaranteed uptime and hardware control, dedicated Inference Endpoints or a specialized inference provider remain the safer path.

**Does Hugging Face Add a Markup on Inference Costs?**

No. The Inference Providers layer routes requests to 18+ compute partners and charges the exact rate those partners publish. There is no per-token margin added by Hugging Face. The cost you see in the model catalog is what you pay, which is the same rate you would pay going directly to the partner. The PRO subscription ($9/month) is a separate platform access fee, not an inference markup.

Together AI is a full-stack open-source inference platform built by ML researchers, and that lineage shows in the infrastructure. The platform co-developed FlashAttention-4, achieving up to 1,605 TFLOPs/s on NVIDIA B200 GPUs, and routes that research directly into production throughput. Fastest models reach ~400+ tokens/second per Artificial Analysis. The OpenAI-compatible API means existing SDK code migrates without a rewrite.

As of May 2026, the Together AI catalog covers 200+ open-weight models across text, image, video, audio, and embeddings, making it one of the broadest multi-modal selections among hosted inference providers. That breadth comes with a cost: each of the models carries its own input and output token rates, and the billing surface across serverless inference, dedicated GPU clusters, image generation (per image), and text-to-speech (per character) is complex. Teams that need wide model access and can tolerate billing unpredictability will find Together AI a strong fit. Teams that need budget predictability at scale frequently find themselves building additional cost-tracking tooling on top.

- •**Models:** Meta Llama 3 and 4 families (including Llama 4 Maverick), DeepSeek-V3.1, V3.2-EXP, and R1, Qwen 3, Mistral variants, FLUX and Google Imagen for image generation, Google Veo 3.0 for video, Cartesia and Whisper for voice
- •**Compatibility:** Python and TypeScript/Node.js SDKs; OpenAI-compatible via`https://api.together.xyz/v1` ; integrates with Vercel AI SDK and Promptfoo
- •**Endpoints:** Chat/completions, vision, code generation, embeddings, fine-tuning, audio/speech, image generation, function calling
- •**Pricing:** Pay-as-you-go per token for serverless inference; 50% batch discount for async workloads; per-image for image generation; per-character for text-to-speech; per-hour for dedicated GPU clusters
- •**Limitation:** No free tier for new users; platform access requires a minimum $5 credit purchase, and premium models like FLUX Pro require $50 in lifetime spend before they become queryable

Together AI fits ML engineers and research teams that need the widest possible open-weight model selection, including multimodal coverage across text, image, video, and audio, without managing GPU clusters. The self-serve fine-tuning stack (SFT, DPO, and LoRA) makes it a reasonable choice for teams customizing open-weight models at the research stage. If your workload is exploration-heavy and you can tolerate per-model pricing variation, Together AI covers more ground in a single API than most alternatives.

- •**FlashAttention-4** (co-developed by Together AI's Chief Scientist Tri Dao) delivers up to 1,605 TFLOPs/s on NVIDIA B200 GPUs, with fastest models reaching 400+ tokens/second per Artificial Analysis.
- •**200+ model catalog across five modalities** , including text, image, video, audio, and embeddings, under one OpenAI-compatible API endpoint.
- •**Self-serve fine-tuning** via SFT, DPO, and full or LoRA adapters, without requiring enterprise gating or a separate vendor.

| Pros | Cons | 
|---|---|
| Broadest open-weight catalog in this roundup: 200+ models across text, image, video, audio, and embeddings | No free tier; requires a minimum $5 credit purchase to start, plus $50 lifetime spend to unlock premium models | 
| OpenAI-compatible API makes migration from existing code nearly frictionless | Billing unpredictability is a recurring complaint: per-model pricing varies widely and hidden operational costs often exceed listed API fees | 
| Self-serve fine-tuning (SFT, DPO, LoRA) available without enterprise gating | Serverless tier offers no infrastructure control; latency zone selection and hardware tuning require upgrading to Dedicated Endpoints | 
| 50% batch discount for async workloads reduces cost on non-time-sensitive inference | Navigating serverless quantization tiers (Turbo, Reference, Lite) and separate Dedicated Endpoint pricing can cause unexpected cost overruns when moving from dev to production | 

Together AI uses pay-as-you-go pricing with no mandatory subscription. Serverless text inference ranges from $0.10 per million tokens for smaller models (Llama 3 8B Instruct Lite) to $0.88 per million tokens for larger ones (Llama 3.3 70B). Llama 4 Maverick runs at $0.27 input / $0.85 output per million tokens. A 50% batch discount applies to async workloads. Image generation is billed per image, text-to-speech per character, and dedicated GPU clusters per hour. New users must purchase a minimum of $5 in credits to begin. For current model-specific rates, check [together.ai/pricing](http://together.ai/pricing).

**Does Together AI Support Fine-Tuning on Its Standard Pay-as-You-Go Plan?**

Yes. SFT, DPO, and LoRA fine-tuning are available to standard users without enterprise gating. Full fine-tuning is also supported. The fine-tuning stack is self-serve, meaning you can launch training jobs through the API without a sales conversation. Note that fine-tuning costs are separate from inference costs and billed at their own rates.

**Why Do Developers Report Billing Surprises on Together AI?**

The pricing surface is wide: each of the ~200 models carries unique input and output token rates, and different modalities (image, audio, video) use different billing units entirely. The serverless quantization tiers (Turbo, Reference, Lite) and separate Dedicated Endpoint pricing carry different cost profiles, and moving from development to production without explicitly configuring routing logic can result in unexpected charges. Developers building cost-sensitive applications typically need to instrument per-model spend tracking from the start rather than relying on aggregate billing summaries.

Groq runs custom Language Processing Units (LPUs) designed from the ground up to execute large language model inference at speeds GPU-based providers cannot match. Groq's LPU is an ASIC (Application-Specific Integrated Circuit) meaning a chip engineered entirely for one task: LLM token generation. Unlike GPUs, which are general-purpose processors adapted for AI workloads, ASICs sacrifice flexibility for extreme efficiency on their target function. That's the source of Groq's speed advantage, and also the reason its model catalog will always be narrow: the hardware can't be repurposed for arbitrary new architectures the way a GPU cluster can.

The result is consistently low time-to-first-token and 500+ tokens per second on select production models, with GPT-OSS 20B reaching ~903 tokens/sec per Artificial Analysis benchmarks. For real-time chat, voice agents, and interactive applications where latency is the primary constraint, no hosted API comes closer to instant.

**A significant development for teams evaluating Groq:** In late December 2025, Nvidia [licensed Groq's LPU technology and hired away its founding CEO and president](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html) in a deal reported by CNBC at approximately $20B, though terms were not independently verified or disclosed by Nvidia. Groq stated that GroqCloud will continue operating without interruption under new CEO Simon Edwards, and the cloud business was explicitly excluded from the transaction. However, the deal reduced Groq's technical staff substantially, and community sentiment among existing API users has trended negative, with developers citing concerns about the pace of new model additions and long-term product direction ([Groq Community, February 2026](https://community.groq.com/t/any-clarification-from-groq-team-about-the-future/1021)). For teams building production systems on Groq, this adds a new layer of platform risk worth factoring into your architecture decisions.

Outside of the Nvidia acquisition, the primary tradeoff with Groq is scope. Groq hosts a curated catalog of roughly a dozen production-ready text models rather than a broad library, offers no embeddings endpoint, and has a documented pattern of [deprecating models with short notice.](https://console.groq.com/docs/deprecations) Speed itself creates an additional constraint: because requests complete so fast, developers hit requests-per-minute ceilings faster than on any slower provider, turning Groq's core advantage into a rate-limit trap on the free tier. Most teams use Groq as the speed layer in a multi-provider architecture rather than a sole inference provider.

- •**Models:** Meta Llama 4 Scout, Llama 3.3 70B, Llama 3.1 8B, OpenAI GPT-OSS 20B and 120B, Qwen3 32B, Whisper Large v3 (audio), Canopy Labs Orpheus (TTS), Groq Compound (agentic orchestration), Groq Compound Mini.
- •**Compatibility:** OpenAI-compatible REST API at`https://api.groq.com/openai/v1` ; official Python and JavaScript/TypeScript SDKs; community libraries for C#, Dart, PHP, and Ruby
- •**Endpoints:** Chat/completions, vision, code generation, audio/speech, function calling; no embeddings, no image generation
- •**Pricing:** Pay-as-you-go per token; 50% batch discount; up to 50% prompt caching discount; free tier with no credit card required
- •**Limitation:** No embeddings API, requiring a separate provider for RAG pipelines or semantic search

Groq is the right choice when minimal time-to-first-token is a hard requirement and your workload fits within its model catalog. Groq achieves consistently low TTFT across its model catalog, with Llama 3.1 8B throughput reaching ~659 tokens/sec per Artificial Analysis. Real-time voice agents, interactive coding assistants, and user-facing chat interfaces all benefit directly from LPU-backed response times. Teams already on the OpenAI SDK can validate the speed advantage in under a minute. The free tier, which requires no credit card, removes signup friction entirely.

- •**LPU hardware delivers consistently low TTFT** across supported models, with no cold-start delays unlike GPU-based serverless providers.
- •**Drop-in OpenAI compatibility** means existing SDK code runs on Groq without logic rewrites; the one audit step is confirming parameter support before switching.
- •**Prompt caching cuts costs up to 50%** on requests sharing an identical token prefix, with cached tokens excluded from rate-limit counts.

| Pros | Cons | 
|---|---|
| Best-in-class throughput for interactive workloads, with GPT-OSS 20B reaching ~903 tokens/sec per Artificial Analysis | High speed accelerates developers into RPM ceilings faster than on any slower provider | 
| No credit card required for the free tier; Developer plan unlocks roughly 10x higher limits | Aggressive model deprecations with short notice force rapid code changes | 
| Transparent, linear pricing with no hidden fees or instance reservations | Rate limits apply per organization, not per API key, catching multi-project setups off guard | 
| 50% batch discount available for non-time-sensitive workloads | No embeddings endpoint; developers must manage a separate provider for RAG pipelines | 

Groq uses pay-as-you-go token pricing. Llama 3.1 8B Instant costs $0.05 per 1M input tokens and $0.08 per 1M output tokens. GPT-OSS 20B costs $0.075 input and $0.30 output per 1M tokens. Async batch processing carries a 50% discount off paid rates. Prompt caching offers up to 50% off cached token costs, with those tokens excluded from rate-limit calculations. The free tier is available with no credit card; the Developer plan unlocks roughly 10x higher consumption limits. For current rates across all models, check [groq.com/pricing](http://groq.com/pricing) directly.

**Does Groq's Speed Advantage Hold Under Production Load?**

Groq's LPU hardware delivers consistently fast inference with no cold starts, unlike GPU-based serverless providers. The caveat is rate limits: because requests complete so quickly, high-throughput workloads hit requests-per-minute ceilings faster than on slower providers. Building exponential backoff and retry logic into your integration is effectively mandatory for production use, not optional.

**Can I Use Groq as My Only Inference Provider?**

For most production teams, no. Groq has no embeddings endpoint, limited modality coverage, and a deprecation pattern that requires periodic code changes. The platform works best as the speed layer in a multi-provider setup: route latency-critical user-facing requests to Groq and handle embeddings, batch jobs, and fine-tuned models through a provider with broader coverage.

Cerebras Inference runs on the Wafer-Scale Engine-3, a processor that sidesteps GPU memory bottlenecks entirely. Like Groq's LPU, the Wafer-Scale Engine is an ASIC — a chip purpose-built for a specific workload (AI matrix operations at scale) rather than general-purpose compute. The entire silicon wafer functions as a single processor, eliminating the inter-chip communication overhead that slows GPU clusters. The tradeoff, consistent with any ASIC architecture, is that catalog breadth is constrained by what the hardware can efficiently execute. This explains why Cerebras supports only a handful of models rather than the broad catalogs available on GPU-backed providers.

As of publication, Cerebras has 4 active models supported — 2 production (Llama 3.1 8B, GPT-OSS 120B) and 2 preview (Qwen 3 235B Instruct, GLM 4.7) — and has recently announced the deprecation of Llama 3.1 8B and Qwen 3 235B Instruct on May 27, 2026, which would reduce the active catalog to 2 models. Note that Cerebras has also reduced free-tier rate limits on GPT-OSS 120B and GLM 4.7 due to high demand.

Albeit with a limited model catalog, Cerebras delivers benchmark-leading raw throughput: Artificial Analysis measures Llama 3.1 8B at ~2,328 tokens/sec on Cerebras, and GPT-OSS-120B at 2,053 tokens/sec. At those speeds, developers can rethink how they structure agentic loops, context retrieval, and UI rendering, not just swap a provider endpoint.

However, the gap between benchmark numbers and real-world experience is often a material consideration. Developer Adam Larson tested the Cerebras Code Max plan extensively and [reported never hitting 500 tokens/sec](https://www.youtube.com/watch?v=7Ut2lpNVZSQ) on extended runs, let alone the marketed 2,000, with throughput dropping under 100 tokens/sec on shorter tasks. While still exceptionally fast compared to many large models, he cites TPM throttling, peak-hour queuing, and context windows capped below native model limits as issues impacting the advertised speed. While the Cerebras hardware has incredibly fast theoretical speed, it appears that the overall platform has not been able to consistently live up to the hardware's theoretical potential.

- •**Models:** Meta Llama 3.1 8B, OpenAI GPT-OSS-120B, Qwen 3 235B Instruct (preview), GLM 4.7 (preview)
- •**Compatibility:** Python and Node.js SDKs; OpenAI-compatible via`https://api.cerebras.ai/v1` ; standard parameters including`frequency_penalty` ,`logit_bias` , and`presence_penalty` are unsupported and return 400 errors
- •**Endpoints:** Chat/completions, code generation, function calling; no vision, embeddings, audio, or image generation
- •**Pricing:** Free tier at 1M tokens/day; Developer pay-as-you-go from $0.10/1M tokens (Llama 3.1 8B); Cerebras Code Pro at $50/month and Code Max at $200/month for coding workloads; enterprise custom pricing
- •**Limitation:** Advertised speeds of 2,000+ tokens/sec frequently do not materialize in production, with real-world throughput reported well below 500 tokens/sec in extended testing

Cerebras fits teams routing speed-critical, high-volume synchronous tasks where raw throughput matters more than catalog breadth. The 1M token/day free tier covers prototyping agentic workflows and small internal tools without immediate budget pressure. Engineers building multi-provider architectures often assign Cerebras to the fast path while keeping other providers for deep-context reasoning, complex structured output, or modalities the platform does not support.

- •Wafer-Scale Engine-3 hardware delivers benchmark-leading throughput, with Llama 3.1 8B measured at ~2,328 tokens/sec by Artificial Analysis.
- •Free tier provides 1M tokens per day with no waitlist, covering serious prototyping and pilot workloads without a credit card.
- •Token bucketing rate-limit algorithm replenishes capacity continuously rather than resetting at fixed intervals, reducing burst-then-idle patterns.

| Pros | Cons | 
|---|---|
| Benchmark-leading raw throughput on supported models, validated by Artificial Analysis | Real-world throughput frequently falls well below benchmark figures, per independent developer testing | 
| 1M tokens/day free tier with no waitlist, viable for real prototyping | Context windows capped below native model limits, constraining complex agentic and coding workflows | 
| OpenAI-compatible API; the key integration step is auditing for unsupported parameters before switching | TPM throttling and peak-hour queuing undercut the speed advantage the platform is built around | 
| Consistent performance under load due to deterministic Wafer-Scale Engine execution | Catalog limited to 4 active models, with 2 further deprecations announced for May 27, 2026; no embeddings, vision, audio, or image generation endpoints | 

The free tier covers 1M tokens per day with no credit card required. Pay-as-you-go Developer pricing starts at $0.10 per 1M tokens for Llama 3.1 8B, with rates varying up to $2.25/M input and $2.75/M output for GLM-4.7, a 24x spread across the catalog. Cerebras also offers Code Pro ($50/month) and Code Max ($200/month) subscription plans for coding workloads, with higher rate limits and daily token allowances. Enterprise pricing is custom. Note that PayGo credits and subscription plans cannot be combined on the same model.

**Does Cerebras Support Prompt Caching?**

Yes. Cerebras offers automatic prompt caching at no additional cost, with no code changes required. The system processes prompts in 128-token blocks and reuses cached computations from recent requests within the same organization. Cached tokens are not billed separately, making repeated system prompts and shared context prefixes more cost-efficient for agentic workflows.

**Which OpenAI API Parameters Does Cerebras Not Support?**

Cerebras drops several standard OpenAI parameters: `frequency_penalty`, `logit_bias`, and `presence_penalty` all return 400 errors. Teams migrating from OpenAI or routing through a multi-provider layer need to strip these parameters before sending requests to Cerebras, or they will see silent failures in frameworks that do not surface the underlying 400 response cleanly.

Baseten is an inference platform built for ML engineering teams that need maximum control over how models run in production. Where managed API providers abstract away infrastructure entirely, Baseten exposes it: you select the GPU, configure the serving engine, set your autoscaling rules, and own the deployment. The platform converts models — open-source, custom, or fine-tuned — into production-ready API endpoints with autoscaling, observability, and optimized serving infrastructure.

Baseten raised $300M in a Series E round in January 2026 at a $5B valuation, led by IVP and CapitalG, with Nvidia anchoring the round. The round reflects the growing enterprise demand for high-performance inference infrastructure that is not locked to a single model family or cloud provider. Customers including Cursor, Notion, and Clay use Baseten to power custom model deployments that require dedicated hardware, private endpoints, and compliance guarantees.

The platform includes Baseten Chains, a multi-step inference orchestration framework that lets different steps in a pipeline run on different hardware — useful for RAG systems, voice AI pipelines, and compound agent workflows. Baseten also offers multi-node fine-tuning and pre-training jobs that can be promoted directly to production endpoints, and Baseten Embeddings Inference, which is optimized specifically for throughput and latency on RAG and search workloads.

Baseten's Frontier Gateway product lets AI labs white-label Baseten's serving infrastructure under their own brand, positioning Baseten as infrastructure-of-record for model labs that need managed serving without building their own platform.

- •**Models:** DeepSeek V3/V4, Llama 4 Scout/Maverick, Llama 3.3, Kimi K2.6, GLM 5, Gemma 3, Qwen, NVIDIA Nemotron 3, Whisper, and any custom model packaged via the Truss framework. No fixed catalog — you deploy any model on your own GPU allocation.
- •**Compatibility:** OpenAI-compatible endpoints for Model APIs; custom Truss deployments follow your own API contract; integrates with Datadog for observability
- •**Engines:** Engine-Builder-LLM (TensorRT-LLM compilation for GPT-class models), BIS-LLM (optimized for mixture-of-experts models like DeepSeek), BEI (embeddings inference)
- •**Endpoints:** Chat completions (OpenAI-compatible via Model APIs), embeddings, custom multi-step pipelines via Chains SDK, fine-tuning/pre-training
- •**Pricing:** Pay-as-you-go GPU compute per minute. H100 (80GB): $0.10833/min (~$6.50/hr); A100 (80GB): $0.06667/min (~$4.00/hr); A10G: $0.02012/min; Model API per-token pricing (e.g., DeepSeek V4: $1.74 input / $3.48 output per 1M tokens). Enterprise volume discounts available. Free experimentation credits for new accounts.
- •**Compliance:** SOC 2 Type II certified, HIPAA-compliant, GDPR-enabled
- •**Limitation:** Requires meaningful ML engineering investment to use effectively. Baseten is not a turn-key API — deploying a custom model requires packaging via Truss, configuring serving engines, and managing GPU infrastructure. Teams without dedicated MLOps capacity will find the setup overhead significant compared to managed API providers.

Baseten is the right choice for ML engineering teams deploying custom, fine-tuned, or proprietary models in production — the kind of teams building at Cursor-scale AI features that require dedicated GPU instances, HIPAA compliance, multi-node training pipelines, and advanced observability. It is also the platform of choice for AI labs that need to serve their own model weights to customers without building their own infrastructure. Teams prototyping on a managed API and evaluating whether to migrate to dedicated infrastructure will find Baseten's Model APIs a useful middle ground — OpenAI-compatible endpoints for popular open-source models with per-token pricing — before committing to the full Dedicated Deployment setup.

- •**Dedicated Deployments with GPU selection:** Choose specific GPU types (H100, B200, A100, A10G, L4, T4) and configure instances for your exact performance and cost requirements. No shared compute; your model runs on dedicated hardware.
- •**Baseten Chains:** Multi-step inference pipelines where each step can run on different hardware, with point-to-point communication. Enables complex compound AI systems — voice AI, RAG, agentic workflows — without a separate orchestration layer.
- •**Engine-level optimizations:** TensorRT-LLM compilation (Engine-Builder-LLM), MoE-specific optimization (BIS-LLM), and embeddings-specific serving (BEI) built into the platform. You get hardware-level performance without implementing it yourself.
- •**Frontier Gateway:** White-label serving infrastructure for AI labs — Baseten operates the infrastructure while labs expose it under their own brand and API surface.

| Pros | Cons | 
|---|---|
| Maximum infrastructure control: choose GPU, configure engines, set autoscaling rules | Significant MLOps overhead — requires Truss packaging, engine configuration, and infrastructure management | 
| SOC 2 Type II, HIPAA, and GDPR compliance make it viable for regulated industries | Pricing is primarily per-GPU-minute, not per-token — cost modeling requires capacity planning rather than simple per-call estimates | 
| Multi-node fine-tuning and pre-training with direct promotion to production endpoints | No managed model catalog in the traditional sense — you bring your model; Baseten provides the infrastructure | 
| Baseten Chains enables multi-hardware pipeline orchestration without a separate framework | Less suited for teams that want zero infrastructure work — managed API providers like Fireworks offer simpler onboarding with fewer knobs | 
| 225% better cost-performance on high-throughput inference vs. standard GPU cloud deployments (per Google Cloud benchmark on A4/Blackwell hardware) | Enterprise features and dedicated Slack/Zoom support require Pro or Enterprise tier; Basic tier is self-serve only | 

Baseten charges for GPU compute time, not per token. GPU pricing per minute: H100 (80GB) at $0.10833/min (~$6.50/hr), B200 (180GB) at $0.16633/min (~$9.98/hr), A100 (80GB) at $0.06667/min (~$4.00/hr), A10G (24GB) at $0.02012/min, L4 (24GB) at $0.01414/min, T4 (16GB) at $0.01052/min. CPU instances range from $0.00058/min (1 vCPU, 2GB RAM) to $0.01382/min (16 vCPUs, 64GB RAM). Model API pricing (per-token, for one-click model access) includes: DeepSeek V4 at $1.74 input / $3.48 output per 1M tokens, DeepSeek V3.1 at $0.50 input / $1.50 output, Kimi K2.6 at $1.00 input / $3.90 output, GLM 5 at $0.95 input / $3.15 output. New accounts receive free credits for experimentation. Pro and Enterprise tiers offer volume discounts and dedicated GPU access. Contact [baseten.co](http://baseten.co) for enterprise pricing.

**Do I Need to Be an ML Engineer to Use Baseten?**

Effectively, yes for Dedicated Deployments. Baseten requires packaging models via the open-source Truss framework, configuring serving engines, and managing GPU resources. This is meaningfully more complex than calling a managed API. Baseten's Model APIs offer a simpler entry point — one-click OpenAI-compatible endpoints for popular open-source models — but the platform's full value is in Dedicated Deployments, which require MLOps capacity to use well.

**How Does Baseten Compare to Just Renting a GPU from a Cloud Provider?**

Baseten sits between a raw GPU rental (like a Lambda Labs instance or AWS p4de) and a fully managed inference API. You get production-grade serving infrastructure — autoscaling, load balancing, TensorRT-LLM compilation, observability dashboards — without building it from scratch. The tradeoff versus a fully managed API is that you manage the deployment; the tradeoff versus a raw GPU is that you get production-grade serving infrastructure out of the box. Baseten benchmarks cite 225% better cost-performance vs. standard GPU cloud deployments for high-throughput inference on Google Cloud A4 (Blackwell) hardware.

Modal is a serverless GPU infrastructure platform that lets Python developers deploy any workload — inference, fine-tuning, batch jobs, sandboxes — without managing servers or Kubernetes. The core abstraction is the Python decorator: annotate a function with `@app.function(gpu="H100")` and Modal handles containerization, GPU scheduling, autoscaling, and billing. The platform's Rust-based container stack spins up GPUs in under 1 second, making cold starts effectively invisible for most workloads.

Modal closed an $87M Series B in September 2025 at a $1.1B valuation. Customers include Lovable, Substack, Suno, and Cognition AI — a mix of fast-growing AI-native companies and established enterprises that want GPU infrastructure without the operational overhead of managed clusters.

Modal's differentiation is that it gives you full code control with serverless economics. Unlike managed API providers that abstract everything, Modal runs your code, on your chosen hardware, with your inference framework of choice (vLLM, SGLang, TGI, TensorRT, or anything else). Unlike raw cloud GPU rentals, it handles all infrastructure work automatically. The platform supports the full ML lifecycle under one billing account: online inference, offline batch, training, sandboxes, and notebooks.

- •**Models:** Any open-source or custom model; no fixed catalog. Production-ready examples include Llama 3/4, Qwen3, FLUX Kontext, Whisper, Kyutai STT, Mistral, vision-language models, protein folding models, and text embedding models. You choose the model and framework.
- •**Compatibility:** You implement your own endpoint; OpenAI-compatible APIs are achievable (Modal provides example templates) but not automatic. Integrates with any Python ML library.
- •**Engines:** vLLM, SGLang (recommended for H100/H200 decode-heavy workloads), TGI, TensorRT, Unsloth (fine-tuning), torchtune, GRPO, and any other framework installable via pip
- •**Endpoints:** Online inference (real-time with token streaming, WebRTC, WebSocket support), offline batch processing, fine-tuning (SFT, RL via GRPO), sandboxes (secure ephemeral environments for AI-generated code), notebooks (GPU-backed collaborative notebooks)
- •**Pricing:** Consumption-based per-second GPU compute; no idle charges; auto scale-to-zero. H100: $0.001097/sec (~$3.95/hr); H200: $0.001261/sec (~$4.54/hr); B200: $0.001736/sec (~$6.25/hr); A100 (80GB): $0.000694/sec (~$2.50/hr); L4: $0.000222/sec; T4: $0.000164/sec. CPU: $0.0000131/core/sec. Starter plan: $30/month free credits, 10 GPU concurrency. Team plan: $250/month + compute, $100/month free credits, 50 GPU concurrency. Enterprise: custom.
- •**Compliance:** SOC 2 and HIPAA compliant; zero data retention security model
- •**Limitation:** No managed model catalog. You must write inference code, select your framework, and handle model loading, batching, and API design yourself. This is a meaningful setup investment compared to turn-key providers. Not suitable for teams that want to call an endpoint and go.

Modal is best for Python-native engineering teams that want maximum flexibility and serverless GPU economics without infrastructure management. It excels for: custom model deployments where no managed provider hosts your model; batch inference at scale (evaluations, RL rollouts, document processing); fine-tuning pipelines that need GPU-backed training without managing a cluster; teams building multi-step AI applications that combine inference, code execution (Sandboxes), and batch jobs in a single Python codebase. Modal can save 50%+ on high-throughput, short-context tasks compared to per-token API providers, per Modal's own benchmarks — though the comparison depends heavily on workload characteristics. Teams without Python ML engineering capacity or teams that want a zero-setup API call should use a managed provider instead.

- •**Sub-second cold starts:** Rust-based container stack launches GPU containers in under 1 second; GPU snapshotting loads 7B+ models in seconds rather than minutes.
- •**Full code control:** You run your own inference code in your own container — no black-box serving, no model lock-in, no framework constraints. Use any library, any model, any optimization technique.
- •**Unified ML lifecycle:** Online inference, batch processing, fine-tuning, sandboxes, and notebooks all under one platform and one billing account. No stitching together separate services.
- •**Scale to zero:** Automatic scale-to-zero when idle means you pay nothing when traffic stops — unlike dedicated GPU deployments billed by the hour.

| Pros | Cons | 
|---|---|
| Sub-second GPU cold starts and GPU snapshotting for fast model loading eliminate cold-start latency issues | No managed model catalog — you must write your own inference code and handle model loading, batching, and API design | 
| Full code control: any framework, any model, any optimization technique, no black-box constraints | Higher setup effort than turn-key API providers; requires Python ML engineering capacity | 
| Consumption-based per-second billing with auto scale-to-zero; no idle charges | OpenAI compatibility requires implementation; not drop-in compatible out of the box | 
| $30/month in free compute credits with no commitment (Starter plan) | GPU availability during peak demand may require retry logic; no guaranteed capacity without enterprise tier | 
| SOC 2 and HIPAA compliant with a zero data retention security model | Documentation and examples cover common use cases, but less hand-holding than managed API providers | 

Modal charges per second of actual GPU compute used, with no charges for idle time. GPU rates: H100 at $0.001097/sec (~$3.95/hr equivalent), H200 at $0.001261/sec (~$4.54/hr), B200 at $0.001736/sec (~$6.25/hr), A100 80GB at $0.000694/sec (~$2.50/hr), L4 at $0.000222/sec, T4 at $0.000164/sec. CPU compute: $0.0000131/core/sec. Storage: $0.09/GiB/month with 1 TiB free. The Starter plan includes $30/month in free compute credits with 3 workspace seats and 10 GPU concurrency. The Team plan is $250/month plus compute, includes $100/month in free credits, unlimited seats, and 50 GPU concurrency. Enterprise pricing is custom with higher GPU concurrency and volume discounts. Startup and academic grant programs offer up to $10,000 in free compute. See [modal.com/pricing](http://modal.com/pricing) for current rates.

**How Is Modal Different from Just Renting a GPU on Lambda Labs or RunPod?**

Raw GPU rentals give you a machine; you build everything else — containerization, serving, autoscaling, load balancing, and billing management. Modal handles all of that automatically in exchange for writing infrastructure logic as Python decorators. The key advantages over raw GPU rental are: auto scale-to-zero (you pay nothing when idle), sub-second cold starts (GPU snapshotting makes model loading fast), and a unified platform for inference, batch, and training without managing separate clusters.

**Can I Use Modal for Production LLM Inference at Scale?**

Yes, and it is in production at companies including Lovable, Harvey AI, and Mistral. The practical requirements are: you need to implement your inference server (Modal provides templates for vLLM and SGLang), handle batching and streaming logic, and design your own API surface. For teams with Python ML engineering capacity, Modal can deliver lower latency and lower cost at scale than per-token API providers — particularly for high-throughput, short-context workloads. For teams that want a zero-configuration endpoint, a managed API provider is a better fit.

Fireworks hosts 200+ open-source models across text, vision, audio, embeddings, and image generation, with new model weights going live within 24 hours of public release. Every model runs on FireAttention, Fireworks' production inference engine. If your foundation model needs adaptation, FireOptimizer covers the full post-training stack: SFT, LoRA fine-tuning, RFT, and RL pipelines, all self-serve, no second vendor required. [Start with the Serverless API](https://docs.fireworks.ai/getting-started/quickstart) if you're evaluating On-Demand or Enterprise Reserved GPU options.

Pricing and feature data gathered from official provider documentation and publicly available benchmark sources including Artificial Analysis. Rates and model availability change frequently. Verify current pricing and catalog details at each provider's site before making infrastructure decisions.
