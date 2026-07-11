---
title: AI At the Forefront of Media and Entertainment
topic: industry
subtopic: trends
secondary_topics: []
summary: Industry overview of AI use cases in media and entertainment, including personalization,
  content workflows, and operational implications for ML teams.
source: arize
url: https://arize.com/blog/ai-at-the-forefront-of-media-and-entertainment/
author: David Burch
published: '2022-07-07'
fetched: '2026-07-11T04:45:16Z'
classifier: codex
taxonomy_rev: 1
words: 1816
content_sha256: 91b27880a7ccac75c58f9953800bb594739025afb0fc88ab4d5ff15477e6153b
---

# AI At the Forefront of Media and Entertainment

![Malav Shah_blog](https://arize.com/wp-content/uploads/2022/07/Malav-Shah_blog.jpg)

              # AI At the Forefront of Media and Entertainment

Malav Shah is a Data Scientist II at DIRECTV. He joins DIRECTV from AT&T, where he worked on multiple consumer businesses – including broadband, wireless, and video – and deployed machine learning (ML) models across a wide array of use cases spanning the full customer lifecycle from acquisition to retention. Malav holds a Master’s Degree in Computer Science with a specialization in Machine Learning from Georgia Tech, a degree he puts to good use every day at DIRECTV by applying modern ML techniques to help the company deliver innovative entertainment experiences.

**Can you outline your career journey and why you first got into machine learning?**

It has been an interesting journey. During my undergraduate years, I actually studied information technology so most of my coursework was not initially in machine learning. Around my junior year, I took an AI course where we learned about Turing machines and that got me really interested in the world of artificial intelligence. Even back then, I knew that I had found my calling. I started taking some additional classes outside of my usual coursework and eventually took on a capstone project building a model predicting outliers in medical diagnosis and prognosis that left me fascinated with the power of machine learning. I did my Master’s at Georgia Tech and specialized in machine learning, taking a variety of courses from data and visual analytics to an AI class taught by former Google Glass technical lead [Thad Starner](https://www.cc.gatech.edu/home/thad/). After graduating, I took on my first role at AT&T working for about a year-and-a-half in the Chief Data Officer’s organization building acquisition and retention models for the company’s broadband product. In July of 2020, I joined a new organization within DIRECTV as part of the team responsible for all things data science with a say in how we build up ML infrastructure and our MLOps pipeline across the entire organization. Being in a centralized data organization where I could impact not just my team but other teams as well was a big motivator for joining DIRECTV.

**What attracted you to your current role? **

I interned for AT&T while completing my master’s degree. While the internship was focused on the broadband product, I also touched wireless and streaming video – so things that I used every day as a consumer. Upon graduation, most of the other roles I was getting offered at the time were in software engineering or ML engineering, but AT&T offered me a data scientist position. Being a data scientist and thinking through how to do research and solve problems ultimately proved appealing.

That role directly led to an opportunity to be part of a journey in video streaming building on a nearly 30-year-old legacy at DIRECTV. The chance to build and define new cloud tools, new infrastructure, and machine learning tools at such an early stage of my career is exciting. I don’t think I could get so much exposure to so many levels of executives anywhere else.

**How is the machine learning organization structured at DIRECTV – is there a central ML team or are most attached to the product or business teams? **

Our team within DIRECTV acts as a center of excellence. Our responsibilities are two-pronged. The first responsibility is to help solve problems and develop solutions for stakeholders from marketing, customer experience (CX), and other teams. For example, we might help build a model from scratch and deploy it into production for the marketing team before handing it over to their data scientists to own – so they own the day-to-day, while we offer continued model updates as new requirements come in. The second part of our team’s job is to define the infrastructure that these teams will use, ensuring they have the tools and technologies they need to create and deploy machine learning models effectively. Our team is also responsible for defining best practices for ML development and deployment across the organization. To that end, we are always on the lookout for ways to improve our existing ML pipelines based on our strategy and goals, either by building something in-house or looking at what capabilities are out there in the market.

**In assessing this infrastructure, how do you assess whether to build or buy? The ML infrastructure landscape has obviously evolved a lot over the past several years. **

That’s an interesting question that came up recently in the context of assessing ML observability platforms like Arize. In general, we look at business value first to ensure that any new capability is actually going to drive value for the organization. Then, we look at how soon we need the capability, the length of time it would take to build in-house, the capabilities we might build versus a vendor, and finally the cost to buy or build. This evaluation process takes up quite a bit of our time, but it has proved effective for delivering maximum return on investment to the business.

**What are your machine learning use cases?**

Primarily, DIRECTV is doing a lot of structured data modeling. For example, we work with our customer experience team to build a net promoter score (NPS) detractor model that we use to enable better experiences for customers that face issues with our service. We also work with our marketing stakeholders to build models around “personalized” customer offers and prediction of short-term as well as long-term churn.

One other area of interest is content intelligence – not analytics, but intelligence. In the content intelligence space, building a recommendation engine for the various carousels that customers see on the DIRECTV product is one of our key areas of focus. We are also starting to develop and see more traction on computer vision and natural language processing (NLP) models. Arize’s launch of image and NLP [embedding monitoring](https://arize.com/blog/monitor-unstructured-data-with-arize/) is something that we will likely need as we transition to working more with unstructured data over the next year.

**So much has changed about the media landscape in the past several years alone. Are you seeing an uptick in things like  concept drift? **

Consumption after the pandemic definitely skyrocketed. As people were stuck in their homes, churn declined industry-wide. With people working from home, these habits may have some staying power – and not just in rural areas where satellite TV is already a leader. One of the other trends in the streaming industry is a historical increase in sports viewership in general compared to 2019 (you shouldn’t really compare 2020 or 2021 given compressed sports schedules and canceled events). Sports fan engagement is also becoming a big trend as more streaming services in the industry get into sports and add interactivity, like enabling people to bet on TV. With these ever-changing consumption patterns, it becomes more important for us to track things like concept drift and feature drift to make sure we are addressing model performance issues immediately.

**What are some of the challenges you deal with once models are deployed into production – and why is  model monitoring important? **

In the video industry, behaviors are changing rapidly. If you are catching drift a month later, then it may negatively impact model performance and lead to a loss of business value. That’s one of the main reasons why I think real-time ML monitoring updates are so important in MLOps. If my model has drifted this morning, then I should know it that second. If my prediction has drifted, or if there is feature drift or some feature is empty, then I don’t want to wait a week for an analyst to check it – ideally I want to know before a weeks’ worth of predictions are out in the field.

Models are never perfect; they are always going to drift based on changing behaviors, changing data, or changing source systems. Having a centralized monitoring platform like Arize is immensely beneficial.

**What advice would you give people taking on their first data science role? **

One of the things that I advise newly-graduated data scientists to not do is obsess over having perfect metric scores right away. While focusing on a model metric like [accuracy](https://arize.com/glossary/accuracy/) is important, it’s conceptually more important to focus on understanding the underlying data – what the data is doing, what the data is telling you – and making sure that you understand the business impact and the problem that you are trying to solve. These fundamentals matter, but often people lose sight of them as they move too quickly to trying to build the best model. Instead, I would say focus 70 to 80% of your time on everything you are putting into the model because garbage in is garbage out. Once you’ve made sure you aren’t putting garbage into the model, the rest mostly takes care of itself.

One additional piece of advice for new grads is to pay attention to the wave of data-centric AI tools coming out. These will likely be the next big thing in machine learning and are worth following closely.

**How do you collaborate with business and product leads and tie model metrics to business results? **

That’s always happening. Whenever we are creating models for any stakeholder, we are regularly meeting with them to ensure what we are seeing matches what should be seen in the real world. When starting a project, making sure the requirements and the data are there and that you understand the data correctly is critical. I don’t even get into what type of model I am going to build until the later stages of the development cycle – which might be in sprint four or even sprint five. My approach isn’t to start by describing what type of model I want to build; I prefer to start with what the business value should drive first. Having a deep understanding of the data also helps me answer nuanced questions when presenting to the business executives and stakeholders.

**How do you view the evolving MLOps and ML infrastructure space? **

I think we’re moving to a very innovative era in machine learning because there are a lot of new ML solutions coming up across the industry every single week. ML observability is a great example of a space where hundreds of things are happening. Production ML versus production of other applications are completely different because other applications have been around for a while – 15 or even 25 years – and they have a very mature production pipeline, but for machine learning it’s still relatively new. It will be exciting to see how we can make ML deployment, which is a pain point for many teams, easier and seamless. Other areas of innovation that I will be watching closely include automated insight generation tools, data-centric AI tools and how we can further improve the ML infrastructure space where everything is on the cloud.
