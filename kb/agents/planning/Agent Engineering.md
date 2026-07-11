---
title: Agent Engineering
topic: agents
subtopic: planning
secondary_topics: []
summary: Defines agent engineering as a practical discipline, covering autonomy, orchestration,
  tools, and production design.
source: latent-space
url: https://www.latent.space/p/agent
author: Latent Space
published: '2025-03-24'
fetched: '2026-07-11T05:18:23Z'
classifier: codex
taxonomy_rev: 1
words: 1817
content_sha256: bf135cbcb2b181b12742f893e82d70d74a692956e9f8a3c1804afeeb0774f6f4
---

# Agent Engineering

# Agent Engineering

### Defining Agents, Why now, and why Agents are the biggest opportunity for AIEs

*This post contains elaborations on swyx’s  2025 AI Engineer Summit keynote, which also serves as a cohesive overview of a selection of Agents talks from the conference which link-clickers can preview.*

*You can find the original*

[video](https://youtu.be/5N33E9tC400)and[slides](https://docs.google.com/presentation/d/1SWoBIvTQu__uNEvSawmNcROiUx-n86O_fP0arZcTGb8/edit?usp=sharing)here.*If you enjoyed our  Claude Plays Pokemon Lightning pod,  we are doubling down with a Claude Plays Pokemon hackathon with David from Anthropic! Sign up here.*

When we first asked ourselves what we’d do differently from [Summit 2023](https://www.ai.engineer/summit/2023) and [WF 2024](https://www.ai.engineer/worldsfair/2024), the answer was a clearer focus[1](https://www.latent.space#footnote-1) on practical[2](https://www.latent.space#footnote-2) examples and techniques. After some debate, we finally decided to take “**agent engineering**” head on.

First thing in discussing agents, we have to do the simple task of **defining agents**.

![](https://substackcdn.com/image/fetch/$s_!qu6j!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67a33efa-25d8-4d4d-a19b-5f45efdac082_1464x816.png)

## Defining Agents: A Linguistic Approach

Simon Willison, [everyone’s favorite guest on LS](https://www.latent.space/p/2024-simonw) and [2023](https://www.youtube.com/watch?v=AjLVoAu-u-Q) and [2024](https://www.youtube.com/watch?v=eTTMUWP5B0s) AI Engineer keynoter, loves asking people on their agent definitions. It is an open secret that nobody agrees, and therefore debates about agent problems and frameworks are near-impossible since you can set the bar as low or as high as you want. Your choice of word is also strongly determined by your POV: Intentionally or not, **people always overemphasize where they start from** and trivialize every perspective that doesn’t.

![](https://substackcdn.com/image/fetch/$s_!U62G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f7a1818-ef7f-4ec0-8818-750768dcecb9_1064x574.png)

In fact, even within OpenAI the definitions disagree — in day 1 of the conference [OpenAI released a new working definition for the Agents SDK](https://youtu.be/joHR2pmxDQE):


An agent is an Al application consisting of


amodelequipped with

instructionsthat guide its behavior,

access totoolsthat extend its capabilities,

encapsulated in aruntimewith a dynamic lifecycle.

We’ll acronymize this as “**TRIM**”, but note what it DOESN’T say compared to OpenAI’s own [Lilian Weng](https://x.com/lilianweng/status/1673535600690102273) (now co-founder of Thinking Machines with Mira Murati) in [her post](https://lilianweng.github.io/posts/2023-06-23-agent/):


Agent = LLM + memory + planning skills + tool use

Everyone agrees on Models and Tools, but TRIM forgets **planning** and **memory**, and Lilian takes **prompts** and **runtime** orchestration for granted.

Achieving common understanding of a word is not a technical matter; but a linguistic one. And the most robust approach is **descriptive, not prescriptive**. Aka, achieving a fully spanning (maybe [MECE](https://en.wikipedia.org/wiki/MECE_principle)) understanding of how every serious party defines the word. [Simon has collected over 250 replies](https://til.simonwillison.net/twitter/collecting-replies) — so I did the last-mile of reading through all the groupings and applying human judgment…

**The Six Elements of Agent Engineering**

I’ve ranked them in rough descending order of commonality/importance:

- LLMs with - **Tools**: the thing everyone agrees on. Big 3 “LLM OS” tools are RAG (- [Contextual talk](https://youtu.be/kPL-6-9MVyA))/- [Search](https://www.latent.space/p/exa), Sandboxes/Canvas (- [OpenAI talk](https://youtu.be/1XvN5EBDnDw)) and- [Browsers](https://www.latent.space/p/browserbase)/- [CUA](https://www.latent.space/p/openai-agents-platform).- *“Agent = LLM + memory + planning skills +*—- **tool use**”- **Lilian Weng**

- Encoded - **Intent:**Intents come in via- **multimodal I/O**(eg- [Voice talk](https://youtu.be/2p2ErKRELHM)), are encoded in- **Goals**and verified via- **Evals**(- [Snake Oil](https://youtu.be/d5EltXhbcfA),- [Verifiers talk](https://www.youtube.com/watch?v=JIsgyk0Paic)) run in- **Environments**- *“An agent is a system that can pursue a goal-oriented behavior, adapt along the way to achieve its goals.”*-- **Chisom Rutherford**

- LLM-Driven - **Control Flow**: as- [Anthropic’s Agents talk](https://youtu.be/D7_ipDqhtwk)explain,- **LLMs-in-the-loop**is a common line between preset “Workflows” and autonomous “Agents”.- [3](https://www.latent.space#footnote-3)- *"The more agentic an application is, the more an LLM decides the*-- **control flow**of the application"- **Harrison Chase**

- Multi Step - **Planning:**for which the SOTA is- **editable plans**, as- [the Deep Research](https://youtu.be/eJOjdjO45Sc)- [talk](https://youtu.be/eJOjdjO45Sc)and- [Devin](https://youtu.be/T7NWjoD_OuY)/- [Manus](https://manus.im/)agents have shown are working well- *“An AI system component that performs non-trivial,*-- **multi-step**operations that previously would have required a human.”- **Daniel Miessler**

- Long Running - **Memory:**which create coherence and self-improvement loops. Beyond MemGPT/- [MCP memory](https://www.latent.space/p/why-mcp-won), we also highlight- [Voyager, SteP style reusable workflows and skill libraries](https://www.latent.space/p/why-mcp-won)as a more structured form of memory.- *“An AI system that's capable of carrying out and completing*—- **long running**, open ended tasks in the real world”- **Dan Jeffries**

- Delegated - **Authority:**Trust is the most overlooked element and yet- [the oldest](https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem). “Stutter-step agents”- [4](https://www.latent.space#footnote-4)get old fast. For read-heavy workflows you can- **Trust but Verify**(- [Brightwave talk](https://youtu.be/MWTJIAwAAnk)) but success in the- **enterprise**needs more (- [Writer talk](https://youtu.be/pPvoLjYj_mY)).- *“An agent is*” —- **trusted**to act on behalf of and in the interest of those being represented. If there’s no trust there is no agent.- **Roman Pshichenko**


When n > 3, acronyms can be helpful mnemonics, so we have selected the first letter to form **IMPACT**[5](https://www.latent.space#footnote-5).

You can FEEL when an agent forgets one of these 6 things. OpenAI’s TRIM agent framework has no emphasis on **memory, planning, or auth**, and while these can all be categorized as existing at the tool layer, they take on special roles and meaning in agent engineering and probably should have a lot more care put into them.

## Agents, Hot and Cold

We’ve tried to accurately report the general “it’s so over”/”we are so back” duality of man in the AI Eng scene over the past years.

**Spring 2023. **In [The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT](https://www.latent.space/p/agents) we tried to explain why the excitement of ChatGPT segued immediately into AutoGPT and BabyAGI (further explored with [Itamar Friedman of Codium now Qodo](https://www.latent.space/p/codium-agents?utm_source=publication-search)).


![The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT](https://substackcdn.com/image/fetch/$s_!DhMA!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79e364f2-7240-46b5-b975-829cf973f881_1996x1292.png)

**Fall 2023 - Spring 2024**. Then came the nadir of sentiment in [Why AI Agents Don't Work (yet)](https://www.latent.space/p/imbue?utm_source=publication-search) with Kanjun of Imbue, with [the first OpenAI Dev Day](https://www.latent.space/p/devday) launching custom GPTs to a flop and subsequent board crisis. The [Winds of AI Winter](https://www.latent.space/p/mar-jun-2024) lasted all the way til [David Luan asked us why Agents had become a bad word](https://www.latent.space/p/adept?utm_source=publication-search) in Silicon Valley:


#### Why Google failed to make GPT-3 + why Multimodal Agents are the path to AGI — with David Luan of Adept

![Why Google failed to make GPT-3 + why Multimodal Agents are the path to AGI — with David Luan of Adept](https://substackcdn.com/image/fetch/$s_!Mymd!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F142817627%2F8083048f-1d79-4221-a147-f0ae1d5d59d0%2Ftranscoded-1711089112.png)

**Summer 2024**. The rebound came as [Crew AI](https://www.youtube.com/watch?v=Dc99-zTMyMg&t=2s) and [LlamaIndex’s Agentic RAG](https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=2s) became the most viewed talks at[ World’s Fair](https://www.latent.space/p/worlds-fair-2024?utm_source=publication-search), our podcast on Llama 3 also introduced the first discussion of Llama 4’s focus on agents, which [Soumith teased in his talk](https://youtu.be/jMoAaZP_Kkw).


![Llama 2, 3 & 4: Synthetic Data, RLHF, Agents on the path to Open Source AGI](https://substackcdn.com/image/fetch/$s_!3Z77!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F146879553%2F98be2229-f3ec-4662-8ef7-714db586abee%2Ftranscoded-1721750543.png)

**Fall 2024**. It was Strawberry season, and with [OpenAI hiring the top Agents researchers](https://www.latent.space/p/shunyu?utm_source=publication-search) and releasing 100% reliable structured output and o1 in the API, reasoning models reignited the agent discussion in a very big way….


#### From API to AGI: Structured Outputs, OpenAI API platform and O1 Q&A — with Michelle Pokrass & OpenAI Devrel + Strawberry team

![From API to AGI: Structured Outputs, OpenAI API platform and O1 Q&A — with Michelle Pokrass & OpenAI Devrel + Strawberry team](https://substackcdn.com/image/fetch/$s_!xQ2V!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F148799668%2Fb1279f7c-e88f-4fd1-8ac0-643d677d40e3%2Ftranscoded-1726859610.png)

… if you also forgot about [Claude 3.5](https://www.latent.space/p/claude-sonnet?utm_source=publication-search), released in June and updated in Nov, which doubled Anthropic’s market share by simply being the best coding model and the model powering many SOTA agents like [Bolt](https://www.latent.space/p/bolt?utm_source=publication-search), [Lindy](https://www.latent.space/p/lindy?utm_source=publication-search), and [Windsurf](https://www.latent.space/p/windsurf?utm_source=publication-search) ([talk](https://www.youtube.com/watch?v=bVNNvWq6dKo&t=881s)):


#### The new Claude 3.5 Sonnet, Computer Use, and Building SOTA Agents — with Erik Schluntz, Anthropic

![The new Claude 3.5 Sonnet, Computer Use, and Building SOTA Agents — with Erik Schluntz, Anthropic](https://substackcdn.com/image/fetch/$s_!C_oq!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F151960189%2F588ac991-62db-47de-a8e5-36cf7a7f6077%2Ftranscoded-1732777363.png)

All of which led up to **Winter-Spring 2025**, when OpenAI shot back with its first [Operator](https://www.latent.space/p/browserbase?utm_source=publication-search) and [Deep Research](https://www.latent.space/p/gdr?utm_source=publication-search) agents and we went [All In on Agent Engineering](https://www.latent.space/p/2025-summit) for NYC.


#### The Agent Reasoning Interface: o1/o3, Claude 3, ChatGPT Canvas, Tasks, and Operator — with Karina Nguyen of OpenAI

![The Agent Reasoning Interface: o1/o3, Claude 3, ChatGPT Canvas, Tasks, and Operator — with Karina Nguyen of OpenAI](https://substackcdn.com/image/fetch/$s_!BEvf!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F155459121%2F7a907b81-3f57-46a3-bbab-f74dca6cedfa%2Ftranscoded-1738374183.png)

In fact, you can track ChatGPT’s growth numbers closely to model releases ([as I did](https://www.youtube.com/watch?v=5N33E9tC400)) and it is clear that the reacceleration of ChatGPT is all due to [reasoning/agent work](https://youtu.be/5N33E9tC400):

![](https://substackcdn.com/image/fetch/$s_!FjAB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8f76158-7889-49f1-898d-94f94fb5e9e9_1710x1046.png)

However, we think this chronology tracking model progress and general sentiment swings isn’t even a complete account of the agent resurgence, which is still on-trend for those paying attention to broad benchmarks.

![](https://substackcdn.com/image/fetch/$s_!5aiV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbc0287f-a878-42cb-8db2-f84104470413_1132x805.png)

[from m-ric of smolagents](https://huggingface.co/posts/m-ric/116861695030454)(our

[lightning pod with him](https://www.youtube.com/watch?v=QytYcjTkkQU&list=PLWEAb1SXhjlc5qgVK4NgehdCzMYCwZtiB&index=12&t=344s&pp=iAQB)). the agent horizon varies depending on reliability cutoff, but METR says

[it doubles every 3-7 months](https://x.com/swyx/status/1902541093943832864)

![](https://substackcdn.com/image/fetch/$s_!7py1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85a33d1a-7b04-4117-bd49-b5e36707d249_1399x767.png)

## Why work on Agent Engineering Now?

- **Obvious Catalysts**: the more dramatic stuff that is a must-know- **Better Models**: reasoning of course, also more coding, MMLU/GPQA
- **Better Tool Use**:- [100% structured output](https://www.latent.space/p/openai-api-and-o1?utm_source=publication-search)and- [BFCLv3](https://www.latent.space/p/lmarena?utm_source=publication-search)/IFEval
- **Better Tools**: improvements in the Big 3 tools and- [MCP winning](https://www.latent.space/p/why-mcp-won)the long tail

- **Slow-burn Trends**: broader arcs that drive order-of-magnitude updates- **Business Model Shifts**:- [$2-20k ChatGPT](https://www.latent.space/p/chatgpt-max)and- [Sierra](https://www.latent.space/p/bret)charging for outcomes
- **1000x Moore’s Law**: Reasoning models are following- [GPT4’s cost drop curve](https://www.latent.space/p/reasoning-price-war)
- **>100x inference**:- [Speculative Editing](https://www.latent.space/p/inference-fast-and-slow)& ASICs leading us to- [5000 tok/s](https://www.latent.space/p/together)
- **Model Diversity**: multiple labs taking share, including- [xAI/TML](https://buttondown.com/ainews/archive/ainews-xai-grok-3-and-mira-muratis-thinking/), enabling…
- **Multi-agent Research**: from- [OpenAI’s](https://www.youtube.com/watch?v=joHR2pmxDQE&list=PLcfpQ4tk2k0VGHcZxjSoAe_r5VbdHXmjy)to- [Pydantic](https://www.latent.space/p/pydantic)to- [Crew AI](https://www.youtube.com/watch?v=Dc99-zTMyMg&t=2s)is improving
- **RL Finetuning**:- [Will Brown did a great talk](https://www.youtube.com/watch?v=JIsgyk0Paic)on this, but we’ll have more soon.


This is why there’s a new resurgence in agents and the field of Agent Engineering is just now becoming the hottest thing in AI Engineering.

## Full talk here

See me speed thru [my slides on YouTube and leave a comment](https://youtu.be/5N33E9tC400) on what else you see!

[1](https://www.latent.space#footnote-anchor-1)

Saying no to a lot of interesting directions in AI - focusing in on just one of the tracks we had last year but making a deep exploration of one topic rather than going wide

![](https://substackcdn.com/image/fetch/$s_!rbAB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b505392-0346-46af-b036-bf17baad4c41_692x348.png)

[2](https://www.latent.space#footnote-anchor-2)

No direct vendor pitches; a draconian rule inspired by [dbt’s Coalesce conference](https://coalesce.getdbt.com/). This feels harsh because of course some of the people most qualified to talk about a problem also sell a solution for it; this meant we had to actively solicit talks outside the CFP process from people who would not normally apply to speak, like [Bloomberg](https://youtu.be/b2GqTDWtg6s) and [LinkedIn](https://youtu.be/n9rjuBuShko) and [Jane Street](https://youtu.be/0ML7ZLMdcl4), and the only way for a vendor to get on our stage is to also bring a customer to talk about their real lived experiences, like [Method Financial/OpenPipe](https://youtu.be/zM9RYqCcioM) and [Pfizer/Neo4j](https://youtu.be/OpVkWc3YnFc) and [Booking.com/Sourcegraph](https://youtu.be/UXOLprPvr-0).

[3](https://www.latent.space#footnote-anchor-3)

[Rahul’s (Ramp’s) talk](https://www.youtube.com/watch?v=-rsTkYgnNzM) also frames the choice as a form of [Bitter Lesson](https://x.com/swyx/status/1902454997427904865) - workflows get you far in the short term, but often get steamrolled by the next order of magnitude gain in intelligence or cost/intelligence.

[4](https://www.latent.space#footnote-anchor-4)

Agents that ask for confirmation before every single external action - many real agents ([like Windsurf](https://youtu.be/bVNNvWq6dKo)) have had to figure out clever ways of exempting actions from human approval in order for the agent to have meaningful autonomy.

[5](https://www.latent.space#footnote-anchor-5)

“write agents with IMPACT!” too hokey? I like it because M, P, A, C, and T came naturally already, so the only armtwisty one was “Intent”, because I didn’t want to limit it to OpenAI TRIM’s “Instructions” alone — the combination of Instructions and Evals felt better to guide agent behavior in the same way that [the generator-verifier gap](https://x.com/swyx/status/1867995447878672723) works at the model level.

I'm coming from the future. These milestones were hit but due to context management issues the quality wasn't what we hoped.

I enjoy hearing how those working in this space define an “AI agent”. I recently published my thoughts here, and they align fairly closely with the above definition: https://open.substack.com/pub/matthewdionis/p/the-rise-of-true-ai-agents
