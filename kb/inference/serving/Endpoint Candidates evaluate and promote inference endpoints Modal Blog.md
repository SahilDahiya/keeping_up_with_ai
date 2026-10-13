---
title: 'Endpoint Candidates: evaluate and promote inference endpoints | Modal Blog'
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- evals-observability/evaluation
summary: Modal's Endpoint Candidates feature lets teams stage alternate inference
  deployments, mirror a sample of production traffic to them, and compare latency,
  throughput, and cost before promoting a candidate; it extends a Pingora-based proxy
  with per-candidate bounded buffers and a shared chunk-count budget so slow or failing
  mirrors are cancelled instead of blocking production requests.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/endpoint-candidates
author: Amit Lohe; Deven Navani; Garrett O'Brien
published: '2026-10-12'
fetched: '2026-10-13T06:12:47Z'
classifier: claude
taxonomy_rev: 2
words: 617
content_sha256: e2c5cabd4c5d75e82afbfd755620c4a45a81bec8531747e326260538f338366d
---

# Endpoint Candidates: evaluate and promote inference endpoints | Modal Blog

Latency, throughput, and cost optimization are at the core of modern inference engineering. Without testing and measurement, these metrics cannot be reliably improved.

We’ve been focused on inference performance [for](https://modal.com/blog/trillion-tokens-trillion-parameters) [some](https://modal.com/blog/serverless-servers) [time](https://modal.com/blog/achieve-sota-specdec) [now](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary), and we’re building several new tools to help you optimize your own inference servers–starting with [Endpoint Candidates](https://modal.com/docs/guide/endpoint-candidates).

Endpoint Candidates allow you to stage alternative deployments for your [Dedicated Endpoints](https://modal.com/docs/guide/dedicated-endpoints#dedicated-endpoints), so you can evaluate the impact on quality, latency, throughput, and cost. Each Candidate can mirror production, handling a sample of production traffic while Modal runs the underlying infrastructure. When you’re ready, promote your Candidate to production from the dashboard.

With Candidates, you can test new model checkpoints–or even entirely different models–without rolling your own traffic-mirroring and deployment infrastructure. Endpoint Candidates are generally available for all Modal workspaces.

## Getting started

To create a new Candidate, start with an existing Dedicated Endpoint in your Modal environment. Select **Create candidate** to choose an open model from Modal’s catalog or bring your own weights from a Hugging Face repo or a Modal Volume.

![User interface for creating an endpoint candidate.](https://modal-cdn.com/cdnbot/pop-up-1_9c20e6e3.png) 

Once your Candidate is ready, configure your traffic sample to start mirroring production traffic to it. Production continues to handle every original request and return the response your users see.

![User interface for mirroring production traffic.](https://modal-cdn.com/cdnbot/pop-up-2_bb3e5ae5.png) 

Use the dashboard to inspect the Candidate’s inference metrics, including latency and throughput, and run [performance benchmarks](https://modal.com/docs/guide/dedicated-endpoints#benchmarks) to understand its behavior under load. Each Candidate also has its own URL, so you can run your existing evaluations against it to assess output quality.

When you’re ready, promote the Candidate from the dashboard. Modal starts a production rollout at the existing Endpoint URL. Your other Candidates remain available, so you can continue testing them independently.

![User interface for promoting candidates to production.](https://modal-cdn.com/cdnbot/pop-up-3_8f83db2e.png) 

Endpoint Candidates use [standard Modal compute pricing](https://modal.com/pricing), including compute used for mirrored requests.

## Keeping production moving

One of the challenging parts of building traffic mirroring was keeping slow mirrors from holding up production. When several Candidates receive copies of a large request, they may read the data at different speeds. A proxy can end up [buffering substantial amounts of data](https://lucumr.pocoo.org/2020/1/1/async-pressure/) while waiting for the slower Candidates.

To address this, we extended our Pingora-based proxy to fork each request stream into a separate, bounded buffer for every Candidate receiving a copy. Each mirror reads independently: if a new chunk arrives and a buffer is full, the proxy cancels that mirrored request while production and the other mirrors continue.

But a bounded buffer for each mirror still leaves a problem: a busy proxy may be mirroring many requests at once. So we also cap the body data retained by mirrors within each proxy process. They share request-body chunks, so each chunk counts only once against this budget.

Removing a chunk from a buffer doesn’t necessarily free its memory, since a network write may still be holding it. We keep counting that chunk until the last mirror releases it. If adding the next chunk would exceed the budget, the proxy cancels that request’s mirrors while the original request continues.

Mirroring is best-effort by design: mirrored requests may be dropped under pressure, so production doesn't have to wait for a slow or failing Candidate.

## What’s next

We’re expanding how you can create and evaluate Candidates, from more control over compute placement and serving recipes to richer metrics views for comparing deployments.

We’re working to automate more of that experimentation, too. When we [introduced Auto Endpoints](https://modal.com/blog/introducing-auto-endpoints#going-full-auto-start-great-and-continually-improve), we described our work on automating inference optimization. Candidates give those optimizations a place to prove themselves: a way for Modal to test promising changes against your traffic, then surface measured improvements in latency, throughput, or cost.
