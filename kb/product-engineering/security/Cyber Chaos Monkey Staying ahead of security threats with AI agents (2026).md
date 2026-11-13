---
title: 'Cyber Chaos Monkey: Staying ahead of security threats with AI agents (2026)'
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- agents/multi-agent
summary: Details Shopify's Cyber Chaos Monkey, an agentic vulnerability-hunting system
  that runs live offensive engagements against production infrastructure via a Discovery/Sandbox
  pipeline, contained with per-engagement k8s jobs, a credential proxy, and egress
  allowlisting, plus a two-person-integrity design where a separately-aligned judge
  agent monitors the executor's full session and can kill it on policy violations.
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/cyber-chaos-monkey
author: Dan Scofield
published: '2026-11-12'
fetched: '2026-11-13T06:12:16Z'
classifier: claude
taxonomy_rev: 2
words: 1553
content_sha256: 34c50184a4eb8c59104f5d580fec0bae56ee1aedbf5f2fbbf25a2d07f52b0602
---

# Cyber Chaos Monkey: Staying ahead of security threats with AI agents (2026)

We're obsessed with protecting merchant and buyer data. We reinvent our security programs relentlessly, throwing away what doesn't keep pace with the evolving landscape and challenging ourselves to multiply both the depth and coverage of our capabilities with AI.

Earlier in 2026, [we described](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) our agentic approach to discovering and fixing vulnerabilities in our software. Since then, we've developed an agentic vulnerability hunter that runs live against our production infrastructure. We hand this system live credentials and every possible thing we know about the system (like bugs, infrastructure, and source), then steer it using the most capable cyber models available to find novel ways to bypass our safeguards.

So far, our agents have executed tens of thousands of offensive engagements, identified and acted on dozens of impactful findings, without causing an outage or incident. We call this system the Cyber Chaos Monkey (CCM), and here's how we built it.

## Finding vulnerabilities before attackers

Across the industry, we’ve seen an explosion in vulnerability reports as frontier models drive the cost of vulnerability discovery towards zero.

