---
title: Baseten Chains is now GA for production compound AI systems
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/baseten-chains-for-production-compound-ai-systems
author: Marius Killinger
published: '2025-02-06'
fetched: '2026-11-12T06:09:40Z'
classifier: null
taxonomy_rev: 2
words: 1038
content_sha256: 9d29a81915e2567b0446123278279b651b4b546157d1814f3d572aa0f0e5a56d
---

# Baseten Chains is now GA for production compound AI systems

News
# Baseten Chains is now GA for production compound AI systems

Baseten Chains delivers ultra-low-latency compound AI at scale, with custom hardware per model and simplified model orchestration.


- Authors
- Date
- February 6, 2025

TLDR

Baseten Chains is an SDK for deploying performant compound AI systems to production. Chains enables AI builders to ship ultra-low-latency compound AI with unique hardware and autoscaling for each step, eliminating performance bottlenecks and model orchestration headaches while keeping inference cost-efficient. With improved performance and developer tooling since beta, we’re thrilled to announce that Chains is now generally available!

Deploying compound AI systems requires a different toolset than single-model deployments. Traditional approaches often force developers to build monolithic deployments where workflows and hardware are tightly coupled, and intricate model orchestration must be manually implemented. But this can be cumbersome and error-prone, leading to excess hardware, engineering, and maintenance costs, as well as performance bottlenecks.

Serving compound AI systems performantly in production brings unique challenges around:

- **Model orchestration:** Managing multiple AI models and processing steps, as well as their data exchange.
- **Latency:** Since models and processing steps need to pass data to one another, compound AI systems can easily incur excess latency.
- **Reliability:** If one part of the system fails, the entire request fails.
- **Cost:** Without sufficient composability, you can end up paying for idle GPU time and unnecessary egress costs.

After working with industry leaders serving AI-native products at massive scale, we saw the need for a more efficient way to deploy compound AI systems in production. We set out to build a solution that lets you:

1. Deploy **ultra-low-latency compound AI systems**, with efficient data exchange between models.
2. Reduce hardware costs and eliminate performance bottlenecks with **custom hardware and autoscaling per model** or processing step.
3. Save time with an **expressive developer experience** and comprehensive observability.

That’s why we built Baseten Chains, a framework and SDK for serving highly-performant compound AI systems in production.

Now with additional performance and DevEx improvements since our beta launch, we’re thrilled to announce the general availability of Chains for production AI!

Baseten Chains is an SDK for building and deploying [compound AI workflows](https://www.baseten.co/blog/compound-ai-systems-explained/), built on top of our open-source model packaging library, [Truss](https://github.com/basetenlabs/truss). A “Chain” refers to your entire compound workflow, like a retrieval-augmented generation (RAG) or audio transcription pipeline. Chains are composed of “Chainlets,” the individual subtasks or business logic.

A Chainlet can be any model, data coordination, or processing step. For example, a transcription Chain could be composed of three Chainlets that:

1. Download and transform incoming audio, defining chunks for further processing (data coordination)
2. Detect silence using a voice activity detection (VAD) model, and chunk the audio accordingly (AI model and processing step)
3. Transcribe the audio (AI model)

Each Chainlet runs on its own hardware with custom autoscaling. In our transcription example, we can scale up many replicas of our chunking Chainlet to quickly chunk long audio clips in parallel. Chunking can be done on CPUs, so we can make our pipeline more cost-efficient by not using more expensive GPUs for this step.

[Chainlets call each other directly](https://www.baseten.co/blog/baseten-chains-explained/) without a centralized “orchestration executor.” This helps us keep latencies low by eliminating the need to retrieve and send intermediary results for each step in your workflow. It also makes building complex workflows intuitive, because combining Chainlets is like calling and combining “normal” Python functions.

You can build any compound AI system with Chains while gaining the model performance and fluid horizontal scaling that Baseten specializes in. A Chain is implemented in typed Python code; the Chains library handles all of the orchestration according to how you define Chainlet interactions in the code (including networking between models, choosing transport layers and protocols, serializing data, managing data types, and more).

For instance, the following code snippet builds a simple Chain that prints “hello” to each person in a list of provided names:

python

```
import asyncio
import truss_chains as chains
# This Chainlet does the work.
class SayHello(chains.ChainletBase):
    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"
# This Chainlet orchestrates the work.
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):
    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet
    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(
                self._say_hello.run_remote(name)))
        
        return "\n".join(await asyncio.gather(*tasks))
```
The code highlights how “chaining” two Chainlets is as easy as calling local, type-safe `async` Python functions, but we can easily implement more complex use cases. For instance, “SayHello” could be an LLM instead of a simple string template, allowing us to take more complex actions for each person.

Common use cases for Chains include:

- Agents
- AI phone calling
- [Audio transcription](https://docs.baseten.co/chains/examples/audio-transcription) (like our [world’s fastest Whisper](https://www.baseten.co/blog/the-fastest-most-accurate-and-cost-efficient-whisper-transcription/) implementation)
- Content creation (images, text, and video)
- Any custom, multi-step, or multi-model AI workflow

In addition to many stability improvements, our main focus since our beta release has been on further boosting performance and developer experience.

To boost performance, we’ve added:

- [**Output streaming**](https://docs.baseten.co/chains/guides/streaming) for lower initial response times
- [**Binary IO**](https://docs.baseten.co/chains/guides/binaryio) (extending the JSON-centered Pydantic ecosystem with NumPy array support and raw bytes) for performant serialization of numeric data

Since beta, we’ve also added feature support for:

- **Subclassing for easy reuse of Chainlets:** with minimal code changes, you can deploy a base Chainlet on different hardware, with different concurrency, dependencies, model weights, and more.
- **Chains Watch to live-patch deployed code:** run an exact copy of your production hardware and interface, with live code patching that lets you test changes rapidly.
- A **linter** to quickly identify Chains definition errors before pushing code, more expressive **logging**, and many UI improvements around **promoting**, **waking**, and **managing Chains environments**.

Baseten exists to provide the most performant, reliable, and scalable infrastructure for AI-native products. Chains enables AI builders to ship complicated multi-model workflows in a cohesive yet individualized way, coupling a delightful DevEx with ultra-low-latency inference, custom hardware, and massive horizontal scaling.

Chains is now GA, but we’re constantly leveraging customer feedback to push the boundaries of state-of-the-art model performance in production. For rapid multi-model inference and simplified [model management](https://www.baseten.co/platform/model-management/) for your production AI workloads [reach out to our engineers](https://www.baseten.co/talk-to-us/), and come talk to us at [NVIDIA GTC](https://www.baseten.co/resources/event/basten-nvidia-gtc/) or [KubeCon Europe](https://www.baseten.co/resources/event/baseten-kubecon-europe-2025/)!
