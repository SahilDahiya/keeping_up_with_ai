---
title: Building multi-component AI workflows at scale with Chains
topic: product-engineering
subtopic: architecture
secondary_topics:
- agents/tool-use
summary: Explains multi-component AI workflows with Chains, including orchestration
  across model and application steps.
source: baseten
url: https://www.baseten.co/blog/baseten-chains-explained/
author: Marius Killinger; Rachel Rapp
published: '2024-07-02'
fetched: '2026-07-11T04:09:29Z'
classifier: codex
taxonomy_rev: 1
words: 2544
content_sha256: c44bd9edce3c64434636d639c3a61fde0c54d16dcf774457814a5b60549bdfc5
triage: keep
skip_reason: null
---

# Building multi-component AI workflows at scale with Chains

![Baseten Chains explained](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747441077-chains-explained.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

![A gif showing the flow of data through a modularized workflow built with Baseten Chains](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1719484777-cleanshot-2024-06-26-at-13-37-09.gif%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A Baseten speech-to-text Chain with autoscaling for each step

A Baseten speech-to-text Chain with autoscaling for each step## Why we built Chains 

We first built [Truss](https://docs.baseten.co/deploy/overview), an open-source Python package, to simplify the complex problem of packaging, serving, and deploying ML models. Truss provides a unified approach to seamless production deployments and portability for version control and sharing. Model deployments with Truss on Baseten now run millions of requests every day for our customers' production ML inference workloads.

However, after working with so many AI builders, we saw the increasing need to expand inference capabilities in a new direction. Our customers found that:

- They were often writing cumbersome scripts to coordinate inference across multiple models.
- They were paying too much for hardware by not separating CPU workloads from GPU ones.
- They couldn’t quickly test locally, which drastically slowed down development.

Engineers frequently need to deploy several remote services that work together efficiently, each performing a particular sub-task on custom-configured hardware. They want to orchestrate the data flow between those services, and it should be as easy as writing any conventional Python program.

That’s why we built Chains.

## Chains design goals

Baseten Chains is a Python framework for building and orchestrating multi-component AI workflows with optimal scaling for each component. For a higher-level overview of the key features of Chains, check out our [Chains launch blog post](https://www.baseten.co/blog/introducing-baseten-chains/). Here we'll cover the more technical details of Chains design and implementation.

Chains are composed of “Chainlets,” modular services that can be linked together for real-time inference. They enable developers to combine business logic with ML models, making building model pipelines easy, performant, and robust.

### A delightful developer experience

Based on feedback from our customers, our goal was to enable:

- Modularized inference pipelines with a holistic developer experience.
- Optimal hardware utilization for each step in the pipeline.
- Local testability, type-checking, and code quality enforcement.

We wanted building modular workflows to make sense instantly in an IDE. Remote procedure calls (RPCs, or calls that execute code on a remote server via a local client) should feel like regular Python with code completion and type-checking. Users should not have to worry about data serialization, transport layers, authentication, retries, or propagating errors raised in remotes.

With this in mind, we constrained a potential code generation phase to the deployment process to ensure it didn’t interrupt the coding experience. Classes and functions must retain their typed signatures, allowing a rapid local feedback loop to catch common errors (think typos in names, wrong argument orders, or types) and avoid time-consuming deployment cycles.

### Computational expressivity

We wanted to give users flexibility in the computational graph structures they can compose. Chainlets call each other directly without a centralized “orchestration executor” or “workflow type” turning them into an executable application. Since each Chainlet is already a service, we instead designate one Chainlet as the “entry point” to the workflow. This Chainlet is served as the client-facing API.

The code that runs in each Chainlet supports control flow, conditional execution, and fanning out multiple RPCs to other Chainlets. The overall workflow (Chain) is an emergent concept defined by your Chainlets’ dependency structure and control flow. In other words, to code a Chain with the SDK, you only have to implement Chainlet classes; all your Chainlets together implicitly make up the Chain. Then, each time you deploy a Chain on Baseten, it gets its own version ID and can be managed on the status page of the Baseten UI.

### Extensibility with Truss

![The Baseten Truss logo](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1719946181-1677613813776.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

From customers, we received feedback that [Truss](https://docs.baseten.co/deploy/overview) sometimes feels restricting:

- Specifying configurations in separate YAML files creates a disconnect from their model implementation code.
- Code organization is restricted to a special “packages” directory, breaking Python import assumptions and IDE introspection.
- Truss error detection is challenging due to implicit class contracts, not inheriting from standardized base classes, or using concrete type interfaces for init arguments.
- Insufficient tooling for local execution can slow development speed and lead to errors being overlooked before remote deployment.

While enabling multi-component workflows was our primary focus, we also used the development of Chains as an opportunity to address these pain points with Truss and improve the developer experience for any model deployment.

To make Chains a viable alternative to Truss, we also included all popular Truss model capabilities in Chains: deploying your code, creating Docker images with your exact software requirements, and automatically bundling data dependencies on Baseten quickly. You can control what hardware you run on, including ML accelerators, auto-scaling up and down to zero, fast cold boosts, and more.

Most of these functionalities transparently reuse existing Truss features, applied Chainlet per Chainlet. In addition, we implemented the ability to develop a Chain with multiple Chainlets, some with non-trivial dependencies, while working in a single source tree with coherent code introspection.

## How we built Chains

While it’s technically possible to manually implement what Chains does with bare HTTP requests, it would involve:

- Writing extensive boilerplate code.
- Risking errors due to incoherent request-response payload types.
- Obscuring meaningful application logic with additional code, which makes complex applications hard to write and maintain.

These problems are often addressed unsatisfactorily by:

- RPC frameworks like gRPC that generate interfaces in an explicit build phase, but are heavyweight and disrupt the coding flow.
- Frameworks that generate classes dynamically or depend on Python decorators, which often undermine code completion and type checking.

We took all of this into account while building Chains. Let’s dive into the details.

### Chainlets

Chainlets are modular services linked together to form a full workflow (your Chain). For Chainlets to leverage one another, they need to be explicitly declared as dependencies and provided as an init argument.

```
@chains.mark_entrypoint
class MyChainlet(chains.ChainletBase):
  def __init__(self, other_chainlet = chains.depends(OtherChainlet, retries=3)) -> None:
    self._other_chainlet = other_chainlet
```
Chainlets must always be declared as dependencies and not instantiated directly. `chains.depends()` enables the framework to track dependencies and offers advanced customization of RPCs, such as for retries and timeouts.

Each Chainlet must follow a class contract with only one public element as its API: the `run_remote()` method. The only requirement of this method is that signatures must be fully type-annotated for proper input and output serialization. Simple Python types (like `int`, `str`, or `list[float]`) or user-defined Pydantic models (for complex/nested types) are allowed.

The function body can contain arbitrary code; RPCs can be made to other Chainlets, and the return values can be used directly. For example:

```
async def run_remote(self, text: list[str], parameter: int) -> tuple[bool, float]:
    value = 0
    for x in text:
        value += await self._other_chainlet.run_remote(text)  # RPC
    if value > parameter:
        return (False, value)
    return (True, value)
```
These two ingredients—the `chains.depends()` directive, and the way to call other Chainlets with control flow—are all you need to compose arbitrary computational graphs.

The `run_remote()` method is the only public API of a Chainlet and the only point other Chainlets can interact with (any attribute values or properties cannot be accessed). This is because these Chainlets are distributed servers, not local Python class instances. While the public API has this rigid yet simplistic structure, you can use private attributes and helper methods to structure your implementation code appropriately.

### Remote deployment

You might be wondering: where is the connection between these seemingly local Python classes and the deployed services?

The magic happens when a Chain is deployed to Baseten with this CLI command:

`truss chains deploy my_chain.py`The framework knows that `MyChainlet` is the targeted entrypoint in the source file because of the `mark_entrypoint` tag (alternatively, you can provide the class name as a CLI argument). It also knows that this Chainlet depends on `OtherChainlet`, because it was marked with the `chains.depends()` directive. 

To ensure a clear schema for serializing data over the transport layer, Pydantic models are created for the inputs and outputs of the `run_remote()` method. For `OtherChainlet` to be used in `MyChainlet` via RPCs, a “stub” is created: a class that implements the same protocol as `OtherChainlet` but delegates the actual work execution to the remote instance.

![A diagram showing function calls between four Chainlets part of a local Baseten Chain](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1719931927-marius-tech-post-fig-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

The stub class internally creates a remote session for the deployed OtherChainlet service, handling the packing and unpacking of the request and response payloads, authorization, and retries. Then, a wrapper class is generated for each Chainlet, which injects the generated stubs in place of dependency Chainlet instances and transforms each Chainlet into a FastAPI server. The generated Pydantic models define the request and response schemas.

Finally, all generated Chainlet servers are deployed on Baseten (analogous to deploying Truss models).

![A flow chart showing the RPCs and data flow between four Chainlets part of a Chain deployed to Baseten](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1719932052-marius-tech-post-fig-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Each Chainlet runs in a Docker container with autoscaling and dedicated hardware (e.g. GPUs)

Each Chainlet runs in a Docker container with autoscaling and dedicated hardware (e.g. GPUs)Even though much of the code looks like normal Python and a local execution mode is possible, we chose the method name `run_remote()` because we want users to remain aware of the RPC that is “hidden” in its invocation. Local Python functions could be slow or raise an exception for various reasons; RPCs can take long or fail for the same reasons. Additionally, they can lag due to network latency, any added overhead, or overload of the remote service, which may also lead to failures and timeouts.

### ML dependencies

In practice, one Chainlet (e.g., for serving a large ML model) may require special Python packages and hardware drivers, while other Chainlets do not. In the remote deployment, the automatic Docker image build ensures each Chainlet runs in the environment it needs. But how does this work during local development?

To ensure coherence across the overall Chain application, all Chainlets are defined in a single source file (or multiple files imported in the same local Python runtime). To support this, we selectively deviate from the general Python style guideline of placing imports at the top of the file and instead place Chainlet-specific imports in the `init` of individual Chainlets as needed.

```
1import truss_chains as chains
2import numpy as np
3
4
5class PhiLLM(chains.ChainletBase):
6    remote_config = chains.RemoteConfig(
7        docker_image=chains.DockerImage(
8            pip_requirements=[
9                "numpy",
10                "transformers==4.41.2",
11                "torch==2.3.0",
12            ],
13        ),
14    )
15
16    def __init__(self) -> None:
17        import torch
18        import transformers
19
20        self._model =
21        transformers.AutoModelForCausalLM.from_pretrained(
22            "microsoft/Phi-3-mini-4k-instruct",
23            torch_dtype=torch.float16
24        )
25        ...
26
27
28class PoemGenerator(chains.ChainletBase):
29    remote_config = chains.RemoteConfig(
30        docker_image=chains.DockerImage(
31            pip_requirements=["numpy"],
32        ),
33    )
34
35    def __init__(self, phi_llm:
36    PhiLLM=chains.depends(PhiLLM)) -> None:
37        self._phi_llm = phi_llm
38
39    def run_remote(self, words: list[str]) -> list[str]:
40        ...
```
Common dependencies, such as NumPy, are imported at the top of the script and included in the Docker images of both Chainlets. In contrast, PyTorch (`torch`, which contains large GPU binaries) is only included where needed: in the `PhiLLM` Chainlet.

All common dependencies (top-level imports) must be installed in the local development environment. Since only the Chainlet definition code is executed during the deployment process (not the actual implementations, `run_remote()` and `__init__`), installing other packages (such as `torch`) is not required to work locally, although it is beneficial for full code introspection.

### Local debugging

Chains supports local testing and debug execution, two improvements on Truss. In the simplest case, local instances of Chainlets are instantiated and run, altogether leaving out the code generation and remote deployments. You only need to instantiate the entrypoint Chainlet in `chains.run_remote()`.

While installing all software dependencies (such as `torch`) in your local development environment may be possible, access to accelerator hardware required by specific models is not always possible. In this case, Chains allows a hybrid testing mode, where hardware-hungry Chainlets can be substituted during local execution with a fake implementation. This allows us to test the business logic of all the remaining components.

```
class FakePhiLLM:
    def run_remote(self, messages: Messages) -> str:
        return "A Fake poem."
   
with chains.run_local():
    poem_generator = PoemGenerator(phi_llm=FakePhiLLM())
    print(poem_generator.run_remote(["moon", "sun"]))
```
## A Chains user story

One exemplary use case for Chains is speech-to-text transcription for long (2+ hours) audio files.

Staying within the typical constraints of HTTP request-response semantics, we want our transcription to finish in a few minutes at most. Since ML transcription models can only handle short audio snippets (up to 30 seconds), the file must be split into small chunks. Instead of downloading and chunking the input file serially, concurrent partial downloads can speed this up.

We want to spare the expensive GPU node any work that can be done on the cheaper CPU ones, for example, by separating the I/O and coordination logic (which can be done on CPU) from the “raw” transcription (which happens on the GPU). Having CPU-bound operations block an idle GPU is a needless cost and a waste of resources.

Given these constraints, Chains allows us to build an optimized transcription pipeline like this:

- An entrypoint Chainlet receives the transcription request and defines chunks to be processed in parallel (e.g., 5-minute audio segments).
- Each audio chunk is delegated to a separate Chainlet, which makes a range download (i.e., downloads only the relevant 5-minute segment). Smaller 30-second chunks are then created and sent to the transcription Chainlet.
- Each Chainlet processes multiple requests in parallel, auto-scales based on demand, and only uses the hardware and dependencies it requires (CPUs for audio chunking and GPU for the transcription).
- All Chainlets collect the results of their sub-tasks and send them back to their caller.
- Finally, the top-level Chainlet returns the complete end-to-end transcription to the client.

This particular Chain is explained in more detail and with complete code in our [audio transcription guide](https://docs.baseten.co/chains/examples/audio-transcription) in the docs, where you can also find another end-to-end example of [how to build a RAG pipeline with Chains](https://docs.baseten.co/chains/examples/build-rag).

## The future of Baseten Chains

After seeing the impact Chains has had on so many customers, we’re excited to release it as a beta feature to a broader audience.

Like any beta feature, this also means improvements and functionality will be added on a rolling basis. While we’ve built the holistic framework that abstracts away the transport layer between Chainlets, one of our first priorities is to make it even more performant. We currently use HTTP with JSON payloads, and both can be upgraded with more effective implementations. Another performance optimization could be guaranteed co-location of Chainlet deployments.

We've implemented validations upon Chainlet definition to enforce correct usage and guide users. However, they are heuristic and not foolproof; improvements could include type checker plugins or additional deployment integrity checks. We have considered a function-based approach, which would eliminate some of the API and typing complications resulting from a class-based system. However, with pure functions, it would become less convenient to make static resources (like loaded models) available to the function body, so we did not pursue this.

All that said, customers are already leveraging Chains effectively, enjoying blazing-fast audio-to-text for large inputs. We’re looking forward to user feedback and feature requests, and we’re already hard at work on the next iteration of Chains!
