---
title: The Role of OpenTelemetry (OTEL) in LLM Observability
topic: evals-observability
subtopic: tracing
secondary_topics:
- infra-platform/deployment
summary: Explains OpenTelemetry’s role in LLM observability and why standard traces
  matter for production systems.
source: arize
url: https://arize.com/blog/the-role-of-opentelemetry-in-llm-observability/
author: Dat Ngo
published: '2024-10-08'
fetched: '2026-07-11T04:50:10Z'
classifier: codex
taxonomy_rev: 1
words: 3574
content_sha256: 4ed6f7e51e868a4d08b99cc5dadc775d7e28467dc6210d8ef4d16afbb29ce33b
---

# The Role of OpenTelemetry (OTEL) in LLM Observability

![The Role of OpenTelemetry in LLM Observability 3 The Role of OpenTelemetry in LLM Observability](https://arize.com/wp-content/uploads/2024/10/The-Role-of-OpenTelemetry-in-LLM-Observability-3-1021x560.jpg)

              # The Role of OpenTelemetry (OTEL) in LLM Observability

If you’ve ever tried developing–or harder yet, productionizing–an LLM application, you know that getting things to work as intended is not as easy as you think. Excluding demos on X, many folks struggle to build a quality LLM application into a viable product.

For the first time, many of us are designing systems that have to take into account non-determinism and much more variability occurring in the system than before. Things go off the rails more often, and break a lot more in the LLM world than in standard software. This can be hard to navigate, but with a little engineering rigor and lessons from software engineering, it doesn’t have to be so difficult.

So how do you actually build systems the right way? Based on my experience working alongside customers who have productionized real consumer facing LLM applications with real business ROI, I wanted to share some tidbits that I’ve learned that you might find helpful in your journey. And here’s the takeaway: *If you want to increase quality, you need to increase velocity. *

This might seem simple, but it’s a lesson from software engineering and testing cycles. The faster your testing cycles get, the more cycles you can iterate through in the same amount of time. Ultimately, you’ll be able to build a better quality system in the same amount of time.

For LLM development, you can reduce this iteration cycle time with LLM observability.

## What is LLM Observability and Why Does it Matter?

LLM observability is the ability to see what is happening in your LLM application, understand quickly how to mitigate issues, evaluate outputs, run root cause analysis, and ultimately improve your system. Having observability alongside your LLM application allows you to move much faster and farther than if you had to do this without any observability tooling helping you.

You can think of LLM development and LLM observability, as two sides of the same coin. They go hand-in-hand and when in sync, allow you to produce the best quality system efficiently. LLM observability isn’t just for production. It’s actually equally, if not more helpful in the development lifecycle.

And thus, the reason for this article: We’re going to talk about OTel and its role in LLM Observability

If you’re new to OpenTelemetry (OTel), this article will explain why it’s becoming a crucial component in monitoring and optimizing LLM performance, and in getting those testing cycles faster.

Even if you’re already familiar with OTel, there’s plenty of new information here for you. The world of LLM observability is ever evolving, and some exciting new design patterns are emerging—so read on to stay ahead of the curve.

## What is OpenTelemetry?

OpenTelemetry (OTel) is a framework designed to create and manage data from “telemetry” — which which is the automated process of collecting data from remote sources and transmitting for monitoring and analysis. As the open standard for telemetry data , OTEL gives us a standardized way to collect data on our software applications (and LLM applications). This allows us to get observability and all the benefits it provides.

Some examples of telemetry in action might include:

- Sensors in cars that can transmit diagnostic information to a manufacturer
- Sensors attached to wildlife that collect things like behavior or migration patterns for researchers
- Medical devices that can monitor and transmit vital signs

This matters not only in the software engineering world but also in the LLM world, because no one wants to be highly coupled with their observability platform. Having an open standard means that consumers win and can switch easily in the ecosystem. It’s become the long term standard, and is battle-tested over years of software development in the past decade.

OTel is comprised of 3 parts: traces, metrics, and logs. We’re mostly going to talk about traces in this post, which allow you to track and analyze the path of a request as it moves through different parts of a distributed system.

### Why You Should Use OpenTelemetry for LLM Apps

While very rare, some people might choose to use something outside of OpenTelemetry to form, emit and collect telemetry data. This approach is not ideal from an engineering perspective, and here’s why.

**Imagine for a second, not using OTel for your LLM observability, and instead using a vendor/non-standard instrumentation from some 3rd party to instrument your application (we’ll cover instrumentation later in the article). And let’s say down the road, you decide to switch your observability stack.**

*…You would have to rewrite all the lines of code you originally touched.*

**This is bad engineering.**

Using an open standard is best practice (and how most software is observed today), rather than being tightly coupled to something that isn’t standardized or vendor-specific. You want to avoid vendor lock in.

OpenTelemetry has great open-source support from the community, the standard is constantly adapting to changes, and is widely adopted by most developers in the software telemetry space.

Of course you could get observability to work using something outside of OpenTelemetry, but what I’m trying to convey is that it’s not ideal from an engineering perspective. Tightly coupled systems are fragile and end up needing more effort as things change. In the LLM ecosystem today, things are changing so quickly, it’s very likely that your stack and approach will also change.

## Using an Example to Understand OpenTelemetry and LLM Observability

Imagine you are the manager for a very advanced manufacturing line at Tesla, and you are tasked with implementing new processes, making things better and avoiding issues in these processes.

![Process for getting some visibility in a factory](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-09-at-9.46.27 AM-1024x230.png)

Here’s a problem you may have:

*“I have a complex manufacturing process where things go wrong, break or slow down. How do I have some visibility into what’s going wrong, so I can improve things over time?”*

In this real world example, what you might do is collect more data to see where things are going off the rails. Here’s how you might go about getting some visibility in this factory:

- First, decide what process you want to optimize. This part should be easy since you should know this domain, and you should generally know how this process works at a high level.
- You might set up some ways to collect data, let’s say for instance, you could set up cameras on the factory floor to see how workers are operating, and how processes are actually happening.
- After setting up the camera, you would then send the camera feed to some central server or place where you can see all the data in a single place.
- You’ll review footage when things slowed down or the process broke, likely from some really nice UI that allows you to replay, rewind and review the original footage.

### OTel in Software Engineering

In the software world, things aren’t so different–it’s just abstracted into the software terms.

![Comparison to software engineering](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-09-at-9.53.13 AM-1024x528.png)

Instead of observing a manufacturing line, you might be observing a software application, or some microservices architecture.

The setting up of cameras is equivalent to the instrumentation of code. Instrumentation is simply setting up some code to create, process and export telemetry data coming from your application. Basically, you’re adding some lines of code to watch some other code process.

Just like in the example of the Tesla manager, we’ll likely need to send or export the data using OTel exporters. Also, we might send to some central place, some OTel receivers or OTel collectors.

What’s important to note is that OTel collectors are actually comprised of three parts: receivers, processors, and exporters (we’ll review this later).

Finally, you’ll look at your telemetry data with a useful OTel compatible tool. For APM (application performance monitoring) observability some tools might be AWS XRay, HoneyComb, Datadog, etc.

### Benefits of OTEL for LLM Application Development

Now moving to LLM applications, there are very many similarities to the software engineering example we just reviewed.

![Arize's OpenInferences (OTel Compatible)](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-09-at-9.56.05 AM-1024x510.png)

I’m going to use the example of observability with the open-source library[ OpenInference](https://github.com/Arize-ai/openinference), which is our open-source OTel compatible instrumentation, and our other open-source package [Arize Phoenix](https://github.com/Arize-ai/phoenix) to view the trace data.

In comparison to the examples above, here’s what Arize’s OpenInference looks like, which is OTel compatible:

- Instead of a microservices architecture like in the software application, many LLM applications will either use a framework, or folks might choose to hand roll their own orchestration. This might include a router, its sub-component and/or some other complex LLM architecture.
- The instrumentation here is similar to OTel instrumentation, this time using OpenInference, but here we can take advantage of auto-instrumentation on any frameworks we might have. Since most LLM orchestration frameworks are open-source, we can easily form the OTel data using something like OpenInference (we will cover what OpenInference is later). And of course, if you’ve hand rolled your own custom orchestration, you can custom instrument like normal OTel.
- Since OpenInference is OTel compatible, it will use the already existing OTel exporters and receivers to send to the Arize Phoenix instance.
- Lastly, we can see our LLM traces and spans data to inspect, root cause, replay, curate into datasets, experiment and perform workflows that will help build a better LLM application like root causing, debugging, experimentation, etc.

![Example of LLM Traces and Spans in Arize Phoenix UI](https://arize.com/wp-content/uploads/2024/10/image1-1-1024x532.gif)

## A Deeper Dive into OTEL for LLM Observability

Below, we’ll review some of the major components that make up OpenTelemetry. Again this is not an exhaustive list of components and walkthrough, but just some pieces that I think are important to the reader in the context of this article. Again, I’ll use both Arize and Phoenix as examples, since both function similarly with regard to OTel.

![Chart describing Arize:Phoenix Usage of OTel](https://arize.com/wp-content/uploads/2024/10/image13.png)

### Instrumentation

This part is where telemetry data is created, and emitted. This helps make our system observable. Below is an example of how telemetry data is sent by our Open Source Project, Arize Phoenix.

There’s a lot to unpack here, but I’ve simplified how instrumentation works into some brief bullet points:

- Import OpenTelemetry: Use API for libraries, both API and SDK for services.
- Configure API: Set up tracer/meter with a name and version.
- Configure SDK: Define export options programmatically.
- Create Data: Generate traces/metrics using tracer/meter.
- Export Data: Send telemetry via exporters or the OpenTelemetry Collector

To summarize this step, this is where users will add some lines of code in their LLM application to start forming, and emitting telemetry data. The normal work flow is that you take a dev branch of your application, and start instrumenting the application. With OpenInference, this is generally an iterative process if you are custom instrumenting an application, or a few lines change if you are using a major LLM framework.

There are many examples of instrumentation in both the [OTel docs](https://opentelemetry.io/docs/concepts/instrumentation/), and in the [Arize Phoenix docs](https://docs.arize.com/phoenix/tracing/concepts-tracing/how-does-tracing-work#instrumentation https://opentelemetry.io/docs/concepts/instrumentation/) if you need tangible examples. I won’t go into super depth here, as instrumentation could be its own article, but just know it should be straight forward, but sometimes there are some idiosyncrasies as you get deeper.

### Exporters

An exporter takes the spans created via instrumentation and exports them to a collector. In simple terms, it just sends the data to some endpoint. Nothing fancy here, but it’s also good to know another term: **OpenTelemetetry Protocol** (or OTLP, for short) is the means by which traces arrive from your application at some endpoint you’ve chosen. Not much more to know than those two things.

Learn more about exporters in the OTel docs [here](https://opentelemetry.io/docs/concepts/components/#exporters).

### Processors

Processors modify or transform data collected by receivers before sending it to exporters, based on predefined rules such as filtering or renaming. Their order in the pipeline determines the sequence of operations. While optional, some processors are recommended.

A real use case is to use processors in an OTel collector to split trace data between LLM observability and APM observability as an example. It allows users to specify some logic if they need to.

Learn more about processors in the Otel docs [here](https://opentelemetry.io/docs/collector/configuration/#processors).

### Receivers

Receivers collect telemetry from various sources, using pull or push methods, and can support multiple data types. They are configured in the receivers section, often with default settings. Custom configurations override these defaults. The Collector requires at least one receiver.

Nothing remarkable about receivers here, other than they are built to receive telemetry data.

Learn more about receivers in the OTel docs [here](https://opentelemetry.io/docs/collector/configuration/#receivers).

### OTel Collector

The specific definition of an OTel collector goes as follows: An OTel Collector is made up of 3 major components, receivers, processors, and exporters. It might be a little confusing at first that a collector contains the exporter, but I’ll go into depth on this.

You can think of the OTel collector as a core building block for OTel. OTel was meant to work in distributed systems, so you could have patterns where collectors are sending to collectors and so forth, passing data and processing logic along the way. But, you don’t have to use this definition of OTel Collector. You can use the parts that are needed and drop the other components.

![Collector graphic from the OTel docs.](https://arize.com/wp-content/uploads/2024/10/Screenshot-2024-10-04-at-1.41.29 PM-1024x571.png)

### Semantic Conventions

Semantic Conventions in OpenTelemetry define standardized names for various operations and data, ensuring consistency across codebases, libraries, and platforms. These conventions apply to traces, metrics, logs, and resources, providing a common naming scheme.

The way you can think about these conventions or attributes, are fields that are going to be standardized in this framework. These conventions are the reason that things that OTel comptable, are indeed compatible.

Learn more about Semantic Conventions in the Arize docs [here, ](https://github.com/Arize-ai/openinference/blob/main/spec/semantic_conventions.md)and in the OTel docs [here](https://opentelemetry.io/docs/concepts/semantic-conventions/).

### Telemetry Data

I always found it helps to actually see what telemetry looks like, in this case, this is what telemetry data looks like from OpenInference. This is an example of a call to an LLM and the telemetry data collected as a json. This telemetry data helps make up trace hierarchy and all the associated data and attributes.

This makes sense to see OTel attributes like **start_time, end_time, **but also the need for additional custom attributes like **llm.input_message** that help us specifically with LLM observability and those workflows.

![opentelemetry data](https://arize.com/wp-content/uploads/2024/10/image11-940x1024.png)

## Advanced Concepts in OpenTelemetry

**What is OpenInference in Relation to OpenTelemetry? **

OpenInference is built on the foundations of OTel, but with some extra special LLM sauce. OpenInference is basically OTel, but at Arize, we added some extra semantic conventions (attributes) that are specific to the LLM observability world. This allows you to do some pretty cool workflows for troubleshooting, experimentation and beyond.

You might ask, “But what happens if I’m not using Arize Phoenix and choose to use some other OTel compatible back end?” Well those extra [semantic attributes](https://github.com/Arize-ai/openinference/blob/main/spec/semantic_conventions.md) in OpenInference will just become custom attributes in that new OTel compatible back end. They are completely compatible. That’s the beauty of OTel!

We encourage the usage of our tooling with our conventions (we think it has some pretty cool functionality) but you are free to choose your OTel tool of choice. As a good practitioner, I’m always going to advocate that you choose what works best for your situation even if it’s not our tooling.

### New Architecture Paradigms

As you get deeper into this space, you’ll notice some patterns that are brand new to the world, even to veteran OTel folks. One of these new patterns is understanding that for the first time we have a new ‘joining pattern’ in OTel.

Here are two situations where you might encounter this.

#### Situation 1

Even though we instrumented our application and we have traces and spans already in our observability platform, there are other pieces of data we need to attach to our traces and spans. We will need to attach things like LLM as a judge evals or user feedback data to our existing traces and spans to understand what traces may have performed well or not well, aka to discern signal from our data.

The need to attach data to trace/spans at a later time, is required because our LLM as judge evals process might be done a later time in batch for instance, or we might only want to choose to evaluate a sample of trace/spans due to cost constraints. With user feedback, aka thumbs up/thumbs down, a user might take a few minutes to give a signal to the chatbot that they are not having the best experience, but we don’t want to wait on their input in order to collect our telemetry and would rather send the telemetry data instantly.

We need to join this evaluation/feedback data on some identifier. But here’s the tricky part, the identifier used by OTel is generally a spanID. This spanID is non-deterministic and only available at instantiation. This is important to understand.

There are a few patterns that are emerging as industry practice:

- **Running Evals and Annotations Where Traces Live:**If your observability platform can perform your evals with data that exist in the trace/span data (no additional information is needed outside of trace & span data), the platform could run those evals where the traces/span live, and attach the eval data then and there. Same idea goes with human annotation. Everything can be done where the traces live, clean and easy.
- **Storing SpanIDs in Memory or on the Application Side:**This pattern might be more common with user feedback data. You would want to design a pattern that keeps the instantiated spanIDs in application memory for as long as a user is allowed to give feedback for a specific session or message. Meaning if a user gives feedback, we want the spanID to which this feedback data belongs to. The best way to do this is to have it available in the application memory. It is the cleanest pattern I’ve seen to date.- *ProTip: As an example you can store traces in memory, using built in*- [in_memory_span_exporter](https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-sdk/src/opentelemetry/sdk/trace/export/in_memory_span_exporter.py)from OTel
- **Joining on a Deterministic ID:**This helps us avoid the issue of having to save off non-deterministic spanIDs in memory. Deterministic IDs can be a concatenation of date, userIDs, etc.. Some identifier we know, that way our unique key is easy to attach feedback data or eval data to.

Sometimes we have different OTel traces in the same application and need to direct them effectively and efficiently. Here’s another pattern to be aware of:

#### Situation 2

Let’s say you have OTel traces that I need to send to your APM observability tool and your LLM observability tool, and they are both being set to the global Tracer Provider. How do you get the right traces to the right places?

Here’s what you could do:

- You could add attributes to the APM traces and the LLM traces to mark them, then send them to an OTel collector with processor logic to split the traffic. In this way, you wouldn’t have to touch the instrumentation as much, but you would have to create an OTel collector and define the logic.The collector approach centralizes trace routing, simplifies configuration changes, and offloads routing complexity from the application, though it introduces an additional component and potential latency.
- Alternatively, instead of using another OTel Collector to split the traces, you can use local tracers rather than the [Tracer Provider](https://opentelemetry.io/docs/concepts/signals/traces/#tracer-provider). Local tracers offer more direct control and potentially lower latency but require more complex application code and redeployment for changes.

For smaller, simpler setups, local tracers may be sufficient, while the OTel Collector is recommended for larger-scale deployments requiring flexibility and advanced processing.

**A Simple Working Example**

If you want to learn by doing, below is an example how this all works together using Arize Phoenix.

[You can also check out the Colab here.](https://docs.arize.com/phoenix/tracing/llm-traces-1)

```
import phoenix as px
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
import os
from gcsfs import GCSFileSystem
from llama_index.core import (
    Settings,
    VectorStoreIndex,
    StorageContext,
    set_global_handler,
    load_index_from_storage
)
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import llama_index
# To view traces in Phoenix, you will first have to start a Phoenix server. You can do this by running the following:
session = px.launch_app()
# Initialize LlamaIndex auto-instrumentation
LlamaIndexInstrumentor().instrument()
os.environ["OPENAI_API_KEY"] = ""
# LlamaIndex application initialization may vary
# depending on your application
Settings.llm = OpenAI(model="gpt-4-turbo-preview")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
# Load your data and create an index. Here we've provided an example of our documentation
file_system = GCSFileSystem(project="public-assets-275721")
index_path = "arize-phoenix-assets/datasets/unstructured/llm/llama-index/arize-docs/index/"
storage_context = StorageContext.from_defaults(
    fs=file_system,
    persist_dir=index_path,
)
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
# Query your LlamaIndex application
query_engine.query("What is the meaning of life?")
query_engine.query("How can I deploy Arize?")
# View the traces in the Phoenix UI
px.active_session().url
```
## Conclusion

I hope this article provided valuable insights into the basics of OTel, and the trends observed in the LLM observability space from some of the top LLM teams. My aim is to share some knowledge and best practices we’ve seen, and give a vantage point that might help you out in your own building. As always, I encourage you to do your own research (DYOR).

Check out some our free tooling:

- OSS [Arize Phoenix (](https://phoenix.arize.com/)[give us a star on GitHub!](https://github.com/Arize-ai/phoenix))
- [Arize Enterprise](https://arize.com/sign-up/)(includes a free tier)
