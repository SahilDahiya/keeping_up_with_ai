---
title: OpenTelemetry LLM Tracing with Vercel AI SDK and Pydantic Logfire
kind: blog
topic: evals-observability
subtopic: tracing
secondary_topics: []
summary: Shows how enabling experimental_telemetry on Vercel AI SDK generateText/streamText
  calls emits rich OpenTelemetry spans (full prompt, response, token counts, streaming
  latency, tool calls) following the OTel GenAI semantic conventions (gen_ai.* / ai.*),
  which any OTel backend can render as readable conversations.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/vercel-ai-sdk-logfire-otel
author: Petyo Ivanov
published: '2026-04-14'
fetched: '2026-07-16T22:03:50Z'
classifier: claude
taxonomy_rev: 2
words: 1070
content_sha256: c33b230297b6237850caf55acd4ed486c81af1b44acfe6d3191d40e413808152
---

# OpenTelemetry LLM Tracing with Vercel AI SDK and Pydantic Logfire

Vercel has done some genuinely nice work with OpenTelemetry. Next.js ships with built-in OTel instrumentation for route handlers, server components, and fetch calls. The `@vercel/otel` package makes the setup a one-liner, and it handles both Node.js and Edge runtimes. You get request-level visibility into your Next.js app without writing any instrumentation code.

But the fascinating part is the AI SDK. Enable `experimental_telemetry` on a `generateText` or `streamText` call, and the SDK emits rich OTel spans with the full prompt, the model's response, token counts, streaming latency, and tool call details. It follows the [OpenTelemetry Semantic Conventions for GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) (`gen_ai.*` attributes) alongside a richer set of AI SDK-specific ones (`ai.*`). That's a lot of useful data, just sitting there waiting for a backend to pick it up.

On our end, Pydantic Logfire is built around these same conventions. When GenAI spans come in from the Vercel AI SDK, Pydantic AI, OpenAI instrumentation, LangChain, or anything else that follows the standard, the LLM Panel picks them up and renders them as readable conversations with token usage, cost, and latency metrics. No integration to configure. Point your OTel exporter at Logfire, and the data lands in the right views.


Before walking through setup, here's a live trace from a Vercel AI SDK app sending telemetry to Logfire. Click anywhere in the embedded view to explore the spans, token counts, and timing:

- **Conversation replay**in the LLM Panel, with system prompt, user messages, and assistant responses rendered as a readable thread
- **Token usage**per call, with input tokens, output tokens, and calculated cost
- **Streaming latency**, including time to first chunk and tokens per second
- **Tool call traces**for agentic workflows, where each tool invocation gets its own span with arguments and results
- **Next.js route spans**from- `@vercel/otel`, which auto-instruments route handlers and fetch calls so you see the full request lifecycle alongside your LLM calls


Three steps. All of them are configuration, with no application code changes required beyond a single option on your AI SDK calls.


