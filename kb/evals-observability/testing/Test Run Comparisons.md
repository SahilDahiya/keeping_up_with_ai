---
title: Test Run Comparisons
topic: evals-observability
subtopic: testing
secondary_topics:
- evals-observability/evaluation
summary: Explains test-run comparisons for evaluating changes across LLM application
  versions and identifying regressions.
source: langchain
url: https://www.langchain.com/blog/test-run-comparisons
author: The LangChain Team
published: '2023-10-17'
fetched: '2026-07-11T04:39:15Z'
classifier: codex
taxonomy_rev: 1
words: 647
content_sha256: f4dac5b9ed8fe684b214f0d0b256926a771e8690a45c3f5d5b22202cebd0fa15
---

# Test Run Comparisons

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb122c83ac7211fe594d2_Screenshot-2023-10-14-at-3.42.23-PM-1.png)

One pattern I noticed is that great AI researchers are willing to manually inspect lots of data. And more than that, they build infrastructure that allows them to manually inspect data quickly. Though not glamorous, manually examining data gives valuable intuitions about the problem.[- Jason Wei, OpenAI](https://twitter.com/_jasonwei/status/1708921475829481683?s=20&ref=blog.langchain.com)

Evaluations continue to be one of the hardest parts of building LLM applications. It's really tough to evaluate in a quantitative way the effect of changes to your prompt, chain, or agent. We're bullish on [LLM-assisted evaluation](https://docs.smith.langchain.com/evaluation/evaluator-implementations?ref=blog.langchain.com), but, at the same time, we definitely recognize that it's hard to have complete trust in them.

Jason's tweet above sums up what we see a lot of the best researchers (and engineers) doing. They want to manually inspect data to gain intuition about the problem. At LangChain, we want to build the infrastructure to help do that - which is why we're excited to announce Test Run Comparisons today.

In the [initial release of LangSmith](https://blog.langchain.com/announcing-langsmith/) we had support for running tests, including scoring them with LLM-assisted feedback. However, each test was run in isolation. We quickly saw two usage patterns emerge:

- People are still hesitant to trust the LLM-assisted feedback directly
- Users often wanted to not only score their test run in isolation, but also compare it to previous iterations

When building Test Run Comparisons, we kept both of these insights in mind. We wanted to create an easy UX to see multiple test runs side-by-side. We also wanted to create an easy UX where people could use LLM-assisted evals (or regex/other eval) to get an initial score, then manually explore those datapoints for further insights.

So how does it work?

First, you need to set up a dataset and run some tests. See [documentation here](https://docs.smith.langchain.com/evaluation?ref=blog.langchain.com) for instructions on how to do that. Nothing new here, so if you've already done that for an existing project you're all good.

Inside a dataset, you can easily select two (or more) test runs, then click `Compare`.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594e4_Screenshot-2023-10-14-at-3.42.42-PM.png)

From there, you will be brought into the Test Run Comparison view. This should look like the below

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb122c83ac7211fe594d2_Screenshot-2023-10-14-at-3.42.23-PM-1.png)

You can easily see the inputs, the reference output, and then the actual output for each datapoint - along with any [eval metrics](https://www.langchain.com/resources/llm-evaluation-metrics), time and latency for that run.

This view is designed to make it easy to quickly compare test runs across the same inputs. If you want a deeper look at a particular datapoint, you can click on that row and sidebar will pop up allowing you to drill down into the details of those runs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594dd_Screenshot-2023-10-14-at-3.46.17-PM.png)

On that sidebar, we've also added up and down carets (▲ and ▼) to easily flip between runs.

This view should hopefully make it easy to compare runs for a particular datapoint. But how do you know what datapoints to be looking at?

We've added filters for each column - similar to Excel. Using these filters, you can filter the rows according to any criteria.

💡

The criteria we recommend using to start? Filter one test run to datapoints it got correct, and the other one to datapoints that it got incorrect. This allows you to quickly drill on places of significant difference between the two test runs, which should more easily allow you to discover what has changed.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594da_Screenshot-2023-10-14-at-3.53.17-PM.png)

Building an LLM application is hard. A big part of that is understanding how the LLM is working on a particular task. Setting up an evaluation dataset and then being able to easily compare runs on that dataset is crucial for developing the understanding needed to improve the application. Test Run Comparison in LangSmith aimed at solving this problem. Please let us know any feedback you have!

LangSmith is in private beta - [sign up here](https://smith.langchain.com/?ref=blog.langchain.com). We'll be rolling out more access over the next few weeks, as well as continuing to add features like this.
