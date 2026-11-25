---
title: Deploy private Hugging Face models without sharing your access token
kind: blog
topic: product-engineering
subtopic: security
secondary_topics:
- infra-platform/deployment
summary: 'Baseten implemented read-only Hugging Face Trusted Publishers using OIDC:
  a 1-hour, single-repo, read-only token is issued at deploy time instead of a long-lived
  access token, removing standing credentials for pulling private model weights.'
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deploy-private-hugging-face-models-without-sharing-your-access-token/
author: Matt Howard; Yun Zou; Chloe Florit
published: '2026-11-24'
fetched: '2026-11-25T06:07:47Z'
classifier: claude
taxonomy_rev: 2
words: 718
content_sha256: 71db11d8845212bd0dc1fc38beabffa9c943729f5dd5cbe55e87ebf75a00539b
---

# Deploy private Hugging Face models without sharing your access token

Security
# Deploy private Hugging Face models without sharing your access token

Baseten partnered with Hugging Face to ship read-only Trusted Publishers, and is the first inference provider to pull private weights with short-lived tokens.


- Authors
- Published

Many teams store fine-tuned and proprietary model weights in private Hugging Face repos. Deploying those models on an external platform has usually meant handing over a long-lived access token that works until someone deletes it. Hugging Face Trusted Publishers improved on this by issuing short-lived tokens at deploy time, but until recently, those tokens could also write to your repo, which is more access than a deployment needs.

To maintain a high bar for security, we wanted to go further: no long-lived credentials anywhere, and no access beyond pulling the weights. We asked Hugging Face for a read-only option, and they shipped it within days. Trusted Publishers now supports read-only access, so inference providers get a 1-hour token that can only pull from a single repo and can't modify it.

We're proud to be the first inference provider to support read-only Trusted Publishers, joining our existing OIDC support for pulling weights from S3 and GCS. We'll keep working with partners across the industry to make workload identity and scoped access controls the default for AI infrastructure.

Before Trusted Publishers, the standard way to give a provider like Baseten access to a private model was a long-lived Hugging Face token. A long-lived token has three issues:

- **It never expires.** The token works until you delete it in Hugging Face. If it leaks, anyone who has it can download your private models until you notice and delete it.
- **It often has more access than it needs.** A classic read token can read every private repo you can access, including repos in your Hugging Face organizations.
- **It’s rarely rotated.** To swap in a new token, you need to create it in Hugging Face, update it in Baseten, and delete the old one. Because that takes coordination across two systems, teams often keep the same token.

Trusted Publishers solves these problems by replacing the stored token with short-lived tokens issued at deploy time. But before the read-only option was added, the relevant Trusted Publisher token could both read from and write to the private repository. This meant anyone with that token could modify the repository, even if they only needed to download the model weights.

With read-only access, Hugging Face issues a token at deploy time that can only read your repo and expires within an hour.

Read-only Trusted Publishers uses OpenID Connect (OIDC). When you deploy a model, Baseten creates a signed identity token that says which organization and team the deployment belongs to and what type of workload it is (for example, a model build, which downloads the model’s weights). Hugging Face checks the signature and compares the organization, team, and workload type to your Trusted Publisher settings. If they match, it issues the short-lived, read-only token. There’s no long-lived token that can be leaked or needs to be rotated.

To set up Hugging Face OIDC on Baseten:

1. **Get your Baseten IDs:** Find your organization and team IDs with the Baseten CLI. These tell Hugging Face which Baseten workloads to trust.
2. **Add Baseten as a read-only Trusted Publisher:** In your Hugging Face repo settings, add Baseten, scope it to your organization and team, and set it to Read-only.
3. **Point your Truss config at the repo:**

yaml

```yaml
weights:  
  - source: hf://acme/private-model@main
  mount_location: /models/private-model    
  auth:      
    auth_method: HF_OIDC      
    hf_oidc_resource: acme/private-model
```
For step-by-step instructions, including gated models and volume sync, see the [setup guide](https://docs.baseten.co/organization/oidc#authenticate-to-hugging-face).

Attackers have always gone after long-lived credentials and privileged access, but agent-driven attacks now move from a leaked key to stolen data in minutes. Read-only Trusted Publishers is one of many controls we've added to stay ahead of these threats. This post is part of our [security series](https://www.baseten.co/blog/category/security), where engineers across Baseten share how we protect customer models and data, from cluster hardening to identity and access management.

Stay tuned for another blog on API key hygiene in the coming weeks. Learn more about [our overall security stance](https://www.baseten.co/blog/improved-controls-for-the-new-era-of-cyberattacks/), and [how we secure the hardware we run on](https://www.baseten.co/blog/how-we-secure-100-clusters-across-20-clouds/).

If you want to dive deeper into any of these topics with our engineers, [reach out](https://www.baseten.co/talk-to-us/)!
