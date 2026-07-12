---
title: How Zapier builds production-ready AI products
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/monitoring
summary: Case study of Zapier building production-ready AI products with observability,
  evals, and feedback loops across real customer workflows.
source: braintrust
url: https://www.braintrust.dev/blog/zapier-ai
author: null
published: '2026-01-01'
fetched: '2026-07-11T04:34:26Z'
classifier: codex
taxonomy_rev: 1
words: 1144
content_sha256: 30a736964c62c0d69abdfd573aa102d6ae742e89f636c5df1a5976b376788e17
---

# How Zapier builds production-ready AI products

With [Mike Knoop](https://x.com/mikeknoop), Co-Founder

50% → 90%+

Accuracy improvement

2-3 months

Time to production quality

![AI Actions](https://www.braintrust.dev/customers/stories/zapier/ai-actions.jpg)


[Zapier](https://zapier.com/) is the world’s leading workflow automation platform, directly connecting to over 6,000 apps and supporting developers and non-developers at over 2 million companies.

Zapier was also one of the first companies to embrace GenAI:

- Shipped AI by Zapier with support for 4,000+ app integrations in early 2022
- [Mike](https://twitter.com/mikeknoop)and- [Bryan](https://twitter.com/bryanhelmig)gave up their exec team roles to be ICs and- [go all-in on AI summer 2022](https://www.youtube.com/watch?v=Mbf_lK-sj2Y)
- [Launched OpenAI on Zapier](https://twitter.com/zapier/status/1601217614641889280)in December of 2022, less than 2 weeks after ChatGPT was released
- One of 11 launch partners for [ChatGPT plugins](https://openai.com/index/chatgpt-plugins)
- Rolled out a [suite of AI features](https://twitter.com/mikeknoop/status/1658497363529596928)in May 2023, including text-to-zap and semantic search
- Shipped [custom AI chatbots](https://twitter.com/mikeknoop/status/1669125943879954433)in June 2023

Since then, the Zapier team has continued to ship amazing features like [Zapier Central](https://twitter.com/mikeknoop/status/1765408616121852137) (AI bots), [AI Actions](https://actions.zapier.com/), and many more internal and external use cases.

At Braintrust, we’ve had the opportunity to support Zapier since August of 2023. In that time, we've learned a lot by watching their AI development process evolve.

In this post, we’re excited to share some of [Mike](https://twitter.com/mikeknoop)’s insights on how Zapier goes from an initial idea to a production-ready AI product:

Prototype & build V0

Ship V1

Collect user feedback

Establish a set of evals

Iterate and improve product

Optimize

Step 1 is all about quickly validating whether your AI feature idea is feasible with existing models. To do this effectively, you should very quickly cycle through different prompts and examples to get a sense for what works and what doesn’t. In this initial phase, Zapier only uses the smartest (and therefore the most expensive/slow) models - GPT-4 Turbo and Claude Opus.

Braintrust’s playground is a great place to do this. Here's an example testing out newly released GPT-4o:

After validating your idea, you should build and ship v1. **Sub 50% accuracy is okay!** In this stage of the development process, “vibes” (i.e. having your team sanity check outputs one by one) is sufficient to make progress.

The goal of this step is to rapidly improve and then get your feature into the hands of users as quickly as possible. Having real users try your product is the best way to understand usage patterns and collect a diverse set of inputs, both of which are foundational to making future improvements.

We find that many teams get stuck here. To mitigate the risks of shipping, you can:

- Label the feature as “beta”
- Ship to internal users
- Ship to a very small subsegment of external users
- Make the feature opt-in
- Keep humans in the loop (e.g. suggestions)

After shipping v1, you should obsessively collect every piece of feedback you can. This includes both explicit feedback (e.g. thumbs up/down or stars) and implicit feedback (e.g. errors, whether the user accepted a change or asked a follow-up). Zapier generally weights explicit feedback more.

You will now have a growing collection of examples with user feedback. Let negative feedback guide you towards areas to improve, and tinker with your prompts/code to attempt to fix those issues.

However, as you go to commit your new update, you will likely realize that while you may have fixed one set of issues, it’s hard to know how your update will impact performance overall. From here, you have 3 options:

- Ship the change, hope for the best, and see what customers think
- Do a manual vibe-checking exercise every time you want to make an update
- Establish a set of evals

A well-defined set of evaluations accurately scores your application on a broad set of examples, similar to a natural-language test suite. Evals are particularly effective when your test set is both diverse and reflects real customer usage patterns.

To bootstrap a great test set, Zapier leverages customer examples from step 3. Both positive and negative feedback are helpful:

- Positive customer feedback: use the inputs/outputs as examples of what good looks like
- Negative customer feedback: correct the outputs and then include them as test cases. This is worth the effort as these examples represent areas where your product struggles

Over time, you can start to construct golden datasets out of these examples to benchmark performance and prevent regressions.

Braintrust is purpose-built for this workflow. The Zapier team uses Braintrust to log user interactions, dig into their logs, track customer feedback, filter on that customer feedback, and directly add interesting logs to their test sets. Braintrust’s datasets feature also abstracts away the pain of managing and versioning test sets.

![Logs view](https://www.braintrust.dev/customers/stories/zapier/mike-logs-view.png)


After you construct a test set and run an evaluation, Braintrust also helps you understand high-level performance, dig into specific examples where your model performs poorly/well, and filter by which examples got better or worse. This gives you and your team the signal to confidently decide whether or not to ship an update into production!

Now that you've established a feedback loop, you should continue iterating to improve product quality. The ability to immediately test whether an update moved you in the right direction gives you the freedom and confidence to absorb customer feedback, make a change, test it, and ship your change. This enables you to rapidly improve performance.

Prototype with flagship model (GPT4, Opus)Prompt playground

Ship to limited group

Collect user feedbackLogs and datasets

Run evalsEvals

Optimize cost and latency

in Braintrust

iterate

**With this feedback loop in place, Zapier has improved many of their AI products from sub-50% accuracy to 90%+ within 2-3 months.**

As accuracy increases, you can start expanding your product’s availability (e.g. shipping to more users) and capabilities (e.g. allowing it to take more actions independently).

You’ve shipped an amazing AI product if:

- Quality is sufficiently high
- The product is available to a good portion (or all) of your user base
- Product usage is high

Congrats!

At this point, the Zapier team will begin thinking through how to optimize cost and latency. By the time you reach this step, you should have a robust set of evals to test your AI product on, making it straightforward to benchmark how swapping in cheaper/smaller models impacts your product’s accuracy.

*Note: this step can come earlier if your product is prohibitively expensive to ship with frontier models or requires super low latency.*

LLMs are incredibly powerful, and we love seeing companies release great AI features. It’s been a lot of fun working with Mike and the Zapier team as they continue to push the limits of leveraging LLMs to amaze their customers.

We hope this guide will serve as inspiration for AI teams struggling to overcome the initial inertia of shipping AI features. We can’t wait to see what you will ship :).

Learn how Braintrust enables rapid iteration from beta to production-ready—collect feedback, establish evals, iterate, and ship with confidence.
