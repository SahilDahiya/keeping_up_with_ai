---
title: Does One LLM Fit All? Public vs. Domain vs. Fine-Tuned
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: 'Compares public LLMs (ChatGPT, Bard), domain models, and fine-tuned models
  for enterprise deployment: public models offer fast time-to-value and prompt-based
  self-serve but carry cost, latency, and an accuracy ceiling from training on public
  data rather than ground truth. Fine-tunes right-size the model per task and learn
  continuously from feedback, at the price of training effort and per-use-case deployment.'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/does-one-large-language-model-fit-all
author: Nicky Budd-Thanos
published: '2023-07-27'
fetched: '2026-08-20T06:10:55Z'
classifier: claude
taxonomy_rev: 2
words: 512
content_sha256: 19225859ddee5933d0e3323e98dddfd8f30087b549d47d7f003e7961ea05df07
---

# Does One LLM Fit All? Public vs. Domain vs. Fine-Tuned

Yesterday, we [hosted a webinar](https://cresta.com/public-and-private-large-language-models) designed to dig further into the ways that public and private large language models (LLM) differ from one another - and complement one another. Moderated by Cresta CMO Scott Kolman, the webinar welcomed [John Donovan](https://www.linkedin.com/in/johndonovanatt/), technologist and former CEO of AT&T Communications and Tim Shi, Cresta’s co-founder and CTO, to share their expertise and unique perspectives on generative AI and the enterprise. Tim kicked off with background on LLMs and the impact they have had on applications of AI. As he said, the core of what makes LLMs remarkable is the scale involved; with proper programming, you can scale a model to billions - or even *trillions* - of parameters. With this, the model starts to have emergent capabilities, meaning that it develops better language understanding and better reasoning. So how to consider whether to deploy a public LLM - like ChatGPT, Bard, or some others you may be familiar with - or a private LLM? Here, we got into the pros and cons of deploying a public LLM:

### Public LLM - Pros

- Quick time to value - a very low barrier to entry
- Ability to enable self-serve through prompt design
- Vast public knowledge

### Public LLM - Cons

- Very large models can be costly and slow - as the model continues to grow, downstream costs in time and resources may be involved
- Can’t continuously learn from feedback
- Accuracy ceiling on critical tasks - public LLMs are trained on public data, not truth

Next, our panelists turned their attention to Domain Models and Fine-tune Models. Domain Models find themselves in the middle of these generic, publicly available LLM and the Fine-tune Models; they are trained on domain-specific data, and thus will show value immediately. An example of this would be [Cresta's Ocean-1 model](https://cresta.com/blog/introducing-ocean-1-worlds-first-contact-center-foundation-model), the world's first contact center foundation model, designed specifically to draw on contact center expertise. What about Fine-tune Models and their pros and cons?

### Fine-tune LLM - Pros

- Pick the right size for the right task
- Continuously learn from feedback data, making the model ever more bespoke and tuned to your particular business needs
- Reach high accuracy for critical tasks

### Fine-tune LLM - Cons

- Require effort to train
- Difficult to self-serve
- Per use case deployment

During the webinar, Tim also addressed security and privacy considerations when it comes to these different types of LLMs and how exactly those in the contact center space should be thinking about deploying generative AI applications in the most effective ways. Next week, we’ll dig into some of the C-level insights that John shared with us - including his take on how boards and the C-suite are evaluating generative AI solutions, three critical drivers that companies and vendors should be addressing with their deployments, and much more. In the meantime, [**download the on-demand webinar replay now**](https://cresta.com/public-and-private-large-language-models) and share with your team! And to understand what Cresta’s custom-built generative AI products can do for your contact center, get in touch and [**request a demo now**](https://cresta.com/request-a-demo).
