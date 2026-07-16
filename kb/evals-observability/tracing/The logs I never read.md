---
title: The logs I never read
kind: blog
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/tool-use
summary: A dogfooding walkthrough of tracking down a customer bug in a distributed
  system through Logfire traces rather than reading all the logs, framed by how large
  context windows and tool use have made coding agents productive but also more prolific
  bug generators.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/the-logs-i-never-read
author: Marc
published: '2026-02-05'
fetched: '2026-07-16T22:04:31Z'
classifier: claude
taxonomy_rev: 2
words: 1004
content_sha256: 1209193c0516d6c42abb76c757517d04af81e7bf2ba4d2126f450d509f237adb
---

# The logs I never read

The art of finding bugs will endure through the brave new age of ~~LLM-assisted engineering~~ vibe coding: as coding agents get closer to mimicking a real developer every day, the number of bugs they output must also go up, at least in absolute terms. Even if that turns out to be false, we thankfully have plenty of bugs stashed away for the rainy day when you warm your feet on an overheating GPU telling you a boolean check is inverted.

The coziness fades away in a typical production system though: your bugs are suddenly in a distributed system, with one half being in the production cluster, the other half a third-party service and the third half on the machine your customer uses. Given that you are reading this blog, I assume you did not skimp on observability, logging the crap out of your services, but considering how easy it is with Pydantic Logfire (*he said, eyeing his paycheck*) to instrument and accumulate obscene amounts of log data, how are you going to read it all?

Even at Pydantic, our code isn't bug-free from the get-go, but at least this presents an opportunity to showcase how much [of our own dogfood](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) we eat at the company and how you, too, can have a taste. Let's track down a customer issue without reading all that [extensive documentation](https://pydantic.dev/docs/logfire/get-started).


Even if you are a skeptic, there's no denying that LLMs have had an impact on more than Silicon Valley stock prices. If you haven't already, I highly recommend you draw back the curtain and see [how little it takes to build a coding agent on top of a competent LLM](https://ampcode.com/how-to-build-an-agent) though. Besides model improvements, two things have, over the last year or two, made these tools especially productive:

- Context windows large enough to be useful, along with patterns to manage them, regardless of whether they are called "subagents", "skills" or "planning mode".
- Tool use, *i.e.*the ability of that predictive text hallucination engine to actually affect the real world and fetch information from it.

The second part is where true power comes from: [Set up integration with Logfire MCP](https://pydantic.dev/docs/logfire/guides/mcp-server/) -- the [ model context protocol](https://modelcontextprotocol.io/docs/getting-started/intro), which is fancy talk for "a JSON request/response shipped through a pipe or a REST call" -- and suddenly your local coding agent has full access to production logs as if they were on the local filesystem.


Say a customer sends you a message and your first instinct is to forward it straight to a coding agent:

Prompt> a customer sent me the following message:

Hey guys, I’m trying to set up OTEL export from (redacted) to Logfire, with OTEL Push URL as

[https://logfire-eu.pydantic.dev](https://logfire-eu.pydantic.dev), and Authorization=.. in the header. This works if I curl it manually, but (redacted)’s integration keeps giving me 400s: Bad Request: Failed to send logs to OTEL:`HTTPStatusError("Client error '400 Bad Request' for url 'https://logfire-eu.pydantic.dev/v1/logs'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400")`...

Instructing the agent to search the logs miraculously works, delegating the search to Logfire through the MCP server:

Agent> I can see errors being captured on fusionfire-ingest at ingest.rs:177. Now let me check whether any of the

`BadRequest`errors correlate with (redacted)'s traffic. The interesting one is this:`BadRequest("invalid json: invalid type: integer \1769189520546375936, expected a string at line 1 column 186")`...

Prompt> check the source, maybe, but can't you see from the trace what's wrong?

Agent>... For a /v1/logs endpoint, column 186 in a typical OTEL JSON ExportLogsServiceRequest would be around the traceId or spanId field inside the first log record. These are defined as hex strings in the OTEL JSON spec but (redacted) is sending them as integers.


Certainly an observability company would not forget to instrument the full error message on a parsing endpoint, but if we *imagine* this was the case, we can still salvage this. Proving that developers are not entirely obsolete yet, try this prompt and take a screenshot for your boss:

Prompt> looks suspiciously close to create_at

Agent> You're right — 1769189520546375936 is suspiciously close to the created_at value on the span itself (1769189584933.621 ms, i.e. 1769189584933621000 ns). Let me check: .. So the issue is: (redacted) sends timeUnixNano as an integer instead of a string, which fails serde deserialization against the strict OTEL JSON schema. ..


We may not (and cannot, for data protection reasons) be logging the raw request payload, but it was possible to roughly correlate the field that failed parsing anyway by guessing the byte offset from the struct definition of the source.


There's magic in having the production logs virtually next to the source, allowing a coding agent to do much of the cross-checking. This is not unlike how a human would approach this task without any AI in the loop: browsing the relevant logs, trying to correlate the problem with the respective call site in the source code and looking at the actual data. Logfire allowed an agent to do most of the legwork, and we merely had to nudge it in the right direction by intuiting that we were looking at a timestamp.


The bug indeed turned out to be a parsing issue: The [OpenTelemetry spec](https://opentelemetry.io/docs/specs/otlp/) uses Protobuf for its log messages. The Protobuf standard requires 64-bit integers to be encoded as strings in JSON, all because JavaScript [can only safely handle integers up to 2^53 - 1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER), and languages without this limitation tend to forget about it. [Postel's Law](https://en.wikipedia.org/wiki/Robustness_principle) says receivers should be lenient, but the official OpenTelemetry Rust crate rejects integer literals outright.

Here's where the problem lies: The third-party log emitter technically sent Protobuf JSON in violation of the spec: 64-bit integers were not encoded as strings, but as integer literals. The crate also violates the spec by not accepting it, and of course two wrongs don't make a right here. On our system, JSON-encoded Protobuf is much less common than binary encoded, especially with an encoder that has this particular quirk.

In the end, we are glad to have found this and [offer a fix upstream](https://github.com/open-telemetry/opentelemetry-rust/pull/3329) for good measure. And those logs? Still haven't.
