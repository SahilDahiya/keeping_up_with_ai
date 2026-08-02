---
title: 'Kimi K3: The Complete Developer Guide'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: together
url: https://www.together.ai/blog/kimi-k3-guide
author: Zain Hasan; Shobhit Dixit
published: '2026-08-01'
fetched: '2026-08-02T06:52:30Z'
classifier: null
taxonomy_rev: 2
words: 1534
content_sha256: a868da58a541cd17c0e9afb99c8984a58b8ae95df4095d0ca54ba6f03b5868db
---

# Kimi K3: The Complete Developer Guide

What you'll learn

- What is Kimi K3, and what makes it different?
- What is under the hood: KDA, Attention Residuals, and the Stable LatentMoE architecture
- How do you use reasoning effort, streaming, tools, vision, and 1M context?
- How do you take it from a first API call to production?
- How does Kimi K3 compare to the frontier on coding and agentic benchmarks?
- How much does Kimi K3 cost on Together AI?

Kimi K3 is Moonshot AI's most capable model to date: a 2.8-trillion-parameter model and the world's first open-source model in the 3-trillion-parameter class. It is designed for frontier intelligence work like long-horizon coding, end-to-end knowledge work, and deep reasoning. It is also the first open-weights model competing at the GPT 5.6 Sol and Claude Fable 5 tier, and Together AI is working directly with the Moonshot team to serve it.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a6a3dfd2ebabab7a73eacb1_KimiK3_API.jpeg)

## The largest open-weight model released

The Kimi team is deeply committed to scaling, and it shows: in nine of the twelve months from July 2025 to July 2026, Kimi models set the upper bound of open-model scale. At 2.8 trillion parameters, K3 is now the largest open-weight model ever released.

## What is under the hood

Two architectural updates form K3's backbone, both designed to help information flow more easily through longer sequences and deeper into the network:

- **Kimi Delta Attention (KDA):** a hybrid linear attention mechanism that provides an efficient foundation for scaling attention across very long contexts. This is the first Kimi model to support a 1M context length.
- **Attention Residuals (AttnRes):** selectively retrieves representations across model depth rather than accumulating them uniformly.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a68de21003a8f4b178241d1_k3-arch.avif)

On top of that, Moonshot pushed Mixture-of-Experts sparsity further with the Stable LatentMoE framework, efficiently activating 16 of 896 experts. At this level of sparsity, roughly 2% of experts activated per token, routing and optimization become first-order challenges, so several supporting techniques enable stable training at 2.8T scale:

- **Quantile Balancing:** derives expert allocation directly from router-score quantiles, eliminating heuristic updates and a sensitive balancing hyperparameter.
- **Per-Head Muon:** extends the Muon optimizer to optimize attention heads independently for more adaptive learning at scale.
- **Sigmoid Tanh Unit (SiTU):** improves activation control.
- **Gated MLA:** improves attention selectivity.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a68e4403f7c166f744ff08a_stable-latentmoe.png)

## How to use Kimi K3 on Together AI

The API is OpenAI-compatible. The snippets below target Together AI and use the official Together Python SDK.

### Thinking effort

K3 can be configured with the top-level reasoning_effort field. Three levels are supported: low, high, and max, with max as the default. On Together, thinking can also be switched off via the standard reasoning={"enabled": False} toggle.

### Streaming

Streaming responses deliver separate reasoning_content (the thinking trace) and final-answer content deltas.

### Vision input

Multiple images can be provided as input. Moonshot has also released a visual reasoning benchmark, [Perception Bench](https://www.kimi.com/blog/perception-bench).

**Vision limits:**

- No limit on the number of images, but the whole request body must stay under 100 MB.
- Recommended maxima: 4K (4096x2160) for images. Higher resolutions cost processing time and tokens without improving understanding.
- Token cost scales with resolution.

### Structured output

Use response_format with json_schema and strict: true to constrain the final message.content.

The looser {"type": "json_object"} mode also works on Together when you only need syntactically valid JSON. Either way, keep max_tokens generous: the whole thinking trace is spent before the first schema-constrained token is emitted, so a tight cap truncates the JSON rather than the reasoning.

### Tools and tool_choice

K3 keeps the standard tool-choice constraints. The standard loop: declare functions in tools; when the model returns tool_calls, append the complete assistant message to history, then append one tool message with the matching tool_call_id for each call, then call again. Use tool_choice="required" on a first turn to force at least one tool call, and switch back to "auto" afterward. Changing tool_choice does not invalidate the prefix cache.

### Dynamic tool loading

You can place a complete tool definition (full name, description, and parameters) inside a system message that carries a tools field and no content. The tool becomes available from that message's position onward.

Key rules:

- Dynamic declarations use exactly the same format as the top-level tools field.
- They apply per request and are not retained by the server, so keep the message in later request history yourself. Keeping it preserves both the tool's availability and the cached prefix; dropping it means the model can no longer call that tool and the changed prefix may miss the cache.
- Appending a dynamic declaration to the end of messages does not affect the cached prefix; removing or modifying an earlier declaration may hurt cache hits after the point of change.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a68e4a5b38eec947a86dda6_dynamic-tool-loading.png)

