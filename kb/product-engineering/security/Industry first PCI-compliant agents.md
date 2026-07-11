---
title: 'Industry first: PCI-compliant agents'
topic: product-engineering
subtopic: security
secondary_topics:
- agents/tool-use
summary: Explains PCI-compliant payment workflows for agents, focusing on secure action-taking
  and sensitive-data handling.
source: sierra
url: https://sierra.ai/blog/payments
author: Maya Hope
published: '2026-05-12'
fetched: '2026-07-11T03:51:07Z'
classifier: codex
taxonomy_rev: 1
words: 1006
content_sha256: e977589e89cf00dce1faa49d7d7814491503515a26c94a0f17dfdca334be8aa5
---

# Industry first: PCI-compliant agents

# An industry first: Sierra launches fully PCI-compliant payments

Payments are critical for any business — whether a customer is looking to book a hotel, pay a bill, upgrade a subscription, or set up a payment plan. Getting these moments right impacts revenue and brand loyalty. AI agents handle most conversations well, but the moment money changes hands the experience typically reverts to “please hold” or “I’ll need to transfer you”. That changed today, when Sierra became the first Level 1 PCI-compliant conversational AI platform.

## The challenge of PCI DSS when working with agents

Any company that accepts payments is required to comply with PCI DSS (Payment Card Industry Data Security Standard) — the global standard for handling cardholder data. This requires strict controls, including third-party audits, tightly scoped data access, and rigorous security testing.

Today’s agents and their supporting infrastructure aren't designed to meet these requirements out of the box. They often log conversations, retain information, and pass data between the model, orchestration layer, external tools, and logging systems — all of which make it hard to control, isolate, and audit sensitive payment information.

That’s why the agent hands the customer over to an IVR or external link to collect a payment. So what should take 30 seconds turns into a transferred call, hold music, and a request to repeat your information all over again.

## The solution: from conversation to completed transaction in one experience

Today, Sierra is introducing the first Level 1 PCI-compliant payment capability for AI agents. It works across chat and voice, and is verified by the [Visa Global Service Provider Registry](https://visa.com/onthelist). So any business using Sierra can:

- Collect card and ACH payments securely, directly in the conversation;
- Confirm the payment was successful in real time, with receipts sent to the customer before the conversation ends; and
- Integrate with their existing payment processors—without the need to change providers, replace systems, or rebuild their payment infrastructure.

## How it works

When a customer wants to make a purchase or leave payment details on file, the agent switches to a secure transaction flow which removes the agent while the processor completes the payment. From the customer’s perspective, nothing changes — it’s one fast, consistent experience with no interruptions.

Customers provide card or ACH details through secure and compliant infrastructure — keypad input for voice, secure embedded forms for chat. That data routes directly to the payment processor or gateway used by the business. The agent never sees raw card information and only receives non-sensitive data like payment status and last four digits.

Within seconds, the agent returns to confirm the payment and wrap up the interaction. No IVR. No extra steps.

![A two-panel chatbot interface showing an AI agent assisting a user with healthcare bill payment, including identity verification and a successful $99.99 transaction.](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F0456d8f55c23e6684d0ffe5737c3212e28e4d93a-4528x2586.png&width=3840&quality=75)

## Secure and compliant, from the ground up

Our system clearly separates sensitive card data from the rest of the experience, so businesses always know where it’s handled and where it isn’t.

![A flow diagram showing a customer making a payment through a Sierra AI voice agent, which securely processes cardholder data with a payment API and provides transaction status.](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Fa10667878d87000a954a16a7bf369ef63a59bf12-2000x1126.png&width=3840&quality=75)

## What that means in practice:

- **Cardholder data (CHD) isolation by architecture.**It flows through dedicated PCI-certified infrastructure and never touches Sierra's core platform.
- **LLMs don’t touch sensitive data.**During secure payment mode, prompts follow a predetermined, server-validated sequence—not LLM-generated.
- **Audit-ready compliance.**Full Attestation of Compliance (AOC) and Shared Responsibility Matrix available via the Sierra Trust Center.
- **Agent separated by design.**When a customer enters a card number on their keypad, that information is captured and protected by a separate, secure layer. The AI agent handling the conversation cannot access, intercept, or pass along that data.

## Easy to integrate

Payments plug into existing payment systems through a standard integration. Enterprises can simply add AI-native payment experiences on top of what already exists.

## Proven at scale

Leading businesses are completing thousands of payments daily while delivering fast, personalized experiences through their agents.

SiriusXM handles many daily inbound payment calls—and customers needing to update payment information or pay a balance can now resolve the issue at any time of day.

“PCI compliance is non-negotiable for us, but so is delivering a seamless customer experience. SiriusXM listeners call every day to update their payment information or pay a balance. With Sierra’s secure voice payment flow, customers can resolve payment needs easily—without requiring a live agent or a frustrating IVR experience—while meeting the strict PCI compliance standards our business demands.”

![A smiling man with a beard and dark hair, wearing a blue shirt, dark sweater, and grey blazer.](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2Fc47b0519629bf40f781f8d675a88ad037587ec8d-2455x2150.jpg&width=3840&quality=75)

Wayne Thorsen

COO

This capability extends to all cases of handling PCI data, not just those that involve authorizing a payment. A financial services company automated card activation over voice, enabling customers to securely activate their cards in seconds while meeting PCI requirements. The solution limited the need for a handoff to a separate PCI-compliant phone IVR and achieved an 85% resolution rate.

## The full payment journey, in the conversation

Sierra Payments supports the complete range of enterprise payment workflows:

- Authentication and identity verification—confirming a customer's identity before activating a replacement credit card
- Card capture and ACH payments—securely process a utility bill payment for a customer and set up automatic payments from their bank account
- Payment plan setup and installment agreements—offering a patient the option to split a $300 medical bill into three monthly payments instead of paying all at once
- Alerts and balance management—flagging an upcoming subscription payment and updating the card on file before an account goes inactive
- Confirmation and real-time receipts—instantly sending a receipt when a customer upgrades their flight seat

Upgrading a subscription, booking a trip or paying a bill shouldn’t be slow or frustrating. When the payment experience is fast and easy, customers hang up feeling good about the brand.

That's what Sierra is built for, creating better customer experiences that leave customers feeling heard, helped, and valued.
