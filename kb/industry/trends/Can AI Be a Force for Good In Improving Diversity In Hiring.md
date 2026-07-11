---
title: Can AI Be a Force for Good In Improving Diversity In Hiring?
topic: industry
subtopic: trends
secondary_topics:
- product-engineering/security
summary: Discusses AI in hiring and diversity, with emphasis on fairness, responsible
  deployment, and social impact risks.
source: arize
url: https://arize.com/blog/can-ai-be-a-force-for-good-in-improving-diversity-in-hiring/
author: David Burch
published: '2022-07-11'
fetched: '2026-07-11T04:45:20Z'
classifier: codex
taxonomy_rev: 1
words: 2134
content_sha256: c448d9bafc9fc0a436d8f8785e97b96e1b0034a6d32a1740b5a15d88df25a948
---

# Can AI Be a Force for Good In Improving Diversity In Hiring?

![Khyati_Sundaram-blog_image (1)](https://arize.com/wp-content/uploads/2022/07/Khyati_Sundaram-blog_image-1.jpg)

              # Can AI Be a Force for Good In Improving Diversity In Hiring?

Khyati Sundaram is the CEO and Chairperson of [Applied](https://www.beapplied.com/). Founded in 2016, Applied’s mission is to be the essential platform for unbiased hiring. To that end, the company offers a comprehensive hiring platform relied on by clients like Ogilvy and UNICEF to improve diversity by applying lessons from behavioral science, such as anonymizing applications and removing gendered language from job descriptions. Throughout the company’s history, Applied has been hesitant to use machine learning on its platform given the potential of AI to [amplify the very harmful biases](https://www.thomsonreuters.com/en-us/posts/legal/ai-enabled-anti-black-bias/) the company is seeking to prevent. However, after years of research, Applied now sees a disruptive opportunity to train and deploy models to help ensure that humans make fairer hiring decisions at scale. This updated offering could not come at a time of greater need given the continued lack of diversity at most global enterprises and technology companies.

**Can you introduce yourself and share some of the inspiration behind Applied?**

I am the CEO and Chairperson of Applied. My background is quite mixed: I am an ex-economist and ex-investment banker with years of experience as an entrepreneur working with data science and technology. Prior to Applied, I started and led a company that used machine learning and automation to build more sustainable supply chains. My inspiration in leading Applied comes from my own personal journey. Back in 2018, I was winding down my first startup and starting to look for jobs. As I put myself back on the job market, a nightmare unfolded. Despite having an upward career arc from economics to banking and then starting my own company, I could not find a job for over eight months. That experience incentivized me to read about the hiring market, how people are hiring, and technology solutions. It was then that I realized that everything about hiring was completely broken. This is not just my own singular experience; there are quite a few people in the same boat who are unable to get jobs despite having all the skills – and that has to do with the systems that perpetuate systemic issues along with the lack of level access to economic opportunities.

**What are some of the biases riddling the hiring process today? **

We all have cognitive shortcuts, or what we call biases or heuristics. It’s worth clarifying that systemic biases are not always good nor bad; they are contextual. If you are walking down the street and there is a car hurtling toward you at 100 miles an hour, for example, you will likely move out of its way. This mental shortcut is itself a bias, and it serves you well in that moment and in that context. But if you apply a similar shortcut in the hiring context, it can have catastrophic consequences. 40 years of academic research and now almost five years of data from Applied clearly show that a lot of the decisions that humans make on other humans in areas like hiring, promotions, salary negotiations, and progression are all rife with bias. These are unconscious biases, so we can’t really train them out of existence because they are in our heads – evolutionary and systemic. Instead, we need to empower people and give them guardrails and systems to protect themselves and others.

In terms of what these biases look like in hiring, there are many examples. A simple one is affinity bias: if you went to the same school or if your name sounds similar to another person, you instantly like them. There is nothing logical there – it’s a tribal mechanism – but it means that you might call someone for the interview whether they are suited for that job or not. Another example is stereotype bias, where someone might say “women are bad at math.” Categorically that’s not true, but when we prime women to say they are bad at math or technology, many women don’t end up choosing those careers. Two other related biases include group think – when the desire for adhering to the group decision drives out good decision making – along with bias of the loud, where a certain individual might sway the group decision. Finally, another source of bias that I always find very fascinating is when people list personal interests or hobbies on their resumes or CVs. This can interfere with the hiring process in a number of ways, resulting in misguided assumptions about the candidates’ resilience or biasing the perceptions of hiring staff through shared interests.

There are mountains of evidence that tell us we’ve been hiring incorrectly for a long, long time.

**How has AI amplified this or made the problem worse? **

Biases can occur in various parts of the journey to shipping an ML model. It can exist in the generation of the dataset, it can exist in the training and evaluation phases of a model, and on through the ML lifecycle. [Arize’s work on this](https://arize.com/blog/machine-learning-bias-tracing/) is spot-on because understanding where the bias is present in production is really important.

One of the biggest historical [examples](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G) of AI making the problem worse was at Amazon, where a resume-screening algorithm essentially taught itself that male candidates were preferred and downplayed common attributes like coding languages while emphasizing words preferred by men like “executed” or “captured.” The lesson here is that if you take in historic data without really putting countermeasures into your model, then more likely than not you are going to keep adapting and replicating previous winners – and in most organizations, previous winners are white men. That’s what is happening with ML models today. While addressing this is paramount, it’s also important to note that this is just one piece of the puzzle. Most people are optimizing for this part and forgetting the rest of the story.

**How is Applied helping companies reduce their blindspots in hiring today? Is killing the resume in favor of skills tests a big part of it?**

Nearly every piece of information that sits on a CV is noise and is not predictive of whether a person can do the job. This is the fundamental premise of Applied: can we take away the noise and replace it with something better, like skills-based testing? We see Applied as a decision intelligence system which at every point of the funnel is trying to give you the right information while taking away the wrong information. We think about it in terms similar to the world of MLOps: Applied is providing better observability and [explainability](https://arize.com/blog/model-explainability-primer/) throughout the hiring funnel, helping hiring managers take better care about the quality of the match.

At Applied, we take a very considered approach about where we use AI. It’s worth emphasizing at the outset that we are not using any AI or machine learning to screen a hiring decision, so whether you get a job is not dependent on a particular feature of an algorithm – it is still humans making those decisions. That is because I have a high bar for when to release an ML model, even though it might be an improvement compared to everything else out there.

Today, we are using or experimenting with machine learning in three areas. First, we use ML to help in stripping away all of the information that is causing noise in the hiring funnel. On a resume that would include your name, your university, your age, how long you worked at a certain company, and other variables that have been debunked by science to be predictive of talent. Once we remove all of that, we use Applied’s library of skills that match to a given job title. So if I have a sales manager job, for example, can I use ML to predict the five top five skills needed for that hire? Once you are ready to test on skills, machine learning can also help in making the scoring more effective. In today’s world, most of the status quo tools are using some kind of keyword scoring or keyword search, and that is all based on historic data or a notion of what good looks like. As a result, what ends up happening is that a model relies on really noisy signals.

Using machine learning to make scoring more effective is something we are currently testing. We intentionally decided to not use neural networks for this, because we know that every other company has tried that and it would likely match a pattern and people who have done well in certain kinds of tests will likely also do well on the future tests. We are currently testing a genetic algorithm, replaying all the jobs on the platform to see how the model would impact job outcomes. We haven’t deployed this into production yet because we’re still in the testing phase.

Finally, there are models we use in sourcing such as our tool for writing inclusive job descriptions. The language used to describe many technology jobs was developed back in the early days of modern computing when homogeneity was the norm and racism was much more explicit and often went unchallenged. Today, we’re challenging that kind of language. It’s not embedded in code itself, of course, but in how we talk about these concepts. So we are using machine learning to help in stripping out potentially problematic words and making the funnel more effective and more robust.

**One problem we see is that a model may be perfect in training or validation, but still has a  disparate impact on a protected class once deployed into production. Is that something you see?**

Definitely, and it’s super difficult to solve. I alluded to the fact that we can build counter-biases into the data during the training stage, but you still have to test in a real world environment which is difficult because it is high stakes. One example of this that I saw recently was a company using a model to optimize programmatic buys of job advertisements. Three months into the campaign, they realized that women and ethnic minorities were not being served with ads. This happened not because anyone sat there at the pre-production or production stage and planned it that way, but because women and intersectional women in particular were more expensive to reach with ads. So a model optimizing on cost-per-click might end up reaching absolutely no intersectional women at all. This speaks to the importance of full testing in the real world and the importance of observing models.

**What will it take for diversity to start getting better given how pervasive and systemic the problem continues to be at large companies? **

Part of the reason the problem persists is that it has been a sidebar. It’s conversations that happen on the sideline with minorities, and there is no real accountability with the majority. Today, I still have to apply to five times the number of jobs as a similarly qualified white man.

Making progress starts with a conversation and real understanding and empathy. The second piece – and this is where I am much more optimistic – is optimizing the interplay between human judgment and machine learning data. Where do we use gut and human judgment and where do we use machine learning data, and how do we augment each other? We haven’t done that well in the past. Most of the hiring automation tools you see have completely removed human judgment in areas like screening, and models have optimized for the wrong data.

This is partly a process problem – the hiring process is imbued with biases throughout and there is no accountability on outcomes and no mechanism to tell people exactly where they are going wrong. This is what we are trying to solve at Applied. Across the hiring funnel, it’s about saying to someone in the moment something like “you just asked the wrong question and caused half of the women to drop from the interview stage.”

**What’s next for Applied?**

In MLOps and DevOps, observability is a key mechanism and guardrail against failure. That’s what we are trying to build at Applied for hiring – a platform where everyone cares deeply about the quality for the match and knows what high ROI looks like. I also want Applied to be a mechanism for education, where we are not just giving this market a solution but also a bigger stream of consciousness. In hiring, we all know that we have been doing things incorrectly for a long time. There is a distinct need to improve the way hiring works, not just for the bottom line but also to become a more heterogeneous and inclusive society. My dream is to not only build a great company, but also a society-wide expression of inclusivity.
