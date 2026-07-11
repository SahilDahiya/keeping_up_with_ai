---
title: 'AIEWF Daily Dispatch: The great loops debate and the state of AI engineering'
topic: industry
subtopic: trends
secondary_topics:
- agents/planning
summary: Dispatch on the loops debate and the state of AI engineering, capturing emerging
  vocabulary for production AI systems.
source: latent-space
url: https://www.latent.space/p/aiewf-daily-dispatch-locomotives
author: Richard MacManus
published: '2026-07-03'
fetched: '2026-07-11T05:09:25Z'
classifier: codex
taxonomy_rev: 1
words: 1157
content_sha256: 5daaff75c0b95b4a48b6c2c48772a33ef86fecc95535ee96de5235224a9f4d8e
---

# AIEWF Daily Dispatch: The great loops debate and the state of AI engineering

# AIEWF Daily Dispatch: The great loops debate and the state of AI engineering

### The AI Engineer World’s Fair ended with a debate about loops, a report on the state of AI engineering, and closing keynotes focused on what to build next.

![](https://substackcdn.com/image/fetch/$s_!M0WA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d4f7346-6688-4240-b077-16bf6f4a4a34_1280x815.jpeg)

One of the highlights of the final day of the AI Engineer World’s Fair was a debate about loops. It nicely captured an argument running through the whole conference: are autonomous software factories viable now, or is the engineering discipline lagging behind the ambition?

Allie Howe from Keycard was the moderator and she opened by asking, “is there or is there not a delta between the hype behind loops and what actually works in practice?”

The pro-loop case was presented by Geoffrey Huntley, creator of the [Ralph Loop](https://ghuntley.com/loop/), and Keycard CEO Ian Livingstone. Huntley opened by saying loops are already here. “It’s inevitable, it’s here to stay,” adding that “I don’t see myself going back to writing code by hand.”

Livingstone said that verifiability is ultimately what it’s about — and you can achieve that with any code, regardless of how it was produced. He also pointed out that loops have always been a core aspect of software development:

“A loop is at the core of ‘I try something, I learn something, I apply something.’ And all we’re really talking about is how quickly we can expedite that process.”

On the skeptical side were Dex Horthy from HumanLayer and Greg Pstrucha from Subroutine. Horthy began by noting that he wasn’t anti-loops. “The basic take here is not whether loops are good or bad,” he said, noting that “Kubernetes is actually built on loops — built on control loops. But they’re deterministic loops.” Horthy’s issue is that “the hype is outrunning the discipline.”

“I haven’t seen proof that we are at a point where we can just step up an abstraction level,” Horthy said, referring to agents controlling the coding. “I actually think we need to step down an abstraction level, if anything.”

Pstrucha was mainly concerned about the economic viability of agentic loops, which he said wasn’t sustainable. You can’t “orchestrate your problems away by buying more tokens,” he said.

“[We’re] kind of like locomotive engineers now. That’s our job: to keep the locomotive on the rails.”

- Geoffrey Huntley, loops advocate

Huntley then offered this wonderful analogy for loopmaxxing: “[We’re] kind of like locomotive engineers now. That’s our job: to keep the locomotive on the rails.”

The discussion turned to [software factories](https://www.latent.space/p/software-factories), the metaphor that has really taken hold of the industry. Horthy worries that when everything is automated in a factory-like agent environment, “you never touch the problem.” So instead, he advises to start small and iterate with agent loops — to “build up intuition” and not try to automate end to end from the start.

Even Huntley recognized some of the dangers in loops. He said that software factories represent where we are headed in the future, but cautioned that it’s not yet solved in the market. “This is frontier thinking,” he said.

At the end of the hour-long debate, Howe polled the audience to ask which side ‘won’. Ironically, this resulted in a human failure: the stage lights were too bright for Howe or any of the debate participants to see how many hands were raised. If only an agent was in charge of dimming the lights.

## Anthropic’s next big thing: Claude Tag

Perhaps one example of a company moving to a software factory model is Anthropic. Mike Krieger, one of the co-founders of Instagram back in Web 2.0 and now Head of Labs at Anthropic, was interviewed by swyx in one of the morning sessions.

Krieger talked about [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag), Anthropic’s internal model which the company announced to the world last week. He described Tag as more delegated, asynchronous and proactive than Claude. It perhaps suggests what an early software factory looks like in practice — not agents replacing a team, but multiple people delegating responsibilities to a system like Claude Tag.

![](https://substackcdn.com/image/fetch/$s_!Av0r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26adc828-7702-490a-be57-f91ac1adb699_1280x800.jpeg)

“Most usage is actually much more delegated,” he said regarding his team’s usage of Tag. He gave an example of how they instruct the agents: “Don’t just fix this bug. Now you are responsible for this part of the codebase, and I want you to monitor this feedback channel and proactively take on tasks.”

“That’s really changed how we operate currently,” he continued. “It’s much more this multiplayer, async, proactive way.”

However, he also indicated there are some negative consequences to becoming more automated. He noted that his team is “bottlenecked on reviews” and on the “human ability to fully conceptualize what we’re doing.”

## 2026 AI Engineer Survey

Back to the current reality for most AI engineers. This morning, Barr Yaron from Amplify presented her annual survey of the industry.

According to Amplify’s data, 95% of respondents now use agents — roughly double last year’s share. Among teams using agents, 89% said those agents could write data, up from 52% the previous year.

“Agents are no longer reading, summarizing, drafting,” Yaron said. “They’re taking actions inside the systems.”

![](https://substackcdn.com/image/fetch/$s_!zAbI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce7fe746-5558-4484-92a2-82f5309f0230_1280x800.jpeg)

The controls, however, remain comparatively primitive. Human approvals and permissions were the two leading safeguards, followed by a scattered collection of task decomposition, retrieval, memory and sandboxing techniques.

“Nobody has settled the control layer for agents,” Yaron said.

Cost is also a concern. Forty percent of respondents said that AI costs regularly limit how ambitiously they use AI, while another 36% said it sometimes does. Token usage is now the second-most monitored production metric, behind quality.

The survey captured the conference’s central contradiction. AI has made experimentation cheaper and enabled teams to produce more software, but 59% of respondents to the Amplify survey fear that today’s AI-generated code is creating long-term liabilities.

## Closing keynotes

The final sessions of the conference appropriately took us back to thinking optimistically about AI technology — about building with it. After all, that’s why the AI Engineer World’s Fair exists, and it’s where the fun is!

Theo Browne showcased several software projects he had built, or was still building, with AI. His point was that the scale of what an individual developer can realistically attempt has shifted. “What used to be a startup is now a side project,” he said, while projects he would once have dismissed as “too big” are moving within reach.

Garry Tan, president and CEO of Y Combinator, followed by giving that optimism an organizational form. The fastest-growing founders YC sees, he said, are “not treating AI as autocomplete, they’re treating it as a workforce.”

![](https://substackcdn.com/image/fetch/$s_!TVDr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f4f4636-6d5b-422a-97c9-e653e4f100e3_1280x750.jpeg)

Tan’s closing prescription was: “Build an AI-native company, not a company that just uses AI.”

The debates during the week showed how much engineering remains before the AI-native vision is viable for all. But the closing keynotes offered a reminder of why the engineers who attended this conference are pursuing it: they just want to ride those locomotives!
