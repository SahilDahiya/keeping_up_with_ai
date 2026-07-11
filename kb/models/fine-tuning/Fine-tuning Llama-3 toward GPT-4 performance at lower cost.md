---
title: Fine-tuning Llama-3 toward GPT-4 performance at lower cost
topic: models
subtopic: fine-tuning
secondary_topics:
- models/benchmarks
summary: Shows fine-tuning Llama 3 toward GPT-4-like task performance at lower cost.
source: together
url: https://www.together.ai/blog/finetuning
author: Hassan El Mghari
published: '2024-07-12'
fetched: '2026-07-11T04:23:24Z'
classifier: codex
taxonomy_rev: 1
words: 1696
content_sha256: b1d311d82d7cab3d2a4edc30a5f053114a1b5a7851599607a9e0103292941e43
triage: keep
skip_reason: null
---

# Fine-tuning Llama-3 toward GPT-4 performance at lower cost

The success of Llama-3 has been incredible, proving that open source models are rapidly catching up to closed models without compromising private ownership. Our customers have been using their own proprietary data to fine-tune small OSS models like Llama-3 to run their tasks with greater accuracy than even the top closed-source models are capable of. Their fine-tuned model is small, accurate, and fully owned and controlled by them.

Discover how to leverage Together AI's platform to fine-tune Llama-3-8b on your proprietary data, creating a custom model that outperforms leading OSS alternatives like Llama-3-70b and is comparable to leading closed-source alternatives like GPT-4 at a fraction of the cost. This step-by-step guide demonstrates how a fine-tuned Llama-3 8B model went from 47% accuracy on the base model to 65% accuracy, even surpassing Llama-3-70B (64%) and coming close to GPT-4o (71%). Learn how you can create faster, more accurate, and fully owned AI solutions for your specific use cases, all while reducing costs by an order of magnitude compared to using GPT-4.

