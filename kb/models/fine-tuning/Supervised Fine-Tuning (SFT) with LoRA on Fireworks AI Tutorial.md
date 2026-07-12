---
title: 'Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI: Tutorial'
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Tutorial for supervised fine-tuning with LoRA, including setup, training,
  and deployment workflow.
source: fireworks
url: https://fireworks.ai/blog/supervised-fine-tuning-tutorial
author: null
published: '2025-05-12'
fetched: '2026-07-11T04:16:55Z'
classifier: codex
taxonomy_rev: 1
words: 905
content_sha256: 21ec4abc4848bd7c6313980c7ce98ea2c3f9e79d97be18fb84c68a7302822774
triage: keep
skip_reason: null
---

# Supervised Fine-Tuning (SFT) with LoRA on Fireworks AI: Tutorial

Supervised Fine-Tuning (SFT) is critical for adapting general-purpose Large Language Models (LLMs) to domain-specific tasks, significantly improving performance in real-world applications. Fireworks AI facilitates easy and scalable SFT through its intuitive APIs and support for Low-Rank Adaptation (LoRA), allowing efficient fine-tuning without full parameter updates.

LoRA significantly reduces the computational cost of fine-tuning large models by updating only a small subset of parameters in a low-rank structure, making it particularly suitable for large models like LLaMA or DeepSeek.

qLoRA (Quantized LoRA) further improves efficiency by enabling fine-tuning of 4-bit and 8-bit quantized models (dependent on model types) without sacrificing performance, reducing memory requirements even more.

Fireworks AI supports both LoRA and qLoRA tuning, allowing up to 100 LoRA adaptations to run simultaneously on a dedicated deployment without extra cost.

**Step-by-Step Guide to Fine-Tuning with Fireworks AI**

Go to fireworks.ai > Model Library > Filter “Tunable”

You can also filter for “Serverless” models if you are planning to run it serverless

This ensures that you are selecting models which allow LoRA-based tuning and deployments. These models support uploading LoRA adapters even if they were trained on another platform. You can also upload custom models that have the same architecture as the tunable ones in the list, and those models will also be tunable. For example, a deepseek distilled llama 8b model works just as well as a vanilla llama 8b model.

**Let’s say we select “ DeepSeek R1 Distill Llama 70b”**

**⚠️ Note:** Serverless LoRA is not currently supported (February 2026). Please check our [ Documentation Page](https://docs.fireworks.ai/fine-tuning/fine-tuning-models) for the latest updates on supported features and fine-tuning capabilities.

- **Prepare the dataset**

Datasets must adhere strictly to the JSONL format, where each line represents a complete JSON-formatted training example.

**Minimum Requirements:**

- •Minimum examples needed: 3
- •Maximum examples: Up to 3 million examples per dataset
- •File format: JSONL (each line is a valid JSON object)

**Message Schema:** Each training sample must include a messages array, where each message is an object with two fields:

- •role: one of system, user, or assistant
- •content: a string representing the message content

Here's an example conversation dataset (one training example, pretty printed for illustration, but in JSONL it should be flattened to one line):

1234567

Save this locally as **trader_poe_sample_data.jsonl**


b. Upload the dataset

Then you can upload the data set via the UI.

Go to Home> Datasets > Create Dataset

**(Optional)** You can also upload this dataset to Fireworks AI via firectl

To create a dataset, run:

1

and you can check the dataset with:

1

**Step a: Select the model you want to fine-tune**

- •Click on “Finetune this model”. Make sure the model is seen in the drop down list.
- •(This is another view for you to see all the models that are available to finetune)

**Step b: Upload the dataset (Training & Eval Datasets)**

You can upload your dataset from your local machine that you saved as a jsonl file, or if you created a Fireworks AI Dataset in Step 2, you can select that dataset from the dropdown.

💡Note: Explanations can be found in theour docs pageor you can run the command - firectl create sftj --help.

Once you run the fine-tuning job, you will see the job details on the “Fine-Tuning” page.

💡Note: The maximum number of tokens packed into each training batch. (default 32768)

Once the fine-tuning job is completed. You will see “Deploy the LoRA” option at the top right.

Select the LoRA model from the drop-down list.

Click “Continue”

Then select your deployment. You can either deploy the LoRA model “serverless” or via an “on-demand deployment”.


Deployment Options:

- **Serverless :**LoRA add-ons deployed serverless are charged per token (at base model rates) and available continuously without cold starts. See list of models supported for serverless LoRA deployment
- **On-demand:**LoRA add-ons deployed to on-demand deployments utilize the same pricing, hardware and scaling behavior as its underlying deployment. Please note that your See list of models supported for on-demand LoRA deployment

💡 PS: Use an existing on-demand deployment to load the LoRA model onto (instead of serverless)

PS: As we are fine-tuning the [DeepSeek R1](https://fireworks.ai/blog/deepseek-r1-deepdive) Distill Llama 70B, we will need to deploy the LoRA on -demand, rather than serverless. Use an existing on-demand deployment to load the LoRA model onto (instead of serverless)

Enter the model display name and click “Submit”

- •Validate your dataset thoroughly before uploading.
- •Use a higher loraRank for larger model capacity, e.g., 32 for complex tasks.
- •Monitor job health and logs for errors.
- •earlyStop: False is good for quick experimentation, but use True for early stop that will end your training early if there is no significant progression on loss.
- •Use descriptive names for dataset IDs and models for clarity.

- •**Minimum examples for effective SFT**: 3
- •**Maximum examples**: 3,000,000 per dataset
- •**Required file format**: JSONL
- •**Message roles**: system, user, assistant
- •**Upload process**: Must first create a dataset record via API, then upload JSONL
- •**Supported models for LoRA**: Use Model Library to filter and see the model list
- •**qLoRA is automatically applied to 70B parameter models for optimal performance**
- •**Fine-tuning config**: latest example uses 1 epoch, lr=1e-4, loraRank=8

By following these steps, you can effectively adapt LLMs to your specific use case using Fireworks AI’s fine-tuning pipeline with LoRA. This approach ensures lower costs, faster training, and scalable deployment for real-world applications.
