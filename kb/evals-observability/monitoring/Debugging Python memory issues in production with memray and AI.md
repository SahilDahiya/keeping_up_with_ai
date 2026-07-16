---
title: Debugging Python memory issues in production with memray and AI
kind: blog
topic: evals-observability
subtopic: monitoring
secondary_topics:
- product-engineering/case-studies
summary: Debugging recurring Kubernetes OOM kills on a production Python service using
  memray heap profiling plus AI-assisted analysis to trace the leak to specific request
  patterns.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/debugging-memory-with-memray-and-ai
author: Hasan Ramezani
published: '2026-03-20'
fetched: '2026-07-16T23:01:32Z'
classifier: claude
taxonomy_rev: 2
words: 1330
content_sha256: 500e6e9c41d0798bbf49671e9faed62b7ca1b2761c3ccd8476ebb31e26667278
---

# Debugging Python memory issues in production with memray and AI

Our backend service was getting killed. Not metaphorically. Kubernetes was sending OOM (Out of Memory) signals to our `crud-api` pods, and they were restarting several times a day. Memory usage spiked under certain request patterns, and the pods would hit their memory limits and get terminated.

The tricky part? We couldn't reproduce it locally. The problem only showed up under real production traffic, when users ran certain queries that returned large result sets.

This post walks through how we used [memray](https://github.com/bloomberg/memray), Bloomberg's memory profiler for Python, to attach to a live process in Kubernetes, identify the root cause (serializing oversized query results), and how Claude Code helped us quickly trace the problem through a large codebase and suggest a fix.


Memray is a memory profiler for Python, built by Bloomberg and open-sourced in 2022. Unlike most Python profilers that focus on CPU time, memray tracks every memory allocation made by your Python process, including allocations from C extensions and native libraries.

What makes it particularly useful for production debugging:

- **It can attach to a running process.**You don't need to restart your application with special flags or instrumentation. You connect to a live process, record for as long as you need, then detach.
- **It captures native (C/C++) allocations**in addition to Python-level allocations. This matters when the leak is in a compiled extension.
- **It generates rich reports.**Flamegraphs, tree views, summary tables, and statistics that make it straightforward to identify where memory is being allocated.
- **The overhead is manageable.**While you wouldn't leave it running permanently, attaching for a few minutes to capture a snapshot is practical even in production.

You can install it with pip:

```
pip install memray
```
For the full documentation, see [bloomberg.github.io/memray](https://bloomberg.github.io/memray/).


The typical workflow when your production Python process is eating memory looks like this:


First, identify the pod that's showing high memory usage and exec into it:

```
kubectl exec -it <pod-name> -n <namespace> -- /bin/bash
```

Once inside, find the PID of the Python process you want to profile:

```
ps aux | grep python
```
You'll typically see something like:

```
app    1    0.5  12.3  2048000  512000 ?  Ssl  08:00  1:23  python -m uvicorn main:app
```
The PID here is `1` (common in containers where the app is the entrypoint process).


This is the key step. Memray can attach to a running Python process without restarting it, using the `attach` command:

```
memray attach <PID> -o /tmp/memray-output.bin
```
Memray injects itself into the target process and starts recording all memory allocations. The process continues running normally while memray captures data in the background.

Let it run for a few minutes under normal traffic. The longer you record, the clearer the allocation patterns become.


Press `Ctrl+C` to stop recording (or memray will stop when you detach). Then generate a flamegraph:

```
memray flamegraph /tmp/memray-output.bin -o /tmp/memray-flamegraph.html
```
Or a summary table showing the top allocations:

```
memray summary /tmp/memray-output.bin
```
The summary output looks something like this:

```
📏 Total allocations:
   1,234,567 allocations
   512.34 MB total memory
📊 Top allocations by size:
   200.12 MB  app/services/query.py:87    (list.append)
    89.45 MB  app/serializers/response.py:45 (json.dumps)
    45.67 MB  lib/python3.11/json/encoder.py:204 (encode)
    ...
```

Use `kubectl cp` to pull the report files out of the pod:

```
kubectl cp <namespace>/<pod-name>:/tmp/memray-flamegraph.html ./memray-flamegraph.html
kubectl cp <namespace>/<pod-name>:/tmp/memray-output.bin ./memray-output.bin
```
Now you have the raw data locally and can generate different report types as needed:

```
memray tree memray-output.bin
memray stats memray-output.bin
```

At this point we had a memray report pointing at the general area of the problem. The flamegraph showed that a significant chunk of memory was being allocated in the query handling and serialization layers. The summary confirmed it: hundreds of megabytes were being consumed by `list.append` and `json.dumps` calls in our response serialization path.

In the past, this is where the slow part of debugging would begin. We'd open the flamegraph in a browser, study the call stacks, cross-reference them with the codebase, and manually walk through the code path trying to understand which specific queries were triggering the allocations, why the results were so large, and where the right place to fix it was. That process meant jumping between memray's output, the source code, git blame, and sometimes even production logs, piecing the story together frame by frame. It could easily take half a day or more.

This time, we tried something different. We opened the repository in Claude Code and gave it everything we had: the memray summary output, the top allocation sites, and a description of the symptoms.

The memray profile shows that the largest memory consumers are in our query result handling and response serialization. The top allocation sites are in our query service and response serialization layers. Memory spikes happen under certain requests and cause OOM kills. Can you trace the data flow and find what's going wrong?


Claude Code searched the codebase, followed the call chain from the API endpoint through the query service to the database client and back through serialization. It identified the problem within minutes: when a user sent a query, the `crud-api` fetched the full result set from the database service, loaded all rows into memory, and then serialized the entire response as JSON. There was no limit on the number of records returned or the total size of the response. A single query that matched millions of rows would cause the service to try to serialize all of them at once, spiking memory well past the pod's limits.

What previously required us to manually read flamegraphs, trace call stacks across files, and reason about data flow took Claude Code a few minutes. It could hold the memray output and the full codebase context simultaneously, connecting the allocation sites in the profiler to the actual query handling logic across multiple modules.

Claude Code didn't just diagnose the problem, it also generated the fix. It suggested two changes and produced the code for both:

- **Add a limit on the number of records**returned from the database query, with a sensible default and a maximum cap.
- **Add a size limit on the response payload**, so even if individual records are large, the total serialized response stays within bounds.


Here's the full debugging loop:

- **Detect**: Kubernetes alerts on high memory usage or OOM kills.
- **Attach**:- `kubectl exec`into the pod, use- `memray attach`to profile the live process.
- **Analyze**: Generate flamegraphs, summaries, and tree reports from the memray output.
- **Identify**: Use Claude Code to trace the allocation sites through the codebase and find the root cause.
- **Fix**: Apply the fix (in our case, adding query limits and response size caps), deploy, and verify memory stabilizes.

The combination of memray for precise memory profiling and AI for rapid codebase analysis turned what could have been a multi-day debugging session into something we resolved in an afternoon.


A few things we learned along the way:

- **Profile in production, not just staging.**Memory leaks often depend on real traffic patterns. A staging environment with synthetic data might never trigger the same code paths.
- **Record long enough.**A 30-second profile might not show the leak. We recorded for 5-10 minutes to get a clear picture of allocation trends.
- **Use**Before diving into flamegraphs, the stats summary gives you a quick read on where the bulk of allocations are happening.- `memray stats`first.
- **Always set limits on query results and response sizes.**Unbounded result sets are one of the most common causes of memory spikes in API services. Every query path should have a maximum row count and a response size cap.
- **Use AI to accelerate the "last mile."**The profiler tells you- *where*memory is being allocated. AI tools like Claude Code help you understand- *why*and- *how to fix it*, especially in large codebases where the allocation site and the root cause are several layers apart.

Memory debugging doesn't have to be painful. With the right tools and workflow, you can go from "the pods are crashing" to "here's the fix" in a single session.
