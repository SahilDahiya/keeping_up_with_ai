---
title: 'Hugging Face and Langfuse: 5 Ways to use them Together'
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/tracing
- models/fine-tuning
summary: Shows ways to combine Hugging Face workflows with Langfuse for model experimentation,
  tracing, evaluation, and deployment feedback loops.
source: langfuse
url: https://langfuse.com/blog/2025-03-13-use-hugging-face-together-with-langfuse
author: null
published: '2025-03-13'
fetched: '2026-07-11T04:35:09Z'
classifier: codex
taxonomy_rev: 1
words: 1119
content_sha256: 6c6ead7f623f617fd8f64d6296c0e1be619bd784786ec26c8e8400b3c3e519d5
---

# Hugging Face and Langfuse: 5 Ways to use them Together

![🤗 Hugging Face and 🪢 Langfuse: 5 Ways to use them Together](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-03-13-hugging-face-with-langfuse%2Fhugging-face-with-langfuse.png&w=3840&q=75)

# 🤗 Hugging Face and 🪢 Langfuse: 5 Ways to use them Together

Hugging Face and Langfuse are popular platforms to develop and run LLM applications. This guide shows you 5 ways how to use both platforms together to simplify open source LLM development.

![Picture Jannik Maierhöfer](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fjannikmaierhoefer.jpg&w=96&q=75) Jannik Maierhöfer

Jannik MaierhöferHugging Face and Langfuse are popular platforms to develop and run LLM applications. This guide shows you 5 ways how to use both platforms together to simplify your open source LLM development.


