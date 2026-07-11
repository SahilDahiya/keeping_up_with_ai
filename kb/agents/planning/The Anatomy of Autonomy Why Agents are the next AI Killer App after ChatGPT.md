---
title: 'The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT'
topic: agents
subtopic: planning
secondary_topics:
- industry/trends
summary: Explains why agents became a major AI application pattern after ChatGPT and
  what autonomy changes in product design.
source: latent-space
url: https://www.latent.space/p/agents
author: Latent Space
published: '2023-04-19'
fetched: '2026-07-11T05:23:28Z'
classifier: codex
taxonomy_rev: 1
words: 3168
content_sha256: 955f20784e96210d6c94061c4c74785a96c0a7dee25a964daf150bd2b5e4dc46
---

# The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT

# The Anatomy of Autonomy: Why Agents are the next AI Killer App after ChatGPT

### Auto-GPT/BabyAGI Executive Summary, a Brief History of Autonomous Agentic AI, and Predictions for Autonomous Future

*Welcome to the 12k new listeners who checked out  the Segment Anything pod!*

*We’ve launched a  new community page with our upcoming events in SF, NY and Miami (this Friday)! See you if you’re in town!*

*Discussions happening on  Hacker News and Twitter.*

“GPTs are General Purpose Technologies”[1](https://www.latent.space#footnote-1), but every GPT needs a killer app. Personal Computing needed VisiCalc, the smartphone brought us Uber, Instagram, Pokemon Go and iMessage/WhatsApp, and mRNA research enabled rapid production of the Covid vaccine[2](https://www.latent.space#footnote-2).

One of the strongest indicators that the post GPT-3 AI wave is more than “just hype” is that the killer apps are already evident, each >$100m opportunities:

- **Generative Text for writing**- Jasper AI going 0 to $75m ARR in 2 years
- **Generative Art for non-artists**- Midjourney/Stable Diffusion- [Multiverses](https://www.latent.space/p/multiverse-not-metaverse?utm_source=%2Fsearch%2Fmultiverse&utm_medium=reader2)
- **Copilot for knowledge workers**- both GitHub’s- [Copilot X](https://twitter.com/swyx/status/1638550858073006089)and “- [Copilot for X](https://www.latent.space/p/what-building-copilot-for-x-really)”
- **Conversational AI UX**-- [ChatGPT](https://lspace.swyx.io/p/everything-we-know-about-chatgpt)/ Bing Chat, with a long tail of Doc QA startups

I write all this as necessary context to imply:

The fifth killer app is here, and it is **Autonomous Agents**.

![](https://substackcdn.com/image/fetch/$s_!D80L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a68add7-01a3-4d2d-a050-edeeeae66ddd_1996x1292.png)

But first, as usual, let’s start with an executive summary to catch up those out of the loop.

## Auto-GPT Executive Summary

[Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT/tree/master/autogpt) (and its younger sibling [BabyAGI](https://github.com/yoheinakajima/babyagi)) are independently developed Python projects, open sourced March [30th](https://fortune.com/2023/04/15/babyagi-autogpt-openai-gpt-4-autonomous-assistant-agi/) and [April 2nd](https://github.com/yoheinakajima/babyagi/graphs/contributors) respectively, which have caught enormous popularity, with Auto-GPT [trending #1 on Twitter and GitHub](https://twitter.com/SigGravitas/status/1646117442031349761?s=20) in the past 2 weeks ([far outpacing every other open source AI project](https://star-history.com/#Significant-Gravitas/Auto-GPT&CompVis/stable-diffusion&facebookresearch/segment-anything&hwchase17/langchain&Date) including [Segment-Anything](https://www.latent.space/p/segment-anything-roboflow#details), Stable Diffusion, and the now Sequoia-crowned [$200m-valuation-LangChain](https://web.archive.org/web/20230414032253/https://www.businessinsider.com/sequoia-leads-funding-round-generative-artificial-intelligence-startup-langchain-2023-4?r=US&IR=T)).

Both projects do * not* involve foundation model training or indeed any deep ML innovation; rather they demonstrate viability of applying

*existing*LLM APIs (GPT3, 4, or any of the alternatives) and reasoning/tool selection prompt patterns

**in an infinite loop,**to do potentially

**indefinitely long-running**, iterative work to

**accomplish a high level goal**set by a human user.

We do mean “high level” — [Toran Richards](https://www.linkedin.com/in/toran-bruce-richards-54139814b/?originalSubdomain=uk)’ [original demo](https://github.com/Significant-Gravitas/Auto-GPT/commit/c74ad984cfa755031a85296c45a8a8d77e0b8906?short_path=b335630#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5) for Auto-GPT was “*an AI designed to autonomously develop and run businesses with the sole goal of increasing your net worth*”, while Yohei Nakajima coded up [Jackson Fall’s viral HustleGPT prompt on ChatGPT](https://twitter.com/jacksonfall/status/1636107218859745286) and told it to *“ start and grow a mobile AI startup”*. In the 2 weeks since, community members have

[built extensions](https://twitter.com/SullyOmarr/status/1646632867412459521)and

[clones](https://twitter.com/_Lonis_/status/1646641412182536196)and

[agent managers](https://twitter.com/thegarrettscott/status/1645918390413066240)and

[frameworks](https://twitter.com/dysmemic/status/1645535982996054016)and

[ChatGPT plugins](https://twitter.com/skirano/status/1646582731629887503)and

[visual toolkits](https://twitter.com/wm_eddie/status/1646752950541492225)and so on, with usecases in

[market research](https://twitter.com/SullyOmarr/status/1645205292756418562),

[test driven development](https://twitter.com/adamcohenhillel/status/1644836492294905856), and

[scientific literature review](https://twitter.com/eimenhmdt/status/1644199933321306112).

Beyond those similarities, the projects are very different in their approaches.

- BabyAGI is intentionally small, - [adding and stripping out LangChain](https://twitter.com/yoheinakajima/status/1644326587389853697?s=20), with its initial code being- [less than 150 lines](https://replit.com/@YoheiNakajima/babyagi?v=1#main.py)and- [10 env vars](https://github.com/yoheinakajima/babyagi/blob/17f1e830e44d83f8b6d52e3b932ba26a98e702a0/.env.example#L8)(it is now ~800LOC).![](https://substackcdn.com/image/fetch/$s_!RD5d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d77b77f-dc06-4458-a61e-0059dc9c688f_1508x1096.png) - GPT4 visualizing the codebase. - [Other attempts](https://github.com/yoheinakajima/babyagi/pull/207).
- While Auto-GPT is - **more expansive**(7300 LOC), with the ability to clone GitHub repos, start other agents,- [speak](https://twitter.com/SigGravitas/status/1641649430230351872?s=20), send tweets, and generate images, with- [50 env vars](https://github.com/Significant-Gravitas/Auto-GPT/blob/ecf2ba12db11ff19bce359b842f810f0e2d09d6a/.env.template)to support every vector database and LLM provider/Text to Image model/Browser.![Image Image](https://substackcdn.com/image/fetch/$s_!zCgM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F728f39f3-9bf1-4e75-bdfe-cb0ea2f7acbb_1200x1716.jpeg) - [full list from source](https://github.com/Significant-Gravitas/Auto-GPT/blob/ecf2ba12db11ff19bce359b842f810f0e2d09d6a/autogpt/prompt.py#L47)

The projects have caught the imagination of leading AI figures as well, with Andrej Karpathy calling AutoGPTs the “[next frontier of prompt engineering](https://twitter.com/karpathy/status/1642598890573819905?s=20)” and Eliezer Yudkowsky [approvingly observing](https://twitter.com/ESYudkowsky/status/1640511156254289926) BabyAGI’s refusal to turn the world into paperclips even when prompted.

## A Brief History of Autonomous AI

In my understanding of neurobiology, [every convolution](https://blogs.scientificamerican.com/talking-back/einsteins-brain-more-special-than-we-ever-knew/) that wrinkles the brain a bit more makes us a little smarter. In a similar way, AI progresses by “convolutions”, and in retrospect our path to the present day has been obvious. I’d like to map it out:

![](https://substackcdn.com/image/fetch/$s_!cf67!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5eeaff61-b705-42c5-8d52-24f9a12d9c32_1996x1292.png)

**Key Autonomy Capabilities arranged in rough chronological order**

- **Foundation models**:- Everything starts with the evolution - *and*widespread availability of massive LLMs (via API or Open Source). The sheer size of these models finally allow for- [3 major features](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1):- ~perfect natural language understanding and generation
- world knowledge ( - [175B Parameters can store 320GB](https://arxiv.org/pdf/2301.00774.pdf), which is 15 Wikipedia’s)
- [emergence](https://www.jasonwei.net/blog/emergence)of major capabilities like- **in-context learning**

- This leads to the rise of the early prompt engineers, like - [Gwern Branwern](https://gwern.net/gpt-3)and- [Riley Goodside](https://twitter.com/goodside/status/1569128808308957185)who explored creative single-shot prompts.

- Capability 1: Metacognition (self improvement of pure reasoning) - [Kojima et al (2022)](https://arxiv.org/abs/2205.11916)found that simply adding “- [let’s think step by step](https://twitter.com/shaneguML/status/1530244895713046528)” to a prompt- *dramatically*raised the performance of GPT3 on benchmarks, later found to be effective due to externalizing the working memory for harder tasks.
- [Wei et al (2022)](https://arxiv.org/abs/2201.11903)formalized the technique of Chain of Thought prompting that further improved benchmark performance.
- [Wang et al (2022)](https://learnprompting.org/docs/intermediate/self_consistency)found that taking a majority vote of multiple Chains of Thought worked even where regular CoT was found to be ineffective.
- More and more techniques like - [Calibrate Before Use](https://arxiv.org/pdf/2102.09690.pdf),- [Self-Asking](https://ofir.io/self-ask.pdf),- [Recursively Criticize and Improve](https://twitter.com/johnjnay/status/1641786389267185664),- [Automatic Prompt Engineering](https://sites.google.com/view/automatic-prompt-engineer), appear.


- **Capability 2: External Memory**(reading from mostly static external data)- The capability of in-context/few shot learning could be used to cheaply update a foundation model beyond its’ knowledge cutoff date and focus attention on domain specific, private data
- The constraints of limited context length lead to the need for embedding, chunking and chaining frameworks like LangChain, and vector databases like - [Pinecone (now worth $700m), Weaviate ($200m), and Chroma ($75m)](https://archive.is/wCoqH).
- Another way of using natural language to access and answer questions form relational databases are the Text to SQL companies, which included Perplexity AI ( - [$26m Series A](https://techcrunch.com/2023/04/04/ai-powered-search-engine-perplexity-ai-lands-26m-launches-ios-app/)), Seek AI (- [$7.5m Seed](https://lspace.swyx.io/p/sarah-nagy#details)), and a long tail of other approaches including- [CensusGPT](http://censusgpt.com/)and- [OSS Insight](https://ossinsight.io/explore/).


- **Capability 3: Browser Automation**(sandboxed read-- **and-write**in a browser)- Sharif Shameem (an upcoming guest! more on a future pod) first demoed - [GPT-3 automating Chrome to buy Airpods](https://twitter.com/sharifshameem/status/1645664932418162688)in 2021.
- [Adept raised a Series A](https://www.businesswire.com/news/home/20220426005963/en/AI-Transformer-Inventors-Launch-Adept-with-65M-to-Lend-a-Hand-to-Knowledge-Workers)with an all-star team of Transformer paper authors and launching the- [ACT-1 Action Transformer](https://www.adept.ai/blog/act-1)(now with a- [hefty $350m Series B](https://www.forbes.com/sites/kenrickcai/2023/03/14/adept-ai-startup-raises-350-million-series-b/?sh=7c29c7672cc3)despite the departure of Vaswani et al)
- [Nat Friedman’s NatBot](https://twitter.com/natfriedman/status/1575631194032549888)brought browser automation back into the zeitgeist a year later, showing how an agent can make a restaurant reservation across google search and maps from a single natural language instruction.
- [Dust XP1](https://dust.tt/xp1)was also released but was read-only, did not do any automation.- [MULTI·ON](https://multion.ai/)went that extra mile and is now also in- [the ChatGPT Plugin Store](https://twitter.com/DivGarg9/status/1648074780430696448).
- A nice variant of browser agents are desktop agents - - [Embra AI](https://embra.app/)seem to be the most hyped here (though still pre launch), and- [Rewind AI](https://twitter.com/RewindAI)could be next.
- It would seem that - [Multi-modal GPT4](https://www.latent.space/p/multimodal-gpt4)’s visual capability would be able to greatly enable the desktop agents here, especially where no accessibility text or DOM is available.


- **Capability 4: Tool making and Tool use**(server-side, hooked up to everything)- **Search.**Generated answers from memorized world knowledge, or retrieved and stuff into context from a database, will never be as up to date as just searching the web. OpenAI opened this can of worms with- [WebGPT](https://openai.com/blog/webgpt/), showing their solution to crawling the web, summarizing content, and answering with references (now live in ChatGPT Plugins and in Bing Chat, but replicated in the wild with- [Dust](https://twitter.com/dust4ai/status/1587104029712203778)and- [others](https://www.notion.so/44485e5c97bd403ba4e1c2d5197af71d)).
- **Writing Code to be Run**. We knew that GPT-3 could write code, but it took a certain kind of brave soul like- [Riley Goodside to ask it to generate code](https://twitter.com/goodside/status/1568448128495534081)for known bad capabilities (like math) and to- *run*the code that was generated.- [Replit turned out](https://twitter.com/amasad/status/1568825727528878081)to be the perfect hosting platform for this style of capability augmentation (- [another example here](https://twitter.com/sergeykarayev/status/1569377881440276481)).
- **ReAct**.- [Yao et all (2022)](https://arxiv.org/abs/2210.03629)coined- [the ReAct pattern](https://react-lm.github.io/)which introduced a- [delightfully simple](https://til.simonwillison.net/llms/python-react-pattern)prompt template for enabling LLMs to make reliable tool choices for- **Rea**soning +- **Act**ing given a set of tools.- [Schick et al (2023)](https://arxiv.org/abs/2302.04761)introduced the Toolformer that specifically trained a model with special tokens, but this does not seem as popular.
- **Multi-model Approaches.**Models calling other models with capabilities they didn’t have were also being explored, with- [HuggingGPT/Microsoft JARVIS](https://github.com/microsoft/JARVIS)and- [VisualChatGPT](https://github.com/microsoft/visual-chatgpt/tree/main).
- **Self-Learning**.- [Self-Learning Agent for Performing APIs](https://twitter.com/DYtweetshere/status/1631349179934203904)(SLAPA) searches for API documentation to teach itself HOW to use tools, not just WHEN. This approach was adapted for the OpenAPI (fka Swagger) spec for ChatGPT Plugins, which- [also used natural language](https://twitter.com/mitchellh/status/1638966754226610181?lang=en).
- Other semi-stealth mode startups that may be worth exploring in this zone are - [Fixie AI](https://fixie.ai/)and Alex- [Minion AI](https://minion.ai/).
 - At this point it is worth calling out that we have pretty much reached the full vision laid out by - [this excellent post from John McDonnell](https://jmcdonnell.substack.com/p/the-near-future-of-ai-is-action-driven)6 months ago:

![https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1560f3c6-b6c3-48d0-be93-4560f3290dd7_1544x1512.png https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1560f3c6-b6c3-48d0-be93-4560f3290dd7_1544x1512.png](https://substackcdn.com/image/fetch/$s_!z814!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1560f3c6-b6c3-48d0-be93-4560f3290dd7_1544x1512.png)

So what net new thing are we seeing in this most recent capability spurt?

I think the clue is in the 4 agents that naturally evolved in BabyAGI (scroll up for diagram):

- The “ - **context agent**” (Capability 1 + 2) could be a much smarter version of the data augmented retrieval that both- [LlamaIndex](https://twitter.com/jerryjliu0/status/1647626532519841793)and- [Langchain](https://blog.langchain.dev/retrieval/)are working on. Yohei added the need for “- [relevant (task) context](https://twitter.com/yoheinakajima/status/1644326588794941440?s=20)” which may be slightly different than the classic semantic similarity algorithms offered by the vector databases.- **Active learning**may see a return to favor as autonomous “context agents” actively surface things they don’t know for prioritization

- The “ - **execution agent**” calls OpenAI, or any other- **foundation model**, and could optionally make or use any provided tools to accomplish a task (Capability 3 + 4)
- The “ - **task creation agent**”, well, creates tasks, but must not hallucinate and must self criticize and learn from previous tasks (Capability 1 + 2). Challenging, but not outside the bounds of- [simple common sense benchmarks](https://www.latent.space/p/benchmarks-101#details).
- And the last agent is the “ - **prioritization agent**”. Ah! A new task!

That leads us to identify…

- **Capability 5: Planning, reflexion, and prioritization**- [Shinn et al (2023)](https://nanothoughts.substack.com/p/reflecting-on-reflexion)showed that Reflexion - an autonomous agent with dynamic memory and self-reflection, could dramatically improve on GPT-4 benchmarks.
- [Shoggoth the Coder](https://twitter.com/atroyn/status/1645957559298449408)won the recent ChatGPT Plugins Hackathon as an independent agent capable of proposing and submitting PR fixes to open source projects.
- [Meta’s Simulacra paper](https://arxiv.org/abs/2304.03442)showed the entertaining potential of autonomous NPC agents interacting with each other in a game-like setting.
- Regardless of use case, autonomous agents will be expected to plan further and further ahead, prioritizing task lists, reflecting on mistakes and keeping all relevant context in memory. - [The “Sparks of AGI” paper](https://arxiv.org/pdf/2303.12712)specifically called planning out as a notable weakness of GPT-4, meaning we will likely need further foundation model advancement before this is reliable.
- The recent - [LangChain Agents webinar](https://twitter.com/jh_damm/status/1646233661832929280?s=20)discussion also highlighted the need for the ability to stack agents and coordinate between them.
- In the - [Latent Space Community](https://www.latent.space/p/community), AI virtual software developer platform- [e2b](https://github.com/e2b-dev/e2b)is already discussing the potential of having fleets of AI developer workers.


## Why Autonomous AI is the Holy Grail

**What makes software valuable to humanity? **In both my investing and career advice, I am fond of encouraging people to develop a “**theory of value of software**”.[3](https://www.latent.space#footnote-3)

One of the clearest value drivers[4](https://www.latent.space#footnote-4) of software is automation. The one currency we all never have enough of is **time**, and the ability to obsolete human effort, whether by clever system design, hiring someone else, or programming a machine, both frees up our time and increases our ability to scale up our output by just doing more in parallel. In fact this can be regarded as a core definition of technology and civilization:

“Civilization advances by extending the number of operations we can perform without thinking about them” — Alfred North Whitehead.


The relationship betwen **automation** and **autonomy** is subtle but important:

- ChatGPT doesn’t do anything without your input, but once you punch the right prompts in, it can do an awful lot of research for you, especially - [with Plugins](https://www.latent.space/p/chatgpt-plugins#details)
- AutoGPTs by default require you to enter a goal and hit “yes” to approve each step it takes, but that is incrementally easier than having to write responses
- AutoGPTs also have limited ( - *run for N steps*) and unlimited (- *run forever)*“- [continuous modes](https://github.com/Significant-Gravitas/Auto-GPT#-continuous-mode-%EF%B8%8F)” which are fully autonomous but very likely to go wrong and therefore have to be closely monitored

We’ve just explained that technological and civilization advance requires us to be able to do things *without thinking about them*, so clearly full autonomy with as much trust and reliability as possible is the ultimate goal here. Let a thousand agents bloom! AI Assistants is where most people start, but Josh Browder is working on [AI Lawyer](https://twitter.com/jbrowder1/status/1612312707398795264), Replika is working on [AI Waifu](https://www.youtube.com/watch?v=SFKA7T-v6WE), I want AI Junior Developers and AI Video and Podcast and Newsletter Editors, Karpathy wants us to keep going with the [AI C-Suite](https://twitter.com/karpathy/status/1642610417779490816?s=20).

Fortunately, we don’t have to reason out every step of this progression from first principles, because [the Society of Automotive Engineers](https://sae.org/) established a shorthand for this almost a decade ago:

![The Rise of Autonomous Vehicles: Pros & Cons of Self-Driving Cars | Study The Rise of Autonomous Vehicles: Pros & Cons of Self-Driving Cars | Study](https://substackcdn.com/image/fetch/$s_!izVZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3751512-e1f9-4397-98c5-a62ae4e2e14e_984x924.png)

[the 5 levels of autonomy](https://www.steinlaw.com/resources/studies/the-rise-of-autonomous-vehicles/)

I’ll assume you are familiar with some of the self driving car discourse[5](https://www.latent.space#footnote-5), but it's time to understand that self-driving AI agents in 2023 are just about where self-driving cars were in ~2015. We are beginning to have some intelligence in the things we use, like Copilot and Gmail autocompletes, but it's very lightweight and our metaphorical hands are always at ten and two.

In the next decade, we'll want to hand over some steering, then monitoring, then fallback to AI, and that will probably map our progress with autonomous AI agents as well.

Edit from May 2023: we found out from our upcoming podcast guest Itamar Friedman of Codium that they had already done some thinking on [6 levels of Autonomous Code Integrity](https://www.codium.ai/blog/the-6-levels-of-autonomous-unit-testing-explained/). Check them out!

In the following decade, we’ll develop enough trust in our agents that we go from a many-humans-per-AI paradigm down to one-human-per-AI and on to many-AIs-per-human, following an accelerated version of the industrialization of computing from the 1960s to the 2010s since it is easier to iterate on and manipulate bits over atoms.

There will be two flavors, or schools of thought, on autonomous AI:

- The Jobs School: AI Agents that augment your agency, as “ - [bicycles for your mind](https://www.themarginalian.org/2011/12/21/steve-jobs-bicycle-for-the-mind-1990/)”
- The Zuck School: AI Algorithms that replace your agency, hijacking your mind

We’ll want to try our best to guide our efforts to the former, but we won’t always succeed.

## Related Reads

- LangChain’s take on - [Autonomous Agents](https://blog.langchain.dev/agents-round/)

## Misc Observations I couldn’t put anywhere

I will perhaps expand these in future, or not, but happy to discuss each in comments.

- Despite needing prompt templates, tool selection, memory storage and retrieval, and orchestration of agents, - [neither Babyagi nor AutoGPT use LangChain](https://twitter.com/swyx/status/1648539094438273024). EDIT:- [LangChain’s docs](https://python.langchain.com/en/latest/use_cases/autonomous_agents.html)now have some implementations.
- The new FM “Bitter Lesson” - Every time we try to finetune foundation models to do a certain task, software engineers can write abstractions on top to do it less efficiently but faster. - ReAct/SLAPA > Toolformer/Adept ACT-1
- there’s families of transformers and alternative architectures (H3, fwd-fwd algo) but nobody can name any that have stuck

- Academic research of deep reinforcement learning for agents seems trapped in games? - MineDojo, Deepmind DreamerV3, GenerallyIntelligent - [Avalon](https://youtu.be/g0muj39vCCY)
- CICERO diplomacy is notable because did NOT use deep RL?

- Semantic search has been less of a killer product. why?
- Backend GPT has not led anywhere. why?
- “wen AI Agents” easier to discuss than “wen AGI”
- all the open source winners are new to open source lol? is “open source experience” that valuable?
- Why do people all use pinecone to store like 10 things in memory
- Safety - no more AGI off switch with autonomous agents - AGI Moloch means have fun staying poor = have fun staying safe
- we’re calling for the wrong kinds of pause: - pause on fleets of workers until we have extremely well developed constitutions and observability?


- Predictions - there will be “AI Agent platforms” - with tools all enabled → Zapier and fixie well placed

- there will be “AI Agent fleets” - especially if “idempotent”, readonly

- custom research into the 4 kinds of agents - “context agent” → active learning
- execution agent is most straightforward but need to do its job well
- task creation → problems: hallucination, omission
- prioritization agent - will need to do DAGs
- spawn on command
- [Actor model](https://twitter.com/hadiazouni/status/1648375237283659792?s=20)/ Agent Oriented Programming?

- 5th agent - - [reflection? metalearning?](https://twitter.com/karpathy/status/1642607620673634304)

- there will be “AI social networks” - subreddit simulator


- orchestration and the cyborg problem - [sarahcat observation](https://twitter.com/sarahcat21/status/1646920947134504962)is correct
- [swyx commentary on cyborg nodes](https://www.swyx.io/temporal-centicorn#humans-in-the-loop-vs-ml-in-the-loop)would be amazing

- Are level 5 agents - [AGI-hard](https://www.latent.space/p/agi-hard)?- hard as self driving cars - perpetually 5 years away - uber & apple gave up
- must know when to yield to humans - easy to require confirm for destructive actions, but sometimes unclear
- “Interesting non-obvious note on GPT psychology is that unlike people they are completely unaware of their own strengths and limitations. E.g. that they have finite context window. That they can just barely do mental math. That samples can get unlucky and go off the rails.” Etc. - [karpathy](https://twitter.com/karpathy/status/1642598890573819905)

- must solve prompt injection ( - [hey @simon](https://twitter.com/simonw/status/1648521987776745472?s=20))
- will probably need to self improve statefully
- principal agent problem - we dont know how to prioritize humans, and you want to eval bot ability to prioritize? good luck



## (Update): Sept 2023 update

As we learned more about how people build agents, and what the valuable parts of the stack are, I updated the chart [based on a @karpathy](https://twitter.com/karpathy/status/1707437820045062561) tweet.

![](https://substackcdn.com/image/fetch/$s_!FTUI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff08de1b1-3327-4fe0-8bc5-2ae36e717b77_1238x788.png)

[1](https://www.latent.space#footnote-anchor-1)

The title of an influential [recent OpenAI paper](https://openai.com/research/gpts-are-gpts), but also [an actual concept](https://en.wikipedia.org/wiki/General-purpose_technology) in the study of technology — something your humble correspondent first learned about in research for the Tech Strategy chapters of [my book](https://learninpublic.org/toc) 3 years ago. Worth internalizing.

[2](https://www.latent.space#footnote-anchor-2)

[Dr. Katalin Kariko’s story of perseverance](https://www.nytimes.com/2021/06/10/podcasts/the-daily/mrna-vaccines-katalin-kariko.html) is worth a full listen, if you haven’t heard the story.

[3](https://www.latent.space#footnote-anchor-3)

Theory of Theory of Value of Software: If you set out with the goal to understand what makes some lines of code more valuable than other lines of code, and try to make predictions by running your theories through lots and lots of data while reducing your “loss”, the idea is that you’ll be better able to invest your time, money, and creativity in more rewarding directions than people who don’t take the same effort.

[4](https://www.latent.space#footnote-anchor-4)

I am not yet ready to publish [my full list](https://github.com/sw-yx/brain), but software value drivers include: Demand and Supply Aggregators, Production-ready frameworks for underspecified Standards, “Shadow IT” to circumvent internal politics and byzantine rules, systems of record ([Zawinswyx’s Law](https://dx.tips/platform-kinds)), and also replacing people and manual processes.

[5](https://www.latent.space#footnote-anchor-5)

Sidenote: if you are excited about a self driving car future, you *must *visit San Francisco and befriend someone with access to the Cruise apps. There’s ~200 of these fully self-driving all over the city every night. [The future is very close!](https://twitter.com/Cruise/status/1644073327475171328)

https://twitter.com/mcraddock/status/1645779894670950400/photo/1

A bit bigger map of LLM + Prompt Enginnering

Great deconstruction plus love the wordplay on anatomy of autonomy
