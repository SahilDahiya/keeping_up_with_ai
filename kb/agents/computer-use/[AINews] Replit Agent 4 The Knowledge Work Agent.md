---
title: '[AINews] Replit Agent 4: The Knowledge Work Agent'
topic: agents
subtopic: computer-use
secondary_topics:
- agents/planning
summary: Covers Replit Agent 4 as a knowledge-work agent and what that implies for
  coding-agent workflows.
source: latent-space
url: https://www.latent.space/p/ainews-replit-agent-4-the-knowledge
author: Latent Space
published: '2026-03-12'
fetched: '2026-07-11T05:13:37Z'
classifier: codex
taxonomy_rev: 1
words: 2218
content_sha256: b4780a28bffa33ecba252e59aadfafce37340e2f92963de286a1b4e6d5a52c9b
---

# [AINews] Replit Agent 4: The Knowledge Work Agent

# [AINews] Replit Agent 4: The Knowledge Work Agent

### Replit Agent 4 lets us reflect on a couple disparate releases.

**Replit just  tripled in valuation to $9B in the last 6 months.** You can accuse Amjad Masad of many things, but you cannot deny he and his team’s

[incredible pulse](https://x.com/amasad/status/2031755113694679094?s=20)on what the “current meta” in tech is:

![](https://substackcdn.com/image/fetch/$s_!e-5-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d51887-ef65-46b8-88f3-275ddd3ae978_1186x1494.png)

Perhaps if you’re not close to Replit (eg you never saw their [2015 Master Plan](https://blog.replit.com/replit-raises-400-million-dollars) or their [Documentary](https://x.com/amasad/status/2029251832460263632?s=20)), you might watch that 8 minute video and think it is a generic AI platform launch like any other. But this Replit is unrecognizable from the “coding with some AI tacked on” platform that [Replit was just 2 years ago](https://www.youtube.com/watch?v=ju73sWVtvU0), with a bunch of now veritably antiquated conventional wisdoms of the time:

Now that software engineering is approximately solved, where does a coding platform go? Well for Replit, it means going up the stack to be a fully integrated productivity suite, with a canvas, apps, sites, slides, [videos](https://x.com/Replit/status/2024578806208745637?s=20), and others.

This is a smart pivot that is inline with one of the most dominant themes of 2026 - now that coding agents have solved coding, it is the same coding agent builders that are expanding their scope to more and more knowledge work tasks, including [Pi → OpenClaw](https://www.latent.space/p/ainews-sci-fi-with-a-touch-of-madness), Claude Code → Cowork, and [every model lab working on Excel and PowerPoint integrations](https://x.com/claudeai/status/2031790754637717772), and [Notion building Custom Agents](https://www.notion.com/blog/introducing-custom-agents) for every other knowledge work integration in the world.

## Our Running Trends List of 2026 in AI

We have been somewhat accumulating a list of AI Trends that Matter in 2026 and it has slowly emerged through our coverage this year:

- Coding Agents → Knowledge Work Agents (today’s piece)
- [Death of IDE](https://www.latent.space/p/ainews-openai-codex-app-death-of)→ “Dark” Software Factories - with- [no code review](https://www.latent.space/p/reviews-dead)
- AI research automation (aka - [RSI](https://www.latent.space/p/ainews-autoresearch-sparks-of-recursive), sometimes “AI Scientist”)
- World Models ( - [AMI](https://www.latent.space/p/ainews-yann-lecuns-ami-labs-launches),- [Adversarial](https://www.latent.space/p/adversarial-reasoning?utm_source=publication-search))
- “ - [AI for Science](https://www.latent.space/p/science)” finally working


AI News for 3/10/2026-3/11/2026. We checked 12 subreddits,[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**NVIDIA’s Nemotron 3 Super Release and the Open-Model Efficiency Push**

- **Nemotron 3 Super**was the clearest technical release of the day: a- **120B parameter / ~12B active**open model with- **1M context**, a- **hybrid Mamba-Transformer / SSM Latent MoE**architecture, and explicit support for agentic workloads. NVIDIA positioned it as unusually open —- **weights, data, recipe, infra details**— and performance-focused for Blackwell-era deployment, with claims of- **up to 2.2x faster inference than GPT-OSS-120B in FP4**and large throughput gains over prior Nemotron releases (- [announcement via @ctnzr](https://x.com/ctnzr/status/2031762077325406428),- [tech perspective via @kuchaev](https://x.com/kuchaev/status/2031765052970393805),- [Wired reporting on NVIDIA’s broader open-model investment](https://x.com/willknight/status/2031792027390587313)).
- Third-party reactions converged on the same theme: - **strong capability-per-active-parameter and unusually high serving speed**.- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2031765321233908121)scored it- **36 on the AA Intelligence Index**, ahead of- **gpt-oss-120b (33)**but behind- **Qwen3.5-122B-A10B (42)**, while noting- **~10% higher throughput per GPU**than GPT-OSS-120B and launch-day serving speeds of- **up to 484 tok/s**. Community and infra support landed immediately across- [vLLM](https://x.com/vllm_project/status/2031779213527957732),- [llama.cpp](https://x.com/ggerganov/status/2031819920363733205),- [Ollama](https://x.com/ollama/status/2031777869681000676),- [Together](https://x.com/togethercompute/status/2031831368339243454),- [Baseten](https://x.com/basetenco/status/2031775755253026965),- [W&B Inference](https://x.com/wandb/status/2031778471614300563),- [LangChain](https://x.com/LangChain/status/2031784791251525934), and- [Unsloth GGUFs](https://x.com/UnslothAI/status/2031778104306499749).
- The most interesting technical discussion was about - **why it is fast**.- [@ctnzr](https://x.com/ctnzr/status/2031776463029186920)highlighted- **native multi-token prediction (MTP)**as a key inference optimization: provisional multi-token guesses get verified on subsequent passes, exploiting otherwise-unused GPU compute at small batch sizes.- [@bnjmn_marie](https://x.com/bnjmn_marie/status/2031821490916905089)also quantified a major- **KV-cache advantage**versus Qwen3.5-122B: roughly- **8,192 bytes/token in BF16**for Nemotron’s attention KV term versus- **24,576 bytes/token**for Qwen3.5-122B, making long-context serving materially lighter.

**Agent Infrastructure, Orchestration, and the “Bigger IDE” Thesis**

- The strongest product trend was a shift from “chat with a model” to - **persistent agent runtimes and orchestration layers**.- [@karpathy](https://x.com/karpathy/status/2031767720933634100)argued the “age of the IDE is over” framing is wrong; instead,- **“we’re going to need a bigger IDE”**where the unit of work becomes- **an agent rather than a file**, and later extended that into the notion of- **legible, forkable agentic orgs**with real-time observability and control (- [follow-up](https://x.com/karpathy/status/2031770607466291393),- [org legibility thread](https://x.com/karpathy/status/2031774631498273005)).
- Multiple launches fit that framing. - **Perplexity**announced- **Personal Computer**, an- **always-on local/cloud hybrid**that runs on a- **Mac mini**, works across local files/apps/sessions, and can be controlled remotely (- [launch](https://x.com/perplexity_ai/status/2031790180521427166),- [waitlist](https://x.com/perplexity_ai/status/2031790221612957875)). It also expanded- **Computer for Enterprise**, describing orchestration across- **20 specialized models**and- **400+ apps**(- [enterprise launch](https://x.com/perplexity_ai/status/2031799033489211771),- [API platform update](https://x.com/perplexity_ai/status/2031828396435771563)). Separately,- **Replit Agent 4**pitched a more collaborative, canvas-like workflow with- **parallel agents**for apps, sites, and slides (- [launch](https://x.com/amasad/status/2031755113694679094)), while- **Base44 Superagents**emphasized “batteries included” integrations with Gmail, Slack, Stripe, CRM, and more for nontechnical users (- [launch](https://x.com/MS_BASE44/status/2031758998475505848)).
- The engineering discussion is increasingly around the - **harness**, not just the model.- [@Vtrivedy10](https://x.com/Vtrivedy10/status/2031751769051570256)described a fast-moving design space where improved models unlocked product experiences that were previously too brittle, with a self-improving loop of- **evals/metrics → autonomous harness edits → hill climbing**. LangChain added- **autonomous context compression**to Deep Agents so models can compact at task boundaries instead of hard token thresholds (- [announcement](https://x.com/LangChain_OSS/status/2031799813851730075)), while- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2031798071345234193)published a technical writeup on- **computer access for agents**, covering execution loops, filesystem context, network access, and guardrails.

**Anthropic, Claude-Centric Workflows, and Early RSI Anxiety**

- A major meta-story was - **Anthropic’s institutional framing of powerful AI**. The company launched- **The Anthropic Institute**, led by- **Jack Clark**in a new- **Head of Public Benefit**role, with a mandate spanning ML engineering, economics, and social science to shape the public conversation around advanced AI (- [launch](https://x.com/AnthropicAI/status/2031674087374815577),- [leadership note](https://x.com/AnthropicAI/status/2031674092290474421),- [Jack Clark on role change](https://x.com/jackclarkSF/status/2031746605117010245)).
- At the same time, several tweets amplified concerns that Anthropic may be seeing - **early recursive-self-improvement dynamics**internally. The most substantive references came indirectly via discussion of a- **TIME**article:- [@kimmonismus](https://x.com/kimmonismus/status/2031803194817511744)summarized claims that- **70–90% of the code used in developing future models is now written by Claude**, model release cadence has compressed from months to- **weeks**, and some researchers think- **fully automated AI research could be as little as a year away**.- [@Hangsiin](https://x.com/Hangsiin/status/2031752106496135541)highlighted one especially striking line: Claude being- **427x faster than human overseers**at some internal tasks, with nested parallel usage patterns already common.
- This narrative had an immediate practical counterpoint: - **operational dependence on Claude Code**. A login/auth outage triggered visible developer pain, with- [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2031777214321262637)joking that Silicon Valley productivity fell 90%,- [@dejavucoder](https://x.com/dejavucoder/status/2031760986907312635)reporting inability to log in, and- [@HamelHusain](https://x.com/HamelHusain/status/2031783246980399375)describing fallback to token-based access. The outage even prompted- [@karpathy](https://x.com/karpathy/status/2031792523187040643)to note his- **autoresearch labs got wiped out in the OAuth outage**, framing future frontier-model service interruptions as potential- **“intelligence brownouts.”**

**Research on Agent Evals, Retrieval, Post-Training, and Self-Improvement**

- Several papers focused on what looks like the next bottleneck: - **measuring and improving agent systems**, rather than just base-model quality.- [@karinanguyen_](https://x.com/karinanguyen_/status/2031789998811595154)released- **PostTrainBench v1.0**, a benchmark for whether frontier agents can- **post-train language models in a simplified setting**, explicitly aimed at tracking progress toward- **AI R&D automation / recursive self-improvement**. One notable ablation from the thread: for- **GPT-5.1 Codex Max**,- **medium reasoning effort beat high**, because extra tokens caused context compaction and hurt performance (- [ablation details](https://x.com/karinanguyen_/status/2031790007028236452)).
- On the agent-learning side, - [@omarsar0](https://x.com/omarsar0/status/2031727864199208972)highlighted- **EvoSkill**, where an executor/proposer/skill-builder triad discovers and refines reusable skills from failures; on OfficeQA it reportedly improved- **Claude Code + Opus 4.5 from 60.6% to 67.9% exact match**.- [@dair_ai](https://x.com/dair_ai/status/2031726356292407366)shared- **AgentIR**, a- **reasoning-aware retriever**that jointly embeds an agent’s reasoning trace with its query; they report- **68% accuracy on BrowseComp-Plus**, versus- **52%**for larger conventional embedding models and- **37%**for BM25.
- There was also renewed emphasis on - **agent reliability as a security problem even without adversaries**.- [@random_walker](https://x.com/random_walker/status/2031693490669654447)argued many AI-agent failures arise from unreliability rather than explicit attacks, pointing to a Princeton response to NIST on the need to define, measure, and mitigate that failure mode. Combined with the growing emphasis on eval craft — e.g.- [@gabriberton](https://x.com/gabriberton/status/2031653520429203498)calling eval creation the most useful skill in the age of code agents — the center of gravity keeps shifting toward- **measurement, harnesses, and production feedback loops**.

**Multimodal Models, Embeddings, and Physical/Visual AI**

- On the multimodal side, - **Google’s Gemini Embedding 2**drew practical pricing analysis rather than benchmark talk.- [@osanseviero](https://x.com/osanseviero/status/2031691784074477766)summarized the release: embeddings for- **text, images, video, audio, PDFs**, plus- **Matryoshka embeddings**for lower-dimensional storage.- [@neural_avb](https://x.com/neural_avb/status/2031648857625395321)offered the most useful deployment note:- **text pricing appears high relative to competitors**, suggesting the model is best reserved for- **multimodal retrieval**; video embedding costs can explode unless clients aggressively lower- **FPS**before upload.
- **Qwen3.5’s multimodal architecture**also got a detailed community breakdown from- [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2031686944040915152): a- **hybrid attention**stack mixing- **Gated DeltaNet linear attention**and- **Gated full attention**, with a- **397B A17B MoE**variant and- **27B dense**variant,- **262k native context**extensible toward- **1M**, and- **MTP**in training. That thread is useful mostly as a compact survey of where attention innovation is going:- **hybrid linear/full attention, GQA, DSA, and MoE routing**are now core design axes.
- In vision/physical AI, - **Reka Edge**launched as a production-focused VLM for physical AI, claiming- **3x fewer input tokens**and- **65% faster throughput**than leading 8B models across image/video understanding, object detection, and tool use (- [launch](https://x.com/RekaAILabs/status/2031781818349834628)). Google also shared two healthcare deployments: an AI system that identified- **25% of interval breast cancers**missed by standard screening (- [Google](https://x.com/Google/status/2031734020979998795)) and a real-world study of- **AMIE**for conversational clinical reasoning that found it safe, feasible, and well-received by patients (- [Google Research](https://x.com/GoogleResearch/status/2031777657835139263)).

**Top tweets (by engagement)**

- **Perplexity’s “Personal Computer”**: always-on local/cloud agent on a Mac mini with remote control and local app/file access (- [launch](https://x.com/perplexity_ai/status/2031790180521427166)).
- **Anthropic Institute / Jack Clark’s new role**: Anthropic formalizes a public-benefit and public-discourse effort around powerful AI (- [Anthropic](https://x.com/AnthropicAI/status/2031674087374815577),- [@jackclarkSF](https://x.com/jackclarkSF/status/2031746605117010245)).
- **Replit Agent 4**: collaborative, multi-agent canvas for shipping apps/sites/slides (- [announcement](https://x.com/amasad/status/2031755113694679094)).
- **NVIDIA Nemotron 3 Super**: open 120B/12B-active hybrid model with 1M context and day-0 ecosystem support (- [@ctnzr](https://x.com/ctnzr/status/2031762077325406428)).
- **Claude Code outage as infra risk**: frontier-model auth failure visibly disrupting real engineering workflows (- [@karpathy](https://x.com/karpathy/status/2031792523187040643),- [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2031777214321262637)).

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Qwen Model Releases and Benchmarks**

- [M5 Max just arrived - benchmarks incoming](https://www.reddit.com/r/LocalLLaMA/comments/1rqnpvj/m5_max_just_arrived_benchmarks_incoming/)- **The post discusses the arrival and benchmarking of the M5 Max 128GB 14” laptop, focusing on testing various machine learning models using the**- `mlx_lm`- **tool. The models tested include Qwen3.5-122B-A10B-4bit, Qwen3-Coder-Next-8bit, Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-6bit, and gpt-oss-120b-MXFP4-Q8. The benchmarks reveal performance metrics such as tokens-per-second and peak memory usage for different prompt sizes. The author initially faced issues with BatchGenerator but resolved them by using a fresh Python environment and**- `stream_generate`- **. The results show varying performance across models, with peak memory usage ranging from 25.319 GB to 92.605 GB and generation speeds from 14.225 to 87.873 tokens-per-second.**Commenters are eager for the benchmark results, with one expressing interest in the performance of the Qwen 3.5 27b MLX models. Another commenter humorously notes the anticipation for the benchmarks.- The benchmarks for the M5 Max 128GB 14” using - `mlx_lm.generate`show varying performance across different models and configurations. For instance, the- **Qwen3.5-122B-A10B-4bit**model achieves a prompt throughput of- `1,239.7 t/s`at 16K context with a peak memory usage of- `73.8 GB`. In contrast, the- **Qwen3-Coder-Next-8bit**model reaches- `1,887.2 t/s`at 32K context, but with higher memory consumption at- `89.7 GB`.
- The - **Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-6bit**model shows a significant drop in generation throughput, with only- `14.9 t/s`at 32K context and a peak memory usage of- `30.0 GB`. This suggests a trade-off between model complexity and performance, as more distilled models may require less memory but also offer reduced throughput.
- The - **gpt-oss-120b-MXFP4-Q8**model demonstrates impressive performance with a prompt throughput of- `2,710.5 t/s`at 16K context and a relatively low peak memory usage of- `64.9 GB`. This indicates that the model is optimized for high throughput while maintaining efficient memory usage, making it suitable for applications requiring fast processing speeds.

- [Qwen3.5-35B-A3B Uncensored (Aggressive) — GGUF Release](https://www.reddit.com/r/LocalLLaMA/comments/1rq7jtm/qwen3535ba3b_uncensored_aggressive_gguf_release/)- **The release of Qwen3.5-35B-A3B Aggressive on**- [Hugging Face](https://huggingface.co/HauhauCS/Qwen3.5-35B-A3B-Uncensored-HauhauCS-Aggressive)is notable for its uncensored nature, maintaining the original model’s capabilities without refusals (- `0/465 refusals`- **). This model features**- `35B`- **parameters with**- `~3B`- **active, utilizing a mixture of experts (MoE) with**- `256 experts`- **and**- `8+1 active per token`- **. It supports multimodal inputs (text, image, video) and employs hybrid attention mechanisms (Gated DeltaNet + softmax in a**- `3:1`- **ratio). The model includes various quantization formats like**- `BF16`- **,**- `Q8_0`- **, and**- `Q6_K`- **, and is optimized for vision support with**- `mmproj`- **. Recommended sampling parameters include**- `temp=1.0`- **,**- `top_k=20`- **, and**- `presence_penalty=1.5`- **. Users are advised to use the**- `--jinja`- **flag with**- `llama.cpp`- **for optimal performance.**The community appreciates the release, with users expressing gratitude for the developer’s efforts and anticipation for trying the model once all components, like- `Q4_K_M`, are available.- Velocita84 raises a critical point about the need for evaluating Kullback-Leibler Divergence (KLD) to substantiate claims of ‘no capability loss’ in the Qwen3.5-35B-A3B model. This metric is essential for quantifying the difference between the probability distributions of the original and modified models, ensuring that the aggressive uncensoring does not degrade performance.
- Iory1998 highlights concerns about potential quality degradation, particularly in handling long context scenarios. This is a common issue with large language models where modifications, such as aggressive uncensoring, might impact the model’s ability to maintain coherence and accuracy over extended text inputs. The commenter questions how the modified model compares to the original in these aspects.
- No-Statistician-374 mentions the anticipation for the Q4_K_M version of the model, indicating a community interest in different quantization formats. This suggests that users are keen on exploring various configurations to optimize performance and resource usage, reflecting the technical community’s focus on balancing model size and computational efficiency.


## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
