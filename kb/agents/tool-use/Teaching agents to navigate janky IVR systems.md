---
title: Teaching agents to navigate janky IVR systems
kind: blog
topic: agents
subtopic: tool-use
secondary_topics:
- product-engineering/case-studies
summary: Details five concrete failure modes voice agents hit navigating IVR phone
  trees for other companies (response timing during preambles, keyword vs conversational
  response modes, detecting a human vs hold-music greetings, unpredictable/broken
  menu trees, and DTMF tone-vs-speech input handling), which raised Sierra agents'
  IVR success rate from ~50% to 85%.
triage: null
skip_reason: null
source: sierra
url: https://sierra.ai/blog/navigating-ivr-systems
author: Marta Garcia Ferreiro; Raymond Mo
published: '2026-08-11'
fetched: '2026-08-12T06:27:52Z'
classifier: claude
taxonomy_rev: 2
words: 1298
content_sha256: 7d2e4e7994caf16e23bce1b20832f9db7a23c06f10843d86283d4a4661d73729
---

# Teaching agents to navigate janky IVR systems

# Teaching agents to navigate janky IVR systems

AI agents increasingly need to call other companies to get their work done. For example, a healthcare provider has to check a patient’s prior authorization for an MRI with their insurer. Or an auto insurance company needs to call a repair shop to get the status and estimated cost of a customer’s repair.

The hard part is not, as many assume, the infrastructure. That already exists: the spoken word over the public switched telephone network. It’s navigating IVR systems designed for people. Turns out that agents find these as frustrating as we do.

Agents built on Sierra can now navigate the most challenging IVR systems out of the box: they understand when to call, how to get through a multi-level menu, when to stay silent, and how to recognize when they’ve reached a person. All agents come with monitors so you understand their IVR performance, and memory so they improve with every call.

With IVR navigation skills out of the box, an agent’s success rates increase by almost 50% to 85% — and this capability is already being used by a number of our customers.

- A top 5 healthcare payer’s agent gives doctor’s offices timely prior authorization updates for their patients. The company built it in less than five days on Sierra.
- A digital pharmacy with a nationwide footprint uses their agent to call local pharmacies so they can transfer medications seamlessly.
- A leading revenue cycle management company’s agent calls payers to get claim status, with a 70% overall success rate and 94% for specific payers.

## Agents, like people, find navigating IVRs hard. Why?

You’d think AI agents could easily navigate another computer system: they’d just listen to the options, pick one, and repeat. In practice, there are five challenging hurdles to navigate.

1. **Timing is key when navigating IVRs** , which often start with a preamble where no response is required — like a legal disclosure or instruction, “press 2 for Spanish”. If the agent answers too quickly it will miss what the IVR says, derailing the call. It needs to classify everything that’s being said: Is this a statement or question? Is the correct “answer” words, numbers, or just silence? Additionally, when on hold, people know to stay silent, something agents aren’t naturally good at. Conversely, if they stay quiet too long, the IVR assumes no one is there, repeats itself, or gives up.
2. **IVRs and people require different kinds of responses** . Voice prompts (“in a few words, tell me why you’re calling”) require keyword answers, not sentences. But once the agent reaches a support associate, it needs to have a conversation, otherwise the person hangs up.
3. **It can be surprisingly hard to detect a person at the end of a phone tree** . Most IVRs end when you reach a person who can take care of your issue. But hold music can end abruptly mid-note, cut off by “hello?” with no transition. And many IVRs play recorded greetings during holds (“Hello, and thank you for calling! Your call is valuable to us”) that can sound nearly identical to a support associate.
4. **IVRs are unpredictable** . Sometimes the phone tree itself is broken — it tells you to “press 3” but only accepts speech, or sends you down a dead end. When you call matters too. During lunch or outside working hours, the agent can navigate the entire tree only to find no one at the other end. And sometimes there simply isn’t a path to the goal — perhaps the right department requires an account number the agent doesn’t have.
5. **Key pad tones (DTMF) require special handling** . Many IVRs, especially authentication gates on healthcare and financial lines, accept only DTMF input, the tones a phone keypad generates when you press the numbers. Speaking “two” at a DTMF-only prompt does not work. The agent must classify which modality the IVR expects and emit tones with correct duration and inter-digit spacing.

## How Sierra solves it

Our platform combines built-in navigation, memory, and intelligent retries so agents can handle what happens in the real world.

- **IVR navigation out of the box** . Agents built on Sierra come ready to handle the mechanics of IVRs: when to speak or stay silent, whether to use speech or keypad tones, how to get through multi-level menus, and how to recognize when they’ve reached a person. Customers don’t need to hardcode the path through every phone tree. To identify when it has reached a person, the agent plots where it thinks it is in the phone tree against what was just said, and what it hears in the audio.
- **The agent can reason through quirks the IVR doesn’t explain** . Member IDs are a good example. An ID may contain letters or a suffix identifying a dependent, while the IVR accepts only numbers. If the IVR rejects the full ID, the agent can retry without the letter prefix or dependent suffix.
- **Memory and intelligent retries** . As every phone line is different, agents built on Sierra are designed to remember which paths work, when departments are actually open, and how to reach the goal. If a call fails, they can use that knowledge to decide when and how to try again rather than starting from scratch.
- **A learning loop.** Every call builds context about what worked, what failed, and where the agent got stuck. Sierra uses that feedback to improve navigation and retries over time.

## How we evaluate performance

To test the effectiveness at scale and systematically improve performance, we built a representative set of IVR trees based on our experience across industries, including many of the technical quirks outlined above. Each tree has goals like “reach a human”, “retrieve a fact”, or “execute an action”. The agent is completely blind to the tree’s structure, it only has the goal and necessary customer details, just like in real life.

We then grade the agent on whether it achieved the goal. For example, if success was “find out how much is covered by the insurer for knee surgery”, the agent has to come back with the right number.

Because most of the challenges are audio-based, we run the evaluation over the real telephone network. The agent dials the number, hears synthesized prompts, sends real DTMF tones, and sits through timers and holds.

To understand which capability contributes what, we ran the same agent on every task in two configurations: a “bare” control arm with only the goal and basic tools, and a “guided” experiment arm with the generic IVR navigation feature switched on. With this feature enabled, the overall pass rate increases by 49%, from 57% to 85%, with the largest lifts “reach a person” tasks. In a real agent, we take that starting pass rate and hillclimb with specific customer context.

![A flow chart with three boxes titled Benchmark driver, Sierra voice agent, and IVR simulator](https://sierra.ai/-/cdn/image?src=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fca4jck6w%2Fproduction%2F69fd0919327e6a232ef99ed28edf117623240100-4017x1512.png&width=3840&quality=75)

## Sierra solves today’s messy IVRs and shapes the future

Sometimes an agent successfully navigates the IVR, reaches a person, and hits a new problem: the company has a policy against serving automated callers. Today, our agents identify themselves directly and schedule a callback with a person.

Longer term, we think agents need a standard way to identify themselves as trusted, authorized callers — and for businesses to give them permission to complete specific tasks.

At the same time, IVRs themselves are changing. Companies are [replacing phone trees](https://sierra.ai/customers/r1-rcm) with AI agents that can handle requests directly or route callers to the right person. That transition will take time. Until then Sierra enables agents to navigate today’s messy phone systems, while we work towards better ways for trusted agents to interact with businesses.
