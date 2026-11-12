---
title: Amnesiac generalist behemoths are not the future of language models
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/amnesiac-generalist-behemoths-are-not-the-future-of-language-models
author: Charles O'Neill
published: '2025-07-28'
fetched: '2026-11-12T06:15:46Z'
classifier: null
taxonomy_rev: 2
words: 963
content_sha256: 7db9c979e0318f11e80d35e5a2cd4043cfd59bf3e9f1e2ed7b8bb04926355620
---

# Amnesiac generalist behemoths are not the future of language models

Position
# Amnesiac generalist behemoths are not the future of language models

You don’t need a generic genius. You need a specialist learner.


- Authors
- Date
- July 28, 2025

We got an intern at Baseten the other day. They were brilliant. They knew the definition of every computing concept in my vocabulary. They read faster than anyone I’ve ever met. They even shipped a feature within their first hour (not just a PR, actually deployed to production). They even corrected my understanding of RAFT consensus (politely, but still). I thought I'd found a 10x engineer.

However, about a day in, I realised they were also an idiot. A task they did perfectly, first try, on Monday morning I then had to re-explain in the exact same level of detail on Monday afternoon. They remembered everything perfectly but after an hour of chatting they literally forgot all of it. Some tasks I could just quickly say some poorly defined vibe of what I wanted and they got it perfectly. Others, no matter how much I talked to them and explained what I wanted, they refused to do it in the way I wanted.

Most importantly, the intern wasn’t **learning**.

Of course, our intern isn’t a person but rather a language model from Big Token (you know which companies I mean). A behemoth model with probably half a trillion parameters that is obviously the most amount of intelligence and compression we've fit in a single hard-drive, but that unfortunately has all the shortcomings I've listed above.

OpenAI, Anthropic, and Google have sold us a story: stick with their big, expensive, generalist models for everything. Don't look for alternatives. Don't question why your clinical scribe needs the same model that writes poetry. Just trust that next month's update will finally solve hallucinations, that your 320 versioned prompts in Prompteams are a normal part of doing business, that intelligence alone will eventually overcome the fact that these models never actually learn from your specific use case.

The reality is you're paying $50k/month for a model that confidently tells your customers your company was founded in 1742 (it wasn't). You've written a 2,000-word prompt with seventeen different "IMPORTANT: NEVER DO X" clauses that breaks the moment someone asks a slightly different question. You watch helplessly as each model update (system prompts, hidden finetuning runs behind the scenes) makes your carefully tuned system perform worse, not better, at your specific task. Anthropic quantises the model one day and all your work is down the drain anyway; OpenAI goes down and you have to helplessly twiddle your thumbs; not your weights, not your brain.

Here's what they don't tell you: GPT-4o can write Shakespeare, solve differential equations, and code in 50 languages. Your insurance claim classifier needs exactly none of those abilities. Those are billions of parameters dedicated to haiku generation sitting idle while your model struggles to remember that claims over $10,000 require manager approval. You're essentially hiring a Nobel laureate to work exclusively as a filing clerk.

"But don't I need flexibility?" you might ask. "What if I want to use the same model for different tasks?" Let's be honest; 80% of companies using LLMs in production use them for 1-3 core tasks. You're not building AGI. You're automating customer support, or extracting data from documents, or generating product descriptions. You need a specialist, not a generalist who forgets everything between conversations.

I don’t think this is axiomatic. I don't think we need to live in this world. I believe in a world where models don't have amnesia but get better at every attempt of the tasks they're doing. Where your model learns that when customer Sarah from Toledo mentions "the usual," she means product SKU-4829. Where error rates drop by 73% after three months of continuous learning. Where you can run your model on even a single GPU (although of course you can up this if you like). Importantly, where you can choose exactly what point on the Pareto frontier of cost/latency vs performance you’d like to be on, and rest assured that you are indeed on the Pareto frontier.

The big generalist models will always thrive in the chatbot world; no argument there. But we're now seeing companies doing real, specific tasks. Clinical scribes that need to understand medical terminology, not ancient Greek. Insurance policy selectors that need to master state regulations, not constitutional law. Customer service agents that need to know your product inside out, not every product ever made.

That's what we build at Baseten. We eval your task, we optimise your very own model for it, and we host it with continual learning. One of our clients reduced their monthly AI spend by over 50% while improving accuracy by 64%. Another finally solved their hallucination problem after nine months of prompt engineering. It turns out when you train a model exclusively on insurance policies, it stops making up coverage that doesn't exist.

There's only so much differentiation you can get from your competitors by constructing a better prompt. They can copy your prompt in an afternoon. But a model that's been learning from your specific use case for six months, and that's been optimised on your actual customer interactions, well, that’s a real moat.

The future isn't one massive intern that forgets everything between conversations. It's a team of specialists who remember, who learn, who get better at their jobs every single day. While everyone else is still explaining the same task to their amnesiac genius for the thousandth time, your model will have already mastered it, improved on it, and moved on to solving problems you haven't even thought of yet. That’s an actual competitive advantage.

Stop paying for Shakespeare when you need spreadsheets. Let's build something that actually learns.
