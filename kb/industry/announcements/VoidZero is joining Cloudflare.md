---
title: VoidZero is joining Cloudflare
topic: industry
subtopic: announcements
secondary_topics: []
summary: VoidZero — the company behind Vite, Vitest, Rolldown, Oxc, and Vite+ — joins
  Cloudflare, with commitments that the tools stay MIT-licensed, vendor-agnostic,
  and community-led, mirroring the earlier Astro acquisition; notable AI angle is
  Cloudflare consolidating the JS toolchain under its developer platform.
source: cloudflare-ai
url: https://blog.cloudflare.com/voidzero-joins-cloudflare/
author: Evan You
published: '2026-06-04'
fetched: '2026-07-11T04:13:02Z'
classifier: claude
taxonomy_rev: 1
words: 1834
content_sha256: 3948bb52db474b84afc0a6679d78331a233bce67712ed470367f8021630e88d7
---

# VoidZero is joining Cloudflare

VoidZero, the company behind [ Vite](https://vite.dev/),

[,](https://vitest.dev/)

__Vitest__[,](https://rolldown.rs/)

__Rolldown__[, and](https://oxc.rs/)

__Oxc__[, is joining Cloudflare. As part of this change, all team members of VoidZero are joining Cloudflare, too.](https://voidzero.dev/posts/announcing-vite-plus-alpha/)

__Vite+__Before saying anything else, we want to make the most important thing clear: Vite, Vitest, Rolldown, Oxc, and Vite+ will stay open source, vendor-agnostic, and community-driven. Nothing about that changes.

Cloudflare's mission is to help build a better Internet. And a better Internet is an open Internet. Developers need choice, frameworks need a neutral foundation, and applications need to be portable. It is not reasonable to expect the entire web ecosystem to build around a single vendor. The most important tools and frameworks are portable by design.

Vite is one of the few foundational tools that the whole JavaScript ecosystem agrees on. It earned that position by being fast, excellent, portable, and vendor-neutral. One of the best ways Cloudflare can help build a better Internet is by investing in that foundational open source toolchain. A toolchain that makes the Internet better for everyone, not just people who use Cloudflare or choose to host with us.

Over the last few years we've invested heavily in making Cloudflare the best place to build and run websites, applications, and agents on our [ developer platform](https://www.cloudflare.com/developer-platform/). But ultimately that choice will always be yours. Run your Vite application anywhere you want.

Today's news gives Vite more resources to keep growing, while the things that make Vite what it is remain the same:

- Vite remains MIT-licensed and open source.
- Vite remains vendor-agnostic. Applications built with Vite run anywhere and will continue to do so.
- Vite's roadmap continues to be driven by the broader Vite team and community, and continues to be developed in the open.
- Evan and the rest of the VoidZero team continue to lead Vite, Vitest, Rolldown, Oxc, and Vite+.
- Cloudflare is committing engineering and resources to those projects, not redirecting them.

We made the same kind of commitment when [ Astro joined Cloudflare](https://blog.cloudflare.com/astro-joins-cloudflare/) earlier this year. Astro is still open source, and still deploys anywhere. The team is still shipping the roadmap they were already shipping.

This commitment matters even more with Vite, because Vite is not one framework. Vite is the foundation underlying so many: [ Vue](https://vuejs.org/),

[,](https://svelte.dev/docs/kit/introduction)

__SvelteKit__[,](https://nuxt.com/)

__Nuxt__[,](https://astro.build/)

__Astro__[,](https://www.solidjs.com/)

__Solid__[,](https://qwik.dev/)

__Qwik__[,](https://angular.dev/)

__Angular__[,](https://reactrouter.com/)

__React Router__[. Even](https://tanstack.com/start)

__TanStack Start__[now has a Vite-based implementation in](https://nextjs.org/)

__Next.js__[. Vite has become a shared foundation for the JavaScript ecosystem.](https://blog.cloudflare.com/vinext/)

__vinext__Our number one goal is to maintain the trust that has earned Vite so much adoption. Not with our words here, but by proving it every day in how we support and develop these projects.

We also want to put our money where our mouth is when it comes to our support for open source and shared ecosystem foundations. As part of this announcement, Cloudflare is committing $1 million to a Vite ecosystem fund to support maintainers and contributors, administered by the Vite core team. Vite is bigger than VoidZero or Cloudflare, and the people who have helped build it should be part of what comes next.

The Vite and Cloudflare teams have been collaborating well before this announcement, starting in 2024 with the [ Vite Environment API](https://vite.dev/guide/api-environment). The Environment API lets Vite run server code in something other than Node.js during development. We worked closely with the Vite team on its design, and then built the

[on top of it.](https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin/)

__Cloudflare Vite plugin__When you run `vite dev` with the Cloudflare plugin, your server code runs inside [ workerd](https://github.com/cloudflare/workerd), the same open-source runtime that powers Workers in production. Durable Objects, D1, KV, R2, Workflows, Workers AI, Agents, Service Bindings, Workers RPC – all of it runs locally inside the same runtime model as production.

For a long time, the cost of developing on a non-Node runtime was that local dev felt like a worse version of production. The Environment API removed that cost without forcing anyone to adopt a Cloudflare-specific dev server. Any runtime that wants to plug into Vite can do the same thing. That kind of design – a generic mechanism in Vite with provider-specific implementations – has proven to work well and is one we want to keep building on.

We knew we were on to something when we saw adoption of the Cloudflare Vite plugin take off:

Vite's adoption curve is one of the more remarkable things to watch in the ecosystem right now. As of this writing, Vite is at roughly **129M weekly downloads**. The Cloudflare Vite plugin (`@cloudflare/vite-plugin`) is at almost **14M weekly downloads**.

If you had told us a year ago that a Cloudflare Vite plugin would reach downloads equivalent to more than 10% of Vite itself, we wouldn’t have believed you. What happened? AI happened. More software is being created than ever before, and a lot of it starts with AI-generated code. Those applications need a default stack and a place to run. Agent-coded applications are choosing Vite, and increasingly they are choosing Vite running on Cloudflare.

Developers used to be the only users of dev servers, bundlers, linters, formatters, and CLIs. That is no longer true: agents are using them too, constantly. They scaffold projects, run dev servers, read errors, write tests, lint and format code, deploy previews, and iterate.

A lot of AI-generated applications already start as Vite apps, because Vite is fast, well understood, and broadly compatible with what agents have seen in their training data. Fast feedback loops have always been important. They become even more critical when writing software with agents:

- Fast builds, because they iterate more than humans do.
- Fast tests, because they re-run the suite constantly to verify their own work.
- Fast linting and formatting, because those tools become guardrails.
- Clear, structured errors, because the agent has to read and act on them.
- Consistent CLIs, because small inconsistencies cause big detours.

The entire VoidZero toolchain is built for this kind of loop. Vitest, Rolldown, Oxc, Oxlint, and Oxfmt are each among the fastest tools in their respective categories, and they work well when they are run over and over by an agent. Vite+ brings those pieces together into one toolchain, with one CLI, one configuration model, and fewer moving parts. That makes the development loop easier for people to understand, and easier for agents to drive reliably.

We are dogfooding this ourselves. The Cloudflare dashboard is built on Vite. Oxlint is already [ saving days of engineering time](https://x.com/rozenmd/status/2037582692355621289?s=46&t=tJveHCYtiY5v-kdgTMClJQ) in Cloudflare codebases.

[, the agent harness framework from the Astro team, is also moving onto Vite as its foundation. Flue can run agents on Node.js, Cloudflare Workers, GitHub Actions, GitLab CI/CD, and more, and the Cloudflare target now uses the official Cloudflare Vite plugin and workerd integration. Vite is becoming the default application foundation inside Cloudflare too.](https://www.flueframework.com/)

__Flue__A few years ago, the job of a build tool was straightforward: take source files, produce a bundle, hand it off. That is not enough for modern applications, especially in a world where some of those applications are agents themselves.

A modern application is server-rendered routes, APIs, background jobs, queues, databases, object storage, real-time, auth, plus a growing list of agents and AI capabilities. The "build" is no longer the end of the story. It is the start of a deployment that has to understand all of those pieces.

That means Vite has to become more than a build tool. It needs to understand more of the application, while staying true to what made Vite work in the first place: speed, simplicity, and portability.

[ Void](https://void.cloud/), a deployment platform designed for Vite, has been another testbed for these ideas. It helped explore what a modern application framework should own, what deployment should feel like, and how much of the full application lifecycle can be unified around one toolchain. We have learned a lot from that work.

Now the work is putting those lessons in the right place. Some belong in Vite itself as provider-agnostic primitives: first-class abstractions and hooks for backends, APIs, agents, and deployment that any provider can implement. Other lessons belong inside Cloudflare. Cloudflare will provide a first-class implementation of those hooks on Workers and the rest of our Developer Platform.

Even though some Vite maintainers are joining Cloudflare, changes to Vite itself will continue to go through the same open contribution process as any other Vite contribution. Features added to Vite itself should not be Cloudflare-specific. They will work anywhere Vite works.

The same principle shaped how we think about the future of Cloudflare's own tooling. We are not moving Vite in the direction of Cloudflare. We are doing the opposite: moving Cloudflare's application tooling onto Vite, so it is built on top of the same workflows developers already know.

We recently shipped a technical preview of

__cf__

If we do this right, the Cloudflare CLI should feel like Vite, not like a separate thing bolted on next to Vite.

- `cf dev`should be a superset of- `vite dev`. Same speed, same hot module replacement, same plugin model, plus the Cloudflare runtime and bindings when you want them.
- `cf build`should understand Vite projects natively, without an adapter dance.
- `cf deploy`should make deploying a Vite app to Cloudflare simple.

If you are running Vite today, the path to Cloudflare will feel like swapping in a superset of the commands you already know. Same project shape. Same Vite workflows. The entire Cloudflare developer platform available when you want it.

In the short term, nothing changes for Vite users or the frameworks building on top of Vite:

- Vite, Vitest, Rolldown, Oxc, and Vite+ keep shipping. The VoidZero team keeps contributing and leading them.
- The Cloudflare Vite plugin keeps improving.
- The Environment API and the broader story of "run your server code in the right runtime locally" keeps getting better, including for non-Cloudflare runtimes.

Longer term:

- We start the work on moving the Cloudflare CLI toward an experience built directly on top of Vite.
- Vite will get new, clean, provider-agnostic primitives for full-stack apps and agents that work for everyone on any platform.
- Over time, we intend to open-source the - __Void platform__

We will do all of this in public and with the community. The same way Vite has always been built.

Vite, Vitest, Rolldown, Oxc, and Vite+ exist because a deep ecosystem of open source contributors put years of work into them. These projects are already foundational to how the web is built, and we are grateful to everyone who helped get them here. Thank you to everyone who has contributed code, reviews, issues, docs, plugins, integrations, and support along the way.

We are excited to welcome the VoidZero team to Cloudflare, and excited to put more resources behind these projects. Our job now is to help them grow, stay open, and power the JavaScript ecosystem for everyone.

Vite keeps being Vite. Cloudflare gets to help.

If you want to try Vite on Cloudflare today, run:

`npm create vite@latest`

`npx wrangler deploy`
