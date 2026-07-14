---
title: Building a RAG app with MongoDB Atlas
topic: rag-retrieval
subtopic: pipelines
secondary_topics: []
summary: Walkthrough of building a RAG app with MongoDB Atlas, covering retrieval
  setup, model calls, and evaluation of the generated answers.
source: braintrust
url: https://www.braintrust.dev/blog/rag-mongodb
author: Braintrust Team
published: '2024-11-18'
fetched: '2026-07-11T04:33:25Z'
classifier: codex
taxonomy_rev: 1
words: 1211
content_sha256: 18db579dc6477caf6237e3a455525dcb29cb6146d276da591577412e87f6997e
---

# Building a RAG app with MongoDB Atlas

18 November 2024Ornella Altunyan7 min

Retrieval augmented generation (RAG) is a powerful technique for adding context to your LLM responses. However, retrieving the context typically involves API calls, and therefore, you can only iterate on RAG applications in your codebase. In Braintrust, you can simplify this workflow by instead pushing the retrieval tool from your codebase to our UI, then iterating with prompts and models in an intuitive interface until you get your desired results.

One of the most common RAG applications is an AI agent that answers questions about your documentation. Let's say you deploy one to your users, and you receive some feedback that they wish it included more code examples in its responses. Normally, you would have to jump into your codebase, tweak the prompt, and try out the changes. If you want to compare multiple versions side-by-side, you'd have to deploy each version separately.

Using Braintrust functions, a RAG agent can be defined as just two components:

- A system prompt containing instructions for how to retrieve content and synthesize answers
- A vector search tool, implemented in TypeScript, which embeds a query, searches for relevant documents, and returns them

This architecture enables you to experiment with different prompts together with retrieval logic, side-by-side, all within the playground UI.

Let's jump into the details.

To follow along, you'll need a few accounts:

and `node`, `npm`, and `typescript` installed locally.

When you log into your Atlas account, you'll need to [create a new cluster](https://www.mongodb.com/docs/guides/atlas/cluster/). Call it `braintrust-docs`, and configure your [network access](https://www.mongodb.com/docs/guides/atlas/network-connections/) to allow the IP address `0.0.0.0/0`.

This makes your cluster accessible to everyone that is a database user in your Atlas account. Do not use this IP address for enterprise clusters.

Find the [connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/) for your cluster, and add it to a new `.env.local` file along with your Braintrust API key:

bash

