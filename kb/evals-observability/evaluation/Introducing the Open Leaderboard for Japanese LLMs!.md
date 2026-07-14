---
title: Introducing the Open Leaderboard for Japanese LLMs!
kind: blog
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/benchmarks
summary: The Open Japanese LLM Leaderboard evaluates models on 16+ llm-jp-eval tasks
  (NLI, translation, summarization, QA, code generation), motivated by Japanese-specific
  challenges like the three-script writing system and the absence of word boundaries
  for tokenization.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/leaderboard-japanese
author: Akim Mousterou; Yusuke Miyao; Namgi Han; Takumi Okamoto; Shigeki Ishida; Hysts;
  Clémentine Fourrier
published: '2024-11-20'
fetched: '2026-07-14T22:09:37Z'
classifier: claude
taxonomy_rev: 1
words: 1492
content_sha256: d0d97ba65d118448f75e4927cf9e11d3925bedc1b118bc36ce4ee46feae7aec7
---

# Introducing the Open Leaderboard for Japanese LLMs!

Viewer • Updated  •  164 •  420  •  7  

# 
	[
		
	](https://huggingface.co#introduction-to-the-open-leaderboard-for-japanese-llms)
	
		Introduction to the Open Leaderboard for Japanese LLMs
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/leaderboard-japanese.md)

