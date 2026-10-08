---
title: Sentient & Fireworks Powers Decentralized AI At Viral Scale
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/Story-Sentient
author: null
published: '2026-07-16'
fetched: '2026-10-08T06:11:22Z'
classifier: null
taxonomy_rev: 2
words: 1215
content_sha256: 081cd79d57b05cd12ad1da2192917f14413cc09583f5a556db2b0f0307e61c66
---

# Sentient & Fireworks Powers Decentralized AI At Viral Scale

- •**1.8M+ Waitlisted Users in 24 Hours**: Viral launch built for massive early interest for Sentient's products.
- •**25-50% More Concurrent Users per GPU**: Industry-leading efficiency vs. tested alternatives.
- •**Enterprise-Grade Performance without Overhead**: Cost-effective scale, even under extreme concurrency.
- •**Rapid Iteration & Launch:** From hackathon to public release of a 70B model powering multi-agent chat in weeks, not months.

Backed by $85 million from Founders Fund, Pantera, Framework Ventures, and Polygon Labs, Sentient unites Sandeep Nailwal (Polygon), Himanshu Tyagi (Witness Chain), and Princeton professor Pramod Viswanath at the helm. Their Princeton-driven research team is chasing a single, audacious goal: deliver the ultimate AI experience by fusing the planet’s collective intelligence into one open, decentralized network. Powered by blockchain and open-source models, Sentient turns transparency into a feature and democratizes AI for everyone.

At the helm of product, Technical Product Manager Oleg Golev leads the charge in bringing that vision to life – starting with **Dobby**, an open-source family of LLMs showcasing AI loyalty at the model layer, fine-tuned to be loyal to personal freedom and the crypto community. The models possess unique qualities (distinct personality traits and human-like tone) that make it a perfect choice for content virality, while maintaining academic breakthroughs in post-training value and safety alignment.

