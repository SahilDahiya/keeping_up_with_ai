---
title: Resilient observability by design
topic: evals-observability
subtopic: monitoring
secondary_topics:
- infra-platform/deployment
summary: Describes resilient observability design for AI systems, including reliability
  considerations for storing, querying, and using production traces.
source: braintrust
url: https://www.braintrust.dev/blog/resilient-design
author: Braintrust Team
published: '2025-04-03'
fetched: '2026-07-11T04:33:32Z'
classifier: codex
taxonomy_rev: 1
words: 742
content_sha256: f89e11a0ac6c22dd91cb41caae77995b950b5e067ae4a310e7104329caa02f17
---

# Resilient observability by design

3 April 2025Ornella Altunyan, Sachin Padmanabhan4 min

Great AI observability enhances your LLM infrastructure without compromising stability. That's why Braintrust is designed as a non-blocking, optional layer for your AI workloads. Your application's core logic runs uninterrupted while we quietly log data in the background. This means even if Braintrust experiences downtime or network issues, your product stays up and stable.

Our inline features follow the same principle. They're designed to operate independently, even within your app's critical path, so your system can function reliably without direct dependence on Braintrust services.

Our SDK logger is initialized to `asyncFlush: true` by default, meaning log data is sent in the background without blocking your running code. When you log an AI request or result, our SDK quickly queues that log and immediately returns control to your application. The logs are then transmitted to our backend asynchronously, often in batches to minimize overhead.

Even if Braintrust experiences downtime, your application continues running normally. Your API calls, user requests, or batch jobs proceed as usual, while the logging system handles network issues separately. If Braintrust is unavailable, your app will continue running, and the worst case scenario is that some logged data will not make it. If you set [BRAINTRUST_FAILED_PUBLISH_PAYLOADS_DIR](https://www.braintrust.dev/docs/instrument/advanced-tracing#tune-performance), then you can further ensure those payloads are saved locally, and you can then upload them later.

Serverless functions and edge runtimes have unique constraints since they may terminate immediately after returning a response. We account for this by making sure logging remains non-intrusive even in ephemeral environments. By default, the async logging works on platforms like Vercel and Cloudflare Workers, which provide a mechanism (such as [ waitUntil](https://vercel.com/changelog/waituntil-is-now-available-for-vercel-functions)) to finish background tasks after sending a response. In these environments, you can keep

`asyncFlush: true` and we'll automatically use the platform's background task APIs, so your serverless function doesn't have to wait for logs to send.For other serverless platforms that don't support background completion, you can disable async flushing (`asyncFlush: false`) and flush logs at the end of each function call. This prevents log loss while keeping overhead minimal.

The SDK also provides [tunable parameters](https://www.braintrust.dev/docs/instrument/advanced-tracing#tune-performance) (like queue sizes and drop policies) to prevent log operations from holding up your function. In practice, many teams have found our defaults safe for serverless use. We've engineered Braintrust so that logging "just works" without interfering with execution in both long-running servers and cloud functions.

The Braintrust [AI Proxy](https://www.braintrust.dev/docs/deploy/ai-proxy) provides a standardized interface for executing LLM workloads across multiple providers. It's lightweight, stateless, and runs globally on Cloudflare Workers, so it will only go down if Cloudflare itself experiences an outage.

When accessing via `https://api.braintrust.dev/v1/proxy`, requests are routed through AWS CloudFront. For applications requiring maximum resilience, we recommend implementing a tiered fallback strategy:

- Primary endpoint: `https://api.braintrust.dev/v1/proxy`(via CloudFront)
- Secondary endpoint: `https://braintrustproxy.com/v1/`(direct Cloudflare access)
- Tertiary fallback: Direct provider API calls (for example, OpenAI)

This helps make sure your LLM operations continue even in the unlikely event of infrastructure disruptions at both CloudFront and Cloudflare.

Braintrust [Prompts](https://www.braintrust.dev/docs/evaluate/write-prompts) enable versioning and iteration of your LLM workloads while maintaining production reliability. Our client-side implementation ensures prompts remain available even during service disruptions.

The `loadPrompt` function implements a sophisticated strategy:

- Initial prompts are fetched from Braintrust's servers
- A two-level caching system stores prompts in both memory and on disk
- Subsequent calls retrieve prompts from cache, eliminating network dependencies
- Disk caching persists across application restarts, providing continuity

For mission-critical applications requiring absolute reliability, we offer a complete offline solution through our prompt pulling mechanism. By running `npx braintrust pull`, you can download prompt definitions as standalone code files that can be directly imported into your application. These files contain complete Prompt object definitions that function independently of the Braintrust service, ensuring your application remains operational under any circumstances.

We believe that observability should enhance, never compromise, your application's stability. By operating asynchronously and separating logging from critical execution paths, we can make sure that your system's core functionality remains uninterrupted even if logs fail or connections drop. We strongly recommend that you stress test your application — a quick way to do this is to set `BRAINTRUST_API_URL` to a bogus endpoint (or a local proxy) and confirm your app continues to function normally. This simple test provides confidence that your observability layer operates as designed, enhancing your system without introducing new points of failure.

Effective observability isn't just about collecting data, it's about building reliability and resilience into your applications.
