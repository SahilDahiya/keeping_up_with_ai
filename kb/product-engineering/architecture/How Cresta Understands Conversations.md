---
title: How Cresta Understands Conversations
kind: blog
topic: product-engineering
subtopic: architecture
secondary_topics: []
summary: 'Walks through the three NLP layers behind real-time agent coaching: rule-based
  keyword matching (cheap but breaks on ambiguity), deep-learning semantic understanding
  that reads intent from word order and relationships, and context tracking across
  both speakers. Uses a concrete ''I need to ask my spouse'' example where keyword
  matching misreads a buying signal as an objection.'
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/cresta-understands-conversations
author: null
published: '2022-01-06'
fetched: '2026-08-20T06:10:33Z'
classifier: claude
taxonomy_rev: 2
words: 1045
content_sha256: c54fb5926b5ad4450b2a8667105d83f4a1ca92e45e5c1273b03f3b8f4411dc71
---

# How Cresta Understands Conversations

Artificial intelligence (AI) has become a critical component of the modern [contact center](https://cresta.com/solutions/). This is especially true of real-time coaching solutions, which rely on AI to understand conversations and assist agents in real-time. But AI has become such an overused and abused phrase, it’s difficult to separate the signal from the noise.At Cresta, one question we often get from prospects is “What sets one solution’s AI apart from another?” The simple answer? It's [complicated!](https://techcrunch.com/sponsor/nvidia/how-the-revolution-of-natural-language-processing-is-changing-the-way-companies-understand-text/?guccounter=1&guce_referrer=aHR0cHM6Ly9jc2UuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAcHcT1AKoY5u_x_AOEyFPWQyJk4dhhGEKl_WWPfEKqS4dp5PbfMxVSR3DlAeWF5-kcbroeMRrl4Wjyl-jyLbCte2MHRAvHwpm58Nv9hzTrPLiOCXXY1baQJXJK4qJkg2cSJEsvwuSzon7JkHm74bx8Qa5krnoLev_eaQqRFLNOZhttps://techcrunch.com/sponsor/nvidia/how-the-revolution-of-natural-language-processing-is-changing-the-way-companies-understand-text/?guccounter=1&guce_referrer=aHR0cHM6Ly9jc2UuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAcHcT1AKoY5u_x_AOEyFPWQyJk4dhhGEKl_WWPfEKqS4dp5PbfMxVSR3DlAeWF5-kcbroeMRrl4Wjyl-jyLbCte2MHRAvHwpm58Nv9hzTrPLiOCXXY1baQJXJK4qJkg2cSJEsvwuSzon7JkHm74bx8Qa5krnoLev_eaQqRFLNOZ) There are a variety of factors you could use to describe an AI solution. When it comes to real-time coaching, one of the defining characteristics is how well it understands human language, or [natural language processing (NLP)](https://www.lexalytics.com/lexablog/context-analysis-nlp). This blog walks through some of the NLP approaches Cresta uses to understand and coach conversations.  

## The Challenge: Language is Difficult to Understand

Understanding human language is no easy task for machines. Language is complex, dynamic, versatile and contextual. We can say the exact same thing in multiple ways and the same word can have [multiple meanings](https://researchoutreach.org/articles/how-context-influences-language-processing-comprehension/).Take the phrase, “Bill is on the way.” This could mean someone named Bill is on his way or it could mean a credit card bill is in the mail. Chances are good that customer service agents would naturally infer the difference. But nothing comes naturally to computers.Real-time coaching makes things even harder. Unlike chatbots, which only need to keep track of one person, real-time coaching solutions need to keep track of both the customer and the agent. Furthermore, conversations between two people are extremely dynamic and can go in a variety of directions. Fortunately, recent advances in AI ([especially](https://www.ibm.com/cloud/learn/conversational-ai) NLP) have made it easier to wrangle this complexity.

## How Cresta’s Expertise AI™ Understands Conversations

Cresta's underlying Expertise Engine is constantly evolving to take advantage of the latest advances in AI and NLP research. But But there are three primary NLP approaches our Expertise Engine uses to understand conversations - keyword matching, semantic understanding and context tracking.

### **Keyword Matching**

The first and simplest NLP approach Cresta uses is keyword matching. Keyword matching is a rule-based NLP approach that relies on user-defined rules to understand language. Much like if-then logic, if the AI system detects a keyword, it triggers the corresponding rule. If a rule has not been created for a particular keyword, then the AI does not trigger any coaching.This approach is easy to configure but struggles to handle complex and dynamic conversations where multiple meanings come into play. Relying too heavily on keyword matching can result in inaccurate or incorrect coaching. For this reason, keyword matching is best suited for simple use cases like triggering a tool-tip when a competitor’s name is mentioned.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f4055f71eb5bdad086f_68135f3087085596dacfb5b4_Screen-Shot-2022-01-06-at-10.06.00-AM.avif)

Keyword matching is best suited for simple scenarios where the desired action is clearly defined.

### **Semantic Understanding**

Semantic understanding is an advanced NLP approach that is core to Cresta's Expertise Engine. This method infers the meaning behind what’s being said by looking at things like word order, sequence and the relationship between words and phrases. This advanced approach has become possible in recent years thanks to [recent advances in deep learning and natural language understanding (NLU](https://www.ibm.com/blogs/watson/2020/12/how-bert-and-gpt-models-change-the-game-for-nlp/)). Deep learning is a machine learning approach that imitates the way humans learn. Using training data, deep models detect patterns and automatically determine optimal responses.Let’s look at an example of semantic understanding in action. How should AI coach an agent at this moment?

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f4055f71eb5bdad0881_68135f3087085596dacfb5b7_Screen-Shot-2022-01-06-at-10.03.43-AM.avif)

