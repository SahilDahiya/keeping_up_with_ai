---
title: GraphQL for the React Redux Developer
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/graphql-for-the-react-redux-developer
author: null
published: '2021-07-01'
fetched: '2026-08-20T06:11:33Z'
classifier: null
taxonomy_rev: 2
words: 1394
content_sha256: 3f221a0e5b56475f007db7ce3d2b73f45c56a9a362e3e2f16b7b4985e554f20f
---

# GraphQL for the React Redux Developer

## Overview

GraphQL is a popular API query language for clients to access data on servers. Cresta uses GraphQL in different ways to act as a bridge between our frontend and backend systems. This blog will discuss how a developer familiar with Redux can migrate over to GraphQL using the popular Apollo Client library to take advantage of GraphQL features.At Cresta, simplicity and speed are a couple of our core values for our development team. In a typical application with client and server components, client state management is typically different from server state management.  For example, it’s popular to use Redux for client state management and REST API for server state manipulation. However, if GraphQL is used for both purposes, we gain greater simplicity.This guide offers insights and tips for developers like yourself, who have an understanding of Redux using GraphQL and Apollo Client as a client state store. We’ll explore a use case by taking part in an existing redux [react chat client](https://github.com/cliffhall/react-chat-client) and partially converting its [message history component](https://github.com/cliffhall/react-chat-client/blob/master/src/components/MessageHistory/index.js) while using GraphQL and Apollo Client. Let’s dive in. 

## Why GraphQL?

Many libraries are available for state management and synchronizing data with the server, so why use GraphQL?On the one hand, there are Redux, MobX, and so on, which do an excellent job of client state management but leave the server synchronization as a completely separate task to be implemented by you (or by using a library such as [Redux-API](https://github.com/lexich/redux-api) to ease this implementation).On the other hand, there are tools like Firebase, Realm Sync, and PouchDB+CouchDB, which abstract and automate database synchronization so that you only need to deal with client data. However,  you also loses control of the data synchronization process. The abstraction makes it hard to control what data synchronizes first. It could skip synchronization of non-critical data altogether. Furthermore, this approach locks the application to a specific (and sometimes proprietary) database system.By using GraphQL, you get a more balanced solution between the two sets of tool types.  Because both the client and server speak the same language, synchronization becomes easier, yet you still maintain control.  For the client state, you may use a library like Apollo Client. A GraphQL server defines and exposes the Query API layer so that clients can access/save data with it. On the server-side, a variety of choices exist.* Additionally, it should be noted that GraphQL is an open standard, which prevents vendor lock-in and makes it easier to swap out parts of the system in the future as the application evolves.

## Intro to Apollo Client

As official documentation describes, Apollo Client is a complete state management library with GraphQL. Interestingly, one of its key features is zero-config caching, making it easy to use as a state store. Furthermore, Apollo Client already comes with support for React applications.

### Dispelling a Myth Regarding Apollo Client

Apollo Client is frequently used with a GraphQL backend, so some programmers believe the myth that it can ONLY be used with a GraphQL backend. The truth of the matter is - Apollo Client can absolutely be used as a client-only, in-browser store without any backend. Below is a basic code sample that initiates a client with only in-memory caching, without specifying any GraphQL backend to connect to:

![GraphQL](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7dff_68135f2bdf31c82ad396738d_GraphQL-1.avif)

More specifically, in the code example presented above, an in-memory cache is provided to the client to connect to, and the local state can be stored in this cache, according to this [Apollo Client Documentation](https://www.apollographql.com/docs/react/local-state/managing-state-with-field-policies/#storing-local-state-in-the-cache). It’s an easy assumption to make, but Apollo Client can be used either with GraphQL or as an in-browser store without any backend. 

## Chrome Extension Tool

To make debugging more manageable, the [Apollo Client Devtools](https://chrome.google.com/webstore/detail/apollo-client-devtools/jdkknkkbebbapilgoeccciglkfbmbnfm) may be installed in your Chrome browser to watch queries and client cache state as you debug the code.

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7e1b_68135f2bdf31c82ad39673ad_Blog_Chrome-Extension-Tool.avif)

Now that we’ve addressed a common myth and have the tools we need, let’s begin the use case example of replacing Redux store with Appollo Client.

## Replacing Redux Store with Apollo Client

### Example - Displaying State

Let’s look at one example of a react-redux component to show message history in a redux chat app. Note how react-redux passes state threads into the component as a react props value:

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7e05_68135f2bdf31c82ad3967396_GraphQL-2.avif)

In this example, the threads state contains a dictionary of arrays, with the recipient being the key. Each array contains elements with key (numeric sequence number), from (string identifying the sender) and text (string for the message text) for that recipient.Examine the screenshot below to see how the new code looks. This shows how you can convert this component using Apollo Graph QL (you can test it [here](https://codesandbox.io/s/nifty-dream-hy3ic)).

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7dfc_68135f2bdf31c82ad3967393_GraphQL-3.avif)

The above screenshot shows that by using the Apollo Client useQuery method, the client GraphQL cache can be queried, and the return values can be passed as props to the react UI component to render.This example is not super helpful, however it does render a static, hardwired state into the UI. To realize the full power of using Apollo Client cache as a store, let’s explore how to modify the stored values in the in-memory cache.

### Making Modifications to the Store

To make modifications to the store Redux, you can use Actions and Reducers. However, when Apollo Client cache is used as a store, the way to make modifications is slightly different:

- A query is specified: this limits the scope of data that is modified.
- You can invoke the readQuery method on the cache to read existing data from the query, with the returned result being similar to the state passed into a reducer.
- This data (similar to a reducer) can then be modified by creating a new object representing the new state and then written back into the cache by the writeQuery method.

## Example - Modifying State

The above example shows how to access the store, but what about modifying the store when new messages are received? In this Redux example, whenever a new message is received, the reducer code updates this threads Redux state by concatenating the new message to the array corresponding to the recipient. See below:

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7e02_68135f2bdf31c82ad3967390_GraphQL-4.avif)

The corresponding, converted code with Apollo Client is below, and you can test it [here](https://codesandbox.io/s/nifty-dream-hy3ic). 

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ec6a9681dea1a7df9_68135f2bdf31c82ad3967399_GraphQL-5.avif)

Note the following:

- The Apollo GraphQL client cache acts as an in-memory state store similar to the Redux store.
- To access its state, use `readQuery` on the cache first.
- The `writeQuery` call can do dispatching actions on the “store”

## Comparison - Pros and Cons

As shown in the comparison table below, the advantage of using Apollo Client is by simplification - that is, it’s the opportunity to unify usage of GraphQL for both client state store and interactions with backends.**Apollo ClientRedux***Pros:*

- Extend to GraphQL backends easily
- Use the same GraphQL query syntax for both client and server

*Pros:*

- react-redux integrates with react components via props
- Easy JS syntax to access store

*Cons:*

- No easy support or concept for middleware

*Cons:*

- Does not easily connect with GraphQL server

## Next Steps

This guide explains how to convert part of a simple, open-source Redux chat app from Redux to Apollo Client. However, you can apply the concepts explained to other Redux applications too.You can clone the sample converted chat app at this GitHub [link](https://github.com/jerryc8/graphql-client-demo). Feel free to clone, modify and experiment.Below are some next steps to take this to the next level:

- Choose a GraphQL backend out of the variety of choices available*
- Connect to a GraphQL backend: After you choose a GraphQL backend, pass the link parameter to the ApolloClient constructor. The same web application is now easily converted to establish a bridge to a GraphQL backend.
- Explore fragments: as opposed to queries, “fragments” define pieces of data that can be re-used in multiple places.
- In addition to the message history example, take the existing redux-based chat application and convert the whole application to use Apollo Client instead.
- Explore apollo-cache-persist to save the store into browser local storage.
- Explore Optimistic UI to get the best of both worlds - fast client cache for UI, and backend for synchronized storage.

Let us know your thoughts and whether you’d like to see more on this topic.*Examples of GraphQL backends:

- Hasura
- PostGraphile
- Apollo Server
- Prisma
- dgraph.io (SaaS)
- FaunaDB (SaaS)
