---
title: 'MCP Python SDK v2 beta: what is new and how to try it'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/mcp-python-sdk-v2-beta
author: Marcelo Trylesinski
published: '2026-07-27'
fetched: '2026-07-28T06:57:18Z'
classifier: null
taxonomy_rev: 2
words: 1692
content_sha256: e748a2dd4dc8907ba35f92a826da5a7115b7d2cbf77d568a7140fb503fe89034
---

# MCP Python SDK v2 beta: what is new and how to try it

Tomorrow the [2026-07-28 revision of the MCP specification](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
lands. It's the largest revision of the protocol since launch: a stateless core, a first-class extensions framework,
MCP Apps, Tasks as an extension, and authorization hardening. We'll be marking the launch with a
[live release party on YouTube](https://www.youtube.com/live/T8OrdNOzvcU), so join us to celebrate and see what's new.

The Python SDK beta already speaks it. I help maintain that SDK, so let's walk through what changed, and what you get
for free when you point it at [Pydantic Logfire](https://pydantic.dev/logfire).


```
uv add "mcp[cli]==2.0.0rc1"         # or: pip install "mcp[cli]==2.0.0rc1"
```
The exact pin matters. `pip` and `uv` won't resolve to a pre-release unless you ask for one, so an unpinned install
gives you the latest v1.x instead.


Let's start with the smallest thing that works. Two type-hinted functions and a docstring:

```
from mcp.server import MCPServer
mcp = MCPServer("Demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```
That's a complete MCP server. You don't write JSON Schema, because `a: int, b: int` *is* the schema.

The same package is a full client. In v1 you had to stack three things: a transport context manager, a
`ClientSession` around it, and a hand-called `await session.initialize()`. Now it's one object:

```
import asyncio
from mcp import Client
from server import mcp
async def main() -> None:
    async with Client(mcp) as client:
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(result.structured_content)  # {'result': 3}
asyncio.run(main())
```
`Client` takes a server object (in memory, no transport at all, which is how you should test), a URL for Streamable
HTTP, or any transport context manager. Swap `mcp` for `"http://localhost:8000/mcp"` and the same code talks to a
remote server.


The renames are the first thing your v1 codebase hits, because the old import paths are gone rather than deprecated:

- `FastMCP`is now- `MCPServer`- `mcp.server.fastmcp.*`moved to- `mcp.server.mcpserver.*`. If you built your server with decorators, that rename is most of the port.
- **The wire types moved to their own distribution**,- `mcp-types`, imported as- `mcp_types`. It depends on nothing but Pydantic and- `typing-extensions`, so a gateway or a proxy can consume MCP's wire shapes without installing an HTTP stack.
- **Every field is snake_case**:- `result.is_error`,- `tool.input_schema`,- `listing.next_cursor`. The JSON on the wire is still camelCase, only the Python attribute spelling changed.
- **Transport configuration moved to**and the app builders.- `run()`- `MCPServer`is about what your server- *is*, so- `MCPServer("x", port=9000)`is a- `TypeError`now.
- **The low-level**Handlers are constructor arguments with one uniform shape,- `Server`was rebuilt, not renamed.- `async (ctx, params) -> result`, and the ambient- `server.request_context`ContextVar is gone.

Two changes don't announce themselves with an import error, so watch for them. Sync `def` tools now run on a worker
thread instead of blocking the event loop, which matters to thread-affine code. And the HTTP client is `httpx2`, which
verifies TLS through the operating system trust store instead of `certifi`'s bundle, so a minimal container with no
system CA store can suddenly start failing handshakes.


v2 serves both revisions at once. The same `streamable_http_app()` answers a 2025-era client's `initialize` and a
2026-era client's requests, with no flag to flip and no separate deployment.

- **No handshake, no session.**Every request carries its protocol version, client info, and capabilities in- `_meta`, and discovery is a plain- `server/discover`request. Over Streamable HTTP there's no- `Mcp-Session-Id`on the 2026 path, so nothing ties a modern request to a worker, and any replica behind a round-robin load balancer can answer.
- **Roots, sampling, and MCP-level logging are deprecated**(SEP-2577) on every protocol version, and- `ping`is removed outright. Expect an- `MCPDeprecationWarning`on your first- `ctx.info(...)`after upgrading.
- **Change notifications become one stream.**- `subscriptions/listen`replaces the standalone GET stream and- `resources/subscribe`.
- **Requests are routable without parsing bodies.**Modern HTTP requests carry- `Mcp-Method`and, for tool-ish calls,- `Mcp-Name`(SEP-2243), so gateways and rate limiters can route on headers alone.

And then there's the one that will actually change how you write tools.


This is the big one, so let's take it slowly.

Sometimes a tool can't finish in one round trip. It needs something only the user has: a choice, a confirmation, a
credential. Before 2026-07-28, the server got it by *calling back*. In the middle of handling your `tools/call`, it
opened its own request to the client: an elicitation, a sampling call, a `roots/list`.

The 2026-07-28 spec retires that back-channel. There is no channel for it, so `ctx.elicit()` and
`ctx.session.create_message()` raise `NoBackChannelError` on a modern connection.

Instead, **the server returns**. It answers `tools/call` with an `InputRequiredResult` carrying what it still needs
plus an opaque `request_state` token. The client fulfills the request, then calls the same tool *again*, with its
answers and the token attached. The server now has what it was missing and returns a normal `CallToolResult`.

That's the whole mechanism, and the nice part is that every leg is an ordinary client-to-server request. Nothing ever flows the other way.

Now, you rarely build that by hand. You declare a dependency instead, and the SDK does the round trips for you:

```
import asyncio
from typing import Annotated
from mcp_types import ElicitRequestParams, ElicitResult
from pydantic import BaseModel
from mcp import Client
from mcp.client import ClientRequestContext
from mcp.server import MCPServer
from mcp.server.mcpserver import AcceptedElicitation, Elicit, ElicitationResult, Resolve
mcp = MCPServer("Bookshop")
class Quantity(BaseModel):
    copies: int
async def ask_quantity() -> Elicit[Quantity]:
    """Resolver: ask the user how many copies to put aside."""
    return Elicit("How many copies?", Quantity)
@mcp.tool()
async def reserve(title: str, quantity: Annotated[ElicitationResult[Quantity], Resolve(ask_quantity)]) -> str:
    """Reserve copies of a book, asking the user how many."""
    if isinstance(quantity, AcceptedElicitation):
        return f"Reserved {quantity.data.copies} of {title!r}."
    return "Nothing reserved."
async def answer(context: ClientRequestContext, params: ElicitRequestParams) -> ElicitResult:
    return ElicitResult(action="accept", content={"copies": 2})
async def main() -> None:
    async with (
        Client(mcp, mode="legacy", elicitation_callback=answer) as legacy,
        Client(mcp, elicitation_callback=answer) as modern,
    ):
        for client in (legacy, modern):
            result = await client.call_tool("reserve", {"title": "Dune"})
            print(client.protocol_version, result.structured_content)
asyncio.run(main())
```
If you've used FastAPI, `Resolve(...)` is `Depends`. Same move, same reason.

The `quantity` parameter never appears in the tool's input schema, so the model is never told about it and can't
invent it. A parameter the model can't supply is a parameter the model can't get wrong.

Run that file and both clients get the same answer:

```
2025-11-25 {'result': "Reserved 2 of 'Dune'."}
2026-07-28 {'result': "Reserved 2 of 'Dune'."}
```
One tool body, two protocol eras. That's the part I like: you don't write the fork.


Here's where it gets fun for me, because I work on [Logfire](https://pydantic.dev/logfire) too.

v2 depends on `opentelemetry-api` directly and ships an OpenTelemetry middleware **enabled by default**. Every server
emits a SERVER span per inbound message, and the client emits a CLIENT span per outbound request. It only depends on
the API half of OpenTelemetry, so with no exporter installed a span is a no-op and costs you basically nothing.

To see them, call `logfire.configure()`. That's the whole integration:

```
import logfire
import uvicorn
from mcp.server import MCPServer
logfire.configure(service_name="mcp-server", distributed_tracing=True)
mcp = MCPServer("logfire-demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    with logfire.span("add {a} + {b}", a=a, b=b) as span:
        result = a + b
        span.set_attribute("result", result)
        return result
uvicorn.run(mcp.streamable_http_app(), host="127.0.0.1", port=8000)
```
And the client:

```
import asyncio
import logfire
from mcp import Client
logfire.configure(service_name="mcp-client")
async def main() -> None:
    with logfire.span("mcp session"):
        async with Client("http://127.0.0.1:8000/mcp") as client:
            tools = await client.list_tools()
            logfire.info("server exposes {names}", names=[t.name for t in tools.tools])
            result = await client.call_tool("add", {"a": 2, "b": 3})
            logfire.info("add(2, 3) -> {content}", content=result.content)
asyncio.run(main())
```
Those are two separate processes. In [Logfire](https://pydantic.dev/logfire) they arrive as one trace:

```
mcp session                    [mcp-client]
  MCP send server/discover     [mcp-client]
    server/discover            [mcp-server]
  MCP send tools/list          [mcp-client]
    tools/list                 [mcp-server]
  server exposes ['add']       [mcp-client]
  MCP send tools/call add      [mcp-client]
    tools/call add             [mcp-server]
      add 2 + 3                [mcp-server]
  add(2, 3) -> ...             [mcp-client]
```
The client injects W3C trace context into the request's `_meta` and the server extracts it (SEP-414), so a tool call
made by an agent on one machine and executed on another is a single connected tree, with your own `add 2 + 3` span
nested underneath. If an inbound message has no trace context, say from a client that isn't the SDK, the server span
parents to whatever is current instead of starting an orphan trace.

Query that `tools/call add` span back out and here's what it carries:

```
gen_ai.operation.name = execute_tool
gen_ai.tool.name      = add
jsonrpc.request.id    = 3
mcp.method.name       = tools/call
mcp.protocol.version  = 2026-07-28
```
`mcp.method.name` and `mcp.protocol.version` are on every span, `jsonrpc.request.id` on every request, and
`tools/call` spans follow OpenTelemetry's GenAI semantic conventions. That last one is why your tool calls group in a
tracing UI the way any other agent's do, without extra code. A handler that raises sets the span status to error, and
so does a tool result with `is_error=True`.

Now go back to that dual-era example and look at it in Logfire. The legacy client shows the old back-channel, with the
server's elicitation nested *inside* the tool call:

```
MCP send tools/call reserve        req=2
  tools/call reserve               req=2   proto=2025-11-25
    MCP send elicitation/create    req=1
```
The modern client shows two `tools/call reserve` spans instead, with different request ids:

```
tools/call reserve                 req=2   proto=2026-07-28
tools/call reserve                 req=3   proto=2026-07-28
```
That second one is the retry. No nested call back to the client, just the tool being asked again with the answer attached. Multi-round-trip requests are the kind of thing that's hard to reason about from the spec text alone, and much easier to believe when you can see both shapes side by side.

To preview spans locally without sending them anywhere, run with `LOGFIRE_SEND_TO_LOGFIRE=false LOGFIRE_CONSOLE=true`.


The spec lands tomorrow, and the point of a beta is the feedback. If you maintain an MCP server or client in Python,
the most useful thing you can do today is pin `2.0.0rc1`, port something real, and tell us what hurt.

- Read [What's new in v2](https://py.sdk.modelcontextprotocol.io/v2/whats-new/)for the full tour, and the[migration guide](https://py.sdk.modelcontextprotocol.io/v2/migration/)for every breaking change
- File feedback with the [v2 feedback template](https://github.com/modelcontextprotocol/python-sdk/issues/new?template=v2-feedback.yaml)
- Or come argue with me in `#python-sdk-dev`on the[MCP Contributors Discord](https://discord.gg/6CSzBmMkjX)

If you want those traces in a real UI, Logfire has a [free tier](https://pydantic.dev/pricing), and the
[getting started guide](https://pydantic.dev/docs/logfire/get-started/) takes about two minutes.
