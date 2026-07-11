---
title: What Does It Take To Pioneer Successful LLM Applications In Healthcare and
  the Life Sciences?
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/evaluation
summary: Healthcare and life-sciences case discussion on what it takes to build successful
  LLM applications, including domain constraints and evaluation needs.
source: arize
url: https://arize.com/blog/ai-llm-in-healthcare-and-the-life-sciences-klick-health/
author: David Burch
published: '2024-02-21'
fetched: '2026-07-11T04:48:24Z'
classifier: codex
taxonomy_rev: 1
words: 2149
content_sha256: 5b49a12d60b4f850719cef86965842429b9884582600ecacaa95fbd18d6288d2
---

# What Does It Take To Pioneer Successful LLM Applications In Healthcare and the Life Sciences?

Peter Leimbigler is a Data Science Team Leader within the Consulting practice at Klick Health. As the largest independent commercialization partner in its industry, Klick pioneers new AI-powered applications for clients across life sciences, pharmaceuticals, medical device, and consumer health to accelerate growth and improve experiences and outcomes for patients and consumers. That’s especially true in the current wave of emerging developments in generative AI. We caught up with Peter to learn more about AI work for clients, large language model (LLM) use cases, and thoughts on the evolving LLM operations (LLMOps) landscape.

#### Can you introduce yourself, covering your background and your role at Klick Health?

I lead the data science team at Klick Consulting, which helps define and solve complex problems in the healthcare and life sciences space across a wide range of clients – startup to global, at various lifecycle stages. We evaluate and adopt technology to serve business needs, and are excited to be taking an experiment-driven approach to using LLMs effectively and responsibly. This includes staying up to date on models themselves, as well as the blossoming field of LLMOps.

Career-wise, I’m one of those data scientists who pivoted into the role from an adjacent quantitative field. I studied physics as an undergraduate, then earned a Master of Science in Medical Biophysics at the University of Toronto. I used Python and other open-source software to wrangle and analyze complex datasets and brought this experience to interesting problems in industry at Klick.

Data science fulfilled my personal desire to work at the intersection of various different disciplines rather than hyper-specializing. Ultimately, I wanted to make a real impact in the lives of actual people. I was fortunate to be among the first data scientists at Klick, working on a centralized team to address data and advanced analysis needs across the company. I then evolved into my current consulting role where I fit data solutions to client problems while collaborating closely with the advanced analytics and data science functions beyond the Consulting team.

#### What should people know about Klick Health and why AI is core to what you do?

Klick Health is the world’s largest independent commercialization partner for healthcare and life sciences. Data and analytics have always been a pillar of our offerings, from augmenting human experts to work faster, to equipping clients with competitive insights and forecasts.

Within Klick, Klick Consulting is a growth acceleration partner for consumer and prescription based healthcare companies. We integrate strategy and execution, going further than most consultancies to bring our recommendations to market through our team of specialists. AI is a great example of where we have been helping clients. Clients want to use it to solve real problems, but often find themselves working on projects that don’t move the needle because of perceived technical or regulatory hurdles.

In the wake of the excitement and investment triggered by ChatGPT’s launch, Klick has established a generative AI center of excellence that supports the entire organization to learn how to use AI tools effectively and responsibly, and to support internal and client-facing projects where genAI technology is deployed. This Klick-wide initiative is designed to promote hands-on experience, which we believe is critical for us to learn what is and isn’t useful in this fast-moving field.

As an example, Klick has augmented our own internal operations platform with a chat-based feature that allows us to more easily and efficiently ideate, summarize reports, perform research, and analyze or reshape in-house proprietary data. Through this interface, we are learning best practices for how to improve existing workflows, and how to recognize tasks which are a good fit for LLM-based approaches. Chat is an intuitive and natural interface, yet requires training and practice for effective use, which we’ve intentionally fostered across Klick.

The excitement around genAI is warranted, but there’s a need to see past the hype and understand the nuances of evaluating and using large language models. Klick knows that hands-on experience is the best way to learn these nuances, and we’re enabling all parts of the organization to learn by doing, and to share learnings with our clients.

#### How do you think generative AI in particular will reshape life sciences, pharmaceuticals, and consumer health?

It’s difficult to answer this question well, given the sheer volume of genAI advances in these and other fields. But we are seeing it applied to speeding up drug discovery and development – the best known example probably being DeepMind’s AlphaFold – or to predict drug-target interactions to narrow down preclinical drug candidates. This holds promise to tackle the long tail of rare diseases, and advancing precision medicine or personalized medicine, as in tailoring treatments to individual genetic, environmental, and behavioral factors.

Supporting clinical trials is another example that comes to mind. At Klick, we have experience supporting clinical trial success by using demographic and geospatial data to reach recruitment targets and address some of the big challenges facing clinical trials, such as diversity and inclusion – helping trial sponsors enroll individuals who better represent the real-world patient population. Patients also face language barriers or historical mistrust in medical research, and Klick has worked hard to address these barriers creatively and sensitively. GenAI could personalize the patient experience to increase engagement and potentially reduce attrition, which is another big challenge. Training trial site staff and streamlining documentation in a regulation-heavy context also come to mind as tasks for which GenAI is well suited.

Another way I believe genAI will really change healthcare is by augmenting and streamlining doctor-patient interactions – the face-to-face conversations where, say, a primary care provider evaluates their patient and makes a diagnosis and recommendations. Imagine pairing each visit with a summary of diagnoses and treatment plans tailored to each patient’s level of medical knowledge, with language translations and interactive Q&A seamlessly available. I’d expect this would greatly increase patient satisfaction, adherence, and health outcomes. Beyond the patient experience, GenAI has great potential to alleviate administrative burden, reduce errors, and free up healthcare providers to do their core job of improving patient lives.