What is Hugging Face?[Hugging Face](https://huggingface.co)is a platform for machine learning and AI. It provides a range of tools and services for developers to build, train, and deploy machine learning and language models.


What is Langfuse?[Langfuse](https://langfuse.com)is an open-source platform for LLM engineering. It provides tracing and monitoring capabilities for AI agents, helping developers debug, analyze, and optimize their products. Langfuse integrates with various tools and frameworks via native integrations, OpenTelemetry, and SDKs.

**This guide shows you how to:**

- Trace Hugging Face models
- Evaluate Hugging Face smolagents
- Use Hugging Face models in the Playground and Evaluators
- Use Hugging Face datasets for Dataset Experiments
- Deploy Langfuse on Hugging Face Spaces

[1) Trace Hugging Face Models with Langfuse](https://langfuse.com#1-trace-hugging-face-models-with-langfuse)

Hugging Face allows you to query a variety of open source and specialized fine tuned models. One of the most common integration patterns is to query a Hugging Face model with Python and automatically trace the model calls via Langfuse. Using the [Langfuse OpenAI integration](https://langfuse.com/integrations/model-providers/openai-py), you can easily point to any Hugging Face model endpoint. For example calling the `Meta-Llama-3-8B-Instruct` model:

```
import os
from langfuse.openai import OpenAI
from langfuse import observe
# Set up your environment variables
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..."
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..."
os.environ["LANGFUSE_BASE_URL"] = "https://cloud.langfuse.com"
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_..."
# Initialize the OpenAI client pointing to the Hugging Face Inference API
client = OpenAI(
    base_url="https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct/v1/",
    api_key=os.getenv('HUGGINGFACE_ACCESS_TOKEN'),
)
# Optionally, use the @observe() decorator to trace other application logic as well
@observe()
def get_poem():
    completion = client.chat.completions.create(
        model="model-name",  # this can be an arbitrary identifier
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a poem about language models"},
        ]
    )
    return completion.choices[0].message.content
print(get_poem())
```
![Hugging Face Model Trace in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface%2Fhuggingface-example-trace.png&w=3840&q=75)


For more examples, check out the [Langfuse Hugging Face Integration documentation](https://langfuse.com/integrations/model-providers/huggingface).

[2) Trace Hugging Face Smolagents with Langfuse](https://langfuse.com#2-trace-hugging-face-smolagents-with-langfuse)

For developers using Hugging Face’s minimalistic agent framework—** smolagents**—integrating with Langfuse can help you trace multi-step processes and monitor your agents’ reasoning. Below is a simplified example that shows how to instrument smolagents:

```
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
# Initialize the tracer provider and set up the OTLP exporter to send traces to Langfuse
trace_provider = TracerProvider()
trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))
SmolagentsInstrumentor().instrument(tracer_provider=trace_provider)
# Now, create a smolagent and run it
from smolagents import CodeAgent, ToolCallingAgent, DuckDuckGoSearchTool, HfApiModel
# Initialize the model (you can provide additional parameters as needed)
model = HfApiModel(model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B")
# Create an agent that can perform a web search
search_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    name="search_agent",
    description="Agent to perform web searches."
)
# Create a manager agent that coordinates the operations
manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[search_agent],
)
result = manager_agent.run("How can Langfuse be used to monitor and improve the reasoning of smolagents when executing multi-step tasks?")
print(result)
```
![Hugging Face Smolagent Trace in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fintegration-smolagents%2Fsmolagent_example_trace.png&w=3840&q=75)


This integration allows you to see detailed traces for each step your smolagent performs. Learn more about this integration in the [smolagents documentation](https://huggingface.co/docs/smolagents/en/index).

[3) Hugging Face Models in Playground and Evaluators](https://langfuse.com#3-hugging-face-models-in-playground-and-evaluators)

You can also use Hugging Face models in the [Langfuse Playground](https://langfuse.com/docs/playground) and for [LLM-as-a-Judge evaluators](https://langfuse.com/docs/scores/model-based-evals). This lets you test your prompts and use open source models for model-based evaluations.

To add a Hugging Face model in Langfuse, navigate to your project settings. Create a new model connection and select openai as the provider. Replace the API Base URL with the endpoint for the model (e.g. `https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct/v1/`). Add your Hugging Face access token to the API Key field. For the model name, you can use any arbitrary identifier.

![Hugging Face Playground in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface%2Fadd-hugging-face-to-playground.png&w=3840&q=75)


Learn more about how to set up Langfuse’s [LLM-as-a-Judge evaluators](https://langfuse.com/docs/scores/model-based-evals) and the [Langfuse Playground](https://langfuse.com/docs/playground).

[4) Hugging Face Datasets for Dataset Experiments](https://langfuse.com#4-hugging-face-datasets-for-dataset-experiments)

Hugging Face offers a variety of datasets that can be used to evaluate LLMs and AI agents. These datasets can be used to run [Langfuse Dataset Experiments](https://langfuse.com/docs/datasets/overview).

This example shows how you can bring Hugging Face datasets into your observability pipeline, allowing you to track performance and evaluation scores with Langfuse.

First, we fetch a dataset from Hugging Face. In this case the [GSM8K dataset](https://huggingface.co/datasets/openai/gsm8k) containing math word problems.

```
import os
import pandas as pd
from datasets import load_dataset
from langfuse import Langfuse
# Load a benchmark dataset (e.g., GSM8K)
dataset = load_dataset("openai/gsm8k", split="train[:10]")  # limit to first 10 for demo
df = pd.DataFrame(dataset)
print("First few rows of the dataset:")
print(df.head())
# Initialize your Langfuse client (ensure you have your API key configured)
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..."
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..."
os.environ["LANGFUSE_BASE_URL"] = "https://cloud.langfuse.com"
langfuse = Langfuse(api_key=os.getenv("LANGFUSE_SECRET_KEY"))
# Create a new dataset in Langfuse
dataset_name = "GSM8K_Benchmark"
langfuse.create_dataset(
    name=dataset_name,
    description="Benchmark dataset for evaluating LLM performance",
    metadata={"type": "benchmark"}
)
# Upload each dataset item to Langfuse
for i, row in df.iterrows():
    langfuse.create_dataset_item(
        dataset_name=dataset_name,
        input={"question": row["question"]},
        expected_output={"answer": row["answer"]},
        metadata={"index": i}
    )
```
![Hugging Face Dataset in Langfuse](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface-agent-course%2Fexample-dataset.png&w=3840&q=75)


You can then loop over the dataset items to test your application for every dataset input.

```
dataset = langfuse.get_dataset("<langfuse_dataset_name>")
# Run our agent against each dataset item
for item in dataset.items:
    langfuse_trace, output = run_your_application(item.input["text"])
    # Link the trace to the dataset item for analysis
    item.link(
        langfuse_trace,
        run_name="notebook-run-01",
        run_metadata={ "model": model.model_id }
    )
    # Optionally, store a quick evaluation score for demonstration
    langfuse_trace.score(
        name="<example_eval>",
        value=1,
        comment="This is a comment"
    )
```
You can repeat this process with different:

- Models (OpenAI GPT, local LLM, etc.)
- Tools (search vs. no search)
- Prompts (different system messages)

Then compare them side-by-side in Langfuse:

![Dataset run overview](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface-agent-course%2Fdataset_runs.png&w=3840&q=75)

![Dataset run comparison](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface-agent-course%2Fdataset-run-comparison.png&w=3840&q=75)


For more details on how to use Langfuse Dataset Experiments, check out the [docs](https://langfuse.com/docs/datasets/overview).

[5) Deploy Langfuse on Hugging Face Spaces](https://langfuse.com#5-deploy-langfuse-on-hugging-face-spaces)

Langfuse can also be deployed directly on Hugging Face Spaces—combining the instant accessibility of Spaces with the power of Langfuse observability.

To deploy, simply create a new Hugging Face Space, select Docker as your SDK, and choose Langfuse as the template. You’ll need to set up persistent storage and configure the environment variables for secure operation.

![Hugging Face Spaces Deployment](https://langfuse.com/_next/image?url=%2Fimages%2Fcookbook%2Fhuggingface%2Fhuggingface-space-setup.png&w=3840&q=75)


For a step-by-step guide on deploying Langfuse on Spaces, check out the [Hugging Face Langfuse Spaces documentation](https://huggingface.co/docs/hub/en/spaces-sdks-docker-langfuse#what-is-langfuse).

[Next Steps](https://langfuse.com#next-steps)

Find out more about all features in the [Langfuse docs](https://langfuse.com/docs).

(Note: This blog post was also published on Hugging Face ([link](https://huggingface.co/blog/MJannik/hugging-face-and-langfuse)))
