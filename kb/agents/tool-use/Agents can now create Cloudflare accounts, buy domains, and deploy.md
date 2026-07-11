---
title: Agents can now create Cloudflare accounts, buy domains, and deploy
topic: agents
subtopic: tool-use
secondary_topics:
- infra-platform/deployment
summary: Via a protocol co-designed with Stripe for Stripe Projects, coding agents
  can now provision a Cloudflare account, start a paid subscription, register a domain,
  and receive an API token to deploy — end-to-end with humans only approving payment
  and terms of service.
source: cloudflare-ai
url: https://blog.cloudflare.com/agents-stripe-projects/
author: Sid Chatterjee
published: '2026-04-30'
fetched: '2026-07-11T04:13:10Z'
classifier: claude
taxonomy_rev: 1
words: 1494
content_sha256: 5226b367fc919c6f34a7f771be2414f8496fd038863eefa3a89ed745a56cee4b
---

# Agents can now create Cloudflare accounts, buy domains, and deploy

Coding agents are great at building software. But to deploy to production they need three things from the cloud they want to host their app — an account, a way to pay, and an API token. Until now these have been tasks that humans handle directly. Increasingly, agents handle them on the user’s behalf. The agent needs to perform all the tasks a human customer can. They’re given higher-order problems to solve and choose to use Cloudflare and call Cloudflare APIs.

Starting today, agents can provision Cloudflare on behalf of their users. They can create a Cloudflare account, start a paid subscription, register a domain, and get back an API token to deploy code right away. Humans can be in the loop to grant permission and must accept Cloudflare's terms of service, but no human steps are otherwise required from start to finish. There’s no need to go to the dashboard, copy and paste API tokens, or enter credit card details. Without any extra setup, agents have everything they need to deploy a new production application in one shot. And with Cloudflare’s [ Code Mode MCP server](https://blog.cloudflare.com/code-mode/) and

