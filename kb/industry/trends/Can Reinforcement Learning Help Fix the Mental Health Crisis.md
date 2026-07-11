---
title: Can Reinforcement Learning Help Fix the Mental Health Crisis?
topic: industry
subtopic: trends
secondary_topics:
- models/reasoning
summary: Application-oriented discussion of reinforcement learning in mental health,
  useful mainly as industry context for AI use cases.
source: arize
url: https://arize.com/blog/can-reinforcement-learning-help-fix-the-mental-health-crisis/
author: David Burch
published: '2022-06-09'
fetched: '2026-07-11T04:45:06Z'
classifier: codex
taxonomy_rev: 1
words: 2621
content_sha256: fda310a657a7923651bea51ab3026150007c7004d37b3db7d1521751008eade9
---

# Can Reinforcement Learning Help Fix the Mental Health Crisis?

![stefano_goria_blog2](https://arize.com/wp-content/uploads/2022/07/stefano_goria_blog2.jpg)

              # Can Reinforcement Learning Help Fix the Mental Health Crisis?

Stefano Goria is Co-Founder and Chief Technical Officer (CTO) of Thymia, a company aiming to make mental health assessments faster and more accurate through an approach that combines video games based on neuropsychology with analyses of facial microexpressions and speech patterns. Founded in 2020, Thymia’s arrival comes at a time of great need given the [growing](https://www.wsj.com/articles/teens-mental-health-suffered-during-covid-19-pandemic-cdc-study-finds-11648763344) [mental health crisis](https://www.nytimes.com/2022/04/23/health/mental-health-crisis-teens.html) globally in the wake of COVID-19. As Thymia’s technical co-founder, Goria leads the charge in developing the AI systems that undergird the company’s end-to-end solution to empower clinicians. With a PhD in theoretical physics and nearly a decade building machine learning (ML) models for Citi and J.P. Morgan, he brings a unique perspective and array of skills to the task.

**What is your career background and what is the inspiration behind Thymia?**

I have a background in theoretical physics. I did my PhD researching the theoretical aspects of the Higgs Boson search shortly before the discovery of the particle. After graduating, I worked as a quant for eight years – first at a software company and then at large American banks, including Citibank and then J.P. Morgan.

In these roles, I did a wide array of modeling tasks from classical statistical learning all the way up to reinforcement learning (which I like a lot). I also built up my machine learning and modeling expertise, sharpening my skills to ensure that I can bring cutting edge research all the way into production.

Although these eight years of my career were very satisfying from a learning and technical point of view, I found myself yearning for a higher purpose and calling. One day I looked around the trading floor at J.P. Morgan and saw a lot of super smart people incredibly focused on better shuffling money around and wondered: why am I doing this?

It was then that I decided to put my energy and drive into something else, leaving in March of 2020 to join Entrepreneur First. Their approach is to invest in people before a company exists, bringing together a cohort with diverse backgrounds and placing them in a structured environment designed to yield co-founders ready for venture capital investment. It’s a difficult proposition to make work, but it was fantastic for me because I got to meet my co-founder Emilia Molimpakis, who had the initial idea and spark for Thymia. In seeing her pitch, I realized immediately that it would be the perfect way for me to use what I know about complex technology and modeling in a purpose-rich space to help people.

My co-founder has been exposed to this domain for a long time as an academic, pushing her to bridge the gap between what’s known today in research essentially and what’s actually using clinical practice. There is a big tension between what can be done and what is actually done, which is why Thymia exists.

Today, we have more significant funding and are hiring to expand a team of 12 people. Things are running faster and changing a lot – at the beginning, I was coding everything and am now leading a small team – and in a few months it will probably be even bigger.

**Can you tell me more about the problems Thymia is trying to solve in terms of harmful biases or data quality in mental healthcare? **

Mental health care is in crisis today, and it’s reaching a fevered pitch as the demand for help far outstrips supply. Part of the problem is that mental health care is massive and very complicated. Thymia is attacking a specific angle of mental health care: helping clinicians have objective measures of things that thus far have been very subjective in two ways: what the patient is reporting about themselves and what the clinician is perceiving as the underlying cause.

This is a big problem because if you don’t have solid objective metrics to identify symptoms, then you have very weak instruments to tailor treatment. The net result is that even though you may see a psychiatrist and on day one they tell you that you are depressed, for example, it still takes a long and painful time to get to the correct treatment. A big reason why is that it is so hard to do something simple like see if something is working or not.

That’s the core problem we are tackling. There are a wealth of things that can be objectified that are going to inform the clinical path and clinical decisions on what the best treatment is for a specific individual, but these things unfortunately have not always been used. There are things that are known in research, but are not yet making it into the clinical reality. That’s the big difference between a clinician working in physical health and someone working in mental health; you cannot today ask for a blood test for mental health – it doesn’t exist – and that’s so important because it can give you a strong handle on how things are going. It’s not removing the human element, it’s actually expanding the time for a clinician to dedicate to the human aspects instead of trying to guess things that can be measured.

So the core problem we’re tackling is improving the quality of assessment and measurement of core symptoms relevant for mental health diagnosis, starting with depression.

**How does AI fit in and what types of models are you training and deploying into production? **

What we’re doing is extremely exciting from a scientific point of view. From a data perspective, we are looking at three main modalities of data. The first is video, where we examine snippets of recordings and focus on micro-expressions – which can be encoded in a certain way that are called action units – and then examine things like how much you move your head, whether you’re looking at one part of the screen, whether your eyebrow is raised, whether you’re smiling, and more. We also look at speech and how someone speaks, so the energy and the pace and many other features. Some of them are intuitively related to depression (such as a slower pace and lower energy), while other connections are less intuitive but nonetheless there.

Then we look at the content. What someone chooses to say is very informative – when you have a free speech-eliciting task like describing something that you see on screen, the way you speak about it is very telling. Are you, for example, using a lot of personal pronouns, is there an excess of “me” with respect to the broader population, are you more concerned about events in the future than in the past – these are all very important things that we can capture.

Then we look at behavioral data, which is everything that happens on-screen that can be translated into some action with a timestamp. So you can imagine a constant stream of data when you do something on screen. We do this when we ask people to play simple video games, so we know when they click how they react to specific inputs. The pace, the number of errors in the game, the reaction times, and other features are extremely telling in creating symptom profiles.

These three modalities of data are very different, which pushes the models handling this to the limit of what is today mainstream AI. So if you were to look under the hood, we’re using a vast collection of techniques – some of them are in the deep neural net area, while others are a lot more explicit feature engineering that is relevant to handling a large set of multimodal timed events – so it’s a combination of different techniques. Sometimes, it’s more relevant to look at unsupervised learning – so we look at clustering some of the features and mapping them to a cluster of symptoms – and other times we rely on supervised learning, where we rely on architecture that we use to change and fine tune to our models.

It’s an interesting area where we might have a massive amount of features, but not a massive amount of data – so we need to be smart because it’s not just a matter of running the machine long enough to get the right answer. There is a lot of understanding the domain and knowing what works and what doesn’t, which is in itself something super fascinating that brings me a lot closer to how I was doing things as a quant in finance where building a model that made sense – not just gave out the right answer – was one of the key requirements.

On top of that, we’re now introducing reinforcement learning, which is fantastic for me personally because it’s something I enjoy doing – including in fields like biodiversity, where I recently [authored a paper](https://www.nature.com/articles/s41893-022-00851-6) that outlines an approach to decide how to best protect geographical areas to maximize biodiversity over time.

We also use reinforcement learning at Thymia. In particular, we are targeting anhedonia because losing pleasure in doing things is one of the key symptoms of depression. One neat way of tackling that is playing games. These can be very simple games where a player chooses between different options and does not know in advance which one is good or less good. This offers a very nice mathematical representation where the game itself can be solved as a reinforcement learning problem. So what you do is compare the way the human is playing the game to the optimal way a machine would play the game to maximize the reward. Comparing these is very informative and essentially measures how much someone is enjoying the exercise.

**Having been founded in 2020, you must have an interesting purview on mental health in the wake of the pandemic – have you seen any underlying shifts or  data drift since starting Thymia? **

We were founded in the middle of the pandemic, so this has been our only reality. We’ve seen companies in the mental health space really change the way they’re providing care and navigate a massive spike in demand. Because of the need for remote care, there is a lot less friction in trying new tools. It will be interesting to see in two years time what the real underlying changes will be.

**How do you navigate labeling and ground truth?**

In terms of labeling, the data that we are producing generally falls under three categories. The first category is metrics for understanding symptoms – for example, we may be measuring speech rate or the energy levels in your voice. These are objective things that can just be measured as part of an AI-driven mental state exam, and generally there isn’t a labeling issue with this category.

The other categories are at the symptom and diagnosis label level. First, I should stress that what we want to produce is symptom measurement as opposed to looking at diagnosis because this is what is relevant for clinicians – they really want to have a stronger handle on symptoms, because that is what drives treatment, as opposed to a plain diagnosis label. So we may use a diagnosis label, but this is to help the models and is not really our main focus.

When we approach symptoms as a supervised problem, then we necessarily have to rely on someone labeling the data – either the patient and the clinician. It might seem like a circular loop to try to get rid of subjectivity by asking a subjective question to a patient to train models. The reality, however, is that it’s not a blocker for the model to work when you have thousands of these data points. On the flip side, we also ask clinicians their view. While it’s a subjective measure, it’s a high quality subjective measure given the clinician’s domain expertise.

In building Thymia and thinking about how to improve this data over time, we decided to go and embed the core activities that we administer and the core models in a bigger platform where clinicians will do all their interactions with the patients, so that there’s a wealth of extra data that can be used for understanding the full picture.

We are also a kicking off unsupervised learning exercises as well. While it’s very early stages, it’s surely the way to go when the training data will grow. It’ll be a lot more interesting than having a cluster of features that speak direction to a cluster of symptoms without us explicitly labeling them.

**How do you approach  model monitoring?**

Infrastructure. Since Thymia was founded in 2020, we are beneficiaries of the fact that MLOps technology and knowledge has evolved and become well understood. We started out with a well-structured workflow – from data to modern prototyping to production quality models, deployment in production, and ongoing monitoring infrastructure – from the very beginning. This certainly can’t be taken for granted with an older system; companies starting out today are in an advantageous position because they already know what’s important to track.

We think of monitoring in two axes: auditability and monitoring. With auditability, it’s critical to demonstrate that the model is built on data that is collected in an ethical way, with clear consent. With monitoring, we want to see whether the model quality and performance over time.

**What do you think some of the unique ethical concerns are of AI in mental health care? **

Broadly, this is a massive topic. We are embedding a few things as core at Thymia including ethical use of technology, informed data use, and more.

One of the key things worth emphasizing that we’ve done since the beginning – and we’re making sure this is clear and enforced going forward – is guaranteeing patients that the data generated by Thymia’s models will only ever be used in a clinical path and will never be shared with third parties, which is unfortunately [common](https://www.wsj.com/articles/you-give-apps-sensitive-personal-information-then-they-tell-facebook-11550851636) [today](https://www.mobihealthnews.com/news/study-popular-womens-health-apps-dont-meet-basic-privacy-security-standards) with popular mental health apps. We make sure that patients know very clearly at the outset that Thymia is here to help their clinicians and there is no other hidden aspect.

Ultimately, we feel it is important to build a technology that can help across different modalities. If someone is not comfortable going on video, maybe they are comfortable using their voice or playing a video game. No matter what, each is a great data stream to us and we will always offer communication, choice, and transparency.

Broadly, we’ve been following guidance from the UK government and Alan Turing Institute’s principles for the responsible design of AI systems, which is a great starting point for organizations to do the right things from the beginning. We also follow frameworks in healthcare and are exploring potentially certifying parts of the platform as a medical device.

**What is the common thread between mental health, biodiversity and financial services? **

It is always a source of satisfaction to see something I learned in one place applied in a different one and learn something new. Every time I apply it is so exciting, because you learn something more about how the model works and something more about the domain itself when you frame a problem in a slightly different way.

The applicability of reinforcement learning. Also, working on complex modalities that have non premium dependencies is another commonality. And if you like finance and health, another aspect is both are very regulated so it pushes you to do things right from the start in terms of observability, explainability, and auditability. The common element is it’s a regulated space and you need to be able to answer questions on what you are doing.
