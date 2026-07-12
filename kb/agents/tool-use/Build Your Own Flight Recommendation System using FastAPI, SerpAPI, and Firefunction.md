---
title: Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction
topic: agents
subtopic: tool-use
secondary_topics:
- prompt-engineering/structured-output
summary: Tutorial for building a function-calling application with FastAPI, SerpAPI,
  and structured tool invocation.
source: fireworks
url: https://fireworks.ai/blog/function-call-vercel-fastapi-serp
author: null
published: '2024-08-29'
fetched: '2026-07-11T04:16:43Z'
classifier: codex
taxonomy_rev: 1
words: 1754
content_sha256: ca780f2adb76e2e497e64de0be5f27727171e4858fe251666aa40d06d8121304
triage: keep
skip_reason: null
---

# Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction

- Prerequisites
- Tech Stack
- High-Level Data Flow and Operations
- Steps
- Generate the
- Generate the SerpApi API Key
- Create a new FastAPI application
- Install Dependencies
- Define Data Models using Pydantic
- Initialize FastAPI App
- Integration with Firefunction V2
- Create a Chat API endpoint
- Use SerpApi to generate recommendations from Google Flights in real-time
- Run FastAPI App Locally
- Create a new Next.js application
- Install AI SDK
- Build Conversation User Interface
- Run Next.js Application Locally
- Conclusion

Imagine you're planning a last-minute getaway. You've got a few days off, but you're not sure where to go, or how to get there. Instead of spending hours scouring the internet for travel options, wouldn't it be great if you could simply type in your preferences and instantly receive tailored suggestions?

