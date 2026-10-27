---
title: 'Logs vs traces: why logs are not enough'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/why-traces-when-you-have-logs
author: Marcelo Trylesinski
published: '2026-10-26'
fetched: '2026-10-27T06:17:06Z'
classifier: null
taxonomy_rev: 2
words: 1645
content_sha256: 440ab7156fae9bfe49864af92db29f15ea7fe18b0ec02fb5e715e2daf91a9f69
---

# Logs vs traces: why logs are not enough

Developers ask me this a lot: "Why do I need traces? I have logs." I asked the same question for years.

The short answer: a log line records that something happened at one point in time. A span records an operation, with a trace ID, a span ID, a parent span ID, and a start and end time. Those fields tell you which operations belong to the same request, what called what, and where the time went. Plain logs don't carry them, so you end up guessing.

The long answer is easier to show than to explain.

## 

Here is a checkout handler. It loads the cart and the discounts concurrently, then charges the user. Three users check out at the same time, and the discount service is slow for one of them.

```
import asyncio
import logging
import random
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger("checkout")
async def fetch_cart(user_id: int) -> list[str]:
    await asyncio.sleep(random.uniform(0.05, 0.1))
    logger.info("cart loaded")
    return ["book", "mug"]
async def fetch_discounts(user_id: int) -> float:
    await asyncio.sleep(2.0 if user_id == 2 else random.uniform(0.05, 0.1))
    logger.info("discounts loaded")
    return 0.1
async def charge(user_id: int, items: list[str], discount: float) -> None:
    await asyncio.sleep(random.uniform(0.1, 0.2))
    logger.info("payment charged")
async def checkout(user_id: int) -> None:
    logger.info("checkout started")
    items, discount = await asyncio.gather(fetch_cart(user_id), fetch_discounts(user_id))
    await charge(user_id, items, discount)
    logger.info("checkout finished")
async def main() -> None:
    await asyncio.gather(*(checkout(user_id) for user_id in (1, 2, 3)))
asyncio.run(main())
```
This is the output:

```
2026-10-19 11:15:13,441 INFO checkout started
2026-10-19 11:15:13,441 INFO checkout started
2026-10-19 11:15:13,441 INFO checkout started
2026-10-19 11:15:13,493 INFO cart loaded
2026-10-19 11:15:13,494 INFO cart loaded
2026-10-19 11:15:13,503 INFO discounts loaded
2026-10-19 11:15:13,506 INFO cart loaded
2026-10-19 11:15:13,527 INFO discounts loaded
2026-10-19 11:15:13,605 INFO payment charged
2026-10-19 11:15:13,606 INFO checkout finished
2026-10-19 11:15:13,659 INFO payment charged
2026-10-19 11:15:13,659 INFO checkout finished
2026-10-19 11:15:15,442 INFO discounts loaded
2026-10-19 11:15:15,588 INFO payment charged
2026-10-19 11:15:15,588 INFO checkout finished
```
One checkout took about two seconds. Which user was it? Which of the three "checkout started" lines does the last "checkout finished" belong to? The logs can't say.

With three requests you can squint and work it out. With three hundred requests per second, the lines from different requests interleave and you can't.

## 

The usual fix is a request ID. You store it in a `contextvars.ContextVar` and add it to every log record with a filter. This replaces the `logging.basicConfig` call in the first example:

```
import contextvars
import logging
import uuid
request_id: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="-")
class RequestIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id.get()
        return True
handler = logging.StreamHandler()
handler.addFilter(RequestIDFilter())
logging.basicConfig(format="%(asctime)s %(request_id)s %(message)s", level=logging.INFO, handlers=[handler])
```
Then `checkout` calls `request_id.set(uuid.uuid4().hex[:8])` before its first log line. `asyncio` copies the context into each task, so `fetch_cart` and `fetch_discounts` see the same ID:

