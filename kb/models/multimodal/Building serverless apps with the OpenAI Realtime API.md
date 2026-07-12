---
title: Building serverless apps with the OpenAI Realtime API
topic: models
subtopic: multimodal
secondary_topics:
- product-engineering/architecture
summary: Guide to building serverless apps with the OpenAI Realtime API, focusing
  on real-time voice interaction architecture and deployment patterns.
source: braintrust
url: https://www.braintrust.dev/blog/realtime-api
author: Braintrust Team
published: '2024-11-04'
fetched: '2026-07-11T04:33:29Z'
classifier: codex
taxonomy_rev: 1
words: 881
content_sha256: 1009223b34b39339a50030ca2072769629a9710d8f774ee9d2696755b9139913
---

# Building serverless apps with the OpenAI Realtime API

4 November 2024Ornella Altunyan, Kevin Chen6 min

In early October, OpenAI released the [Realtime API](https://platform.openai.com/docs/guides/realtime), designed for building advanced multimodal conversational experiences. This API enables rich AI applications with features like speech-to-speech interaction and simultaneous multimodal output. However, there are three key pain points that need to be solved before you can use the API to build secure and scalable production applications:

- User-facing credentials
- Logging
- Evaluations

At Braintrust, we want building AI applications with the most cutting-edge models to be a simple, wonderful developer experience. Today, we’re excited to announce support for the Realtime API via the Braintrust [AI proxy](https://www.braintrust.dev/docs/deploy/ai-proxy), and solutions to these specific pain points.

The OpenAI Realtime API is built on WebSockets to enable a responsive user experience. However, if you’re using a serverless backend like Vercel or AWS Lambda, which do not support WebSockets, it’s impossible to connect to the API without hosting a separate server somewhere else.

The API also currently lacks client-side authentication, making it insecure to connect to the API directly from the user’s browser.

The architecture requires developers to solve these problems by [setting up a separate, long-running Node.js relay server](https://github.com/openai/openai-realtime-console/blob/6ea4dba795fee868c60ea9e8e7eba7469974b3e9/README.md#using-a-relay-server). The relay server runs the provided [ relay.js](https://github.com/openai/openai-realtime-console/blob/main/relay-server/lib/relay.js) code and holds an OpenAI API key to handle Realtime API connections. Running a separate server complicates your architecture, but the only alternative—storing your API key in the frontend—isn’t secure for production.

Because all Realtime API calls need to pass through the relay, it also has to scale up quickly to handle your app’s traffic without impacting responsiveness. We believe that developers would rather focus on the features that make their app unique, rather than infrastructure scaling.

To address this operational complexity, we rearchitected a solution using our existing [AI proxy](https://www.braintrust.dev/docs/deploy/ai-proxy). This way, you won’t need to embed your OpenAI API key directly into your backend, and you can continue using whichever serverless platform you’re used to using for building AI applications.

The AI proxy securely manages your OpenAI API key, issuing [ temporary credentials](https://www.braintrust.dev/docs/deploy/ai-proxy#create-temporary-credentials) to your backend and frontend. The frontend sends any voice data from your app to the proxy, which handles secure communication with OpenAI’s Realtime API. This offloads the infrastructure burden to us, and allows you to focus on building your app.

Use this form to generate a Braintrust temporary credential. Use this credential in place of the OpenAI API key in your app to prevent exposing your API key to the client.

```
import { OpenAI } from "openai";
const client = new OpenAI({
  baseURL: "https://api.braintrust.dev/v1/proxy",
  apiKey: "YOUR_TEMPORARY_CREDENTIAL",
  // It is safe to store temporary credentials in the browser because they have
  // limited lifetime and access.
  dangerouslyAllowBrowser: true,
});
async function main() {
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [{ role: "user", content: "What is a proxy?" }],
  });
  console.log(response.choices[0].message.content);
}
main();
```
To access the Realtime API through the Braintrust proxy, change the proxy URL when instantiating the `RealtimeClient` to `https://braintrustproxy.com/v1/realtime`.

As an example, we [forked the sample app](https://github.com/braintrustdata/openai-realtime-console) from OpenAI and hooked it up to our proxy with just a [couple of lines of code](https://github.com/braintrustdata/openai-realtime-console/pull/1):

typescript

```
const LOCAL_RELAY_SERVER_URL =
  process.env.REACT_APP_LOCAL_RELAY_SERVER_URL ||
  "https://braintrustproxy.com/v1/realtime";
const apiKey = process.env.OPENAI_API_KEY;
const client = new RealtimeClient({
  url: LOCAL_RELAY_SERVER_URL || undefined,
  apiKey,
  dangerouslyAllowAPIKeyInBrowser: true,
});
```
Use the temporary credential you generated in place of the OpenAI API key in your app to prevent exposing your API key to the client. You can also use our proxy with an AI provider's API key, but you will not have access to other Braintrust features, like logging.

typescript

```
const PROXY_URL =
  process.env.BRAINTRUST_PROXY_URL || "https://braintrustproxy.com/v1";
// Braintrust API key starting with `sk-...`.
const BRAINTRUST_API_KEY = process.env.BRAINTRUST_API_KEY;
async function main() {
  const response = await fetch(`${PROXY_URL}/credentials`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${BRAINTRUST_API_KEY}`,
    },
    body: JSON.stringify({
      // Leave undefined to allow all models.
      model: "gpt-4o-realtime-preview-2024-10-01",
      // TTL for starting the request. Once started, the request can stream
      // for as long as needed.
      ttl_seconds: 60 * 10, // 10 minutes.
      logging: {
        project_name: "My project",
      },
    }),
    cache: "no-store",
  });
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Failed to request temporary credentials: ${error}`);
  }
  const { key: tempCredential } = await response.json();
  console.log(`Authorization: Bearer ${tempCredential}`);
}
main();
```
In addition to client-side authentication, you’ll also get the other benefits of building with Braintrust, like logging, built in. We support logging audio, as well as text, structured data, and images. When you connect to the Realtime API, a log will begin generating, and when your session is closed, the log will be ready to view. Each LLM and tool call will be contained in its own span inside of the trace. And most importantly, all multimodal content is now able to be uploaded and viewed as an [attachment](https://www.braintrust.dev/blog/attachments) in your trace. This means that you won’t have to exit the UI to double-click on an LLM call and view the input and output, no matter what type of format its in.

You can use this [open-source repo](https://github.com/braintrustdata/openai-realtime-console) as a starting point for any projects using the Realtime API. Because your app will automatically generate logs in Braintrust, you will have data in exactly the right format to run [evaluations](/docs/evaluate.

[Try building with the OpenAI Realtime API](https://www.braintrust.dev/docs/deploy/ai-proxy#use-realtime-models) today and [let us know](https://www.braintrust.dev/contact) what you create!
