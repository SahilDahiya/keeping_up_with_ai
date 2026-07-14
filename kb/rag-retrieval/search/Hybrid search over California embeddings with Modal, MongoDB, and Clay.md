---
title: Hybrid search over California embeddings with Modal, MongoDB, and Clay
topic: rag-retrieval
subtopic: search
secondary_topics: []
summary: Example of hybrid search over embeddings, combining vector retrieval with
  MongoDB and a geospatial dataset.
source: modal
url: https://modal.com/blog/mongodb-search-california
author: null
published: '2024-09-24'
fetched: '2026-07-11T04:29:51Z'
classifier: codex
taxonomy_rev: 1
words: 709
content_sha256: d97e0353dbf66a98be7d777be0384930e20de455e5665db90e80da563bbbdce4
triage: keep
skip_reason: null
---

# Hybrid search over California embeddings with Modal, MongoDB, and Clay

[Back](https://modal.com/blog)

# Hybrid search over California embeddings with Modal, MongoDB, and Clay

[Charles Frye](https://twitter.com/charles_irl)

Data APIs, foundation models, serverless infrastructure from Modal, and the [MongoDB Atlas data platform](https://www.mongodb.com/atlas) make a potent
combination.

I used that stack for [my first RAG chatbot app](https://youtu.be/twHxmU9OxDU?list=PL1T8fO7ArWleyIqOy37OVXsP4hFXymdOZ) back in January of 2023. But the strength of this combination is deeper than
just the latest tech fads.

To demonstrate the general power of this stack, I put together a very
different kind of hybrid search app: search over the state of California based
on timestamps, geolocation data, and satellite image embeddings (using a
foundation model from [Clay](https://madewithclay.org/) and [Development Seed](https://developmentseed.org/)). Try it [here](https://modal-labs--clay-hybrid-search.modal.run/), or check out the code
and run it for yourself [here](https://github.com/modal-labs/search-california/tree/main).

![search-california user interface](https://modal-cdn.com/cdnbot/mongodb-search-california-ui.png)



## How does it work?

At a high level, here’s how signals from a satellite become results of a hybrid search query run by MongoDB and rendered in your browser, all orchestrated by Modal:

- Every few days, the European Space Agency’s [Sentinel satellites](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2)collect images of the entire Earth. The images are uploaded to cloud storage and[made available via an API](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a/).
- [Every day, we query that API for new images in a specific area-of-interest](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/extract.py#L58-L64)— here, the- [state of California](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/data/california.geojson). Areas-of-interest defined in GeoJSON format are- [available for free on the Internet](https://github.com/ropensci/geojsonio/tree/7e4cc683ed3d6eec38a8cae5ce03fa6d82acafc7/inst/examples). We- [cache them in MongoDB](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/database.py#L74-L78).
- The responses of that API, also formatted as JSON documents, are [uploaded to a MongoDB Atlas cluster](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/database.py#L63-L72).
- Asynchronously, that [database is queried](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/extract.py#L67-L76)to find entries that do not have an associated embedding.
- Any entries without embeddings are [communicated](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/extract.py#L80-L86)to a[serverless embedding service](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/embeddings.py)running the[Clay v1 foundation model for satellite imagery](https://clay-foundation.github.io/model/index.html). We run the model’s forward pass on hundreds of sub-regions at once on A10 GPUs and[merge them into a single embedding with a bit of custom PyTorch code](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/embeddings.py#L100-L123).
- These embeddings are [communicated back to the MongoDB Atlas cluster](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/backend/extract.py#L87-L100)for storage.
- A small [Alpine JS frontend client](https://github.com/modal-labs/search-california/blob/main/frontend/static/js/app.js)for querying this data in a UI is served via a[simple static FastAPI serve](https://github.com/modal-labs/search-california/blob/96a586fac3d6ba1b953366a7156cb2f1fa505f73/frontend/serve.py)r.
- That client sends hybrid search requests based on geo-location, image embedding, and timestamp to the MongoDB Atlas cluster.

This entire application — from API queries and data persistence to GPU inference
and hybrid search — is delivered using nothing but Modal and MongoDB Atlas.
Setting it up for yourself requires only credentials on these platforms and a
few commands. See the [full code](https://github.com/modal-labs/search-california/) for details.

## Why Modal and MongoDB Atlas?

This hybrid satellite image search application is intended as a novel demonstration of the emerging category of applications that rely on data APIs and foundation models to drive compelling new experiences.

For these applications, Modal and MongoDB Atlas make for a natural pair due to their shared strengths.

- **Versatility & Developer Experience**- Modal makes it easy to run heterogeneous Python workloads in the cloud. In our demo, we used it for everything from running small scheduled jobs to serving a database client to accelerating neural networks with GPUs. - MongoDB Atlas also makes it easy to run diverse cloud storage and search services supporting diverse applications. The JSON document model reduces impedance mismatch between data APIs and data storage and provides a unified interface. - Together, they enable iteration at the speed of thought.
- **Scalability**- Modal’s serverless infrastructure scales with your workloads, so you only pay for the resources you need — and you have them when you need them. Customers like - [Suno](https://suno.com/)serve- [applications at scale](https://modal.com/blog/suno-case-study)with Modal.- MongoDB Atlas is built for scale, with built-in data tiering, point-in-time recovery, and rich telemetry. And like the Sentinel satellites, Atlas is worldwide: global data distribution, multi-cloud reach, and multi-region replication. - Together, they ensure your compute and data infrastructure match your needs at any scale.
- **AI and ML Capabilities**- Modal provides on-demand access to - [powerful GPUs](https://modal.com/docs/guide/gpu), like NVIDIA H100s, that can run the latest foundation models. We back them up with easy-to-use but powerful cloud-native development primitives, like distributed dictionaries & queues and remote storage designed for large files.- MongoDB Atlas provides flexible search (text, geospatial, vector) that can both power and be powered by contemporary foundation models. Atlas ties these capabilities to operational data, ensuring freshness and reliability. - Together, they connect the most powerful hardware and intelligent models to your application and its data.
