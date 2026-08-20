---
title: 'Inside Cresta''s Platform: Auth, APIs, and Scaling'
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- infra-platform/deployment
summary: Cresta's platform re-architecture into four layers (client, edge orchestration,
  service/platform including ML services, and infra), motivated by supporting third-party
  API consumers alongside the first-party web app. Covers microservice scaffolding
  that unifies logging, config, CI/CD and testing, plus migrating auth and config
  off Netlify lambdas into dedicated services.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/platform-auth-apis
author: null
published: '2021-06-25'
fetched: '2026-08-20T06:14:00Z'
classifier: claude
taxonomy_rev: 2
words: 530
content_sha256: 88c481c8324d2453043eab62c2e592452b8110ddad209dadc17d249bc466b520
---

# Inside Cresta's Platform: Auth, APIs, and Scaling

As Cresta scales its engineering org, a key driver for delivering business impact will be developer velocity. We would like to build a foundation that empowers squads to deliver on new features and capabilities without worrying about non-business logic or use-case specific technical decisions. We began this exploration from the question:

*How do we define/support a robust API layer that will allow us to support our 1st party usage and potential future 3rd party usage?*

As we started defining what systems and architecture would allow us to achieve our goals, it became apparent that it made sense to expand the scope of the exercise into a broader analysis of an architecture that will support Cresta as we scale, increase the number of services we maintain, and look to build out internal/external applications, APIs, and data systems.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f37f39f99bb6d9fe593_6813893539a2397816a2d578_platform-auth-apis-body.webp)

The above diagram presents a multi-layered architecture that represents the direction we would like to move towards at Cresta. At a high level, these layers are:

- **Client:** 1st and 3rd party integrations that leverage Cresta’s functionality. In present form, this is Cresta’s first-party web app or various of our direct integrations. In the future, this may include a Cresta SDK or integrations with an exposed public API.
- **Edge:** Responsible for serving and supporting Cresta clients. Our Edge layer will orchestrate the interaction between clients and multiple backend services while hiding the underlying backend architecture.
- **Service/Platform:** Our core business logic functionality. Today, this would include our ML services. In the future, this may include other data systems or platform services providing common functionality that can be leveraged by other backend services.
- **Infra.** Provides infrastructural components that allow the system to be abstracted away from the underlying environment (e.g. cloud service provider).

During the past quarter, we have begun investing in building out our platform, and the following efforts have been or are soon to be completed:

- **Microservice framework:** We have built out scaffolding to make it easy for engineers to spin up new services and unify some of the common auxiliary functionality such as logging, config, CI/CD, and testing.
- **Migrating from Netlify to new services:** Using our new microservice framework, we have begun migrating certain functionality related to authentication and config into new services that provide us greater control/reliability over our previous setup running lambdas on Netlify.
- **API tooling:** Tooling has been added to make it easy to spin up new API endpoints and share handling of cross-cutting concerns such as request authentication.

In the future, we expect that these investments will allow us to execute on capabilities such as:

- **Open API:** The proposed architecture provides a foundation from which we can work to provide public APIs. These APIs will allow us to provide better integration between our and our customers’ data ecosystems, facilitating actions such as historical data ingestion/exports.
- **Data Infra at Cresta:** Some of the frameworks/patterns we are implementing will better position us to support real-time streaming data applications. Increasing our data capabilities will allow us to be more data-driven in our product direction, provide more powerful analytics, and also improve the capabilities of our[AI solutions](https://cresta.com/solutions/) by providing mechanisms for richer data transformations.
