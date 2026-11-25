---
title: Post-train your own medical ASR model to outperform the frontier
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/evaluation
summary: Besimple fine-tuned Nemotron 3.5 Transcribe and Qwen3-ASR for medical terminology
  using an iterative loop that targets a 274,541-term medical dictionary, mixing synthetic
  TTS and human speech; using 813 hours of audio and ~$500 of GPU time, Term-WER dropped
  to 0.87% and 2.05% respectively, beating closed medical ASR models.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/post-train-your-own-medical-asr-model-to-outperform-the-frontier/
author: Lei Pan; Ardin Lo; Brandon Tai; Reese Tateo; Yi Zhong
published: '2026-11-23'
fetched: '2026-11-25T06:07:49Z'
classifier: claude
taxonomy_rev: 2
words: 1725
content_sha256: 1ad24c45f28287f4e4a6d03b79c02c721ff561b7dff36f33a0bf09f219c0d3fd
---

# Post-train your own medical ASR model to outperform the frontier

News
# Post-train your own medical ASR model to outperform the frontier

How Besimple adapted Nemotron 3.5 Transcribe and Qwen3-ASR to medical terminology using Baseten Training.


- Authors
- Last updated
- Originally published

Unlike standard transcription use cases, voice agents in healthcare need to transcribe specific drug names, procedures, and diagnoses correctly. But general-purpose ASR models often miss rare medical terms, and the closed medical models that do better don't let teams control the weights or adapt them to their own vocabulary.

