---
title: 'AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers'
topic: agents
subtopic: planning
secondary_topics:
- product-engineering/architecture
summary: Covers loops, software factories, and forward-deployed engineering as recurring
  patterns in AI engineering practice.
source: latent-space
url: https://www.latent.space/p/aiewf-daily-dispatch-loops
author: Richard MacManus
published: '2026-07-01'
fetched: '2026-07-11T05:09:47Z'
classifier: codex
taxonomy_rev: 1
words: 1153
content_sha256: f4bfd78bd21f8b4298b8cf08507ee9885b5f965a6cc84c46710eecd0602d1407
---

# AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers

# AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers

### On Tuesday at the AI Engineer World's Fair, there was a lot of talk about loops, agent engineering, and the emergence of software factories. Also a hot topic: open models.

![](https://substackcdn.com/image/fetch/$s_!i4cw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee341b9f-8fd3-47e5-87db-9b3d0fc72de5_1280x720.jpeg)

Loops, loops and more loops. That word, loop, dominated conversations on day 2 of the [AI Engineer World’s Fair](https://www.ai.engineer/worldsfair/2026) — the first full day of keynotes and sessions. Perhaps knowing in advance what everyone would be talking about, AIEWF cofounder swyx titled his opening talk, “Loopcraft: The Art of Stacking Loops.”

swyx began by commenting on the evolution of AI engineering from 2022: from chat, to tools, to goals. “These days, we’re all about automations,” he added. “We’re all about cron jobs and loops.”

![](https://substackcdn.com/image/fetch/$s_!O16d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30e4c714-6ee4-41d1-899f-e0e3afee363b_1280x769.jpeg)

Allie Howe, a member of technical staff for Keycard, then introduced the main stage track for the day: Software Factories. She referenced Geoffrey Huntley’s influential article, “[everything is a ralph loop](https://ghuntley.com/loop/),” a theory about turning an AI coding agent into a persistent worker by repeatedly restarting it against the same spec.

Pablo Castro from Microsoft then talked about Foundry, the company’s “AI app and agent factory.” He claimed that a “learning loop” occurs when people and agents work together.

OpenAI’s Alexander Embiricos and Romain Huet were next on, and they focused a lot on Codex, the company’s coding agent. One point they made was that using multiple agents via loops can result in enhanced productivity.

![](https://substackcdn.com/image/fetch/$s_!dfdM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6d35a5b-4958-4c34-926a-00156642dab9_1280x850.jpeg)

“There will be a lot of talk today about loops,” Embiricos said. “And if you can connect the agent to not only the work that you have to do, but *why* it has to be done, that’s how you can get the agent to start to begin much more work. And then if you can connect it to what you do afterwards, review and deploy, that’s how you help it land much more work.”

This segued to a presentation by Peter Steinberger, the “ClawFather” of OpenClaw, now working for OpenAI. He too was all-in on loops, noting that he designs loops to manage agents. He added that deciding what to pay attention to is his main challenge nowadays — and that the future is “better loops” to help solve this issue.

![](https://substackcdn.com/image/fetch/$s_!6tmE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5478973-1c9b-43a6-a1bf-e7346be0f717_1280x850.jpeg)

## Software factories

All this talk of looping led naturally to the concept of “software factories,” the subject of a presentation by Tereza Tížková from a company called Factory. She defined a software factory as “the whole loop, the whole lifecycle of developing software with autonomy.” She added that this doesn’t mean just coding, but also “collecting all the signals, reacting to user feedback [and] to logs, prioritizing what’s important, then orchestrating it all.”

![](https://substackcdn.com/image/fetch/$s_!PgI3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F366dac2b-5c86-4c55-aa69-327233d5d93a_1280x723.jpeg)

Zach Lloyd from Warp also spoke about software factories; in fact, his thesis was that “software engineering will become factory engineering.” Loops in Lloyd’s framing were about improving the system.

In both Tížková and Lloyd’s talks, the emphasis was on having the agents doing the building for you. “You’ll be building the thing that builds the product,” was how Lloyd put it.

Afterwards, I went down to Warp’s booth in the AIEWF expo hall and spoke to Lloyd about software factories. I particularly wanted to know why Warp, which began as a CLI tool for developers, has pivoted into a ‘software factory’ platform where developers aren’t supposed to do coding anymore.

“The way to think of the factory is, like, pick your repos, pick the parts of the lifecycle that you want to automate, pick the ways in which you want humans to be brought into the loop,” Lloyd told me. “And different organizations [and] code bases will have different preferences for, like, do you fully automate code review [or] do you have humans do hard coding, stuff like that.”

![](https://substackcdn.com/image/fetch/$s_!fuIy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f5ffb36-1b2a-49c5-acaa-73af9ffe3a47_1280x800.jpeg)

I noted that the term “factory” might be offputting to many developers, since it implies mechanized rote work — much different from the creative era of coding we’ve just come from. Lloyd recognizes this is a challenge, but he argues software factories will become a new discipline of engineering — and that it still requires problem solving.

“For better or worse, the power of these systems is so great and the ability to accelerate is so strong that just writing stuff by hand...I don’t think it’s going to make sense for very much longer,” he said.

(For more from Zach Lloyd on software factories, stay tuned for a Latent Space interview to publish shortly.)

## Forward Deployed Engineers

Related to loops and software factories, another theme from AIEWF today was the trendy new role of Forward Deployed Engineers. In [an interview with Natalie Meurer](https://www.latent.space/p/forward-deployed-engineers-aiewf), Head of Agent Engineering at Sierra, I established that FDEs are also sometimes called “agent engineers.” The main point is to help organizations adapt to agents, from a development perspective.

Meurer pointed out that a lot of the work of integrating AI into companies these days is in orchestrating agents.

“In practice, most customer-specific work takes place at the orchestration layer rather than in the models themselves,” she told me.

Cursor’s VP of Forward Deployed Engineering, Pauline Brunet, also ran a session today at AIEWF, in which she positioned FDE as part of the shift to software factories. “We partner with your organization to co-design and co-build your AI software factory,” she said. “We transform how you design, develop, and maintain software across your entire life cycle.”

![](https://substackcdn.com/image/fetch/$s_!6GAG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ae6bbb3-a932-4ba4-917b-56bffdbdc915_1280x960.jpeg)

(More insights from Brunet coming in an upcoming Q&A.)

## Open Source AI

Another key theme from AIEWF today was the rise of open source AI. Zixuan Li, the head of intriguing new Chinese company Z.ai, was due to make an appearance at the conference. Because of travel issues, he couldn’t make it in person. He did make a virtual presentation, though, focusing on the company’s groundbreaking open LLM, GLM-5.2 — its “flagship model for long-horizon tasks.”

He also introduced ZCode, a harness that “supports all frontier models.” Li compared it specifically to OpenAI’s Codex.

![](https://substackcdn.com/image/fetch/$s_!rJ6b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04e4d1b2-dcb8-4904-b162-65f424c8a967_1280x750.jpeg)

HuggingFace’s Thomas Wolf then interviewed Olive Song from Chinese company MiniMax, which recently released its latest open-weight model, M3.

Open source AI is a big reason why [local AI is becoming more popular](https://www.latent.space/p/ahmad-osman-local-ai). Ahmad Osman is the founder of Osmantic, a company building open source software for deploying and operating local AI systems. He spoke to us today and noted that open models have improved dramatically in recent times.

“Architectures are becoming more efficient, and many small improvements compound,” he said. “Once a frontier lab demonstrates that a capability is possible, the open source ecosystem can work backwards from that and find ways to reproduce it more efficiently.”

## Conclusion

Those were the big trends from day 2 of the AI Engineer World’s Fair. I’ll be back tomorrow with all the action and analysis from day 3. Don’t forget to [tune into the keynotes](https://www.youtube.com/@aiDotEngineer/streams) on YouTube if you’re following from work or home.
