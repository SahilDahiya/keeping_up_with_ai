---
title: How Pydantic cut CI costs with RunsOn
kind: blog
topic: infra-platform
subtopic: cost
secondary_topics:
- product-engineering/case-studies
summary: 'Pydantic/Logfire cut monthly CI costs from $18,200 (August 2026) to $5,700
  (September) by moving GitHub Actions to RunsOn''s ephemeral EC2 runners: Spot instances
  for interruption-tolerant jobs, On-Demand for merge-queue/release paths, and Graviton
  ARM runners for most Python/TypeScript/agentic jobs, even as runner-minutes kept
  climbing with AI-driven PR volume (2,032 PRs merged in August vs. 365 a year earlier).'
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/ai-oh-my-ci
author: Bill Easton
published: '2026-10-16'
fetched: '2026-10-17T06:14:36Z'
classifier: claude
taxonomy_rev: 2
words: 725
content_sha256: 45d49681d8ca21834bbcd4ffc8fc6db94e18bfce2e28829ed6f2895e80b0cf98
---

# How Pydantic cut CI costs with RunsOn

[Pydantic runs on RunsOn](https://runs-on.com/). We moved to RunsOn on September 1. It launches ephemeral EC2 runners for [Logfire](https://pydantic.dev/logfire)'s GitHub Actions workflows in our AWS account. Logfire is built in our `pydantic/platform` repository. Previously, we used a mix of GitHub Actions, Depot, and Ubicloud for our CI infrastructure.

Why did we make the move? Our CI bill rose from $3,990 in June to $10,778 in July, nearly three times April's spend. By August, it had reached $18,200. By August 30, the Logfire team had merged 2,032 pull requests that month. Over the same 30 days in 2025, a team of the same size merged 365 pull requests. Our CI costs were exploding as the team adopted AI and began shipping more than ever before.

## 

| Month | Total CI cost | Total runner minutes | 
|---|---|---|
| April 2026 | $3,813 | — | 
| May 2026 | $3,665 | — | 
| June 2026 | $3,990 | — | 
| July 2026 | $10,778 | — | 
| August 2026 | $18,200 | 1,230,264 | 
| September 2026 | $5,700 | 1,617,654 | 

The main CI workflow in `pydantic/platform` ran 4,194 times in May, 6,669 times in June, 11,919 times in July, and 20,659 times through August 30. Growth continued after the move: runner minutes rose from 1,230,264 in August to 1,617,654 in September, while total CI cost fell to $5,700.

We weren't delivering slop. We shipped real products, added important tests, improved browser coverage, and ran significantly more automated reviews. AI accelerated all of it. A repository that once merged hundreds of pull requests per month now merges thousands, with bots creating much of that activity and responding to the rest. RunsOn gave us a way to absorb that growth without slowing the team down.

## 

With RunsOn, GitHub still orchestrates every workflow, while fresh EC2 runners start in our AWS account and disappear when the job finishes. We did not have to replace GitHub's CI control plane or build our own runner platform to control the machines, networking, storage, and cost underneath it.

Once RunsOn was installed in our AWS account and connected to GitHub, ordinary jobs mainly needed a different runner label and the RunsOn setup action. Container builds needed some additional cache and registry changes.

GitHub Actions and managed runner services had let us reach this scale without operating a runner fleet. Above a million runner minutes per month, we wanted more control over which machines we paid for. RunsOn handles the runner lifecycle. We still manage our AWS account, runner catalog, capacity strategy, storage, cache policy, quotas, and telemetry. [RunsOn pays for itself at 22 jobs per day](https://runs-on.com/blog/runson-break-even/), a threshold we were well past.

Today, our catalog ranges from one-core ARM runners to 16-core image builders. Most Python, TypeScript, agentic, and control-plane jobs run on Graviton; x64 remains for container builds and tests that require it. Each preset contains several eligible EC2 families so the Spot allocator has more capacity pools to choose from. RunsOn's [Magic Cache](https://runs-on.com/docs/performance/caching/actions/) serves existing `actions/cache` calls close to the runners, while sticky EBS disks preserve expensive BuildKit state.

We did not make every job Spot. Merge-queue validation, release publishing, deployments, and jobs with expensive restarts use On-Demand instances. Long, interruption-sensitive jobs use capacity-optimized Spot placement. Shorter jobs use price-capacity-optimized placement. The private deployment spans three availability zones, and a circuit breaker temporarily sends new jobs to On-Demand after a burst of interruptions. This sounds complex, but RunsOn does the heavy lifting.

September was our first month on RunsOn. Our total CI cost was $5,700, down from $18,200 in August. That includes the RunsOn license and all AWS costs: compute, EBS, S3 cache storage, and data transfer.

## 

Three rules mattered more than any individual instance type:

- **Use Spot where retries are cheap.** Keep the merge queue and release paths on On-Demand capacity.
- **Right-size against the critical path.** The cheapest runner is the one that meets the workload's latency target at the lowest total cost.
- **Keep cache near the compute.** Retain it only while it is likely to be reused.

AI increased the amount we could deliver, and our CI bill grew with it. We did not ask the agents to stop. We changed where their builds and tests ran, then kept tuning the machines, caches, and capacity as the workload grew.
