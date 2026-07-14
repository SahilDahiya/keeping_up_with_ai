---
title: How do you make an LLM, anyway? Microsoft just published a textbook.
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: arize
url: https://arize.com/blog/how-do-you-make-an-llm-anyway-microsoft-textbook/
author: Laurie Voss
published: '2026-07-13'
fetched: '2026-07-14T06:43:54Z'
classifier: null
taxonomy_rev: 1
words: 2071
content_sha256: 7cb8e4f3e49ea685e8345fc554c52bdd61e3bbd28d6caad78ab8670feec6f81d
---

# How do you make an LLM, anyway? Microsoft just published a textbook.

If you’re like me, you use large language models every day, but exactly how they get made is a mystery. There’s something about reading the whole internet? And then “training”? And it all takes thousands of high-end GPUs months of work? The details are fuzzy.

You’re not alone, and in fact the mystery has been deepening for the last few years. Prior to around GPT-4, the big model labs used to publish how they did their work on a regular basis. After that everybody went quiet as things became trade secrets.

But last week Microsoft broke that trend: it published an incredibly detailed 109-page [technical report on MAI-Thinking-1](https://microsoft.ai/pdf/mai-thinking-1.pdf), the reasoning model it [announced at the Microsoft Build Conference](https://microsoft.ai/news/introducing-mai-thinking-1/). One commentator [@nrehiew_](https://x.com/nrehiew_) said it “could really serve as an updated textbook for LLM training today.”

But textbooks are long. Who has that kind of time? So here instead is the extremely abbreviated version of how a modern lab produces a model that matches Sonnet 4.6 in capability. I promise not to use any big words.

**Step one: download the whole internet, then throw most of it away**

A frontier model starts life as a web-scraping and data-janitorial project of awesome scale. Microsoft’s corpus comes from four places: its own web crawler, Common Crawl (the public archive of the web that nearly every lab uses), books and journals licensed directly from publishers, and public GitHub code.

The proprietary crawl alone pulled in about 1.2 trillion web pages. Then it got aggressively filtered: spam, adult content, blocklisted domains, pages that are mostly navigation bars (a signal of domain squatters), and, notably, AI-generated content, which Microsoft actively detects and removes so the model learns from humans rather than from other models’ outputs. Filtering and deduplication cut those 1.2 trillion pages down to a small fraction of the original haul.

Deduplication is a big part of the process. Exact copies are easy to catch, but the web’s real redundancy is sneakier. One example: SEO hacking has resulted in a web with thousands of “calculator” pages identical except for which numbers are being added together. Another example: the same binary-search-tree homework solution written independently by ten thousand students. The report describes a whole arsenal for this, including using one model’s understanding of meaning to find documents that say the same thing in different words. Repetition matters because a model that sees the same content over and over starts memorizing instead of generalizing, and big models are the worst offenders.

Then comes the diet decision, and here’s the single most surprising fact in the report for a general reader: the final training mixture is **54.6% code**. A model marketed for reasoning is mostly fed programming. Math gets special treatment: high-quality math text is so scarce that Microsoft’s entire cleaned-up math hoard amounts to roughly 300 billion tokens, and the model is shown that data more than five times over during training. Ordinary web text, by contrast, is so abundant that the model never even sees half of it once.

**Pre-training: predict the next word, 30 trillion times**

Next comes pre-training. The model reads the corpus and learns to predict what comes next, over and over, and that one dumb-sounding objective is where all of its raw knowledge comes from. For MAI-Thinking-1 this meant 30 trillion tokens on 8,192 of NVIDIA’s most powerful GPUs, running for months. The single number everyone watches during those months is the “loss”: a running score of how badly the model is guessing the next word, which should fall steadily as training goes on.

The chart of that score over time is the heartbeat monitor of a training run, and in real life it isn’t a serene downward glide. It has spikes, moments where something goes briefly haywire and the model gets dramatically worse before recovering. Labs almost always smooth this chart before showing it to anyone, averaging away the scary blips. Microsoft published theirs raw, spikes visible, with a note that the run recovered from each one on its own and never needed a manual intervention.

But they don’t just launch into pre-training with the full dataset and hope for the best. There are thousands of knobs you can turn; how do you decide which combination is going to produce the best model?

The answer is: you train a lot of small models. For any design question (this data source or that one, this architecture tweak or not), they train a “ladder” of miniature versions of each candidate, from a few hundred million parameters on up, getting bigger each time, and watch which design improves fastest as scale increases. A trend that holds across the whole ladder is trusted at full scale.

To compare candidate models, they boil everything down to one decision metric they call Efficiency Gain: how much extra compute would our current design need to match the new design’s performance? In practice, the difference between the candidate models is usually small: one architecture variant in the report’s tables wins by 3%. But the wins compound: across four successive generations of the design, the accumulated improvements left the final version 69% more efficient than the first. Frontier model design is less about breakthroughs and more about stacking small, verified gains, one cheap experiment at a time.

The same small-test approach picks the data diet. At one point Microsoft trained 183 small models from scratch on 61 different data mixtures just to map out how the proportions of code, web text, and everything else trade off against each other. They also share a cautionary tale: a mixture that looked clearly better at small scale turned out to be worse at large scale, because two of its star datasets were repetitive in ways that only started to hurt once the model was big enough to memorize them. Cheap experiments guide expensive ones, but they can also lie to you, and part of the discipline is figuring out when.

**Mid-training: the stage you’ve never heard of**

Between pre-training and the stuff that makes a model feel like an assistant, there’s a finishing-school phase the report calls mid-training. No new data goes in. Instead, Microsoft re-filters the existing corpus down to its highest-quality subset, tilts it even harder toward math, science, and code, and re-packs it into much longer documents. That last part is where long context comes from: the model is pre-trained reading passages of 16,000 tokens, then stretched to 64,000, then to 262,000. When a model card brags about a 256K context window, this unglamorous stretching phase is the thing being bragged about.

**Post-training: where the model learns to behave**

After pre-training and mid-training, you don’t have an assistant. You have an extremely knowledgeable autocomplete. It can continue any text you give it, but it doesn’t answer questions, doesn’t use tools, doesn’t think before responding, and doesn’t decline to help with anything. Every one of those behaviors is installed afterward, in post-training, and in this report post-training means “reinforcement learning.” (For how most product teams iterate without training their own frontier models, see [The end of fine-tuning](https://arize.com/blog/the-end-of-fine-tuning/).)

The mechanics of reinforcement learning are surprisingly easy to understand. Give the model a math problem and let it generate 128 different attempts. Run a checker over the attempts: a symbolic math engine verifies the answers, or for a coding task, the test suite either passes or it doesn’t. Then nudge the model’s weights toward whatever the successful attempts did and away from what the failures did. Repeat across millions of problems. For fuzzier qualities like helpfulness, tone, and safety, where there’s no test suite, the graders are other AI models: [judge models scoring against rubrics](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production/), plus a model trained on thousands of human preference ratings to predict which of two answers a person would prefer. [AI evals are a data science problem](https://arize.com/blog/ai-evals-are-a-data-science-problem-what-most-teams-get-wrong/) for the same reason: the graders only work if you treat the labels and rubrics seriously.

There is also a whole bag of strategies to prevent the models cheating at this training, because models absolutely cheat. Microsoft built its coding practice problems from real GitHub pull requests, packaging each one as a containerized environment where the model has to fix a bug and pass hidden tests. The model discovered it could sometimes just search the internet for the original fix, so Microsoft cut off network access. Then it started digging through the repository’s git history to find the solution commit, so Microsoft built “time-traveled” copies of each repository with all future commits scrubbed. It also tried tampering with the test files themselves, so the graders now reset every test file before scoring and language models watch the training rollouts for new tricks. A meaningful slice of frontier-lab engineering is an anti-cheating arms race against the lab’s own model — the same [reward-hacking problem](https://arize.com/blog/how-to-evaluate-ai-agents-and-build-better-specs) agent builders hit when they try to evaluate AI agents in the wild.

**Is synthetic data okay?**

Microsoft markets this model with the phrase “no synthetic data and no distillation,” which sounds like an absolute: nothing AI-generated anywhere in the process. The truth is more nuanced, and the report is up-front about that.

In pre-training, the claim is literal: no AI-generated text goes into the corpus, and AI-generated content found in the wild gets scrubbed out. But post-training is full of synthetic material. The coding problems include AI-generated bugs and tests. The tool-use training relies on more than 150 fully synthetic environments (fake booking systems, fake inventory databases) containing 130,000 AI-generated tasks. Nobody at Microsoft hand-wrote those.

The distinction Microsoft is actually drawing: synthetic tasks are fine, synthetic teachers are not. What Microsoft refuses to do is let the model’s knowledge or reasoning style be inherited from some other lab’s model, which is what “distillation” means in this context: training your model to imitate a stronger model’s outputs. It’s the fast way to build a good model and most of the industry quietly does it. An AI-generated practice problem, by contrast, doesn’t teach the model to imitate anyone. The model still has to solve it on its own.

**It’s LLMs all the way down**

The last thing the report teaches is the one I’d most want an AI engineer to take away: a frontier model is built by AI systems doing jobs you would recognize from your own work.

LLM agents, not humans, wrote the container configurations that turned 4.87 million GitHub pull requests into executable training environments, of which about 266,000 survived validation. LLM judges scored web pages for quality during data curation, and rather than hand-tweaking the judge’s instructions, Microsoft used [prompt-optimization tools](https://arize.com/blog/prompt-optimization-few-shot-prompting/) that automatically generate variations of the judge’s prompt, test each one against roughly 2,000 human-labeled examples, and keep whichever version agrees with the humans most. LLM monitors watched the training process for the cheating described above. Judges, agents, evals, monitoring: the inside of a frontier lab’s pipeline is the same shape as the agent and evaluation work I do in [Arize AX](https://arize.com/docs/ax/), just at mind-boggling scale. (See also [Building the AI factory for self-improving agents](https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/).)

One detail I love: some of those pipeline models are Qwen models, Alibaba’s open-weights family. Microsoft used a Qwen model as the optimized quality judge and Qwen embeddings to find semantically duplicate documents. The flagship American enterprise model, trained on proudly clean and licensed data, was partly curated by Chinese open-source models. The report states this plainly, in the appendix, like it’s nothing.

**Why did Microsoft publish all of this?**

Labs went quiet about training for competitive reasons, so it’s fair to ask why Microsoft just handed out this textbook. You can find the answer in the same keynote where they announced the model: alongside the models, Microsoft launched Frontier Tuning, which sells enterprises on customizing MAI models with their own data and workflows inside their own compliance boundary. If your pitch is “bring us your proprietary data and we’ll tune a model on it,” then “here is exactly how we train, on clean, licensed, traceable data” is a key part of the sales pitch.

Regardless of motive, the result is the first readable end-to-end account of frontier model training in years, and it demystifies the whole process in a way I think is great. The data work is janitorial. The big decisions are made with small, cheap experiments. The behavior you experience as intelligence is installed by graders and reward signals after the fact. And the people building these things are running agents, judges, and evals, same as you.
