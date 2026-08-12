---
title: Fireworks launches fine-tuning service - Rapidly iterate on quality and scale
  to production through Fireworks inference
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: fireworks
url: https://fireworks.ai/blog/fine-tune-launch
author: null
published: '2024-03-08'
fetched: '2026-08-12T06:28:19Z'
classifier: null
taxonomy_rev: 2
words: 959
content_sha256: 9bef63ca36f6499b5a0396581ed974d71480b9c98f0a33eb42b771d1c562cb54
---

# Fireworks launches fine-tuning service - Rapidly iterate on quality and scale to production through Fireworks inference

- •**Fine-tuning service launch** Fireworks is offering an affordable LoRA fine-tuning service for 10 models, including Mixtral. The service costs $2 per 1M training examples for Mixtral and similarly competitive rates for other models
- •**Tune and iterate rapidly -** Our ultra-fast tuning and model deployment process lets you go from dataset to querying a fine-tuned model in minutes. Quickly switch between and compare models. Fireworks lets you keep 100 models and immediately ready for usage, with no extra cost.
- •**Seamless, cost-free integration into blazing-fast inference** - Your fine-tuned models are served serverless on the Fireworks inference platform with**no additional costs** and with fast speeds like our base models

Fireworks is excited to announce our fine-tuning service to better enable customized models to be used with our blazing fast inference service! Fine-tuning is a crucial part of improving model accuracy on individual use cases. In the past year, we’ve seen huge usage of our “[model deployment](https://readme.fireworks.ai/docs/model-upload)” service that allows users to upload models to Fireworks that were fine-tuned on other services. As part of Fireworks’ commitment to [building the best production platform](https://fireworks.ai/blog/spring-update-faster-models-dedicated-deployments-postpaid-pricing), we’re excited to offer fine-tuning directly on the Fireworks platform. Our service is focused on rapidly iterating on and seamlessly deploying fine-tuned models.

Fine-tuning is the process of providing many examples to an LLM to improve model performance. Specifically, Fireworks’ fine-tuning process uses a technique called LoRA that enables improved performance without requiring large amounts of data or reductions in model speed. Fine-tuning is helpful with a variety of tasks, especially those that require customization for specific formats or domains, like generating SQL code or responding with a specific tone.

Fine-tuning can offer huge increases in model accuracy and provide a “moat” for your app through differentiated quality. However, the process of fine-tuning can be painful, due to:

- •**Iteration Time** - Existing platforms require hours to fine-tune a model, additional time to deploy the model and still more time to boot up GPUs for serving
- •**Fine-tuning Cost** A single fine-tuning job can cost dozens of dollars between the fine-tuning process and GPU loading. This lengthy and costly fine-tuning process may need to be repeated dozens of times when iterating
- •**Slow and Expensive Model Serving -** Even after you’ve created the perfect model, existing platforms charge 2x the cost to serve fine-tuned models or require models to be served on slower or more expensive dedicated GPU capacity

Fine-tuning on Fireworks offers

- •**Seamless, cost-free integration into blazing fast inference platform** Fireworks hosts fine-tuned models using the same set-up as our “serverless” base models, so fine-tuned models are fast, with speeds up to 300 tokens/sec. (Note that fine-tuned model speeds are slightly slower than base model speeds due to technical constraints). We also don’t charge additional cost to use a fine-tuned model. You’ll pay $0.50 / 1M tokens for inference on fine-tuned Mixtral, exactly like you would for base Mixtral. Therefore,**running inference on fine-tuned models on Fireworks should offer inference speeds several times that of competitors, at half the cost or lower** (especially our[fastest models](https://fireworks.ai/blog/spring-update-faster-models-dedicated-deployments-postpaid-pricing) of Mixtral and[Llama 70b chat](https://fireworks.ai/models/fireworks/llama-v2-70b-chat) )
- •**Immediate iteration and experimentation** Fireworks tuned models can be deployed in a ~minute and used instantly without waiting for GPUs to be booted up. Fireworks lets you deploy up to 100 fine-tuned models, so you can quickly compare models and swap them into live services. There’s no cost to deploying fine-tuned models, you’ll only pay for traffic used.

- •**Competitive cost to tune** - Unlike other platforms, we don’t charge additional service fees for fine-tuning. We charge only per token of training data, as shown below (dataset size * number of epochs), with a minimum charge of $3. Both our rates for training and for minimum charges are lower than competitors. Competing platforms charge $4 / 1M training tokens for Mixtral and large models and $1/1M training tokens for smaller models

|  | $ / 1M tokens in training | 
|---|---|
| Models up to 16B parameters | $0.50 | 
| Models 16.1B - 80B | $3.00 | 
| Mixtral | $2.00 | 

Tuning a model is easy on Fireworks through our “Firectl” command line interface (see [docs](https://readme.fireworks.ai/docs/fine-tuning-models)). Let’s say that you wanted to tune Mixtral-8x-7b-instruct to have a specific tone/accuracy for instruction following by using the [databricks/databricks-dolly-15k](http://databricks/databricks-dolly-15k) dataset. First, you just prepare a dataset in a JSONL file - we even provide code (see [documentation](https://readme.fireworks.ai/docs/fine-tuning-models)) to convert any dataset to a JSONL file. The data would appear like so:

1234

Next, you provide fine-tuning settings to specify which model to use, how the model should format/interpret the training data and hyperparameter settings. We enable 2 hyperparameters to be changed - epochs and learning rate. You can also connect your fine-tuning job to Weights and Biases to view progress visually in their interface.

12345678910111213

Afterwards, you simply provide your data and your settings in the Firectl to start a fine-tuning job and will be provided with a model to deploy and use seamlessly with the Fireworks inference service.

Fine-tuning is a powerful tool that enables you to quickly provide improved accuracy to your users. Fireworks makes it faster and easier to tune and serve models. Get started today with our fine-tuning docs ([link](https://readme.fireworks.ai/docs/fine-tuning-models)). Tune, deploy and compare fine-tuned models within minutes with Fireworks’ near-instantaneous deployment of fine-tuned models. When you’ve found a model you like, serve it fast and cost-effectively at scale through the Fireworks inference engine.

We’ll be investing further in our tuning service in the coming months, with planned features like special fine-tuning options for conversational formats and function calling. We’d love to hear your feedback! Please join the #fine-tuning channel of our [Discord](https://discord.gg/mMqQxvFD9A) to chat directly with the team or other fine-tuning users. We’re excited to see what you build!
