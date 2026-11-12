---
title: Forward deployed engineering on the frontier of AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/forward-deployed-engineering
author: Matthew Blau
published: '2025-06-10'
fetched: '2026-11-12T06:07:16Z'
classifier: null
taxonomy_rev: 2
words: 1955
content_sha256: b2c08040b58aa7c192142e017c025a4db9a6ab28ce9b0171f1caf12892a76750
---

# Forward deployed engineering on the frontier of AI

Community
# Forward deployed engineering on the frontier of AI

How forward deployed engineers (FDEs) accelerate value, shape product, and how to build and scale an effective team.


- Authors
- Date
- June 10, 2025

The world’s fastest-growing AI dev tooling companies are all facing a similar question: how do you accelerate adoption of highly technical products when the market is evolving faster than any roadmap can capture?

One solution is building out a Forward Deployed Engineering (FDE) function. An FDE team sits within the engineering organizations and works directly with your customers’ engineers to accelerate time to value with your product.

The first question I get about FDE is whether it’s just a different name for more commonly understood functions, such as consulting, solutions architecture, or sales engineering. These roles are valuable and are a better fit than FDE for many companies. While there are some tactical differences – FDE tends to be more hands-on than other functions – the main difference is strategic.

**Forward Deployed Engineering is unique because it sits within the engineering organization and makes regular contributions to the product, both through building the product and having an outsized influence on the product roadmap.**

By sitting within engineering and working directly with customers, FDE expands the product's perimeter. Where consultants, solutions architects, and delivery teams often operate at the boundary between the product and the customer, FDE moves the boundary itself.

Investing in an FDE function makes sense when you have:

1. **Substantial product and/or technology risk**: You’re operating in a market where it’s hard to forecast more than a few months out. The underlying technology and market demand are moving faster than your “core” product can expand.
2. **Deeply technical stakeholders**: Your customers are some of the most senior technical people at their respective companies – staff engineers, CTOs, and engineering leads – and expect equally technical counterparts.
3. **High leverage from customer-driven innovation:** Work done to meet individual customer needs frequently reveals broader product opportunities and can directly inform (or even become) core features.

