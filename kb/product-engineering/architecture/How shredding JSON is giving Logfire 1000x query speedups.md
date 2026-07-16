---
title: How shredding JSON is giving Logfire 1000x query speedups
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- inference/optimization
summary: How Logfire 'shreds' nested JSON attributes into typed columns in its columnar
  store for up to 1000x query speedups—turning 30s-timeout queries into sub-second—covering
  schema inference and dynamic column materialization.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/dynamic-shredding-2026-01-26
author: Adrian Garcia Badaracco
published: '2026-01-26'
fetched: '2026-07-16T23:01:38Z'
classifier: claude
taxonomy_rev: 2
words: 2968
content_sha256: cd4eedc62e6dd058e0b6085f0bacaff60843321b1318c416254a981273b1707d
---

# How shredding JSON is giving Logfire 1000x query speedups

Querying data in Logfire is about to get dramatically faster. Consider >1,000 times faster in some cases. Queries that previously timed out after 30 seconds now complete in under a second.

"Seeing much faster <customer_attribute> query times! Feels basically instant now", says an early access customer


This technical blog post details how we achieved this through dynamic shredding, an optimization for querying semi-structured attributes data. We'll begin to roll out this feature to all customers in February 2026.


OpenTelemetry data (the data that Logfire ingests) is semi-structured data. It contains a mix of:

- Fixed schema fields (timestamp, span name, etc.)
- Semi-structured attributes (HTTP status codes, user IDs, regions, etc.)

Semi-structured data is sent via `attributes` (per-span key-value pairs) or resource attributes (`otel_resource_attributes` in Logfire; these are per-resource key-value pairs where a resource is a service/k8s pod/etc, essentially an instance of your application or service).

When you write code like:

```
app = FastAPI()
@app.get('/user/{user_id}')
async def handle_request(user_id: str) -> dict[str, str]:
  with logfire.span(f'handle_request for user {user_id}', user_id=user_id):
    return {"user_id": user_id}
```
This generates an export along the lines of:

```
{
  "resource": {
    "attributes": {
      "service.name": "my-web-service",
      "region": "us-west-2"
    }
  },
  "spans": [
    // Manual span created by user code
    {
      "span_name": "handle_request for user user123",
      "start_time": "2024-01-01T12:00:00Z",
      "end_timestamp": "2024-01-01T12:00:01Z",
      "message": "handle_request for user user123",
      "trace_id": "0194c7b1e5f4a3b2c1d0e6f7a8b9c0d1",
      "span_id": "abcdef1234567890",
      "parent_span_id": "1234567890abcdef",
      "attributes": {
        "user_id": "user123",
        "http.status_code": 200,
      },
    },
    // Automatic span created by OpenTelemetry FastAPI instrumentation
    {
      "span_name": "GET /user/{user_id}",
      "start_time": "2024-01-01T12:00:00Z",
      "end_timestamp": "2024-01-01T12:00:01Z",
      "message": "GET /user/user123",
      "trace_id": "0194c7b1e5f4a3b2c1d0e6f7a8b9c0d1",
      "span_id": "1234567890abcdef",
      "parent_span_id": null,
      "attributes": {
        "http.method": "GET",
        "http.response": 200,
      },
    }
  ]
}
```
I'm using JSON here for illustration, although we support various wire formats (OTLP protobuf, JSON, etc.); most data is sent as protobuf over gRPC. There are also some details like timestamps being represented as integers (epoch nanos) rather than ISO strings and an extra level of nesting from scopes that I've omitted for clarity.

A couple of things to note here:

- Some fields like `start_timestamp`,`end_timestamp`,`span_name`, and`message`are fixed-schema fields that exist for every span and are strongly typed.
- Attributes are semi-structured and can vary widely between spans.
Some attributes like `http.status_code`and`http.method`are common and have semantic meaning in the OpenTelemetry spec, while others like`user_id`are application-specific and could be an integer in some places and a string in others.

We ultimately store this data as Parquet files in object storage, with a columnar schema roughly like:

