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
url: https://www.baseten.co/blog/autoscaling-schedules-reduce-cold-start-delays-for-predictable-traffic/
author: Jonathan Rochette; Archit Mishra; Mingming Lang; Chloe Florit
published: '2026-10-30'
fetched: '2026-10-31T06:05:56Z'
classifier: null
taxonomy_rev: 2
words: 429
content_sha256: 3b7541adc37e2744264739b77c795a8724c28dbaf70c332074f853ef4c9f65c8
---

# Autoscaling schedules: reduce cold-start delays for predictable traffic

### Published

![Autoscaling schedules](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793337826-baseten-blog-2026-thumbnails-16.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Autoscaling schedules reduce cold-start delays by raising the minimum number of replicas before predictable traffic arrives. You can set a schedule to recur (e.g., weekday mornings) or to run once (e.g., ahead of a product launch). Configure up to 10 schedules per environment through the dashboard, CLI, or Management API.

Autoscaling adjusts the number of replicas to match incoming traffic. When demand increases, new replicas need time before they can handle requests. This is their [cold-start time](https://docs.baseten.co/deployment/autoscaling/startup-times), which includes allocating compute resources, starting the serving software, and loading the model. Requests that wait during a cold start have longer end-to-end response times.

[Autoscaling schedules](https://docs.baseten.co/deployment/autoscaling/schedules) help avoid cold-start delays by starting additional replicas before traffic arrives. You can set a schedule to recur (e.g., every weekday morning) or to run once (e.g., ahead of a launch).

## **Schedule autoscaling around demand** 

Many workloads have predictable traffic. Autoscaling schedules let you change your autoscaling settings at set times, so you don’t need to maintain an external cron job to do it.

- **Recurring peaks:** Raise the minimum number of replicas during work hours and lower it overnight. For example, a meeting-transcription app can scale up before meetings begin and back down after the peak.
- **Planned events:** Schedule a temporary capacity increase for product launches, load tests, or migrations to a new deployment.

![Illustrative example: starting additional replicas before an expected traffic surge can help keep end-to-end response times consistent as request volume increases.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793337606-latency-surge-no-eyebrow-subtitle.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Illustrative example: starting additional replicas before an expected traffic surge can help keep end-to-end response times consistent as request volume increases.

## **How autoscaling schedules work**

Each schedule sets a time window and the minimum and maximum number of replicas for that window. The minimum sets the lowest number of replicas the autoscaler keeps running during the window. The maximum limits the total number of replicas the autoscaler can run. When no schedule is active, the environment uses its default settings.

To configure a schedule:

- Create up to 10 schedules per environment, all using one shared timezone.
- Choose a daily, hourly, or one-time window. Windows can’t overlap and must last at least five minutes.
- Use the dashboard, CLI, or Management API.

![Two autoscaling schedules for a production environment.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1793337660-autoscaling-schedules-faithful.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Example from the Baseten UI: Two autoscaling schedules for a production environment.

## **Get started** 

Start replicas before your expected traffic arrives to reduce cold-start delays. [Follow the setup guide](https://docs.baseten.co/deployment/autoscaling/schedules) to configure schedules through the dashboard, CLI, or Management API, or [talk with our engineers](https://www.baseten.co/talk-to-us/) to customize the setup for your workload.
