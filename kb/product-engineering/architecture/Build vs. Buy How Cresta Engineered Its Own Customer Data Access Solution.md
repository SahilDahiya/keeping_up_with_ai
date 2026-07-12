---
title: 'Build vs. Buy: How Cresta Engineered Its Own Customer Data Access Solution'
topic: product-engineering
subtopic: architecture
secondary_topics:
- infra-platform/deployment
summary: Engineering case study on building a customer data access layer, useful for
  understanding integration tradeoffs in enterprise AI products.
source: cresta
url: https://cresta.com/blog/build-vs-buy-how-cresta-engineered-its-own-customer-data-access-solution
author: Sergey Kruk
published: '2025-03-20'
fetched: '2026-07-11T03:55:27Z'
classifier: codex
taxonomy_rev: 1
words: 880
content_sha256: 20e9ee9137fdec31bd811a6159d61082042d2133281c41ef741d38d6f0884d9b
---

# Build vs. Buy: How Cresta Engineered Its Own Customer Data Access Solution

There is that moment in life of every startup when it’s no longer three people in someone’s garage. Early on everyone wears multiple hats and if the scope is small, having access to everything is fine. But as the company matures, scalable and auditable data access processes are required to provide customers with the assurance their data is protected.Access provisioning is a big topic on its own and there are a lot of providers. But since they all try to make a living out of it, there is only so much customization one can hope for. After having a nasty experience with one of the providers who tremendously overpromised and drastically underdelivered we made a decision to build a provisioning solution for access to customer data ourselves — within the security team.

## Why 'Build' Won Over 'Buy' at Cresta

The question 'build vs. buy' is very popular in the SaaS world, but I believe it is only ever posed for real to engineering. Other departments tend to lean towards the «buy» answer a lot. Not the case for Cresta security. As we proudly advertise that our team consists of engineers, we always consider the 'build' option very seriously.The goal of the solution is to be able to answer at any given moment who of the employees has access to which customer data and why. Our engineering already allowed us to leverage the identity provider we use, so what remains is:

- Make it more granular and transparent
- Leave a paper trail in our SIEM
- Account for edge cases, such as on call and customer-facing roles

First, we needed to teach our production and our SSO provider to work together in determining whether an employee has access to a given customer data or not. This integration is detached from the process of requesting and granting access. The persisted state of access is stored in the SSO provider. This allowed us to not introduce additional software in the way of a user, once the access request is processed and granted.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f2953741fbd2b41a413_68135f5a5bb0f0f1923a9dc3_CustomerDataAccess-1.avif)

For managing approval flow we decided to use the application, where Cresta employees spend a significant amount of time already — corporate messaging platform. Yes, we created a chat bot. The flow could then become as complicated or as simple as our policies require that to be:

- All actions are recorded and forwarded to SIEM
- Line manager and security team are defined in our SSO provider, so we know the pool of approvers
- We can allow escalation to happen in urgent situations
- We can account for the pool of employees being on call
- We can account for the employees assigned to the accounts in a CRM

## Build vs. Buy: The Pros and Cons of Our Custom Solution

There are definitely pros and cons to our solution.

#### Pros of Building Our Own Access Solution

- **Compliance as code.**Not in the usual sense, where one writes a script to see if something violated a policy. In our case code is the policy. It’s not enough to write a document and have everyone acknowledge they read it and hope they will follow it. In our case the policy is engineered as software.
- **Flexibility.**We can always find a solution to unblock people in what they do. It will never be as flexible as 'everyone is the admin', but it can be pretty swift while staying compliant and justifiable for an audit.
- **Financial advantage.**Provided we can manage the scope, almost always an in-house solution comes out cheaper.
- **Eat your own dog food.**As it is a service, we go through the same process any software solution at Cresta would go through. We went through design reviews and developed everything according to our change management policies. Which allows us to test how security influences engineering flow.

#### Cons of Building Instead of Buying

- **Friction.**Yes, we are building a solution that no one asked for. Maybe not everyone even knew there was a problem that needed to be solved. People tend to be more tolerant if it’s a bought solution. Even if it’s very expensive and not very convenient, the barrier to write a support ticket or to join an external office hours meeting is high enough that users find a way to live with whatever problem they have.Having someone reachable inside definitely lowers the tolerance to inconveniences. I personally have nothing against healthy friction. Different departments exist for a reason and they protect their goals. But it’s something to pay attention to, if you decide to build anything inside.
- **Maintenance.**This is in a way a consequence of the point above. There is a high risk of the scope creep. Then it levels out the expected financial advantage and possibly the transparency of the policies. If there are a lot of special cases and exceptions, the policy becomes as full of bugs as the code. Even if you manage to keep your scope intact, this product stays for you to maintain.

Overall our experience with building and using this custom tool is positive so far. We do enjoy solving security and compliance problems with an engineering solution. Sometimes the answer to the 'build vs. buy' question can be 'build' for the security team too.
