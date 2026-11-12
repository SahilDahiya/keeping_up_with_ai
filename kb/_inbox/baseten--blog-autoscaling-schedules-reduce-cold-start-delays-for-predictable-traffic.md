---
title: 'Autoscaling schedules: reduce cold-start delays for predictable traffic'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/autoscaling-schedules-reduce-cold-start-delays-for-predictable-traffic
author: Jonathan Rochette
published: '2026-11-01'
fetched: '2026-11-12T06:13:28Z'
classifier: null
taxonomy_rev: 2
words: 387
content_sha256: 687d4624e7c864f9af9ac313e89759b4f972a437d2b1a73dff5267f93d8c679f
---

# Autoscaling schedules: reduce cold-start delays for predictable traffic

Product
# Autoscaling schedules: reduce cold-start delays for predictable traffic

Use autoscaling schedules to start replicas before your traffic arrives, so requests don’t wait on cold starts.


- Authors
- Date
- November 1, 2026

TLDR

Autoscaling schedules reduce cold-start delays by raising the minimum number of replicas before predictable traffic arrives. You can set a schedule to recur (e.g., weekday mornings) or to run once (e.g., ahead of a product launch). Configure up to 10 schedules per environment through the dashboard, CLI, or Management API.

Autoscaling adjusts the number of replicas to match incoming traffic. When demand increases, new replicas need time before they can handle requests. This is their [cold-start time](https://docs.baseten.co/deployment/autoscaling/startup-times), which includes allocating compute resources, starting the serving software, and loading the model. Requests that wait during a cold start have longer end-to-end response times.

[Autoscaling schedules](https://docs.baseten.co/deployment/autoscaling/schedules) help avoid cold-start delays by starting additional replicas before traffic arrives. You can set a schedule to recur (e.g., every weekday morning) or to run once (e.g., ahead of a launch).

Many workloads have predictable traffic. Autoscaling schedules let you change your autoscaling settings at set times, so you don’t need to maintain an external cron job to do it.

- **Recurring peaks:** Raise the minimum number of replicas during work hours and lower it overnight. For example, a meeting-transcription app can scale up before meetings begin and back down after the peak.
- **Planned events:** Schedule a temporary capacity increase for product launches, load tests, or migrations to a new deployment.

Each schedule sets a time window and the minimum and maximum number of replicas for that window. The minimum sets the lowest number of replicas the autoscaler keeps running during the window. The maximum limits the total number of replicas the autoscaler can run. When no schedule is active, the environment uses its default settings.

To configure a schedule:

- Create up to 10 schedules per environment, all using one shared timezone.
- Choose a daily, hourly, or one-time window. Windows can’t overlap and must last at least five minutes.
- Use the dashboard, CLI, or Management API.

Start replicas before your expected traffic arrives to reduce cold-start delays. [Follow the setup guide](https://docs.baseten.co/deployment/autoscaling/schedules) to configure schedules through the dashboard, CLI, or Management API, or [talk with our engineers](https://www.baseten.co/talk-to-us/) to customize the setup for your workload.
