---
title: 3 Key Concepts for Creating AI Product Experiences
topic: product-engineering
subtopic: ux-patterns
secondary_topics: []
summary: Covers product-design principles for understandable AI experiences, including
  how users form trust and interpret system behavior.
source: cresta
url: https://cresta.com/blog/keys-for-creating-understandable-ai-product-experiences-2
author: null
published: '2020-06-30'
fetched: '2026-07-11T04:00:31Z'
classifier: codex
taxonomy_rev: 1
words: 1424
content_sha256: 1050528b001b7d3c81f65e5dd9325aac999888800b3db459fda611b5e6d0ac48
---

# 3 Key Concepts for Creating AI Product Experiences

AI-powered products are more prevalent than ever before: automatically organizing your photos, driving a car without any human input, and helping you craft a perfect email. These three examples all use AI but the product experience and constraints for each are vastly different. As more and more products use AI, it’s important to ensure the product experience and constraints align with the AI's application.For example, consider the automatic organization of photos. Here, accuracy doesn’t need to be perfect. If you are searching for “dogs,” it's ok to return lots of of dog-like-photos as it is relatively easy to scroll and find the exact photo you're looking for - this is called a “high recall” approach.In this post, we'll cover three key product design concepts to consider when developing an AI product:

- **Precision vs. recall:**how accurate does the experience need to be?
- **Fallbacks:**what is the alternative if the AI output is not correct?
- **Control:**can users understand what is happening and give feedback?

[caption id="attachment_22834" align="aligncenter" width="750"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f214ac8f9fdcc37db15_68135f234c7f2a2ec675e895_pizza.avif)

When is it more important to not miss opportunities, and when is it not alright to pick the wrong result?[/caption]

## Precision vs Recall

To illustrate the concept of precision vs. recall, let’s use a common example: image classification. Say you have a cutting-edge state-of-the-art AI model that classifies images as pizzas or not pizzas. With this model, you have a set of test data to help you evaluate how good your model is. You show it 50 images that are pizzas and 50 that are not pizzas. You then run the model on these images and look at the results.**Recall** asks: How many images did the model classify as a pizza in total?" Say your model classified 40 as pizzas, recall would be 40/50 = 80%.**Precision** takes all of the images you classified as a pizza and asks: How many of them were actually a pizza? If only 30 out of those images classified as pizzas were actually pizzas, precision would be 30/40 = 75%.High precision means serving only relevant answers at critical points. High recall means not missing correct answers. The needs of your AI application will shape the priorities of your model.High recall is used in applications where the user picks a result from a select few sample sizes. The cost of missing an answer is greater than the cost of getting it correct on the first try. Google photo search for example serves many results, one of which is the correct answer, and the user can select the result she is looking for. User success in this scenario is finding the right photo.Tesla’s self-driving cars drive on the other hand, are examples of high precision design. These cars need to avoid accidents despite not having access to a large database of sample crash data. Considering the size and weight of a car, a car's onboard systems must take extremely severe actions, and do so with significant foresight, in order to avoid an accident. For this reason, the system must precisely predict an accident is going to take place.[caption id="attachment_22835" align="aligncenter" width="600"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f214ac8f9fdcc37db08_68135f234c7f2a2ec675e886_does-the-auto-pilot-feature-strike-again-your-guess-is-as-good-as-ours_3.avif)

Even the most sophisticated models still need to be tested against real world data.[/caption]

## Fallbacks

Spoiler alert: AI systems aren’t perfect. If your product doesn’t account for this, “you’re gonna have a bad time.” It’s important to consider the alternative outcomes for when your AI predictions fail.Let’s look at two examples: Gmail’s Smart Compose and Amazon Echo.Smart Compose is a feature in Gmail that helps complete phrases as you are typing. If there is a bad prediction, say you are saying “Good morning” and after “Good” smart compose comes back and shows “evening”, it’s not a big deal. You can just continue typing “morning” and it won't negatively impact the experience.For Amazon Echo on the other hand, as an audio-based system the fallback is more difficult. Echo has to understand what you are saying. If you speak to it and say “Play the latest Drake album” and Alexa is unable to understand you, there isn’t an alternative. The voice fallback is much harder to deliver and very frustrating when it goes wrong. For this reason, the best fallback is often silence. For automated phone systems, another example of an audio-based system, the fallback is being transferred to an operator.

