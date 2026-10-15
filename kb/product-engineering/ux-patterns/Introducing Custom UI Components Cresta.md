---
title: Introducing Custom UI Components | Cresta
kind: blog
topic: product-engineering
subtopic: ux-patterns
secondary_topics:
- prompt-engineering/structured-output
summary: Cresta's AI Agent now generates task-specific interactive UI components (calendars,
  seat maps, running-total pickers) from a natural-language spec built in its Conductor
  engine, instead of answering every request with text; component actions are also
  logged as plain text so handoffs to humans or other systems stay intact.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/solving-chats-tl-dr-problem-introducing-custom-ui-components
author: Ping Wu
published: '2026-09-10'
fetched: '2026-10-15T06:10:42Z'
classifier: claude
taxonomy_rev: 2
words: 999
content_sha256: b1cb053c2d94028625fb0061d5db5e6f14a3de16ea459cb4f926a259eb66c4c7
---

# Introducing Custom UI Components | Cresta

We’ve all been there: asking a chat AI agent why your bill went up, and getting back a paragraph listing every charge and fee in one message. You ask again to make sense of it, and get another paragraph back.

What you wanted wasn’t more text to reread; you wanted to see this month's charges next to last month's, so the difference was obvious without doing the math yourself. The task was about comparing what changed, so the interface needed to show the differences side by side, not describe them via text line by line.

This same principle holds everywhere chat is used to get something done: the interface should match the task, not the other way around. Yet most chat AI agents are configured to answer every request the same way: with text.

Today, we’re introducing **Custom UI Components for Cresta AI Agent**, bringing purpose-built, interactive visuals directly into the flow of the conversation. Instead of forcing every answer into text, the AI agent can surface the interface that best fits what the customer is trying to understand or do.

## The Right Interface For the Task At Hand

Much like a human concierge understands whether to point to a map, show a picture, or hand over the right form, Cresta AI Agent brings in the right visual at the right point in the interaction, making the moment clearer for the customer.

A hotel guest choosing a room swipes through room options with photos, prices, and amenities, or sees nearby properties plotted against the airport or downtown. Rather than trying to convert a dense paragraph of text into a mental picture, the customer sees the answer in its most useful form.


A customer building a phone plan doesn't want a list of add-ons to price out in their head; they want a running total. So the agent shows one: toggle on international calling, data, or a device warranty, and watch the price update with each selection, all before committing to a plan.

This isn’t a redesign of chat. It’s a way for the agent to surface the right interface when text alone isn’t enough.

## A Visual Experience That Still Feels Like Your Brand

Custom UI Components inherit your chat widget’s theme, colors, typography, and shape by default, so a fare comparison, billing summary, or claim tracker feels like a native part of the brand experience your customers have come to expect.

Each component is designed for the task and use case in front of the customer. An airline can create a seat map that reflects its cabin, while a financial institution can offer a payoff tool suited to its products and disclosures. The visual is bespoke, and the experience remains consistent.

## Describe What You Need, and Watch It Take Shape

Building an interactive visual for an agent usually means a new project: a design phase, an engineering queue, a timeline that runs separately from the AI agent itself.

Custom UI Components are built in [Conductor—](https://cresta.com/blog/cresta-conductor-the-agent-for-ai-agent-development)an agentic engine for building, testing, and improving AI agents—using natural language as part of the same workflow used to develop the AI Agent’s prompts and tools.

A builder describes the component along four axes: its goal, how it should look, the data it receives, and the data it returns. From this, Conductor assembles the component, purpose-built for the brand and use case.

The agent and its interfaces share one build flow, giving the team control over the flow of the conversation and the components it calls, tightening the build-test-launch loop. What used to be a time- and resource-intensive process can now take shape in an hour or less. ``


```
Build a custom appointment scheduler for visitors who want to book a healthcare appointment.
Goal:
Let the visitor view available appointment dates and time slots, select one, review their choice, and confirm the booking without typing.
Component behavior:
- Display the soonest available dates first.
- Show available time slots for the selected date.
- Tapping a slot selects it; tapping it again deselects it.
- Nothing is booked until the visitor selects “Confirm appointment.”
- After confirmation, show a success state with the selected provider, date, time, and location.
- If no slots are available, display the next available date and a clear fallback message.
Layout:
Use a calendar at the top and a vertical list of time-slot buttons below it.
Support 1–3 providers and up to 12 time slots per day.
Make the component responsive for mobile and desktop chat-widget widths.
Data inputs:
- Provider name
- Provider specialty
- Appointment type
- Available dates
- Available time slots with time zone
- Location
Data outputs:
When the visitor confirms, return:
- Provider
- Appointment type
- Selected date
- Selected time with time zone
- Location
Use the existing widget branding and accessible UI primitives. Ensure the component has clear loading, empty, error, selected, and confirmed states.
```
## Every Interaction Carries Forward as Text

A component isn't a dead end if the conversation needs to transfer to a human agent or get logged in a downstream system. Every action taken inside one is also captured as plain text: “Customer selected seat 14C.”

If the conversation transfers to a human agent or flows into a CCaaS platform, CRM, or other system of record, the next person or system can see exactly what the customer chose, without needing to render the component itself.

## This Is What Better Experiences **Look Like** 

A wall of text shouldn’t stand between a customer and a confident decision. Every extra clarifying question a customer has to answer is one more opportunity to frustrate and, potentially, lose them.

Custom UI Components close that gap, not by making chat flashier, but by making it capable to show, guide, and collect information the way each task actually needs. That’s exceptional customer experience: fewer dead ends, fewer hand-offs, and a clear path from question to action.

To see how Custom UI Components work, [request a demo](https://cresta.com/request-demo-ai-agent) now.
