---
title: Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/rag-with-astro-fastapi-surrealdb-tailwind
author: null
published: '2024-08-14'
fetched: '2026-08-12T06:30:30Z'
classifier: null
taxonomy_rev: 2
words: 1954
content_sha256: ea17fb5bc19aef6c0a1ab3092929f16baae53f8dca7cf657973aef331b80c253
---

# Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1

Large Language Models have revolutionized how we retrieve information or build search systems. Retrieval-augmented generation (RAG) methodology has become a common way to access or extract information.

This guide teaches you how to build a Retrieval-Augmented Generation application using SurrealDB, Fireworks, FastAPI, and Astro. By the end of this guide, you will be able to update the chatbot’s knowledge visually and obtain the latest and personalized responses to your queries.

You'll need the following:

- •[Node.js 18](https://nodejs.org/en/blog/announcements/v18-release-announce) or later
- •A [Fireworks](https://fireworks.ai/api-keys) account

The following technologies are used in creating our RAG application:

| Technology | Type | Description | 
|---|---|---|
| FastAPI | Framework | A high performance framework to build APIs with Python 3.8+. | 
| Astro | Framework | Framework for building fast, modern websites with serverless backend support. | 
| TailwindCSS | Framework | CSS framework for building custom designs. | 
| SurrealDB | Platform | A multi-model database platform. | 
| Fireworks | Platform | Lightning-fast Inference platform to run generative AI models. | 

This is a high-level architecture of how data is flowing and operations that take place 👇🏻

- •When a user asks a question, relevant vectors to the latest user question are queried from SurrealDB. Further, they are combined with the user messages to create a system context. The response is then streamed to the user from Fireworks hosted [Llama 3.1 405B Instruct](https://fireworks.ai/models/fireworks/llama-v3p1-405b-instruct) Model.
- •When a user updates the existing knowledge other system, vector embeddings with metadata are created for the particular information, and then pushed to SurrealDB

You can find various methods to install and run the SurrealDB server in the [documentation](https://surrealdb.com/docs/surrealdb/installation/). Let's opt for installing SurrealDB using its dedicated [install script](https://github.com/surrealdb/install.surrealdb.com) for our scenario. In your terminal window, execute the following command:

12

The above command attempts to install the latest version of SurrealDB (per your platform and CPU type) into the `/usr/local/bin` folder in your system.

Once that is done, execute the following command in your terminal window:

The above command does the following:

- •Starts the SurrealDB server at `0.0.0.0:4304` network address.
- •Enables trace level logging producing verbose logs in your terminal window.
- •Sets the user and password of the default database as `root` .
- •Creates the file `mydatabase.db` to persist data on your filesystem.

Model inference requests to the Fireworks API require an API Key. To generate this API key, log in to your Fireworks account and navigate to [API Keys](https://fireworks.ai/api-keys). Enter a name for your API key and click the **Create Key** button to generate a new API key. Copy and securely store this token for later use as `FIREWORKS_API_KEY` environment variable.

Locally, set and export the `FIREWORKS_API_KEY` environment variable by executing the following command:

First, let's start by creating a new project. You can create a new directory by executing the following command in your terminal window:

1234

Next, you can install the required dependencies by executing the following command in your terminal window:

12345

The above command installs the required libraries to run ASGI Server, FastAPI, Fireworks, SurrealDB and LangChain in your Python project.

Next, create a file `main.py` with the following code:

12345678910111213141516171819202122

The above code imports the following:

- •`os` module to use the environment variable you’ve set earlier.
- •`List` to denote a list of elements of specific type.
- •`BaseModel` class to define models of the request body FastAPI endpoints.
- •`StreamingResponse` class to generate streaming responses from FastAPI endpoints.
- •`CORSMiddleware` FastAPI middleware to enable Cross Origin Resource Sharing of FastAPI endpoints.
- •`fireworks.client` SDK for conveniently accessing Fireworks supported LLMs.
- •`SurrealDBStore` class by LangChain to use SurrealDB as vector store.
- •`FireworksEmbeddings` class via LangChain Fireworks integration to use Nomic AI Embeddings Model.

To create the data types of request body in your FastAPI endpoints, append the following code in [main.py](http://main.py) file:

12345678910111213

The above code defines three [Pydantic](https://docs.pydantic.dev/latest/) models:

- •**LearningMessages** : a model that will store the input string with a single field called`messages` .
- •**Message** : a model that will store each message containing two fields,`role` and`content` .
- •**Messages** : a model that will store the input as a list of`Message` model.

To set the Fireworks API key used by Fireworks module internally, append the following code in [main.py](http://main.py) file:

123

The above code uses the `os` module to load the environment variable `FIREWORKS_API_KEY` as Firework’s API Key.

To use `FireworksEmbeddings` class to create an embeddings generator using the `nomic-ai/nomic-embed-text-v1.5`, append the following code in [main.py](http://main.py) file:

To define the SurrealDB vector store configuration, append the following code in [main.py](http://main.py) file:

123456

The above code uses the following values to establish a SurrealDB Vector Store with LangChain:

- •`ws://localhost:4304/rpc` as the database URL to establish a WebSocket connection with SurrealDB. Using a WebSocket connection allows to send and receive messages from SurrealDB using the WebSocket API.
- •`root` as both the username and password of the SurrealDB instance.
- •`vectors` as the collection name of the vector store to and from which the relevant vectors will be inserted and queried from.
- •Uses `embeddings` generator as the embedding function.

To initialize a FastAPI application, append the following code in [main.py](http://main.py) file:

123456789101112

The code above creates a FastAPI instance and uses the `CORSMIddleware` middleware to enable Cross Origin requests. This allows your frontend to successfully POST to the RAG application endpoints to fetch responses to the user query, regardless of the port it is running on.

To update application’s knowledge in realtime by generating vector embeddings and inserting them into SurrealDB, you’ll create an `/update` endpoint in your FastAPI application. Append the following code in [main.py](http://main.py) file:

12345678910

`update(messages: LearningMessages)` method -

- •Accepts a single string as `messages` containing comma (,) separated messages to be inserted in your SurrealDB vector store.
- •Awaits connection set up with SurrealDB.
- •Creates `metadata` list, each item being length of each message received as input.
- •Creates `ids` list, each item being a randomly generated id for each message received as input.
- •Using the `embeddings` generator passed as the embeddings function, it generates the vector embedding of each message. Alongwith each message’s metadata, it inserts the vector embedding into the SurrealDB vector store.

To generate personalized responses that uses the application’s existing knowledge, you’ll create an `/chat` endpoint in your FastAPI application. Append the following code in [main.py](http://main.py) file:

123456789101112131415161718192021

`chat(messages: Messages)` method -

- •Accepts a list of `Message` model as`messages` .
- •Awaits connection set up with SurrealDB.
- •Defines a system prompt to restrict it to answer what it already knows.
- •Performs a similarity search on the latest `Message` , which represents a user query.
- •Loops over all similar vector embeddings and appends them into the system prompt defined earlier.
- •Prepends a `Message` model, representing role of the system and it’s content as the system prompt created.
- •Uses fireworks Chat Completion API to stream LLAMA 3.1 70B Chat model context aware responses.
- •Returns a StreamingResponse using the `yield_content` function.

The `yield_content` function loops over each [Document](https://js.langchain.com/docs/modules/data_connection/document_loaders/creating_documents) (received as the similar vector with it’s metadata), and streams the `content` value of it as part of the API response.

With all that done, here’s how our [`main.py`](http://main.py) will finally look like containing both the endpoints:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293

Execute the following command in another terminal window:

The app should be running on [localhost:8000](http://localhost:8000/). Let’s keep it running while we create an user interface to invoke the endpoints to create responses to user queries.

Let’s get started by creating a new Astro project. Open your terminal and run the following command:

`npm create astro` is the recommended way to scaffold an Astro project quickly.

When prompted, choose the following:

- •`Empty` when prompted on how to start the new project.
- •`Yes` when prompted whether to write Typescript.
- •`Strict` when prompted how strict Typescript should be.
- •`Yes` when prompted to whether install dependencies.
- •`Yes` when prompted to whether initialize a git repository.

Once that’s done, you can move into the project directory and start the app:

The app should be running on [localhost:4321](http://localhost:4321/). Let's close the development server as we move on to integrate TailwindCSS into the application.

For styling the app, you will be using Tailwind CSS. Install and set up Tailwind CSS at the root of our project's directory by running:

When prompted, choose:

- •`Yes` when prompted to install the Tailwind dependencies.
- •`Yes` when prompted to generate a minimal`tailwind.config.mjs` file.
- •`Yes` when prompted to make changes to Astro configuration file.

With choices as above, the command finishes integrating TailwindCSS into your Astro project. It installed the following dependency:

- •`tailwindcss` : TailwindCSS as a package to scan your project files to generate corresponding styles.
- •`@astrojs/tailwind` : The adapter that brings Tailwind's utility CSS classes to every`.astro` file and framework component in your project.

To create reactive interfaces quickly, let’s move onto integrating React in your application.

To prototype the reactive user interface quickly, you are gonna use React as the library with Astro. In your terminal window, execute the following command:

`npx` allows us to execute npm packages binaries without having to first install it globally.

- •`Yes` when prompted whether to install the React dependencies.
- •`Yes` when prompted whether to make changes to Astro configuration file.
- •`Yes` when prompted whether to make changes to`tsconfig.json` file.

To create conversation user interface easily, let’s move onto installing an AI SDK in your application.

In your terminal window, run the command below to install the necessary library for building the conversation user interface:

The above command installs the following:

- •`ai` library to build AI-powered streaming text and chat UIs.
- •`axios` library to make HTTP requests.

Inside `src` directory, create a `Chat.jsx` file with the following code:

`chat.jsx` does the following:

- •Imports the `useChat` hook by`ai` SDK to manage the conversation between user and the application. It takes care of saving the entire conversation (on the client-side) and using them as the request body when it calls the user defined`api` endpoint to fetch the response from chatbot.
- •Exports a React component that returns a form containing an `<input>` element to allow users to enter their query. It then loops over all the messages in the entire conversation, including the latest response to the user query.

Now, let’s create a component that will allow the user to supply some strings to the application to take into consideration before it answers any of the user query.

Inside `src` directory, create a `Update.jsx` file with the following code:

`Update.jsx` -

- •Imports `axios` library and`useState` hook by React.
- •Exports a React component that returns a form containing an `<textarea>` element to allow users to enter multiple strings, wherein each string is represented between comma(s).
- •Upon form submission, it POSTs the messages as JSON to the [`http://localhost:8000/update`](http://localhost:8000/update) endpoint.
- •To use the React components on the home page of your Astro application, make the following changes in `src/pages/index.astro` file:

1234567891011121314151617181920

The changes above being with importing both the Chat and Update React components. Then, it uses Astro's [`client:load` directive](https://docs.astro.build/en/reference/directives-reference/#clientload) to make sure that both the components are loaded and hydrated immediately on the page.

Run your Astro application by executing the following command in another terminal window:

The app should be running on [localhost:4321](http://localhost:4321/).

Congratulations, you created a Retrieval-Augmented Generation application using [SurrealDB](https://surrealdb.com) and [Fireworks](https://fireworks.ai/). With SurrealDB’s vector store, you are able to insert and update vector embeddings on the fly over WebSockets, and perform similarity search to user queries using vector embeddings generated internally for you.

Further, using Fireworks, you are able to invoke Llama 3.1 70B Chat model with system context and generate personalized responses to user queries.
