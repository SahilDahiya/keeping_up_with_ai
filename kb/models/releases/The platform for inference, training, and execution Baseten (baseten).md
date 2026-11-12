---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: models
subtopic: releases
secondary_topics:
- product-engineering/architecture
summary: Introduces mammoth-1 (27B) and elephant-1 (9B), decision models post-trained
  from Qwen3.5 that output a probability distribution over choice/score/boolean answers
  instead of generating text, enabling cheaper classification with confidence-based
  escalation thresholds.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1
author: Max Kirkby
published: '2026-10-21'
fetched: '2026-11-12T06:09:00Z'
classifier: claude
taxonomy_rev: 2
words: 776
content_sha256: 32141d9b83d7203682613f0548f99d3762b9bfb6df641240a8942dff2e8f565a
---

# The platform for inference, training, and execution | Baseten

AI models
# The top ranked decision models in the world: mammoth-1 and elephant-1

mammoth-1 and elephant-1 are decision models trained by our internal research team, Base Labs. They are open-source and free to try for a week.


- Authors
- Date
- October 21, 2026

We’re proud to release two of the world’s best decision models, trained by our own research lab: [mammoth-1](https://www.baseten.co/library/mammoth-1/) (27B) and [elephant-1](https://www.baseten.co/library/elephant-1/) (9B)!

mammoth-1 ranks #1 out of 208 decision models, and elephant-1 is the leading 9B decision model on the Jev Decision Index. Both models are [open-source](https://huggingface.co/baselabs) and free to try for a week on Baseten Model APIs, with zero data retention (ZDR) by default.

Since TypeSafe introduced Jev and the System One API, decision models have emerged as a new category. We post-trained Qwen3.5-9B and Qwen3.5-27B to build two of the best. Here’s a closer look at their capabilities, use cases, and how to evaluate them for your stack.

Unlike generative LLMs, decision models don’t generate text. Instead, they return a probability distribution (a score for every possible answer, with all scores summing to 1) over the possible answers to each question.

You can ask decision models 3 types of questions:

- **Choice**: pick an option from a list (e.g., which team owns this ticket: infrastructure, billing, security, or support?)
- **Score:** rate the input on a given scale (a 2 point scale would be low vs high). For example, how urgent is this ticket, low or high?
- **Boolean**: answer yes or no (e.g., is this email a phishing attempt?)

Using generative LLMs for classification tasks, like routing a ticket or flagging spam, is costly and slow because the amount of computation they perform is overkill for the required output of the task. The response alone also doesn’t provide a reliable measure of certainty.

Decision models like elephant-1 and mammoth-1 skip text generation, which makes it cheaper and faster to serve in production. Customizable confidence thresholds help determine when to accept an answer and when to escalate it. For example, a support ticket can be routed automatically when the model is 90% confident, and sent to a person when confidence is lower. The models can also be post-trained so their confidence better reflects how often they’re right.

In short, decision models are built to understand the request and make a decision without spending time writing a response. Compared to a reasoning model, a decision model may give up to a 10x speed up.

Here are a few use cases:

- Ticket triage and routing
- Spam and phishing detection
- Prompt guardrails and jailbreak detection
- Routing requests between small and frontier LLMs

We built elephant-1 and mammoth-1 to be generalist decision models that could handle a broad range of tasks, from routing support tickets to checking requests for safety. We trained and evaluated decision-making using data from five domains, mirroring previous work: knowledge and reasoning, language, tools and automation, retrieval and classification, and arts and human taste.

mammoth-1 ranks #1 on the Jev Decision Index 0.4, while elephant-1 is tied for #8 overall and is the leading 9B decision model. On the separate Artificial Analysis Decision Index, elephant-1 is tied for #1 with the previous best model, d1-ultra.

mammoth is a better fit if your task needs more general knowledge. If you mainly need quick reasoning, then choose elephant-1.

We fine-tuned Qwen3.5-9B and Qwen3.5-27B on 6.21 million decision-making examples. To train each model, we used a dataset that combined public datasets with synthetically generated examples covering core decision skills, safety and abstention, and judging and expert domains. We refined the data through repeated training and evaluation runs with elephant-1, then used the final mix to train both models. This included examples that taught it when to answer “I don’t know,” when the model was uncertain about the accuracy of its answer. Read more about how we trained it in our technical report [here](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models).

elephant-1 and mammoth-1 are part of a growing set of decision models. To choose the right decision model for your workflow, we recommend you evaluate:

- Accuracy: Does it make the right decisions? Include difficult cases.
- Confidence: Does it know when it’s unsure? Check when to accept an answer and when to escalate, and set your confidence threshold accordingly.
- Speed and cost: Measure latency and cost per decision at your expected traffic level. Include retries and fallbacks.

You can try [elephant-1](https://www.baseten.co/library/elephant-1/) and [mammoth-1](https://www.baseten.co/library/mammoth-1/) for free for a week through Baseten Model APIs. Both models are also open-source on [Hugging Face](https://huggingface.co/baselabs). You can read the technical report from our research lab, Base Labs, [here](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models). We look forward to seeing how you use them!
