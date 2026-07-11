---
title: Why Transcription is Vital to Contact Center AI
topic: models
subtopic: multimodal
secondary_topics:
- evals-observability/evaluation
summary: Explains why transcription quality is a core dependency for downstream AI
  systems that operate on spoken conversations.
source: cresta
url: https://cresta.com/blog/transcription-is-critical-to-contact-center-ai
author: null
published: '2022-02-10'
fetched: '2026-07-11T04:02:53Z'
classifier: codex
taxonomy_rev: 1
words: 1105
content_sha256: 1810c32902d7dd6f2be84313870c14714618af5c526959814de8620b5cf45137
---

# Why Transcription is Vital to Contact Center AI

## Why Transcription is Vital to Contact Center AI

Any fool can know. The point is to understand. –Albert Einstein

The multitude of ways artificial intelligence (AI) is helping to realize the future of contact centers is exciting. And, thanks to the digital adoption [spurred](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/the-covid-19-recovery-will-be-digital-a-plan-for-the-first-90-days) by the early months of COVID-19, if that future isn’t happening now, then it’s right around the corner.But no matter how rapidly contact center AI (CCAI) evolves, it’s important to understand it remains tethered to an easily overlooked factor — transcription accuracy. And, for those who are responsible for investing in the future of [customer service AI](https://cresta.com/customer-service/), it’s crucial to know why.

## To Understand What We’re Saying, Machines Need to Know What’s Being Said

Contrary to Einstein’s POV, the ability for machines to understand speech does come down to their ability to know exactly what’s being said. Or, more specifically, natural language understanding (NLU) is entirely dependent on a given AI’s ability to transcribe the varying pitches, accents, noises, and dialects that constitute human speech.And, to make a difference in the modern contact center, understanding what’s being said needs to happen in real time.Enter transcription engines, which, traditionally, have had separate [acoustic](https://www.rev.com/blog/resources/what-is-an-acoustic-model-in-speech-recognition), pronunciation and [language models](https://www.techtarget.com/searchenterpriseai/definition/language-modeling), each trained separately. Getting these models to work in concert required a lot of time and effort. Traditional transcription engines were difficult to tune and offered relatively low transcription accuracy. However, transcription architecture has advanced rapidly over the past decade.Today’s best-in-class speech engines use an end-to-end (E2E) model that unifies and optimizes audio and language modeling. Text transcribed in this way is now processed through multiple NLP pipelines, working in sync to generate structured data. This data is then interpreted by NLU systems to better [understand](https://cresta.com/blog/cresta-understands-conversations/) the intentions, goals, and salient parts of what’s being said.Ironically, this modern architecture is both simpler and more accurate than its forebears. And, perhaps most importantly, E2E transcription engines are also much easier to fine-tune on customer-specific data. Within contact centers specifically, this means their transcription accuracy quickly improves as they’re trained on brand and product-specific customer interactions. E2E is quickly becoming the gold standard for modern transcription engines and is the approach we use here at Cresta.But this brings us back to our original point — exceptional natural language understanding (NLU) like that employed by [Cresta](https://cresta.com/blog/cresta-understands-conversations/), is only as good as the structured data it’s given, which is only as good as the quality of transcription.Meaning (in turn) the ability of real-time coaching to help agents help their customers is tied to the accuracy of its transcription engine. As the very non-Einsteinian saying goes, “garbage in, garbage out.”

## The Industry Standard for Measuring Transcription Accuracy

Okay, so how do we define what a “good” transcription accuracy is? That’s a simple question, but one that’s a bit complicated to answer.Let’s start with word error rate (WER), the [industry standard](https://www.assemblyai.com/blog/2021-benchmark-report/) for measuring transcription accuracy of speech-to-text capability. WER is [calculated](https://deepgram.com/blog/what-is-word-error-rate/) by totaling substitutions, insertions, and deletions in a piece of transcribed text and dividing that amount by the number of words that were actually said. And, as it is with most tech, as platforms that offer speech-to-text improve year to year, their respective WERs go down.For example, in 2018, one of the leading speech-to-text platforms boasted a WER of about [30%](https://www.voicegain.ai/post/speech-to-text-accuracy-benchmark-june-2020-results). By 2020 their estimated average dropped to [27%](https://www.cxtoday.com/speech-analytics/how-reliable-is-speech-to-text-in-2021/#:~:text=As%20per%20benchmarks%20published%20in,scored%20a%20slightly%20better%2084%25.). By 2021, just a year later, another estimate clocked this same WER at [12%](https://www.assemblyai.com/blog/2021-benchmark-report/). So, as transcription engines improve, the definition of “good transcription accuracy” will remain fluid. For reference, today’s “off-the-shelf” speech-to-text products (e.g., Amazon, Google, IBM Watson) average WERs of [25%](https://deepgram.com/blog/what-is-word-error-rate/).

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f5ce13f4bc3f91986fd_68135f3032482e8c5d313acd_transcript-example.avif)

It’s important to note that much like NLU “garbage in, garbage out”, WER measurements are heavily influenced by the quality of training data. For many businesses, the WER for their business-specific terms will be much more important than WER for general language. Which is why tunability is so important.

## What Cresta Looks for in Modern Transcription Engines

All this said, there are a lot of ways you can measure the quality of modern transcription engines. So, by way of example, here are the three main criteria in addition to transcription accuracy that our own engineers prioritize when it comes to transcription engines at [Cresta](http://cresta.com/):

### 1. Customizability

For contact center applications, the ability to customize and tune transcription engines is paramount. Each business is different, and quickly tuning transcription models to accurately detect brand-specific language is necessary for effective AI-powered features (e.g., “fiber” as it relates to fiber-optic bandwidth service, as opposed to the thing [1 in 10](https://www.usnews.com/news/health-news/articles/2021-06-08/fewer-than-1-in-10-american-adults-get-enough-dietary-fiber#:~:text=June%208%2C%202021%2C%20at%206%3A47%20a.m.&text=TUESDAY%2C%20June%208%2C%202021%20(,a%20bowl%20of%20whole%20grains.&text=Fiber%20intake%20was%20assessed%20using%20dietary%20questionnaires.) Americans don’t get enough of). In doing so, WER for specific customers can be significantly improved. Cresta’s proprietary transcription approach allows our teams to quickly create custom transcription models for each customer.

### 2. Real-Time

Latency is vitally important for transcription engines used in real-time contact center applications. This is because initial (i.e., non-final) transcripts are first surfaced and then adjusted to become more accurate as more context is gathered. Final results for some audio segments can take much longer to arrive (500ms to 2s after) than the initial guesses (100ms to 500ms). Latency is at the core of Cresta’s real-time architecture, allowing us to present highly accurate transcriptions to agents and managers as a conversation unfolds

### 3. Integrability

Last but not least, is integrability. The best-in-class transcription engines can take in audio streams from many different sources, including SIPREC, Amazon Connect, directly from the agent desktop, etc. And with audio systems constantly evolving, especially with the shift to CCaaS and UCaaS, quick and easy integrations are critical. With this in mind, Cresta has been built to quickly integrate into cloud and hybrid environments, helping us deliver on our promise of functioning as a true intelligence layer for customer conversations.

## Transcription Accuracy and the Future of Contact Center AI

So what does the future hold for transcription engines? At some point in the future, will flawless transcription accuracy be possible for contact center AI? Probably not. Even [human-powered](https://www.nytimes.com/wirecutter/reviews/best-transcription-services/) transcription services fail to maintain a 100% accuracy rate due to the fact that language itself is constantly adapting and evolving.But 100% accuracy isn’t the point. At [Cresta](https://cresta.com/), rather than aspiring towards automation, we believe the true power of AI lies in using it to assist the workforce. This means delivering effective real-time coaching and productivity capabilities that helps agents deliver impactful customer experiences.For more about how Cresta’s transcription engine is helping customers, take a peek at our recent case study featuring Crissa Graham and Jason Love from [Holiday Inn Club Vacations](https://cresta.com/blog/holiday-inn-driving-customer-obsession-with-cresta/). 😎**Thank you **to Ashish Agarwal and Daniel Hoske for input, reviews and edits.
