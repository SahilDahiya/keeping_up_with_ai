---
title: Build with OpenAI’s Whisper model in five minutes
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/openai-whisper-in-five-minutes
author: Justin Yi
published: '2022-10-18'
fetched: '2026-11-12T06:13:30Z'
classifier: null
taxonomy_rev: 2
words: 739
content_sha256: cc937074888b015a4c8bfa819cd51ed7569ef0ed4afe26b17a80112f81e00deb
---

# Build with OpenAI’s Whisper model in five minutes

AI engineering
# Build with OpenAI’s Whisper model in five minutes

Deploy OpenAI Whisper for free on Baseten instantly from our model library. Or stick around to learn how to package and deploy Whisper with Truss.


- Authors
- Date
- October 18, 2022

As soon as I saw [Whisper](https://openai.com/blog/whisper/) — OpenAI’s open-source neural network for automatic speech recognition — I knew I had to start experimenting with it. The model isn’t an incremental improvement on speech-to-text, it is a paradigm shift from “this technology could be cool one day” to “this technology has arrived.” Tested around the Baseten office, it captured not just English but Urdu, Mandarin, French, and more with stunning accuracy.

You can try Whisper for yourself from our model library.

I’m a new grad software engineer, not an ML or infrastructure expert, so it was very satisfying to be able to deploy this impactful model. In this blog post, I’ll first show you how you can deploy Whisper instantly as a pre-trained model, then walk you through the steps I took to package and deploy the model myself.

If you’re as excited as I am about Whisper, you’ll want to start using it right away. That’s why we added Whisper to our pre-trained model library, so all Baseten users can deploy Whisper in seconds for free.

All you have to do is sign in to your Baseten account and deploy Whisper from the model library. Deploying the model takes just a few clicks and you’ll be up and running all but instantly.

If you don’t have a Baseten account yet, you can [sign up for free here](https://app.baseten.co/signup?utm_source=blog&utm_campaign=whisper).

To invoke the model, just pass in a dictionary with a URL pointing to an MP3 file, like this:

json

```
{
  "url": "https://cdn.baseten.co/docs/production/Gettysburg.mp3"
}
```
That should be everything you need to get started building an application powered by Whisper. But if you’re interested in the mechanics of how I deployed this novel model, stick around for the rest of the writeup!

I used Truss, Baseten’s open-source model packaging and serving library, to deploy Whisper. You can see the packaged model in its entirety in this example Truss.

To get started, I installed Truss from PyPi and created a new Truss:

bash

```
pip install --upgrade truss
truss init whisper
```
Whisper was created with PyTorch, one of Truss’ supported frameworks, but some of its dependencies were brand new. Fortunately, they were easy to add in my Truss’ configuration file.

yaml

```
requirements:
  - git+https://github.com/openai/whisper.git
  - --extra-index-url https://download.pytorch.org/whl/cu113
  - requests
system_packages:
  - ffmpeg
```
Another interesting challenge was working with GPUs to run the model. Whisper, like many large models, not only requires GPUs for model training but also for model invocation. In Truss, signaling that a GPU is needed is a two-line config.

```
resources:
  cpu: "4"
  memory: 16Gi
  use_gpu: true
  accelerator: A10G
```
But you’re not here for infrastructure, you’re here for awesome ML models. The heart of any model packaged as a Truss is the *predict* function in the `model/model.py` file. Let’s take a look:

python

```
def predict(self, request: Dict) -> Dict:
    with NamedTemporaryFile() as fp:
        fp.write(request["response"])
        result = whisper.transcribe(
            self._model,
            fp.name,
            temperature=0,
            best_of=5,
            beam_size=5,
        )
        segments = [
            {"start": r["start"], "end": r["end"], "text": r["text"]}
            for r in result["segments"]
        ]
    return {
        "language": whisper.tokenizer.LANGUAGES[result["language"]],
        "segments": segments,
        "text": result["text"],
    }
```
You’ll notice that the model is invoked on a file path. Like most models that interface with anything more complicated than strings or numbers, such as audio in this case, Whisper relies on pre-processing work to turn the input into something it can use. With Truss, pre- and post-processing functions are bundled with the model invocation code in the same file.

```
def preprocess(self, request: Dict) -> Dict:
    resp = requests.get(request["url"])
    return {"response": resp.content}
def postprocess(self, request: Dict) -> Dict:
    return request
```
After I put together the Truss of the Whisper model, it was time to deploy. Getting the model on Baseten was as simple as calling `truss push` on the Truss of the Whisper model, pasting my Baseten API key when prompted.

`truss push`
Then, I was able to call the model from the CLI.

`truss predict -d '{"url": "https://cdn.baseten.co/docs/production/Gettysburg.mp3"}'`
Since first deploying Whisper, I've worked with the model in a ton of situations, including a cool high-throughput project for Patreon. I want to see what you build with Whisper too! Please send me any ideas or neat demos at [support@baseten.co](mailto:support@baseten.co).
