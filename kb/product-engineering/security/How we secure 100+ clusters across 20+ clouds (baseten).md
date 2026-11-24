---
title: How we secure 100+ clusters across 20+ clouds
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/gpu-clusters
summary: Explains how Baseten hardens 100+ GPU clusters across 20+ clouds (including
  less-uniform neoclouds with public addresses/open ports) to a consistent security
  baseline, with a checklist for evaluating a provider's security posture.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-secure-100-clusters-across-20-clouds/
author: Stephen Day; Hao Wu
published: '2026-11-20'
fetched: '2026-11-24T06:06:32Z'
classifier: claude
taxonomy_rev: 2
words: 1890
content_sha256: 81381d9c87c72895d7eaccf3d6b32edf6125560f8af9d93f4fc7873317c6aec1
---

# How we secure 100+ clusters across 20+ clouds

Security
# How we secure 100+ clusters across 20+ clouds

We design clusters to be secure by default and apply controls that hold every cluster we run on to that design.


- Authors
- Last updated
- Originally published

TLDR

Because we treat compute as fungible across many GPU providers, we have to take steps to ensure our security standard holds on every cluster we run on. This post covers how we do it, including a checklist at the end you can apply to your own fleet, or when evaluating a provider’s security standards.

Running inference for other companies requires a high bar of trust, and we have to continuously earn that trust when it comes to serving our customers’ models, processing their data, and offering the products they build on both. We're proud to partner with teams like Cognition, Coinbase, Cursor, Datadog, HubSpot, Ramp, and many more, and we put controls in place to protect their models and data wherever they run.

This post covers how we hold our security standard across our entire fleet—20+ clouds and 100+ clusters—including over a dozen neoclouds that help us unlock global scale (and run workloads active-active) to reliably meet any level of customer demand. For an introduction to this security series and a look at how we’ve adapted our defenses to agent-speed attacks, read our overview blog [here](https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/).

