---
title: How we achieved SOC 2 and HIPAA compliance as an early-stage company
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/how-we-achieved-soc-2-and-hipaa-compliance-as-an-early-stage-company
author: The Baseten Team
published: '2023-03-08'
fetched: '2026-11-12T06:13:10Z'
classifier: null
taxonomy_rev: 2
words: 695
content_sha256: 6214d56109dcdaa601b1537b5b3872b23490ee3f82c0ae471b2c44706dd931dd
---

# How we achieved SOC 2 and HIPAA compliance as an early-stage company

News
# How we achieved SOC 2 and HIPAA compliance as an early-stage company

Baseten is a SOC 2 Type II certified and HIPAA compliant platform for fine-tuning, deploying, and serving ML models, LLMs, and AI models.


- Authors
- Date
- March 8, 2023

In March of 2023, we announced that Baseten is [SOC 2 Type II certified](https://www.baseten.co/blog/soc-2-type-2/) and [HIPAA compliant](https://www.baseten.co/blog/baseten-announces-hipaa-compliance).

Pursuing compliance isn’t a trivial decision—there is an opportunity cost to dedicating limited engineering resources to compliance—but our existing security posture and development practices made becoming compliant a relatively seamless process. We prioritized compliance work so that our customers can rely on our platform to run mission critical models and process sensitive information.

We knew from the beginning that we’d need to make our platform compliant despite the constraints of being an early-stage company. Fortunately, there’s a big overlap between the groundwork for a productive engineering culture and a successful compliance effort.

We started with table stakes development practices from day one:

- **Code review** ensures all changes are approved by at least one other developer.
- **Automated testing** both locally and on merge catches bugs and regressions.
- **CI/CD** to deploy anytime, anywhere.
- **A staging environment** (or multiple) for testing more complex changes.

And used them to build good architecture:

- **Infrastructure as code** so that the benefits from our development practice extend down our stack.
- **Modular architecture** to make it feasible to replace any single component from our system if our needs change.
- **Observable operations** to make sure we know what’s actually going on in those servers and clusters.

Then added on solid security practices:

- **Store only the data we need** because if we don’t have it, we can’t lose it.
- **Don’t use Personally Identifying Information (PII) in multiple places**. Instead, we store it in a secure location and use anonymous identifiers elsewhere. Bonus: this makes deletion logic cleaner.
- **Alerts are our friend** as a strong system with no one monitoring it is like a castle wall with no guards. Our systems only remain compliant due to our continuous vigilance.
- **Controls and oversight** are necessary as we grow.

A SOC 2 Type II report requires a penetration test. Of course, we ask our pentesters to go over all the regular stuff: XSS, redirect issues, port scans, and so forth.

This standard coverage would be enough to get certified. But we wanted to take the opportunity to have outside experts test our system more comprehensively.

We directed our pentesters to expand their testing to act at the deepest possible level that a customer could act. For example, they tried to execute arbitrary code from a model deployed on our service. We know that we have these servers locked down and customer data isolated, but we wanted to make sure of it, so we went past the generic requirements and asked our pentesters to frame their attack from a deep understanding of the product and its attack surface.

Scalable compliance requires extensive documentation and tooling; this ensures:

1. That we know every detail required to be compliant, and
2. That we have a paper trail of everything we’ve historically done and are currently doing that we can share with our customers and auditors.

A tool that made the inevitable documentation work easier was Drata, a compliance automation platform. We used Drata to track our progress toward checking every box before the audit and for streamlining tasks like getting a signature from every employee on our process documentation.

Secure, compliant systems have always been a priority for us, so we’ve been investing in them since day 1. SOC 2 Type II and HIPAA are the start of our conversations about security, not the end.

When we use a service like S3 or EC2, we know that the data on those services is protected in a SOC 2 compliant manner. We rigorously engaged with the certification process to give you the same peace of mind running your workloads on our platform. When you use Baseten, you can communicate to your customers that their data is protected under both the letter and the spirit of SOC 2 and HIPAA.
