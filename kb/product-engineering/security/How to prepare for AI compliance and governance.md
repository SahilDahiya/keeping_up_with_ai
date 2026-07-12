---
title: How to prepare for AI compliance and governance
topic: product-engineering
subtopic: security
secondary_topics:
- evals-observability/monitoring
summary: Connects AI compliance and governance to engineering controls such as observability,
  audit trails, data boundaries, review workflows, and policy enforcement.
source: braintrust
url: https://www.braintrust.dev/blog/ai-compliance-governance
author: Braintrust Team
published: '2026-04-13'
fetched: '2026-07-11T04:31:14Z'
classifier: codex
taxonomy_rev: 1
words: 967
content_sha256: 7eaa5aa46c51e8367bb36c4ccb635f9b2fc98171121436e6c7312fa7675e1eaf
---

# How to prepare for AI compliance and governance

13 April 2026Ross Stapleton-Gray6 min

As AI moves from experimentation to infrastructure, compliance and governance expectations are catching up fast. Most organizations are aware of their need to comply with regulations such as the GDPR, or, for those in more closely regulated sectors, HIPAA and other sector-specific rules. The same approach is only recently being applied to AI, but adoption has been rapid and teams need to prepare.

The most important steps in this direction are the [EU AI Act](https://artificialintelligenceact.eu/ai-act-explorer/) and [ISO/IEC 42001](https://cloudsecurityalliance.org/blog/2026/03/18/understanding-iso-42001-responsible-ai-governance-in-an-evolving-regulatory-landscape). The first is a legal and regulatory framework for companies building with AI. The second is an international compliance standard for governing the AI lifecycle.

Both are imposing new stresses on security and compliance teams. But AI observability can help your organization adhere to and manage these regulations.

The EU AI Act, which entered into force in 2024, is the world's first comprehensive AI regulation. Similar to the GDPR, it applies to any organization that deploys or sells AI into the EU, regardless of where it's headquartered.

The law introduces a risk-based framework, with the strictest obligations placed on systems labeled as having "high-risk" (meaning AI products that impact critical infrastructure, education, and law enforcement) and systems deemed to have "unacceptable risk" (meaning malicious AI designed to harm human safety). Most companies will fall under the "minimal risk" or "limited risk" categories, though the law applies conditions to all risk levels.

Compliance is not simple. Regulators expect transaction-level audit evidence and system logs showing who did what, when, and why. Failure to produce this evidence can mean fines, loss of market access, or both.

Given the law's novelty and its requirements, many organizations are still working to implement the observability platforms that can produce the evidence necessary to demonstrate compliance.

ISO/IEC 42001, published in 2023, is the first international compliance standard for AI management systems. It provides a structured framework for governing AI across its lifecycle, covering risk management, transparency, monitoring, and continual improvement.

Compliance with ISO 42001 is voluntary, like other existing ISO standards. But it's quickly becoming a global benchmark for AI governance. Organizations are now finding that the framework is a prerequisite in procurement and enterprise partnerships, and a useful way to demonstrate auditable, repeatable AI controls to customers, partners, and others.

Estimates suggest that ISO 42001 can cover up to 70-80% of EU AI Act requirements, so the foundational work does not need to be duplicated.

The EU AI Act and ISO 42001 are also similar in that both require organizations to demonstrate that these controls are working in reality with substantive proof supported by production data.

This is different from traditional governance approaches which rely on static documentation, periodic audits, manual reporting, and fragmented logs. Because AI systems are constantly changing, and because the reasoning behind their actions is often opaque, these new frameworks expect more than the usual compliance theater. Teams now need to produce logs, traces, and model performance data that can be treated as evidence of how their AI products are operating, and which can stand up to the scrutiny of a thorough audit.

AI observability is the capability to continuously monitor, log, trace, and explain AI system behavior in production. It's the operational structure that allows teams to understand and improve their AI products, and it also gives them the tools to produce evidence on how their AI products are performing. This evidence is critical to compliance with both the EU AI Act and ISO 42001.

The EU AI Act explicitly requires automatic logging that enables traceability of system behavior. AI observability platforms like Braintrust include the real-time event logging, model input/output tracking, and decision lineage reconstruction needed to satisfy this requirement.

The regulation is essentially asking a series of questions about AI product performance: Why did this model make this decision? What changed between last month and today? Logging and tracing captures the evidence necessary to answer those questions.

Both the EU AI Act and ISO 42001 require ongoing risk assessment, rather than older models of pre-scheduled moment-in-time review. Because models change and AI regresses, the security threats are ever present and require constant monitoring.

With AI observability, teams can detect when models drift, identify when bias emerges in model outputs, and monitor performance degradation over time.

These new laws and frameworks require real-time, verifiable evidence that can withstand expert audits, instead of after-the-fact reporting.

AI observability creates logs, time-stamped decision records, and system-wide audit trails. This is the kind of evidence that can pass an audit of AI system performance.

ISO 42001 is following the same trajectory as earlier standards like ISO 27001. Initially ISO 27001 was voluntary, and taken on by teams as an exercise in security hygiene. As its popularity grew, enterprise buyers with the highest security standards began demanding it. Now it's simply a baseline expectation for customers and partners of all sizes and industries.

The same process has started for ISO 42001. Procurement pressure is growing as buyers increasingly require proof of AI governance maturity. Its similarities with the EU AI Act mean it has value beyond customer demand. Its global applicability gives it credibility outside the EU regulatory regime. And its focus on auditability can serve as external validation of internal controls for a variety of audiences.

AI governance is entering a new phase. The EU AI Act enforces legal accountability for any company with EU customers or operations. ISO 42001 is quickly becoming another industry standard that security teams need to implement. And AI itself is developing at such a rapid pace that any team not focusing on security and compliance is at risk of falling behind.

Those who invest early in AI observability will shorten time to compliance, reduce audit risk, build trust with regulators and customers, and gain a defensible advantage in competitive AI-driven markets.
