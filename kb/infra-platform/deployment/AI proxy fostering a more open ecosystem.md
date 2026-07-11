---
title: 'AI proxy: fostering a more open ecosystem'
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/security
summary: Introduces an AI proxy pattern for routing model calls across providers while
  centralizing logging, credentials, access control, and production visibility.
source: braintrust
url: https://www.braintrust.dev/blog/ai-proxy
author: Braintrust Team
published: '2023-11-20'
fetched: '2026-07-11T04:31:19Z'
classifier: codex
taxonomy_rev: 1
words: 1106
content_sha256: 878f488530d6e94ee229f45fdc38d8e0b17549bc2524b26664cd6a24819f14d8
---

# AI proxy: fostering a more open ecosystem

20 November 2023Ankur Goyal7 min

Like most of us, I spent last weekend thinking about the past, present, and future of AI. It's hard to imagine the industry
without OpenAI — an institution we all look to, respect, and rely on — at its forefront. I for one am rooting for the
company and brilliant folks who work there to continue leading the way. However, I also realized that the AI ecosystem
benefits from being interoperable and default open and that we at [Braintrust](https://braintrustdata.com/) have an
important role to play in that.

For months, a few key challenges in AI development have been nagging me:

- The prevailing LLM toolset is the OpenAI SDK. However, because the libraries are specific to OpenAI, you end up writing code that is not interoperable with other providers, making it harder to evaluate alternatives.
- While developing LLM apps, I frequently rewrite small pieces of code, and re-run the same AI calls over and over again. Each time, I implement a slightly different cache, because of the proliferation of languages and platforms.
- It's a pain to manage API keys within and across providers, e.g. to load balance and dynamically route workloads. I wish I could just manage a single API key, specify the model, and let a system automatically call the right system for me.

This weekend felt like the perfect time to address these challenges. I'm very excited to announce the newest feature of Braintrust:
an AI proxy. The proxy addresses the above pain points by embracing OpenAI's interface as the *lingua franca* for
LLMs, and adding caching, logging, and API key management behind the scenes. It also supports popular open source models like
[LLaMa 2](https://ai.meta.com/llama/) and [Mistral](https://mistral.ai/) via [Perplexity](https://www.perplexity.ai/)
and all of [OpenAI's](https://platform.openai.com/docs/models) and
[Anthropic's](https://docs.anthropic.com/claude/reference/getting-started-with-the-api) models.

If you have something built on GPT-4 or another model, you can now try it out on LLaMa2, Mistral, Anthropic, or others — and vice versa — without changing any code. We believe this is just the start and that the AI proxy will enable our current and future customers to build robust, low latency systems that work across a thriving and open ecosystem of model providers.

Before we get into the details, here's a quick demo + instructions to try it out. You can use your favorite OpenAI drivers, and
set the base url to `https://api.braintrust.dev/v1/proxy`. Try running the following script in your favorite language, twice.

javascript

```
const client = new OpenAI({
  baseURL: "https://api.braintrust.dev/v1/proxy",
});
async function main() {
  const start = performance.now();
  const response = await client.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: "What is a proxy?" }],
    seed: 1, // A seed activates the proxy's cache
  });
  console.log(response.choices[0].message.content);
  console.log(`Took ${(performance.now() - start) / 1000}s`);
}
main();
```
If you have access to Perplexity or Anthropic, feel free to use their API keys with `mistral-7b-instruct` or
`claude-instant-1.2` instead. Under the hood, we're proxying the requests, caching the results with end-to-end
encryption, and streaming back the results.

Read on to learn more technical details, or check out
[the docs](https://www.braintrust.dev/docs/deploy/ai-proxy).

The AI proxy is optimized for a few key objectives: low latency, security, and portability:

- Latency was the toughest to achieve — although there are a variety of techniques to run code close to users,
we settled on [Cloudflare Workers](https://workers.cloudflare.com/)which offer a unique combination of low latency, streaming support, and low cost. In our tests, we're able to get end-to-end latencies consistently under 100ms and often around 50ms, when results are cached.
- Our customers tend to be very security conscious, so we wanted to make sure our cache cannot (even theoretically) leak data across users. We achieve this by encrypting model responses using your API key (which we do not store or log) and 256-bit AES-GCM encryption. We are also in talks with the Cloudflare team to support additional security measures for enterprise customers.
- We're betting on the OpenAI API protocol as the *lingua franca*for LLMs, and therefore mapping each supported provider into an OpenAI compatible format. As far as we know, this is the first, and if not, certainly the easiest, way to access Anthropic's models by swapping in`claude-2`for`gpt-4`. We'll figure out a way to make this scale — via open source or other forms of open collaboration.

The feature I'm personally most excited by is the cache. When I'm writing code, I like to tinker and re-run things very often. For example, I was recently working on an LLM-based list-of-strings comparator and tweaked the threshold at which I use an LLM to compare strings. Each time I tweaked this threshold, a majority of the string comparisons were the same, but I'd waste minutes (!) waiting for GPT-4 to recompute the same results.

The AI proxy solves this problem by caching model calls for you, both ordinary and streaming. By default,
requests with `temperature=0` or the new [ seed parameter](https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter),
are cached. You can also set the

`x-bt-use-cache` to `always` or `never` to more directly control this behavior.Because the cached values are encrypted in terms of your API key, the cache is not shared across users. Braintrust customers can choose to share cached values across users in their organization.

You can use your OpenAI, Anthropic, and Perplexity API keys to access their respective models. However, if you're a Braintrust user, you can create a single API key that will work across services (even on the free plan). Create a Braintrust account and enter a value for each service you'd like to use:

![Secret configuration](https://www.braintrust.dev/blog/img/secret-config.png)


Then, pass your [Braintrust API key](https://www.braintrustdata.com/docs#create-an-api-key) into the SDK instead
of a provider-specific one. When you issue a request, the proxy will translate your Braintrust API key into the
appropriate secret behind the scenes. We believe this pattern is very powerful — you can configure how you want
the proxy to behave behind the scenes without changing a single line of code — and are already working on features
like deeper integration within Braintrust's evaluation and logging tools, load balancing, and model routing.

The AI proxy is available for all to use, for free, as a beta. You get a common interface across providers and
caching out of the box, and if you create a [Braintrust account](https://braintrustdata.com/), you can configure
a single API key to work across OpenAI, Anthropic, and Perplexity, as well as a number of other powerful features
like [evaluations]([https://www.braintrustdata.com/docs/evaluate](https://www.braintrustdata.com/docs/evaluate), [logging](https://www.braintrustdata.com/docs/instrument),
and more.

We hope it's straightforward enough to use that you'll always just use `https://api.braintrust.dev/v1/proxy` as a default base
url. We are also interested in expanding the proxy's features, providers, and of course fixing bugs and
improving performance. Let us know your thoughts by [email](https://www.braintrust.dev/contact) or on
[discord](https://discord.gg/6G8s47F44X).
