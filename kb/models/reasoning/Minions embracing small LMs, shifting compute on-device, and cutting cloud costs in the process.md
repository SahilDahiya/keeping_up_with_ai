---
title: 'Minions: embracing small LMs, shifting compute on-device, and cutting cloud
  costs in the process'
topic: models
subtopic: reasoning
secondary_topics:
- infra-platform/cost
summary: Explores using small language models and on-device compute to reduce cloud
  inference costs.
source: together
url: https://www.together.ai/blog/minions
author: Avanika Narayan; Dan Biderman; Sabri Eyuboglu; Avner May; Scott Linderman;
  James Zou; Christopher Ré
published: '2025-02-25'
fetched: '2026-07-11T04:24:26Z'
classifier: codex
taxonomy_rev: 1
words: 1114
content_sha256: 833c18dbc1ce4b9109ec6ca90042d2e169a7ae41da1fd68e871b488a12b98728
triage: keep
skip_reason: null
---

# Minions: embracing small LMs, shifting compute on-device, and cutting cloud costs in the process

## Summary

We present Minions, a method that shifts a substantial portion of LLM workloads to consumer devices by having small on-device models collaborate with frontier models in the cloud. By only reading long contexts locally, we reduce cloud costs with minimal or no quality degradation. We imagine a future where an “intelligence layer” running persistently on-device interacts with frontier models in the cloud to deliver applications with cost-effective, “always-on” intelligence.

## The Tailwinds: Frontier Models Cost $$$, While Local Hardware is Collecting Dust

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee9023ab_67bda572081ca50d1897db8e_img1_computer_dust.png)

Compute is everywhere—our [laptops](https://www.apple.com/newsroom/2024/05/apple-introduces-m4-chip/), [phones](https://www.apple.com/apple-intelligence/), [cars](https://www.trendforce.com/news/2024/05/03/news-tsmc-reportedly-commences-production-of-teslas-next-generation-dojo-chips-anticipates-40x-increase-in-computing-power-in-3-years/), and even [eyeglasses](https://www.qualcomm.com/products/mobile/snapdragon/xr-vr-ar/snapdragon-ar1-gen-1-platform) ([shoutout to Chris](https://www.youtube.com/watch?v=-cqwXxUo_q8), and no, not our advisor ❤️) — and the amount of compute on these consumer devices seems to be growing rapidly (*e.g.* Nvidia just announced [a desktop](https://www.nvidia.com/en-us/project-digits/) with Blackwell GPUs). Thanks to incredible packages like [Ollama](https://ollama.com/) 😊 (along with many others), consumer devices can now run surprisingly capable small LMs. While we’re calling them “small”, remember that we’re talking about models that have billions of parameters and can tackle real tasks. And they are improving rapidly.

With models of that caliber on-device, we can envision a world where laptops host always-on coding assistants that tirelessly refactor our code, local agents that process documents seamlessly, and smart security systems that detect anomalies before they escalate. We’re getting there—but not quite yet. Today’s local LMs handle more humble tasks, like auto-complete, text summarization, and small-scale RAG pipelines. Any moderately challenging task is handled by frontier models on the cloud. However, these models are not cheap. Consider our code refactoring dream; asking **OpenAI’s o1 a single question on a respectable code repository (with one million tokens) will cost us >$15¹**!!!

¹ o1 current rate is $15.00 / 1M tokens.

## The Big Question: Can Local LMs Step Up?

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee9023a1_67bda631f9a954386b6a28af_together-blog-minions-2.png)

Small LMs are improving rapidly. Perhaps even more rapidly than their frontier counterparts. But it’s undeniable that for some higher order/domain-specific reasoning tasks (i.e., medical reasoning) frontier models have a clear advantage. Instead of seeking to replace big models with small ones, we ask: to what extent can these two model tiers** collaborate to reduce cloud API costs**? 

To mimic the dream use cases mentioned above – of continuous grunt work on device – we analyze three data-intensive tasks that involve retrieving and integrating data from long domain-specific documents:

