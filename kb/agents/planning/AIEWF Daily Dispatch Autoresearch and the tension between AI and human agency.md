---
title: 'AIEWF Daily Dispatch: Autoresearch and the tension between AI and human agency'
topic: agents
subtopic: planning
secondary_topics:
- evals-observability/evaluation
summary: Conference dispatch on autoresearch and human agency, useful for understanding
  agent loops and human-in-the-loop boundaries.
source: latent-space
url: https://www.latent.space/p/aiewf-daily-dispatch-agency
author: Richard MacManus
published: '2026-07-02'
fetched: '2026-07-11T05:09:35Z'
classifier: codex
taxonomy_rev: 1
words: 1018
content_sha256: 40551dc4f664c362de13d61e6479515e6be7022322df84f85ae6d1b31b98d1be
---

# AIEWF Daily Dispatch: Autoresearch and the tension between AI and human agency

# AIEWF Daily Dispatch: Autoresearch and the tension between AI and human agency

### The software factory vision met resistance today from speakers defending human understanding and control.

![](https://substackcdn.com/image/fetch/$s_!yyfq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5879355c-6a34-432c-bd6a-a4ace5715f5e_1280x850.jpeg)

Wednesday was autoresearch day on the AI Engineer World’s Fair main stage.

Autoresearch is — you guessed it — a kind of loop. Introspection co-founder Roland Gavrilescu explained it best in [an interview](https://www.latent.space/p/autoresearch-introspection) with Latent Space this morning. He said autoresearch “allows you to build loops in which agents help maintain the system itself.” He called it an “outer loop” that “studies and maintains” the primary, inner loop.

While autoresearch was not specifically mentioned by Anthropic’s Thariq Shihipar, who works on Claude Code, his keynote reflected the same idea of continuous discovery and adaptation. “The models are grown, not developed,” he said. “We sort of figure out and learn with the model as we use it.”

![](https://substackcdn.com/image/fetch/$s_!pnSj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F101677a1-5186-4db9-9b98-8376f22dbad0_1280x800.jpeg)

Former Google engineering leader Addy Osmani also spoke about loops, but his framing differed sharply from Gavrilescu’s.

Where autoresearch puts agents into the loop that studies and maintains the system, Osmani argued that the outer loop should remain human. “Agents can run much more of the inner execution loop,” he said. “But that outer loop is still engineering.” His summary was even more direct: “That inner loop is capability. The outer loop is agency.”

![](https://substackcdn.com/image/fetch/$s_!hchG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd19ebe6a-9249-4038-a2a1-7ba5ec745724_1280x705.jpeg)

**Human agency is still important**

This tension between what agents should do and what human engineers should retain was a recurring theme throughout the day. I also detected some pushback against the “software factory” framing that [dominated Tuesday](https://www.latent.space/p/aiewf-daily-dispatch-loops). This tweet from Notion’s Geoffrey Litt summed it up:

![X avatar for @geoffreylitt](https://substackcdn.com/image/fetch/$s_!l1IK!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F722626068293763072%2F4erM-SPN.jpg)

![](https://pbs.substack.com/media/HMFXT3iaQAAUFln.jpg)

Litt drew a large audience in the Design Engineering track today, where he [spoke about](https://x.com/geoffreylitt/status/2072382778763583603) “how and why humans need to understand our code.” Lily Zhang tweeted [the key takeaway](https://x.com/lily_gpupoor/status/2072469046000496963): “The future will be very polarized: those who understand will keep having the next big idea. Those who delegate understanding will be replaced by the agent.”

Later, Litt [posted a thread](https://x.com/geoffreylitt/status/2072525040873328890) expanding on his argument. Although he acknowledged that agents are increasingly capable of handling more of the process, humans still need to understand what is happening. “You can learn what the agent is doing to make sure you can be an active participant in the creative process,” he wrote.

Another AIEWF speaker seeking to reinforce human agency was Paul Bakaus, who ran a session about his new design tool, Impeccable. Bakaus rejected both extremes: continuing to design entirely by hand, or “loop-maxing” toward a fully hands-off process. “The truth is somewhere in the middle,” he told me after his session.

His goal is to let agents handle the laborious first 80% of the work, before bringing the human back in “for the last 20% to make it a unique thing — to really put in your taste, your point of view.”

“There is no auto, and there will be no auto.”

- Paul Bakaus, Impeccable

For Bakaus, that is not simply a temporary limitation of today’s models. It is also about authorship and accepting responsibility for your work. “People need purpose, and they want to play a role in whatever they create,” he said. “When you work with the agent, then you feel more ownership of the product.”

This philosophy is built into Impeccable itself. “There is no auto, and there will be no auto,” Bakaus told the audience. What he means is that his product will never “one-shot” a solution — the user must be involved in the design process. “The point is to give you a way to steer what you want to end up with,” he added.

**Generative media**

The same question surfaced during a panel on generative media. As image, video and audio models become more capable, the issue is not merely what they can generate, but whose judgment shapes the result.

Nicole Brichtova, who works on Google’s generative media products, including Nano Banana, drew a distinction between average preference and cultivated expertise. “Somebody who has honed a craft has a very different level of expertise,” she said. “You see things that the average human will not.”

![](https://substackcdn.com/image/fetch/$s_!JX28!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3cfc820-15ab-4a95-ac1a-f453700888dd_1280x850.jpeg)

This matters because every model has a default aesthetic, whether its creators acknowledge it or not. “It ends up being us,” Brichtova said. “It ends up being the modeling teams.” She suggested that model developers may need to work more closely with people who have “a really creative point of view” — effectively bringing the art director back into the loop.

Shane Gu made the same point more broadly. Even as models become better at generating and refining their own outputs, he argued, humans must retain the sensitivity to notice what is wrong, generic or insufficient.

“Maybe right now the AI can do a lot of all the promptings and it’s sufficient, but if it’s like that, never be satisfied [that] AI is generating the content. Always find your sensitivity.”

**Agentic sites**

Even the web itself — the ultimate human information network — is grappling with how much automation to use.

In his session this afternoon on “agentic sites,” Adobe principal scientist Carlos Sanchez demonstrated websites that assemble and personalize pages in real time based on a visitor’s intent. He presented this transition as increasingly inevitable: “This is now possible. It’s only going to get better. It’s only going to get cheaper. It’s only going to get faster.”

![](https://substackcdn.com/image/fetch/$s_!OGEi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7fdeb44-4405-444d-9ff1-977f40b1976f_1280x800.jpeg)

But Sanchez also sounded a note of caution. “With AI, it’s very easy to build things, but it’s hard to know what to build,” he told me afterwards. That becomes especially important when an agent is generating experiences on behalf of a brand. “You cannot just generate the whole site,” he said, because the result may stray outside the brand’s guidelines.

That brings the discussion back to autoresearch. Agents may increasingly be able to observe, evaluate and improve other agents, but humans must still define the goals, judge the results, and take responsibility for what the loop produces.

As impressive as agentic technology is now, and as compelling an idea as automated “software factories” might be, you still need humans in the loop.
