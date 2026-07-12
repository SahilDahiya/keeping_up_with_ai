---
title: How Cresta Scales Real-Time Insights with ClickHouse
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/monitoring
summary: Architecture case study on scaling real-time AI insights with ClickHouse
  for high-volume conversation analytics.
source: cresta
url: https://cresta.com/blog/how-cresta-scales-real-time-insights-with-clickhouse
author: Xiaoyi Ge
published: '2025-01-28'
fetched: '2026-07-11T03:58:53Z'
classifier: codex
taxonomy_rev: 1
words: 1226
content_sha256: b2e7562a36686aa250838e0ce78629672bf4d5b8e5f844ffaed40b6870a373a0
---

# How Cresta Scales Real-Time Insights with ClickHouse

## Introduction

As enterprises scale, the ability to analyze massive datasets in real-time becomes a cornerstone of decision-making. At Cresta, ensuring our contact center clients have access to accurate and actionable insights led us to adopt ClickHouse, a high-performance data warehouse. This article explores the challenges we faced and how we leveraged ClickHouse to meet the demands of our growing customer base.

## Background

At Cresta, we empower contact centers with actionable insights through the Cresta Director UI (e.g., Performance Insights and Leaderboard, as screenshots as shown below), which fetches, filters, and aggregates raw data (e.g., events, annotations) in real-time. This capability supports flexible usage patterns, even when raw data volumes exceed tens of millions of records per day for some of our largest enterprise customers. Customers can query data across virtually unlimited time ranges, such as weekly aggregates spanning six months, resulting in billions of records. Aggregating these large-scale datasets in a responsive and flexible manner posed a significant technical challenge.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138a380d01dbc2343867ec_Screenshot-2025-01-16-at-3.18.42%25E2%2580%25AFPM-1024x1019.avif)

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138a510db13e25f3cbfcdb_Screenshot-2025-01-16-at-3.avif)

Previously we addressed these needs by pre-aggregating data via cron jobs into an AWS-managed PostgreSQL database. While effective initially, this approach became unsustainable as Cresta’s customer base and data volume grew exponentially. Several critical issues emerged:

#### Infrastructure Cost

Hourly cron jobs pre-aggregating rapidly growing datasets led to rapidly rising AWS PostgreSQL compute costs. By migrating to a self-managed data warehouse on AWS Elastic Block Store (EBS) disks, compute costs became negligible, limited to machine expenses, while storage costs dropped by nearly 50%.

#### Scalability

Supporting larger enterprise customers pushed our PostgreSQL-based solution to its limits. With raw data volumes reaching tens of millions of records per day, pre-aggregation queries (involving data across tens of tables) became increasingly slower, sometimes exceeding the scheduled cron job interval. Even aggregated tables, query performance struggled due to the complexity of our operations, which involved intricate aggregations such as computing set unions across large conversation datasets. This required creating the creation of numerous database indexes tailored to specific query patterns—a cumbersome and unsustainable practice.

#### Real-Time Aggregation Performance

ClickHouse offered the blazing-fast query performance required for real-time aggregation. Designed for speed, as detailed in [why ClickHouse is so fast](https://clickhouse.com/docs/en/concepts/why-clickhouse-is-so-fast), it handles our query patterns and data sizes with ease. By employing proper table schemas and settings, ClickHouse enables direct aggregation of raw data. For future scaling, we can leverage auto-updated materialized views to further enhance query performance, as described in[ supercharging your ClickHouse queries](https://clickhouse.com/blog/clickhouse-faster-queries-with-projections-and-primary-indexes).

#### Extensibility

Deploying ClickHouse within Kubernetes clusters allows us to extend its capabilities for various use cases. Today, we operate three dedicated ClickHouse clusters for:

- Real-time data aggregation
- Raw event storage and preprocessing
- Internal observability

After evaluating solutions such as AWS Redshift, Google BigQuery, and Snowflake, we chose ClickHouse for its cost-effectiveness, scalability, extensibility, and high performance. This open-source, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP) has proven to be the ideal foundation for Cresta’s rapidly evolving data needs.

## System Architecture Overview

At Cresta, the ClickHouse deployment supports multiple clusters optimized for different data types and use cases. Below, we detail the architectures of the `conversations` and `events` clusters, highlighting their data flow and purpose.

#### Conversations Cluster

The `conversations` cluster processes conversational data, including conversations, messages, AI-based annotations, agent performance scores, and more. These datasets are stored in a PostgreSQL database, which serves as the source of truth for ClickHouse. Data is indexed into ClickHouse through three primary paths:

