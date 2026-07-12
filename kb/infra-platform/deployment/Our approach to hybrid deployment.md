---
title: Our approach to hybrid deployment
topic: infra-platform
subtopic: deployment
secondary_topics:
- product-engineering/security
summary: Describes a hybrid deployment approach for AI observability, balancing managed
  services with customer-controlled data and infrastructure boundaries.
source: braintrust
url: https://www.braintrust.dev/blog/hybrid-deployment
author: Braintrust Team
published: '2025-01-08'
fetched: '2026-07-11T04:32:45Z'
classifier: codex
taxonomy_rev: 1
words: 565
content_sha256: 965238050eda9b9544049650ba6fbe5243b92bb8d680659f1f6cb0242bc5feef
---

# Our approach to hybrid deployment

8 January 2025Ornella Altunyan4 min

When it comes to using Braintrust as part of your LLM development workflow, we want to make sure you have full flexibility and control over your data. To accomplish this, we designed our architecture with two main components: the **data plane** and the **control plane**. The data plane is the component that handles the actual data, while the control plane serves the UI along with metadata. When you deploy Braintrust in hybrid mode, you host the data plane (experiment logs, dataset records, etc.) in your own environment, while the control plane (web app and metadata) is hosted by Braintrust. Customers like [Notion](https://www.notion.com/) and [Ramp](https://ramp.com/) use our hybrid deployment model to take advantage of our newest UI and platform features while simultaneously keeping sensitive data secure.

This model gives you the best of both worlds: security and compliance *and* UI updates. All your data, like experiment inputs/outputs, logs, and sensitive customer information, lives securely in your own environment. You can make sure it’s behind a firewall or VPN and meets your organization’s compliance requirements. And since the UI and metadata are hosted by Braintrust, you can visit our site to see the latest features and improvements, just like any other SaaS product. Our product engineering team can continuously polish every little detail and fix bugs instantly, and you don’t have to manually update anything.

Because the data plane runs entirely in your environment, Braintrust's servers and employees do not require access to it. All data requests from the Braintrust UI go directly from your browser to your self-hosted data plane (via CORS), bypassing our servers. The data plane sends only metrics and status telemetry back to the control plane, not logs, traces, or customer data.

The data plane contains your data:

- Experiment records (input, output, expected, scores, metadata, traces, spans)
- Log records
- Dataset records
- Prompt playground prompts and completions
- Human review scores

The control plane stores metadata:

- Experiment and dataset names
- Project names and settings
- Organization info
- API keys (hashed)
- Encrypted LLM provider secrets

Auth credentials are managed through our external authentication service ([Clerk](https://clerk.com/)).

In most setups, the Braintrust SDK will communicate with both your data plane and the control plane to retrieve various metadata, but it’s also possible to constrain all SDK communication solely to your data plane. You can [configure it](https://www.braintrust.dev/docs/admin/self-hosting/advanced#constrain-sdks-to-the-data-plane) so that the data plane acts as a proxy to the control plane, eliminating any need for outbound connections from the SDK to Braintrust’s servers.

- You get access to the latest Braintrust features automatically.
- You decide where to host the data plane and what data to purge, so you can meet any data residency requirements like GDPR.
- You can configure rate limits, custom URLs, and domain proxies to ensure the deployment works within your IT environment and security policies.

We provide a [Docker Compose configuration](https://github.com/braintrustdata/braintrust-deployment) file that you can use as-is or adapt to your infrastructure. After starting the containers, you’ll point to your newly hosted API in your Braintrust settings. From there, any time you load Braintrust via [braintrust.dev](https://braintrust.dev), your browser will connect to your self-hosted data plane to retrieve and store data.

You can also [self-host on AWS](https://www.braintrust.dev/docs/admin/self-hosting/aws) via Terraform.

For more information, check out the [self-hosting guide](https://www.braintrust.dev/docs/admin/self-hosting). We’re also happy to help set up advanced deployment scenarios— just reach out to [support@braintrust.dev](mailto:support@braintrust.dev).
