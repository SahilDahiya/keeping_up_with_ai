---
title: '[AINews] Open Models, Model Labs vs Agent Labs, and What''s Untrainable —
  Sarah Guo'
topic: models
subtopic: releases
secondary_topics:
- agents/planning
summary: Discusses open models, model labs versus agent labs, and what remains hard
  to train directly.
source: latent-space
url: https://www.latent.space/p/ainews-open-models-model-labs-vs
author: Latent Space
published: '2026-06-11'
fetched: '2026-07-11T05:10:32Z'
classifier: codex
taxonomy_rev: 1
words: 1617
content_sha256: 5432196142f263f8fc3da57fc50b4760e75695f37091f9063d4c60f3a0b402e6
---

# [AINews] Open Models, Model Labs vs Agent Labs, and What's Untrainable — Sarah Guo

# [AINews] Open Models, Model Labs vs Agent Labs, and What's Untrainable — Sarah Guo

### a quiet day lets us reflect on a great essay

Sarah Guo is a [friend of the pod](https://x.com/TheTuringPost/status/2061901518522188251?s=20) and [Queen of AI](https://open.spotify.com/episode/2FIOWcKF1Mnl2Nh1UJHJ2H), and after our [Satya crossover pod](https://www.latent.space/p/satya-2026) (great [recap here from Gokul Rajaram](https://x.com/gokulr/status/2064837699568300344)) wrote an excellent article on [her Substack](https://saranormous.substack.com/p/the-untrainable?r=1o4vkp&utm_campaign=post&utm_medium=web&triedRedirect=true). Go read it, and come back for this reaction:

![](https://substackcdn.com/image/fetch/$s_!76lN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F709bf7b6-3173-4a7f-9099-fcabd2ebd438_1954x2078.png)

This framework (based on [legibility, another worthwhile concept if you are unfamiliar](https://www.youtube.com/watch?v=96S_64ipHOA)) simultaneously addresses a lot of the themes we have discussed on the Satya pod, but also Latent Space over the last two years:

- **The Place of Open Models:**With Braintrust in 2024 we were- [maximally bearish on Open Model adoption](https://www.latent.space/p/braintrust?utm_source=publication-search), only to turn around by our- [Pmarca](https://www.latent.space/p/pmarca),- [Cursor](https://www.latent.space/p/cursor-third-era), and- [Notion in 2026](https://www.latent.space/p/notion?utm_source=publication-search)pods
- [Agent Labs vs Model Labs](https://www.latent.space/p/agent-labs?utm_source=publication-search):- [the Devin is in the Details](https://www.swyx.io/cognition)- **doing unglamorous work**: arranging a company’s private reality so a model can act on it, handing the model the tools to act, working with the customer to change the reality of its workforce. A company that brings the translation is tough to copy – and the translation never ends. Integration and maintenance run as long as the relationship does,- **won by teams that put domain-specialized engineers and tools next to the customer**.”
- **Free Verifiable Benchmarks**: Why labs like Anthropic were so quick to pick up- [FrontierCode](https://www.latent.space/p/ainews-frontiercode-benchmarking)for the- [Fable launch](https://www.latent.space/p/ainews-anthropic-claude-fable-5-mythos), and why Sarah agrees, even with us, that “The most cited benchmark score of the year is a map of- **territory about to be worthless**, and a notice of who is about to lose the right to say what counts as good.”

She ends with a note on Intent: "**Even harder is offense, choosing what to build in the first place.** That’s what I spend the year looking for, and I find it maybe three times. The model is no help there. It will do whatever you point it at and can’t tell you what’s worth pointing it at, and you can’t benchmark that, so you can’t train it. It’s also the reason the incumbents don’t take everything: they keep the ground they have, and the next thing comes from someone who finds a use before the rest of us. Maybe intent is an even scarcer input than compute.”

AI News for 6/9/2026-6/10/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Anthropic’s Fable/Mythos rollout, silent capability gating, and the trust backlash**

- **Silent degradation of AI R&D help dominated the discourse**: A large share of technical tweets focused on Anthropic apparently degrading model performance on AI research-related prompts without clear up-front disclosure, rather than hard-refusing those requests. Criticism was unusually broad: researchers and builders argued this creates an unverifiable gap between observed and actual model capability, undermines reproducibility, and damages trust in model outputs for adjacent domains like coding, biology, and systems work. Representative critiques came from- [@natolambert](https://x.com/natolambert/status/2064699044145095104),- [@martin_casado](https://x.com/martin_casado/status/2064727048460058937),- [@drfeifei](https://x.com/drfeifei/status/2064735920281313688),- [@antirez](https://x.com/antirez/status/2064766431531532588),- [@ClementDelangue](https://x.com/ClementDelangue/status/2064673792303955985), and- [@deanwball](https://x.com/deanwball/status/2064665679307985244). Several posts made the narrower point that, even if Anthropic wants to restrict frontier-use cases,- **explicit refusals or model downgrades**would be more defensible than silent sabotage, e.g.- [@hlntnr](https://x.com/hlntnr/status/2064733332882026565),- [@](https://x.com/_arohan_/status/2064644778147643401)- [arohan](https://x.com/_arohan_/status/2064644778147643401)- [@DBahdanau](https://x.com/DBahdanau/status/2064692204287799728).
- **Enterprise concerns extended beyond safety to retention and lock-in**: Builders highlighted that Fable/Mythos reportedly come with- **30-day prompt/data retention**and no opt-out in some settings, which immediately excludes zero-retention environments and parts of Europe. See- [@GergelyOrosz](https://x.com/GergelyOrosz/status/2064618497150210391)on prompt-history retention and opaque model changes, and- [@scaling01](https://x.com/scaling01/status/2064685085379477742)on zero-data-retention incompatibility. A second-order lesson repeated by multiple practitioners: treat frontier APIs as unstable dependencies, maintain model portability, and verify outputs continuously with evals and harnesses, as argued by- [@dbreunig](https://x.com/dbreunig/status/2064751540003643738),- [@omarsar0](https://x.com/omarsar0/status/2064753171214299209), and- [@yacineMTB](https://x.com/yacineMTB/status/2064801103447736398).
- **Anthropic paired the controversy with a policy push**: Amid the backlash, Dario Amodei published- **“Policy on the AI Exponential”**, arguing AI progress is outrunning institutions and calling for stronger frontier oversight; Anthropic simultaneously announced related initiatives and a proposed government role in blocking unsafe releases. See- [@DarioAmodei](https://x.com/DarioAmodei/status/2064781775247950326)and- [@AnthropicAI](https://x.com/AnthropicAI/status/2064783418844762489). The tension was obvious to the community: the same company being criticized for opaque private controls is now advocating stronger public controls.

**Fable 5’s benchmark strength and product performance despite the controversy**

- **Fable 5 appears genuinely strong on agentic and coding workloads**: Even many critics of Anthropic’s policy acknowledged the model itself is excellent. Community reports had it leading or near-leading on a wide mix of evaluations:- [Agent Arena](https://x.com/arena/status/2064807170714358193)showed- **#1 overall**with especially large margins in confirmed task success and user praise, albeit weaker steerability;- [@mchlhess](https://x.com/mchlhess/status/2064734182648221952)said it “completely demolishes” his benchmark;- [@JasonBotterill](https://x.com/JasonBotterill/status/2064699951578505446)noted- **81.9% on SimpleBench**;- [@lvwerra](https://x.com/lvwerra/status/2064758389406589134)reported- **#1 on CADGenBench**;- [@scaling01](https://x.com/scaling01/status/2064812046902817051)highlighted strong computer-use results; and- [@LechMazur](https://x.com/LechMazur/status/2064815890651140447)flagged- **#1 on PACT**negotiation.
- **Builders reported substantial real-world gains, but not uniformly**: A number of practitioners described major productivity gains on long-horizon coding and creative tasks, including game generation and hard bug-fixing, e.g.- [@kimmonismus](https://x.com/kimmonismus/status/2064744343349399634),- [@walden_yan](https://x.com/walden_yan/status/2064755974548902006), and- [@hrishioa](https://x.com/hrishioa/status/2064717079526383699). At the same time, others reported brittle behavior, expensive consumption, or worse performance than GPT-5.5 on specific tasks, such as- [@Sentdex](https://x.com/Sentdex/status/2064738018255159363)and- [@QuixiAI](https://x.com/QuixiAI/status/2064771682397569364). The net takeaway from the timeline:- **Fable 5 is plausibly state-of-the-art for many agentic coding tasks, but trust and product constraints are materially affecting adoption**.
- **Distribution and integration moved quickly**: Perplexity added- **Claude Fable 5 as an orchestrator model**in Computer for Pro/Max users via- [@perplexity_ai](https://x.com/perplexity_ai/status/2064771411894567373)and- [@AravSrinivas](https://x.com/AravSrinivas/status/2064775723886182427). Apple developers got- **Foundation Models framework support for Claude**for multi-step reasoning, longer context, and code use via- [@ClaudeDevs](https://x.com/ClaudeDevs/status/2064756984617021807). Community behavior also suggested substitution pressure toward OpenAI/Codex after the backlash, including- [@dylan522p](https://x.com/dylan522p/status/2064727949274955953)reporting usage share moving from Anthropic toward OpenAI.

**Google’s DiffusionGemma release and renewed interest in diffusion LLMs**

- **Google released DiffusionGemma under Apache 2.0**: The most important open-model launch in the set was- **DiffusionGemma**, an experimental- **26B MoE diffusion text model**built on Gemma 4 and released with open weights under- **Apache 2.0**. Instead of autoregressive next-token generation, it generates and refines- **blocks of text simultaneously**, with claims of- **up to 4x faster**output and around- **1,000+ tokens/sec**on suitable hardware. See- [@Google](https://x.com/Google/status/2064741293163418032),- [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2064741061352636762),- [@googlegemma](https://x.com/googlegemma/status/2064741002204545467), and- [@sundarpichai](https://x.com/sundarpichai/status/2064744343743922189).
- **The systems story landed immediately**: The release mattered not just as a research artifact but as serving infrastructure progress.- [@vllm_project](https://x.com/vllm_project/status/2064753414735900835)said DiffusionGemma is the first diffusion LLM natively supported in- **vLLM**, citing- **1200+ output tok/s**at batch size 1 on a single H200 with FP8.- [@danielhanchen](https://x.com/danielhanchen/status/2064760001567306232)showed it running locally via- **llama.cpp**with GGUFs;- [@UnslothAI](https://x.com/UnslothAI/status/2064743714875220118)emphasized local execution on- **18GB-class**hardware; and- [@_philschmid](https://x.com/_philschmid/status/2064745464252055647)summarized the inference footprint as- **3.8B active params**and- **256-token block denoising**.
- **Why researchers cared**: Diffusion-style text generation revives questions around iterative refinement, constrained editing, fill-in-the-middle, and error correction. Multiple reactions framed it less as a productized competitor and more as a fertile research direction for- **non-sequential decoding**and refinement-heavy tasks; see- [@omarsar0](https://x.com/omarsar0/status/2064742095387005352),- [@mervenoyann](https://x.com/mervenoyann/status/2064753402064601181), and- [@dbreunig](https://x.com/dbreunig/status/2064752321817719204).

**Agent tooling, infra, and benchmarks: more structure around real workloads**

- **Benchmarks are shifting from preference to trace-based agent metrics**:- [@arena](https://x.com/arena/status/2064748918135824876)detailed the methodology behind- **Agent Arena**, which mines long-horizon traces for objective signals like bash errors, tool hallucination, and “insanity” rather than relying on human preference for every step. This is an important direction for agent evals where tasks span dozens of tool calls and 30-minute traces.
- **Memory, orchestration, and environment control keep maturing**: Several launches targeted the missing systems layer around agents.- [@Teknium](https://x.com/Teknium/status/2064764570519146935)shipped GUI-based- **Hermes Agent profiles**and later- **Write Gate**approval controls for memory/skill updates via- [@Teknium](https://x.com/Teknium/status/2064831491130130879).- [@weaviate_io](https://x.com/weaviate_io/status/2064703135902216618)described structured agent memory using groups, topics, and scopes in- **Engram**.- [@bromann](https://x.com/bromann/status/2064760446847168811)argued for bringing client-side/browser capabilities into the agent loop.- [@FactoryAI](https://x.com/FactoryAI/status/2064764834928107914)launched- **Missions**on Factory Desktop.
- **Detection, routing, and community harnesses**:- [@perceptroninc](https://x.com/perceptroninc/status/2064732691845824833)launched- **Agentic Detection**, using multi-call zoom/reason loops for dense ambiguous visual detection instead of a one-shot detector;- [@vllm_project](https://x.com/vllm_project/status/2064679109406740827)highlighted- **Inferoa**, a community agent harness optimized around inference economics; and- [@Azaliamirh](https://x.com/Azaliamirh/status/2064810291574305013)introduced- **DeLM**, a decentralized multi-agent framework that reportedly reaches- **65.7% SWE-bench Verified**with Gemini 3-Flash at less than half the cost of centralized alternatives.

**Optimization, retrieval, and scientific-modeling work worth tracking**

- **Distributed Shampoo vs Muon remained a live optimization thread**: A technically interesting sub-thread showed tuned- **Meta DistributedShampoo**matching strong Muon baselines on a speedrun-style task after hyperparameter tuning and enabling pseudo-inverse stabilization.- [@](https://x.com/_arohan_/status/2064631528806908134)- [arohan](https://x.com/_arohan_/status/2064631528806908134)- **3.2766**with vanilla package + tuning, while- [@kellerjordan0](https://x.com/kellerjordan0/status/2064761560732713360)pushed back on calling it “vanilla” because the critical stabilization flag was undocumented. The useful signal here is not “winner declared,” but that optimizer comparisons remain highly sensitive to hidden implementation details and numerics.
- **Late-interaction retrieval got better kernels**:- [@tonywu_71](https://x.com/tonywu_71/status/2064701365318767100)released- **late-interaction-kernels**, fused Triton kernels for MaxSim used in ColBERT/ColPali/LateOn, claiming numerical equivalence to PyTorch at a fraction of the memory footprint. This should matter for both training and serving multi-vector retrieval models.
- **Scientific and multimodal modeling**:- [@giffmana](https://x.com/giffmana/status/2064718736783823145)highlighted new work showing- **diffusion video models**linearly encode physical information better than V-JEPA/VideoMAE on some probes, challenging a common “videogen models are dumb physics simulators” narrative. In biotech,- [@edunov](https://x.com/edunov/status/2064774943766925696)introduced- **DeCAF-Pearl**, a flow-map cofolding model reportedly- **~5x faster**than Pearl while maintaining quality. On architecture research,- [@ZyphraAI](https://x.com/ZyphraAI/status/2064842130447851947)released- **Zamba2-VL**under Apache 2.0, extending hybrid SSM-Transformer ideas into VLMs.

**Top tweets (by engagement)**

- **Policy / governance**:- [@DarioAmodei on “Policy on the AI Exponential”](https://x.com/DarioAmodei/status/2064781775247950326)was the highest-engagement technical/policy post, framing frontier AI as advancing faster than institutions can react.
- **Security / safety failure mode**:- [@jsrailton](https://x.com/jsrailton/status/2064661778978533571)drew major attention to malware authors embedding nuclear/biological text to trigger LLM refusals and evade AI malware analysis—a concrete example of attackers exploiting safety behavior.
- **Open models**:- [@googlegemma](https://x.com/googlegemma/status/2064741002204545467)and- [@Google](https://x.com/Google/status/2064741293163418032)on- **DiffusionGemma**were the biggest pure model-release posts.
- **Research access norms**:- [@drfeifei](https://x.com/drfeifei/status/2064735920281313688)concisely stated the broad consensus from academia: scientific progress requires access to the best tools, including AI.
- **Model capability signal**:- [@mchlhess](https://x.com/mchlhess/status/2064734182648221952)saying- **Fable 5 “completely demolishes”**his benchmark became one of the most-cited capability endorsements.

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Open-Weight Model Drops: North Mini Code and DiffusionGemma**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
