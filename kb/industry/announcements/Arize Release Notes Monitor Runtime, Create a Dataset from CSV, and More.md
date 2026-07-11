---
title: 'Arize Release Notes: Monitor Runtime, Create a Dataset from CSV, and More'
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/monitoring
summary: Arize release notes covering monitor runtime, dataset creation from CSV,
  and related product updates.
source: arize
url: https://arize.com/blog/arize-release-notes-feb-14/
author: Sarah Welsh
published: '2025-02-14'
fetched: '2026-07-11T04:51:31Z'
classifier: codex
taxonomy_rev: 1
words: 426
content_sha256: 86c685b15268d9fd66612853a8afbfeb78d99493b117db6da2f0d2b897666d8f
---

# Arize Release Notes: Monitor Runtime, Create a Dataset from CSV, and More

![Release notes Feb 14 Text reads: Release Notes, February 14, 2025](https://arize.com/wp-content/uploads/2025/02/Release-notes-Feb-14-1021x560.jpg)

              # Arize Release Notes: Monitor Runtime, Create a Dataset from CSV, and More

## Enhancements

### Monitor Runtime

Users can now schedule when monitors run. Users can configure their monitors to run:

- Hourly & Daily: Select specific days of the week.
- Daily, Weekly & Monthly: Runs at 12 AM UTC after creation.
- Default Behavior: Monitors will continue running every 3 hours, 7 days a week unless configured otherwise.

![Screenshot of what it looks like to schedule when monitors run in Arize](https://arize.com/wp-content/uploads/2025/02/Define-the-Alerting.png)


## Column Specification With Exporting Data

Users can now export only the columns they care about for large datasets, reducing SDK export time by up to 95%.

- Specify which columns of data you’d like to export when exporting data via the [ArizeExportClient](https://arize-client-python.readthedocs.io/en/latest/llm-api/exporter.html)
- When using the `export_model_to_df`function, users can specify the`columns`parameter to only export specific columns.

![Screenshot of Export to notebook](https://arize.com/wp-content/uploads/2025/02/Export-to-notebook-1024x838.png)


## Create a Dataset from CSV

Users can now upload CSVs as a dataset in Arize. Columns in the file will be attributes that users can access in Experiments or in Prompt Playground. [Learn more here](https://docs.arize.com/arize/llm-datasets-and-experiments/how-to-datasets/create-a-dataset-from-csv).

![Screenshot of how you can upload a dataset via csv in Arize.](https://arize.com/wp-content/uploads/2025/02/Create-dataset-from-CSV.png)


## Monitor Improvements

We’ve made some updates to make monitors more organized, searchable, and user-friendly. Here’s what’s new:

- Cardless Design – A sleek, modern table view for better readability.
- Project-Level Monitors – LLM and ML monitors now have separate tabs.
- Search & Sort – Find monitors by name or dimension, plus sort by any column.
- Summary Stats – See how many monitors triggered in the last 24 hours
- New LLM Monitor Types – Clearer categories:
- Custom Metric Monitor → Performance Monitor with a custom metric preselected.
- Span Property Monitor → Data Quality Monitor for span properties.
- Evaluation Monitor → Data Quality Monitor for evaluations.
- Quick Monitor for Errors – Easily enable error count monitoring (count, status_code = ERROR).


![](https://arize.com/wp-content/uploads/2025/02/Screenshot-2025-02-19-at-2.33.54 PM.png)



## OTEL Tracing Via HTTP

We’ve added support for HTTP protocol when sending traces to Arize through an OTEL tracer.

To use: Specify `/v1/traces` as the endpoint and `Transport.HTTP` as the transport in our register helper

```
// tracer_provider = register(
    endpoint="https://otlp.arize.com/v1/traces",     # NEW
    transport=Transport.HTTP,                        # NEW
    space_id=SPACE_ID,
    api_key=API_KEY
    project_name="test-project-http",
)
```
## 📚 New Content

The latest video tutorials, paper readings, ebooks, self-guided learning modules, and technical posts:

💯 [How 100X AI Uses Phoenix to Supercharge AI-Driven Troubleshooting](https://arize.com/blog/how-100x-ai-uses-phoenix-to-supercharge-ai-driven-troubleshooting/)

🤖 [Understanding Agentic RAG](https://arize.com/blog/understanding-agentic-rag/)

⚙️ [Multiagent Finetuning: A Conversation with Researcher Yilun Du](https://arize.com/blog/multiagent-finetuning-a-conversation-with-researcher-yilun-du/)