Add two environment variables (in `.env.local` for development, or your deployment platform's env config):

```
OTEL_EXPORTER_OTLP_ENDPOINT=https://logfire-api.pydantic.dev
OTEL_EXPORTER_OTLP_HEADERS=Authorization=Bearer <your-logfire-write-token>
```
These are [standard OpenTelemetry environment variables](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), not Logfire-specific. `OTEL_EXPORTER_OTLP_ENDPOINT` tells any OTel exporter where to send data. `OTEL_EXPORTER_OTLP_HEADERS` attaches headers to every export request, here the Logfire write token for authentication. Any OTLP-compatible backend works here; we're using Pydantic Logfire.

Grab your write token from **Project Settings > Write Tokens** in Logfire.


Create `src/instrumentation.ts` (Next.js picks this up automatically on startup):

```
import { registerOTel } from '@vercel/otel'
export function register() {
  registerOTel({ serviceName: 'my-ai-app' })
}
```
`@vercel/otel` reads the `OTEL_EXPORTER_OTLP_*` env vars and configures a trace exporter automatically. Install it along with its peer dependencies:

```
npm install @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
```

Add `experimental_telemetry` to your `streamText`, `generateText`, `generateObject`, or `streamObject` calls:

```
import { openai } from '@ai-sdk/openai'
import { streamText, type UIMessage, convertToModelMessages } from 'ai'
export async function POST(req: Request) {
  const { messages }: { messages: UIMessage[] } = await req.json()
  const result = streamText({
    model: openai('gpt-4o-mini'),
    system: 'You are a helpful assistant.',
    messages: await convertToModelMessages(messages),
    experimental_telemetry: {
      isEnabled: true,
      functionId: 'chat',
    },
  })
  return result.toUIMessageStreamResponse()
}
```
The `functionId` becomes part of the span name in Logfire. Use descriptive values like `'chat'`, `'summarize'`, or `'classify'` to make filtering easy.

That's it. Three lines in `instrumentation.ts`, two env vars, one option per AI call.


Each AI SDK call produces a two-level span hierarchy. An outer span (`ai.streamText`) covers the full operation, including any tool-call loops. Inside it, a provider span (`ai.streamText.doStream`) represents the actual API call to the model. If your call uses tools, each invocation gets its own `ai.toolCall` child span with the function name, arguments, and result.

The SDK emits attributes in two namespaces:

| Attribute | What it contains | 
|---|---|
| `ai.prompt.messages` | Full message array sent to the model | 
| `ai.response.text` | The model's text response | 
| `ai.response.toolCalls` | Tool calls in the response | 
| `ai.response.msToFirstChunk` | Time to first streamed token (ms) | 
| `gen_ai.request.model` | Requested model name | 
| `gen_ai.usage.input_tokens` | Input token count | 
| `gen_ai.usage.output_tokens` | Output token count | 
| `gen_ai.system` | Provider identifier (e.g. `openai`) | 

The `ai.*` attributes carry the rich, Vercel-specific data: full message content, tool call details, streaming performance metrics. The `gen_ai.*` attributes follow the [OpenTelemetry Semantic Conventions for GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/), which is what makes this work with any OTel-compatible backend. Logfire reads both: `gen_ai.*` for dashboards and token aggregation, `ai.*` for the conversation replay in the LLM Panel.


The `@vercel/otel` package is tied to Next.js. For Express, Fastify, Hono, or plain Node.js apps, use `@pydantic/logfire-node` instead:

```
import logfire from '@pydantic/logfire-node'
logfire.configure({ serviceName: 'my-ai-service' })
```
This sets up the OTel SDK and OTLP exporter the same way `@vercel/otel` does. The AI SDK's `experimental_telemetry` option works identically since it uses the global OTel tracer, regardless of how it was initialized.


Three independent teams built the pieces that make this possible:

- **Vercel**added OpenTelemetry instrumentation to the AI SDK, emitting spans with- `ai.*`and- `gen_ai.*`attributes on every LLM call
- **The OpenTelemetry project**defined the OTLP wire protocol and the GenAI semantic conventions that standardize how LLM telemetry is represented
- **Pydantic**built Logfire to ingest OTLP data and render LLM-specific views when it detects GenAI attributes: conversation replay, token usage, cost calculation

None of these teams coordinated on an integration. The pieces work together because they all follow the same standard. And because Logfire's LLM Panel detects the telemetry format automatically, it works the same way for PydanticAI, OpenAI instrumentation, Anthropic instrumentation, and LangChain, all in the same UI. If your app calls multiple providers or uses multiple AI frameworks, every call shows up in one place.


The AI SDK v7 is in active beta, with a new provider spec and internal restructuring. The core OTel span attributes, the ones Logfire reads, are stable across versions. Because Logfire consumes standard OTel data rather than hooking into SDK internals, upgrading your AI SDK version won't break your observability setup.


Clone the [demo app](https://github.com/pydantic/logfire-vercel-ai-demo), add your Logfire write token, and run `npm run dev`. Or add `experimental_telemetry: { isEnabled: true }` to an existing Vercel AI SDK project. If you already have `@vercel/otel` set up, all you need is the one-line option on your AI calls and the two Logfire env vars.

[Sign up for Logfire](https://logfire.pydantic.dev) to get a write token and start seeing your LLM traces.
