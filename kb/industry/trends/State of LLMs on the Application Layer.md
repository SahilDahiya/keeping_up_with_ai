---
title: State of LLMs on the Application Layer
topic: industry
subtopic: trends
secondary_topics:
- models/benchmarks
summary: Application-layer snapshot of LLM usage and model trends, useful for understanding
  production model adoption and quality/cost tradeoffs.
source: langfuse
url: https://langfuse.com/blog/2025-10-13-state-of-llms-september-2025
author: null
published: '2025-10-13'
fetched: '2026-07-11T04:35:43Z'
classifier: codex
taxonomy_rev: 1
words: 733
content_sha256: b09783f593c373faaa36885bf9ba2351e9055371e18c57e88e09a93cf0b2bda4
---

# State of LLMs on the Application Layer

# State of LLMs on the Application Layer

We have analyzed model adoption of 20.000+ organizations building LLM applications and agents in the last 12 months. Here is what we found.

![Picture Felix Krauth](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Ffelixkrauth.jpg&w=96&q=75) Felix Krauth

Felix Krauth[About Langfuse](https://langfuse.com#about-langfuse)

Langfuse is the [leading open source LLM observability platform](https://langfuse.com/blog/2024-11-most-used-oss-llmops) powering safe and scalable LLM applications for 10s of thousands of organizations. The data on Langfuse Cloud tells a story of a rapidly growing market and allows us to get a unique view on the state of the LLM application layer.

We power global enterprises like [Khan Academy](https://langfuse.com/users/khan-academy), [SumUp](https://langfuse.com/users/sumup) and [Merck](https://langfuse.com/users/merckgroup) as well as AI-native startups like [Magic Patterns](https://langfuse.com/users/magic-patterns-ai-design-tools), [Circleback](https://circleback.ai/) and [Juicebox](https://juicebox.ai/) to build safe and scalable LLM applications and agents.

[About this Report](https://langfuse.com#about-this-report)

The core of what we do is helping developers to ship LLM applications and agents faster and more reliably. Our dataset gives a **unique view on how models are adopted on the application layer** instead of consumers that use those models via apps like Claude, Gemini or ChatGPT.

- The data comes from **over 20.000 organizations**on Langfuse Cloud
- **Billions of LLM traces and observations**(- [see data model](https://langfuse.com/docs/observability/data-model)) on Langfuse Cloud (no self-hosted data included)
- **59 unique models tracked across major providers**, longtail of models is not included and grouped into "Other"
- **Time Period:**12 months (Oct 2024 - Sep 2025)

[Status Quo in September 2025](https://langfuse.com#status-quo-in-september-2025)

Here is where the market stands in September 2025: OpenAI is still the dominant player (55.3%), followed by Google (13.1%) and Anthropic (7.3%). The longtail of models is not included and grouped into "Other" (24.3%).

![Status Quo in September 2025](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-10-13-state-of-llms-september-2025%2FMarketshare-sep.png&w=3840&q=75)


[Change over the last 12 months](https://langfuse.com#change-over-the-last-12-months)

The past 12 months show clear changes in the market.

![Status Quo in September 2025](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-10-13-state-of-llms-september-2025%2FMarketshare-12mo.png&w=3840&q=75)


| Provider | Sep 2025 | Oct 2024 | Change |
|---|---|---|---|
| OpenAI | 55.3% | 82.7% | -27.4 pts |
| Other | 24.3% | 10.0% | +14.3 pts |
| 13.1% | 0.5% | +12.6 pts | |
| Anthropic | 7.3% | 6.8% | +0.5 pts |

[Key Insights](https://langfuse.com#key-insights)

- **OpenAI is yielding market share**(down -27.4 points) while Google, Anthropic and "Other" model providers grow.
- **Google's Rise:**Google went from 0.5% → 13.1% (26x) share in just 12 months.
- **Anthropic is relatively stable**at 7.3%
- **"Other" models rising**strongly signals that the LLM market is fragmenting beyond the "Big Three," with organizations adopting specialized models, open-source alternatives, and regional providers.

[Market Share by Model](https://langfuse.com#market-share-by-model)

Let's take a look at market shares on model level.

![Market Share by Model](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-10-13-state-of-llms-september-2025%2Ftop-models-over-time.png&w=3840&q=75)


**What we see**

- The market is operating on a **~6 month effective model lifecycle**– Several October 2024 top-20 models effectively disappeared
- **Application builders are heavily relying on small efficient models**(OpenAI nano or mini: Gemini Flash; Anthropic’s Opus model not relevant)
- The **story isn't "OpenAI vs everyone else"—it's fragmentation vs. consolidation**. While the Big Three (OpenAI, Google, Anthropic) consolidate around 75% of tracked share, the "Other" 25% represents hundreds of specialized models serving specific use cases, geographies, or price points.

**Key Takeaways:**

- **Organizations aren't building on stable platforms**; they're building on a constantly shifting foundation. This creates both opportunity (rapid innovation) and risk (technical debt accumulates fast).
- **Staying flexible and being ready to swap out models will pay off**when building applications and underlying infrastructure.

[Top 15 Models - September 2025](https://langfuse.com#top-15-models---september-2025)

- GPT-4o mini (OpenAI): 14.2%
- GPT-4o (OpenAI): 10.9%
- GPT-4.1 (OpenAI): 9.8%
- gemini-2.5-flash (Google): 9.4%
- GPT-4.1 mini (OpenAI): 8.3%
- gemini-2.0-flash (Google): 3.7%
- Claude Sonnet 4 (Anthropic): 3.6%
- GPT-5 nano (OpenAI): 3.4%
- GPT-5 mini (OpenAI): 3.2%
- GPT-5 (OpenAI): 1.7%
- Claude Sonnet 3.7 (Anthropic): 1.5%
- GPT-4.1 nano (OpenAI): 1.0%
- o3 (OpenAI): 0.9%
- o4-mini (OpenAI): 0.6%
- Claude Sonnet 3.5 (Anthropic): 0.6%

[Top 15 Models - 12 Month Average](https://langfuse.com#top-15-models---12-month-average)

- GPT-4o mini (OpenAI): 24.2%
- GPT-4o (OpenAI): 16.4%
- GPT-4.1 mini (OpenAI): 6.6%
- GPT-4.1 (OpenAI): 6.3%
- gemini-2.0-flash (Google): 5.3%
- gemini-2.5-flash (Google): 4.4%
- Claude Sonnet 4 (Anthropic): 2.0%
- GPT-4.1 nano (OpenAI): 1.8%
- Claude Sonnet 3.7 (Anthropic): 1.8%
- Claude Sonnet 3.5 (Anthropic): 1.2%
- GPT-5 nano (OpenAI): 1.1%
- GPT-5 mini (OpenAI): 0.8%
- Claude Haiku 3 (Anthropic): 0.8%
- text-embedding-3-large (OpenAI): 0.7%
- text-embedding-ada-002 (OpenAI): 0.7%

**Data source:** Langfuse LLM observability platform

**Analysis period:** October 2024 - September 2025

*Want to reach out to talk about this story? Write us at  press@langfuse.com.*
