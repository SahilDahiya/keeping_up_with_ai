---
title: Why You Need To Monitor Recommender Systems
topic: evals-observability
subtopic: monitoring
secondary_topics:
- rag-retrieval/search
summary: Explains why recommender systems need monitoring and what signals matter
  for production ranking quality.
source: arize
url: https://arize.com/blog/why-monitor-recommendation-systems/
author: Amber Roberts
published: '2022-12-01'
fetched: '2026-07-11T04:44:31Z'
classifier: codex
taxonomy_rev: 1
words: 1764
content_sha256: fcaf30831f6386c376eb88bea38e07a3bd2094acb538aaf47ad80dfe22d597da
---

# Why You Need To Monitor Recommender Systems

![recommendation-system-arize](https://arize.com/wp-content/uploads/2022/02/recommendation-system-arize-1000x560.png)

              # Why You Need To Monitor Recommender Systems

## An overview of recommendation systems, including how teams should monitor and troubleshoot models in production

*Learn more** about how Arize helps clients observe recommendation systems,  sign up for a free account, dive into an*


*interactive demo*

*or*

*request a trial*

*of Arize.*Millions of machine learning algorithms over the last several years have been funded, researched, tested, and deployed across industries for the [sole purpose](https://www.grandviewresearch.com/industry-analysis/recommendation-engine-market-report) of providing relevant recommendations. While there are likely thousands of blog posts dedicated to teaching ML teams how to build these systems and measure success, few offer the full picture – including how to proactively monitor and maintain them once in production. Here are the five Ws (and an H) of recommendation systems.

## Who Do Recommendation Systems Impact?

Everyone reading this. While most people associate recommendation systems with media and ecommerce, they actually exist in nearly every industry domain. From [healthcare](https://link.springer.com/article/10.1007/s10844-020-00633-6) to [finance](https://www.pwc.in/assets/pdfs/consulting/financial-services/fintech/publications/recommender-systems-new-opportunities-in-financial-services.pdf), there is an increasing demand for insightful predictions to increase customer, client, or user experience. These systems can operate using a single input – like music – or multiple inputs within and across platforms like news, books, and search queries.

## What Is A Recommendation System?

A **recommendation system** (sometimes replacing “system” with a synonym such as a “platform” or “engine”), is a subclass of information filtering systems that seek to predict the *rating* or *preference* a user would give to an item. Recommendation engines power our social media feeds, streaming services, online shopping, dating apps, and more to predict what *you* – the consumer – want to consume.

## What Methods Are Used To Generate Recommendations?

There are several common types of recommendation engines, including:

**Content-Based **

A[ content-based recommender](https://www.analyticsvidhya.com/blog/2015/08/beginners-guide-learn-content-based-recommender-systems/) works with data that the user provides, either explicitly (i.e. ratings) or implicitly (i.e. clicking on a link). A user profile is generated based on that data, which is then used to make suggestions to the user.

**Collaborative Filtering**

[Collaborative filtering](https://arize.com/blog-course/monitoring-collaborative-filtering-recsys/) can be divided into **Item-Item CF ***(*“Users who liked this item also liked…”) and **User-Item CF** (“Users who are similar to you also liked…”). Collaborative filtering is based on the assumption that people who agreed in the past will agree in the future – and that they will like similar kinds of objects as they liked previously.

**Popularity-Based**

This system checks which products or movies are most popular among users in a given time period and will directly recommend those top items.

**Hybrid**

Most recommender systems now use a hybrid approach, combining collaborative filtering, content-based filtering with other more advanced approaches.

## When Should You Start Monitoring Your Recommendation Models?

As soon as they are in production! Recommendation systems, like all models, encounter issues once deployed. Models can gradually decay over time, digest outliers, and over or under-index for specific cohorts – all potentially upending business results.

While research environments can be controlled, problems with served models quickly become far more complex when met with the real world. Challenges include constant data changes, rewriting the model in a new language, or pushing features into a store.

Unfortunately, [most ML teams](https://arize.com/resource/survey-machine-learning-observability-results/) don’t know what’s wrong with their models until it’s too late. That is why it is crucial to monitor for data quality, drift and performance as soon as you push your recommendation system into production.

## Where Does the Data To Train Recommendation Systems Come From?

Recommendation systems are only as powerful as the data they ingest, and there are a multitude of data sources that range from *explicit* to *implicit*.

You might have experienced some common **explicit data collection** tactics. These include asking a user to:

- Rate an item on a sliding scale
- Search for an item
- Rank a collection of items from favorite to least favorite
- Choose the better prediction
- Create a list of items that the user likes

*See[ rocchio classification](https://en.wikipedia.org/wiki/Rocchio_algorithm) or other similar techniques.

Examples of **implicit data collection** might include:

- Browsing history
- User viewing times
- The items that a user purchases online
- A list of items that a user listens to or watches
- A user’s social network or search activity

## Where Are the Biggest Challenges In Recommendation Systems?

The following represent some of the most common issues ML practitioners encounter with recommendation systems.

- **Cold Start:**For a new user or item, there often isn’t enough data to make accurate recommendations.
- **Scalability:**In many environments, there are millions of users and products. Thus, a large amount of computation power is often necessary to calculate recommendations.
- **Sparsity:**The number of items sold on major e-commerce sites, for example, is extremely large. Often, even the most active users will only have rated a small subset of the overall database. Thus, even the most popular items have very few ratings.
- **Synonyms:**Most recommender systems are unable to discover latent associations and treat these products differently.
- **Shilling Attacks:**In a recommendation system where everyone can give ratings, brands may give many positive ratings for their own items and negative ratings for their competitors’. It is often necessary for collaborative filtering systems to introduce precautions to discourage such manipulations.
- **Diversity:**Collaborative filters are expected to increase diversity because they help discover new products. Some algorithms, however, may unintentionally do the opposite. Because collaborative filters recommend products based on past sales or ratings, they cannot usually recommend products with limited historical data. This bias can then lead to a negative feedback loop.
- **New-Item Problem:**When a new item is introduced, its lack of ratings makes it difficult to confidently recommend it to a user.
- **Non-Normalized Ratings:**In a recommendation system that takes feedback in the form of a rating, there is nothing to stop a user from giving the same rating for every item. This could either be due to biased ratings or disinterest. For example, a user may rate all movies they mildly-to-thoroughly enjoyed as five stars – or may rate everything as three stars to skip ahead.
- **User Explainability:**It is often difficult, if not impossible, for a user to know what action or actions are leading to a specific recommendation – and if there is anything they could do to no longer receive recommendations due to a specific feature.
- **Model Observability:**The data science team responsible for creating the recommendation engine may not be able to easily identify the features and events that led to a specific recommendation and whether or not those recommendations are biased (this is why- [Arize](https://arize.com), for example, is built to help ML practitioners perform root cause analysis and understand why a model is behaving a certain way).

## Why Are Recommendation Systems So Difficult To Evaluate?

Since it is important to measure the prediction error that compares expected results with the actuals the model produces as an output, performance is evaluated once the ground truths are received. There are many ways to evaluate recommendation engines given they are predictive models with algorithms that generally look to minimize the error of a function with metrics.

Here are some of the most [popular metrics](https://arize.com/glossary/) for monitoring the performance of recommendation systems.

Predictive Metrics:

- [Precision](https://arize.com/blog-course/precision-ml/): how many recommendations are relevant among the provided recommendations.
- [Recall](https://arize.com/blog-course/precision-vs-recall/): how many recommendations are provided among all the relevant recommendations.
- [Area under the ROC curve (AUC)](https://arize.com/blog/what-is-auc/)
- [F1-measure](https://arize.com/blog-course/f1-score/)
- False-positive rate
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Normalized Mean Absolute Error (NMAE)

Rank Accuracy Metrics:

- [Mean Average Precision (MAP) @ K](https://arize.com/blog-course/monitoring-collaborative-filtering-recsys/#metrics)indicates how relevant the list of recommended items is.
- Mean Average Recall (MAR) @ K indicates how well the recommender can recall all of the items in the test set that the user has rated positively.
- [Normalized Discounted Cumulative Gain](https://arize.com/blog-course/ndcg/)(NDCG) is a measure of ranking quality that is often used to measure effectiveness of web search engine algorithms or related applications.
- [Hit Ratio](https://towardsdatascience.com/ranking-evaluation-metrics-for-recommender-systems-263d0a66ef54)is simply the fraction of users for which the correct answer is included in the recommendation list of length- *L.*
- [Mean Reciprocal Rank (MRR)](https://arize.com/blog-course/monitoring-collaborative-filtering-recsys/#metrics)is also known as- *average reciprocal hit ratio (ARHR).*

Business Specific Measures

- Click-Through Rates
- Conversion Rates
- Sales and Revenue
- User Behavior and Engagement Metrics

## Why Do Companies Invest Heavily In Recommendation Systems?

It’s immensely profitable. Take video streaming, for example. Netflix’s iconic AI-driven recommendation system, which [is](https://arxiv.org/abs/1905.01986) [proven](https://arxiv.org/pdf/1908.08328.pdf) to increase engagement and reduce customer churn, is estimated to be worth nearly $1 billion to the company. The number is likely similar at Alphabet, where 70% of time spent on [YouTube](https://www.cnet.com/news/youtube-ces-2018-neal-mohan/) is due to its suggested videos.

## How Can Teams Proactively Monitor, Investigate, and Improve the Performance Of Recommendation Systems In Production?

You need to implement [ML observability](https://arize.com/ml-observability/) into your pipeline.

An example is illustrative. Imagine that you are a machine learning engineer working for a premium music service. After spending a great deal of time collecting customer data and training and testing various models, your team has built an ML-powered recommendation engine to give your listeners personalized playlist recommendations based on their most listened-to songs to boost daily active users and reduce churn.

Now you will need to:

- Confidently take models from research to production
- Monitor real-time [model performance](https://arize.com/blog/monitor-your-model-in-production/), with support for delayed ground truth
- Root cause model failures and performance degradation using [explainability](https://arize.com/blog/model-explainability-primer/)and slice analysis
- Conduct multi-model performance comparisons
- [Surface drift](https://arize.com/blog/take-my-drift-away/),- [data quality, data consistency issues](https://arize.com/blog/solving-data-quality-with-ml-observability-and-data-operations/)and connect to actual performance or business impact

In order to achieve these objectives, you will need to implement ML observability into your workflow. Unless you are able to detect major issues early, your model may negatively impact customer trust by annoying users with songs and podcasts that are irrelevant to them – leading to churn – or miss the mark by underperforming in certain genres of music.

Recommendation systems, like all ML models, tend to degrade in performance over time – often failing silently. ML observability is the practice of obtaining a deep understanding into your model’s performance across all stages of the model development cycle: as it is being built, once it is deployed, and long into its life in production. Armed with ML observability, teams can iterate and improve their models quickly.

## Conclusion

Recommendation engines are powerful tools in enhancing customer experiences and improving overall business outcomes. Given the vast amount of resources required to build these systems, it’s critical to maximize ROI and minimize time-spent troubleshooting. ML observability is a key part of how teams can do just that, proactively surfacing blindspots in model performance and addressing them quickly.
