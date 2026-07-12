---
title: Deploying Models In An Evolving Housing Market
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/monitoring
summary: Case discussion on deploying models in a changing housing market and monitoring
  model behavior under shifting real-world conditions.
source: arize
url: https://arize.com/blog/deploying-models-in-an-evolving-housing-market/
author: David Burch
published: '2022-06-22'
fetched: '2026-07-11T04:45:12Z'
classifier: codex
taxonomy_rev: 1
words: 1416
content_sha256: edbbcd4cdbfb2545adf639590990258825b5f4b1e0941eb8fbd12e118e1f13fd
---

# Deploying Models In An Evolving Housing Market

![Chris-Murphy](https://arize.com/wp-content/uploads/2022/07/Chris-Murphy.jpg)

              # Deploying Models In An Evolving Housing Market

Chris Murphy is Senior Director and Data Scientist at Homepoint, the nation’s third-largest wholesale mortgage lender. With a commitment to putting people front and center throughout the homebuying experience, Homepoint supports successful homeownership as a crucial element of broader financial security and well-being by delivering long-term value beyond the loan. Behind the scenes, AI plays an important role in helping the organization accomplish this mission. As the senior lead on a growing team, Murphy is charged with ensuring the company deploys effective models in an evolving marketplace.

**What is your career background and how did you first get into machine learning? **

I completed my PhD in physics. After a few years of doing research, I became intrigued by all of the exciting news and breakthroughs in data science and knew friends that made a successful transition into the field. After going through Insight Data Science, I landed my first job in data science at Wayfair. Now, I’m happily leading a team at Homepoint.

When I first joined Homepoint, there was a lot of greenfield for developing data science at the company as we underwent a big transformation in terms of adopting technology. Since then, it has been really nice to lead full stack data science and work on a wide range of different projects.

**Can you also talk about how you made a transition into financial services given others may be interested in joining that industry but might be wondering about the learning curve and cross-applicability of skills?**

There are a lot of transferable skills in terms of modeling techniques and how to approach challenges even though the specific business problems are different. At the end of the day, most industries are tackling tasks like increasing revenue or reducing costs. That said, there are a lot of acronyms and terminology to learn in this industry. Before starting at Homepoint, I actually bought [a book on home buying](https://www.amazon.com/How-Your-Perfect-First-Home/dp/1731350120) to better understand the market.

**On that note, how does Homepoint fit into the broader market and why would a buyer choose to work with you?**

At Homepoint, we emphasize the broker advantage. Mortgage brokers work with many different wholesalers, which translates into a big advantage in rates – ultimately saving a buyer more money because they have more options to choose from when getting their loan. There is a [dataset](https://www.consumerfinance.gov/data-research/hmda/historic-data/) that is publicly available as part of the [Home Mortgage Disclosure Act](https://www.consumerfinance.gov/data-research/hmda/) that anyone can consult to compare the difference. We’ve done some exploratory data analysis on this dataset to show that working with brokers actually saves people money, both upfront and in terms of better interest rates. Homepoint also stands out in the service we offer people across the loans that we have in our portfolio. We retain a large servicing staff and the machine learning team has models that help in those efforts. Homepoint also has some great programs, like [Homepoint Cash Compete](https://www.homepointfinancial.com/press/homepoint-extends-deal-winning-capability-of-independent-loan-originators-through-all-cash-offers/).

**What are some of your machine learning use cases at Homepoint?**

ML spans many different areas of the business. In operations, for example, we try to optimize how we assign loans to associates, underwriters, or closers. There are also some more bread and butter-type data science activities. Similar to how an ecommerce company might want to predict who is going to churn, we are trying to predict who might want to refinance or who is going to be delinquent on their loans. There is also some outlier detection done on loans, so if we don’t fund as many loans as we thought we were going to last week, for example, we try to understand whether it is just market conditions or whether there is something operationally that needs to be worried about. There are also some teams working on text reading and optical character recognition (OCR). Finally, there is a lot of ML infrastructure being built. We now have a data profiler up and running and we also have a feature store, so there has been a lot of work going on in the engineering side of things.

**Underwriting has many established processes and complexities. As you apply state of the art ML techniques into these use cases, what best practices ensure that you are successful?**

The data science team at Homepoint has been fortunate because we started from scratch, so we had a chance to do things right from the beginning. Often, companies will be hyper-focused on growth – just wanting to get stuff done quickly – and aren’t really worried about the setup part. It has really been the opposite at Homepoint, where we spin up our own processes and have our own products running on our Kubernetes cluster. We are really getting it done ourselves and are constantly in contact with business partners, operations partners, and the pricing team to iterate on what they need from a business perspective. From a technology perspective, we are self-sufficient in setting things up and evolving from there.

**How do you decide on which algorithms to use – and how do you navigate tradeoffs between a model that might be a better predictor but that is more of a black box?**

A few years ago when the interest rates were super low, our models would do things like predict who would refinance and then have the marketing team reach out with personalized messages. With market conditions now changing so quickly, we really need to have nimble models that are not going to overfit – so it might be doing something like a tree-based model or even a linear model in some cases. We are trying to really be nimble in terms of not overfitting on data. Another consideration is ensuring a large enough training set where we have a variety of market conditions in the data.

**Can you talk about your approach to ****explainability**** and ****bias tracing****?**

We’re using a variety of techniques, from SHAP to some third party packages like Microsoft’s[ Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox#getting-started) (particularly their[ Error Analysis](https://erroranalysis.ai/) package), to ensure fairness across the board. Understanding what features are important for explaining a given set of outliers is definitely useful to know across the business.

**What is your approach for navigating things like ****concept and data drift****? **

One approach where we saw success relative to competitors post-COVID was in not having super generic models. In a challenging environment, models with a narrower focus tend to perform better than do-everything sorts of models. Having a narrower focus ultimately helped us have better performance in predicting things like refinances or delinquencies, particularly in 2020.

Good reporting and monitoring is also helpful. No one wants the dreaded business partner email inquiring about something that doesn’t look right, which is why we have [model monitoring](https://arize.com/model-monitoring/) in place. Depending on the use case, usually our models are retrained with a pretty frequent cadence as well.

**What are some best practices for ensuring your training data stays relevant when things are changing all the time? **

In some cases, you need to make sure that you have a long enough time period while also ensuring that you don’t use the full amount of data – skewing it toward more recent data can be useful on a time series analysis or just making sure you’re capturing enough rate variations.

On some projects at Homepoint, treating the time length of the training dataset almost as another hyperparameter that you want to optimize is helpful. Looking back too far might introduce bias or data that does not matter much anymore, but you still need a large enough window to make sure you have enough data to train your model well enough. This varies a lot depending on the type of loan and business.

**Can you talk about how you balance fully automated systems versus human in the loop?**

We use both. For personalization of marketing on loan programs, for example, we are using a combination of machine learning modeling as well as information about the borrowers themselves to inform more human-based approaches with brokers.

**What is the most rewarding and most challenging part of your job? **

It’s really rewarding to take data science projects from inception to the finish line and to see ideas – even small ones – get deployed into the real world and make a difference. One challenge – and this isn’t a bad thing – is navigating digital transformation and being a more tech-savvy business, but it’s exciting to see us move in the right direction.
