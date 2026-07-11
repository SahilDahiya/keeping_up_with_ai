---
title: 'DeepSeek V3.2''s path to GPT-5-level performance: sparse attention, RL at
  scale, and context reuse'
topic: models
subtopic: reasoning
secondary_topics:
- models/fine-tuning
summary: Explains DeepSeek V3.2 architecture and training choices including sparse
  attention, RL, and context reuse.
source: baseten
url: https://www.baseten.co/blog/deepseek-v3-2/
author: Charles O'Neill; Alex Ker
published: '2025-12-05'
fetched: '2026-07-11T04:06:46Z'
classifier: codex
taxonomy_rev: 1
words: 1335
content_sha256: a2334381f2ff9d97593771e51b71295b4ebc22ca65d469a098fef06bad58a545
triage: keep
skip_reason: null
---

# DeepSeek V3.2's path to GPT-5-level performance: sparse attention, RL at scale, and context reuse

![DeepSeek V3.2 & the path to GPT-5 level performance](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1764967757-deepseek-v3-2.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

The launch of DeepSeek-V3.2 showed that by reducing long-context compute cost via architecture improvements and intentionally scaling RL, you can achieve GPT-5 level reasoning and agentic performance.

Ilya Sutskever shared that the end of the pretraining is here as foundation labs have burned through all of the tokens available on the internet.

Rather than relying on scaling laws, the launch of DeepSeek-V3.2 showed that by reducing long-context compute cost via architecture improvements and intentionally scaling RL, you can achieve GPT-5 level reasoning and agentic performance. And all this is achievable with a smaller, older backbone that is cheaper and faster to run during inference time.

In this post, we will cover the top 3 direction‑setting contributions of the DeepSeek-V3.2 paper that we think will evolve into the new standard training practices that are worthwhile for ML engineers to understand. These double as tested knobs to turn if you would like to improve base models for a specific use case.

## (1) DSA + MLA: reducing costs

Architecturally, DeepSeek‑V3.2 is almost the same model as V3.1‑Terminus. The primary innovation is DeepSeek Sparse Attention (DSA) layered on top of MLA, multi‑head latent attention, a dense attention variant that projects KV vectors into lower dimensional space to reduce memory usage.

DSA is composed of two components. First, a tiny lightning indexer scores all past tokens for relevance to the current query token. Then a token selector picks the top‑k previous tokens (2,048 out of a 128k context, a hyperparameter DeepSeek team selected) for the MLA to run on. Note that the indexer and selector are both learned. In combination, they create an attention mask that filters out less relevant tokens.

One of the biggest bottlenecks for running LLMs is that multihead attention is a quadratic, O(N^2), operation. However, since the lightning indexer is in FP8 with a handful of heads, its nominal quadratic cost is dwarfed by the savings from not doing full MLA on the entire context. End‑to‑end cost per token is almost flat out to 128k during prefilling, and only grows linearly in k during decoding, on the order of O(N*k) where k<<N.

![Equation for lightning indexer for DeepSeek V3.2](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1764966344-image1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Equation for lightning indexer for DeepSeek V3.2

Equation for lightning indexer for DeepSeek V3.2The real implication is DSA is there so we can afford an absurd number of reasoning tokens. If we look at the Speciale variant, on reasoning benchmarks (AIME, HMMT, IMOAnswerBench, LiveCodeBench), Speciale often matches or beats Gemini‑3.0‑Pro. But there is no free lunch; Speciale consumes ~1.5–2x more output tokens than Gemini and GPT‑5 for the same problems. For example, on Codeforces, it reaches 2701 with ~77k output tokens per solution on average, vs 22–29k for GPT‑5 and Gemini‑3.0‑Pro.

![Lightning Indexer and Top-k Selector](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1764967848-image4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Lightning Indexer and Top-k Selector

Lightning Indexer and Top-k SelectorDSA is effectively trading FLOPs spent on parameters for FLOPs spent on tokens during inference time. That’s a different knob than we’ve had historically. The lesson is if you can’t yet afford a bigger or intensively pretrained base model, lean into test‑time compute and make it cheap with better attention. This framing matters for RL vs SFT: SFT mainly improves what you can do at 1x test‑time compute, whereas RL + DSA lets you buy capability by increasing test‑time compute and still stay within a linear cost envelope.

![Inference Cost Decrease from DeepSeek-V3-1-Terminus to DeepSeek-V3.2](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1764967871-image2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Inference Cost Decrease from DeepSeek-V3-1-Terminus to DeepSeek-V3.2

Inference Cost Decrease from DeepSeek-V3-1-Terminus to DeepSeek-V3.2## (2) Scaling RL: increasing performance reliably

DeepSeek explicitly stated their RL budget is >10% of pre‑training compute, which is disproportionately large compared to historical spend for RL. Interestingly, Grok recently admitted to operating in this same regime, and other labs likely do as well. It's in the same ballpark as what Meta’s ScaleRL paper calls out as the high‑return regime: once RL is a double‑digit fraction of pre‑training FLOPs, you start to see qualitatively new behaviour rather than marginal polish: [https://arxiv.org/html/2510.13786v1](https://arxiv.org/html/2510.13786v1?utm_source=chatgpt.com).

DeepSeek uses GRPO but implements fixes discussed in recent theory papers. They selected some subset of the zoo of GxPO-variants to induce stability in training: unbiased KL estimate with corrected K3 estimator has been discussed for a while, and off-policy sequence masking to reduce learning from off-policy rollouts. Keep Routing and Keep Sampling Mask are also used to increase training stability for the model by aligning differences between training and inference.

Put together, this is a clean instantiation of what the newer RL literature is converging on. Scaling RL is now less about inventing a new objective and more about making the old objective actually match what the infra (training vs inference) is doing. This is a strong data point for the broader RL vs SFT narrative: once you fix the mismatch and pay the FLOPs, RL reliably buys you big jumps in reasoning that SFT alone cannot do.

On the agent side, DeepSeek’s main contribution is how they package environments for RL. They synthesized 1,827 general agent environments and 4,417 tasks, each exposing a toolset and an automatic verifier; plus real‑world environments for code repair (GitHub issue/PR pairs) and search (commercial web APIs), and a Jupyter‑based code‑interpreter setup. Every environment is essentially a tuple `<env state, tools, task, verifier>`. Once you have that, RL is "just" GRPO with verifiable rewards.

This may suggest a new type of moat for companies looking to differentiate the models they are serving. Compared to pre‑training data made up of webtext that anyone can scrape, agentic RL data is akin to curated micro‑simulators with tailored tools and verifiers, which is much harder to replicate casually. Proprietary usage data from apps or quality synthetic data generators may become an increasingly valuable asset.

## (3) Revised thinking for tool use: smarter context management

DeepSeek V3.2 also quietly patches one of the big pain points of thinking models in agents: how you manage the context with frequent tool calls.

In the original DeepSeek-R1 recipe, CoTs (Chain of Thought) are discarded after each message thus the model must re‑reason from scratch. For complex tool flows (e.g. multi‑hop search or multi‑round code debugging), this strategy forces the model to burn tokens rederiving the same partial plan every turn. The result is significant token inefficiencies that incur unnecessary costs and increase latency.

In this model, accumulated reasoning traces are only dropped when a new user message appears. Tool outputs and subsequent tool calls do not cause previous thoughts to be flushed; the reasoning state persists across the multi‑step trajectory. When you do eventually drop reasoning, the tool‑calls history and their results remain in the context.

![Thinking retention in DeepSeek V3.2 reasoning chain](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1764967991-image3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Thinking retention in DeepSeek V3.2 reasoning chain

Thinking retention in DeepSeek V3.2 reasoning chainFor evaluations, DeepSeek shows that explicit context‑management policies are effectively another axis to squeeze the juice out of test‑time compute. On BrowseComp, simple strategies like "summarise when you hit 80% of context" or "discard all tool history and restart" can move the pass rate from ~53% to ~68%.

So in addition to scaling RL and increasing thinking tokens with reduced costs, it turns out aggressively recycling context during run-time is a clever third lever for models to execute without exceeding the context window in completing complex tasks.

## The intelligence vs. efficiency tradeoff

In summary, open source is catching up to gold standards in closed source, but they require approximately twice as many tokens. DeepSeek‑V3.2‑Thinking is roughly GPT‑5‑High‑tier on many reasoning and coding benchmarks, but slightly behind Gemini‑3.0‑Pro overall. The high‑compute Speciale variant often matches or beats Gemini‑3.0‑Pro and attains gold‑medal performance on IMO, CMO, IOI and ICPC WF without competition‑specific tuning.

While DeepSeek-V3.2 is less efficient intelligence-wise per token, it is more efficient on a per-dollar basis when measured against any of its closed source counterparts by many multiples today (e.g. $10 output for GPT5 vs. 0.45 output for DeepSeek-V3.2 on Baseten).

For reasoning tasks where max quality is required, DeepSeek-V3.2 would be an excellent, cost-effective choice. Try it in Model APIs on Baseten today: [https://www.baseten.co/library/deepseek-v3-2/](https://www.baseten.co/library/deepseek-v3-2/).
