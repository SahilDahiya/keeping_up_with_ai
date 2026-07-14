---
title: 'Open Responses: What you need to know'
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- agents/tool-use
summary: 'Argues Chat Completions is a poor fit for agentic workloads and proposes
  Open Responses, an open version of OpenAI''s Responses API: stateless by default
  with encrypted reasoning, standardized model params, and provider-side agentic loops
  that execute tool calls before returning.'
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/open-responses
author: Shaun Smith; Ben Burtenshaw; Merve; Pedro Cuenca
published: '2026-01-15'
fetched: '2026-07-14T22:20:58Z'
classifier: claude
taxonomy_rev: 1
words: 1591
content_sha256: f977553c31c331d9939932cb76712a78836300d6221429e6f20f88a785161fd4
---

# Open Responses: What you need to know

Updated     •  20  

#### huggingface/documentation-images

![](https://cdn-avatars.huggingface.co/v1/production/uploads/1583856921041-5dd96eb166059660ed1ee413.png) 

 Published
					January 15, 2026 

  Upvote 

 112

The era of the chatbot is long gone, and agents dominate inference workloads. Developers are shifting toward autonomous systems that reason, plan, and act over long-time horizons. Despite this shift, much of the ecosystem still uses the **Chat Completion** format, which was designed for turn-based conversations and falls short for agentic use cases. The **Responses format** was designed to address these limitations, but it is closed and not as widely adopted. The **Chat Completion** format is still the de facto standard despite the alternatives.

This mismatch between the agentic workflow requirements and entrenched interfaces motivates the need for an open inference standard. Over the coming months, we will collaborate with the community and inference providers to implement and adapt Open Responses to a shared format, practically capable of replacing chat completions.

Open Responses builds on the direction OpenAI has set with their  [ Responses API](https://platform.openai.com/docs/api-reference/responses)  launched in March 2025, which superseded the existing Completion and Assistants APIs with a consistent way to:

- Generate Text, Images, and JSON structured outputs
- Create Video content through a separate task-based endpoint
- Run agentic loops on the provider side, executing tool calls autonomously and returning the final result.

Open Responses extends and open-sources the Responses API, making it more accessible for builders and routing providers to interoperate and collaborate on shared interests.

Some of the key points are:

- Stateless by default, supporting encrypted reasoning for providers that require it.
- Standardized model configuration parameters.
- Streaming is modeled as a series of semantic events, not raw text or object deltas.
- Extensible via configurable parameters specific to certain model providers.

We’ll briefly explore the core changes that impact most community members. If you want to deep dive into the specification, check out the [Open Responses documentation](https://www.openresponses.org/).

Client requests to Open Responses are similar to the existing Responses API. Below we demonstrate a request to the Open Responses API using curl. We're calling a proxy endpoint that routes to Inference Providers using the Open Responses API schema.

```
 curl https://evalstate-openresponses.hf.space/v1/responses \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $HF_TOKEN" \
+  -H "OpenResponses-Version: latest" \
   -N \
   -d '{
         "model": "moonshotai/Kimi-K2-Thinking:nebius",
         "input": "explain the theory of life"
       }'
```
Clients that already support the Responses API can migrate to Open Responses with relatively little effort. The main changes involve how reasoning content is exposed:

- Expanded reasoning visibility: Open Responses formalizes three optional fields for reasoning items: `content`(raw reasoning traces),`encrypted_content`(provider-specific protected content), and`summary`(sanitized from raw traces).

OpenAI models used to only expose `summary` and `encrypted_content`. With Open Responses, providers may expose their raw reasoning via the API. 
Clients migrating from providers that previously returned only summaries and encrypted content will now have the
opportunity to receive and handle raw reasoning streams when supported by their chosen provider.

- Implementing richer state changes and payloads, including more detailed observability—for example, a hosted Code Interpreter can send a specific `interpreting`state to improve agent and user visibility during long-running operations.

For Model Providers, implementing the changes for Open Responses should be straightforward if they already adhere to the Responses API specification. For Routers, there is now the opportunity to standardize on a consistent endpoint and support configuration options for customization where needed.

Over time, as Providers continue to innovate, certain features will become standardized in the base specification.

In summary, migrating to Open Responses will make the inference experience more consistent and improve quality as undocumented extensions, interpretations, and workarounds of the legacy Completions API are normalized in Open Responses.

You can see how to stream reasoning chunks below.

```
 {
  "model": "moonshotai/Kimi-K2-Thinking:together",
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "explain photosynthesis."
    }
  ],
  "stream": true
}
```
Here’s the difference between getting an Open Response and using OpenAI Responses for reasoning deltas:

```
// Open weight models stream raw reasoning
event: response.reasoning.delta
data: { "delta": "User asked: 'Where should I eat...' Step 1: Parse location...", ... }
// Models with encrypted reasoning send summaries, or sent as a convenience by Open Weight models
event: response.reasoning_summary_text.delta
data: { "delta": "Determined user wants restaurant recommendations", ... }
```
Open Responses distinguishes between “Model Providers” — those who provide inference — and “Routers” — intermediaries who orchestrate between multiple providers.

Clients can now specify a Provider along with provider-specific API options when making requests, allowing intermediary Routers to orchestrate requests between upstream providers.

Open Responses natively supports two categories of tools: internal and external. Externally hosted tools are implemented outside the model provider’s system. For example, client side functions to be executed, or MCP servers. Internally hosted tools are within the model provider’s system. For example, OpenAI’s file search or Google Drive integration. The model calls, executes, and retrieves results entirely within the provider's infrastructure, requiring no developer intervention.

Open Responses formalizes the agentic loop which is usually made up of a repeating cycle of reasoning, tool invocation, and response generation that enables models to autonomously complete multi-step tasks.

![process diagram](https://huggingface.co/huggingface/documentation-images/resolve/main/openresponses/image1.png)


[image source: openresponses.org](https://www.openresponses.org/specification#the-agentic-loop)

The loop operates as follows:

- The API receives a user request and samples from the model
- If the model emits a tool call, the API executes it (internally or externally)
- Tool results are fed back to the model for continued reasoning
- The loop repeats until the model signals completion

For internally-hosted tools, the provider manages the entire loop; executing tools, returning results to the model, and streaming output. This means that multi-step workflows like "search documents, summarize findings, then draft an email" use a single request.

Clients control loop behavior via `max_tool_calls` to cap iterations and `tool_choice` to constrain which tools are invocable:

```
{
  "model": "zai-org/GLM-4.7",
  "input": "Find Q3 sales data and email a summary to the team",
  "tools": [...],
  "max_tool_calls": 5,
  "tool_choice": "auto"
}
```
The response contains all intermediate items: tool calls, results, reasoning.

Open Responses extends and improves the Responses API, providing richer and more detailed content definitions, compatibility, and deployment options. It also provides a standard way to execute sub-agent loops during primary inference calls, opening up powerful capabilities for AI Applications. We are looking forward to working with the Open Responses team **and the community at large** on future development of the specification. 

![acceptance test](https://huggingface.co/huggingface/documentation-images/resolve/main/openresponses/image2.png)


You can try Open Responses with [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) today. We have an early access version available for use on [Hugging Face Spaces](https://huggingface.co/spaces/evalstate/openresponses) - try it with your Client and Open Responses Compliance Tool today!

  Updated     •  20 

😻

 7

Use Open Responses with Hugging Face Inference Providers

More Articles from our Blog

agentsguicommunity

  76

 July 10, 2025 announcementopen-sourcecommunity

 
- +16

 106

 June 8, 2026 Does this mean that the next step for local llm endpoint providers (like vLLM) is to support hosted tools?

Yes - I think we will see a lot more of this pattern especially for Agents offloading work to sub-agent Tool Loops via Open Responses.

Are you going to open source the code of the API?

This comment has been hidden (marked as Resolved)        

      •

 I hope this doesn't normalize the obscuring of raw output.

Maybe there is a use for this. We donot need an "agent loop" insider the vendor boxes.

What we definitely need is a good omni-adopted API for basic inference without anything more than general custom tool calling. 

Only putting in inference paramters and that's that. I suppose that is the reason why the community stayed with the Completions API yet, right?

Agent loops are supposed to be implemented in the agent system not in the LLM vendors system.

They can simply add their proprietary Agent loop thingy as an "internal" tool.

However I would highly urge the community to consider the strategic implications for further evolution of these tools. There is the danger that specific vendor based models might be highly optimized to only provide good responses on their internal tools / subagent loops. Of course they have an incentive to control the whole workflow to secure their marketshare.

Opposed to that: when everyone is using the APIs in their custom designed loop-procedure (or some from open source agent orchestration tools) the decision about what models to use is somewhat dependent on the basis of how well theses behave with external tool calling. This is rather the situation we want to be in.

Maybe there is a use for this. We donot need an "agent loop" insider the vendor boxes.


What we definitely need is a good omni-adopted API for basic inference without anything more than general custom tool calling.Only putting in inference paramters and that's that. I suppose that is the reason why the community stayed with the Completions API yet, right?

Agent loops are supposed to be implemented in the agent system not in the LLM vendors system.


They can simply add their proprietary Agent loop thingy as an "internal" tool.However I would highly urge the community to consider the strategic implications for further evolution of these tools. There is the danger that specific vendor based models might be highly optimized to only provide good responses on their internal tools / subagent loops. Of course they have an incentive to control the whole workflow to secure their marketshare.

Opposed to that: when everyone is using the APIs in their custom designed loop-procedure (or some from open source agent orchestration tools) the decision about what models to use is somewhat dependent on the basis of how well theses behave with external tool calling. This is rather the situation we want to be in.


I agree