Here, the customer’s intent to purchase might be obvious to a human. But for AI, it's much more complex. Using simple keyword matching, the model would detect the phrase “spouse” and think the customer is using their spouse as an excuse to avoid making a purchase. This excuse is more common than you think!

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f4055f71eb5bdad0884_68135f3087085596dacfb5c9_Screen-Shot-2022-01-06-at-10.02.25-AM.avif)

Semantic understanding helps Cresta understand the nuances of human language.

Using semantic understanding, the model observes the entire statement and registers that despite using the word "spouse", the customer actually intends to make a purchase. With this information, Cresta can accurately coach the agent to assume the sale. While this approach is extremely powerful, semantic understanding alone is not enough to teach AI to understand like humans.

### **Context Tracking**

Conversations are nonlinear and ambiguous. They can cover many different topics and take many different paths. As humans, we rely on context to cut through this ambiguity. We use what we know about a person and what they’ve already said during the conversation to help us determine how to respond. At Cresta, our Expertise Engine creates context using a deep learning concept called context tracking. Context tracking tracks what has already been said in a conversation, and uses this knowledge to help AI take more accurate actions.For example, how should Cresta help an agent when a customer says “It’s too expensive for me”? It depends on the context.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f4055f71eb5bdad087b_68135f3087085596dacfb5b1_Screen-Shot-2022-01-06-at-10.04.21-AM.avif)

For an existing customer trying to cancel her subscription, Cresta will coach an agent on how to prevent churn and retain the customer. Alternatively, if a new customer is looking for a better deal, Cresta will coach the agent to offer the new customer a promotion.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f4055f71eb5bdad087e_68135f3087085596dacfb5cc_Screen-Shot-2022-01-06-at-10.02.40-AM.avif)

By understanding what has already been said in a conversation, context tracking allows Cresta to deliver more accurate coaching.

## Picking the Right Approach

These are just three of the NLP approaches we use at Cresta to understand conversations. You might be asking, how do we choose which approach to use? It depends!Factors like use case, channel, user experience, and customer experience all come into play. But one thing is certain, to be effectively understand and coach conversations at scale, semantic understanding and context tracking are a must.Ultimately, building tailor-fit real-time coaching solutions is a balancing act and there is no one-size-fits-all approach. This is where Cresta’s highly-skilled AI teams come into play. Using internal tools and processes, a concert of engineers, data scientists, and deployment teams quickly build, train, and tune bespoke AI models that address each customer’s individual needs and goals. During this process, teams test different NLP approaches to determine the combination that yields the best customer experience, employee experience and the greatest ROI.Most importantly, this is an ongoing process of improvement. With each additional conversation, our Expertise Engine processes gets smarter, delivering better coaching and helping Cresta to deliver [compounding value quarter after quarter.](https://cresta.com/blog/3-compounding-benefits-of-ai-driven-real-time-coaching)
