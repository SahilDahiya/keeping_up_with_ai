---
title: A note on the Hugging Face agent incident | Modal Blog
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/computer-use
summary: Modal clarifies that in the Hugging Face agent intrusion, the compromised
  environment was a customer's own unauthenticated, publicly-exposed Sandbox endpoint
  that executed untrusted submitted code, not a breach of Modal's platform or isolation;
  recommends authentication, IP allowlisting, and outbound restrictions for public-facing
  sandboxes.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/a-note-on-the-hugging-face-agent-incident
author: null
published: '2026-07-27'
fetched: '2026-07-29T06:53:09Z'
classifier: claude
taxonomy_rev: 2
words: 176
content_sha256: f76991d85b153aee9392c0c1d0cb6a8e5b01967684e2369a6ccd8717ed8ac473
---

# A note on the Hugging Face agent incident | Modal Blog

[Back](https://modal.com/blog)

# A note on the Hugging Face agent incident

Hugging Face published a [technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) of a recent agent intrusion, which names Modal as the third-party infrastructure the agent used as a launchpad.

**Modal's platform and isolation were not compromised in any way.**

The environment involved was a customer's own application. It was deployed to a endpoint that was publicly accessible without authentication, and it was designed to compile and execute code submitted by anyone on the internet in a Modal Sandbox. The code execution the attacker obtained took place inside that customer's own container, within Modal's standard sandbox isolation boundary. No other customer workloads were affected.

While customers can expose Sandboxes to unauthenticated traffic, this is never the default, and Modal provides the authentication, network, and monitoring controls to keep production workloads locked down. We recommend that anything exposed to the public internet require [authentication](https://modal.com/docs/guide/sandbox-networking#connecting-to-sandboxes-with-http-and-websockets), [IP allowlist,](https://modal.com/docs/guide/sandbox-networking#inbound-access-control) [restrict its outbound network access](https://modal.com/docs/guide/sandbox-networking#outbound-access-control) to only what it needs, and treat any code or input it accepts from users as untrusted.

For additional questions, email [security@modal.com](https://modal.com).
