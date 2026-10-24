---
title: Augment Your LiveKit Agent with Modal GPUs
kind: blog
topic: inference
subtopic: optimization
secondary_topics:
- infra-platform/deployment
summary: Modal shows how to run a LiveKit video avatar (BitHuman's Expression Video
  Avatar voiced by Qwen3-TTS) on serverless GPUs, using Modal Sticky Sessions for
  container affinity across the avatar's `/launch` WebSocket session and GPU snapshots
  to hide cold starts that would otherwise require reloading gigabytes of model weights.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/livekit-modal
author: Ben Shababo; Andrew Hinh
published: '2026-10-15'
fetched: '2026-10-24T06:10:19Z'
classifier: claude
taxonomy_rev: 2
words: 324
content_sha256: 9bf3a6403f4bf9503d2fd3fbfecd91753ea5eda297303eec33876b81d3fc254e
---

# Augment Your LiveKit Agent with Modal GPUs

[LiveKit](https://livekit.com/) and their [Agents SDK](https://docs.livekit.io/agents/) are a popular choice for implementing WebRTC-based audio-video applications. In
this article, we share how you can use open-weights models or custom ones
running on Modal alongside LiveKit agents.

We’ll use [BitHuman’s](https://docs.bithuman.ai/) open weights [Expression Video Avatar](https://docs.bithuman.ai/models/expression-2), voiced
by [Qwen3-TTS](https://huggingface.co/collections/Qwen/qwen3-tts), to create a
clone of Modal’s GPU Enjoyer in Residence, [Charles Frye](https://x.com/charles_irl).

## Running a LiveKit Video Avatar with Sticky Sessions

A common pattern with audio-video applications is using custom models as
plug-and-play components. Increasingly so, we’ve seen users power video avatars
and [replace proprietary model APIs with open weights models](https://modal.com/blog/fast-cheap-batch-transcription) (or self-hosted proprietary models) using Modal’s [serverless GPUs](https://modal.com/blog/truly-serverless-gpus).

![Architecture of the LiveKit + Modal avatar stack.](https://modal-cdn.com/cdnbot/imageyhel63fp_34d2fec9.webp)

LiveKit Agents already supply an avatar interface, and we’ll use their BitHuman
integration which comes prepackaged as a [self-hosted GPU container](https://docs.bithuman.ai/deploy/self-hosted). The
container exposes a `/launch` endpoint which runs the avatar and joins the
LiveKit room. For low-latency HTTP communication between the endpoint and
external clients, we expose the endpoint using a [Modal Server](https://modal.com/docs/guide/servers). However, the endpoint
returns as soon as the avatar joins, which contends with how Servers scale by
in-flight requests.

Recently, we released [Sticky Sessions](https://modal.com/docs/guide/sticky-sessions), a first-class
primitive for guaranteeing strong container affinity.
This allows WebSocket connections to reconnect to the same container, where a
client can start one or more sessions on a Server container. I.e., we can start
and end the session from the client-side, and Modal will hold that Session’s
slot on the container as if there was a running request.

When a participant joins a room, the LiveKit agent starts a Sticky Session,
joins the room, and calls the `/launch` endpoint using the session token. Cold
starts are hidden by [GPU snapshots](https://modal.com/docs/examples/gpu_snapshot),
where otherwise we’d have to reload gigabytes of model weights onto the Server.
When the call is complete, the agent ends the session.

See the full code [here](https://github.com/modal-projects/modal-livekit-avatar).

## Get started now

See the LiveKit [Agent SDK](https://docs.livekit.io/agents/) and [Modal](https://modal.com/docs/guide/intro) docs for more information.
