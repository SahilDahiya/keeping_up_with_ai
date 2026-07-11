---
title: LLM Product Development for Product Managers
topic: product-engineering
subtopic: ux-patterns
secondary_topics:
- evals-observability/evaluation
summary: Product-management guide for LLM applications, connecting user workflows,
  quality criteria, feedback, and evals to AI product development decisions.
source: langfuse
url: https://langfuse.com/blog/2024-11-llm-product-management
author: null
published: '2024-11-13'
fetched: '2026-07-11T04:34:55Z'
classifier: codex
taxonomy_rev: 1
words: 1178
content_sha256: e47ef72de8e8efae5ccfba37229b06cacf9994e2a25780e2139d43efb5802561
---

# LLM Product Development for Product Managers

# LLM Product Development for Product Managers

Learnings from working with hundreds of teams on how to build great AI products.

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc Klingen

Marc KlingenThis blog post is loosely based on a conversation I had with

[Rina](https://www.linkedin.com/in/rina-alexin), Co-founder and CEO of[Productside](https://productside.com/), who had some great questions from the PM perspective. Thank you, Rina, for having me on your podcast!

[Introduction](https://langfuse.com#introduction)

In today's rapidly evolving technological landscape, product managers are increasingly tasked with incorporating AI into their products. While the allure of AI is strong, successful implementation requires careful consideration of use cases, quality metrics, and user experience. This guide draws from practical insights to help product managers navigate the complexities of AI product development, from initial prioritization to production deployment.

Please note that this is based on my experience working with hundreds of Langfuse customers and users. While I aim to generalize, I recognize that there are many other valuable use cases and best practices. Please reach out to me if you would like to discuss this further!

[Selecting the Right AI Use Cases](https://langfuse.com#selecting-the-right-ai-use-cases)

The foundation of successful AI product development lies in choosing the right problems to solve. Rather than chasing general capabilities that major AI companies will eventually solve, focus on specialized, domain-specific applications where your organization can provide unique value. When evaluating potential AI features, consider both risk and return - particularly in enterprise contexts where brand reputation or compliance/legal risks are at stake.

Generalizing a bit:

- In internal tools, use cases that demonstrate greater efficiency and cost savings are usually prioritized, as these often have strong support from leadership
- In customer-facing products, it's interesting to differentiate between automation and augmentation use cases. While augmentation can improve over time and build user trust, automation is typically easier to implement since it replaces manual workflows without requiring changes in user behavior

[Biggest Challenge: Good Requirements and Iteratively Improving Use Cases in Production](https://langfuse.com#biggest-challenge-good-requirements-and-iteratively-improving-use-cases-in-production)

A common challenge is that LLM use cases are often not well specified. This applies across use cases:

- Chat applications are very open ended and it's hard to have a good understanding of all the different ways users will use the application
- Agentic applications that augment/replace a human workflow have more edge cases than initially anticipated
- Context retrieval/summarization suffers from context that is user-provided or changes over time

Usually a very good approach is to:

[Initial dataset](https://langfuse.com#initial-dataset)

Create a dataset of 50-200 examples that represent the production use case on a best effort basis.

[Gold standard responses and evaluations](https://langfuse.com#gold-standard-responses-and-evaluations)

Create "gold standard" responses for each example and implement evaluation to be able to reliably compare a response to the gold standard.

[Define target metrics](https://langfuse.com#define-target-metrics)

Set expectations with stakeholders on how good the responses need to be to be considered acceptable for an initial beta/production release. The goal here is to be able to release the use case early and learn from production feedback.

[Iterate against target metrics](https://langfuse.com#iterate-against-target-metrics)

Iterate on application in development to hit the target expectations.

[Release to production](https://langfuse.com#release-to-production)

Release the use case to production and use production evaluation / monitoring techniques to identify edge cases on which the application does not meet the quality expectations

[Close the loop](https://langfuse.com#close-the-loop)

Iteratively add these examples to the dataset to increasingly improve the quality of the performance benchmark used in development and make it more representative of the production use case

[Evaluations](https://langfuse.com#evaluations)

This workflow requires a robust evaluation framework built on four pillars:

- **Implicit User Feedback**is often overlooked although it helps capture production performance very effectively. It usually needs to be carefully designed as a part of the product UX.- *"If you build a customer success application and suggest a response to a user with an agent in the loop, if the agent doesn't edit the text and just hits send, that's probably good feedback, whereas if it's heavily edited, it's negative feedback."*
- **Explicit User Feedback**is simpler to implement as it only involves an explicit (👍/👎) button
- **Manual Expert Annotation**is what most teams try to avoid as it's expensive and time-consuming. However, it's often the only way to get a true sense of quality while also being the benchmark for any automated evaluation
- **Automated Evaluations**(like "LLM as a Judge") helps scale out the evaluation process but usually needs lots of iterations

[Implementation Best Practices](https://langfuse.com#implementation-best-practices)

-
**Decouple Prompt Engineering from Development**. Create separate workflows for prompt optimization and software development. This allows domain experts and product managers to iterate on prompts independently of engineering cycles. Some teams adopt a dedicated prompt engineering tool (e.g.[Langfuse Prompt Management](https://langfuse.com/docs/prompts)) for this.
-
**Do not neglect Latency Optimization in favor of perfect accuracy**. User experience significantly depends on response speed. Consider these strategies:- Optimize for fast initial token delivery so users see that something is happening
- Implement engaging loading states
- Pre-generate partial results where possible

-
**Do not build workarounds for current model limitations**. There are many issues that might limit the performance of an LLM application. Some of them will most likely be solved with future model releases, some are more specific to your use case. Generally it is advisable to focus most of the optimization efforts on the use-case related problems as these are the learnings that persist when new models are released.
-
**Do not over-optimize on costs in the early stages of the product lifecycle**. While cost concerns often dominate early discussions, they shouldn't overshadow value creation, especially in B2B contexts. Often the value to be created is much larger than the cost of the AI feature. Also, with new model releases, costs can go down significantly while the use case scales.
-
**Explore different implementation strategies**. There are many ways to implement an AI feature. When getting started, it is usually advisable to experiment with multiple different approaches to explore the space of possible solutions before optimizing a single approach for performance. This might otherwise lead to a local optimum. LLM application frameworks such as LangChain, Langgraph, or Llamaindex are a good starting point to explore different approaches and learn about the trade-offs.

[How to learn more as a PM](https://langfuse.com#how-to-learn-more-as-a-pm)

- Visit [learnprompting.org/docs](https://learnprompting.org/docs)for prompt engineering fundamentals
- We collected some good resources here: [langfuse.com/library](https://langfuse.com/library)
- Experiment with existing AI products to understand various UX patterns. Some core patterns emerge, and having a solid mental model of the different options is beneficial.
- Study implementations in your domain. What went well? What are particular pitfalls that are unique to your use case?
- It is highly recommended that you build your own prototypes, even as a non-technical PM. LLMs have made creating prototypes very accessible. Building with these tools will help you develop a good intuition for their capabilities and limitations. Many frameworks offer cookbooks and end-to-end examples that can be easily executed in platforms like Google Colab.

[Conclusion](https://langfuse.com#conclusion)

Successful AI product management requires balancing technical capabilities with user needs while maintaining clear quality standards. By focusing on specialized use cases, implementing robust feedback loops, and planning for technological evolution, product managers can build AI features that deliver real value while minimizing risks.
