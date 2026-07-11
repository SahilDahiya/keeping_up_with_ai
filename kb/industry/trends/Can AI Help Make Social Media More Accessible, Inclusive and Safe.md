---
title: Can AI Help Make Social Media More Accessible, Inclusive and Safe?
topic: industry
subtopic: trends
secondary_topics:
- product-engineering/security
summary: Examines AI applications for social media accessibility, inclusion, and safety,
  focusing on responsible deployment tradeoffs.
source: arize
url: https://arize.com/blog/can-ai-help-make-social-media-more-accessible-inclusive-and-safe/
author: David Burch
published: '2021-12-14'
fetched: '2026-07-11T04:44:00Z'
classifier: codex
taxonomy_rev: 1
words: 1596
content_sha256: 845ccc18bbbeef6fb76be72ab0dfdfc32127728ac8b10ef2ffa6019ca95c0fed
---

# Can AI Help Make Social Media More Accessible, Inclusive and Safe?

![ramit-sawhney-sharechat ramit sawhney on ai ethics arize ai](https://arize.com/wp-content/uploads/2021/12/ramit-sawhney-sharechat.png)

              # Can AI Help Make Social Media More Accessible, Inclusive and Safe?

### Looking outside the U.S. yields fresh perspective — and hope

Ramit Sawhney is Lead AI Scientist at ShareChat, a rapidly-growing social media unicorn valued at over $3 billion. While ShareChat may not be a household name in the U.S., it is in South Asia. In all, over 160 million active monthly users — including millions in hard-to-reach areas with low connectivity — rely on ShareChat to share short videos, audio, photos and text with friends and family in over 15 languages.

With its roots firmly in India, ShareChat has a unique vantage point on the issues of ethics and fairness in AI. It’s also the perfect home for Sawhney, who has written extensively about bias in machine learning with research papers on topics ranging from using machine learning (ML) to [detect offensive Hindi-English](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kPmmgjoAAAAJ&citation_for_view=kPmmgjoAAAAJ:u5HHmVD_uO8C) tweets to multimodal neural financial models accentuating gender-based stereotypes. As the U.S. grapples with potential societal harms in social media in the aftermath of the recent [Facebook files](https://www.wsj.com/articles/the-facebook-files-11631713039), this interview comes at an auspicious time for AI practitioners and industry watchers alike.

**Arize: What’s your role at ShareChat and how does the company leverage AI in production today?**

**Sawhney:** One of the key problems that ShareChat is trying to solve, and even the unique selling point of the product, is that it targets a very different demographic than you might see with other social media platforms. From a NLP perspective, the different demographic here represents low resource domains, Indic languages, tier two and tier three cities or regions in India where English is never spoken. In fact, with India being such a huge country, there are more than 100 different languages and dialects within just India itself. So the problem that arises is that we have a huge population, but there is not one single language for one single mode of communication that all of the people use.

And that’s where ShareChat comes in, with a product that uniquely caters to this diverse audience. The goal for our data science and ML engineering team then becomes: how do we democratize AI to create a social media platform for people in low bandwidth areas — people with totally different languages, in places where advertisements might be totally different?

Prior to joining ShareChat, much of my published research focused on social media usage. I’ve long been interested in leveraging social media and AI to build a safer and more accessible space online, which means combating problems like preventing abuse and hate speech, identifying potential suicide ideation, and more.

At ShareChat, the goals are very similar. ShareChat wants to build a more inclusive, highly accessible and diverse platform. AI is central to those efforts. We’re dealing with billions and billions of videos and pieces of user generated content on any given day, and the biggest problem we’re helping to solve is how to decide which videos should be served to the user.

That is my focus as lead AI scientist at ShareChat: leveraging AI for in-session personalization to deliver the best feed for all users across different languages, dialects and regions of India.

**Arize: What are some of the biggest takeaways from your research and real-world practice with regards to ethics and fairness issues in AI? **

**Sawhney:** When most people initially start out in ML and AI, they’re almost always chasing the best-performing model — at times forgetting that other dimensions exist. Later, you realize that the best performance today might not necessarily be the best thing that translates to a product tomorrow.

My perspective as a researcher informs my approach at ShareChat. It’s about having the right mindset, such as when you’re trying to consider whether gender should be a parameter in your neural network model. If I were not exposed to research, I might have simply treated gender as a binary variable, or I wouldn’t have even considered it as any special kind of feature. But after talking to different people globally, understanding how the community infers more sensitive aspects, I started going beyond and asking the right kinds of questions and listening. Such as: should gender just be a binary kind of label or should we think of it as a more diverse spectrum? Or how privacy-conscious do we want our models to be? We understand that the more data you can feed to these models, the more they can learn about the users to deliver the most relevant ads or the most engaging feed, but are those numbers single handedly enough to make sure that that’s the best user experience?

Within India, our cultural diversity and richness makes these issues even more complicated because it becomes more difficult to slot users into certain categories. At ShareChat, we’re making a conscious effort to be more inclusive and serve more diverse intent, keeping in mind that the best experience does not need to be just the best and easily quantifiable results — it could also be a more privacy-conscious, or more inclusive, or safer, space online.

**Arize: Do you think companies or organizations should incentivize or have a systematic approach to tackling things like bias or hate speech, or global governance of AI in general? **

**Sawhney: **This is a really relevant and important question for companies. At startups in particular, you often have a great open and collaborative kind of environment where competing pressures can make this question tricky. Companies find themselves asking: where do you want to push for performance and the best models first and where do you prioritize things like combating hate speech or toxic behavior? And is creating a safe space afterthought? Sadly, it is at some companies. The great part about ShareChat is that creating a safe space comes first, especially given our broader mission.

Of course, it’s a complicated task. With content moderation at ShareChat, we’re not just looking at abuse detection in text — which is something I’ve done in my prior research — but also audio detection. So what about potentially profane or abusive language in any kind of audio and video for that matter? What about not-safe-for-work kind of videos, which could vary all the way from extreme violence to content that is just not appropriate?

Each of these questions presents a unique AI challenge, which opens up a very interesting dimension of how we want to have governance over the app. My personal opinion, which parallels ShareChat’s governance, is that safety should go hand-in-hand with things like performance and model development because at the end of the day even though it might impact the numbers it does create a much safer and open atmosphere. I’ve always preferred having a longer term vision. The best product or model is not necessarily the one where the immediate numbers are the best.

When taking on these issues, it’s also important to look outside the company for perspective. One of the first things I did upon joining ShareChat was to launch an [ AI Abuse Detection Challenge](https://sharechat.com/events/abuse-detection-challenge), which is open for global participation, to combat abusive text in over 15 languages.

In devising this challenge at ShareChat, I also wanted to realistically incorporate human content moderators as part of the process because it mirrors what happens in the real-world. I don’t think we’re at the point where AI can completely replace humans in safety detection or even more sensitive issues like suicide ideation detection. But we’re at a point where AI can be the first step, reducing the load and mental strain on annotators and moderators. The ethics issues around subjecting human moderators to this content is also critical to keep in mind even though it’s not directly tied up to the performance metrics of a certain product or AI model.

**Arize: How do you think about ML monitoring and observability of models in production? **

**Sawhney:** It’s an interesting question because it’s very different when you come from a research background into the industry. In research, you’re not running a lot of models in production. It was very different to come into ShareChat and see a bunch of different models running simultaneously at this massive scale every single day.

So while a researcher might not need a dedicated application for ML monitoring or [ML observability](https://arize.com/ml-observability/), when you start looking at tens or hundreds of models that are running every day with huge amounts of features, you start realizing that you need different kinds of monitoring applications around these systems. You want things in monitoring applications like alerting, the ability to track feature and other [drift types](https://arize.com/model-drift/) and the ability to compare lots of models from one place.

And that goes hand in hand again with a whole idea of being more systematic about our models. A lot of times, at least from a research perspective, we give a lot of value to the ML model architectures and designing fancy, complex architectures. But a bigger problem in industry is: how do we maintain this, how often do we want to retrain this and how often do these models start drifting away from the behavior that we intended? That’s where monitoring has become essential.

With the amount of scale ShareChat has in terms of data and its models, it becomes really important to not just focus on the actual model architectures but also on maintaining, deploying, and monitoring models. From that perspective, MLOps and ML monitoring platforms are definitely the future because ML itself is the future — and we need the infrastructure to support it.
