---
title: Building secure mobile apps in the agentic era (2026)
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/harness
- evals-observability/monitoring
summary: Shopify built an agentic mobile-app security review system -- one OWASP MASVS/MASTG-based
  skill per attack surface (deep links, WebViews, stored data, dependencies), each
  item reviewed individually with only its own code -- that runs daily to catch vulnerabilities
  as code throughput rose 11x (434k LOC/week) after moving to agent-written mobile
  code.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/secure-agentic-apps
author: Michael Hughes
published: '2026-11-18'
fetched: '2026-11-20T06:12:54Z'
classifier: claude
taxonomy_rev: 2
words: 1300
content_sha256: aac1c0f0175899b2ec8522c27f8c47e87c3c0c8fc7491a341fe88cc48c3d6020
---

# Building secure mobile apps in the agentic era (2026)

**In the agentic era, code throughput in our mobile apps has increased to the point where we're now shipping 11x compared to the same time last year. To ship quickly and securely at this pace, we needed to innovate our approach to mobile application security.**

![Sample app security review listing attack surfaces, inventories, and issue verdicts for deep links, WebViews, and stored data.](https://cdn.shopify.com/s/files/1/0779/4361/files/mobile-security-02.png?v=1794941665)

*Sample app with mock data*

Across our [12-week rewrite of the Shopify app,](https://shopify.engineering/shopify-app-rebuild) we averaged \~434,000 lines of code changed per week. The same time last year, we were shipping \~39,000 lines of code per week in the Mobile Shopify app.

Not only are we shipping 11x the code, but [the industry is seeing](https://www.theregister.com/security/2026/11/13/this-years-bug-count-just-passed-100k/5309882) record numbers of vulnerabilities in codebases that have been reviewed by humans for years. To keep ahead, we needed to change how we work.

We've been busy building with agents. We've written about [why we went back to native](https://shopify.engineering/back-to-native), how we [rebuilt the Shopify app in 12 weeks](https://shopify.engineering/shopify-app-rebuild), how [Helix](https://shopify.engineering/helix) helped agents rebuild the Shopify app's 300+ screens, and how [Remote Dev](https://shopify.engineering/remote-dev) lets agents build and test in parallel.

Our existing [vulnerability scans](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) already look for vulnerabilities in the code we change. We wanted to go further and minimize our attack surface while enforcing the practices that keep vulnerabilities from appearing in the first place. There's a lot to cover in a mobile app, and each area has its own best practices. Every incident we've handled has also taught us something that we apply from then on. So we needed to see each app's whole attack surface, notice when it changes, and check every part of it against what we've learned so far.

This post covers what we built, and what we'd suggest to anyone building apps with agents.

## Start with a map of the attack surface

For each app, we keep a list of everything security-sensitive, grouped into surfaces: deep links, WebViews, stored data, permissions, dependencies, etc. For each surface, we write a sentence or two about why it matters. Every item on the list has a verdict and a link to the code it came from.

We limit each item to one of five verdicts:

- Fix (with a severity)
- Tradeoff
- Secure
- Fixed
- Debug only

## Write the knowledge down as skills

The map is produced by a set of skills, one for each surface. We started with OWASP's mobile app security standard ([MASVS](https://mas.owasp.org/MASVS/)) and testing guide ([MASTG)](https://mas.owasp.org/MASTG/), and added what we've learned from vulnerabilities reported against mobile apps, including our own. Each skill describes what to list, what good looks like, and what to check.

Because they're skills, they aren't tied to one tool. The scheduled review uses them, we use them for one-off security reviews, and any agent working in the code can load them. When we learn something new, we update the skill and every later run picks it up.

## Keep each review small

If you ask a model to find vulnerabilities in a whole app, you get a long, vague list. So each skill first takes a complete inventory: every deep link route and every parameter it reads, every WebView and the hosts it loads, every WebView javascript interface method, every Keychain and Keystore entry, and every dependency and its version. Then the model reviews one item at a time, with only the code that item touches.

![Deep-link inventory linking routes and parameters to code, with a coupon link flagged because its next-page URL is not checked.](https://cdn.shopify.com/s/files/1/0779/4361/files/mobile-security-03.png?v=1794941665)

*Sample app with mock data*

For a deep link, that means looking at one route, every parameter it reads and the code that reads each one, and asking what happens when a parameter is hostile. The answer is specific enough to verify. When it depends on whether something can actually be exploited, the model can pass that question to one of the frontier cybersecurity models.

## Learn from every incident

When we handle an incident or a [HackerOne report](https://hackerone.com/shopify), we fix the bug, then add that class of problem to the skills. Every run checks the current code against all of those classes, and each surface has a short checklist of the best practices we expect.

![Deep-link security review flagging a coupon link that opens any HTTPS page, with past incident checks and link-handling best practices.](https://cdn.shopify.com/s/files/1/0779/4361/files/mobile-security-04.png?v=1794941665)

*Sample app with mock data*

## Review the changes every day

Every weekday, the latest frontier models look at the changes made to the app and update the attack surface. Then they dig into each individual change in the attack surface and look for vulnerabilities with cybersecurity models:

1. **Prepare** takes the inventory at the latest commit and compares it with the last accepted map. An item counts as "changed" only when a cited line of code changed, or when the inventory reports a change to it.
2. **Review** requires the model to judge each changed or new item, with read-only tools and nothing but the code. A second pass reads the changed files for anything security-relevant that no item covers. We check every answer before using it: its format, line ranges, and wording, and make sure that it doesn't contain a secret.
3. **Publish** builds the new map and a page of what changed, and posts a summary to Slack.

The changes page lists every security-sensitive change since the last run, with a verdict for each one.

![Sample app security changes between two commits, showing new and fixed deep-link issues and a WebView moved into a sandbox.](https://cdn.shopify.com/s/files/1/0779/4361/files/mobile-security-05.png?v=1794941665)

*Sample app with mock data*

## Watch for changes outside the repo

Some problems never show up in our own diffs. Industry-wide vulnerabilities are announced with increasing frequency in the platforms and packages we depend on, and we need to react to them. We have automated dependency tracking and bumping, but sometimes there are issues that still need attention. To stay on top of the latest issues, agents regularly read security news and check each item against the map and our code. The agent posts a short briefing and only pings the team when something affects us. Here’s an example of what one of those briefs looks like:

*🟢 **Mobile security briefing** · Nothing affects the apps.*

*🔁 **Ongoing***

- ***Example package 2.3 security release**: fix ships Thursday, bumps ready for both apps, since Mon 3 Nov.*

*⚪ **Worth knowing***

- ***Example browser engine update**: three critical fixes, none exploited. Not us: phones get the update automatically.*

*💤 **Quiet**: platform bulletins, known-exploited vulnerabilities, research blogs.*

We've also used the same skills on third-party libraries before adopting them, which gives a dependency the same map and verdicts as our own code.

## Security at agentic pace

Agents let us ship more changes, faster. To keep them secure, we:

- Keep a map of each app's attack surface, so we can see what we ship and where we can make it smaller.
- Write down our best practices and the lessons from past incidents and turn them into skills, enforcing them on every app.
- Break the review into small, well-defined problems, like one deep link or WebView at a time, so the model can operate on a defined problem space.
- Review what changed every weekday, and check security news against our apps for problems that don't come from our own code.

We run these checks in addition to the work of [Dispatch,](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) our agentic vulnerability scanner. Dispatch finds and proves vulnerabilities in the code we change, and the attack surface map makes sure each app as a whole stays small and follows our best practices.

Every vulnerability we find and fix strengthens the checks we run on the next change. That’s how we’re building secure mobile apps in the agentic era.

*Want to solve hard problems like these? [We’re hiring](https://www.shopify.com/careers).*
