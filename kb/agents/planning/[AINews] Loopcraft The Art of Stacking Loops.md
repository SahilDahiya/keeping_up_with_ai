---
title: '[AINews] Loopcraft: The Art of Stacking Loops'
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/evaluation
summary: AINews piece on Loopcraft and stacking feedback loops for AI systems.
source: latent-space
url: https://www.latent.space/p/loopcraft
author: Latent Space
published: '2026-06-12'
fetched: '2026-07-11T05:10:30Z'
classifier: codex
taxonomy_rev: 1
words: 1826
content_sha256: d05aa8d5105cb6e9db3aedcb905b7ddd0295f761245bc6a1be255545d856a044
---

# [AINews] Loopcraft: The Art of Stacking Loops

# [AINews] Loopcraft: The Art of Stacking Loops

### a quiet day lets us highlight a great concept from Peter Steinberger, Boris Cherny, and Andrej Karpathy

There’s a lot of “loop discourse” in the air:

- [Steipete](https://x.com/steipete/status/2063697162748260627): “Here’s your monthly reminder that you shouldn’t be prompting coding agents anymore. You should be designing loops that prompt your agents.”
- [Boris](https://x.com/0xwhrrari/status/2064804504608887040): “I don’t prompt Claude anymore. I write loops, the loops do the work.”
- [Andrej](https://www.youtube.com/watch?v=kwSVtQ7dziU)on- [Autoresearch](https://www.latent.space/p/ainews-autoresearch-sparks-of-recursive?utm_source=publication-search): To get the most out of the tools that have become available now you have to- **remove yourself as the bottleneck**. You can’t be there to prompt the next thing. You need to take yourself outside. You have to- **arrange things such that they’re completely autonomous**and the more you know how can you maximize your token throughput and- **not be in the loop**. This is the goal and the name of the game now is to- **increase your leverage**…. I don’t want to be the researcher in the loop looking at results etc, I’m holding the system back.- **So the question is how do I refactor all the abstractions so that I’m not I have to arrange it once and hit go.**”

We like this a lot and people don’t realize how many loops we are already in:

![](https://substackcdn.com/image/fetch/$s_!6Y74!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F517bbc58-4f26-46b5-a12e-f4a5f84b0a30_1986x1118.png)

More minimalist, a smaller set of loops:

![](https://substackcdn.com/image/fetch/$s_!4fI5!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F347a258a-520b-4c35-9bb5-84d753fcbe5b_920x380.png)

One might argue the entire game of the next century is to be able to **stack loops** as effectively as possible. In the early days of each phase, it will be valuable to know when to go **DOWN** a loop when things go wrong (for **reliability**)… but it will probably be more valuable to know how to go **UP** a loop as models improve (for **leverage**).

If you don’t figure out how to do this, don’t be salty when you lose to those that do.

Rich has his “[Bitter Lesson](https://x.com/RichardSSutton/status/2056419165502935198)” for models. We now have **the Salty Lesson for agents**:


Don’t fix things yourself, as you have done historically.

Instead focus on systems that scale with more agents, like goals and orchestration.

AI News for 6/10/2026-6/11/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Anthropic’s Fable 5 rollout, covert sandbagging backlash, and model behavior debates**

- **Silent degradation policy was quickly reversed after public backlash**: Multiple posts focused on Anthropic’s decision to covertly degrade- **Claude Fable 5**for some AI-research-related use cases, then reverse course within roughly a day.- [Simon Willison](https://x.com/simonw/status/2064918665859080392)welcomed the rollback;- [MTS live](https://x.com/MTSlive/status/2064922000020398331)summarized that Anthropic was reversing the policy;- [Kim Monismus](https://x.com/kimmonismus/status/2065003618710008084)framed it as a retreat after criticism from researchers. The strongest technical criticism centered less on the existence of safeguards and more on- **opaque behavior at the model layer**:- [Code Star](https://x.com/code_star/status/2064931207310118940)argued safeguards are normal but “obfuscation without warning” violates the user/provider contract, while- [Clement Delangue](https://x.com/ClementDelangue/status/2065069246124613999)called avoidance of AI manipulation important.
- **The substantive dispute is about governance, transparency, and access to frontier models**: Several researchers drew a distinction between legitimate restrictions and hidden sabotage.- [Ryan Greenblatt](https://x.com/RyanPGreenblatt/status/2064948033423598035)said blocking frontier AI R&D may be reasonable in principle, but silent sandbagging is not; later he argued for- **access programs with KYC/monitoring**for safety/security researchers rather than broad capability denial (- [1](https://x.com/RyanPGreenblatt/status/2065182720133841069),- [2](https://x.com/RyanPGreenblatt/status/2065174434672148487)).- [Natasha/Lambert](https://x.com/natolambert/status/2065082135682383950)gave the most detailed critique: the main error was an- **uneven safety implementation that misled users**, undermined trust, and reinforced concentration of power over who gets to do frontier research.- [Gergely Orosz](https://x.com/GergelyOrosz/status/2065029326215528474)turned this into an engineering recommendation: put models behind- **provider-agnostic routers/harnesses**so teams can switch vendors quickly when T&Cs or behavior become unacceptable.
- **Fable 5’s capabilities are strong, but its product behavior is still noisy and expensive**: Benchmarks and anecdotes were mixed.- [htihle](https://x.com/htihle/status/2065050640154350043)reported- **87.8% on WeirdML**, the first model above 70% average on each task there.- [ProximalHQ](https://x.com/ProximalHQ/status/2065184730279223410)said Fable 5 ranks- **#1 on FrontierSWE**, with runs productive for nearly- **20 hours**on some tasks. But practical reports highlighted cost, refusals, and odd phrasing:- [threepointone](https://x.com/threepointone/status/2065131942279016700)spent about- **$250**on a ~10k LOC PR and didn’t find it worth it;- [Cline](https://x.com/cline/status/2065192415498277335)said cheaper models plus adversarial review loops often match or beat it on cost/perf;- [tamaybes](https://x.com/tamaybes/status/2065147305494450248)described Fable inventing internal “codenames” during coding, leaking its own “neuralese” into outputs. Benchmarks also suggested sharp asymmetries depending on task framing:- [scaling01](https://x.com/scaling01/status/2065209370145702040)pointed to- **200/200 refusals on ProgramBench**, while- [thoughtfullab](https://x.com/thoughtfullab/status/2065096885514227876)and- [karinanguyen](https://x.com/karinanguyen/status/2065198770292146280)highlighted unusually strong post-training/AI-improves-AI behavior.

**Automated AI research and agentic optimization systems**

- **Recursive SI showed a general system hitting SOTA on public optimization benchmarks**: The most technically notable release was from- [Richard Socher](https://x.com/RichardSocher/status/2065094362774876232)and- [Recursive SI](https://x.com/_rockt/status/2065061990800802249), who presented an early “automated open-ended discovery system” for AI research. They claim state-of-the-art results on three public tasks:- **NVIDIA SOL-ExecBench**,- **NanoGPT Speedrun**, and- **NanoChat autoresearch**, and they- [open-sourced the discoveries](https://x.com/_rockt/status/2065061993271202171). Detail tweets from- [cong_ml](https://x.com/cong_ml/status/2064992941844615246)gave the metrics: on NanoChat, reaching the same loss- **1.3× faster**; on NanoGPT Speedrun, reducing runtime from- **79.7s to 77.5s**; on SOL-ExecBench, improving mean score from- **0.699 to 0.754**over 235 kernels. This is notable less as “AGI research automation” than as evidence that current systems can already contribute on- **narrow, high-feedback systems optimization tasks**.
- **Microsoft’s Arbor points in a similar direction for long-horizon autonomous research**:- [Hugging Papers](https://x.com/HuggingPapers/status/2065062300218749172)highlighted- **Arbor**, a Microsoft Research autonomous research agent using- **persistent hypothesis-tree refinement**. The claim: it beats Codex and Claude Code across six research tasks and reaches- **86% Any-Medal on MLE-Bench Lite**. Together with Recursive’s results, Arbor suggests a growing split in “agents for research” between: (1) systems optimized for rapid iterative systems tuning, and (2) systems optimized for- **long-horizon hypothesis management**.
- **Benchmarks are adapting to measure AI-on-AI improvement and real-world labor tasks**:- [thoughtfullab](https://x.com/thoughtfullab/status/2065096885514227876)positioned- **PostTrainBench**as a recursive-self-improvement eval—AI training weaker models and measuring loop progress directly.- [dawnsongtweets](https://x.com/dawnsongtweets/status/2065095757988868190)introduced- **Agents’ Last Exam (ALE)**, a rolling benchmark over- **1,500 expert-sourced tasks across 55 occupations**; frontier agents solve a meaningful fraction of work, but on the hardest tier all tested systems scored- **0%**.- [manoelribeiro](https://x.com/manoelribeiro/status/2065055795998233039)introduced- **SciConBench**with- **9.11k questions from Cochrane reviews**, finding that frontier agents still cannot synthesize scientific conclusions reliably. The pattern across these releases: agents are increasingly useful in bounded loops, but remain brittle on- **expert synthesis and economically valuable long-horizon tasks**.

**Data infrastructure becomes a first-class bottleneck: robotics, dataset observability, and dependency tracing**

- **Macrodata Labs launched to build the robotics data loop**: The clearest infra startup announcement came from- [Guilherme Penedo](https://x.com/gui_penedo/status/2064981375694909757),- [Hynek Kydlíček](https://x.com/HKydlicek/status/2064984505706774779), and- [Macrodata Labs](https://x.com/macrodata_labs/status/2064984775652192652). Their thesis: robotics is where LLMs were a few years ago, and the hard part is not architecture but- **messy multimodal physical data pipelines**—video, multi-rate sensors, heterogeneous formats, hand tracking, subtask segmentation, reward model scoring, and continuous ingestion. Their first product,- **Refiner**, is an open-source framework plus cloud runtime for turning raw demonstrations into training-ready datasets with sharding, checkpointing, observability, and lineage. This drew support from multiple infra-focused practitioners who view “look at the data” and pipeline introspection as still underbuilt in multimodal/agentic settings (- [Code Star](https://x.com/code_star/status/2064997532602663203),- [eliebakouch](https://x.com/eliebakouch/status/2065114511439249852)).
- **Data quality/debugging is becoming more explicit and instrumented**:- [Goodfire](https://x.com/GoodfireAI/status/2065118189986717902)introduced- **predictive data debugging**, arguing that preference/DPO datasets contain hidden pathologies—from broken guardrails to hallucinations—and should be analyzed before training.- [AllenAI](https://x.com/allen_ai/status/2065100726032839024)released- **ModSleuth**, tracing the dependency graph of modern LLMs and showing that models increasingly rely on large chains of- **other models plus datasets**; they cite- **Olmo 3**as depending on- **89 models and 183 datasets**, and- **Nemotron 3**on- **273 models and 560 datasets**. This is a useful corrective to simplistic “model trained on web data” narratives: modern LLM construction is already deeply- **compositional and synthetic**.
- **Memory, retrieval, and vector infra remain active design space despite larger contexts**:- [Weaviate’s Engram](https://x.com/kamtybor/status/2065028126636204243)proposes an- **extract → transform → commit**memory maintenance loop instead of naively appending chat logs;- [Weaviate Playground](https://x.com/weaviate_io/status/2065055262851973306)packaged this and related RAG/agent demos. On the retrieval side,- [Qdrant](https://x.com/qdrant_engine/status/2065056457461321761)argued larger context windows do- **not**make retrieval obsolete because context still imposes cost/latency, while- [rishdotblog](https://x.com/rishdotblog/status/2065026144903315545)warned against vector search without guardrails. The trend is toward- **active memory management and retrieval efficiency**, not simple replacement by giant context windows.

**Inference speed, kernel work, and open systems releases**

- **Diffusion and speculative/local inference saw concrete speed wins**:- [Demis Hassabis](https://x.com/demishassabis/status/2064873362799600042)highlighted- **DiffusionGemma**, described as- **4× faster**than other Gemma 4 variants;- [osanseviero](https://x.com/osanseviero/status/2065041448135770436)said demos had to be slowed down for viewers.- [Unsloth](https://x.com/UnslothAI/status/2065107734916432189)released- **Gemma 4 MTP GGUFs**, claiming- **1.4–2.2×**faster local inference with no accuracy loss; the 12B model reportedly reaches- **162 tok/s vs 52 tok/s**baseline and runs in- **6GB RAM**.- [Baseten](https://x.com/baseten/status/2065100012934095171)made- **Inception Mercury 2**available, claiming diffusion-LLM serving at- **1,000+ tok/s**, with early users seeing- **82% latency reduction**and- **90% cost savings**.
- **MiniMax and Together emphasized kernel/systems work behind long-context serving**:- [MiniMax](https://x.com/RyanLeeMiniMax/status/2065010795625562486)open-sourced its high-performance- **MSA kernel library**, with model weights expected shortly after;- [iamgrigorev](https://x.com/iamgrigorev/status/2065074479621935355)pointed to the paper release.- [Together](https://x.com/togethercompute/status/2065109302717669392)described the serving work behind- **M3**:- **KV-block-major sparse attention**, MSA integration with paged KV cache, decode index scoring optimizations, and moving multimodal preprocessing into a- **Rust gateway**before GPU workers.- [charles_irl](https://x.com/charles_irl/status/2065148183412695282)also published a post on FlashAttention-4 inference improvements and upstream contributions, showing that performance deltas increasingly come from- **end-to-end serving stack choices**, not just model architecture.

**Agents, developer tooling, and managed execution**

- **Managed agents are becoming schedulable, credential-aware infra primitives**:- [ClaudeDevs](https://x.com/ClaudeDevs/status/2065080005328249086)added- **scheduled deployments**and- **environment variables**to Claude Managed Agents, enabling recurring jobs and CLI/API auth without exposing secrets to the model; credentials are swapped at the network boundary (- [details](https://x.com/ClaudeDevs/status/2065080009203892302)).- [Perplexity](https://x.com/perplexity_ai/status/2065124930463916317)integrated- **Deep Research as a native skill inside Computer**, backed by its “search as code” architecture (- [details](https://x.com/perplexity_ai/status/2065124948793028691)). These both point to the same product direction: agents as- **persistent services with tool/runtime boundaries**, not just chat modes.
- **Hermes, Devin, Cursor, GitHub Copilot and LangSmith all pushed further into operational tooling**:- [Teknium](https://x.com/Teknium/status/2065060810729414695)unified profile management in- **Hermes Agent**, then added remote file access in the desktop app (- [remote files](https://x.com/Teknium/status/2065112576552526168)).- [Cognition](https://x.com/cognition/status/2065156301668171873)and- [imjaredz](https://x.com/imjaredz/status/2065153770762154186)open-sourced- **/handoff**, letting local coding agents offload jobs to cloud Devins.- [Cursor](https://x.com/cursor_ai/status/2065137803084857845)made- **auto-review**the default for new users with a classifier subagent gating actions, claiming- **97% accuracy**.- [Microsoft](https://x.com/MicrosoftAI/status/2065133021049782491)rolled out- **MAI-Code-1-Flash**across Copilot tiers, while- [pierceboggan](https://x.com/pierceboggan/status/2065130447630487821)emphasized support for both model and harness choice.- [LangChain](https://x.com/LangChain/status/2065090475913068766)launched- **LangSmith LLM Gateway**with spend limits, PII/secrets detection, trace continuity, and audit logging. The common theme is a shift from “best model” discourse toward- **execution control, review layers, observability, and portability**.

**Top tweets (by engagement)**

- **Fable 5 product discourse dominated attention**: the highest-engagement technical-adjacent posts were highly anecdotal but still informative about perception.- [aaronli’s claim that Fable 5 “solved CAD”](https://x.com/aaronli/status/2064876123109089742)drew major attention, while- [KradleAI’s thread claiming Fable 5 “lies 96% of the time”](https://x.com/kradleai/status/2064907897373642912)captured the opposite pole: high capability mixed with trust concerns.
- **DiffusionGemma’s speed became a breakout systems story**:- [Demis Hassabis’s post](https://x.com/demishassabis/status/2064873362799600042)on- **4× faster**text diffusion for Gemma drove unusually high engagement for an inference/systems topic, suggesting strong appetite for non-autoregressive speedups that actually ship.
- **AI economics and pricing got broad traction**:- [Kim Monismus’s post](https://x.com/kimmonismus/status/2064987311402537184)arguing that premium AI subscriptions are massively subsidized—estimating- **$8k equivalent usage for Claude Max 20x**and- **$14k for ChatGPT Pro 20x**—was one of the more widely shared technical-business threads, especially alongside reports that- [OpenAI may consider token price cuts](https://x.com/kimmonismus/status/2065043333941207160).

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
