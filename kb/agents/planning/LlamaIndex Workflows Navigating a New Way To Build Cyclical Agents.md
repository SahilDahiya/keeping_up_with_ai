---
title: 'LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents'
topic: agents
subtopic: planning
secondary_topics:
- agents/tool-use
summary: Explains LlamaIndex Workflows as a pattern for building cyclical agents with
  explicit control flow.
source: arize
url: https://arize.com/blog/llamaindex-workflows-a-new-way-to-build-cyclical-agents/
author: John Gilhuly
published: '2024-08-08'
fetched: '2026-07-11T04:49:26Z'
classifier: codex
taxonomy_rev: 1
words: 1007
content_sha256: 714c93721c6f8ca435e122d2580c008f32b3d28bfce70277cfa6c6f6a3e9064d
---

# LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents

![llamaindex-workflows-get-started-conceptual](https://arize.com/wp-content/uploads/2024/08/llamaindex-workflows-get-started-conceptual-1021x560.jpg)

              # LlamaIndex Workflows: Navigating a New Way To Build Cyclical Agents

Last week, [LlamaIndex released](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex) **Workflows**, a new approach to easily create **agents**. Workflows use an event-based architecture instead of the directed acyclic graph approach used by traditional pipelines or chains. This new approach brings with it new considerations for developers looking to create agentic systems, as well as new questions on how to evaluate and improve these systems.

This blog dives into how workflows work and which use cases they are best suited for. This new technique shines when used with complex, multi-step processes — processes that are extremely difficult to debug and measure. To help alleviate these pains, we also dive into how Arize Phoenix can be used to trace and evaluate Workflows.

## What Are Workflows in LLM App Development?

Workflows are an orchestration approach that lets you define agents as a series of Steps. Each of these steps represents a component of your application, for example a call to an LLM or a call to a vector database to retrieve documents. Steps receive and emit events, and can access a shared context that allows them to pass data from step to step and keep a state across multiple runs.

This event-driven architecture means that there is no need to explicitly define the paths between nodes, or in this case, steps. Instead, steps can naturally transition between each other and loop back to previously traversed paths when they encounter errors. This makes workflows great at handling complex tasks with many different branching paths or loops.

## Workflows vs Graphs

The main alternative to the event-driven approach used by Workflows is a directed acyclic graph approach. The directed acyclic graph method requires you to define nodes and edges in your application, with nodes being operations or functions, and edges defining how the application can move between these functions. This approach is great for structured applications that use a set of predefined paths. However, this approach can be overly rigid and prevent applications from returning to previous steps, or conditionally jump between functions more often.

The event-driven approach used by Workflows gives more freedom to applications to jump around. By allowing steps to subscribe to events, Workflows remove the need to predefine each possible path.

Beyond their ability to handle intricate, looping flows well, workflows come with the additional benefit that steps can be more easily self-contained than nodes in a graph. Steps can be in full control of handling their inputs and outputs, instead of relying on the definitions of the edges connected to them. This makes defining things like optional or default values much easier.

To sum up, workflows are great at handling:

- Complicated agents, especially those that often loop back to previous steps
- Dynamic applications that use many optional and default variable values

While graphs are great at handling:

- Linear applications with rigid paths. For example, defining a workflow for an agent that simply calls an LLM and performs some form of structured data extraction may only add unnecessary complexity.

Ultimately, it all depends on your use case. Whichever approach you choose, having visibility into your application is critical. With that in mind, let’s dive into how you can trace your Workflows.

## How To Trace Workflows


The easiest way to visualize the paths taken by your Workflows is using Arize Phoenix. [Our integration](https://docs.arize.com/phoenix/hosted-phoenix#tracing-how-to-send-in-your-first-trace) allows you to easily visualize the step-by-step invocations of agents set up via Workflows, all without adding extensive logging code to your application.

To set up this integration:

First, create an account at [app.phoenix.arize.com](https://app.phoenix.arize.com/login)

Then, install the necessary packages to your application:

```
!pip install opentelemetry-sdk opentelemetry-exporter-otlp
!pip install "arize-phoenix[evals,llama-index]" "openai>=1" gcsfs nest-asyncio "openinference-instrumentation-llama-index>=2.0.0"
!pip install -U llama-index-callbacks-arize-phoenix
```
Next, enable Phoenix and connect it to your LlamaIndex application:

```
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter as HTTPSpanExporter,
)
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
# Add Phoenix API Key for tracing
PHOENIX_API_KEY = ""
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"api_key={PHOENIX_API_KEY}"
# Add Phoenix
span_phoenix_processor = SimpleSpanProcessor(HTTPSpanExporter(endpoint="https://app.phoenix.arize.com/v1/traces"))
# Add them to the tracer
tracer_provider = trace_sdk.TracerProvider()
tracer_provider.add_span_processor(span_processor=span_phoenix_processor)
# Instrument the application
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)
```
With that code in place, you are now able to see step-by-step traces appear in your Phoenix dashboard with each invocation of your agent. These capture inputs and outputs from each step, allowing you to easily debug and identify issues.

Implementing proper tracing is critical to get your application functioning properly. Once you get to a runnable, MVP state, however, evaluating and improving the performance of your application becomes even more important.

## Evaluating Workflows

Workflows can be evaluated using the same approach as evaluating any agent. Agents are typically complex enough that strictly evaluating full run-throughs of the application won’t tell you all that much. Instead, look to evaluate each step of the application independently.

The process can be broken down into these steps:

- Add tracing for visibility into your application
- Create a set of test cases (inputs and expected outputs) for your application
- Break your agent into discrete components
- For each of these components, define some sort of evaluation criteria
- Run your test cases through your application, measure the performance against your evaluation criteria
- Iterate on your app and repeat steps #2-5

Luckily, Workflows make step #3 even easier. Each step in your Workflow already represents a discrete component that can be evaluated.

This process can be implemented into your application natively, however Phoenix provides an Experiments feature that makes this significantly easier. For details on running an experiment in Phoenix, [see here](https://docs.arize.com/phoenix/datasets-and-experiments/how-to-experiments/run-experiments).

## Takeaways

Workflows are a great option for those building complex agents. The event-driven architecture significantly improves the developer experience when defining cyclical or potentially cyclical flows, and the discrete nature of each step simplifies passing variables between components.

They may not be critical for basic, linear applications, however Workflows are well worth becoming familiar with and considering when building your next agent.

For more examples of using Workflows with Arize Phoenix, check out these example notebooks:
