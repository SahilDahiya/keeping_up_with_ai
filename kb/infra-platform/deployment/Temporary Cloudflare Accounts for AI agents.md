---
title: Temporary Cloudflare Accounts for AI agents
topic: infra-platform
subtopic: deployment
secondary_topics:
- agents/tool-use
summary: Temporary Cloudflare Accounts let agents run 'wrangler deploy --temporary'
  to ship a Worker with zero signup — a 60-minute claimable account with auto-provisioned
  API token — with Wrangler itself prompting agents about the flag, removing human-built
  OAuth/dashboard friction from the deploy loop.
source: cloudflare-ai
url: https://blog.cloudflare.com/temporary-accounts/
author: Sid Chatterjee
published: '2026-06-19'
fetched: '2026-07-11T04:12:50Z'
classifier: claude
taxonomy_rev: 1
words: 933
content_sha256: 11edb3f9d18d05b53ce77b96160bd37ab53778d95d8abed806c2623bb47b831d
---

# Temporary Cloudflare Accounts for AI agents

Everyone's writing code with AI agents today. But the moment an agent needs to deploy something — and needs to sign up and create an account — it slams face-first into a wall built for humans: a browser-based OAuth flow, a dashboard to click through, an API token to copy-paste, a multi-factor authentication prompt to satisfy. For an interactive copilot sitting next to a developer, that's annoying. For a background agent, it's a hard stop.

Today we're rolling out Temporary Cloudflare Accounts for Agents.

Agents can now deploy [ websites](https://www.cloudflare.com/solutions/frontends/),

[, and](https://www.cloudflare.com/products/workers/)

__APIs__[right away, without first needing to sign up for an account.](https://www.cloudflare.com/products/agents/)

__agents__Any agent can now run `wrangler deploy --temporary `and deploy a Worker to Cloudflare. This temporary deployment stays live for 60 minutes, during which time you can claim the temporary account, making it permanently your own. If you don't, it expires on its own.

Our goal? Let your agent code and ship.

Frictionless temporary accounts matter more than it might first seem:

- **Background AI sessions have no human in the loop, and are becoming the norm**. Any auth step that needs a browser, a copy-paste, or "click here in 60 seconds" means an agent gets stuck and may choose to deploy elsewhere.
- **Trial-and-error is the agent's superpower**. Agents need a tight write → deploy → verify loop. They need cheap, throwaway deployment targets, so they can curl their own output and decide whether they got it right.
- **Agent platforms are building their own ways for deploying code to "just work" without extra steps or credentials**. People are starting to expect that this process just works, without the need to sign up for other services that they've not used before or heard of.

Temporary accounts are built around [ Wrangler](https://developers.cloudflare.com/workers/wrangler/), our Developer Platform command-line interface (CLI) tool that lets developers bootstrap new projects, manage their configurations and resources, and deploy and update them.

Wrangler usage is widely [ documented](https://developers.cloudflare.com/workers/examples/) online and agents know how to use it very well. But if you hadn’t yet signed in and granted Wrangler permission to your Cloudflare account, when the agent tried to deploy, it would get stuck at the sign-up and authentication step. And you might rightly ask: How do agents and LLMs know that this new

`--temporary` flag in Wrangler exists, so that they actually use it without a human explicitly telling them to do so?To solve this, we updated Wrangler to prompt the agent with a message that tells it about the `--temporary` flag:

When the agent discovers this, and then runs **wrangler deploy**`--temporary` flag, Cloudflare provisions a temporary account for the agent to use, gives Wrangler an API token to work with, and provides a claim URL that the agent can give back to the human.

Make sure you’re using the latest [ Wrangler release](https://github.com/cloudflare/workers-sdk/releases), fire up your favorite coding agent, and write a prompt to deploy a "hello world" app in build mode:


`Make a very simple hello world Cloudflare Worker in TypeScript and deploy it using wrangler, don't ask me questions, do the best you can`

The agent will run wrangler, pick up the `--temporary` flag from the output messages, build your script, and deploy it instantly, no human in the loop required:

As you can see, the agent wrote the script, deployed it using the `--temporary` flag, curled the preview link it got from the output, and verified that the result matches the code.

This is great, but agentic coding is often not about one single deployment. A session can go through a cycle of multiple code changes. This is not a problem: the agent can iterate on the Worker script and redeploy the changes as many times as it wants (within the 60-minute claim window). Type this prompt:


`Now change hello world to "hello cloudflare" and redeploy`

Look at the agent changing the source code, reusing the previously created temporary account, redeploying a new version and rechecking the result:

At any point, you can claim the temporary account and make it yours permanently. When you click the claim link you will be taken to a page where you can either sign up for or sign in to Cloudflare, and then claim the temporary account that your Worker was deployed to. This includes claiming not just Workers, but resources like databases and other bindings, too.

If you do not claim these temporary accounts within 60 minutes, they will be automatically deleted.

This is just one way we’re eliminating the signup barrier for agents. We recently [ announced a partnership with Stripe](https://blog.cloudflare.com/agents-stripe-projects/) and a new protocol we co-designed that lets agents provision Cloudflare on behalf of their users — creating an account, starting a subscription, registering a domain, and getting an API token to deploy code, with no copy-pasting tokens or entering credit card details. Last month, we collaborated with WorkOS on the launch of

[, which anyone can adopt, to let agents provision new accounts using well-established, existing OAuth standards.](https://workos.com/auth-md)

__auth.md__There’s a ton going on in this space, and we’re excited to keep making it easier for agents to use Cloudflare, and for developers to make their own apps [ agent-ready](https://isitagentready.com/). Temporary accounts are one more step toward frictionless agentic deployments — stay tuned for more.

Temporary accounts have some limitations, and their capabilities may change over time; check the [ developer documentation](https://developers.cloudflare.com/workers/platform/claim-deployments/) for more information and then go build something. Point your agent at Cloudflare, see how far it gets, and tell us what we can improve or what delights you — share what you’ve built on

[or hop into the](https://x.com/CloudflareDev)

__X__[.](https://community.cloudflare.com/)

__Cloudflare Community__
