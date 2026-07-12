---
title: AI Model Performance Metrics Explained
topic: evals-observability
subtopic: monitoring
secondary_topics:
- inference/serving
summary: Explains model performance metrics used in production inference, including
  latency, throughput, and quality signals.
source: baseten
url: https://www.baseten.co/blog/ai-model-performance-metrics-explained/
author: Kenzie Amack
published: '2026-02-09'
fetched: '2026-07-11T04:06:17Z'
classifier: codex
taxonomy_rev: 1
words: 1655
content_sha256: 4eae818e58fbebeb4af84ba24260dc5b8f4d93154f62f7fbfee9c2f65ef3314c
triage: keep
skip_reason: null
---

# AI Model Performance Metrics Explained

![performance-metrics](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1773096546-performance-metrics_blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Users no longer tolerate slow AI. Optimizing performance isn’t as simple as chasing big benchmark numbers. This blog dives into the three key inference metrics that shape perceived performance and shows how different workloads demand different tradeoffs. The “fastest” model depends entirely on how your users interact with your product.

In AI, yesterday’s breakthrough is today’s baseline. When ChatGPT launched in 2022, users were blown away when they received any reasonable response. Just a few years later, and the shiny newness has worn off, along with their originally low expectations. End users can now be found complaining about LLMs being “[ frustratingly slow](https://community.openai.com/t/gpt-is-becoming-frustratingly-slow-more-and-more/1150950)”. At Baseten, we’ve seen developers focus shift to match these new user expectations. A year ago, very few developers were optimizing for performance, it was all about

*quality*. Now as quality becomes more widely available with recent model releases, the focus has shifted to performance. Developers now come to us because shaving even milliseconds off inference latency can be a step function change in the user experience. As the adoption of AI has increased, end user expectations for performance have quickly risen, demanding the application layer (and their developers) to keep up.

But improving performance can mean many different things. It’s vital that developers understand what AI model performance metrics matter, and how they can make thoughtful decisions when optimizing performance with their end users in mind.

## The basics of performance

So, what is “performance” during inference? There are three key AI model performance metrics that heavily influence the end user experience. 1) Time to first token, 2) Tokens per second, 3) End-to-end latency. Here’s what they mean:

- Time to first token (TTFT): the length of time between when a prompt is submitted and the first response token appears. Lower TTFT is better.
- Tokens per second (TPS): how many output tokens are produced per second. Higher TPS is better.
- End-to-end latency: the total time from when the prompt is sent to when the final output token is produced. Lower E2E latency is better.

Every user interaction is influenced by these model performance metrics. TTFT influences the user's first impression of a model’s response time since it’s the time a user waits to see the first output token. A low wait time means the user before they know something is working via a partial response quickly and the application is responsive. TPS on the other hand, influences the length of time a user waits to see the subsequent output tokens. A high TPS also means the application can handle many concurrent users, making it robust to requests at scale — an important consideration for LLM inference performance in production environments.

These metrics will vary by both API provider and model. API providers have different performance optimizations to make models more performant such as batching, quantization, KV cache aware routing, etc. Performance can vary by model as well. Smaller models are on average more performant because they require less memory bandwidth and compute, allowing higher throughput and lower inference latency on the same hardware. While smaller models are generally more performant and efficient, many developers shy away from them due to the loss of quality that can come with having fewer parameters. However, with techniques like SFT / RL we can push these models to be on par with larger models on quality while retaining their performance benefits. Models also have “personalities” that influence both the output style and the number of tokens they generate for a given prompt. It’s key to understand that latency, TPS, and end-to-end latency *will not *translate across models. Some models are more “talkative” and create more output tokens on average. It’s key to re-evaluate performance baselines during model shifts.

## Evaluating API providers

When evaluating providers and you’ll want to check for:

- Does this API provider have consistently good performance across other models I may be interested in? (in case model swapping is needed in the future)
- Is performance stable and consistent? Does this provider have good performance all the time, or does it vary in ways that affect my workload?
- Is the provider reliable with high uptimes?
- Does this provider enable me to scale (higher rate limits or more GPUs) to support my short term traffic?

