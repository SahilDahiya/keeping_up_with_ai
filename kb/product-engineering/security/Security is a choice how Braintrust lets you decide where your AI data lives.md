---
title: 'Security is a choice: how Braintrust lets you decide where your AI data lives'
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: Explains data-control choices for AI observability, including where data
  lives, how security boundaries are enforced, and deployment implications.
source: braintrust
url: https://www.braintrust.dev/blog/security-data-control
author: Braintrust Team
published: '2026-01-21'
fetched: '2026-07-11T04:33:38Z'
classifier: codex
taxonomy_rev: 1
words: 489
content_sha256: fd095b267194fcd29e323ffd2f5dc9aa12d8329b02442d547bc794e36d1e1988
---

# Security is a choice: how Braintrust lets you decide where your AI data lives

Jan 21, 2026Ross Stapleton-Gray3 min

Building AI products means handling your most sensitive data: customer conversations, proprietary prompts, and production traces. For security teams evaluating AI infrastructure, one question matters most: where does my data actually live?

Braintrust supports multiple deployment options to meet you where you are:

**Fully managed SaaS**: Fast onboarding with enterprise-grade security. SOC 2 Type II certified, HIPAA compliant, with all data encrypted in transit and at rest. Comprehensive access controls and regular security audits. Customer data is hosted in AWS, with regional choice including the EU.

**Hybrid deployment**: The best of both worlds for teams with strict data residency or compliance requirements. Hybrid deployment addresses the specific needs of security-conscious organizations.

Braintrust's [hybrid deployment model](https://www.braintrust.dev/blog/hybrid-deployment) separates the **control plane** (UI, metadata, authentication) from the **data plane** (your actual AI data). Here's what that means for security:

**Your data plane lives entirely in your environment.** All experiment logs, traces, datasets, prompts, completions, and customer inputs stay within your VPC or on-premises infrastructure. Braintrust's servers never store or proxy this sensitive data.

**The control plane handles only metadata.** Braintrust manages the web UI, authentication (via Clerk), and lightweight metadata like project names and API key hashes. Zero AI data transits through our infrastructure.

**You get SaaS convenience with on-prem control.** Instant UI updates and new features without manually upgrading anything, while your sensitive data remains behind your firewall or VPN.

Configure global masking functions to automatically redact PII (emails, phone numbers, SSNs) before logging data. Masking applies to inputs, outputs, metadata, and context fields, ensuring sensitive information never leaves your environment unprotected.

Deploy behind your firewall with your own identity access management policies, encryption key management, and audit trails. Use VPC peering, private networking, or complete air-gapping. The control plane never requires network access to your data plane; all browser and SDK requests go directly to your infrastructure via CORS.

Braintrust's AI assistant, Loop, helps teams analyze logs and optimize prompts, but no models are trained on your data. Your prompts, traces, and customer conversations remain private and are never used to improve models.

- **SOC 2 Type II certified**with comprehensive security controls
- **HIPAA compliant**with Business Associate Agreements available
- **Encryption everywhere**: TLS 1.2 in transit, AES-256 encryption at rest for all data
- **Role-based access control**with SSO, granular permissions, and project isolation

- [Trust Center](https://trust.braintrust.dev/): Access SOC 2 reports, security controls, and compliance documentation
- [Security documentation](https://www.braintrust.dev/docs/security): Detailed technical security architecture and policies
- [Hybrid deployment guide](https://www.braintrust.dev/blog/hybrid-deployment): Deep dive into our architecture and data flow
- **Terraform modules**: Deploy with official infrastructure-as-code templates for- [AWS](https://github.com/braintrustdata/terraform-aws-braintrust-data-plane),- [GCP](https://github.com/braintrustdata/terraform-google-braintrust-data-plane), and- [Azure](https://github.com/braintrustdata/terraform-azure-braintrust-data-plane)

Hybrid deployment gives you enterprise-grade security and complete data control, with the speed and innovation of a modern SaaS platform. Companies like Notion, Stripe, Zapier, Ramp, and Coursera trust Braintrust to handle their most sensitive AI workloads.

Ready to evaluate Braintrust? Start with our [Trust Center](https://trust.braintrust.dev/) or reach out at [info@braintrust.dev](mailto:info@braintrust.dev) to discuss your security requirements.
