---
title: Serverless routing made sticky | Modal Blog
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- inference/serving
summary: Describes Modal's Sticky Sessions, built on the fprs stateless proxy underlying
  Modal Servers, which guarantees every request in a session lands on the same container
  for stateful workloads like streaming STT and voice agents, replacing the max_containers=1
  anti-pattern with session-based autoscaling.
triage: null
skip_reason: null
source: modal
url: https://modal.com/blog/serverless-routing-made-sticky
author: Siwon Park; Kartik Sinha; Kathir Meyyappan; Daniel Shaar
published: '2026-10-20'
fetched: '2026-10-21T06:10:23Z'
classifier: claude
taxonomy_rev: 2
words: 1150
content_sha256: e5c56af9dce87eae26e90e2add41a48988f13f13ff8a0d7b2b6602e483ee8e42
---

# Serverless routing made sticky | Modal Blog

At Modal, our serverless compute powers real-time inference, training, and batch jobs, scaling automatically with demand. [Sandboxes](https://modal.com/docs/guide/sandboxes) offer a different model, containers whose lifecycles you explicitly control. A growing number of workloads require something in-between; autoscaling serverless compute that maintains continuity between requests. Consider a [speech-to-text model](https://modal.com/docs/examples/streaming_kyutai_stt) with decoder state for an audio stream, a [voice agent](https://github.com/modal-projects/modal-phonon-voice-bot) that holds a conversation, or a [multiplayer game](http://curvytron.modal.dev). For these workloads, users must come back to the same container on every reconnect for the entirety of their session.

We recently launched [Sticky Sessions](https://modal.com/docs/guide/sticky-sessions#sticky-sessions), built on top of our low-latency [Modal Servers](https://modal.com/blog/serverless-servers). Every session’s requests land on the same container. To use Sticky Sessions, just create a Modal Server with the `@modal.sessioned()` decorator and start the sessions with the [SDK](https://modal.com/docs/sdk/py/latest/Server#sessions) or the [HTTP API](https://modal.com/docs/guide/sticky-sessions#starting-and-using-a-sticky-session):

```
@app.server()
@modal.sessioned()
class Server:
    @modal.enter()
    def start(self):
	      subprocess.Popen(["python", "-m", "http.server", "8000"])
@app.local_entrypoint()
def main():
    session = Server.sessions.start(idle_timeout=600)
    headers = {"Modal-Authorization": f"Bearer {session.token}"}
    print(requests.get(Server.get_url(), headers=headers).text)
```
## Serverless with strong affinity

Modal has supported [WebSockets via Web Functions](https://modal.com/blog/websocket-launch) for some time. However, a WebSocket connection is tied to a Function “input”, not a container—if the connection drops, a new input is created on reconnect and can land on a different container.

Stateful web UIs such as [Gradio](https://gradio.app/guides/deploying-gradio-with-modal#sticky-sessions) and [Streamlit](https://modal.com/docs/examples/serve_streamlit) are workloads that need strong affinity guarantees between requests and backend containers. Every request has to reach the process that holds the user’s state. One anti-pattern workaround is setting `max_containers=1`, which guarantees stickiness by giving up scaling entirely.

Modal Servers already provide a [softer form of affinity](https://modal.com/docs/examples/server_affinity); requests that share the same `Modal-Affinity-Routing-Key` header are routed to the same container in a best-effort manner. The container can still be scaled down or replaced at any time, routing future requests to a different container.

Sticky Sessions provide stronger routing guarantees by ensuring all requests in the same session land on the same container.

## Modal Servers gave us the foundation

Sticky Sessions build on the infrastructure we developed for [Modal Servers](https://modal.com/blog/serverless-servers). At the core of this infrastructure is our in-house stateless proxy (fprs). The proxy provides low-latency routing and load balancing using in-memory cached routing state reconciled from durable storage. Servers already give us a way to route HTTP traffic to a container, manage container lifecycles, and scale the fleet based on demand.

Sticky Sessions needed three things that the current request-level routing didn’t provide:

- **Fixed routing:** Every request in a session reaches the same container.
- **Session lifecycle:** The container’s host tracks which requests belong to which sessions and determines when each session becomes idle.
- **Session-based autoscaling:** The container fleet scales with the number of active sessions rather than requests.

## Making serverless infrastructure session-aware

From the client’s perspective, a Sticky Session works like a pipe. Once the client creates a session, every future request for that session will be directed to the same container.

This may seem simple, but Modal’s serverless infrastructure was built and optimized for the opposite idea; that individual requests are independent. In viewing Modal Servers from the perspective of sessions (rather than just requests), we had to reason about authorization, load balancing, and autoscaling from first principles.

![](<https://modal-cdn.com/cdnbot/modal-session-routing%20(2)93hifwbe_4e5e407e.webp>) 

### Authorization

Modal Servers require [Proxy Tokens](https://modal.com/docs/guide/webhook-proxy-auth) by default. To share Sticky Sessions, you shouldn’t need to turn off authentication or pass your Proxy Token around.

Instead, each [`sessions.start()`](https://modal.com/docs/sdk/py/latest/Server#sessionsstart) request returns a signed session token to grant access to that session. Sharing this token among clients lets multiple participants access the same state in a room, game, or collaborative app.

Maintaining the session-to-container mapping in the proxy would require keeping that mapping consistent through restarts and across multiple replicas. To avoid this, we encode routing metadata directly into the token. Our proxies validate the token and route requests to the container holding the session.

### Load Balancing

Since we’re not storing session state in the proxy, the authoritative view of session state lives only on the host that owns the session. This means the load balancer cannot have an instantaneous global view of available capacity.

To discover available capacity, our load balancers periodically probe containers for a snapshot of their available concurrency. The load balancers then use a combination of recent routing decisions and the probed snapshots to inform container selection. This evenly distributes sessions across available containers while minimizing wasted roundtrips to containers that are out of capacity.

### Autoscaling

Modal Servers autoscale on request volume, aiming to achieve a per-container request concurrency target. The request-driven autoscaler assumes that request traffic can be rebalanced evenly across the serving fleet of containers. This model works well for stateless Servers. However, Sticky Sessions behave differently in that session traffic is not *movable*. Each session’s traffic has to land on the same container even if traffic volume varies across sessions.

This motivated having sessions be the unit of concurrency, akin to Modal Functions with inputs. A container can be configured to run 1 or more sessions concurrently. When concurrency runs out, new sessions wait in a queue for existing sessions to end or a new container to become ready. The autoscaler continuously monitors active session counts and queued demand to make scaling decisions that appropriately size the compute fleet.

## What Sticky Sessions unlock

Sticky Sessions’ strong routing and lifecycle guarantees on top of Servers enable first-class support for a new suite of applications on Modal:

**Low-latency voice agents:** The [Modal Phonon Voice Bot](https://github.com/modal-projects/modal-phonon-voice-bot) runs a [Pipecat](https://docs.pipecat.ai/) agent with [Gradium Phonon](https://huggingface.co/gradium/phonon-31m-en) text-to-speech over WebRTC. Each call is a Sticky Session that is pinned to a container, so WebRTC signaling reaches the container that holds the peer connection. The session keeps the container active while the audio flows through WebRTC.

**Shared rooms**: Our [sessioned chat room example](https://modal.com/docs/examples/sessioned_chatroom) backs each chat room with a Sticky Session. Every client that connects with the session token is routed to the same container. Each room’s messages are broadcasted to everyone in the room. Clients can drop and reconnect to the same room for the lifetime of the chat room session.

**Gaming:** Gaming applications keep state in memory to maintain continuity and reduce lag. Sticky Sessions support both preserving progress and hosting concurrent rooms of players.

## A brave, sticky world

At Modal, we love using Modal. Amidst our quest for [infinite scale](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds) and [frontier performance](https://modal.com/blog/trillion-tokens-trillion-parameters), we find ourselves playing (a lot of) [Curvytron](https://www.curvytron.com/). And of course, we host our own speedy (no more input lag excuses!) us-east deployment on Modal Servers atop Sticky Sessions.

![](<https://modal-cdn.com/cdnbot/Screenshot 2026-10-20 at 2qy6rb6_k_45814f98.webp>) 

Like many multiplayer games, Curvytron has players in a shared room competing against one another in real-time. With Sticky Sessions, players can create a room, share the game link, and play with others! Modal scales based on active room count automatically.

Special thanks to Claudia Zhu, Richard Gong, Akshat Bubna, Michael Waskom, and Ben Shababo for helping shape this feature!

If you’re interested in building foundational infrastructure for the next generation of software, we’re [hiring](https://modal.com/company#careers).
