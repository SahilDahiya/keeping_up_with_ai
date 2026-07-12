---
title: Evaluating Model Performance Across Clouds
topic: models
subtopic: benchmarks
secondary_topics:
- inference/serving
- infra-platform/cost
summary: Evaluates model performance across cloud providers, focusing on latency,
  cost, quality, and provider-selection tradeoffs for production inference.
source: langfuse
url: https://langfuse.com/blog/2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse
author: null
published: '2025-08-13'
fetched: '2026-07-11T04:35:33Z'
classifier: codex
taxonomy_rev: 1
words: 1094
content_sha256: 854a12107e632e959aceeb109fe341eae86cb6f4b81056b1254b4061081359a2
---

# Evaluating Model Performance Across Clouds

# Evaluating Model Performance Across Clouds

This guide shows you how to use an automated benchmarking script in Shadeform that will help you measure self-hosted model performance across clouds.

![Picture Jannik Maierhöfer](https://langfuse.com/_next/image?url=%2Fimages%2Fpeople%2Fjannikmaierhoefer.jpg&w=96&q=75) Jannik Maierhöfer

Jannik MaierhöferWhile many AI startups have built their applications around closed source model APIs, a growing number are turning to self-hosted open source or custom models—especially in sectors that handle sensitive data like healthcare and legal.

Self-hosted models allow companies to retain full control over their data and fully customize the model to their application, making it an attractive choice for both privacy and competitive edge.

[How to Self-Host a Model](https://langfuse.com#how-to-self-host-a-model)

When self-hosting, companies can either deploy the model in their own datacenter (if they have the capital), or (more commonly) deploy the model in the cloud.

However, if you deploy in the cloud, how do you go about choosing which cloud is best for your deployment?

Many will opt for a hyperscaler like AWS, GCP, or Azure, but will suffer higher prices.

For companies who are capital sensitive, running in one of the 50+ new dedicated AI clouds like Lambda Labs, Nebius, Crusoe, or others is an alternative.

[Evaluating Clouds for Self-Hosting](https://langfuse.com#evaluating-clouds-for-self-hosting)

When evaluating these new clouds, outside of pricing, we care most about how our model is going to perform for the end user once deployed—latency, throughput, etc.

There are many factors that contribute, from GPU specs to storage and networking configurations. However, it’s almost impossible to gauge model performance by looking at a cloud’s stat sheet.

The only reliable way to determine how your deployment will perform is to test it yourself. Luckily, we’ve put something together to make that process much simpler.

[Shadeform x Langfuse: Automated Cross-Cloud Benchmarking](https://langfuse.com#shadeform-x-langfuse-automated-cross-cloud-benchmarking)

Shadeform teamed up with Langfuse to put together an [automated benchmarking script](https://platform.shadeform.ai/templates/cd968d1e-a2c0-405b-b4f7-04025131f14b) that will help you easily measure self-hosted model performance across clouds.

With [Shadeform](https://www.shadeform.ai/)’s multi-cloud GPU marketplace and launch template feature, we can easily pre-load and deploy the script across multiple cloud environments to evaluate them.

Here’s how the script works:

- Creates a local deployment of Langfuse inside the GPU instance.
- Starts a vLLM server––the current gold standard inference engine––with a specified Hugging Face model.
- Feeds a series of prompts to the model.
- Langfuse traces each chat completion and records latency, tokens, and tokens/second.

Once the script completes, you’ll be able to view the results from the Langfuse UI.

[Getting Started](https://langfuse.com#getting-started)

[Create a Shadeform account and go to the template](https://langfuse.com#create-a-shadeform-account-and-go-to-the-template)

If you don’t have one already, create a Shadeform account [here](https://platform.shadeform.ai/).

Once you have an account and can access the platform, you can find the benchmarking template [here](https://platform.shadeform.ai/templates/cd968d1e-a2c0-405b-b4f7-04025131f14b).

[Save the benchmarking template as a copy to customize it](https://langfuse.com#save-the-benchmarking-template-as-a-copy-to-customize-it)

Before we begin, we’ll want to save the template as a copy.

To do this, click “Save as a Copy” in the top right corner.

![1](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F12.png&w=3840&q=75)


Your copy of the template can be found in the “Templates” tab on the navigation bar under “My Resources”.

[Customize your template](https://langfuse.com#customize-your-template)

To customize your template, click on your copy of the template, and then click “Edit” in the top right corner.

![2](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F11.png&w=3840&q=75)


Scroll down to the section titled “Environment Variables”.

Start by replacing the HUGGINGFACE_ACCESS_TOKEN value with your own.

Next, replace the MODEL_ID value with the id of the Hugging Face model you want to evaluate, e.g. deepseek-ai/DeepSeek-R1.

![3](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F07.png&w=3840&q=75)


(Optional) If you want to customize the batch of prompts used to benchmark the model, scroll down to the “Startup Script” section.

Find the section of the script titled — BENCHMARKING SCRIPT SETUP —. Here, you’ll find a list of prompts that you can customize to your needs.

![4](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F10.png&w=3840&q=75)


When you finish configuring the script, click “Update Template” at the bottom.

[Select a GPU instance from the cloud you want to evaluate](https://langfuse.com#select-a-gpu-instance-from-the-cloud-you-want-to-evaluate)

Click “Compute Marketplace” on the navigation bar, scroll down, and filter the results by “Cloud”.

![5](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F08.png&w=3840&q=75)


Next, find a GPU instance you want to test on (e.g. 8x H200) and click “Launch”.

![6](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F09.png&w=3840&q=75)


[Deploy the template and wait for the script to complete](https://langfuse.com#deploy-the-template-and-wait-for-the-script-to-complete)

Find the field titled “Template” towards the top of the launch page and select your copy of the benchmarking template.

![7](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F06.png&w=3840&q=75)


Once your configurations populate, click “Deploy”.

The script should take around 15-30 minutes to complete depending on the model and GPU(s) used. You can check the script’s status by clicking on the “Running Instances” tab on the navigation bar, clicking on the instance, and clicking “Logs”.

You should see the following message once everything has finished: “Benchmarking complete, view the results at: <instance-ip>:3000”

![8](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F05.png&w=3840&q=75)


[Access the Langfuse UI to see the benchmark results](https://langfuse.com#access-the-langfuse-ui-to-see-the-benchmark-results)

Once the script has completed, go to <instance-ip>:3000 to view the results.

When you get to the Langfuse UI, you’ll be met with an authentication screen.

A user is provisioned by default so you don’t have to create a new user.

Username: [ops@shadeform.ai](mailto:ops@shadeform.ai)

Password: 12345678

Alternatively, any user created will automatically bind to the default organization with the pre-configured benchmarking project.

Once you've authenticated in the Langfuse UI, click "Go to project" under the project titled "Benchmark Run 1".

Next, click "Tracing > Traces" on the left-hand navigation bar.

Here, you will see a table with each trace labeled "Prompt n" based on the order of the list of prompts.

The table will show you the latency (time it took to generate), the total tokens used, as well as the tokens per second.

![12](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F03.png&w=3840&q=75)


Clicking on a trace will show the details of each response.

![13](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F02.png&w=3840&q=75)


[(Optional): Run additional tests](https://langfuse.com#optional-run-additional-tests)

If you want to run additional benchmarks in the same session, you’ll need to SSH into the instance.

To SSH, click on the instance in the “Running Instances” tab.

Scrolling down, you’ll find a “Get Private Key” button.

Click this button and follow the instructions on screen.

![14](https://langfuse.com/_next/image?url=%2Fimages%2Fblog%2F2025-08-13-evaluating-model-performance-accross-clouds-with-shadeform-and-langfuse%2F01.png&w=3840&q=75)


Once you have successfully SSH’d into the instance, you can copy the python benchmarking script from the template into a new .py file and edit as needed before running.

[Repeat steps 5 & 6 for the next cloud](https://langfuse.com#repeat-steps-5--6-for-the-next-cloud)

Because you saved the template as a copy in step 2, it’s ready to be deployed on any other cloud instance for evaluation.

Simply repeat steps 5 & 6 for the next cloud you want to evaluate.

[Summary](https://langfuse.com#summary)

Self-hosted models offer significant advantages over closed source API solutions, especially for companies handling sensitive data. But, choosing the right cloud to deploy your model in can be both time and resource intensive. This automated benchmarking script simplifies performance evaluation across cloud environments, enabling companies to confidently select the optimal deployment solution based on real-world metrics.