```
start_timestamp: Timestamp(Microsecond, "+00:00")
end_timestamp: Timestamp(Microsecond, "+00:00")
span_name: Utf8View
message: Utf8View
trace_id: FixedSizeBinary(16)
span_id: FixedSizeBinary(8)
parent_span_id: FixedSizeBinary(8)
attributes: Utf8View (JSON)
otel_resource_attributes: Utf8View (JSON)
```
Some background on columnar storage, Parquet and zone map pruning is beneficial to understand the rest of this blog post. I recommend reading [MotherDuck's excellent overview of the topic](https://motherduck.com/learn-more/columnar-storage-guide/).


Pydantic started as a library to validate and parse JSON data efficiently.
When we built Logfire, we initially stored all attributes as JSON blobs in a single column and relied on [Jiter](https://github.com/pydantic/jiter) (one of the fastest JSON parsers out there in any language) to rip through the JSON data as quickly as possible.
This is the layout detailed above (`attributes: Utf8View (JSON)`).

This approach was simple but made a fundamental mistake: we were optimizing to do work faster, but we couldn't really avoid doing the work. Compression is also suboptimal since a single varying attribute makes Parquet level dictionary compression ineffective and even zstd struggles with highly variable data, all the JSON syntax overhead, etc.

The biggest problem really ends up being extra IO: since most of our data is stored on object storage, extra IO from downloading large JSON blobs, and especially the latency of starting these downloads, ends up dominating query runtimes much more so than any CPU work.


To make queries fast, we need to avoid unnecessary work. For normal columns DataFusion / Parquet avoid unnecessary work by using columnar storage (allowing reading only the columns you need) and zone maps / min-max statistics (allowing skipping entire row groups or pages that don't match your filter predicates).

So when you write a query like:

```
SELECT count(*) FROM records WHERE duration < 0;
```
The system can efficiently read just the `duration` column and skip row groups where the max duration is < 0 based on the stored statistics.
In this case this is a valid query, duration is a f64 so in theory it could have values <0.
In practice though duration is always >= 0 so this query will be very fast: based on statistics we know no rows match and we can return 0 immediately.

So how can we enable this for semi-structured data like attributes stored as JSON?

Our initial solution was *static shredding*: we manually picked a small set of commonly queried attributes
(like `http.status_code`, `http.method`, etc.) and extracted these into their own strongly typed columns during ingestion.

So when we receive:

| attributes | 
|---|
| {'http.response.status_code': 200, 'url.full': 'https://example.com?foo=bar'} | 
| {'my_llm_response': 'large text'} | 
| {'user_id': '123'} | 

Assuming our hardcoded shredding configuration extracts `http.response.status_code`, `url.path`, and `db.query.text`, we would store:

| _lf_attributes | _lf_attributes_http.response.status_code | _lf_attributes_url.path | _lf_attributes_db.query.text | 
|---|---|---|---|
| null | 200 | https://example.com?foo=bar | null | 
| {'my_llm_response': 'large text'} | null | null | null | 
| {'user_id': '123'} | null | null | null | 

Now we can run queries like:

```
SELECT count(*) FROM records WHERE _lf_attributes_http.response.status_code = 500;
```
We can use statistics to prune files / row groups / pages that don't match,
and then scan just the `_lf_attributes_http.response.status_code` column which is strongly typed (int64) and compresses well.

Of course you as a user don't have to use the `_lf_attributes_http.response.status_code` column directly, you can write:

```
SELECT count(*) FROM records WHERE attributes->'http.response.status_code' = 500;
```
And we rewrite this under the hood to use the shredded column.

I thought it worth mentioning the `_lf_attributes` prefix: one of the challenges with the current static shredding approach
is that these columns are user-visible, e.g. if you run `select * from records limit 10` you'll see these columns.
Since these are an internal implementation detail, we'd rather not leak them to you.
We want to keep the logical layout of `attributes` as a single JSON column from your perspective,
while optimizing the physical layout under the hood.


There are several issues with this scheme:

- **Limited Flexibility**: Only a small, hardcoded set of attributes are shredded. If users want to query other attributes (e.g.,- `user_id`,- `session_id`,- `region`), they pay the full cost of JSON storage and parsing. Queries on these attributes can get slow on projects with 100s of GBs of data. We can't easily add new shredded attributes without code changes and deployments. This is particularly painful with indexing; we only have indexes on the hardcoded set of shredded attributes.
- **High Cost for Unshredded Attributes**: Queries that filter on unshredded attributes (e.g.,- `attributes->>'user_id' = 'user123'`) require scanning the entire JSON column, leading to high I/O, poor compression, and expensive JSON parsing. This results in slow queries and high resource usage. Since data is stored in chunks, even a single large unshredded attribute can bloat the entire column, making all queries expensive even if they are not touching that attribute.
- **User-visible columns**: The shredded columns are visible to users, leading to confusion and clutter in query results. Users may not understand the purpose of these internal columns, and they can complicate query writing and result interpretation.
- **Overheads**: As you can see, there are several columns that may be all- `null`s (e.g. if the application doesn't do DB queries, the- `_lf_attributes_db.query.text`column is always null). Although Parquet / Arrow / DataFusion are quite efficient at handling nulls, there is still some overhead in storage and processing for these unused columns.

Every query touching `attributes` that isn't filtering on the small hardcoded set of shredded attributes pays these costs.

For example, consider the query:

```
SELECT * FROM events WHERE attributes->>'my_llm_response' like '%important%';
```
This query needs to scan the entire `attributes` JSON column since `my_llm_response` is not shredded.
Even though `my_llm_response` is a large attribute it may be a *rare* attribute that only appears in a small fraction of rows.
Think about it this way: you probably have many more spans that don't involve LLM calls than ones that do, even in an agentic application.

```
┌─────────────────────────────────────────┐
│  Cost 1: Download Entire _lf_attributes │
│  (could be GBs of data)                 │
└─────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│  Cost 2: Poor Compression                │
│  Variable structure → zstd 10% efficiency│
└──────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Cost 3: JSON Parsing                   │
│  Jiter does lazy parsing, worst case    │
│  must parse entire row.                 │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Cost 4: In-Memory Operations           │
│  Create copies of extracted values      │
│  Do comparisons in memory               │
└─────────────────────────────────────────┘
```
**The Result**: this query has to parse and scan potentially GBs of JSON data, much of which is irrelevant to the query, just to get the few rows that contain `my_llm_response`.

Or consider the query:

```
SELECT * FROM events WHERE attributes->>'user_id' = 'user123';
```
This query now has the opposite problem: even if 1/3 of rows contain a `user_id` attribute, we have to scan the entire JSON column to find them,
which includes those large `my_llm_response` attributes that bloat the column size.


Rather than storing all attributes in a single JSON column, we automatically extract the **most frequently accessed attributes** into separate, strongly typed columns.
This happens automatically during data ingestion and compaction—no configuration needed.

Let's compare the physical layout of data before and after dynamic shredding.

**Before (Current)**:

| _lf_attributes | _lf_attributes_http.response.status_code | _lf_attributes_url.path | _lf_attributes_db.query.text | 
|---|---|---|---|
| null | 200 | https://example.com?foo=bar | null | 
| {'my_llm_response': 'large text'} | null | null | null | 
| {'user_id': '123'} | null | null | null | 

**After (With Dynamic Shredding)**:

| _lf_attributes | _lf_attributes_http.response.status_code | _lf_attributes_url.path | _lf_attributes_my_llm_response | _lf_attributes_user_id | 
|---|---|---|---|---|
| null | 200 | https://example.com?foo=bar | null | null | 
| null | null | null | large text | null | 
| null | null | null | null | 123 | 

This layout is generated dynamically for each Parquet file we write out based on the actual data we see. We don't have to include all null columns and we can prioritize shredding the most frequently seen or largest attributes.

Now when the query above runs:

```
SELECT * FROM events WHERE attributes->>'my_llm_response' like '%important%';
```
It can efficiently scan just the `_lf_attributes_my_llm_response` column:

```
┌─────────────────────────────────────────┐
│  Benefit 1: Index pruning               │
│  Zone maps and full text search indexes │
│  let us skip entire files / row groups  │
└─────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│  Benefit 2: Download Only Relevant Column│
│  (_lf_attributes_my_llm_response)        │
└──────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Benefit 3: Better Compression          │
│  English text string data               │
│  via zstd + dictionary encoding         │
│  Maybe FastLanes in future?             │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Benefit 4: Zero JSON Parsing           │
│  Data already extracted & typed         │
│  No deserialization, zero copy into mem │
└─────────────────────────────────────────┘
```
This query now benefits from the full efficiency of progressive narrowing / pruning and columnar storage.
It is as fast as if `my_llm_response` were a first-class column in the schema.


We've been working on this feature for nearly 6 months now.
It's required a lot of upstream changes in DataFusion to enable expression pushdown and predicate pushdown for JSON accessors.
This is the blessing and the curse of working with an upstream open source project: we get to build on a solid foundation, but we also have to wait for upstream changes to land and get released.
We've worked on this feature in a way that benefits not only us but anyone using DataFusion with semi-structured or nested data, including Parquet/Arrow struct columns and the newly introduced [Json Variant type](https://parquet.apache.org/docs/file-format/types/variantencoding/).

We've had to refactor core parts of the DataFusion execution engine to push down expressions into the Parquet reader so that it can use the physical file layout to optimize expression evaluation (in our case to decide if we need to read from the `_lf_attributes` remainder column or if there is a shredded column we can use instead).
This work is done and has fully landed as of DataFusion 52.1.0 (Jan 2026).

The remaining work involves actually getting these expressions into the scan operators, e.g. for cases like:

```
SELECT attributes->>'http.response.status_code', count(*)
FROM records
GROUP BY attributes->>'http.response.status_code';
```
Pulling out the `attributes->>'http.response.status_code'` expression from the GROUP BY clause and pushing it down into the Parquet scan so that we can use the shredded column directly is a bit tricky, and involves complex expression rewriting and optimization passes, but we expect to land this work in DataFusion by Feb 2026.
The upshot of this is that we've been able to contribute major improvements to DataFusion that benefit a broad community of users.


Our plan to land this while minimizing bugs and breakage for users is to first rewrite our query path (non-destructive, most of this has already been done) to use dynamic shredding but keep the static shredding in the write path. Along with this change we'll eliminate and isolate all notion of hardcoded shredded columns from the codebase into a self-contained section of the write path. Essentially our initial heuristic for dynamic shredding will mimic the current static shredding configuration. This lets us test out the vast majority of these changes without making any irreversible changes (like writing out a new physical layout).

Once we have confidence that the dynamic shredding query path is solid, we can flip the switch in the write path to enable dynamic shredding using the discovery algorithm.


Analysis of our production data has shown that 99% of our existing Parquet files have fewer than 128 unique top-level keys in the `attributes` JSON column.
The P50 is closer to 32 unique keys.

We've thus chosen a default of extracting the top 128 largest (by total size across all rows) keys from each JSON column during ingestion/compaction.

This automatic discovery approach balances the tradeoff between:

- Extracting enough attributes to cover common query patterns and maximize performance benefits
- Avoiding excessive column proliferation and overhead from shredding too many attributes

For example, if you accidentally start sending logs like `logfire.span('foo', **{uuid.uuid4(): 'some value' for _ in range(1000)})`, we don't want to shred all 1000 dynamically generated keys.
This algorithm is robust to even such pathological cases because it will shred the non-unique keys that dominate the data while putting the rest of the "accidental" dynamically generated keys into the reduced JSON column.
Queries against these rare keys will still work, just with the usual JSON parsing overhead.
Queries against the rest of the data will remain fast.

Having a hard cap on the number of shredded columns lets us have a controlled overhead in terms of Parquet column count which avoids bloating the schema and incurring excessive overheads in parsing of Parquet metadata. Our empirical measurements shows that ~ 1000 columns is not a problem for Parquet / DataFusion, but more than that and you start to see a noticeable performance overhead.


As we discover which attributes to shred, we also need to determine the data type for each shredded column.
We do this by keeping track of the current planned output data type for each candidate attribute as we scan through the data and widening the type as needed.
The basic rule is `Int` -> `Float` -> `JSON`, `Bool` -> `JSON` and `String` -> `JSON`.
There is an important distinction between `String` and `JSON`.
Consider the values `[{"user_id": "123"}, {"user_id": 456}]`.
In this case we would store the data as JSON which practically speaking is a `Utf8View` column containing JSON strings: [`"123"`, `456`].
This means JSON parsing is still needed to read from this column but we still benefit from columnar storage, compression, and to some extent pruning.
If on the other hand we have `["123", "456"]` we can store this as a `Utf8View` column directly without JSON parsing: [`123`, `456`].



Our shredded data layout predates both the Parquet Variant type and [ClickHouse's JSON support](https://clickhouse.com/blog/a-new-powerful-json-data-type-for-clickhouse)
but is very similar to these approaches.

Our long term plan is to adopt the Parquet Variant type for storing the remaining unshredded attributes, which will give us essentially the same architecture but using an industry standard data layout that other query engines can also read and write, and moving complexity from our code to DataFusion / Parquet itself.

The DataFusion community (us included) is still working through some of the details of the Parquet Variant type. Namely we need to incorporate the variant UDFs into DataFusion and need to add support for statistics of nested struct types to enable pruning.


We will initially have basic support for zone map pruning on shredded columns, but in the future we would like to add more index types like:

- Inverted indexes for text columns to speed up `LIKE`and full-text search queries, e.g. so you can quickly filter LLM responses for keywords.
- Bloom filters for high-cardinality columns to speed up equality filters.


Our initial approach will be to shred based on attribute size/frequency in the data.
This lets us self-contain the heuristic within the write path for each Parquet file.
In the future we may want to incorporate query usage patterns into the shredding decision.
For example if we see that `user_id` is frequently queried but is not a large attribute, we may want to shred it anyway.
This would require tracking query patterns over time and feeding this back into the ingestion/compaction pipeline.
We would also use this approach to decide what indexing strategies to pursue for each shredded column.


In the next few months you'll probably see your Logfire queries get orders of magnitude faster.
You don't need to do anything on your end, just continue to use [Logfire](https://pydantic.dev/logfire?utm_source=adrian_blogpost) as you currently do!
