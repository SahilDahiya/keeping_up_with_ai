---
title: Arize AI Partners with Algorithmia to Enable Better MLOps and Observability
  for Enterprises
topic: industry
subtopic: announcements
secondary_topics:
- evals-observability/monitoring
summary: Partnership announcement between Arize and Algorithmia focused on bringing
  ML observability into enterprise MLOps workflows.
source: arize
url: https://arize.com/blog/arize-ai-partners-with-algorithmia/
author: Aparna Dhinakaran
published: '2021-04-19'
fetched: '2026-07-11T04:42:31Z'
classifier: codex
taxonomy_rev: 1
words: 1847
content_sha256: c2a082090f93f12c63642400fb2ffdedcd18a2e4967f3ea2acb08ae24b6676a5
---

# Arize AI Partners with Algorithmia to Enable Better MLOps and Observability for Enterprises

![Algorithmia -Arize blog cover Algorithmia - Arize](https://arize.com/wp-content/uploads/2022/08/Algorithmia-Arize-blog-cover.jpg)

              # Arize AI Partners with Algorithmia to Enable Better MLOps and Observability for Enterprises

*Written in collaboration with Ezra Citron, Customer Solutions Consultant at Algorithmia.*

We’re excited to share that Arize AI and Algorithmia are partnering to help organizations deliver more models to production, maximize their performance, and minimize model risk.

From optimizing delivery ETAs to protecting against defaults, modern companies of all sizes and industries understand the value of leveraging machine learning and AI to achieve key business objectives. However, despite the often significant and accelerating R&D investments in ML systems, taking a model from research to production isn’t an easy feat. [Machine learning operations](https://algorithmia.com/mlops?utm_medium=arize&utm_source=guest-blog) (MLOps) and ML observability are some of the most significant challenges faced by teams trying to scale their ML efforts.

## AI Investment Problem

In the last decade, digital transformation has been elevated to a mission-critical imperative for many organizations. At its core, this shift has accelerated companies’ use of cloud computing to power how they build and operate their technology stacks—the most advanced teams have leveraged this transition to adopt a data-centric approach to tackle key business objectives and fuel customer engagement. As Clive Humby put simply: Data is the new oil.

How teams harness the power of data and applications can make or break a business. The effects of this are especially acute when considering the increasing reliance on automation and machine-learned systems that power AI.

Today, a wealth of business intelligence and data processing solutions are available to help organizations make sense of their data and build machine learning models into their businesses. The north star is to leverage unique data and machine learning to give one’s business an edge over the competition.

However, the reality is that despite an ever-growing investment in AI, many organizations fail to reach this desired result for multiple reasons. Algorithmia’s [2021 enterprise trends in machine learning report](https://info.algorithmia.com/2021?utm_medium=arize&utm_source=guest-blog&utm_campaign=IC-2012-2021-ML-Trends) revealed that 83% of all organizations had increased their AI/ML budgets in the past year. The average number of data scientists employed has grown by 76%. Despite this level of investment, the time required to deploy a trained model to production has increased, with 64% of all organizations taking a month or longer. Organizations are struggling with the operational components needed to deploy and operate ML models in production after the development stage.

Once over the initial hurdle of getting ML models into production, another challenge is monitoring and optimizing model performance. Without proper model observability, the reality is that AI investment can sometimes feel like you’re throwing money into a black box. A model that worked for one customer or scenario doesn’t work for another. What worked last Thursday doesn’t work this Tuesday. A recommendation from a model for credit or purchase angers a customer. Have you added risk and cost to your business that you don’t understand? Data is the new oil, but only if harnessed in the right way.

How can organizations that invest heavily in data science reap the rewards of that investment? Simply investing in ML and developing models is not enough. To unlock the value in your ML investment, you need MLOps—and a critical component of your MLOps—ML observability.

That’s why we’re excited to share that Arize AI and Algorithmia are partnering to help organizations deliver more models to production, maximize their performance, and minimize model risk.

With a simple integration, customers will be able to leverage the combined power of Algorithmia’s enterprise MLOps platform and Arize’s ML observability platform to deploy models and manage performance at scale.

## Streamline Machine Learning Operations

Algorithmia’s [enterprise MLOps platform](https://algorithmia.com/mlops?utm_medium=arize&utm_source=guest-blog) manages all stages of the production ML lifecycle from deployment and operations to governance and security—enabling data science and ML teams to deliver more models quicker while protecting the business. With Algorithmia, organizations of all sizes can easily:

- Connect, load, catalog, version, and validate models for production in a central platform.
- Manage costs, control infrastructure usage, monitor operations, and deliver models and services at high velocity.
- Minimize risk with enterprise-grade security and governance across all data, models, and infrastructure.

**Bridge the Gap Between Data Science and ML Engineering**

As enterprise AI/ML systems grow to operate at scale, deep model observability is critical to make well-informed business investments and build a high-performing MLOps practice. Arize AI provides real-time monitoring and observability to help teams understand how their models perform in the real world and improve their performance. The ability to upload offline (training or validation) baselines into an evaluation store for automated drift, data quality, and performance analysis creates an active feedback mechanism between data science and engineering teams so that they can:

- Manage and improve machine learning investment through a single pane of glass.
- Map drift changes to actual performance changes.
- Make real-time drift assessments, multi-model performance comparisons, fairness/bias evaluations, and performance monitoring assessments with support for delayed ground truth.
- Complete root-cause analyses to troubleshoot model failures/performance degradation using explainability and slice analysis.

Leveraging the Arize and Algorithmia platforms give struggling teams a streamlined ability to test and compare model performance, discover the root cause of issues in production, manage risks and costs, and uncover retraining opportunities. This solution empowers teams to increase the velocity at which they can develop and iterate on models, increase model quality, and decrease cost, delivering AI into the business as if it were a product.

**Get Started with the Algorithmia-Arize Integration**

For existing Algorithmia customers, integrating with the Arize AI platform is simple. If you’re not familiar with Algorithmia or Arize, sign up for an [Algorithmia demo](https://algorithmia.com/demo?utm_medium=arize&utm_source=guest-blog) and [early access](https://arize.com/) to Arize. Below, we’ll explain the basic components of the integration; to test it out, you’ll need accounts on both platforms.

The general workflow is that when you deploy your model on Algorithmia, you’ll add some code to establish a connection with Arize and to log the features, prediction, and actuals every time the model is called. You can then use these data on the Arize side for model tracking and explainability.

In the code samples below, we’re just showing the parts associated with establishing the connection to Arize and logging the data; for the complete code showing the integration end-to-end, visit [Algorithmia’s Developer Center](https://algorithmia.com/developers/integrations/arize).

Before incorporating the logging functionality into an Algorithmia algorithm, you can use a Jupyter notebook or your favorite local IDE to test the part of the code that sends data to Arize, to make sure the connection is configured properly and the library dependencies are in place. We recommend this workflow for development, as debugging is often more efficient in a local environment.

Begin by importing the necessary Arize classes from the Arize Python client library, as well as some additional Python modules and libraries:

from arize.api import Client from arize.types import ModelTypes import datetime import joblib import pandas as pd

Note that the code sample below assumes a trained model serialized as *MODEL_NAME.joblib* and some test data in the pandas *DataFrames X_test* and *y_test*. Calling the to_json() method on X_test, the first row of data looks like this:

```
{
"mean radius":{"204":12.470000267},
"mean texture":{"204":18.6000003815},
...
"worst symmetry":{"204":0.3014000058},
"worst fractal dimension":{"204":0.0874999985}
}
```
The *arize.api.Client* object establishes the connection to your account on Arize, so you’ll need to provide your secret Arize credentials. The *Client’s log_bulk_predictions()* and *log_bulk_actuals()* methods do the heavy lifting, sending the specified data to the Arize platform:

import Algorithmia import pandas as pd #Provide Algorithmia secret; we recommend reading from an environment variable. ALGORITHMIA_API_KEY = "ALGORITHMIA_API_KEY" #Establish a connection with Algorithmia. client = Algorithmia.client(ALGORITHMIA_API_KEY) #Identify your new algorithm and instantiate an algorithm object. ALGO_ENDPOINT = "ALGO_OWNER/ALGO_NAME/ALGO_VERSION" algo = client.algo(ALGO_ENDPOINT) #Optionally set timeout parameters for testing purposes. algo.set_options(timeout=60) #Pipe JSON payload into algorithm and convert JSON output back to DataFrame. input = X_test.to_json() result_json = algo.pipe(input).result result_df = pd.read_json(res)

After you verify that the sample data are being logged to Arize, simply move the logging functionality into an Algorithmia algorithm, which will be exposed as an API endpoint to be called in real-time. Once you’ve uploaded your serialized model and published the algorithm, you can send data straight into it through the pipe() function, as demonstrated in the example code below.

Note that since the Algorithmia API requires JSON-formatted data for its apply() function, you’ll need to convert any production and/or test data to JSON before sending them as algorithm input. Algorithmia will return the response directly as another JSON object with the algorithm output stored in the object’s result attribute. You can then convert the JSON output into the desired type—in this example, back into a pandas DataFrame.

Below is an example of code that can be used to call your published model on Algorithmia. The Algorithm code itself is shown in the [integration guide on the Developer Center](https://algorithmia.com/developers/integrations/arize).

import Algorithmia import pandas as pd # Provide Algorithmia secret; we recommend reading from an environment variable. ALGORITHMIA_API_KEY = "ALGORITHMIA_API_KEY" # Establish a connection with Algorithmia. client = Algorithmia.client(ALGORITHMIA_API_KEY) # Identify your new algorithm and instantiate an algorithm object. ALGO_ENDPOINT = "ALGO_OWNER/ALGO_NAME/ALGO_VERSION" algo = client.algo(ALGO_ENDPOINT) # Optionally set timeout parameters for testing purposes. algo.set_options(timeout=60) # Pipe JSON payload into algorithm and convert JSON output back to DataFrame. input = X_test.to_json() result_json = algo.pipe(input).result result_df = pd.read_json(res)

When you call your algorithm, your prediction events are now logged to Arize, and the platform discovers your model and sets up dashboards, monitors, and analytics for your predictions.

Default dashboards are set up to highlight critical evaluation and data metrics. In addition to inference metrics, you can also send operational metrics from Algorithmia to Arize. For a detailed, step-by-step walk-through of this integration, visit [Algorithmia’s Developer Center](https://algorithmia.com/developers/integrations/arize).

![](https://arize.com/wp-content/uploads/2021/04/arize1.png)

![](https://arize.com/wp-content/uploads/2021/04/arize2.png)


*Example PSI Monitor *

![](https://arize.com/wp-content/uploads/2021/04/arize3.png)

**About Arize AI**

Arize AI is a [Machine Learning Observabililty](https://arize.com/model-monitoring) platform that helps ML practitioners successfully take models from research to production, with ease. Arize’s automated [model monitoring](https://arize.com/ml-monitoring/) and analytics platform help ML teams quickly detect issues the moment they emerge, troubleshoot why they happened, and improve overall model performance. By connecting offline training and validation datasets to online production data in a central inference store, ML teams are able to streamline [model validation](https://arize.com/ml-model-failure-modes/), [drift detection](https://arize.com/take-my-drift-away/), [data quality checks](https://arize.com/data-quality-monitoring/), and [model performance management](https://arize.com/monitor-your-model-in-production/).

Arize AI acts as the guardrail on deployed AI, providing transparency and introspection into historically black box systems to ensure more effective and [responsible AI](https://www.forbes.com/sites/aparnadhinakaran/?sh=5d7691024958). To learn more about Arize or machine learning observability and monitoring, visit our [blog](https://arize.com/blog/) and [resource hub](https://arize.com/resource-hub/)!

**About Algorithmia**

Algorithmia is the enterprise MLOps platform. It manages all stages of the production ML lifecycle within existing operational processes, so you can put models into production quickly, securely, and cost-effectively.

Unlike inefficient and expensive do-it-yourself MLOps management solutions that lock users into specific technology stacks, Algorithmia automates ML deployment, optimizes collaboration between operations and development, leverages existing SDLC and CI/CD systems, integrates with best-of-breed tools, and provides advanced security and governance.

Over 130,000 engineers and data scientists have used Algorithmia’s platform to date, including the United Nations, government intelligence agencies, and Fortune 500 companies. To learn more, [explore the Algorithmia platform](https://algorithmia.com/product) and [get your demo](https://algorithmia.com/demo?utm_medium=arize&utm_source=guest-blog) today.
