---
title: '[AINews] Lilian Weng summarizes 35 papers on Harness Engineering for RSI'
topic: agents
subtopic: planning
secondary_topics:
- models/reasoning
summary: Summarizes harness-engineering papers through Lilian Weng’s lens, connecting
  agent structure with recursive improvement.
source: latent-space
url: https://www.latent.space/p/ainews-lilian-weng-summarizes-35
author: Latent Space
published: '2026-07-08'
fetched: '2026-07-11T05:09:21Z'
classifier: codex
taxonomy_rev: 1
words: 1804
content_sha256: 4f47438e2bb835c9fc3d6e60ffa91023b0440be858aee02e5ae7a4680ee504d3
---

# [AINews] Lilian Weng summarizes 35 papers on Harness Engineering for RSI

# [AINews] Lilian Weng summarizes 35 papers on Harness Engineering for RSI

### a quiet day lets us read some condensed insight

Congrats to Meta Superintelligence on [having the top 2/3 image/video models](https://x.com/AIatMeta/status/2074577662840832382) in the world! This would’ve been a candidate for a title story, but unfortunately that is pretty much all the detail we have about Muse Image/Video - no paper, no technical detail whatsoever. Still, this beats [the Microsoft MAI models from last month](https://www.latent.space/p/ainews-microsoft-build-mai-thinking) which is nice.

We are noted [Lilian Weng fans](https://news.smol.ai/issues?pattern=lilian%2520weng), so we take notice whenever she drops another research recap, especially rare now that she is a cofounder at Thinky. Today she is thinking about the relationship of harnesses to RSI:

![X avatar for @lilianweng](https://substackcdn.com/image/fetch/$s_!FaQj!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1923619459643711488%2FqmXOBhZ1.jpg)

While we have written before about how [even Greg Brockman is now quietly endorsing agent/harness engineering](https://www.latent.space/p/ainews-all-model-labs-are-now-agent?utm_source=publication-search), it is refreshing for a respected thinker and neolab cofounder like Lilian to also agree that “*Even when many harness improvement[s] get eventually internalized into core model,  the need to specify goals and context will not disappear*.”

![](https://substackcdn.com/image/fetch/$s_!BNEu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5005c722-fdff-4ea8-aee0-6b37e44da978_1512x886.png)

[Her post](https://lilianweng.github.io/posts/2026-07-04-harness/#harness-layer-vs-core-intelligence) breaks out the main proven design trends in harnesses that everyone should know, and then recaps the harness optimization literature, most notably from the well [known ACE paper](https://arxiv.org/abs/2510.04618) to even more recent trends like [Meta-Harnesses](https://arxiv.org/abs/2603.28052),  which we have [covered anecdotally on AINews](https://www.latent.space/p/ainews-its-meta-harness-summer).

![](https://substackcdn.com/image/fetch/$s_!L_Ci!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F603a46c6-cedc-4b38-a660-2fa1d4b3f4ba_1626x1146.png)

It surely also provides a hint as to what Thinky is Thinking, beyond just [Interaction Models](https://www.latent.space/p/ainews-thinking-machines-native-interaction?utm_source=publication-search).

AI News for 7/06/2026-7/07/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Agent Products, Harnesses, and Long-Running Workflows**

- **Anthropic expands “background agent” UX on top of Claude**: The biggest product launch by engagement was- [Claude Cowork coming to mobile and web](https://x.com/claudeai/status/2074525815820169320), positioning Claude as a task-running background teammate rather than a foreground chat UI. Related posts show the product convergence around a shared home tab and tighter Chat/Cowork integration from- [@mikeyk](https://x.com/mikeyk/status/2074531605537046953). Separately, Anthropic extended access to- **Claude Fable 5**on paid plans through July 12 in a highly engaged announcement from- [@claudeai](https://x.com/claudeai/status/2074548242386178258), though many users noted the awkward timing relative to weekly limits in reactions from- [@kimmonismus](https://x.com/kimmonismus/status/2074606005963391225)and others.
- **Harness engineering is increasingly the center of agent design**: Lilian Weng’s new post was widely referenced as reframing recursive self-improvement around the- **harness**, not direct weight self-modification; Sakana’s summary connects this to- **The AI Scientist**,- **ShinkaEvolve**, and- **Darwin Gödel Machine**in- [their thread](https://x.com/SakanaAILabs/status/2074489949529776308). LangChain echoed the same shift with a new- **Deep Agents**course and an open-source harness project in posts from- [@LangChain](https://x.com/LangChain/status/2074539083204820997)and- [@hwchase17](https://x.com/hwchase17/status/2074547871194698207). Google is also productizing this direction: Gemini API- **Managed Agents**added- **background execution**,- **remote MCP servers**,- **custom function calling**, and- **credential refresh**in posts from- [@_philschmid](https://x.com/_philschmid/status/2074533915038027972)and- [@OfficialLoganK](https://x.com/OfficialLoganK/status/2074552932318765376).
- **Practical agent infra keeps getting more opinionated**: There were several notable operator-facing updates:- **Codex Mobile iOS**added task management, filtered diffs, SSH key login, branch comparison, and attachment flows in posts from- [@Dimillian](https://x.com/Dimillian/status/2074396968223211819)and- [@reach_vb](https://x.com/reach_vb/status/2074400018769793176);- **Hermes Agent**added pluggable secrets managers plus native- **1Password**integration and export of sessions/datasets to formats including private Hugging Face repos in- [@Teknium’s](https://x.com/Teknium/status/2074564207555772912)- [threads](https://x.com/Teknium/status/2074639961727655959);- **Weaviate 1.38**made its MCP server GA with runtime-gated write access, notably allowing- **MCP_SERVER_WRITE_ACCESS_ENABLED**to be flipped live without restart in- [@victorialslocum’s post](https://x.com/victorialslocum/status/2074493681403339104). A more experimental pattern came from- [@omarsar0](https://x.com/omarsar0/status/2074506169352180108), using a Dial MCP server so agents can escalate decisions via phone call/SMS/iMessage for human-in-the-loop control.

**Model and Modality Releases: Audio, Speech, Robotics, and Media Generation**

- **Meta’s Muse Image/Muse Video push agentic generation into media**: Meta Superintelligence Labs launched- **Muse Image**and previewed- **Muse Video**in announcements from- [@AIatMeta](https://x.com/AIatMeta/status/2074577662840832382),- [@alexandr_wang](https://x.com/alexandr_wang/status/2074555909347369105), and- [@_tim_brooks](https://x.com/_tim_brooks/status/2074578008296628698). The notable technical angle is not just image quality, but an explicitly- **agentic generation loop**: planning, web search, tool use, code execution, and self-refinement before rendering. Meta also says performance improves with- **scaled test-time compute**, and that self-refinement behavior emerged during RL rather than being hand-scripted in- [this follow-up](https://x.com/AIatMeta/status/2074587864923250873). On public evals, Muse Image quickly reached- **#2 on Image Arena**behind GPT Image 2 in- [Arena’s ranking](https://x.com/arena/status/2074581979765539153), while Muse Video debuted at- **#3 on Video Arena**in- [another Arena post](https://x.com/arena/status/2074591193783320851).
- **NVIDIA and Cohere both shipped strong audio releases**: NVIDIA released- **Audex**, a- **30B parameter / 3B active MoE**with- **1M context**for unified text+audio work, summarized by- [@HuggingPapers](https://x.com/HuggingPapers/status/2074384562952749254)and described in more detail by- [@_weiping](https://x.com/_weiping/status/2074537900172050704). The model’s core claim is preserving text intelligence while adding broad audio generation and understanding via a single MoE backbone. Cohere launched- **Cohere Transcribe Arabic**, described as the most accurate open-source Arabic ASR model, under- **Apache 2.0**, with emphasis on- **dialects**,- **code-switching**, and- **Arabic-accented English**in posts from- [@cohere](https://x.com/cohere/status/2074499759616729149)and- [@JayAlammar](https://x.com/JayAlammar/status/2074511963934118282).
- **Open robotics keeps consolidating around Hugging Face + NVIDIA**: NVIDIA expanded its robotics stack into the HF ecosystem by bringing- **GR00T 1.7**and- **Isaac Teleop**into- **LeRobot**, aimed at open humanoid robotics workflows, in- [@NVIDIARobotics’s announcement](https://x.com/NVIDIARobotics/status/2074380795855147072)and- [integration guide](https://x.com/NVIDIARobotics/status/2074390485251113317). On the embodied side, UMA showed a strong full-stack robotics narrative:- [@RemiCadene](https://x.com/RemiCadene/status/2074442725814878510)described a prototype built by a small team in 9 months, while- [the Northstar reveal](https://x.com/RemiCadene/status/2074442439142609237)and- [@psermanet’s safety note](https://x.com/psermanet/status/2074512829617491996)emphasized vertically integrated hardware/software for trustworthy robots.

**Training, Inference, and Post-Training Techniques**

- **Liquid AI’s “Antidoom” directly targets reasoning-loop failure modes**: One of the clearest technical releases of the day was- [Liquid AI’s Antidoom](https://x.com/liquidai/status/2074494130126811473), an open-source training method to reduce- **doom loops**where small reasoning models repeat tokens until context exhaustion. The reported reductions are substantial:- **LFM2.5-2.6B from 10.2% → 1.4%**and- **Qwen3.5-4B from 22.9% → 1%**under greedy sampling, with downstream eval gains. The method,- **FTPO (Final Token Preference Optimization)**, relabels the loop-triggering token and redistributes probability toward alternatives, summarized well by- [@helloiamleonie](https://x.com/helloiamleonie/status/2074498103982408044)and- [@LiorOnAI](https://x.com/LiorOnAI/status/2074547819114086561). This is a good example of the field’s recent pattern: removing specific failure modes rather than only scaling parameters.
- **Inference efficiency and compression remain a major frontier**: NVIDIA’s- **Puzzle-75B-A9B**compression work got strong attention via- [@omarsar0](https://x.com/omarsar0/status/2074543978129793462): compressing a hybrid MoE parent model while preserving reasoning, coding, long-context, and agentic quality, with roughly- **2x server throughput**and- **1M-context concurrency on H100 rising from 1 request to 8**. On the tooling side,- **Nsight Python 1.0**launched in- [@HagedornBastian’s post](https://x.com/HagedornBastian/status/2074509770342445375), making GPU perf analysis scriptable in Python. Unsloth also shipped- **GGUFs for DeepSeek-V4-Flash**, plus export to- **NVFP4/FP8**and speedups for- **GRPO**and MoEs in- [@danielhanchen’s update](https://x.com/danielhanchen/status/2074510444778463331).
- **Agent RL and verification are getting more specialized**:- [@cwolferesearch](https://x.com/cwolferesearch/status/2074558199819067606)highlighted how- **GRPO-style normalization**is being adapted for agentic RL at the- **task**or- **environment**level to handle higher reward variance in multi-turn environments. Separately,- [@omarsar0](https://x.com/omarsar0/status/2074556579580711050)flagged a training-free- **verifier**paper from Stanford/NVIDIA/Berkeley that reads calibrated continuous scores off scoring-token logits, posting strong numbers across- **Terminal-Bench V2, SWE-Bench Verified, RoboRewardBench, and MedAgentBench**and suggesting verification is becoming an independent scaling axis.

**Interpretability, Model Internals, and the “J-Space” Debate**

- **Anthropic’s J-space work dominated interpretability discussion, but also drew sharp criticism**: The community split between seeing the work as useful mechanistic analysis and objecting to the consciousness framing. Strong critiques came from- [@danburonline](https://x.com/danburonline/status/2074429991576650014),- [@paul_cal](https://x.com/paul_cal/status/2074388528243310976), and- [@scaling01](https://x.com/scaling01/status/2074432865794679235), who argued the vectors are causal largely by construction under the Jacobian-lens definition. A useful historical reference came from- [@jacobandreas](https://x.com/jacobandreas/status/2074487546692735002), pointing readers back to the original- **Jacobian lenses**paper.
- **The stronger technical takeaway is cross-model structure, not consciousness rhetoric**:- [@eliebakouch](https://x.com/eliebakouch/status/2074532904009421260)computed- **CKA similarity**on J-lens geometry across- **38 open models**and found surprisingly universal layer/depth organization, even across unrelated families like- **Llama**and- **OLMo**. Anthropic and Neuronpedia also released- **J-lens weights for open models**, noted in- [this follow-up](https://x.com/eliebakouch/status/2074537985102565795). In parallel, Goodfire introduced- **Block-Sparse Featurizers**for multidimensional concepts in activations, arguing many vision concepts are inherently- **2–4 dimensional blocks**rather than single directions, in- [their thread](https://x.com/GoodfireAI/status/2074634702737281303).

**Benchmarks, Evaluations, and Domain-Specific Systems**

- **Agent and legal benchmarks continue to expose the gap between “passes many criteria” and “fully solves real work”**:- [Agent Arena](https://x.com/arena/status/2074484787663052849)placed- **Claude Sonnet 5 (Thinking)**at- **#6**, with strongest signals in confirmed task success and bash usage, but still with uncertainty around steerability. Artificial Analysis launched- **Harvey LAB-AA**, a legal-agent benchmark over- **120 private legal tasks across 24 practice areas**, where- **Claude Fable 5**led at- **14.2% all-pass rate**;- **Claude Opus 4.8**and- **GLM-5.2**tied at- **7.5%**, with GLM hitting that at roughly- **~6% of Fable’s cost per task**in- [their release](https://x.com/ArtificialAnlys/status/2074541975186165887). The big message is that models can satisfy many individual rubric items yet still fail to produce acceptable end-to-end deliverables.
- **Research automation and specialized domain systems are broadening**: Google promoted- **Experience AI Scientist**, a multi-agent system for end-to-end scientific workflows, in- [this ICML post](https://x.com/GoogleResearch/status/2074384746076135575). DeepMind also launched- **Predicting the Past**, grounding Gemini in- **Aeneas**and- **Ithaca**for Greek/Latin historical analysis via plain-English interactions, in- [their thread](https://x.com/GoogleDeepMind/status/2074513661750546762). On legal AI commercialization,- **Norm Ai**announced a- **$120M Series C at $1.2B valuation**and described a full-stack “agentic law” setup spanning software plus an AI-native law firm in- [@johnjnay’s post](https://x.com/johnjnay/status/2074485345593245833).

**Top tweets (by engagement)**

- **Claude access / product rollout**:- [Claude Cowork on mobile and web](https://x.com/claudeai/status/2074525815820169320)and- [Fable 5 access extended through July 12](https://x.com/claudeai/status/2074548242386178258)were the most-engaged technically relevant product announcements.
- **Open-source developer program**:- [@ClaudeDevs offering 6 months of Claude Max 20x for open-source maintainers](https://x.com/ClaudeDevs/status/2074570404035993780)drew massive engagement and is likely to matter for tool adoption in OSS ecosystems.
- **Meta media generation**:- [Muse Image launch](https://x.com/AIatMeta/status/2074577662840832382)and- [Arena’s #2 ranking for Muse Image](https://x.com/arena/status/2074581979765539153)were the biggest multimodal product stories.
- **Reasoning reliability**:- [Liquid AI’s Antidoom release](https://x.com/liquidai/status/2074494130126811473)stood out as the day’s highest-signal training technique post.
- **Interpretability**:- [Cross-model J-lens universality across 38 open models](https://x.com/eliebakouch/status/2074532904009421260)was the strongest technical follow-on to the J-space discourse.

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Open Model Releases and Inference Efficiency**

- [New open model from Tencent Hy: Hy3 (295B total 21B active - apache 2.0)](https://www.reddit.com/r/LocalLLaMA/comments/1uoozt4/new_open_model_from_tencent_hy_hy3_295b_total_21b/)- **Tencent released the non-preview Hy3 open model collection on**- [Hugging Face](https://huggingface.co/collections/tencent/hy3), described as a- `295B`- **-parameter MoE with**- `21B`- **active parameters, now under Apache 2.0 rather than the prior restrictive community license. The post highlights that the earlier license reportedly excluded use in regions including South Korea, the UK, and the EU, while top comments point to claimed benchmark gains over HY3-Preview and frame this as potentially relevant for high-end local/home inference setups.**Commenters viewed the Apache 2.0 relicensing as the most important change, especially given Tencent’s recent translation models also using Apache licensing. There was cautious optimism that the reported benchmark improvements may translate to real-world usefulness, but with implicit skepticism until tested outside vendor charts.- Commenters highlighted that - **Hunyuan/HY3**is now listed as- **Apache 2.0**, contrasting it with the prior “community” license that reportedly restricted usage in regions such as- **South Korea, the UK, and the EU**. This was viewed as technically important for deployment because Apache 2.0 removes many commercial and geographic usage barriers.
- Several users focused on whether Tencent’s claimed benchmark improvements over - **HY3-Preview**will translate into real-world workloads. Given the reported- `295B`- **total /**- `21B`- **active**MoE-style configuration, commenters suggested it could be relevant for “high-end home setups” if inference formats such as- **GGUF**become available.
- There was early speculation that HY3 could become an alternative to - **Qwen**and- **MiniMax**models in local/open-weight workflows, but commenters were waiting for quantized releases and independent testing before drawing conclusions.


## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
