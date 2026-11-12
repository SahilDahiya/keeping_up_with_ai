---
title: How Baseten is using "docs as code" to build best-in-class documentation
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/docs-as-code
author: Philip Kiely
published: '2022-03-09'
fetched: '2026-11-12T06:12:56Z'
classifier: null
taxonomy_rev: 2
words: 1032
content_sha256: 8c58cc419457fb9e45da0c96dea4a3e0b9cdbe8b7145e992e81ce6fe5765e26c
---

# How Baseten is using "docs as code" to build best-in-class documentation

Community
# How Baseten is using "docs as code" to build best-in-class documentation

"Docs as code" uses code tools/practices for documentation, easing engineers' contributions, enhancing quality, and saving time.


- Authors
- Date
- March 9, 2022

When I joined Baseten as a technical writer in January 2022, I was impressed by how much high-quality writing a small company had managed to produce while working heads-down on building an ambitious product. Baseten has a long-running project to support every team member in writing and publishing a blog post on a topic of their choosing, from photo restoration to [parental leave](https://www.baseten.co/blog/designing-parental-leave-at-an-early-stage-startup/).

While a blog post is a one-time commitment that can be scheduled out and easily prioritized relative to other work, documentation must grow and evolve alongside the product. Every enhancement and new feature shipped gives docs a chance to fall behind. While I was hired to help our docs keep pace with the rapid iteration of our product, in order to provide truly best-in-class docs for a technical audience, we need to directly include the engineers in creating the documentation.

When I joined Baseten, [our documentation](https://docs.baseten.co/?utm_source=engineering&utm_medium=blog&utm_campaign=docs_as_code) was hosted on GitBook, but there was discussion of switching to another solution. I started by taking a step back to understand the needs of all four groups of stakeholders:

- Engineers, who want to use familiar tools that minimize the friction of writing documentation
- Marketers, who need to be able to make updates without relying on technical workflows
- Designers, who ensure that the docs have consistent branding and style with the rest of our sites
- Your friendly neighborhood technical writer (me!), who owns the docs site and related outcomes. I need to write large chunks of documentation, review other peoples’ changes, get my own changes reviewed, and establish internal workflows and documentation for technical writing.

While our existing system had a lot going for it — the simple web interface had enabled our team to publish thousands of words of customer-facing documentation covering key features — I realized that there was a big opportunity to improve the experience for engineers.

Previously, for an engineer to contribute docs for the first time, they had to get a GitBook account set up, then use the web interface to draft docs. From there, changes went live instantly, unless they chose to use GitBook’s review tool. In all, this was too much friction for small changes and not enough flexibility for large ones. More than updating our tooling, we needed to update our whole approach to take the next step in documenting the Baseten platform. Enter … docs as code!

[Docs as code](https://www.writethedocs.org/guide/docs-as-code/) is a philosophy of writing documentation with the same tooling and practices as writing code, from each developer’s preferred text editor to a version-controlled publishing sequence with pull requests, build previews, and even automated testing. Combined with a web interface for non-technical contributors, a docs as code workflow satisfies all four stakeholders.

Fortunately, our existing docs solution, GitBook, offers a GitHub sync which enables a docs as code workflow. We just needed to set it up.

We did also evaluate other hosted options including Read the Docs and ReadMe, as well as self-hosting with a docs-oriented static site generator like Docusaurus or MkDocs. But a self-hosted option didn’t seem feasible for an immediate migration. While Read the Docs has a similar GitHub integration, and ReadMe has compelling visual features, we decided that no platform offered a complete package worth switching to.

Setting up the GitBook-GitHub sync was quick and painless. Pro tip for GitBook users: move the docs to a dedicated folder, and add a .gitbook.yaml file in the root of the repo with the following config:

yaml

```
root: ./docs
structure:  
    readme: README.md  
    summary: SUMMARY.md
```
This restructure lets you add an internally-facing README for your workflow documentation and style guide. With these in place, docs as code was up and running.

The GitBook-GitHub sync had one major lingering issue. The written word is powerful, but useful documentation often requires pictures, GIFs, and even videos to show, not just tell, how to use a product. Unfortunately, Git does not handle large blob files well, and a revision history across hundreds of megabytes of product screenshots and screencasts would make the repository painfully slow to use. While GitHub addresses this with Git LFS, GitBook doesn’t support Git LFS and, per their support team, doesn’t plan to.

Fortunately, our existing infrastructure offered solutions. Images and GIFs live on AWS S3, in a dedicated folder within the static asset bucket used for the production app, which already had a CDN configured through Cloudfront. Add Loom to create and host screencasts, and the GitHub repository can be text-only. Docs as code unlocks your normal toolbox to solve problems.

All of the tooling in the world is pointless unless someone actually uses it. Within an hour of the GitHub Sync going live, a developer made a one-line commit to the documentation. Since then, I have merged over a dozen pull requests to the docs, each one with a formal review to improve the baseline quality of our documentation.

Docs as code is more than just a GitHub integration, it is a philosophy and process that merits continuous investment. Besides the technical setup, we:

- Added a documentation style guide
- Wrote meta-documentation on how to contribute docs
- Incorporated documentation tasks into our work tracking system

These human-facing improvements help everyone know what to write and how to write it. Plus, establishing a role that owns docs lets developers pop in when they have something to contribute without getting sidetracked by technical debt within the docs themselves.

Part of our continuous investment in docs moving forward is complete coverage of platform features, followed by in-depth references for view components and model templates. To fully satisfy our designers and my own interest in customized workflows, a self-hosted and fully branded docs site is definitely in our future. At Baseten, we prioritize investing in tooling for developer productivity and quality of life, and our recent transition to docs as code shows that these investments can be iterative and incremental while yielding real value.

Baseten’s documentation is available at [docs.baseten.co](https://docs.baseten.co/?utm_source=engineering&utm_medium=blog&utm_campaign=docs_as_code).