That's exactly what we'll be creating in this guide: a personalized recommendation system for flights using [Fireworks](https://fireworks.ai/), [SerpApi](https://serpapi.com/), [FastAPI](https://fastapi.tiangolo.com/), and [Next.js](https://nextjs.org).

In this tutorial, we're going to create a **Flight Recommendation System** utilizing Firefunction-v2 to streamline the extraction of Departure and Arrival Airport Code (IATA Code) and the date or time of travel recommendations, as well as flight details, from dynamically received user inputs.

You'll need the following:

- •[Node.js 18](https://nodejs.org/en/blog/announcements/v18-release-announce)or later
- •A [Fireworks](https://fireworks.ai/api-keys)account
- •A [SerpApi](https://serpapi.com)account

Following technologies are used in creating our RAG application:

| Technology | Type | Description |
|---|---|---|
| FastAPI | Framework | A high performance framework to build APIs with Python 3.8+. |
| Next.js | Framework | The React Framework for the Web. |
| TailwindCSS | Framework | CSS framework for building custom designs. |
| Fireworks | Platform | Blazing fast LLM Inference platform. |
| SerpApi | Platform | A real-time API to access Google search results. |

This is a high-level diagram of how data is flowing and operations that take place 👇🏻

When a user types in a query like “Flights from San Francisco to Dulles”, a tool call is generated as per the registered function spec in Firefunction v2. Further, they are used to query `SerpApi` for real-time results. The response is then returned to the user.

- •

- •

- •

- •

HTTP requests to the Fireworks API require an API Key. To generate this API key, log in to your Fireworks account and navigate to [API Keys](https://fireworks.ai/api-keys). Enter a name for your API key and click the **Create Key** button to generate a new API key. Copy and securely store this token for later use as `FIREWORKS_API_KEY` environment variable.

Locally, set and export the `FIREWORKS_API_KEY` environment variable by executing the following command:

12

HTTP requests to the SerpApi require an authorization token. To generate this token, while logged into your SerpApi account, navigate to the [dashboard](https://serpapi.com/dashboard), scroll down to **Your Private API Key** section, and click the **Clipboard** icon. Copy and securely store this token for later use as `SERPAPI_API_KEY` environment variable.

Locally, set and export the `SERPAPI_API_KEY` environment variable by executing the following command:

12

First, let's start by creating a new project. You can create a new directory by executing the following command in your terminal window:

1234

Next, you can install the required dependencies by executing the following command in your terminal window:

12345

The above command installs the required libraries to run ASGI Server, FastAPI, OpenAI, Fireworks AI, and SerpAPI in your Python project.

Next, create a file `main.py` with the following code:

123456789101112131415161718

The above code imports the following:

- •`os`module to use the environment variables you’ve set earlier.
- •`List`to denote a list of elements of specific type.
- •`json`to parse string model outputs as JSON.
- •`datetime`module to get today’s date.
- •`openai`module to conveniently call OpenAI API.
- •`serpapi`module to scrape and parse search results from Google Search.
- •`BaseModel`class to define models of the request body FastAPI endpoints.
- •`CORSMiddleware`FastAPI middleware to enable Cross Origin Resource Sharing of FastAPI endpoints.

To create the data types of request body in your FastAPI endpoints, append the following code in [main.py](http://main.py) file:

123456789

The above code defines two [Pydantic](https://docs.pydantic.dev/latest/) models:

- •**Message**: a model that will store each message containing two fields,`role`and`content`.
- •**Messages**: a model that will store the input as a list of`Message`model.

To initialize a FastAPI application, append the following code in [main.py](http://main.py) file:

123456789101112

The code above creates a FastAPI instance and uses the `CORSMiddleware` middleware to enable Cross Origin requests. This allows your frontend to successfully POST to the GenAI application endpoints to fetch responses to the user query, regardless of the port it is running on.

Firefunction-v2 is a function calling LLM that can help you with build agentic use cases like chat assistants that involve function calling capabilities, alongside general chat capabilities.

In the code below, we're defining a set of tools utilizing Firefunction-v2 to streamline the extraction of Departure and Arrival Airport Code (IATA Code) and the date or time of travel recommendations, as well as flight details, from dynamically received user inputs. This approach not only improves the user experience by automating the workflow but also demonstrates the practical application of Firefunction-v2 in real-world scenarios.

In each function, you’ll define a structure like below:

- •`name`: A personalized name for your function.
- •`description`: Few characters to illustrate the use case of the function.
- •`parameters`: The values the function is supposed to extract from the user prompt.- •`properties`: A structured object containing the name, description and type of the values with instructions that need to be extracted. Make sure to have a detailed description that allows AI to produce accurate results to your intended use case.
- •`required`: The name of the values that are necessary to be generated from this tool, if invoked by AI.

- •

12345678910111213141516171819202122232425262728293031323334353637

The code above does the following:

- •Creates a date in YYYY-MM-DD format using the `datetime`module.
- •`flight_generator`: A function that outputs (if found), four arguments pertaining to the departure and arrival of the flights based on the[IATA](https://www.iata.org/en/publications/directories/code-search)codes of the airports by which the user could fly between the timings as gathered from their prompt.

To generate personalized responses by using Fireworks Firefunction-v2, you’ll create an `/chat` endpoint in your FastAPI application. Append the following code in [main.py](http://main.py) file:

1234567891011121314151617181920

The above code does the following:

- •Accepts a list of `messages`that could be specified natural language format “Flights from San Francisco to New York this Sunday”.
- •Defines a system prompt to let the assistant be able to call the fireworks functions you’ve defined earlier using tools array. Prepends a `Message`model, representing role of the system and it’s content as the system prompt created.
- •Uses Fireworks Chat Completion API to invoke Firefunction-v2 to generate params for booking flights.
- •Serializes the output obtained from the chat completion API to a JSON and extracts the arguments obtained, containing the value of flight details.

SerpApi helps you access real-time data from many internet sources namely YouTube or Google Flights, facilitating dynamic content generation and flight searches.

To retrieve relevant results from Google Flights, you need to set the SerpApi engine to `google_flights` and pass the date and airport codes of arrival and departure, the currency and the language SerpApi should return results in. SerpApi then returns details of relevant flights matching the user's query, enabling personalized flight recommendations.

12345678910111213141516171819202122232425

The code above does the following:

- •Creates a params dict with `api_key`parameter to SerpApi key obtained earlier.
- •Checks if the arguments obtained earlier had `arrival_date`in it. It updates the`params`dict to contain the expected arrival and departure date and related airport codes. It also sets the currency and language SerpApi should respond real time flight details with.

Once you’ve obtained the response, you’re going to selectively create an array of flights that contain JSON objects representing details of each recommendation by SerpApi and return it as the response.

1234567891011121314151617181920

The code above does the following:

- •It creates a `flights`array to be returned as response. Each item in the`flights`array represents the price and airline logo of the flight, with it’s arrival and departure dates and airport names.

With all that done, here’s how our [ main.py](http://main.py) will finally look like containing both the endpoints:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129

Run your FastAPI application by executing the following command in another terminal window:

12

The app should be running on [localhost:8000](http://localhost:8000/). Let’s keep it running while we create an user interface to invoke the chat endpoint to create responses to user queries.

Let’s get started by creating a new Next.js project. Open your terminal and run the following command:

12

When prompted, choose:

- •`Yes`when prompted to use TypeScript.
- •`No`when prompted to use ESLint.
- •`Yes`when prompted to use Tailwind CSS.
- •`No`when prompted to use`src/`directory.
- •`Yes`when prompted to use App Router.
- •`No`when prompted to customize the default import alias (`@/*`).

Once that is done, move into the project directory and start the app in development mode by executing the following command:

123

The app should be running on [localhost:3000](http://localhost:3000/).

In your terminal window, run the command below to install the necessary library for building the conversation user interface:

12

The above command installs the following:

- •`ai`library to build AI-powered streaming text and chat UIs.

Inside the `app` directory, replace the code inside `page.tsx` file with the following code:

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384

The code above does the following:

- •Imports the `useChat`hook by`ai`SDK to manage the conversation between user and the application. It takes care of saving the entire conversation (on the client-side) and using them as the request body when it calls the user defined`api`endpoint to fetch the response from chatbot.
- •Exports a React component that returns a form containing an `<input>`element to allow users to enter their query. It then loops over all the messages in the entire conversation, including the latest response to the user query.
- •Finally, loops over the list of flights and creates their preview using flight’s arrival and departure details, the airline it’s for and it’s cost.

Run your Next.js application by executing the following command in another terminal window:

12

The app should be running on [localhost:3000](http://localhost:3000/).

In this tutorial, you learned how to create a real-time recommendation system using SerpApi and Fireworks AI. With Fireworks `Firefunction-v2`, you’re able to identify exactly the set parameters from a dynamically received user prompt, and defining a set of pre-knowledge to help the AI predict the user needs even better.

Now, just imagine the convenience of planning your next adventure, thanks to the intelligence of AI.
