---
title: Testing OpAMP clients against the spec | Pydantic Logfire
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/fleet-opamp-core
author: Bill Easton
published: '2026-11-11'
fetched: '2026-11-12T06:22:35Z'
classifier: null
taxonomy_rev: 2
words: 1108
content_sha256: 565818ad83a436372eb24566b832739850ea31bfcd9b884f79305145a86af6f6
---

# Testing OpAMP clients against the spec | Pydantic Logfire

[Fleet Management](https://pydantic.dev/logfire/fleet-management) in [Pydantic Logfire](https://pydantic.dev/logfire) speaks [OpAMP](https://opentelemetry.io/docs/specs/opamp/), the OpenTelemetry protocol for managing agents. We ship OpAMP clients for Rust, Go, Node.js, Python, Java and .NET. They share one protocol core, written once in Rust. This post is about how that core is built, checked and tested, and what those same checks found when we pointed them at the upstream OpenTelemetry clients.

## 

With Fleet Management, a remote management protocol is now in every process you run. Its job is to let a server change what those processes do. If the client gets reconnects wrong, a server restart becomes a thousand clients reconnecting in the same second. If it gets credentials wrong, a key rotation locks out the fleet. If it applies two configs in the wrong order, every machine ends up on the old one. And it gets all of these wrong on every machine at once.

## 

An OpAMP client is mostly a state machine. It says hello, reports status, heartbeats, answers the server's requests for a full report, accepts or rejects remote config, rotates the credentials the server offers, keeps its instance ID across restarts, backs off when the server is down. None of that depends on the language. Writing it six times means six sets of bugs, found and fixed six times.

So we wrote it once. The core takes events (bytes arrived, a timer fired, the application changed its status) and returns what to do next (send these bytes, set this timer, hand this config to the application). It doesn't read the clock or the network. Time and randomness come in as arguments.

Each language runs the same code:

- **Go, Node.js and Java** run it as a WebAssembly module: in [wazero](https://wazero.io/), in Node's own WebAssembly engine, and in [Chicory](https://github.com/dylibso/chicory), which is pure Java.
- **Python and .NET** run it as a native library built from the same Rust, and their tests hold every reply byte for byte to the WebAssembly module's.
- **Rust** links it directly.

The WebAssembly module has no imports. It can't open a file or a socket even if a bug told it to. What's left in each language is a thin shell: open connections, start TLS, move bytes, call back into the application.

## 

Each layer catches a different kind of mistake.

**The spec, as a list.** We quoted every normative statement in the OpAMP spec, about 300 of them, each with an ID. Everything below traces back to one of those IDs, so for any MUST in the spec you can find what checks it.

**A model of the protocol.** The client's protocol, each feature flow and the server are written as [TLA+](https://lamport.azurewebsites.net/tla/tla.html) models and checked with TLC: every reachable state, within bounds, against safety invariants and liveness properties like "a client that loses its connection reconnects".

**Proofs of the pure functions.** [Kani](https://model-checking.github.io/kani/) proves properties of the core's functions for every input, and [Verus](https://github.com/verus-lang/verus) proves the URL, header and redirect rules.

**Tying the model to the code.** A model is only useful if the code does what the model says. Recorded runs of the real code are checked by TLC as behaviors of the model. Then the other direction: TLC draws behaviors from the model, and the code has to take each step the way the model does.

**Black-box conformance.** A suite of scenarios runs every client against a reference server over HTTP and WebSocket. It runs ours and the upstream OpenTelemetry clients, unchanged. CI fails if any of ours misses a MUST.

**Torture.** Hours of seeded faults at once: the server restarting, a proxy dropping and delaying packets, the process frozen and thawed. The checks are simple to state: status never goes backward, the client catches up when things go quiet, and nothing storms or leaks.

Then the usual hygiene, applied hard: fuzzing of every byte interface, 100% coverage of the core, Miri on the unsafe code at the WebAssembly boundary, and mutation testing, so a deliberate bug in the code, the model or a proof has to be caught by something.

## 

Fleet has to work with the OpAMP clients people already run, so the upstream clients go through the same scenarios as ours, and we connect them to Fleet the way a customer would. That turned up bugs in the Collector's OpAMP extension and Supervisor, and in the Java, Python and .NET OpAMP clients. We reported each one, and sent a fix where we could.

**Instance identity.** OpAMP identifies each agent by an instance UID, and the server can assign a new one.

- .NET didn't adopt a server-assigned UID, and sent its own in mixed-endian byte order ([#5406](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/issues/5406), fixed in [#5420](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/pull/5420)).
- Python ignored `new_instance_uid` ([#5092](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5092), fix in [#5096](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5096)), and doesn't send the `OpAMP-Instance-UID` header ([#5285](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5285)).
- Python sent queued messages with the sequence number and UID from when they were queued, not when they were sent ([#5097](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5097), fixed in [#5107](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5107)).

**Reconnects and status.** The cases that only show up when a connection drops.

- The Java client didn't reconnect after the server closed the WebSocket ([#3182](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/3182), fixed in [#3192](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/3192)), and didn't send a fresh status report when it did reconnect ([#3188](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/3188), fixed).
- Its first WebSocket status report could be dropped while the connection was still opening ([#3183](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/3183)), and HTTP errors never reached the application's callbacks ([#3184](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/3184)).
- The Python client's disconnect, heartbeat and retry behavior differs from the spec ([#5119](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5119)).

**Capabilities.** A client declares what it does, and the server may only rely on what it declared.

- The Java client left out `ReportsStatus`, which every client must declare ([#3185](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/3185), fixed in [#3189](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/3189)).
- The Collector's OpAMP extension didn't declare `ReportsHeartbeat`, so a server couldn't change its heartbeat interval ([#51427](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/51427), added in [#51426](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/51426)).
- The Supervisor applied a heartbeat interval of 0, which turns heartbeats off over WebSocket, and reported remote config status when configured not to ([#48363](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/48363)).

**Crashes.** The Supervisor panics at startup if its persistent state file is empty ([#52720](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/52720)), and the OpAMP extension panics if a custom capability is unregistered twice ([#52719](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/52719)).

One more finding is a critical security vulnerability. Our core isn't affected.

None of these are exotic. They're in the parts of the protocol a demo never reaches: a second connection, a server that renames you, a message that waits in a queue. That's the case for writing the protocol once, checking it against every MUST, and running every client through the same scenarios.

## 

- [Fleet overview](https://pydantic.dev/docs/logfire/observe/fleet/) in the [Logfire](https://pydantic.dev/logfire) docs.
- The OpAMP clients and their language guides: [pydantic/opamp-clients](https://github.com/pydantic/opamp-clients).
- The [OpAMP specification](https://opentelemetry.io/docs/specs/opamp/).

If you work on OpAMP, or run it at scale, we'd like to compare notes. Find us on [GitHub](https://github.com/pydantic/opamp-clients/issues) or through [contact](https://pydantic.dev/contact).