*The full repo is available here if you want to run all the code yourself:* [https://github.com/togethercomputer/finetuning](https://github.com/togethercomputer/finetuning)

## Dataset Transformation

The first thing we'll do is download the Math Instruct dataset. Navigate to [MathIntruct on HuggingFace](https://huggingface.co/datasets/TIGER-Lab/MathInstruct/tree/main) and click download next to ** MathInstruct.json**. After we do this, we'll run a quick cleanup script to

[remove duplicates](https://github.com/togethercomputer/finetuning/blob/main/utils/remove-duplicates.py), remove 1,000 problems to save them for evals, and rename the final file to

**. If you want to follow along, feel free to**

*MathInstruct-207k.json*[clone the GitHub repo](https://github.com/togethercomputer/finetuning)and use the

**file to fine-tune a smaller dataset.**

*TrainMathInstruct-500.json*Next, we need to transform this dataset into a `.jsonl` file, since that's the file format Together supports. We can use some Python code and the Llama-3 instruct format to do this:

```
import json
dataset = "MathInstruct-207k"
old_file_path = f"{dataset}.json"
new_file_path = f"Formatted{dataset}.jsonl"
# Load old format JSON data
with open(old_file_path, "r", encoding="utf-8") as old_file:
    old_data = json.load(old_file)
# Define Llama-3 prompt and system prompt
llama_format = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
{model_answer}<|eot_id|>
"""
formatted_data = []
system_prompt = "You're a helpful assistant that answers math problems."
# Transform the data into the correct format and write it to a JSONL file
with open(new_file_path, "w", encoding="utf-8") as new_file:
    for piece in old_data:
        temp_data = {
            "text": llama_format.format(
                system_prompt=system_prompt,
                user_question=piece["instruction"],
                model_answer=piece["output"],
            )
        }
        new_file.write(json.dumps(temp_data))
        new_file.write("\n")
```
``We can then use ** check_file** function from Together's SDK to verify that our dataset is valid and in the correct format:

```
from together.utils import check_file
report = check_file(new_file_path)
print(report)
assert report["is_check_passed"] == True
```
``If the assertion passes, you're ready to upload your dataset to Together AI!

## Uploading & checking your dataset

Now that we have a valid dataset, we'll upload it to Together AI via the Python SDK. Make sure to ** pip install together**, save your API key as an environment variable called

**, then run the following code to upload it and verify that it was uploaded successfully.**

*TOGETHER_API_KEY**You can also upload a dataset **through our CLI**.*

```
import os
from together import Together
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
dataset = "MathInstruct-207k"
# Upload your formatted data and get back the file ID
response = client.files.upload(file=f"Formatted{dataset}.jsonl")
fileId = response.model_dump()["id"]
# Verify that the file was uploaded successfully
file_metadata = client.files.retrieve(fileId)
print(file_metadata)
```
## Starting a Fine-tuning job

We're now ready to fine-tune a model using our uploaded dataset! We'll create a fine-tuning job using Llama-3-8B as our base model, specify our dataset as the ** training_file**, use 5 epochs, and optionally add a

[Weights and Biases](https://wandb.ai/site)API key if we want to monitor the fine-tuning job with graphs such as a loss curve.

```
import os
from together import Together
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
dataset = "MathInstruct-207k"
# Trigger fine-tuning job
resp = client.fine_tuning.create(
    suffix="mathinstruct-207k-v2",
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    training_file=fileId,
    n_epochs=5,
    batch_size=8,
    learning_rate=1e-5,
    wandb_api_key=os.environ.get("WANDB_API_KEY"),
)
```
``After you run this code, your fine-tuning job will be kicked off. You'll be able to view it on your [Together AI jobs dashboard](https://api.together.xyz/jobs).

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a18b7db6b74c1c11317ffc_699e0b050e253022dcd5c0da_66915c19baa83fd2619e9b16_jobs.png)

### Running your fine-tuned model

When your fine-tuning job has finished (this dataset takes ~2-14 hours depending on the number of epochs), you'll be able to view and launch it from your dashboard on Together AI.

Navigate to the Models page, click on your fine-tuned model, and click Deploy to create an endpoint with one of the hardware configurations below. For this tutorial, we'll deploy on 1 A100-80GB. (If you don't mind lower latency, you can also deploy on cheaper hardware like L40s or RTX-6000s.)

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a18b7db6b74c1c11317ff9_699e0b050e253022dcd5c0df_66915d2247eb0a6bcd377429_runningmodel.png)

After your endpoint spins up, you can test it in the Together AI playground by clicking the green Play button, or you can call directly from your code using our API. We'll be calling it through our API in the following section to fully evaluate it.

## Running evaluations to see results

Now that we have our fine-tuned model, we want to see if it performs better than the base model (and other models out there). We'll be using an LLM to judge the results (also known as LLM-as-a-judge) since it's straightforward, but there are more sophisticated and deterministic ways you can also use to evaluate your model.

To do this, we'll take 1000 math problems that the LLM has never seen before and run them through both the base Llama-3-8B and our fine-tuned Llama-3-8B, and evaluate the accuracy of each. We'll also run them through LLama-3-70B and GPT-4o to see the accuracy from the top OSS and proprietary models to put it in perspective.

To start, let's define our eval dataset. We'll grab 1000 problems from the dataset that were not used in the initial training and save them to a file called ** EvalDataset-1000.json**. We can then iterate through each problem and have our base and fine-tuned model both answer it, then store results in

**.**

*results.json**Note: All this code, including the dataset and eval dataset, are available **on GitHub here**.*

```
import json
from together import AsyncTogether
import os
import asyncio
async_together_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
base_model = "meta-llama/Llama-3-8b-chat-hf"
top_oss_model = "meta-llama/Llama-3-70b-chat-hf"
finetuned_model = "FINETUNED_MODEL_ID"
evaluator_model = "meta-llama/Llama-3-70b-chat-hf"
eval_dataset = "EvalDataset-1000.json"
async def chatCompletion(model, instruction):
    completion = await async_together_client.chat.completions.create(
        messages=[
            {"role": "user", "content": instruction},
        ],
        model=model,
        max_tokens=1500,
    )
    return completion.choices[0].message.content
async def main():
    # Get all responses for the eval dataset & save them to results.json
    with open(eval_dataset, "r", encoding="utf-8") as eval_file:
        eval_data = json.load(eval_file)
    results = []
    for example in eval_data:
        (
            baseModelCompletion,
            topOSSModelCompletion,
            finetunedModelCompletion,
        ) = await asyncio.gather(
            chatCompletion(base_model, example["instruction"]),
            chatCompletion(top_oss_model, example["instruction"]),
            chatCompletion(finetuned_model, example["instruction"]),
        )
        results.append(
            {
                "groundTruthAnswer": example["output"],
                "baseModelAnswer": baseModelCompletion,
                "topOSSModelAnswer": topOSSModelCompletion,
                "fineTunedModelAnswer": finetunedModelCompletion,
            }
        )
    with open("results.json", "w", encoding="utf-8") as results_file:
        json.dump(results, results_file, indent=4)
```
``Now that we have the results from the 1000 problems from our base and fine-tuned models, we can send them to an evaluator model (in this case, we'll use Llama-3-70B) to grade them on accuracy and output a final score:

```
baseModelCount = 0
topOSSModelCount = 0
fineTunedModelCount = 0
badResponses = 0
numErrors = 0
async def evalCompletion(groundTruthAnswer, modelAnswer):
    isAccurate = await async_together_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You will be given a ground truth answer and a model answer. Please output ACCURATE if the model answer matches the ground truth answer or INACCURATE otherwise. Please only return ACCURATE or INACCURATE. It is very important for my job that you do this.",
            },
            {
                "role": "user",
                "content": f"""{groundTruthAnswer}
                               {modelAnswer}""",
            },
        ],
        model=evaluator_model,
    )
    if isAccurate.choices[0].message.content == "ACCURATE":
        return 1, 0
    elif isAccurate.choices[0].message.content == "INACCURATE":
        return 0, 0
    else:
        return 0, 1  # Return 1 for badResponses
for result in results:
    try:
        (baseModelCount_inc, topOSSModelCount_inc, fineTunedModelCount_inc) = await asyncio.gather(
            evalCompletion(result["groundTruthAnswer"], result["baseModelAnswer"]),
            evalCompletion(result["groundTruthAnswer"], result["topOSSModelAnswer"]),
            evalCompletion(result["groundTruthAnswer"], result["fineTunedModelAnswer"]))
        baseModelCount += baseModelCount_inc[0]
        topOSSModelCount += topOSSModelCount_inc[0]
        fineTunedModelCount += fineTunedModelCount_inc[0]
        badResponses += (baseModelCount_inc[1] + topOSSModelCount_inc[1] + fineTunedModelCount_inc[1])
    except Exception as e:
        numErrors += 1
print("Base model (Llama-3-8b): ", f"{baseModelCount / len(results) * 100}%")
print("Top OSS model (Llama-3-70b): ",f"{topOSSModelCount / len(results) * 100}%")
print("Fine-tuned model: ", f"{fineTunedModelCount / len(results) * 100}%")
```
## Results

``We evaluated a dataset of 1000 math problems on the base model, our fine-tuned model, and top large models such as Llama-3-70B and GPT-4o. Here are the results for accuracy:

| Model | Accuracy (%) |
|---|---|
| Base model (Llama-3-8B) | 47.2% |
| Fine-tuned model (Llama-3-8B) | 65.2% |
| Top OSS model (Llama-3-70B) | 64.2% |
| Top proprietary model (GPT-4o) | 71.4% |


Our small 8B fine-tuned model **outperformed the base model by nearly 20%,** beat out top OSS model LLama-3-70B, and achieved over 90% of GPT-4o's accuracy. It also leads all evaluated models in accuracy and gets 91% of GPT-4o's accuracy while being much faster, 50x cheaper than GPT-4o, and giving the end user full ownership of the model and weights (you can download and run the model yourself).

Not only is our fine-tuned model more accurate, its responses are more succinct and organized, translating to lower costs and faster response times when running tasks.

Let's look at a quick example next.

### Comparing responses from the base and fine-tuned models

For the following question (where C is the correct answer), notice the difference in the base model and fine-tuned model responses.

**Question:** A sum of money is to be distributed among A, B, C, D in the proportion of 5 : 2 : 4 : 3. If C gets Rs. 1000 more than D, what is B's share?

Answer Choices: (A) 1000 (B) 3000 (C) 2000 (D) 4000 (E) 5000

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/69a18b7eb6b74c1c11318000_699e0b050e253022dcd5c0d4_66915d2ecbaeaf9bb91dfc30_finalanswer.png)

The base model got the answer wrong and took 311 tokens, while the fine-tuned model answered correctly using only 100 tokens.

### Conclusion

Our walkthrough shows that fine-tuning small open-source models like Llama-3-8B can result in a custom model that is smaller, faster, cheaper, and more accurate for performing specific tasks. Even more, we didn't have to compromise flexibility or ownership, meaning we can use our own proprietary data to fine-tune a model, and then either use Together to host it, or download and run it ourselves.

The Llama-3-8B model that we trained on math problems in this blog post outperformed leading OSS models and got close to GPT-4o performance, while only costing <$100 total to fine-tune on Together AI. To learn more, check out our guides on [Fine-tuning on Together AI](https://docs.together.ai/docs/fine-tuning-cli), or get in touch to ask us any questions!
