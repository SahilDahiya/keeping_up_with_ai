---
title: Partnering with Meta to bring Llama 3 to Firework’s inference and fine-tuning
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/announcing-llama3-on-fireworks
author: null
published: '2024-04-18'
fetched: '2026-08-12T06:29:01Z'
classifier: null
taxonomy_rev: 2
words: 400
content_sha256: 56ba0b97560dddb12c9c4839ff03dce9af11d5e0f00b3a763b9996658656d2b9
---

# Partnering with Meta to bring Llama 3 to Firework’s inference and fine-tuning

We are pleased to announce the availability of the open-source Llama 3 8B and 70B models with 8k context, served from our blazing fast inference stack. Llama 3 is pretrained on over 15 trillion tokens and with a vocabulary of 128K tokens that encodes language much more efficiently.

List of Llama 3 Series of Models:

Apart from adding the base models, over the next few days, we will be adding support for fine-tuning Llama 3 models, serving of LoRA adapters and increasing inference speeds further. Our serveless inference stack allows to serve 100s of LoRA adapters with NO additional cost.

1. [State-of-the-art performance](https://github.com/meta-llama/llama3/blob/main/eval_details.md) : The new 8B and 70B parameter Llama 3 models establish a new state-of-the-art for open-source language model benchmarks. Improvements in pretraining, instruction fine-tuning, and architecture have led to superior performance on industry benchmarks and real-world use cases compared to competing models.
2. [Open and responsible development](https://ai.meta.com/blog/meta-llama-3-meta-ai-responsibility/) : Meta is taking an open approach by releasing Llama 3 models early to enable community innovation. This is combined with a strong focus on responsible development and deployment, providing new safety tools, an updated[Responsible Use Guide](https://llama.meta.com/responsible-use-guide) , and a system-level approach to mitigating potential harms.
3. Extensible platform with more to come: The 8B and 70B models are just the beginning. In the coming months, Meta plans to release larger models with up to 400B parameters with new capabilities like multimodality, multilingual conversation, and longer context.

Our goal at Fireworks is to make Open-source AI accessible to developers and businesses by providing the best language and image models at lightning-fast speeds with the utmost reliability.

Our industry-leading inference speed and quality for image and text generation are utilized by companies like Quora, Sourcegraph, Upstage, Tome, and Anysphere for their production use cases.

To quickly get up and running using Llama 3 on the Fireworks visit [fireworks.ai](https://fireworks.ai/) to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.

12

Below code snippet instantiates `Fireworks` client and uses chat completions API to call the Llama 3 listed at - `accounts/fireworks/models/llama-v3-70b-instruct`.

12345678910111213

The above API request results in the below response.

12345678910

For enterprises who need even faster speeds or throughput, you can serve Llama 3 on your own [dedicated GPU infrastructure](https://readme.fireworks.ai/docs/dedicated-deployments) or personalized enterprise configurations. If you have any questions or would like to learn more, please don't hesitate to [contact us](https://fireworks.ai/company/contact-us).

Happy building!
