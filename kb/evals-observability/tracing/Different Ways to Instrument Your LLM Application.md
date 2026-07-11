---
title: Different Ways to Instrument Your LLM Application
topic: evals-observability
subtopic: tracing
secondary_topics: []
summary: Survey of instrumentation approaches for LLM applications, focused on tracing
  and observability setup choices.
source: arize
url: https://arize.com/blog/different-ways-to-instrument-your-llm-application/
author: Evan Jolley
published: '2024-07-25'
fetched: '2026-07-11T04:49:12Z'
classifier: codex
taxonomy_rev: 1
words: 1116
content_sha256: 289e78e99814d46c886c4cfd5d6ea3b511d48fc1b19c82d78bb8b459ec285d72
---

# Different Ways to Instrument Your LLM Application

![llm-instrument-cover-art-blog](https://arize.com/wp-content/uploads/2024/07/llm-instrument-cover-art-blog-1000x560.jpg)

              # Different Ways to Instrument Your LLM Application

*Thanks to John Gilhuly for his contributions to this piece*

LLM instrumentation is the process of monitoring and collecting data in an LLM application, and it plays an important role in achieving the level of performance and reliability necessary in these systems.

This blog explores the different ways you can instrument your LLM application, comparing manual and automatic instrumentation techniques, and looking into the unique benefits that OpenTelemetry (OTEL) brings to the table. By the end, you’ll have an understanding of how to implement effective instrumentation strategies to improve the performance and reliability of your LLM applications.

## What Is LLM Tracing?

[LLM tracing](https://docs.arize.com/phoenix/tracing/llm-traces-1) is a tool for understanding how an LLM application is functioning. It involves monitoring and collecting detailed data on the flow of requests through a system which helps pinpoint issues and optimize performance.

Tracing helps track down various issues in LLM applications, such as application latency, token usage, and runtime exceptions among others. For example, it could highlight slow invocations of LLMs, display the breakdown of token usage to surface the most expensive LLM calls, capture critical runtime exceptions like rate-limiting, or view all documents retrieved during a retriever call. It can be used to view the embedding text used for retrieval, the parameters and prompts used when calling out to an LLM, the description and function signature of tools the LLM has been given access to, and the response of that LLM.

## How Is Otel Useful for Gen-AI Applications?

OTel enhances the tracing process by offering a standardized way to collect and format telemetry data. It integrates with various LLM frameworks and provides detailed insights into the performance and behavior of models. OTel helps to achieve increased visibility into an application’s internals, helping to better optimize and debug.

Several aspects make OTel particularly useful in LLM applications. It is vendor-neutral, allowing tracing of many different large language models and frameworks. It provides standardized data collection, offering a consistent way to collect and analyze telemetry data across different components of an application. However, while OTel does have automatic instrumentation options, these are not built with LLMs in mind. To properly instrument an LLM app, adding manual instrumentation or using an additional framework like OpenInference is necessary.

## What Is OpenInference?

OTel itself was initially created to capture tracing on many different kinds of applications. OpenInference is an extension of OTel that is specifically intended to provide detailed tracing on LLM apps. Like OTel, OpenInference is a vendor-agnostic open-source project. Though its main contributor and maintainer is Arize, it works with any OTel-compatible collector or backend. Similar to OTel, OpenInference also provides both manual and automatic instrumentation options.

## Automatic vs. Manual LLM Instrumentation

Automatic instrumentation automatically captures traces which allows for comprehensive coverage but offers less control over the details of what is traced. Manual instrumentation, on the other hand, involves explicitly adding traces to an application’s code. This allows for detailed control over what is traced but requires more effort to implement.

### Automatic Instrumentation

Arize natively supports collecting traces generated via [OpenInference](https://github.com/Arize-ai/openinference/tree/main) manual and automatic instrumentations. Automatic instrumentations offered by OpenInference today include [OpenAI](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/openai), [LlamaIndex](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/llamaindex), [LangChain](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/langchain), [MistralAI](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/mistralai), [DSPy](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/dspy), [AWS Bedrock](https://docs.arize.com/arize/integrations/aws-bedrock), and [Autogen](https://docs.arize.com/arize/large-language-models/tracing/auto-instrumentation/autogen). Below is an example of how to get started with the OpenAIInstrumentor

```
# Import open-telemetry dependencies
from arize_otel import register_otel, Endpoints
# Setup OTEL via our convenience function
register_otel(
    endpoints = Endpoints.ARIZE,
    space_key = "your-space-key", # in app space settings page
    api_key = "your-api-key", # in app space settings page
    model_id = "your-model-id", # name this to whatever you would like
)
# Import the automatic instrumentor from OpenInference
from openinference.instrumentation.openai import OpenAIInstrumentor
# Finish automatic instrumentation
OpenAIInstrumentor().instrument()
```
When the Arize SDK’s register_otel function does not offer enough customization, or your application is already using OTel to trace other calls, the opentelemetry_sdk can be used directly. Below is an example of this:

```
import os
# Import open-telemetry dependencies
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.sdk.resources import Resource
# Import the automatic instrumentor from OpenInference
from openinference.instrumentation.openai import OpenAIInstrumentor
# Set the Space and API keys as headers for authentication
headers = f"space_key={ARIZE_SPACE_KEY},api_key={ARIZE_API_KEY}"
os.environ['OTEL_EXPORTER_OTLP_TRACES_HEADERS'] = headers
# Set resource attributes for the name and version for your application
resource = Resource(
    attributes={
        "model_id":"openai-llm-tracing", # Set this to any name you'd like for your app
        "model_version":"1.0", # Set this to a version number string
    }
)
# Define the desired endpoint URL to send traces
endpoint = "https://otlp.arize.com/v1"
# Set the tracer provider
tracer_provider = trace_sdk.TracerProvider(resource=resource)
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))
tracer_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace_api.set_tracer_provider(tracer_provider=tracer_provider)
# Finish automatic instrumentation
OpenAIInstrumentor().instrument()
```
### Manual Instrumentation

Manual instrumentation enables flexible control over what aspects of an LLM application are traced. OTel offers three primary methods for manual instrumentation: using decorators, the `with` clause, and starting spans directly.

#### Decorators for Instrumentation

Using decorators is a straightforward way to instrument functions. By applying a decorator to a function, a span that tracks the function’s execution is automatically created. Decorators simplify the code by reducing the need for explicit span management, making instrumentation cleaner and more maintainable.

```
from opentelemetry import trace
tracer = trace.get_tracer(__name__)
@tracer.start_as_current_span("do_work")
def do_work():
    print("doing some work...")
```
#### The `with` Clause for Capturing Traces

Another method is to use the `with` clause to create spans. This technique involves wrapping code within a with statement that starts a span. This method is useful if there are specific blocks of code within or across functions that need to be traced. Starting a span within a with clause ensures that the span is automatically closed when the block exits, making the span readable and reducing the risk of forgetting to end spans.

```
def do_work():
    with tracer.start_as_current_span("span-name") as span:
        # do some work that 'span' will track
        print("doing some work...")
        # When the 'with' block goes out of scope, 'span' is closed for you
```
#### Starting Spans and Passing Context for Function Calls

When traces are needed in multiple non-contiguous sections of code, you can manually start spans and pass the application context as a parameter. This makes it possible to instrument complex workflows where a single `with` statement cannot encompass all the operations that require tracing.

```
def do_work():
    parent_span = tracer.start_span("parent")
    with trace.use_span(parent_span, end_on_exit=True):
        # do some work that 'parent' tracks
        print("doing some work...")
        child_span = tracer.start_span("child", parent=parent_span)
        with trace.use_span(child_span, end_on_exit=True):
            # do some work that 'child' tracks
            print("doing some nested work...")
        # Manually end the child span if not using 'with'
        child_span.end()
    # Manually end the parent span if not using 'with'
    parent_span.end()
```
## Questions?

Feel free to reach out in the [Arize community](https://arize.com/community/)!
