---
title: The website of the future may assemble itself for every visitor
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/tool-use
summary: Adobe agentic-sites case study on assembling grounded personalized web pages
  for humans and agents.
source: latent-space
url: https://www.latent.space/p/the-website-of-the-future
author: Richard MacManus
published: '2026-07-02'
fetched: '2026-07-11T05:09:29Z'
classifier: codex
taxonomy_rev: 1
words: 1148
content_sha256: bed00c4fcd9860c80ea775cd4456b34a2fd816c0393e57c30ad5254b783c4993
---

# The website of the future may assemble itself for every visitor

# The website of the future may assemble itself for every visitor

### Adobe is experimenting with “agentic sites” that generate pages around an individual user’s intent. At AIEWF, we talked to Carlos Sanchez about the Web's future.

![](https://substackcdn.com/image/fetch/$s_!KiR3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F888e1825-8152-418b-9a18-152de1328077_1280x720.jpeg)

For as long as I can remember (and I managed websites in the dot-com period), “personalization” has been a holy grail for websites. But up till now, that’s typically meant selecting from a predefined set of options. A retailer might recommend an item based on a previous purchase, or place a visitor into one of several audience segments — that’s been the extent of personalization.

Adobe Principal Scientist [Carlos Sanchez](https://x.com/csanchez) is exploring a more radical possibility: what if the website itself could be assembled around the needs of each visitor?

At the AI Engineer World’s Fair in San Francisco, Sanchez demonstrated what Adobe calls an “agentic site” — a web experience that interprets a visitor’s intent, retrieves relevant material from the company’s existing content, and composes a personalized page in real time.

Adobe calls this approach an “audience of one.” Sanchez’s larger point was that the technology is no longer hypothetical.

“Many people don’t even think it’s possible to generate a web page on the fly,” he told Latent Space after his session. “People think it is future-looking. No, you can do this. It’s not the future, it’s the present now.”

**From personalized components to personalized pages**

During his presentation, Sanchez demonstrated a site that used the visitor’s browsing behavior and search queries as signals. The system grouped those signals into an intent category — such as exploring, researching or preparing to purchase — and then used an LLM to assemble a page suited to that intent.

In one example, a visitor interested in camping received a version of a coffee-machine site whose copy, product selection and supporting content had been reorganized around making coffee outdoors.

Sanchez also showed a more open-ended interface in which someone could enter a query such as “Europe AI conferences” and receive a page composed specifically around that request.

“We call this ‘audience of one,’ because the idea is to personalize the site in real time based on the user accessing it and what the user is doing,” Sanchez said.

The idea is that the site’s existing content is the grounding corpus. Adobe’s system retrieves from that material rather than asking an LLM model to invent an entire experience from scratch.

For AI engineers, one potential constraint is latency. In his session, Sanchez said that Adobe evaluates models not only for accuracy, but also for speed: “We don’t want the site generation to take more than one or two seconds.”

Sanchez says the economics are already becoming plausible. He estimated the current inference cost at “one to two cents per page.”

“But our point is also this is only going to get cheaper,” he said. “This is where we are today. In six months, who knows where we’re going to be.”

**AI makes it easier to build, but harder to choose**

Adobe has not yet broadly deployed these experiences on production customer sites. Sanchez said the company is presenting the concept to customers and looking for organizations willing to experiment.

Commerce is an obvious initial use case, because personalization can be connected directly to conversion. But the opportunity is not necessarily limited to retail. “It could work for other things — anything that needs more conversion and has a big matrix of user types or personas,” he told me.

Still, Sanchez acknowledged that he’s unsure if agentic sites will become a widespread reality.

“With AI, it’s very easy to build things, but it’s hard to know what to build,” he said. “We build things and then we find the customers.”

It’s not just Adobe feeling the uncertainty around its ‘audience of one’ concept. Website owners are currently evaluating all kinds of AI functionality: chat interfaces, structured content (like WebMCP), generative UI, personal agents, and more. Not to mention trying to find ways to bring users in from third-party AI platforms.

“I think it’s a combination of all these crazy different ways,” Sanchez said. “You are in a chat, I want to show UI, I want to get you to buy something. Then you’re in a site, I want to steer you this other way. Maybe you’re in an OpenAI chat and I want to bring you into my site. Everybody’s trying to figure this out on the marketing side.”

**A web built for humans — and agents**

Of course, websites in 2026 and beyond won’t just be personalized for human visitors.

As personal agents become more capable, a user may delegate some purchases or research tasks entirely. The agent could arrive carrying a much richer expression of the user’s preferences than the destination site could infer from cookies or recent browsing behavior.

Sanchez expects websites to evolve for both kinds of visitor. “Whether it’s going to be two versions [of a website] or not, that may be blurry,” he said. “But obviously, you’re going to have to target both.”

Also, not every transaction will work the same way. A personal agent might autonomously reorder toilet paper, while a person buying a jacket may still want to inspect the product and make the final choice through a visual interface.

That means websites will need to support different levels of delegation and involvement, rather than treating “agentic commerce” as a single interaction pattern.

Technologies such as WebMCP could allow a site to expose structured tools directly to an agent, while MCP Apps and other generative interfaces could bring interactive product experiences into the user’s chat environment. An A2A backend might allow agents to interact without traversing the conventional visual site at all.

It might end up being one site with both visual components and agent-accessible tools — two distinct experiences — or perhaps a human-facing website paired with an agent-to-agent service.

“That’s still what everybody’s trying to figure out,” Sanchez said. “But there’s going to be agentic targeting, for sure.”

## Whither websites?

Whether websites survive the AI era at all is another big question we’re all grappling with.

What I gleaned from Sanchez at AIEWF was that the traditional website is unlikely to disappear completely, but its role will surely change.

Rather than being a fixed collection of pages that every visitor navigates, a “website” could become a governed content and interaction system that assembles an appropriate interface on demand. At least, that’s the future that Adobe is actively exploring.

15 years ago the Data Portability Working Group, @chris Saad et al, was working on making this an open tech standard that would allow users to choose, and perhaps even monetize, which portions of their interest graph to expose to a site they visited. Let’s see Adobe lead the reconvening of a user-centric, open standard around this, so a whole ecosystem of innovations can flourish!
