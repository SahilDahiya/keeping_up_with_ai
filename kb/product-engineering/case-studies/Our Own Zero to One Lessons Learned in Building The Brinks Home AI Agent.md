---
title: 'Our Own Zero to One: Lessons Learned in Building The Brinks Home AI Agent'
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/planning
summary: Production case study on building an AI agent from zero to one, with lessons
  about scope, rollout, and operational constraints.
source: cresta
url: https://cresta.com/blog/our-own-zero-to-one-lessons-learned-in-building-the-brinks-home-ai-agent
author: Phil Kolterman
published: '2025-03-18'
fetched: '2026-07-11T04:01:08Z'
classifier: codex
taxonomy_rev: 1
words: 1383
content_sha256: 27423be01f3f9efa3ed0b59fd6bc100b2553a29219bde12a5b0e5dd4d3d6374c
---

# Our Own Zero to One: Lessons Learned in Building The Brinks Home AI Agent

Over the past four months, our team at Brinks Home has embarked on a transformative journey to build and deploy an AI agent that handles customer calls. This project represents our foray into true agentic technology—one that seamlessly blends human intuition with artificial intelligence. From day one, our trusted partner, Cresta, has been by our side. Cresta has been a long time partner for Brinks Home AI agent assist and Insights products. We are thrilled to have extended the relationship!In a nod to inspiration, we named our AI agent “Veronica” in honor of Veronica Moturi, Senior Vice President of Customer Experience. That choice of names has been fun, but it has also been a bit confusing! As such the team affectionately adopted the nickname “Virty-Vee” to distinguish our digital counterpart. Today Virty-Vee is live and taking calls for Brinks Home!

## Harnessing LLM Strengths and Bridging Integration Challenges

We kicked off our project by addressing technical support calls—a use case that might seem counterintuitive to traditional call center strategies. Normally self service begins with simple customer care and billing use cases. We recognized early on that knowledge-intensive scenarios are actually a natural place to start for Large Language Models. With our comprehensive knowledge base and secure access to customer data, the LLM navigated complex troubleshooting with remarkable finesse.On the other hand, it’s inherently challenging to develop and implement the interfaces and train the model to interact seamlessly with our transactional systems. Emerging technical solutions may eventually allow the AI agent to emulate a human interface, but for now, it requires real IT work to bridge the gap with APIs. We’re currently working to bridge these integration and capability gaps as we improve the agent. Our goal is to enable Virty-Vee to perform all call center functions in our CRM via robust API integration.

## The Novelty Boost: Turning Skepticism into Delight

One of the most rewarding aspects of our journey has been the unprompted customer feedback. Many callers, initially expecting a typical IVR experience, were delighted to engage with Virty-Vee. Their spontaneous compliments and genuine conversational exchanges—transforming routine calls into engaging interactions—validated our belief that when technology is executed well, it doesn’t just work; it delights.

## Performance: The Backbone of Voice Interactions

In voice interactions, every millisecond counts. Unlike visual applications where users might tolerate a brief delay, a voice conversation demands near-instantaneous responsiveness. Developing a responsive agent like Virty-Vee has underscored the importance of agile, reliable API performance. A lag in response can disrupt the natural flow of conversation and erode customer trust—making performance a non-negotiable aspect of our design.

## Building Durable Assets: Knowledge, Data, and APIs

At the heart of our AI agent lie three critical assets: a refined knowledge base, high-quality data, and robust APIs. Over the past three years, we’ve meticulously rebuilt our help center and internal knowledge bases. Our CRM is fully API-enabled. Our data lake and medallion data architecture enables complex understanding of customer experience. Each iteration has been a step toward excellence. These assets form the foundation of Virty-Vee’s capabilities, ensuring that every customer interaction is powered by accurate, up-to-date information and reliable integration points. Special thanks to Doug Bianchi, Shiva Vuppula and Rahul Strivastava for the work enabling the AI agent as well as the entire Everest self-service and Rouge One Customer support teams for all development over the years making it possible!

## Data-Driven Quality Through Automated Testing

