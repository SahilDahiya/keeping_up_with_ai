---
title: Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps
kind: blog
topic: models
subtopic: reinforcement-learning
secondary_topics:
- prompt-engineering/structured-output
summary: Fine-tunes LiquidAI's LFM2.5-350M with GRPO via the TRL library on ~500 samples
  over 100 steps (runnable on a free-tier Colab/Kaggle GPU), raising structured-output
  schema compliance on the IFStruct benchmark from 22.6% to 29.7%.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/grpo-with-trl-ifstruct
author: Leonie Monigatti; Ben Burtenshaw; Sergio Paniego
published: '2026-09-03'
fetched: '2026-09-04T06:15:50Z'
classifier: claude
taxonomy_rev: 2
words: 470
content_sha256: f96896d974ff38ac8d22eea6c1f0f9c9a16a5b8092c18b943963bc78198b3e3a
---

# Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps

[Text Generation •  0.4B • Updated   •  91.5k  •  411](https://huggingface.co/LiquidAI/LFM2.5-350M)  

#### LiquidAI/LFM2.5-350M

![](https://cdn-avatars.huggingface.co/v1/production/uploads/61b8e2ba285851687028d395/EsTgVtnM2IqVRKgPdfqcB.png) 

Published
					September 3, 2026 

  Upvote 

 10

iamleonie    

This guide is a fully public, inexpensive recipe for making a small model substantially better at structured-output compliance. We fine-tune [LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) with Group Relative Policy Optimization (GRPO) using the [TRL library](https://huggingface.co/docs/trl/en/index) and evaluate it on the [IFStruct benchmark](https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0). The full run takes around 500 samples and 100 training steps, small enough for a free-tier Colab or Kaggle GPU, and is available on [GitHub](https://github.com/Liquid4All/cookbook/blob/main/finetuning/notebooks/grpo_with_trl_ifstruct.ipynb). The results show that even a light fine-tuning procedure improves performance **from 22.6% to 29.7%** on the IFStruct benchmark.
Structured output is one of the most common real-world tasks for LLMs, yet most benchmarks fold it into broader reasoning or extraction scores rather than measuring it on its own. Whether a model reliably returns valid, parseable output in the requested format and shape — schema compliance — is often what decides whether it can be wired into a downstream system at all.

## 
	
		
	
	
		Prerequisites
	

This guide has two halves that run in different places:

## 
	
		
	
	
		IFStruct Evaluation on LFM2.5-350M (Base model)
	

Then we start the base-model server with the following command:

Once the server is running, we can run the full benchmark with 2000 samples:

## 
	
		
	
	
		GRPO Fine-tuning with TRL on Structured Outputs
	

### 
	
		
	
	
		Training data
	

Because the Nemotron data distribution differs from the IFStruct evaluation, we augment the prompts to close two gaps between them:

### 
	
		
	
	
		Model and LoRA
	

This trains ~6M parameters, about 1.66% of the model.

### 
	
		
	
	
		Reward functions
	

### 
	
		
	
	
		Training
	

We train for 100 steps with 8 generations per prompt group, sized for a free-tier 16 GB GPU:

As you can see in the notebook, over the run, all three reward components climb, the KL from the reference model lifts off zero after warmup, and the truncated-completion fraction stays near zero.

### 
	
		
	
	
		Merging and saving the model
	

Finally, we merge the LoRA adapter back into the base weights and save it as a single self-contained checkpoint, ready to convert to GGUF for serving:

## 
	
		
	
	
		IFStruct Evaluation on GRPO Tuned LFM2.5-350M
	

Then we serve the merged model with the following command:

Then, we will run the full IFStruct evaluation again with the fine-tuned model:

Comparing the two runs on the identical serving stack:

	

## 
	
		
	
	
		Conclusion
	


```
brew install llama.cpp
llama-server --version
```
| IFStruct group | base | GRPO-tuned | Δ | 
|---|---|---|---|
| **Overall** | 22.6% | **29.7%** | **+7.1** | 
| JSON | 18.0% | 31.9% | +13.9 | 
| YAML | 27.2% | 27.5% | +0.3 | 
| Wrapper key | 28.5% | 29.7% | +1.2 | 
| Bare list | 16.6% | 29.7% | +13.1 | 

 Text Generation •  0.4B • Updated   •  82.4k  •  97 

More Articles from our Blog

nlpguidecommunity

  112

 August 26, 2026  106

 August 18, 2026