#### What have your clients/accounts gravitated towards with LLM applications? What have they found challenging or interesting?

I can speak to [an example from consumer health](https://idx.klick.com/articles/so-you-want-to-build-a-chatbot-lessons-from-prototyping-a-large-language), where one of our clients had a knowledge base that they had prepared for a patient portal – a platform for people with certain chronic conditions to self-inform, gain confidence, and find peers and other individuals who share their personal health journey. Our client had this library of medically validated articles grounded in the latest available clinical guidelines and vetted professionally, and they wanted to meet the challenge that different patients have very different information needs and health circumstances. One approach would be to use a recommender engine to personalize the articles that each user sees, which we actually helped prototype as well.

We built an LLM-powered chat interface to personalize access to this knowledge base, and tackled questions like how to load, retrieve, and present the right information from this large library of knowledge, keeping LLM responses accurate while matching the users’ expectations of tone, complexity, and style of engagement. We experimented with different approaches, and learned how to steer and govern an LLM to provide personalized support and self-directed learning for users whose health challenges span a wide range of complexity and individual variation.

With healthcare, regulatory considerations are always top of mind. This being a prototype for a consumer-facing application, it was critical for us to find a robust way to govern system behavior by monitoring free-text inputs and outputs. This need for monitoring and observability is what led us to Arize. We addressed some of the top challenges of LLM applications, such as the risk of inaccuracies (hallucinations) and the overwhelming space of possible natural-language inputs and outputs.

#### What were your key learnings from building the prototype?

It’s relatively easy to stand up a demo of an LLM workflow with LangChain or LlamaIndex, or roll your own orchestration logic. Such a proof of concept can be shopped around internally, but developing further toward a viable and robust application is another matter, and that’s where Klick Consulting can help.

Another learning was not exactly specific to LLM apps: it’s deceptively challenging to align user needs and business goals, and to create an experience that is “sticky,” with appeal and value beyond first impressions to retain users. So it’s easy to get started, but hard to deploy, operationalize, and monitor an LLM app. You’re still building (or at least prototyping) a product, and will need to consider product strategy, user experience, and well-established principles of software design and development.

Another key learning: it really pays to iterate and experiment quickly, prioritizing the need for lean teams with fast feedback loops. If you wait for publications or competitors to share their own best practices, you’re already behind the curve. We believe the ideal approach is to foster hands-on experience through small teams of motivated individuals who start with a concrete business problem, as opposed to starting with the technology and then looking for use cases.

#### Why is [LLM observability](https://arize.com/llm) important, why did you choose [Phoenix](https://phoenix.arize.com/)?

We knew that governing LLM behavior poses unique challenges. We also recognize that any consumer-facing application built with LLMs needs a solution that can not just detect and flag issues but also help analyze the root cause of failure modes, such as hallucinations. This is especially important in the heavily regulated area of healthcare. That was our top concern going in. How do you catch inaccurate responses in the medium of freeform text? It’s critical to be able to trace through the intermediate steps that led to an output that’s unexpected – such as a semantic outlier, as opposed to a number that goes off the charts – and troubleshoot. What were the prompt and model parameters? Did the problem show up in the user’s query, whether intentional or not? Did their query find a gap in your knowledge base, or retrieved similar yet irrelevant chunks of text?

LLM observability answers such questions. We adopted Phoenix due to its excellent documentation and support and well designed ability to integrate quickly into our existing prototyping workflows. The notebook-centric design made it seamless to integrate into our offline experiments. Arize has also nurtured an active community of LLMOps learners, professionals, and advocates that I’ve personally found very helpful to (try to) stay on top of new developments.

#### What are some of the unique challenges of LLMs in production?

Controlling hallucinations is top of mind, which is a big part of why the retrieval augmented generation motif exists. And somewhat related to that, there’s always a chance that an LLM’s next-token prediction walks into an unintended space that might be surprising or offensive to the user. So this non-deterministic nature of LLM output along with the inherent ambiguity and nuance of human language combine to produce an intractably large space of possible interactions.

Being able to sift through large volumes of natural-language user interactions is important, and where Phoenix shines. It productizes the workflow of taking your user inputs and model responses, getting embedding vectors from your embedding model of choice, and then clustering and projecting these embedding vectors into 3D space for interactive inspection and visual detection of themes and anomalies. We had been doing this manually in an ad hoc manner, but Phoenix streamlines this and lets us focus on what matters most to our application and users.

#### How do you view the evolving LLMOps tools landscape?

There are many players meeting needs across the spectrum of rolling your own LLMOps through to fully managed platforms. The right choice will depend on your application and its specific monitoring/observability needs, as well as organizational size, experience, capability, and mandate.

#### “Outcomes over optics” is a value on your homepage – what does that look like for your team, and how do you collaborate with other teams and clients to ensure anything built with AI is delivering the results that matter?

Prioritizing outcomes over optics is one of Klick’s founding principles. It speaks to our commitment to our work and captures our desire to go beyond where some agencies or consultancies stop. We deliver not just polished reports, but follow through to build artifacts, such as machine learning models or software prototypes, perform rigorous evaluations, and provide data-informed recommendations to give confidence to our clients and their own audiences and stakeholders. So our insights and recommendations will always be informed by repeatable and reliable processes. We value reproducibility, transparency (e.g., methodology, data provenance, caveats), and clarity of our data narratives, and ultimately aim to make tangible business impact.

#### Anything you want to add?

Klick is growing, doing meaningful work, and always looking for the industry’s brightest minds to join our team! Take a look at our open roles at [https://careers.klick.com/](https://careers.klick.com/) or connect with me at pleimbigler@klick.com.