## Control

It's common to say AI is “like a black box” - a model returns a prediction but does the user understand why? This is where the concept of control comes into play. Offering users some insight and input into the system is a great way to let humans participate in the intelligence.[caption id="attachment_22837" align="aligncenter" width="300"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f214ac8f9fdcc37db02_68135f234c7f2a2ec675e883_netflix-rating-system-1024x475-1-300x139-1.avif)

A great example of communicating to the user how their feedback can impact the model.[/caption][caption id="attachment_22838" align="aligncenter" width="300"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f214ac8f9fdcc37db05_68135f234c7f2a2ec675e880_pasted-image-0-300x63-1.avif)

Netflix is always connecting the dots between subscribers who like the same shows.[/caption]A good user experience with control is Netflix recommendations. Netflix helps users understand why they are getting results. By presenting users with a list of previously watched titles and letting users rate titles, Netflix offers users a feedback loop to influence and improve their product experience. More so, the product experience gets even better the more you engage with ratings.Counter to this example are ride sharing services like Uber and Lyft. When it comes to shared rides, these services do not allow users to influence their rides. This leads to a rather painful rider experiences -- many people know the feeling of passing their house to pick up another passenger, only to be dropped off at home 5 minutes later.[caption id="attachment_22839" align="aligncenter" width="300"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f214ac8f9fdcc37db12_68135f234c7f2a2ec675e88b_Lyft-screenshot-1.avif)

What if Lyft let users see and control the experience they’re about to get?[/caption]One potential feedback loop ride sharing services could introduce is to allow users to section off streets the rider wants to avoid on their daily commute. Another option is to more stringently stay on the previewed route that users see when they initially book their ride. If ride sharing apps let users select rides based on a route preview, users could make more informed decisions on the rides they take (instead of sitting through poor experiences and asking for refunds).

**Applying these concepts at Cresta**

So how do we apply these principles at Cresta? At Cresta, our live coaching AI provides sales and support agents recommended responses and behavioral coaching in real-time, during customer conversations. For us, it’s critical that our users trust the insights our AI generates. In terms of AI guidance - relevancy increases trust, and trust increases usage.Here are some examples of these principles being applied in our product:

- **Precision vs. recall:**We are constantly balancing precision and recall. Let's consider suggested responses where we present agents with 3-4 recommended responses to send to a customer. If precision is low, then most of the suggestions are irrelevant, which erodes the trust of the agent on the software; if recall is low, then we miss opportunities to effectively assist the agent. In the case of suggested responses, because we can present multiple responses to the agent, we lean towards recall. This balancing act between precision and recall happens throughout our product. Our engineers are constantly finding ways to improve precision and recall while balancing their respective tradeoffs.
- **Fallbacks:**Knowing that our AI won’t always recommend an agent’s preferred response, we let agents save their favorite responses using hotkeys. This way, their favorite responses are easily accessible when the Cresta’s recommendations are not the perfect fit.
- **Control:**Cresta lets managers influence the agent coaching experience. Much like the feedback loop the Netflix’s like button offers users, Cresta lets managers select 2-3 coaching behaviors which they would like Cresta to prioritize as part of an agent’s coaching routine. Cresta then systematically tailors the- [agents' coaching](https://cresta.com/product/)routines based on these preferences.

## Summary

In summary, as more and more products utilize AI, it’s important to keep three key user considerations in mind:

- **Precision vs. recall:**Deciding on the right trade-off between recall and precision
- **Fallbacks:**Ensuring that there exists fallbacks as an alternative to complete the task when predictions fail
- **Control:**Giving users control through the use of feedback systems

Not properly considering these can lead to frustrating user experiences and in some cases (such as self-driving cars), the stakes could be really high.At Cresta we are using these principles to inform a great user experience and help agents become experts on day one. If you are interested in defining cutting edge AI + HCI paradigms, please [explore our careers page](https://cresta.com/careers/).**Thanks** to Jessica Zhao, Amy Lee, Alex Roe, and Osman Javed for edits and reviews.
