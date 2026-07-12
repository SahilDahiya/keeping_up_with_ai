---
title: What do LLMs think when you don't tell them what to think about?
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/reasoning
summary: Investigates what LLMs do under underspecified prompting and how that affects
  evaluation.
source: together
url: https://www.together.ai/blog/what-llms-think
author: Yongchan Kwon; James Zou
published: '2026-02-06'
fetched: '2026-07-11T04:20:19Z'
classifier: codex
taxonomy_rev: 1
words: 1131
content_sha256: 8f0820c31bfb56d2f8e35b9dd12081ff912acf068a8fe034f87de09a23de9a1b
triage: keep
skip_reason: null
---

# What do LLMs think when you don't tell them what to think about?

Summary

Our interactions with large language models (LLMs) are dominated by task- or topic-specific questions, such as “*solve this coding problem*” or “*what is democracy?*” This framing strongly shapes how LLMs generate responses, constraining the range of behaviors and knowledge that can be observed. We study the behavior of LLMs using minimal, topic-neutral prompts. *Despite the absence of explicit task or topic specification, LLMs generate diverse content; however, each model family exhibits distinct topical preferences*. GPT-OSS favors programming and math, Llama leans literary, DeepSeek often produces religious content, and Qwen tends toward multiple-choice questions. We further observe that our generation settings can degenerate into repetitive or meaningless outputs, revealing model-specific quirks, such as Llama generating personal social media URLs.

Paper: [https://arxiv.org/abs/2602.01689](https://arxiv.org/abs/2602.01689)

Project Page: [https://tinyurl.com/mzr5cckz](https://tinyurl.com/mzr5cckz)

**What do we study?**

Most LLM behavior analyses are constrained: the prompt heavily shapes what the model can say [1,2]. This is useful—but it is also deeply limiting.

**Prompts act like filters.** A math question forces mathematical reasoning; a chat template forces the model into an assistant persona. Large parts of the model’s generative space are never exercised at all. What we observe is not the model’s natural behavior, but the behavior induced by our instructions. So we ask a more basic question:

*What does a language model generate when you do not tell it what to generate?*

To answer this, we study near-unconstrained generation. We use topic-neutral, open-ended seed prompts such as “Actually,” “Let’s think step by step,” or even just punctuation like “.” We remove chat templates entirely—no system prompt, no roles—and use standard decoding. This setup approximates the model’s top-of-mind behavior: a glimpse of its learned generative prior before alignment and prompting take over.

**Why this matters**

If you care about model auditing, behavioral monitoring, LLM fingerprinting, or safety and privacy risks, conditional benchmarks alone are not enough. We need to look into raw model generations and see how LLMs behave in diverse inputs and prompting conditions.

As an underexplored but scientifically intriguing setting, **near-unconstrained generation allows us to observe what models prefer to talk about, what kinds of content they over-represent, and how they fail when fixed chat templates and special tags are removed. **Crucially, these signals turn out to be systematic rather than anecdotal.

**Results: What LLMs think when you don't tell them what to think about?**

**Result 1: Model families have distinct knowledge priors**

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b27e85d90537426e209_698583095784bd8a7277a378_1957131c.png)

[https://tinyurl.com/mzr5cckz](https://tinyurl.com/mzr5cckz).

As shown in Figure 1(a), *despite the lack of explicit instructions or topics in prompts, LLMs generate a broad range of topics.* LLMs generate various categories, including the liberal arts (e.g., literature, philosophy, and education), science and engineering (e.g., physics, mathematics, and programming), as well as areas such as law, finance, music, sports, cooking, agriculture, archaeology, military, and fashion.

More surprisingly, shown in Figure 1(b), **different model families gravitate toward different parts of the semantic space—even when given the same minimal prompts. **GPT-OSS overwhelmingly defaults to programming (27.1%) and mathematics (24.6%). More than half of a model family’s output concentrates in these two domains! Llama produces far more literary and narrative text (9.1%), with less emphasis on technical domains (See Figures 2). DeepSeek often generates religious content at a substantially higher rate than other families. Qwen frequently outputs multiple-choice exam questions, complete with answer options. 

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b26e85d90537426e1f3_698583095784bd8a7277a375_fe108f93.png)

What is striking here is consistency. These distributions persist across different prompts, embedding models, and semantic labelers. The behavior looks less like noise and more like a population-level fingerprint. Figure 3 shows representative examples.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b27e85d90537426e20c_698583095784bd8a7277a37e_8eccc954.png)

