---
title: Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific
  Subdomains
topic: infra-platform
subtopic: deployment
secondary_topics:
- models/multimodal
summary: Architecture note on routing incoming voice traffic with customer-specific
  subdomains in a production voice platform.
source: cresta
url: https://cresta.com/blog/understanding-crestas-voice-platform-handling-incoming-traffic-with-customer-specific-subdomains
author: Florin Szilagyi
published: '2025-02-25'
fetched: '2026-07-11T04:03:07Z'
classifier: codex
taxonomy_rev: 1
words: 920
content_sha256: f7990a3b79559964de5aeea7636d65e841fada0fd23e179479472f1489688a76
---

# Understanding Cresta’s Voice Platform - Handling Incoming Traffic with Customer-Specific Subdomains

Cresta’s voice platform is a cutting-edge solution designed to provide real-time insights and actionable intelligence during customer interactions. It integrates with a wide variety of Contact Center as a Service (CCaaS) platforms, capturing and processing live audio streams to assist agents with timely guidance and recommendations. To shed light on this technology, we’ve divided our exploration into a three-part series, that will be published over the next couple weeks:

**Part One (this article): Handling Incoming Traffic with Customer-Specific Subdomains**

****In this first installment, we dive into how Cresta manages incoming traffic efficiently, including how customer-specific subdomains ensure scalability and isolation. We’ll explore the role of DNS, ingress controllers, and AWS Elastic Load Balancers in routing traffic to the right services.

**Part Two: Voice Stack**

****The second article will focus on how the platform processes live audio streams through its voice stack and how business logic layers power real-time guidance for agents. This part will highlight key components like speech recognition and how conversation data flows through the system.

**Part Three: ML Services, Inference Graphs, and Real-Time Intelligence**

****The final installment will take you deeper into the machine learning (ML) stack, exploring how inference graphs orchestrate model workflows, how customer-specific policies influence ML processing, and how Cresta delivers actionable insights in real-time.

### Glossary

Going forward, we want to clearly define some domain- or Cresta-specific terms

- **Customer profile**— this is a partitioning detail for the customer data, with an 1 to n relationship between customers and profiles (one customer can have multiple profiles), with each profile residing in an AWS region.
- **CCaaS**— Contact Center as a Service - a cloud-based solution that provides contact center functionality, such as call handling, customer support and communication management. Examples include Amazon Connect, 8x8, Five9, etc. Cresta currently supports- [over 20 CCaaS integrations](https://cresta.com/integrations/).

## Overview of Traffic Handling in Cresta’s Platform

Cresta’s voice platform needs to handle incoming traffic efficiently and route it to the appropriate services. Cresta employs a system to manage customer-specific subdomains, ensuring scalability and flexibility.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f556ab0f6dd6ca7089f_68135f594b351d4eb641ef81_image-6-1024x455.avif)

Each customer has their own unique subdomain, e.g.'customer1.us-west2.cresta.ai' that acts as an entry point. This isolates customer traffic, ensuring that the requests and resources are routed to their specific environments, without coupling the underlying compute infrastructure (EKS in our case) to the URLs, and without requiring a separate routing service to proxy requests from a generic domain, e.g. 'platform.cresta.ai', to the environment where the customer’s resources are located.This also helps provide transparency to the hosting region, for data sovereignty considerations, as customers may want data to not pass across regions. For examples, customers in the EU will want all their data held in EU data centers due to GDPR.Our services are hosted inside Kubernetes clusters (EKS), which means all traffic will eventually end up being served by one of our Kubernetes deployments. Handling traffic and routing to the correct services has a few moving parts:

- **DNS Resolution**: We use **AWS Route 53** as our DNS service for resolving domain names to the correct cluster’s load balancer.
- **ExternalDNS Controller:**Kubernetes controller that synchronizes exposed Kubernetes Ingresses hosts with DNS providers (Route 53 in our case). It creates or updates DNS records in Route 53 based on the spec.rules.host field in Ingress resources.
- **AWS Load Balancer Controller:**Kubernetes controller that provisions and manages **AWS Elastic Load Balancers (ELBs)**.
- **Ingress Controller:**The **NGINX Ingress Controller** manages and routes in-cluster traffic based on Ingress rules. Requests are routed to the appropriate service by matching rules like domain name or path.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f562ecf47a3a965024e_68135f594b351d4eb641ef84_image-7-1024x472.avif)

### Traffic flow

Whenever a new customer profile (a partitioning detail for a customer’s data, 1 customer can have n profiles) is registered, the profile has a specific subdomain that will be created in the ingress rules. In practice, our customer profile provisioning flow will create the new ingress rules using Flux-CD which will lead to DNS entries being provisioned.

- **DNS Entry Creation (ExternalDNS):**When an Ingress rule (like `api.us-west-2-staging.cresta.ai`) is registered, the external-dns controller creates a DNS entry in Route 53 pointing to the load balancer’s endpoint.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f562ecf47a3a965023e_68135f594b351d4eb641ef8d_VoicePlatform-blog1-1024x790.avif)

- **Load Balancer Provisioning (AWS Load Balancer Controller):**The AWS load balancer controller creates ELBs in AWS based on the LoadBalancer Kubernetes services. In our case, for handling external traffic there is an ELB associated with the NGINX LoadBalancer service.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f562ecf47a3a9650251_68135f594b351d4eb641ef87_VoicePlatform-blog1-2-1024x505.avif)

- **Routing Within the Cluster (Ingress Controller):**Once the ELB forwards the traffic to the Kubernetes cluster, the NGINX Ingress Controller evaluates the domain and path to route the traffic to the appropriate service. Cresta uses Wallarm, based on the Community NGINX Ingress Controller, which adds additional security features like real-time attack detection, API Security, detailed analytics, etc.- *Example of incoming reques*t:POST https://api.us-west-2-staging.cresta.ai/v1/customers/- *Ingress rule that matches the request and redirects it to the apiserver service inside the cluster:*

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f562ecf47a3a965024b_68135f594b351d4eb641ef8a_VoicePlatform-blog1-3-1024x590.avif)

We don’t want to get in too many of the nitty gritty details, but one important aspect that needs to be mentioned as part of the routing mechanism is handling long-running calls / audio streams. In case the connection to our servers gets severed, we need to be able to recover the connections and resume the calls.For the app installed on the agent’s desktop, since we control the audio paths so we have implemented recovery protocols. If the streaming connection is interrupted, these protocols can re-establish the connection and resume the stream from the point of disruption, ensuring minimal data loss.For CCaaS we rely on the external platform’s stream recovery mechanism.We will go deeper into the voice stack in part 2 of this article series. Stay tuned.