Quality assurance is a cornerstone of our approach, especially in call center interactions where subjective human evaluations can lead to opinion fallacies. Relying solely on individual experiences often results in inconsistent standards. That’s why we’ve invested in automated regression testing powered by LLMs to simulate and evaluate voice interactions. This system provides objective, measurable insights, ensuring that as our release sizes grow, our development remains agile and error-free. Without these automated processes, software development would likely drag on and become increasingly error prone—a risk we simply cannot afford in today’s fast-paced, customer-focused environment. Great work Andy Young and Daniel Reynolds for all the innovative work on test automation!

## Building LLM Security from the Ground Up

At Brinks Home, security is job one and securing our AI agent from the outset has been a fundamental part of our development process. We’ve embedded cyber and data security directly into the AI agent as a routine extension of our self-service security best practices. Every API endpoint is rigorously managed to safeguard against unauthorized access, ensuring that our integration points remain secure throughout. The experience as done today is both deeply informed and anonymous. Virty-Vee has deep information about the customer but at the same time she never has or retains actual identification of the customer.Crucially, we partner only with providers and services that have undergone thorough inspections and maintain rigorous security practices. A special shout-out goes to Cresta and Robert Kugler. Cresta has been a true partner in addressing our system-level security needs, demonstrating proactive certification and a steadfast commitment to our security requirements.

## An Interdisciplinary Team Effort and Change Management

This initiative has been the most interdisciplinary program I’ve ever been involved in. It demanded a deep integration of IT capabilities with business expertise—essentially a large-scale system rip-and-replace that required every team member to bring their A-game. Alongside technical challenges, we faced significant change management and training hurdles.Transitioning to this new mode of operation required a concerted effort from our operations team, who did an outstanding job managing the training, process shifts, and cultural adjustments needed for success. A heartfelt thank you goes to Veronica Moturi and her team for their invaluable leadership and partnership throughout this journey. Congratulations Laytoa Oliver, Dustin Shurader, Elizabeth Lopez, Enes Podbiccanin, Eric Talyor, Olivia Shead, & Kevin McBrayer – thank you for being great business partners and making this happen!

## Managing AI Agents

It’s a common misconception that AI agents like Virty-Vee require less oversight than their human counterparts. In reality, managing her demands the same level of precision and continuous quality assurance. Our experience with Cresta’s agent assist—deployed for our human agents over the past two years—has set the standard for how we measure and support Virty-Vee. Whether it’s ensuring smooth call handoffs or delivering detailed call summaries, the parallels between managing human and AI agents are striking.

## The Hard Truth: It’s Harder Than It Looks

Building an AI agent is a steep learning curve, and I won’t sugarcoat it—there were plenty of challenges along the way. Early on in our digital journey Brinks Home experimented with a proof-of-concept using off-the-shelf CCaaS services and our in-house ChatGPT implementation. Issues like voice lag, model drift, and maintaining a consistent personality quickly emerged with these commodity tools. We needed a partner! Given our long history with Cresta, turning to them on this venture was a natural choice. In a software landscape where many promise the moon but deliver vaporware, Cresta has consistently proven to be a beacon of reliability. Big shout out to Megan Schildmier, Casey Woolwine, Josh Levin, Gray Wang, Ray Swank, Alex Cramer, Ping Wu and the entire Cresta team for making it look easy!

## The Road Ahead: Expanding Capabilities and Enhancing Experience

As indicated, we are currently working to make Virty-Vee fully capable of all call center functions in our CRM via API integration. Looking ahead, our next steps are clear:

- **Personalization:**We’re focused on fine-tuning her personality to ensure every customer interaction feels uniquely tailored.
- **Customer 360 Awareness:**Our vision is for Virty-Vee to have full access to our customer 360 data, so that every call feels like a continuation of a conversation where the agent already knows you.
- **Omnichannel Integration:**We want to better integrate her with our self-service platforms—moving customers seamlessly between voice, app, and chat for a unified experience.
- **Expansion of Use Cases:**Beyond customer interactions, we’re exploring additional internal voice use cases and broader applications of the- [Cresta AI Agent](https://cresta.com/cresta-ai-agent/)experience across Brinks Home.

## In Conclusion

This journey to develop an agentic AI solution has been a masterclass in innovation, collaboration, and relentless improvement. We have navigated complex technical challenges, integrated multidisciplinary teams, and built a solution that not only meets today’s demands but is poised for tomorrow’s opportunities. A sincere thank you to all the teams and partners whose dedication and expertise have made this achievement possible.