```
2026-10-19 11:16:29,713 16bac7c6 checkout started
2026-10-19 11:16:29,791 16bac7c6 cart loaded
2026-10-19 11:16:31,714 16bac7c6 discounts loaded
2026-10-19 11:16:31,816 16bac7c6 payment charged
2026-10-19 11:16:31,817 16bac7c6 checkout finished
```
That's better. You can filter by `16bac7c6` and see one request. To read it, though, you subtract timestamps.

The gap between "cart loaded" and "discounts loaded" is 1.9 seconds. That isn't how long the discounts took. Both calls started at the same time, so the discounts took 2.0 seconds and the cart took 78 milliseconds. Every gap between two lines is attributed to whatever code ran in between, and the logs don't name that code. A blocking call nobody logged looks exactly like a slow discount service.

## 

This is the answer I hear most, and it's a good one. Say every line is JSON, every service passes the request ID along, and every operation logs `duration_ms` when it finishes. This is the slow checkout from the same program with a JSON formatter:

```
{"ts": "11:37:35.684", "request_id": "5adf2211", "event": "checkout started", "user_id": 2}
{"ts": "11:37:35.765", "request_id": "5adf2211", "event": "cart loaded", "duration_ms": 81}
{"ts": "11:37:37.685", "request_id": "5adf2211", "event": "discounts loaded", "duration_ms": 2001}
{"ts": "11:37:37.828", "request_id": "5adf2211", "event": "payment charged", "duration_ms": 142}
{"ts": "11:37:37.828", "request_id": "5adf2211", "event": "checkout finished", "duration_ms": 2144}
```
For this request, that's enough. `duration_ms` says the discounts took 2001 ms. If all your requests look like this one, keep your logs.

It stops being enough in three situations.

### 

Say `fetch_discounts` retries after a timeout, or the checkout loads discounts once per item. Now the request has two `discounts loaded` lines. The request ID says both belong to this request. It doesn't say which one `charge` waited for, or which call in the checkout made each one. For that, every operation needs its own ID and its caller's ID.

### 

