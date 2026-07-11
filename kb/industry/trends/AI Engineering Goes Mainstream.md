---
title: AI Engineering Goes Mainstream
topic: industry
subtopic: trends
secondary_topics:
- agents/planning
summary: Summarizes AI engineering becoming mainstream, with emphasis on agent engineering
  and applied AI system practices.
source: latent-space
url: https://www.latent.space/p/aiewf-2025-keynotes
author: Latent Space
published: '2025-06-13'
fetched: '2026-07-11T05:17:25Z'
classifier: codex
taxonomy_rev: 1
words: 2559
content_sha256: 3e4e8c961b65f1f0dab9985f3e2a3fc92a0c4958fcfe84269781c57235a17224
---

# AI Engineering Goes Mainstream

# AI Engineering Goes Mainstream

### AI Engineer World's Fair 2025 Recap — Recapping as much as we can, with exclusive infographic summaries from our friends at Thoth.ai!

When I wrote about [the Rise of the AI Engineer](https://www.latent.space/p/ai-engineer) almost 2 years ago, I noted that it would feel “inferior” to the ML Engineer and AI Researcher for a long time. Now we see Andrew Ng writing up the “[GenAI Application Engineer](https://www.deeplearning.ai/the-batch/issue-305/)”, Hamel coining “[AI Scientist](https://x.com/HamelHusain/status/1913655324655096316)”, and even [Greg Brockman](https://x.com/swyx/status/1930439481754300570) (upcoming guest!) explaining how engineers can have the same impact as researchers at the World’s Fair.

There’s no playbook for “setting up a new sub-industry” — it’s a mix of [devrel/ community building](https://www.swyx.io/big-l-notation#lpn2---the-learninpublic-grand-slam), [economics/industrial organization](https://en.wikipedia.org/wiki/Industrial_organization), and [anthropology+set theory](https://x.com/swyx/status/1933596321526788576). We started by building out one of the [leading newsletters](https://github.com/swyxio/ai-notes/blob/main/Resources/Good%20AI%20Podcasts%20and%20Newsletters.md), then podcasts, surveys[1](https://www.latent.space#footnote-1), where we cover everything from [mental models](https://www.latent.space/p/dec-2023-audio) to [trend charts](https://www.latent.space/p/reasoning-price-war) to [coding tools](https://www.latent.space/p/token-data-war) to [paper syllabi](https://www.latent.space/p/2025-papers) to [daily news](https://news.smol.ai/), anything AI Engineers need, right down to [the job description](https://www.latent.space/p/hiring). But perhaps the highest signal, most intentional thing we do to move the industry forward is organize the AIE conferences.

It’s an odd feeling to run a large industry conference: on one hand, we’ve spent months planning every minute of the event and playing 300D calendar tetris, and on the other we’re so busy running the show that we don’t actually see much of it. And afterward we’ve still got postproduction[2](https://www.latent.space#footnote-2) and sponsor needs to handle that it’s hard to write an authoritative overview that is still timely. So here’s one person’s best-efforts overview, but *you shouldn’t miss the OTHER recaps from others linked below*.

![](https://substackcdn.com/image/fetch/$s_!aSCK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F644b89fa-10bb-4da0-bce0-c23255eca809_2244x1526.png)

[google photos album](https://photos.google.com/share/AF1QipMjlcuNBaKKcMxnUd6ylVeLzI7crRFEecxisR26wn4iJUun79oyg4-lvg45AHyb5g?key=bzRpSXBoblZGMUNRV1lKcWJTekI5V2N2V19GOHFn)

## Highest Level Highlights

**Final count**: **3,098** (20% C-level, 17% management, 22% principal/staff eng, 17% senior eng) from a nice split of company sizes (1/3 >1k employees, 1/3 <50) AI engineers, including [306 speakers](https://www.ai.engineer/#speakers) over 30 workshops + 10 tracks each for 2 days (not to forget: our [69 online speakers](https://www.youtube.com/watch?v=J3oJqan2Gv8&list=PLcfpQ4tk2k0Vu8ZKg_5TzN87mRhRJt71Y)) and [30(!!!) independent events](https://www.ai.engineer/#events) across the city.

**Special thanks **to our community, from [Laurie Voss](https://twitter.com/laurie_voss), our incredible emcee, to all track hosts — [Henry Mao](http://x.com/calclavia) (MCP), [Brittany Walker](https://x.com/brittwalker_) (Tiny Teams), [Eugene Yan](http://x.com/eugeneyan) (RecSys), Neo4J and [Stephen Chin](https://twitter.com/steveonjava) (GraphRAG), [Ankur Duggal](https://www.linkedin.com/in/ankurduggal/) (AI in Fortune 500 1), [Alessio Fanelli](http://x.com/fanahova) (Architect 1), PromptQL and [Alex Reibman](https://x.com/AlexReibman) (Agent Reliability), [Seenia Hong](https://x.com/seeniahong) (AI PM), [Ishan Dhanani](https://x.com/0xishand) (AI Infra), [Thor Schaeff](https://x.com/thorwebdev) (Voice), [Vibhu Sapra](https://x.com/vibhuuuus) (SWE-Agents), OpenPipe and [Kyle Corbitt](https://x.com/corbtt) (Reasoning+RL), [Dat Ngo](https://x.com/dat_attacked) (Retrieval+Search), Braintrust and [Olmo Maldonado](https://x.com/ibolmo) (Evals), [Randall Hunt](https://x.com/jrhunt) (AI in Fortune 500 2), [Matt Redmond](https://x.com/mttrdmnd) via Bryan Bischof (Architects 2), [Allie Howe](https://x.com/vtahowe) (Security), [Alexis Gauba](https://x.com/alexisgauba) (AI Design Eng), [Jaril Valenciano](https://x.com/notjaril) (Gen. Media), and [Era Qian](https://x.com/eraqian) (Autonomy+Robotics, especially bringing in [KScale](https://www.kscale.dev/) and [Tesla Optimus](https://x.com/eraqian/status/1929770223361839482)), interviewers [Phlo Young](https://x.com/YoungPhlo_/status/1930243924825911576), [Sarah](https://x.com/SarahChieng)/[Tyler](https://x.com/tyler_fong_), Jensen wrangler [Nader Khalil](https://x.com/swyx/status/1930644246517928123) and everyone who volunteered and helped others where we simply couldn’t (team credits in [livestream](https://www.youtube.com/live/U-fMsbY-kHY?si=0kIFf8vmkhIQiXDH&t=32500)). It was truly the “Avengers Assemble” of AI Eng.

**Launches** both on stage and by sponsors during AIEWF week (NON-EXHAUSTIVE!):

- **Gemini 2.5 Pro (06-05)**launched onstage by- [Logan Kilpatrick](https://x.com/OfficialLoganK/status/1930657743251349854)’s keynote (with roadmap for- **Gemini Code, Deep Research API, and Computer Use API)**
- **OpenAI Agents TypeScript SDK**- [launched](https://x.com/OpenAIDevs/status/1929950012160790876)by Dominik Kundel for his workshop
- **OpenAI Agent Robustness Team**- [announced](http://agent robustness https://x.com/gdb/status/1930831992171749773)by Fouad Matin, Security keynote
- **Anthropic MCP Request for Startups**- [offered by](https://x.com/opentools_/status/1930368990968459432)Theodora Chu, MCP PM
- **Anthropic Claude Code Plan Mode**- [with Boris Cherny](https://www.youtube.com/live/U-fMsbY-kHY?si=_onXlDuAwdqyTI8m&t=19746), Claude Code creator
- **Dagger’s**- [container-use](https://github.com/dagger/container-use)launched onstage by- [Solomon Hykes](https://x.com/roblyu/status/1931070879980749017)’ keynote
- **Morph Liquid Metal and Magi-1 model**launched onstage- [by Jesse Han](https://www.youtube.com/live/U-fMsbY-kHY?si=fKUbfLeAt54L4wq_&t=5272)and hiring Christian Szegedy as “- [one of the highest aura announcements ever](https://x.com/willccbb/status/1930759464518599004)”
- **Verified Superintelligence**by Morph’s- [Christian Szegedy](https://www.youtube.com/live/-9E9_21tx04?si=OoOcwoVX_M8nLeQW&t=12545), announced as- [Trinity](https://x.com/morph_labs/status/1933181394588483868)
- **AI Diplomacy**launched- [onstage by Alex Duffy](https://every.to/diplomacy)—- [best speaker](https://x.com/swyx/status/1931552069984608486)for Tiny Teams
- **ElevenLabs**launched their- [v3 alpha](https://x.com/elevenlabsio/status/1930689774278570003)with- [Thor Schaeff](https://x.com/thorwebdev/status/1931128508279107837)— track host for Voice
- **LlamaIndex’s**- [LlamaCloud Excel Support](https://youtu.be/jVGCulhBRZI?si=XyHV___0gbniF1oK&t=512)
- **ARC-AGI 3**previewed- [onstage by Greg Kamradt](https://x.com/arcprize/status/1932137879742063073), President ARC Foundation
- **Huxe AI**- [launched](https://x.com/raizamrtn/status/1930655918800388359)by- [former guest](https://www.latent.space/p/notebooklm)Raiza Martin, AI Product Mgmt keynote
- **Exa Research**- [launched](https://x.com/ExaAILabs/status/1930691085476745605)from- [former guest](http://latent.space/p/exa)Will Bryk —- [best speaker](https://x.com/swyx/status/1931552069984608486)in Search
- [Traversal AI](https://www.traversal.com/)
- **Modal’s**- [LLM Almanac](https://modal.com/llm-almanac/advisor)- [launched](https://x.com/charles_irl/status/1929615080494416213)by upcoming guest Charles Frye
- **HackAPrompt AIE**- [launched](https://www.hackaprompt.com/track/aiengineer)by- [former guest](https://www.latent.space/p/learn-prompting?utm_source=publication-search)Sander Schulhoff
- **Simon Willison’s PelicanBench**ELO rankings on- [his blog](https://simonwillison.net/2025/Jun/6/six-months-in-llms/)
- *let*- [@swyx](https://x.com/swyx)know if we missed some big launch

## Bonus Post AIEWF Lightning Pod with Alex Duffy (Best Speaker, Tiny Teams) on AI Diplomacy

## Links to Your Reflections, Takeaways

Apart from all the posts in [the AI Engineering community](https://x.com/i/communities/1929211810798043448) and [tags of @aidotengineer](https://x.com/search?q=%22%40aidotengineer%22%20-from%3Aaidotengineer&src=typed_query&f=live), these are the bigger reflections/recap posts we know of:

- **swyx**:- [AIEWF Day 1 on TBPN](https://x.com/search?q=from%3Atbpn%20swyx&src=typed_query&f=live)
- **swyx**:- [AIEWF Day 2 on ThursdAI](https://x.com/altryne/status/1930717886747959620)
- **Turing Post**:- [Holy Shit moments vs Not There Yet](https://x.com/TheTuringPost/status/1933857238395064548)(- [video](https://www.youtube.com/watch?v=XbwwpfYPVWk))
- **Simon Willison:**- [The last six months in LLMs, illustrated by pelicans on bicycles](https://simonwillison.net/2025/Jun/6/six-months-in-llms/)
- **Lance Martin**:- [The state of AI agents](https://x.com/RLanceMartin/status/1932855783718576153)
- **Charlie Guo**:- [The State of AI Engineering (2025)](https://www.ignorance.ai/p/the-state-of-ai-engineering-2025)
- **Danny Thompson**:- [How Tiny Teams Built $10M Startups in Months](https://www.listennotes.com/podcasts/the-programming/inside-the-ai-engineer-QxtpSivcndC/)
- **Mickey Bazeley**:- [AIE x MongoDB reflections on Multi-Agent Systems](https://x.com/BazeleyMikiko/status/1931067784517312784)
- **Anita Kirkovska**(- [guest author](https://www.latent.space/p/anita-tdd?utm_source=publication-search)):- [What’s shaping AI products, agents, and infrastructure in 2025](https://www.vellum.ai/blog/top-takeaways-from-the-ai-engineer-worlds-fair#3-vibe-coding-shapes-whats-ahead)
- **Patrick Ellis:**- [The startup playbook is being rewritten in real-time](https://www.geekwire.com/2025/takeaways-from-the-ai-engineer-worlds-fair-the-startup-playbook-is-being-rewritten-in-real-time/)
- **Derek Sheerin**:- [Reflections on the AI Engineering World Fair 2025](https://www.aussiebytes.com/thoughts-on-the-ai-engineering-world-fair-2025-reflections-and-future-considerations/)
- **Lena Hall**:- [FOMO track from AIEWF](https://www.youtube.com/watch?v=Xavr7WlbYSA)
- **Short takes**:- [Alex Volkov](https://x.com/altryne/status/1931387685014585688),- [Yogi Miraje](https://x.com/yogi_miraje/status/1931540035125608698),- [Danny Thompson](https://x.com/DThompsonDev/status/1931385166603194729),- [Eugene Yan](https://x.com/eugeneyan/status/1931475698696565010),- [Balazs Nemethi](https://x.com/nembal/status/1931790354627575887)

## Mainstage Keynote Recaps

As AIEWF is basically “18 conferences in one”, and many speakers would be keynoters in any other conference, there’s too much to cover by any one person, but we do have plenary stages for stuff that doesn’t quite fit into any one theme.

Because the [Day 1](https://www.youtube.com/watch?v=z4zXicOAF28) and [Day 2](https://www.youtube.com/watch?v=U-fMsbY-kHY) livestreams are already up, we’ll focus on them for now and break out selected takeaways later, illustrated by [our friends from Thoth AI](https://libraries.thoth.art/aiewf2025/), returning to AIEWF for the second time!

## Asha Sharma — Spark to System: Building the Open Agentic Web

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!SHVk!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6320e157-d532-43d5-8aca-e1977868cf75_3360x2520.png)

[full transcript](https://libraries.thoth.art/aiewf2025/talk/spark-to-system-building-the-open-agentic-web)on Thoth!

In a tightly polished set of demos, Microsoft sees the next leg of AIE in 3 themes:

- from - **pair → peer**programming: GitHub Copilot can be @assigned and GraphRAG on your codebase and even autonomously do MLE with- [Project Amelie](https://theaieconomy.substack.com/p/microsofts-project-amelie-introduced-build-2025)
- from - **software → agent**factory: every company should have a platform (aka “AI Foundry”) that can help churn out agents with the- [full set of LLM OS](https://news.smol.ai/issues/25-05-27-mistral-agents)tools: model routing, security, reliability, agentic RAG, MCP tools, observability… and even voice posts, imagegen, and posting directly to LinkedIn!
- from - **cloud → local**AI: running open models on device with- [Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started)

*swyx’s note: we are very sorry that the 3rd demo ran overtime just as the demos were heating up in the youtube chat; we’ll try to make it up on a full pod.*

## Sarah Guo — The State of Startups & AI 2025

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!Ptng!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86ffbb5c-6db0-4151-953f-a1d22670502a_3360x2520.png)

[full transcript](https://libraries.thoth.art/aiewf2025/talk/conviction-session)on Thoth!

The top lesson from the last 2.5 years since founding Conviction:

“

I have never seen the uptake from users that has been possiblein the last couple years… AI engineering is quite a bit harder than people had hoped, but the value creation is massive.We see companies going from 0 to 100m in run rate faster than we’ve ever seen in any technology revolution before.”

How to build Cursor for X:

- **Reasoning is the new vector for scaling**
- **Agents, agents, agents**: less of chatbots, more like a colleague
- **Multimodality**isn’t niche: both Video and Voice will sweep the economy
- Sam Altman: “ - **Last year’s model is a commodity**”
- **Code is the first AI Killer App**because it’s structured text with deterministic validation, on the path to AGI, and most imptly engineers can build for themselves.

She abstracts this to a recipe for building Thick AI Wrappers ([we approve](https://www.latent.space/p/gpt-wrappers)) and that startups that do this in every vertical and profession can leapfrog incumbents — if they have good execution and don’t rest on a launch. See their [Requests for Startups](https://www.conviction.com/startups.html).

## Simon Willison — The last six months in LLMs, illustrated by pelicans on bicycles

Best recapped on [his website](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) and [Hacker News](https://news.ycombinator.com/item?id=44215352):

![](https://substackcdn.com/image/fetch/$s_!8Iv3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb997cfd-92ef-43a4-b78a-6457f0acf2cf_2098x1518.png)

The big trends:

- **30 significant model releases in last 6 months**: Nova is cheap, DeepSeek was great, Mistral Small was a great competitor to Llama 3.3, Claude 3.7 → GPT 4.5 → o1-pro → Gemini 2.5 Pro → GPT 4.1 → Claude 4. 4o imagegen was very special
- **Bugs**:- [4o sycophancy](https://www.latent.space/p/clippy-v-anton),- [Grok’s issues](https://www.theatlantic.com/technology/archive/2025/05/elon-musk-grok-white-genocide/682817/),- [Claude 4’s snitching](https://github.com/t3dotgg/SnitchBench)was a big deal
- **MCP = Tools+Reasoning**: “I think this is the most powerful technique in AI Engineering right now”
- **Security: The Lethal Trifecta**: when models have 1) access to private data, 2) exposure to malicious instructions, 3) exfiltration vectors

This was our first year handing out [Best Speaker awards](https://x.com/swyx/status/1931552069984608486) to spark the competitive spirit in our speakers, and Simon handily won the overall AIE Best Speaker trophy with his mix of humor and technically relevant insight.

![](https://substackcdn.com/image/fetch/$s_!q9Zn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25bec7b2-573d-49f6-9c1d-9563d818025c_2130x1506.png)

## Antje Barth — Building Agents at Cloud-Scale

![Image Image](https://substackcdn.com/image/fetch/$s_!2RYe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb637c6a4-0c09-4662-a599-8d323acc8a7e_1680x1260.jpeg)

Antje teased the coming [Alexa+Claude](https://www.anthropic.com/news/claude-and-alexa-plus) integration, discussed how Amazon Q Developer (also [presented by Vikash Agrawal from the team](https://www.youtube.com/watch?v=utxVvGJ4bcg)) was built in 2 weeks, with [Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) (name picked by AI!) that is basically a form of Agent-specific AWS SDK that has a [surprisingly complete](https://x.com/swyx/status/1932329014380917220) set of agent capabilities supported.

![](https://substackcdn.com/image/fetch/$s_!cteJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04c07938-e75b-43bc-a284-e7bbbaef1bba_2110x1506.png)

## Kevin Hou — Windsurf everywhere, doing everything, all at once

![Image Image](https://substackcdn.com/image/fetch/$s_!Z4A1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd676b2db-ed76-4f98-978f-9ae97d8a185d_1680x1260.jpeg)

**Software Engineering != Coding. **Returning for [his 3rd time at AIE](https://www.youtube.com/@aiDotEngineer/search?query=kevin%20hou), Kevin revealed the “secret sauce” of Windsurf is progressively abstracting the inner and then outer loop of software engineering with AI, and then modeling the “meta-learning” that engineers do, right up to using their **data flywheel (ship → feedback → improve)** to build their SWE-1 model for both handling tasks **end-to-end** (only asking humans for review and approval) and for **conversational**, human-in-the-loop tasks.

![](https://substackcdn.com/image/fetch/$s_!CPKM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c1b8d11-6405-48a1-be22-b62e99029694_2080x1488.png)

## Greg Brockman - #define AI Engineer

We will probably defer a full breakdown of this to Greg’s podcast but [this](https://x.com/vitrupo/status/1930683787094184165) was the most popular clip from our chat (with a [special cameo from Jensen Huang](https://x.com/swyx/status/1930644246517928123)):

![](https://substackcdn.com/image/fetch/$s_!HbB1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F906a8554-cae0-4cb4-bdcb-5ba092a2b51c_604x816.png)

## Logan Kilpatrick — A year of Gemini progress + what comes next

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!tOOs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa27b839a-6a12-4590-9f0d-9ed1087b046b_1680x1260.png)

[full talk transcript](https://libraries.thoth.art/aiewf2025/talk/a-year-of-gemini-progress-what-comes-next)on Thoth!

Logan knew how to please the crowd by starting “[Google Day](https://x.com/OfficialLoganK/status/1930695546848845904)” with the final Gemini 2.5 Pro preview launch onstage, but perhaps the real alpha came at the end discussing the GDM roadmap - our read is that Veo 3 is likely to be merged into mainline Gemini, more Gemma models will be released, new architecture work for infinite context is underway, and that still-not-shipped Gemini Ultra is still on the table.

![](https://substackcdn.com/image/fetch/$s_!1si6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F562f9444-2ac9-44d9-a932-1d1a6f7ffc38_1952x1570.png)

He is increasingly pushing the thesis that [models are becoming agents out of the box](http://AI models are becoming agents out of the box) which is informing the work that is being done by the API team, which also shared the roadmap including new announcements for **Gemini Code, Deep Research API, and Computer Use API.**

![](https://substackcdn.com/image/fetch/$s_!ttwg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59e2e58e-c3e2-4c68-a344-31a1f0e2c058_3706x2420.png)

## Jack Rae — Thinking Deeper in Gemini

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!VDZN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbad975f6-b84d-401c-8f0c-ee3daf539123_1680x1260.png)

[full transcript](https://libraries.thoth.art/aiewf2025/talk/thinking-deeper-in-gemini)on Thoth!

Jack presented this keynote for the reasoning team at Gemini just [before departing for Meta’s new Superintelligence division with Alexandr Wang](https://news.smol.ai/issues/25-06-11-execuhires-2). When [Flash Thinking](https://news.smol.ai/issues?pattern=flash%2520thinking&filterTags=true&filterDesc=true) first emerged it seemed an unusual terminology for what everyone else was calling “inference time compute”. But it seems clearer that their definition of thinking is more than just raw chain of thought quantity ([17x higher (!!!) than 2.0 Flash as Artificial Analysis observes](https://x.com/ArtificialAnlys/status/1920497711352328557)), but also on efficiency and reasoning from a small set of axioms. New science will be invented only after we can cleanly recreate old research.

![](https://substackcdn.com/image/fetch/$s_!hXPS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F767774a1-85d5-40bb-b5d7-abb90b358d34_3300x1622.png)

## Solomon Hykes — Containing Agent Chaos

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!zNmR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60d0f218-3447-4728-9866-c45c9447a57d_3360x2520.png)

[full transcript](https://libraries.thoth.art/aiewf2025/talk/containing-agent-chaos)on Thoth!

In one of the most talked-about launches of the conference, Solomon Hykes retook to the same stage he launched DockerCon to **open source** [container-use](https://github.com/dagger/container-use), Dagger’s answer for containerized environments for every agent (something that until now has been constrained to [custom orchestration](https://www.latent.space/p/modal)/[Firecracker in the cloud](http://latent.space/p/e2b), or non-sandboxed [git worktrees](https://x.com/_mohansolo/status/1920190769857769935) in local dev. If you [run parallel Claude Code instances](https://x.com/blader/status/1933276781043462421), this is the way.

![](https://substackcdn.com/image/fetch/$s_!7ExJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F239e0261-1578-4f3f-b7ef-8efa787f6a5b_1194x1066.png)

[Greg](https://x.com/gregce10/status/1930672793219379312)! (nyc speaker returning!)

## Jesse Han — The Infrastructure for the Singularity

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!KIv-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a127ab6-ba48-4699-bd57-58875876a1ef_1680x1260.png)

[full talk transcript](https://libraries.thoth.art/aiewf2025/talk/the-infrastructure-for-the-singularity)on Thoth!

Jesse Han, as a former member of the GPT4 team, took a much more philosophical view, arguing that we want to cater to the machine’s fundamental desires and work backward from there. Yes they want sandboxing, but we also want superlative cloud infrastructure to match the needs of the superintelligence. He announced **Morph Liquid Metal and Magi-1 model, **as well as hiring Christian Szegedy as Chief Scientist as “[one of the highest aura employment announcements ever](https://x.com/willccbb/status/1930759464518599004)”.

## George Cameron — Trends Across the AI Frontier

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!z7Io!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76148f7c-b4eb-45c0-9258-7a24f84f34cf_3360x2520.png)

[full transcript](https://libraries.thoth.art/aiewf2025/talk/trends-across-the-ai-frontier)in Thoth!

With Micah absent due to all-too-familiar visa issues, George delivered with Artificial Analysis’ trademark polish, an overview of all the big trends. The “money” slide was an unexpected rerendition of [Wirth’s Law (aka Gates’ Law)](https://www.swyx.io/eponymous-laws) - what distillation/ inference/hardware people giveth, bigmodel/reasoning/agents people taketh.

![](https://substackcdn.com/image/fetch/$s_!3Ex3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a37b4a7-b69a-4029-94ae-84dbf650684c_2104x1510.png)

## Barr Yaron — State of AI Engineering 2025

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!D1tD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6eb0cfb0-0cfa-4a9e-b94e-6920c2992065_3360x2520.png)

[https://libraries.thoth.art/aiewf2025/talk/state-of-ai-engineering-2025](https://libraries.thoth.art/aiewf2025/talk/state-of-ai-engineering-2025)

This is the second official AIE survey done with Barr/Amplify. As mentioned we’ll discuss this when the full survey results are published, but a fun chart was Barr being able to quantify the gap between Text and other modalities. This is probably the last year that Voice AI trails behind Image gen.

![](https://substackcdn.com/image/fetch/$s_!4V2m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc386e7e-7322-4fcf-a602-5ff18cc1d29c_2124x1544.png)

## Alex Atallah — fun stories from building OpenRouter and where all this is going

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!d0C3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cf07070-4eb4-420e-a4f5-acb28b38e82b_1680x1260.png)

[https://libraries.thoth.art/aiewf2025/talk/fun-stories-from-building-openrouter-and-where-all-this-is-going](https://libraries.thoth.art/aiewf2025/talk/fun-stories-from-building-openrouter-and-where-all-this-is-going)

[OpenRouter is Andrej’s new candidate for top tier eval](https://x.com/karpathy/status/1917546757929722115), and we were delighted to have Alex join AIE to tell the OpenRouter story for the first time. We think [LLM Gateways are a very fundamental component of the AI Engineering stack](https://www.latent.space/p/gateway), and OpenRouter is objectively one of the biggest in production LLM gateways right now, and grows in importance as relevant model lab diversity increases (not at all a consensus opinion when OpenRouter started). Alex outlined the future of “**Inference-Native Middleware**” as a input -*and output*- transform complement to MCPs.

![](https://substackcdn.com/image/fetch/$s_!ZCfy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1edfbf3c-1683-4d44-87bc-2169fe7990ff_2106x1486.png)

## Sean Grove — The New Code

![Expanded View Expanded View](https://substackcdn.com/image/fetch/$s_!UGff!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3ba9f5b-f54e-49bd-8a2a-81d62f4079bb_3362x2520.png)

[https://libraries.thoth.art/aiewf2025/talk/prompt-engineering-is-dead-everything-is-a-spec](https://libraries.thoth.art/aiewf2025/talk/prompt-engineering-is-dead-everything-is-a-spec)

The last conference Ben organized pre AI Engineer ended with [Sean, Ben, and myself](https://www.youtube.com/watch?v=35nC0AtdlJE), so it seems weirdly fitting that AIEWF 2025 ends with the AI versions of us. Sean now works on Alignment Research at OpenAI, advocating for why things like the [OpenAI Model Spec](https://openai.com/index/introducing-the-model-spec/) are underrated and in fact needed, directly addressing the [4o sycophancy issue](https://www.latent.space/p/clippy-v-anton), and arguing that the best coder is actually just going to be the best communicator (and well structured communication, like having a spec, is the best approach both to alignment and for creating anything with AI).

![](https://substackcdn.com/image/fetch/$s_!bbaX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7053290-eb0b-4125-80e5-2108fd90435a_2118x1506.png)

There’s more recaps to do, particularly with the bigger tracks of the conference and the major launches, but we’ll just get this out now just to ship in a timely fashion.

To give the speakers their due credit, please skim the timelines of:

Day 1:

and Day 2:

for the full story!

[1](https://www.latent.space#footnote-anchor-1)

full survey shipping soon! thanks for taking part - You can see preliminary results in Barr’s presentation at the [end of Day 2](https://www.youtube.com/watch?v=U-fMsbY-kHY). We also had a brief attempt at a foundation and there may be another crack at that someday.

[2](https://www.latent.space#footnote-anchor-2)

Other than the [8 livestreams](https://x.com/swyx/status/1931559851769160183) + [the online track](https://www.latent.space/p/aiewf-2025), we will edit and post up all talk videos in weeks, not months

https://danafharbaugh.substack.com/p/disco-ball-warfare

How AI helped a lost Veteran find healing and launch a groundbreaking new business.
