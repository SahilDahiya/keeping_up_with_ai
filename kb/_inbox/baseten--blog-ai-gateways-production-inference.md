---
title: The two AI gateway patterns in production inference
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ai-gateways-production-inference/
author: Amit Gambhir
published: '2026-08-25'
fetched: '2026-08-26T06:09:32Z'
classifier: null
taxonomy_rev: 2
words: 2432
content_sha256: b0f0e89df8a718e111c3d72c3350add292e15543a0349e154830e7ad873b1f0e
---

# The two AI gateway patterns in production inference

![A guide to AI gateways in production](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787612433-baseten-blog-2026-thumbnails-15.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

An AI gateway centralizes the decisions surrounding a model request: who can make it, where it goes, what limits apply, what happens when infrastructure degrades, and how usage is measured. One useful way to understand the category is through two dominant patterns: gateways that help applications access many model providers, and gateways that help model owners serve their own models to many customers. Ultimately, gateway selection is more of an architectural decision than a procurement one.

## Every model request carries more decisions than a prompt

A customer sends a request to your model API. Before the model generates a single token, your system has to answer a surprising number of questions:

1. Is the API key valid?
2. Which customer and plan does it represent?
3. Which model or deployment should serve the request?
4. Has the customer reached a usage limit?
5. Is the serving infrastructure healthy?
6. How will consumption be attributed?
7. And if part of the system is degraded, what should the customer see?

Every production AI system answers these questions somewhere. Without a deliberate architecture, the answers spread across application code, authentication services, infrastructure configuration, billing pipelines, and incident-response procedures, each with its own view of the request.

An AI gateway brings those decisions into a consistent control layer. That layer is carrying more weight than it used to. Menlo Ventures estimated that enterprise spending on model APIs grew from roughly $3.5 billion in late 2024 to $8.4 billion by mid-2025 ([source](https://menlovc.com/perspective/2025-mid-year-llm-market-update/)). Model calls now represent a meaningful and fast-growing operating expense, revenue stream, or both.

The underlying systems have also changed: teams are no longer serving a single model behind a single endpoint. They are operating multiple model versions and deployments, exposing APIs to external customers, and treating inference as revenue-generating infrastructure.

These questions matter to any team running AI in production, but they become existential when you own, fine-tune, or operate the models and need to expose them safely to multiple customers. In that situation, the gateway is no longer “just” a convenient interface to someone else's API. It becomes part of the product you are selling.

## Most AI gateways follow one of two patterns

"AI gateway" has become a broad label for products that handle model routing, authentication, observability, cost controls, reliability, governance, or some combination of them. In practice, most production deployments follow one of two dominant patterns.

![Two dominant AI gateway patterns: application-side access to multiple model providers, and customer-facing access to models you operate.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787665003-1_trust-graph-a-3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Two dominant AI gateway patterns: application-side access to multiple model providers, and customer-facing access to models you operate.

### Access gateway: one application, many model providers

In the first pattern, the application team is the gateway's primary user. The gateway presents one interface across different provider APIs, centralizes credentials and policy, collects usage data, and supports switching or falling back to external model services.

This is the pattern most developers first associate with an AI gateway. Cloudflare AI Gateway, Kong AI Gateway, LiteLLM, OpenRouter, Portkey, and the Vercel AI Gateway are all commonly evaluated for application-side access and routing, although several span more than one function.

### Serving gateway: your model, many customers

The second pattern reverses the traffic relationship: the gateway sits between external customers and the models your organization operates. The model owner — not an application consuming third-party APIs — is its primary user.

The serving gateway’s job is to issue credentials, isolate tenants, enforce limits, expose a stable and branded API, meter consumption, and connect customer traffic to production model deployments.

Both patterns centralize policy around model requests, but they optimize for different owners, traffic flows, and operational problems. Teams that treat them as interchangeable end up evaluating the wrong products.

The question that separates the patterns is: whose traffic is the gateway controlling, and on whose behalf is it making decisions? An access gateway controls your application's outbound model traffic on behalf of an engineering or platform team. A serving gateway controls your customers' inbound traffic on behalf of your model business. That difference shapes the significance of nearly every capability.

## How a serving-side gateway processes a request

The rest of this article follows the serving side. It's the less documented of the two patterns, and it's the one that changes your architecture most when you're the one who owns the models.

The clearest way to understand what a serving gateway owns is to trace a single customer request through it.

![A serving-side gateway carries customer identity and context across routing, protection, inference, metering, and auditing.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1787664956-2_processing-a-request-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A serving-side gateway carries customer identity and context across routing, protection, inference, metering, and auditing.

### Establishing identity

The gateway validates the credential and resolves it to the appropriate customer context: an organization, user, project, plan, or entitlement.

The credential is the join key connecting a request to limits, usage records, billing, support, and audit history. A gateway that can tell you a key is valid, but not which customer or commercial policy it represents, can authenticate traffic, but can't operate a business on it.

### Selecting the serving path

Once the caller is known, the gateway resolves the requested model and selects an eligible serving path, such as a deployment, region, capacity pool, or model version. In more sophisticated systems, that decision can take into account backend state: deployment health, capacity, or [KV cache locality](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/#how-kv-aware-routing-works), so requests land where their existing context can be reused.

Model routing is tied to model identity, capacity, availability, and customer policy; keeping that policy in the gateway lets teams change how a model is served without modifying every product that calls it.

### Protecting the service

The gateway applies the policies that protect both the infrastructure and the other customers using it: request or token limits, concurrency constraints, overload protection, and tenant isolation. These controls keep one tenant's bad afternoon from becoming every tenant's bad afternoon.

Complete outages are the obvious worst-case. Production systems more often experience partial degradation: a backend slows without failing, a customer produces an unexpected burst, or a region approaches capacity. A serving gateway needs a clear answer for those conditions, not only for whether a service is technically up or down.

### Measuring usage

After a request is served, the model owner needs to know what was consumed and by whom. Relevant units may include input and output tokens, characters, requests, duration, or another model-specific measure. That usage must be associated with the correct customer and serving path.

These records support invoicing, pricing, capacity planning, margin analysis, customer support, and abuse detection. Placing the responsibility in application code leads to duplicated implementations that must independently handle streaming, partial failures, and reconciliation with the inference system. Metering belongs in the layer that sees every request.

### Producing an auditable result

Finally, the system records what happened: which deployment served the request, at what latency, with what errors (if any), usage, and under which policy decisions.

The distinguishing requirement is the join between the external customer request and the underlying inference event. Without it, teams debug two disconnected systems: the API surface customers see, and the infrastructure that generated the response. When a customer disputes a bill or reports a slow request, that join is the difference between a clear answer and an investigation.

## What to evaluate in an AI gateway

Every gateway advertises authentication, routing, and observability. But those features do not tell you whether the architecture is right; these questions do.

### Can it represent your customer model?

A production model business rarely has a flat list of API keys. Customers may contain users and projects; plans may have different limits; and enterprise accounts may need credential rotation without losing usage history.

Evaluate whether the gateway's identity model aligns with how you expect to sell and support the API, not just whether it can generate a key.

### Can it protect tenants from one another?

Ask how the gateway behaves when one customer bursts, exhausts a quota, creates excessive concurrency, or floods the API with malformed traffic.

Plenty of gateways have limits on paper. The real test is whether the gateway holds the commercial and operational boundaries of your service when the underlying model approaches capacity. Isolation is easy to claim and hard to verify: ask how it works, not whether it exists.

### Can it support a commercial API?

The gateway should provide a reliable identity-and-usage layer for billing, credential management, customer support, and reconciliation.

It doesn't have to become your invoicing or subscription-management system. But those systems need trustworthy data from somewhere.

### What does it know about inference?

A traditional gateway understands HTTP requests, endpoints, and status codes. An inference-aware gateway can also understand deployments, streaming generation, token consumption, backend health, and model-specific performance signals. That context determines what it can measure and which decisions it can make safely.

The tradeoff is: a gateway disconnected from inference may offer greater portability or provider neutrality, but more context must be reconstructed through integrations. A gateway closer to inference may have deeper operational awareness, but you should look closely at how portable that integration is, and who's operating the gateway when something breaks at 2 a.m.

### Where does it run?

A gateway may run in the application layer, as an independently operated service, or alongside the inference platform. Its location determines which decisions can happen inside the inference path, how much backend context is available, and whether another service boundary sits between policy enforcement and token generation. It also changes failure domains, data paths, observability, deployment ownership, identity integration, and portability.

The correct choice follows from what traffic the gateway controls: access-side traffic tends to point toward the application layer or an independently operated proxy. Serving-side traffic points toward the inference layer. The answer follows from who owns the models.

### What must your team still build?

No gateway eliminates every part of operating a commercial model API. Your team may still need a developer portal, subscription management, invoicing, customer analytics, or support tooling.

Ask not only what the gateway provides, but what remains between its capabilities and the complete customer experience you plan to launch.

## For model labs, key gateway decisions often belong closest to inference

Let’s return to the organizational question: what traffic is the gateway controlling, and on whose behalf is it making decisions? For a model lab offering an API, the answers are: your customers' traffic, and on your behalf.

An access gateway can often treat model providers as interchangeable HTTP endpoints because, from the application's perspective, that is what they are. A serving gateway cannot. Its decisions are directly connected to the infrastructure running the models: which customers are authorized, how much they can consume, what usage their requests generate, and whether the deployments underneath can serve them reliably.

For teams serving their own models, the highest-leverage gateway decisions often belong closest to inference. Integrating the serving layer with inference offers concrete benefits; policy can be applied before expensive model execution. Customer identity and usage attribution can be handled by the same system. The gateway can operate with awareness of the deployments beneath it rather than reconstructing their state from outside. And there are fewer independently operated components between a customer request and a model response.

None of this makes application-side or provider-neutral gateways unnecessary. They solve a different problem, and one organization may legitimately run both: one gateway governing how internal applications consume external models, and another serving the organization's own models to customers.

## How Baseten Frontier Gateway implements this architecture

The distinction between a serving gateway and an inference gateway becomes concrete when you look at how a serving-side gateway is implemented.

The [Baseten Frontier Gateway](https://www.baseten.co/blog/introducing-baseten-frontier-gateway/) is a managed serving-side gateway for teams exposing Baseten-hosted models as production, multi-tenant APIs. It is built on Baseten [Dedicated Inference](https://www.baseten.co/products/dedicated-inference/), giving model labs the customer-facing controls described above without requiring them to build and operate a separate gateway system.

### Manage customer access

Frontier Gateway generates and manages the API keys that labs distribute to downstream customers. Every request is authenticated and authorized before it reaches the model, with those controls handled natively in the inference path rather than in application code or a separately operated proxy.

### Enforce usage limits

Labs can apply token- or request-based usage limits per API key, protecting deployments from abuse and helping prevent one tenant's traffic from degrading service for everyone else. Limits can be scoped per group (with users mapped to a group) and per model, and keys inherit their group's limits, so rotating a customer's credentials doesn't change their spend posture.

### Attribute model consumption

Frontier Gateway tracks token and character consumption per API key, giving labs customer-level usage records without requiring them to wrap billing and metering logic around every inference call.

### Serve the API under your brand

Requests are exposed through a lab-branded domain while Baseten routes them to the underlying inference infrastructure. Customers integrate with your API and your brand, not Baseten’s.

### Operate on production inference infrastructure

The Baseten Frontier Gateway is co-located with the inference infrastructure it governs. Labs inherit the platform underneath, including elastic, pay-as-you-go GPU capacity, inference observability, Baseten's enterprise-grade security and compliance posture, and high uptime SLAs.

When [Poolside launched its Laguna models](https://www.baseten.co/resources/customers/how-baseten-powered-poolsides-model-launch-in-record-time/), its whitelabeled API was live on Frontier Gateway within 48 hours of account creation, with a P50 time to first token (TTFT) of 146 ms for Laguna XS.2 and 605 ms for Laguna M.1.

Frontier Gateway is built for the serving pattern rather than the access pattern, which is exactly what lets it operate inside the inference path. That said, Frontier Gateway is designed for teams serving models running on Baseten; it is not positioned as a universal proxy for routing application traffic across third-party proprietary API providers.

## From model weights to a product that customers can use

A trained model is several steps away from becoming a usable model API. Between the two sits everything this article has described: identity, tenancy, limits, reliability, metering, observability, and a stable developer-facing endpoint.

This is the layer where a model stops being a research artifact and starts becoming a product. Every production AI system has a gateway, even if its responsibilities are scattered across application code, infrastructure, and operational tooling. The architectural decision is not whether those responsibilities will exist; it is whether you will build them intentionally.

If you need help turning your model into a scalable, production API, [reach out](https://www.baseten.co/talk-to-us/) to talk to our engineers, or learn more about the Baseten Frontier Gateway [here](https://www.baseten.co/products/frontier-gateway/).
