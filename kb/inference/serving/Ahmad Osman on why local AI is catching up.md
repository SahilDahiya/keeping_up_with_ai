---
title: Ahmad Osman on why local AI is catching up
topic: inference
subtopic: serving
secondary_topics:
- models/releases
summary: Discusses local AI progress and the deployment implications of increasingly
  capable local models.
source: latent-space
url: https://www.latent.space/p/ahmad-osman-local-ai
author: Richard MacManus
published: '2026-06-30'
fetched: '2026-07-11T05:09:53Z'
classifier: codex
taxonomy_rev: 1
words: 1510
content_sha256: 5d643a1c909b931fcfd92d859022f812024e2004ad26eb6c39fda616c0c6c0d0
---

# Ahmad Osman on why local AI is catching up

# Ahmad Osman on why local AI is catching up

### After two packed AIEWF workshops, Ahmad Osman makes the case that local AI is catching up fast — from laptops and phones to enterprise-grade infrastructure.

![Ahmad Osman at AIEWF Ahmad Osman at AIEWF](https://substackcdn.com/image/fetch/$s_!9BC6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9842112b-570d-48b7-92f3-7cbb05681776_1280x720.jpeg)

[Ahmad Osman](https://www.ahmadosman.com/about/) has been advocating for local AI — running models on your own computer, workstation or dedicated hardware — long before it became a major theme at this year’s [AI Engineer World’s Fair](https://www.ai.engineer/worldsfair/2026). He is also the founder of [Osmantic](https://osmantic.com/), a company building open source software for deploying and operating local AI systems.

One of the themes emerging from AIEWF is that open source LLMs are becoming increasingly credible alternatives to large, proprietary frontier models. Since most local AI systems depend on open models, that shift strengthens the case Osman has been making. As he told Latent Space, “the gap between open-source models and closed-frontier models keeps shrinking.”

Osman makes the argument even more explicitly on a website called [Open Source AI Must Win](https://opensourceaimustwin.com/), where he writes that “the ability to study, build, repair, deploy, audit, adapt, teach, preserve, and run intelligence systems without asking permission is of existential importance.”

At AIEWF, Osman ran a two-part workshop on local LLMs and workstation agents. The sessions showed how quickly the field is moving — from models running on phones and laptops, to dedicated GPU workstations and enterprise infrastructure.

The interest in Osman’s workshops was not limited to hardware hobbyists, either. Attendees ranged from students considering their first AI-capable machine to enterprise executives thinking about model routing, private infrastructure and control over company data.

In the following Q&A, Osman explains why local AI is attracting more attention, how the model and hardware landscape has changed, and why he expects more developers and enterprises to begin treating local AI as serious infrastructure.

## Making local AI tangible

**Latent Space:** Can you summarize what the workshops were about and what attendees were looking for?

**Ahmad Osman:** It was a two-part workshop, and there was more demand than we had space for. Some people unfortunately had to be turned away.

I came in with a website we had prepared to demonstrate local AI. It was essentially a hardware arena where people could compare systems such as the DGX Spark, AMD Strix Halo machines and other devices. You could run them against one another, or compare them with a frontier cloud model, and see the performance, output quality, speed and latency for yourself.

The main idea was to make local AI feel real. There is still a perception of it that dates back to 2022, when the models were much less capable. But everything has improved substantially since then.

There is still a lag behind frontier models — perhaps four to eight months — but local and open models are catching up. We wanted people to interact with these systems rather than just hear a theoretical argument about them.

The software behind the demo is open source and available on GitHub. The second workshop went further into setting it up and showing the full system in action.

## A model is only one part of the system

**Latent Space:** What is missing when people think of local AI as simply running a model on their own machine?

**Osman:** There is a big misconception about products such as ChatGPT or Claude Code. They come with a complete infrastructure around the model and around the agent. It is not just one thing.

A friend of mine bought an RTX 5090 to run Qwen 3.5 locally. He connected Claude Code to the model and asked it to change the RGB lighting on the GPU, but it failed. He then used the hosted Claude Code service, and it worked.

I asked whether he had given the local model internet search access. He had not. The model’s training data had a cutoff date, while the software and documentation he needed had since changed.

Once we gave the local system access to a search endpoint, it was able to complete the task.

That is the point: when you use a hosted agent, you are not only using a model. You are using search, tools, infrastructure and other services around it.

With our open source deployment system, we are trying to provide the complete experience — from a chat interface and document ingestion to agents, harnesses and search tools. That end-to-end layer has been lacking in the local AI ecosystem.

## Interest spans students, enthusiasts and enterprises

**Latent Space:** Who came to the workshop? Were they mainly hardware enthusiasts, or people trying to build privacy-based applications?

**Osman:** It was a very wide audience.

At the end of the second workshop, a student asked me what hardware she should buy before going to college. An executive from Intel asked how we could get the software running on Windows in a particular way to improve the user experience.

Some people were enthusiasts. Others had very enterprise-focused questions. The common thread was interest in running something they can control, whether that means a model on a MacBook, a GPU at home or a dedicated cluster of high-end enterprise hardware.

People asked about enterprise model routing, data collection, traces, agent sandboxing and latency. Others asked how many GPUs I have at home. The answer is 22 RTX 3090s.

The breadth of interest surprised me. This was my first AI workshop, and I was lucky enough to do two of them back to back.

## You may not need to buy a GPU

**Latent Space:** Do developers need to go out and buy GPUs to experiment with local AI?

**Osman:** It depends on the size of the model you want to use.

You can run a four-bit Qwen model on a MacBook. At the other extreme, a very large frontier-class open model might require several RTX Pro 6000 GPUs.

But the broader trend is that models are becoming much more efficient. On a modern phone, you can now run a model that outperforms systems people were using in the cloud only a couple of years ago, without using all of the device’s memory.

That shows how far model efficiency has come in a relatively short time.

## Models and hardware are improving together

**Latent Space:** Is the progress mainly coming from better software and models, or from hardware as well?

**Osman:** The models have improved dramatically.

Architectures are becoming more efficient, and many small improvements compound. Once a frontier lab demonstrates that a capability is possible, the open source ecosystem can work backwards from that and find ways to reproduce it more efficiently.

We are seeing models with tens of billions of parameters deliver performance that would previously have required much larger systems. Some of those models can run on an RTX 3090 released in 2020. Two years ago, that level of capability on that hardware would not have been realistic.

This is still a very new field, and we do not know the end state. But we know the systems will continue to improve.

## The rise of hybrid and sovereign AI

**Latent Space:** Do you expect more applications to combine local and cloud AI?

**Osman:** Yes. Edge models are going to become more popular, and this is not only about consumers.

Enterprises are increasingly aware that the models they depend on may not always remain available to them in the same form. Providers can change quality, pricing, access or policies.

That creates an incentive to move toward dedicated hardware and secure compute. It does not necessarily have to sit on premises. A company can use dedicated, colocated hardware that it controls.

The benefit is that the quality of the model does not unexpectedly change, access cannot simply be removed, and the company retains control over its intellectual property, data, privacy and compliance obligations.

Open source models are also continuing to close the gap with frontier proprietary systems. We have seen a rapid progression through Llama, Mistral, Qwen, DeepSeek, GLM and Kimi models. Each generation narrows the gap.

## Specialized models may be the real opportunity

**Latent Space:** Where do you think this leads for businesses?

**Osman:** I have believed for some time that smaller, specialized models are the future for many business use cases.

An enterprise may begin with a general model and collect traces, messages and feedback from how employees use it. Over time, that data can support a more specialized model tuned to the company’s particular work.

That can improve performance, reduce costs and make the system more useful for the business.

I also think open source model companies may increasingly monetize through licensing for fine-tuning, reinforcement learning or specialized commercial deployments.

As more companies move away from relying entirely on cloud APIs and secure their own compute, these labs will have an incentive to keep releasing strong open models while capturing value when businesses adapt them for proprietary use cases.

The broader direction is toward greater sovereignty: companies and individuals controlling their models, compute and data, while still benefiting from the rapid progress of the open source ecosystem.
