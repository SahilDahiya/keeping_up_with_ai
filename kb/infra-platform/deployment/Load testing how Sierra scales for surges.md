---
title: 'Load testing: how Sierra scales for surges'
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/testing
summary: Explains load testing for agent systems so conversation serving can scale
  through traffic surges without quality or latency collapse.
source: sierra
url: https://sierra.ai/blog/load-testing
author: Mark McBride
published: '2026-05-12'
fetched: '2026-07-11T03:52:34Z'
classifier: codex
taxonomy_rev: 1
words: 765
content_sha256: 177af7d2714752974cdf060d7d9b997ccf5843933dc93deb58ff8fe4adb169ef
---

# Load testing: how Sierra scales for surges

# Load testing: how Sierra scales for surges

Call volume in customer service can fluctuate wildly. Sometimes these surges are predictable — the holiday rush, Black Friday, a price increase, or a product update. Other times, they’re not: a viral meme, a local emergency, or an unexpected outage. Whatever the cause, AI agents need to be ready.

For Sierra, that readiness starts with ensuring our platform is robust enough to handle the huge increases in traffic we’re seeing as more companies launch agents and as voice conversations take off. But we also run targeted load tests when specific brands are preparing for major events like big sales or seasonal spikes.

## Testing at the extremes

Retailers have been quick to adopt AI, and we have many customers preparing for Black Friday. Almost all of them have a different version of the same question: if their peak call volume were to exceed predictions by 2x or 3x or 5x, could Sierra *and* their internal systems handle the load? The answer should be an unqualified yes! To understand how our systems perform under pressure, our teams recently put our platform through internal load tests at more than 20x typical peak traffic. As the old saying goes, “*time spent in reconnaissance is seldom wasted.*”

Our first step was to pick a partner — one with high seasonality and tens of millions of annual phone calls — and define success from their perspective. How many conversations would need to run concurrently? For how long? And with what latency requirements? These are traditional system metrics, but agents built on Sierra don’t just route calls like an IVR — they handle entire conversations. So while measuring throughput and uptime were critical, we also needed to assess the quality of those conversations. Could the agent listen, reason, and respond effectively — with the right tone, cadence, and replies — even at massive scale?

## The "flight" simulator

With these criteria defined, our team built an internal load-testing tool capable of generating millions of simulated calls, each modeled on real-world customer scenarios. The simulated traffic was introduced into our production environment alongside normal traffic — starting small and scaling gradually to our “peak, peak, peak” scenario, and then far beyond — all without impacting live customer conversations.

Throughout the process, we monitored every layer of the system: from Sierra’s core platform services to the external infrastructure and APIs they depend on. To make the process repeatable for future tests, we developed a dedicated dashboard that displayed, in real time, how each part of the system performed. Unlike our production dashboards, this one focused on a single partner, allowing us to isolate behavior within the load test without affecting their live traffic.

We also built a scalability playbook — a detailed guide outlining the manual steps and triggers to ensure agents scale smoothly during sudden spikes in demand.

## Finding and fixing bottlenecks

Even in systems designed to scale seamlessly by adding capacity, stress testing inevitably surfaces hidden limits. Some were predictable — rate limits, resource quotas, configuration ceilings — while others were inefficiencies that emerged only when many thousands of conversations happened simultaneously.

Each round of testing generated concrete improvements: architectural tweaks, caching improvements, and better handling of concurrent conversations. We’d then test again, with higher volumes each time. Within a week, Sierra was confidently handling 20x our platform’s typical peak traffic with stable latency, consistent quality, and no degradation in agent performance.

When the final customer test arrived, it was uneventful — in the best possible way. Our customer ran their scripts, driving the higher-than-expected load through our systems, and the agent performed as designed: resolving customer issues, maintaining the quality of conversations, and scaling without intervention.

## Continuous readiness

Load testing at Sierra isn’t a one-off exercise; it’s part of a continuous capacity and resilience program. Our systems evolve quickly as new companies launch agents and voice volumes grow. Each new test informs how we scale, how we provision redundancy, and how we prepare for the next surge — whether that’s a global retail event like Black Friday or something no one saw coming.

For large enterprises, these tests are more than technical validation; they’re a demonstration that Sierra can support large, established enterprises with significant customer bases under real-world conditions. And for our engineers, they’re an opportunity to push the boundaries of distributed systems — to build infrastructure that scales effortlessly, while maintaining the quality of every customer interaction.

Because at the end of the day, the best load test is the one that feels like nothing happened at all.
