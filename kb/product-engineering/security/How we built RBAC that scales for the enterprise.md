---
title: How we built RBAC that scales for the enterprise
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: Engineering writeup on building RBAC for enterprise AI infrastructure and
  balancing autonomy with control.
source: baseten
url: https://www.baseten.co/blog/rbac-from-the-ground-up-solving-for-autonomy-vs-control/
author: Matt Howard; Samiksha Pal; Rachel Rapp
published: '2026-04-23'
fetched: '2026-07-11T04:05:37Z'
classifier: codex
taxonomy_rev: 1
words: 1951
content_sha256: e76db35898dad21932e24348f1a004522b995c3c6f3bd256486f5d4a52873a17
triage: keep
skip_reason: null
---

# How we built RBAC that scales for the enterprise

![How Baseten built RBAC that scales for the enterprise](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1776885335-baseten-blog-2026-thumbnails-5.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

## RBAC from the ground up: Solving for autonomy vs. control

There are two things every organization needs from its inference platform, and they pull in opposite directions.

The first is individual autonomy: engineers and researchers need to deploy models, iterate on training jobs, and push changes to workloads without waiting on an admin or filing a ticket (in other words: speed matters). The second is access control: security teams need defined roles and audit trails, platform teams need the ability to take swift action during incidents, and IT needs to be able to provision and deprovision access predictably.

Lock everything down, and you've protected your production environment but created a bottleneck for every engineer trying to ship. Open everything up, and you have velocity but no governance. Aside from sacrificing one for the other, the shortcut is to take a high-autonomy solution and retrofit access controls. This is what most inference providers do, and we’ve heard the pain from customers who left them.

Instead, we built Baseten's permission model from the ground up: a single organization (previously called a “workspace”) containing multiple teams — each with isolated resources and access controls — while billing, user provisioning, and compliance remain unified at the top. Because scalable RBAC goes beyond permission models and teams, we also provide environment-level restrictions and granular API keys scoped to specific teams, environments, and models.

![Baseten's permission model, with the “organization” as the outer container holding unified billing and organization-member roles (Admin and Member), and two isolated team containers nested beneath it. Each team owns its own members, models, Chains, secrets, API keys, environments, and training projects.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1776886352-figure-1-3.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Baseten's permission model, with the “organization” as the outer container holding unified billing and organization-member roles (Admin and Member), and two isolated team containers nested beneath it. Each team owns its own members, models, Chains, secrets, API keys, environments, and training projects.

Baseten's permission model, with the “organization” as the outer container holding unified billing and organization-member roles (Admin and Member), and two isolated team containers nested beneath it. Each team owns its own members, models, Chains, secrets, API keys, environments, and training projects.The result is an RBAC system where a three-person startup and a 5000-person enterprise (and everything in between) can operate without friction, and where the controls necessary at enterprise scale don't come at the cost of the developer experience and velocity our users demand.

In the rest of this blog, we’ll explain the design choices we made to build RBAC that scales for the enterprise and what we learned along the way.

## RBAC day 0: Where companies start

You (should) build what your users need. When you're building an AI platform and your earliest users are individual developers and small teams, a flat, user-centric model is the obvious design choice. At that stage, everyone in an organization shares the same context, the same models, and the same level of access.

Our first permission model at Baseten reflected that:

![A flat permission model, with the organization at the top and members, billing, models, training projects, environments, API keys, and secrets all sitting at the same level.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1776886454-figure-2-2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) A flat permission model, with the organization at the top and members, billing, models, training projects, environments, API keys, and secrets all sitting at the same level.

A flat permission model, with the organization at the top and members, billing, models, training projects, environments, API keys, and secrets all sitting at the same level.And as a tree:

```
Organization
├── Members
├── Billing
├── Models
├── Training projects
├── Environments
├── API keys
└── Secrets
```
In this model, every resource lives under a single organization. Autonomy and velocity are prioritized: an engineer can deploy a model, call it, and share it with a teammate directly.

The model starts breaking when a company has multiple teams working independently. Senior engineers have the same permissions as their interns, and even the research team with experimental models can make changes directly to production.

As user bases grow, you need a permissions structure that accounts for complex, many-to-many relationships and can accommodate organizations of any size and structure.

## An aside on building holistic primitives à la Stewart Butterfield

Before getting into the technical design, we want to explain why we approached building RBAC the way we did (skip to the next section if you just want the structural details).

Before Slack launched, Stewart Butterfield wrote an internal memo making the case for why Slack would win. His argument was about organizational primitives, not features. Communication, context, and how work flows through a company needed to be first-class concepts in Slack.

We're selling a reduction in information overload, relief from stress, and a new ability to extract the enormous value of hitherto useless corporate archives. We're selling better organizations, better teams. That’s a good thing for people to buy and it is a much better thing for us to sell in the long run. We will be successful to the extent that we create better teams.

The same logic applies here: it would have been straightforward to ship RBAC feature-by-feature with model-level permissions, an environment lock, and a second type of API key. But the result would have been patchwork and would require custom configuration every time an organization changes shape.

(Believe it or not, most inference providers’ RBAC — if not nonexistent — is that patchwork. More on that below in “RBAC in the inference landscape”.)

We wanted to build an access control model where the answers to "who can modify production?" and "what happens when we spin up a new team?" fall naturally out of the system's structure. It takes longer to build, but it’s an investment that scales.

## The design decision: Where do groups go in the hierarchy?

When you add a grouping to a permission model, the first question seems simple: does it go above the organization, or below it?

Above would mean that a single company would have multiple organizations on Baseten, each with their own top-level settings, signup and login, and billing. You're essentially creating multiple independent organizations and giving users a way to switch between them.

This is faster to build, and some hyperscalers use this model. The disadvantage is that users end up with a fragmented experience: multiple logins, multiple API key contexts, and admins lose the ability to see what's happening across their teams from a single view.

Putting a “team” group below the organization means the organization stays supreme; users belong to the organization, and also to one or more teams within it. Billing, membership, and top-level oversight stay at the organization level. We chose this structure.

### The final team structure

```
Organization
├── Organization Members (Admin | Member)
├── Billing (org-level, unified)
└── Teams
    ├── Team Members (Team Admin | Team Member)
    ├── Models, Chains, Training Projects
    ├── Secrets (team-scoped)
    ├── Team API Keys (team-scoped)
    └── Environments (with optional restricted access)
```
In terms of user experience, this means when you log into Baseten you see everything in one place: all resources across the teams you have access to, one billing view, and one place to manage members. Organization admins get implicit access to all teams, and individual users can hold different roles in different teams.

## Restricted environments: RBAC at the environment level

Baseten users can create environments (like “staging” and “production”) on their models, which provide promotion and tracking across different source deployments while maintaining a consistent inference API endpoint. By default on Baseten, environments are unrestricted, meaning any organization member can modify deployments, autoscaling settings, and other configurations. But in building teams and rethinking our permission model, we discovered many customers wanted to lock down access to certain environments, like production, while allowing their users broad access to the model as a whole.

When you mark an environment as restricted, only users you explicitly grant access can make changes to it. Restrictions are team-scoped: when you restrict a production environment, it applies to every model and Chain within that environment and team. The restriction applies only to management operations, not to observability or serving. Users can still view metrics, read logs, and call inference endpoints.

## Granular API keys: Least-privilege for production

If the only API key you can give an external partner is one that can also redeploy your models, you have a problem. We built three distinct team API key types for granular access control:

- **Full access:**deploy models, call endpoints, and manage resources.
- **Inference only:**call model endpoints, nothing else.
- **Metrics only:**export metrics, no inference or management.

Beyond key type, team API keys can be scoped to specific environments and, within those environments, to specific models. This gives users flexibility and control over how their various systems may call and interact with their models. It also allows users to safely provide inference API access to their partners and their own customers.

![Two examples showing how API key scoping decisions can flow. Example A traces an inference-only key restricted to the production environment across all team models. Example B shows a full-access key spanning all environments but locked to a single specific model.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1776885511-figure-3-1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Two examples showing how API key scoping decisions can flow. Example A traces an inference-only key restricted to the production environment across all team models. Example B shows a full-access key spanning all environments but locked to a single specific model.

Two examples showing how API key scoping decisions can flow. Example A traces an inference-only key restricted to the production environment across all team models. Example B shows a full-access key spanning all environments but locked to a single specific model.## RBAC in the inference landscape

Autonomy and control come into tension whenever access management is an afterthought. Treat your permission model as a first-class product decision instead of a collection of feature requests from enterprise customers.

We won’t name names, but let’s just say we’ve done our homework and know how other inference providers approach RBAC. Often it’s barely existent; sometimes, it’s:

- **On a single, flat account level:**no sub-accounts, teams, or project-level isolation. Within an account, users get assigned roles; to assign these roles, you need to contact the providers’ support team. If two teams need to operate independently without seeing each other's workloads, the only option is separate accounts.
- **At the workspace level:**because team isolation is not within the workspace, three teams that need to operate independently means three workspaces, each with separate billing and member management (and no single-pane visibility).

Relying on separate accounts or workspaces as the isolation primitive fragments control. That's why we targeted the sweet spot of combining a unified organization with nested teams, environment-level restrictions, and model- and environment-scoped API keys.

## RBAC for every company stage

Our RBAC model is designed to be invisible when you don't need it and highly adaptable when you do.

**For early-stage companies or individual developers, **you're automatically placed in the default team: no added complexity of a team-specific UX. Use restricted environments and granular API keys only when you need to.

**For scaling organizations,** you can add teams as needed — like to isolate a production environment, onboard a new group, or separate experimentation from serving. 

**Enterprises** can leverage a full RBAC hierarchy, restricted environments, granular API keys, and centralized billing and audit visibility, all from a single workspace and a single view of what your organization is doing. 

Organizations of every size and complexity use the Baseten inference platform, and we’re proud to offer an RBAC model that fits their needs. If RBAC is important to your enterprise, or if you want to use an inference platform that will grow with you, [ reach out](https://www.baseten.co/talk-to-us/)!
