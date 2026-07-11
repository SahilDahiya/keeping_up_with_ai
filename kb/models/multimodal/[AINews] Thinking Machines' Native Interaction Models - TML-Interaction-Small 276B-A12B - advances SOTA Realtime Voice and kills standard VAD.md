---
title: '[AINews] Thinking Machines'' Native Interaction Models - TML-Interaction-Small
  276B-A12B - advances SOTA Realtime Voice and kills standard VAD'
topic: models
subtopic: multimodal
secondary_topics:
- inference/serving
summary: Covers native interaction models for realtime voice and why VAD-free designs
  matter for conversational latency.
source: latent-space
url: https://www.latent.space/p/ainews-thinking-machines-native-interaction
author: Latent Space
published: '2026-05-12'
fetched: '2026-07-11T05:11:42Z'
classifier: codex
taxonomy_rev: 1
words: 2050
content_sha256: 7adfdea2ee5ce021eaaa1c201927004c10f3c91e67691b206369fff0a28b92d9
---

# [AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice and kills standard VAD

# [AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice and kills standard VAD

### well done, Team Thinky.

By complete coincidence, the day we [released](https://x.com/neilzegh/status/2053945753073074484?s=20) Neil Zeghidour (CEO of Gradium, the for profit spinoff of the vaunted [Kyutai Moshi](https://kyutai.org/))’s [talk](https://www.youtube.com/watch?v=P_RI1kCkRbo&time_continue=0&source_ve_path=MjM4NTE&embeds_referring_euri=https%3A%2F%2Fx.com%2F) on what remains to be built for realtime voice, **Thinking Machines** emerged for only the [third](https://news.smol.ai/issues/25-10-01-thinky) [time](https://news.smol.ai/issues/25-02-18-ainews-xai-grok-3-and-mira-muratis-thinking-machines) in a ~year (despite much drama) to drop [Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/), **TML-Interaction-Small** is a 276B parameter MoE with 12B active., which immediately advances the state of the art of realtime voice models as Neil had laid out, updating [the famously dead GPT 4o “her” demo](https://openai.com/index/hello-gpt-4o/) with far more detailed demos that are presumably far closer to real use:

The [full blogpost](https://thinkingmachines.ai/blog/interaction-models/) has lots of demos of the level of continuous interactivity, focusing on streams of “time-aligned microturns” of 200ms each:

![](https://substackcdn.com/image/fetch/$s_!LR03!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02190942-3f50-4067-ae03-97c6b504b3a3_1490x1592.png)

Using encoder-free early fusion, with images and audio all processed <200ms, similar to Meta’s [Chameleon](https://arxiv.org/abs/2405.09818):

![](https://substackcdn.com/image/fetch/$s_!S2rk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68576e99-b00a-4069-b93f-bbe906ddd810_1336x1602.png)

There are a number of official benchmarks that the team shows beating both [GPT-Realtime-2](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and) and [Gemini 3.1-Flash](https://www.latent.space/p/ainews-nano-banana-2-aka-gemini-31) on basic things like BigBench Audio and IFEval and FD-bench, but the level of interactivity aimed for required making 2 new internal benchmarks for time awareness, simultaneous translation, and visual proactivity:

- **TimeSpeak:**Can the model- **initiate speech**at user-specified times?- Example: “I want to practice my breathing, remind me to breathe in and out every 4 seconds until I ask you to stop.”

- **CueSpeak:**Can the model speak at the- **appropriate moment?**- Example: “Everytime I codeswitch and use another language, give me the correct word in the original language.”

- [RepCount-A](https://arxiv.org/abs/2204.01018)- **continuous visual tracking and timely counting**.
- [ProactiveVideoQA](https://arxiv.org/abs/2507.09313)
- [Charades](https://arxiv.org/abs/1604.01753)- Stream a user audio instruction: “Say ‘start’ when the person starts doing {action} then say ‘Stop’ when they stop.”


But look past the numbers: the single most visceral demo is this one buried at the bottom. Play the samples and feel the AGI:

![](https://substackcdn.com/image/fetch/$s_!V7pE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bfcadcb-b746-4873-aed4-6095f19f5897_1478x1676.png)

The closing notes leave tantalizing hints to Thinky’s roadmap, including an intriguing pairing of background agents with interactive models, which we like a whole lot.

![](https://substackcdn.com/image/fetch/$s_!PeGT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef289b1c-4613-4835-98e6-475906d494da_1394x588.png)

AI News for 5/9/2026-5/11/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Thinking Machines’ Native Interaction Models and the Shift Beyond Turn-Based AI**

- **Full-duplex multimodal interaction as a first-class model capability**: The day’s clearest technical theme was- [Thinking Machines’ preview of “interaction models”](https://x.com/miramurati/status/2053939069890298321), described as models trained- **from scratch**for real-time interaction rather than layering speech, turn-taking, and tool use onto a turn-based LLM. The accompanying- [technical post](https://x.com/thinkymachines/status/2053938892152435174)and team commentary from- [@johnschulman2](https://x.com/johnschulman2/status/2053940452789981426),- [@soumithchintala](https://x.com/soumithchintala/status/2053940215505645938), and- [@cHHillee](https://x.com/cHHillee/status/2053940218747842619)frame this as a- **human↔AI bandwidth**problem: models should be able to listen, speak, watch, think, search, and react concurrently. Demos emphasized continuous-time awareness, interruption handling, simultaneous speech, visual proactivity, and background tool use without explicit “now I’m thinking / now I’m searching” boundaries. Team members also highlighted that many tasks that previously needed special-purpose systems become zero-shot once the type signature is effectively continuous- **audio+video+text → audio+text**(- [@johnschulman2](https://x.com/johnschulman2/status/2053940940885332028)).
- **Why it matters technically**: Several reactions converged on the same point: this is not “another chatbot demo” but a change in interface assumptions.- [@liliyu_lili](https://x.com/liliyu_lili/status/2053942465477197891)pointed to- **visual proactivity**(“tell me when I start slouching”, “count my pushups”) as a missing primitive in current systems;- [@rown](https://x.com/rown/status/2053950123139575863)called it the first general- **video+speech**model that is visually proactive;- [@kimmonismus](https://x.com/kimmonismus/status/2053952846064767384)and- [@giffmana](https://x.com/giffmana/status/2053953584300003405)both emphasized that native interactivity is the deeper innovation than raw benchmark claims. This launch also implicitly raises the bar for “realtime” multimodal systems, as noted by- [@swyx](https://x.com/swyx/status/2053960011748098462). One implementation detail surfaced via- [@eliebakouch](https://x.com/eliebakouch/status/2053982248253190180): the stack is using- **SGLang**.

**OpenAI’s Enterprise and Security Push: Deployment Company and Daybreak**

- **OpenAI is moving down-stack into services and deployment**: OpenAI announced the- [OpenAI Deployment Company](https://x.com/OpenAI/status/2053824997777457651), a majority-owned unit built to help enterprises deploy frontier models into real workflows. The key operating detail is- **150 Forward Deployed Engineers and Deployment Specialists**coming in via the acquisition of- [Tomoro](https://x.com/OpenAI/status/2053824999736410415), with- [@gdb](https://x.com/gdb/status/2053884619695730745)citing- **$4B of initial investment from 19 partners**. Multiple observers read this as OpenAI adopting a Palantir-/Microsoft-style field-engineering model:- [@kimmonismus](https://x.com/kimmonismus/status/2053844403488194827)argued OpenAI wants to own the- **deployment layer**of the AI economy, while- [@matvelloso](https://x.com/matvelloso/status/2053881988529139765)connected it to the historical enterprise success pattern of embedding technical staff close to customer operations.
- **Daybreak: security-specific model distribution, workflow, and trust tiers**: OpenAI also launched- [Daybreak](https://x.com/OpenAI/status/2053939702110269822), an umbrella effort around defensive cyber operations and continuously securing software, with- [@sama](https://x.com/sama/status/2053951874408276193)positioning it as a practical response to rapidly improving AI cyber capability. The product pitch, summarized by- [@TheRundownAI](https://x.com/TheRundownAI/status/2053945340592631843), combines- **GPT-5.5**,- **Codex**, repository threat modeling, vuln discovery, patch generation, and response automation, with differentiated access tiers including- **Trusted Access for Cyber**and a more specialized- **GPT-5.5-Cyber**. This stands in contrast to Anthropic’s more restrictive cyber posture, a tension captured by- [@kimmonismus](https://x.com/kimmonismus/status/2053941490490265661). For teams building secure agent systems, a separate warning from- [@lukOlejnik](https://x.com/lukOlejnik/status/2053758553723211988)is relevant:- **“Your LLM is not a security boundary”**—Microsoft Semantic Kernel reportedly allowed prompt injection to be turned into host-level RCE because the framework over-trusted model output rather than the model itself failing.

**Agent Harnesses, Local-First Tooling, and Control Surfaces**

- **Better agent control planes are becoming a product category**: A recurring complaint is that useful agents need autonomy, but engineers still want reversible, inspectable control.- [@itsclelia](https://x.com/itsclelia/status/2053716807748567329)addressed this with- **aggit**, a Rust CLI for local/remote, S3-backed storage of agent artifacts, enabling stash/branch/restore semantics outside the main Git history. In the same vein,- [@_catwu](https://x.com/_catwu/status/2053999857799672111)highlighted a new- `claude agents`terminal control plane for managing multiple Claude Code agents, and- [@cursor_ai](https://x.com/cursor_ai/status/2053939390410612988)pushed Cursor into- **Microsoft Teams**, where the agent reads the full thread and opens a PR. These are all signs that “agent orchestration” is converging on concrete UX patterns rather than prompt tricks alone.
- **Deep Agents / Hermes / local agents are maturing quickly**:- [@masondrxy](https://x.com/masondrxy/status/2053717333433340034)noted that- **Deep Agents CLI**can hot-swap underlying model providers- **mid-conversation without losing context**, a nontrivial systems capability that many agent stacks still miss. LangChain also highlighted- **harness profiles**for provider/model-specific tuning (- [tweet](https://x.com/masondrxy/status/2053882188870074848)), and separate pricing analysis from the same author argued that- **DeepSeek V4 Flash**can be dramatically cheaper than GPT/Gemini flash-tier options for high-volume agent workloads (- [tweet](https://x.com/masondrxy/status/2053855842076942555)). On the local side, Hugging Face added- [Hermes Agent support in local apps plus native trace visualization](https://x.com/mervenoyann/status/2053857347429151163), while- [@Teknium](https://x.com/Teknium/status/2053961675985113404)previewed- **computer use with any model**via Hermes Agent and CUA, explicitly targeting local/open models as well as frontier APIs.- [@onusoz](https://x.com/onusoz/status/2053812410730037256)joining Hugging Face to improve local models in- **OpenClaw**and related open harnesses is another strong signal that local agent ergonomics are now strategic infrastructure.
- **A design thesis emerging around tools**:- [@threepointone](https://x.com/threepointone/status/2053751241977594102)argued that agents may asymptotically want just- **two primitive tools: search and execute**, with dynamic semantic discovery of capabilities rather than ever-expanding static tool menus. That complements the broader move toward configurable harnesses instead of giant monolithic prompts.

**Benchmarks, Efficiency, and Open-Model Economics**

- **Coding-agent benchmarking is finally measuring harness+model pairs**:- [Artificial Analysis launched a Coding Agent Index](https://x.com/ArtificialAnlys/status/2053865095076438427)spanning SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA, comparing not just models but- **model+harness combinations**. Their topline:- **Opus 4.7**in Cursor CLI scored- **61**, with- **GPT-5.5**in Codex/Claude Code close behind; top open-weight setups included- **GLM-5.1**,- **Kimi K2.6**, and- **DeepSeek V4 Pro**in Claude Code, still competitive but meaningfully behind. The benchmark also exposed large variation in- **cost per task**(>30x),- **token usage**(>3x),- **cache hit rates**(80–96%), and- **time per task**(>7x). That benchmark was complemented by OpenHands’ updated software-engineering benchmark announcement (- [tweet](https://x.com/OpenHandsDev/status/2053839810343620980)) and Claw-Eval’s more agentic task mix across office, finance, terminal, and web tasks, where- [MiMo-V2.5-Pro led and DeepSeek V4 Flash looked unusually efficient for its size](https://x.com/nathanhabib1011/status/2053786853929824385).
- **TurboQuant skepticism is increasing**: Multiple posts pointed to a more sober view of the recently popular quantization/serving technique.- [@_EldarKurtic](https://x.com/_EldarKurtic/status/2053809592061030546)presented what he described as the first comprehensive study of- **TurboQuant**, covering accuracy, latency, and throughput;- [@vllm_project](https://x.com/vllm_project/status/2053852636093239555)linked the Red Hat / vLLM investigation as a starting point; and- [@jbhuang0604](https://x.com/jbhuang0604/status/2053882357833208262)bluntly summarized the takeaway as “it doesn’t really work well.” This is exactly the sort of infra claim where independent reproduction matters.
- **Local/open models continue to improve faster than hardware ceilings**:- [@ClementDelangue](https://x.com/ClementDelangue/status/2053825719587815711)made the strongest high-level argument here: on the same top-end MacBook Pro memory ceiling, the “smartest open-weight model you can actually run” improved from Llama 3 70B-era capability to- **DeepSeek V4 Flash mixed-Q2 GGUF**-era capability at roughly- **4.7x in 24 months**, implying a doubling every- **10.7 months**, faster than Moore’s Law. Supporting datapoints came from- [@victormustar](https://x.com/victormustar/status/2053780086596288781)on the rapid growth of GGUF uploads and from repeated community observations that- **Qwen 3.6**,- **Gemma 4**, and DeepSeek variants are now usable locally for nontrivial agent tasks.

**Research Highlights: MoE Modularity, Diffusion/Byte Models, and Agent Dynamics**

- **Architectures and evaluation**: AllenAI’s- **EMO**was highlighted by- [@TheTuringPost](https://x.com/TheTuringPost/status/2053795343658303860)as a more modular Mixture-of-Experts design where document-level routing induces shared expert pools; notably, keeping only- **25% of experts**reportedly costs just- **~1%**performance versus- **10–15%**degradation in standard MoEs under similar pruning (- [follow-up](https://x.com/TheTuringPost/status/2053795410490339720)). On generative evaluation,- [@qberthet](https://x.com/qberthet/status/2053795951228371311)introduced- **MIND (Monge Inception Distance)**as a purportedly faster, more sample-efficient replacement for FID.
- **Diffusion for language and byte-level modeling**: Several papers pushed non-AR language modeling.- [@LucaAmb](https://x.com/LucaAmb/status/2053867347023466850)reported continuous bitstream diffusion nearly matching autoregressive models under their evaluation setup;- [@JulieKallini](https://x.com/JulieKallini/status/2053853543552217478)introduced- **Fast BLT**, using diffusion for parallel byte decoding to make byte-level LMs less inference-bound;- [@sriniiyer88](https://x.com/sriniiyer88/status/2053882384211419375)framed it as combining block byte-diffusion with self-speculative decoding. Relatedly,- [@LiangZheng_06](https://x.com/LiangZheng_06/status/2053806963839168619)noted a useful property of diffusion models for post-training: because sampling is differentiable, reward gradients can in principle flow straight to parameters more directly than in standard LLM setups.
- **Agent behavior under long horizons**: Two strong empirical threads surfaced. First,- [“The Memory Curse”](https://x.com/omarsar0/status/2053863994499408214)claims long histories degrade cooperation in multi-round social dilemmas because models become more- **history-following and risk-minimizing**, with explicit CoT sometimes amplifying the problem. Second,- [PwC work summarized by @dair_ai](https://x.com/dair_ai/status/2053866106151182419)argues that the value of clarification is highly time-dependent:- **goal clarification loses most of its value after ~10% of execution**, while input clarification remains useful longer. Together these suggest that long-horizon agent quality is constrained as much by memory/control policy as by raw model IQ.
- **Scaling and self-improvement**: Marin’s- **Delphi**scaling work, summarized by- [@WilliamBarrHeld](https://x.com/WilliamBarrHeld/status/2053919463880462453), claims a- **0.2%**prediction error when extrapolating from small pretrains to a- **25B / 600B token**run. Separately,- [@omarsar0](https://x.com/omarsar0/status/2053978221193130434)highlighted- **AutoTTS**, where an LLM searches the test-time scaling controller space itself, reportedly beating hand-designed strategies for about- **$39.9**of discovery cost.

**Top tweets (by engagement)**

- **OpenAI’s enterprise/services move**:- [OpenAI launches the Deployment Company](https://x.com/OpenAI/status/2053824997777457651)and- [Tomoro acquisition / 150 FDEs](https://x.com/OpenAI/status/2053824999736410415).
- **OpenAI’s security productization**:- [Daybreak announcement](https://x.com/OpenAI/status/2053939702110269822)and- [@sama’s framing](https://x.com/sama/status/2053951874408276193).
- **Thinking Machines’ interaction models**:- [Mira Murati’s launch tweet](https://x.com/miramurati/status/2053939069890298321)and the- [technical preview thread](https://x.com/thinkymachines/status/2053938892152435174).
- **Artificial Analysis Coding Agent Index**:- [benchmark launch and topline findings](https://x.com/ArtificialAnlys/status/2053865095076438427).
- **Agent tooling / developer workflow**:- [Hermes Agent computer use with any model](https://x.com/Teknium/status/2053961675985113404),- [Cursor in Microsoft Teams](https://x.com/cursor_ai/status/2053939390410612988), and- [Codex OpenAI Developers plugin](https://x.com/OpenAIDevs/status/2053925962287583379).

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Qwen 3.6 Local Inference Advances**

- [MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)- **The image (**- [link](https://i.redd.it/7qopol51pi0h1.png)) shows Unsloth’s Hugging Face profile listing newly published MTP-preserving GGUF builds:- `unsloth/Qwen3.6-27B-GGUF-MTP`- **and**- `unsloth/Qwen3.6-35B-A3B-GGUF-MTP`- **. The post’s technical significance is that these GGUFs retain the MTP / next-token prediction layers, but users still need to build a specific llama.cpp MTP PR rather than relying on standard llama.cpp support. One commenter reports a runtime/assertion failure with the 27B GGUF:**- `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`- **, suggesting either metadata parsing, model conversion, or PR compatibility issues remain unresolved.**Comments reflect anticipation for upstream llama.cpp MTP support, with users repeatedly checking the GitHub repo and asking whether MTP is now supported “out of the box.”- A user compiling the new - `27B`GGUF model hit a runtime assert in- `qwen35_mtp.cpp`:- `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`. This suggests the GGUF/model metadata or conversion path may be missing- `nextn_predict_layers`, which is required for Qwen3.5 MTP speculative/next-token prediction layers.
- One technical thread notes that - **MTP support in GGUF**is important for local inference, especially for the- `35B A3B`variant, which commenters associate with improved context-length handling. Another commenter asks whether this means- `llama.cpp`now supports MTP “out of the box,” implying uncertainty around whether support is merged/stable versus only available in a PR or fork.
- A commenter claims - `ik_llama`- **MTP is currently faster than the**- `llama.cpp`- **PR**, and adds that it supports Hadamard-based quants, described as similar to “turboquants.” This is a potentially relevant implementation/performance distinction for users comparing local MTP inference backends.


## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
