---
title: Defense in depth in the age of agents
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: sierra
url: https://sierra.ai/blog/defense-in-depth-in-the-age-of-agents
author: George Davis
published: '2026-08-13'
fetched: '2026-08-14T06:27:53Z'
classifier: null
taxonomy_rev: 2
words: 903
content_sha256: 1c9f237f5e75ca7233e521d39c153c48ee33dca018e43d787ec70afbcf41d68f
---

# Defense in depth in the age of agents

# Defense in depth in the age of agents

In Neil’s post on [context engineering](https://sierra.ai/blog/context-engineering-the-key-to-great-agents), he discussed the difference between flow-based agents and agents built on goals and guardrails. The former follow a predefined path, like a decision tree, flow chart or standard operating procedure. While customers can speak naturally, the system still operates on “if this, then that.”

At Sierra, we build agents using goals and guardrails so they can think and reason independently, whether originating a mortgage, disputing a charge, or helping select the right pair of skis. That freedom is what makes them so powerful — and the guardrails they are given so important. Because when an agent is no longer following a predefined path, you need a new way to ensure it stays within the boundaries set by your business.

![Photo of a man on a phone, asking for phone eligibility - plus two images of the agent guardrails that go into this request](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Fad33cd1f18188aae5a3bd389237c34dcc478251c-1920x808.png&width=3840&quality=75)

## A new take on an old security principle

The basic idea of defense in depth — that you need layers — is the same, but agents change what those layers do. Some protections may be hard coded, like never exposing a customer’s full payment details. Others require context and judgment, such as: Will the insurance cover this? Can I get a refund? Or, I want to report fraud on my account. What an agent can and can’t say is also specific to your business. One retail agent might be free to comment on a competitor’s offering, while for another, that might be an immediate brand risk.

The other challenge is that the threats these guardrails are designed to protect against constantly evolve. A “customer” might hide encoded instructions inside a message, role play as the agent’s supervisor to change a policy, or use a prompt injection to trick the agent into doing something it should not do. Other threats involve bad content that should never appear in a conversation, regardless of who introduced it. Increasingly these categories blur, with skilled adversaries combining techniques.

It’s for all these reasons that you need AI to guard AI.

## The solution to AI problems is more AI

Inside Sierra, every customer message passes through several layers before the agent responds:

- **Content:** The customer’s knowledge — the help center articles, product documentation, and policies — that the agent retrieves and grounds its responses in.
- **Rules and policies:** Natural-language instructions the agent must follow, expressed in plain English (“never compare our products to a competitor’s by name”).
- **Supervisors:** Separate models that audit the conversation in real time, blocking, rewriting, or nudging the agent when content or behavior crosses the line.
- **Deterministic guards:** Non-model checks that can’t be talked out of doing their job — like preventing account-modification tools from even being available to the agent until the customer has been authenticated.

![A triangle with four segments, outlining Sierra's multilayered approach](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F1f00c31257c53556e60a17b2aacf1c942191a92f-4320x2520.png&width=3840&quality=75)

A single message can trigger half a dozen of these checks before any reply goes back. A supervisor agent screens the input. The agent draws on the relevant content and applies the relevant policies. Another supervisor reviews the proposed response. A deterministic guard scans the output for sensitive data. Only then does the customer see a reply.

Layering matters because each layer addresses a different kind of risk and has its own failure mode. Content grounds the agent in trusted knowledge, but the same retrieval pipeline can also pull in instructions someone planted inside it. Rules and policies live in the same prompt as customer input, where a sufficiently insistent message can compete for the model’s attention. Supervisors catch nuance that fixed rules can’t, but as agents themselves they share some of the limitations they’re built to detect. Deterministic guards enforce the absolutes that can’t be left to model judgment, but only fire on what’s been explicitly defined.

The strength of the system is the layers covering each other: Together they’re robust to a much wider range of pressure than any single technique could be on its own.

## Beyond the runtime

Runtime guardrails are necessary but not sufficient. Two practices sit alongside them.

- **Continuous evaluation:** New attacks emerge constantly, so an agent that was robust last quarter isn’t automatically robust today. Sierra works with trusted third parties to run regular adversarial assessments and red-team evaluations — millions of attempts in aggregate — with the findings feeding back into the platform.
- **Continuous monitoring:** Even with strong guardrails, individual conversations can stray, and adversaries probe constantly for new openings. Sierra analyzes live traffic at two levels.
  - Across the platform, Threat Detection watches for patterns that suggest abuse, regression, or emerging attack techniques. Within an individual agent, Agent Monitors catch behavior that might have slipped through the runtime checks — anything that warrants review against the business’s specific policies and expectations.
  - Before changes ship, Simulations let teams stress-test their agents in advance, surfacing regressions in guardrail behavior before any customer sees them.

![Diagram outlining the life of a message](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Fede0317eaabef41bdf724bcf4e45980ce908c052-4320x2520.png&width=3840&quality=75)

## As AI gets smarter, so must the systems that protect it

As models become more capable, agents will take on more responsibility, encounter situations you didn’t anticipate, and need to make even more decisions you can’t prescribe in advance. Keeping them within bounds without putting them back on predefined “if this, then that” paths will require defense in depth to evolve with them.
