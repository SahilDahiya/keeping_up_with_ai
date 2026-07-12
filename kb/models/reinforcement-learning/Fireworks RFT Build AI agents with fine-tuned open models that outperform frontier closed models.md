---
title: 'Fireworks RFT: Build AI agents with fine-tuned open models that outperform
  frontier closed models'
topic: models
subtopic: reinforcement-learning
secondary_topics:
- agents/planning
summary: Explains reinforcement fine-tuning for building agent models that can outperform
  closed frontier models on target tasks.
source: fireworks
url: https://fireworks.ai/blog/fireworks-rft
author: null
published: '2025-11-10'
fetched: '2026-07-11T04:16:57Z'
classifier: codex
taxonomy_rev: 1
words: 958
content_sha256: 973a972e23beb66cc6074ff099cb25c536a380f02d3ddb439bf18eefafb97b40
triage: keep
skip_reason: null
---

# Fireworks RFT: Build AI agents with fine-tuned open models that outperform frontier closed models

Fireworks RFT enables you to fine-tune frontier open models like DeepSeek V3 and Kimi K2 for your agentic product. Genspark beat frontier closed model quality by 10% in less than a month. Vercel achieved 94% error-free code generation and 40X faster speeds. Fireworks RFT is easy to use for application developers, enterprises and researchers alike - taking you from local evaluator to production in hours. [Start training today](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models) — completely free through November 24, 2025

**Fireworks RFT is a managed service for reinforcement learning.**

Train open models to excel at your product use case—multi-turn agents, coding, or complex reasoning. Fireworks RFT makes RL training accessible: no infrastructure to manage, and a developer-friendly workflow to securely connect production environments with training. Optimizing a model for your specific use case significantly enhances quality, accelerates performance, and reduces cost.

**Genspark: Training Deep Research Agents**

Genspark used RFT to train large state-of-the-art open models for their Deep Research agent, which gathers and synthesizes information into actionable insights. In less than a month, they achieved +10% better quality vs a SOTA closed model, +33% more tool calls, and ~50% cost reduction.

Genspark’s CTO Kay Zhu said,"We are really excited to see what we were able to achieve by partnering with Fireworks. Fireworks enabled us to own our AI journey, and unlock better quality in just four weeks. This resulted in a better product experience for our customers."

Check out the full [Genspark x Fireworks case study](https://fireworks.ai/blog/genspark) for more details.

**Vercel: Training Code Fixing Models**

Vercel, a leading platform provider for full-stack web applications, used RFT to significantly boost its v0 AI code generation tool's performance and quality. This resulted in a 93% error-free generation rate, a 33% improvement over closed-source models, and 40X faster speeds that improved the product experience.

Vercel’s CTO, Malte Ubl, highlighted"Vercel's v0 model is a composite model. The SOTA in this space changes every day, so you don't want to tie yourself to a single model. Using a fine-tuned reinforcement learning model with Fireworks, we perform substantially better than SOTA."

Check out more details in the full [Vercel x Fireworks case study](https://fireworks.ai/blog/vercel).

Application developers need the best quality models for their specific use cases. Closed models offer limited customization and control—you can't use your own data or quality signals to tune them. Building and maintaining RL infrastructure in-house requires a specialized team and significant ongoing effort as new models come out and training techniques evolve.

Fireworks RFT is specifically designed to enable application developers, enterprises, and researchers to seamlessly and securely train models for product use cases:

Modern AI agents aren't single-shot. They're systems that gather information across multiple turns, use tools dynamically, maintain context, and make complex decisions. RFT is designed for these agents:

- •Deep Research Agents: Gather and synthesize information into actionable insights
- •Customer Support Agents: Handle complex issues requiring internal systems and context
- •Advanced Code Generation: Multi-step reasoning for complex code tasks
- •Domain-Specific Language: Generate structured outputs matching your exact format requirements

Fireworks RFT can help you improve model performance, quality, and tool calls for complex use cases.

Fireworks RFT eliminates infrastructure complexity by

- •Fully managing everything from high-performance GPU infrastructure to training orchestration
- •Seamlessly integrating with your production environment, via our open source Eval Protocol SDK
- •Building in observability to give you visibility into every tool call your agent makes, helping you understand and improve performance

Many companies need strict data controls to meet regulatory and compliance requirements. That’s why RFT is built with enterprise security and compliance in mind. Whether you're a startup or a Fortune 500 company, we offer training and deployment options that match your requirements:

- •Fully Managed Training: Everything is handled by Fireworks with SOC 2 and GDPR-ready compliance, with data encrypted both in transit and at rest.
- •Secure Training (Bring Your Own Bucket): For regulated industries requiring maximum control, use your own cloud storage and keep reward functions proprietary. Training data never persists on our platform beyond active workflows.
- •Full Range of Deployment options: including Bring Your Own Cloud (BYOC), on-demand, or reserved capacity.

Easily test with and train new models as the frontier evolves. Just swap out the base model and train again with your existing evaluator in our automated flow.

**Fireworks RFT helps you go from local evaluator to fine-tuned frontier models in production in hours. **It works seamlessly with your existing development environment. We standardize the end-to-end flow around these core components:

- •The Evaluator (The Goal): This function scores your model's output (0.0 to 1.0), defining what success looks like for your specific use case. A well-designed evaluator is key to achieving optimal quality aligned with your users' needs.
- •The Rollout (The Action): One complete run of your multi-turn agent in its environment. Running rollouts in your environment lets you leverage existing data, tools, and APIs.
- •The Training Loop: Fireworks manages the training loop - the rollout generates a trajectory and trace, the evaluator scores it, and the trainer updates model weights.

**Once training completes, deploy your fine-tuned models anywhere with Fireworks:** Bring Your Own Cloud (BYOC), serverless environments, on-demand instances, or reserved capacity.

Ready to start training? Our [Reinforcement Fine-Tuning documentation](https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models) has a complete guide to getting started, or check out our [quickstart video](https://www.loom.com/share/24ba433601de45ba8b63d9fb34c31fd5?t=72).

Now on the Fireworks Inference Cloud you can:

- **Serve**models at scale using the power of Firework’s Inference Cloud
- **Train**specialized models effectively with our upgraded Reinforcement Fine Tuning
- **Deploy**to production seamlessly with just one click
- **Monitor**performance and iterate for continuous improvement

If you need help with more advanced optimizations, our team provides deep expertise to ensure tailored performance, quality, and optimization for your needs. For inquiries, please email [[email protected]](https://fireworks.ai/cdn-cgi/l/email-protection#1b72756a6e72697e685b7d72697e6c74697068357a72), or connect with us on [Discord](https://discord.com/invite/mMqQxvFD9A).
