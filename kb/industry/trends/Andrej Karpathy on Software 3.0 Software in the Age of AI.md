---
title: 'Andrej Karpathy on Software 3.0: Software in the Age of AI'
topic: industry
subtopic: trends
secondary_topics:
- agents/computer-use
summary: Karpathy Software 3.0 discussion on software in the age of AI and what changes
  for builders.
source: latent-space
url: https://www.latent.space/p/s3
author: Shawn swyx Wang
published: '2025-06-17'
fetched: '2026-07-11T05:17:21Z'
classifier: codex
taxonomy_rev: 1
words: 1569
content_sha256: 92b8b6aed5c4a1d614cfd21420886db8339fca8684bda12dba73cdeb15320ad6
---

# Andrej Karpathy on Software 3.0: Software in the Age of AI

# Andrej Karpathy on Software 3.0: Software in the Age of AI (UPDATED with Full Transcript)

### Annotated screenshots of Andrej's talk at YC AI Startup School 2025

Update: you can watch the full talk on YouTube now!

Slides are here: [https://docs.google.com/presentation/d/1sZqMAoIJDxz79cbC5ap5v9jknYH4Aa9cFFaWL8Rids4/edit?usp=sharing](https://docs.google.com/presentation/d/1sZqMAoIJDxz79cbC5ap5v9jknYH4Aa9cFFaWL8Rids4/edit?usp=sharing)

[Lots](https://x.com/search?q=karpathy%20startup%20school&src=typed_query) of people were excited about Andrej’s talk at [YC AI Startup School](https://events.ycombinator.com/ai-sus) today. Sadly, I wasn’t invited. Talks will be published “[over the next few weeks](https://x.com/karpathy/status/1935072460132811011)”, by which time the talk might be [deprecated](https://x.com/karpathy/status/1935077692258558443). Nobody seems to have recorded fancams.

But… it’s not over. You can just do things!

Using PeepResearch[™](https://x.com/swyx/status/1921992616448831754) I collated all available tweets about the talk and ordered[1](https://www.latent.space#footnote-1) them using available hints from good notetakers (credited in last slide) **UPDATE**: and now we have [the full transcript](https://www.donnamagi.com/articles/karpathy-yc-talk)! I’ll go thru most of the impt takeaways here and **subscribers can get the full slides at the bottom.**

![](https://substackcdn.com/image/fetch/$s_!6-Ej!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4feb05c2-736a-471d-adf0-bc4123b536dd_2938x1696.png)

**to annotate**

**the full talk video**when it’s up in a few weeks.

**UPDATE: Slides are now synced with the full transcript if you want to read thru**

![](https://substackcdn.com/image/fetch/$s_!2pmt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46bbef44-4ed9-4b52-983b-8fedb5a4bf76_2888x1688.png)

## Part 0: Software 3.0 - Prompts are now Programs

We first discussed Software 3.0 in ** Rise of The AI Engineer**, but it’s an obvious consequence of

[the Software 2.0 essay](https://news.ycombinator.com/item?id=34881881)+ “

[the hottest new programming language is English](https://x.com/karpathy/status/1617979122625712128)”.

![](https://substackcdn.com/image/fetch/$s_!_BDp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfb3a323-ecd1-471a-92bd-38e09c2e7ba4_2670x1596.png)

He originally wrote the Software 2.0 essay while observing that it was eating Software 1.0 at Tesla. And he’s back now to update it for Software 3.0.

In place of modifying the Software 2.0 chart like I did, Andrej debuts a new diagram showing the patchwork/coexistence of Software 1.0/2.0/3.0, noting that “**Software 3.0 is eating 1.0/2.0**” and that “**a huge amount of software will be rewritten**”:

![](https://substackcdn.com/image/fetch/$s_!5m5_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37f6dc0f-b8a8-4234-851e-75f851a0af4f_2896x1694.png)

Andrej is still focused on prompts for programs, and we [slightly disagreed back in 2023](https://x.com/karpathy/status/1674873002314563584) and still do: the “[1+2=3](https://www.latent.space/i/131896365/the-role-of-code-in-the-evolution-from-software-to-software)” variant of Software 3.0 is the entire reason why AI Engineers have far outperformed Prompt Engineers in the last few years and continue to do so.

![](https://substackcdn.com/image/fetch/$s_!Hf5V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc11ca15-3919-4b89-81b1-f5959f5dd5a2_2772x1638.png)

## Part 1: LLMs are the new computers

### LLMs are like Utilities

![](https://substackcdn.com/image/fetch/$s_!POb9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00bd8870-c055-4e3b-a392-c55153348567_2100x1166.png)

### LLMs are like Fabs

![](https://substackcdn.com/image/fetch/$s_!vXAU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff66e305a-7c95-4ea0-9376-74f16dc3f2c6_2096x1134.png)

### LLMs are like OSes

![](https://substackcdn.com/image/fetch/$s_!UhtK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38efe115-99ef-4642-8792-7b8406d486e3_1982x936.png)

![](https://substackcdn.com/image/fetch/$s_!F0Ii!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97198a48-bac3-4de9-a360-076d66c8547d_2036x1102.png)

### LLMs are like Timeshare Mainframes…

![](https://substackcdn.com/image/fetch/$s_!ASqJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe1704e-99d7-4573-9986-3b596fd8fb5c_2670x1300.png)

although as he argues in [Power to the People](https://karpathy.bearblog.dev/power-to-the-people/), LLMs also exhibit some unusual reversal of the normal flow of expensive frontier tech:

![](https://substackcdn.com/image/fetch/$s_!yu0H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb64e530a-cc3c-44c6-8393-f83fcec470cb_2020x1096.png)

As we leave the cloud for [Personal/Private AI](https://www.youtube.com/watch?v=jMoAaZP_Kkw&t=1s), some signs of Personal Computing v2 are being born in [Exolabs + Apple MLX](https://x.com/abeleinin/status/1935046342336036975/photo/1) work.

### Part 1 summary:

![](https://substackcdn.com/image/fetch/$s_!6e1-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2aa8ade-7f06-4f5b-b268-89ffdc8e97d1_2048x1152.png)

## Part 2: LLM Psychology

LLMs are “people spirits”: stochastic simulations of people, with a kind of emergent “psychology”

![](https://substackcdn.com/image/fetch/$s_!UJpg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e4dc78b-83d3-4578-a0bb-a60afcffc24a_2084x1114.png)

Andrej highlights two problems with how current LLMs simulate people:

**Jagged Intelligence (**[https://x.com/karpathy/status/1816531576228053133](https://x.com/karpathy/status/1816531576228053133))**:**

The word I came up with to describe the (strange, unintuitive) fact that state of the art LLMs can both perform extremely impressive tasks (e.g. solve complex math problems) while simultaneously struggle with some very dumb problems. E.g. example from two days ago - which number is bigger, 9.11 or 9.9? Wrong.

…


Some things work extremely well (by human standards) while some things fail catastrophically (again by human standards), and it's not always obvious which is which, though you can develop a bit of intuition over time.Different from humans, where a lot of knowledge and problem solving capabilities are all highly correlated and improve linearly all together, from birth to adulthood.Personally I think these are not fundamental issues. They demand more work across the stack, including not just scaling. T

he big one I think is the present lack of "cognitive self-knowledge", which requires more sophisticated approaches in model post-training instead of the naive "imitate human labelers and make it big" solutions that have mostly gotten us this far. For an example of what I'm talking about, see Llama 3.1 paper section on mitigating hallucinations: https://x.com/karpathy/status/1816171241809797335For now, this is something to be aware of, especially in production settings. Use LLMs for the tasks they are good at but be on a lookout for jagged edges, and keep a human in the loop.


**Anterograde Amnesia (**[https://x.com/karpathy/status/1930003172246073412](https://x.com/karpathy/status/1930003172246073412)**):**

I like to talk explain it as LLMs are a bit like a coworker with Anterograde amnesia - they don't consolidate or build long-running knowledge or expertise once training is over and all they have is short-term memory (context window). It's hard to build relationships (see: 50 First Dates) or do work (see: Memento) with this condition.

The first mitigation of this deficit that I saw is the Memory feature in ChatGPT, which feels like a primordial crappy implementation of what could be, and which led me to suggest this as a possible new paradigm of learning here:

[https://x.com/karpathy/status/1921368644069765486](https://x.com/karpathy/status/1921368644069765486)We're missing (at least one) major paradigm for LLM learning. Not sure what to call it, possibly it has a name -

system prompt learning?Pretraining is for knowledge.

Finetuning (SL/RL) is for habitual behavior.

Both of these involve a change in parameters but a lot of human learning feels more like a change in system prompt. You encounter a problem, figure something out, then "remember" something in fairly explicit terms for the next time. E.g. "It seems when I encounter this and that kind of a problem, I should try this and that kind of an approach/solution". It feels more like taking notes for yourself, i.e.

something like the "Memory" feature but not to store per-user random facts, but general/global problem solving knowledge and strategies.LLMs are quite literally like the guy in Memento, except we haven't given them their scratchpad yet. Note thatthis paradigm is also significantly more powerful and data efficient because a knowledge-guided "review" stage is a significantly higher dimensional feedback channel than a reward scaler.…

Imo this is not the kind of problem solving knowledge that should be baked into weights via Reinforcement Learning, or least not immediately/exclusively. And it certainly shouldn't come from human engineers writing system prompts by hand.

It should come from System Prompt learning, which resembles RL in the setup, with the exception of the learning algorithm (edits vs gradient descent). A large section of the LLM system prompt could be written via system prompt learning, it would look a bit like the LLM writing a book for itself on how to solve problems. If this works it would be a new/powerful learning paradigm.With a lot of details left to figure out (how do the edits work? can/should you learn the edit system? how do you gradually move knowledge from the explicit system text to habitual weights, as humans seem to do? etc.).

**Part 2 Summary:**

![](https://substackcdn.com/image/fetch/$s_!nSkP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52b60959-cb5a-42b7-9592-c7f0412c2c5c_1796x1064.png)

## Part 3: Partial Autonomy

![](https://substackcdn.com/image/fetch/$s_!ebLx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff01b5d84-6abb-4e80-a6d1-4fd2d58daef2_2028x1132.png)

We like the Iron Man Suit analogy — the suit extends us in two useful ways:

- Augmentation: giving the user strength, tools, sensors and information
- Autonomy: the suit at many times has a mind of its own- taking actions without being prompted

How can we design AI products that follow these patterns?

### Part 3a: Autonomy Sliders

The **Autonomy Slider** is an important concept that lets us choose the level of autonomy for the context, eg:

- **Cursor**: Tab -> cmd+K -> Cmd+L -> Cmd+I (agent mode)
- **Perplexity**: search -> research -> deep research
- **Tesla**Autopilot: Level 1 to Level 4

![](https://substackcdn.com/image/fetch/$s_!Vgtd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F131f6c2f-e059-4d79-a7b3-440191870891_2022x876.png)

![](https://substackcdn.com/image/fetch/$s_!c3Qu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F074e6d7d-b491-4d80-9d9d-1b6e236731e2_2034x808.png)

![](https://substackcdn.com/image/fetch/$s_!EinW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25c8935e-a7df-4b01-a660-f99871df3bd2_1146x656.png)

### Part 3b: Human-AI Generation-Verification Loop

In the Generation <-> verification cycle, we a need full workflow of partial autonomy - the faster the loop the better:

- **To improve verification**: Make it easy, fast to win
- **To improve generation**: Keep AI on tight leash

![](https://substackcdn.com/image/fetch/$s_!dg5M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d4c0207-f4e5-4a7b-b69b-7a0717b55282_2048x1536.png)

### Part 3c: The Demo-Product Gap

The reason we need PARTIAL autonomy is because of the significant gap still between a working demo and a reliable product.

He[ recounts](https://x.com/ethanniser/status/1935056628350599473) riding a Waymo prototype with zero interventions in 2014 and thinking that self-driving is “here”… but there was still a lot to work out.


"Demo is works.any(), product is works.all()"

![](https://substackcdn.com/image/fetch/$s_!Z85f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9890b449-073f-44c3-ae3c-21caa2052626_2634x1520.png)

## Part 4: Vibe Coding

The tweet that launched a thousand startups:

![](https://substackcdn.com/image/fetch/$s_!G97n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e1b7835-b594-44d1-a9cb-b5dc4329c374_2048x1536.png)

now [has its own Wikipedia page](https://en.wikipedia.org/wiki/Vibe_coding)!

However, there are still a lot of remaining issues. While [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/), he found that the AI speedups vanished shortly after getting local code running:

![](https://substackcdn.com/image/fetch/$s_!rHzD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc531c163-8e1f-4066-ab10-4cacb14ccd72_2048x1536.png)

The [reality of building web apps in 2025](https://x.com/karpathy/status/1905051558783418370) is a disjoint mess of services that are very much designed for webdev experts to keep their jobs, and not accessible to AI.

Poor old Clerk got a NEGATIVE mention, and Vercel’s @leerob a positive one, in how their docs approaches will respectively tuned for humans vs agents.

![](https://substackcdn.com/image/fetch/$s_!_wm7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09b77458-d0fe-45ce-af2a-094ce898de0b_1480x1070.png)

## Part 5: Build for Agents

**The bottom line **is that toolmakers must realize that “there is new category of consumer/manipulator of digital information”:

1. Humans (GUls)

2. Computers (APls)

**3. NEW: Agents <- computers... but human-like**

![](https://substackcdn.com/image/fetch/$s_!KUGg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd93ae423-972e-4576-8a88-ebf3a7f79b21_2048x1152.png)

Concretely: having llms.txt works because HTML is not very parseable for LLMs.

![](https://substackcdn.com/image/fetch/$s_!kXCV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccc58150-ca34-471f-abb5-6bb159ca4d53_1638x902.png)

He also shouted out “Context builders” like Gitingest and Cognition’s DeepWiki, which we profiled for a lightning pod:

## Closing / Recap

This is the Decade of Agents.

![](https://substackcdn.com/image/fetch/$s_!_oGS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b1b8a05-5dae-42d5-843e-4568ff60306f_2385x1216.png)

Less AGI 2027 and flashy demos that don’t work.

More partial autonomy, custom GUIs and autonomy sliders.

![](https://substackcdn.com/image/fetch/$s_!396e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e0d797a-0c33-41bc-83f6-89141c959468_1922x1447.png)

Remember that Software 3.0 is eating Software 1/2, that their Utility/Fabs/OS characteristics will dictate their destiny,  improve the generator-verifier loop, and **BUILD FOR AGENTS 🤖**.

![](https://substackcdn.com/image/fetch/$s_!rpf2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff72d6a56-dff2-4b7f-9b49-4d5ab842bc54_2286x1336.png)

## Full Slides for LS Subscribers

here :) link below

![](https://substackcdn.com/image/fetch/$s_!OiMo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7afc886d-0291-4798-8fd3-5d076a1c2fc0_3004x1676.png)

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
