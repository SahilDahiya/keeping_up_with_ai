---
title: Creating a Natural-Sounding Text-to-Speech Voice
kind: blog
topic: models
subtopic: multimodal
secondary_topics:
- agents/harness
summary: Contrasts end-to-end voice-to-voice agents (cost scales with call length)
  against the cheaper 'stitched' STT to turn-detection to LLM to TTS pipeline Cresta
  runs in production, then details a five-step professional voice-cloning process
  from ~5 hours of studio speech. Notes telephony's 300-3400 Hz band strips the presence
  that makes web demos sound better than real calls.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/creating-a-natural-sounding-text-to-speech-voice
author: Henry Zhang
published: '2026-02-10'
fetched: '2026-08-20T06:10:07Z'
classifier: claude
taxonomy_rev: 2
words: 1005
content_sha256: 55230704be55e521866dc81f9212d1cb3d4de745c6d8b28bab8f98253cdd709e
---

# Creating a Natural-Sounding Text-to-Speech Voice

Currently, two approaches dominate when it comes to building voice AI agents:

1. **Voice-to-voice** : A promising approach for the long term, but cost scales exponentially with call length.
2. **“Stitched” pipeline** : Speech to text (STT) → turn detection → Large Language Model (LLM) response → text to speech (TTS). This approach is significantly cheaper and offers greater control of the LLM response, thus improving instruction following and function tool calling, which is critical to reliably handling complex use cases in production.

At Cresta, we use the stitched approach for our [AI Agents](https://cresta.com/ai-agent) in production. To get a reliable and natural experience, you need all four pieces to sing:

1. **STT** with low word error rate (WER)
2. **Turn detection** that’s accurate*and* low-latency
3. **LLM-generated content** that reads like spoken conversations, not formal essays
4. **TTS voice** that sounds natural and is aligned with the customer’s brand

In this article, we will focus on #3 and #4: the *content* and the *voice*.

## Crafting the voice of Cresta

We auditioned many voices from leading TTS providers. None felt distinctly Cresta, so we chose the hard path: professionally cloning a Cresta employee’s (Crestan) voice, following five broad steps.

### Step 1: Define the brand

We translated “how Cresta sounds” into 12 measurable traits: pitch height, brightness, pace, melody, and more.

The short brief: *A trusted guide with modern polish.* 

More specifically:

- Overall energy that’s upbeat enough to feel reassuring and positive without being over the top
- Low-mid average pitch with a darker voice color brings confidence and authority
- Mildly warm resonance kept very clean with crisp, but not sharp, diction
- A measured and natural conversational pace with intentional pauses between ideas and sentences
- Intonation with just enough liveliness to be memorable and persuasive

### Step 2: Curate the scripts

Customer support conversations often require explicit spelling of numbers, URLs, codewords, and specific brand names. To clone the voice of Cresta, we developed scripts that emphasize these challenging cases based on real customer conversations in production, and we included unscripted segments to capture genuine emotions.

We also had the voice talent prepare ten short personal stories—covering joy, sadness, empathy and other strong emotions—to elicit authentic prosody on demand. TTS models learn the voice actor's intonation, rhythm, and timbre, rather than simply memorizing the specific recordings of certain sentences.

### Step 3: Coach the Crestan voice “actor”

Great voice cloning requires relaxed, confident delivery. Reading pure transcripts can lead to people without formal acting training over-enunciating and tensing up. To maintain a natural, conversational delivery, we recorded the voice "actor" and me (Henry) having natural conversations in the studio. We also worked with a voice coach to soften the speaker's habitual uptalk and vocal fry without eliminating their unique identity.

### Step 4: Record in a professional studio

To ensure consistent, high-fidelity capture, we opted to record in a professional podcast studio. Crucially, microphone placement and distance were meticulously calibrated, as these foundational elements cannot be corrected in post-production. We recorded approximately five hours of speech spanning diverse contexts to provide the TTS model with the necessary breadth for robust learning.

A direct comparison between the studio recording and an at-home mic setup revealed the profound impact of the professional environment: the studio voice boasts significantly less background noise and echo, without sacrificing the inherent "warmth" and natural character of the Crestan's voice.

Watch a behind-the-scenes look at the process here:

### Step 5: Edit during post-production

Volume fluctuations between sessions can result in jarring, sentence-to-sentence volume changes in the voice clone. As such, we normalized the volume and applied compression to mitigate occasional bursts of over-excitement. Voice equalization (EQ) helps remove muddiness (around 100–300 Hz) and adds clarity (around 3–5 kHz) to the voice.

However, this editing may not directly translate into great-sounding phone calls with AI agents, as telephony systems only preserve the 300–3400 Hz frequency range. This limitation loses a voice’s “presence” and “clarity”, thereby explaining [why AI agents often sound different in web-based demos compared to actual production phone calls](https://cresta.com/blog/building-voice-ai-that-actually-works-balancing-realistic-voices-vs-production-ready-performance).

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/698a7fa96d38a71f2ed88957_blog--creating-a-natural-sounding-text-to-speech-voice--in-line-graph-1.avif)

*Figure: Voice equalization that is tailored to the Crestan’s voice*

## Teaching the LLM to speak (and not write) like a human

Even a technically perfect TTS voice can sound robotic when reading an awkward script. LLMs often default to written formal language, such as, "Please wait while I retrieve your account information," which immediately signals "bot." To counter this, we meticulously tune prompts for *spoken* language. 

Here are a few example principles:

- **Few short sentences:** Long, complex sentences flatten vocal inflection and invite a monotonous delivery. Our target is a maximum of 15 words per sentence and no more than three sentences per turn.
- **One question at a time:** AI agents should avoid asking multiple questions in a single turn, as this often triggers involuntary caller interruptions after the first question. Also, placing a statement after a question invites the caller to preemptively jump in and answer the question, disrupting the AI agent and degrading the conversational experience.
- **Empathetic acknowledgement:** Repetitive, canned phrases and overly general transition statements can feel robotic and cold. Responses that acknowledge the caller’s specific concern can convey empathy and inspire confidence in the AI agent’s ability to understand and help. In sensitive use cases, such as healthcare appointment booking, acknowledging the caller’s underlying emotional state is a critical prerequisite before returning to the core task.
- [**Omnichannel**](https://cresta.com/blog/crestas-ai-agent-is-omnichannel-seamless-conversations-anytime-anywhere) **delivery:** Lengthy, alphanumeric sequences, such as complex URLs or security keys, should not be read aloud. Transmitting the link via SMS or chat saves the user from a cumbersome spelling exercise.

## The result

By pairing a professionally cloned “Cresta” voice with an LLM tuned for conversational speech, we’ve built a voice agent that sounds like a trusted guide, not a scripted bot.

If you’re curious how this translates in reality, try our Signal voice agent on [cresta.com](http://cresta.com), and tell us what you notice first: the calm presence, the natural pacing, or simply that you forgot it wasn’t human halfway through.
