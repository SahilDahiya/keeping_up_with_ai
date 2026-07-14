---
title: Introducing the Open Leaderboard for Hebrew LLMs!
kind: blog
topic: models
subtopic: benchmarks
secondary_topics:
- evals-observability/evaluation
summary: An open leaderboard for Hebrew LLMs, motivated by Hebrew's root-and-pattern
  morphology breaking tokenization strategies designed for simpler languages; it evaluates
  on Hebrew-native tasks (Q&A, sentiment, winograd, translation) rather than translated
  English benchmarks.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/leaderboard-hebrew
author: Shaltiel Shmidman; Tal Geva; Omer Koren; Clémentine Fourrier
published: '2024-05-05'
fetched: '2026-07-14T22:10:23Z'
classifier: claude
taxonomy_rev: 1
words: 754
content_sha256: d1dc74e82fa231c106c6895c9f41133c34b001952518f210a53205387fcaf527
---

# Introducing the Open Leaderboard for Hebrew LLMs!

Viewer • Updated  •  43.6k •  70  •  2  

# 
	[
		
	](https://huggingface.co#introducing-the-open-leaderboard-for-hebrew-llms)
	
		Introducing the Open Leaderboard for Hebrew LLMs!
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/leaderboard-hebrew.md)

[  Upvote 59 ](https://huggingface.co/login?next=%2Fblog%2Fleaderboard-hebrew)

[Shaltiel ShmidmanShaltiel    ](https://huggingface.co/Shaltiel)

![DICTA: The Israel Center for Text Analysis's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641c500c21964f8f6d456bb5/8Ue0UMUF7yHs3KsEc7Ybm.png)

[dicta-il](https://huggingface.co/dicta-il)

[Tal GevaTalGeva    ](https://huggingface.co/TalGeva)

[HebArabNlpProject](https://huggingface.co/HebArabNlpProject)

[Omer KorenOmerKo    ](https://huggingface.co/OmerKo)

[Webiks](https://huggingface.co/Webiks)

![Clémentine Fourrier's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1644340617257-noauth.png) 

  Hebrew is a morphologically rich language with a complex system of roots and patterns. Words are built from roots with prefixes, suffixes, and infixes used to modify meaning, tense, or form plurals (among other functions). This complexity can lead to the existence of multiple valid word forms derived from a single root, making traditional tokenization strategies, designed for morphologically simpler languages, ineffective. As a result, existing language models may struggle to accurately process and understand the nuances of Hebrew, highlighting the need for benchmarks that cater to these unique linguistic properties.

LLM research in Hebrew therefore needs dedicated benchmarks that cater specifically to the nuances and linguistic properties of the language. Our leaderboard is set to fill this void by providing robust evaluation metrics on language-specific tasks, and promoting an open community-driven enhancement of generative language models in Hebrew. We believe this initiative will be a platform for researchers and developers to share, compare, and improve Hebrew LLMs.

## 
	[
		
	](https://huggingface.co#leaderboard-metrics-and-tasks)
	
		Leaderboard Metrics and Tasks
	

We have developed four key datasets, each designed to test language models on their understanding and generation of Hebrew, irrespective of their performance in other languages. These benchmarks use a few-shot prompt format to evaluate the models, ensuring that they can adapt and respond correctly even with limited context.

Below is a summary of each of the benchmarks included in the leaderboard. For a more comprehensive breakdown of each dataset, scoring system, prompt construction, please visit the `About` tab of our leaderboard. 

- **Hebrew Question Answering**: This task evaluates a model's ability to understand and process information presented in Hebrew, focusing on comprehension and the accurate retrieval of answers based on context. It checks the model's grasp of Hebrew syntax and semantics through direct question-and-answer formats.- *Source*:- [HeQ](https://aclanthology.org/2023.findings-emnlp.915/)dataset's test subset.
 
- **Sentiment Accuracy**: This benchmark tests the model's ability to detect and interpret sentiments in Hebrew text. It assesses the model's capability to classify statements accurately as positive, negative, or neutral based on linguistic cues.- *Source*:- [Hebrew Sentiment](https://huggingface.co/datasets/HebArabNlpProject/HebrewSentiment)- a Sentiment-Analysis Dataset in Hebrew.
 
- **Winograd Schema Challenge**: The task is designed to measure the model’s understanding of pronoun resolution and contextual ambiguity in Hebrew. It tests the model’s ability to use logical reasoning and general world knowledge to disambiguate pronouns correctly in complex sentences.- *Source*:- [A Translation of the Winograd Schema Challenge to Hebrew](https://www.cs.ubc.ca/~vshwartz/resources/winograd_he.jsonl), by Dr. Vered Schwartz.
 
- **Translation**: This task assesses the model's proficiency in translating between English and Hebrew. It evaluates the linguistic accuracy, fluency, and the ability to preserve meaning across languages, highlighting the model’s capability in bilingual translation tasks.- *Source*:- [NeuLabs-TedTalks](https://opus.nlpl.eu/NeuLab-TedTalks/en&he/v1/NeuLab-TedTalks)aligned translation corpus.
 

## 
	[
		
	](https://huggingface.co#technical-setup)
	
		Technical Setup
	

The leaderboard is inspired by the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard), and uses the [Demo Leaderboard template](https://huggingface.co/demo-leaderboard-backend). Models that are submitted are deployed automatically using HuggingFace’s [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index) and evaluated through API requests managed by the [lighteval](https://github.com/huggingface/lighteval) library.
The implementation was straightforward, with the main task being to set up the environment; the rest of the code ran smoothly.

## 
	[
		
	](https://huggingface.co#engage-with-us)
	
		Engage with Us
	

We invite researchers, developers, and enthusiasts to participate in this initiative. Whether you're interested in submitting your model for evaluation or joining the discussion on improving Hebrew language technologies, your contribution is crucial. Visit the submission page on the leaderboard for guidelines on how to submit models for evaluation, or join the [discussion page](https://huggingface.co/spaces/hebrew-llm-leaderboard/leaderboard/discussions) on the leaderboard’s HF space.

This new leaderboard is not just a benchmarking tool; we hope it will encourage the Israeli tech community to recognize and address the gaps in language technology research for Hebrew. By providing detailed, specific evaluations, we aim to catalyze the development of models that are not only linguistically diverse but also culturally accurate, paving the way for innovations that honor the richness of the Hebrew language. Join us in this exciting journey to reshape the landscape of language modeling!

## 
	[
		
	](https://huggingface.co#sponsorship)
	
		Sponsorship
	

The leaderboard is proudly sponsored by [DDR&D IMOD / The Israeli National Program for NLP in Hebrew and Arabic](https://nnlp-il.mafat.ai/) in collaboration with [DICTA: The Israel Center for Text Analysis](https://dicta.org.il) and [Webiks](https://webiks.com), a testament to the commitment towards advancing language technologies in Hebrew. We would like to extend our gratitude to Prof. Reut Tsarfaty from Bar-Ilan University for her scientific consultation and guidance.
