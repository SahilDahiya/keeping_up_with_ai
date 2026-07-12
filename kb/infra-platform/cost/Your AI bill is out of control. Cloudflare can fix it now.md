---
title: Your AI bill is out of control. Cloudflare can fix it now.
topic: infra-platform
subtopic: cost
secondary_topics:
- evals-observability/monitoring
summary: AI Gateway adds dollar-denominated spend limits plus a closed beta of identity-driven
  budgets and model routing via Cloudflare Access, so enterprises can attribute LLM
  spend per person/team (e.g. $5,000/month frontier models for engineering, $200 for
  interns) instead of one opaque shared API key.
source: cloudflare-ai
url: https://blog.cloudflare.com/ai-gateway-spend-limits/
author: Ming Lu
published: '2026-06-05'
fetched: '2026-07-11T04:13:00Z'
classifier: claude
taxonomy_rev: 1
words: 1455
content_sha256: 12bd083803b44e7fd5dbf047f82272d35346c8e619bd239922cb186faf880cd3
---

# Your AI bill is out of control. Cloudflare can fix it now.

There isn't a CIO on the planet not worried about AI spend right now. CFOs are increasingly nervous, too.

For fear of falling behind, many companies have pushed their employees to use AI as aggressively as possible. The edict was clear: "Move fast, we'll figure out the bill later." And for the most part, it worked: AI has been genuinely transformational for the teams that leaned in.

But the costs are real: we’ve heard countless horror stories of huge bills and painful overages on token spend.

**Today, we're announcing spend controls in Cloudflare AI Gateway, and a closed beta for identity-driven budgets and routing using Cloudflare Access and your existing identity provider.**

As we’ve spoken with hundreds of companies about their AI strategy, we’ve seen a common story: The company gives every engineer access to frontier models through a shared API key. Usage takes off. At the end of the month, finance pulls the invoice and nobody can explain where the money went. Was it the machine learning team training a new pipeline? Was it an intern running Claude Opus on email triage? Was it a runaway continuous integration job that burned through 50 million tokens in a weekend? Nobody knows, because the API key doesn't tell you who used it.

Without guidelines, staff will generally reach for the biggest model available. And why wouldn't they? If there's no budget, no visibility, and no routing logic, the rational move is to use the most powerful model for everything. The problem is that most tasks don't need a frontier model. A code review summary doesn't need the same model as a complex architecture refactor. A log parser doesn't need the same model as a customer-facing content generator. It should be easy to select the *right* tool for the job, rather than defaulting to the most powerful and expensive one. And it should be simple to see where the spend is going.

You can't calculate ROI on your AI spend without visibility on what you're spending, and you can't protect that ROI without controls. Every other line item in a business has a budget and per-team attribution and AI spend should be no different.

