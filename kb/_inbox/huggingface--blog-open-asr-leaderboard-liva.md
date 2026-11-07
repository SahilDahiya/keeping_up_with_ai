---
title: Egyptian and Nigerian English join the Open ASR Leaderboard
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/open-asr-leaderboard-liva
author: Eric Bezzam; Ashley Mo; Aoi Otani
published: '2026-11-06'
fetched: '2026-11-07T06:21:16Z'
classifier: null
taxonomy_rev: 2
words: 356
content_sha256: ca17e0fe66eaeced8fd328a44dea0384051c7bf8a84763918c152698248aaade
---

# Egyptian and Nigerian English join the Open ASR Leaderboard

# 
		
	
	
		Egyptian and Nigerian English join the Open ASR Leaderboard

[Update on GitHub](https://github.com/huggingface/blog/blob/main/open-asr-leaderboard-liva.md)

  [Upvote 5](https://huggingface.co/login?next=%2Fblog%2Fopen-asr-leaderboard-liva) 

![Eric Bezzam's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6384db7fb2906edaf835a91d/MOTXxaOmjlTZ8wONYifnD.jpeg) 

[Ashley Moashleymo2025](https://huggingface.co/ashleymo2025)    

![Liva AI's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/64d5eff05900b6d111c9e1ad/upXC_tilVUY3zVD_7UqJu.png)

[liva-ai](https://huggingface.co/liva-ai)

![Aoi Otani's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/64d5eff05900b6d111c9e1ad/hGnt9yx6LyQP5a2MBpXGg.jpeg) 

[Aoi Otaniaonorii](https://huggingface.co/aonorii)    

![Liva AI's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/64d5eff05900b6d111c9e1ad/upXC_tilVUY3zVD_7UqJu.png)

[liva-ai](https://huggingface.co/liva-ai)

A few months ago, we added private data to the [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard): 11 splits from Appen and DataOceanAI covering scripted and conversational speech from five accents ([blog](https://huggingface.co/blog/open-asr-leaderboard-private-data)). The community response was great, with many **highlighting the importance of held-out sets for trustworthy evaluations**. Since then, we added one more private split for Indian-accented English with Voice Arena ([blog](https://huggingface.co/blog/open-asr-leaderboard-global-south)).

We’re excited to announce a new collaboration with [Liva AI](https://huggingface.co/liva-ai) to add even more private data with two new accents: **Egyptian** 🇪🇬 and **Nigerian** 🇳🇬.

| Dataset | Accent | Duration \[h\] | Style | Transcription | 
|---|---|---|---|---|
| Liva AI Conversational EG | Egyptian | 1.34 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 
| Liva AI Conversational NG | Nigerian | 1.55 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 

This is part of our continued effort to improve representation in ASR evals (more accents and more languages) and to improve trust (new private data to minimize benchmaxxing, and new data providers). We’re excited to see the community continuing to push ASR performance for the world 🤗

## 
		
	
	
		Richer accent breakdown in the Private tab

With these new accents, we can now present a richer breakdown of accents, based on [Kachru’s Three Circles](https://en.wikipedia.org/wiki/World_Englishes#Kachru%27s_Three_Circles_of_English) (kudos to Hume AI for this idea in their [leaderboard](https://huggingface.co/spaces/HumeAI/asr-leaderboard)). The Open ASR Leaderboard will now report:

1. US vs. non-US (*UK, Australia, Canada, India, Nigeria, Egypt*)
2. Inner Circle (*US, UK, Australia, Canada*) vs. Outer & Expanding Circles (*India, Nigeria, Egypt*)

As more accents join, we’ll split the Outer and Expanding Circles.

![thumbnail](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/open_asr_leaderboard/private_data_accent_breakdown.png) 

## 
		
	
	
		About Liva AI

Liva AI collects multimodal interaction data through consumer products used by real people. Because Liva owns both the collection environment and distribution, it can design products around specific model gaps across domains, industries, languages, modalities, and interaction types. This gives it access to natural, high-context behavior that emerges through real product use, rather than artificially elicited or task-based interactions.
