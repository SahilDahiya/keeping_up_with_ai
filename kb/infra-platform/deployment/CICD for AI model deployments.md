---
title: CI/CD for AI model deployments
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics: []
summary: Reference CI/CD pipeline for AI model deployments covering safe staging via
  development deployments, automated pre-production testing, gradual traffic cutover,
  and fast rollback, illustrated with Truss's `truss push` workflow.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/ci-cd-for-ai-model-deployments
author: Vlad Shulman
published: '2024-04-30'
fetched: '2026-11-12T06:12:16Z'
classifier: claude
taxonomy_rev: 2
words: 931
content_sha256: 30d8f61566dc015088e4f5f559c578544f8b4e2056197c6980845481c465179e
---

# CI/CD for AI model deployments

AI engineering
# CI/CD for AI model deployments

In this article, we outline a continuous integration and continuous deployment (CI/CD) pipeline for using AI models in production.


- Authors
- Date
- April 30, 2024

Continuous integration and continuous deployment (CI/CD) is an industry standard for everything from web to mobile to API development. But for AI models, deployment is often a manual process.

What would CI/CD look like for AI models? Broadly, AI models need a pipeline that looks like any other CI/CD setup:

1. A safe environment to deploy model updates without affecting production.
2. A way to test newly deployed models before promoting to production.
3. A way to seamlessly transition traffic from an old production deployment to a new one.
4. A way to revert to a previous production deployment if there are any issues.

At least the first three steps should be fully automated, and any reversions should be quick and seamless.

Below, we’ll walk through a reference architecture for CI/CD for AI models using Baseten’s model management and model inference APIs.

Baseten uses Truss, our open source model packaging framework, for model deployment. Every deployment starts with:

`truss push`
By default, this creates a development deployment of your model. The development deployment is a kind of staging environment for your model. A development deployment is similar to a production deployment of a model, but it has limited autoscaling capabilities and a live reload model server for faster development.

A model can have any number of active deployments, but one is specially designated as the development deployment. Creating a development deployment of a model does not affect production, just as pushing a web application to staging does not affect other environments.

Deploying a model can take several minutes. To check the status of your model as it deploys, use [the GET endpoint for a model’s development deployment](https://docs.baseten.co/api-reference/gets-a-models-development-deployment).

bash

```
curl --request GET \ 
--url https://api.baseten.co/v1/models/{model_id}/deployments/development \ 
--header "Authorization: Api-Key $BASETEN_API_KEY" \ 
```
Once the `status` in the response is `ACTIVE`, you have a development deployment of your model that is ready to run inference.

You can also use the `--wait` flag in `truss push` to wait until the model deployment has finished or failed to [receive a return code from the command](https://truss.baseten.co/reference/cli/push).

With your active development deployment, you can validate your new model. Generative AI models are generally non-deterministic, though this can be controlled in some cases such as temperature for LLMs and seed for image models. Still, testing model output is not as straightforward as testing a standard application. But there’s still useful information that you can gather, such as:

- Testing that the model accepts expected input types and produces expected output types.
- Testing any pre- and post-processing steps on the model server.
- Running benchmarks, perplexity checks, or other spot checks on output quality.
- Ensuring model response speeds fall within an expected range.

To test the model, use the [development deployment inference endpoint](https://docs.baseten.co/api-reference/development-predict):

```
curl -X POST https://model-{model_id}.api.baseten.co/development/predict \
  -H 'Authorization: Api-Key YOUR_API_KEY' \
  -d '{}' # JSON-serializable model input
```
This special endpoint calls the development deployment directly and does not affect production.

Once the development deployment has been validated, it’s time to [promote it to production](https://docs.baseten.co/deploy/lifecycle#promoting-to-production). You can do this from the model dashboard within the Baseten app, but for CI/CD of course we’ll use [the API endpoint](https://docs.baseten.co/api-reference/promotes-a-development-deployment-to-production).

```
curl --request POST \ 
--url https://api.baseten.co/v1/models/{model_id}/deployments/development/promote \ 
--header "Authorization: Api-Key $BASETEN_API_KEY" \ 
--data '{
  "scale_down_previous_production": true
}'
```
Once again, you can [monitor the deployment status](https://docs.baseten.co/api-reference/gets-a-models-production-deployment) for the production deployment. The previous production deployment will remain active until the promotion is complete; traffic will seamlessly move from the previous production deployment to the new one.

Failures happen in software development. What matters most is quick recovery.

When you promote a model deployment to production, the previous production deployment isn’t deleted. Instead, it’s optionally scaled to zero but sticks around as a published deployment with full autoscaling capabilities. If needed, you can restore that old production deployment by promoting it back to production.

While this is possible through the Baseten UI, you can also do this programmatically in your CI/CD script. By [polling the production deployment](https://docs.baseten.co/api-reference/gets-a-models-production-deployment), the script can determine if the `status` is ever `UNHEALTHY` or `FAILED`. Then, the script can [promote a previous deployment to production](https://docs.baseten.co/api-reference/promotes-a-deployment-to-production).

```
curl --request POST \ 
--url https://api.baseten.co/v1/models/{model_id}/deployments/{deployment_id}/promote \ 
--header "Authorization: Api-Key $BASETEN_API_KEY" \ 
--data '{
  "scale_down_previous_production": true
}'
```
This minimizes the interruption to your production service and gives you time to debug and re-deploy the failed deployment, which sticks around as a non-production published deployment for easy debugging access.

Completing these steps as a manual process is time consuming. Fortunately, you can create a script to automate this process into a true CI/CD pipeline.

In your script:

1. Create a development deployment.
2. Validate the deployment for speed and correctness.
3. Promote the deployment to production.
4. Fall back to a previous production deployment in case of errors.

The hardest part of building a CI/CD pipeline for an AI model is figuring out how to validate that the model is functioning properly when outputs are non-deterministic. To make this feasible, separate model evaluation from model deployment. Gain confidence in output quality through manual testing and comprehensive benchmarks before initiating a production deployment process. That way, your CI/CD pipeline is only responsible for checking that the model is fast and functional.

A strong CI/CD pipeline saves time and manual effort in the model deployment process. For help designing and implementing a CI/CD pipeline that works for your models, please reach out to [support@baseten.co](mailto:support@baseten.co).
