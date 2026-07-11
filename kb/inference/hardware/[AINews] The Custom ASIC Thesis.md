---
title: '[AINews] The Custom ASIC Thesis'
topic: inference
subtopic: hardware
secondary_topics:
- infra-platform/gpu-clusters
summary: Summarizes the custom ASIC thesis for AI infrastructure and why specialized
  chips matter for inference economics.
source: latent-space
url: https://www.latent.space/p/ainews-the-custom-asic-thesis
author: Latent Space
published: '2026-02-21'
fetched: '2026-07-11T05:14:27Z'
classifier: codex
taxonomy_rev: 1
words: 837
content_sha256: a30486c24814ef29e1e81a271896abd376634934ec7e640f0d0bb06ff9aee933
---

# [AINews] The Custom ASIC Thesis

# [AINews] The Custom ASIC Thesis

### Taalas HC1 runs 16,960 tok/s/user Llama 3.1 8B with custom silicon. Actually fast LLMs are on their way...


AI News for 2/19/2026-2/20/2026. We checked 12 subreddits,[544 Twitters](https://twitter.com/i/lists/1585430245762441216)and 24 Discords (262channels, and12582messages) for you. Estimated reading time saved (at 200wpm):1242minutes.[AINews’ website](https://news.smol.ai/)lets you search all past issues. As a reminder,[AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can[opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack)of email frequencies!

Congrats to the [ggml + Huggingface team](https://news.ycombinator.com/item?id=47088037), note the [Opus 4.6 METR debate](https://x.com/METR_Evals/status/2024923422867030027), and read [Chris Lattner’s Claude C Compiler analysis](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software). But those aren’t the top stories.

Today, 2.5 year old [Taalas announced](https://taalas.com/the-path-to-ubiquitous-ai/) a **shockingly fast 16,960 tokens per second** per user production API service for the Llama 3.1 8B model (launched July 2024):

![](https://substackcdn.com/image/fetch/$s_!oVQ7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49185ac5-439f-4605-ba64-42d42591e30c_2050x1478.png)

While there are some other non-speed gains (less build cost and power draw), it is also offset by some other footnotes on quantization (which they note the HC2 will resolve with standardized low precision FP4).

**This is an impressive result…. that we have no idea how to productize yet.** And anytime there is a huge capability overhang opening up, AI Engineers should rush in to figure out the “capability market fit”.

As for the overall proposition of going custom ASIC, we’re still thinking about this week’s Latent Space with [Martin Casado and Sarah Wang](https://www.latent.space/p/a16z), where Martin reiterated his conviction in the math of doing custom accelerators (ASICs) **PER MODEL**, essentially “baking the LLM into silicon”, foreshadowing [the OpenAI Broadcom deal](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/):

**Martin: **It makes sense to actually do a custom ASIC if you can do it in time. The question now is timelines, but not money because rough math:

- *If it’s a billion dollar training run, then the inference for that model has to be over a billion, otherwise it won’t be solvent.*
- *So let’s assume if you could save 20%, (which you could save much more than 20% with an ASIC), that’s $200 million.*
- *You can tape out a chip for $200 million.*

*Right? So now you can literally like justify economically, not timeline wise. That’s a different issue. *

**swyx:** An ASIC per model, because that, that’s how much we leave on the table every single time we do generic Nvidia.

**Martin Casado:** Exactly. No, it, it is actually much more than that. You could probably get, you know, a factor of two, which would be 500 million. Typical MFU would be like 50.

We understand the tradeoffs that custom chips offer faster/cheaper inference in exchange for lower model quality (by being, in Taalas’ case, 1.5 years behind the frontier), but that gap is virtually certain to close as LLMs continue to standardize in architecture and, more to the point, OpenAI and others start doing **fully** integrated model-chip codesign as Martin predicts. It’s not even about the cost savings at this point - the potential of actual **frontier quality + >20,000 tok/s inference **is incomprehensible to AI Engineers of today and we should start those thought experiments and product surfaces today with an expectation that we’ll get there in under 2 years from today.

![](https://substackcdn.com/image/fetch/$s_!AQKx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F135eb2d4-a2b3-41db-8d80-3456a144fb84_3092x1430.png)

**AI Twitter Recap**

**Frontier model evals: Gemini 3.1 Pro, SWE-bench, MRCR, and “bipolar” real‑world performance**

- **Gemini 3.1 Pro shows strong retrieval + mixed agentic usability**: Context Arena’s MRCR update reports- **Gemini 3.1 Pro Preview**near-ties- **GPT‑5.2 (thinking:xhigh)**on easier retrieval (2‑needle @128k AUC- **99.6% vs 99.8%**) and notably stronger on harder multi‑needle retrieval (8‑needle @128k AUC- **87.8%**, beating GPT‑5.2 thinking tiers reported there) (- [DillonUzar](https://x.com/DillonUzar/status/2024655613293215855)). Separately,- **Artificial Analysis**highlights a likely underappreciated angle:- **token efficiency + price**; they claim their Intelligence Index suite cost- **$892**on Gemini 3.1 Pro Preview vs- **$2,304**(GPT‑5.2 xhigh) and- **$2,486**(Opus 4.6 max), with fewer tokens consumed than GPT‑5.2 in their runs (- [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2024677979390169536)).
- **But engineers report “bench strength, product weakness”**: multiple threads complain Gemini’s tooling/harnesses lag—e.g., model availability inconsistencies in the CLI and buggy agent behavior in “Antigravity,” plus a worrying “UI lies / model lies” confusion where the app claims Gemini but reports Claude underneath (- [Yuchenj_UW](https://x.com/Yuchenj_UW/status/2024708583829753909),- [Yuchenj_UW](https://x.com/Yuchenj_UW/status/2024721228842565851)). Even enthusiastic takes (“faster horse”) are juxtaposed with frustration about actually using it day‑to‑day (- [theo](https://x.com/theo/status/2024808734053347608)).
- **SWE-bench Verified evaluation methodology matters again**: MiniMax points to an “independent look” at SWE-bench Verified results for- **MiniMax M2.5**under the same setup, implying earlier comparisons across labs may have been apples-to-oranges (- [MiniMax_AI](https://x.com/MiniMax_AI/status/2024646767325958285)). Epoch AI explicitly acknowledges this failure mode: they updated SWE‑bench Verified methodology because their prior runs were systematically different from others, and now see results closer to developer‑reported scores (- [EpochAIResearch](https://x.com/EpochAIResearch/status/2024924403142910137)).
- **Benchmark oddities are prompting “what are we measuring?” debates**: one example—frontier models “smash ARC-AGI” yet struggle with Connect 4, suggesting ARC‑style puzzles may capture only a narrow slice of spatial/game reasoning despite being designed to resist overfitting (- [paul_cal](https://x.com/paul_cal/status/2024748708223402120)). Another thread expects only a few models to make progress on a “simple harness” for ARC‑AGI‑3 and flags cost as the constraint (- [scaling01](https://x.com/scaling01/status/2024650634746610041),- [scaling01](https://x.com/scaling01/status/2024661145286557872)).

## Keep reading with a 7-day free trial

Subscribe to Latent.Space to keep reading this post and get 7 days of free access to the full post archives.
