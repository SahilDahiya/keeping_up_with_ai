---
title: 'Building IaC providers for Logfire: design decisions that mattered'
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/monitoring
summary: Design decisions in building Terraform/IaC providers for Logfire so customers
  manage alerts, dashboards, projects, and tokens as code, including how to model
  observability resources for declarative provisioning.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/infrastructure-as-code-provider-for-logfire
author: Bruno Espino
published: '2026-03-30'
fetched: '2026-07-16T23:01:30Z'
classifier: claude
taxonomy_rev: 2
words: 1498
content_sha256: 0d4491999604d2da12dd4096885844b3af1afa481751033638460cf4fdf7ef15
---

# Building IaC providers for Logfire: design decisions that mattered

Customers wanted to manage parts of Pydantic Logfire in code instead of rebuilding them by hand.

That included things like SQL alerts, dashboards, projects, channels, and tokens. The exact reason varied a bit by resource, but the underlying request was the same: customers wanted Logfire configuration to fit into the same workflows they already use for infrastructure.

That request also lines up with the usual reasons teams adopt infrastructure as code in the first place. HashiCorp's own [Terraform guidance on IaC](https://developer.hashicorp.com/well-architected-framework/define-and-automate-processes/define/as-code/infrastructure) emphasizes the same themes: version control, consistent environments, testing, and automation. Terraform's [plan workflow](https://developer.hashicorp.com/terraform/tutorials/cli/plan) gives teams a reviewable change set before apply, and Terraform's [state and drift model](https://developer.hashicorp.com/terraform/plugin/sdkv2/best-practices/detecting-drift) gives them a source of truth for managed objects. Those benefits are just as useful for product configuration as they are for cloud resources.

That became a [Terraform provider](https://github.com/pydantic/terraform-provider-logfire), published to both the Terraform Registry and the OpenTofu Registry, plus a [Pulumi provider](https://github.com/pydantic/pulumi-logfire) built on top of the same ideas.

This post is a practical story: what problem we were trying to solve, what we chose to model first, and which design decisions turned out to matter when implementing IaC for Logfire.


- **A public API is necessary, but not sufficient.**Teams want product configuration to fit into the same workflows they already use for infrastructure.
- **The value is not just "declarative syntax".**It is version control, reviewable plans, repeatable setup, and drift-aware lifecycle management.
- **Keep the provider focused on durable resources.**Start with the parts people actually want to review, recreate, and automate.
- **Good docs matter as much as good code.**If people cannot find the resources and understand how they behave, the provider will not get adopted.


It is easy to say "we already have an API" and treat that as enough.

That is true if all someone needs is one-off automation. It is not true if they want their product configuration to live inside the same workflows they use for infrastructure.

The practical difference is not the transport. It is the workflow.

With a provider, teams can:

- keep configuration in Git
- review a change before applying it
- recreate the same setup in another environment
- detect when managed state drifts from what they declared

For product configuration, that matters a lot more than just having a documented REST endpoint. Declarative observability configuration, with version-controlled state and reviewable plans, is a different thing from scripting against an API.


The useful question was not "what endpoints do we have?" It was "what parts of Logfire do users actually want to manage through an Infrastructure as Code (IaC) workflow?"

That led us to start with:

- projects
- notification channels
- alerts
- dashboards
- write tokens
- read tokens
- organizations for self-hosted deployments

Those are the parts people were already thinking about as configuration, not just UI state. They are durable, shared, and worth reviewing.

Trying to wrap the whole API would have been the wrong goal. A provider gets valuable much faster if it starts with the parts people actually want to keep in version control and talk about in code review.


This is probably the easiest trap to fall into.

If the goal becomes "cover every endpoint", you end up spending time modeling things that are technically possible to automate but not especially useful to manage declaratively.

That also makes the provider harder to learn. More resources, more schema, and more edge cases do not automatically make the product more usable.

For [Logfire](https://pydantic.dev/logfire), it was better to start with the configuration that felt stable and important enough to manage in code, and leave the rest alone until there was a clearer reason to expose it.


The provider configuration is intentionally small:

```
terraform {
  required_providers {
    logfire = {
      source  = "pydantic/logfire"
      version = ">= 0.1.0, < 0.2.0"
    }
  }
}
provider "logfire" {
  api_key = var.logfire_api_key
  # Self-hosted only:
  # base_url = "https://logfire.example.com"
}
```
For SaaS, the provider can infer the API endpoint from the API key region. Self-hosted users set `base_url` explicitly.

The same idea carries into the Pulumi provider too:

```
pulumi config set --secret logfire:apiKey pylf_v2_us_...
# Self-hosted only:
# pulumi config set logfire:baseUrl https://logfire.example.com
```
The important decision here was keeping hosted and self-hosted on the same provider surface. If the product's concepts are the same, users should not feel like they are dealing with two different products just because one deployment lives on our infrastructure and the other lives on theirs.


A provider feels real when a short config creates something a team would otherwise click together in the UI.

This example from the Logfire provider provisions a project, a webhook channel, an alert, a dashboard, and a write token:

```
resource "logfire_project" "production" {
  name        = "production"
  description = "Production observability project"
}
resource "logfire_channel" "alerts_webhook" {
  name   = "alerts-webhook"
  active = true
  config {
    type   = "webhook"
    format = "auto"
    url    = "https://example.com/logfire-webhook"
  }
}
resource "logfire_alert" "execution_errors" {
  project_id  = logfire_project.production.id
  name        = "execution-errors"
  time_window = "1h"
  frequency   = "15m"
  channel_ids = [logfire_channel.alerts_webhook.id]
  notify_when = "has_matches"
  query = <<-SQL
    select
      service_name,
      trace_id,
      otel_status_message as exception_message
    from records
    where deployment_environment = 'prod'
      and span_name = 'Alert execution error occurred'
    order by start_timestamp desc
  SQL
}
resource "logfire_dashboard" "production_overview" {
  project_id = logfire_project.production.id
  name       = "production-overview"
  slug       = "production-overview"
  definition = file("${path.module}/dashboard.json")
}
resource "logfire_write_token" "production_ingest" {
  project_id = logfire_project.production.id
}
output "production_write_token" {
  value     = logfire_write_token.production_ingest.token
  sensitive = true
}
```

Dashboards are a good example of a place where a provider can easily become annoying.

We could have tried to model every panel, query, and layout detail directly in HCL. That would have made the schema much bigger, and it would still have been a worse authoring experience than using the UI.

For Logfire, `definition = file(...)` was the better tradeoff. Teams can build the dashboard in the UI, export the JSON definition, and version that artifact without forcing everything through a huge handwritten schema.


I followed the latest [Terraform Plugin Framework](https://developer.hashicorp.com/terraform/plugin/framework) tutorial, got the provider working locally, and then started shaping it around the Logfire resources we cared about.

After that was working, I used Pulumi's docs on [building and publishing packages](https://www.pulumi.com/docs/iac/guides/building-extending/packages/publishing-packages/) and their [ pulumi-tf-provider-boilerplate](https://github.com/pulumi/pulumi-tf-provider-boilerplate) template to port it to Pulumi.

That order mattered. Terraform forced the resource model to get concrete first. Once that was in place, porting it to Pulumi was much more straightforward than it would have been if we were still changing the core shape of the provider.

The framework part itself is not the hard part. The hard part is the provider contract: what is user-configured, what is computed, what is sensitive, how updates behave, and which resources only make sense in self-hosted mode. If those decisions are messy, the provider will feel messy too.


A provider is not done when the code compiles. It is done when someone outside your team can discover the resources quickly, understand what works for SaaS and self-hosted, and copy a minimal example without guessing.

For Logfire, the [Terraform Registry docs](https://registry.terraform.io/providers/pydantic/logfire/latest/docs) are the main entry point for that. The Pulumi provider publishes the same kind of reference documentation in the Pulumi Registry.


If your product is self-hosted, you will often need both:

- a Helm chart or deployment story that runs the product
- an infrastructure as code provider that configures the product

For Logfire, the [Helm chart](https://github.com/pydantic/logfire-helm-chart) handles the runtime side of self-hosting. The provider handles product configuration like projects, alerts, dashboards, channels, and tokens.

Trying to make one layer do both jobs usually leads to awkward abstractions.


If I had to compress the whole experience into a short checklist, it would look like this:

- start with durable resources, not full API coverage
- keep SaaS and self-hosted in the same provider when the product surface is the same
- prefer practical import paths over giant schemas when the UI already exists
- publish docs where users already expect to find them
- keep the provider focused on workflows people actually want to automate and review

Users do not really care which internal generator or framework you chose. They care that the product concepts make sense, that the provider behaves predictably, and that they can fold your product into workflows they already trust.

If your product has an API and users already think about it as part of their system, an infrastructure as code provider is usually not a nice extra feature. It is how the product starts fitting the way those teams already work.

You can now use Terraform, OpenTofu, or Pulumi to manage your Logfire SQL alerts, dashboards, projects, channels, and tokens as code. [Try Logfire](https://logfire.pydantic.dev).


- [Terraform provider for Logfire](https://github.com/pydantic/terraform-provider-logfire)
- [Terraform Registry docs for Logfire](https://registry.terraform.io/providers/pydantic/logfire/latest/docs)
- [Pulumi provider for Logfire](https://github.com/pydantic/pulumi-logfire)
- [OpenTofu provider docs](https://opentofu.org/docs/language/providers/)
- [OpenTofu provider requirements docs](https://opentofu.org/docs/v1.9/language/providers/requirements/)
- [Terraform guidance on infrastructure as code](https://developer.hashicorp.com/well-architected-framework/define-and-automate-processes/define/as-code/infrastructure)
- [Terraform plan docs](https://developer.hashicorp.com/terraform/tutorials/cli/plan)
- [Terraform drift detection docs](https://developer.hashicorp.com/terraform/plugin/sdkv2/best-practices/detecting-drift)
- [Terraform Plugin Framework docs](https://developer.hashicorp.com/terraform/plugin/framework)
- [Pulumi package publishing guide](https://www.pulumi.com/docs/iac/guides/building-extending/packages/publishing-packages/)
- [Pulumi Terraform bridge boilerplate](https://github.com/pulumi/pulumi-tf-provider-boilerplate)
- [Logfire Helm chart](https://github.com/pydantic/logfire-helm-chart)
