---
title: Embedding English Wikipedia in under 15 minutes
topic: rag-retrieval
subtopic: embeddings
secondary_topics:
- infra-platform/deployment
summary: Walkthrough of embedding English Wikipedia quickly, covering large-scale
  embedding jobs, batching, and storage workflow.
source: modal
url: https://modal.com/blog/embedding-wikipedia
author: null
published: '2024-01-23'
fetched: '2026-07-11T04:30:49Z'
classifier: codex
taxonomy_rev: 1
words: 2446
content_sha256: 9f49548645956ececae9c8deb33461d0f1e88213f6e8752f5727a66e4a39c083
triage: keep
skip_reason: null
---

# Embedding English Wikipedia in under 15 minutes

[Back](https://modal.com/blog)

# Embedding English Wikipedia in under 15 minutes

[Jason Liu](https://twitter.com/jxnlco)

Text embeddings are a key component of production-ready applications using large language models (LLMs). A text embedding model transforms chunks of text into vectors of floating-point numbers that represent their semantic meaning, allowing us to quantitatively compare strings for similarity. Creating embeddings on a large corpus of text enables us to build applications like search and recommendation engines, as well as give additional context to LLMs for Retrieval-Augmented Generation (RAG) on custom documents.

Embedding models behind APIs like OpenAI’s [ text-embedding-ada-002](https://platform.openai.com/docs/api-reference/embeddings) are a great way to get started with building for these use cases. However, as
you gather user data and tailor your applications using that data, you will
likely get

**higher-quality results at lower cost**if you used this data to

[fine-tune](https://modal.com/docs/examples/llm-finetuning)an open-source embedding model. This requires setting up large-scale embedding jobs, which can be a challenge due to rate limits, infrastructure complexity, and the infeasibility of getting a large number of GPUs for short bursts of time. So what can we do? Enter Modal.

Modal provides a serverless solution for organizations grappling with scaling
workloads. Modal’s technology enables rapid scaling across many GPUs, which we
can use to run large-scale workloads, such as generating embeddings for a
massive text dataset, at lightning speed. In this post, we’ll go over everything
you need to embed the entire English Wikipedia in just 15 minutes using Hugging
Face’s [Text Embedding Inference](https://huggingface.co/docs/text-embeddings-inference/index) service on Modal. Using Modal’s serverless solution, this job comes out to just
over $15.

More specifically, we will:

- Discuss the advantages of using open source models.
- Explain the fundamentals of using Modal.
- Guide you through the necessary code to implement our embedding client on the Wikipedia dataset.

Shortening the embedding generation time from multiple hours to just a few minutes enables more frequent experimentation, which is crucial for continuous model fine-tuning in production use cases (as you have to regenerate embeddings for your entire corpus of data every time). In future posts, we’ll delve into using Modal for other aspects of this workflow (running grid search on and fine-tuning your own embedding models) to create more tailored user experiences.

## Why open-source models?

Closed-source models are a great way to get started with creating and using embeddings, but they run into two critical limitations in production:

- As you run your model in production, you gather a corpus of rich preference data that can be used to improve the performance of your model. However, fine-tuning proprietary models with this custom data you’ve gathered is either impossible or highly cost-prohibitive.
- Remote APIs have a number of drawbacks, such as rate limits, unreliable tail latencies, and high costs associated with tokens rather than compute time.

For these reasons, we believe that open-source embedding models that
progressively get better with fine-tuning are best suited for embedding use
cases like RAG workflows in production. Thousands of [open-source models](https://huggingface.co/models?pipeline_tag=sentence-similarity&sort=trending) are available on Hugging Face.

## Why Modal?

Model makes it easy to run your code in the cloud and push to production. By only paying for what you use, and abstracting away all the complexity of deploying and serving, Modal provides a simplified process to help you focus on what’s important—your product.

To follow along with some of these examples, you’ll need to

[create a Modal account](https://modal.com/signup). You’ll get $30 out of the box and all of the features to try out immediately. Once you’ve done so, make sure to[install the Modal Python package](https://pypi.org/project/modal/)using a virtual environment of your choice, and you can run all of the code we provide below.

## Modal Concepts

Before we dive into the code, let’s take a look at some of the key concepts that
Modal provides that will allow us to run our embedding job quickly and
efficiently. In order to understand that, we’ll need to look at two concepts - a `Function` and a [ Volume](https://modal.com/docs/guide/volumes).

### Functions

Modal functions package the code you want to run, along with their environment. They describe the image, the requirements, and the storage we want to attach in order to get the job done.

```
import modal
app = modal.App()
pandas_image = modal.Image.debian_slim().pip_install("pandas")
volume = modal.Volume.from_name("embedding-wikipedia", create_if_missing=True)
@app.function(image=pandas_image, gpu="A100", volumes={"/root/foo": volume})
def my_fn():
    # perform tasks here
```
Using Modal functions, you could for example, provision on-demand GPUs for fine-tuning workloads, define endpoints to serve large language models at scale, and even spin up hundreds of containers to process large datasets in parallel.

### Volumes

In order to load large datasets and models efficiently, we can use Modal’s [Volumes](https://modal.com/docs/guide/volumes) feature. Volumes are a way to mount data into
your containers and allow you to read and write to them as if they were a local
file system. You can create a new volume using the `modal volume create` command.

## Embedding Wikipedia

Now that we’ve got a good understanding of some key concepts that Modal
provides, let’s load the `wikipedia` dataset in a persistent volume we’ve
created called `embedding-wikipedia`, set up the Hugging Face inference server,
and run our distributed batch GPU job to embed the entire dataset.

The Hugging Face inference server is a fast way to get started to test different models from Hugging Face. They offer an easy-to-use client and a wide range of configurations to make the most out of your infrastructure.


### Loading the Dataset

We’ll be using the Hugging Face `datasets` library to download the dataset
before saving it explicitly into a directory of our choice for future use. In
order to do so, we’ll create a file called [ download.py](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/embeddings/wikipedia/download.py),
where we’ll create our first

[Modal image](https://modal.com/docs/guide/images)with the

`datasets` package installed.Note here that we explicitly need to commit and save new changes to our volume. If not, these changes will be discarded once the container is shut down. See more information in our docs

[here](https://modal.com/docs/guide/volumes#volume-commits-and-reloads).

```
import modal
volume = modal.Volume.from_name("embedding-wikipedia")
image = modal.Image.debian_slim().pip_install("datasets")
app = modal.App(image=image)
cache_dir = "/data"
@app.function(volumes={cache_dir: volume}, timeout=3000)
def download_dataset(cache=False) -> None:
    from datasets import load_dataset
    # Download and save the dataset locally
    dataset = load_dataset("wikipedia", "20220301.en", num_proc=10)
    dataset.save_to_disk(f"{cache_dir}/wikipedia")
    # Commit and save to the volume
    volume.commit()
```
You can then run this file by using the command

`modal run download.py::download_dataset`### Hugging Face Embedding Inference Server

For our embedding function, we’ll be using the Hugging Face [Text Embedding Inference](https://github.com/huggingface/text-embeddings-inference) server. We’ll walk through how to leverage caching of model weights by defining
another custom Modal image, managing container state through a Modal `cls` , and
lastly, leveraging this new container in our other functions.

### Parameters

Let’s start by defining some parameters for the `Text Embedding Inference` program. In our case, we’re specifying the specific embedding model we’re using
and increasing the maximum batch size so that we can speed up our embedding job.

```
MODEL_ID = "BAAI/bge-small-en-v1.5"
BATCH_SIZE = 768
LAUNCH_FLAGS = [
    "--model-id",
    MODEL_ID,
    "--port",
    "8000",
    "--max-client-batch-size",
    str(BATCH_SIZE),
    "--max-batch-tokens",
    str(BATCH_SIZE * 512),
]
```
### Defining Our Image

We’ll be using the recommended image for A10G GPUs for this example. If you’d
like to explore other GPU models, you should make sure to download the correct
model listed [here](https://huggingface.co/docs/text-embeddings-inference/supported_models).
Note that we also override the default entrypoint so that it is compatible with
Modal.

```
tei_image = (
    Image.from_registry(
        "ghcr.io/huggingface/text-embeddings-inference:86-0.4.0",
        add_python="3.10",
    )
    .entrypoint([])
    .pip_install("httpx", "numpy")
)
```
### Creating our Modal Class

Using a Modal class enhances control over a container’s lifecycle (see more [here](https://modal.com/docs/guide/lifecycle-functions)):

- Initialize once at boot with **@enter**.
- Handle calls from other functions using **@method**decorators.
- Clean up at shutdown with **@exit**.

We initialize a server at boot, spinning out an inference server that maintains
its state for subsequent requests and optimizes initialization costs. Modal
simplifies lifecycle management by requiring only a couple function definitions
and a decorator. Additionally, we configure the app class for specific images
and GPUs through [ app.cls](https://modal.com/docs/reference/modal.App#cls) parameters. Once we’ve set this up, most of our code will focus on preparing our
data and efficiently sending it to the

`TextEmbeddingsInference` servers.```
import modal
GPU_CONFIG = "A10G"
def spawn_server() -> subprocess.Popen:
    import socket
    process = subprocess.Popen(["text-embeddings-router"] + LAUNCH_FLAGS)
    # Poll until webserver at 127.0.0.1:8000 accepts connections before running inputs.
    while True:
        try:
            socket.create_connection(("127.0.0.1", 8000), timeout=1).close()
            print("Webserver ready!")
            return process
        except (socket.timeout, ConnectionRefusedError):
            # Check if launcher webserving process has exited.
            # If so, a connection can never be made.
            retcode = process.poll()
            if retcode is not None:
                raise RuntimeError(f"launcher exited unexpectedly with code {retcode}")
@app.cls(
    gpu=GPU_CONFIG,
    image=tei_image, # This is defined above
)
class TextEmbeddingsInference:
    @modal.enter()
    def open_connection(self):
        # If the process is running for a long time, the client does not seem to close the connections, results in a pool timeout
        from httpx import AsyncClient
        self.process = spawn_server()
        self.client = AsyncClient(base_url="http://127.0.0.1:8000", timeout=30)
    @modal.exit()
    def terminate_connection(self, exc_type, exc_value, traceback):
        self.process.terminate()
    async def _embed(self, chunk_batch):
        texts = [chunk[3] for chunk in chunk_batch]
        res = await self.client.post("/embed", json={"inputs": texts})
        return np.array(res.json())
    @modal.method()
    async def embed(self, chunks):
        """Embeds a list of texts.  id, url, title, text = chunks[0]"""
        # in order to send more data per request, we batch requests to
        # `TextEmbeddingsInference` and make concurrent requests to the endpoint
        coros = [
            self._embed(chunk_batch)
            for chunk_batch in generate_batches(chunks, batch_size=BATCH_SIZE)
        ]
        embeddings = np.concatenate(await asyncio.gather(*coros))
        return chunks, embeddings
```
### Generating Embeddings

Let’s take stock of what we’ve achieved so far:

- We first created a Modal `App`.
- Then, we created a persistent `Volume`that could store data in between our script runs and downloaded the entirety of English Wikipedia into it.
- Next, we put together our first Modal `cls`object using the Text Embedding Inference image from Docker and attached an`A10G`GPU to the class.
- Lastly, we defined a method we could call from other app functions using the `@method`decorator.

Now, let’s see how to use the dataset that we downloaded with our container to
embed all of Wikipedia. We’ll first write a small function to split our dataset
into batches before seeing how we can get our custom Modal `cls` object to embed
all of the chunks.

### Chunking Text

We’ll be using the [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) model in
order to embed all of our content. This model has state-of-the-art benchmark
results at great peformance. It has a maximum sequence length of 512 tokens so
we can’t pass in an entire chunk of text at once. Instead, we’ll split it into
chunks of 400 characters for simplicity using the function below, but in
practice you’ll want to split it more intelligently and include overlap between
chunks to avoid losing information.

```
def generate_chunks_from_dataset(xs, chunk_size: int = 400):
    for data in xs:
        id_ = data["id"]
        url = data["url"]
        title = data["title"]
        text = data["text"]
        for chunk_start in range(0, len(text), chunk_size):
            yield (
                id_,
                url,
                title,
                text[chunk_start : chunk_start + chunk_size],
            )
```
To amortize the overhead of data transfer, we batch our `generate_chunks_from_dataset` chunks into batches of 512 chunks each. This
allows us to pass in a batch of 512 chunks to our Modal `cls` object to embed at
once.

```
def generate_batches(xs, batch_size=512):
    batch = []
    for x in xs:
        batch.append(x)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
```
### Mapping the embedding function

After creating a function to batch our dataset, we can now pass these chunks to
our Modal `cls` object for embedding. We use a custom image with the `datasets` library installed to easily load our dataset from disk. Additionally, we have
logic to extract a subset of the dataset.

To call our custom Modal `cls` object and use the `.embed` function with our
data batches, we simply use the `.map` function. Modal takes care of managing
the containers, serializing and deserializing inputs, and handling the lifecycle
of each container.

```
@app.function(
    image=Image.debian_slim().pip_install("datasets"),
    volumes={cache_dir: volume},
    timeout=5000,
)
def embed_dataset():
    dataset = load_from_disk(f"{cache_dir}/wikipedia")
    model = TextEmbeddingsInference()
    text_chunks = generate_chunks_from_dataset(dataset["train"], chunk_size=512)
    batches = generate_batches(text_chunks, batch_size=batch_size)
    # Collect the chunks and embeddings
    for batch_chunks, batch_embeddings in model.embed.map(batches, order_outputs=False):
        ...
    return
```
Once we have this function we can use `modal run` on this [ main.py](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/embeddings/wikipedia/main.py) file to execute the specific function:

`modal run main.py::embed_dataset`## Further customization

### Deploying on a schedule

In a production setting, you might want to run this on a schedule as new data
comes in or as you get more user data. This allows you update data and models in
production without having to worry about the underlying infrastructure. You just
need to modify the `@app.function` decorator to add in a `schedule` parameter.
This can be modified to any arbitrary period that you’d like to use depending on
your use case.

```
@app.function(..., schedule=modal.Period(days=1))
def my_function():
    pass
```
We can then deploy this function using the command

`modal deploy --name wikipedia-embedding main.py`If you’d like to change the frequency, just change the schedule parameter and re-deploy, and you’re good to go!

### Uploading your dataset

If you check out our example code, you’ll notice that we’ve uploaded the
embedded dataset to a [public Hugging Face dataset](https://huggingface.co/datasets/567-labs/wikipedia-bge-small-en-v1.5-full).
We provide some details in the README on how to do this. In practice, how you
handle this data will depend on your use case. You can also can follow similar
steps to upload it to a private dataset or insert it into your favorite vector
database.

### GPUs go brr

For free accounts, Modal caps the concurrent number of GPUs that can be used
to 10. Using 10 GPUs in parallel still greatly speeds up the embedding job, but
if you are on a [paid plan](https://modal.com/pricing), the GPU limit can be
raised.

All we really need to do then is crank up the value of `max_containers` to a
number like 50, and we’ll end up with 50 separate containers (each with their
own `A10G` GPU) processing batches of text to be embedded.

```
@app.cls(
    gpu=GPU_CONFIG,
    image=tei_image,
    max_containers=50,  # Number of concurrent containers that can be spawned to handle the task
)
class TextEmbeddingsInference:
    # Rest of code below
```
## Conclusion

In this post, we show how to use some of Modal’s abstractions to run massive parallelizable jobs at scale. Having the ability to scale unlocks new business use cases for companies that can now iterate on production models more quickly and efficiently. By shortening the feedback loop with Modal’s serverless GPUs, teams are free to focus on experimentation and deployment.

We’ve uploaded our full code [here](https://github.com/modal-labs/modal-examples/tree/main/06_gpu_and_ml/embeddings/wikipedia),
which helps you quickly get started and also showcases how to upload your own
generated embeddings to Hugging Face. You can also check out some [example datasets](https://huggingface.co/567-labs) that contain embeddings we
computed using some popular open source embedding models.

Try running your own large-scale batch jobs by [creating your free Modal account](https://modal.com/signup), and follow [@modal](https://x.com/modal) on X/Twitter to stay posted on
upcoming posts on further customizing your embeddings workflow.
