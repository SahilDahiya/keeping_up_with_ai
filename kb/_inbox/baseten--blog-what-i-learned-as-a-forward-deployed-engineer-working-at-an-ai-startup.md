---
title: What I learned as a forward-deployed engineer working at an AI startup
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/what-i-learned-as-a-forward-deployed-engineer-working-at-an-ai-startup
author: Het Trivedi
published: '2024-05-31'
fetched: '2026-11-12T06:12:22Z'
classifier: null
taxonomy_rev: 2
words: 1347
content_sha256: ff8bda680db3173cf1ce62b75dbd99269e73c8afafc75cf0fc91d40acb6c401c
---

# What I learned as a forward-deployed engineer working at an AI startup

Community
# What I learned as a forward-deployed engineer working at an AI startup

My first six months at Baseten exposed me to a huge range of exciting engineering challenges as I learned how to make an impact as a forward-deployed engineer.


- Authors
- Date
- May 31, 2024

In January 2024, I started working full-time as a forward-deployed engineer (FDE) at Baseten. Baseten enables customers to deploy and run inference on cutting-edge generative AI models. My role as an FDE is to work with customers to deliver cutting-edge ML solutions at scale using Baseten.

In the past 6 months, I've learned a lot about the kinds of challenges customers face when deploying generative AI for production use cases. I quickly realized that there's a world of difference between a weekend project posted to X and incorporating AI and ML in a way that works and scales for millions of users. The AI space is rapidly evolving and customers come to FDEs for guidance on how to run the latest and greatest AI models in production. It has been a wild ride so far, but I wouldn't trade it for anything!

Every company defines its FDE role somewhat differently. While the title may sound similar to roles like solutions architect or product engineer, forward-deployed engineering at Baseten is an integral part of the engineering organization and upholds the same high technical standards and expectations as the rest of the engineering team. I like to think of my role as being akin to a technical co-founder for our customers' AI projects. As an FDE, you partner closely with customers who are using your company's products, working side-by-side to help them maximize the value they derive from your platform.

At Baseten, that means tackling a different complex technical challenge every day. Need to optimize a model's architecture for performance? Develop a speech-to-text pipeline? Consult on a CI/CD pipeline for a novel AI system? The demands are diverse, because on the other side of the table are the top ML engineers from major companies - your counterparts who live and breathe this stuff. As the first person to get a call when there's a gnarly technical problem or ambitious new project, I get to see how tons of different companies and industries operate and become an expert in building robust production AI services.

Let's rewind to August of 2023. I was working on my startup, but despite my best efforts, I hadn't yet found product-market fit. After nearly a year of hard work, I realized it was time to pivot and explore new opportunities.

While my current entrepreneurial pursuit didn't pan out, I knew I still wanted to work in AI. While I was figuring out next steps I decided to focus on side projects and enjoy building things while searching for the right fit. With the release of ChatGPT and the increasing buzz around generative AI, I was inspired to start tinkering with these cutting-edge technologies.

I began experimenting with GPT APIs, building retrieval-augmented generation (RAG) systems, and creating small chatbots. As I delved deeper into these projects, I noticed a lack of tutorials that went beyond the basics of building with AI, and I started blogging about my learnings and experiences.

Along the way I found a tool called Truss, which I used to deploy open-source LLMs. I wrote a blog post about it, which was discovered by a co-founder of Baseten, the creators of Truss. He slid into my DMs, invited me to hang out at the office and meet the team, and gave me some interesting projects to work on. Once I got my foot in the door, I kept at it until I scored the job offer.

Being an FDE is a highly technical role that also incorporates elements of customer-facing work. The time I spend wearing different hats varies from day to day, but over time it looks something like:

- 75% software engineering and model optimization
- 15% technical consulting and solution design
- 10% customer relationship management

My main goal is to help customers deploy open source, fine-tuned, or custom models behind API endpoints, hit their requirements for latency, throughput, and cost, and get live traffic running reliably through the model endpoints. This requires three main skills I've honed in the last six months as an FDE.

Customers don't just use Baseten to run simple models out of the box. They come to us with hairy technical challenges like "How can we optimize our model serving latency by 10x while keeping costs flat?" or "What's the best way to horizontally scale our generative AI pipeline to handle 100x more traffic?" After scoping the problem with the customer, we'll work with them to design a solution and kick off the implementation.

In my opinion, this is the best part about being an FDE. You get to take powerful generative AI models and mold them into highly optimized, production-ready solutions tailored to each customer's unique needs. In this phase, we place a lot of emphasis on optimizing the models to get the best performance possible. We'll leverage advanced tools and techniques to boost performance — maybe using TensorRT to dramatically improve inference latency, or intelligently caching model weights for the fastest possible cold start. The possibilities are wide open, so we have a ton of freedom to innovate and push the boundaries of what's possible with ML engineering.

Once we've got an optimized model, it's time to put it through its paces with rigorous testing, benchmarking, and hardening to ensure it meets the customer's requirements. Often this is done with the customer side-by-side so that there are no "works on my machine" quirks before handing it off.

If the customer is satisfied with the technical implementation and the pricing is agreed upon, we seal the deal. Delivering a rock-solid solution that exceeds the customer's expectations is one of the best feelings in the world. Once a solution is shipped, you transition into a support role to ensure a smooth hand-off to the customer's team and resolve any issues that arise.

Oftentimes with software engineering roles, it's hard to measure the impact your work has on the company. As an FDE, the impact is very clear. Every time you ship a solution, that's new value you're delivering to customers and new revenue hitting the company's bottom line — because of you! Customers also tend to show a lot of appreciation and gratitude when you help them solve hard problems, which adds to that sense of personal fulfillment.

But that metaphorical sword cuts both ways. Your actions stand between successful delivery and a failed engagement. Losing a customer is a good learning experience, but it can be tough to shake that nagging feeling that you could've done better.

There's also a ton of context-switching in this role that you've got to be ready for. It's not a typical software job where you can hunker down and focus on one project. As an FDE, you're juggling multiple in-depth projects simultaneously while also handling customer relationships. It's easy to get bogged down in technical rabbit holes and lose sight of priorities. Staying successful means remembering that shipping solutions and keeping customers happy is the name of the game.

My first six months at Baseten have been the beginning of an amazing journey. I've had the incredible opportunity to work on the bleeding edge of AI and ML engineering. On top of that, I've had the privilege to work with some of the most amazing people. Every job posting asks for a "can do attitude" but here I see that lived out every single day. We're a small but growing team and are able to punch well above our weight because everyone is passionate, optimistic, and has that scrappy startup hustle mentality.

We’re actively hiring for a number of technical roles at Baseten, including on the forward-deployed engineering team. If the journey I’ve written about resonates with you and you’re looking for exciting, high-impact work with the best technologies and coworkers around, check out our openings at [baseten.co/careers](http://baseten.co/careers).
