---
title: DeepSeek V3 just got vision capabilities!
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/deepseekv3-document-inlining
author: null
published: '2024-12-18'
fetched: '2026-08-12T06:30:59Z'
classifier: null
taxonomy_rev: 2
words: 438
content_sha256: a90936d3e5ebc3a619ad147e3249d2034d3d6c1299908ff101c55eb49fd03880
---

# DeepSeek V3 just got vision capabilities!

2024 has been the year of large multimodal models. From Stable LM 2 to DeepSeek v3, the growth in the model capabilities along with benchmark metrics has been unprecedented. Not only did we see exceptionally good task-specific models, critical reasoning also became a core component of model capabilities.

The last model release of 2024- DeepSeek v3, caught a ton of eyeballs because of how it blew up on the benchmark leaderboard. Not only did DeepSeek v3 beat GPT4-o in all the benchmarks, but it did exceptionally well on coding tasks. It has state-of-the-art benchmarks, achieving impressive scores on various tests, including 87.1% on MMLU and 87.5% on BBH.

[Source: DeepSeek V3 HuggingFace Benchmark](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe8y6fAUYpEjSlBWOyUEUqgD3FK9sUEp-cxEx7DfomReE3czQPBbzgo5hNpKZCHNmy4BGiu_2V_d-So76Y1tekKuY8ivJjuUUvapAhiZQsSyxUoHRgcRXp20F4OQach4z0_v2UY?key=e61Z4ANOkw-RtWmvoqINwrPG)

DeepSeek v3 has positioned itself pretty strongly on the quadrant of being open-source, cost-efficient, and high-performance. They have used Multi-Token Prediction (MTP) which enables the model to output multiple tokens at once, increasing speed up to 1.8x tokens per second.

You can now try DeepSeek v3 on Fireworks!

—> Try it out on [Fireworks Model Playground](https://fireworks.ai/models/fireworks/deepseek-v3/playground)

—> Try it as a [Fireworks API](https://fireworks.ai/models/fireworks/deepseek-v3)

DeepSeek v3 model in spite of its mighty reasoning and coding capabilities, it doesn’t have vision capabilities. You can now give DeepSeek V3 or any other LLM on Fireworks Model Library vision capabilities, using Fireworks’ recent feature - Document Inlining!

Step 1: Navigate to [https://fireworks.ai/](https://fireworks.ai/)

Step 2: Next, click on "Model Library"

Step 3: Next, click on “DeepSeek V3”

Step 4: Next, click on “Playground”

Step 5: Type "Can you process images?” Press Enter

Step 6: As you see, out-of-the-box DeepSeek V3 doesn’t have vision capabilities. But now, let’s give DeepSeek v3 Steroids - Fireworks Document Inlining! You can turn it on with a simple click (as shown below)

Step 7: Now, click on Upload Image/PDF and

Step 8: And there you go! DeepSeek v3 can now see, without any fancy integrations!

You can use Document Inlining feature via playground and APIs by simply appending your image URL with `#transform=inline`

Checkout detailed [documentation on Document Inlining here](https://docs.fireworks.ai/firesearch/inline-multimodal)!

[Fireworks](https://fireworks.ai/signup) is an enterprise scale LLM inference engine. Today, several AI-enabled developer experiences built on the Fireworks Inference platform are serving millions of developers.

Fireworks lightning fast serving stack enables enterprises to build mission critical Generative AI Applications that are super low latency. With methods like prompt caching, speculative API, we guarantee high throughput performance with low total cost of offering (TCO) in addition to bringing best of the open-source LLMs on the same day of the launch.

If you have more questions, [join our community](https://discord.gg/J6ayEBXz) and tag a fireworks team member or [drop a note](https://fireworks.ai/company/contact-us) to discuss building with LLMs from prototype to production.
