---
title: How to use Braintrust with any framework or provider
topic: evals-observability
subtopic: tracing
secondary_topics:
- infra-platform/deployment
summary: Integration guide for capturing Braintrust traces and evals across different
  AI frameworks and model providers without locking the application stack to one SDK.
source: braintrust
url: https://www.braintrust.dev/blog/any-framework-any-provider
author: Braintrust Team
published: '2026-06-16'
fetched: '2026-07-11T04:31:25Z'
classifier: codex
taxonomy_rev: 1
words: 1819
content_sha256: 86b015b97a578291d8f774261cae0f0e7914cb0d2aeeb4075d751cd2be28ca1c
---

# How to use Braintrust with any framework or provider

16 June 2026Jess Wang10 min

Every AI team's stack looks different. Some build agents with LangGraph, some with CrewAI, and some roll their own loop and never look back. Some run everything through the Vercel AI SDK, while others have a Go service that has never touched a Python SDK. Most teams mix model providers: OpenAI for one feature, Claude for another, and a self-hosted model for the workload that can't leave the VPC.

Braintrust is designed for this reality. You instrument your app once, via SDKs or OpenTelemetry, and keep using whatever agent framework and model providers you prefer, while getting consistent traces, evals, and debugging across everything. Even as your stack evolves, the way you measure quality stays the same.

There are three paths to getting traces into Braintrust, and you can mix them as needed.

**Auto-instrumentation** is the recommended starting point. One call at startup patches every supported AI library, so all LLM calls are captured (inputs, outputs, latency, token usage, and costs) without wrapping individual clients:

python

```
import braintrust
braintrust.auto_instrument()
braintrust.init_logger(project="My Project")
```
In TypeScript, the equivalent is `initLogger()` plus running your app with `node --import braintrust/hook.mjs`, or the matching bundler plugin if you're on Vite, Next.js (Webpack or Turbopack), Nuxt, esbuild, or Rollup. This goes well beyond two languages. Braintrust ships SDKs for Python, TypeScript, Go (compile-time instrumentation via Orchestrion), Ruby, Java (a ByteBuddy agent that instruments at JVM startup), and .NET. Auto-instrumentation covers the OpenAI, Anthropic, Gemini, Mistral, and Cohere SDKs, plus frameworks like LangChain, LlamaIndex, LiteLLM, DSPy, Instructor, and the agent frameworks below. See the [full support matrix](https://www.braintrust.dev/docs/integrations/sdk-integrations) for versions. Streaming is handled for you by Braintrust, since chunks are collected and logged as a single span.

**Manual instrumentation** is there when you want explicit control, or if you've built your own framework. Wrap individual clients with helpers like `wrapOpenAI`, or use spans directly to trace retrieval steps, tool calls, and business logic alongside your LLM calls, so an eval trace shows your whole pipeline rather than just the model call.

**OpenTelemetry** covers everything else. If you'd rather not add a Braintrust SDK, or you're in a language without one, point your existing OTel setup at Braintrust as a backend. With pure OTLP, it's two environment variables:

bash

```
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.braintrust.dev/otel
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <api key>, x-bt-parent=project_id:<project id>"
```
Braintrust implements the OpenTelemetry GenAI semantic conventions, so spans carrying `gen_ai.*` attributes are automatically mapped to structured inputs, outputs, metadata, and token metrics, including cache read and write tokens. LLM calls become spans you can save as prompts and evaluate in the playground. You can also set Braintrust-native fields like scores, expected values, and tags directly from OTel spans via the `braintrust.*` attribute namespace. For Python and TypeScript, the `BraintrustSpanProcessor` drops into your existing tracer provider, with a `filterAISpans` option so only AI-related spans get sent, and a `customFilter` hook for fine-grained sampling. There's also an OTel compatibility mode and distributed tracing support for messy real-world cases, like a Braintrust-instrumented service calling an OTel-instrumented one, or the reverse, with the trace context flowing across the HTTP boundary in both directions.

