---
title: A/B testing can't keep up with AI
topic: evals-observability
subtopic: evaluation
secondary_topics:
- product-engineering/architecture
summary: Explains why traditional A/B testing is too slow for AI products and argues
  for eval-driven experimentation loops that compare model, prompt, and product changes
  before rollout.
source: braintrust
url: https://www.braintrust.dev/blog/ab-testing-evals
author: Braintrust Team
published: '2025-09-03'
fetched: '2026-07-11T04:31:04Z'
classifier: codex
taxonomy_rev: 1
words: 739
content_sha256: e543415c27235b569b625fa9baa6983914199bd764632e05f6ccac02947fdc24
---

# A/B testing can't keep up with AI

3 September 2025Mengying Li, Ankur Goyal4 min

Evals are still a new practice for many product teams. Engineers often compare them to unit or integration tests, but those analogies don't capture their full potential.

What's really happening is a broader shift: we're moving from one era of product experimentation to another. In a world where interfaces, content, and features can adapt dynamically to each individual, why keep optimizing for the best *average* experience? The recent acquisitions of [Statsig by OpenAI](https://www.statsig.com/blog/openai-acquisition) and [Eppo by Datadog](https://www.datadoghq.com/blog/datadog-acquires-eppo/) hint at the turning point: A/B testing is no longer sufficient for AI product optimization. The future is evals.

Both evals and A/B testing start from the same place: you've noticed, heard, or hypothesized that the user experience of your product could be better. Whether you're testing a new onboarding flow or refining AI responses, the goal is to collect data. You want users to be more likely to stay because of better features, more relevant responses, or smoother interactions.

The process is remarkably similar too:

- **Start with a hypothesis**: In A/B testing, you might hypothesize that "Users get confused about our getting started page and can't immediately see our value. A more targeted tutorial will improve their experience." With evals, it might be: "Users are rejecting responses because of formatting issues, so the format part of our prompt needs to be fixed."
- **Define success criteria**: In A/B testing, this could be "users will use the product more frequently." For evals: "AI responses will better respect users' formatting preferences and users are more likely to accept the change."
- **Establish metrics**: This might be something like increasing engagement days, or using scorers to evaluate prompt changes.
- **Target specific segments**: Focusing your analysis where it matters most, whether it's specific user cohorts or a distinct type of query.

A/B testing assumes it's expensive to create variants. Let's say you're building a new onboarding flow for your banking app. You have two hypotheses:

- Users will have a better experience if they complete a financial goals assessment first
- Users want to just jump straight into account setup

To test these with an A/B experiment approach, you build each experience out, expose a fraction of your users to each, and compare conversion rates. Each variant requires significant design and engineering work. You really can't explore 20 options at once.

AI eliminates this constraint. When AI can automatically update your onboarding flow (or itself through prompt modifications), the core assumption behind A/B testing dissolves. You can now have 20 variants, or as many variants as you have users, or just one that updates automatically every 30 minutes based on real-user feedback. This points toward AI-generated interfaces that personalize dynamically for each user rather than optimizing for statistical averages.

Instead of testing a handful of options and waiting weeks for results, teams can now test dozens of variations and see what works immediately. The system learns and improves continuously through the eval feedback loop. Where traditional testing required careful planning and complex analysis, evals give teams direct feedback that anyone can understand.

Many existing skills from A/B testing still apply: forming hypotheses, defining success criteria, analyzing different user segments, and understanding what improvements actually matter. What's fundamentally different is the shift from building every feature by hand to defining the rules that let systems build themselves. Teams become architects of automated improvement rather than craftspeople manually tweaking each detail.

We're not yet at the point where most products automatically generate a different experience for every user, since implementing evals well is non-trivial. But that's clearly the direction we're headed.

Understanding evals through the lens of A/B testing provides a familiar bridge to this new world while highlighting the unique advantages: rapid iteration, infinite variants, immediate feedback, and the ability to optimize continuously rather than in discrete experimental cycles.

When you can use evals instead of A/B tests, you should. Think evals first and put as much optimization as possible there. Of course, there are still important cases where traditional A/B testing remains valuable, like model selection with real-world constraints (use evals to optimize each model's performance, then A/B test how latency differences affect real users) or optimizing non-AI product areas where it's still impractical to use LLMs.

At the end of the day, the companies that evolve to think in evals will build products that improve faster than their competitors can run a single A/B test.
