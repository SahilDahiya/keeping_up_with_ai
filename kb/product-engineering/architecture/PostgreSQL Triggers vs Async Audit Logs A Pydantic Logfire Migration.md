---
title: 'PostgreSQL Triggers vs Async Audit Logs: A Pydantic Logfire Migration'
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics:
- evals-observability/tracing
summary: Migrating Logfire's audit logging from synchronous PostgreSQL triggers to
  async event-based logs, covering reliability, write-path performance, and capturing
  who-did-what context without blocking the request.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/audit-logs-replace-database-triggers
author: Hasan Ramezani
published: '2026-05-05'
fetched: '2026-07-16T23:01:23Z'
classifier: claude
taxonomy_rev: 2
words: 1558
content_sha256: 1d37b8f8401a6f69f2262d2b982bc0afbf4fe4513c8fe9726050c384ce145219
---

# PostgreSQL Triggers vs Async Audit Logs: A Pydantic Logfire Migration

Audit logs are one of those features that seem simple until they aren't. Every change to a sensitive resource — a user, a project, an API key — needs to be recorded reliably, with full context about who did what and when. For [Logfire](https://pydantic.dev/logfire), our observability platform, we started with what felt like the obvious choice: PostgreSQL triggers. It worked well, until a routine migration turned into an incident.

This post walks through both approaches, the problems we hit, and why we ultimately moved audit logging from the database layer to the application layer with async processing via Redis.


When we first built audit logging for Logfire, database triggers felt like the natural fit. The appeal was clear:

- **Guaranteed coverage**— every INSERT, UPDATE, and DELETE on tracked tables would fire a trigger, regardless of which part of the application made the change.
- **Consistency**— the audit log entry and the data change happen in the same transaction. If the transaction rolls back, so does the audit record.
- **No application code changes**— adding audit logging to a new table was just a matter of creating a trigger.


We created a PL/pgSQL trigger function that ran after every INSERT, UPDATE, or DELETE on tracked tables. Each tracked table had three statement-level triggers — one for each operation — using `REFERENCING NEW/OLD TABLE` to access the changed rows.

The trigger function would compute a JSONB diff between the old and new row values, filter out noise (like `updated_at`-only changes), redact sensitive fields (like tokens), and insert a record into the `audit_logs` table.

The tricky part was context. Database triggers don't know who made a request or where it came from. To solve this, the application set a PostgreSQL session variable before each query — a `#`-delimited string containing the organization ID, user ID, project ID, IP address, source, API key ID, and OAuth client ID. The trigger function parsed this string to populate the audit record.

This was a nicely self-contained system. It worked well for normal operations. The problems appeared when we needed to do anything outside of normal operations.



As Logfire grew, we regularly needed to run data migrations that updated many rows at once. Every one of these migrations had to carefully disable and re-enable audit triggers around the bulk operation. Every engineer writing a migration had to remember this ritual, and forgetting meant one of two bad outcomes:

- **The migration hangs or times out.**Audit triggers fire for every row in a bulk update, each computing JSONB diffs and inserting a record. A migration touching thousands of rows would generate thousands of audit entries, making the migration take orders of magnitude longer than expected.
- **Audit log spam.**Even if the migration completes, you now have thousands of system-generated audit entries that don't represent real user actions, polluting the audit trail.


This wasn't hypothetical. We discovered the migration performance issue during an incident. A routine migration that should have completed in seconds ran for an unexpectedly long time in production. The trigger was firing for every row in a bulk update, each one computing JSONB diffs and inserting into the `audit_logs` table within the same transaction. The migration effectively turned into an audit log bulk-write operation.

After diagnosing the issue and adding the disable/enable trigger wrapper, we stepped back and asked: should we be doing this at the database level at all?


Database triggers operate with limited context. We had to pass request metadata through a session variable — a `#`-delimited string parsed in PL/pgSQL. This was fragile and hard to extend. Adding a new field meant updating the format string, the parser, and every call site.

Triggers also can't distinguish between a user action and a system operation. The `source` field helped, but it required the application to set it correctly before every query. And they have no concept of the broader request context — you can't easily log things like "this change was part of an API call to endpoint X" or track non-database events like logins.


