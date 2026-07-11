---
title: It's Time To Build AI | UX
topic: product-engineering
subtopic: ux-patterns
secondary_topics: []
summary: Short essay arguing that AI UX is a primary product surface and should be
  designed as deliberately as model prompts.
source: latent-space
url: https://www.latent.space/p/build-ai-ux
author: Latent Space; Maggie Appleton; Linus Lee; Geoffrey Litt
published: '2023-04-26'
fetched: '2026-07-11T05:23:24Z'
classifier: codex
taxonomy_rev: 1
words: 903
content_sha256: 155722ac4c1e40b781efc21b2ee1e6d7985f53cb0eba02d89db6e997df7f9609
---

# It's Time To Build AI | UX

# It's Time To Build AI | UX

### Bridging the Capability Overhang from Generative AI to Generative UI

In early April, a [conversation](https://twitter.com/Mappletons/status/1642538016739655681) between swyx and [Maggie](https://twitter.com/mappletons) (and later [Geoffrey](https://twitter.com/geoffreylitt/) and [Linus](https://twitter.com/thesephist)) snowballed into a SF meetup centered around our joint interests as UX people crossing over into AI. The original plan was for 15-30 people, then Ivan Zhao [graciously offered](https://twitter.com/swyx/status/1646212086224265216) Notion HQ[1](https://www.latent.space#footnote-1) to host 80 people, and [interest](https://partiful.com/e/Dfw3sbzb8JjDqzaO6FzE) bloomed into almost 400 signups with unfortunately more people on waitlist than we could accommodate. We put out a [Call For Demos](https://twitter.com/swyx/status/1625579361536716800), [68 people submitted](https://docs.google.com/spreadsheets/d/1zEvVwZJ5u1eM9Nu-SjRDNpsrX2LIYPYGnZaVfEg9qr0/edit#gid=0), and [16 presented live](https://www.youtube.com/watch?v=JdwpVKKrL2o).

But this isn’t just a meetup recap blogpost.

**It is a call to arms.**

We are no stranger to [manifesting meetups](https://www.swyx.io/manifest-meetups), but even by SF standards the event was a smashing success, with [many great UX people](https://twitter.com/swyx/status/1648856081605730305) all in one room. We aren’t surprised; we think the potential in and demand for novel AI UX interaction is enormous:

- OpenAI staff - [often comment](https://twitter.com/BorisMPower/status/1625431580243116033)on how ChatGPT is primarily a “UX innovation” that made existing capability accessible, just nobody “jumped on the opportunity”
- Linus has ranted about how - [Most knowledge work isn't a text-generation task](https://twitter.com/thesephist/status/1592925458924195840), the- [sorry state of PromptOps Tools](https://twitter.com/thesephist/status/1630387644545789953)and- [prompt engineering](https://twitter.com/thesephist/status/1569957540292608000), and that- [text is the lowest denominator, not endgame](https://twitter.com/thesephist/status/1639067500200570881).
- Maggie, - [co-organizer of Future of Coding London](https://twitter.com/Mappletons/status/1527952928950173696), and champion of- [End User Programming by developers](https://twitter.com/Mappletons/status/1561357946960990213)for truly personal computing (e.g.- [programming portals](https://twitter.com/Mappletons/status/1584239896520056833)), also warns about- [Generative AI and the Expanding Dark Forest](https://twitter.com/Mappletons/status/1610214373338845185).
- Geoffrey, ever a champion of - [Malleable Software](https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming.html), and in particular- [spreadsheets over text](https://twitter.com/geoffreylitt/status/1587159378804834305), has reminded people that- [Chat will never feel like driving a car](https://twitter.com/geoffreylitt/status/1640110619746529280).
- swyx likes smol ideas that stick in big brains. And making people go “ooh!”

We think what Nat Friedman calls the [AI capabilities overhang](https://twitter.com/natfriedman/status/1636769905671544832?lang=en) is in part due to people not exploring the “*latent space”* of AI UX (including Generative UIs, many of which were explored in the demos featured below).

As Linus said in his [opening comments](https://youtubetranscript.com/?v=JdwpVKKrL2o&t=153):


“I spent a lot of time exploring different kind of interfaces for highlighting and structuring and helping people navigate text and one of my key takeaways from that year was thatwe have to go beyond just staring at walls of text and prompting.”

We fundamentally believe that the ultimate potential for LLMs is not merely to build “ChatGPT for your docs” (though that is great and needed too!). To do that, we must break out of the textbox, but also **create spaces to share** new UX paradigms and concepts with each other, both online and IRL, in a lightweight fashion that encourages collaboration, inspiration, and friendly competition rather than fundraising.

If you too, believe that there is a better world waiting for us on the other side of the border box, ping us to help.

xoxo,

Your fellow AI | UX enjoyers

![](https://substackcdn.com/image/fetch/$s_!x0zZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad174617-2b6f-43ce-910d-81713d1ab94f_2658x1984.png)

*PS:  If you are in 🗽 NYC - the first AI | UX will be hosted by  Paul Butler on May 17 - register/share it here! *

*To start events  in your city,  come coordinate on our Discord.*

## Full Meetup Video

**Timestamps and individual submitted demos **

- **6:15**: Mindmapping Canvas, with Chat- [Alex Brinsmead](https://twitter.com/AlexBrinsmead)-- [MindPilot](https://www.loom.com/share/916cb741875043fb815bf23ac62b4a4a)
- **9:34**: 3D editor with Stable Diffusion Img2Depth- [Alvin Ghouas](https://twitter.com/alvinghouas)-- [ProductStudio](https://www.youtube.com/watch?v=QuQUCxJc0lc)
- **12:40**: Beautiful writing app with affordances for feeling, inspirations, suggestions, summaries, and praise!- [Amelia Wattenberger](https://twitter.com/Wattenberger)-- [PenPal](https://twitter.com/Wattenberger/status/1645434961825255425?s=20)- I'm really curious to see how we can move beyond generating text. Prompts are basically pieces of context - what if we could prompt text like we prompt MidJourney? … Once you have primitives, let users customize it!
- **19:00**: Zero in on what you need to know, with resources suggested- [Apoorva Srinivasan](https://twitter.com/apoorvasriniva)-- [Personalized Generative Learning Graph](https://www.loom.com/share/eb4ea5c702e44a909eb9f06e536813f6)
- **22:00**: Editing a spreadsheet in Potluck with natural language, falling back to direct manipulation- [Geoffrey Litt](https://twitter.com/geoffreylitt/)-- [AI in Potluck - a Computational Medium](https://share.cleanshot.com/56p4ct8K)
- **29:25**: GANBreeder/ArtBreeder mapped with a Leap Motion Controller- [Gray Crawford](https://twitter.com/graycrawford)-- [Mapping Image Generation to Movement](https://www.dropbox.com/s/x4izjoifl7bmusk/gray.m4v?dl=0)
- (long dinner break)
- **1:11:42**: for Level 4 Syntopical Reading, Proactive Search, Omnidirectional Linking- [Jeremy Nixon](https://twitter.com/JvNixon)-- [Omni](https://twitter.com/JvNixon/status/1589395568534913026)
- **1:19:40**: Projectional Editor for Text, Tone Switching Palette for Text (inspired by FigJam), Zoom Previews for Text- [Kabir Goel](https://twitter.com/KabirGoel)-- [3 demos](https://www.loom.com/share/b970c846313d4944aeec0044fec5a862)
- **1:24:40**: a Calmer Twitter Client (- [Kasra Kyanzadeh](https://twitter.com/kasrak)-- [Feedpaper](https://twitter.com/kasrak/status/1648797613280591873)- [open source](https://github.com/kasrak/feedpaper))
- **1:29:00**: AI-native CMS: Ingest any Markdown and expose as a Chat component- [Marie and Michael Fester](https://twitter.com/michaelfester)-- [MarkPrompt](https://share.cleanshot.com/1Z2Br7Ls)
- **1:35:20**: Animate by choosing from options each time- [Mary Rose Cook](https://twitter.com/maryrosecook)-- [LLM Augmented Animation](https://www.youtube.com/watch?v=k1PwIpgSMtw)
- **1:40:24**: Point at website elements and decide what you want them to look like. "It'd be cool to program by pointing at things instead of typing them."- [Max Krieger](https://twitter.com/maxkriegers)-- [Seemixer](https://youtu.be/iuyC6muzO3c)
- **1:45:00**: Programming Tutor that prompts you to think critically as you solve problems- [Miguel Acevedo](https://twitter.com/miguelace_)-- [OpenCode](https://www.youtube.com/watch?v=ARxHuT1q_bk)
- **1:50:20**: Programming like Factorio!- [Paul Shen](https://twitter.com/_paulshen)-- [LLMs as Function Blocks](https://www.youtube.com/watch?v=V0O3C80z81s)
- **1:57:50**: With prompts on your notes taken- [Rob Haisfield](https://twitter.com/RobertHaisfield)-- [AI Zettelkasten](https://www.loom.com/share/f89ba0553b5947c8bf1027f0a1ac9e21)
- **2:02:19**: Making ephemeral UI with filterable/sortable/tables, ffmpeg, and video controls- [Sean Grove](https://twitter.com/sgrove)-- [Generative UI ChatGPT Plugin](https://www.youtube.com/watch?v=xgi1YX6HQBw)

[1](https://www.latent.space#footnote-anchor-1)

With special thanks to **Emily** at Notion HQ for going out of her way to be an incredible venue host helping us with food, A/V and even post-meetup recordings (*with timestamps!*). Notion seem to not mind at all that I once “[reverse prompt engineered Notion AI](https://www.latent.space/p/reverse-prompt-eng)”.

Would be so good to get an updated article on this topic given there is more movement here now e.g. v0, Figma, replit and so many more.
