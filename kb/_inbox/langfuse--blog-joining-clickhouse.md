---
title: Langfuse joins ClickHouse - Langfuse
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: langfuse
url: https://langfuse.com/blog/joining-clickhouse
author: null
published: '2025-12-09'
fetched: '2026-07-18T06:38:30Z'
classifier: null
taxonomy_rev: 2
words: 1219
content_sha256: f17918fcd88227a376a77f2a6625fc7aa398e84dc3a9d10a82005440450391e7
---

# Langfuse joins ClickHouse - Langfuse

# Langfuse joins ClickHouse

Our goal continues to be building the best AI engineering platform

![Picture Max Deichmann](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmaxdeichmann.jpg&w=96&q=75)

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75)

![Picture Clemens Rawert](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fclemensrawert.jpg&w=96&q=75)

![ClickHouse acquires Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Facquisition%2Fbanner.jpg&w=3840&q=75)


ClickHouse has acquired Langfuse.

If you're reading this as a Langfuse user, your first question is probably: What does this mean for me?

Our roadmap stays the same, our goal continues to be building the best AI engineering platform, and we remain committed to open source and self-hosting. There are no immediate changes to how you use Langfuse and how you can reach out to us.

What *does* change is our ability to move faster. With ClickHouse behind us, we can invest more deeply into performance, reliability, and our roadmap that helps teams build and improve AI applications in production.

