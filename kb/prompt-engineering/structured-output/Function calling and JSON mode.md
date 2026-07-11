---
title: Function calling and JSON mode
topic: prompt-engineering
subtopic: structured-output
secondary_topics:
- agents/tool-use
summary: Explains function calling and JSON mode for structured LLM application outputs.
source: together
url: https://www.together.ai/blog/function-calling-json-mode
author: Together AI
published: '2024-01-31'
fetched: '2026-07-11T04:23:40Z'
classifier: codex
taxonomy_rev: 1
words: 1877
content_sha256: 692729a205621a848384efa09883357ca20e58f15cc80f4e967ec1edd1a67107
triage: keep
skip_reason: null
---

# Function calling and JSON mode

We are excited to introduce JSON mode & function calling on Together Inference! They are designed to provide you with more flexibility and control over your interactions with LLMs. We currently support these features in [Mixtral](https://api.together.xyz/playground/chat/mistralai/Mixtral-8x7B-Instruct-v0.1), [Mistral](https://api.together.xyz/playground/chat/mistralai/Mistral-7B-Instruct-v0.1), and [CodeLlama](https://api.together.xyz/playground/chat/codellama/CodeLlama-13b-Instruct-hf) with more coming soon. In this post, we'll introduce and walk you through how to use JSON mode and function calling through the Together API!

## Introduction to JSON mode and function calling

While both JSON mode and function calling can enhance your interaction with LLMs, it's important to understand that they are not interchangeable — they serve different purposes and offer unique benefits. Specifically:

**JSON mode** allows you to specify a JSON schema that will be used by the LLM to output data in this format. This means you can dictate the format and data types of the response, leading to a more structured and predictable output that can suit your specific needs.

**Function calling** enables LLMs to intelligently output a JSON object containing arguments for external functions that are defined. This is particularly useful when there is a need for real-time data access, such as weather updates, product information, or stock market data, or when you want the LLM to be aware of certain functions you've defined. It also makes it possible for the LLM to intelligently determine what information to gather from a user if it determines a function should be called. Our endpoint ensures that these function calls align with the prescribed function schema, incorporating necessary arguments with the appropriate data types.

## JSON Mode

With JSON mode, you can specify a schema for the output of the LLM. While the OpenAI API does not inherently allow for the specification of a JSON schema, we augmented the `response_format` argument with `schema`. When a schema is passed in, we enforce the model to generate the output aligned with the given schema.

Here's an example of how you can use JSON mode with Mixtral:

### Example:

```

```
```
import os
import json
import openai
from pydantic import BaseModel, Field
# Create client
client = openai.OpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = os.environ['TOGETHER_API_KEY'],
)
# Define the schema for the output.
class User(BaseModel):
    name: str = Field(description="user name")
    address: str = Field(description="address")

# Generate
chat_completion = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    response_format={
        "type": "json_object",
        "schema": User.model_json_schema()
    },
    messages=[
        {"role": "system", "content": "You are a helpful assistant that answers in JSON."},
        {"role": "user", "content": "Create a user named Alice, who lives in 42, Wonderland Avenue."}
    ],
)
created_user = json.loads(chat_completion.choices[0].message.content)
print(json.dumps(created_user, indent=2))

```
In this example, we define a schema for a `User` object that contains their name and address. The LLM then generates a response that matches this schema, providing a structured JSON object that we can use directly in our application in a deterministic way.

The expected output of this example is:

```
{
  "address": "42, Wonderland Avenue",
  "name": "Alice"
}
```
### More Examples:

**Array and Optional argument:**

We also support optional arguments. This example is based on the one above, but with an optional argument called `explanation`.

```
from typing import Optional
client = openai.OpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = os.environ['TOGETHER_API_KEY'],
)
class Result(BaseModel):
    ordered_numbers: List[int]
    explanation: Optional['str']
chat_completion = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    response_format={
        "type": "json_object",
        "schema": Result.model_json_schema()
    },
    messages=[
		{"role": "system", "content": "You are a helpful assistant that answers in JSON."},
        {"role": "user", "content": "Please output this list in order of DESC [1, 4, 2, 8]."}
    ]
)
response = json.loads(chat_completion.choices[0].message.content)
print(json.dumps(response, indent=2))
'''
{
  "ordered_numbers": [
    8,
    4,
    2,
    1
  ],
  "explanation": "The function 'desc' sorts the input list in descending order."
}
'''
```
``**Nested data types:**

This example demonstrates handling nested data types in JSON responses. Two Pydantic models are defined: `Address` with fields `street`, `city`, `country`, and `zip`, and `User` with fields `name`, `is_active`, and `address` (which uses the `Address` model). The model generates a JSON response that creates a user with the given details, following the defined schema.

```
import os
import json
import openai
from pydantic import BaseModel, Field
# Create client
client = openai.OpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = os.environ['TOGETHER_API_KEY'],
)
# Define the schema for the output.
class Address(BaseModel):
    street: str
    city: str
    country: str
    zip: str
class User(BaseModel):
    name: str = Field(description="user name")
    is_active: bool = Field(default=True)
    address: Address

# Generate
chat_completion = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    response_format={
        "type": "json_object",
        "schema": User.model_json_schema()
    },
    messages=[
        {"role": "system", "content": "You are a helpful assistant that answers in JSON."},
        {"role": "user", "content": "Create a user named Alice, who lives in 42, Wonderland Avenue, Wonderland city, 91234 Dreamland."}
    ],
)
created_user = json.loads(chat_completion.choices[0].message.content)
print(json.dumps(created_user, indent=2))
'''
{
  "name": "Alice",
  "address": {
    "street": "Wonderland Avenue",
    "city": "Wonderland",
    "country": "Dreamland",
    "zip": "91234"
  },
  "is_active": true
}
'''
```
``For more detailed information, check out our [documentation on JSON mode](https://docs.together.ai/docs/json-mode).

## Function Calling

With function calling, it will output a JSON object containing arguments for external functions that are defined. After the functions are defined, the LLM will intelligently determine if a function needs to be invoked and if it does, it will suggest the appropriate one with the correct parameters in a JSON object. After that, you can execute the API call within your application and relay the response back to the LLM to continue working.

Let's illustrate this process with a simple example: creating a chatbot that has access to weather data. The function is defined in `tools`:

### Example:

```
import os
import json
import openai
# Create client
client = openai.OpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = os.environ['TOGETHER_API_KEY'],
)
# Define function(s)
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
          }
        }
      }
    }
  }
]

# Generate
response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
		    {"role": "user", "content": "What is the current temperature of New York?"}
		],
    tools=tools,
    tool_choice="auto",
)
print(json.dumps(response.choices[0].message.dict()['tool_calls'], indent=2))
```
In this example, we define an external function that gets the current weather in a given location. We then use this function in our chat completion request. The AI model generates a response that includes calls to this function, providing real-time weather data for the requested locations. The expected output is:

```
[
  {
    "id": "...",
    "function": {
      "arguments": "{\"location\":\"New York\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    },
    "type": "function"
  }
]
```
``If `tool_choice="auto"`, the model might choose not to invoke any function calls. To always use a function, you can simply specify `tool_choice= {"type": "function", "function": {"name": "<function_name>"}}`. Moreover, you can prevent the model from calling functions by specifying `tool_choice="none"`.

### More Examples

**Parallel function calling**:

This example demonstrates how to call a function in parallel for multiple inputs. The user request is to get the current temperature of New York, San Francisco, and Chicago. The model generates a response that calls the `get_current_weather` function for each of these locations in parallel, returning an array of function call objects.

```
# Define function(s)
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
          }
        }
      }
    }
  }
]

# Generate
response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
		    {"role": "user", "content": "What is the current temperature of New York, San Francisco and Chicago?"}
		],
    tools=tools,
    tool_choice="auto",
)
print(json.dumps(response.choices[0].message.dict()['tool_calls'], indent=2))
'''
[
  {
    "id": "...",
    "function": {
      "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    },
    "type": "function"
  },
  {
    "id": "...",
    "function": {
      "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    },
    "type": "function"
  },
  {
    "id": "...",
    "function": {
      "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    },
    "type": "function"
  }
]
'''
```
**No function calling:**

This example shows how the model behaves when the user request does not require a function call. The same function `get_current_weather` is defined as a tool, but the user request is to find the location of Zurich, which does not require the function. The model generates a response that informs the user it cannot provide geographical information and only retrieves the current weather in a given location.

```
# Define function(s)
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
          }
        }
      }
    }
  }
]

# Generate
response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
		    {"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": "Where is Zurich?"}
		],
    tools=tools,
    tool_choice="auto",
)
print(response.choices[0].message.dict()['content'])
'''
I'm sorry, but I don't have the capability to provide geographical information. My current function allows me to retrieve the current weather in a given location. If you need help with that, feel free to ask!
'''
```
**Multi-turn example:**

This example shows how to use a function call in a multi-turn conversation to enrich the dialogue with function responses and generate a response based on the updated conversation history.

```
# Example function to make available to model
def get_current_weather(location, unit="fahrenheit"):
    """Get the weather for some location"""
    if "chicago" in location.lower():
        return json.dumps({"location": "Chicago", "temperature": "13", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "55", "unit": unit})
    elif "new york" in location.lower():
        return json.dumps({"location": "New York", "temperature": "11", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
          }
        }
      }
    }
  }
]
messages = [
    {"role": "system", "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."},
    {"role": "user", "content": "What is the current temperature of New York, San Francisco and Chicago?"}
]

response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        if function_name == "get_current_weather":
            function_response = get_current_weather(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
    function_enriched_response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=messages,
    )
    print(function_enriched_response.choices[0].message.model_dump()['content'])
'''
The current temperature in New York is 11 degrees Fahrenheit, in San Francisco it is 55 degrees Fahrenheit, and in Chicago it is 13 degrees Fahrenheit.
'''
```
``For more detailed information, check out our [documentation on function calling](https://docs.together.ai/docs/function-calling).

## Conclusion

We believe that JSON mode and function calling are a significant step forward, bringing a new level of versatility and functionality to AI applications. By enabling a more structured interaction with the model and allowing for specific types of outputs and behaviors, we're confident that it will be a valuable tool for developers.

We can't wait to see what you build on Together AI! For more info, check out our [function calling](https://docs.together.ai/docs/function-calling) and [JSON mode](https://docs.together.ai/docs/json-mode) docs.