As [Palantir's Ted Mabrey noted](https://open.substack.com/pub/tedmabrey/p/sorry-that-isnt-an-fde?selection=d3e081e7-4cfe-402d-a668-1b4e7ab88564&utm_campaign=post-share-selection&utm_medium=web) about their own FDE team: "*When the things you need to build are de facto infinite, the only thing that matters over any reasonable duration of time is how quickly you can extend the perimeter of the product.*"

These characteristics are very common among today’s cohorts of AI-native and AI-enabled developer tools companies, leading to a renaissance in companies exploring the creation of FDE or FDE-like teams.

Building an FDE team requires a substantial and intentional effort around recruiting, enabling, and retaining a team capable of this work.

Recruiting for a “true” FDE is very difficult. You are looking for individuals who are both top-tier engineers and whom you can trust to work closely with customers. These folks have high optionality – they could easily be highly compensated engineers at FAANG or start their own companies. In my experience, these engineers join the role because they enjoy a high degree of autonomy, solving hard problems, and appreciate working with counterparts who can challenge them technically.

Even if you can recruit those folks, you will likely struggle to retain them if you assign them work that doesn’t meet this bar: you will also need to organize other functions within the company, from product to sales, to maximize the impact of the FDE team.

This investment only makes sense if there is a genuine need for it. Instead of an FDE team, you may simply be better off with a highly experienced specialist, such as a technical account manager, if the real pain point facing your business is providing periodic technical guidance to your customers. But if FDE sounds right to you, read on for thoughts on how to overcome the challenges of recruiting and enabling this kind of team.

At Baseten, our mission is to build the world’s best inference platform for mission-critical AI workloads. While our self-service developer platform enables many customers to deploy and serve production inference without ever interacting with anyone at Baseten, there are equally many fast-growing AI-native companies whose success hinges on their ability to serve the latest model with the tightest latency bounds using optimizations that are only now transitioning from research to production.

This is where the Forward Deployed Engineering team comes in: **the team’s charter is to accelerate our customers to value while building the products and tools that push the frontier of the Baseten product.**

Given the technical complexity of AI inference, the sophistication of our users, and the rapidly expanding value that AI-native companies can deliver and capture, investing in an FDE team makes sense for us at both a technical and strategic level.

We launched the FDE function early, at the first signs of product-market fit, and scaled it as we grew. Along the way, we faced three primary challenges: going from zero to one in FDE, consistently hiring high-caliber engineers, and closely aligning the function within product development. In the next sections, I’ll address each of these challenges individually.

The first challenge is defining and establishing what FDE means within your company.

Initially, when discovering product-market fit, founders and early engineers typically fill the FDE role, shortening the product-engineering loop to bridge the gap between the existing product and the customers’ pain points.

Forward deployed engineering is the natural evolution of this process for companies that are rapidly scaling post-PMF. Ideally, your founding FDEs are established engineers in your startup who enjoy working with design partners to push the product perimeter forward. At Baseten, every early engineer worked closely with customers at some point, and two of those engineers went on to create our forward-deployed team.

When we formally established the function, there was some discussion about moving FDE into the go-to-market organization to better align the team’s priorities with sales and customer success. But keeping FDE embedded within engineering proved to be the right call. While this choice introduced some coordination overhead, it preserved the team’s autonomy and ensured a deep technical understanding of the product. This allowed FDEs to operate independently at the deal level while making meaningful contributions to core product development.

The second challenge in scaling FDE is hiring. Hiring is always hard, especially on the technical frontiers, especially at startups, especially for multidisciplinary roles. While sourcing, landing, onboarding, and retaining exceptional talent remains a constant challenge, we’ve discovered a repeatable process for staffing the team.

Baseten’s FDE team is made up of engineers from varied technical backgrounds. Many, including myself, are ex-founders, while others are engineering alums from companies like NVIDIA, Databricks, Rivian, and others. We range in experience from fifteen-year industry veterans to new grads to interns through our program with the University of Waterloo.

If the backgrounds of forward-deployed engineers are so different, what do they share in common? They’ve each cleared a challenging double-bar hiring process. First, each candidate must pass Baseten’s standard technical interview bar. In parallel, we also screen for deep product intuition and interest (rather than experience) in working and communicating with customers.

Every FDE we hire at Baseten brings:

1. Extremely solid software engineering fundamentals
2. Deep curiosity about problems at every level of the stack, from ML to infrastructure to networking
3. The desire to work closely with end users to understand their problems
4. A good “PM hat” to see patterns in customer requests and use those patterns to inform product direction
5. A strong bias toward action and a founder mindset to keep going until a problem is truly solved

Everything on this list is essential, but one of our key early lessons was to hire for software fundamentals first.

Initially, we thought that Baseten needed to build an FDE team full of ML experts. This significantly reduced our “addressable market” of viable candidates. Over time, we discovered that engineers who operate comfortably across different stacks can quickly pick up ML fundamentals – or LLM quirks – on the job. Just as importantly, we’ve found that customer-facing skills like empathy and clear communication are very coachable for technically strong engineers with the right attitude.

Another useful heuristic I found was to understand the motivation of candidates looking to join FDE. For incredible engineers, there is typically a more direct path to becoming an “L6 at Google” than taking an FDE role, where, on top of growth as an engineer, they are expected to spend time with customers and actively engage in product direction. A great FDE candidate is someone who is specifically choosing FDE over another technical role.

By hiring for software fundamentals and drive over domain expertise, we’ve been able to scale a strong, flexible team relatively quickly in a competitive talent market.

The third challenge is scaling FDE to support a larger, more mature go-to-market motion while staying close to the product.

At past companies, I sometimes found that customer-adjacent teams would build up a complex series of workflows to meet customer needs, but – with the squeaky wheel greased – those workflows never translated into our product. Without that integration, the next series of products we did ship would stray even further from customer needs.

To address this at Baseten, our north star is that 70% of what gets built within FDE gets integrated into the product. This is a collaborative process where we work with the product team and other engineering teams to either build features directly within FDE or translate them into product discovery and validation that informs the company's overall roadmap.

The remaining 30% is the cost of operating in a chaotic environment. Still, that cost is much lower than the hundreds or thousands of hours that would have otherwise been used to bring to market a fully fledged product that wouldn’t find feature-market fit.

1. **Engage with customers early**: We embed FDEs at the earliest stage of the customer journey. This drives better alignment with sales and ensures solutions address real-world problems.
2. **Keep FDE within Engineering**: By maintaining FDE as part of engineering, close to core systems and shipping code directly, the team doesn't get siloed away from engineering.
3. **Hire builders and let them build:** Recruit engineers who are both technically strong and motivated to engage with customers. Support them with roles that handle non-engineering overhead, so FDEs can stay focused on building scalable solutions and tools that create leverage.
4. **Prioritize Software Engineering fundamentals**: Role-specific knowledge, like advanced ML techniques, can be taught, but strong engineering instincts are essential.
5. **Contribute frequently to the product**: At least 70% of what FDE builds should be integrated back into the main product, to be developed by either FDE or the broader product engineering organization.

Forward Deployed Engineering isn't for every company. Building an engineering team that interfaces closely with customers is a demanding task. For companies that have a clearly defined product boundary, the right solution is often to build out a solution architecture or an implementation team. It can be cheaper, faster, and yield more predictable results.

For companies with highly technical products that are quickly evolving and positioned to both deliver and capture immense customer value, an FDE team with a startup ethos can be transformative. This combination is especially common at AI-native companies like Baseten, where our FDE team has become indispensable by enabling our customers and our product to remain at the forefront of generative AI.

If you’re a founder or engineering executive and you think an FDE team could be a fit at your company, or you’re already scaling the team to meet customer demand, please don’t hesitate to reach out. I’d love to exchange ideas on this critical function. And to every engineer reading this who sees themselves thriving on this kind of team, we're always hiring at Baseten!
