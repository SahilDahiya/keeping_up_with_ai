---
title: Evaluating and Monitoring Voice AI Agents
topic: models
subtopic: multimodal
secondary_topics:
- evals-observability/evaluation
- agents/planning
summary: Covers evaluation and monitoring for voice AI agents, including speech-specific
  quality signals and agent behavior beyond text-only evals.
source: langfuse
url: https://langfuse.com/blog/2025-01-22-evaluating-voice-ai-agents
author: null
published: '2025-01-22'
fetched: '2026-07-11T04:35:01Z'
classifier: codex
taxonomy_rev: 1
words: 563
content_sha256: 5d52b5813fbd6d144156995095c6a405d03690c87eae35d7329cbc125ae86c9d
---

# Evaluating and Monitoring Voice AI Agents

# A Guide to Evaluating Voice AI Agents

A comprehensive guide to production and development evaluation of Voice AI applications based on a conversation with Brooke Hopkins from Coval.

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc Klingen

Marc KlingenAs Voice AI applications continue to advance, developers are met with complex challenges in testing, evaluating, and monitoring their voice agents.

In this blog post, we'll explore how you can create more robust and reliable voice applications. We'll draw insights from setups we have seen from our users at [Langfuse](https://langfuse.com/) and the recent discussion ([full video](https://www.youtube.com/watch?v=hPrPqry1yQQ)) between me and Brooke (Co-Founder of [Coval](https://www.coval.dev/)) to provide a comprehensive guide on Voice AI evaluation.

[The Evolution of Voice AI Testing](https://langfuse.com#the-evolution-of-voice-ai-testing)

Voice AI applications present complexities that extend beyond traditional LLM implementations. In addition to [challenges](https://langfuse.com/faq/all/llm-observability) caused by the non-deterministic nature of language models, developers must also handle:

- Audio Quality and Metrics
- User Interruptions
- Speech-to-Text (STT) Accuracy
- Text-to-Speech (TTS) Output Quality
- Real-Time Streaming Interactions

As voice applications mature, the need for both high-level integration testing and detailed component evaluation becomes critical.

[Understanding the Voice AI Testing Pyramid](https://langfuse.com#understanding-the-voice-ai-testing-pyramid)

Developing effective voice applications requires a dual approach to evaluation strategies:

- **Online Evaluation:**Focuses on real-time production monitoring, performance tracking, and analyzing user interactions.
- **Offline Evaluation:**Involves development testing, ranging from end-to-end agent testing to granular unit tests and validating conversation flows.

Using this testing pyramid is essential for effective Voice AI testing, ensuring your voice agents perform optimally in live environments.

[Evaluations of Single Messages vs. Conversation Level](https://langfuse.com#evaluations-of-single-messages-vs-conversation-level)

The second duality we see in voice agent evaluation is between observing and evaluating single messages and evals on the whole conversation.

**Single turn evaluations:**

- [Trace](https://langfuse.com/docs/tracing)the step-by-step execution of a single message
- Monitor the tool calls and other application logic used by the voice agent
- Stream-based interaction analysis

**Multi turn evaluations:**

- Performing end-to-end simulation testing on the whole conversation
- Testing for regressions caused by different prompt versions or model changes
- Classifying and detecting anomalies in the conversation flow

[Integration Best Practices and Development Workflow](https://langfuse.com#integration-best-practices-and-development-workflow)

Usually, there are two phases in the voice agent development workflow:

**Early development stages:**

- Quick integration tests and online evaluations
- Trace and debug individual components of the conversation

**Application running in production:**

- Implement specific unit tests for cases spotted in development
- Detailed performance monitoring and conversation level evaluations
- Ongoing regression testing

The type of evaluation also depends on the type of the voice application. Some applications might require a closer monitoring of model costs whereas other might focus on the conversation flow and the accuracy of tool calls:

**Transactional Voice Applications (e.g., Appointment Scheduling):**

- Trace individual function calls and apply evaluations to single messages.
- Perform end-to-end testing of complete user journeys.

**Complex Applications (e.g., Virtual Assistants):**

- Focus on conversation-level testing and monitor conversation arcs.
- Monitor tool calls and application logic.

We are excited that [Coval](https://www.coval.dev/) will natively integrate
with Langfuse. With this integration, Langfuse users can use Coval to perform
end-to-end simulation testing on the whole conversation of their voice agents.
Reach out if you are interested to try it.

[Resources](https://langfuse.com#resources)

- Watch the full discussion with Brooke Hopkins and Marc Klingen [here](https://www.youtube.com/watch?v=hPrPqry1yQQ).
- Learn more about Langfuse:
- [Tracing](https://langfuse.com/docs/tracing)LLM applications
- [LLM Observability Challenges](https://langfuse.com/faq/all/llm-observability)
- Tracking [model Usage and Cost](https://langfuse.com/docs/model-usage-and-cost)
- Performing [LLM-as-a-Judge Evaluations](https://langfuse.com/docs/scores/model-based-evals)

- Check out the [Coval docs](https://docs.coval.dev/getting_started/welcome).
