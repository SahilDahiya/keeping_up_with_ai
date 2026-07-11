---
title: Four Predictions for AI In 2023
topic: industry
subtopic: trends
secondary_topics: []
summary: Arize prediction piece on 2023 AI and MLOps trends, including observability,
  generative AI adoption, and operational maturity for ML systems.
source: arize
url: https://arize.com/blog/2023-predictions/
author: Aparna Dhinakaran
published: '2022-12-23'
fetched: '2026-07-11T04:46:25Z'
classifier: codex
taxonomy_rev: 1
words: 1007
content_sha256: 7555c7c22eecd257b6f7ec0f7879b4ad15281ae977d0d46391f0e801252ba37b
---

# Four Predictions for AI In 2023

![2023 Prediction@2x 2023 MLOps Predictions](https://arize.com/wp-content/uploads/2022/12/2023-Prediction@2x-1021x560.jpg)

              # Four Predictions for AI In 2023

From major corporations to startups to independent research labs, machine learning (ML) teams work hard every day to build and deploy models that improve the way we live and work. As the end of the year approaches, it is worth pausing to marvel at their progress.

In many ways, that story in 2022 starts and ends with [generative AI](https://www.arize.com/blog/generative-ai/). The past year saw the launch of not only OpenAI’s Dall-E 2 (April), but also Midjourney (April), Stability AI’s Stable Diffusion 2 (August), and ChatGPT (November). Less headline-grabbing but no less transformational are the steady drumbeat of near-weekly technical breakthroughs in everything from [robotics transformers](https://dblalock.substack.com/p/2022-12-18-arxiv-roundup-robotics) to [improved genome studies](https://pubmed.ncbi.nlm.nih.gov/35017556/).

To most technical ML practitioners, the problem today is not a lack of novel research, tools, or techniques – it’s that they can’t keep up!

Before looking ahead, here is a report card on [last year’s predictions](https://arize.com/blog/five-predictions-for-ai-in-2022/).

- *AI Fairness Will Get Worse Before It Gets Better*- *:*- **TRUE**. The full impact of AI acting in discriminatory ways is not likely fully known, but this year leaves a lot to be desired. For example, it is now clear that- [harmful](https://huggingface.co/spaces/society-ethics/DiffusionBiasExplorer)- [biases](https://openai.com/blog/reducing-bias-and-improving-safety-in-dall-e-2/)lurk in prominent text-to-image and large language models. Model bias also continues to rear its ugly head in more workaday models, impacting everything from- [health outcomes](https://www.science.org/doi/10.1126/science.abo2788)to- [insurance claims](https://www.nytimes.com/2022/12/14/business/state-farm-racial-bias-lawsuit.html). Finally, there is still a- [long way to go](https://arize.com/resource/rise-of-ai-risk-disclosure/)in ensuring better diversity in hiring and AI ethics.
- *Enterprises Will Stop Shipping AI Blind:*- **PARTIAL CREDIT.**While adoption of ML observability is accelerating and- [market leaders](https://labelstud.io/blog/report-data-centric-ai-changing-tech-workflows/)are emerging, the reality is that- [many teams](https://arize.com/wp-content/uploads/2022/02/The-Industry-is-Ready-for-Machine-Learning-Observability-at-Scale-Final.pdf)have still not yet set up monitoring to quickly detect and diagnose problems with models in production. That is particularly true for teams with deployed computer vision and natural language processing models since the tools for monitoring things like- [embedding drift](https://arize.com/blog/monitor-unstructured-data-with-arize/)are still so new.
- *The Citizen Data Scientist Will Rise:*- **PARTIAL CREDIT**. While the adoption of low-code tools is still a factor in democratizing data science, it is in some ways overshadowed by the- [revolution](https://scale.com/blog/text-universal-interface)emerging around large language models with text as a- [universal interface](https://scale.com/blog/text-universal-interface).
- *The ML Infrastructure Ecosystem Will Get More Crowded and Complex*- *:*- **TRUE**. With investment in AI and machine learning infrastructure tools- [surging](https://www.businessinsider.com/top-venture-capitalists-investing-ai-machine-learning-startups-2022-10#saam-motamedi-greylock-partners-12)this year, the space is only more crowded. In all, 85.7% of data scientists and ML engineers- [say](https://arize.com/wp-content/uploads/2022/02/The-Industry-is-Ready-for-Machine-Learning-Observability-at-Scale-Final.pdf)they still sometimes have “trouble navigating a confusing/crowded ML infrastructure space.”
- *ML Engineering Jobs Will Outpace Available Talent, Creating a Talent Crunch:*- **TRUE.**While recent layoffs are cause for concern, the past year is mostly a story of- [labor shortages](https://www.wsj.com/articles/labor-market-layoffs-inflation-recession-11664462809)across the economy –- [especially](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm)in data science and machine learning engineering.

To cap off the year, here are some things to keep an eye out for in 2023.

## 1. Generative AI Will Go Mainstream (and So Will Its Growing Pains)

Generative AI is capturing the public imagination in a way few technical breakthroughs have since the [advent](https://www.loc.gov/collections/edison-company-motion-pictures-and-sound-recordings/articles-and-essays/history-of-edison-motion-pictures/early-motion-picture-productions/) of the motion picture over 100 years ago. With powerful applications like Github Copilot and ChatGPT already proving valuable, many companies are eager to embrace the technology more broadly. However, generative AI remains a wild west. There is a lot to unpack over the course of the next year around [bias](https://twitter.com/spiantado/status/1599462375887114240), [copyright](https://news.bloomberglaw.com/ip-law/wild-west-of-generative-ai-raises-novel-copyright-questions), [scalability](https://arize.com/blog/four-takeaways-from-arizeobserve-unstructured/), [security](https://arstechnica.com/information-technology/2022/09/twitter-pranksters-derail-gpt-3-bot-with-newly-discovered-prompt-injection-hack/), and how to monitor this new technology. In short, generative AI will take a village – and we need to build that village.

## 2. Economic Uncertainty Will Be a Crucible for the ML Infrastructure Market

AI is likely to take on elevated importance as inflation and economic turbulence put pressure on companies to deliver greater efficiency and productivity. Given shifting priorities, the days of central ML teams taking months or years to build and maintain proprietary feature stores or monitoring tools in-house are likely numbered. Buying over building will likely become more common, particularly as teams need to prioritize projects that move the needle on revenue in the near term. Given the economic environment, it is also not unlikely that procurement pressure and even layoffs may impact ML teams in certain sectors. Against that backdrop, only the strongest MLOps tools adding real value for teams will thrive. Expect tools like orchestration platforms – which reflect outdated assumptions on connecting many disparate tools – along with non-category leaders to struggle to raise capital or go out of business.

## 3. Best-of-Breed Platforms Will Chip Away At Legacy Players

It happened in DevOps and now it’s happening in MLOps: in technical fields, best-of-breed platforms tend to win the day. Given the complexity of modern machine learning, ML teams are demanding more depth from tools at each stage of the model lifecycle. As a result, end-to-end platforms that emerged a decade ago to empower both citizen data scientists and ML teams are losing developer-share and [undergoing layoffs](https://www.techtarget.com/searchenterpriseai/news/252524275/Troubled-AI-vendor-DataRobot-hit-by-more-layoffs). Even big players like Amazon (SageMaker) and Google (Vertex) offering end-to-end solutions do not currently reflect the technical depth needed for each part of the ML lifecycle, though a wave of consolidation could change that.

## 4. Working With Unstructured Data Will No Longer Be Optional

Unstructured data is everywhere. According to [multiple estimates](https://mitsloan.mit.edu/ideas-made-to-matter/tapping-power-unstructured-data), 80% of data generated globally is in the form of unstructured images, text, video or audio. Over the past few years, some of the most powerful modern applications of machine learning – from large language models like ChatGPT to computer vision models that can detect cancer or rare medical disorders – leverage unstructured data. Any ML platform that is not built to handle unstructured use cases risks irrelevance or limited growth prospects. At the same time, ML teams that find ways to harness computer vision or NLP models – even if only applying a pre-trained model to a narrow business use case – may find new competitive advantages.

## Conclusion

While every outlook here may not seem bright and sunny, there is much to be optimistic about when it comes to the future of AI and ML teams. Here’s hoping everyone can start off 2023 with their sights on making this industry better!
