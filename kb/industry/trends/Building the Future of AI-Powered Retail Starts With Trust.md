---
title: Building the Future of AI-Powered Retail Starts With Trust
topic: industry
subtopic: trends
secondary_topics:
- product-engineering/security
summary: Retail-focused discussion of AI adoption and why trust, monitoring, and responsible
  deployment matter for customer-facing AI systems.
source: arize
url: https://arize.com/blog/building-the-future-of-ai-powered-retail-starts-with-trust/
author: David Burch
published: '2022-05-03'
fetched: '2026-07-11T04:44:50Z'
classifier: codex
taxonomy_rev: 1
words: 1338
content_sha256: 77b56172c346ebc52949f7ef69dac1e4a37d069e985e797576466facf7fc553c
---

# Building the Future of AI-Powered Retail Starts With Trust

![Jiazhen Zhu_blog2](https://arize.com/wp-content/uploads/2022/07/Jiazhen-Zhu_blog2.jpg)

              # Building the Future of AI-Powered Retail Starts With Trust

Jiazhen Zhu leads the end-to-end data team at Walmart Global Governance DSI, a diverse group of data engineers and data scientists united in building a better platform through data-driven decisions and data-powered products. Zhu first joined Walmart Global Tech in 2019 to oversee both data engineering and machine learning, giving him a unique vantage point into the interrelated worlds of DataOps, MLOps and data science. Before Walmart Global Tech, Zhu was a data scientist and software engineer at NTT Data.

**Can you briefly introduce yourself and outline your role at Walmart Global Tech?**

Currently, I am the lead data engineer and machine learning engineer at Walmart Global Tech. I work with data end-to-end, starting with where we get the data on through to how we clean the data, transfer the data, feed the data into model training and then ultimately move models into the production layer. I enjoy overseeing this process and bring a decade of experience working in both data and machine learning, building platforms across both.

**What was your career journey leading up to this point? **

After completing my bachelor’s degree in computer science, I worked as a software engineer at Citi focused on the data warehouse used to build models and support scalable data modeling. Then, I completed a master’s degree in data science and worked as both a software engineer and data scientist. All of this is interrelated as data engineering and machine learning engineering are really just part of software engineering – typically, the software engineer will be focused on the application or UI or full-stack tasks, whereas the machine engineer and data engineer are more focused on the data and model, respectively.

**How does Walmart Global Tech fit into Walmart overall?**

Walmart Global Tech works on cutting-edge technologies that create unique and innovative experiences for our associates, customers and members across Walmart, Sam’s Club and Walmart International. We solve the myriad challenges that every retailer faces, whether it’s dealing with suppliers, distribution, ordering, innovation, shopping experience, or after-sales service. The one commonality across all of these is that they all benefit from technology.

**You oversee both data engineering and machine learning – any lessons for others in terms of the benefits of structuring the organization this way? This must give you a unique vantage point on data-centric AI, per  your recent blog. **

In other companies, these functions are often separated in different organizations. My own experience is that if we can combine the different roles – particularly the data scientists, the research scientists, data engineers, machine learning engineers, and software engineers – in one team, it can speed up product development. Since most of the domains require specialized knowledge, combining many different roles into one team can also help bring new innovative ideas to the product.

**How do you think about the build-versus-buy calculus when it comes to ML platforms? **

For MLOps platforms, which is obviously a new area, it varies – it’s not as simple as saying we have one tech stack that we follow every time. What we do is approach these decisions based on requirements – then we make sure that each component will be easy to replace or rebuild, so down the road we don’t have to rebuild the whole thing just because one component no longer fits our needs.

**What types of models is Walmart Global Tech deploying into production and why? **

It depends on the area, requirements, and end-customers. At the outset, I always start with the question: do we need machine learning at all to solve this problem, or is there an easier way to fix it that we should implement instead? If machine learning is necessary, then it’s often much easier and better to pick a simple model like regression or linear regression to ensure good performance. We leverage those types of models for base cases. When there is a good existing model to use, we often will adapt or use it – like BERT for natural language processing.

I want to emphasize that for the model itself, trust is critical. Not everyone will trust the model. This is why I said at the beginning that the simplest is often the best. Not using machine learning – or if you do need to use machine learning, leveraging a model that offers easier explanations like linear regression models – is preferable. The black box nature of BERT or deep learning makes the task of helping people or customers understand the model more difficult.

Ultimately, if customers or people don’t trust the model it’s useless. So building a process to explain the model is critical. It’s also important to troubleshoot the model itself.

**Sounds like  model explainability and being able to trust a model’s decisions is really important to your team?**

Yes, it’s important not only for the model but also for the product and its customers. If you can explain a model to a customer or a user, you can explain it to yourself also – so it’s win-win that way as well. No one likes a black box.

**What is your strategy for  model monitoring and troubleshooting model performance? **

Since change is always happening, monitoring is really the key to successful MLOps. Whether it’s from a data engineering or machine learning engineering perspective, we always task the role with monitoring all processes across the pipeline or infrastructure. The data engineer, for instance, will look at whether there are data quality issues, data mismatches, missingness, and more.

For machine learning, monitoring spans both the data and the model itself. We look at [data drift, concept drift](https://arize.com/model-drift/) and performance across key metrics (i.e. [AUC](https://arize.com/blog/what-is-auc/)) to get to the bottom of issues and inform the retraining process. There is a lot you can track, so having access to key metrics for root cause analysis and getting notifications and alerts really helps.

**This must be a really interesting time at Walmart given record demand, supply chain challenges, inflation and a lot more. Have you experienced any interesting issues with production models reacting to a new environment?**

Definitely, yes. The one constant is that the data are always changing. A model trained on social network data, for example, may see broad impacts to model performance when the social network data drastically changes or disappears overnight. Issues like these are very common.

**Half of data scientists we recently  surveyed (50.3%) say that their business counterparts do not understand machine learning. How have you successfully navigated this hurdle to scale your ML practice? **

This kind of situation is common in the industry. As discussed, some models are black boxes – and few trust black boxes that are unopened, which is why explainability is so important. If your customers look at it and understand why a model made a particular decision, trust will grow over time.

**For models that directly impact customers, how do you incorporate customer feedback into your models?**

Customer feedback is so important. The data might change or the concept might change, but if customer feedback is part of the ML process then we can use that customer data to retrain the model in near real-time and have better model performance and a better ability to predict reality as a result. Having that human-in-the-loop process to check things can help ensure that models are relevant and performing well.

**What is your most favorite and least favorite part of your current role? **

I love data and I love playing with data, so that’s really one of my favorite aspects of my current role. Incidentally, it’s also one of the more difficult parts of the job because you need to know the data well before you fit it into a model. In terms of machine learning, one of the hardest things is knowing how to pick the right approach – not just for the model, not just for the data, but also the tech stacks, scalability and everything about the ML pipeline.
