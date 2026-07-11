---
title: '[AINews] The Unreasonable Effectiveness of Closing the Loop'
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/evaluation
summary: Explains why closing the loop is powerful in AI systems, linking feedback,
  evaluation, and iterative improvement.
source: latent-space
url: https://www.latent.space/p/ainews-the-unreasonable-effectiveness
author: Latent Space
published: '2026-02-25'
fetched: '2026-07-11T05:14:19Z'
classifier: codex
taxonomy_rev: 1
words: 1673
content_sha256: efa952c780493cc17ea06b1e7e320ef072d4cf77a03742a540e833b873003afa
---

# [AINews] The Unreasonable Effectiveness of Closing the Loop

# [AINews] The Unreasonable Effectiveness of Closing the Loop

### Everyone launching everything everywhere all at once.

Through the [dozens ](https://x.com/swyx/status/2026439784361766954)of midsize launches today (see the rest of the recaps below), one theme that we’re seeing is something I’ve come to call “[closing the loop](https://x.com/Scav/status/2021656781521670487)”:

![](https://substackcdn.com/image/fetch/$s_!veEG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F436292a8-2f3a-47fe-844e-a846b2c8d7fd_1186x1474.png)

[tweet](https://x.com/Scav/status/2021656781521670487)

In the DevTools industry, we often talk about the concept of the “inner loop” (what happens in the IDE, “squashed” inside a git commit), vs the “outer loop” (what happens in the cloud, “between” git commits, say after every git push). For a long time in the 2010s, all the action was in the “outer loop” - GitLab and multiple CI/CD unicorns, GitHub, Netlify/Vercel, and more, whereas the “inner loop” was generally free and open source (often thanks to Microsoft, but increasingly Facebook and Atlassian/Vercel) - VSCode, Language Servers, TypeScript, Prettier, and so on.

With AI, **things flipped dramatically** - Copilot kicked off the wave of Inner Loop coding agent applications that eventually became vanguarded by Cursor, whereas Outer Loop tools did grow thanks to AI, but remained relatively unchanged (or AI SRE or AI Data Engineering as a category seemed to particularly struggle).

Today many of the leading coding agent companies took steps in the “Close the Outer Loop” direction. For a lead graphic the first thing that springs to mind is the og:image for the [Devin Autofix launch](https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments) from a few weeks ago:

![](https://substackcdn.com/image/fetch/$s_!-p7X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6308ab6a-efac-48ed-b2ba-d2c569bec220_3840x2160.png)

The above only applies to review comments, but you can close the outer loop in many, many other ways. [Cursor’s highly anticipated big ship today](https://x.com/cursor_ai/status/2026369873321013568?s=20) was a combination of [full computer use](https://cursor.com/blog/agent-computer-use) and video output to give you high bandwidth review of the results rather than just looking at code diffs:

![X avatar for @cursor_ai](https://substackcdn.com/image/fetch/$s_!wxSG!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1970182748146180096%2FdhZeXi_X.jpg)

Claude Code, celebrating it’s first anniversary (as we discussed on today’s special podcast and short retrospective), launched ** Remote Control for Max users**, which allows people to close the loop in their phones, away from the Inner Loop of the terminal:

![X avatar for @claudeai](https://substackcdn.com/image/fetch/$s_!pIkX!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1950950107937185792%2FQOfEjFoJ.jpg)

Last but not least, Cognition [launched Devin 2.2](https://x.com/twitter/status/2026439784361766954), where a headline feature was how Devin Review now [automatically closes the loop](https://x.com/cognition/status/1983983151157563762) back into Devin runs.

If you are so inclined you could view all these as generalizations of the “Ralph Loops” that were popular in social media last month, often still with humans in the loop, but increasingly less so over time.

Don’t miss the other midsize launches today that would otherwise have been title stories in their own right - Notion Custom Agents, Inception Mercury 2, and the smaller Qwen 3.5 variants.

**AI Twitter Recap**

**Frontier model ecosystem: Qwen 3.5 “medium series” and open-weight momentum**

- **Qwen 3.5 Medium Model Series**: Alibaba released a tightly scoped set of “more intelligence, less compute” models—- **Qwen3.5-Flash**(hosted),- **Qwen3.5-35B-A3B (MoE)**,- **Qwen3.5-122B-A10B (MoE)**, and- **Qwen3.5-27B (dense)**—arguing that architecture + data + RL can outperform sheer parameter scaling. Notable details include- **Flash defaulting to 1M context**and built-in tools in the hosted offering. See the full announcement and links to Hugging Face/ModelScope/APIs from- [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2026339351530188939).- Early practitioner reactions emphasize how strong - **35B-A3B**and- **122B-A10B**feel in practice (e.g.,- [@andrew_n_carr](https://x.com/andrew_n_carr/status/2026347588950372752),- [@JustinLin610](https://x.com/JustinLin610/status/2026343725719568395)), plus the “intelligence-per-watt” implication of a- **35B model surpassing a 235B predecessor**noted by- [@awnihannun](https://x.com/awnihannun/status/2026353100144218569).
- **Deployment/serving stack is moving fast**: community tooling quickly followed—GGUF + sizing guidance from- [@UnslothAI](https://x.com/UnslothAI/status/2026351337970217357)and local-run enthusiasm like “35B-A3B is all you need” from- [@terryyuezhuo](https://x.com/terryyuezhuo/status/2026344442186326332). Qwen also highlighted SGLang support (- [tweet](https://x.com/Alibaba_Qwen/status/2026348924433477775)).
- **Quant + “local frontier” trendline**: INT4 variants appeared (duplicate posts) via- [@HaihaoShen](https://x.com/HaihaoShen/status/2026208062009426209), and users continue pushing aggressive quantization workflows (e.g., Unsloth praise for ultra-low-bit local Qwen by- [@0xSero](https://x.com/0xSero/status/2026223879077712269)).
- **Evaluation signals**: Qwen’s flagship- **Qwen3.5-397B-A17B**trended on HF (- [@Ali_TongyiLab](https://x.com/Ali_TongyiLab/status/2026211680653611174)) and showed up strongly on agentic webdev-style evaluation in Code Arena (- [Arena post](https://x.com/arena/status/2026337606137725363)). Arena also posted rank deltas vs Qwen 3.0 (- [comparison](https://x.com/arena/status/2026404630297719100)).


**OpenAI + Anthropic “coding agents as product surface area” (APIs, remote control, web sockets, proof-of-work UX)**

- **OpenAI: GPT-5.3-Codex in the Responses API**: OpenAI shipped- **GPT-5.3-Codex**to all developers via the- **Responses API**(- [announcement](https://x.com/OpenAIDevs/status/2026379092661289260)), with pricing cited by- [@scaling01](https://x.com/scaling01/status/2026379113099862018)(- **$1.75 input / $14 output**as tweeted). OpenAI also expanded- **file input types**(docx/pptx/csv/xlsx/etc.) for agents ingesting “real-world files” directly (- [tweet](https://x.com/OpenAIDevs/status/2026420817568084436)).- Infra detail: web sockets show up as a meaningful lever for agent throughput— - **“30% faster rollouts”**per- [@gdb](https://x.com/gdb/status/2026380170765152302). This matches broader chatter about why websockets took time and how state is stored upstream vs VRAM (- [thread](https://x.com/dejavucoder/status/2026219239477215657),- [follow-up](https://x.com/dejavucoder/status/2026223111021220265)).
- Benchmarks: third-party scoreboard posts claim strong placements for Codex 5.3 across TerminalBench/IOI/LiveCodeBench/VibeCodeBench ( - [ValsAI](https://x.com/ValsAI/status/2026385804940230786)).

- **Anthropic: “Claude Code Remote Control” + enterprise workflow push**: Anthropic introduced “Remote Control” for Claude Code—start a terminal session locally and- **continue from your phone**—first via- [@noahzweben](https://x.com/noahzweben/status/2026371260805271615), then officialized by- [@claudeai](https://x.com/claudeai/status/2026418433911603668), with rollout confirmation from- [@_catwu](https://x.com/_catwu/status/2026421789476401182).- Separate enterprise positioning: “Cowork and plugin updates” for customizing Claude across teams landed with extremely high engagement ( - [@claudeai](https://x.com/claudeai/status/2026305186671608315)).

- **Cursor: “review is demo videos, not diffs”**: Cursor announced a major UX pivot—agents can- **use the software they build**, then send- **videos of their work**(“demos, not diffs”) (- [launch](https://x.com/cursor_ai/status/2026369873321013568),- [links](https://x.com/cursor_ai/status/2026369880795263328)). Multiple builders describe cloud agents as a practical step-change: async, VM-based testing, self-verification, and demo artifacts (- [example](https://x.com/fredrikalindh/status/2026379400879730794),- [another](https://x.com/jsngr/status/2026371033201103036),- [“creative director over sims”](https://x.com/jasonyuan/status/2026375381872423133)).

**Diffusion for language: Inception Labs Mercury 2 and “speed as the next battleground”**

- **Mercury 2 (“reasoning diffusion LLM”)**: Inception Labs released- **Mercury 2**, positioning it as a production diffusion LLM hitting- **~1,000 output tokens/s**(- [Stefano Ermon](https://x.com/StefanoErmon/status/2026340720064520670)). Artificial Analysis contextualizes it as- *not*frontier-leading on intelligence, but unusually strong on- **output speed**with decent agentic/coding evaluations, including comparisons on Terminal-Bench Hard and IFBench scoring claims (- [analysis thread](https://x.com/ArtificialAnlys/status/2026360491799621744)).
- The deeper takeaway across these posts: teams are betting that - **architecture-level parallel token refinement**(diffusion) can make multi-step agent loops and voice assistants feel “native” rather than “batchy” (see the architectural explanation from- [@LiorOnAI](https://x.com/LiorOnAI/status/2026376138428395908)). This sits alongside broader sentiment that 2026 competition may be defined by- **latency + throughput**, not just raw benchmark maxima.

**Agents: reliability, safety failures, memory + context rot, and new multilingual evals**

- **Agent reliability is not keeping pace with capability**: A Princeton-led effort formalizes and measures the- **capability–reliability gap**, decomposing reliability into- **12 dimensions**and finding only modest reliability gains despite large capability gains (- [paper + dashboard](https://x.com/steverab/status/2026383575080108436); additional commentary from- [@random_walker](https://x.com/random_walker/status/2026384543700115870)). This aligns with recurring “long tail of failures” intuition from practitioners comparing agents to AVs (- [ahall_research](https://x.com/ahall_research/status/2026338695536848987)).
- **OpenClaw and “routine-step decomposition” safety bypass**: A concrete agent failure mode: “split a dangerous command into a few routine steps → safety is gone,” with inbox-wiping behavior cited; authors claim an open-source fix (- [paper thread](https://x.com/shi_weiyan/status/2026300129901445196)).
- **AGENTS.md (and equivalents) can hurt**: Two high-signal posts summarize research showing- **LLM-generated context files decrease success**while increasing costs; developer-written minimal context helps slightly but still increases cost. See- [@omarsar0](https://x.com/omarsar0/status/2026306141181898887)for the paper summary and- [@_philschmid](https://x.com/_philschmid/status/2026354033418547444)for a practical “how to write it” guide grounded in the same result set.
- **New SWE-bench Multilingual leaderboard**: A push to evaluate software engineering agents beyond English/Python. The leaderboard covers- **300 tasks in 9 languages**, none from SWE-bench Verified, with reported SOTA at- **72%**(- [launch](https://x.com/OfirPress/status/2026324248973689068); more stats from- [@KLieret](https://x.com/KLieret/status/2026322986907652295)). The implication: model rankings can invert across languages—important for global dev tooling and for data-collection strategies.

**Data + benchmarks: OCR saturation, “new optimizer” skepticism, and adaptive/continual data pitches**

- **OCR/document parsing benchmarks saturating**: Multiple posts argue OmniDocBench is hitting a ceiling (e.g.,- **~95%**with failures on real documents) and that exact-match metrics penalize semantically correct parses. See- [@llama_index](https://x.com/llama_index/status/2026342120236396844)and- [@jerryjliu0](https://x.com/jerryjliu0/status/2026408921385284001). Related: confusion at why OCR remains hard despite cheap synthetic data (- [gabriberton](https://x.com/gabriberton/status/2026335831632626156)) and a study suggesting text extraction beats image representations for PDF QA (- [cwolferesearch](https://x.com/cwolferesearch/status/2026344301907583469)).
- **“Nature MI optimizer” controversy**: A highly technical critique calls out suspicious baselines and potential test-set hyperparameter selection in a new optimizer paper with dramatic plots, urging independent validation and better-tuned baselines (e.g., nanogpt speedrun) (- [giffmana](https://x.com/giffmana/status/2026223201957597563); plus additional experimental context from- [@YouJiacheng](https://x.com/YouJiacheng/status/2026224486367027622)).
- **Adaption Labs: “Adaptive Data”**: Several tweets pitch a shift from static datasets to a “living asset” loop, with claims of- **82% average quality gains**across- **242 languages**and an early access/community program (- [company](https://x.com/adaptionlabs/status/2026281291847446721); additional framing from- [@sarahookr](https://x.com/sarahookr/status/2026286134104613157); third-party paraphrase- [here](https://x.com/sudip_r0y/status/2026286762851774475)). Treat as a directional thesis (data drift/feedback loops) rather than a validated standard until more methodology is public.

**Compute, chips, and robotics: Meta–AMD megadeal, MatX’s “HBM+SRAM” bet, and scaling humanoid control**

- **Meta ↔ AMD infrastructure deal**: Meta announced a multi-year agreement to integrate AMD Instinct GPUs with- **~6GW**planned data center capacity for the deployment (- [@AIatMeta](https://x.com/AIatMeta/status/2026266818789454057)). Commentary frames it as a major capex/compute signal on the eve of NVIDIA earnings (- [kimmonismus](https://x.com/kimmonismus/status/2026279386681356704)).
- **MatX “One” accelerator**: MatX announced a- **$500M Series B**and pitched a chip architecture combining- **systolic-array efficiency**with better utilization on smaller matrices, aiming for- **high throughput and low latency**, explicitly addressing long-context workloads via HBM while preserving SRAM-first latency characteristics (- [reinerpope](https://x.com/reinerpope/status/2026351870852358492)). Karpathy highlights the “two memory pools” constraint (SRAM vs DRAM/HBM) and frames memory+compute orchestration as a core puzzle for upcoming token demand (- [karpathy](https://x.com/karpathy/status/2026452488434651264)).
- **Liquid AI LFM2-24B-A2B**: Liquid AI released- **LFM2-24B-A2B**, a- **24B MoE**with- **~2.3B active/token**, optimized for efficiency and edge inference in a 32GB footprint (- [launch](https://x.com/liquidai/status/2026301771539202269)). Distribution arrived quickly across- **Ollama**(- [tweet](https://x.com/ollama/status/2026305296709173535)) and- **LM Studio**(- [tweet](https://x.com/lmstudio/status/2026322404142633131)).
- **Robotics scaling: NVIDIA SONIC (GEAR-SONIC)**: A standout robotics thread claims a- **42M-parameter**policy trained on- **100M+ mocap frames**and- **500k+ parallel simulated robots**, transferring- **zero-shot**to a real humanoid with- **100% success**across 50 sequences; code/weights are open (- [Jim Fan thread](https://x.com/DrJimFan/status/2026350142652383587), plus links- [here](https://x.com/DrJimFan/status/2026350144300658891)). The key “systems” claim is that dense supervision from motion tracking acts like a scalable analogue to next-token prediction for whole-body control.

**Top tweets (by engagement, technical/industry-relevant)**

- **Claude Code Remote Control**rollout:- [@claudeai](https://x.com/claudeai/status/2026418433911603668)
- **Qwen 3.5 Medium Model Series**release:- [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2026339351530188939)
- **Cursor agents ship “demos not diffs”**:- [@cursor_ai](https://x.com/cursor_ai/status/2026369873321013568)
- **Karpathy on CLIs as agent-native interface**:- [@karpathy](https://x.com/karpathy/status/2026360908398862478)
- **Meta–AMD 6GW infrastructure deal**:- [@AIatMeta](https://x.com/AIatMeta/status/2026266818789454057)
- **Mercury 2 diffusion LLM launch**:- [@StefanoErmon](https://x.com/StefanoErmon/status/2026340720064520670)
- **NVIDIA SONIC humanoid control (open source)**:- [@DrJimFan](https://x.com/DrJimFan/status/2026350142652383587)
- **MatX chip + $500M Series B**:- [@reinerpope](https://x.com/reinerpope/status/2026351870852358492)
- **AGENTS.md research summary (context can hurt)**:- [@omarsar0](https://x.com/omarsar0/status/2026306141181898887)
- **OpenAI GPT-5.3-Codex in Responses API**:- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2026379092661289260)

**AI Reddit Recap**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
