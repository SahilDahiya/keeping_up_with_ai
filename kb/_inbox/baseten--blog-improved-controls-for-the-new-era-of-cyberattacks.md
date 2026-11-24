---
title: Improved controls for the new era of cyberattacks
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/
author: Sameer Paranjpye; Kabir Sikand
published: '2026-11-20'
fetched: '2026-11-24T06:06:36Z'
classifier: null
taxonomy_rev: 2
words: 895
content_sha256: 8a4a892aa4a0d365a5338fff52befd7dc882b6564f18f502c2c859e566a122f4
---

# Improved controls for the new era of cyberattacks

Security
# Improved controls for the new era of cyberattacks

Cyber threats are increasing in volume, speed, and sophistication. This is our approach to staying ahead of them, alongside the controls we offer our customers.


- Authors
- Published

At some point in the last six months, the security world changed. Models got very good at finding exploits. Agents became relatively simple to set up. Swarms of agents are now a normal attack pattern. Critical vulnerabilities used to lie dormant deep inside widely used software libraries for years. Now, agent swarms try every door, exploit zero-day vulnerabilities, and exfiltrate data within minutes.

As the threat landscape evolves and grows more capable, we have evolved our defenses to match.

We’ve observed a drastic shift in the methodologies, attack patterns, threat vectors, and incentives of malicious actors in the cybersecurity space. AI assistance has enabled threat actors to deploy complex attacks at breakneck speed, and this is happening across every industry. Just this week, Google released its [Q4 AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold), with a headline takeaway being that threat actors are moving from AI-assisted attack patterns to fully autonomous AI-led attacks. Multi-agent frameworks and automated exploits of vulnerabilities alongside new monetization schemes (like [LLMJacking](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)) have changed the picture entirely. The field has reached an inflection point.

Alongside this, our customers and partners are shipping product updates at an increased pace. With more code shipping faster than ever, review processes are stretched, and more attack surfaces are being deployed at almost every organization. The combination has led to incident after incident across many technology and technology-adjacent industries. It’s keeping engineering and security teams up at night and on weekends.

The security standards that were good enough even a year ago no longer meet today's bar, because what used to require a nation-state-level adversary now only needs a capable model and an orchestration tool. In practice, that means:

- **Supply chains are at elevated risk.** Attackers target upstream vendors, software dependencies, and long-lived credentials to open doors.
- **Exfiltration takes minutes.** Once inside, sophisticated attackers can exfiltrate data in minutes with agent swarms that pivot through target networks.
- **LLM inference is now a prime target.** Attacks aim at model weights and GPU capacity, where a swarm can replicate and spread further. Not all compute arrives with the same level of hardening; newer GPU clouds have grown quickly, and their controls haven't had as much time to mature. For anyone building on top of them, that can create a bottom-up set of risks.

Securing against agent-speed attacks means we have to implement defenses at agent speed. At Baseten, we’ve found AI-assisted defense to be a force multiplier for monitoring, detection and response, and remediation across our software stack and supply chain. In addition to our other controls, this looks like:

- **Defense in depth.** We assume any single control can quickly fail, including the infrastructure beneath us, and we layer controls so a compromise in one place has little to reach. We run hardened containers and configurations, mutually authenticate request paths, and isolate and lower the context of customer workloads.
- **Detection and response in seconds.** Agents analyze activity across our network to flag malicious behavior faster and more accurately than static rules, and alerts trigger automated escalation designed to stop agent-based attacks.
- **Attacking ourselves.** Alongside third-party penetration testing, we run agentic red teaming against our own code with programs like OpenAI’s Daybreak Red. We find vulnerabilities sooner and patch them sooner.

Our customers ask us a simple question: how can I protect my sensitive data and workloads on Baseten?

- **Your identity system can stay in charge.** Employees are provisioned and sign in through your IdP and are assigned fine-grained roles mapped to your groups.
- **No need for long-lived secrets.** Workloads can reach your cloud with short-lived tokens, so there is no stored key to steal. Baseten API keys are scoped, expire, and can be revoked at any time.
- **You can hold the keys to your weights.** Served weights can be encrypted with keys in your own cloud KMS. You can revoke Baseten’s access to the keys at any time to disable decryption.
- **You can set the network boundaries.** Adjust ingress and egress allowlists to ensure only your infrastructure can reach your deployments. Additionally, single-tenant deployments can reach us over private connectivity.
- **Your data stays where you put it.** Inference runs only in regions you approve, and we maintain zero data retention for your inference data.
- **You can verify activity.** Audit logs are exportable to your own detection tools.

The landscape is always evolving, and the job won’t ever be done. We want to share our learnings and contribute to the conversation about emerging defense mechanisms and the new reality of agent-speed attack patterns. Over the coming weeks, you’ll hear more from us about the inner workings of our security programs and practices from across the Baseten engineering, infrastructure, and security organizations, including:

- What security at agent speed looks like
- API key hygiene
- Container and network security
- Identity and access management
- Observability, detection, and response

We hope this helps strengthen the security posture of our friends, customers, and partners across the industry. Stay tuned for more content on these subjects, and [reach out](https://www.baseten.co/talk-to-us/) if you’d like to discuss any of these topics in more depth with our engineers.
