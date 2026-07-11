---
title: SWE Agents Too Cheap To Meter, The Token Data War, and the rise of Tiny Teams
topic: industry
subtopic: trends
secondary_topics:
- agents/computer-use
- evals-observability/evaluation
summary: Analyzes coding-agent pricing, user data acquisition, LMArena, and the shift
  from token margins to feedback/data loops.
source: latent-space
url: https://www.latent.space/p/token-data-war
author: Latent Space
published: '2025-05-24'
fetched: '2026-07-11T05:17:47Z'
classifier: codex
taxonomy_rev: 1
words: 1346
content_sha256: 1794a802bb05429bdd2aacd4e5c4983da8c515017cd57114e841e305d036b87d
---

# SWE Agents Too Cheap To Meter, The Token Data War, and the rise of Tiny Teams

# SWE Agents Too Cheap To Meter, The Token Data War, and the rise of Tiny Teams

### Cheap SWE Agents are enabling teams with more millions in ARR than employees. Reflections after the OpenAI Codex and Google Jules Launches, Cognition DeepWiki, and LMArena's $100m raise.

*btw  Gamma, Bolt, Oleve and more are presenting on the new Tiny Teams track, and  leads of both OAI Codex and Google’s Jules will be presenting at AI Engineer World’s Fair! *

**You know the drill by now**- the AIE expo and all 3 conf hotels are now

**sold out**! Join the Hackathon and fill out the State of AI Engineering Survey!