[  Upvote 39 ](https://huggingface.co/login?next=%2Fblog%2Fleaderboard-japanese)

![Akim Mousterou's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/63171caf1cc81c5e95ed7b92/29I5Lr0vLRcQR7AfCZcYj.jpeg) 

  [Akim MousterouAkimfromParis    ](https://huggingface.co/AkimfromParis)

![LLM-jp's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/649259b1b2bcb8358cf77958/WEl_gpGpAWQte_podstYD.png)

[llm-jp](https://huggingface.co/llm-jp)

[Yusuke Miyaomiyao-yusuke    ](https://huggingface.co/miyao-yusuke)

![LLM-jp's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/649259b1b2bcb8358cf77958/WEl_gpGpAWQte_podstYD.png)

[llm-jp](https://huggingface.co/llm-jp)

[Namgi HannamgiH    ](https://huggingface.co/namgiH)

![LLM-jp's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/649259b1b2bcb8358cf77958/WEl_gpGpAWQte_podstYD.png)

[llm-jp](https://huggingface.co/llm-jp)

[Takumi Okamotot0-0    ](https://huggingface.co/t0-0)

![LLM-jp's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/649259b1b2bcb8358cf77958/WEl_gpGpAWQte_podstYD.png)

[llm-jp](https://huggingface.co/llm-jp)

[Shigeki Ishidash1gechan    ](https://huggingface.co/sh1gechan)

![LLM-jp's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/649259b1b2bcb8358cf77958/WEl_gpGpAWQte_podstYD.png)

[llm-jp](https://huggingface.co/llm-jp)

![hysts's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1643012094339-61914f536d34e827404ceb99.jpeg) 

  ![Clémentine Fourrier's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1644340617257-noauth.png) 

  We'd like to announce the ** Open Japanese LLM Leaderboard**, composed of more than 20 datasets from classical to modern NLP tasks to understand underlying mechanisms of Japanese LLMs. The Open Japanese LLM Leaderboard was built by the 

**, a cross-organizational project for the research and development of Japanese large language models (LLMs) in partnership with**

[LLM-jp](https://llm-jp.nii.ac.jp/en/)**Hugging Face**.

The Japanese language presents its own specific challenges. Morphologically rich and in constant evolution due to historical and cultural interactions with the rest of the world, its writing system is based on a mixture of three separate sets of characters: simplified Chinese ideographic symbols kanjis (漢字), a phonetic lettering system, Hiraganas (平仮名 / ひらがな), and Katakanas (片仮名 / カタカナ) often used for foreigners words. Modern Japanese is arguably one of the hardest language to process, as it mixes up a blend of Sino-Japanese, native Japanese, Latin script (romaji /ローマ字), loanwords from the Dutch, Portuguese, French, English, German, plus Arabic and traditional Chinese numerals. In addition, the Japanese digital world brought us an evolution of emoticons written in Unicode : ), Kaomoji using Cyrillic alphabet. (っ °Д °;)っ and Greek alphabets ＿φ(°-°=). Without forgetting, of course, the classic emojis that originated from Japan with the rise in popularity of mobile phones in the 1990s.

![Japanese writing system](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/fxTPcxQqAo49s_jE_5wCw.png)


The intricate writing system of Japanese hides an extra layer of complexity, the lack of space between words. Similar to the Chinese or Thai languages, Japanese language doesn’t have white space between linguistic units, making the detection of word boundaries extremely difficult during tokenization. Over the years, the vibrant Japanese ecosystem (from prestigious university laboratories and AI startups to the R&D centers of industry giants) has incorporated the specificities of Japanese NLP to develop modern robust Japanese LLMs, but the field has been lacking a centralized and open system to compare these models.

We therefore introduce the Open Japanese LLM Leaderboard, a collaboration between Hugging Face and LLM-jp, to foster transparency in research, and encourage an open-source model development philosophy. We strongly believe this initiative will serve as a platform for Japanese and international researchers to collaborate, evaluate, and enhance Japanese LLMs.

## 
	[
		
	](https://huggingface.co#introduction-to-the-leaderboard-tasks)
	
		Introduction to the Leaderboard Tasks
	

The Open Japanese LLM Leaderboard evaluates Japanese LLMs using a specialized evaluation suite, ** llm-jp-eval**, covering a range of 16 tasks from classical ones (such as 

*Natural Language Inference, Machine Translation, Summarization, Question Answering*) to more modern ones (such as

*Code Generation*,

*Mathematical Reasoning*or

*Human Examination*). Tasks are launched in 4-shot.

Datasets have been compiled by the evaluation team of LLM-jp, either built from scratch with linguists, experts, and human annotators, or translated automatically to Japanese and adjusted to Japanese specificities, and for some requiring long context reasoning. For a better understanding of the leaderboard, we will detail samples from 8 datasets (in Japanese followed by the English translation in light gray). For more details about all the available tasks, please see to the “About” tab of the leaderboard, and official links on each datasets.

### 
	[
		
	](https://huggingface.co#jamp)
	
		Jamp
	

**Jamp** (*Controlled Japanese Temporal Inference Dataset for Evaluating Generalization Capacity of Language Models*) is the Japanese temporal inference benchmark for NLI. The dataset explore English and Japanese sentence pairs of various temporal inference patterns annotated with the golden labels such as entailment, neutral, or contradiction.

![Jamp](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/EF2BuJC_oWvw2Jc5kvGCo.png)


### 
	[
		
	](https://huggingface.co#jemhopqa)
	
		JEMHopQA
	

**JEMHopQA** (*Japanese Explainable Multi-hop Question Answering*) is a Japanese multi-hop QA dataset that can evaluate internal reasoning. It is a task that takes a question as input and generates an answer and derivations. 

![JEMHopQA](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/ZicrCMz4LtXDxSxeBBTl-.png)


### 
	[
		
	](https://huggingface.co#jcommonsenseqa)
	
		jcommonsenseqa
	

**jcommonsenseqa** is a Japanese version of CommonsenseQA, which is a multiple-choice question answering dataset. The purpose of this dataset is to evaluate commonsense reasoning ability.

![jcommonsensqa](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/s21OdhQIRRW7dqTF9mYoq.png)


### 
	[
		
	](https://huggingface.co#chabsa)
	
		chABSA
	

**chABSA** was developed as an *Aspect-Based Sentiment Analysis* dataset. ChABSA is based on financial reports of Japanese listed-companies in the 2016 fiscal year, annotated on the pair of entity, the attribute, and the sentiment. More specifically, 230 out of 2,260 companies listed in Japan (roughly 10% of all company)  were annotated according to the taxonomy of the Japanese financial regulator, *Financial Service Agency (FSA)*.

![chABSA](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/O2kTDa1w0YAJOW1quXuDQ.png)


### 
	[
		
	](https://huggingface.co#mbpp-ja)
	
		mbpp-ja
	

The **mbpp-ja** dataset is a programming dataset: it is a Japanese version of *Mostly Basic Python Problems dataset* (MBPP) translated from English into Japanese by ** LLM-jp** by leveraging the translation tool 

**.**

[DeepL](https://www.deepl.com)![mbpp-ja](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/g21y5x0BuCWlX6foubsv5.png)


### 
	[
		
	](https://huggingface.co#mawps)
	
		mawps
	

Based on the dataset `MAWPS` *(A Math Word Problem Repository)*, the Japanese **mawps** dataset is a mathematical evaluation dataset. This version evaluates the abilities of solving novel tasks by reasoning step-by-step, procedure otherwise known as Chain-of-Thought (CoT) reasoning, and was adjusted to converting names of people, units, and places to fit the Japanese context. The level of mathematical reasoning is rather simple: addition, subtraction, multistep arithmetic, and single or pairs of equations.

![mawps](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/1FXowoymJJ72r6I2Q9si_.png)


### 
	[
		
	](https://huggingface.co#jmmlu)
	
		JMMLU
	

**JMMLU** is a knowledge dataset using four-choice question answers. It consists in Japanese-translated questions from a portion of MMLU dataset that evaluates knowledge on high-school level tests. Based on 57 subjects such as astronomy, chemistry, sociology, international law, etc., questions and answers were translated in Japanese, while being adjusted to unique Japanese cultural context like Japanese civics, Japanese geography, and Japanese idioms. 

![JMMLU](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/gVojua_19QLpFJqGSA8xz.png)


### 
	[
		
	](https://huggingface.co#xl-sum)
	
		XL-Sum
	

**XL-Sum** is a summarisation dataset based on the research titled *“XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages”* that leverages the Japanese translation of articles from BBC News. The dataset is separated in three parts; the title, the text (the full-length article), and the summary. Topics include global issues, politics, technology, sports, and culture.

![XL-Sum](https://cdn-uploads.huggingface.co/production/uploads/63171caf1cc81c5e95ed7b92/dlMq7ii_VfVzYHLDQx7Y_.png)


## 
	[
		
	](https://huggingface.co#technical-setup)
	
		Technical Setup
	

The leaderboard is inspired by the ** Open LLM Leaderboard**. Models that are submitted are deployed automatically using HuggingFace’s 

**, evaluated through the**

[Inference endpoints](https://huggingface.co/docs/inference-endpoints/index)**library on the version 1.14.1, with memory-efficient inference and serving engine,**

[llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)**on the verison v0.6.3, and computed in the backend by the premium computer platform for research in Japan,**

[vLLM](https://github.com/vllm-project/vllm)**.**

[mdx](https://mdx.jp/)## 
	[
		
	](https://huggingface.co#observations)
	
		Observations
	

According to the Japanese LLMs guide ** Awesome Japanese LLM** (available in Japanese, English, and French), Meta's 

`LLama` open-source architecture seems to be the favourite of many Japanese AI labs. However, other architectures have also been successfully leveraged by the Japanese open-source community, such as `Mistral` from French Mistral, and `Qwen` by Chinese Alibaba. These are the architectures which led to the best scores on the Japanese LLM Leaderboard.On general language processing tasks, we observe that Japanese LLMs based on open-source architectures are closing the gap with closed source LLMs, such as the Japanese LLM `llm-jp-3-13b-instruct`, developed by LLM-jp and funded by university grants, reaching a performance similar to closed source models. Domain specific datasets, such as `chABSA` (finance), `Wikipedia Annotated Corpus` (linguistic annotations), code generation (`mbpp-ja`) and summarization (`XL-Sum`) remain a challenge for most LLMs. Interestingly, models originating from Japanese-based companies or labs have better scores on the specific `JCommonsenseMorality` dataset. It evaluates model ability to make choices according to Japanese values when against ethical dilemmas

## 
	[
		
	](https://huggingface.co#future-directions)
	
		Future directions
	

The Open Japanese LLM Leaderboard will follow the development of the evaluation tool ** llm-jp-eval** to reflect the constant evolution of Japanese LLMs. The following are just examples of future directions in llm-jp-eval that we would like to support, feel free to contact us to give a hand or suggest directions!

- **New datasets: More Japanese evaluations**The evaluation team of llm-jp-eval is working on this section, adding at the moment- [JHumanEval](https://huggingface.co/datasets/kogi-jwu/jhumaneval)- *Japanese version of HumanEval*) and- [MMLU](https://github.com/hendrycks/test)- *Measuring Massive Multitask Language Understanding*).
- **New evaluation system: Chain-of-Thought evaluation**We'd like to compare the performance of LLMs between when employing Chain-of-Thought prompts against basic prompts to have a finer understanding of model behaviors.
- **New metric support: Out-of-Choice rate**For some evaluation tasks that already have a clear list of labels used in the specific task, such as Natural Language Inference, we'd like to add a complementary metric, testing how often the model predicts out-of-choice tokens. As the choices are provided in the prompt, this will allow us to evaluate how well each LLM is able to follow specific instructions.

## 
	[
		
	](https://huggingface.co#acknowledgements)
	
		Acknowledgements
	

Built by the research consortium **LLM-jp**, the Open Japanese LLM Leaderboard is proudly sponsored by the ** National Institute of Informatics** in Tokyo, Japan in collaboration with the  high-performance computing platform, 

**program.**

[mdx](https://mdx.jp/)We would like to extend our gratitude to **Prof. Yusuke Miyao** and **Namgi Han** from the *University of Tokyo* for their scientific consultation and guidance, as well as **Clémentine Fourrier** and **Toshihiro Hayashi** of *Hugging Face* that has assisted with the integration and customization of their new evaluation framework and leaderboard template.