We see evidence of this in Shopify’s [bug bounty program](https://www.shopify.com/ca/bugbounty), which has seen almost a 300% increase in reports since 2024. Needing to review, validate, and act on this volume of reports makes the program much harder to operate.

Our hypothesis is that, although frontier models give our adversaries unprecedented capabilities, those models are a rising tide that lifts all boats. We believe that, since we have a massive informational advantage when it comes to our own software systems, we can harness that asymmetry along with frontier models to: (1) find many of the most impactful security issues in our system before anyone else; and (2) make it prohibitively expensive for adversaries to find any issues we miss. Attackers target our production systems, so our testing has to as well. We built CCM so that testing doesn't put availability or merchant data at risk.

## What is CCM?

Conceptually, CCM is a graph-engineered agentic bug-bounty researcher with access to source code, threat intelligence, past reports, and infrastructure/deployment records. Just like a bug-bounty researcher, CCM has the ability to call live Shopify production infrastructure using live test shops and organizations.

The name is an homage to [Chaos Monkey](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116), a tool Netflix introduced in 2011 to randomly shut down production instances, ensuring their services could survive real failures without customer impact as they moved to AWS. The practice has since grown into the discipline of chaos engineering, which focuses on experimenting on production systems to build confidence in their behavior under adverse conditions. Tobi regularly releases Chaos Monkeys across Shopify, like an annual deletion of recurring meetings from our team’s calendars.

With CCM, we are applying chaos engineering to security by deliberately attacking our own production systems to find weaknesses before they can impact our merchants and buyers.

Architecturally, we separate the system into two basic components: Discovery and Sandbox.

![CCM workflow: upstream ideas enter Discovery, which queries system knowledge, sends leads to Sandbox for testing, and uses results to generate further engagements.](https://cdn.shopify.com/s/files/1/0779/4361/files/ccm-diagram-1.png?v=1794411929)

Each CCM engagement is an investigation into a potential vulnerability or an attempt to achieve a specific security objective. That can start with an idea, hypothesis, or report originating from a human security engineer; other upstream security agents; or feedback loops within our Discovery tool itself. These can be specific (“find similar risks to a bug bounty report in other places”) or abstract (“achieve RCE on Shopify admin”), and they kick off six steps:

- **Step 1:** These ideas are sent as input to Discovery.
- **Step 2:** The latest cyber models are used to refine the idea, and identify places in the code or configuration that may lead to a vulnerability.
- **Step 3:** When Discovery identifies a promising lead, it sends structured data describing potential issues to the Sandbox where our agents try to exploit the bug.
- **Step 4:** Hands-on testing, like installing packages and building fuzzers. Unsurprisingly to any offensive security engineer, we have found that one of the most powerful primitives agents use in the Sandbox is making live requests to Shopify, reading our production logs to see how the request was processed, reconciling it against source code, and iterating.
- **Step 5:** When the Sandbox agents have completed testing, any findings are put into a report that is sent back to Discovery and upwards.
- **Step 6:** Discovery analyzes the results, and executes feedback loops that may generate further engagements.

## How do we keep CCM safe?

Recent incidents, where AI agents in security testing reached systems they were never meant to touch, show why containment has to be built in from the start. We have engineered a set of layered security controls that address both technical risks (e.g., leaking credentials, breaking out of the network) and fundamental risks to alignment (e.g., the agent not following our Rules of Engagement).

### Technical controls

CCM is a standard containerized workload and we use best-practice security controls throughout the architecture. Every CCM engagement has a corresponding k8s job. The Job pod has a handful of containers running, and the application controller is a state-machine-based orchestrator. Everything else is deferred to sidecar containers (like maintenance tasks and the offensive agent itself).

![CCM sandbox network: a pod in a Kubernetes node routes requests through credential and egress proxies to approved internet services.](https://cdn.shopify.com/s/files/1/0779/4361/files/ccm-diagram-2.png?v=1794411929)

- **Containerization and least privilege**: The offensive agent runs in a container with no escalated permissions. The only data seeded to the agent is a set of ephemeral Shopify credentials (e.g., a session cookie and CSRF token) that the orchestrator writes to a shared volume before the offensive agent starts. The agent can read these credentials but can’t modify them. The containers themselves are Debian-based and come pre-loaded with many development packages and security testing tools.
- **Credential proxy**: When calling our "knowledge" services or model providers, the agent passes a placeholder header in a request to a credential proxy. This replaces the placeholder with a real credential and sends the request via an egress proxy. There is strict control on which headers can be injected into which domains, and the credentials themselves rotate regularly.
- **Egress controls**: Our egress proxy is effectively an allowlist on top of nginx, and egress proxy pods are the only ones capable of exiting the VPC. We allow only Shopify production domains, our knowledge services, model providers, and a select set of package managers (e.g., our own package proxies).

### Managing alignment risks

We manage alignment risks in two ways. First, we supply a strict set of Rules of Engagement (RoE) to every agent. The rules leave the agent free to try any exploit against its target, and set hard limits on what it may do once an exploit works, such as moving to other systems or retaining access.

Second, we don't trust that the execution agent will maintain alignment throughout its task execution. Instead, we rely on two-person integrity (TPI), the idea that a second party must review the work of the acting party to confirm it does not pose a security risk. TPI is commonly used to protect the most sensitive information in governments, and to conduct the most risky red team operations. For CCM, our novel twist on TPI is to use a second agent that is differently prompted and aligned than the agent executing the engagement.

In practice, we do this by feeding the session logs from our offensive agent into a separately aligned agent (i.e., using a different model) in real time. If that agent identifies risky behavior that's incompatible with the RoE, the second agent makes a tool call that instantly kills the offensive agent. The "judge" agent reads all events from the "executor" session, including responses, thinking, tool calls, and tool call results.

![CCM positive control loop: the orchestrator starts executor and judge agents, monitors them, and terminates the run when the judge flags a breach, is lost, or the executor finishes.](https://cdn.shopify.com/s/files/1/0779/4361/files/ccm-diagram-3.png?v=1794411929)

We’ve designed our system to require explicit positive control as diagrammed above: if the "judge" times out, crashes, or fails to adjudicate messages from the "executor," the run ends. The orchestrator that implements this TPI is the pod’s main application container, with the "executor" and "judge" running as native sidecar containers within the same pod. The orchestrator maintains a heartbeat signal with both “executor” and “judge.” If either dies, the orchestrator container will exit. The pod's restart policy prevents the orchestrator from restarting, so k8s tears down both sidecars and the job terminates.

Keeping everything pod-local (but isolated) reduces the risk of network partitions disrupting the communication between the “orchestrator,” “executor,” and “judge.” Similarly, an eviction triggered by k8s will terminate every container in the pod, so evictions can’t leave “execution” containers running without their paired “judge” and TPI is never at risk.

## Putting our advantage to work

CCM is a bet on asymmetry. Frontier models lower the cost of finding vulnerabilities for everyone, but we know our own systems better than any outside attacker ever will.

Using the same class of models with that informational advantage lets us reach the most impactful issues first. It simultaneously drives up the cost for external parties to achieve the same result, by forcing attackers to compete with agents that work around the clock and start with the full picture.
