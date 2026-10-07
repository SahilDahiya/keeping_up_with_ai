---
title: TypeSafe AI scales Jev to trillions of tokens in three days on Modal | Modal
  Blog
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/typesafeai-case-study
author: null
published: '2026-10-05'
fetched: '2026-10-07T06:10:08Z'
classifier: null
taxonomy_rev: 2
words: 553
content_sha256: e27c8e8e58c33f5b40b3ff96b05c6cb9b04d066183f12b6ec60c46534450fd60
---

# TypeSafe AI scales Jev to trillions of tokens in three days on Modal | Modal Blog

[TypeSafe AI](http://typesafe.ai)’s manifesto is contrarian for an AI lab: “Build Prod, Not God.” Their first model, Jev, delivers fast, structured decisions with frontier intelligence. In the course of a launch week, demand for Jev went stratospheric.

Modal helped TypeSafe train and deploy a new class of frontier model, then scale to over one trillion tokens in three days while meeting their requirements for ultra-low-latency inference without managing their own infrastructure.

## A new class of frontier model

Jev isn’t a large language model. It’s a **System One Model**–as in fast, intuitive thinking. Jev achieves similar levels of intelligence on System One tasks when [compared to frontier LLMs](https://evals.typesafe.ai/), but focuses on decisions rather than generalized intelligence.

To bring Jev to life, TypeSafe built a [custom stack entirely focused on automation](https://typesafe.ai/blog/introducing-system-one-models-and-jev): with a new model architecture, parallel sampler for maximum efficiency, and training method they call Reinforcement Learning for Calibrated Decisions (RLCD).

Unlike LLMs, Jev isn’t autoregressive and it doesn’t generate text. Instead, it takes state and questions as input, and outputs typed, structured values with probabilities. For example, take a customer support ticket as input:

```
{
  "state": "Hi, I've been trying to connect my Stripe account for 3 days and the integration keeps failing. Please help ASAP.",
  "model": "jev-latest",
  "questions": {
    "department": {
      "type": "choice",
      "instructions": "Which team should handle this?",
      "criteria": {
        "billing": "Payment or subscription issues",
        "technical": "Bugs or integration problems",
        "sales": "Pricing or account questions"
      }
    }
  }
}
```
The user defines the `choice` primitive, which directs Jev to choose an option from a list. Given the options `sales`, `technical`, or `billing` , Jev returns outputs and probabilities:

```
{
  "model": "jev-1.13.0",
  "answers": {
    "department": {
      "type": "choice",
      "choice": "technical",
      "confidence": 0.78,
      "probabilities": {
        "technical": 0.85,
        "sales": 0.0,
        "billing": 0.15
      }
    }
  }
}
```
Jev doesn’t generate outputs sequentially, but in parallel–producing intelligent, low-latency responses suitable for workloads like large-scale automation, fast browser use, and generative user interfaces.

## Scaling exponentially over a weekend

Jev launched publicly on a Thursday. One week later, it topped the leaderboard on OpenRouter for contexts between 1K-10K tokens, handling 15.1% of requests. This is just a slice of the demand being handled by the TypeSafe team, which they now measure “in the trillions” of tokens.

![Jev OpenRouter share.](https://modal-cdn.com/blog/images/jev_or.webp) 

To scale their systems while serving Jev at the price-performance frontier, the TypeSafe team needed full control of their stack–from networking and routing to autoscaling for unpredictable load. Most importantly, they needed that control without the headache of managing their own infrastructure.

After all, inference is a (very) big thing, but it’s not everything.

## Building on Modal

Modal’s infrastructure is uniquely suited for model launches like Jev: bursty, high-concurrency workloads where every millisecond counts. Instead of guessing at capacity needs or overpaying for a compute reservation, AI labs can use Modal’s serverless platform to train, serve, and scale any type of model: LLMs, System One Models, world models, and more.

“Modal served 1 trillion tokens for Jev within three days of launch. Their team was proactive and responsive as we scaled to meet unprecedented demand, and we could stay focused on shipping instead of managing infrastructure.”

Jev's launch is one example of what the Modal platform was built for. Bring any model, any serving code, and scale to trillions of tokens per day.
