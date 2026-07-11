---
title: In the Matter of OpenAI vs LangGraph
topic: agents
subtopic: planning
secondary_topics:
- product-engineering/architecture
summary: Compares OpenAI and LangGraph approaches to agent orchestration and framework
  design.
source: latent-space
url: https://www.latent.space/p/oai-v-langgraph
author: Latent Space
published: '2025-04-20'
fetched: '2026-07-11T05:18:05Z'
classifier: codex
taxonomy_rev: 1
words: 1122
content_sha256: 174d4582496b7a4c30b6083cd473c7588fa938a31558098f2e3ae794cb6b6f13
---

# In the Matter of OpenAI vs LangGraph

# In the Matter of OpenAI vs LangGraph

### The silent war in Agent Engineering gets loud.

*Quick reminder:  AI Engineer CFPs close soon! Take a look at “undervalued tracks” like Computer Use, Voice, and Reasoning, and apply via our CFP MCP (talks OR workshops, we’ll figure it out). *

*Relevant to today’s quick post we do have an  Agent Reliability track. Also: take  the 2025 State of AI Engineering Survey!*

The AI attention economy has enabled a hypeboi priesthood who exist in a state of [perpetual](https://www.goodreads.com/quotes/78381-the-first-words-that-are-read-by-seekers-of-enlightenment) performative orgasmic nirvana, minds continually blown as every launch Changes Everything, vibing at gigahertz oscillations of “it’s so over” vs “so back”. OpenAI’s “[Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)” is the latest such earth shatterer:

![](https://substackcdn.com/image/fetch/$s_!jhQf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffce66548-8530-40df-a357-e7c8e13f3a77_601x487.png)

This guide, however, has been less[ well received than Anthropic’s](https://x.com/aiDotEngineer/status/1908230651985485955) equivalent.

If you watch his [multiple](https://latent.space/p/langchain) [appearances](https://www.latent.space/p/shunyu) with us, Harrison Chase is not someone who is quick to “anger”, so calling [this guide](https://x.com/aaditsh/status/1912925307386183693) “[misguided](https://x.com/hwchase17/status/1914016302261506421)” and doing a word by word teardown can seem like fighting words for him[1](https://www.latent.space#footnote-1).

![](https://substackcdn.com/image/fetch/$s_!no5J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F201f144a-3adc-447b-afc2-4b59ac311362_2390x1314.png)

At the heart of the battle is a core tension we’ve discussed several times on the pod - team “Big Model take the wheel” vs team “nooooo we need to write code” (what used to be called chains, now it seems the term “workflows” has won).

## Team Big Workflows

You should read [Harrison’s full rebuttal](https://blog.langchain.dev/how-to-think-about-agent-frameworks/) for the argument, but minus the LangGraph specific parts, the argument that stood out best to me was that you can **replace every LLM call in a workflow with an agent and still have an agentic system:**

![](https://substackcdn.com/image/fetch/$s_!GDCp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e47efdb-80c3-4904-a2d3-ddc595b83139_853x765.png)

And the ideal agent framework lets you start from one side of the spectrum and move to the other, [optimizing for making code easy to change](https://overreacted.io/optimized-for-change/):

![](https://substackcdn.com/image/fetch/$s_!ZWvQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0862fbbb-eebe-433b-b8f2-8b814c1a969f_894x585.png)

You’ll find this necessary because sometimes you DO want to reverse decisions from having too many agents - as [fellow speaker Augment Code](https://www.youtube.com/watch?v=Iw_3cRf3lnM) found in [their #1 SWE-Bench entry](https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1):

![](https://substackcdn.com/image/fetch/$s_!6qOh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff91375cc-2cee-44f0-b822-3e1f04aca8ba_1488x382.png)

[tweet](https://x.com/augmentcode/status/1906821537325576385)

## Team Big Model

To be clear it’s easy to understand where the Big Model folks are coming from: if you work with Big Lab enough, you’ve seen hundreds of engineer-hours of hand tuned workflows obliterated overnight with the next big model update — the AI Engineer equivalent of learning the Bitter Lesson again and again. This is why “[AI engineering with the Bitter Lesson in mind](https://x.com/swyx/status/1902454997427904865)” was such a resonant topic at the Summit (now at 124k views across platforms):

Specifically, I think the success of both OpenAI and [Gemini’s Deep Research](https://www.latent.space/p/gdr) this year primarily leveraging O3 to reason through research planning and execution, and later [Bolt](https://www.latent.space/p/bolt?utm_source=publication-search) and [Manus AI](https://www.youtube.com/watch?v=Xtw6Og7fNG0) doing the same with Claude, with very little workflow engineering, has demonstrated that there’s a lot to be said for building general purpose agents that simply augment models without the “inductive bias” constraints of workflows. O-team researcher Hyung Won Chung noted that adding more structure gets you wins in the short term, but that structure tends to lose in performance as the model (pretrain or inference compute) keeps scaling up.

![](https://substackcdn.com/image/fetch/$s_!rPDd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F518933ca-2674-4984-9afd-20df1ba73bf6_1188x810.png)

[from this talk](https://www.youtube.com/watch?v=kYWUEV_e2ss&t=370s). we are using this insight slightly out of context: Hyung Won was making statements about INTERNAL model architecture, but we think it also applies about EXTERNAL systems built around the model — one wonders if he’d also endorse that extrapolation.

If your goal is to build AGI, to build a horizontal platform, particularly one targeting non-technical consumers who are confused by even having a model selector, then it’s an understandable position to take, and (even encourage, for the purposes of dataset/human feedback collection).

## Workflows AND Agents, not OR

Ultimately the reason I argue Harrison isn’t -actually- taking a fighting stance is he leaves room for the spectrum to exist and makes a remarkably (for someone with obvious skin in the game) balanced argument that you’re going to just want options for doing both:

![](https://substackcdn.com/image/fetch/$s_!0wbj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F019331c5-299c-4f4e-b103-7cfeb4ae8369_612x488.png)

I find this hard to debate - if meaningful conversation is to be had, it really is more about where the current state of this Pareto frontier really is today (I’m not sure it is convex yet) and how to move it out.

What -is- true is that there is such a thing as bad ideas to avoid in creating workflows that will DEFINITELY get steamrolled, and also the converse - **workflow systems that maintain value as their underlying models get upgrades** - as we saw last year with [AlphaCodium’s initial release](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/) in Jan and then its value persisting “out of distribution” in Nov after [the release of o1](https://www.qodo.ai/blog/system-2-thinking-alphacodium-outperforms-direct-prompting-of-openai-o1/) - as we discuss on [our pod covering Flow Engineering](https://www.latent.space/p/bolt?utm_source=publication-search).

![](https://substackcdn.com/image/fetch/$s_!nS-T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F949940d0-63ba-400d-904c-0cdc37f72175_1494x1140.png)

## IMPACT of Agent Frameworks

The other pretty cool thing that Harrison did in his piece was publish [a full comparison table of all relevant Agent Frameworks today](https://docs.google.com/spreadsheets/d/1jzgbANBVi6rNzZVsjZC2CSaCU-byXGlSs0bgy2v2GNQ/edit?usp=sharing), although of course even he couldn’t escape [the McCormick trap](https://x.com/swyx/status/1912294047454228736). It’s useful to test our [descriptive metaframework of everybody’s Agent definitions](https://www.latent.space/p/agent) against a new out-of-distribution Agents definition:

![](https://substackcdn.com/image/fetch/$s_!DJfn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0aee6de-16b7-46ed-9040-c4a40accacf9_1640x855.png)

I think this is a remarkably fair shopping list of abstractions and features for the discerning Agent Engineer — it also articulates why you feel certain gaps when an Agent Framework promises you the world and yet you can’t do some things easily.

## The Great Debates

To callback to our intro, if your mind is continually blown, it can never be made up. I think that helping people make up their minds is a valuable service to the community.

If you like learning from this kind of debate, we’re doubling down on the success of [the Dylan v Frankle showdown](https://lu.ma/ls) from last year’s NeurIPS, and also accepting submissions for what we’re calling “The Great Debates” - good faith debaters from two sides of a relevant industry debate. Everybody wins, but the people who are best able to change minds win the most. [Apply in pairs](https://sessionize.com/ai-engineer-worlds-fair-2025)!

![](https://substackcdn.com/image/fetch/$s_!GACi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b70e86-faa2-4cae-9eaf-cd958863821b_645x566.png)

[https://sessionize.com/ai-engineer-worlds-fair-2025](https://sessionize.com/ai-engineer-worlds-fair-2025)

[1](https://www.latent.space#footnote-anchor-1)

As I’ll argue: they’re actually not! Harrison is ever the diplomat.

Thanks for this!

The terminology of 'chain' in LangChain lingo has never been clear to me since it seems to refer to both individual nodes and the entire workflow, so I'm happy it has been superseded by 'workflow'. LangGraph is their best to date imo.

Anthropic's Building Effective Agents article makes the distinction between agentic loops and deterministic workflows clearer than any other thoughtpiece, even though it oversimplifies the distinction. I get the impression that most people building in this space (myself included) see it more as a spectrum of agency.

I'm keen to see this Agent Framework Breakdown evolve. It's a great start for what could ultimately become a very useful resource.

"Harrison did in his piece was publish a full comparison table of all relevant Agent Frameworks"

Thanks for that , very interesting !!

How does n8n.io fit in here ?
