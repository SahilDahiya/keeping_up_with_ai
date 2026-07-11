---
title: '[AINews] OpenAI launches GPT 5.6 Sol/Terra/Luna, Codex becomes ChatGPT superapp'
topic: models
subtopic: releases
secondary_topics:
- agents/computer-use
summary: Covers GPT-5.6 model releases and Codex becoming a ChatGPT superapp, relevant
  to coding-agent product direction.
source: latent-space
url: https://www.latent.space/p/ainews-openai-launches-gpt-56-solterraluna
author: Latent Space
published: '2026-07-10'
fetched: '2026-07-11T05:09:15Z'
classifier: codex
taxonomy_rev: 1
words: 3428
content_sha256: a4a5183418acac544d1eb4894e9f6890cb221d004df3d86e7d632bb36bfaa2d5
---

# [AINews] OpenAI launches GPT 5.6 Sol/Terra/Luna, Codex becomes ChatGPT superapp

# [AINews] OpenAI launches GPT 5.6 Sol/Terra/Luna, Codex becomes ChatGPT superapp

### A big day for OpenAI.

On any other day, the launch of a surprisingly good/competitive [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) from Meta Superintelligence Labs, including, for the first time, in the [Meta Model API](https://developer.meta.com/ai/resources/blog/build-with-muse-spark/) (signaling high confidence for broad usage and third party testing which [is bearing out in their sister models](https://x.com/alexandr_wang/status/2074687661428572403)), would deserve title story status, but they had the misfortune of going up against a mainline frontier model launch:

As [previewed a couple weeks ago](https://openai.com/index/previewing-gpt-5-6-sol/) before government approval, 5.6 comes in three new sizes, Sol, Terra and Luna, corresponding to the sizes of Sun, Earth and Moon, as an alternative to the more literary sizing of Claude variants, and a new `ultra` effort level, *“our highest-capability setting, coordinating multiple agents across parallel workstreams to finish complex tasks faster”:*


`max`gives GPT‑5.6 even more time than`xhigh`to reason and explore alternatives, run checks, and revise its approach. ultra goes further bycoordinating four agents in parallel by default, trading higher token use for stronger results and faster time-to-result on demanding tasks.

On multiple benchmarks (not just the ones featured here), 5.6 both achieves higher performance at lower cost than Fable or Opus.

![](https://substackcdn.com/image/fetch/$s_!S2WI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d7bcf2a-7c60-4e1d-9aaf-db0b03cc4801_1470x1406.png)


“Terra performs just above Fable 5, while Luna outperforms Opus 4.8; each does so in roughly one-third of the time, with about half as many output tokens, and at approximately one-quarter the estimated cost. It also sets new state-of-the-art results on Terminal‑Bench 2.1 and DeepSWE, which test complex command-line workflows and long-horizon engineering in real codebases.”

There are also harder-to-benchmark improvements in computer use, presentation/document generation, and scientific research that should nevertheless be taken very seriously.

As we [predicted in April](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp?utm_source=publication-search), the newly launched [ChatGPT Work](https://x.com/OpenAI/status/2075274271845404744?s=20) and Codex desktop app update today is probably the penultimate step for OpenAI’s superapp strategy (the last open question is what happens to the agentic browser….)

![](https://substackcdn.com/image/fetch/$s_!SAjG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1521892-45ba-4676-a486-65663d1a6bb9_846x1090.png)

AI News for 7/08/2026-7/09/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**OpenAI launched a new three-model GPT‑5.6 family and simultaneously expanded the product stack around it.**

- OpenAI announced - **GPT‑5.6 Sol, Terra, and Luna**rolling out across- **ChatGPT, Codex, and the API**via- [@OpenAI](https://x.com/OpenAI/status/2075271421149020426)and- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075273992609599834)
- In ChatGPT, - **Plus, Pro, Business, and Enterprise**users get access to- **GPT‑5.6 Sol**through medium+ effort settings, while- **Pro and Enterprise**can select- **GPT‑5.6 Pro**for highest-quality results on complex tasks, per- [@OpenAI](https://x.com/OpenAI/status/2075271435573244008)
- API pricing introduced a tiered lineup: - **Sol $5 / $30 per million input/output tokens**,- **Terra $2.5 / $15**,- **Luna $1 / $6**, with- **cache-write pricing**added for the first time and- **90% cache-read discount**retained, according to- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)
- OpenAI framed the family around a price-performance ladder: - **Sol = flagship/highest ceiling**,- **Terra = GPT‑5.5-like capability at lower cost**,- **Luna = fastest/cheapest high-volume option**, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075286157186003348)
- The launch bundled major app-layer changes: - **ChatGPT Work**, a new- **desktop app merging Codex + ChatGPT**,- **Sites**beta,- **programmatic tool calling**, and- **multi-agent beta**in the Responses API, via- [@OpenAI](https://x.com/OpenAI/status/2075274271845404744),- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075275868268789885), and- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075274093327470923)

**Official claims and benchmark results**

**OpenAI’s official message emphasized strong agentic/coding performance, better artifact quality, and improved economics.**

- Sam Altman called it “ - **obviously the best model we have ever produced**” in the launch post, linking the release blog, via- [@sama](https://x.com/sama/status/2075266471316615436)
- Altman also highlighted enterprise economics: “ - **5.6 sol is a huge step forward for dollars-per-task**,” via- [@sama](https://x.com/sama/status/2075267201058426944)
- Greg Brockman said the goal is “ - **the best price for any level of target performance**” and the highest possible ceiling, via- [@gdb](https://x.com/gdb/status/2075271293474353553)
- OpenAI claimed - **GPT‑5.6 Sol sets a new high of 53.6 on Agents’ Last Exam**, beating- **Claude Fable 5 adaptive by 13.1 points**; at medium reasoning it beats Fable by- **11.4 points at roughly one-quarter the estimated cost**, while- **Terra and Luna also outperform Fable at around one-sixteenth the cost**, via- [@OpenAI](https://x.com/OpenAI/status/2075271423992680532)
- OpenAI said GPT‑5.6 improves - **artifact quality across presentations, documents, and spreadsheets**, with outputs exportable into existing enterprise tools, via- [@OpenAI](https://x.com/OpenAI/status/2075271432041545782)
- OpenAI positioned GPT‑5.6 as state of the art for - **reasoning through complex tasks**and for producing materials matched to templates, reference files, and preferred style inside- **ChatGPT Work**, via- [@OpenAI](https://x.com/OpenAI/status/2075274275104399670)
- OpenAI also said GPT‑5.6 is its - **most capable model yet on cyber and bio-related tasks**, with some API calls potentially blocked or paused for extra safety review in dual-use areas, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075274080740380829)
- OpenAI highlighted better - **Computer Use**performance: faster, more token-efficient, support for- **batching and parallel operations**across multi-step tasks, plus picture-in-picture supervision, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075276074980884862)

**Independent evaluations and third-party measurements**

**Independent evals broadly placed Sol near or at the frontier, especially on coding-agent workloads, while also surfacing caveats.**

- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)reported- **GPT‑5.6 Sol (max)**scores- **59**on its Intelligence Index,- **1 point below Claude Fable 5 (max)**, at- **about one-third of Fable’s cost per task**
- On the same analysis, - **Terra**and- **Luna**score- **55**and- **51**on the Intelligence Index, with- **~50%**and- **~80%**lower cost per task than Sol, respectively, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)
- Artificial Analysis said - **Sol leads the Coding Agent Index at 80**, ahead of Fable 5 and Opus 4.8, and is also cheaper per task than both on their harnesses, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)
- It also noted - **Sol defines a new Pareto frontier of intelligence vs output tokens**, while- **Terra and Luna are not on that frontier**, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268984539410521)
- Artificial Analysis found - **minor improvement over GPT‑5.5 in AA‑Omniscience**but with a- **higher hallucination rate**than GPT‑5.5 max, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268990004605023)
- It reported - **similar GDPval-AA v2 performance to Claude Fable 5**, suggesting comparable ability on economically valuable tasks, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268987550932998)
- [@ValsAI](https://x.com/ValsAI/status/2075270642359029972)ranked GPT‑5.6- **#2 on Vals Index and Vals Multimodal Index**, saying Fable 5 remains ahead on several benchmarks but GPT‑5.6 is “clearly in the same class”
- Vals also said - **Sol is #1 on CyberBench and Excel Modeling Benchmark**, and #1 on- **Legal Research Bench, ProofBench, SWE-bench, and Terminal-Bench 2.1**, adding that Fable had a nearly- **100% refusal rate on CyberBench**, via- [@ValsAI](https://x.com/ValsAI/status/2075270644711997581)
- [@arcprize](https://x.com/arcprize/status/2075270869992264003)said- **GPT‑5.6 Sol scores 7.8% on ARC‑AGI‑3**and is the- **first verified frontier model to ever beat an ARC‑AGI‑3 game**
- [@GregKamradt](https://x.com/GregKamradt/status/2075274981794300113)noted- **92.5% on ARC‑AGI‑2**, calling it SOTA while costing- **an order of magnitude less**than GPT‑5.5 Pro three months earlier
- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075423964378366427)later reported- **GPT‑5.6 Sol (max) leads CritPt**, a benchmark of unpublished research-level physics problems, by roughly- **4 points over Claude Fable 5**
- [@llama_index](https://x.com/llama_index/status/2075351095258296378)said day-0 ParseBench results show GPT‑5.6 continues to do well on- **text and tables**but still struggles on- **charts and layout**, and that- **Luna is ~6× cheaper than Sol with only minor degradations**
- [@jerryjliu0](https://x.com/jerryjliu0/status/2075356305099800717)similarly said ParseBench shows- **no high-level change versus GPT‑5.5**on tables/text/charts/layout, stressing persistent weakness on- **complex text layouts, chart transcription, and source-element bounding boxes**

**Technical details**

**The technical story of GPT‑5.6 is as much about inference orchestration and token efficiency as raw capability.**

- OpenAI shipped - **three model tiers**with multiple- **reasoning effort levels**; users discussed- **Light, Medium, High, Extra High, Ultra**, leading to a large configuration matrix, via- [@rasbt](https://x.com/rasbt/status/2075369179817902176)
- OpenAI added - **Programmatic Tool Calling**in the Responses API and- **Multi-agent beta**, indicating more explicit support for orchestrated tool use and agent decomposition, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075274093327470923)
- OpenAI’s app layer now uses - **Codex as the core**of the new Work product, per- [@sama](https://x.com/sama/status/2075293792048136572)and- [@gdb](https://x.com/gdb/status/2075276416686723110)
- Several posts stress - **parallel agents/subagents**as a major capability lever;- [@aidan_mclau](https://x.com/aidan_mclau/status/2075337767949865464)explicitly mentions users can increase the number of- **5.6 subagents**
- [@LiorOnAI](https://x.com/LiorOnAI/status/2075277748394967122)summarized likely drivers as- **adaptive reasoning**,- **parallel agents**,- **programmatic tool use**, and- **higher token efficiency**
- Artificial Analysis reported - **Sol max uses ~15k output tokens per Intelligence Index task vs 16k for GPT‑5.5**, and fewer than Opus 4.8, GLM‑5.2, and Gemini 3.5 Flash at comparable intelligence, via- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)
- [@OpenRouter](https://x.com/OpenRouter/status/2075271807855452196)said early testing found the 5.6 models- **more token efficient**, lowering both cost and time-to-task completion
- The desktop/app layer brought a - **Chrome extension**,- **revamped in-app browser**,- **authenticated sites**,- **persistent multi-tab sessions**,- **file downloads**, and tighter cross-device handoffs, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075275868268789885),- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075276009902112976), and- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075292716737736919)
- **Sites**entered beta for paid users, offering hosting, storage, and optional auth for GPT-built apps, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075275892591591469)and- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075337081304522853)

**The “Sol autonomously post-trained Luna” claim**

**This was the most provocative technical claim around the launch, but its interpretation became contested almost immediately.**

- Multiple accounts amplified the statement that - **OpenAI says GPT‑5.6 Sol autonomously post-trained GPT‑5.6 Luna**, via- [@scaling01](https://x.com/scaling01/status/2075269113488789984),- [@tejalpatwardhan](https://x.com/tejalpatwardhan/status/2075272564629451110), and- [@dejavucoder](https://x.com/dejavucoder/status/2075270116909232129)
- The claim fueled RSI/autoresearch speculation; - [@tenobrus](https://x.com/tenobrus/status/2075282678652522712)said if true as stated, it would be a “pretty large update” for automated researcher timelines
- [@eliebakouch](https://x.com/eliebakouch/status/2075281402807844872)framed it as OpenAI asking Sol to post-train Luna “with- **100k GPUs**” for an experiment
- [@gdb](https://x.com/gdb/status/2075363531042726216)said the implication is easy to overlook for accelerating engineering workflows, reinforcing that OpenAI wants this read as more than a marketing flourish
- But skeptical clarifications emerged quickly: - [@nikolaj2030](https://x.com/nikolaj2030/status/2075297831376793764)asked whether this actually meant Sol completed a- **small controlled post-training task**—modifying a config, editing a scheduler file, and launching a run—rather than end-to-end real-world post-training of Luna
- [@nrehiew_](https://x.com/nrehiew_/status/2075316190386462888)interpreted the screenshot similarly: Sol could go from high-level ideas to- **editing configs and launching experiments**, not fully owning Luna’s end-to-end post-training
- [@scaling01](https://x.com/scaling01/status/2075354327791587467)argued that what’s probably happening is a model implementing- **LLM-as-a-judge graders**, reward-shaping logic, or small training configs on top of existing OpenAI RL infrastructure—not autonomous end-to-end research or training systems
- [@scaling01](https://x.com/scaling01/status/2075359429717836251)explicitly said we should distance these statements from- **literal autonomous end-to-end post-training or research**, which models still cannot do
- Counterbalancing that skepticism, - [@aidan_mclau](https://x.com/aidan_mclau/status/2075328409400738229)said it is routine for him to have- **5.6 e2e do an entire RL run**, suggesting meaningful internal workflow automation even if not self-sufficient research
- The consensus across technical observers was not that Sol independently invented and trained Luna, but that GPT‑5.6 may now be capable of - **executing meaningful chunks of model-improvement workflows inside mature internal infrastructure**

**Internal productivity and recursive improvement signals**

**OpenAI also used internal-usage data to argue that GPT‑5.6 materially changes researcher throughput.**

- [@scaling01](https://x.com/scaling01/status/2075269455781703850)highlighted an OpenAI claim that it- **doubled experiment throughput per researcher**since the start of the year
- [@eliebakouch](https://x.com/eliebakouch/status/2075273299148341327)quoted OpenAI saying average daily output tokens per active researcher were- **more than twice the highest level observed for GPT‑5.5**during internal testing
- Another OpenAI stat, relayed by - [@eliebakouch](https://x.com/eliebakouch/status/2075273992185782661), said over six months the share of research compute devoted to- **internal coding inference grew 100-fold**, while- **internal agentic token usage increased ~22-fold**
- [@FakePsyho](https://x.com/FakePsyho/status/2075291659814781370)linked these developments to OpenAI’s performance in top programming contests, describing systems close to GPT‑5.6 plus custom harnesses as decisively beating elite human competitors
- This fed broader RSI/autoresearch discussion, especially from people who see long-horizon coding and heuristic optimization as proxies for model-improvement capability

**Product implications: ChatGPT Work, Codex merge, desktop, and Sites**

**The model launch doubled as a product strategy reset: OpenAI is pushing from “chatbot” to “work OS.”**

- OpenAI launched - **ChatGPT Work**, an agent powered by- **Codex + GPT‑5.6**that can act across apps and files, stay on tasks for hours, and turn a goal into finished work, via- [@OpenAI](https://x.com/OpenAI/status/2075274271845404744)
- Work can ingest context from - **docs, Slack, Notion, Microsoft 365, and Google Drive**and produce- **decks, docs, spreadsheets, dashboards, visualizations, and interactive explanations**, summarized by- [@kimmonismus](https://x.com/kimmonismus/status/2075271465964798147)
- The - **Codex app merged into the new ChatGPT desktop app**, confirmed by- [@avstorm](https://x.com/avstorm/status/2075266403297362364)and- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075275880704995342)
- Developers now get - **inline diff editing**,- **PR review side panel**, better- **SSH video rendering**, and stronger- **computer use**, via- [@romainhuet](https://x.com/romainhuet/status/2075286364476850430)and- [@reach_vb](https://x.com/reach_vb/status/2075280626362560805)
- **Sites**lets users turn work into shareable hosted apps/websites from ChatGPT, via- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075275892591591469)and- [@simpsoka](https://x.com/simpsoka/status/2075278935366287842)
- [@OpenAI](https://x.com/OpenAI/status/2075310019185389913),- [@OpenAI](https://x.com/OpenAI/status/2075310020653351324), and- [@OpenAI](https://x.com/OpenAI/status/2075310022121472399)marketed GPT‑5.6 through case studies: a- **broccoli farmer**, a- **mathematician**, and a- **family cereal business**
- This product reframing was read by some as OpenAI’s answer to Anthropic’s Cowork / Claude Code stack, via - [@jerryjliu0](https://x.com/jerryjliu0/status/2075295459304710496)and- [@kimmonismus](https://x.com/kimmonismus/status/2075280933452669000)

**Facts vs opinions**

**Facts / directly sourced claims**

- GPT‑5.6 family names, rollout channels, and access tiers: - [@OpenAI](https://x.com/OpenAI/status/2075271421149020426),- [@OpenAI](https://x.com/OpenAI/status/2075271435573244008),- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075273992609599834)
- API prices and cache-write policy: - [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905)
- OpenAI’s benchmark claims on Agents’ Last Exam: - [@OpenAI](https://x.com/OpenAI/status/2075271423992680532)
- Artificial Analysis and Vals leaderboard placements: - [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905),- [@ValsAI](https://x.com/ValsAI/status/2075270642359029972)
- ARC‑AGI‑3 7.8% claim: - [@arcprize](https://x.com/arcprize/status/2075270869992264003)
- ParseBench caveats: - [@llama_index](https://x.com/llama_index/status/2075351095258296378),- [@jerryjliu0](https://x.com/jerryjliu0/status/2075356305099800717)
- Safety testing finding jailbreaks on GPT‑5.6 Sol: - [@alxndrdavies](https://x.com/alxndrdavies/status/2075279477626564933)

**Opinions / interpretation / hype**

- “Best model we have ever produced”: - [@sama](https://x.com/sama/status/2075266471316615436)
- “First time I’ve felt comfortable delegating the hardest problem out there”: - [@reach_vb](https://x.com/reach_vb/status/2075269547439907269)
- “Not enough people are emotionally prepared for GPT‑6”: - [@scaling01](https://x.com/scaling01/status/2075276735650648258)
- “OpenAI is competing on cost curves, not benchmarks”: - [@LiorOnAI](https://x.com/LiorOnAI/status/2075277748394967122)
- “The engineers were allowed to cook”: - [@TheHumanoidHub](https://x.com/TheHumanoidHub/status/2075272514755059773)
- “Generational fumble” regarding Codex becoming ChatGPT Desktop: - [@theo](https://x.com/theo/status/2075312087723876556)

**Different perspectives**

**Supportive views**

- Many developers and evaluators saw GPT‑5.6 as a meaningful frontier advance, especially in coding and knowledge work: - [@gdb](https://x.com/gdb/status/2075270503405924466),- [@AravSrinivas](https://x.com/AravSrinivas/status/2075270640177938547),- [@OpenRouter](https://x.com/OpenRouter/status/2075271807855452196),- [@Teknium](https://x.com/Teknium/status/2075392507794624803)
- Several posts focused on - **cost efficiency**as the real win, with Sol matching frontier peers while being materially cheaper:- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905),- [@omarsar0](https://x.com/omarsar0/status/2075270117131259925),- [@cline](https://x.com/cline/status/2075278343927365991)
- Others highlighted the - **agentic stack**—Work, Codex, multi-agent, programmatic tools—as more strategically important than raw benchmark deltas:- [@TheRundownAI](https://x.com/TheRundownAI/status/2075273458661949763),- [@kimmonismus](https://x.com/kimmonismus/status/2075271465964798147),- [@fidjissimo](https://x.com/fidjissimo/status/2075305622120325363)

**Neutral / analytical views**

- Some analysts saw Sol as roughly - **same class as Fable**, but not decisively ahead overall:- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905),- [@ValsAI](https://x.com/ValsAI/status/2075270642359029972)
- [@teortaxesTex](https://x.com/teortaxesTex/status/2075274583226069040)argued the release may reflect OpenAI strong post-training recovering toward Anthropic despite a stronger Anthropic base model
- [@simonw](https://x.com/simonw/status/2075306164993315192)pointed to notable API additions but also implied growing product complexity

**Critical / skeptical views**

- [@scaling01](https://x.com/scaling01/status/2075268278105067566)asked whether- **GPT‑5.6 Sol is worse at math**, pushing back on the “everything got better” narrative
- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268990004605023)found- **higher hallucination rate vs GPT‑5.5**
- [@scaling01](https://x.com/scaling01/status/2075279452494299273)criticized the ARC‑AGI‑3 scoring setup, saying Sol would score- **0% under official scoring methodology capped at $10k**and objecting to use of a- **$25k**budget
- [@Hangsiin](https://x.com/Hangsiin/status/2075277820528607704)and- [@Hangsiin](https://x.com/Hangsiin/status/2075278682160275561)pointed to- **subscription/credit confusion**, saying Sol costs more credits than GPT‑5.5 while usage limits differ less than API pricing suggests
- [@QuinnyPig](https://x.com/QuinnyPig/status/2075334468462899442)said OpenAI’s pricing/subscription strategy is confusing, particularly around future pricing jumps or inclusion terms
- [@rasbt](https://x.com/rasbt/status/2075369179817902176)highlighted UX complexity:- **2 modes × 3 models × 5 effort levels = 30 configurations**
- [@MParakhin](https://x.com/MParakhin/status/2075361980446289925)complained that- **GPT‑5.6 Pro no longer has extended thinking**, preferring an option to pay for much longer reasoning
- [@theo](https://x.com/theo/status/2075312087723876556)and- [@simonw](https://x.com/simonw/status/2075348941215006888)criticized the growing app/mode fragmentation around ChatGPT, Codex, and Work

**Safety and security concerns**

**The launch also surfaced one of the strongest public cyber-safety debates around a recent frontier model release.**

- [@alxndrdavies](https://x.com/alxndrdavies/status/2075279477626564933)from the AI Safety Institute said they found- **universal jailbreaks in all rounds of testing**that enabled long-form agentic task completion in- **vulnerability discovery and exploit development**
- [@EthanJPerez](https://x.com/EthanJPerez/status/2075296476817985751)called it “- **the highest stakes safety issue of any model release yet**”
- [@yonashav](https://x.com/yonashav/status/2075286161241612664)praised OpenAI for allowing third-party unreleased-model safety assessments to be published even when inconvenient
- [@Mononofu](https://x.com/Mononofu/status/2075414796426764507)said ease of jailbreaking plus reward-hacking reports make them worried OpenAI may have rushed the release to keep pace with Fable
- At the same time, OpenAI explicitly warned some cyber/bio requests may be paused or blocked mid-stream for additional review, via - [@OpenAIDevs](https://x.com/OpenAIDevs/status/2075274080740380829)
- This created a split narrative: strong cyber capability is treated as a product advantage by some evaluators, but as a serious deployment risk by safety researchers

**Context**

**Why this matters goes beyond a single model benchmark win.**

- The launch happened amid a compressed week of frontier competition that also included new releases from - **Meta Muse Spark 1.1**and- **Grok 4.5**, leading multiple observers to describe the frontier as newly crowded:- [@matanSF](https://x.com/matanSF/status/2075276339607654802),- [@kimmonismus](https://x.com/kimmonismus/status/2075322537592922345)
- OpenAI’s differentiation is increasingly framed less as “best raw benchmark score” and more as - **cost-efficient agentic work**, consistent with posts from- [@sama](https://x.com/sama/status/2075267201058426944),- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2075268970492657905), and- [@LiorOnAI](https://x.com/LiorOnAI/status/2075277748394967122)
- The product bundling suggests OpenAI is moving from a model vendor to a - **full-stack work platform**, with its own browser, connectors, orchestration primitives, hosted app deployment, and desktop runtime
- The strongest forward-looking signal may be the internal claim that researchers already use these systems to materially increase output and automate chunks of RL/post-training workflows, even if public discussion often overstates that as “the model trained itself”
- The launch also sharpens a recurring engineering question raised by many tweets: whether the frontier is now bottlenecked less by a single monolithic model and more by - **orchestration quality, tool APIs, subagents, evaluation harnesses, and economics**

**Frontier models and evaluations**

- **Meta launched Muse Spark 1.1**and the- **Meta Model API**in public preview, positioning it as a strong- **agentic, coding, multimodal, and computer-use**model. Official posts came from- [@finkd](https://x.com/finkd/status/2075218444056707458),- [@alexandr_wang](https://x.com/alexandr_wang/status/2075218936266998230),- [@shengjia_zhao](https://x.com/shengjia_zhao/status/2075220782465290620),- [@ren_hongyu](https://x.com/ren_hongyu/status/2075224643829711101), and- [@OpenAIDevs](https://x.com/MetaforDevs/status/2075268072022401526)
- Key technical details repeatedly cited: - **1M-token context window**,- **video understanding**, multimodal reasoning, and API availability, with- [@altryne](https://x.com/altryne/status/2075237837033889911)and- [@xinyun_chen_](https://x.com/xinyun_chen_/status/2075276047495659656)among those emphasizing long-horizon agentic gains
- Benchmark claims around Muse Spark 1.1 included competitiveness with - **GPT‑5.5**and- **Opus 4.8**on agentic evals, strong performance on- **Harvey’s Legal Bench, TaxEval, MedScribe**, and some out-of-distribution evals over- **Opus 4.8**and- **Grok 4.5**, via- [@alexandr_wang](https://x.com/alexandr_wang/status/2075233663323947120),- [@alexandr_wang](https://x.com/alexandr_wang/status/2075275671815999956),- [@_jasonwei](https://x.com/_jasonwei/status/2075265159430623334), and- [@cline](https://x.com/cline/status/2075271057326719152)
- External reaction ranged from surprise and enthusiasm—e.g. - [@kimmonismus](https://x.com/kimmonismus/status/2075232528726708245),- [@preston_ojb](https://x.com/preston_ojb/status/2075229604244271470),- [@0interestrates](https://x.com/0interestrates/status/2075330028729143634)—to practical integration pushes from- [@cline](https://x.com/cline/status/2075271057326719152)
- **Grok 4.5**continued to draw benchmark discussion:- [@arena](https://x.com/arena/status/2075301317560742373)said it reached- **#3 in Code Arena: Frontend**, while- [@alexgshaw](https://x.com/alexgshaw/status/2075273675331580218)discussed- **Terminal-Bench 2.1**reward-hacking caveats. Several posters argued Grok now belongs in the frontier set, including- [@teortaxesTex](https://x.com/teortaxesTex/status/2075347335412953265)

**Agents, orchestration, and developer tooling**

- Multiple posts reinforced that - **harness/orchestration quality**is becoming as important as the base model.- [@dair_ai](https://x.com/dair_ai/status/2075241322655727682)highlighted a study where changing only the orchestration layer cut- **blended cost per task 41%**,- **tokens 38%**, and- **median wall-clock 44%**at quality parity
- LangChain/LangSmith tooling updates focused on observability for coding agents: tracing - **Claude Code**sessions into LangSmith via- [@LangChain](https://x.com/LangChain/status/2075233516380717246), plus discussion of- **OpenWiki Brains**for proactive memory agents from- [@BraceSproul](https://x.com/BraceSproul/status/2075277759937695979),- [@hwchase17](https://x.com/hwchase17/status/2075277641066938454), and- [@colifran_](https://x.com/colifran_/status/2075406926087934376)
- [@ManusAI](https://x.com/ManusAI/status/2075236343429599432)launched- **Branch**, allowing parallel sessions that inherit full context
- [@antigravity](https://x.com/antigravity/status/2075265852992057448)described investment in- **dynamic agent teams, active sidecars, and generative UI**
- [@CoreWeave](https://x.com/CoreWeave/status/2075293731998286263)introduced- **ARIA**, an AI Research and Improvement Agent inside W&B that reads runs, forms hypotheses, launches experiments, and scores against baselines
- [@TheTuringPost](https://x.com/TheTuringPost/status/2075303983422578740)highlighted- **SkillCenter**, a package manager/index for agent skills, while- [@steveruizok](https://x.com/steveruizok/status/2075303919664734295)shipped a “papercuts” CLI for agents to report broken tool paths and frustrations

**Inference, efficiency, and open model infrastructure**

- **Ollama**announced fundraising and said it now has- **9M+ active builders**, framing the moment as scaling “open models into AI that you can own,” via- [@ollama](https://x.com/ollama/status/2075211168407503016)
- **Hugging Face / Reachy Mini**economics were striking:- [@andimarafioti](https://x.com/andimarafioti/status/2075222463777042454)said- **9k Reachy Minis**generate- **15k hours of conversation/month**; using GPT-realtime would cost- **$45k/month**, so they built an open alternative at- **$0.25/hour**and free on laptop
- [@dmitrshvets](https://x.com/dmitrshvets/status/2075248269580538081)shared speculative decoding research claiming- **4.37×**speedup over autoregressive decoding and- **+24.7%**over a strong DFlash baseline
- [@fal](https://x.com/fal/status/2075284936756539813)detailed a diffusion serving stack reaching- **0.45s inference**using kernel optimizations, quantization-aware distillation, and timestep distillation
- [@ostrisai](https://x.com/ostrisai/status/2075286667456582080)added isolated reference-token attention for Krea2 edit training; example timings showed major gains from KV caching, such as- **31.63s → 10.90s**for 3 refs
- [@vllm_project](https://x.com/vllm_project/status/2075301430123176037)announced the first- **vLLM Conference**, underscoring how open inference stacks remain a central layer of the ecosystem
- [@QuixiAI](https://x.com/QuixiAI/status/2075418782470643958)reported- **Qwen3.6-35B-A3B-NVFP4**at- **65 tok/s**on dual B60 with custom SYCL kernels and- **128k context**

**Robotics, multimodal systems, and AI-for-science**

- [@perceptroninc](https://x.com/perceptroninc/status/2075261142038196727)launched- **Perceptron Egocentric**, an embodied reasoning/annotation system said to beat pipelines built on- **Gemini 3.5 Flash**and- **Gemini Robotics-ER 1.6**
- [@DataChaz](https://x.com/DataChaz/status/2075303718153789944)summarized the economics:- **10–15× cheaper**than human annotation, with- **+77% end-to-end F1**on- **WGO-Bench**(- **0.280 vs 0.158**)
- [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2075286203583398181)emphasized the output structure: subtask boundaries, per-hand actions, left/right hand grounding, and dense labels from raw egocentric/robot video
- Google Research released - **SensorFM**, a sensor foundation model trained on- **1 trillion minutes**of unlabeled wearable data from- **5 million consented participants**, via- [@GoogleResearch](https://x.com/GoogleResearch/status/2075283854093607016)
- [@SebastienBubeck](https://x.com/SebastienBubeck/status/2075407986772861047)said GPT‑5.6 helped formalize the- **unit distance solution**in- **1 million lines of LEAN**, compressing what would previously require a team over years into a short single-person effort
- [@TheTuringPost](https://x.com/TheTuringPost/status/2075289747875107013)highlighted a Stanford paper on the- **“Agentic Garden of Forking Paths”**, where AI research personas reproduced human-like ideological variation;- **86%**of analyses passed independent AI review and- **78%**were judged methodologically sound by humans

**Policy, safety, and ecosystem debate**

- A cluster of posts sharply criticized the EU’s - **Chat Control**law/proposal from civil-liberties and anti-surveillance angles, including- [@perrymetzger](https://x.com/perrymetzger/status/2075226601298514418),- [@IterIntellectus](https://x.com/IterIntellectus/status/2075258469561844112), and- [@dhh](https://x.com/dhh/status/2075295777673634256)
- Open-source advocacy remained loud: - [@AndrewYNg](https://x.com/AndrewYNg/status/2075271586400403567)said protecting open source AI is critical to permissionless innovation, while- [@Dan_Jeffries1](https://x.com/Dan_Jeffries1/status/2075253735563886595)argued restricting open source AI would be “civilizational suicide”
- [@cognition](https://x.com/cognition/status/2075308920755618144)addressed trustworthiness concerns around open-source-derived coding agents, saying their- **SWE‑1.7**built on- **Kimi K2.7**was specifically trained for trustworthiness and refused surveillance-style scenarios where the base model complied
- On evaluation methodology and behavior science, - [@TransluceAI](https://x.com/TransluceAI/status/2075271925665063046)argued for measuring- **how systems behave in the world**, not just raw capabilities
- Forecasting/futures discussion centered on - **AI 2040**, with endorsements and critiques from- [@NeelNanda5](https://x.com/NeelNanda5/status/2075271483207872874),- [@RichardMCNgo](https://x.com/RichardMCNgo/status/2075301126921175166),- [@scaling01](https://x.com/scaling01/status/2075296890325712944), and others debating compute gaps, geopolitical assumptions, and takeoff dynamics

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Chinese Open Models: Releases and Scrutiny**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
