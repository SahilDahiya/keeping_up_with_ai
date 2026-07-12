---
title: Supporting privacy and compliance for EU teams
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: Covers privacy and compliance requirements for EU AI teams, including data
  residency, controls, and deployment choices for observability data.
source: braintrust
url: https://www.braintrust.dev/blog/eu-privacy-compliance
author: Braintrust Team
published: '2026-03-12'
fetched: '2026-07-11T04:32:03Z'
classifier: codex
taxonomy_rev: 1
words: 711
content_sha256: e716637213ea52e966bf18c2c41bc0bf8fcb21ec2691c4a412d3fd28bc0547cf
---

# Supporting privacy and compliance for EU teams

12 March 2026Ross Stapleton-Gray4 min

As Braintrust's customers build and ship AI-powered products, they both ingest and produce data of a scale and complexity that goes beyond traditional software. For the security, compliance, and risk teams in these organizations, this raises familiar questions about where the data lives and how it's controlled.

These concerns are especially acute for organizations that manage data from or about residents of the European Union (EU), whose General Data Protection Regulation (GDPR) grants those data subjects important control over their own data. Honoring those rights requires more accountability from service providers, and attention to data security and data residency. For providers subject to the GDPR, the architecture of Braintrust's platform matters as much as the feature set it offers.

Braintrust's platform was intentionally built to separate the **control plane** from the **data plane** at the level of architecture. This gives customers flexibility in how and where their AI data is stored, accessed, and governed, and makes it straightforward for teams in the EU to satisfy the security, privacy, and compliance needs of their broader organizations.

![Control plane and data plane architecture](https://www.braintrust.dev/blog/img/control-data-plane.png)


**Braintrust's control plane** manages the UI, metadata, authentication, and management functions of a customer's environment. It allows admins to control key access and management details like project settings, user identity, and feature flags. It lives in Braintrust's managed service and is delivered as SaaS.

**Braintrust's data plane** stores the actual AI data that customers use for their evals and observability, like experiment logs, traces, prompts, completions, and datasets. This is the sensitive information that compliance frameworks and legal regulations focus on, and what security and data protection teams need to safeguard.

Braintrust's architecture was built specifically to decouple these two layers. This ensures that customer data never has to transit or reside in infrastructure that admins didn't choose or don't control, while maintaining the benefits of SaaS product delivery.

Maintaining control over where data lives is crucial for EU teams. The GDPR requires that personal data about EU residents be processed in ways that respect strict residency and consent obligations. With Braintrust, you can choose to:

- Host your data plane entirely **within the European Union**, helping satisfy local residency requirements and simplifying GDPR compliance.
- Keep data in your own **customer-controlled environments**(e.g., your VPC), so you can apply your organization's encryption, access control, logging, and audit policies.

This flexibility enables teams to build their eval and observability architecture in accordance with compliance requirements from the start, rather than trying to retrofit controls after the fact.

This decoupling also supports data sovereignty, so teams across the EU can adhere to laws in their local jurisdictions. Braintrust's architecture lets EU customers approach their privacy and sovereignty needs in two ways:

- **SaaS customers**can select an EU region for their data plane, helping satisfy both regulatory requirements and internal risk policies.
- [Bring Your Own Cloud](https://www.braintrust.dev/docs/admin/index#self-host-braintrust)customers

Because the control plane remains a managed service, customers still benefit from the best parts of SaaS: instant updates and new features, a unified UI and authentication experience, and Braintrust-managed infrastructure for operational tasks.

At the same time, only the data plane handles interactions with the customer's AI systems, so sensitive data never needs to traverse or reside in Braintrust's managed hosting unless you choose otherwise. Customers get the speed and convenience of SaaS with the security and governance benefits of self-hosted infrastructure.

Organizations operating across multiple jurisdictions often face conflicting requirements about where data must reside. Braintrust's deployment options help satisfy these needs without sacrificing developer velocity.

Braintrust's separated planes and hosting choices make compliance with GDPR feasible. This also benefits any customer operating at global scale, customers who prefer data to be held locally, and organizations in regulated industries like finance and healthcare.

Decoupling the control plane from the data plane is a privacy-centric design choice built into the architecture of Braintrust's platform. It is designed to make the work of security and compliance teams easier, and for those in the EU, it has meaningful business value.

Braintrust customers working under GDPR regulations can align their data governance, residency requirements, and risk posture directly with the technical deployment of the platform.

Reach out to the Braintrust security team or explore the [Trust Center](https://trust.braintrust.dev/) for deployment guides and compliance resources.