- **Financial analysis**over 100-page 10-K reports (- **FinanceBench**
- **Medical reasoning**over patient records (- **LongHealth**
- **Question answering**over scientific papers (- **QAsper**

## The Naive Attempt: Minion

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1012498640ee90238a_67bda63eb6bab5576a682504_together-blog-minions-3.png)

We first tried a simple approach: letting the on-device LM, which has access to data, chat freely (see Figure 1 below) with a cloud model—like a junior analyst consulting a senior expert. The models choose which information to share and when to terminate the conversation. Since the long document is not sent to the cloud, we** pay only 3.3% of the cloud cost while maintaining 87%** of cloud model performance. Not bad at all! But why do we lose 13 points? It seems like performance takes a hit due to two limitations of the current generation of small LMs:

- **Long Context Struggles**– As document length increases, small LMs perform worse.
- **Multi-Step Confusion**– As instructions become more complex and multipart, small LMs struggle to follow them reliably.

Beyond these challenges, **hardware utilization (on consumer GPU like 4090) remained low, **leaving both compute and potential accuracy gains on the table (h/t [Large Language ](https://arxiv.org/abs/2407.21787)🐒’s)**.** A back-and-forth chat does not take advantage of batching on-device, which is crucial for achieving high utilization.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee902399_67bce612941a512aaab25d3a_img4_minion_chat.png)

## The Sophisticated Attempt: Minions

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee902393_67bda64799c8a11af9dc75c0_together-blog-minions-5.png)

The lessons we learned led us to the enhanced Minions protocol (emphasis on plural “s”). MinionS introduces a **decomposition-execution-aggregation** loop that addresses the weaknesses of small LMs, while making them work harder (in MinionS, we work harder *and* smarter).

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee902396_67bce63879ad47e34224097d_img6_minion_chat.png)

Here is how it works:

- **Decompose**– The remote LM decomposes the task into smaller, single-step subtasks to be executed on chunks of the context. But how can it decompose the task and chunk the context without seeing it? To this end, we have the remote LM generate code for task decomposition and chunking, which is executed on-device where the context is available.
- **Execute**– The local LM runs the subtasks in parallel, filtering only the most relevant outputs and communicating them to the remote LM.
- **Aggregate**– The remote LM combines the local outputs, finalizing the answer or looping and requesting another round of subtasks.

Minions delivers** 97.9% of the accuracy of remote-only solutions while costing just 17.5% as much**!

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1012498640ee90238d_67bce6a0a108cebe52c70f40_img_7_cost_reduction.png)

## Tuning The Minions

Digging deeper, we found key levers that allow us to navigate the cost-accuracy tradeoff:

- **Model Choice Matters**– Currently, local models below- **3B parameters are not effective for the Minion/Minions protocols.**By fixing the remote model and varying the local model (exploring different sizes and generations), we show that the- **Minions**protocol wouldn’t have been feasible until mid-2024 (until the release of gpt4-turbo and llama3.1-8B)!
- **Scaling of inference-time compute**– Techniques like- **repeated sampling, finer-grained decomposition, and context chunking**(see Figure 4)- **Sequential Communication Helps**–- **Allowing for more**- **communication rounds**generally improves accuracy at the cost of compute.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee9023a7_67bce6b344e199d3f7e4b575_img8_scaling_samples.jpeg)

## To Infinity and Beyond

![Gru with scarf stands amid clouds while six Minions fly on rockets in the sky.](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b1112498640ee90239d_67bda65505731846fec21f34_together-blog-minions-9.png)

MinionS is a first step towards establishing a communication protocol between small on-device LMs and frontier LMs. As GPUs become ubiquitous across consumer and edge devices, we need smarter ways to distribute AI workloads—reducing reliance on expensive cloud APIs while unlocking powerful local applications. If you are a practitioner, researcher, or hacker, we’d love to get you involved with Minions:

- **Practitioners**: we encourage you to apply MinionS to your own workloads — please see the quickstart in our- [GitHub repository](https://github.com/HazyResearch/minions).
- **Researchers**: we see significant opportunities for further research, including improving communication efficiency through better co-design of local and remote models, alternative communication signals beyond natural language, and enhancing inference speed via systems and algorithmic advances.
- **Hackers**: we are just getting started with MinionS, and are excited to continue building. If you are excited by our vision, we’d love to see PRs and new projects that expand our community!

## Additional Resources

- How do you use MinionS? Check out our [GitHub repository](https://github.com/HazyResearch/minions)for sample scripts.
- Want to learn more? Read our [paper](https://arxiv.org/abs/2502.15964).

## Acknowledgments

A huge thank you to Jeff Morgan, Michael Chiang, Patrick Devine, and the entire Ollama team for their support throughout this release. We’re also grateful to Together AI for generously providing compute resources and credits. Lastly, thanks to the Hazy Lab members – Jon Saad-Falcon, Jerry Liu, Jordan Juravsky, Ben Viggiano, Kelly Buchanan and Michael Zhang – for their valuable feedback on this post and throughout our work.
