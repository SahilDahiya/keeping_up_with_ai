---
title: adb Benchmarks
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/monitoring
summary: Benchmarks Arize database performance at the storage and application level
  for AI observability workloads powered by high-volume traces and model data.
source: arize
url: https://arize.com/blog/adb-benchmarks/
author: Jason Lopatecki
published: '2025-09-17'
fetched: '2026-07-11T04:53:18Z'
classifier: codex
taxonomy_rev: 1
words: 334
content_sha256: d9ddf5bd0b0df8c090985ce05b4502528c10c926780ddd6ae53011e6b5316367
---

# adb Benchmarks

In launching [adb (Arize database)](https://arize.com/blog/introducing-adb-arizes-proprietary-olap-database/) we wanted to benchmark adb both internally as a database and at the system level in our application. Our goal is to show both the performance of the database that powers the application and the end application delivered user experience.

The benchmark tests cover these areas:

- Dataset Upload Programmatic
- Dataset Upload UI
- Trace Upload Programmatic
- Real Time Ingest to Read Time
- Search Over Large Data

The end application was tested under the following scenarios and we expect similar experiences under similar conditions:

- Internet connection speed test: 150MB Down / 150MB Upload
- MAC

## Dataset Upload

The dataset upload tests how fast adb can upload and make available a large batch of data.


![Dataset Upload](https://arize.com/wp-content/uploads/2025/09/Dataset-Upload-2.jpg)

**Dataset upload**

The above shows a diagram of the dataset upload, a CSV or dataframe is uploaded into adb. The test shows how fast a large file can be uploaded into adb. The file upload uses a batch insertion datapath in adb that is designed for extremely fast ingestion of large files.

## Trace Ingestion

The trace ingestion tests show how quickly adb can make individual realtime events available in the UI.

![Trace Ingestion](https://arize.com/wp-content/uploads/2025/09/Trace-Ingestion-4.jpg)


**Trace Insertion**

The trace insertion path utilizes the realtime ingestion path of adb going from event to user interface with subsecond timing.

## Full Text Search

Full text search tests the ability to run search across a large number of spans with large chat text input and output attributes.

![Full Text Search](https://arize.com/wp-content/uploads/2025/09/Full-Text-Search-2.jpg)


**Full Text Search**

Spans are ingested in adb with 25KB chat text strings in each span across two tests of 5M and 10M spans each. Full text search shows the search timing for regexp search across the data.

![adb benchmarks](https://arize.com/wp-content/uploads/2025/09/adb-benchmarks-4.png)

Want to understand how adb achieves these numbers? Read our [introduction to adb](https://arize.com/blog/introducing-adb-arizes-proprietary-olap-database/) to see the architecture decisions that enable petabyte-scale performance with sub-second latency.

Give adb a spin by [signing up for Arize AX](https://app.arize.com/auth/join) and let us know what you think.