PL/pgSQL is not a language most teams want to maintain complex business logic in. The audit trigger function grew to over 80 lines of procedural SQL with string parsing, JSONB manipulation, and conditional logic. Testing it required running against a real database, and debugging meant reading PostgreSQL logs rather than application traces.


We migrated audit logging out of the database and into the application layer over the course of several weeks, moving one table at a time. Each migration was a focused PR: "Move roles audit logs to application," "Move users audit logs to application," and so on — 15 PRs in total. Once all tables were migrated, we dropped the trigger functions entirely.


The new system uses a producer-consumer pattern with three components:

- **Producer**— when a service performs an auditable action, it serializes the audit record and pushes it onto a Redis list. The call returns immediately — no database write, no trigger overhead.
- **Queue**— a Redis list acts as a durable buffer between the application and the database.
- **Consumer**— a worker cron job runs every 30 seconds, pops up to 1,000 records from the queue, and batch-inserts them into PostgreSQL in a single transaction. If anything goes wrong, the records are pushed back onto the queue for retry.

```
API Request → Service → Redis RPUSH → Worker (every 30s) → PostgreSQL
```

**Context propagation** became straightforward. Instead of stuffing context into a PostgreSQL session variable and parsing it in PL/pgSQL, we use Python's `ContextVar` — set once by middleware and available throughout the request lifecycle. Adding a new context field is just adding a key to a dictionary.

**Sensitive data filtering** moved from SQL string matching to application code, where it's easier to write, test, and extend. We filter out tokens, passwords, and secrets before anything hits Redis.

**Audit coverage expanded** beyond just database operations. We can now log events like logins, logouts, and failed authentication attempts — things that don't involve a table mutation and were invisible to the trigger-based system.

**Migrations became simple again.** No more disable/enable trigger dance. Bulk data operations just run without worrying about audit log side effects.


| Database triggers | Application-level + Redis | |
|---|---|---|
| Coverage guarantee | Automatic — every SQL statement is captured | Manual — each service must call the audit function | 
| Performance impact | Synchronous, in the same transaction | Async, near-zero impact on request latency | 
| Migration compatibility | Must disable/enable triggers around bulk ops | No special handling needed | 
| Context richness | Limited to what fits in a session variable | Full access to request context, headers, etc. | 
| Event types | Only database operations | Can log logins, logouts, failed attempts, API calls | 
| Consistency | Same-transaction guarantee | Eventual (up to 30 seconds delay) | 
| Language/debugging | PL/pgSQL, tested via database | Python, unit-testable, observable with Logfire | 
| Failure mode | Audit failure can block the operation | Audit failure doesn't affect the user operation | 


The async approach does come with trade-offs that are worth acknowledging:

**Eventual consistency.** There's up to a 30-second window where a change has been made but the audit record hasn't been written yet. For most compliance and debugging use cases, this is fine. If you need real-time audit trails (e.g., for financial transactions), the trigger approach provides stronger guarantees.

**Manual instrumentation.** With triggers, every change is automatically captured. With the application-level approach, an engineer could add a new service endpoint that modifies a tracked table and forget to add the audit call. We mitigate this through code review and by making the audit call part of our service patterns, but it's a real risk.

**Redis as a dependency.** We now depend on Redis being available for audit logging. If Redis goes down, audit entries are lost until it recovers. In practice, Redis is already a critical dependency in our stack, so this doesn't change our operational requirements.


**Start with the simplest approach, but know when to move on.** Database triggers were the right choice when we had a handful of tables and no bulk migrations. They let us ship audit logging quickly with near-zero application code. But as the system grew, the friction compounded.

**Incidents reveal assumptions.** We assumed migrations would be fast because the SQL was simple. We didn't account for the trigger overhead on bulk operations. It took a production incident to make this visible.

**Migrate incrementally.** We moved one table at a time over several weeks. Each PR was small, focused, and independently deployable. At no point did we have a "big bang" migration that could have caused widespread issues.

**Audit logging is business logic.** It might feel like infrastructure, but the decisions about what to log, when to filter sensitive data, and how to handle edge cases are all business concerns. Keeping this logic in the application where it can be tested, traced, and evolved alongside the rest of the codebase has been a clear win.

If you're building audit logging and your system is simple — a few tables, no bulk operations, no async requirements — triggers are a fine choice. But if you see yourself writing `DISABLE TRIGGER` in migration scripts, that's the signal to start planning the move to the application layer.
