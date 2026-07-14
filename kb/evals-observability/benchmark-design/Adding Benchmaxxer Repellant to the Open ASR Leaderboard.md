---
title: Adding Benchmaxxer Repellant to the Open ASR Leaderboard
kind: blog
topic: evals-observability
subtopic: benchmark-design
secondary_topics:
- models/benchmarks
summary: Adds private held-out Appen/DataoceanAI accent and conversational splits
  to the Open ASR Leaderboard to blunt benchmaxxing and test-set contamination, keeping
  the public average WER separate behind a toggle, and discusses the text normalizer
  needed to standardize model outputs.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/open-asr-leaderboard-private-data
author: Eric Bezzam; Steven Zheng; Eustache Le Bihan; Sergio Bruccoleri; Jeanine Sinanan-Singh;
  Casey Ford; Guanbo Wang; Yukai Huang; Ke Li; Yufeng Hao; Liao Xiaoling
published: '2026-05-06'
fetched: '2026-07-14T22:03:37Z'
classifier: claude
taxonomy_rev: 1
words: 1630
content_sha256: c81a61d248c58038750a4e837cf00c981e829d6ee4e7deb193fec185ffb77220
---

# Adding Benchmaxxer Repellant to the Open ASR Leaderboard

Automatic Speech Recognition •  2B • Updated   •  899k  •  1.04k  

#### CohereLabs/cohere-transcribe-03-2026

