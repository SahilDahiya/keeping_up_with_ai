---
title: How to Use ChatGPT to Diagnose Revenue Opportunities
kind: blog
topic: prompt-engineering
subtopic: techniques
secondary_topics:
- product-engineering/architecture
summary: Shows the actual structured prompt used to summarize retention calls into
  numbered fields (did the visitor ask to cancel, and why), then explains why GPT-4
  is too slow and expensive at millions of conversations per month. Cresta's answer
  is a system that batches GPT-4, clusters the resulting summaries semantically to
  surface themes, and folds human feedback back in.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/how-to-use-chatgpt-to-diagnose-revenue-opportunities
author: Ryan Muir
published: '2023-06-15'
fetched: '2026-08-20T06:12:35Z'
classifier: claude
taxonomy_rev: 2
words: 763
content_sha256: c5696302baf7c4eb8b0b86b3d325e29cc670a4472211670e9f6c477baaf1ec8e
---

# How to Use ChatGPT to Diagnose Revenue Opportunities

As mentioned in our previous blog post about the "[The emerging stack of Generative AI](https://cresta.com/blog/the-emerging-stack-of-generative-ai/)," GPT-4 serves as the core of an LLM (large language model)-powered system. However, in order to optimize contact center performance, we need more than just an LLM; we need LLM-powered AI systems and products working together to provide valuable insights and assistance. Cresta's proprietary generative AI products achieve this by leveraging multiple LLMs to deliver maximum value for contact center professionals.

### The need for AI/LLM-powered systems in contact centers

Although GPT-4 and other LLMs offer remarkable capabilities in natural language understanding (NLU) and content creation, a contact center relies on more than just these aspects to ensure seamless customer experiences. Insights, analytics, and support for real-time decision-making are critical to train, coach, and optimize agent performance – and this is where LLM-powered AI systems come into play.

Summarize the following retention conversation between a internet company’s agent and a visitor. Format the summary as:

1. Did visitor ask to cancel service? Yes or No or Not Sure

2. Visitor's reason for canceling is

Conversation:

<redacted>

Summary:

1. Yes
2. Visitor’s reason for canceling is they are unhappy with the recent service; they work from home and have had multiple outages in the last week. The Visitor has already installed [competitor’s] services.

*GPT-4 and other LLMs offer remarkable capabilities in natural language understanding and summarization*

### Extracting insights at scale

As we can see, GPT-4 can provide powerful insight into a single conversation. However, it can be expensive and slow to apply at scale, especially considering our largest customers can have millions of conversations per month. We built an AI system to not only deploy GPT-4 at scale, but also incorporate human feedback data to continuously improve its accuracy on custom datasets.

Then our [Insights product](https://cresta.com/product/insights/) uses clustering (automatic grouping of patterns based on semantic understanding) to find common themes among GPT-4 summaries from large-scale conversation sets. 

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f465385a4675b86cd57_68135f3f42f30b88f2e0c7e6_image-1-1024x729.avif)

As you can see, this is a clear example of how one can go from an out-of-the-box LLM to a scalable, enterprise-grade AI system and eventually build AI products around the capability. Now let’s zoom out and take a look at our overall approach for optimal value for the modern contact center.

### Cresta's approach: Leveraging multiple LLM-driven systems for optimal value

[Cresta's AI](https://cresta.com/about/) system integrates multiple LLMs to offer a comprehensive solution for contact centers. These subsystems work in tandem to:

  1. Automatically analyze large conversation datasets for valuable insights and potential business value. Cresta recently worked with a smart-home security device company who had little visibility into their calls and the key revenue-driving moments within them. Cresta leveraged our internal Value Discovery tool to find the optimal path of behaviors that drove sales conversions in their calls.

  1. With input from Cresta and Customer domain experts, leverage the key outputs of our Value Discovery Assessment from step 1 to drive differentiating pockets of business value, applying GPT-4 and other large-scale LLMs as teacher models to train smaller, bespoke LLMs and refine with both automated and human expert feedback
  2. Synthesize data and model outputs based on call reasons, churn reasons, agent behaviors, and other customer interaction factors; feed into our AI-driven systems and allowing agents, managers, and executives to pinpoint areas of coaching and potential improvement
  3. Deliver post-call insights and real-time assistance (e.g., hints, suggested responses, autocompose) to agents during customer interactions, driving more conversations through pivotal, revenue-defining moments; resulting in higher conversion rates and agent satisfaction

![Hint example](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f465385a4675b86cd5a_68135f3f42f30b88f2e0c7cb_blog-chatgpt-revenue-oppotunities-photo-2b.avif)

  1. Track performance metrics over time to measure and optimize contact center agents, managers, enabling data-driven decision making and further refining our models and the tangible value that they are driving

By combining the capabilities of various LLMs under a unified AI system, and then into full-stack AI products, Cresta transforms contact center operations and ensures all aspects of customer engagement are fine-tuned to create exceptional experiences.

### Conclusion

While ChatGPT is an integral part of an LLM-powered contact center, the real key to unlocking trapped business value lies in implementing comprehensive AI/LLM-powered systems and products. [Cresta's solutions](https://cresta.com/solutions/) deliver the necessary insights and assistance for agents, managers, and executives, leading to improved performance across the board. By embracing Cresta's AI-driven approach, contact centers can unlock the full potential of generative AI, resulting in proven business success.Cresta’s Value Discovery Assessment process for revenue maximization can provide bespoke insights into your own contact center operations, discovering pivotal, KPI-driving moments in your conversations and quantifying their value.**Schedule a customized demo and learn more about a Value Discovery Assessment with Cresta today!**
