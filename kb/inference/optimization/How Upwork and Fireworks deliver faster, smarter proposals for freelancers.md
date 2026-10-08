---
title: How Upwork and Fireworks deliver faster, smarter proposals for freelancers
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- models/fine-tuning
- product-engineering/case-studies
summary: Upwork's Uma assistant serves custom Llama-3.1 LoRA models for real-time
  freelancer proposal drafting, using FireAttention v2 for long-context handling and
  FireOptimizer's quantization plus adaptive speculative execution to cut latency
  roughly an order of magnitude versus off-the-shelf open-source serving.
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/story-upwork-proposal
author: null
published: '2026-07-16'
fetched: '2026-10-08T06:11:16Z'
classifier: claude
taxonomy_rev: 2
words: 943
content_sha256: bdb5bcc2aaaabd9e9757401df28c51a62017ec78247662888b63fe141ed8a59b
---

# How Upwork and Fireworks deliver faster, smarter proposals for freelancers

[Upwork](https://www.upwork.com/), the world's largest work marketplace, connects businesses with independent talent across over 10,000 skills in categories like website & app development, creative & design, data science & analytics, among others. From startups to Fortune 100 firms, Upwork enables companies to collaborate with freelancers, boosting productivity and driving innovation through flexible, scalable workforce solutions.

Founded in 2015, Upwork has grown to become a leader in the work economy, facilitating over $3.8 billion in talent earnings as of last year. With a global reach and a diverse array of skill categories, Upwork continually innovates to meet the evolving needs of both businesses and freelancers in the digital age.

As Upwork scaled its AI initiatives and launched [Uma, Upwork’s Mindful AI](https://www.upwork.com/uma), they faced a critical challenge: how to deliver high-quality, instantaneous AI assistance in a complex, multi-model environment connecting millions of freelancers with businesses worldwide.

Upwork recently expanded the capabilities of its AI, Uma, across the Upwork platform experience, adding the ability for Uma to create tailored proposal drafts, assisting freelancers in crafting compelling job proposals quickly and effectively, to help them stand out and win more work. The new Uma capability:

- •Analyzes job postings to understand key requirements and preferences
- •Considers the freelancer's skills, experience, and past successful proposals
- •Generates tailored suggestions for proposal content, including relevant skills, experience highlights, and project approaches
- •Offers real-time writing assistance, helping freelancers articulate their value proposition clearly

*“Uma is the brain behind key parts of Upwork’s hiring and matching process. Features like Uma’s ability to create tailored proposal drafts helps reduce friction for freelancers by helping them accurately communicate their services and offerings, positioning their unique skill sets and expertise to clients to stand out and win more work.” - Andrew Rabinovich, Upwork’s Head of AI & Machine Learning*

Developing this feature required a solution that could:

- •Provide **ultra-fast inference** for **real-time** user interactions
- •Support **custom, task-specific AI** models for **superior results**
- •Scale efficiently to meet the demands of **a global user base**
- •Adapt to the diverse range of job categories and proposal styles on the platform.

Upwork chose Fireworks to power a key component of their custom-AI strategy within Uma, where multi-AI model workflows are being used to tackle key experiences in the hiring and matching processes.

Fireworks enables freelancers and businesses on Upwork to discover each other, get started, and complete more high-quality work by offering:

1. **Ultra-fast inference capabilities**: Essential for maintaining natural conversational flow and enabling rapid iterations in proposal writing. Fireworks' [FireAttention v2](https://fireworks.ai/blog/fireattention-v2-long-context-inference) technology allows for efficient processing of long contexts, crucial for understanding complex job descriptions and freelancer profiles.
2. **Seamless integration of custom LLMs**: Fireworks' Enterprise API plugs effortlessly into Upwork's Uma platform, making it as easy to use as any closed-source model provider. This allows Upwork to deploy custom Llama-3.1 LoRA models tailored to their specific use cases, enhancing the relevance and accuracy of AI-generated content.
3. **Advanced optimization and scaling**: Leveraging [FireOptimizer](https://fireworks.ai/blog/fireoptimizer), Fireworks ensures efficient resource use even at scale. This includes:
  - •[Quantization techniques](https://fireworks.ai/blog/fireworks-quantization) to reduce model size without compromising performance
  - •Adaptive speculative execution for optimal throughput
  - •[Multi-LoRA support](https://fireworks.ai/blog/multi-lora), enabling Upwork to fine-tune and deploy multiple task-specific models efficiently

Upwork implemented Fireworks' solution to serve custom AI models for Uma’s ability to create proposal drafts, with an eye towards future expansion. The implementation focused on:

- •Seamless integration with Uma, Upwork's existing AI platform
- •Flexibility to support a growing ecosystem of task-specific models
- •Continuous optimization using FireOptimizer, ensuring ongoing performance improvements

*“Fireworks offers incredible TTFT (time-to-first-token) and ITL (inter-token latency) without the need to manage our own machines.” - Zhao Chen, Director of AI & Machine Learning at Upwork*

In Upwork's marketplace, speed and quality of AI-enabled interactions are paramount:

1. **Real-time assistance**: Freelancers can receive instantaneous, tailored suggestions while crafting proposals, significantly reducing time-to-apply for jobs.
2. **Improved matching**: Faster, more accurate proposals lead to better matches between freelancers and clients, enhancing overall marketplace efficiency.
3. **Scalable performance**: As user engagement with AI features grows, Fireworks ensures consistent performance across millions of interactions.

Fireworks' advanced technologies, including FireAttention v2 and FireOptimizer, play a crucial role in delivering this high-speed, high-quality AI experience across Upwork's platform.

*“Not only were latency metrics nearly an order-of-magnitude less than off-the-shelf open-source options with the hardware we had access to but total cost of ownership was reasonable compared to procuring similar hardware internally.” - Zhao Chen, Director of AI & Machine Learning at Upwork*

The Fireworks partnership not only powers some of Upwork's current AI features but also opens doors for ongoing optimization and innovation:

1. **Continuous model refinement**: Fireworks' infrastructure, particularly its multi-LoRA support, enables Upwork to rapidly iterate on their AI models, ensuring they evolve with the platform's needs.
2. **Scalable AI integration**: As Upwork expands AI capabilities across their platform, Fireworks provides the necessary scalability and performance through technologies like FireOptimizer and FireAttention v2.
3. **Performance optimization**: Adaptive serving capabilities, powered by FireOptimizer, allow Upwork to continually enhance AI performance while managing resources efficiently.

And while the spotlight has been on LLM-powered workflows, Fireworks also offers [multimodal](https://fireworks.ai/blog/multimodal-enterprise), vision, audio and image generation models as part of the model library.

- •**Explore custom AI solutions**: Learn how to develop and deploy custom AI models tailored to your specific use cases with [multi-LoRA technology](https://fireworks.ai/blog/multi-lora).
- •**Optimize your AI performance**: Discover how [FireOptimizer](https://fireworks.ai/blog/fireoptimizer) can enhance your AI models' speed and efficiency.
- •**Join our community**: Connect with other developers and the Fireworks team in our [Discord channel](https://discord.gg/fireworks-ai).
- •**Get in touch**: Ready to transform your AI strategy? [Contact us](https://fireworks.ai/contact) to discuss how Fireworks can power your next-generation AI features.
