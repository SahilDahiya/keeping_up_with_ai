---
title: Crusoe is now a Pydantic AI model provider
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/crusoe-pydantic-ai-model-provider
author: Emmanuel Acheampong; Laís Carvalho
published: '2026-08-14'
fetched: '2026-08-15T06:11:55Z'
classifier: null
taxonomy_rev: 2
words: 996
content_sha256: e67af64a390c4aba3bb52b4fc2767dcb9f2c218aba870dc664bcd94a732adde4
---

# Crusoe is now a Pydantic AI model provider

*The following is a guest post from [Crusoe](https://crusoe.ai/), written by [Emmanuel Acheampong](https://www.linkedin.com/in/emmanuel-acheampong/), Senior Developer Relations Manager. Co-authored by [Laís Carvalho](https://www.linkedin.com/in/laisbsc/), Developer Relations at Pydantic.*

Crusoe is now a native model provider in [Pydantic AI](https://pydantic.dev/docs/ai/overview/). One string, `'crusoe:zai/GLM-5.2'`, and your agents run on Crusoe Managed Inference: streaming, tool calling, structured output, and the full open model catalog on the Crusoe Intelligence Foundry, all out of the box.

This post covers why the integration was built, how it works, and how to use it.

## 

Crusoe is the cloud for AI, however you build it. Open models are a fast-growing part of that picture, and they deserve infrastructure built for them. Crusoe Managed Inference serves the open catalog end to end on the Crusoe Intelligence Foundry: GLM, Llama, DeepSeek, Qwen, Gemma, gpt-oss, Kimi, and the NVIDIA Nemotron™ 3 family, with day-zero support for new releases.

Serving open weights is half of that work. The other half is meeting developers in the open source tools they already use. Crusoe is an upstream provider in LiteLLM and now a native Pydantic AI provider. Each integration follows the same principle: contribute the code upstream, keep it maintained, and let the framework's own conventions handle configuration.

Nothing in this stack locks you in. The models are open weights, the frameworks are open source, and the provider described in this post lives in the [pydantic-ai repository](https://github.com/pydantic/pydantic-ai), not in a Crusoe SDK. The ecosystem gets stronger when open and closed keep pushing each other forward, and builders match each workload to the right model. That is the outcome we are investing in.

## 

Plenty of teams were already running Pydantic AI agents against Crusoe. It worked, but it meant wiring up `OpenAIProvider` with a custom `base_url`, managing the API key by hand, and losing model profile inference along the way. Model profiles matter more than they sound: they tell Pydantic AI how each model family handles JSON schemas, tool definitions, and output formats. Point a generic OpenAI provider at a GLM or gpt-oss model and you get OpenAI defaults, which are not always the right ones.

A native provider removes all of that. The endpoint, the key handling, and the per-family profiles ship in the framework.

## 

The integration adds a `CrusoeProvider` to `pydantic-ai`, following the same pattern as other OpenAI-compatible providers. Install Pydantic AI, or the slim package with the `openai` group:

```
uv add logfire "pydantic-ai-slim[openai]"
```
Generate a key in the [Crusoe Cloud console](https://console.crusoecloud.com/) under Intelligence Foundry, then set it:

```
export CRUSOE_API_KEY="cr_..."
```
That is the whole setup. The shorthand string does the rest:

```
import logfire
from pydantic_ai import Agent
logfire.configure()
logfire.instrument_pydantic_ai()
agent = Agent('crusoe:zai/GLM-5.2')
result = agent.run_sync('In one sentence: why do open agent stacks matter in 2026?')
print(result.output)
```
Structured output works the way you would expect from Pydantic AI, because the provider infers the right profile for the model family:

```
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
logfire.configure()
logfire.instrument_pydantic_ai()
class GpuSpec(BaseModel):
    name: str
    memory_gb: int
    interconnect: str
agent = Agent('crusoe:zai/GLM-5.2', output_type=GpuSpec)
result = agent.run_sync('Summarize the NVIDIA HGX™ B200 as a spec.')
print(result.output)
#> name='NVIDIA HGX B200' memory_gb=1536 interconnect='5th-Gen NVLink (1.8 TB/s per GPU), PCIe Gen5'
```
If you need explicit control, construct the provider yourself:

```
import logfire
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.crusoe import CrusoeProvider
logfire.configure()
logfire.instrument_pydantic_ai()
model = OpenAIChatModel(
    'meta-llama/Llama-3.3-70B-Instruct',
    provider=CrusoeProvider(api_key='your-api-key'),
)
agent = Agent(model)
result = agent.run_sync('Be concise. Defend the Oxford comma.')
print(result.output)
```
The provider also accepts a custom `httpx.AsyncClient` or a preconfigured `AsyncOpenAI` client, so it fits whatever connection pooling or proxy setup you already run.

Under the hood, `CrusoeProvider` maps the supported model families to their correct Pydantic AI profiles: `meta-llama`, `deepseek-ai`, `qwen`, `google` (Gemma), `moonshotai` (Kimi), `zai` (GLM), and `openai` (gpt-oss, which uses the harmony profile). Tool schemas and JSON output behave correctly per family without any configuration on your side. Families without an explicit profile fall back to OpenAI-compatible defaults.

## 

What you get from the pairing is a short list with a lot behind it. Pydantic AI brings the agent framework: type-safe outputs, tools, streaming, and evals through Pydantic Evals, with tracing through Pydantic [Logfire](https://pydantic.dev/logfire). Crusoe brings the inference layer built for agent workloads. MemoryAlloy, our cluster-wide KV cache fabric, routes requests cache-aware, which matters for agents that re-send system prompts and accumulated history on every turn. Cached input pricing means the loop stays cheap as contexts grow.

The main learning from building the provider: the OpenAI-compatible pattern in Pydantic AI is well factored. The whole integration is one provider class, a profile map, and tests that mirror the existing Nebius provider. If you serve open models behind an OpenAI-compatible endpoint, contributing a provider is a weekend project, and the maintainers' review process makes the result better than what you started with.

## 

Two steps: grab a key from the [Intelligence Foundry](https://console.crusoecloud.com/request-foundry), then `uv add logfire "pydantic-ai-slim[openai]"` and point an `Agent` at `crusoe:` plus any model in the [catalog](https://docs.crusoecloud.com/managed-inference/overview/).

Once that first agent runs:

- The [Pydantic AI documentation](https://pydantic.dev/docs/ai/overview/) covers what comes after a single`run_sync` : tools, streaming, dependency injection, and multi-agent flows.
- Every example above calls `logfire.configure()` . That is[Pydantic Logfire](https://pydantic.dev/logfire) , and it turns each run into a trace you can open: model calls, tool calls, retries, and token costs, queryable with SQL. The[Pydantic AI integration docs](https://pydantic.dev/docs/logfire/integrations/llms/pydanticai/) cover the setup, and the free tier is enough to watch your first agents work.
- [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/) is worth reaching for when you start swapping models in the catalog and need to know whether the swap made things better.

If you build something interesting on this stack, we would love to hear about it. Reach the Crusoe developer community at [devcommunity@crusoe.ai](mailto:devcommunity@crusoe.ai), and follow [Crusoe for Developers on LinkedIn](https://www.linkedin.com/showcase/crusoedev/) and [@crusoedev on X](https://x.com/crusoedev) for model launches, cookbook drops, and more walkthroughs.

An agent framework with validation at its core, and inference built for agents underneath it. That is the stack we wanted to use ourselves, so we wired it in.