[ AI Gateway](https://developers.cloudflare.com/ai-gateway/) sits between your applications and AI providers. Instead of calling OpenAI, Anthropic, Google, or any other provider directly, your requests route through AI Gateway first.

This immediately gives you several useful tools:

- Unified billing to easily switch between different providers and models
- Logging across all providers — every request, token count, and cost in one place
- Response caching
- Rate limiting
- __Content guardrails__- __block Personally Identifiable Information (PII) and secrets__

However, AI Gateway didn’t have an easy way to answer who is spending what or how you might set limits on AI spend.

You could see aggregate usage across your account. But you couldn't see that Jane from engineering burned through \$2,000 on Claude this month while the entire data science team only used \$400. You couldn't set a budget that said "engineering gets \$5,000/month on frontier models, interns get \$200/month on Kimi K2.6."

That changes today.

AI Gateway now supports [ spend limits](https://developers.cloudflare.com/ai-gateway/features/spend-limits) as a core feature. These are true cost control measures in the form of budgets set in dollars, not tokens, that track cumulative spend across all requests, operating independently of traditional rate limiting.

You can scope limits to any combination of dimensions: model, provider, or admin-defined custom attributes like user, team, or application. Windows can be fixed (resets on the first of the month, Monday, or midnight) or rolling, and set to daily, weekly, or monthly.

AI Gateway calculates cost per request based on the model's pricing, and tracks cumulative spend against your limit in real time. You can easily track your model spend on our analytics dashboard and filter by model, provider, or any custom attribute.

You have options for what happens when the budget limit is reached. AI Gateway will block further requests by default. Or you can set up rules through [ Dynamic Routes](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) to route requests to a fallback model after you’ve hit a spend limit, so that a hard spending cap won’t kill your engineers’ workflow. We’re working to add the capability for you to also send alerts when a limit is reached.

Spend limits are available in open beta today for all AI Gateway users across all plans. Configure them in your gateway settings in the dashboard or via the API.

We're tracking token costs inside Cloudflare already. Every Cloudflare employee uses AI tools daily, routing millions of requests and billions of tokens per month through AI Gateway. We faced the same question every company faces at this scale: who's using what, and how do we budget for it?

We solved this by enabling AI Gateway to add identity to every request. When an employee authenticates via Cloudflare Access, we extract their identity from the JSON Web Token (JWT) and attach it as metadata on the AI Gateway request. This makes per-user token consumption, team-level usage breakdowns, and cost attribution across the organization all visible in one place.

In addition to spend limits, today we’re also announcing identity-driven budgets and policies as a closed beta.

Spend limits in AI Gateway let you set budgets by model, provider, or custom attributes. But your application has to pass that metadata, and AI Gateway trusts whatever it receives. For verified, automatic attribution, you need identity.

When combined with [ Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/), AI Gateway can see who is making each request — not just which account, but which employee, which identity provider (IdP) group, which service, etc.

Here's what that looks like in practice.

You can set per-user budgets, say \$500/month for individual contributors and \$2,000 for senior engineers. When a user hits their limit, requests can be downgraded to a cheaper model or blocked.

You can set per-team model policies. For instance, your ML team gets Claude Opus and GPT-4o. The brand design team can access generative image and video models. Interns use open-source models on Workers AI. These policies map directly to your existing IdP groups, the same identity provider groups you already manage.

For [ CI/CD](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/) pipelines and autonomous agents,

[allow you to give each agent a named identity. You can see that your code review bot used 5 million tokens this week while your documentation generator used 500,000. If one agent is running out of control, apply a budget policy without affecting any others.](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)

__Access service tokens__Every AI Gateway log entry will include the authenticated identity: email, IdP group, service token name. Export these to your analytics platform, and you've got a cost-by-user-by-team breakdown without building anything custom.

Under the hood, you create a Cloudflare Access application for your AI Gateway endpoint and configure policies based on your IdP groups. When a developer or agent makes a request, they authenticate via OAuth, using the typical CLI device-code flow. AI Gateway validates the token and extracts the identity. You don't need to write a custom Worker, parse JWTs yourself, or rely on honor-system metadata headers.

We recently wrote about [ how we built our internal AI engineering stack](https://blog.cloudflare.com/internal-ai-engineering-stack/). This is what we are making available today — so you can use it, too, and you don't have to build it yourself.

If you would like access to the closed beta, [ sign up here](http://www.cloudflare.com/lp/ai-gateway-identity-aware-endpoints-beta/).

Setting a budget is necessary. But once you’ve got a budget, how do you make the most of it?

The reality is that not every request needs a frontier model: a summarization task can run on a smaller, cheaper model without meaningful quality loss, while a large-scale code refactor might require the bleeding edge. But without controls, people will almost always opt for the most advanced model.

A solution for that is coming next: We're building intelligent, task-based routing in AI Gateway. For each request, we can analyze and automatically route it to the model that will give you the best result at the lowest cost. This is in active development, so follow our [ developer docs](https://developers.cloudflare.com/ai-gateway/) and

[.](https://developers.cloudflare.com/ai-gateway/changelog/)

__changelog__It’s free to get started with AI Gateway. Spend limits are available now for all users.

If you haven't already, [ create a gateway](https://developers.cloudflare.com/ai-gateway/get-started/) and point your applications at it. From there, set up spend limits in the dashboard or via API. Start with a high limit in monitoring mode to understand your current usage patterns before you start enforcing.

If you want per-user attribution and team-based policies, [ sign up](http://www.cloudflare.com/lp/ai-gateway-identity-aware-endpoints-beta/) for the identity-driven budgets closed beta, and we'll get you set up with the Access integration.

We want to hear how you're managing AI costs today. Join the conversation on [ Cloudflare Community](https://community.cloudflare.com/) or

[to discuss your broader AI security strategy.](https://www.cloudflare.com/ai-security/)

__reach out__
