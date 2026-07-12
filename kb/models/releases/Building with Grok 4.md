---
title: Building with Grok 4
topic: models
subtopic: releases
secondary_topics:
- models/reasoning
summary: Notes on building with Grok 4, including model behavior, practical integration
  considerations, and evaluation needs for new model adoption.
source: braintrust
url: https://www.braintrust.dev/blog/grok-4
author: Braintrust Team
published: '2025-07-11'
fetched: '2026-07-11T04:32:39Z'
classifier: codex
taxonomy_rev: 1
words: 1734
content_sha256: 68f6fd718fd363c511434c1e7d41e748cdfb88d78e05d844bc7da93f6ff6a518
---

# Building with Grok 4

11 July 2025Wayde Gilliam9 min

xAI recently released their latest family of Grok models: Grok 4 and the premium Grok 4 Heavy. If you missed it, you can catch a replay of the [livestream](https://x.com/xai/status/1943158495588815072).
According to the xAI team, these reasoning-only models (you can't turn it off) provide substantial improvements over Grok 3, primarily because they were trained to use tools rather than just generalize on their own.

While presenting the latest model as a means to further "maximizing truth seeing", Musk boldly claimed that these new models are "smarter than almost all graduate students in all disciplines simultaneously" and "better than PhD students" when it comes to academic questions.

But the real question is, "Can it create a good 'pelican riding a bicycle' SVG?"

[Simon Willison](https://x.com/simonw) has a rather [unique test](https://www.youtube.com/watch?v=YpY83-kA7Bo) that he runs on new models, where he asks the model to create an image of a pelican riding a bicycle, followed by a request to describe the image it created.
Quirky tests like these can help us understand the proclivities of various LLMs. You can read Simon's full writeup on his experience with Grok 4 on his [blog](https://simonwillison.net/2025/Jul/10/grok-4/).

With Braintrust, you can evaluate tests like this in a systematic way. In this post, we'll share how you might set up tasks and scorers to
understand how well each model does on these kind of tasks, starting with Grok 4. To make things interesting, we'll define a custom 'LLM-as-Jury' scorer that combines *several* LLM-as-a-judge scorers from OpenAI, Anthropic, and xAI.

For the purposes of this demo, we'll keep things simple and not worry about [aligning the scorers to human judgments](https://www.braintrust.dev/docs/best-practices/scorers#develop-and-align-llm-based-scorers).

The first thing you need to do is create a Braintrust [project](https://www.braintrust.dev/docs/admin/projects).

Next, we'll import some libraries and set up our OpenAI client to call out to xAI. Make sure you have the appropriate API keys configured in your own `.env` file.

python

```
import base64
import json
import os
from datetime import datetime
from functools import partial
from textwrap import dedent
import braintrust as bt
import cairosvg
from anthropic import Anthropic
from dotenv import load_dotenv
from IPython.display import SVG, Image, Markdown, display
from openai import OpenAI
load_dotenv()
# Grab our Braintrust project
bt_project = bt.projects.create(name="YOUR_PROJECT_NAME")
grok_client = OpenAI(api_key=os.getenv("XAI_API_KEY"), base_url="https://api.x.ai/v1")
anthropic_client = OpenAI(api_key=os.getenv("ANTHROPIC_API_KEY"), base_url="https://api.anthropic.com/v1")
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
wrapped_grok_client = bt.wrap_openai(grok_client)
```
To run an eval, you need three things:

- Some data (a list of inputs we want to use to evaluate a task on)
- A task (a function like an LLM call that takes a single example from our data to perform some work)
- A scorer (a means to know how well our task performed)

Since our data will come by way of queries to create and describe an SVG image, we can move on to defining the task we want to evaluate.

First, we need a method to generate an SVG.

python

```
@bt.traced()
def create_svg_image(image_description: str, client, model_name: str, generation_kwargs: dict = {}):
    rsp = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": image_description}],
        **generation_kwargs,
    )
    # Extract svg content - handle both markdown wrapped and plain SVG
    content = rsp.choices[0].message.content  # type: ignore
    # Remove markdown code blocks if present
    # ...
    # Find SVG content if it's embedded in text
    if "<svg" in content:
        start = content.find("<svg")
        end = content.find("</svg>") + 6
        if start != -1 and end != 5:  # end != 5 means </svg> was found
            content = content[start:end]
    svg_string = content.strip()
    return svg_string
```
When you run this method with some code like this:

python

```
svg_string = create_svg_image(
    "Generate an SVG of a pelican riding a bicycle",
    client=wrapped_grok_client,
    model_name="grok-4-0709",
    generation_kwargs={"max_tokens": 10000},
)
display(SVG(data=svg_string))
```
... you'll get something like this:
![A pelican SVG](https://www.braintrust.dev/blog/img/grok-4-and-pelican-sample-svg.png)


Second, we'll need a task that takes an image and uses the same model to generate a description of the image.

python

```
@bt.traced()
def describe_image(image_path: str, client, model_name: str, generation_kwargs: dict = {}):
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode()
    image_url = f"data:image/png;base64,{image_data}"
    rsp = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "Describe this image in markdown format. Include the following sections: Simple Description, Main Subject, Background and Setting, Style and Tone\nUse bullet points for all sections after the Simple Description section.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image"},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            },
        ],
        **generation_kwargs,
    )
    content = rsp.choices[0].message.content  # type: ignore
    return image_url, content
```
This returns something like this:

```
## Simple Description
The image depicts a minimalist cartoon illustration of a white bird-like figure with a yellow beak, small wings, and an orange leg extended downward, appearing to interact with a small gray object via directional arrows, all set against a solid black background.
## Main Subject
- A central white, oval-shaped figure resembling a cartoon bird or penguin
- Features a small yellow beak pointing to the right
- Small, outstretched white wings on either side of the body
- An orange leg extending downward from the body, with an arrow along it pointing down
- A small gray oval or blob-like object at the end of the leg
- A larger downward arrow below the gray object, suggesting motion or direction
## Background and Setting
- Entirely solid black, creating a void-like environment
- No additional scenery, objects, or details present
- The setting emphasizes isolation and focus on the central subject
## Style and Tone
- Highly simplistic and minimalist, using basic geometric shapes like ovals and lines
- Cartoonish and illustrative, with flat colors and no shading or depth
- Neutral to slightly whimsical tone, possibly educational or diagrammatic due to the arrows indicating direction or force
```
And lastly, we'll need a top-level task that puts these all together:

python

```
@bt.traced()
def create_and_describe_image(image_description: str, client, model_name: str, generation_kwargs: dict = {}):
    # Create SVG Image
    svg_string = create_svg_image(
        image_description, client=client, model_name=model_name, generation_kwargs=generation_kwargs
    )
    # Convert SVG to PNG and save
    os.makedirs("_temp", exist_ok=True)
    png_data = cairosvg.svg2png(bytestring=svg_string.encode("utf-8"))
    with open("_temp/created_image.png", "wb") as f:
        f.write(png_data)
    # Ask model to describe the image it created
    image_url, description = describe_image(
        image_path="_temp/created_image.png", client=client, model_name=model_name, generation_kwargs=generation_kwargs
    )
    return {"image_url": image_url, "description": description}
```
The last component required to run an eval is one or more scorers. To demonstrate how to build your own custom scorers, we'll define an LLM-as-Jury which uses multiple LLM-as-Judge classifiers to derive a final judgement on how well the model did with describing the image it created.

In this example, we define OpenAI, Anthropic, and Grok judges, and average their scores to arrive at a final verdict.

python

```
class LikertScale(BaseModel):
    score: int = Field(
        ...,
        description="A score between 1 and 5 (1 is the worst score and 5 is the best score).",
        min_value=1,
        max_value=5,
    )  # type: ignore
    rationale: str = Field(..., description="A rationale for the score.")
def ask_llm_judge_about_image_description(client, model_name, input, output):
    gen_kwargs = {"response_format": LikertScale}
    if model_name.startswith("claude"):
        gen_kwargs = {}
    rsp = client.chat.completions.parse(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": dedent("""\
                    You are a critical expert in determining if a generated image matches what the user asked for and whether or not an AI model did a good job in describing that image.
                    The score must be an integer between 1 and 5.  You should respond ONLY with a JSON object with this format:{score:int, rationale:str}. Make sure you escape any characters that are not valid JSON.
                    Only response with a string that can be parsed as JSON using `json.loads()`. Double check your work!
                    """),
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"Here is the image generated from the description: {input}"},
                    {"type": "image_url", "image_url": {"url": output["image_url"]}},
                    {
                        "type": "text",
                        "text": f"Here is the description of the generated image: {output['description']}",
                    },
                    {
                        "type": "text",
                        "text": "Return a score between 1 and 5 based on how well the image matches the description and how well the description matches the image. 1 is the worst score and 5 is the best score.",
                    },
                ],
            },
        ],
        **gen_kwargs,
    )
    if model_name.startswith("claude"):
        parsed = json.loads(rsp.choices[0].message.content)
        return (parsed["score"] - 1) / 4
    else:
        parsed: LikertScale = rsp.choices[0].message.parsed
        return (parsed.score - 1) / 4
def is_good_description(input, output, expected=None, metadata=None):
    oai_judge_score = partial(
        ask_llm_judge_about_image_description, client=openai_client, model_name="gpt-4o", input=input, output=output
    )()
    anthropic_judge_score = partial(
        ask_llm_judge_about_image_description,
        client=anthropic_client,
        model_name="claude-3-5-sonnet-20240620",
        input=input,
        output=output,
    )()
    grok_judge_score = partial(
        ask_llm_judge_about_image_description,
        client=wrapped_grok_client,
        model_name="grok-4-0709",
        input=input,
        output=output,
    )()
    return [
        Score(name="is_good_description_judge_oai", score=oai_judge_score),
        Score(name="is_good_description_judge_anthropic", score=anthropic_judge_score),
        Score(name="is_good_description_judge_grok", score=grok_judge_score),
        Score(name="is_good_description_jury", score=(oai_judge_score + anthropic_judge_score + grok_judge_score) / 3),
    ]
```
When we run that against our outputs from `create_and_describe_image()`, we'll get something like this to add to our traces:

python

```
score = is_good_description(
    input="Create an SVG of a two cats riding a bicycle",
    output=rsp,
)
score
# [Score(name='is_good_description_judge_oai', score=1.0, metadata={}, error=None),
#  Score(name='is_good_description_judge_anthropic', score=0.75, metadata={}, error=None),
#  Score(name='is_good_description_judge_grok', score=1.0, metadata={}, error=None),
#  Score(name='is_good_description_jury', score=0.9166666666666666, metadata={}, error=None)]
```
Here, we'll run a single eval with Grok 4, but this can also be extended to add more image descriptions and tests with different models.

python

```
current_date_str = datetime.now().strftime("%Y%m%d%H")
print(current_date_str)
# This code was written to run in a Jupyter notebook
await bt.EvalAsync(
    name="YOUR_PROJECT_NAME",
    experiment_name=f"reasoning-xai-grok4-0709-{current_date_str}",
    data=lambda: [bt.EvalCase(input="Generate an SVG of a pelican riding a bicycle")],  # type: ignore
    task=partial(
        create_and_describe_image,
        client=wrapped_grok_client,
        model_name="grok-4-0709",
        generation_kwargs={"max_tokens": 10000},
    ),
    scores=[is_good_description],
    metadata={"vendor": "xai", "model": "grok-4-0709"},
)
```
Running this returns this nice summary:

```
=========================SUMMARY=========================
reasoning-xai-grok4-0709-2025071115-ea1bd6d0 compared to reasoning-xai-grok4-0709-2025071115:
75.00% 'is_good_description_judge_anthropic' score
75.00% 'is_good_description_judge_grok'      score
100.00% 'is_good_description_judge_oai'       score
83.33% 'is_good_description_jury'            score
1752272157.79s start
1752272241.95s end
32.16s (-126.19%) 'duration'                    	(1 improvements, 0 regressions)
16.06s (-62.58%) 'llm_duration'                	(1 improvements, 0 regressions)
326tok (-) 'prompt_tokens'               	(0 improvements, 0 regressions)
1062tok (-5300.00%) 'completion_tokens'           	(1 improvements, 0 regressions)
1388tok (-5300.00%) 'total_tokens'                	(1 improvements, 0 regressions)
4tok (-) 'prompt_cached_tokens'        	(0 improvements, 0 regressions)
0tok (-) 'prompt_cache_creation_tokens'	(0 improvements, 0 regressions)
See results for reasoning-xai-grok4-0709-2025071115-ea1bd6d0 at https://www.braintrust.dev/app/braintrustdata.com/p/<your-project-name>/experiments/reasoning-xai-grok4-0709-2025071115-ea1bd6d0
EvalResultWithSummary(summary="...", results=[...])
```
Based on the results, it looks like our jury thinks Grok 4 did well, with Anthropic giving it maximal praise.

With Braintrust, we can quickly view, aggregate, and add more experiments to better understand how well different models perform on this task.

![All our experiments](https://www.braintrust.dev/blog/img/grok-4-and-pelicans-eval-experiments.png)


You can select any experiment to see the individual eval trace:
![An example eval](https://www.braintrust.dev/blog/img/grok-4-and-pelicans-eval-example.png)


More evals of course.

In addition to improving the scorers, you can add more image descriptions to test these models out, as well as test more models. Braintrust makes it easy to [group
and aggregate results](https://www.braintrust.dev/docs/evaluate/interpret-results#use-aggregate-scores) by vendor or model family so that you can systematically measure the progress of these models over time.

If you have any interesting tests you run when a new model comes out, [let us know](https://x.com/braintrustdata)!
