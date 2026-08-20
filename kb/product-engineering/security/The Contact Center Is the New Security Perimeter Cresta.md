---
title: The Contact Center Is the New Security Perimeter | Cresta
kind: blog
topic: product-engineering
subtopic: security
secondary_topics: []
summary: 'Documents contact centers and helpdesks as a live attack surface with named
  incidents: Coinbase''s 2024/25 bribery of overseas support agents affecting 69,461
  customers, RAC staff convicted over 29,500 crash records, and Octo Tempest/Scattered
  Spider systematically vishing helpdesks for MFA resets. Cites Verizon''s 2025 DBIR
  finding third-party involvement in breaches doubled from 15% to 30%.'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/the-new-perimeter-is-your-contact-center-why-observability-now-belongs-in-your-tech-stack
author: Robert Kugler
published: '2025-10-23'
fetched: '2026-08-20T06:15:16Z'
classifier: claude
taxonomy_rev: 2
words: 815
content_sha256: 97eccb3f46694bd7a0b845b82637a7c704b3c024cb9ddea0d02761fbba4119cb
---

# The Contact Center Is the New Security Perimeter | Cresta

Over the last two years, attackers have zeroed in on contact centers and helpdesks because one well‑timed conversation or one compromised agent account can sidestep hardened perimeter controls.

Coinbase’s 2024/25 incident is the clearest example: criminals bribed overseas support agents to siphon sensitive customer data later used in social‑engineering scams. [Coinbase rejected a $20M ransom](https://www.coinbase.com/en-de/blog/protecting-our-customers-standing-up-to-extortionists), but the downstream harm touched 69,461 customers, per the company’s [state AG filing](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/f61fae18-f669-499e-9a87-f4d323d281f8.html).

And this is not an isolated case. In the UK, [two RAC call‑center specialists were convicted](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/10/criminal-record-and-suspended-prison-sentence-handed-to-former-rac-employees/) for copying and selling 29,500+ crash‑victim records. In the U.S., [prosecutors described a Louisiana ring](https://www.justice.gov/usao-wdla/pr/ringleader-bank-fraud-conspiracy-case-receives-lengthy-federal-prison-sentence) that recruited Teleperformance call‑center insiders serving USAA Bank, then printed counterfeit checks leading to federal sentences in 2025. And in India this past August, [Delhi Police alleged “insider moles”](https://timesofindia.indiatimes.com/city/delhi/2-6cr-credit-card-fraud-gang-busted-18-nabbed/articleshow/123337639.cms) at an authorized CPP call center leaked SBI credit‑card data that fueled a ₹2.6 crore fraud; 18 arrests have since followed (the case is ongoing).

Security teams have seen this movie before. [Microsoft’s deep dive on Octo Tempest](https://www.microsoft.com/en-us/security/blog/2025/07/16/protecting-customers-from-octo-tempest-attacks-across-multiple-industries/) (aka Scattered Spider) documents systematic helpdesk targeting: impersonation, vishing, MFA resets, and remote‑assist tools to obtain initial access. In 2023, the MGM/Caesars incidents showed just how quickly a [“service desk” pretext](https://unit42.paloaltonetworks.com/threat-group-assessment-muddled-libra-2024/) can escalate into enterprise‑scale disruption.

Zoom out and the macro data says third‑party pathways are rising: [Verizon’s 2025 DBIR](https://www.verizon.com/business/resources/infographics/2025-dbir-smb-snapshot.pdf) analyzed 12,195 confirmed breaches and highlights that the share of breaches involving a third party doubled, from 15% to 30% year over year. That’s exactly where many contact centers sit: outsourced, distributed, and permissioned.

## **Why attackers love contact centers**

- **High leverage, high pressure:** Agents and team leads can view and change customer data under strict time‑to‑resolution goals. Criminals either social‑engineer them (convince an agent to “help”) or recruit/bribe them.
- **Fragmented oversight:** Voice, chat, email, CRM, and knowledge live across systems that rarely share real‑time telemetry with security. Gaps = gray space for exfiltration.
- **Vendor surface area:** BPOs and contractors add distance between SecOps and day‑to‑day agent actions - exactly the “third‑party” dynamic DBIR calls out.

## **What “observability” means in a contact center (and why it reduces risk)**

In engineering, observability means seeing internal state from external signals. In contact centers, it means instrumenting every conversation and workflow so you can *detect and act* on risky behavior in real time:

1. **End‑to‑end conversation intelligence** (voice, chat and email) with searchable transcripts and signals (PII exposure, payment handling, escalations). This moves QA from tiny samples to broad coverage and gives security a reliable trail.
2. **Real‑time agent assistance and guardrails** that push the right next step and block the wrong one (e.g., no sensitive verification bypass scripts; no off‑policy refunds or address changes).
3. **Behavioral baselining** : which agents repeatedly access high‑value records off‑queue? Which teams copy unusual amounts of data after hours? Turning patterns into alerts is how you spot bribery, coercion, or account sharing early. This is exactly the gap exploited in the Coinbase and USAA patterns.
4. **Unified telemetry** across telephony, chat, CRM, and knowledge systems so SecOps can correlate “who said what” with “what changed in the account.”

## **Where Cresta fits**

Cresta isn’t a Security Information and Event Management (SIEM) or data loss prevention (DLP) tool, but our real‑time guidance, conversation intelligence, and QA automation substantially increase observability in the exact workflows attackers are abusing:

- [Agent Assist](https://cresta.com/agent-assist) provides in‑the‑moment guidance, knowledge retrieval, AI summaries, and workflow automations. These controls help standardize how sensitive data is handled and reduce risky improvisation.
- [Behavioral QM](https://cresta.com/cresta-quality-management) and performance insights on compliance behaviors give leaders a unified view of what’s happening across conversations, making it easier to spot anomalous behaviors, compliance drift, and training gaps at scale.
- Cresta across channels ([now including email](https://cresta.com/blog/email-is-in-the-loop-cresta-expands-agent-assist-and-conversation-intelligence-across-every-major-channel) ) extends the same real‑time insight and QA to a channel that’s historically under-leveraged in many centers. That’s critical because many high‑risk account changes and phishing pivots flow through email threads.
- [Opera](https://cresta.com/opera) helps security and risk teams surface potential fraud signals and risky behaviors within conversations, enabling agent-driven investigations and workflows to mitigate fraud and account compromise.
- [Screen recording](https://cresta.com/blog/closing-last-mile-quality-management-gaps-the-role-of-screen-recording-in-contact-centers) speeds up incident response processes and ensures agents and businesses remain compliant with laws and regulations.
- [AI Analyst](https://cresta.com/cresta-ai-analyst) enables analysts and business users to discover and investigate emerging threats within conversational data.

Adding Cresta’s “in-the-conversation” visibility and guardrails to your security stack shrinks the gray space where social‑engineering and insider abuse thrive.

## **The takeaway**

Attackers go where decisions get made fast and verification gets messy–which is exactly what contact centers are built for. You can’t reduce exposure with policy documents alone.

You need observability inside the conversation and the workflow, coupled with real‑time guardrails that help agents do the right thing under pressure. Platforms like Cresta provide that layer unifying signals across channels, guiding agents in the moment, scaling QA, and enforcing responsible handling of sensitive data, so the next attempted scam has fewer places to hide.