Braintrust captures provider calls, tool calls, and agent steps as trace spans, independent of which framework runs the loop. Different teams pick different frameworks, and frameworks need to be migrated, but when the trace structure is consistent, you can compare, eval, and debug behavior the same way, regardless of what produced it.

For LangGraph, `auto_instrument()` registers a global LangChain callback handler that LangGraph also uses, capturing graph execution, node transitions, and model calls. If you want explicit control, configure the handler directly:

python

```
from braintrust import init_logger
from braintrust.integrations.langchain import BraintrustCallbackHandler, set_global_handler
init_logger(project="My Project")
set_global_handler(BraintrustCallbackHandler())
# ...build and invoke your StateGraph as usual
```
For CrewAI, the same `auto_instrument()` call traces a run as one nested trace that mirrors the execution flow: crew kickoff, task execution, agent reasoning (role, goal, backstory, available tools), LLM calls with full provider config, and tool calls with arguments, outputs, retries, and cache hits, plus token metrics and time-to-first-token on streaming calls. Use `setup_crewai()` if you want CrewAI traced without patching other libraries, and the integration works with any model provider CrewAI supports.

The same pattern extends to the OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, AutoGen, AgentScope, Mastra, Google ADK, Strands, and LiveKit Agents, and even to workflow engines like Temporal. If your framework is already instrumented with OpenTelemetry, keep that setup and route the spans to Braintrust, with no re-instrumentation required.

The benefits of framework neutrality are organizational as much as technical. A team that uses one framework and a team on a custom loop still end up with traces that can be compared side by side, scored with the same evals, and debugged with the same process.

Tracing is about getting the data into Braintrust. The next step is to eval with that data. Braintrust's eval primitives can be applied across frameworks and providers. An `Eval()` is three things (a dataset, a task, and scorers), and the task is just a function. Whatever happens inside it, whether a LangGraph invocation, a CrewAI kickoff, or your bespoke agent loop, gets traced and scored identically:

python

```
from braintrust import Eval, init_dataset
from autoevals import Factuality
Eval(
    "My project",
    data=init_dataset(project="My project", name="My dataset"),
    task=lambda input: run_my_agent(input),  # any framework in here
    scores=[Factuality],
    trial_count=3,  # run each input multiple times to measure variance
)
```
Run it locally with `bt eval my_eval.py` (add `--watch` for re-runs on file changes), or wire it into CI with the GitHub Action, which posts results as a PR comment. Running `bt eval tests/ --first 20` makes a cheap smoke run on pull requests, with the full suite reserved for merges. Experiments are immutable snapshots, so regressions between any two runs are always comparable, and metadata like `model` and `prompt_version` makes the comparisons filterable.

Some tasks genuinely can't run inside an eval file, like agents with heavy dependencies, internal APIs behind a VPN, or OS-specific tooling. In those cases, remote evals and sandboxes close the gap. Run `bt eval path/to/eval.py --dev` and your eval becomes a local server that the Braintrust playground can trigger. Parameters you define in code (model selectors, editable prompts, custom options) appear as UI controls, and your code never leaves your infrastructure, since only results are sent to Braintrust. You can also push the eval as a sandbox artifact, and Braintrust will invoke it on demand in an isolated cloud environment, so teammates can run your agent eval from the playground without cloning the repo.

Adopting Braintrust doesn't mean starting from zero. There are a few common ways teams bring existing data in.

**From existing observability tooling, via OpenTelemetry.** If your app already emits OTel traces, Braintrust works as an additional sink. Keep your current instrumentation and exporters, add Braintrust as a destination, and consolidate AI-specific analysis there. The `filterAISpans` option keeps infrastructure noise out.

