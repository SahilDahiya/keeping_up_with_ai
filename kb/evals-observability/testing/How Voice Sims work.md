---
title: How Voice Sims work
topic: evals-observability
subtopic: testing
secondary_topics:
- models/multimodal
summary: Explains how voice simulations test agents before production by generating
  realistic spoken interactions and edge cases.
source: sierra
url: https://sierra.ai/blog/how-voice-sims-work
author: Kumar Pandya
published: '2026-05-12'
fetched: '2026-07-11T03:52:42Z'
classifier: codex
taxonomy_rev: 1
words: 662
content_sha256: 7e9b61ac2f35bceccad7780cfa3e10dfb8ed2d42000d49aa461fadbda1399b54
---

# How Voice Sims work

# How Voice Sims work

[Voice Sims](https://sierra.ai/blog/voice-sims-test-agents-in-real-world-conditions-before-they-talk-to-your-customers) enable companies to put AI agents through their paces — thousands of practice runs — before they ever speak to a real customer. This is how we engineered Voice Sims.

## Dual loop architecture

At the heart of Voice Sims are two moving parts working in sync:

- **The simulated call loop**, which acts like a real person would on the phone.
- **The voice loop**, which powers the agent, makes sure it listens, pauses, and responds naturally.

The two loops send chunks of audio back and forth in a repeatable process, allowing you to rerun the same conversation to find and fix problems. In parallel, an LLM acts as a judge, evaluating the conversation against defined success criteria to determine whether the agent succeeded or failed.

![Dual loop architecture diagram](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Ff8d961357b3485dcd4ad68d78b398426d07fc93a-4320x2520.png&width=3840&quality=75)

## The simulated call loop (mock customer)

Every simulation begins with a persona — defined by a goal, mood, language, and patience level. Sometimes they’re calm and easygoing; other times frustrated, confused, or impatient. These personas are converted into speech using synthetic voices and then “muddied” with background noise to make them feel real. And if you need keypad input, the system even plays the same touch-tone beeps (DTMF) you’d hear when pressing the numbers on your phone.

The result: the agent isn’t talking to a perfect transcript, it’s dealing with something that feels like an actual human on the line.

## The voice loop (the agent)

On the other end is our voice loop — the engine that powers the agent. It listens (i.e. takes in streaming inputs), understands (i.e. turns speech into text and routes it through the agent); and it speaks (i.e. generates a natural-sounding response back into audio). All in real time.

Because real conversations are messy, the voice loop also manages timing. If the mock customer interrupts, the agent pauses, emits a progress indicator if it needs additional time, then responds once it’s ready. Silence, interruptions and overlapping speech are all tracked, so you can test not just what the agent says, but when.

It also enforces good habits. For example, reading complex information slowly and clearly, avoiding reading URLs out loud, or falling back on the keypad when needed.

## One conversation, two loops

Here’s how a simulated call unfolds:

- Using our mock user agent, we generate a message per the Simulation guidelines.
- That message is fed in via small chunks of audio to the Sierra voice loop.
- The agent listens, processes the information, and replies out loud.
- That reply becomes the customer’s next input.
- Back and forth until the call finishes — either because the customer achieves what they want (for example, returning a pair of shoes), or the agent fails.

Because the two loops stay in sync on timing — pauses, interruptions, people talking over each other — the call feels like the real thing. And since the whole thing is reproducible, you can replay the same call again and again, making it easier to debug and improve.

## Running simulations in practice

Voice Sims run wherever you build and ship agents.

- In Agent Studio (no code): Replay audio, scrub through waveforms, and see exactly where things broke down.
- Programmatically (via CLI): Bake tests into your CI/CD pipeline so bad code or broken agents don’t get merged into production.

Nor do you have to write every test from scratch. Simulations can be auto-generated using a company’s standard operating procedures, knowledge base, call flows or even past transcripts. That means you can test many different things, without it being a huge manual lift.

## Training for chaos

The best way to prepare agents for the real world is to practice the chaos: background noise, interruptions, and timing glitches.

With Voice Sims, all of that unpredictability becomes part of the training ground — producing agents that are tougher, more reliable, and ready for real customers, before they’re ever on the phone.
