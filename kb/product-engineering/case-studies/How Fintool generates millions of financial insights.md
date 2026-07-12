---
title: How Fintool generates millions of financial insights
topic: product-engineering
subtopic: case-studies
secondary_topics:
- evals-observability/monitoring
summary: Case study of Fintool generating financial insights at scale, using evaluation
  and observability to manage quality in high-volume AI workflows.
source: braintrust
url: https://www.braintrust.dev/blog/fintool
author: null
published: '2026-01-01'
fetched: '2026-07-11T04:32:17Z'
classifier: codex
taxonomy_rev: 1
words: 819
content_sha256: 7638d654032fe2afe989df405ef59f592fb1dc06e9c061dc9c631b924f842e16
---

# How Fintool generates millions of financial insights

With [Nicolas Bustamante](https://www.linkedin.com/in/bustamantenicolas/), CEO & Co-founder

1.5B

Tokens processed daily

70M

Document chunks analyzed

![Fintool Feed](https://www.braintrust.dev/customers/stories/fintool/fintool-feed.png)


[Fintool](https://fintool.com/?utm_source=braintrust&utm_medium=blog&utm_campaign=case-study) is an AI equity research assistant that helps investors make better decisions by processing large volumes of unstructured financial data, from SEC filings to earnings call transcripts. They serve leading institutional investors such as Kennedy Capital and First Manhattan, as well as companies like PricewaterhouseCoopers.

For institutional investors, trust is paramount, and a single overlooked disclosure can have serious consequences. However, the sheer volume of daily regulatory filings makes it impossible for humans to review every document. Fintool addressed this problem by developing Fintool Feed, a Twitter-like interface where they summarize key sections of documents based on user prompts. Investors select the companies they want to monitor and configure alerts by specifying what type of information they want to be summarized.

However, the team soon realized the need for real-time monitoring to maintain quality and user confidence. They faced a few key challenges:

- Managing over 1.5 billion tokens across 70 million document chunks while processing gigabytes of data daily.
- User prompts ranging from broad compliance monitoring to particular disclosures, like board membership changes.
- The need for superior accuracy and reliability.

In this case study, we'll share how Fintool used Braintrust to develop a repeatable evaluation workflow that scales to massive amounts of data while maintaining trust in high-stakes financial contexts.

1.5B tokens daily + trusted insights

Define quality standards + format rules

Curate golden datasets

Automate evals with LLM-as-a-judge

Add human in the loop oversight

Fintool makes sure every insight includes a reliable source, like an SEC document ID, and automatically flags anything that’s missing or doesn’t look right. This is a big deal in finance, where trust comes down to having data you can verify.

They don’t just check that sources are included. They also make sure they’re valid, properly formatted, and tied directly to the insights. The team set up custom rules in Braintrust, like requiring SEC IDs and double-checking quoted text, and real-time monitoring catches anything that doesn’t meet the standards.

![Format rules](https://www.braintrust.dev/customers/stories/fintool/format-rules.png)


Fintool also uses span iframes to show citations within trace spans, so expert reviewers can quickly validate the content.

![Format rules](https://www.braintrust.dev/customers/stories/fintool/span-iframes.png)


Fintool leverages Braintrust’s tools to benchmark the quality of LLM outputs in real time. The engineering team crafts golden datasets tailored to specific industries and document types, like healthcare compliance or tech KPIs.

The golden datasets are built by combining production logs with handpicked examples that reflect real-world scenarios, which helps the datasets stay fresh as Fintool processes over 1.5 billion tokens across 70 million data chunks daily.

Each generated insight is evaluated using LLM-as-a-judge scorers on key metrics like accuracy, relevance, and completeness. Braintrust automatically updates whenever Fintool adjusts prompts or ingests new data, preventing surprise regressions and saving valuable engineering resources.

python

```
FORMAT_PROMPT = """You are a format validator. Check if the following text follows this format:
1. A short business description paragraph
2. Followed by a markdown numbered list of product lines, where each bullet point:
    - Starts with the product name
    - Contains a short description of the product line
Text to validate:
<text>
{output}
</text>
Respond with:
"PASS" if it follows the format perfectly
"FAIL" if it deviates from the format"""
format_quality = LLMClassifier(
    name="Format Check",
    prompt_template=FORMAT_PROMPT,
    choice_scores={"PASS": 1, "FAIL": 0},
)
```
Using automated scoring functions frees up bandwidth for human reviewers to focus on the toughest cases.

When content gets a low score or is downvoted, a human expert is immediately notified to step in. They can approve, reject, or edit the Markdown to fix issues like poor formatting. Since the Fintool database is linked directly to Braintrust, the expert can update the live content right from the Braintrust UI.

![Human review](https://www.braintrust.dev/customers/stories/fintool/human-review.png)


This quick response means that any problems are addressed and improved as soon as possible.

This evaluation workflow has helped Fintool manage millions of LLM-generated insights, improving accuracy, consistency, and efficiency at scale. By streamlining their eval process, Fintool is able to make sure their financial summaries and alerts meet the highest standards of trust and reliability. Key successes include:

- Scalability: Fintool now processes millions of datapoints daily, delivering reliable financial insights at scale without compromising quality. Automating evals allows human reviewers to focus on the most challenging cases.
- Efficiency: Automated, real-time evals makes detecting and resolving quality issues faster
- Accuracy: Enforcing rigorous citation and format validation rules improved the precision of Fintool insights to make sure they meet the specific needs of institutional investors
- Convenient human review: Human reviewers can intervene quickly and manage edits and updates right from the Braintrust UI

Fintool has set a new standard for financial AI, delivering timely and actionable insights with accuracy and efficiency.

Fintool processes 1.5 billion tokens daily while maintaining rigorous citation standards. Learn how Braintrust enables automated quality checks, human-in-the-loop oversight, and real-time monitoring for high-stakes AI applications.