“The Open World is the world we want to live in, but it is only possible by leveraging blockchain to make AI more transparent and just.” - Sandeep Nailwal, Cofounder of Polygon & Sentient [source](https://thedefiant.io/news/press-releases/vitalik-buterin-and-sandeep-nailwal-headline-decentralized-agi-summit-ethdenver-tackling-threats-of-centralized-ai?)

Their flagship app, **Sentient Chat**, initially integrated 15 specialized AI agents to deliver fast, complex workflows for research, productivity, and search — alongside Open Deep Search (ODS), a fast, transparent search alternative that outperformed closed-source systems on search benchmarks (SimpleQA and FRAMES) that outperformed Perplexity and ChatGPT on search benchmarks.

These efforts target systems like ChatGPT and Gemini as part of a broader vision to scale community-driven AI products that compete with closed-source incumbents.

**Dobby Arena**: An early experimental platform for community feedback that supported initial tuning of the Dobby models and user experience—though the real impact comes from the Sentient Chat, multi-agent framework, and underlying model innovations.

**Sentient Chat**: A production-grade multi-agent assistant powered by Dobby-70B, launched virally at the Open AGI Summit during ETH Denver with over 1.8 million users waitlisted in 24 hours.

**Open Deep Search**: A complementary project which enables transparent, high-speed search that supports Sentient’s vision of decentralized AI infrastructure. Achieving SOTA benchmarks on SimpleQA and FRAMES benchmarks, ODS is built to challenge opaque algorithms and pairs naturally with Sentient Chat to deliver fast, explainable search in multi-agent workflows.

These products required infrastructure that could handle real-time inference, extreme concurrency, and unpredictable traffic—all without compromising on latency or reliability.

Sentient’s products went viral fast. But viral success brings infrastructure pain, such as:

**Concurrency Bottlenecks**: Multi-agent reasoning, multiple LLM calls, and real-time search required low latency performance to maintain user trust, especially during multiturn conversations.

**Unpredictable Spikes:** Waitlist-gated product launches opened to users via random access code leads to sudden spikes, sometimes thousands of concurrent users with no time for manual scaling.

**Costly Inefficiencies at Scale:** Internal GPU clusters and infra like vLLM would have required more GPUs for less throughput.

**No Room for Downtime**: Slowdowns meant lost momentum against fast-moving competitors like ChatGPT and Claude.

Sentient benchmarked multiple infra providers, including custom silicon options. Fireworks outperformed all, delivering **up to 50% more throughput per GPU** and more consistent performance under real-world load. This translated into fewer GPUs, lower costs, and seamless launches.

“In our first app, we recorded **1.5 million responses in five days**, from **90,000 unique users**, with up to **1,000–2,000 active users at any given time**. That was with a **query cap of 10–20 per user**.”

Fireworks provided a custom-engineered, high-performance infrastructure platform platform built on NVIDIA Blackwell and designed specifically for high-concurrency, burst-tolerant AI workloads for top performance under extreme load. Starting in January 2025, they used:

**Serverless endpoints** for fast iteration, testing, and deployment

**Custom-dedicated deployments** for real-time inference in Sentient Chat and Dobby Arena

**FP8-optimized hardware** enables high throughput for tasks like summarization and sentiment analysis while efficiently utilizing GPU resources.This setup let Sentient iterate rapidly and scale confidently—without building and managing hyperscale infrastructure themselves. Fireworks evolved from a technical solution to a strategic growth multiplier.

Fireworks began working with Sentient in early January 2025 to support the Dobby model rollout and community engagement campaigns.

**Jan 25** Sentient x Fireworks Hackathon (150–200 attendees) with early access to Dobby-Mini

**Jan 27** Public release of **Dobby-Preview-1-8B** and **Dobby-Preview-2-8B**

**Feb 3–7** Internal migration to **Dobby-70B** for primary workloads

**Feb 12** Public release of **Dobby-70B** on Fireworks

**Feb 18** Launch of **Dobby Arena V2** (benchmark testing against other models)

**Feb 26** Launch of **Sentient Chat**, closure of Dobby Arena (\~13 QPS, 5.6M queries)

Throughout these launches, Sentient combined **serverless endpoints** and **custom-tuned deployments** to support testing, scaling, and launch without performance degradation.

**Challenge**: Ensure instant UX, even for multiturn conversations.

**Solution**: Low-latency inference across workloads.

**Result:** Native-app-like responsiveness with industry-leading speed and consistency.

**Challenge**: Support thousands of concurrent users, agents, and API calls without slowdowns or failures.

**Solution**: Maintained low timeout and failure rates, even under intense load.

**Result**: Smooth experience during viral moments (thousands of concurrent users) with no GPU glitches.

**Challenge**: Serverless endpoints alone couldn’t meet ultra-low latency needs.

**Solution**: Fully managed dedicated deployments tuned to Sentient’s needs.

**Result**: Consistent performance across devices and networks without self-hosting burden.

✅ **25-50% Higher Throughput Per GPU**: More queries, users, and agents per dollar.

✅ **Enterprise-Grade Latency & Uptime**: Instant user experience with Sub-2s responses even in complex multi-agent scenarios.

✅ **Stable Under Viral Load**: 5.6M+ queries in a week with zero degradation.

✅ **Fast Iteration + Production-Grade Reliability**: Serverless endpoints enabled rapid shipping. Dedicated deployments ensured real-time performance.

✅ **Expanded Product Potential**: Unlocks multi-agent reasoning, RAG, reasoning, summarization, and search.

**3.2M+ model queries**

**155K+ unique users**

**\~8 queries per second**

**1.8M+ votes cast** comparing Dobby 70B to other LLMs

**5.6M+ model queries**

**190K+ unique users**

**\~13 queries per second**

**2M+ votes cast** comparing Dobby 70B to other LLMs

- •Near-instant response speeds
- •Powered by Fireworks' infrastructure
- •Integrated initially with 15 community-built AI agents + real-time search - with many more
- •rolling out over the coming months
- •Positioned as a challenger to ChatGPT, Gemini, and Claude

**Customer Quote**

“The very first feedback we got from early testers of Sentient Chat was, ‘Wow, how did you get it this fast?’ It was running on Fireworks. Somehow they’re doing magic behind the scenes to make high-concurrency workloads just work.”— **Oleg Golev, Technical Product Manager, Sentient**

Sentient didn’t just need infrastructure; they needed leverage. Fireworks delivered. Aligned on performance, reliability, and ambition, Sentient, creator of the Dobby open-source AI models, chose Fireworks to match their pace as they advance the frontier of applied AI with rigor and speed. With Fireworks’ Blackwell-optimized inference stack, they achieved:

- •25–50% more users per GPU
- •Sub-2s responses kept users engaged, even under peak load
- •No slowdowns or failures—even with thousands of concurrent users
- •Leveraging Fireworks’ infrastructure, Sentient scaled testing and accelerated iteration.

Sentient builds cutting-edge AI. Fireworks makes it run faster, scale further, and stay resilient.

Sentient scaled like a hyperscaler—without the cost or complexity. Fireworks provided serverless speed, custom deployment power, and cost-efficient growth.