[Multi-cloud Capacity Management (MCM)](https://docs.baseten.co/concepts/howbasetenworks#multi-cloud-capacity-management-mcm) allows us to treat GPUs as completely fungible, regardless of the cluster or cloud provider they’re sourced from—hyperscalers and neoclouds alike.

When you work with hyperscalers like AWS or GCP, they hand over managed clusters with years of hardened defaults. Neoclouds are often less hardened (and less uniform): some lease bare machines, some run Kubernetes for you, and some work through a partner that operates the control plane. Often, they have public addresses and open ports.

Because we can run workloads on any of 20+ providers, every cluster must be evaluated so we can add necessary controls on top wherever needed. For neoclouds in particular, this often means building our security posture on top of them, so every cluster is hardened before it serves traffic.

To bring the same controls to every cluster, we start from a threat model with four trust boundaries: the infrastructure layer, operating partners, workloads, and internal access.

| Boundary | What it separates | What we defend against | 
|---|---|---|
| The infrastructure layer | Our platform from a provider's hardware, network, and defaults | A compromised provider, or a cluster that arrives exposed | 
| Operating partners | Baseten from any third party that operates a layer of the stack | A compromised partner, or stolen partner credentials | 
| Workloads | One customer's code from other tenants and from the node | Malicious or compromised customer code, or a compromised image | 
| Internal access | Our engineers from production clusters | Misused or stolen engineer access | 

The infrastructure layer is the foundational trust boundary and follows the cluster lifecycle. We control a cluster’s exposure from handover through operation to decommission.

At handover, we close every public port except the ones that serve traffic. We put the Kubernetes API behind an allowlist, and we set SSH to key-only access with regularly rotated keys. SSH access is provided on-demand with multi-factor authentication (MFA) and no long-lived credentials. A baseline scan then checks the cluster before it joins the fleet.

In operation, traffic to and from each cluster moves through secure channels so a cluster accepts traffic only from trusted Baseten infrastructure. Node joins are protected and designed so a machine can't add itself to a cluster. Hosts and Kubernetes are patched on a set cadence.

At decommission, we wipe customer data before the machines go back to a provider.

Some layers of the stack are operated by someone else: a provider runs the hardware and its console, and on some clusters a partner runs the Kubernetes control plane.

Anyone who operates a layer gets the least access that the layer needs. Partners notify us of control plane changes, so cluster changes don't arrive unannounced, and provider consoles require hardware-bound MFA.

Because we treat all end-user code as untrusted, we isolate it at build, at runtime, on the network, and from other customers’ secrets.

To enforce workload isolation, we take the following steps:

- **Customer builds run in microVMs:** Each build runs arbitrary customer code with broad permissions, so each one gets its own kernel.
- **Every image comes through our build platform:** Customer and platform images live in separate registries, so the two stay separate.
- **Tenants are isolated on the network:** Network policy separates tenants, and cross-cluster traffic uses mTLS for authentication and encryption in transit.
- **RDMA goes through a node agent:** Direct memory transfers between nodes pass through an agent that authorizes each one.
- **Customer secrets are encrypted in our control plane:** They’re segregated by organization, never baked into images or code, and reach only that customer’s own deployments.
- **Runtime detection runs on every node:** It watches for breakout attempts, including through the GPU runtime.

The last boundary is the one around us (or anyone managing a fleet). Access is restricted, fully logged, monitored, and audited. Those logs also leave the cluster, so someone with access to a cluster can't erase the record of how they used it.

We assume any of these boundaries can fail, so we scope credentials to one cluster at most. Even a fully compromised cluster holds no credential that reaches another cluster or the control plane beyond a limited scope. Within a cluster, network policy and node boundaries keep a compromised workload or node from reaching the rest of the cluster.

We also plan for the worst case: an attacker who controls a whole cluster. In that case, it’s imperative that the damage is contained to that cluster; to do so, we scope keys by least privilege:

- **Deploy keys are per cluster max, and read-only:** The key a cluster uses to pull its configuration can't change what any cluster runs.
- **Each cluster has its own certificate authority:** A token signed in one cluster is not valid in another.
- **Distribution credentials rotate within an hour:** Rotation restricts how long a stolen credential can be misused.

We avoid any credential, key, or trust root that spans the fleet. We limit each credential to the smallest scope we can, and at most to one cluster. With strict permissions in place, even someone who takes over a cluster should hold no credential that opens another cluster or the control plane. Any credential that reaches from a cluster to the control plane or to another cluster is limited to the smallest scope it needs.

These four boundaries cover who can reach a cluster, but clusters also need to be secured against every possible input: configs, images, weights, and software.

To secure the entire supply chain, each input has a control of its own:

- **Cluster configuration:** Each cluster pulls its configuration with its own read-only deploy key, so a compromised cluster can't change what any cluster runs.
- **Images:** Every image comes through our build platform, and customer images and platform images stay in separate registries.
- **Model weights:** Weights arrive over our data distribution path. The path has full audit logs, and we flag actions that don’t match any expected data flow.
- **Host software:** Hosts and Kubernetes are patched to deal with known and potential risks.

We verify controls from inside and outside each cluster to check that standards hold and don’t drift.

From the inside, Kubernetes audit, host, DNS, and SSH logs from every cluster flow to one system for monitoring, with alerts that page an on-call responder. The data distribution path is fully audit-logged, and we flag actions that don’t match an expected data flow.

From the outside, a daily scan checks every cluster’s external perimeter, and we regularly verify each provider’s security posture.

Together, these checks mean a workload gets the same protections on any cluster where MCM can place it.

Use this checklist to audit your own fleet or to evaluate an infrastructure provider. Each item should be true for every cluster.

- **Fleet-wide credentials:** No credential, key, or trust root spans more than one cluster. Ideally, credentials are least privileged.
- **Deploy keys:** Each cluster pulls its configuration with its own read-only key.
- **Certificate authority:** Each cluster has its own CA.
- **Credential rotation:** Data distribution credentials rotate within an hour.

- **Public ports:** Every public port is closed except those serving traffic.
- **Kubernetes API:** The API is behind an allowlist.
- **SSH:** Access is key-only, and keys rotate.
- **Baseline scan:** A scan passes before the cluster joins the fleet.
- **Traffic path:** Traffic to and from each cluster moves through secure channels.
- **Node joins:** Joins are protected, so a machine can't add itself to a cluster.
- **Patching:** Hosts and Kubernetes are patched on a set cadence.
- **Decommission:** Customer data is wiped before machines go back to the provider.

- **Least access:** Each partner has only the access its layer needs.
- **Change notice:** Partners notify you before control plane changes.
- **MFA:** Every provider console requires it.
- **Vendor credentials:** Credentials for outside vendors are per cluster and write-only.

- **Builds:** Customer builds run in microVMs.
- **Image source:** Every image comes from your build platform.
- **Registries:** Customer and platform images live in separate registries.
- **Model weights:** Weights arrive over an audited distribution path.
- **GPU isolation:** GPU workloads run with hardened isolation.
- **Tenant networking:** Tenants are isolated on the network.
- **Cross-cluster traffic:** Traffic between clusters is mutually authenticated.
- **RDMA:** Transfers go through an agent you control that authorizes each one.
- **Secret storage:** Secrets live in an encrypted store you control, never in images or code.
- **Secret delivery:** Secrets reach only the workloads that need them.
- **Runtime detection:** Detection runs on every node, including for breakouts through the GPU runtime.

- **Standing access:** Ideally, no one has standing administrative access to production clusters.
- **Access logs:** Every access path is logged, and logs are shipped off the cluster.

- **Centralized logs:** Kubernetes audit, host, DNS, and SSH logs from every cluster flow to one system, with alerts that page an on-call responder.
- **Data flows:** Flows that don't match an expected pattern are flagged.
- **Perimeter scans:** Every cluster's external perimeter is scanned at a regular cadence.
- **Provider verification:** Each provider’s security posture is verified.

- **Ownership:** Every finding has an owner and a deadline.
- **Closing gaps:** Gaps are tracked to closure with a feature, control, or process change.
- **Provider accountability:** Gaps on a provider’s side are raised with them and followed up until fixed.

While securing 20+ clouds takes dozens of security practices, much more goes into keeping inference, training, and sandboxes secure for all of our customers across our entire platform.

This is the first in a series of blogs that will go deeper into how we do that—stay tuned for more coming each week in the [security section of our blog](https://www.baseten.co/blog/category/security). If you want to learn more about our general approach to security, you can [read this blog](https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/). And if you want to go deeper into any of our controls with one of our engineers, [reach out](https://www.baseten.co/talk-to-us/).
