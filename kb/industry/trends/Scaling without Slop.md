---
title: Scaling without Slop
topic: industry
subtopic: trends
secondary_topics:
- product-engineering/architecture
summary: Argues for scaling AI systems without low-quality output, emphasizing engineering
  taste, workflows, and quality controls.
source: latent-space
url: https://www.latent.space/p/2026
author: Swyx
published: '2026-01-23'
fetched: '2026-07-11T05:15:26Z'
classifier: codex
taxonomy_rev: 1
words: 1563
content_sha256: b32c16dfafa304386918c31fe1698f5851bf76cb76d92a077c07eb8b12d793f2
---

# Scaling without Slop

# Scaling without Slop

### We've been quiet — announcing our 2026 plans! The State of Latent Space is here.

**First off, a few major announcements**:

- [Yi Tay returns](https://www.youtube.com/watch?v=unUeI7e-iVs&pp=2AazFNIHCQmHCgGHKiGM7w%3D%3D)to the podcast today! If you enjoyed his insights on being- [a 10,000x Yolo Researcher](https://www.latent.space/p/yitay), then you’ll love- [our catchup on Gemini’s IMO Gold](https://www.youtube.com/watch?v=unUeI7e-iVs&pp=2AazFNIHCQmHCgGHKiGM7w%3D%3D)and more.
- *Welcome to*- [the 80,000 AINews subscribers](https://news.smol.ai/)! We are doubling down on Substack, making Latent Space the one email subscription to keep up on a daily (AINews), weekly (LS Pod), and broader (LS Essays) basis. You can- [opt-in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)as needed.
- *Latent Space is also turning into a podcast network! Our first new show, focused on AI For Science, will launch next week, inspired by*- [our Chan-Zuckerberg pod](https://www.latent.space/p/biohub)! We also have a new physical space/studio at- [Kernel in SF](https://luma.com/mvgshes8)!
- [AI Engineer](https://ai.engineer/)is growing! The- [first official AIE Europe](https://www.ai.engineer/europe)is coming to London April 8-10, and both- [Super Early Bird tix](https://www.accelevents.com/e/u/checkout/ai-engineer-europe-2026/tickets/order)and- [Speaker CFPs](https://www.accelevents.com/e/ai-engineer-europe-2026/speaker-registration)first deadline is Jan 31st.
- **We are hiring**across all platforms:- [AIE Head of Operations](https://www.linkedin.com/jobs/view/4365155357/),- [AIE Marketing & Community Manager](https://www.linkedin.com/jobs/view/4365148563/),- [LS Researcher/Writer](https://docs.google.com/forms/d/e/1FAIpQLScUDOFrqXScx7JZQG9gbacpvIZggp_qCKHKzuzigNIaJruh9w/viewform?usp=dialog)(or occasional- [Guest Writer](https://docs.google.com/forms/d/e/1FAIpQLSeHQAgupNkVRgjNfMJG9d7SFTWUytdS6SNCJVkd0SMNMXHHwA/viewform?usp=dialog)!)

At every AIE conference I run, I give myself the challenge of doing the shortest keynote for a “State of the Nation” type address. For [AIE Code](https://ai.engineer/code), I declared [War on Slop](https://www.youtube.com/watch?v=IoiHI7p12Ao).

This was partially inspired by seeing the motivating factors behind products like [Codemaps](https://cognition.ai/blog/codemaps) and [Review](https://cognition.ai/blog/devin-review#the-modern-code-review-workflow), and partially a reaction to the “[Canadian Girlfriend AI Coding](https://news.ycombinator.com/item?id=46690007)” [performative productivity porn](https://x.com/levelsio/status/2013023626098852014) that took over the timeline:

![](https://substackcdn.com/image/fetch/$s_!K1vr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7eb5ed0e-8611-4579-84c5-a9f47a16078a_1196x1032.png)

[tweet](https://x.com/johnpalmer/status/2012911338276720852?s=46)

I didn’t expect Slop to then be picked up as word of the year by [Merriam-Webster](https://www.merriam-webster.com/wordplay/word-of-the-year) and [the Economist](https://www.economist.com/culture/2025/12/03/and-the-economists-word-of-the-year-for-2025-is) and the [American Dialect Society](https://americandialect.org/2025-word-of-the-year-is-slop/)[1](https://www.latent.space#footnote-1), but clearly the theme of fighting Slop is resonating as [generative AI rips the authenticity from creation](https://theoatmeal.com/comics/ai_art), piles up [open source maintainer workload](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/), fills up [academic conference submissions](https://news.ycombinator.com/item?id=46720395), taking up [20% of YouTube videos](https://x.com/dexerto/status/2006330639960694808?s=46) (earning [millions per year](https://x.com/kimmonismus/status/2006013682472669589?s=46)) and running [entire Instagram channels](https://x.com/0xgaut/status/2013684399796023760?s=46) and the [Apple App Store](https://x.com/philo01/status/2008880081456996510?s=46), slowly [deadening the Internet](https://kudmitry.com/articles/dead-internet-theory/).

There are a few gut reactions to Slop that are reasonable:

- simply reject all AI-generated content, perhaps making exception for AI-assisted, perhaps requiring - [proof of human review](https://x.com/geoffreylitt/status/2008243455810748713?s=46)
- [severely cut back on quantity](https://x.com/tbpn/status/1976042713628946446)to message and deliver quality
- [just eat the steak](https://www.youtube.com/watch?v=jrClns8kt7E)and learn to enjoy the slop machine

However, they feel variously dissatisfying in their general defeatism and pessimistic view of human taste being scalable.

First off, I’ll reiterate the obvious point that plenty of Slop has been made by humans, both well-meaning and cynical, for centuries — **AI does not have a monopoly on making Slop**. However, AI does make it easy to scale thoughtless output and it is harder to signal intent, effort and quality — an emphasis of my [recent writing retreat](https://lu.ma/dwr2025). If you creatively/skillfully wield AI as "a new brush”, then [AI Kino](https://x.com/paularambles/status/1989029622395322816?s=46) is very possible.

But more importantly, if your solution to AI slop basically means you cut back on your own human output, that doesn’t solve the fact that AI slop will continue to far outpace human output, and therefore simply overwhelm you and your community by sheer brute force and our [own recsys](https://www.youtube.com/watch?v=LxQsQ3vZDqo&list=PLcfpQ4tk2k0UMEJY1KzWu02OkvCc1e5og)’ inability to keep up with our tastes. Humanity slowly starves to death gorging on its own excrement spewed from artificial intestines.

The most important problem in media now is **scaling without slop**, period, whether or not AI generated or entirely human-origin. Actually I lied, it’s not just a media problem: any act of creation and exercise of free will is is subject to the quality-quantity tradeoff, whether you’re building a new product or texting your adult kids.

Any experienced creator will tell you that there can be very little relationship between effort and result - the thing you slaved on for a month gets overdone and incoherent, whereas the throwaway tweet of frustration done in 3 seconds gets viral and [used as an example for decades to come](https://overreacted.io/a-social-filesystem/#a-record). Sometimes -you- can’t tell what’s slop, sometimes one man’s slop is another man’s kino.

The central problem to solve is the **changing the slope of slop**, not giving up on humans.

![](https://substackcdn.com/image/fetch/$s_!3sGI!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F156f1b45-1efc-457f-a6c4-938834a5c443_2184x1064.png)

[edits welcome](https://excalidraw.com/#json=pzdirqbvTBf4xMXq7hJ0r,PVqS1ejycTPq2SVdVUW99w)

This is the problem I am working on now for both **AI Engineer** and **Latent Space**. The case studies of increasing quantity AND quality have been fascinating.

## Scaling AI Engineer

AI Engineer grew from one event a year in [2023](https://www.latent.space/p/ai-engineer) and [2024](https://www.latent.space/p/worlds-fair-2024?utm_source=publication-search) to 4 ([AIE NYC](https://www.youtube.com/watch?v=D7BzTxVVMuw&pp=2AbNUQ%3D%3D), [AIE WF](https://www.youtube.com/watch?v=z4zXicOAF28&pp=2AYR), [AIE Paris](https://www.youtube.com/watch?v=wyUdpmj9-64), [AIE CODE](https://www.youtube.com/watch?v=xmbSQz-PNMM&pp=2AbuGg%3D%3D)) in 2025, and there will be at least 7 AIEs around the world in 2026.

![](https://substackcdn.com/image/fetch/$s_!QJhJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff59b0852-1c72-425f-a53f-320783ce0d4c_1448x1852.png)

[new AIE website](https://www.ai.engineer/)

Viewership did not just 3x, but [more than 10x’ed](https://socialblade.com/youtube/handle/aidotengineer/futureprojections):

![](https://substackcdn.com/image/fetch/$s_!3A6Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7060d05-7337-47ec-b26e-4a894af83b44_3054x1300.png)

And [anecdotally](https://x.com/hesamation/status/2011159982386094482?s=46), quality has also improved:

![](https://substackcdn.com/image/fetch/$s_!2152!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff54753f8-03df-47cc-8f7c-591a26da32f1_1182x1890.png)

I remember a former 2024 speaker who is known for speaking his mind, and being privately pretty cynical about AIE, in 2025 coming back to me to say that conversations and talks felt a lot more authentic and serious this time around.

I say this not as a brag, but I think there are a lot of conscious and subconscious decisions made that contribute toward building a leading IRL and online community for serious, grounded AI discussion without resorting to fearmongering or hyperbole.

Slop has definitely crept in, but here we have kept closer to “Scaling Law X” than Scaling Law 0 and I’m happy about that.

## Scaling Latent Space

Latent Space (now joined with [AINews](https://news.smol.ai/)) has been a tougher beast. The value of media cycles often fit to [Sonal Choksi’s McClusky Curve](https://x.com/swyx/status/1556791154477244417) — flanked on the left by [TBPN](https://www.securitiesdocket.com/2025/10/13/how-tbpn-became-silicon-valleys-newest-obsession-the-new-york-times/), and on the right by [Dwarkesh](https://www.dwarkesh.com/podcast). We did AMAZING as a podcast - regularly in the 30-50th ranks of the overall US Tech podcasts in Apple, and considered by many to be a top 3 AI podcast, being featured on [the GPT5 launch](https://www.latent.space/p/gpt-5-review), and featuring conversations with [Greg Brockman](https://www.latent.space/p/gpt5-codex?utm_source=publication-search) and [Fei-Fei Li](https://www.youtube.com/watch?v=60iW8FZ7MJU) and [Mark Zuckerberg](https://www.latent.space/p/biohub?utm_source=publication-search) and [Noam Brown](https://youtu.be/ddd4xjuJTyg) and [Bret Taylor](https://youtu.be/0G1vd3Trj2U) and [Chris Lattner](https://youtu.be/04_gN-C9IAo) and [the Claude Code team](https://youtu.be/zDmW5hJPsvQ) and more household names to come.

While [our YouTube numbers](https://www.youtube.com/@latentspacepod) are still wanting (pls like and subscribe! we started YouTube way, way too late in this game), audio subscribers are still incredibly strong, and Flightcast estimates us at about 1.5m all time unique listeners now.

![](https://substackcdn.com/image/fetch/$s_!4NJQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe338905b-ae35-48aa-a8db-3659a4baafc9_1906x760.png)

But we fell behind on writing, evidenced by 2025’s [Agent Labs Thesis](https://www.latent.space/p/agent-labs) far underperforming the [AI Engineer Reading List](https://www.latent.space/p/2025-papers) (which we’ve continued to maintain, but slowly left behind as less and less frontier knowledge is published).

There’s only so much that one person can do. I am very inspired by creative networks that build a platform for multiple people to shine and contribute their talents, like [Dropout TV](https://www.avclub.com/how-dropout-broke-through-in-2025-tv-comedy) and [Morning Brew](https://www.youtube.com/@morning-brew) and [SemiAnalysis](https://semianalysis.com/). This is part of the movement that [a16z has termed New Media](https://www.a16z.news/p/meet-the-a16z-new-media-fellows), and perhaps unlike most on that list, I want to try to build a platform clearly bigger than me and hopefully bigger than the some of its parts.

The game plan for 2026’s Latent Space is threefold:

- **More shows, more hosts**: The 1-2 hour interview podcast format is cool but Alessio and I can only do so much. We’ll be doing more education (the booming area of- **AI for Science**is our next focus, with new hosts), but also entertainment (AI can be fun! and AI people are REALLY FUN). Most of our new investments will go into more YouTube and video-native formats.
- **More formats**: AINews joining Latent Space gives you a place for- [regular daily updates and commentary](https://news.smol.ai/). TBA on where the future of AI News should be beyond just a newsletter… but ideas are welcome
- **More writing:**Writing is thinking, and good thinking powers everything great we have done with Latent Space. We will double down on this and, if you’re keen to help, join us as- [a researcher or writer full time](https://docs.google.com/forms/d/e/1FAIpQLScUDOFrqXScx7JZQG9gbacpvIZggp_qCKHKzuzigNIaJruh9w/viewform?usp=dialog), or even- [apply to guest post](https://docs.google.com/forms/d/e/1FAIpQLSeHQAgupNkVRgjNfMJG9d7SFTWUytdS6SNCJVkd0SMNMXHHwA/viewform?usp=dialog)(we have always done very well serving as editors for guest posts)

## The Elements of Curation: Tuning High Taste

The common thread among AIE and LS is that we have to **curate** very well, and then scale one person’s curation to many, hopefully by crowdsourcing but also taking audience/community feedback very seriously. The most visible output of this is “**saying no a lot**”, and this is a lonely job saying no to friends and to sponsors, but even that is too broad a brush. There is no “school for curators”, no Maven or Udemy course for curating. You have to have a point of view, you have to know your audience better than they know themselves, and you have to have the freedom to make mistakes and survive making experiments with a high failure rate. Fortunately, we have enough backing and support (read: donations, partially from generous investors (who have been explicitly told we will never sell or sell out), but operating expenses actually come from Substack subscribers! thank you!) that we don’t have to couple this with any sort of business model.

We just want to Make Good Shit at Scale.

Welcome to 2026. It’s gonna be a fun ride.

[1](https://www.latent.space#footnote-anchor-1)

where it was a [runner-up last year](http://2012), and [coined 2 years ago](https://www.nytimes.com/2024/06/11/style/ai-search-slop.html) perhaps [by @deepfates](https://simonwillison.net/2024/May/8/slop/)

Echoing what I heard from some others - AINews subscribe form does not work - just tried it again - no verification link. Opt-out/opt-in does not help either.

This is great! I’ll be submitting some writing / posts for the guest writing. So much to share about AI architecture being deep in the AI-augmented SWE space in my work.