**From LangSmith, without rewriting your code.** The experimental LangSmith wrapper redirects `@traceable` decorators to Braintrust's `@traced` and `evaluate()` calls to Braintrust's `Eval()`, and your LangSmith-style evaluators are converted to Braintrust scorers automatically. It runs in two modes: parallel, which sends traces and evals to both platforms simultaneously (useful for comparing services or migrating gradually), and standalone, which sends to Braintrust only. The switch is one `setup_langsmith()` call before your LangSmith imports. OpenLLMetry and Traceloop-instrumented apps can likewise forward traces directly.

**From files, scripts, and pipelines.** Test sets and ground-truth data come in through whichever path fits: CSV or JSON upload in the UI with drag-and-drop column mapping, the SDK's `init_dataset()` and `insert()` for programmatic population, or the `bt` CLI for terminal and CI workflows:

bash

```
bt datasets create my-dataset --file records.jsonl
```
The CLI also moves data both directions. `bt sync pull` downloads logs, experiments, and datasets to local NDJSON files for offline analysis or backup, and `bt sync push` sends local data back up. For data living in warehouses or streaming systems, the dataset insert API and BTQL endpoints give you the programmatic hooks to build enrichment pipelines on top, and `bt sql` runs SQL against your logs straight from a script.

For teams building with AI, multi-provider has become the default rather than an edge case. Braintrust makes it safe in two complementary ways.

First, observability and evals are provider-agnostic by construction. Whether a span came from the OpenAI SDK, the Anthropic SDK, or Bedrock, it lands in the same trace format with the same metrics, so comparing models means running the same dataset through multiple experiments and reading accuracy, latency, cost, and token use side by side.

Second, the Braintrust gateway gives you one OpenAI-compatible API in front of every provider. Add your provider keys in Braintrust, either at the organization level as the default or per-project where you need separate billing or credential isolation, point your SDK's base URL at `https://gateway.braintrust.dev`, and you're done. That includes the genuinely useful trick of standardizing on one SDK while calling any provider's models:

python

```
from openai import OpenAI
client = OpenAI(
    base_url="https://gateway.braintrust.dev",
    api_key=os.environ["BRAINTRUST_API_KEY"],
)
# Call Claude through the OpenAI SDK
response = client.responses.create(
    model="claude-sonnet-4-5",
    input=[{"role": "user", "content": "Hello!"}],
)
```
Swapping providers becomes a one-line model-name change, with automatic response caching and logging along the way. Set the `x-bt-parent` header, and gateway calls nest into your distributed traces.

For models the gateway doesn't list, whether self-hosted on Ollama or vLLM, fine-tuned, or proprietary, custom providers plug into the same endpoint. You configure the endpoint URL, API format, and any auth headers (with Mustache templating for values like `{{email}}` and `{{model}}`), optionally declare per-million-token costs so experiment cost estimation stays accurate, and the model shows up in the same dropdowns as GPT and Claude. Custom models work everywhere standard ones do, including as LLM-as-a-judge scorers, so you can grade outputs with your own fine-tuned judge. If you'd rather not route traffic through a gateway at all, SDK and OTel instrumentation work directly against any provider, including your own infrastructure.

This also plays well with the rest of your devx stack. The Vercel AI SDK's native OTel support works with Braintrust out of the box, gateways you already run (Cloudflare AI Gateway, LiteLLM, TrueFoundry) can forward traces in, and the `bt` CLI meets your coding agents where they are. `bt setup` installs Braintrust skill files and MCP config for Claude, Cursor, Copilot, Codex, and others, then instruments your project and verifies it with a captured trace.

Braintrust works with whatever agent framework and model provider you're using: instrument once (SDK or OpenTelemetry), then run evals, debug traces, and compare prompts and models consistently, even as your stack evolves.

If you want to see what that looks like on your stack specifically, the integrations directory has a setup guide for just about everything. And if your framework isn't there yet, the OTel endpoint means you're a couple of environment variables away anyway. [Sign up for free](https://www.braintrust.dev/signup) or [book a demo](https://www.braintrust.dev/contact) to get started.
