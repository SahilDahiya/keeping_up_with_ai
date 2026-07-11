---
title: ICLR 2024 — Best Papers & Talks (Benchmarks, Reasoning & Agents) — ft. Graham
  Neubig, Aman Sanger, Moritz Hardt)
topic: models
subtopic: benchmarks
secondary_topics:
- agents/planning
summary: ICLR 2024 recap focused on benchmarks, reasoning, and agents, with pointers
  to durable research themes.
source: latent-space
url: https://www.latent.space/p/iclr-2024-benchmarks-agents
author: Latent Space
published: '2024-06-10'
fetched: '2026-07-11T05:20:44Z'
classifier: codex
taxonomy_rev: 1
words: 2130
content_sha256: 72c8974c0439625896c31e37955ae1c66ebb37720c70eaa523104ca6b636943f
---

# ICLR 2024 — Best Papers & Talks (Benchmarks, Reasoning & Agents) — ft. Graham Neubig, Aman Sanger, Moritz Hardt)

*Our second wave of speakers for *[AI Engineer World’s Fair](https://www.ai.engineer/worldsfair)* were *[announced](https://x.com/swyx/status/1797654825968291862)*! The conference sold out of Platinum/Gold/Silver sponsors and Early Bird tickets! See our *[Microsoft episode](https://www.latent.space/p/worlds-fair-2024#%C2%A7show-notes)* for more info and *[buy now](https://ti.to/software-3/ai-engineer-worlds-fair)* with code *`LATENTSPACE`*.*

This episode is straightforwardly a part 2 to our [ICLR 2024 Part 1 episode](https://www.latent.space/p/iclr-2024-recap), so without further ado, we’ll just get right on with it!

## Timestamps

**[00:03:43] Section A: Code Edits and Sandboxes, OpenDevin, and Academia vs Industry — ft. Graham Neubig and Aman Sanger**

- **[00:07:44] WebArena**
- **[00:18:45] Sotopia**
- **[00:24:00] Performance Improving Code Edits**
- **[00:29:39] OpenDevin**
- **[00:47:40] Industry and Academia**

**[01:05:29] Section B: Benchmarks**

- **[01:05:52] SWEBench**
- **[01:17:05] SWEBench/SWEAgent Interview**
- **[01:27:40] Dataset Contamination Detection**
- **[01:39:20] GAIA Benchmark**
- **[01:49:18] Moritz Hart - Science of Benchmarks**

**[02:36:32] Section C: Reasoning and Post-Training**

- **[02:37:41] Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**
- **[02:51:00] Let’s Verify Step By Step**
- **[02:57:04] Noam Brown**
- **[03:07:43] Lilian Weng - Towards Safe AGI**
- **[03:36:56] A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis**
- **[03:48:43] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework**

**[04:00:51] Bonus: Notable Related Papers on LLM Capabilities**

## Section A: Code Edits and Sandboxes, OpenDevin, and Academia vs Industry — ft. Graham Neubig and Aman Sanger

- **Guests**- Aman Sanger - - [Previous guest](https://www.latent.space/p/cursor)and- [NeurIPS friend of the pod](https://www.latent.space/p/neurips-2023-startups)!

- [Sotopia](https://openreview.net/forum?id=mM7VurbA4r)(spotlight paper,- [website](https://www.sotopia.world/))
- the role of code in reasoning
- Industry vs academia
- other directions

### Section A timestamps

- [00:00:00] Introduction to Guests and the Impromptu Nature of the Podcast
- [00:00:45] Graham's Experience in Japan and Transition into Teaching NLP
- [00:01:25] Discussion on What Constitutes a Good Experience for Students in NLP Courses
- [00:02:22] The Relevance and Teaching of Older NLP Techniques Like Ngram Language Models
- [00:03:38] Speculative Decoding and the Comeback of Ngram Models
- [00:04:16] Introduction to WebArena and Zotopia Projects
- [00:05:19] Deep Dive into the WebArena Project and Benchmarking
- [00:08:17] Performance Improvements in WebArena Using GPT-4
- [00:09:39] Human Performance on WebArena Tasks and Challenges in Evaluation
- [00:11:04] Follow-up Work from WebArena and Focus on Web Browsing as a Benchmark
- [00:12:11] Direct Interaction vs. Using APIs in Web-Based Tasks
- [00:13:29] Challenges in Base Models for WebArena and the Potential of Visual Models
- [00:15:33] Introduction to Zootopia and Exploring Social Interactions with Language Models
- [00:16:29] Different Types of Social Situations Modeled in Zootopia
- [00:17:34] Evaluation of Language Models in Social Simulations
- [00:20:41] Introduction to Performance-Improving Code Edits Project
- [00:26:28] Discussion on DevIn and the Future of Coding Agents
- [00:32:01] Planning in Coding Agents and the Development of OpenDevon
- [00:38:34] The Changing Role of Academia in the Context of Large Language Models
- [00:44:44] The Changing Nature of Industry and Academia Collaboration
- [00:54:07] Update on NLP Course Syllabus and Teaching about Large Language Models
- [01:00:40] Call to Action: Contributions to OpenDevon and Open Source AI Projects
- [01:01:56] Hiring at Cursor for Roles in Code Generation and Assistive Coding
- [01:02:12] Promotion of the AI Engineer Conference

## Section B: Benchmarks

- **Carlos Jimenez & John Yang (Princeton) et al:**SWE-bench: Can Language Models Resolve Real-world Github Issues? (- [ICLR Oral](https://iclr.cc/virtual/2024/oral/19757),- [Paper](https://arxiv.org/abs/2310.06770),- [website](https://swe-bench.github.io/))- “We introduce SWE-bench, an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories. - Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks. - Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model SWE-Llama can resolve only the simplest issues. - **The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues**. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous.”![](https://substackcdn.com/image/fetch/$s_!qlmU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49eb2ad7-3a0e-4b05-9f8c-cc9bfb378bb1_2156x1506.png) ![](https://substackcdn.com/image/fetch/$s_!gdBq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72146bae-e457-40fd-ae7d-8ec627cdf000_2090x1314.png)

- **Yonatan Oren et al (Stanford)**: Proving Test Set Contamination in Black-Box Language Models (- [ICLR Oral](https://iclr.cc/virtual/2024/session/15093),- [paper](https://arxiv.org/abs/2310.17623),- [aman tweet on swebench contamination](https://x.com/amanrsanger/status/1779620682340704386))- “We show that - **it is possible to provide provable guarantees of test set contamination**in language models without access to pretraining data or model weights. Our approach leverages the fact that when there is no data contamination, all orderings of an exchangeable benchmark should be equally likely. In contrast,- **the tendency for language models to memorize example order means that a contaminated language model will find certain canonical orderings to be much more likely than others**. Our test flags potential contamination whenever the likelihood of a canonically ordered benchmark dataset is significantly higher than the likelihood after shuffling the examples.
- We demonstrate that - **our procedure is sensitive enough to reliably prove test set contamination in challenging situations**, including models as small as 1.4 billion parameters, on small test sets of only 1000 examples, and datasets that appear only a few times in the pretraining corpus.”
- [Outstanding Paper mention](https://blog.iclr.cc/2024/05/06/iclr-2024-outstanding-paper-awards/): “A simple yet elegant method to test whether a supervised-learning dataset has been included in LLM training.”![](https://substackcdn.com/image/fetch/$s_!rEwV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d9f3d4-393e-4f0f-b91a-ec0a4812e9c2_1830x954.png) ![](https://substackcdn.com/image/fetch/$s_!SBpV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92e7cbda-4110-4335-b7b4-b3d57c55bba4_1754x934.png)

- [Thomas Scialom](https://x.com/thomasscialom?lang=en)(Meta AI-FAIR w/- [Yann LeCun](https://x.com/ylecun/status/1788850516660789732?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics))- [paper](https://arxiv.org/abs/2311.12983))- “We introduce GAIA, a benchmark for General AI Assistants that, if solved, would represent a milestone in AI research. GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency.
- GAIA questions are conceptually simple for humans yet challenging for most advanced AIs: - **we show that human respondents obtain 92% vs. 15% for GPT-4 equipped with plugins**.
- GAIA's philosophy departs from the current trend in AI benchmarks suggesting to target tasks that are ever more difficult for humans. We posit that the advent of Artificial General Intelligence (AGI) hinges on a system's capability to - **exhibit similar robustness as the average human does**on such questions. Using GAIA's methodology, we devise 466 questions and their answer.
![](https://substackcdn.com/image/fetch/$s_!bfNl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86c50a84-e2a6-4b42-8e00-9c64a93bf038_2114x1462.png) ![](https://substackcdn.com/image/fetch/$s_!jxkX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F385e9af1-fb68-421e-aa2b-43881bdc700f_1382x902.png)

- [Mortiz Hardt](https://mrtz.org/)(Max Planck Institute)- [ICLR stream](https://iclr.cc/virtual/2024/invited-talk/21799))- “ - **Benchmarks are the keystone that hold the machine learning community together.**Growing as a research paradigm since the 1980s, there’s much we’ve done with them, but little we know about them. In this talk, I will trace the rudiments of an emerging science of benchmarks through selected empirical and theoretical observations. Specifically, we’ll discuss the role of- **annotator errors, external validity of model rankings, and the promise of multi-task benchmarks**. The results in each case challenge conventional wisdom and underscore the benefits of developing a science of benchmarks.”![](https://substackcdn.com/image/fetch/$s_!Oe9H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F144f1b41-802e-491f-8076-bd382f26254c_1266x714.png) ![](https://substackcdn.com/image/fetch/$s_!xBXV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bc7c17f-adfd-4208-89d2-d32ec8eb4464_1232x694.png) ![](https://substackcdn.com/image/fetch/$s_!bo5I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4714e76-1095-4eac-8b66-b990e3be50a2_1226x692.png) ![](https://substackcdn.com/image/fetch/$s_!xqlU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc315b283-97b0-4e90-89c2-e067d5c2e4ce_1220x694.png) ![](https://substackcdn.com/image/fetch/$s_!Cume!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9034af1-eeac-45fb-aa9b-8b39c37992a5_1226x690.png)


## Section C: Reasoning and Post-Training

- **Akari Asai (UW) et al:**- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://iclr.cc/virtual/2024/oral/19736)(- [ICLR oral](https://iclr.cc/virtual/2024/session/15076),- [website](https://selfrag.github.io/))- (Bad RAG implementations) indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation.
- We introduce a new framework called - **Self-Reflective Retrieval-Augmented Generation (Self-RAG)**that enhances an LM's quality and factuality through retrieval and self-reflection.
- Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its generations using special tokens, called - **reflection**- **tokens**. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements.
- Self-RAG (7B and 13B parameters) outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning, and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models. ![](https://substackcdn.com/image/fetch/$s_!Ybrn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee1ca57e-a4dc-405f-b7bc-1f21a5907b19_2940x1646.png) ![](https://substackcdn.com/image/fetch/$s_!7mSe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F170947ab-2851-4aba-b938-d926a0ccaf5b_1844x1222.png)


- **Hunter Lightman (OpenAI):**Let’s Verify Step By Step (- [paper](https://arxiv.org/abs/2305.20050))- “Even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to - **outcome supervision**, which provides feedback for a final result, or- **process supervision**, which provides feedback for each intermediate reasoning step.
- We conduct our own investigation, finding that - **process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset.**Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision.
- To support related research, - **we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels**used to train our best reward model.
![](https://substackcdn.com/image/fetch/$s_!AJC-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49344bbd-5e04-49c4-910d-5a71d34e0d0e_2030x1230.png) ![](https://substackcdn.com/image/fetch/$s_!zuQT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1afd974f-669f-402c-9a7d-1e9497ae2960_1682x1270.png) ![](https://substackcdn.com/image/fetch/$s_!1vqK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff65d1ad6-e269-4526-844d-dc2ffbcb7038_1392x842.png)
- [Noam Brown](https://x.com/polynoamial/status/1777809000345505801?s=46&t=90xQ8sGy63D2OtiaoGJuww)- workshop on- [Generative Models for Decision Making](https://iclr.cc/virtual/2024/22266)- [Solving Quantitative Reasoning Problems with Language Models](https://arxiv.org/abs/2206.14858)(Minerva paper)![](https://substackcdn.com/image/fetch/$s_!B74h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b70f646-fbcf-47aa-8a99-1be49450eb59_1806x1184.png)
- Describes some charts taken directly from the Let’s Verify Step By Step paper listed/screenshotted above ![](https://substackcdn.com/image/fetch/$s_!FNWl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f053a8c-3b71-4b1d-8bcf-71c2a526f73e_994x800.png) ![](https://substackcdn.com/image/fetch/$s_!_u7q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F985260a8-9447-4a43-b6e5-0451d7db8b8a_1912x1394.png) - .


- [Lilian Weng](https://x.com/lilianweng/)(OpenAI)- [ICLR talk](https://iclr.cc/virtual/2024/22336))- OpenAI Instruction Hierarchy: - [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)
 ![](https://substackcdn.com/image/fetch/$s_!0CAl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82aba1dd-ba7c-407c-8ac3-432aa7b4e00d_1254x706.png) ![](https://substackcdn.com/image/fetch/$s_!A31L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72b7aee6-230b-450c-81bb-3aa72057ac8c_1260x690.png) ![](https://substackcdn.com/image/fetch/$s_!sKCl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c885731-5c14-40ff-8c59-d449f2ae7ff3_1258x700.png) ![](https://substackcdn.com/image/fetch/$s_!z1JP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68e49604-a85e-408c-8401-6ac9dc9de087_1164x678.png) ![](https://substackcdn.com/image/fetch/$s_!ki8Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F349f1f4c-9cd9-47d9-b22e-cf56a265e5eb_1246x706.png) ![](https://substackcdn.com/image/fetch/$s_!dLGY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f69acd8-ed8a-4240-b8c3-d6a87b596687_1270x708.png) ![](https://substackcdn.com/image/fetch/$s_!Vzp4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c6c620e-236a-4ad4-bd06-06cd9a7dc178_1248x694.png) ![](https://substackcdn.com/image/fetch/$s_!D9xH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F221612c1-6bf9-4b1a-af49-7d46d1d62652_1254x704.png)

## Section D: Agent Systems

- **Izzeddin Gur (Google DeepMind)**: A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis (- [ICLR oral](https://iclr.cc/virtual/2024/session/15073),- [paper](https://arxiv.org/abs/2307.12856))- [Agent] performance on real-world websites has still suffered from (1) open domainness, (2) limited context length, and (3) lack of inductive bias on HTML.
- We introduce - **WebAgent, an LLM-driven agent that learns from self-experience to complete tasks on real websites following natural language instructions.**
- WebAgent plans ahead by decomposing instructions into - **canonical sub-instructions, summarizes long HTML documents**into task-relevant snippets, and- **acts on websites via Python programs**generated from those.
- We design WebAgent with - **Flan-U-PaLM, for grounded code generation, and HTML-T5, new pre-trained LLMs for long HTML documents**using local and global attention mechanisms and a mixture of long-span denoising objectives, for planning and summarization.
- We empirically demonstrate that our modular recipe improves the success on real websites by over 50%, and that HTML-T5 is the best model to solve various HTML understanding tasks; achieving 18.7% higher success rate than the prior method on MiniWoB web automation benchmark, and SoTA performance on Mind2Web, an offline task planning evaluation.

- **Sirui Hong (DeepWisdom)**: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework (- [ICLR Oral](https://iclr.cc/virtual/2024/session/15076),- [Paper](https://arxiv.org/abs/2308.00352))- We introduce MetaGPT, an innovative meta-programming framework incorporating efficient human workflows into LLM-based multi-agent collaborations. - **MetaGPT encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows, thus allowing agents with human-like domain expertise to verify intermediate results and reduce errors.**MetaGPT utilizes an assembly line paradigm to assign diverse roles to various agents, efficiently breaking down complex tasks into subtasks involving many agents working together.![](https://substackcdn.com/image/fetch/$s_!LICm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffed5c87c-2851-4c59-9c0b-c26c922f6cd2_1972x1418.png)


## Bonus: Notable Related Papers on LLM Capabilities

This includes a bunch of papers we wanted to feature above but could not.

- **Lukas Berglund (Vanderbilt) et al**: The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A” (- [ICLR poster](https://iclr.cc/virtual/2024/poster/19033),- [paper](https://arxiv.org/abs/2309.12288),- [Github](https://github.com/lukasberglund/reversal_curse))- We expose a surprising failure of generalization in auto-regressive large language models (LLMs). - **If a model is trained on a sentence of the form ''A is B'', it will not automatically generalize to the reverse direction ''B is A''. This is the Reversal Curse.**
- The Reversal Curse is robust across model sizes and model families and is not alleviated by data augmentation. We also evaluate ChatGPT (GPT-3.5 and GPT-4) on questions about real-world celebrities, such as ''Who is Tom Cruise's mother? [A: Mary Lee Pfeiffer]'' and the reverse ''Who is Mary Lee Pfeiffer's son?''. GPT-4 correctly answers questions like the former 79\% of the time, compared to 33\% for the latter.


![](https://substackcdn.com/image/fetch/$s_!S0sg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd471729-9b9d-4f69-847b-cdc0caac4a14_2930x1656.png)

- **Omar Khattab (Stanford)**: DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines (- [ICLR Spotlight Poster](https://iclr.cc/virtual/2024/poster/17642),- [GitHub](https://github.com/stanfordnlp/dspy))- presented by Krista Opsahl-Ong
- “Existing LM pipelines are typically implemented using hard-coded “prompt templates”, i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce - **DSPy, a programming model that abstracts LM pipelines as text transformation graphs**, or imperative computational graphs where LMs are invoked through declarative modules.
- DSPy modules are parameterized, meaning they can learn how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques.
- We design a compiler that will - **optimize any DSPy pipeline to maximize a given metric**, by creating and collecting demonstrations.
- We conduct two case studies, showing that succinct DSPy programs can express and optimize pipelines that reason about math word problems, tackle multi-hop retrieval, answer complex questions, and control agent loops.
- Within minutes of compiling, DSPy can automatically produce pipelines that outperform out-of-the-box few-shot prompting as well as expert-created demonstrations for GPT-3.5 and Llama2-13b-chat. On top of that, DSPy programs compiled for relatively small LMs like 770M parameter T5 and Llama2-13b-chat are competitive with many approaches that rely on large and proprietary LMs like GPT-3.5 and on expert-written prompt chains.
![](https://substackcdn.com/image/fetch/$s_!kT5Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe458cf22-f3ca-48a6-abb3-7ae503b395ac_2156x1600.png)