**Result 2: Depth is part of the prior too**

The differences are not only about what and how often models talk about, but also how deeply they go. We assess the complexity of programming and mathematical text in Figure 4.

We find that **GPT-OSS frequently produces advanced or expert-level content (68.2%)**, such as depth-first search, breadth-first search, or dynamic programming (see Figure 3). Llama and Qwen skew much more toward basic or intermediate material. These depth differences remain even when controlling for labeling models and evaluation setups.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b26e85d90537426e1f8_698583095784bd8a7277a382_5f7e0ade.png)

**Result 3: Degenerate text is a signal, not just noise**

Lastly, following previous work [3,4], we also observe that models sometimes fall into repetitive or degenerate patterns, especially when constraints are removed. This behavior is usually discarded as gibberish. **We treated it as data.**

By analyzing where degeneration starts, how often it occurs, and what it looks like, we uncovered stark model-specific differences. GPT-OSS tends to repeat short formatting artifacts such as code block delimiters (```\n\n```\n\n). Qwen produces long conversational phrases, emojis, and Chinese text. Llama sometimes emits URLs pointing to real personal Facebook and Instagram accounts (Figure 6). In-depth analysis is available in the paper.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b27e85d90537426e206_698583095784bd8a7277a385_3057c1de.png)

![Bar charts comparing GPT-OSS, DeepSeek, Llama, Qwen on degeneration ratio, start index, and repeated phrase length.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b27e85d90537426e1ff_698583095784bd8a7277a37b_fb7c364e.png)

**Degenerate text turns out to be one of the clearest windows into safety and privacy risks, precisely because it reflects uncontrolled generation**. These behaviors rarely appear in standard benchmarks, yet they are highly revealing.

**Why this surprised us and takeaway**

Given that all evaluated models are broadly competitive in mathematics, programming, and general-purpose tasks, we initially expected their near-unconstrained generations to exhibit similar semantic distributions across model families. Instead, we observe stark and systematic biases that persist across families. We did not anticipate GPT-OSS to generate math and programming more than 50%, nor did we expect Qwen to generate such a large fraction of multiple-choice exam questions.

These behaviors appear quite robust across various experimental settings. No matter how we varied prompts, embeddings, or labelers, the same patterns kept reappearing. Perhaps most surprisingly, degeneration was not a random failure mode. Rather, degenerate generations displayed consistent structure and style, and in some cases included potentially personally identifiable information. These outputs frequently resembled fragments of the training distribution, although the mechanisms underlying their emergence remain unclear.

Near-unconstrained generation we consider in this work does not replace standard benchmark evaluations. But it exposes something benchmarks systematically miss: what language models are inclined to say when nobody tells them what to say. If we want to understand LLMs as systems rather than just test-takers, we need to study their defaults—not only their best answers or prompt-induced outputs. See our paper for more detailed explanations and experiments.

**References**

[1] Alejandro Salinas, Amit Haim, and Julian Nyarko. What’s in a name? auditing large language models for race and gender bias. arXiv preprint arXiv:2402.14875, 2024.

[2] Tiancheng Hu, Yara Kyrychenko, Steve Rathje, Nigel Collier, Sander van der Linden, and Jon Roozenbeek. Generative language models exhibit social identity biases. Nature Computational Science, 5(1):65–75, 2025.

[3] Sean Welleck, Ilia Kulikov, Stephen Roller, Emily Dinan, Kyunghyun Cho, and Jason Weston. Neural text generation with unlikelihood training. arXiv preprint arXiv:1908.04319, 2019.

[4] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration. arXiv preprint arXiv:1904.09751, 2019.
