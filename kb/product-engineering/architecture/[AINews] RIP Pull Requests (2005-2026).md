---
title: '[AINews] RIP Pull Requests (2005-2026)'
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/computer-use
summary: Argues that agentic development changes the pull-request workflow and software
  delivery loop.
source: latent-space
url: https://www.latent.space/p/ainews-rip-pull-requests-2005-2026
author: Latent Space
published: '2026-04-16'
fetched: '2026-07-11T05:12:30Z'
classifier: codex
taxonomy_rev: 1
words: 1511
content_sha256: 652b79a93599d0f2d868ea03322a7ace46c7bdf70af45d7a78aa8c2bfbb53205
---

# [AINews] RIP Pull Requests (2005-2026)

# [AINews] RIP Pull Requests (2005-2026)

### a quiet day lets us report on the death of the pull requests

**Hot on the heels of  the Death of the Code Review, the Pull Request may be next.**

For anyone that learned to code in the last 15 years it is hard to imagine a life without Git, GitHub, and Pull Requests, but there was a time before them, and it well may come to pass that there is life after.

Pull Requests were arguably [invented in 2005](https://lore.kernel.org/git/20050726073036.GJ6098@mythryan2.michonline.com/), successfully [popularized by GitHub](https://github.blog/2008-02-23-oh-yeah-there-s-pull-requests-now/),  and only 21 years later, [GitHub is for the first time in history](https://x.com/SamMorrowDrums/status/2044375099738825103) allowing people to disable pull requests on their open source repos (you could only disable issues before).

![](https://substackcdn.com/image/fetch/$s_!bm4O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd974198b-3217-4de1-ae09-e8aba5710e67_1364x708.png)

The rise of Generative AI in code has spelled the pending death of the Pull Request for a while now — [Pete Steinberger is by now well known](https://www.youtube.com/watch?v=O_IMsEg91g8&t=4038s&pp=0gcJCdMKAYcqIYzv) (along with [Theo](https://x.com/thekitze/status/2030222687084359871?s=46)) for only wanting Prompt Requests rather than Pull Requests (for multiple reasons, eg 1) no merge conflicts, 2) it’s easier for the maintainer to fix/add to the prompt than to look at code, 3) less likely to have malicious/insecure code slipped into an innocent looking PR), and other folks like [Mitchell Hashimoto](https://news.ycombinator.com/item?id=46930961) and [Amp Code](https://ampcode.com/) have created “reputation”-based systems for handling untrusted code contributions.

In [Building for Trillions of Agents](https://x.com/levie/status/2030714592238956960?s=46), Aaron Levie noted that “the path forward is to make software that agents want.” Humans invented git for human collaboration reasons. It’s increasingly clear that Git-based workflows may not be suitable once we remove the human bottleneck from the flow of code.

And if Code Reviews are dead, and Pull Reviews are dead… how long until Git itself is dead?

AI News for 4/14/2026-4/15/2026. We checked 12 subreddits,

[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and no further Discords.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

**AI Twitter Recap**

**OpenAI Agents SDK Expansion and the New Sandbox-Oriented Agent Stack**

- **OpenAI split the agent harness from compute/storage**and pushed its Agents SDK toward- **long-running, durable agents**with primitives for- **file/computer use, skills, memory, and compaction**. The harness is now open-source and customizable, while execution can be delegated to partner sandboxes instead of being tightly coupled to OpenAI infra, per- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2044466699785920937),- [follow-up](https://x.com/OpenAIDevs/status/2044466729712304613), and- [@snsf](https://x.com/snsf/status/2044514160034324793). This effectively makes “Codex-style” agents more reproducible by third parties and shifts differentiation toward orchestration, state management, and secure execution.
- **A notable ecosystem formed around that launch immediately**:- [@CloudflareDev](https://x.com/CloudflareDev/status/2044467412607901877),- [@modal](https://x.com/modal/status/2044469736483000743),- [@daytonaio](https://x.com/daytonaio/status/2044473859047313464),- [@e2b](https://x.com/e2b/status/2044476275067416751), and- [@vercel_dev](https://x.com/vercel_dev/status/2044492058073960733)all announced official sandbox integrations. The practical pattern is converging on- **stateless orchestration + stateful isolated workspaces**. Example builds already appeared, including a Modal-backed ML research agent with- **GPU sandboxes, subagents, persistent memory, and fork/resume snapshots**from- [@akshat_b](https://x.com/akshat_b/status/2044489564211880169), and Cloudflare guides for Python agents that execute tasks in a sandbox and copy outputs locally from- [@whoiskatrin](https://x.com/whoiskatrin/status/2044477140662395182).

**Cloudflare’s Project Think, Agent Lee, and Voice Agents**

- **Cloudflare had one of the busiest agent-infra release cycles**.- [@whoiskatrin](https://x.com/whoiskatrin/status/2044415568627847671)and- [@aninibread](https://x.com/aninibread/status/2044409784133103724)introduced- **Project Think**, a next-gen Agents SDK centered on- **durable execution, sub-agents, persistent sessions, sandboxed code execution, a built-in workspace filesystem, and runtime tool creation**. In parallel,- [@Cloudflare](https://x.com/Cloudflare/status/2044406215208316985)launched- **Agent Lee**, an in-dashboard agent using- **sandboxed TypeScript**to shift Cloudflare’s UI from manual tab navigation to prompt-driven operations;- [@BraydenWilmoth](https://x.com/BraydenWilmoth/status/2044422996765352226)showed it issuing infra tasks and generating UI-backed results.
- **Voice and browser tooling also moved into the core stack**.- [@Cloudflare](https://x.com/Cloudflare/status/2044423032265957872)shipped an experimental- **real-time voice pipeline over WebSockets**for continuous STT/TTS, while- [@korinne_dev](https://x.com/korinne_dev/status/2044441427736936510)described voice as just another input channel over the same agent connection. On browser automation,- [@kathyyliao](https://x.com/kathyyliao/status/2044479579382026484)summarized the rebranded- **Browser Run**stack:- **Live View, human-in-the-loop intervention, session recordings, CDP endpoints, WebMCP support, and higher limits**. Taken together, Cloudflare is making a strong case that the production agent platform is really a composition of- **durable runtime + UI grounding + browser + voice + sandbox**.

**Hermes Agent’s Self-Improving Workflow and Competitive Positioning**

- **Hermes Agent’s distinctive idea is not just tool use but persistent skill formation**. A Chinese-language comparison from- [@joshesye](https://x.com/joshesye/status/2044295313171571086)contrasts- **OpenClaw**as a more GUI-first, ready-to-use personal assistant with- **Hermes**as a “professional” agent that decides whether a completed workflow is reusable and automatically turns it into a- **Skill**. This “learn from completed tasks” framing appeared repeatedly:- [@chooseliberty](https://x.com/chooseliberty/status/2044425487141781660)showed Hermes autonomously backfilling tracking data, updating a cron job, then saving the workflow as a reusable skill;- [@NeoAIForecast](https://x.com/NeoAIForecast/status/2044521045013762389)emphasized session hygiene and thread branching/search as critical to turning Hermes into a real work environment rather than a disposable chat box.
- **Community sentiment strongly positioned Hermes against OpenClaw**, often bluntly. Examples include- [@vrloom](https://x.com/vrloom/status/2044506378103099816),- [@theCTO](https://x.com/theCTO/status/2044559179151773933), and- [@Teknium](https://x.com/Teknium/status/2044482769536045194)highlighting Hermes’ role in real workflows, including the now-viral autonomous- **Gemma 4 “abliteration”**story from- [@elder_plinius](https://x.com/elder_plinius/status/2044462515443372276): the agent loaded a stored skill, diagnosed NaN instability in Gemma 4, patched the underlying library, retried multiple methods, benchmarked the result, generated a model card, and uploaded artifacts to Hugging Face. There were also concrete product additions:- **browser control via**- `/browser connect`from- [@0xme66](https://x.com/0xme66/status/2044410470770331913),- **QQBot + AWS Bedrock support**from- [@Teknium](https://x.com/Teknium/status/2044557360962871711), a native Swift desktop app alpha from- [@nesquena](https://x.com/nesquena/status/2044516572983923021), and ongoing ecosystem tooling like- [artifact-preview](https://x.com/ChuckSRQ/status/2044504539978465658)and- [hermes-lcm v0.3.0](https://x.com/SteveSchoettler/status/2044536537434755493).

**Model, Architecture, and Training Releases: Sparse Diffusion, Looped Transformers, and Efficient Long-Context MoEs**

- **Several technically meaningful open releases landed across modalities**.- [@withnucleusai](https://x.com/withnucleusai/status/2044412335473713284)announced- **Nucleus-Image**, positioned as the first sparse MoE diffusion model:- **17B parameters, 2B active**, Apache 2.0, with weights, training code, and dataset recipe, and day-0 support in diffusers. NVIDIA followed with- **Lyra 2.0**, a framework for generating- **persistent, explorable 3D worlds**that maintains per-frame 3D geometry and uses self-augmented training to reduce temporal drift, per- [@NVIDIAAIDev](https://x.com/NVIDIAAIDev/status/2044445645109436672). On multimodal retrieval,- [@thewebAI](https://x.com/thewebAI/status/2044435998508240926)open-sourced- **webAI-ColVec1**, claiming top ViDoRe V3 performance for document retrieval- **without OCR or preprocessing**.
- **Architecture research around compute efficiency was especially strong**.- [@hayden_prairie](https://x.com/hayden_prairie/status/2044453231913537927),- [@realDanFu](https://x.com/realDanFu/status/2044459930149941304), and- [@togethercompute](https://x.com/togethercompute/status/2044454051543453745)introduced- **Parcae**, a stabilized- **layer-looping Transformer**formulation. The claim: for fixed parameter budgets, looping blocks can recover the quality of a- **model roughly 2x the size**, yielding a new scaling axis where- **FLOPs scale via looping, not just parameters/data**. NVIDIA also surfaced- **Nemotron 3 Super**, summarized by- [@dair_ai](https://x.com/dair_ai/status/2044452957023047943): an- **open 120B hybrid Mamba-Attention MoE with 12B active parameters**,- **1M context**, trained on- **25T tokens**, with up to- **2.2x throughput vs GPT-OSS-120B**and- **7.5x vs Qwen3.5-122B**. These releases collectively point to a theme:- **memory bandwidth and long-context throughput**are increasingly first-class architectural objectives.

**Google/Gemini’s Product Surge: Mac App, Personal Intelligence, TTS, and Open Multimodal Models**

- **Google stacked multiple launches in one cycle**. The most visible was the native- **Gemini app for Mac**, announced by- [@GeminiApp](https://x.com/GeminiApp/status/2044445911716090212),- [@joshwoodward](https://x.com/joshwoodward/status/2044452201947627709), and- [@sundarpichai](https://x.com/sundarpichai/status/2044452464724967550):- **Option + Space activation, screen sharing, local file context**, native Swift implementation, and broad macOS availability. In parallel,- **Personal Intelligence**expanded globally in Gemini and into Chrome, allowing users to connect signals from products like- **Gmail and Photos**, framed around transparency and user-controlled app connections by- [@Google](https://x.com/Google/status/2044437335425564691)and- [@GeminiApp](https://x.com/GeminiApp/status/2044430579996020815).
- **The more technically interesting model launch was Gemini 3.1 Flash TTS**.- [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2044447030353752349),- [@OfficialLoganK](https://x.com/OfficialLoganK/status/2044447596010435054), and- [@demishassabis](https://x.com/demishassabis/status/2044599020690010217)positioned it as a highly controllable TTS model with- **Audio Tags**,- **70+ languages**, inline nonverbal cues, multi-speaker support, and- **SynthID watermarking**. Independent evaluation from- [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2044450045190418673)put it at- **#2 on its Speech Arena**, just- **4 Elo behind**the top model. Google also open-sourced- **TIPS v2**, a foundational- **text-image encoder under Apache 2.0**with new pretraining recipes, via- [@osanseviero](https://x.com/osanseviero/status/2044520603647164735), and the community flagged the day as unusually dense for Google AI product velocity.

**Research Signals: AI-Assisted Math, Long-Horizon Agents, Eval Shifts, and Open Data**

- **The highest-signal research discourse was around AI-assisted mathematics**.- [@jdlichtman](https://x.com/jdlichtman/status/2044298382852927894)reported that- **GPT-5.4 Pro**produced a proof for- **Erdős problem #1196**, surprising experts by rejecting a long-assumed proof gambit and instead exploiting a technically counterintuitive analytic path using the- **von Mangoldt function**. Follow-ups from- [@jdlichtman](https://x.com/jdlichtman/status/2044307082275618993),- [@thomasfbloom](https://x.com/thomasfbloom/status/2044319103310021078),- [@gdb](https://x.com/gdb/status/2044436998648193333), and others framed it as potentially the first AI-generated- **“Book Proof”**broadly respected by mathematicians. That matters less as a one-off result than as evidence that models may now occasionally find- **non-aesthetic but compact lines of attack**in mature research spaces.
- **Long-horizon agent research also kept converging on state management and harness design**.- [@omarsar0](https://x.com/omarsar0/status/2044436099121209546)summarized- **AiScientist**, where a thin orchestrator coordinates specialized agents through durable workspace artifacts in a- **File-as-Bus**pattern; removing that bus hurts PaperBench and MLE-Bench Lite materially.- [@dair_ai](https://x.com/dair_ai/status/2044435861580984700)highlighted- **Pioneer Agent**for continual small-model improvement loops, while- [@yoonholeee](https://x.com/yoonholeee/status/2044442372864700510)open-sourced- **Meta-Harness**, a repo meant to help users implement robust harnesses in new domains. On evals,- [@METR_Evals](https://x.com/METR_Evals/status/2044463380057194868)estimated- **Gemini 3.1 Pro (high thinking)**at a- **50% time horizon of ~6.4 hours**on software tasks, and- [@arena](https://x.com/arena/status/2044437193205395458)showed- **Document Arena**top ranks shifting with- **Claude Opus 4.6 Thinking**at #1 and- **Kimi-K2.5 Thinking**as the best open model. Meanwhile,- [@TeraflopAI](https://x.com/TeraflopAI/status/2044430993549832615)released- **43B tokens of SEC EDGAR data**, reinforcing the day’s broader push toward more open datasets and open infrastructure.

**Top tweets (by engagement)**

- **Gemini on Mac**:- [@sundarpichai](https://x.com/sundarpichai/status/2044452464724967550)and- [@GeminiApp](https://x.com/GeminiApp/status/2044445911716090212)drove the biggest launch engagement around the native desktop app.
- **Gemini 3.1 Flash TTS**:- [@OfficialLoganK](https://x.com/OfficialLoganK/status/2044447596010435054)and- [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2044447030353752349)highlighted a materially more controllable TTS stack.
- **AI-assisted math proof**:- [@jdlichtman](https://x.com/jdlichtman/status/2044298382852927894)and- [@gdb](https://x.com/gdb/status/2044436998648193333)sparked the strongest research discussion of the day.
- **OpenAI Agents SDK update**:- [@OpenAIDevs](https://x.com/OpenAIDevs/status/2044466699785920937)marked a meaningful platform shift toward open harnesses and partner sandboxes.
- **Anthropic’s subliminal learning paper in Nature**:- [@AnthropicAI](https://x.com/AnthropicAI/status/2044493337835802948)drew major attention to hidden-trait transmission through training data.

**AI Reddit Recap**

**/r/LocalLlama + /r/localLLM Recap**

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
