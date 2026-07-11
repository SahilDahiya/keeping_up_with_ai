---
title: Lessons From Building an Early ChatGPT Plugin In Under 24 Hours
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/tool-use
summary: Retrospective on building an early ChatGPT plugin quickly, including product
  workflow lessons and integration constraints from the plugin ecosystem.
source: arize
url: https://arize.com/blog/building-chatgpt-plugin/
author: Erick Siavichay
published: '2023-04-28'
fetched: '2026-07-11T04:46:53Z'
classifier: codex
taxonomy_rev: 1
words: 2876
content_sha256: 81d07feb4a893be4eb4734af35b92fd3e9830c5fdd0e94310fbc54b1338eab42
---

# Lessons From Building an Early ChatGPT Plugin In Under 24 Hours

![observe-team-cerebral-valley-chatgpt-plugins-hackathon cerebral valley openai sponsored hackathon for creating chatgpt plugins](https://arize.com/wp-content/uploads/2023/04/observe-team-cerebral-valley-chatgpt-plugins-hackathon-1021x560.jpg)

              # Lessons From Building an Early ChatGPT Plugin In Under 24 Hours

## Cerebral Valley’s ChatGPT Plugins Hackathon offered a sneak peek of a burgeoning new ecosystem and best practices learned the hard way from creating a new plugin from scratch (meet Observe!)

*This blog is a collaboration with Aparna Dhinakaran, Chief Product Officer and Co-Founder of Arize AI; Francisco (“Kiko”) Castillo Carrasco, a Data Scientist and Software Engineer at Arize AI; and Xander Song, Developer Advocate at Arize AI*

OpenAI’s ChatGPT plugin system is a game-changing way to integrate ChatGPT with third-party APIs. The plugin system is still in alpha and is not yet available to the public, but we got access by competing at a [plugin hackathon](https://twitter.com/cerebral_valley/status/1646984708956512256) sponsored by OpenAI.

This is the story of how we built a plugin for large language model (LLM) observability overnight and reached the finals of the competition.

## What Is a ChatGPT Plugin?

OpenAI’s plugins offer a way to connect ChatGPT to third-party applications, allowing ChatGPT to interact with APIs defined by developers. This enhances ChatGPT’s capabilities, enabling it to perform a wide range of actions, such as retrieving real-time information (e.g., by browsing the web), knowledge-base information (e.g., by accessing a database), and performing actions on behalf of the user (e.g., placing a delivery order, entering values in a spreadsheet, sending an email).

## What Do You Need To Create an OpenAI Plugin?

To build an OpenAI plugin, developers need to create:

- a manifest file
- an OpenAPI specification
- the API itself

The plugin manifest contains metadata about the plugin and the API, while the OpenAPI specification provides a natural language description of each endpoint in a RESTful API, along with the format and meaning of any inputs and outputs. This allows ChatGPT to intelligently call the endpoint when it thinks it should and interpret the responses.

The release of OpenAI’s plugin system has been likened to the creation of the app store because plugins extend chatbots such as ChatGPT beyond their default capabilities like an app does for a smartphone. In our opinion, the plugin system has the look and feel of a transformative technology.

## LLM Observability and the Observe Plugin

Large language models (LLMs) like GPT-4 are seeing rapid adoption as a way to drive growth and reduce customer pain points. Companies like [Stripe](https://www.pymnts.com/artificial-intelligence-2/2023/stripe-says-its-building-the-payments-foundation-for-tomorrows-ai-economy/), [Duolingo](https://openai.com/customer-stories/duolingo), and Shopify use LLMs to streamline user experience, teach people new languages, and provide shopping assistance. However, LLMs are not perfect. They can sometimes produce “ungrounded” responses that are inaccurate or fail to answer questions altogether. These issues can lead to customer dissatisfaction, loss of trust, churn, and even brand damage.

Many teams face difficulties in evaluating and diagnosing LLMs in production. Traditional approaches like manual review of production data are time-consuming and unscalable, hence the need for [ LLM observability](https://arize.com/llm/). An LLM-based system is

*observable*if it provides a quick and easy way to detect and understand the root cause of production issues and to make improvements. In 24 hours, we built an OpenAI plugin for LLM observability called Observe to help data scientists and engineers analyze and resolve production LLM issues. Observe takes in data stored in a cloud storage bucket and:

- Extracts embeddings for the data
- Reduces the dimensionality of the data with UMAP
- Clusters the data using HDBSCAN
- Generates cluster summaries with the help of GPT-4
- Visualizes the data in lower dimensions within the ChatGPT interface

## Plugin Components

### API

Let’s start with the API itself. The table below shows the endpoints we implemented in addition to the prompts in our OpenAPI spec that describe the purpose of the endpoints, the meaning of each parameter, and an example response. We’ll illustrate what each endpoint does later in the article with examples.

![](https://arize.com/wp-content/uploads/2023/04/openai-chatgpt-plugin-hackathon-observe-table.jpg)


### Manifest File

The manifest file contains metadata about your plugin that tells ChatGPT when to use your plugin. The manifest file for the Observe Plugin is shown below. The important field is `description_for_model`, which states the purpose of the plugin to ChatGPT. In addition, note that the URLs point to localhost for local development; you must change this field to the production domain once the plugin is ready to be deployed. Finally, there is a path to the specification yaml file, which we’ll discuss next.

```
{
    "schema_version": "v1",
    "name_for_human": "Observe Chat",
    "name_for_model": "observeChat",
    "description_for_human": "Plugin to inspect unstructured data, understand key differences by grouping similar data points into clusters.",
    "description_for_model": "Plugin to inspect unstructured data, understand key differences by grouping similar data points into clusters.",
    "auth": {
        "type": "none"
    },
    "api": {
        "type": "openapi",
        "url": "http://localhost:8000/openapi.yaml",
        "is_user_authenticated": false
    },
    "logo_url": "http://localhost:8000/logo.png",
    "contact_email": "support@example.com",
    "legal_info_url": "https://example.com/legal"
}
```
### OpenAPI Specification

Once ChatGPT has decided to use a particular plugin, it looks at the `openapi.yaml` specification file to figure out what each endpoint of the API does, what data to pass, and how to interpret the response. Below is the specification file for our plugin. Each endpoint has a summary field that describes its purpose in natural language. Each parameter in the parameters field is accompanied by a description. Lastly, the responses from each endpoint are described by the schemas in the components section, and once again, each field of the output is accompanied by a natural language description.

```
openapi: 3.0.1
info:
    title: Observe Plugin
    description: Plugin to inspect unstructured data, understand key differences by grouping similar data points into clusters.
    version: "v1"
servers:
    - url: http://localhost:8000
paths:
    /explore/{url}:
        get:
            operationId: exploreData
            summary: Help me explore and understand data given an url. If a URL is not given, ask for one.
            parameters:
                - in: path
                  name: url
                  schema:
                      type: string
                  required: true
                  description: The URL where the data is stored.
            responses:
                "200":
                    description: OK
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/exploreResponse"
    /clusters/{cluster_id}/sample/{n_samples}:
        get:
            operationId: sampleCluster
            summary: Sample my cluster and extract a given number of points inside a cluster and show the text in them
            parameters:
                - in: path
                  name: cluster_id
                  schema:
                      type: string
                  required: true
                  description: ID of the cluster.
                - in: path
                  name: n_samples
                  schema:
                      type: integer
                  required: true
                  description: Number of samples
            responses:
                "200":
                    description: OK
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/clusterSampleResponse"
    /visualize:
        get:
            operationId: visualizeData
            summary: Creates a UMAP plot with all clusters and returns a URL to it. You should load it and show it to the user.
            responses:
                "200":
                    description: OK
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/visualizeResponse"
    /locate/{cluster_id}:
        get:
            operationId: locateCluster
            summary: Locates a cluster of points in a UMAP plot by coloring the points belonging to the target cluster in a stronger color and opacity than the rest. You should load it and send it to the user.
            parameters:
                - in: path
                  name: cluster_id
                  schema:
                      type: string
                  required: true
                  description: ID of the cluster.
            responses:
                "200":
                    description: OK
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/locateResponse"
components:
    schemas:
        exploreResponse:
            type: object
            properties:
                clusters:
                    type: array
                    items:
                        type: string
                    description: The list of clusters, each with their ids and summaries. If a cluster id is -1, call it the "noise cluster", i.e. the cluster with data points that didn't belong to any cluster"
        clusterSampleResponse:
            type: object
            properties:
                textData:
                    type: array
                    items:
                        type: string
                    description: The list of text that belong to that cluster
        visualizeResponse:
            type: object
            properties:
                url:
                    type: string
                    description: The URL to the UMAP plot with the points colored by cluster id.
        locateResponse:
            type: object
            properties:
                url:
                    type: string
                    description: The URL to the UMAP plot with the desired clustered highlighted in comparison to the rest.
```
The summaries and descriptions in the specification file are important because they tell ChatGPT when and how to use each endpoint. When developing a plugin, your prompts often won’t work on the first try, so you’ll have to iterate and experiment. The OpenAI documentation provides [best practices](https://platform.openai.com/docs/plugins/getting-started/writing-descriptions) for writing these descriptions.

## User Flow

### Explore Your Data

![chatgpt plugin observe understanding your data better step](https://arize.com/wp-content/uploads/2023/04/chatgpt-plugins-observe-understsand-data.png)


When the user enters the message “Would you help me understand my data located in …”, ChatGPT recognizes from the description in our plugin manifest file that it should use the Observe plugin. It also recognizes from the descriptions in the OpenAPI spec that it should use the `/explore` endpoint for this particular request. The `/explore` endpoint:

- Downloads the data at the specified URL
- Computes embeddings using a pre-trained language model for each piece of text
- Reduces the dimensionality of the embedding data to two dimensions using UMAP
- Clusters the low-dimensional data using HDBSCAN
- Generates summaries of each cluster

The data computed in this step is saved in memory and accessed by other endpoints. We’ll next dive into what was for us the most novel component of the project, generating cluster summaries using the OpenAI API.

## Summarizing Clusters with the OpenAI API

We use OpenAI’s GPT-4 API to perform summarization, analyze sentiment, and determine the topic of each cluster’s text. With GPT-4, we can further interact with ChatGPT to reason about these clusters. First, we will cover the basics of the OpenAI [Create Chat Completion API](https://platform.openai.com/docs/api-reference/chat/create).

#### OpenAI API Call


We create a wrapper function called `call_openai_api` around OpenAI’s chat completion Python call. This function accepts two parameters:

- `context`– a list of- *messages*, described later, containing the chat history that the model uses to understand what’s happened so far and to contextualize the user’s next query.
- `prompt`– an optional parameter, the string that represents what the user entered into the chat

The function appends new user messages to the end of the context list and returns the chatbot’s response as a string.Next, we will cover what the messages parameter does in the `openai.ChatCompletion.create` function call.

#### Messages

This is a list-like parameter that contains the history of chat messages or changes to the behavior of the chatbot. A message is a dictionary of the following format:

```
{
"role": <string, one of “user”, “assistant”, or “system”>,
"content": <string, the message itself>,
}
```
The “role” key represents the role of this message. Here are the possible string values:

- “user” – this message is coming from the user
- “assistant” – this message is coming from the GPT-4 model
- “system” – allows developers to set the behavior of the model

The “content” key represents the actual message itself. For the “user” or “assistant” roles, the value to the “content” key is the actual message. If the role is “system”, then the value is a prompt-engineered text that describes how the chatbot should behave and respond.

Here’s an example of how we initialized a context variable with an initial system message that will later be passed into the `call_openai_api` function:


We recommend developers to initialize the context variable with a descriptive system message so that the behavior of the model aligns as much as possible the intention of the API call. Usually, you only set this once unless you want to change how you want the chatbot to respond midway through the conversation.

The context variable has a [maximum content capacity](https://platform.openai.com/docs/models/gpt-3-5) of ~8000 [tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) for GPT-4, including the message history between the user and chatbot, so we are limited with how much content we can fit inside, loading in cluster textual information, and any other text interaction with the chatbot.

## Summarization

With GPT-4, summarization tasks become more expressive and allow both the developer and the end-user to interact with fluid, responsive chatbots. With how we initialized the context variable with the system message, GPT-4 is able to analyze all of the messages and generate a summary in the format we want.

To summarize a cluster of texts, we append all texts in a cluster into a single string separated by a token we call **<DIVIDER>**, and then make a call via our wrapper function by passing this string of token-separated texts as a prompt. This is the user’s prompt, so this message gets appended to the context variable under the “user” role. We get a summarization of the cluster that follows the response format as specified in the initial system message. This summarization is appended to the context variable under the “assistant” role, whose content will be displayed to the user via the ChatGPT UI.

Behind the scenes, ChatGPT is storing the messages between the user and the model, including information about the clusters such as their IDs and descriptions, into its context. This allows the user to trigger other endpoints with information generated by triggering the summarization endpoint. We will next cover how we can sample items in a cluster after we have triggered the summarization endpoint.

## Get Examples from a Few Clusters

Next, the user asks for examples from a few clusters in order to get a better feel for their data.

![examples from clusters](https://arize.com/wp-content/uploads/2023/04/examples-from-clusters.png)


The thing to notice about this example is that ChatGPT is able to chain together multiple API calls. Under the hood, requests are made to `/clusters/0/sample/3` and `/clusters/6/sample/3`. Each time, the endpoint selects a random sample of three points from the clusters that were computed and saved in the previous step. ChatGPT not only recognizes that two requests must be made to fulfill the user’s request, but also combines both responses into a single reply to the user.

## Visualize Your Data within ChatGPT

A picture is worth a thousand words, so we provide a way for users to visualize their data inside the ChatGPT interface.

![data visualiziation within chatgpt with observe plugin](https://arize.com/wp-content/uploads/2023/04/load-data-visualize-within-chatgpt.png)


Under the hood, this calls the `/visualize` endpoint, which creates the plot using the saved cluster data, uploads the PNG to a public cloud storage bucket, and returns the URL. ChatGPT renders the image inside in the chat interface.

## Locate Clusters Within the Image

The user can pick out a particular cluster from the image just by asking.

![visualize data within chatgpt](https://arize.com/wp-content/uploads/2023/04/chatgpt-plugins-data-viz.png)


ChatGPT makes requests to `/locate/0` and `/locate/6`. Behind the scenes, the endpoint creates and uploads an image file (this time, highlighting the specified cluster) to cloud storage and returns the URL.

## How To Build An Effective ChatGPT Plugin: Takeaways

Based on our experience, here are a few best practices:

- OpenAI’s GPT models are capable of making multiple API calls and synthesizing the responses into a single output. As long as the prompts describing your input are well-written, ChatGPT knows the order in which to call endpoints (e.g., it knows to call **/explore/<url>**before**/visualize**) and knows to ask the user if it needs additional information to make a request (e.g., it knows to ask for the URL in a user requests to explore their data without providing the URL as part of the initial request).
- ChatGPT plugins can wrap existing APIs and can easily transfer existing applications into the ChatGPT ecosystem.
- Even after solid engineering work has been done to connect this matrix together, good prompt engineering skills are necessary to create a fluid experience for the user.
- The context size of a chat is analogous to the RAM of a physical computer; it’s nice to have more, but it’s important to manage it efficiently.

![Cerebral Valley ChatGPT Plugins Hackathon: Aparna Dhinakaran, Finalist, Pitching on MainStage](https://arize.com/wp-content/uploads/2023/04/aparna-pitching.jpg)


*Aparna pitching the Observe plugin on the main stage.*

![packed house at cerebral valley](https://arize.com/wp-content/uploads/2023/04/packed-house.gif)


*A packed house.*

![Cerebral Valley ChatGPT Plugins Hackathon: Francisco Castillo Carrasco fixing a bug](https://arize.com/wp-content/uploads/2023/04/cerebral-valley-chatgpt-plugins-kiko-fixing-bug.jpg)


*Kiko fixing a bug.*

![](https://arize.com/wp-content/uploads/2023/04/erick-demo-plugin.gif)


*Erick demoing the plugin.*

![cerebral valley openai sponsored hackathon for creating chatgpt plugins](https://arize.com/wp-content/uploads/2023/04/observe-team-cerebral-valley-chatgpt-plugins-hackathon.jpg)


*The amazing team that put all of this together in less than 24 hours.*

## Challenges and Next Steps for the Observe Plugin

What comes next for the Observe plugin? Here are a few thoughts:

- The context size for GPT-4 is currently limited by the OpenAI API to ~8000 tokens, which is only about 10 MB of text data and is much less than the 32K token context size that GPT-4 can actually handle. Even with a larger context size, improved context management practices and perhaps even a new approach would be needed to scale our solution to larger clusters with longer text.
- Although GPT-4 is multimodal, it was difficult to reliably get our UMAP 2D image loaded into the chat and ask ChatGPT reasoning questions such as “Can you explain what the top left cluster is about?”
- The prompts in our OpenAPI specification can be improved. We could evaluate the behavior of our plugin on ambiguous user input to see if ChatGPT clarifies ambiguous requests and asks for missing information. We could measure how well our plugin detects trigger phrases in the user’s prompt and how often it executes the appropriate endpoint(s).
- We built an MVP that handles text data, but our approach can be extended to other modalities. For tabular data, each row can be represented as a piece of text and embedded using a language model (see [this article](https://towardsdatascience.com/boosting-tabular-data-predictions-with-large-language-models-531337f834dc)for details). For image data, we can still get cluster summaries since GPT-4 is multi-modal.
- The speed of the plugin can be improved by parallelizing certain computations and caching datasets and cluster summaries.
- The tool can be augmented by integrating with existing ML observability products such as Arize and [Phoenix](https://phoenix.arize.com/).

## Shoutouts

Thanks to [Cerebral Valley](https://cerebralvalley.ai/) and [Shack15](https://www.shack15.com/) for putting on a great hackathon and supporting the grassroot energy of the generative AI movement!
