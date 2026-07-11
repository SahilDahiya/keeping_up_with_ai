---
title: Trace complex LLM applications with the Langfuse decorator (Python)
topic: evals-observability
subtopic: tracing
secondary_topics:
- product-engineering/architecture
summary: Shows how to trace complex Python LLM applications with the Langfuse decorator,
  including nested calls, metadata, and observability patterns for multi-step workflows.
source: langfuse
url: https://langfuse.com/blog/2024-04-python-decorator
author: null
published: '2024-03-24'
fetched: '2026-07-11T04:34:33Z'
classifier: codex
taxonomy_rev: 1
words: 1454
content_sha256: 460051d9b42b0f2385dc62a0a0ca2113a35bcf52e7cc8081f3b4958e80fefa63
---

# Trace complex LLM applications with the Langfuse decorator (Python)

# Trace complex LLM applications with the Langfuse decorator (Python)

When building RAG or agents, lots of LLM calls and non-LLM inputs feeds into the final output. The Langfuse decorator allows you to trace and evaluate holistically.

![Picture Marc Klingen](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fmarcklingen.jpg&w=96&q=75) Marc

Marc![Picture Hassieb Pakzad](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fhassiebpakzad.jpg&w=96&q=75) Hassieb

Hassieb**Note:** This blog post references our Python SDK v2. We have a new,
improved SDK available based on OpenTelemetry. Please check out the [SDK
v3](https://langfuse.com/docs/sdk/python/sdk-v3) for a more powerful and
simpler to use SDK.

When we initially built complex agents for web scraping and code generation while in Y Combinator, we quickly recognized the need for new LLM-focused observability to truly understand how our applications produced their outputs. It wasn't just about the LLM calls, but also the retrieval steps, chaining of separate calls, function calling, obtaining the right JSON output, and various API calls that the agents should perform behind the scenes. In the end, all these steps led to them breaking many times on our initial users.

This insight prompted us to start working on Langfuse. As many teams were experimenting, we prioritized easy integrations with frameworks like LangChain and LlamaIndex, as well as wrapping the OpenAI SDK to log individual LLM calls. As applications become increasingly complex and agents are deployed in production, the ability to trace complex applications is even more crucial.

[Traces](https://langfuse.com/docs/tracing) are at the core of the Langfuse platform. Until now, generating a trace was straightforward if you used a framework. However, if you didn't, you had to use the low-level SDKs to manually create and nest trace objects, which added verbose instrumentation code to a project. Inspired by the developer experience of tools we admire, such as Sentry and Modal, we created the `@observe()` decorator for Langfuse to make tracing your Python code as simple as possible. Note: we plan to revamp our JS/TS tracing as well.

This post is a deep dive into the `@observe()` decorator, our design objectives, challenges we faced when implementing it, and how it can help you trace complex LLM applications.

*tldr:*

![Decorator Meme](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2Fpython-decorator%2Fdecorator-meme.jpg&w=3840&q=75)


[Introduction](https://langfuse.com#introduction)

In this video, we introduce the decorator and why we think it's an awesome abstraction to merge all Langfuse integrations. *If you are familiar with it, skip this video and jump to the next section.*

[Goals](https://langfuse.com#goals)

When starting to work on the decorator, we wanted to make everything simple that's complex when manually instrumenting your code. Consider this real-world trace of a complex agent, where maintaining the nesting hierarchy manually using the low-level SDK used to come with additional complexity and boilerplate code.

*Example of a nested trace with multiple LLM, non-LLM calls and a LangChain chain*

The goal of the `@observe()` decorator is to abstract away the complexity of creating and nesting traces and spans, and to make it easy to trace complex applications.

The decorator should:

- Trace all function calls and their outputs in a single trace while maintaining the nesting hierarchy
- Be easy to use and require minimal changes to your code
- Automatically capture the function name, arguments, return value, streamed completions, exceptions, execution time, and nesting of functions
- Be fully compatible with the native [Langfuse integrations](https://langfuse.com/integrations)for LangChain, LlamaIndex, and the OpenAI SDK
- Encourage reusable abstractions across an LLM-based application without needing to consider how to pass trace objects around
- Support async environments for our many users that run performance-optimized LLM apps

[Design decisions](https://langfuse.com#design-decisions)

- The decorator reuses the low-level SDK to create traces and asynchronously batch them to the Langfuse API. This implementation was derived from the PostHog SDKs and is [tested](https://langfuse.com/guides/cookbook/langfuse_sdk_performance_test)to have little to no impact on the performance of your application.
- The decorator maintains a call stack internally that keeps track of nested function calls to reflect the observation hierarchy in the trace.
- To be async-safe, the decorator leverages [Python Contextvars](https://docs.python.org/3/library/contextvars.html)for managing its state.
- The same `observe()`decorator is used to create a trace (outermost decorated function) and to add spans to the trace (inner decorated functions). This way, functions can be used in multiple traces without needing to be strictly a "trace" or a "span" function.

[Limitation: Python Contextvars and ThreadPoolExecutors](https://langfuse.com#limitation-python-contextvars-and-threadpoolexecutors)

The power of observability is most visible in complex applications with production workloads. Async and concurrent environments are common in these applications, and the decorator should work seamlessly in these environments. The decorator uses Python's `contextvars` to store the current trace context and to ensure that the observations are correctly associated with the current execution context. This allows you to use the decorator in reliably in async functions.

However, an important exception are Python's ThreadPoolExecutors and ProcessPoolExecutors. The decorator will not work correctly in these environments, as the `contextvars` are not correctly copied to the new threads or processes. There is an [existing issue](https://github.com/python/cpython/pull/9688#issuecomment-544304996) in Python's standard library and a [great explanation](https://github.com/fastapi/fastapi/discussions/9006) in the fastapi repo that discusses this limitation.

In short, the decorator will work correctly in async environments, but not in ThreadPoolExecutors or ProcessPoolExecutors.

[Before and after](https://langfuse.com#before-and-after)

[Status quo: Low-level SDK](https://langfuse.com#status-quo-low-level-sdk)

The low-level SDK is very flexible but it is also *very* verbose and requires passing of Langfuse objects.

```
from langfuse import Langfuse
from langfuse.openai import openai # OpenAI integration
langfuse = Langfuse()
def story(trace):
  span = trace.span(name="story")
  output = openai.chat.completions.create(
        model="gpt-4o",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
        trace_id=trace.id,
        parent_observation_id=span.id
    ).choices[0].message.content
  span.end(output=output)
  return output
def main():
  trace = langfuse.trace("main")
  return story(trace)
```
`@observe()` decorator to the rescue

`@observe()` decorator to the rescueAll complexity is abstracted away and you can focus on your business logic. The OpenAI SDK wrapper is aware that it is run within a decorated function and automatically adds its logs to the trace.

```
from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration
@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-4o",
        max_tokens=100,
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content
@observe()
def main():
    return story()
main()
```
![Simple OpenAI decorator
trace](https://langfuse.com/_next/image?url=%2Fimages%2Fdocs%2Fpython-decorator-simple-trace.png&w=3840&q=75)


[Interoperability](https://langfuse.com#interoperability)

The decorator completely replaces the need to use the low-level SDK. It allows for the creation and manipulation of traces, and you can add custom scores and evaluations to these traces as well. Have a look at the extensive [documentation](https://langfuse.com/docs/sdk/python/decorators) for more details.

Langfuse is natively integrated with LangChain, LlamaIndex, and the OpenAI SDK and the decorator is fully compatible with these integrations. As a result, you can, in a single trace, use the decorator on the outermost function, decorate function calls and API calls that are non-LLM related, and use the native instrumentation for the OpenAI SDK, LangChain and Llama Index.

```
from langfuse.openai import openai
from langfuse.decorators import observe
@observe()
def openai_fn(calc: str):
    res = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
          {"role": "system", "content": "You are a very accurate calculator. You output only the result of the calculation."},
          {"role": "user", "content": calc}],
    )
    return res.choices[0].message.content
@observe()
def llama_index_fn(question: str):
    # Set callback manager for LlamaIndex, will apply to all LlamaIndex executions in this function
    langfuse_handler = langfuse_context.get_current_llama_index_handler()
    Settings.callback_manager = CallbackManager([langfuse_handler])
    # Run application
    index = VectorStoreIndex.from_documents([doc1,doc2])
    response = index.as_query_engine().query(question)
    return response
@observe()
def langchain_fn(person: str):
    # Get Langchain Callback Handler scoped to the current trace context
    langfuse_handler = langfuse_context.get_current_langchain_handler()
    # Pass handler to invoke method of chain/agent
    chain.invoke({"person": person}, config={"callbacks":[langfuse_handler]})
@observe()
def main():
    output_openai = openai_fn("5+7")
    output_llamaindex = llama_index_fn("What did he do growing up?")
    output_langchain = langchain_fn("Feynman")
    return output_openai, output_llamaindex, output_langchain
main();
```
[Outlook](https://langfuse.com#outlook)

The decorator drives open tracing for teams that don't want to commit to a single application framework or ecosystem, but want to easily switch between frameworks while relying on Langfuse as a single [platform](https://langfuse.com/docs) for all experimentation, observability and evaluation needs.

Roadmap: The decorator is currently only available for Python. We will add a similar implementation for JS/TS.

[Add-on](https://langfuse.com#add-on)

If you want to built complex applications while being able to easily switch between models, we strongly recommend using this stack:

- Langfuse Decorator for tracing
- Langfuse OpenAI SDK Wrapper for automatic instrumentation of OpenAI calls
- LiteLLM Proxy for standardization of 100+ models on the OpenAI API

Have a look at [this cookbook](https://langfuse.com/guides/cookbook/integration_litellm_proxy) to see an end-to-end example – we really think you'll like this stack and there are lots of teams in the Langfuse Community who built on top of it.

[Thank you](https://langfuse.com#thank-you)

Thank you to everyone who tested the decorator during the beta phase and provided feedback. We've received several Gists from community members showcasing their own decorator implementations built using Langfuse before the decorator was released as an official integration. We're excited to see what you create with it!

[Get Started](https://langfuse.com#get-started)

Run the end-to-end cookbook on your Langfuse traces or learn more about model-based evals in Langfuse.