[What stays the same](https://langfuse.com#what-stays-the-same)

This is the section we would want to read first, too.

- **Langfuse stays open source and self‑hostable.**There are no planned changes to licensing. As you know, we leaned heavily into OSS over the last years.
- **Langfuse Cloud keeps running as‑is.**Same product, same endpoints, same experience.
- **Support stays the same.**Same channels, same SLAs for existing customers.

[What gets better now](https://langfuse.com#what-gets-better-now)

Joining Clickhouse compresses years of operational learning into immediate, real customer benefits.

- **More engineering leverage on the hardest parts**. Langfuse is a data‑intensive product. Working closely with the ClickHouse engineering team helps us push performance and reliability.
- **Faster progress on enhanced enterprise-grade compliance and security**, with the help of Clickhouse's resources.
- **Learning from Clickhouse's customer success and support playbook**. This puts us years ahead and allows us to spend more time on what we really care about: our users.

[A quick look back](https://langfuse.com#a-quick-look-back)

The longer version of how we got here is in our
[handbook](https://langfuse.com/handbook/chapters/story).

Langfuse started the same way many LLM products start: we were building agents ourselves. And we constantly ran into the same problems.

Building LLM apps is easy to demo and hard to run in production. Debugging is different, quality is non‑deterministic, and the iteration loop is messy. When we did Y Combinator in early 2023, we saw this every week, both in our own projects and in what other founders in our cohort were working on.

So we built a duct tape version of what we wished existed: tracing and evaluation primitives that are **easy to add, easy to self‑host, and actually useful for iterating**.

The very first version was intentionally simple. It ran on **Postgres**, because speed of shipping mattered more than theoretical scaling. That got us to a real product and a real community fast.

Then people actually started to use the product more than we could have imagined.

![Consumption](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Facquisition%2FConsumption.png&w=3840&q=75)


As adoption grew, Postgres became the bottleneck for the workloads Langfuse needed to support (high‑throughput ingestion + fast analytical reads). With **Langfuse v3**, we switched the core data layer to **ClickHouse** to make Langfuse scale for production workloads, both in Cloud and self‑hosted deployments.

![Langfuse v3
architecture](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-langfuse-v3-infrastructure-evolution%2Fog.png&w=3840&q=75)


*And if you like infrastructure deep dives, here’s the  v3 migration write‑up.*

[Why join ClickHouse](https://langfuse.com#why-join-clickhouse)

There are a lot of ways this could have gone. We didn’t plan to sell the company. Actually, we had Term Sheets for a great Series A and were looking forward to some days off over Christmas after an intense year.

What changed wasn’t our conviction in Langfuse, it was realizing how much faster we can go together with ClickHouse, while staying true to what makes Langfuse work: open source, self-hosting, and a product that’s built for real production workloads.

[A shared history (before the acquisition)](https://langfuse.com#a-shared-history-before-the-acquisition)

This dialogue didn’t start with a term sheet. Because Langfuse runs on ClickHouse, we naturally ended up collaborating early and often.

- We’ve always been closely in touch with many teams at ClickHouse: sharing feedback with the database team, and using new features to make Langfuse more reliable. For example, compute-compute separation helps us to reduce the risk of noisy-neighbours on Langfuse Cloud.
- Langfuse Cloud is a large customer of ClickHouse Cloud.
- Teams at ClickHouse use Langfuse to improve their agentic applications.
- We invested heavily in ClickHouse-backed self-hosting: documentation, templates, and deployment patterns, and collaborated closely with ClickHouse on improving that experience.
- As a result, Langfuse introduced thousands of teams to ClickHouse when upgrading from Langfuse v2 to v3.
- We’ve done community meetups together: a ClickHouse meetup at our Berlin office, another one in San Francisco, and an OpenHouse talk in Amsterdam.

Langfuse runs on ClickHouse, ClickHouse uses Langfuse to optimize its agentic products, we share lots of customers and OSS deployments; **that gives ClickHouse every incentive to keep Langfuse fast, reliable, and boringly dependable at scale.**

So in many ways, we operated like long-term partners. This acquisition is a way to make that partnership permanent — and invest aggressively together.

*Max shared on how we use ClickHouse to keep product performance ahead of demand at ClickHouse Open House ( recording) in Amsterdam.*

![Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Facquisition%2Fopenhouse.jpg&w=3840&q=75)

[Culture and engineering fit](https://langfuse.com#culture-and-engineering-fit)

The first time we met Aaron, Yury, Alexey, Tanya, Ryadh, and Pete in-person ended up in a long lunch in Amsterdam. It became obvious we share a similar view on building great developer tooling, how that drives everything within our companies, and how fast analytics is increasingly foundational for building and optimizing agentic products.

We already knew that ClickHouse is one of the best infrastructure engineering teams in the world. More importantly, the engineering culture feels like an instant match:

- open-source identity and stewardship
- developer-first product instincts
- performance and reliability as product features (not afterthoughts)

The whole Langfuse team will join ClickHouse to continue building Langfuse. All of these aspects were important to us and we couldn’t be more excited.

[What we’re focused on next](https://langfuse.com#what-were-focused-on-next)

Our north star doesn’t change: **help teams ship useful, reliable agents by closing the loop from production data to better prompts, evaluations, and product decisions.**

Concretely, we’re investing in:

- **Production monitoring and analytics**for real agent systems (not just offline evals).
- **Workflows across tracing, labeling, and experiments**so iteration loops get shorter.
- **More performance and scale**—especially for large self‑hosted and enterprise deployments.
- **More polish**(UI/UX, developer experience, and docs) so the product stays simple even as the space gets more complex.

You can always follow along on the public
[roadmap](https://langfuse.com/docs/roadmap).

[Thank you](https://langfuse.com#thank-you)

Langfuse exists because the community pushed it forward, through GitHub issues, PRs, feedback, and lots of Slack messages and spontaneous calls to dig into a product feature together.

We’re grateful for the trust you’ve put in us. Joining ClickHouse is our way of honoring that trust by putting more resources behind the thing we care about most: building a product you can rely on.

We’re excited for what’s next!

Max, Clemens, and Marc

[FAQ](https://langfuse.com#faq)

**Is Langfuse still open source?**

Yes. No licensing changes planned.

**Can I still self‑host Langfuse?**

Yes. Self‑hosting is a first‑class path.

**Does anything change for Langfuse Cloud customers today?**

No. Same product, same endpoints, same contracts.

**Where do I go for support?**

No changes: [https://langfuse.com/support](https://langfuse.com/support)

**Will the Langfuse team stay on Langfuse?**

Yes. The team is joining ClickHouse and will keep building Langfuse. Also, we continue [hiring](https://langfuse.com/careers) in Berlin and SF.

[Join the discussion](https://langfuse.com#join-the-discussion)

If you have any other questions, let’s discuss together on [GitHub Discussions](https://github.com/orgs/langfuse/discussions/11593).

If you’re an enterprise customer and have additional questions, feel free to [contact sales](https://langfuse.com/talk-to-us).
