---
title: '[AINews] FrontierCode: Benchmarking for Code Quality over Slop'
topic: models
subtopic: benchmarks
secondary_topics:
- agents/computer-use
summary: Covers FrontierCode and the need for code-quality benchmarks that resist
  superficial generated-code quality.
source: latent-space
url: https://www.latent.space/p/ainews-frontiercode-benchmarking
author: Latent Space
published: '2026-06-09'
fetched: '2026-07-11T05:10:36Z'
classifier: codex
taxonomy_rev: 1
words: 1673
content_sha256: c91390ca5c8189b35e6fa09836be3d1e19c3ab6ad2f6bbc0f4c2bfd6345836b1
---

# [AINews] FrontierCode: Benchmarking for Code Quality over Slop

# [AINews] FrontierCode: Benchmarking for Code Quality over Slop

### We made a thing!

*Second batch of AI Leadership and Engineering+Workshops tickets for  AI Engineer World’s Fair sold out last night! Last 500 tickets on sale now - get while stocks last! 20% off for the first 20 readers who see this.*

It is rare that we are personally involved in the title story of the day, and [Apple’s WWDC announcing Gemini-powered Siri](https://www.youtube.com/watch?v=2TEeQjoY05c) was a possible candidate, but [we’ve been fooled before](https://news.smol.ai/issues?pattern=apple). So instead, we’ve got [FrontierCode](https://x.com/cognition/status/2064061031912288715), the latest in our [War on Slop](https://www.latent.space/p/2026)!

![X avatar for @cognition](https://substackcdn.com/image/fetch/$s_!oP98!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1765909640364068865%2FMvH-m0gd.jpg)

![](https://pbs.substack.com/media/HKT9bbsagAAipOJ.jpg)

If that chart looks familiar, it’s because FrontierCode was explicitly inspired and named for FrontierMath - focusing its hardest tier on extremely hard problems for frontier models 2 years ago:

![X avatar for @EpochAIResearch](https://substackcdn.com/image/fetch/$s_!9eJM!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1866142753127616512%2FDYcE9bN1.jpg)

![](https://pbs.substack.com/media/Gb4xR1VbkAA4zg8.png)

The context of FrontierCode revolves around past work we have done around [SWEBench-Verified](https://www.latent.space/p/swe-bench-dead).

- It is clear that even with the switch to SWEBench Pro, there has been insufficient articulation around - [WTF Happened in 2025](https://www.latent.space/p/wtf2025). As discussed with the OpenAI team in that podcast, there needed to be a lot more work around the rubrics for code quality and maintainability, and that is exactly what the Cog research team ended up building in this first release of FrontierCode.
- Separately, METR found that - [Many SWE-bench-Passing PRs Would Not Be Merged into Main](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/#introduction)and the problem of false positive trajectories (not quite “reward hacks”, but spiritually similar in terms of the unreliability of the benchmark rather than the model) was directly measured and addressed in the FrontierCode report.

With hindsight, FrontierCode’s third tier of problems shows the huge accceleration going into Dec 2025 that suddenly [made agentic engineering and vibe coding possible to go up one level of abstraction](https://x.com/swyx/status/2064081945567580323), to the /goals and loops and metaprompts we are discussing today.

![](https://substackcdn.com/image/fetch/$s_!sdBk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0acd2026-8f85-4504-a5f3-6a0cd82d0b6a_2170x1604.png)

[more context here](https://x.com/swyx/status/2064081945567580323)

AI News for 6/5/2026-6/8/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Coding Agents, Loops, and the Shift from “Passing Tests” to Mergeable Software**

- **FrontierCode raises the bar on coding evals**: Cognition introduced- **FrontierCode**, a new benchmark explicitly targeting whether code is actually- **mergeable**, not merely unit-test passing. Tasks were built with open-source maintainers, with each taking- **40+ hours**and evaluated on dimensions like regression safety, cleanliness, scope, test correctness, and maintainability. The headline result is that the best model,- **Opus 4.8**, scores only about- **13%**on the hardest subset—far below the 50%+ regime common on SWE-Bench-style evals, suggesting coding is much less “solved” than popular benchmarks imply (- [Cognition announcement](https://x.com/cognition/status/2064061031912288715),- [Scott Wu’s summary](https://x.com/ScottWu46/status/2064073699368800475),- [swyx breakdown](https://x.com/swyx/status/2064081945567580323),- [theo’s questions on variance/reproducibility](https://x.com/theo/status/2064126021088215385),- [Cognition response](https://x.com/cognition/status/2064215347503452649)).
- **“Loops” are becoming the dominant agent-control metaphor—but with caveats**: The day’s loudest practical theme was that coding agents should be given- **clear goals, verification criteria, and iteration structure**rather than one-shot prompts. Popular examples include- [dzhng’s “don’t use loops, design state machines”](https://x.com/dzhng/status/2063931263312892406),- [Claude Code’s retrospective on auto mode, routines, and verification](https://x.com/ClaudeDevs/status/2064032814392352816),- [bcherny’s thread](https://x.com/bcherny/status/2064034799711588805),- [OpenAI Codex tips on outcome-first prompting](https://x.com/reach_vb/status/2064028260070215772)and- [Approve-for-me defaults](https://x.com/reach_vb/status/2064044955421769755), plus- [LangChain OSS “rubrics”](https://x.com/sydneyrunkle/status/2064034061165682931). But several practitioners pushed back on naïve loop hype:- [Omar Sar0](https://x.com/omarsar0/status/2064024230396604469)and- [Graham Neubig](https://x.com/gneubig/status/2064011013637234728)emphasized that human checkpoints remain essential outside easily verifiable domains, while- [Hamel Husain](https://x.com/HamelHusain/status/2064019243990188259)joked about muting the word entirely.
- **Agent ergonomics are improving around verification and orchestration**: Product changes across the stack reflect this shift.- [ClaudeDevs added observability dashboards for MCP connector developers](https://x.com/ClaudeDevs/status/2064072801062121906), including adoption, latency, and error views.- [MagicPath launched a Builder plan](https://x.com/skirano/status/2064035120483352776)for external-agent workflows and multiplayer canvas editing.- [LangSmith Sandboxes](https://x.com/LangChain/status/2064030008738296065)and- [Modal’s sandbox scaling story](https://x.com/AmplifyPartners/status/2063998736703856737)point toward the same infrastructure trend: agents need isolated, inspectable, long-running environments.
- **Practical usage patterns are settling**: The strongest operator advice converged on measurable outcomes, bounded autonomy, and thread hygiene.- [Angaisb_ warned against overlong Codex threads degrading performance](https://x.com/Angaisb_/status/2064103464142065852), while- [reach_vb reported success with single-thread context accumulation](https://x.com/reach_vb/status/2064115851503059418). That mismatch itself is useful signal: current agent performance is still strongly shaped by- **harness behavior and workflow choices**, not just base-model quality.

**Model Releases, Local Inference, and Serving Stack Upgrades**

- **Kimi shipped both a stronger coding agent and a desktop agent product**: Moonshot released a major update to- **Kimi Code**, its open-source coding agent, adding- **one-line CLI install**, drag-and-drop- **video as coding context**, ACP support, plugins, and IDE integration (- [announcement](https://x.com/KimiDevs/status/2063981516708024369)). It also launched- **Kimi Work**, a desktop agent product with up to- **300 local sub-agents**, browser-use via extension, finance-focused tool access, and persistent memory (- [product launch](https://x.com/Kimi_Moonshot/status/2063990409903112344),- [desktop availability](https://x.com/crystalsssup/status/2063992904209842215)).
- **Google pushed hard on efficient local deployment**: Gemma got several notable upgrades. New- **QAT Gemma 4**checkpoints reportedly preserve performance while using- **~4x less memory**, with- **Gemma 4 E2B**fitting in about- **1GB**using a mobile quantization format (- [@_philschmid](https://x.com/_philschmid/status/2063990553826439378)). Separately,- **Gemma 4 MTP**was merged into- **llama.cpp**, enabling faster decoding when paired with QAT checkpoints (- [Gemma team](https://x.com/googlegemma/status/2064030477628182814)).- [llama.cpp also added video input support](https://x.com/osanseviero/status/2063985470489448887), expanding local multimodal use cases.
- **Open-source/open-weight competition remains intense**:- [Artificial Analysis reported MiniMax-M3 at 55 on its Intelligence Index](https://x.com/ArtificialAnlys/status/2064066303863005254), which would make it the leading open-weights model once weights are released. M3 adds- **native multimodality**and a- **1M token context window**, with strong GPQA/MMMU-Pro numbers but notable abstention on hallucination-sensitive evals. Meanwhile- [norpadon announced Apple-hardware-optimized quantized Qwen3.5 checkpoints](https://x.com/norpadon/status/2064040631479976240).
- **Serving infrastructure is broadening from text LLMs to world models and omni models**:- **vLLM-Omni 0.22.0**added day-0 support for- **NVIDIA Cosmos 3 world models**, robot serving APIs, TTS models such as- **Qwen3-TTS**and- **VoxCPM2**, faster image/video serving, and broader quantization/hardware coverage (- [release](https://x.com/vllm_project/status/2064013506882703421)). This reflects a broader trend toward generalized multimodal serving rather than text-only inference stacks.

**Benchmarks, Evaluation Methodology, and Real-World Agent Measurement**

- **Agent evaluation is moving from synthetic tasks to in-the-wild telemetry**: Arena launched- **Agent Arena**, a leaderboard based on over- **1M real-world sessions**, using- **causal tracing**rather than voting to estimate treatment effects of orchestrators/harnesses across five signals:- **confirmed success, praise vs complaint, steerability, bash recovery, and tool hallucination**(- [overview](https://x.com/arena/status/2064021507681276234),- [methodology thread](https://x.com/ml_angelopoulos/status/2064028763697127844)). Whether the methodology fully holds up remains to be seen, but it’s one of the clearest attempts yet to benchmark deployed agents using actual usage traces.
- **Specialized benchmarks keep proliferating into new output domains**: Hugging Face and Mecado released- **CADGenBench**, a benchmark for generating and editing- **engineering-grade 3D CAD parts**from drawings or STEP modifications, with metrics covering geometry, topology, interface compatibility, and CAD validity (- [launch thread](https://x.com/MikushRab/status/2063999885796614522),- [Thom Wolf summary](https://x.com/Thom_Wolf/status/2064029993638764672)). This is a meaningful shift: evaluation is expanding beyond text/code into structured artifacts where correctness is physical and geometric.
- **A recurring thesis: good benchmarks become training pipelines**:- [Ofir Press argued](https://x.com/OfirPress/status/2063990430350340575)that the best benchmarks are scalable and rooted in- **real-world crawled data sources**, making them useful not just for measurement but also for data generation. That view shows up implicitly in both FrontierCode and Agent Arena: benchmarks are no longer static scoreboards; they are becoming- **feedback loops for product and RL improvement**.

**Google, Apple, and the Consumer AI Platform Race**

- **Google expanded AI packaging, Search, and developer surfaces**: Google announced a more capable- **NotebookLM**with agentic chat, stronger reasoning, and more output formats for Ultra subscribers (- [launch](https://x.com/NotebookLM/status/2064016460964585549)). It also cut- **Google AI Plus**pricing from- **$7.99 to $4.99/month**while doubling storage to- **400GB**(- [pricing update](https://x.com/NewsFromGoogle/status/2064066310393209100)). On the platform side,- [Google highlighted a major Search upgrade](https://x.com/Google/status/2064034586762354893), including multimodal search and- **Gemini 3.5 Flash**as the new default in AI Mode.
- **Apple’s WWDC AI story centered on integration, not frontier leadership**: Commentary around WWDC focused on a rebuilt- **Siri AI**with on-screen awareness, app actions, personal context, and better voice interaction, alongside concerns about- **EU availability**and hardware gating (- [kimmonismus live thread](https://x.com/kimmonismus/status/2064059964709388774),- [regional limitation note](https://x.com/kimmonismus/status/2064047278105464868)). A technically notable detail came from- [awnihannun](https://x.com/awnihannun/status/2064202168618422396): Apple’s on-device model is reportedly a- **20B-parameter query-routed architecture**that loads experts from NAND into RAM once per query, a nonstandard design optimized for device constraints.

**Research Directions: Continual Learning, Agent Training, and Optimization Debates**

- **Anthropic framed one core blocker for AI in science as infrastructure mismatch**: Its new science blog argues AI has advanced faster in coding than biology because biological databases and tooling were not designed for agent use; the bottleneck is less raw intelligence than- **agent-compatible scientific infrastructure**(- [Anthropic blog thread](https://x.com/AnthropicAI/status/2064054837294354677)). This pairs well with broader calls for harness/environment standardization.
- **Open-source RL and environment protocols are becoming coordination points**:- [OpenEnv was transferred to a consortium including Hugging Face, Meta-PyTorch, Reflection, Unsloth, Modal, Prime Intellect, NVIDIA, and others](https://x.com/ben_burtenshaw/status/2063991191415267492). The pitch is that frontier labs co-train models with tightly coupled harnesses, while open ecosystems need a- **shared protocol layer**between model, harness, environment, and trainer.
- **Continual learning for agents is re-emerging as a practical systems problem**:- [Hivemind announced a system that turns traces from agents like Claude Code, Codex, Cursor, and Hermes into reusable skills](https://x.com/kimmonismus/status/2064001045391462907), claiming measurable gains across setups. Relatedly,- [Nando de Freitas posted a long thread](https://x.com/NandoDF/status/2063938859583389837)outlining a research program around learning from- **interaction consequences**rather than token sequences alone.
- **Optimization discourse was unusually active**: Several threads debated whether- **Muon**is materially distinct from- **Shampoo**, with- [Arohan hinting at a better-than-Shampoo optimizer](https://x.com/_arohan_/status/2064036303021494418)and- [Keller Jordan benchmarking Shampoo and Spectral Descent publicly](https://x.com/kellerjordan0/status/2064062891607888058). The substantive point beneath the drama: there is renewed appetite for- **optimizer-level gains**as a real frontier lever, not just benchmark noise.

**Top Tweets (by engagement)**

- **Signal on UK device scanning**: The highest-engagement technically relevant post was- [Signal’s statement opposing UK demands for on-device scanning and age-verification-linked content inspection](https://x.com/signalapp/status/2064069692168519931). This is more privacy/security policy than AI, but directly relevant to client-side inference and platform trust.
- **OpenAI corporate direction and liquidity**:- [Sam Altman shared OpenAI’s current plan](https://x.com/sama/status/2064088940932641225), and shortly after- [OpenAI announced it had confidentially filed an S-1](https://x.com/OpenAINewsroom/status/2064094175541461220). For AI engineers, the key implication is strategic: both OpenAI and Anthropic now appear to be preserving IPO optionality while ramping capacity and product breadth.
- **NotebookLM and FrontierCode were the day’s biggest pure-product/eval launches**:- [NotebookLM’s upgrade](https://x.com/NotebookLM/status/2064016460964585549),- [Kimi Code](https://x.com/KimiDevs/status/2063981516708024369),- [Kimi Work](https://x.com/Kimi_Moonshot/status/2063990409903112344), and- [FrontierCode](https://x.com/cognition/status/2064061031912288715)dominated the technical conversation, with FrontierCode in particular reshaping the discourse around what “good coding performance” should mean.

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
