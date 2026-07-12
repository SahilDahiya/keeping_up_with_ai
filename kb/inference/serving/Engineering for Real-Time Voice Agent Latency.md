---
title: Engineering for Real-Time Voice Agent Latency
topic: inference
subtopic: serving
secondary_topics:
- models/multimodal
summary: Technical discussion of latency in real-time voice agents and the engineering
  constraints behind responsive spoken interaction.
source: cresta
url: https://cresta.com/blog/engineering-for-real-time-voice-agent-latency
author: Daniel Hoske
published: '2025-10-21'
fetched: '2026-07-11T03:58:00Z'
classifier: codex
taxonomy_rev: 1
words: 1590
content_sha256: 579dc33c63fde17eabe2fa6842d0df9e839fff4bafd9e33319779ef2eb4faa58
---

# Engineering for Real-Time Voice Agent Latency

At Cresta we are building some of the world’s[ most human-like voice AI agents for big enterprises, such as Brinks Home](https://cresta.com/ai-agent). One core challenge in achieving a natural, lifelike experience through voice agents is minimizing latency, the delay between when a caller stops speaking and the AI agent responds.

Even pauses as short as ~300 milliseconds can feel unnatural, while any latency beyond ~1.5 second can rapidly degrade the experience. Achieving sub-second responsiveness requires deep optimizations across the entire system, from telephony and networking to speech recognition (ASR), large language models (LLMs), and text-to-speech (TTS).

How to architect voice agents has been well-described in primers like[ https://voiceaiandvoiceagents.com/#latency](https://voiceaiandvoiceagents.com/#latency). This article explores some of the less obvious engineering techniques Cresta has implemented in real production deployments to reduce latency and deliver more seamless, human-like voice interactions.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/69f9bcc01546b1d74ee24f3c_68f7c922b56deb48fd4531a1_image%2520(21).png)

## Measuring Latency Effectively

Latency optimization starts with accurate measurement. Each system component—ASR, LLM, and TTS—contributes its own delay. To measure real-life performance, engineering teams should not only monitor per-component latency (for example, first-token latency for LLMs, first-byte latency for TTS) but also run end-to-end tests that simulate real calls and record true user experience.

Ideally these tests should:

- Make a simulated call using your telephony / WebRTC media path to the AI agent,
- Store a recording from the caller side, and
- Determine the latency distribution in the recording with an ASR model that has reliable word timestamps.

Note: Latency numbers here roughly represent the median. For voice agents you also need to keep the distribution tight. Good median latency isn’t enough.

## Core Components and Latency Considerations

[Voice agents consist of many components and models](https://voiceaiandvoiceagents.com/#latency) wired up in complex ways. The biggest factor that determines the components is whether you stitch together ASR, LLM, and TTS or use a voice-to-voice approach. 

In this article we’ll focus on the stitched approach. We’ve found voice-to-voice models to not yet be controllable enough for enterprise use cases. We’ll explore voice-to-voice in a separate article.

### Telephony

Your agent can’t do anything without audio bytes. Generally you’ll have limited control over the telephony stack if you need to integrate with your customer’s existing contact centers.

If possible, prefer web-based WebRTC connections over traditional telephony. WebRTC can reduce latency by up to 300ms and provides greater control over latency-relevant settings in the caller’s microphone and speaker.

### Networking

Network latency is primarily constrained by the physical location of telephony infrastructure (ideally you use globally distributed WebRTC infra like[ daily](https://daily.co) or[ LiveKit](https://livekit.io/)) and ML inference (ASR, LLM, TTS). 

For calls within a country well-served by LLM providers (like the U.S.), everything can usually happen in-country. However, once you start serving other markets–for example, Australia–you may realize that your inference/LLM provider only supports Europe/US. This has the potential to add an extra ~200ms to ~300ms of round trip latency. In this event, you may need to switch providers or deploy yourself.

Other technical aspects like packet loss (media protocols use UDP) and packet reordering affect latency, but you may have little control over them.

Focus instead on what you can control: details like TCP handshakes and DNS. Reuse connections especially for the LLM, prefer streaming APIs and avoid DNS in the critical path!

### Audio Processing

Audio preprocessing (for example, echo cancellation and denoising) typically adds 25–50ms. Although smaller, these components are cumulative contributors to total latency.

### Speech Recognition (ASR)

Streaming ASR latency depends heavily on whether your recognition model was tuned for low-latency real-time use cases on the accelerators available to you.

As you stream audio to the ASR model in real time, measure latency by comparing what audio prefix a given transcript was based on to how much audio has already been submitted. With sufficiently small chunks (≤50ms), latency can be as low as 200–300ms.

### Turn Detection

A key decision is determining when the customer has stopped speaking and the voice agent should respond.

The simplest approach uses voice-activity-detection (VAD), usually a combination of volume and an ML model (like[ Silero](https://github.com/snakers4/silero-vad)) that detects the presence of human speech, taking into account more than just silence. The agent responds once it hasn’t seen human speech for x ms. Recently we’ve seen some combined ASR + smart turn detection models come out, for example: [https://flux.deepgram.com/](https://flux.deepgram.com/).

Dependent on your setting of x, this approach suffers both from false positives (the agent interrupts but the caller continues speaking) and high latency (the agent waits too long to respond).

In realistic conversations, we’ve found x >= 600ms to be the bare minimum. Even with 600 ms, agents often misjudge pauses during tasks like spelling numbers.

To handle such cases, you need a semantic turn detection model that decides when the customer has finished speaking based on context, either based on audio (can be concurrent with ASR) or based on text (after ASR). In common cases this approach can reduce response times to under 300ms without cutting users off.

Note that with such semantic turn detection models it’s actually desired that the agent responds later in cases like spelling. User experience is better even though measured latency is higher!

Note: Speculative triggering—starting the LLM call before the user fully stops speaking—can reduce perceived delay, but must be managed carefully to avoid premature API calls or unnecessary costs.

In fact, you *could* call the LLM while the user is speaking and let the LLM predict what they are going to say. This can give you negative latency. But we haven’t found it to be practical yet.

### Large Language Model (LLM)

For voice AI agents, first-token latency is the most critical metric. Dependent on the model, this can range from 250ms (for smaller local models) to over one second (for larger third-party models). Always measure first-token latency independently, as many LLM providers don’t report it.

Reasoning models generally can’t be used within the live response loop. They are too slow! However, there are some approaches where the main response can be created by a smaller model or even use a canned phrase while the model reasons in the background.

Your choice of LLM needs to be based on evaluations and on what quality / latency tradeoff works for your business. For example, we’ve seen the first-token latency of the GPT family increase from gpt-4o through gpt-4.1 to gpt-5 (with ”minimal” reasoning effort). Always choosing the newest model isn’t a no-brainer.

Advanced techniques like hedging (launching multiple LLM calls in parallel and using whichever returns first) can decrease long-tail latency and improve reliability. You could also use the hedging mechanism for failover to a different LLM.

### Text-to-Speech (TTS)

TTS can typically begin once the first few LLM tokens are available, though most providers require at least a full sentence to get good TTS results. Thus, for TTS the first-byte latency is what you most need to worry about. Similar to LLMs, there is a huge quality/latency tradeoff with common TTS models, ranging from 100-500 ms time-to-first-byte.


Quality includes both subjective “vibe” (does the voice sound good?) and more objective metrics (can TTS reliably speak numbers, does it pronounce customer-specific terms correctly?).  Additionally, our customers all want very different custom voices which excludes some TTS providers with less customizability.

### Guardrails

In production deployments, you always need input guardrails that can detect potentially troublesome caller behavior. For example, if a customer is asking for financial advice from a support agent, the agent should refuse to give such advice.

Cresta models these as concurrent calls to LLMs and smaller classifiers that run alongside the main LLM call. This enables the agent to interrupt the main response if a guardrail triggers, without introducing significant delay. Provided the guardrail call rarely takes longer than the main LLM, we’ve found it to be a good tradeoff not to wait for guardrail calls to complete before responding.

## Real-world Latency

In the real world, agents need to call out to external systems to look up information or complete transactions via LLM-triggered tool calls or deterministic code.

That is, voice AI agents are dependent on external systems with unpredictable latency. This requires planning for various possible scenarios:

- If API call latency is long but not too long (say, <1s normally but outliers up to 10s), the agent should return one or more wait messages once the API call exceeds latency thresholds (”I’m looking up … for you”).
- Extremely long or unpredictable calls (>10s) should run asynchronously, though this complicates the customer experience. For example, what can the caller do while the workflow is running, and how should the agent behave once the workflow has finished?
- If you are using a tool call to look up information before the LLM can compose any meaningful (even wait) message, the 1 LLM first-token latency becomes 1 LLM latency + 1 LLM first-token latency.
- If you know when to make an API call in advance–for example, you always need to look up customer information when the call starts–make the call concurrently at the start.

Note: External calls have issues beyond latency. For example, if your customer can’t make the API idempotent or it has heavy concurrency restrictions, you may need to disallow user interruptions while the API call is running.

## Conclusion

Achieving natural, human-like responsiveness in enterprise voice AI requires optimization at every layer of the stack. Each millisecond counts, and thoughtful engineering around measurement, concurrency, and tradeoffs is essential.

Cresta continues to refine these systems to push the boundaries of real-time AI conversation.

If solving these types of challenges excites you, please explore opportunities at[ cresta.com/careers](https://cresta.com/careers).
