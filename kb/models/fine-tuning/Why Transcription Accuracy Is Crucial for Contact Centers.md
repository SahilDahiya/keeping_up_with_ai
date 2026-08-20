---
title: Why Transcription Accuracy Is Crucial for Contact Centers
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics:
- evals-observability/evaluation
summary: 'Details fine-tuning end-to-end ASR base models on hand-annotated customer
  audio: 2-3 weeks of human transcription plus 1-2 weeks of training, roughly 4-6
  weeks total. Reports base-model WER under 11% streaming and under 9% pre-recorded,
  custom models under 9% and 8% respectively, with Slot Error Rate on customer keywords
  cut by close to 30%.'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/why-transcription-accuracy-is-crucial-for-optimizing-performance-in-the-contact-center
author: Jessica Stallings
published: '2024-07-01'
fetched: '2026-08-20T06:16:47Z'
classifier: claude
taxonomy_rev: 2
words: 913
content_sha256: 2e515d390d87a4a478a21b2f079f65d4cab5eb14c206cf5e10152fee1adbe622
---

# Why Transcription Accuracy Is Crucial for Contact Centers

A high-quality voice transcript is crucial in delivering highly effective assistance to agents in real time. At Cresta, we have developed a unique and robust [platform powered by cutting-edge generative AI](https://cresta.com/ai-platform/) to offer highly accurate transcripts in a number of different languages.As with any of our products and capabilities, we strive to constantly innovate, improve, and deliver the best possible performance that outpaces the industry. Read on to learn more about how we do this.

## The base model

We use language and region-based Automatic Speech Recognition (ASR) models trained on a substantial amount of data sampled from a varied set of accent, tone, vocabulary, and noise conditions. The deep learning architecture of these models uses state-of-the-art techniques to train the end-to-end models, which offer higher accuracy than traditional models because of the joint modeling of acoustic, phoneme, and language modeling tasks.We refer to this model as the “base model”. This base model alone exhibits a highly comparable transcription quality when benchmarking against the top ASR providers. Furthermore we also leverage base models that are specific to certain industries, like healthcare and financial services, where common vocabulary already exists in the base model.

## The custom model

In certain cases, customers have specialized vocabularies or technical jargon that comes up frequently in their conversations. In these scenarios, Cresta has the ability to further train or finetune these base models on customer-specific data. This ensures that our models consistently and accurately transcribe the more specialized pieces of the conversation that may ultimately be the most relevant to the customer.We have found that doing so greatly increases the accuracy of our models on customer-specific data and delivers a better experience for the end user.Please refer to the image below to understand what a custom training process would look like:

### Under the hood

The first phase of creating any custom model is for Cresta’s expert human transcribers to hand-annotate the customer-specific audio data so we have a high-quality dataset source to train our base model on. Hand-annotating is an involved task and can take anywhere from 2-3 weeks to complete.We follow this up with a fine-tuning run of our existing language and/or domain-specific base models which can take a further 1-2 weeks. All in, the total customization timeline for a custom model is around 4-6 weeks.

## Evaluating speech recognition models

We perform extensive evaluations of our models with great statistical rigor to ensure that what we deliver will always provide the highest quality and value to the customer.To this end, we use two widely accepted industry-standard statistical metrics:

1. Word Error Rate (abbreviated as WER) - How many **words** the transcription model gets wrong when compared to a human-annotated “ground truth” version of the same audio(s).
2. Slot Error Rate (abbreviated as SER) - How many **keywords** the transcription model gets wrong when compared to a human-annotated “ground truth” version of the same audio(s) and a given**keyword list** .

These metrics give us insight into how well our models perform against any customer data - and makes clear the next steps to further improve the model.

### The details

Both WER and SER calculate how many errors our models make while transcribing audio. On a given model and audio dataset pair, the lower these values are, the higher the quality of the models is.The difference between these metrics is that WER focuses on the entire transcript holistically when calculating how many errors the models make. Meanwhile, SER focuses solely on customer-specific keywords; this is key because even if the model makes tiny errors here and there, we will still get the most important and relevant terms right.In a real-time streaming context with high-quality audio, our English models can safely manage an industry-leading WER of < 11% on our base models and < 9% on our custom models.This gets even better with pre-recorded audio where our English models can deliver a WER of < 9% with our base models and < 8% on our custom models.**To be clear, these numbers are only approximations**. The performance can vary on customer-specific data.We’ve seen our custom training approach reduce the SER by close to 30% on customer-specific data once training is complete.

## Why transcription accuracy matters

When it comes to operations on an enterprise scale, the accuracy of transcription is pivotal for the efficacy of all downstream AI models. Precise transcriptions ensure that the data fed into AI systems is of the highest quality, which is in turn essential for tasks such as sentiment analysis, detection of customer intent and trends, and predictive analytics. Inaccurate transcriptions can lead to significant misunderstands, miscommunications, and erroneous outputs, inhibiting decision-making processes and harming customer interactions.For many companies, where the stakes of customer interactions are high and the margin for error is minimal, ensuring transcription accuracy is not just a technical requirement - but a strategic imperative. This accuracy forms the foundation upon which reliable, actionable insights are built, allowing for operational efficiency, business growth, and competitive advantage.

## More salient features

Cresta’s models are the fastest in the industry and offer the lowest latencies in both the streaming and post-call contexts when compared to the rest of the industry.We also apply numerous post-processing features to deliver the best possible formatting of the transcripts to ensure that our transcripts are not just accurate but also very readable.Cresta is committed to the continual improvement of its voice transcription offering and you can expect our transcription quality to only get better with time!
