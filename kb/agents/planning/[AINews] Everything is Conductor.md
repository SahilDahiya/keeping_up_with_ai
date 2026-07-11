---
title: '[AINews] Everything is Conductor'
topic: agents
subtopic: planning
secondary_topics:
- agents/multi-agent
summary: Frames conductor-style orchestration as an emerging pattern for coordinating
  agent workflows.
source: latent-space
url: https://www.latent.space/p/ainews-everything-is-conductor
author: Latent Space
published: '2026-05-15'
fetched: '2026-07-11T05:11:34Z'
classifier: codex
taxonomy_rev: 1
words: 1726
content_sha256: dfeec13a3d81d4a2763510b068ea21076b8e4da0726c9076d2b08a3ceba4fda3
---

# [AINews] Everything is Conductor

# [AINews] Everything is Conductor

### an ultra quiet day lets us highlight a smaller trend.

*If you’re interested in how AI is improving Healthcare, tune in to our  first pod on it out today, and if you want to meet other top engineers in the field, apply to speak!*

There’s an ongoing joke in evolutionary biology that “Everything is Crab”: [the Crab form factor](https://en.wikipedia.org/wiki/Carcinisation) has independently evolved at least 7 times on earth:

![](https://substackcdn.com/image/fetch/$s_!-UVS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc44b00aa-b057-4698-a9c6-f8e73c7aaaf7_2289x1342.jpeg)

The proximate cause of today’s op-ed is GitHub [announcing the new GitHub App](https://x.com/github/status/2054959324485628120) - as Oren Melamed says, “*If you are  code first you might wanna stay on good ol’ VS Code, but if you are agent first and GitHub first you are in for a treat!*”

![](https://substackcdn.com/image/fetch/$s_!8awu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc0e389d-df44-481c-998d-5524cf58e696_1194x1250.png)

Hmm. That looks familiar…

![](https://substackcdn.com/image/fetch/$s_!DOb8!,w_5760,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d6e93c-4e99-4ff0-8a20-74c75f3a54b8_2310x1298.png)

This is of course very nice for [Conductor](https://conductor.build/), which pioneered this form factor, and now has a loudly vocal fan in Garry Tan, the AI pilled CEO of Y Combinator:

![X avatar for @garrytan](https://substackcdn.com/image/fetch/$s_!NOrH!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1922894268403941377%2F-dGWAt3N.jpg)

Now for two billion dollar questions:

- if you pioneered a form factor, how do you monetize it while others copy it?
- what’s next after this one?

For those interested in alternate histories, here’s what happened with the Kanban board form factor that briefly trended last year:

And here is Maggie Appleton breaking down the design thinking [behind GitHub Ace](https://www.youtube.com/watch?v=ClWD8OEYgp8&t=372s):

AI News for 5/13/2026-5/14/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**Coding Agent Tooling: Codex Mobile, GitHub’s New App, VS Code Multi-Agent UX, and Hermes/Codex Interop**

- **OpenAI pushed Codex further into day-to-day workflows**: the biggest product launch in this set was- **Codex in the ChatGPT mobile app**, letting users start tasks, review outputs, approve commands, and steer execution remotely while Codex continues running on a laptop, Mac mini, or devbox. OpenAI also noted- **Remote SSH is now generally available**for managed remote environments, and later added- **hooks**plus- **programmatic access tokens**for Business/Enterprise automation around the Codex loop (- [OpenAI](https://x.com/OpenAI/status/2055016850849993072),- [OpenAI follow-up](https://x.com/OpenAI/status/2055016852133417389),- [@OpenAIDevs on mobile workflow](https://x.com/OpenAIDevs/status/2055016926213181608),- [@OpenAIDevs on Remote SSH](https://x.com/OpenAIDevs/status/2055016938217377945),- [@OpenAIDevs on hooks/tokens](https://x.com/OpenAIDevs/status/2055032115964870838)). Separately, OpenAI published a technical writeup on the- **Wi`ndows sandbox for Codex**, focused on the tradeoff between utility and constrained machine access for coding agents (- [OpenAI Devs](https://x.com/OpenAIDevs/status/2054735161166819377),- [@gdb](https://x.com/gdb/status/2054744721570820444)).
- **The broader IDE/app ecosystem is converging on “agent-first” UX**: GitHub announced a technical preview of the- **GitHub Copilot App**, described as a desktop environment for parallel workstreams, repo/PR lifecycle management, and model flexibility (- [GitHub](https://x.com/github/status/2054959324485628120),- [@adrianmg](https://x.com/adrianmg/status/2054961575929508067),- [@OrenMe](https://x.com/OrenMe/status/2054959549413503308)).- **VS Code**shipped a new- **Agents window**for multi-agent, multi-project workflows, browser/mobile support via- **vscode.dev/agents**, BYOK improvements, and token-efficiency features like compressed terminal output (- [VS Code](https://x.com/pierceboggan/status/2054775908586934440),- [remote/browser support](https://x.com/pierceboggan/status/2054778014135902715),- [BYOK updates](https://x.com/pierceboggan/status/2054778582216622579),- [terminal compression](https://x.com/pierceboggan/status/2054779764523815264)). On the open side,- **Nous/Hermes Agent**added- **Codex runtime integration**, effectively routing OpenAI-backed turns through Codex CLI/app-server and reusing ChatGPT subscription-backed execution in Hermes sessions (- [Nous Research](https://x.com/NousResearch/status/2054958564951912714),- [@Teknium](https://x.com/Teknium/status/2054958835547443553),- [@HermesAgentTips](https://x.com/HermesAgentTips/status/2054963533800992962)). Kimi also shipped- **Kimi Web Bridge**, a browser extension exposing human-like web interaction to Kimi Code CLI, Claude Code, Cursor, Codex, Hermes, and others (- [Moonshot AI](https://x.com/Kimi_Moonshot/status/2054918374837322140)).

**Agent Infrastructure and Self-Improvement Loops: LangSmith Engine, SmithDB, Sandboxes, and Continual Learning**

- **LangChain’s launch stack was the most substantive agent-infra release cluster**:- **SmithDB**is a database purpose-built for- **agent trace data**, while- **LangSmith Engine**consumes traces, clusters failures, identifies likely code issues, and proposes fixes/evals—turning observability into an improvement loop rather than passive inspection (- [@hwchase17](https://x.com/hwchase17/status/2054754206926700914),- [@caspar_br on Engine](https://x.com/caspar_br/status/2054726851659248068),- [@bentannyhill](https://x.com/bentannyhill/status/2054949581679653326)). Community commentary emphasized SmithDB’s architectural shift toward object storage and a custom storage/query path for this workload shape (- [@caspar_br on SmithDB](https://x.com/caspar_br/status/2054773536603144458),- [@ngates_](https://x.com/ngates_/status/2054859033488580721),- [Chinese summary](https://x.com/0xLogicrw/status/2054852978243404008)).
- **LangChain also announced LangChain Labs**, an applied research effort around- **continual learning**for agents, with the thesis that production traces should become training signal, evals, and targeted capability improvements over long horizons (- [LangChain](https://x.com/LangChain/status/2054971487694749898),- [@jakebroekhuizen](https://x.com/jakebroekhuizen/status/2054973621312073832),- [@willccbb](https://x.com/willccbb/status/2054983266046996839),- [Prime Intellect partnership](https://x.com/PrimeIntellect/status/2054986817779425579)).
- **Execution isolation for agents continues to mature**: W&B/CoreWeave launched- **CoreWeave Sandboxes**for isolated execution in RL, tool use, and eval workloads, explicitly testing destructive commands like- `rm -rf /`at scale (- [Weights & Biases](https://x.com/wandb/status/2054958004118724672)). In a similar spirit, open-source/local dev tooling surfaced around agent debugging:- [@benhylak](https://x.com/benhylak/status/2054987683928383872)highlighted a free local agent debugging stack with traces exposed to Codex/Claude Code for automated eval authoring.

**Anthropic Claude Code Restrictions and the Developer Backlash**

- **The sharpest ecosystem reaction was to Anthropic restricting/reshaping Claude Code usage**, especially for third-party wrappers and high-volume programmatic workflows. Theo’s thread became the focal point: he argued users of T3 Code were effectively hit with dramatic rate-limit reductions despite integrating through the officially supported path, and he subsequently cancelled his subscription while encouraging others to post cancellation screenshots for open-source donations (- [@theo initial thread](https://x.com/theo/status/2054731856248283318),- [subscription cancellation](https://x.com/theo/status/2054732997287625013),- [donation thread](https://x.com/theo/status/2054734057368621176),- [T3 Code clarification](https://x.com/theo/status/2054737293186126056)). Other prominent builders echoed the complaint that Anthropic had effectively cut off open-source devs/apps and destabilized harnesses built around- `claude -p`(- [@theo](https://x.com/theo/status/2054728187498946969),- [@andersonbcdefg](https://x.com/andersonbcdefg/status/2054721558141403242)).
- **There was also a more strategic counterargument**: some users argued Anthropic does not owe developers heavily subsidized flat-fee tokens for third-party apps, and that the ecosystem will likely shift toward more explicit API economics and smarter routing between expensive and cheap models (- [Sentdex](https://x.com/Sentdex/status/2054925517426491739),- [@tadasayy](https://x.com/tadasayy/status/2054922713857462487)). Still, the visible churn signal was nontrivial, including users estimating meaningful ARR loss from reply-thread cancellations alone (- [@thegenioo](https://x.com/thegenioo/status/2054919696663663009),- [Uncle Bob Martin](https://x.com/unclebobmartin/status/2054970327592042661),- [Theo later](https://x.com/theo/status/2055022768262144102)). For agent engineers, the practical takeaway is straightforward:- **subscription-backed harnesses are not stable platform primitives**; provider/model abstraction and BYOK paths look increasingly mandatory.

**Robotics and Embodied AI: Figure’s 24/7 Sorting Stream and the Broader Automation Signal**

- **Figure’s livestream dominated robotics discussion**. The company first showed- **8 hours of fully autonomous, unsupervised work**, then extended to a- **24/7 livestream**, eventually reporting- **24+ hours of continuous autonomous operation without failure**, around- **human-parity throughput**on small package sorting, and operation by- **Helix-02 running entirely onboard**with automatic resets for OOD cases—explicitly claiming- **no teleoperation**(- [Figure CEO Brett Adcock](https://x.com/adcock_brett/status/2054729581391962353),- [24h update](https://x.com/adcock_brett/status/2054946098431881720),- [detailed technical clarifications](https://x.com/adcock_brett/status/2054973511572271172),- [Day 2 livestream](https://x.com/adcock_brett/status/2054970993442169230)). The repeated “Bob, Frank, and Gary” updates were fluffier, but the core signal was sustained autonomous operation at production-like uptime.
- **Interpretation split between skepticism about Figure specifically and broader conviction about robotics acceleration**. Some commenters argued that critics were underestimating what these demonstrations imply for near-term labor substitution, while others noted skepticism was directed more at- **Figure**than at- **robotics as a category**(- [@cloneofsimo](https://x.com/cloneofsimo/status/2054712329431109708),- [@iScienceLuvr](https://x.com/iScienceLuvr/status/2054715505982743009),- [@kimmonismus](https://x.com/kimmonismus/status/2054947354625630462)). Either way, this was one of the clearest “continuous uptime” demos in the batch.

**Research, Benchmarks, and Open Models: Diffusion LMs, Time-Series FMs, Mechanistic Interpretability, and RL/Search**

- **A few technically significant model/research releases stood out**:- **Zyphra’s ZAYA1-8B-Diffusion-Preview**claims a- **4.6–7.7x decoding speedup**versus autoregressive generation with limited quality loss, making the usual case that diffusion LMs enable cheaper rollouts and richer generation modes (- [Zyphra](https://x.com/ZyphraAI/status/2055038845809480113)).
- **Datadog’s Toto 2.0**released- **5 open-weights time-series forecasting models**from- **4M to 2.5B params**under- **Apache 2.0**, claiming #1 on- **BOOM, GIFT-Eval, and TIME**and, more importantly, evidence that scaling laws may finally hold cleanly for TSFMs (- [Datadog](https://x.com/datadoghq/status/2054929795385893108),- [@atalwalkar](https://x.com/atalwalkar/status/2054941930497142826),- [@ClementDelangue](https://x.com/ClementDelangue/status/2054991352295731619)).
- **Goodfire’s interpretability post**argued that Llama uses a geometric “shape-rotating calculator” / Fourier-feature-like mechanism for arithmetic, with steering-based evidence rather than pure post-hoc description (- [GoodfireAI](https://x.com/GoodfireAI/status/2054962242022777189),- [follow-up](https://x.com/GoodfireAI/status/2054962356162363599)).

- **On RL/search and optimizer-style progress**, several threads were notable: a survey framing LLM RL as- **rollout engineering**across- **Generate / Filter / Control / Replay**rather than just PPO-vs-GRPO (- [The Turing Post](https://x.com/TheTuringPost/status/2054713822343266365));- **Pedagogical RL**using privileged information to actively find useful rollouts (- [Souradip Chakraborty](https://x.com/SOURADIPCHAKR18/status/2055057138070733176),- [@lateinteraction](https://x.com/lateinteraction/status/2055065846389649436)); and- **Prime Intellect’s autonomous optimizer search**on the nanoGPT speedrun benchmark, where- **Opus 4.7 reached 2930 steps**and- **GPT-5.5 2950**, beating the- **2990 human baseline**after ~10k runs / ~14k H200 hours (- [Prime Intellect](https://x.com/PrimeIntellect/status/2055056380881744365),- [@eliebakouch](https://x.com/eliebakouch/status/2055059154738278851)). Also noteworthy:- **Kimi K2.6**was reported as- **#1 open-weight model on Finance Agent Benchmark V2**(- [Moonshot AI](https://x.com/Kimi_Moonshot/status/2054803169994272819)), and- **Ring-2.6-1T**got day-0 vLLM support as an open release (- [vLLM](https://x.com/vllm_project/status/2054968127298150506)).

**Top Tweets (by engagement)**

- **OpenAI’s Codex mobile launch**was the clearest product winner by engagement and practical relevance: remote control/review of running coding-agent sessions from ChatGPT mobile (- [OpenAI](https://x.com/OpenAI/status/2055016850849993072)).
- **Theo’s Claude Code backlash threads**captured the strongest developer sentiment shift around platform risk and subscription-backed agent workflows (- [@theo](https://x.com/theo/status/2054731856248283318),- [@theo donations thread](https://x.com/theo/status/2054734057368621176)).
- **Figure’s autonomous humanoid sorting livestream**remained one of the most discussed embodied-AI demos, especially once it crossed the 24-hour mark with detailed claims about onboard policy execution and no teleop (- [Brett Adcock](https://x.com/adcock_brett/status/2054973511572271172)).
- **GitHub’s Copilot App**and- **LangChain’s Engine/SmithDB/Labs**were the most important non-OpenAI tooling launches for agent engineers this cycle (- [GitHub](https://x.com/github/status/2054959324485628120),- [LangChain](https://x.com/LangChain/status/2054971487694749898),- [@hwchase17](https://x.com/hwchase17/status/2054754206926700914)).
- **Prime Intellect’s autonomous optimizer-search result**is worth watching as a concrete example of coding agents being looped into open-ended ML optimization, not just app dev (- [Prime Intellect](https://x.com/PrimeIntellect/status/2055056380881744365)).

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

**1. Qwen 3.6 Local Inference Speedups and Quantization**

- [Multi-Token Prediction (MTP) for Qwen on LLaMA.cpp + TurboQuant](https://www.reddit.com/r/LocalLLaMA/comments/1tckzy2/multitoken_prediction_mtp_for_qwen_on_llamacpp/)- **A patched llama.cpp fork adds Multi-Token Prediction (MTP) support for Qwen plus TurboQuant, reporting**- `21 tok/s`- **→**- `34 tok/s`- **on a MacBook Pro M5 Max 64GB, with a claimed**- `90%`- **MTP acceptance rate; note the raw speedup is ~**- `62%`- **, not**- `40%`- **. Code is published at**- `AtomicBot-ai/atomic-llama-cpp-turboquant`- **, with GGUF MTP quantizations for Qwen 3.6 27B/35B in the**- `AtomicChat/qwen-36-udt-mtp`- **HF collection.**Commenters questioned the TurboQuant framing, arguing it is often slower than- `f16`,- `q8`, or- `q4`; one noted a TurboQuant PR to llama.cpp was rejected because existing Q4 KV-quant rotation support already covered most benefits, with gains mainly at Q3 where quality degradation becomes a concern. Others asked for quality/eval data, since higher speculative/MTP acceptance and tokens/s do not alone establish output parity.- Several commenters argued that - **TurboQuant is not generally faster in llama.cpp**, with one noting it can be slower than- `f16`,- `q8`, or- `q4`. A prior TurboQuant PR to- **llama.cpp**was reportedly rejected because llama.cpp already implements rotations for- `Q4`KV-cache quantization, where standard- `Q4`was faster and showed little gain; TurboQuant may only help around- `Q3`, but with notable quality degradation.
- Users distinguished between speed, quality, and context tradeoffs: - **MTP without TurboQuant**was suggested for speed, while standard- `Q4_1`or- `Q4_0`quantization was recommended for longer context/quality retention. One commenter questioned whether TurboQuant had any Mac-specific advantage, implying the benefit is hardware- or workload-dependent rather than broadly useful.
- A commenter recommended using - **dflash**instead of built-in MTP, claiming it is- `30–40%`faster. They also mentioned that a pull request for this already existed, suggesting the implementation work may duplicate prior llama.cpp integration efforts.


## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
