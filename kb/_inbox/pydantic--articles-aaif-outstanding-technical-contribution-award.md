---
title: AAIF award for MCP Python SDK maintenance
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/aaif-outstanding-technical-contribution-award
author: Marcelo Trylesinski
published: '2026-10-27'
fetched: '2026-10-28T06:13:32Z'
classifier: null
taxonomy_rev: 2
words: 502
content_sha256: 0e796f5bbbec200bcf83623e2915b7f0d0b6dac117a5ee27857890001fa7f3bd
---

# AAIF award for MCP Python SDK maintenance

Last Friday, on day two of [AGNTCon + MCPCon North America](https://events.linuxfoundation.org/agntcon-mcpcon-north-america/),
the [Agentic AI Foundation](https://aaif.io) gave me the **Outstanding Technical Contribution Award** for my work on the
[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

![Marcelo Trylesinski holding the AAIF Outstanding Technical Contribution Award above his head on the AGNTCon + MCPCon North America stage, between Antoni Kozelski and Bartosz Gonczarek from Vstorm](https://pydantic.dev/assets/blog/aaif-outstanding-technical-contribution-award/award-on-stage.jpg)


You can watch the moment on the day two livestream, right after the opening keynote.

## 

I'm one of the two maintainers of the MCP Python SDK. Python developers use it to build MCP servers and clients, and it's where a lot of my time has gone this year.

The biggest piece of that work was v2. We shipped the [v2 beta](https://pydantic.dev/articles/mcp-python-sdk-v2-beta) alongside the
2026-07-28 revision of the MCP specification, with a new `MCPServer` API and multi-round-trip requests. v2 is now the
stable release line.

A lot of v2 is the new specification, implemented in Python: standard error codes, authorization hardening, routable transport headers, a deprecation policy, and OpenTelemetry tracing on by default.

On the specification side, I sponsored [SEP-1288](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1288),
the WebSocket transport. The HTTP transport also runs on [Starlette](https://github.com/Kludex/starlette) and
[Uvicorn](https://github.com/Kludex/uvicorn), which I maintain, so when the SDK finds a bug underneath it, I can fix it
in the layer where it belongs.

Most of that work happens in issues, pull requests, and spec discussions that nobody sees on a conference stage. It's nice to have it noticed.

## 

First, a special thank you to my colleague [Laís Carvalho](https://pydantic.dev/authors/lais-carvalho). She nominated me, and I would not
have been on that stage without her.

To the MCP maintainers and contributors: the SDK is better because of every issue, review, and pull request you sent.

To [Pydantic](https://pydantic.dev): you pay me to work on open source, and you let me spend that time where the
community needs it. That is rarer than it should be.

It also goes both ways. I work on [Pydantic Logfire](https://pydantic.dev/logfire) too, so v2 ships an OpenTelemetry
middleware enabled by default. Call `logfire.configure(distributed_tracing=True)` in your MCP server and
`logfire.configure()` in your client, and every request between them arrives in [Logfire](https://pydantic.dev/logfire) as one trace. The [v2 beta post](https://pydantic.dev/articles/mcp-python-sdk-v2-beta) walks through it.

I also shared the stage with our friends Antoni Kozelski and Bartosz Gonczarek from
[Vstorm](https://vstorm.co/?utm_source=pydantic&utm_medium=partnership&utm_campaign=aaif-outstanding-technical-contribution-award), who won the **Open Agentic
AI Innovation Award**. Congratulations to both of you, and thank you for making the photo a lot better.

The [Logfire MCP server](https://pydantic.dev/docs/logfire/guides/mcp-server/) is where this work lands first. It runs on
the same Python SDK, so the standard error codes, the authorization hardening, and the tracing middleware above all show
up there before anywhere else. I want it to be the best MCP server you connect your coding agent to, and I spend a lot of
my week making that true. If you have a Logfire project, add `https://logfire-us.pydantic.dev/mcp` (or the EU URL) to
your agent and ask it what broke in production last night. Setup takes a few minutes, and the answer usually takes less.

See you at the next MCPCon.
