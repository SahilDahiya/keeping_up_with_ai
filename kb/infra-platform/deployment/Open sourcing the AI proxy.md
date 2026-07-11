---
title: Open sourcing the AI proxy
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/security
summary: Open-source AI proxy notes focused on provider routing, logging, credentials,
  access control, and observability for model calls.
source: braintrust
url: https://www.braintrust.dev/blog/open-sourcing-proxy
author: Braintrust Team
published: '2023-11-27'
fetched: '2026-07-11T04:33:17Z'
classifier: codex
taxonomy_rev: 1
words: 528
content_sha256: 7a1fa0f9ddbc2420a0c99ee24768fe9a48c53288048e757bd8223a59a9bb29de
---

# Open sourcing the AI proxy

27 November 2023Ankur Goyal3 min

Last week, we released the [Braintrust AI Proxy](https://www.braintrust.dev/blog/ai-proxy), a new, free way to access LLaMa2, Mistral,
OpenAI, Anthropic, and many [other models](https://www.braintrust.dev/docs/deploy/ai-proxy#supported-providers) behind the OpenAI protocol with
built-in caching and API key management.

Folks immediately started reaching out about running the proxy in production. We firmly believe
that code on the critical path to production should be open source, so we're excited to announce that the
proxy's source code is now available on [GitHub](https://github.com/braintrustdata/braintrust-proxy) under the
[MIT license](https://github.com/braintrustdata/braintrust-proxy).

You can continue to access the proxy, for free, by using the hosted version at `https://braintrustproxy.com`. It's hosted
on [Cloudflare workers](https://workers.cloudflare.com/) and end-to-end encrypts cached data using 256-bit AES-GCM encryption.
For more details, see the [documentation](https://www.braintrust.dev/docs/deploy/ai-proxy) or [source code](https://github.com/braintrustdata/braintrust-proxy/tree/main/apis/cloudflare).

The repository also contains [instructions](https://github.com/braintrustdata/braintrust-proxy/blob/main/README.md#deploying) for deploying the
proxy to [Vercel Edge Functions](https://vercel.com/docs/functions/edge-functions), [Cloudflare workers](https://workers.cloudflare.com/),
[AWS Lambda](https://aws.amazon.com/lambda/), or as a plain-old [Express server](https://expressjs.com/).

I did some quick benchmarks, from my in-laws' place in California and an EC2 machine (US East N. Virginia) to compare performance across options ([code](https://gist.github.com/ankrgyl/eefb0940399f89aa69e5b0b3145a373e)).
The AWS Lambda functions are deployed in `us-east-1`. `aws-pc` is AWS Lambda with [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html).

In-laws (CA)

bash

```
$ python proxy_benchmark.py -n 100
cloudflare: AVG: 57.98ms,   MIN: 42.39ms,   MAX: 258.04ms
vercel:     AVG: 82.05ms,   MIN: 54.65ms,   MAX: 326.60ms
aws:        AVG: 131.95ms,  MIN: 103.64ms,  MAX: 722.90ms
aws-pc:     AVG: 145.10ms,  MIN: 109.22ms,  MAX: 1704.05ms
```
EC2 (US East N. Virginia)

bash

```
$ python proxy_benchmark.py -n 100
cloudflare: AVG: 32.23ms,   MIN: 20.15ms,   MAX: 283.90ms
vercel:     AVG: 55.72ms,   MIN: 25.03ms,   MAX: 512.94ms
aws:        AVG: 43.91ms,   MIN: 22.20ms,   MAX: 130.78ms
aws-pc:     AVG: 68.13ms,   MIN: 24.46ms,   MAX: 973.50ms
```
As you can see, Cloudflare and Vercel are consistently very fast, and AWS Lambda in US East suffers (as expected) when measured from CA. I was surprised that AWS Lambda with provisioned concurrency was slower than without. Perhaps I misconfigured something...

Along with the open source release, the proxy contains a number of useful built-in features.

The proxy automatically caches responses from the model provider if you set a `seed` value or `temperature=0`.
Seeds are a new feature in the OpenAI API that allows you to create reproduceable results, but most model providers
do not yet support them. The proxy automatically handles that for you.

You can add API keys across providers as [secrets in Braintrust](https://www.braintrust.dev/app/settings?subroute=secrets), and use a single
API key to access all of them. This is a great way to manage your API keys in one place, and share them with your team.

You can now add multiple keys and organizations as [secrets in Braintrust](https://www.braintrust.dev/app/settings?subroute=secrets),
and the proxy will automatically load balance across them for you. This is a simple way to add resiliency across OpenAI accounts
or providers (e.g. OpenAI and Azure).

You can access Azure's OpenAI endpoints through the proxy, with vanilla OpenAI drivers, by configuring Azure endpoints in
[Braintrust](https://www.braintrust.dev/app/settings?subroute=secrets). If you configure both OpenAI and Azure endpoints,
the proxy will automatically load balance between them.

![Configure secrets](https://www.braintrust.dev/blog/img/secrets-endpoint-config.gif)


We have an exciting roadmap ahead for the proxy, including more advanced load balancing/resiliency features, support for more models/providers, and deeper integrations into Braintrust.

If you have any feedback or want to collaborate, [send us an email](https://www.braintrust.dev/contact) or join
our [Discord](https://discord.gg/6G8s47F44X).
