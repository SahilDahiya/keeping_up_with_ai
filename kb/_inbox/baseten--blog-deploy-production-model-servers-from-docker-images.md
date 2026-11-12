---
title: 'Introducing Custom Servers: Deploy production-ready model servers from Docker
  images'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/deploy-production-model-servers-from-docker-images
author: Tianshu Cheng
published: '2024-12-05'
fetched: '2026-11-12T06:09:24Z'
classifier: null
taxonomy_rev: 2
words: 857
content_sha256: f17352509325bcc87cfb58f63e349808e832bc80da7bf8db3069fd985ae04875
---

# Introducing Custom Servers: Deploy production-ready model servers from Docker images

News
# Introducing Custom Servers: Deploy production-ready model servers from Docker images

Deploy production-ready model servers on Baseten directly from any Docker image using just a YAML file.


- Authors
- Date
- December 5, 2024

TLDR

Custom Servers on Baseten allow you to deploy a model server directly from any Docker image using just a YAML file. With full support for Baseten's suite of infrastructure optimizations, you can easily convert any pre-existing Dockerized model server into an elastic autoscaling service. Whereas Truss Server is ideal for Python-based serving without writing server code, Custom Servers are best for pre-configured images (like vLLM) or proprietary Docker images.

We developed [Truss](https://github.com/basetenlabs/truss), an open-source model packaging library, to simplify the process of deploying AI models in production. Truss lets developers deploy powerful model servers for any AI model in pure Python code, leveraging technologies like Docker and Kubernetes while abstracting away their complexity.

While Truss solves key pain points for AI builders, sometimes developers want to deploy model servers directly from Docker images instead. Frameworks like vLLM publish ready-to-use images, and adding additional abstractions on top can feel inelegant. Many of our larger customers also have their own tried-and-true images they want to run with minimal overhead, while still benefitting from Baseten’s optimized autoscaling, on-demand GPU availability, and blazing-fast performance.

Now, developers can easily launch custom model servers on Baseten directly from a YAML config file. Custom Servers are completely configuration-based: push a single command without writing any Python code, and you launch a production-ready server with all of the performance benefits inherent to Baseten’s ML infra.

Check out the demo by [Tianshu Cheng](https://www.linkedin.com/in/tianshu-c), the lead engineer behind Custom Servers, as he deploys a production-ready vLLM model server in minutes!

Custom Servers on Baseten offer:

- **A codeless developer experience.** One YAML file is all you need to deploy a model server from any Docker image.
- **Full integration with the Baseten ecosystem.** You can leverage all of our industry-leading tools and optimizations, so Custom Servers are production-ready from day one.
- **Support for production-critical features.** For example, you can add customized readiness and liveness probes to your servers.

Custom Servers are a new feature introduced in [Truss](https://github.com/basetenlabs/truss) 0.9.40 that enable you to run your model server directly from a Docker image, without relying on Truss Server as an intermediary layer. This addresses situations where using Truss as an internal server is unnecessary, such as deploying vLLM or Triton servers which are already packaged with their own serving logic.

Custom Servers let you:

- **Deploy any Docker image**: Bring any ready-to-use Docker image, whether it’s for an open-source model server like vLLM or a proprietary image built in-house.
- **Skip the Truss Server layer**: Run your model server directly, simplifying the deployment process for pre-packaged models.
- **Include custom readiness and liveness probes**: [Specify custom endpoints](https://docs.baseten.co/truss/guides/custom-server#specifying-a-docker-image-in-config-yaml) for health checks to ensure the precise health monitoring you need.

Custom Servers inherit Baseten’s elastic autoscaling, differing from Truss servers mainly when it comes to the deployment experience and best use cases:

| Feature | Truss Server | Custom Server | 
|---|---|---|
| Model serving DevEx | Python-based model serving with Truss abstraction | Full control over Docker image and serving logic | 
| Need to write model server code? | Required | Not required (assumed to be in the Docker Image) | 
| Best use case | Writing model server code easily, live testing, and rapid iteration | Ready-to-use model servers, highly customized deployments | 

Deploying a Custom Server on Baseten is straightforward: you only need a single configuration file (`config.yaml`).

For instance, you can use the following YAML file to deploy a vLLM model server on Baseten:

yaml

```
base_image:
  image: vllm/vllm-openai:latest
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --port 8000 --max-model-len 1024"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/chat/completions
  server_port: 8000
resources:
  accelerator: A10G
model_name: vllm-model-server
secrets:
  hf_access_token: null
runtime:
  predict_concurrency: 128
```
The Docker image is specified under `base_image`, and the command to start the server is defined in `start_command`. The `readiness_endpoint` and `liveness_endpoint` are both set to `/health`, allowing Kubernetes to determine when the server is ready or unhealthy.

Check out [our documentation](https://docs.baseten.co/truss/guides/custom-server) to get started with more examples.

Custom Servers are a great choice for:

- **Quick-starting popular model servers:** Deploy open-source servers like the [vLLM OpenAI compatible server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html) or [Infinity embedding model server](https://github.com/michaelfeil/infinity) directly from a Docker image, without having to modify or write additional server code. This helps you focus on building use case logic, especially in the early stages of development.
- **Customized model servers:** For advanced developers who are already using highly customized model servers developed in-house.

We’re not just building the world’s most performant ML infra—we’re coupling it with the best developer experience.

Custom Servers are powerful tools inspired by direct feedback from our customers. Whether you're starting with a popular open-source model server or looking to deploy your fully customized in-house image, you now have even more flexibility in how you deploy model servers on Baseten—with or without Truss.

[Follow our guide](https://docs.baseten.co/truss/guides/custom-server#installing-custom-python-packages) to launch your first Custom Server, or [talk to one of our engineers](mailto:team@baseten.co) to hit aggressive performance targets!
