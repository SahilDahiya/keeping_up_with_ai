---
title: Building more human voice experiences
topic: models
subtopic: multimodal
secondary_topics:
- product-engineering/ux-patterns
summary: Explains design and engineering considerations for more human voice-agent
  experiences, including timing, emotion, and conversational flow.
source: sierra
url: https://sierra.ai/blog/building-more-human-voice-experiences
author: Zack Reneau-Wedeen
published: '2026-05-12'
fetched: '2026-07-11T03:53:14Z'
classifier: codex
taxonomy_rev: 1
words: 898
content_sha256: 5ae9d89ba9174bdc53db4b13576060bad71191156e32ab8b1aa3493492581821
---

# Building more human voice experiences

# Building more human voice experiences

Voice is the easiest, fastest, and most natural way for people to communicate. And yet most brands make it difficult for their customers to talk to them, because talking is expensive—handling a phone call can cost between $10 and $20. So businesses lean on “self-service” solutions, which push the hard work onto customers and are clunky at best, ineffective at worst.

Companies building on Sierra are solving this age-old tension between the cost and quality of customer experiences, and voice is a key part of the puzzle. Since launching [seven months ago](https://sierra.ai/blog/sierra-speaks), businesses can now provide 24/7 voice support using AI agents built on our platform. No wait times. No transfers. No callbacks. And if AI can’t solve the problem—it usually can—you get a seamless handoff to a live agent with no need to repeat the same information all over again.

Here are three lessons we’ve learned building great voice experiences with our customers, for their customers. And what’s so interesting is that it’s many little things like these—not one big thing—that’s helped create a better, more human voice experience.

## Separate signal from noise

In the real world, phone calls are full of music, crying babies, side conversations, and other unmentionables. At launch, we took pride in the fact that agents built on Sierra were hyper-responsive to interruptions because one of the most annoying things about traditional IVRs (“press 1 for hours of operation, press 2 to make a payment, press 3 to repeat these options—I’m sorry, I didn’t catch that”) is when they talk over you.

But digging into the data across millions of conversations, we noticed that what the agent interpreted as “interruptions”—its cue to stop talking—was occasionally just background noise: someone walking down a busy street, a TV playing in the background, or even a person telling their dog to stop barking (been there). Agents shouldn’t assume all speech is relevant; they should think about what they’re hearing, like humans.

Our solutions had to be as varied as these examples. To distinguish speech from other sounds, we built a proprietary Voice Activity Detection (VAD) system that outperforms all other models we’re aware of today. We invested heavily in noise reduction, multi-speaker detection, and contextual analysis, which are able to differentiate between interruptions (“wait no not that”), agreement (“okay yup”), and side conversations (“honey, I’m going to pick up the kids”). The result is agents that are adept at accounting for all of these scenarios in real-time.

## Walk and chew gum

To feel human, agents must be able to multi-task. This is especially important for voice, which is such a quick, fluid form of communication. For an AI agent, this means the ability to simultaneously:

- **Think and listen**, so the agent can get ahead. If asked “Can you help me book a hair appointment for my daughter?”, an agent built on Sierra can start pulling up salon options (i.e. calling different APIs) before the customer has even finished their sentence—making it feel smart and responsive.
- **Listen and talk**, so the agent can handle interruptions. If an agent is walking through technical troubleshooting steps and the person interjects—“I already tried that” or “oh wait it’s working now!”—the agent can adapt on the fly so the conversation doesn’t feel robotic. On the other hand, if a person simply chimes in with “okay yup, got it,” it’s likely not an interruption and the agent should continue to respond (but with that affirmation in mind).
- **Talk and think**, so the agent can show progress. If asked “do you have those shoes in a size 9?” an agent built on Sierra might say “let me check if size 9 is available… Sadly we don’t have those, but what about this other similar style?” This prevents dead air while the agent is looking up information in internal systems, which would otherwise be awkward, confusing, and frustrating.
- **Reflect in real-time**, so the agent can be greater than the sum of its parts. For example, even state-of-the-art speech recognition models make mistakes, and one example we’ve seen with banking customers is the confusion of “I want to check my balance” with “I want a chicken salad.” So agents need to ask whether what they think they’ve heard actually makes sense, and correct errors based on context clues.

![Diagram of turn-based systems versus Sierra agents](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Fdefdd6fe3b7eb6a7f7db9a318091961d1620b60f-4320x2160.png&width=3840&quality=75)

## Shorter isn’t (always) sweeter

Unlike traditional rules-based software, AI agents can think and reason, so they’re best able to solve problems when they have more context. This is especially true for voice, where meaning often depends on what was said previously, and where people naturally gravitate toward more detail. If someone mentions that their TV remote isn’t working, they’ll probably provide more details in a voice conversation (“ever since I spilled water on it”) than over chat.

This “more is more” approach is very different for consumers used to retrieval-based systems like search, where sentence fragments and keywords have traditionally been considered best practice. We’ve learned from a design perspective that when agents give more detailed responses, people pick up the cue and share more context in return. But there’s a tradeoff between richness and efficiency, which is why conversation design and experimentation are so important.

If you are excited to work on voice technology, please [reach out](https://sierra.ai/careers). We’re hiring and would love to hear from you.
