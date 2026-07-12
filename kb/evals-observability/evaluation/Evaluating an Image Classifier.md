---
title: Evaluating an Image Classifier
topic: evals-observability
subtopic: evaluation
secondary_topics:
- models/multimodal
summary: Tutorial on evaluating an image classifier with Phoenix, using multimodal
  experiment and tracing workflows.
source: arize
url: https://arize.com/blog/evaluate-image-classifier/
author: John Gilhuly
published: '2024-08-30'
fetched: '2026-07-11T04:49:48Z'
classifier: codex
taxonomy_rev: 1
words: 641
content_sha256: 9f28f057dc421a13a94c4b27c49cf7aef4e172a32bd017ec9ea976ffc68a1776
---

# Evaluating an Image Classifier

Phoenix supports multi-modal evaluation and tracing. In this tutorial, we’ll take advantage of that to walk through the process of setting up an image classification experiment using Phoenix. This involves uploading a dataset, creating an experiment to classify the images, and evaluating the model’s accuracy. We’ll be using OpenAI’s GPT-4o-mini model for the classification task.

This guide assumes you have an OpenAI API key ready to go.

- View the [full notebook here](https://github.com/Arize-ai/phoenix/blob/main/tutorials/multi_modal/image_classification_tutorial.ipynb)
- Loving Phoenix? Consider giving us a [star on Github](https://github.com/Arize-ai/phoenix). It really helps us keep the lights on! ⭐️

## Setting Up Your Environment

To get started, you’ll need to install the necessary dependencies:

```
```
`pip install -q "arize-phoenix>=4.29.0" openinference-instrumentation-openai openai datasets`

			## Connecting to Phoenix

Next, we’ll connect to Phoenix. There are many different ways to host Phoenix, from accessing a cloud instance to self-hosting. The snippet below will connect to a cloud instance of Phoenix if you have `PHOENIX_API_KEY` set in your environment variables. Otherwise, it will launch a local instance.

```
```
```
import os
if "PHOENIX_API_KEY" in os.environ:
    os.environ["PHOENIX_CLIENT_HEADERS"] = f"api_key={os.environ['PHOENIX_API_KEY']}"
    os.environ["PHOENIX_COLLECTOR_ENDPOINT"] = "https://app.phoenix.arize.com"
else:
    import phoenix as px
    px.launch_app()
from phoenix.otel import register
tracer_provider = register()
```

			## Loading the Dataset

We’ll be using a sample image classification dataset from Hugging Face. After loading the dataset, we’ll convert the image data to base64 encoded strings, which Phoenix and OpenAI can handle automatically.

```
```
```
import phoenix as px
from datasets import load_dataset
df = load_dataset("huggingface/image-classification-test-sample")["train"].to_pandas()
import base64
df['img'] = df['img'].apply(lambda x: x['bytes'])
df['img'] = df['img'].apply(lambda x: base64.b64encode(x).decode('utf-8'))
df['img'] = df['img'].apply(lambda x: 'data:image/png;base64,' + x)
```

			We’ll also map the numerical labels to more meaningful class names:

```
```
```
label_map = {1: 'automobile', 2: 'snakes', 3: 'cat', 4: 'tree', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship'}
df['label'] = df['label'].map(label_map)
```

			## Verifying the Dataset

Before proceeding, let’s take a quick look at the first image in the dataset to ensure everything is in order:

```
```
```
from IPython.display import display, Image
image_data = df.loc[0, 'img'].split(',')[1]
image_bytes = base64.b64decode(image_data)
display(Image(data=image_bytes))
```

			## Uploading the Dataset to Phoenix

Now that our dataset is ready, we can upload it to Phoenix. This dataset will be used as the test cases for our experiment.

```
```
```
import datetime
test_cases = px.Client().upload_dataset(
    dataset_name=f"image-classification-test-sample-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}",
    dataframe=df,
    input_keys=["img"],
    output_keys=["label"],
)
```

			## Defining the Experiment Task

We’ll use OpenAI’s GPT-4o-mini model for the classification task. To do this, we first instrument the model to ensure we capture all the necessary traces in Phoenix.

```
```
```
from openinference.instrumentation.openai import OpenAIInstrumentor
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider, skip_dep_check=True)
```

			Next, we define our task, which takes an image and classifies it:

```
```
```
from openai import OpenAI
def task(input):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image? Your answer should be a single word. The word should be one of the following: " + str(label_map.values())},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": input['img'],
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    output_label = response.choices[0].message.content.lower()
    return output_label
```

			## Setting Up Evaluators

For this experiment, our evaluators will be very simple, since we already have ground truth labels in our original dataset to compare to. We simply need to check if the model’s output matches the expected label.

```
```
```
def matches_expected_label(expected, output):
    return expected["label"] == output
```

			## Running the Experiment

With everything set up, we can now run the experiment. This function processes each image in the dataset, classifies it, and evaluates the results:

```
```
```
from phoenix.experiments import run_experiment
import nest_asyncio
nest_asyncio.apply()
run_experiment(
    task=task,
    evaluators=[matches_expected_label],
    dataset=test_cases,
    experiment_description="Image classification experiment",
    experiment_metadata={"model": "gpt-4o"},
)
```

			![Experiment Results in Phoenix](https://arize.com/wp-content/uploads/2024/08/Screenshot-2024-08-29-at-2.24.16 PM.png)

From here, you can modify your task or classification code as much as you’d like, and re-run the experiment to see how your new code compares to this baseline.
