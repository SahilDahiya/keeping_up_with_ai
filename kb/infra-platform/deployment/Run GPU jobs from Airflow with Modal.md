---
title: Run GPU jobs from Airflow with Modal
topic: infra-platform
subtopic: deployment
secondary_topics: []
summary: Shows how to run GPU jobs from Airflow, connecting existing orchestration
  systems to elastic AI compute.
source: modal
url: https://modal.com/blog/modal-airflow
author: null
published: '2024-06-20'
fetched: '2026-07-11T04:30:15Z'
classifier: codex
taxonomy_rev: 1
words: 1667
content_sha256: befeb3c3f8acdbf504f8656439283b6e0ea0b1ed65f9c414d1a4fed4a57e3255
triage: keep
skip_reason: null
---

# Run GPU jobs from Airflow with Modal

[Back](https://modal.com/blog)

# Run GPU jobs from Airflow with Modal

[Kenny Ning](https://twitter.com/kenny_ning)

Many teams use [Airflow](https://airflow.apache.org) to manage multi-stage workflows. However, when scaling workflows from local to production, Airflow relies on Celery or Kubernetes, which are difficult and time-consuming to set up, especially if you need to provision GPUs for AI / ML workflows.

Modal is a much simpler way to manage GPUs [and ](https://modal.com/docs/guide/gpu)[containerized environments](https://modal.com/docs/guide/images), making it ideal for AI / ML workflows. Modal can be triggered directly from an Airflow DAG and can serve as a replacement for your Celery or Kubernetes executor. You’d get the same scalability features from those backends with the ease of installation of the Local executor.

In this blog post, we’ll show you **how to run Modal jobs from Airflow**:

- Install Modal in your Airflow environment
- Set your [Modal token](https://modal.com/docs/reference/modal.config#modalconfig)ID and secret in your Airflow environment
- Option 1: [Deploy](https://modal.com/docs/guide/managing-deployments)your Modal Functions and call`lookup`
- Option 2: Create a custom operator that uses [Modal Sandboxes](https://modal.com/docs/guide/sandboxes)

We’ll go through each of these steps for a simple example: a two-step data pipeline pulling [ELI5 questions](https://www.reddit.com/r/explainlikeimfive/) from Reddit and answering them using an LLM.

## Install Modal in your Airflow environment

We recommend you use [Astro CLI](https://www.astronomer.io/docs/astro/cli/local-airflow-overview) to develop Airflow locally. Astro CLI is provided by the good folks at [Astronomer](https://www.astronomer.io), a fully managed Airflow platform.

To install Modal into this Airflow environment, add `modal` to the `requirements.txt` file of your [Astro project](https://www.astronomer.io/docs/astro/cli/develop-project#add-python-os-level-packages-and-airflow-providers). If you don’t have an Astro project, [download the Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli) and run `astro dev init`.

If you’re using [Astro Hosted](https://www.astronomer.io/docs/astro/astro-architecture), these dependencies will be included in your deployment when you run `astro deploy`.

## Set your Modal token

Set the following environment variables in your Airflow environment:

- `MODAL_TOKEN_ID`
- `MODAL_TOKEN_SECRET`

If you already have Modal set up locally, you can find your token id and secret values by running `cat ~/.modal.toml`. You can also create new token credentials from your [Modal Settings](https://modal.com/docs/guide/workspaces#create-a-token-for-a-workspace).

For local development, you can set these environment variables in `.env` in your Astro project. When you’re ready to deploy to production, you can sync these to your production deployment with [these steps](https://www.astronomer.io/docs/astro/manage-env-vars#manage-environment-variables-locally).

## Option 1: Deploy Modal Functions and call via `lookup`



Good for: Existing Modal users with deployed Functions, teams wanting separation of concerns between Airflow and Modal deploy process

Let’s assume we already have a Modal App called `example-modal-airflow` with two Functions:

- `fetch_reddit`: scrapes ELI5 questions from Reddit
- `answer_questions`: answers lists of questions using an LLM (requires GPU, see- [this example](https://modal.com/docs/examples/trtllm_llama))

If we deploy this App to our workspace with `modal deploy`, we can call it directly from Airflow with `lookup` and `remote`.

```
"""
Airflow DAG using Modal lookup
"""
from airflow.decorators import dag, task
from datetime import datetime
from modal import Dict, Function
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    tags=["example"],
)
def example_modal_airflow():
    # create dict for storing results
    d = Dict.from_name("reddit-question-answers", create_if_missing=True)
    @task()
    def fetch_reddit(**context) -> None:
        """
        This task gets the 100 newest ELI5 questions from Reddit
        """
        # look up function in our deployment
        f = Function.from_name("example-modal-airflow", "fetch_reddit")
        questions = f.remote()
        for q in questions:
            d[q] = None  # store questions first
    @task()
    def answer_questions(**context) -> None:
        """
        Uses LLM example to answer the questions
        """
        # look up inference function
        f = Function.from_name("example-modal-airflow", "answer_questions")
        questions = list(d.keys())
        answers = f.remote(questions)
        # update dict with answers
        for i in range(len(questions)):
            d[questions[i]] = answers[i]
    # define dependencies
    fetch_reddit() >> answer_questions()
# instantiate DAG
example_modal_airflow()
```
You can run `astro run example_modal_airflow()` from the terminal or go to the Airflow UI to trigger the workflow manually:

![airflow_ui](https://modal-cdn.com/cdnbot/airflow-ui.png)



If we go to our Modal dashboard, we can see the run logs for each of these invocations, including GPU utilization for the LLM task:

![gpu_modal_dashboard](https://modal-cdn.com/cdnbot/gpu_modal_dashboard.png)



We’re using a [Modal Dict](https://modal.com/docs/reference/modal.Dict) here as intermediate storage between tasks, which is also easy to inspect for debugging purposes. We can use it to look at an example output of our pipeline directly from any Python environment:

```
>>> import modal
>>> d = modal.Dict.from_name('reddit-question-answers')
>>> for item in d.items():
...   print(item[0])
...   print(item[1])
...   break
...
ELI5 Indian metro system
The Delhi Metro, also known as the DMRC (Delhi Metro Rail Corporation), is a rapid transit system serving the city of New Delhi and its surrounding areas in India. Here's an ELI5 explanation:
**What is it?**
The Delhi Metro is a train-based public transportation system that connects various parts of the city. It's like a big, underground highway for trains that takes people from one place to another.
**How does it work?**
1. **Trains:** The Delhi Metro has 8 lines with over 225 stations, which are connected by trains that run on tracks.
2. **Lines:** There are two types of lines: Phase I (Phase 1) and Phase II (Phase 2). Phase I has 6 lines, while Phase II has 3 more lines.
3. **Stations:** Each station has platforms where passengers can board or exit the train. Some stations have multiple platforms, so you might need to check the signs to find your platform number.
4. **Fares:** You can buy tickets at ticket counters or use your smart cards (like a special kind of debit card).
5. **Frequency:** Trains run frequently, usually every few minutes during peak hours and less often during off-peak hours
```
Here are some other options for passing data between tasks:

- [Pass the data](https://www.astronomer.io/docs/learn/airflow-passing-data-between-tasks)directly: this uses Airflow XComs, which in turn uses the metadata database in your Airflow deployment for storage. This approach is more limited in size of data you can transmit; if you’re using Postgres, that- [limit is 1GB](https://www.astronomer.io/docs/learn/airflow-passing-data-between-tasks#when-to-use-xcoms). Meanwhile, Modal Dicts have- [a limit of 10GB](https://modal.com/docs/guide/dicts).
- Mount a [Volume](https://modal.com/docs/guide/volumes)in your Modal function and store the data there: a lot of raw data is expressed in files (e.g.[NYC taxi trips](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)), and Volumes are a more natural way to store files and directories.

## Option 2: Create a custom Operator that uses Modal Sandboxes


Good for: Existing Airflow users who are looking for an easy way to access GPUs for a task directly in their DAG code

Alternatively, you can write a [custom Operator](https://www.astronomer.io/docs/learn/airflow-importing-custom-hooks-operators) that uses [Modal Sandboxes](https://modal.com/docs/guide/sandboxes) to run Python code in a container defined at runtime.

Your directory structure will look something like this:

```
├── dags/
│   └── example_modal_operator.py # DAG that calls ModalOperator and passes in the function from scripts.py
│   └── utils/
│       └── scripts.py  # Python scripts we want to run inside a Modal Sandbox
├── include/
│   └── modal_operator.py # custom operator that defines how Python functions get run in Modal Sandboxes
```
Let’s start with `modal_operator.py`. In Airflow, an Operator is a Python class that gets instantiated as a task when you call it in a DAG. You may already be familiar with [ BashOperator](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html) or

[. Custom Operators allow you to re-use code across tasks that call the same service:](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html)

`KubernetesPodOperator`Our Operator has three initialization parameters:

- `client`: a- [modal.Client](https://modal.com/docs/reference/modal.Client)object that reads in our token environment variables
- `fn`: the Python function that we want to run in a sandbox
- `sandbox_config`: dictionary of Sandbox parameters (e.g. image, gpus)

```
# include/modal_operator.py
from airflow.models.baseoperator import BaseOperator
import inspect
import modal
class ModalOperator(BaseOperator):
    """
    Custom Airflow Operator for executing tasks on Modal.
    """
    def __init__(self, client, fn, sandbox_config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.fn = fn
        self.sandbox_config=sandbox_config
    def execute(self, context):
        # converts the Python function object into an executable string
        fn_lines = inspect.getsourcelines(self.fn)[0]
        fn_lines.append(f"{self.fn.__name__}()")
        fn_as_string = "".join(fn_lines)
        # runs the function in a Modal Sandbox with the provided config
        sb = modal.Sandbox.create(
            "python",
            "-c",
            fn_as_string,
            client=self.client,
            app=self.app,
            **self.sandbox_config
        )
        sb.wait()
        return sb.stdout.read()
```
Next, let’s define `fetch_reddit` within `scripts.py`:

```
# dags/utils/scripts.py
def fetch_reddit():
    # import task dependencies inside of functions, not global scope
    import os
    import praw
    # Reddit client secrets that are saved as Modal Secrets
    reddit = praw.Reddit(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        user_agent="reddit-eli5-scraper",
    )
    subreddit = reddit.subreddit("explainlikeimfive")
    questions = [topic.title for topic in subreddit.new()]
    file_path = "/data/topics.txt"
    print(f"Writing data to {file_path}")
    with open(file_path, "w") as file:
        file.write("\n".join(questions))
```
Finally, let’s put this script and our new custom Operator together in a DAG:

```
# dags/example_modal_operator.py
"""
## ModalOperator + Sandboxes example
"""
from airflow.decorators import dag
from include.modal_operator import ModalOperator
from dags.utils.scripts import fetch_reddit
from datetime import datetime
import modal
import os
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    tags=["example"],
)
def example_modal_operator():
    reddit = ModalOperator(
        task_id="fetch_reddit",
        # pass in your Modal token credentials from environment variables
        client=modal.Client.from_credentials(
            token_id=os.environ["MODAL_TOKEN_ID"],
            token_secret=os.environ["MODAL_TOKEN_SECRET"],
        ),
        # function we import from `scripts.py`
        fn=get_reddit_questions,
        sandbox_config={
            # define Python dependencies
            "image": modal.Image.debian_slim().pip_install(
                "praw"
            ),
            # attach Modal secret containing our Reddit API credentials
            "secrets": [
                modal.Secret.from_name("reddit-secret")
            ],
            # attach Volume, where the output of the script will be stored
            "volumes": {
                "/data": modal.Volume.from_name("airflow-sandbox-vol")
            },
        },
    )
    reddit
# instantiate the DAG
example_modal_operator()
```
This DAG imports the function in our script, instantiates a Modal Client, and launches the script in a Sandbox via our custom ModalOperator.

**Note**: We are currently working on a Modal [Airflow provider package](https://github.com/astronomer/airflow-provider-sample) that would allow you to install the above `ModalOperator` and associated Modal Connection object directly into your Airflow project.

## Conclusion: Airflow + Modal help each other

The biggest benefit of using Modal with Airflow is that it easily allows you to **isolate your task environment** from your Airflow environment. The current solution for this today is to stand up a complicated deploy process building Docker images, publishing to a registry, and using the KubernetesPodOperator.

For Modal users, defining custom images or attaching GPUs is as simple as a [function decorator](https://modal.com/docs/guide/gpu), while Airflow adds a single control pane to oversee the lifecycle of a multi-stage pipeline. Together you get the best of both worlds: full-featured data pipeline observability and easy GPU container lifecycle management.

## Are you an Astronomer and Modal customer?

We highly encourage you to try out Modal in your Astronomer workflows as we roll out a tighter integration. Please reach out to [support@modal.com](mailto:support@modal.com) or [Astronomer support](https://www.astronomer.io/contact/) if you have any feedback and/or are interested in being a design partner with us.
