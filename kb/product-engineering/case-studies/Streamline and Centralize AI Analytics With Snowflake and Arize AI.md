---
title: Streamline and Centralize AI Analytics With Snowflake and Arize AI
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/monitoring
summary: Describes using Snowflake with Arize to centralize AI analytics and observability
  data for model performance analysis.
source: arize
url: https://arize.com/blog/ai-data-analytics-with-snowflake-and-arize-ai/
author: Krystal Kirkland
published: '2023-07-19'
fetched: '2026-07-11T04:47:25Z'
classifier: codex
taxonomy_rev: 1
words: 787
content_sha256: f88e8677fcb47aa809f219541b470c285a32f48575d0ef30ae2659abd06d079c
---

# Streamline and Centralize AI Analytics With Snowflake and Arize AI

![arize-snowflake snowflake + arize](https://arize.com/wp-content/uploads/2023/07/arize-snowflake.jpg)

              # Streamline and Centralize AI Analytics With Snowflake and Arize AI

*This blog is co-authored by Aman Khan, Group Product Manager at Arize AI*

We’re thrilled to announce that Snowflake and Arize have joined forces to supercharge the machine learning (ML) toolchain and streamline how our joint customers access, analyze, and act on their machine learning model insights.

The [Snowflake Data Cloud](https://www.snowflake.com/) enables customers to unite siloed data, discover and securely share data, power data applications, and execute diverse [AI/ML and analytic workloads](https://www.snowflake.com/en/data-cloud/workloads/ai-ml/). Our new, integrated solution enables customers to stream high-volume ML data from Snowflake in real-time for quick, continual, and comprehensive data analytics with Arize.

Let’s dive into how you can use Arize and Snowflake to make data-driven decisions about your ML models with advanced AI observability and simplified data management.

## Simplified Data Management with Snowflake

Easily provision access with enhanced egress control in Snowflake. This enables you to stream Snowflake data to Arize without moving data out of Snowflake, maintaining full control over your data to manage organizational efficiency, reduce costs, and maintain security standards across the board.

## Advanced AI Observability with Arize

Enable AI observability with a simple one-time setup to instantly gain a single pane of glass view of all your model data. Arize helps close the ML feedback loop to build, ship, and maintain ML models across teams and stakeholders with full resolution into your model data model.

Scale your AI/ML initiatives with purpose-built tooling that compliments your existing ML stack. Create a fully manageable, simple, and scalable data pipeline to automatically extract model insights and boost ROI – without compromise.

“Model observability is key to ensuring trust in machine learning insights,” said Tarik Dwiek, Head of Technology Alliances at Snowflake. “We’re excited to integrate with Arize to help customers leverage the ML tooling they need to build efficient, transparent, scalable AI capabilities and thrive in today’s AI landscape.”

## How the Snowflake Connector Works

![Snowflake Arize data connector](https://arize.com/wp-content/uploads/2023/07/arize-snowflake-data-connector.jpg)


Enable the Snowflake connector to create an automatic data pipeline that continuously syncs and processes data within Snowflake tables to the Arize platform without data movement, preserving governance and security. The connector can be tailored to fit your specific monitoring and observability needs within Snowflake. Whether you want to sync your entire dataset with Arize or opt for various table sampling options, your team retains full control over your data pipeline.

## How to Sync Your Data

Sync your Snowflake Data Cloud with Arize in three easy steps for real-time, continuous [model monitoring](https://arize.com/model-monitoring/). For detailed instructions, visit the [Snowflake](https://docs.arize.com/arize/sending-data-methods/snowflake) page on the Arize docs.

### Step 1: Grant Permissions

Arize syncs model data from each Snowflake table. Grant Arize access permissions to read the table storing your model inference data and to automatically sync new data.

![Grant Permissions Arize Snowflake](https://arize.com/wp-content/uploads/2023/07/grant-permissions-snowflake-table.jpg)


Provide your table directory to Arize. This includes the account ID, database, schema, and table names.

![table snowflake arize](https://arize.com/wp-content/uploads/2023/07/provide-snowflake-table-directory-to-arize.jpg)


From the ‘Dataset Configuration’ card, Arize will automatically generate all the necessary table permissions to paste into a Snowflake SQL worksheet.

![snowflake and arize how to](https://arize.com/wp-content/uploads/2023/07/snowflake-sql-worksheet.jpg)


⚡Pro tip: Be sure to click ‘Run All’ in your Snowflake worksheet to execute the entire sheet.

### Step 2: Configure the Model Schema

Model schemas organize and transform your model data, simplifying monitoring and observability workflows. Define your model schema to specify what data Arize should read from the table.

![snowflake arize configure model schema](https://arize.com/wp-content/uploads/2023/07/log-prediction.jpg)


While a model schema is flexible and will vary based on your model type, environment, and desired performance metric, the change_timestamp schema parameter is **required** to indicate when a row was added to the table and automatically sync new rows to Arize.

### Step 3: Set Up Monitors With Arize

With the connection established, set up monitors and alerts for your ML model in Arize. Enable monitors on performance, drift, and data quality metrics in one click to proactively monitor, troubleshoot, and optimize your models.

![arize setup monitors](https://arize.com/wp-content/uploads/2023/07/setup-arize-monitors.png)


Since your data pipeline automatically syncs new data from your table, use Arize to ensure optimal AI performance in real-time and get alerts when your monitor deviates from expected values.

![arize monitor recall](https://arize.com/wp-content/uploads/2023/07/arize-monitoring-recall.png)


## Conclusion

Use the Arize and Snowflake integration to optimize your ML models using secure, governed, up-to-date data so they can maintain stride with the pace of innovation. As the AI infrastructure landscape rapidly evolves, empower your AI initiatives with a streamlined ML stack to unlock your model’s full potential. Deploy models with the peace of mind that your projects are backed by scalable infrastructure, transparent security practices, and tailored workflows with Snowflake and Arize.

If you need help or have any questions, don’t hesitate to reach out to us for [support on Slack](https://docs.google.com/document/d/1LWUYJR5_kEu7vnmBgdL7ypKWP1j9M1zarlT46l_JIj0/edit#heading=h.o3bebxjyjxlm)!
