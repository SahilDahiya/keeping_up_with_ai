---
title: Fireworks AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/ai-agents-with-aws-agentcore
author: null
published: '2025-10-02'
fetched: '2026-08-12T06:30:57Z'
classifier: null
taxonomy_rev: 2
words: 380
content_sha256: 8cc53cec90f6e879c02977f484aeb3db2f17201a08c6cbb2f206fb6c7b6fa626
---

# Fireworks AI

Fireworks now integrates with AWS AgentCore, enabling developers to deploy AI agents with optimized inference on secure, serverless AWS infrastructure. Build locally, deploy globally with enterprise-grade security and automatic scaling.

[AWS AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) provides serverless infrastructure purpose-built for AI agents. It solves the operational complexity of deploying dynamic AI agents at scale by offering:

- •Serverless scaling with fast cold starts
- •Built-in security and session isolation
- •Framework flexibility - use any open-source framework, protocol, or model
- •Extended runtime support for complex multi-step agent workflows

This eliminates the need to manage containers, orchestration, or scaling infrastructure while maintaining enterprise security requirements.

Fireworks delivers the fastest, highest quality inference engine for agentic workloads. We provide optimizations like adaptive caching and speculative decoding that are critical for multi-turn agent interactions. Combined with AgentCore's serverless deployment, you get:

- •Speed where it matters: Sub-second latency for agent reasoning loops powered by Fireworks' optimized inference stack
- •AWS-native deployment: Deploy directly to your AWS infrastructure with no additional configuration
- •Enterprise ready: Leverage AWS security, compliance, and existing commitments while using Fireworks' inference engine.

To demonstrate this integration, we built two cookbooks using AgentCore Runtime and AgentCore Code Interpreter. These agents can read files, generate python code, run the code and interpret the results. The agents use state of the art open source models [Kimi K2 0905](https://fireworks.ai/models/fireworks/kimi-k2-instruct-0905) and [Qwen 3 Coder 480B](https://fireworks.ai/models/fireworks/qwen3-coder-480b-a35b-instruct) respectively.

The architecture shows the complete flow: develop your agent locally with your choice of models and frameworks, configure it with a Docker file, and deploy to AgentCore Runtime via AWS CodeBuild. Once deployed, users can invoke the agent through the Runtime endpoint with all infra handled serverlessly by AWS.

See our full documentation and both cookbooks in our [**documentation page**](https://fireworks.ai/docs/ecosystem/integrations/agentcore).

Ready to build production AI agents?

1. **Get your Fireworks API key** :[Sign up at fireworks.ai](https://fireworks.ai/)
2. **Review the integration guide** : [Fireworks + AgentCore documentation](https://fireworks.ai/docs/ecosystem/integrations/agentcore)
3. **Deploy your first agent** : Follow the [complete tutorial](https://github.com/fw-ai/cookbook/tree/main/integrations/AgentCore)

The integration supports serverless inference, fine-tuned models, and on-demand deployments. For enterprise deployments leveraging existing AWS compute please reach out to [aws@fireworks.ai](mailto:aws@fireworks.ai)

We will continue to expand our AWS AgentCore integration with additional cookbooks and deeper platform integrations. Stay tuned for more examples covering multi-agent systems, custom tool integration, and production deployment patterns.