The recent launches of the [Codex](https://www.latent.space/p/codex) and [Jules](https://news.smol.ai/issues/25-05-20-google-io) Devin-like autonomous coding agents came with some interesting pricing decisions: **they come at no extra cost 1**. You no longer have a reason NOT to send off every thought to the agents (

[even more than once](https://x.com/latentspacepod/status/1925006338230517773)) even if you intend to eventually code it yourself.

Let me repeat: **YOU CAN FIRE OFF  A CODEX REQUEST EVERY 60 SECONDS AND THEY DON’T CHARGE YOU EXTRA**. YOU SHOULD USE THIS!!!

This comes after a 3 year trend of exploring the SWE Agent pricing spectrum:

![](https://substackcdn.com/image/fetch/$s_!_hhk!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a2e189b-2fbb-4605-a578-7b26516139b3_1996x1410.png)

Variously:

And of course there are a lots of premium and open source coding agents with Bring Your Own Key and reasonably metered usage like [Github Copilot Coding Agent](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/) and the newer [Amp Code](https://ampcode.com/).


Side note: A less rigorous publication than the one you’re reading could observe correlation of the rise of coding agents with the infamous Indeed software developer job postings chart and conclude causation:

without normalizing for the[macro base rate](https://fred.stlouisfed.org/series/IHLIDXUS)and the[shift in job definitions](https://x.com/mtabarrok/status/1901642461237199104?s=61).

However our sense is that, especially with the frontier labs launching effectively unlimited usage plans, the competitive war in coding agents has come to the point where **the norm of charging a premium over token usage as a coding agent GPT wrapper has now FLIPPED to offering discounts in order to get your usage data**.

That’s insane, you say. Lighting VC money on fire at negative margins is unsustainable!

And yet [Perplexity](https://www.perplexity.ai/page/perplexity-ai-in-talks-for-500-lkMydBK6QFuNZI6P5sg0Hw) with [-200% profit](https://x.com/swyx/status/1925117936290996431) is worth $14B and [Cursor](https://techfundingnews.com/ai-coding-tool-cursor-9b-valuation/) is worth $9B. How can you not realize that there is value in user data and acquisition when [OpenAI pays $3B for Windsurf](https://news.smol.ai/issues/25-05-05-cursor-openai-windsurf) at [75x ARR](https://x.com/_HooJR/status/1915013469918597354)?

## Realizing The Value of User Data

The CodeGen, and now SWE Agent[2](https://www.latent.space#footnote-2), market has thus progressed[3](https://www.latent.space#footnote-3) as such:

- First, charge a small flat fee for a new product category ( - [Copilot](https://www.youtube.com/watch?v=yLa3i3rAdEE))
- Then, offer a free consumer edition and make money in enterprise ( - [Codeium](https://www.latent.space/p/windsurf))
- Then seek out the high end of the category and charge a premium ( - [Devin](https://www.youtube.com/watch?v=T7NWjoD_OuY))
- Then broaden audience to noncoders ( - [Bolt](https://www.youtube.com/watch?v=swQLziqWgus&t=370s)) and be MORE agentic (- [Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo))
- Charge flat-rate or free to get user data to build products + models (Codex, Jules)

As the average MMLU and SWEBench of every model goes up, so does the competition for increasingly advanced data to build those models. If we have exhausted GitHub and StackOverflow as datasets reflecting the average programmer, then we need elite ones per domain, and so on. We have heard rumors that there are now niche data services - in the style of [Scale](https://www.turing.com/services/ai) and [Turing](https://www.turing.com/services/ai) - that employ ex-industry professional humans specialized in creating/labeling medical, financial and coding data for labs, paying up to $500k/year per human. A scaled operation of 100 of these would cost an easy $50m/year.

That’s 6.25 TRILLION tokens of GPT4.1. The average coder consumes about 2m tokens a day [per Claude Code numbers](https://www.latent.space/p/claude-code), so if you could figure out a way to collect useful data to your domain, **you can justify giving away tokens as an alternative to paying for data** - probably more because your users are the most specifically suited, self selected and self motivated labelers you will ever get. This is why you can kind of justify that [Perplexity is classifying free tier costs as R&D](https://x.com/marcb_xyz/status/1924917948180742545) if you squint really hard.

When we first wrote about [the Four Wars of the AI Stack](https://www.latent.space/p/dec-2023), most of the conversation was around data acquisition from traditional content houses and synthetic data for the rest. While synthetic data is still relevant e.g. for [changing the Robotics scaling curve](https://www.youtube.com/watch?v=_2NijXqBESI), **the Data War** is now fully focused on getting *YOUR* data as model input and grader. The best bellwether for this is [LMArena](https://www.latent.space/p/lmarena)’s $100m Seed round, done a few months ago but [announced this week](https://www.bloomberg.com/news/articles/2025-05-21/lmarena-goes-from-academic-project-to-600-million-startup?taid=682e0b1550408a000117cdb5&utm_campaign=trueanthem&utm_content=business&utm_medium=social&utm_source=twitter) and raising a lot of eyebrows:

![](https://substackcdn.com/image/fetch/$s_!KF3E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65137124-5fc9-4e08-82f6-a51fc749fd07_1182x1308.png)

given recent drama with [Meta](https://news.smol.ai/issues/25-04-07-ainews-llama-4s-controversial-weekend-release) and [Cohere](https://news.smol.ai/issues/25-04-30-glazegate), though of course it is the only eval with dozens of mentions at Google I/O.

Just as Airbnb doesn’t own hotels and Uber doesn’t own cars, this is an LLM Evals, aka LLM Data, company that doesn’t employ any of the human raters it uses to derive its scores. One appeal of using LMArena beside the warm fuzzies of “giving back” is that all inference in the battles are free, presumably subsidized by every provider partner. The arrival of a16z, Felicis, and other top tier VCs means there is only one way this goes: **You will start getting paid if you are a good LMArena participant**[4](https://www.latent.space#footnote-4).

In other words, GPT wrappers will go from charging a premium on tokens, to charge + flat rate, to free, to **now we pay you to use tokens from us with good feedback**.

And if LMArena can get a $100m blessing to do this for their users… why shouldn’t you?

## Vibe Coding vs Tiny Teams

A few people have asked my opinion on the vibecoding trend. At almost every SF house party, a technical engineer or three will sheepishly admit that they’ve been vibe coding, like it’s some sort of vice. We even went ahead and [put in a Vibe Coding category in the AIE CFP](https://www.latent.space/p/aiewf-2025-cfp). But ultimately we nixed it in favor of “**Tiny Teams**”: the rising trend of small but extremely productive teams augmented by SWE Agents (not necessarily making AI products). The simplest (but hardest) statement of this is “**teams with more m in ARR than employees**”[5](https://www.latent.space#footnote-5), which is rarefied air but already reached by [@levelsio](http://x.com/levelsio)[6](https://www.latent.space#footnote-6), [Cognition](https://www.lennysnewsletter.com/p/inside-devin-scott-wu), [Bolt](https://www.latent.space/p/bolt), [Gumloop](https://x.com/MaxBrodeurUrbas) and [Gamma](https://x.com/thisisgrantlee/status/1917595403752534166).

Tiny Teams are the scaled form of first type of AI Engineer predicted in [The 1000x AI Engineer](https://www.youtube.com/watch?v=qaJXBMwUkoE&t=1s), and is the more realistic near term version of the “one person unicorn” that every thoughtleader is fantasizing about. Tiny Teams are easily profitable - most tech businesses are 60%-90% margin and most cash compensation should be <$250k - and therefore are also likely to lead to [Pegasus](https://www.linkedin.com/posts/jasoncalacanis_the-pegasus-startup-flying-over-vcs-on-the-activity-6598268156068933632-FBmF/) and other outcomes.

The way I put it to a friend recently is that **“vibe coding” is a slop attractor**, while “Tiny Teams” focuses on productivity. One might look askance at [Rick Rubin’s new book on Vibe Coding](https://x.com/AnthropicAI/status/1925926102725202163) as one such instantiation, whereas it’s pretty hard to deny that a Tiny Team (in the way we have defined it) is an unambiguously Good Thing and a direct consequence of declining end-user costs in SWE Agents.

At the end of the day, of course, have a good idea of what you are building (aka [Product Management](https://www.ai.engineer/#tracks)) is paramount, when everywhere you look an AI builder appears:

![](https://substackcdn.com/image/fetch/$s_!BBQ4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd097b24-2e97-408a-a3ca-85ecedc5f4de_1118x1166.png)

[3](https://www.latent.space#footnote-anchor-3)

note that this isn’t the only type of market that this market progression applies to… but the $3b question is: what is the next stage?

[4](https://www.latent.space#footnote-anchor-4)

This is a prediction made without any prior knowledge of LMArena plans, but we’re putting it down for posterity. Anastasios and Wei-Lin are smart guys.

[5](https://www.latent.space#footnote-anchor-5)

a lower but still impressive bar is “teams with more millions in users than employees” - means they just need to work out monetization

[6](https://www.latent.space#footnote-anchor-6)

he has [one employee](https://x.com/thesamparr/status/1547617257731153922)

"You no longer have a reason to send off every thought to the agents"

This isn't clear. Missing "not" or am I on the wrong track?

@Latent.Space How about air-gapped offerings for highly risk averse environments? The problem with all these SaaS AI tools is they require constant internet connectivity, sending sensitive code, architecture, and system context out to external servers.