[Besimple](https://besimple.ai/) used [Baseten Training](https://docs.baseten.co/training) to fine-tune open transcription models for medical terminology recognition—critical for voice agent deployment in healthcare, pharmaceutical, and medical domains—and outperformed every frontier ASR model we tested.

Using MedDictate, a public third-party benchmark of human-spoken medical dictation, fine-tuned Nemotron 3.5 Transcribe scored a medical term word error rate (Term-WER) of 0.87% (lower is better; this is also a 69% improvement over the vanilla model). Using the same training recipe on Qwen3-ASR, it also achieved a low WER of 2.05% (a 64% improvement over the vanilla model), placing it roughly in the middle of the pack among the models we benchmarked and showing the recipe's robustness.

Using 813 hours of speech data and only $500 worth of GPU hours (for both models combined!), this shows that teams can fine-tune a medical ASR model themselves that outperforms even the best domain-specific closed models.

This is how we did it.

Our training target was to improve medical term transcription while preventing regression in general term transcription. After researching publicly available benchmarks, we picked the following benchmarks:

1. [MedDictate](https://huggingface.co/datasets/corti/med-dictate): A benchmark from Corti of human-spoken medical dictation; 24 English recordings are used for evaluation.
2. [MedTerm](https://huggingface.co/datasets/corti/med-term): A benchmark from Corti of synthetic clinical notes read by text-to-speech models; 200 recordings in English are used for evaluation.
3. [FLEURS](https://huggingface.co/datasets/google/fleurs): A benchmark from Google on multilingual speech understanding; 647 recordings in English are used for evaluation.

Because we used a combination of synthetic and real human speech for training, both MedDictate and MedTerm were included to evaluate model performance on synthetic versus real human speech.

Besimple has a large network of human speakers and a rigorous recording and review pipeline, allowing them to easily acquire new human speech data based on training needs. Baseten provided managed training, checkpoint storage, serving infrastructure, and hands-on model and evaluation support. Together, we built a loop that iteratively tests different training and data recipes.

Our first attempt used 100 hours of medical domain script reading collected by Besimple. Full-model fine-tuning improved some medical metrics while regressing others, and the model began repeating itself on long recordings. Even after switching to LoRA, a lightweight fine-tuning method, and mixing general speech into training to stabilize outputs, gains remained modest.

After analyzing the errors, it was clear that models had more trouble with unseen terms. We tried to teach the model word components. For example, if *choledocholithotripsy* became *cholelithotripsy*, train on *choledochojejunostomy* and *choledochoduodenostomy* to reinforce the prefix *choledoch-*. This helped, but the model still struggled to assemble an unseen complete term. The conclusion was to stop working around these vocabulary gaps and cover the vocabulary directly.

We compiled a broad medical dictionary of 274,541 terms. Rather than teaching a model all the terms, we built an iterative training loop that focuses on unfamiliar terms:

1. Evaluate the current model on a fixed sample of dictionary terms.
2. For each term the model still gets wrong, or regresses on, write a new natural sentence using that term.
3. Synthesize the sentences using a text-to-speech (TTS) model with a variety of accents.
4. Append the new clips to the accumulated training data and continue training.
5. Iteratively replace synthetic speech data with human speech data.

A few findings shaped the recipe:

- **Natural sentences beat isolated words.** Training on single words made recognition worse.
- **Breadth beats depth.** Covering more terms helped more than adding extra contexts for a smaller vocabulary.
- **Know when to stop.** Gains on the full dictionary flattened after the third round. Besimple selected that round's scripts as the set to record with human speakers.
- **Human speech is critical.** Human speakers bring the variation that TTS struggles to capture: differences in accent, pacing, emphasis, and how people actually pronounce medical terms.
- **Check synthetic data pronunciation**. For rare terms, TTS models may pronounce them incorrectly. Besimple spot-checked medical term pronunciation and regenerated clips that were pronounced incorrectly with an International Phonetic Alphabet (IPA) pronunciation override.

| Final training data mix | Unique audio hours | Loss share | 
|---|---|---|
| Short passages from medical dictionary (synthetic + human) | 482 | 70% | 
| Human medical passages | 21 | 10% | 
| Human general speech | 67 | 10% | 
| Synthetic dense medical passages | 243 | 10% | 
| Total | 813 | 100% | 

Our final training mix included dictionary sentences, human medical passages, general speech, and dense synthetic medical notes. Human recordings replaced about 28.9% of the synthetic dictionary clips, adding more variation in pronunciation and delivery.

The training runs used a modest compute budget: an estimated $120 for Qwen3-ASR training jobs on H100 GPUs, and $380 for the Nemotron 3.5 Transcribe run on B200 GPUs.

Most improvements come from the iterative loop of identifying unseen medical terms from the dictionary, even if the training data is fully synthetic. Both Nemotron 3.5 Transcribe and Qwen3-ASR improved by over 50% from baseline on both MedDictate and MedTerm when fine-tuned with 710 hours of synthetic medical audio.

We further evaluated the impact of replacing part of the synthetic training data built from medical dictionary passages with 154 hours of real human speech across a variety of accents.

On MedDictate, a benchmark of human spoken medical dictation, replacing it with human speech improved Term-WER further by 20% on both models. The result is more interesting for MedTerm, a benchmark of synthetic clinical notes read by a TTS model. Nemotron 3.5 Transcribe regressed when human data was added, while Qwen3-ASR improved.

Variations in fine-tuning outcomes likely originate from differences in the base models' learning capacities, as well as inherent structural distinctions among the benchmarks. Therefore, selecting an evaluation benchmark that closely mirrors your specific production workload, ideally synthesizing a benchmark directly from production logs, is essential.

| Model | Shares of human speech | MedDictate Term-WER | MedTerm Term-WER | 
|---|---|---|---|
| Nemotron 3.5 Transcribe – Base model | / | 2.83% | 12.45% | 
| Nemotron 3.5 Transcribe – Fine-tuned with 482 hours of synthetic passages from a medical dictionary | 11% | 1.09% | 5.65% | 
| Nemotron 3.5 Transcribe – Fine-tuned with mixed synthetic and human passages from a medical dictionary | 19% | 0.87% | 6.43% | 
| Qwen3-ASR – Base model | / | 5.84% | 14.72% | 
| Qwen3-ASR – Fine-tuned with 482 hours of synthetic passages from a medical dictionary | 11% | 2.57% | 5.69% | 
| Qwen3-ASR – Fine-tuned with mixed synthetic and human passages from a medical dictionary | 19% | 2.05% | 4.82% | 

We further evaluated the models on FLEURS for general term transcription. Fine-tuning can sometimes overfit and cause regression in other areas. Fine-tuned Nemotron 3.5 Transcribe showed improved WER, suggesting that our fine-tuning improved overall transcription capability across the board. Qwen3-ASR demonstrated a slight WER regression on FLEURS, a typical trade-off commonly observed when fine-tuning models.

| Model | MedDictate Term-WER | FLEURS WER | 
|---|---|---|
| Base Qwen3-ASR | 5.84% | 4.59% | 
| Fine-tuned Qwen3-ASR | 2.05% | 5.52% | 
| Base Nemotron 3.5 Transcribe | 2.83% | 5.36% | 
| Fine-tuned Nemotron 3.5 Transcribe | 0.87% | 5.13% | 

> “Baseten made it easy to get from new speech data to a fine-tuned model we could deploy and evaluate. With the entire workflow on one platform, we could focus on the loop that mattered: find the errors, improve the data, and train again. We control the data and model weights, so each experiment gives us a foundation to build on.”

Every stage of the experiment ran on Baseten: training jobs, checkpoint storage, deployment, and evaluation. We went from a new batch of data to a live endpoint on [Baseten Dedicated Inference](https://www.baseten.co/products/dedicated-inference/) without leaving the platform. We ran every round of the experiment independently, launching jobs and deploying checkpoints directly.

**Train**: A Baseten Training job runs Besimple’s trainer on Baseten-managed GPUs, with data attached from the supported data sources. We experimented with data mixes and training recipes, and evaluated via checkpoint deployment.

**Serve in one click**: Every checkpoint a training job writes is saved to Baseten storage and listed on the job page. The process is simple: Pick a checkpoint, choose a serving mode and GPU, and click deploy. The endpoint mounts the weights directly from training storage. You don’t need to download, re-upload, or wrap anything in serving code. The recording below follows that path for a fine-tuned Nemotron 3.5 Transcribe checkpoint, from training recipe to a transcribed clinical dictation.

The workflow we used is available to any team adapting an open ASR model to its own domain:

1. Start with the [Qwen3-ASR cookbook](https://github.com/basetenlabs/ml-cookbook/tree/main/training-jobs/examples/qwen3-asr-transformers) and your own data.
2. Run it as a [Baseten Training Job](https://docs.baseten.co/training/overview); checkpoints land in Baseten secure storage, ready for deployment.
3. Deploy the checkpoint to a batch or real-time endpoint.
4. Evaluate the endpoint on both your domain set and general speech, and turn the failures into your next training dataset.

Interested in building a domain-specific speech model?  Try out the above workflow, or [reach out to the Baseten team](https://www.baseten.co/talk-to-us/research-support/) if you are interested in the recipe, data, or model checkpoint.

| Model | MedDictate Term-WER | MedTerm Term-WER | FLEURS WER | 
|---|---|---|---|
| Base Qwen3-ASR | 5.84% | 14.72% | 4.59% | 
| Base Nemotron 3.5 Transcribe | 2.83% | 12.45% | 5.36% | 
| Fine-tuned Qwen3-ASR | 2.05% | 4.82% | 5.52% | 
| OpenAI GPT Transcribe | 1.48% | 10.64% | 4.86% | 
| ElevenLabs Scribe V2 Medical | 1.13% | 7.09% | 4.23% | 
| Google Gemini 3.5 Transcribe | 1.05% | 9.61% | 4.39% | 
| Fine-tuned Nemotron 3.5 Transcribe | 0.87% | 6.43% | 5.13% | 

*The table above compares base, fine-tuned, and closed ASR models on medical terminology accuracy (MedDictate and MedTerm Term-WER) and general transcription accuracy (FLEURS WER). Lower scores are better across all three benchmarks.*
