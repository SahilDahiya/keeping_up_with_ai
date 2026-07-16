---
title: 'Skills on steroids: on-demand capabilities in Pydantic AI'
kind: blog
topic: prompt-engineering
subtopic: context-engineering
secondary_topics:
- agents/tool-use
summary: 'Introduces progressive disclosure for agent capabilities in Pydantic AI:
  mark a capability defer_loading=True so it collapses to a one-line id+description
  in context, and the model calls load_capability to inject the full instructions/tools
  bundle only when it decides it needs it, cutting input tokens spent loading context
  that has no chance of being used on a given turn.'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/pydantic-ai-capabilities
author: Aditya Vardhan
published: '2026-06-22'
fetched: '2026-07-16T22:03:03Z'
classifier: claude
taxonomy_rev: 2
words: 415
content_sha256: b37f2075ac6d58d62b15b94a1cf33c95db2a90736274c42b554ff203b9f86eb6
---

# Skills on steroids: on-demand capabilities in Pydantic AI

We asked our users which features they wanted and skills came up on top. We dug into what they actually meant when they said "skills", and it was the same answer every time: ** progressive disclosure**.

![Always has been](https://pydantic.dev/assets/blog/skills-on-steroids/always-has-been.jpg)


*(My colleague  David Sanchez shared this on our call when we were designing the feature.)*


Before this, adding a capability meant loading everything onto the model immediately: instructions, tools, all of it, every request, whether it was needed or not.

AI stopped being a free lunch a while ago. Input tokens cost money, and loading context that has no chance of being useful on a given turn is a colossal waste.


Mark a capability with `defer_loading=True` and give it an `id`. That's it. In context, the full bundle collapses to a single line: just the `id` and an optional `description`.

The model starts with a catalog of what's available and nothing more. When it decides it needs a capability, it calls `load_capability`, and we inject the full bundle in one shot. The model asks for it, the model gets it.

```
from pydantic_ai import Agent
from pydantic_ai.capabilities import Capability
orders = Capability(
    id='orders',
    description='Use for order tracking and delivery status.',
    instructions='Always quote the order ID when discussing an order.',
    defer_loading=True,
)
@orders.tool
def order_status(ctx, order_id: str) -> str:
    """Look up shipping status for an order."""
    return f'Order {order_id}: in transit'
agent = Agent(
    'anthropic:claude-sonnet-4-6',
    instructions='You are a customer support agent.',
    capabilities=[orders],
)
```

Instructions? Served only when the model actually needs them.

Model settings? Set per capability, applied when it loads.

Hooks? Structurally gated. Only triggers if the capability is loaded.

That's the whole idea. Your agent knows what it has available. It reaches for what it needs. Everything else stays out of the way until it's useful.

Mark your capabilities with `defer_loading=True` and watch your token costs tank.


On-demand capabilities are in Pydantic AI now:

```
uv add pydantic-ai
```
Mark your heaviest capabilities with `defer_loading=True`, give each an `id`, and let the model reach for them when it needs them.

The [capabilities docs](https://pydantic.dev/docs/ai/core-concepts/capabilities/#on-demand-capabilities) have the full reference.

If it shrinks your context (and your bill), a star on [GitHub](https://github.com/pydantic/pydantic-ai) helps other people find it.

Want to see which capabilities your agents actually load, token by token? [Pydantic Logfire](https://pydantic.dev/logfire) monitors Pydantic AI out of the box, with full-stack and AI traces in one platform. New Team and Growth accounts get a [$10 starter credit](https://pydantic.dev/articles/ai-gateway-starter-credit?utm_source=blog&utm_medium=cta&utm_campaign=pydantic-ai-capabilities) for inference through Pydantic AI Gateway, applied automatically when you upgrade.