```
BRAINTRUST_API_KEY=<your-api-key>
MONGO_URI=<your-mongodb-uri>
```
Make sure to set your `OPENAI_API_KEY` environment variable in the [AI providers](https://www.braintrust.dev/app/braintrustdata.com/settings/secrets) section of your Braintrust account.

The first thing we'll do is upload the files we want to give the LLM for context. First, download this [ docs-sample directory](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/ToolRAG/tool-rag/docs-sample) from GitHub— these documents are various parts of the Braintrust documentation and blog.

Then, we'll upload them in the form of vectors to our database.

To upload the vectors, download the [ upload-vectors.ts](https://gist.github.com/ornellaaltunyan/7d1103bfd77e7d65cb7c4ba70c871aa1) file onto your computer and run the script:

bash

```
npx tsx upload-vectors.ts
```
This script reads all the files from the `docs-sample` directory, breaks them into sections based on headings, and creates vector embeddings for each section using OpenAI's API. It then stores those embeddings along with the section's title and content in MongoDB Atlas.

That's it for setup! Now let's try to retrieve the vectors using Braintrust.

Braintrust allows you to create RAG tools and then run them in the UI, API, and via prompts, enabling you to quickly iterate on assistant-style agents.

The retrieval tool is defined in [ retrieval-and-prompt.ts](https://gist.github.com/ornellaaltunyan/c9d6a4cafa623cb6eb05dab6da8dba23). You'll need to download the file onto your computer to be able to run it.

This code takes a search query, converts it into a numerical vector using OpenAI's embedding model, and then sends that vector to Atlas to find the most similar items stored in the database. It retrieves the top results based on similarity and returns key information (title and content) from the matching items.

To push the tool to Braintrust, run:

bash

```
npx braintrust push retrieval-and-prompt.ts
```
The output should be:

```
1 file uploaded successfully
```
To try out the tool, visit the project in Braintrust, and navigate to **Tools**.

Here, you can test different searches and refine the logic. For example, you could try playing with various
`top_k` values, or adding a prefix to the query to guide the results. If you change the code, run
`npx braintrust push retrieval-and-prompt.ts` again to update the tool.

When we pushed `retrieval-and-prompt.ts`, we also pushed an initial definition of the prompt to Braintrust:

javascript

```
  messages: [
    {
      role: "system",
      content:
        "You are a helpful assistant that can " +
        "answer questions about the Braintrust documentation.",
    },
    {
      role: "user",
      content: "{{{question}}}",
    },
  ],
```
You can run the prompt in the UI and even try it out on some examples:

If you visit the **Logs** tab, you can check out detailed logs for each call:

![Prompt logs](https://www.braintrust.dev/blog/img/mongo/Prompt-logs.png)


We recommend using code-based prompts to initialize projects, but we'll show how convenient it is to tweak your prompts in the UI in a moment.

To get a better sense of how well this prompt and tool work, let's upload a dataset with a few questions and assertions. The assertions allow us to test specific characteristics about the answers, without spelling out the exact answer itself.

The dataset is defined in [ questions-dataset.ts](https://gist.github.com/ornellaaltunyan/2bfe0b81c03959b5514e4d20a923c695). You'll first need to download it to your computer from GitHub. Then, upload it to Braintrust by running:

bash

```
npx tsx questions-dataset.ts
```
Once you create it, if you visit the **Datasets** tab, you'll be able to explore it:

![Dataset](https://www.braintrust.dev/blog/img/mongo/Dataset.png)


To try out the prompt together with the dataset, we'll create a playground. Go to your prompt, and scroll down to **Create playground with prompt**.

Once you create the playground, hit **Run** to run the prompt and tool on the questions
in the dataset.

Now that we have an interactive environment to test out our prompt and tool call, let's define a scorer that helps us evaluate the results.

Select the **Scorers** dropdown menu, then **Create custom scorer**. Choose the **LLM-as-a-judge** tab, and enter

javascript

```
Consider the following question:
{{input.question}}
and answer:
{{output}}
Does the answer satisfy each of the following assertions? Meticulously check each one, and write out your reasoning in the rationale section.
{{#expected.assertions}}
{{.}}
{{/expected.assertions}}
a) It correctly satisfies every assertion.
b) It satisfies some of the assertions
c) It satisfies none of the assertions
```
For the choice scores, configure (a) as 1, (b) as 0.5, and (c) as 0.

![Choice scores](https://www.braintrust.dev/blog/img/mongo/Choice-scores.png)


Once you define the scorer, hit **Run** to run it on the questions in the dataset.

![Playground with scores](https://www.braintrust.dev/blog/img/mongo/Playground-scored.png)


Now, let's tweak the prompt to see if we can improve the results. Hit the copy icon to duplicate your prompt and start tweaking. You can also tweak the original prompt and save your changes there if you'd like. For example, you can try instructing the model to always include a Python and TypeScript code snippet.

Once you're satisfied with the prompt, hit **Update** to save the changes. Each time you save the prompt, you
create a new version. To learn more about how to use a prompt in your code, check out the
[prompts guide](https://www.braintrust.dev/docs/evaluate/write-prompts#using-prompts-in-your-code).

The playground is very interactive, but if you'd like to create a more detailed evaluation, where you can:

- See every step, including the tool calls and scoring prompts
- Compare side-by-side diffs, improvements, and regressions
- Share a permanent snapshot of results with others on your team

then you can run a full experiment by selecting **+Experiments**. Once you run the experiments, you can dig in further to the full analysis:

![Experiment](https://www.braintrust.dev/blog/img/mongo/Experiment.png)


Now that you've built a RAG app in Braintrust, you can:

- [Deploy the prompt in your app](https://www.braintrust.dev/docs/deploy/prompts)
- [Conduct more detailed evaluations](/docs/evaluate
- Learn about [logging LLM calls](https://www.braintrust.dev/docs/instrument)to create a data flywheel
