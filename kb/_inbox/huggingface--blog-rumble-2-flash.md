---
title: 'Rumble-2-Flash: an open 0.5B speech model for 40+ languages'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/rumble-2-flash
author: Reson8; Mark 't Hart; Eustache Le Bihan; Eric Bezzam
published: '2026-11-18'
fetched: '2026-11-19T06:12:56Z'
classifier: null
taxonomy_rev: 2
words: 709
content_sha256: c7a6d1506d93cf00c6c41b72ba6817e23c79f366b032cccdfa5aa1977e39d8c7
---

# Rumble-2-Flash: an open 0.5B speech model for 40+ languages

[Automatic Speech Recognition •  0.5B • Updated   •  453  •  101](https://huggingface.co/Reson8/Rumble-2-Flash)  

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6446c3045aa406ee9e16ba57/9zMH4hwUXITSH7LdLHUJa.png) 

# 
		
	
	
		Rumble-2-Flash: an open 0.5B speech model for 40+ languages

[Update on GitHub](https://github.com/huggingface/blog/blob/main/rumble-2-flash.md)

  [Upvote 10](https://huggingface.co/login?next=%2Fblog%2Frumble-2-flash) 

[Reson8reson8-thomas](https://huggingface.co/reson8-thomas)    

![Reson8's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6446c3045aa406ee9e16ba57/9zMH4hwUXITSH7LdLHUJa.png)

[Reson8](https://huggingface.co/Reson8)

[Mark 't HartMarktHart](https://huggingface.co/MarktHart)    

![Reson8's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6446c3045aa406ee9e16ba57/9zMH4hwUXITSH7LdLHUJa.png)

[Reson8](https://huggingface.co/Reson8)

![Eustache Le Bihan's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/660bc459d81d6112496f30f8/jMrpAckFyg-_iHMI7sn2h.jpeg) 

![Eric Bezzam's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6384db7fb2906edaf835a91d/MOTXxaOmjlTZ8wONYifnD.jpeg) 

Today we're open sourcing [Rumble-2-Flash](https://huggingface.co/Reson8/Rumble-2-Flash) under the Apache 2.0 license. It's a 0.5B-parameter speech recognition model for 40+ languages that competes with models 3-60x its size.

- **Runs anywhere**: native support in 🤗 Transformers and vLLM, no custom code
- **40+ languages**: automatic language detection
- **Output control**: numbers as digits or words, fillers, verbatim repeats, forced language
- **Extremely fast**: an hour of audio in about half a second, with over 7,000 RTFx on full batches
- **Holds up on real phone calls**: on par with NVIDIA's Nemotron 3.5 Transcribe (30B) on a 302-hour call-centre benchmark

## 
		
	
	
		Quickstart

## Transcribe with 🤗 Transformers

```
uv pip install torch transformers accelerate
```
```
from transformers import AutoProcessor, AutoModelForMultimodalLM
model_id = "Reson8/Rumble-2-Flash"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForMultimodalLM.from_pretrained(model_id, device_map="auto")
inputs = processor.apply_transcription_request(
    audio="https://hf.co/datasets/hf-internal-testing/dummy-audio-samples/resolve/main/bcn_weather.mp3",
    language="English",  # omit to detect automatically
).to(model.device, dtype=model.dtype)
output = model.generate(**inputs, max_new_tokens=512)
generated = output[:, inputs["input_ids"].shape[-1]:]
print(processor.decode(generated, return_format="transcription_only")[0])  # return_format="parsed" if detecting language
```
`audio` accepts a local path, a URL, a NumPy array, or a list of these.

## 
		
	
	
		How it's built

Rumble-2-Flash uses the Qwen3-ASR architecture for day-0 support. If your stack runs Transformers or vLLM, it runs Rumble-2-Flash, with no forked runtime or `trust_remote_code`.

To find out how small a model could get before accuracy dropped off, we distilled Rumble-2, our larger production model, into it with on-policy distillation. The student doesn't train on transcripts the teacher wrote. It transcribes the audio itself, and the teacher grades that transcript token by token: at every position, it gives its own probability for what should come next, and the student learns to match it. Because the student learns from its own outputs, it gets corrected on exactly the mistakes it makes, with feedback on every token instead of one score per clip.

On-policy distillation normally requires teacher and student to share a tokenizer, and ours don't: choosing Qwen3-ASR meant taking its vocabulary too. [GOLD](https://huggingface.co/spaces/HuggingFaceH4/on-policy-distillation) removes that restriction. It merges tokens where the two tokenizers split the text differently, so both models are compared over the same text. Tokens that exist in both vocabularies are compared directly, and the rest by their sorted probabilities.

![On-policy distillation with GOLD: the student transcribes, the teacher scores every token, and GOLD aligns the two tokenizers](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/gold.png) 

![On-policy distillation with GOLD: the student transcribes, the teacher scores every token, and GOLD aligns the two tokenizers](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/gold-dark.png) 

## 
		
	
	
		Results

### 
		
	
	
		Accuracy for its size

On the Open ASR Leaderboard [multilingual](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard?languages=Reson8%2FRumble-2-Flash&proprietary=false) track, Rumble-2-Flash averages a **6.96% error rate** across Chinese, German, French, Italian, Spanish, Portuguese, Hindi, Dutch and English. That's better than Meta's omniASR-LLM 7B, a model 15x larger, and ahead of Whisper large-v3. On the [English](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) track it averages **6.6% WER**.

![Average error rate against model size for open-weight models on the Open ASR Leaderboard multilingual track, including English](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/size-vs-wer-en.png) 

![Average error rate against model size for open-weight models on the Open ASR Leaderboard multilingual track, including English](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/size-vs-wer-en-dark.png) 

### 
		
	
	
		Speed

Rumble-2-Flash is also fast. Its throughput depends on how full the batches are: on the larger datasets in HF's Open ASR Leaderboard, where batches stay full, it reaches **over 7,000 RTFx**. That's an hour of audio in about half a second.

### 
		
	
	
		Real phone calls

Clean audio is easy. Phone calls are compressed and noisy, and often have speakers with very different accents. On [AppTek's call-centre benchmark](https://huggingface.co/datasets/apptek-com/apptek_callcenter_dialogues) (302 hours of helpline calls, 14 English accents, scored with AppTek's own script), Rumble-2-Flash reaches **7.86% WER**, on par with NVIDIA's Nemotron 3.5 Transcribe (30B) at 7.78%. That's well ahead of Qwen3-ASR 0.6B (8.7%), from the same model family, and close to Qwen3-ASR 1.7B (7.4%), the only model in the comparison that does better.

![WER on the AppTek call-centre benchmark](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/apptek.png) 

![WER on the AppTek call-centre benchmark](https://huggingface.co/datasets/Reson8/public-media/resolve/main/blog/rumble-2-flash/apptek-dark.png) 

## 
		
	
	
		Try it

The weights are on the Hub at [Reson8/Rumble-2-Flash](https://huggingface.co/Reson8/Rumble-2-Flash). It's also available through our [API](https://www.reson8.dev).

We're very curious what you'll build with it. Tell us in the [Discussions tab](https://huggingface.co/Reson8/Rumble-2-Flash/discussions) what you've made, what you like, and what you'd like to see changed in a next version.