Recommended pattern for large tool catalogs:

1. **Conversation start:** declare only a single search_tools function (implemented by your backend) plus a few core tools, and advertise searchable domain tags in the system prompt.
2. **First turn:** set tool_choice: "required" to force retrieval before answering.
3. **Inject on demand:** insert the full definitions of matching tools via a system message based on retrieval results.
4. **Call directly:** the model uses the loaded tools in subsequent generations.
5. **Cost trade-off:** decide reasoning_effort before the conversation starts.

Code Example:

### 1M context and automatic caching

Together supports the full 1M context length, and context caching is automatic. Keep your long prefix (system prompt, knowledge base, repo dump) byte-stable across requests so later calls can hit the cache. Moonshot recommends placing fixed bulk context (knowledge documents) at the very beginning of the messages array, ahead of the system message, then appending questions and replies after it.

### Sampling parameters

The sampling parameters are fixed and you should omit them from requests. The model was trained using these params and does not support setting alternatives:

- temperature = 1.0
- top_p = 0.95
- n = 1
- presence_penalty = 0
- frequency_penalty = 0

### Preserved thinking

K3 was trained in preserved thinking history mode, so the trace is the state the next turn depends on. Use the following to preserve thinking tokens from the previous turn and forward them to future turns.

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a68e46dd07bdd9524b1aaef_preserved-thinking.png)

Drop the reasoning_content line and the same call answers with a different freshly-invented number every time. In real code you never hand-write the trace; you replay what the model produced, which is the one-liner from the tool loop:

## Kimi K3 pricing

Kimi K3 is priced per token, with a cache-hit input tier that rewards stable prefixes:

![](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/6a68e48397acbd85596f43b3_cost-anatomy.png)

Two cost aspects to internalize:

- **The cache is your lever.** With a >90% hit rate in coding workloads, effective input cost trends toward the \$0.30 floor, but only if you keep prefixes stable. Restructuring earlier messages or tool declarations will break it.
- **Reasoning is billed as output and can be dialed in.** Thinking tokens are output tokens at \$15/M and thinking cannot be fully disabled, but reasoning_effort now has three levels. max remains the default, so a pipeline that never sets the field is paying the maximum reasoning bill on every call, including the trivial ones.

## Kimi K3 benchmarks

Across the evaluation suite, Kimi K3 posts frontier-level numbers. It leads the field on several coding and agentic benchmarks (SWE Marathon, BrowseComp, DeepSearchQA, AutomationBench, OmniDocBench) and stays competitive with the strongest proprietary models on others, while clearly outperforming the other open model tested, GLM-5.2. On a handful of benchmarks it trails Claude Fable 5 and GPT 5.6 Sol, which is consistent with Moonshot's own positioning of the model.

All Kimi K3 results below use reasoning effort set to max.

## How Kimi K3 compares to the frontier

Aggregate benchmark tables only go so far. For a head-to-head read on cost, coding quality, and routing behavior, we ran Kimi K3 against the leading proprietary models on DeepSWE:

- [Kimi K3 vs GPT 5.6 Sol on DeepSWE: cost, coding, and routing](https://www.together.ai/blog/kimi-k3-vs-gpt-5-6-sol-on-deepswe-cost-coding-and-routing)
- [Kimi K3 vs Claude Fable 5 on DeepSWE: cost and coding](https://www.together.ai/blog/kimi-k3-vs-claude-fable-5-on-deepswe-cost-and-coding)

## Frequently asked questions

**What is Kimi K3?** Kimi K3 is Moonshot AI's flagship 2.8-trillion-parameter model and the first open-source model in the 3-trillion-parameter class, built for long-horizon coding, knowledge work, and reasoning.

### **Is Kimi K3 open source?** 

Yes. It is released as an open-weights model, and Together AI works directly with the Moonshot team to serve it.

### **What is Kimi K3's context window?** 

1M tokens (1,048,576), supported in full on Together AI with automatic context caching.

### **How much does Kimi K3 cost on Together AI?** 

\$0.30 per 1M cache-hit input tokens, \$3.00 per 1M cache-miss input tokens, and \$15.00 per 1M output tokens.

### **Can you turn off thinking on Kimi K3?** 

On Together AI you can disable thinking with reasoning={"enabled": False}, or dial reasoning depth with reasoning_effort set to low, high, or max.

### **Does Kimi K3 support vision?** 

Yes. It has native vision and accepts multiple images per request, as long as the total request body stays under 100 MB.

## Kimi K3 is on Together AI. Run it and ship it to production.

Making K3 yours starts with a single API call.

- Run Kimi K3 inference: [Kimi K3 API on Together AI](https://www.together.ai/models/kimi-k3)
- Start building with the API: [read the docs](https://docs.together.ai/docs/quickstart)