![](https://cdn-avatars.huggingface.co/v1/production/uploads/1678549441248-5e70f6048ce3c604d78fe133.png) 

 Published
					May 6, 2026 

  Upvote 

 18

SBruccoleriAppen    

jmss-appen    

c-e-ford-appen    

wgb14    

YukaiHuang    

like2026    

logicbean    

ally-lxl    

**TLDR**: [Appen Inc.](https://huggingface.co/AppenAIResearch) and [DataoceanAI](https://huggingface.co/DataoceanAI1) have provided high-quality English ASR datasets covering scripted and conversational speech over multiple accents. To prevent potential risks of benchmaxxing or test-set contamination, we will keep these datasets private for a high-quality measure of performance on multiple tasks.

**We’re not updating the average WER at this time**: by default, the leaderboard’s Average WER remains computed on public datasets only. You can optionally include the private datasets using the toggle to see their impact 👀

Since its launch in September 2023, the [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) has been visited over 710K times. We’re blown away by the community’s interest and motivation to keep pushing speech recognition 🗣️

Two words sum up the objectives (but also challenges) in maintaining a benchmark like the Open ASR Leaderboard:

- **Standardization**: models can have different conventions for their usage and outputs, e.g. with/without punctuation and casing. Datasets have the same challenges and can be structured differently. To this end, all test sets have been gathered into a- [single dataset](https://huggingface.co/datasets/hf-audio/open-asr-leaderboard)on the Hub for easy access and previewing. Moreover, to standardize model outputs and dataset transcripts, we use a- [normalizer](https://github.com/huggingface/open_asr_leaderboard/blob/0009f5fe216d63eea809f9849f4d4534c6ab341e/normalizer/normalizer.py#L528)that (among other things) removes punctuation and casing, and maps to American spelling. It is based on the normalizer of- [Whisper](https://github.com/openai/whisper).
- **Openness**: the- [UI code](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard/tree/main)and- [evaluation scripts](https://github.com/huggingface/open_asr_leaderboard)are open-sourced. This has helped not only to incorporate new models, but also to improve the quality of the evaluation procedure through community feedback and contributions.

Standardization and openness are essential for meaningful benchmarking, but they also make benchmarks more susceptible to benchmark-specific optimization ("benchmaxxing"), where models improve leaderboard performance without corresponding gains in real-world robustness. As models and use cases evolve, the Open ASR Leaderboard will continue incorporating high-quality datasets and new evaluation settings to better reflect real-world performance and improve robustness against benchmark-specific optimization.

As discussed in our [report](https://arxiv.org/abs/2510.06961), there is no single "catch-all" ASR model: some perform better on American English, others on diverse accents and multilingual settings, while others are optimized for speed or conversational audio. Different applications also prioritize different capabilities, so a model that performs less well on one dimension is not necessarily a worse model overall. The goal of the Open ASR Leaderboard is to capture these nuances and provide a more holistic view of ASR performance.

To this end, we have worked with Appen Inc. and DataoceanAI to curate high-quality datasets for ASR benchmarking. Below is some information on the various splits.

| Dataset | Accent | Duration [h] | Male (%) / Female (%) | Style | Transcription | 
|---|---|---|---|---|---|
| Appen Scripted AU | Australian | 1.42 | 49 / 51 | Read | Punctuated, cased. | 
| Appen Scripted CA | Canadian | 1.53 | 52 / 48 | Read | Punctuated, cased. | 
| Appen Scripted IN | Indian | 1.02 | 49 / 51 | Read | Punctuated, cased. | 
| Appen Scripted US | American | 1.45 | 49 / 51 | Read | Punctuated, cased. | 
| Appen Conversational IN | Indian | 1.37 | 51 / 49 | Conversational, spontaneous | Punctuated, disfluencies. | 
| Appen Conversational US003 | American | 1.64 | 49 / 51 | Conversational, spontaneous | Punctuated, cased, disfluencies. | 
| Appen Conversational US004 | American | 1.65 | 49 / 51 | Conversational, spontaneous | Punctuated, disfluencies. | 
| DataoceanAI Scripted US | American | 2.43 | 54 / 46 | Read | Punctuated, cased (proper nouns), disfluencies. | 
| DataoceanAI Scripted GB | British | 2.43 | 47 / 53 | Read | Punctuated, disfluencies. | 
| DataoceanAI Conversational US | American | 8.82 | NA | Conversational, spontaneous | Punctuated, disfluencies. | 
| DataoceanAI Conversational GB | British | 5.96 | NA | Conversational, spontaneous | Punctuated, disfluencies. | 

Below are sample audio showing the variety of content (scripted, conversational, acronyms, disfluencies, proper nouns).

While private datasets may sound contrary to the spirit of openness, we believe that incorporating such datasets will **increase the trustworthiness** of the Open ASR Leaderboard, as they are less likely to be exploited for benchmaxxing, whether by model developers who explicitly use the public test sets or who try to find training data that closely resembles a particular dataset to boost their score in the macroaverage.

With these datasets, we can also provide targeted metrics to highlight gaps and biases between controlled and often saturated settings (scripted, American accent) and more nuanced conditions (conversational and non-American accents). Below is a screenshot of the new "Private data" tab.

Below is how each column is computed.

- "Average WER" computes a macroaverage of the data provider averages, so that they are weighted equally.
- "Avg Scripted" performs a macroaverage of all scripted datasets.
- "Avg Conversational" performs a macroaverage of all conversational datasets.
- "Avg US" performs a macroaverage of all datasets with American accents.
- "Avg non-US" performs a macroaverage of all datasets with non-American accents.

We intentionally do not provide a score on each split, to avoid model developers from boosting their score with a specific data provider or accent.

Get your model on the Open ASR Leaderboard, and we'll run the evaluation! As before, the process for adding a model to the leaderboard takes place on the Open ASR Leaderboard [GitHub](https://github.com/huggingface/open_asr_leaderboard):

- Open a pull request, and a [model checklist](https://github.com/huggingface/open_asr_leaderboard/blob/main/.github/PULL_REQUEST_TEMPLATE.md#new-model-checklist)will appear. As before, you should report your results on the public datasets.
- We will verify the results on the public sets and compute the metrics on the private ones.
- Confirm the results we’ve obtained.

While you wait for your model to be added to the Open ASR Leaderboard, you can self-report your metrics on the public sets by adding a YAML file like [this](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026/blob/main/.eval_results/open_asr_leaderboard.yaml) to your model card. Your model will then appear on an (unverified) leaderboard that appears on the [dataset page](https://huggingface.co/datasets/hf-audio/open-asr-leaderboard) (see screenshot below). More on this approach to decentralized evaluation can be read [here](https://huggingface.co/blog/community-evals).

They could. We’ve asked Appen and DataoceanAI to not provide this data to their clients. But even if they do not provide this exact data, data from a similar distribution could still help the model on the corresponding evaluation set (similar to benchmaxxing by optimizing for a challenging task from the public sets). To this end, having multiple data providers balances out the advantage a model may get from having used data from one of the providers. And we are open to more data providers and eval sets for the "Private data" tab!

Moreover, to ensure that the private sets do not affect the model ranking, we’ve defaulted the Average WER **to not include the Private sets in its macroaverage.**

In the screenshot below, you can see that "Private data" is toggled off. This means that the macroaverage across datasets does not include it.

Simply toggle on "Private data" splits to include them in the macroaverage.

The "Rank Δ" column shows how the ordering changes relative to the default macroaverage configuration. Including or excluding public datasets also changes the macroaverage, allowing users to tailor the evaluation to the use cases and data distributions most relevant to their application.

We’re excited to hear the community’s feedback on how the new track and dataset toggling features help users identify the model(s) that best fit their application(s). We’re also looking into evaluations that better reflect real-world noisy conditions, and you can expect some news on that 😉

While preparing the private evaluation sets, we took extra care to ensure consistent audio and transcript quality across datasets, including developing tooling to identify challenging cases such as low signal-to-noise conditions or transcript mismatches, since these factors can meaningfully affect WER. More on that in a future post!

 Automatic Speech Recognition •  2B • Updated   •  899k  •  1.04k 

 Benchmark • Updated  •  126k •  17.1k  •  42 

🏆

 1.4k

Explore and compare speech recognition model benchmarks

More Articles from our Blog

audiospeechleaderboard

 
- +1

 9

 June 24, 2026 audiospeechleaderboard

  27

 November 21, 2025 Just a quick observation on how we evaluate our models: The two data vendors mentioned earlier are offering datasets directly to ASR service providers for training. With that in mind, it feels like we should be extra prudent about mixing private data into our evaluations.

At the same time, we're missing out on a lot of high-quality, open-source speech datasets simply because their creators don't have sales teams advocating for them. It would be a huge step forward to open a channel where the research community can recommend these datasets to the leaderboard directly.

P.S. I found myself relating a lot to King George in the movie Hoppers recently. That beaver king just believes the best about everyone. I want to bring that same optimism here—hoping that everyone continues to follow the leaderboard rules, avoids training on open-source test sets, and actively cleans their training data of any contamination.

Wei Chu

Researcher[wei@olewave.com](mailto:wei@olewave.com)

[@weiwchu](https://huggingface.co/weiwchu)  thank you for your comments 🙂 

The two data vendors mentioned earlier are offering datasets directly to ASR service providers for training. With that in mind, it feels like we should be extra prudent about mixing private data into our evaluations.


Completely agree, that is why we don't include these new datasets in the default average WER computation. We hope that users have this nuanced view of the data sources. But also on the types of content, which is why we added splits on scripted/conversational and American/non-American accents.

It would be a huge step forward to open a channel where the research community can recommend these datasets to the leaderboard directly.


This is possible on our GitHub repo! [This checklist](https://github.com/huggingface/open_asr_leaderboard/blob/main/.github/PULL_REQUEST_TEMPLATE.md) describes how a new model or dataset can be contributed.
