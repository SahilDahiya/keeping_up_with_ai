---
title: Calculate Real-Time AI ROI With Custom Metrics
topic: evals-observability
subtopic: monitoring
secondary_topics:
- infra-platform/cost
summary: Shows how custom metrics can connect AI observability data to real-time ROI
  analysis and business impact.
source: arize
url: https://arize.com/blog/calculate-real-time-ai-roi-with-custom-metrics/
author: Krystal Kirkland
published: '2022-12-16'
fetched: '2026-07-11T04:46:21Z'
classifier: codex
taxonomy_rev: 1
words: 932
content_sha256: be5b25d7e9abe047c34567d6d8ee392ef24b8980a10654c316ad1074253293c0
---

# Calculate Real-Time AI ROI With Custom Metrics

![AI-ROI blog cover-2 (1) arize custom metrics udm](https://arize.com/wp-content/uploads/2022/12/AI-ROI-blog-cover-2-1-1021x560.jpg)

              # Calculate Real-Time AI ROI With Custom Metrics

We are excited to announce support for** custom metrics** across the Arize platform. This new feature enables you to tailor any metric to your ML monitoring needs. Learn how to use custom metrics to automate AI ROI calculations, map impact across all model inference data, and reduce overall costs.

*There is a wide breadth of custom metrics applications (i.e. custom performance calculations). Refer **here** for more examples.  *

## The AI ROI Problem

ROI calculations are commonly bespoke, nuanced, and complex for businesses. Add machine learning (ML) into the mix, and you’re left with an even more complex multifactorial calculation that can take days to quantify. According to a [2022 survey of top ML teams](https://arize.com/wp-content/uploads/2022/02/The-Industry-is-Ready-for-Machine-Learning-Observability-at-Scale-Final.pdf), organizations face a few significant problems when calculating AI ROI.

- **Hard to quantify:**54.0% of data scientists and ML engineers report that they encounter issues with business executives not being able to quantify the ROI of ML initiatives
- **Difficult to understand:**nearly as many (50.3%) report that business executives simply do not understand machine learning
- **Highly laborious and costly:**companies that try to quantify AI ROI have to hire individual analysts to manually calculate impact on a model-by-model and case-by-case basis

Despite the challenges in quantifying AI ROI, AI applications significantly impact business-critical needs across industries. From improving patient outcomes and medical diagnostics in the healthcare industry to reducing fraudulent transactions in the financial and insurance industry, the question remains: *To what extent does AI impact my business? Did the update I made to the model improve or degrade business outcomes? Is my current AI ROI calculation reliable? *

## Reliable AI ROI With Custom Metrics

While there’s no one-size-fits-all solution for each calculation, an adequate AI ROI calculation requires a holistic view of all model inference data and performance. Since production environments change quickly, safeguarding your AI investment and providing stakeholders with a real-time view of AI ROI with automatic calculations based on key performance metrics you’ve defined is key.

In Arize’s ML observability platform, custom metrics enable you to easily create bespoke AI ROI calculations using a combination of existing model dimensions and functions. Since Arize ingests your model inference data and automatically evaluates your model performance across all features and slices, creating, maintaining, and evaluating your AI ROI has never been easier or scalable.

Once set up, your real-time AI ROI calculations are available across the platform in dashboards, for monitoring, and performance tracing of issues.

Calculating AI ROI with custom metrics enables teams to:

- **Prioritize investments**: Use performance tracing to get a breakdown of how all your features impact your custom metric and gain a granular understanding of the many dimensions that impact your AI ROI for further investment
- **Reduce spending**: Lower costs by removing the need for manual analysis and automatically understand how production models impact your business
- **Improve accuracy**: Combine the many dimensions of real-time model inference data for the most accurate custom calculation for any use case and monitor your calculations when things go wrong.
- **Inform stakeholders**: Custom metrics make real-time AI ROI calculations available to stakeholders at any time with flexible and shareable dashboards

## Example of Custom Metric

*In Arize, custom metrics are written with a SQL-like query language. Learn more **here**. *

This example covers using custom metrics to calculate the average dollar loss as a percentage of total loan volume (charted daily). Specifically, we use the arize-demo-fraud-use-case model available in all accounts. Sign up for your account [here](https://app.arize.com/auth/join) to get started.

Navigate to the **Custom Metrics** tab within the arize-demo-fraud-use-case model. We’ll use the interactive editor to create our metric. This editor allows you to write your queries with syntax validation, auto-completion of dimension names, and then preview your query result before saving it.

💡**PRO TIP: ***Click on the documentation tab on the top-right to unveil the syntax reference and model schema explorer.*

![arize user defined metric AI ROI workflow](https://arize.com/wp-content/uploads/2022/12/udm-example.png)


Now, edit the placeholder query to calculate the average dollar loss rate. Refer [here](https://docs.arize.com/arize/api-reference/12.-custom-metrics/custom-metric-examples) for a comprehensive list of Arize filters, operators, and functions.

![arize user defined metric sql interface](https://arize.com/wp-content/uploads/2022/12/arize-udm-sql.png)


Click “Test Run” to preview the metric. From there, name the metric “Average Dollar Loss Rate” and save the metric to use when building dashboards and configuring monitors.

![Arize test run user defined metric preview metric workflow AI ROI](https://arize.com/wp-content/uploads/2022/12/arize-udm-test-run-prview-metric.png)


Once the metric is saved, create a monitor using the custom metric you just defined to get alerted when something goes awry. To add a monitor, click on the “…” button on the top right and follow the monitor creation workflow.

![Arize user defined metric loss rate example](https://arize.com/wp-content/uploads/2022/12/arize-udm-avg-dollar-loss-rate.png)


To add the metric to a dashboard, create a dashboard widget by selecting the “Time Series” widget. Add a custom metric to the plot by selecting the `arize-demo-fraud-use-case model`. Under “Metric,” select “Custom Metric” and “Average Dollar Loss Rate.”

![Arize user defined metric fully setup dashboard](https://arize.com/wp-content/uploads/2022/12/udm-arize-example-configured.png)


Finally, share your dashboard with all stakeholders! We recommend setting notifications on alerts so you and relevant stakeholders can receive real-time alerts if any model changes impact critical business metrics.

## Conclusion

An inaccurate AI ROI calculation can leave millions of dollars on the table. At the current pace of innovation, it’s imperative to deploy a method to quickly, efficiently, and reliably quantify AI ROI. By using Arize to create bespoke AI ROI calculations using a combination of existing model dimensions and functions with unprecedented flexibility, businesses can develop an automatic and scalable AI ROI pipeline to optimize company resources for better results.