- **Live Conversations:**Real-time ingestion of ongoing conversation data.
- **Batch Importing Conversations:**Periodic batch importing conversation data for those without live paths.
- **Reindexing or Backfilling Jobs:**Idempotent jobs to ensure consistency and handle updates.

Once the data resides in ClickHouse, Cresta Insights server APIs fetch, filter, and aggregate it to power the [Cresta Director](https://cresta.com/videos/cresta-director-real-time-visibility-for-managers/), the intuitive UI where customers can explore actionable insights and real-time analytics to drive decision-making and optimize performance.

![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138a388c678240b50815ff_ClickHouse-conversations-cluster-1-1024x302.avif)

#### Events Cluster

The `events` cluster handles multiple categories of event data, stored in separate ClickHouse tables optimized for their specific purposes:

- **Analytics Events:**- Flexible schema with a short lifecycle.
- Primarily used for internal monitoring.

- **Conversation Events:**- Well-defined schema with long lifecycle and high SLA.
- Used in public-facing production APIs.

- **Session Logs:**- Tracks user interactions, such as page visits and button clicks.

- **User Events:**- Captures authentication-related data, such as agent login events.


![](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138a370d01dbc2343867e6_ClickHouse-events-cluster-1024x446.avif)

## Challenges and Best Practices

While ClickHouse has been instrumental in addressing Cresta’s data scalability and performance needs, we encountered several challenges during its implementation and optimization. Below, we detail three key challenges and how we approached them.

#### Optimizing Query Perfomance

ClickHouse is known for its high-speed query execution, but achieving optimal performance required deliberate effort:

- **Schema Design:**Poorly designed schemas can result in slow queries and increased resource consumption. We carefully structured our tables to align with our query patterns, focusing on column compression, appropriate primary keys, and clustering keys to minimize disk I/O.
- **Materialized Views:**For frequently accessed aggregated data, we leveraged materialized views to precompute and store results, reducing the load on raw data queries.
- **Indexing Strategies:**We experimented with ClickHouse’s primary and secondary indexing mechanisms, such as sparse and bloom filters, to accelerate specific queries.
- **Query Profiling:**Tools like `EXPLAIN` and `SYSTEM` queries in ClickHouse helped identify bottlenecks, allowing us to iteratively refine query structures and configurations.

By carefully optimizing these aspects, we significantly improved the query performance across our clusters, ensuring fast, reliable access to aggregated data.

#### Deduplicating Data

Given the multiple ingestion paths into ClickHouse (`live`, `batch`, and `reindexing`), data deduplication became a critical concern to maintain data integrity:

- **Deduplication Keys:**We used unique identifiers (e.g., message IDs or conversation IDs) to detect and remove duplicate records during ingestion.
- **Replacing MergeTree:**ClickHouse’s `ReplacingMergeTree` table engine provided a robust mechanism for handling duplicates by replacing older rows with the most recent ones based on a defined version column.
- **Handling Edge Cases:**For certain datasets where deduplication logic was more complex (e.g., detecting partial updates), we implemented pre-ingestion validation scripts to filter redundant records.

This approach ensured data integrity across all ingestion paths, even in complex and dynamic data environments.

#### Joining Tables Flexibly

Joining large tables in ClickHouse can be challenging due to its columnar nature, which isn’t inherently optimized for complex joins:

- **Denormalized Schemas:**To avoid expensive joins, we adopted denormalized schemas for commonly queried data, trading storage efficiency for improved query performance.
- **Sub-Table Generation for Joins:**Recognizing the limitations of direct joins on raw data, we preprocess datasets to create sub-tables optimized for specific join operations. These sub-tables are structured with precomputed fields and streamlined schemas, significantly improving join efficiency across tables.
- **Distributed Joins:**For large-scale joins, we leveraged ClickHouse’s distributed table setup, ensuring queries were parallelized across nodes for better performance.
- **Join Optimization:**Where joins were unavoidable, we focused on optimizing join keys, ensuring that both sides of the join were sorted and indexed appropriately.

By employing these strategies, we were able to flexibly join tables while maintaining query performance and scalability.

## Conclusion and Future Work

Using ClickHouse, Cresta has made its data architecture more scalable and cost-effective while enabling real-time analytics. We’ve tackled challenges like query performance, data deduplication, and flexible joins to build a platform ready for large enterprise customers. As we onboard larger future customers, we’ll focus on improving query performance, exploring advanced ClickHouse features, and enhancing platform flexibility.
