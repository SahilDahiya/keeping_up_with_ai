---
title: 'Langfuse Launch Week #1 - Langfuse'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: langfuse
url: https://langfuse.com/blog/launch-week-1
author: null
published: '2024-04-21'
fetched: '2026-07-17T06:46:56Z'
classifier: null
taxonomy_rev: 2
words: 842
content_sha256: 3b45cb53ae55ea05365c1221491a060205610ace79721d3c5b550414fb47581d
---

# Langfuse Launch Week #1 - Langfuse

# Langfuse Launch Week #1

Unveiling Langfuse 2.0 in a week of releases

![Picture Clemens Rawert](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fclemensrawert.jpg&w=96&q=75)

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75)

![Picture Max Deichmann](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmaxdeichmann.jpg&w=96&q=75)

![Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-1%2Flangfuse-launch-week.png&w=3840&q=75)


[Joins us for Launch Week #1](https://langfuse.com#joins-us-for-launch-week-1)

We’re excited to announce Langfuse's first launch week. We're kicking it off on Monday April 22nd and will release a major upgrade to the Langfuse platform every day until Friday.

- ⭐️ [Star us](https://github.com/langfuse/langfuse/)on GitHub & see*all*of our releases!
- [Twitter](https://x.com/langfuse)will be our main channel for all of Launch Week #1
- Join our [first town hall](https://langfuse.com#townhall)on Wednesday

[Launches](https://langfuse.com#launches)

[Day 0: OpenAI JS SDK Integration](https://langfuse.com#day-0-openai-js-sdk-integration)

```
import OpenAI from "openai";
import { observeOpenAI } from "langfuse";
// wrap the OpenAI SDK
const openai = observeOpenAI(new OpenAI());
// use the OpenAI SDK as you normally would
const res = await openai.chat.completions.create({
  messages: [{ role: "system", content: "Tell me a story." }],
});
```
We [launched](https://langfuse.com/changelog/2024-04-21-openai-integration-JS-SDK) a new wrapper for the OpenAI JS SDK. This integration, designed to enable easier monitoring of OpenAI API usage, features seamless observability with enhancements like automatic tracking of prompts, completions, and API errors, as well as insights into model usage and costs. After a soft launch that gathered user feedback for improvements, the integration is now fully available, complete with comprehensive [documentation](https://langfuse.com/integrations/model-providers/openai-js) and an [example notebook](https://langfuse.com/guides/cookbook/js_integration_openai).

[Day 1: PostHog Integration](https://langfuse.com#day-1-posthog-integration)

We teamed up with [PostHog](https://posthog.com) (OSS product analytics) to integrate LLM-related product metrics into your existing PostHog dashboards. This integration is [now available](https://langfuse.com/changelog/2024-04-22-posthog-integration) in public beta on Langfuse cloud. You can configure it within your Langfuse project settings. When activated, Langfuse sends metrics related to traces, generations, and scores to PostHog. You can then build custom dashboards to visualize the data or use the *LLM Analytics* dashboard template to get started quickly. See [docs](https://langfuse.com/integrations/analytics/posthog) for more information.

[Day 2: LLM Playground](https://langfuse.com#day-2-llm-playground)

We're excited to introduce the [ LLM Playground](https://langfuse.com/docs/playground) to Langfuse. By making prompt engineering possible directly in Langfuse, we take another step in our mission to build a feature-complete AI engineering platform that helps you along the full live cycle of your LLM application. With the LLM playground, you can now test and iterate your prompts directly in Langfuse. Either start from scratch or jump into the playground from an existing prompt in your project. See the 

[docs](https://langfuse.com/docs/playground)for more details and let us know what you think in the

[GitHub discussion](https://github.com/orgs/langfuse/discussions/1170).

[Day 3: Decorator-based integration for Python](https://langfuse.com#day-3-decorator-based-integration-for-python)

We're happy to share that the Decorator-based integration for Python now supports all Langfuse features and is the recommended way to use Langfuse in Python. The decorator makes integrating with Langfuse so much easier. Head over to the [Python Decorator docs](https://langfuse.com/docs/sdk/python/decorators) to learn more. All inputs, outputs, timings are captured automatically, and it works with all other [Langfuse integrations](https://langfuse.com/integrations) (LangChain, LlamaIndex, OpenAI SDK, ...). To celebrate this milestone, we wrote a [blog post](https://langfuse.com/blog/2024-04-python-decorator) on the technical details and created the [example notebook](https://langfuse.com/guides/cookbook/example_decorator_openai_langchain) shown in the video as it demonstrates what's really cool about the decorator. Thanks again to [@lshalon](https://github.com/lshalon) and [@AshisGhosh](https://github.com/AshisGhosh) for your contributions to this!

[Day 4: Datasets v2](https://langfuse.com#day-4-datasets-v2)

We're thrilled to release Datasets v2, featuring significant enhancements to the dataset experience in Langfuse. Improvements include a new editor powered by Codemirror, metadata support on all objects, tables that render inputs/outputs side-by-side, the ability to link dataset runs to traces, and the option to create dataset items directly from traces. We've also extended the public API with new endpoints for programmatic management of datasets. Check out the [changelog](https://langfuse.com/changelog/2024-04-25-datasets-v2) which summarizes all the new features and improvements.

[Day 5: Model-based Evaluations](https://langfuse.com#day-5-model-based-evaluations)

On the final day of Launch Week 1, we're happy to release the biggest change to Langfuse yet: Model-based evaluations run right in Langfuse. So far, it was easy to measure LLM cost and latency in Langfuse. Quality is based on [scores](https://langfuse.com/docs/scores) which can be user feedback, manual labeling results, or be ingested by evaluation pipelines that you built yourself using the Langfuse SDKs/API. Model-based Evaluations in Langfuse make it way easier to continuously evaluate your application on the dimensions you care about. These can be: hallucinations, toxicity, relevance, correctness, conciseness, and so much more. We provide you with some battle-tested templates to get you started, but you can also write your own templates to cover any niche use case that might be exclusive to your application. Check out the [changelog](https://langfuse.com/changelog/2024-04-26-model-based-evaluation) or watch the video to learn more about all the details.

[Launch Week Events](https://langfuse.com#launch-week-events)

[Wednesday: First virtual town hall](https://langfuse.com#townhall)

You're invited to our first virtual town hall. We (Max, Marc and Clemens) will be demoing new features in Langfuse, answering questions and talking about where we're taking the project. We're looking forward to hanging out!

- When: Wednesday, April 24th, noon PT, 9pm CET
- [Recording on YouTube](https://www.youtube.com/watch?v=WGERHcRnBYQ)

[Friday: Langfuse 2.0 on Product Hunt](https://langfuse.com#friday-langfuse-20-on-product-hunt)

We will end the week with the launch of **Langfuse 2.0** on Product Hunt on Friday, April 26th. After our initial launch last year – which led to a [Golden Kitty Award](https://www.producthunt.com/golden-kitty-awards/hall-of-fame?year=2023#ai-infra) – we are very excited to be back on Product Hunt.

[Launch post](https://www.producthunt.com/posts/langfuse-2-0) (*Spoiler: Langfuse became the #1 product of the day 🥇*)
