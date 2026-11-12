---
title: Introducing Baseten Chains
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- infra-platform/deployment
summary: Introduces Baseten Chains, an SDK for composing compound AI systems from
  independently-scaled 'Chainlets,' reporting halved processing time and 6x GPU utilization
  gains for a text-to-speech pipeline.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/introducing-baseten-chains
author: Bola Malek
published: '2024-06-26'
fetched: '2026-11-12T06:12:28Z'
classifier: claude
taxonomy_rev: 2
words: 1103
content_sha256: 1769c8792d3317786c3de7a75be15f99d67a02822d2f55f8b30e103629527323
---

# Introducing Baseten Chains

News
# Introducing Baseten Chains

Learn about Baseten's new Chains framework for deploying complex ML inference workflows across compound AI systems using multiple models and components


- Authors
- Date
- June 26, 2024

TLDR

Chains is a new framework and SDK designed for high-performance workflows using multiple models and components. In practice, we've seen processing times halved and GPU utilization improved 6x for use cases like text-to-speech applications. Sign up and try Chains today or check out our webinar to learn more!

Today, we're excited to announce the [beta release of Chains](https://docs.baseten.co/chains/overview), a framework and SDK designed to simplify the creation and deployment of [compound AI systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) featuring multiple models and components. We’re committed to continuously evolving our platform to deliver the best performance, reliability, and efficiency for the sophisticated AI products our customers build.  The release of [Chains](https://baseten.co/products/chains) represents a giant leap forward in that commitment to enhancing the performance and efficiency of AI infrastructure.

When we first built the [Truss framework](https://docs.baseten.co/truss-reference/overview), we wanted to simplify deploying and scaling models for real production use cases. Truss allowed AI engineers, data scientists, and MLOps teams to consistently serve different types of models using different frameworks in a reliable, performant, and secure manner. However, with the rise of compound AI systems and multimodal products, we knew we needed to evolve the framework to better facilitate workflows leveraging multiple models. Enter Chains.

At the [core of the Chains framework](https://docs.baseten.co/chains/overview#six-principles-behind-chains) is a vision to transform the landscape of AI model integration and multi-step workflow management. Traditional approaches often forced developers into monolithic architectures or cumbersome manual orchestrations. Using Chains frees developers from these constraints by providing a modular, scalable, and efficient method to compose and manage diverse AI workflows with precision.

Chains allow for the assembly of distinct computational steps into cohesive workflows. We achieve this modularity through user-defined components (Chainlets) that encapsulate functionality and can be chained together. Chainlets can be models or business logic, with their interactions defined as a standard Python program. Additionally, users can dictate all computational requirements like hardware resources, scaling, and more for each Chainlet.

By isolating computational steps into separate functions (Chainlets), Chains ensure that resources are allocated based on each Chainlet’s specific needs. Users can pick different GPUs and CPUs for each model or workflow component and add individual auto-scaling policies. This feature allows users to avoid the inefficiencies of overprovisioning, reduces operational costs, and maximizes hardware utilization.

Chains enhance operational efficiency and offer extensive customization options. Developers can tailor each Chainlet to their needs, from specifying compute hardware to customizing software dependencies. This flexibility ensures that our customers can seamlessly integrate new models or functions into existing Chains or adapt them for novel AI workflows.

python

```
class MistralLLM(chains.ChainletBase):
    # The RemoteConfig object defines the resources required for this chainlet.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The mistral model needs some extra Python packages.
            pip_requirements=[
                "transformers==4.38.1",
                "torch==2.0.1",
                "sentencepiece",
                "accelerate",
            ]
        ),
        # The mistral model needs a GPU and more CPUs.
        compute=chains.Compute(cpu_count=2, gpu="A10G"),
        # Cache the model weights in the image and make the huggingface
        # access token secret available to the model.
        assets=chains.Assets(
            cached=[MISTRAL_CACHE],
            secret_keys=["hf_access_token"]),
    )
```
The Baseten UI lets users view critical performance metrics across their entire Chain workflow. Users can view end-to-end latency and throughput to understand the health and performance of all their Chains workflows. As we continue to build out Chains, we’ll introduce more granular analytics to enable greater performance optimization.

We built Chains in response to customer feedback around the biggest challenges in their day-to-day jobs. They could not decouple managing resources and other infrastructure concerns from their workflows. This monolithic structure led to frequent overprovisioning of hardware or less-than-ideal structuring of interactions across workflow components. Chains let customers define the interactions between models and the hardware they run on in a loosely coupled but tightly integrated manner.

```
import truss_chains as chains
# This Chainlet does the work.
class SayHello(chains.ChainletBase):
  def run_remote(self, name: str) -> str:
    return f"Hello, {name}"
# This Chainlet orchestrates the work.
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):
  def __init__(self, 
      say_hello_chainlet=chains.depends(SayHello)) -> None:
    self._say_hello = say_hello_chainlet
  def run_remote(self, names: list[str]) -> str:
    output = []
    for name in names:
      output.append(self._say_hello.run_remote(name))
    return "\n".join(output)
```
For example, let’s look at an actual speech-to-text application. Many of our customers want a single endpoint to handle the transcription of all their audio files, regardless of size, with guaranteed SLAs. One way to do this is with a single development framework that takes the input audio, chunks it into smaller parts, uses a model to transcribe each chunk, and then reconstructs the complete transcript. When doing all of this on the same machine, we encounter problems like:

1. We experience poor GPU memory management since the GPU is idle while the audio is chunked.
2. Processing bottlenecks emerge as the autoscaling algorithm scales based on the number of input files, not the number of transcribed chunks.
3. We create monolithic deployments with tightly coupled processes running on a single machine.

In contrast, a Chain lets you place the processing code in a separate Chainlet, creating an efficient pipeline that scales with the workflow’s true load (corresponding to the length of all the audio files rather than the number of transcription requests).

In practice, we’ve seen **processing times halved and GPU utilization improved 6x**. Defining interfaces between Chainlets (supported via our Pydantic integration) lets us quickly test different chunking algorithms to create an optimal strategy for each use case.

With Chains, we’ve provided a set of out-of-the-box capabilities to streamline the development process. Features such as **auto-complete**, **static type-checking**, and a **simulated local execution environment** make building and testing AI models more intuitive and efficient.

Type checkability is critical for surfacing oversights before you deploy; instead of waiting 10 minutes to find that your model crashed, you get an actionable error message on your local machine in seconds. Type annotations improve code readability, understanding, and maintenance while clarifying input and output types for your team. Meanwhile, code completion helps avoid typos (like field names you could easily misspell in a YAML config) and accelerates your workflow.

You can try the beta for [Chains today with $30 in free credits](https://app.baseten.co/signup/?utm_source=Web&utm_medium=Blog&utm_campaign=Chains-Launch). Your insights will be crucial as we refine this technology to simplify delivering high-performance inference across multiple models.

To learn more about Chains and its future, [check out our webinar](https://www.baseten.co/resources/webinar/multi-model-inference-with-baseten-chains/) with Baseten CTO, co-founder Amir Haghighat, and Software Engineer Marius Killinger.

Chains sets the stage for the next generation of AI applications, empowering developers to build more dynamic, efficient, and effective AI solutions. Join us on this journey to redefine what is possible with AI infrastructure.
