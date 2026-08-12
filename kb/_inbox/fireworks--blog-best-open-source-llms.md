---
title: 'Best Open Source LLMs in 2026: We Reviewed 7 Models'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/best-open-source-llms
author: null
published: '2026-07-08'
fetched: '2026-08-12T06:28:23Z'
classifier: null
taxonomy_rev: 2
words: 5960
content_sha256: da7c7d8d9860a7f1cdbc7afa644da385216f6951115a0b6081db2c8a1e24003b
---

# Best Open Source LLMs in 2026: We Reviewed 7 Models

With new open source LLMs launching constantly, figuring out which model actually fits your use case has become its own endeavor.

The open-source model landscape is moving fast in 2026. [GLM 5.2](https://fireworks.ai/models/fireworks/glm-5p2), [Kimi K3](https://www.kimi.com/blog/kimi-k3) (described by Kimi as open source, though its full weights pending, scheduled for released by July 27, 2026), [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code), [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3), and [DeepSeek-V4-Pro](https://fireworks.ai/models/fireworks/deepseek-v4-pro) all launched between April and July, and several now sit within a few benchmark points of frontier models at a fraction of the serving cost.

The right model depends on four constraints: benchmark quality, context window, modality support, and license terms. A model that leads on composite quality but lacks image input loses to a weaker model when screenshots or visual documents are part of the product. A model with a trillion-parameter MoE architecture and a 1,040k-token context window is the wrong default for a high-throughput extraction route where a smaller, faster model finishes the job at lower cost.

**TL;DR**

The table below spans models for general reasoning, coding, multimodal, long-context, and high-throughput workloads.

Kimi K3 has the highest Artificial Analysis Intelligence and Coding Index scores among the nine models evaluated here. Its weights and license are still pending.

GLM 5.2 leads both indexes among open models available on Fireworks. Other models remain competitive when modality, context window, licensing, or serving cost sets the constraint.

Use the benchmark tables to narrow the field, then run task-level evals before choosing a production route.

| Model | Release date | Params | Context window | Best for | On Fireworks | 
|---|---|---|---|---|---|
| [GLM 5.2](https://fireworks.ai/models/fireworks/glm-5p2) | June 2026 | 743B total | 1,040k tokens | Strongest benchmark profile among currently open models in this set. First eval for broad reasoning, coding, and long-context agents. | [Try in playground](https://fireworks.ai/models/fireworks/glm-5p2) | 
| [Kimi K3](https://www.kimi.com/blog/kimi-k3) | July 2026 | 2.8T total, 16 of 896 experts active | 1M tokens | Benchmark leader awaiting full weights and a Fireworks listing. License details remain unpublished. | Not yet listed | 
| [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code) | June 2026 | 1.02T total | 262k tokens | Coding agents, repository work, patch planning, and multimodal developer tools. Thinking mode is mandatory. | [Try in playground](https://fireworks.ai/models/fireworks/kimi-k2p7-code) | 
| [DeepSeek-V4-Pro](https://fireworks.ai/models/fireworks/deepseek-v4-pro) | April 2026 | 1.6T total | 1,040k tokens | Long-context reasoning and coding from a separate open-source family. Second eval when GLM 5.2 misses on your repo. | [Try in playground](https://fireworks.ai/models/fireworks/deepseek-v4-pro) | 
| [DeepSeek-V4-Flash](https://fireworks.ai/models/fireworks/deepseek-v4-flash) | April 2026 | 284B total | 1,040k tokens | Same 1,040k context class as Pro at higher throughput and lower cost. Default DeepSeek route for high-volume workloads. | [Try in playground](https://fireworks.ai/models/fireworks/deepseek-v4-flash) | 
| [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3) | June 202622, 2025 | 428B total, about 23B activated | 512k tokens | Native image and video input, second-highest GPQA score in the table. First eval when multimodality sets the constraint. | [Try in playground](https://fireworks.ai/models/fireworks/minimax-m3) | 
| [Qwen3.7 Plus](https://fireworks.ai/models/fireworks/qwen3p7-plus) | June 2026 | N/A | 262k tokens | Closed-weight Qwen-family model with image input and training support through Fireworks. Review license before production. | [Try in playground](https://fireworks.ai/models/fireworks/qwen3p7-plus) | 
| [gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b) | August 2025 | 116B total | 131k tokens | Apache-2.0 licensing and fastest median output in this set at 271.4 tokens/second. For bounded, high-throughput tasks. | [Try in playground](https://fireworks.ai/models/fireworks/gpt-oss-120b) | 
| [Gemma 4 31B IT](https://fireworks.ai/models/fireworks/gemma-4-31b-it) | April 2026 | 32.2B dense | 262k tokens | Smaller dense multimodal model with Apache-2.0 licensing and an On-Demand deployment path. First eval when adaptation and deployment control matter more than frontier benchmark rank. | [View On-Demand model](https://fireworks.ai/models/fireworks/gemma-4-31b-it) | 

Architecture helps narrow the evaluation set. A trillion-parameter MoE model can route each token through a smaller active subset, but parameter counts do not establish serving cost or latency. Measure both on the route and workload you plan to use.

Context window size counts only when the model holds coherence at length. A million-token-class context window is useful for codebases, large collections of legal documents, retrieval-heavy agents, and document workflows. A million-token context window only helps if the model can stay coherent for the entire prompt. If it loses track of earlier instructions or evidence halfway through, you end up paying for extra context that does not improve the output.

Licensing and access to the model weights determine whether you can use the model in production. Apache-2.0 and MIT are easier for most teams to approve.

Not all “open source” model licenses are equally simple to use in production. Licenses like Modified MIT and the MiniMax Community license can still be acceptable, but they usually come with extra conditions, so they should be reviewed before you commit to a model. Qwen3.7 Plus is closed weights, so legal and training terms should go through legal review before the model is evaluated.

Model selection is not only about benchmarks. Your deployment path (Serverless or dedicated) determines which models fit your latency, cost, and capacity requirements.

Serverless works for fast trials and bursty traffic. On-Demand fits dedicated capacity, stricter latency targets, and predictable production volume. If you keep repeating the same constraints in prompt after prompt, that is the signal to add post-training to the rollout plan.

When we compared these open source LLMs, we focused on the factors that most directly determine whether a model will work for a real workload: benchmark performance, context window length, license or weight access, multimodal support, and the serving path you plan to run in production.

The benchmark mix covers broad intelligence, hard science reasoning, coding ability, scientific coding, and output speed. Artificial Analysis [Intelligence Index](https://artificialanalysis.ai/#intelligence) and [Coding Index](https://artificialanalysis.ai/models/capabilities/coding) identify first-pass candidates. Use [GPQA](https://artificialanalysis.ai/evaluations/gpqa-diamond), [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam), and [SciCode](https://artificialanalysis.ai/evaluations/scicode) to find where a model breaks under harder prompts.

| Model | AAII | GPQA | HLE | 
|---|---|---|---|
| Kimi K3 | 57.1 | 93.5% | 44.3% | 
| GLM 5.2 | 51.1 | 89.5% | 40.1% | 
| MiniMax M3 | 44.4 | 92.9% | 37.1% | 
| DeepSeek-V4-Pro | 44.3 | 88.8% | 35.9% | 
| Kimi K2.7 Code | 41.9 | 89.6% | 32.8% | 
| DeepSeek-V4-Flash | 40.3 | 89.4% | 32.1% | 
| Qwen3.7 Plus | 39.0 | 90.0% | 33.4% | 
| Gemma 4 31B IT | 29.4 | 85.7% | 22.7% | 
| gpt-oss-120b | 23.8 | 78.2% | 18.5% | 
| Claude Fable 5 | 59.9 | 92.6% | 53.3% | 
| Claude Opus 4.8 | 55.7 | 92.0% | 45.7% | 

- •**Artificial Analysis Intelligence Index:** A composite score across hard model evaluations, including GPQA, HLE, SciCode, AA-LCR, and other tasks.
- •**GPQA:** Graduate-level science reasoning.
- •**HLE:** Humanity's Last Exam, a hard knowledge and reasoning benchmark where most models still have low absolute scores.

| Model | AACI | SciCode | Median output speed | 
|---|---|---|---|
| Kimi K3 | 76.2 | 58.7% | 58.5 tok/sec | 
| GLM 5.2 | 68.8 | 50.5% | 165.3 tok/sec | 
| Kimi K2.7 Code | 60.8 | 47.5% | 43.2 tok/sec | 
| DeepSeek-V4-Pro | 59.4 | 50.0% | 60.1 tok/sec | 
| MiniMax M3 | 58.6 | 45.4% | 91.7 tok/sec | 
| DeepSeek-V4-Flash | 56.2 | 44.9% | 97.9 tok/sec | 
| Qwen3.7 Plus | 55.9 | 45.5% | 53.0 tok/sec | 
| Gemma 4 31B IT | 43.4 | 43.4% | 35.9 tok/sec | 
| gpt-oss-120b | 30.4 | 38.9% | 271.4 tok/sec | 
| Claude Fable 5 | 76.5 | 60.2% | 56.5 tok/sec | 
| Claude Opus 4.8 | 74.3 | 53.5% | 54.1 tok/sec | 

- •**Artificial Analysis Coding Index:** A composite coding score for software engineering tasks.
- •**SciCode:** Scientific coding and reasoning tasks.
- •**Median output speed:** The median generated-token rate. Actual serving speed varies by model, route, prompt shape, and workload.

Scores current as of July 18, 2026. Actual performance varies by prompt, quantization, and inference settings.

- •Kimi K3 has the highest Intelligence and Coding Index scores among the nine models in the table. GLM 5.2 is the highest-scoring open model available on Fireworks today.
- •GLM 5.2 is the first open-model quality eval across Intelligence Index and Coding Index. Fable 5 is the stronger composite reference, while Opus 4.8 provides continuity with earlier frontier comparisons.
- •DeepSeek-V4-Pro and DeepSeek-V4-Flash give you two DeepSeek 1,040k-context routes: Pro for quality and Flash for generated-token rate.
- •MiniMax M3 is the multimodal pick: second-highest GPQA score here, 512k context, and native image and video support.
- •Qwen3.7 Plus is the closed-weights Qwen-family candidate when Fireworks access, image input, 262k context, and supported training workflows matter.
- •gpt-oss-120b is the speed and Apache-2.0 route, but it trails the 2026 open frontier on composite quality.

- •**Release date:** June 2026
- •**Parameters** : 743B total
- •**Context window:** 1,040k tokens on Fireworks
- •**License:** MIT license
- •**Corporate sponsor:**[Z.ai](https://z.ai/blog/glm-5.2)
- •**Model repo:**[zai-org/GLM-5](https://github.com/zai-org/GLM-5)

[GLM-5.2](https://fireworks.ai/models/fireworks/glm-5p2) is [Z.ai's](https://z.ai/blog/glm-5.2) flagship coding model, a 743B-parameter MoE with a 1,040k-token context window on Fireworks. Its IndexShare architecture reuses indexers across sparse attention layers and reduces per-token FLOPs by 2.9x at full context.

The [GLM-5](https://z.ai/blog/glm-5.2) line is built for long coding tasks and context-heavy tool use. GLM 5.2 adds a 1,040k context window, flexible reasoning effort, and a first eval fit for codebase context, multi-document retrieval, implementation planning, and tool-calling agents.

GLM 5.2 posts the highest composite scores of any model currently available on Fireworks in this table: [51.1 on the Intelligence Index](https://artificialanalysis.ai/models/glm-5-2) and [68.8 on the Coding Index](https://artificialanalysis.ai/models/capabilities/coding).

Use GLM 5.2 as the default first eval for broad reasoning, coding, retrieval-heavy agents, and document workflows. It gives teams one baseline before they split work across specialized models.

GLM 5.2 is strongest when the workload needs both long context and function calling. If the request includes images, start with Kimi K2.7 Code, MiniMax M3, or Qwen3.7 Plus instead.

- •Highest Intelligence Index score among currently open, Fireworks-available models here: 51.1
- •Highest Coding Index score among currently open, Fireworks-available models here: 68.8
- •1,040k context window on Fireworks
- •Function calling support
- •Serverless and On-Demand availability on Fireworks
- •165.3 tokens/second median output

| Pros | Cons | 
|---|---|
| Strongest benchmark row among currently open, Fireworks-available models here | Larger model than most simple production tasks need | 
| 1,040k context for long documents and codebases | Text-only; no image input | 
| Function calling support | Requires task-level latency and cost testing against smaller routes | 
| Serverless access makes evaluation fast | Text-only workloads should still be tested against multimodal alternatives when image input is likely | 

**Q: How much context should you test with GLM 5.2?**

Start with the longest prompt your product can justify. Use a real repo, set of documents, support history, or retrieval trace. GLM 5.2 is the right pick when it keeps evidence coherent near the end of a 1,040k-context run.

**Q: What does IndexShare change for GLM 5.2?**

[__IndexShare__](https://z.ai/blog/glm-5.2) reduces per-token FLOPs at long context. That helps the model stay practical for codebase analysis, multi-document reasoning, and long tool traces where a cheaper short-context model would need repeated retrieval loops.

**Q: Is GLM 5.2 multimodal?**

No. GLM 5.2 is a text model for long-horizon coding and agentic work. Use Kimi K2.7 Code, MiniMax M3, or Qwen3.7 Plus when screenshots, design files, or visual documents are part of the product.

**Q: When should GLM 5.2 call tools?**

Use function calling when the model needs fresh data, structured lookups, or repeatable actions. Keep the first eval simple. Use one long context and one or two tools, then score citations, tool arguments, and final answer quality.

- •**Release date:** July 16, 2026
- •**Available on Fireworks:** July 27, 2026
- •**Parameters:** 2.8T total; Stable LatentMoE effectively activates 16 of 896 experts
- •**Context window:** 1M tokens
- •**Release status:** Full weights scheduled for release on July 27; license not yet published
- •**Artificial Analysis comparative provider price:** $3 input and $15 output per million tokens in the July 16 snapshot
- •**Artificial Analysis Intelligence Index:** 57.1
- •**Artificial Analysis Coding Index:** 76.2
- •**GPQA:** 93.5%

[Kimi K3](https://www.kimi.com/blog/kimi-k3) is Moonshot's 2.8-trillion-parameter mixture-of-experts model. Stable LatentMoE effectively activates 16 of 896 experts, while Kimi Delta Attention and Attention Residuals form the rest of the named architecture. The model also supports native vision and a one-million-token context window.

Kimi K3 leads every featured model on the July 16 Artificial Analysis Intelligence and Coding indexes. It also scores 93.5% on GPQA, 44.3% on HLE, and 58.7% on SciCode. Vision, long-context retrieval, repository-scale completion, and tool-use reliability still need workload-specific evaluation.

K3 was $3 per million input tokens and $15 per million output tokens in the Artificial Analysis comparative provider snapshot. Kimi K2.7 Code was $0.95 and $4.

Evaluate Kimi K3 when the test set includes difficult coding or reasoning tasks and the application may need image input or very long context. Use a representative repository task or retrieval trace, and include screenshots when vision will be a part of your workloads.

K3 is a weaker default for bounded extraction or classification. For high-volume summarization, start with a smaller, faster model and promote to K3 only if your evals show a clear quality lift. Compare completion rate and total task cost before choosing the larger model.

- •57.1 Artificial Analysis Intelligence Index
- •76.2 Artificial Analysis Coding Index
- •93.5% GPQA
- •One-million-token context window
- •Native vision
- •2.8T-parameter MoE; Stable LatentMoE effectively activates 16 of 896 experts

| Pros | Cons | 
|---|---|
| Highest Intelligence and Coding Index scores among the featured models | Full weights are estimated to be released July 27; the license has not been published | 
| Native vision and a one-million-token context window qualify it for multimodal and long-context evals | Higher comparative API price than Kimi K2.7 Code in the July 16 Artificial Analysis data | 
| Strong benchmark results support hard reasoning and technical evaluation | Dropping thinking history or switching to K3 mid-session can destabilize generation | 
| Stable LatentMoE effectively activates 16 of 896 experts | Moonshot recommends supernodes with 64 or more accelerators for self-hosting, and KDA creates new challenges for conventional prefix caching | 

**Q: Is Kimi K3 open source?**

Kimi describes K3 as open source. [Its full weights are scheduled for release by July 27, 2026](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart). Its license is not yet public. Teams with open-weight procurement requirements should wait for both artifacts.

**Q: Is Kimi K3 available on Fireworks?**

Kimi K3 is not yet available on the Fireworks model catalog. [__Kimi K2.7 Code__](https://fireworks.ai/models/fireworks/kimi-k2p7-code) is a current catalog-backed Kimi option.

**Q: What should an agent integration preserve across Kimi K3 turns?**

Preserve the model's thinking history and keep behavioral constraints explicit. Dropped thinking history or a mid-session switch to K3 can make generation unstable. K3 can also [__act too proactively__](https://www.kimi.com/blog/kimi-k3) when the user's intent is ambiguous.

- •**Release date:** June 2026
- •**Parameters:** 1.02T total
- •**Context window:** 262k tokens on Fireworks
- •**License:** Modified MIT
- •**Corporate sponsor:** Moonshot AI
- •**Model card:**[__moonshotai/Kimi-K2.7-Code__](https://huggingface.co/moonshotai/Kimi-K2.7-Code)

**🚀 Try Kimi K2.7 Code on Fireworks →**

[Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code) is a coding-specialized 1.02T-parameter MoE model from [Moonshot AI](https://www.moonshot.ai/) with a 262k-token context window. It runs on Fireworks Serverless and On-Demand, supports fine-tuning, and accepts both text and image input. Use it for repository agents that need file search and patch planning, including test-repair loops that use UI screenshots. Thinking mode is mandatory and cannot be disabled.

Kimi K2.7 Code scores 60.8 on the [Coding Index](https://artificialanalysis.ai/models/capabilities/coding) and 47.5% on SciCode. GLM 5.2 has the higher Coding Index score. Kimi K2.7 Code belongs in the eval when the workflow needs image input for UI debugging, screenshot review, or design-to-code tasks.

Use Kimi K2.7 Code for repository agents, code review, bug fixing, IDE copilots, and test generation. It belongs in evals when the model needs to inspect code, propose diffs, reason through failures, and use tool calls.

Teams building screenshot-driven developer tools should give Kimi K2.7 serious consideration. Image input gives Kimi a path into UI analysis, design-to-code workflows, and debugging flows when logs are not enough.

- •60.8 Coding Index for code-heavy tasks
- •1.02T total parameters
- •Image input and function calling on Fireworks
- •Serverless, On-Demand, and fine-tune availability
- •262k context window on Fireworks
- •Modified MIT license

| Pros | Cons | 
|---|---|
| Strong fit for repository agents and code review | Lower broad Intelligence Index than GLM 5.2, DeepSeek-V4-Pro, and MiniMax M3 | 
| Supports image input on Fireworks | Modified MIT license needs review | 
| Fine-tuning path on Fireworks | 262k context is shorter than GLM 5.2 and both DeepSeek V4 models | 
| Better fit for code-specific products than generic chat | Median output speed trails GLM 5.2, DeepSeek-V4-Pro, DeepSeek-V4-Flash, MiniMax M3, and gpt-oss-120b | 

**Q: What changed from earlier Kimi K2 releases?**

Kimi K2.7 Code is tuned for coding-agent workflows and uses fewer thinking tokens than Kimi K2.6. That helps when the product runs many patch-planning, review, and repair loops instead of one isolated prompt.

**Q: What should a Kimi K2.7 Code eval include?**

Use a real repository task with file retrieval, patch planning, tool execution, and failed-test repair. Single-prompt code generation will understate the model's value if your product depends on multi-step agent behavior.

**Q: Is Kimi K2.7 Code multimodal on Fireworks?**

Yes. Kimi K2.7 Code accepts image input on Fireworks, which makes it a better fit than GLM 5.2 for UI debugging, screenshot review, and design-to-code workflows.

**Q: When should you fine-tune Kimi K2.7 Code?**

Fine-tune only after prompt instructions repeat across many traces. If the model keeps needing the same code style, review policy, or repository convention in every prompt, move that behavior into the model instead of lengthening the system message.

- •**Release date:** April 2026
- •**Parameters:** 1.6T total
- •**Context window:** 1,040k tokens on Fireworks
- •**License:** MIT
- •**Corporate sponsor:** DeepSeek
- •**Provider GitHub:**[deepseek-ai](https://github.com/deepseek-ai)

**🚀 Try DeepSeek-V4-Pro on Fireworks →**

[DeepSeek-V4-Pro](https://fireworks.ai/models/fireworks/deepseek-v4-pro) is a large MoE model for reasoning, coding, and long-context work from [DeepSeek](https://www.deepseek.com/). It runs on Fireworks Serverless and On-Demand with function calling and a 1,040k context window, and ships under an MIT License. At 1.6T total parameters, it is the second-largest model in this set by total parameter count, behind Kimi K3's 2.8T.

If GLM 5.2 starts losing the thread on very long prompts, test DeepSeek-V4-Pro as a fallback, since it can handle the same long-context workload while giving you a different model family with different failure modes. DeepSeek-V4-Pro trails GLM 5.2 on composite quality but beats MiniMax M3, DeepSeek-V4-Flash, Qwen3.7 Plus, gpt-oss-120b, and Gemma 4 31B IT on the Coding Index.

Use DeepSeek-V4-Pro when you need long context and a model family separate from GLM. It belongs in evals for hard reasoning, coding agents, repository-scale analysis, and long evidence sets.

DeepSeek-V4-Pro is also useful as a second long-context candidate. If GLM 5.2 behaves poorly on your internal evals, DeepSeek-V4-Pro gives you another 1,040k-context route without changing the serving platform.

- •Open-source DeepSeek V4 family
- •1,040k context on Fireworks
- •1.6T total parameters
- •59.4 Coding Index
- •50.0% SciCode
- •Serverless and On-Demand availability on Fireworks

| Pros | Cons | 
|---|---|
| Separate open-source family from GLM | Larger model than DeepSeek-V4-Flash for routine calls | 
| 1,040k context on Fireworks | Requires matched latency and cost testing against DeepSeek-V4-Flash | 
| Strong coding and reasoning profile | Text-only; no image input | 
| Different frontier open-weight family than GLM | Lower Intelligence Index than GLM 5.2 | 

**Q: What does DeepSeek-V4-Pro add to a GLM 5.2 eval?**

DeepSeek-V4-Pro gives you a second 1,040k-context family with different failure modes. Keep it in the eval when one model overfits your prompt style or loses citations in long evidence sets.

**Q: When is DeepSeek-V4-Pro worth the higher serving cost?**

Use Pro for long-document review, repository-scale refactors, complex reasoning traces, and high-stakes agent routes. Use Flash first when the task is repetitive and easy to grade.

**Q: Is DeepSeek-V4-Pro multimodal?**

No. DeepSeek-V4-Pro is a text model for reasoning, coding, and long-context work. Use Kimi K2.7 Code, MiniMax M3, Qwen3.7 Plus, or Gemma 4 31B IT when image input belongs in the same request.

**Q: What should you test before choosing DeepSeek-V4-Pro?**

Test the exact long-context shape you plan to run in production. DeepSeek-V4-Pro should keep citations, tool outputs, or repository evidence coherent beyond the point where shorter-context models fail.

- •**Release date:** April 2026
- •**Parameters:** 284B total
- •**Context window:** 1,040k tokens on Fireworks
- •**License:** MIT License
- •**Corporate sponsor:** DeepSeek
- •**Provider GitHub:**[__deepseek-ai__](https://github.com/deepseek-ai)

**🚀 Try DeepSeek-V4-Flash on Fireworks →**

[DeepSeek-V4-Flash](https://fireworks.ai/models/fireworks/deepseek-v4-flash) is the faster V4 route for long-context reasoning and agent work. It keeps the 1,040k context window on Fireworks with a 284B MoE design.

DeepSeek-V4-Flash reaches 40.3 on Intelligence Index and 56.2 on Coding Index. It trails DeepSeek-V4-Pro on quality, but it is much closer to Pro than the parameter count suggests and runs faster in the median output-speed row.

Use DeepSeek-V4-Flash when the workload needs 1,040k context and generated-token rate more than the last few benchmark points. It fits retrieval-heavy agents, long-document analysis, and background coding tasks where the model has to read a lot but does not need the strongest open-weight quality model.

DeepSeek-V4-Flash is also the better DeepSeek default for high-volume routes. Promote DeepSeek-V4-Pro only when your eval shows that Flash misses decisions Pro gets right.

- •Open-source DeepSeek V4 family
- •1,040k context on Fireworks
- •284B total parameters
- •56.2 Coding Index
- •97.9 tokens/second median output
- •Serverless and On-Demand availability on Fireworks

| Pros | Cons | 
|---|---|
| Optimized for lower latency and higher throughput | Lower Intelligence Index and Coding Index than DeepSeek-V4-Pro | 
| Same 1,040k context class as DeepSeek-V4-Pro | Text-only; no image input | 
| Faster median output than DeepSeek-V4-Pro | Requires matched evaluation against DeepSeek-V4-Pro on hard reasoning traces | 
| Separate DeepSeek V4 family | Not the first quality eval when GLM 5.2 is available | 

**Q: When does DeepSeek-V4-Flash beat DeepSeek-V4-Pro?**

Flash wins when the prompt is long, text-only, and easy to verify. Retrieval-heavy summaries, background analysis, and low-risk coding routes can use the same 1,040k context class without using Pro on every call.

**Q: How should you route between Flash and Pro?**

Run Flash first on repeatable routes. Escalate to Pro when Flash fails the eval rubric, loses citations, or produces a plan the downstream tool cannot execute cleanly.

**Q: Is DeepSeek-V4-Flash a small model?**

No. DeepSeek-V4-Flash is smaller than DeepSeek-V4-Pro, but it is still a 284B MoE model.

**Q: What should you test first with DeepSeek-V4-Flash?**

Run the same long-context prompt through DeepSeek-V4-Flash and DeepSeek-V4-Pro. If Flash keeps the evidence straight and the answer quality is close, keep the faster route.

- •**Release date:** June 2026
- •**Parameters:** 428B total, about 23B activated
- •**Context window:** 512k tokens on Fireworks
- •**License:** MiniMax Community; commercial deployments must display “Built with MiniMax M3.” One-time notice is required below $20 million in annual revenue, and prior written authorization is required above that threshold.
- •**Corporate sponsor:** MiniMax
- •**Model repo:**[__MiniMax-AI/MiniMax-M3__](https://github.com/MiniMax-AI/MiniMax-M3)

**🚀 Try MiniMax M3 on Fireworks →**

[MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3) is a native multimodal MoE model built for long-context, agentic, and multimodal workflows. It runs on Fireworks Serverless and On-Demand with image input and function calling.

MiniMax M3 is a multimodal candidate for workloads that require image or video input. It has a 512k context window, about 428B total parameters, and about 23B activated parameters. Those architecture figures do not predict serving cost or latency, so production testing should measure both on the intended route.

MiniMax M3 reaches 92.9% on GPQA, second only to Kimi K3 in the benchmark table. It also gives you image input on Fireworks, which makes it the first multimodal eval when visual context belongs in the request.

Use MiniMax M3 when image or video input and a 512k context window match the workload. It fits visual support workflows, research assistants, and media-understanding tasks that do not require a 1,040k context window.

If the workload needs 1,040k context, start with GLM 5.2, DeepSeek-V4-Pro, or DeepSeek-V4-Flash.

- •512k context window on Fireworks
- •Native multimodal support with image input
- •92.9% GPQA, second only to Kimi K3 here
- •428B total parameters, about 23B activated
- •Serverless and On-Demand availability
- •91.7 tokens/second median output

| Pros | Cons | 
|---|---|
| Strong multimodal capabilities | MiniMax Community license needs review | 
| Native image input | Shorter context than GLM 5.2 and both DeepSeek V4 models | 
| Strong GPQA score | Lower Coding Index than GLM 5.2, Kimi K2.7 Code, and DeepSeek-V4-Pro | 
| Native image and video support | Not the right default when 1,040k context is required | 

**Q: Why does MiniMax M3's active-parameter count matter?**

Active parameters describe how much of a mixture-of-experts model participates in processing each token. The count does not establish latency, throughput, or serving cost. Measure those outcomes on the route and workload you plan to use.

**Q: Where does MiniMax M3 fit best?**

It combines 512k context with image and video input. That combination fits support, product-assistant, and media-understanding workloads that need visual context.

**Q: Can MiniMax M3 handle video on Fireworks?**

Yes. MiniMax M3 is built for text, image, and video. Test the exact video input path before you build around it, then use the same eval set you use for screenshots, charts, product images, and visual documents.

**Q: What should you test with MiniMax M3 image and video input?**

Test OCR, chart reading, small UI text, multi-image prompts, and the exact video input path before you build around it.

- •**Release date:** June 2026
- •**Context window:** 262k tokens on Fireworks
- •**Weight access:** closed weights
- •**Training support** : available through Fireworks for supported customer workflows
- •**Corporate Sponsor:** Alibaba Cloud / Qwen

**🚀 Try Qwen3.7 Plus on Fireworks →**

[Qwen3.7 Plus](https://fireworks.ai/models/fireworks/qwen3p7-plus) is a closed-weight model. It appears here because Fireworks customers can access and run it through the same API and serving infrastructure as the open source models on this list, with training support available.

It runs on Fireworks Serverless with 262k context and image input, putting it in the same multimodal tier as [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code) and [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3).

Qwen3.7 Plus scores 39.0 on the [Intelligence Index](https://artificialanalysis.ai/models) and 55.9 on the [Coding Index](https://artificialanalysis.ai/models/capabilities/coding), with 90.0% on GPQA. It trails GLM 5.2, Kimi K2.7 Code, DeepSeek-V4-Pro, and MiniMax M3 on both indexes, but belongs in evals where Qwen-family behavior, multimodal support, and Fireworks access are already part of the product plan.

Use Qwen3.7 Plus when you want a Qwen-family multimodal model on Fireworks with Serverless access and closed weights are acceptable. It fits product assistants, visual support workflows, Qwen-standardized stacks, and agent traces where 262k context is enough.

For tool-heavy agents that require the strongest open-model quality, start with GLM 5.2, Kimi K2.7 Code, DeepSeek-V4-Pro, or MiniMax M3. For open-weight-only procurement, keep Qwen3.7 Plus out of the final shortlist. For Qwen-standardized stacks, keep it in the eval.

- •262k context window on Fireworks
- •Image input
- •90.0% GPQA
- •55.9 Coding Index
- •Serverless availability on Fireworks
- •Closed weights
- •Training support available through Fireworks
- •Qwen-family behavior for teams already building around Qwen

| Pros | Cons | 
|---|---|
| Qwen-family multimodal option on Fireworks | Lower Intelligence Index than GLM 5.2, MiniMax M3, DeepSeek-V4-Pro, Kimi K2.7 Code, and DeepSeek-V4-Flash | 
| Serverless availability | Closed weights; license and access terms need review before production standardization | 
| Strong GPQA score | Shorter context than GLM 5.2 and both DeepSeek V4 models | 

**Q: What does closed weights change for Qwen3.7 Plus?**

Closed weights add procurement and legal review. Fireworks customers can still evaluate and run Qwen3.7 Plus through Fireworks, then review model-specific terms before production standardization.

**Q: When is Qwen3.7 Plus worth testing despite lower composite scores?**

Test Qwen3.7 Plus when the team already has Qwen prompts, evals, or product behavior to preserve. A lower composite score can still win if the model matches the product's existing Qwen-family assumptions.

**Q: Is Qwen3.7 Plus multimodal on Fireworks?**

Yes. Qwen3.7 Plus accepts image input on Fireworks. Test image recognition, small screenshot text, and mixed text-image tool outputs before you move it to production.

**Q: What training support is available for Qwen3.7 Plus?**

Fireworks can support Qwen3.7 Plus training workflows for customers where the use case and model terms fit.

- •**Release date:** August 2025
- •**Parameters:** 116B total
- •**Context window:** 131k tokens on Fireworks
- •**License:** Apache 2.0
- •**Corporate sponsor:** OpenAI
- •**Model repo:**[__openai/gpt-oss__](https://github.com/openai/gpt-oss)

**🚀 Try __g__pt-oss-120b on Fireworks →**

[gpt-oss-120b](https://fireworks.ai/models/fireworks/gpt-oss-120b) is OpenAI's larger open-weight GPT-OSS model. It is built for production general-purpose reasoning use cases, with 116B total parameters.

The selection case is not top composite quality. gpt-oss-120b reaches 23.8 on Intelligence Index and 30.4 on Coding Index, which puts it well below the 2026 frontier open models here. Its use case is high generated-token rate, Harmony-format compatibility, and simple OpenAI-family adoption for teams already familiar with OpenAI conventions.

Use gpt-oss-120b when Apache 2.0 licensing is required and output speed matters more than benchmark rank. It fits summarization, classification, internal assistants, extraction routes, and high-throughput steps where quality requirements are bounded.

Do not use gpt-oss-120b as the first pick for hard coding or frontier reasoning. Start with GLM 5.2, Kimi K2.7 Code, DeepSeek-V4-Pro, or MiniMax M3 when the task needs stronger reasoning.

- •Apache-2.0 license
- •116B total parameters
- •131k context on Fireworks
- •271.4 tokens/second median output
- •Native Harmony response format
- •Serverless availability on Fireworks

| Pros | Cons | 
|---|---|
| Apache 2.0 license | Lowest composite quality among these nine models | 
| Fastest median output speed here | 131k context is shorter than every other model in this slate | 
| OpenAI-family model behavior | Harmony format must be handled correctly | 
| Good fit for high-throughput bounded tasks | Not the right first pick for hard coding or long-context reasoning | 

**Q: Why include gpt-oss-120b if its benchmark row is lower?**

Include gpt-oss-120b in your evals when Apache 2.0 licensing and throughput are hard constraints, and the workload is bounded (summarization, classification, extraction).

**Q: Does gpt-oss-120b use the normal chat format?**

No. The gpt-oss models are designed around [OpenAI's Harmony response format](https://developers.openai.com/cookbook/articles/openai-harmony). If your orchestration layer ignores that format, you should expect lower reliability.

**Q: Is gpt-oss-120b good for coding agents?**

Only for bounded steps. gpt-oss-120b can be useful for fast code summarization or classification, but it trails GLM 5.2, Kimi K2.7 Code, DeepSeek-V4-Pro, DeepSeek-V4-Flash, MiniMax M3, Qwen3.7 Plus, and Gemma 4 31B IT on Coding Index.

**Q: What should you test before routing production traffic to gpt-oss-120b?**

Test schema adherence, short-answer accuracy, refusal behavior, and Harmony-format handling. The model is a better fit for bounded routes than open-ended reasoning traces.

- •**Release date:** April 2026
- •**Parameters:** 32.2B dense
- •**Context window:** 262k tokens on Fireworks
- •**License:** Apache 2.0
- •**Corporate sponsor:** Google
- •**Model repo:**[google-deepmind/gemma](https://github.com/google-deepmind/gemma)

[Gemma 4 31B IT Available for On-Demand Deployment on Fireworks](https://fireworks.ai/models/fireworks/gemma-4-31b-it) [→](https://fireworks.ai/models/fireworks/gemma-4-31b-it)

[Gemma 4 31B IT](https://fireworks.ai/models/fireworks/gemma-4-31b-it) is a smaller multimodal instruction-tuned model from Google. It runs on Fireworks On-Demand, billed per GPU-second at $7–$12 per GPU-hour depending on GPU type. Total deployment cost depends on the type and number of GPUs allocated.

Most models here are MoE systems. Gemma 4 31B IT is the smaller dense option, which makes it easier to adapt and inspect but weaker on frontier reasoning. Use it when Apache 2.0 licensing, image input, and a smaller fine-tune target are more important than top-end benchmark rank.

Gemma 4 31B IT scores 43.4% on SciCode, but its Artificial Analysis Intelligence Index is near the bottom of this nine-model slate, ahead of only gpt-oss-120b. Test it when the deployment requirement favors a smaller dense model over a larger MoE option.

Pick Gemma 4 31B IT when the fine-tuning plan needs Apache 2.0 licensing, dense-model behavior, and image input. Internal tools and domain assistants are the natural fit.

- •Apache 2.0 license
- •Dense 32.2B architecture
- •Image input
- •262k context window on Fireworks
- •On-Demand deployment path
- •Smaller deployment target than trillion-parameter MoE models

| Pros | Cons | 
|---|---|
| Apache 2.0 license | Lower Intelligence Index than the top seven models here | 
| Dense architecture can simplify behavior analysis | Lower median output speed than larger Serverless models in the benchmark rows | 
| Image input support | Not the first pick for hard reasoning or coding | 

**Q: Why use Gemma 4 31B IT on On-Demand?**

Use Gemma 4 31B IT when the workload needs a smaller dense model, image input, and a controlled deployment path.

**Q: When does dense architecture help?**

Dense architecture can be easier to inspect, adapt, and reason about than a large MoE system. Gemma 4 31B IT fits teams that would rather tune a smaller model than prompt around a larger one.

**Q: What tradeoff does Gemma 4 31B IT make?**

Gemma 4 31B IT gives up top-end benchmark rank for a smaller dense architecture, Apache 2.0 licensing, and image input. Use it when adaptation and deployment control beat raw composite score.

**Q: Is Gemma 4 31B IT multimodal?**

Yes. Gemma 4 31B IT accepts image input, and the Gemma library supports multimodal workflows.

**Q: What should you test before fine-tuning Gemma 4 31B IT?**

Fine-tuning is worth the setup when the model repeatedly needs the same terminology, policy, or output shape across many tasks.

Choosing GLM 5.2 over MiniMax M3 or DeepSeek-V4-Flash answers only one question: which model should handle the prompt? Production adds another question. The serving route has to hold up under long prompts, traffic spikes, and latency targets.

Fireworks is built for serving open-source models at production scale. The platform handles the parts most teams do not want to own in every application stack. That includes custom kernels, disaggregated inference, speculative decoding, KV-cache management, prompt caching, quantization, dedicated deployments, and post-training.

The platform processes more than 40 trillion tokens per day. [Fireworks and Harvey ran GLM 5.1 with Claude Opus 4.7 as a callable advisor](https://fireworks.ai/blog/open-source-agents-frontier-advisors), reaching 18/100 all-pass on a 100-task slice of the Legal Agent Benchmark at $368 versus 14/100 for Opus end-to-end at $954, though Opus still led on mean score.

Benchmarks help you shortlist models, but production adds a harder test: can your serving stack keep time to first token, output speed, and cost stable under real traffic spikes?

| Option | How it works | Best for | 
|---|---|---|
| [Serverless](https://docs.fireworks.ai/serverless/overview) | Pay per token, no cold starts, OpenAI-compatible API access | Fast evals and variable traffic for GLM 5.2, Kimi K2.7 Code, DeepSeek-V4-Pro, DeepSeek-V4-Flash, MiniMax M3, Qwen3.7 Plus, and gpt-oss-120b | 
| [On-Demand](https://docs.fireworks.ai/guides/ondemand-deployments) | Private GPUs, autoscaling, and dedicated deployment control | Production routes with predictable traffic, stricter latency targets, or model-specific capacity planning; Gemma 4 31B IT uses this path | 
| [Enterprise Reserved](https://docs.fireworks.ai/deployments/reservations) | Reserved GPU capacity, SLAs, priority support, and bring-your-own-cloud options | High-volume products, regulated workloads, and teams that need isolation or procurement control | 
| [Post-training](https://docs.fireworks.ai/fine-tuning/finetuning-intro) | SFT, LoRA, RFT, RL pipelines, and eval support through FireOptimizer | Repeated behavior, domain vocabulary, code style, ranking policy, or tool-use patterns that should move out of prompts | 

Open models beat the Claude references on GPQA and output speed, while Claude leads several quality and coding measures. Choose the model that fits your workload.

[GLM 5.2](https://fireworks.ai/models/fireworks/glm-5p2) is the starting point for broad reasoning and coding. Use [Kimi K2.7 Code](https://fireworks.ai/models/fireworks/kimi-k2p7-code) when a coding agent needs image input. [MiniMax M3](https://fireworks.ai/models/fireworks/minimax-m3) handles broader image and video work. [DeepSeek-V4-Flash](https://fireworks.ai/models/fireworks/deepseek-v4-flash) pairs a 1,040k-token context window with faster output than DeepSeek-V4-Pro. All four run on Fireworks.

>> [Compare all models in the Fireworks model library](https://fireworks.ai/models). <<

**The information provided in this article is accurate at the time of publication. Model capabilities, benchmarks, and availability change frequently. Always verify current specifications on official model repositories.**
