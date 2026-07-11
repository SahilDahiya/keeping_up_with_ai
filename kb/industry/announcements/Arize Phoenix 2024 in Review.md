---
title: 'Arize Phoenix: 2024 in Review'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/monitoring
summary: Year-in-review post summarizing Arize Phoenix product growth and observability
  features shipped during 2024.
source: arize
url: https://arize.com/blog/arize-phoenix-2024-in-review/
author: John Gilhuly
published: '2024-12-30'
fetched: '2026-07-11T04:51:07Z'
classifier: codex
taxonomy_rev: 1
words: 583
content_sha256: ef8762d1d12af8e87a8071c5814d58abcd4af66a840235c343eaf4bd50d33e38
---

# Arize Phoenix: 2024 in Review

2024 was [Arize Phoenix](http://phoenix.arize.com)‘s biggest year ever.

Granted, it was also Phoenix’s first full year ever, but given how much we crammed into this year we think it still counts 🤗

Over the past year, Phoenix’s [open-source](https://github.com/Arize-ai/phoenix) LLM evaluation and tracing solution has grown from ~20k monthly downloads to over 2.5 million. Our [community](https://join.slack.com/t/arize-ai/shared_invite/zt-2w57bhem8-hq24MB6u7yE_ZF_ilOYSBw) grew to over 6,000 members. We ran dozens of hackathons, meetups, paper reading sessions, workshops, tech talks, and conferences, and got to spend countless hours connecting with the AI developer community.


Throughout all of this, we saw a few notable themes in 2024.

1/ The AI industry moved rapidly and completely toward **agents** in 2024. [New development tools](https://towardsdatascience.com/navigating-the-new-types-of-llm-agents-and-architectures-309382ce9f88) launched seemingly weekly, but despite this rapid progress, key challenges remain unsolved. The question of how to properly [evaluate agents](https://arize.com/blog-course/llm-agent-how-to-set-up/evaluating-ai-agents/) – beyond basic function calling evals and skill tests – stayed an open debate in the field. Expect a lot more from us here in 2025!


2/ **OpenTelemetry** solidifies its position as the preferred standard to build on top of when it comes to LLM observability. By now, the majority of observability tools have shifted or are building support for OTEL.

We luckily made this bet back in Jan 2024, and designed Arize Phoenix to run entirely on OpenTelemetry. This change was a huge unlock for our team, allowing us to iterate more quickly, and take lessons from pre-LLM observability platforms. But this was not an easy shift. We had to figure out everything from dealing with latent data, to properly instrumenting streaming, to handling something as basic as lists. If you’re curious about those, check out our [lessons learned post](https://arize.com/blog/zero-to-a-million-instrumenting-llms-with-otel/).


3/ The industry’s **adoption of LLM evaluations** matured significantly. “LLM as a Judge” is now a recognizable concept for many AI builders. OpenAI launched their own evals product. And how to structure your evals is now a popular discussion topic on X and BlueSky.

We launched a ton of features throughout the year to help AI engineers looking to run their evals. [Datasets & Experiments](https://docs.arize.com/phoenix/datasets-and-experiments/overview-datasets) made Evaluation Driven Development possible, giving users the ability to test iterations of their applications on a consistent set of test cases. [Prompt Playground](https://docs.arize.com/phoenix/prompt-engineering/quickstart-prompts) moved the debugging process into the dashboard, letting devs replay time and test tweaks to their prompts (our team is especially proud of this one, [check it out](https://www.youtube.com/watch?v=wLK5RwHNLUM) if you haven’t!)


Looking back over this year has also made us realize just what a special opportunity we have in Arize Phoenix.That gives us, the Phoenix team, the support to build the AI engineering platform that we want as developers, and the ability to put it in as many people’s hands as possible, with nothing held back. We can spend cycles testing the newest experimental framework. We don’t have to gate features behind paywalls (if you’re looking for our SaaS counterpart, check out [Arize](https://arize.com/)!).

We have the opportunity to build the best possible AI platform there is, and we can do it with no reservations.

But what makes all of the building worth it is seeing the community, aka YOU, using what we’ve built.

Every social mention, every inclusion of Phoenix in a tutorial, every piece of swag seen in the wild, and every star on Github is fuel for the Phoenix team’s fire.

We’ve got big plans for 2025. Expect more features, more community events, more experiments, and many, many more releases in the year to come.


To the skies,

The Phoenix Team (Mikyo, Xander, Dustin, Roger, Parker, Tony, and John)
