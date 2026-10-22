---
title: '𝜏-i18n: Evaluation across languages and beyond task completion'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: sierra
url: https://sierra.ai/blog/tau-i18n
author: Soham Ray
published: '2026-10-21'
fetched: '2026-10-22T06:09:27Z'
classifier: null
taxonomy_rev: 2
words: 774
content_sha256: 9bbed849e8781b863272d944dcde43cf926941fcc22b69d37a45452781873efe
---

# 𝜏-i18n: Evaluation across languages and beyond task completion

# 𝜏-i18n: Evaluation across languages and beyond task completion

In our earlier [𝜏-Voice experiments](https://arxiv.org/html/2603.13686v1), accents caused the largest average drop in task completion among the factors we tested. That raised a broader question: how well do voice agents work for callers in other languages?

Today we’re introducing **𝜏-i18n** (pronounced tau-internationalization), which extends **𝜏**-Voice to five more languages: Spanish, Brazilian Portuguese, Hindi, Korean, and Mandarin.

𝜏-i18n uses the same airline, retail, and telecom tasks across languages. Tasks, policies, tools, and success criteria stay fixed, allowing us to compare performance across languages.

## From internationalization to localization

**Internationalization** is the groundwork that lets a product adapt to different languages and locales. **Localization** is the work of making it fit a particular one. In customer service, that can involve names, dates, currencies, product terms, and local conventions. Voice adds another layer: pronunciation, code-switching, forms of address, and the way people take turns in conversation.

Completing the task is only part of a good call. The conversation also has to feel native, down to what Clay Bavor calls “unreasonable localization.” In Hindi, an agent speaking with a female voice might say **“मैं आपकी मदद कर सकता हूँ”** instead of **“मैं आपकी मदद कर सकती हूँ”**, referring to itself in the masculine. In Mandarin, an agent might say **“执行取消操作”** (“execute a cancellation operation”) where a person would simply say **“帮您取消”** (“help you cancel”). Both get the point across, but neither sounds quite right.

We built 𝜏-i18n around language packs, which lets native speakers define those choices for each locale. The packs adapt caller identities and matching database records, personas, voices, speech conventions, and evaluation rules while keeping the underlying service tasks the same. For example, Korean and Mandarin callers typically give their family name first. An agent that puts the first spoken name into a given-name field can fail authentication even when it hears the name correctly.

## Beyond task completion

Task completion tells us whether the agent achieved the caller’s goal. It doesn’t tell us how the call went. 𝜏-i18n reports two additional measures:

- **Interaction** measures whether the agent participates effectively in the conversation. Does it respond or yield at the right time? Does it avoid interruptions and long monologues? Can it tell when a backchannel (“mm-hmm”) or a stray sound doesn’t need a response? We call that last skill selectivity. Interaction also measures tool-use efficiency, including whether the agent calls tools with the right arguments and avoids agent-caused errors.
- **Generation quality** measures what the caller actually hears. Naturalness captures translationese, grammatical-gender mistakes, inappropriate register, and missed honorifics. Speech fidelity measures whether the audio accurately delivers the intended words, names, and numbers.

We report these outcomes separately because an agent can complete the task while still falling short on the interaction or the language itself.

## Where agents lose ground

Across the three voice agents on the 𝜏-i18n leaderboard and 2,700 primary calls, we see meaningful differences across task completion, interaction, and generation quality. Performance also varies considerably by language.

![Task completion, interaction, and generation](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F1bd77a51355892141704809546a4c87554839034-2080x1216.png&width=3840&quality=75)

On task completion, Spanish, Hindi, and Portuguese trail English by 2.4, 3.8, and 6.4 percentage points on average. Korean and Mandarin trail by 22.6 and 9.1 points, despite running the same tasks, and Korean is the weakest language for all three agents.

Interaction reveals a different set of weaknesses. Korean and Mandarin calls have the most tool failures for every agent. Responsiveness is a common failure: GPT Live 1 and Gemini 3.8 Live miss a caller turn, reply slowly, or fail to yield in more than 80% of calls, against 16% for Grok Voice Think Fast 2.0. Selectivity is weak too: in 26–60% of calls, the agent responds more than three times to backchannels, vocal tics, or speech not directed at it.

And for generation quality, GPT Live 1 leads both task completion (79.9%) and generation quality (63.4%). Grok Voice Think Fast 2.0 leads interaction at 52.6% but scores just 17.7% on generation quality. The most responsive agent is not necessarily the most natural speaker.

## Bringing more languages and locales to the benchmark

These five additions are a starting point. We have open sourced our [codebase](http://github.com/sierra-research/tau2-bench) and **LanguageFactory**, the framework behind the language packs, so native speakers, researchers, and language communities can adapt 𝜏-i18n for more languages and locales.

Contributors will be able to build representative callers, review voices and sample conversations, and define the conventions agents should be evaluated on.

If your language or locale is missing, we’d love your help bringing it to 𝜏-i18n.

*Representing work by Edgard dos Santos Paiva, Ruben Valenzuela and Keshav Dhandhania at Sierra, Karthik Narasimhan at Princeton University and Victor Barres at Mercor.*