`duration_ms` is written when the operation ends. If the discount service hangs until the client gives up, or the process is killed, the request has a `checkout started` line and nothing else. You know something went wrong, not where. When the [Logfire](https://pydantic.dev/logfire) SDK starts a span, it can send a [pending span](https://pydantic.dev/docs/logfire/reference/sql/), so there's a record of the operation and its parent even if it never finishes.

### 

Your HTTP client, database driver, and payment SDK don't know about your `request_id` field. Another team's service may call it `correlation_id`. The request ID covers the lines you wrote. OpenTelemetry instrumentation covers the libraries too, and OpenTelemetry SDKs read and write the same `traceparent` header by default.

Fixing those means more fields: an ID for every operation, its caller's ID, a "started" event, and a header that carries the IDs between services. Here is what you built:

| What you added to your logs | OpenTelemetry's equivalent | 
|---|---|
| Request ID | `trace_id` | 
| Operation ID | `span_id` | 
| Caller's operation ID | `parent_span_id` | 
| "started" event and `duration_ms` | Span `start_time` and `end_time` | 
| A header with the request ID and the calling operation's ID | `traceparent` header, with the `trace_id` and the caller's `span_id` | 

Those are the fields of a span, kept by hand in your log records. You reinvented tracing, one field at a time, with no standard format and no tool that understands it.

The header in the last row is already a standard. [W3C Trace Context](https://www.w3.org/TR/trace-context/) defines `traceparent`, which carries the trace ID and the caller's span ID between services:

```
traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01
```
OpenTelemetry instrumentation for HTTP clients and servers reads and writes it, so you don't have to.

## 

Here is the checkout again with [Pydantic Logfire](https://pydantic.dev/logfire). Each function is a span, created with [`@logfire.instrument`](https://pydantic.dev/docs/logfire/instrument/python/add-manual-tracing/#convenient-function-spans-with-logfireinstrument). To run it, install Logfire with `pip install logfire` and authenticate with `logfire auth`, as the [getting started guide](https://pydantic.dev/docs/logfire/get-started/) describes:

```
import asyncio
import random
import logfire
logfire.configure(service_name="checkout")
@logfire.instrument("fetch cart")
async def fetch_cart(user_id: int) -> list[str]:
    await asyncio.sleep(random.uniform(0.05, 0.1))
    return ["book", "mug"]
@logfire.instrument("fetch discounts")
async def fetch_discounts(user_id: int) -> float:
    await asyncio.sleep(2.0 if user_id == 2 else random.uniform(0.05, 0.1))
    return 0.1
@logfire.instrument("charge")
async def charge(user_id: int, items: list[str], discount: float) -> None:
    await asyncio.sleep(random.uniform(0.1, 0.2))
@logfire.instrument("checkout {user_id=}")
async def checkout(user_id: int) -> None:
    items, discount = await asyncio.gather(fetch_cart(user_id), fetch_discounts(user_id))
    await charge(user_id, items, discount)
async def main() -> None:
    await asyncio.gather(*(checkout(user_id) for user_id in (1, 2, 3)))
asyncio.run(main())
```
There is no request ID, no filter, and no "started" line. Each checkout gets its own trace. These are the spans of the slow one. The last three are children of the `checkout` span:

| Span | Start | Duration | 
|---|---|---|
| checkout user\_id=2 | 0 ms | 2176 ms | 
| fetch cart | 0 ms | 69 ms | 
| fetch discounts | 1 ms | 2001 ms | 
| charge | 2002 ms | 174 ms | 

Logfire draws these as a waterfall, but the table already answers the question. `fetch cart` and `fetch discounts` ran in parallel, the discounts took 2001 ms, and `charge` started only after both finished. You didn't subtract anything.

## 

One slow request is a debugging session. The next question is usually "how often does this happen, and where?" With logs, you parse durations out of message strings. With spans, `duration` is a column.

Logfire stores completed spans in a `records` table you can query with [SQL](https://pydantic.dev/docs/logfire/reference/sql/):

```
SELECT
    span_name,
    count(*) AS calls,
    approx_percentile_cont(duration, 0.95) AS p95_seconds
FROM records
WHERE service_name = 'checkout' AND kind = 'span'
GROUP BY span_name
ORDER BY p95_seconds DESC
```
That gives you the p95 of every step in the checkout. Filter on `parent_span_id IS NULL` to get whole checkouts only, or group by `attributes->>'user_id'` to split them per user.

## 

Logs only contain what someone decided to log. If nobody logged the database query, it's a gap between two timestamps.

Instrumentation libraries create spans for code you didn't write. In Logfire that is one line per library:

```
logfire.instrument_fastapi(app)
logfire.instrument_httpx()
logfire.instrument_asyncpg()
```
Every request, outgoing HTTP call, and SQL query becomes a span with its duration and its parent. The HTTPX and FastAPI instrumentation also writes and reads the `traceparent` header, so a request that crosses three services is one trace.

## 

Traces don't replace logs. Some things are events, not operations: a cache miss, a retry decision, a validation warning. They have no duration, and a log line is the right shape for them.

What changes is that a log line inside a span gets the span's context. Send your standard library logs to Logfire with the [`LogfireLoggingHandler`](https://pydantic.dev/docs/logfire/integrations/logging/logging/):

```
import logging
import logfire
logfire.configure()
logging.basicConfig(handlers=[logfire.LogfireLoggingHandler()], level=logging.INFO)
logger = logging.getLogger("checkout")
with logfire.span("checkout {user_id=}", user_id=2):
    logger.info("discounts loaded")
```
`discounts loaded` is stored as a child of the `checkout` span, with the same trace ID. Your existing `logger.info` calls keep working, and each one now says which request it came from.

So, do you need traces if you have logs? If your logs already carry a request ID, an operation ID, the caller's operation ID, and start and end times, you have the data of a trace, stored as text. Spans carry the same fields in the OpenTelemetry format, which tracing backends read, and Logfire also lets you query them as [SQL columns](https://pydantic.dev/docs/logfire/reference/sql/).