Developers often struggle to find consistent sources of truth for what “good” performance should look like by model and by API providers. [ Openrouter](https://openrouter.ai/z-ai/glm-4.7/providers) and

[can be great places to start LLM performance benchmarks. While these benchmarks work great as developing a baseline, developers should always be wary of “vanilla” benchmarks. Real performance is often achieved by tuning settings to a specific workload. These public benchmarks are a one size fits all approach and likely do not represent the actual performance for each unique workload.](https://artificialanalysis.ai/models/glm-4-7-non-reasoning/providers)

__Artificial Analysis__While benchmarks are a great way to start, API providers should be able to “tune” models to fit your needs within dedicated deployments at scale. This can create meaningful performance gains above and beyond optimized off-the-shelf multi-tenant APIs.

## So, what actually matters

After every new model drop, the Twitter sphere lights up with new performance numbers for API providers vying to be “the fastest” (for every inference provider, the answer is always - us!). In 2025, the broader AI market was nearly fanatical about TPS (see one Twitter frenzy [ here](https://x.com/eersnington/status/1952802432989147377?s=20)). 

It’s easy to get worked up about big performance numbers; however, it's key to double click into what these AI model performance metrics *actually mean *for the end user experience. Let’s take the tweet about TPS from the gpt-oss release (see exhibit below). If you were optimizing for TPS only you would likely pick Provider 3 at ~3,800 TPS. However, if you look at that same providers TTFT they don’t start producing tokens for over 3 seconds! Provider 2 on the other hand which has a TTFT of (0.48) seconds would have already produced 2.3k output tokens before provider 3 generates a single output token. 

![This is an illustrative snip of Openrouter taken from a tweet during the gpt-oss release in August 2025 and does not represent live performance.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1768600052-image-1-16-26-at-1-47-pm.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) This is an illustrative snip of Openrouter taken from a tweet during the gpt-oss release in August 2025 and does not represent live performance.

This is an illustrative snip of Openrouter taken from a tweet during the gpt-oss release in August 2025 and does not represent live performance.We’ve already hinted at it above, but the real metric that matters is *end-to-end latency. *This takes into account the actual request and how it’s served across different providers. In this instance a very long request with a high number of output tokens will have lower end-to-end latency on provider 3 while a request that calls for a shorter output will likely be faster on provider 2 given the significant delta between their TTFT and TPS. A general rule of thumb, for very short requests with just a few thousand output tokens (think a chat or voice response), TTFT matters more. For very long requests near hundreds of thousands (think code generation or document processing), TPS can matter more. Of course, it’s always key to watch end-to-end latency for a given model.

## Navigating tradeoffs

Lastly, it’s key to understand the tradeoffs made when optimizing for performance. We often describe the key inference metrics of cost, performance, and quality as the apices on a triangle. Move any variable and you inevitably change the angle of the other two. When optimizing for performance it is important to be cognizant of the implications for cost and quality. Faster inference is often more expensive. Faster inference can at times be achieved through a loss of quality. Neither of these are poor decisions, but they should be made by taking into account your unique workload.

![Inference is a constant tradeoff between performance, quality, cost.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1768599839-image-1-16-26-at-1-43-pm.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Inference is a constant tradeoff between performance, quality, cost.

Inference is a constant tradeoff between performance, quality, cost.Interestingly, humans can only read 200-300 words per minute, that’s only ~4-7 tokens per second. If you expect your users to read every word, paying a premium for ~4k TPS might not be worth it! In this case, the users perceived performance would be driven by their ability to begin reading the output which is impacted most by time to first token (TTFT). On the other hand in code gen, anything TTFT below 200-300ms feels instantaneous, so this rule may not apply if you are generating large chunks of output that engineers will skim.

Of course, every AI model performance metric matters more or less in specific use cases. Here are some of the high level trends we’ve seen:

- Use cases where TTFT matters more: search, autocomplete type features
- Use cases where TPS matters more: agentic workflows (outputs not consumed by end users)
- Use cases where E2E latency matters more: voice, translation

Listening to user feedback and understanding how they use the product will help you prioritize the right set of model performance metrics to create the best experience. Over time, a great practice is to develop internal benchmarks for your task and use these benchmarks to evaluate new models for performance and quality gains as they emerge.

## Conclusion

To keep up with user expectations, developers are beginning to look at how they can improve perceived performance for their end users. It’s key that developers fully understand how end users interact with their product and prioritize the AI model performance metrics that create meaningful improvements in the user experience. Not all metrics are created equal for every use case, so it’s important to navigate the tradeoffs and consider the broader implications performance can have on model cost and quality.

Here at Baseten, performance (along with inference) is our obsession. If you’re interested in understanding how we build for performance check out our [ research hub](https://www.baseten.co/resources/research/) or experience it for yourself with our latest API,

[.](https://www.baseten.co/library/glm-4-7/)

__GLM 4.7__