[, they’re even better at it.](https://github.com/cloudflare/skills)

__Agent Skills__This all works via a new protocol that we’ve co-designed with Stripe as part of the launch of [ Stripe Projects](https://projects.dev/).

We’re excited to launch this new partnership with Stripe, and also to offer [ $100,000 in Cloudflare credits](https://support.stripe.com/questions/stripe-atlas-perks-partners) to all new startups who incorporate using

[. But this new protocol also makes it possible for any platform with signed-in users to integrate with Cloudflare in the same way Stripe does, with zero friction for the end user.](https://stripe.com/atlas)

__Stripe Atlas__Install the [ Stripe CLI](https://docs.stripe.com/stripe-cli/install) with the

[, login to Stripe, and then start a new project:](https://docs.stripe.com/projects)

__Stripe Projects plugin__`stripe projects init`Then prompt your agent to build something new and deploy it to a new domain. You can watch a condensed two-minute video of this entire flow below:

If the email you’re logged into Stripe with already has a Cloudflare account, you’ll be prompted with a typical OAuth flow to grant the agent access. If there is no existing Cloudflare account for the email you’re logged in with, Cloudflare will provision an account automatically for you and your agent:

You will see the agent build and deploy a site to a new Cloudflare account, and then use the Stripe Projects CLI to register the domain:

The agent will prompt for input and approval when necessary. For example, if your Stripe account doesn’t yet have a linked payment method, the agent will prompt you to add one:

At the end, the agent has deployed to production, and the app runs on the newly registered domain:

The agent has gone from literal zero, no Cloudflare account at all, without any preconfigured [ Agent Skills](https://github.com/cloudflare/skills) or

[, to having:](https://blog.cloudflare.com/code-mode-mcp/)

__MCP server__- Provisioned a new Cloudflare account
- Obtained an API token
- Purchased a domain
- Deployed an app to production

But wait — how did the agent discover that it could do all of this? How did it know what services it could provision, and how to purchase a domain? How did it gain the context it needed to understand how to deploy to Cloudflare? Let’s dig in.

There are three components to the interaction between the agent, Stripe, and Cloudflare shown above:

- **Discovery**— the agent can call a command to query the catalog of available services.
- **Authorization**— the platform attests to the identity of the user, allowing providers to provision accounts or link existing ones, and securely issue credentials back to the agent.
- **Payment**— the platform provides a payment token that providers can use to bill the customer, allowing the agent to start subscriptions, make purchases and be billed on a usage basis.

These build on prior art and existing standards like OAuth, OIDC and payment tokenization — but are used together to remove many steps that might otherwise require a human in the loop.

In the agent session above, before the agent ran the CLI command `stripe projects add cloudflare/registrar:domain`, it first had to discover the [ Cloudflare Registrar](https://domains.cloudflare.com/) service. It did this by calling the

`stripe projects catalog` command, which returns available services:The full set of [ Cloudflare products](https://developers.cloudflare.com/directory/) and services from other providers is

[— arguably overwhelming to humans. But for agents, this catalog of services is exactly the context they need. The agent chooses services to use from this catalog based on what the user has asked them to do and the user’s preferences — but the user needs no prior knowledge of what services are offered by which providers, and does not need to provide any input. Providers like Cloudflare make this catalog available via a simple REST API that returns JSON, and that gives agents everything they need.](https://docs.stripe.com/projects#available-providers)

__long and growing__When the agent chooses a service and provisions it (ex: `stripe projects add cloudflare/registrar:domain`), it provisions the resource within a Cloudflare account. But how is it able to create one on demand, without sending a human to a signup page?

Remember how at the start, the user signed in to their Stripe account? Stripe acts as the identity provider, attesting to the user’s identity. Cloudflare automatically provisions a new account for the user if no account already exists, and returns credentials back to the Stripe Projects CLI, which are securely stored, but available to the agent to use to make authenticated requests to Cloudflare. This means if someone is brand new to Cloudflare or other services, they can start building right away with their agent, without extra steps.

If the user already has a Cloudflare account, they’re sent through a standard OAuth flow to grant access to the Stripe Projects CLI, allowing them to provision resources on their existing Cloudflare account.

You might rightly worry, “What if my agent goes a bit overboard and starts buying dozens of domains? Will I end up on the hook for a massive bill? Can I really trust my agent with my credit card?”

The protocol accounts for this in two ways. When an agent provisions a paid service, Stripe includes a payment token in the request to the Provider (Cloudflare). Raw payment details like credit card numbers aren’t ever shared with the agent. Stripe then sets a default limit of $100.00 USD/month as the maximum the agent can spend on any one provider. When you’re ready to raise this limit, you can then set [ Budget Alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) on your Cloudflare account.

Any platform with signed-in users can act as the “Orchestrator”, playing the same role Stripe does with Stripe Projects, and integrate with Cloudflare.

Let’s say your product is a coding agent. You’d love for people to be able to take what they’ve built and get it deployed to production, using Cloudflare and other services. But the last thing you want is to send people down a maze of authorization flows and decision trees of where and how to deploy it. You just want to let people ship.

Your platform acts as the Orchestrator, with the already signed-in user. When your user needs a [ domain](https://domains.cloudflare.com/), a

[, a](https://developers.cloudflare.com/r2/)

__storage bucket__[to give their agent, or](https://blog.cloudflare.com/dynamic-workers/)

__sandbox__[, you make one API call to Cloudflare to provision a new Cloudflare account to them, and get back a token to make authenticated requests on their behalf.](https://workers.cloudflare.com/)

__anything else__Or let’s say you want Cloudflare customers to be able to easily provision your service, similar to how Cloudflare is partnering with Planetscale to make it possible to [ create Planetscale Postgres databases directly from Cloudflare](https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/). We started working with Planetscale on this well before this new protocol got off the ground, but the flow here is quite similar. Cloudflare acts as the Orchestrator, letting you connect to your PlanetScale account, create databases, and use the user’s existing payment method for billing.

This new protocol starts to standardize the types of cross-product integrations that many platforms have been doing for years, often in ways that were one off or bespoke to a particular platform. Without a standard, each integration required engineering work that often couldn’t be leveraged for future integrations. Similar to how the [ OAuth standard](https://oauth.net/2/) made it possible to delegate access to your account to other platforms, the protocol uses OAuth and extends further into payments and account creation, doing so in a way that treats agents as a first-class concern.

We’re excited to continue evolving the standard, and to work with Stripe on sharing a more official specification soon. We’re also excited to integrate with more platforms —  email us at [ agenticpartnerships@cloudflare.com](https://blog.cloudflare.com), and tell us how you want your platform to integrate with Cloudflare.

Stripe Projects is in open beta, and you can get started even if you don’t yet have a Cloudflare account. Just install the [ Stripe CLI](https://docs.stripe.com/stripe-cli/install), log in to Stripe, and then start a new project:

`stripe projects init`Prompt your agent to build something new on Cloudflare, and show us what you’ve built!
