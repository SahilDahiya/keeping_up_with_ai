---
title: Streaming real-time text to speech with XTTS V2
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- models/multimodal
summary: Walks through deploying a streaming endpoint for XTTS V2 (voice-cloning TTS
  from a 6-second sample) with a 200ms round-trip time to first audio chunk, for near-real-time
  narration across 17 languages.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/streaming-real-time-text-to-speech-with-xtts-v2
author: Het Trivedi
published: '2024-04-18'
fetched: '2026-11-12T06:12:14Z'
classifier: claude
taxonomy_rev: 2
words: 1295
content_sha256: 5d4651f278cd2dd829f4e34a646145215f436e27947a111fcc48865ebbc70863
---

# Streaming real-time text to speech with XTTS V2

AI engineering
# Streaming real-time text to speech with XTTS V2

In this tutorial, we'll build a streaming endpoint for the XTTS V2 text to speech model with real-time narration and 200 ms time to first chunk.


- Authors
- Date
- April 18, 2024

TLDR

In this tutorial, we deploy a streaming endpoint for XTTS V2, a state of the art open source text to speech model with voice cloning capabilities. The streaming endpoint has a total round-trip time to first chunk of as little as 200 milliseconds and delivers near real-time audio playback for a given text — making it an ideal example of a real-time TTS deployment in action.

A text to speech model (or speech synthesis model) is a type of generative AI model that creates a natural, humanlike narration of a text input. A strong text to speech model lets you turn any book into an audiobook or any article into a podcast. But with streaming TTS output, text to speech models can power an entire new class of AI applications.

When you chat with an LLM, the model starts responding as soon as the first characters of output are ready rather than making you wait for it to write the entire reply. With an optimized LLM deployment, you can get that time to first token below a couple hundred milliseconds, making the chat feel instant.

You can do the same for text to speech models. Streaming audio output in real-time TTS mode with super-fast (\~200ms) time to first chunk unlocks massive use cases across conversational user interfaces.

In this tutorial, we’ll build a streaming real-time TTS endpoint for XTTS 2, a realistic text to speech model with support for over a dozen languages.

XTTS V2 is a high-quality open source model that takes in text and, optionally, a voice sample as input and converts the text to an audio recording of the spoken text in the chosen voice. It only needs a six-second audio sample for voice cloning and is capable of generating speech in 17 languages.

Like an LLM, text to speech models like XTTS V2 are autoregressive models that work in tokens. The input text is tokenized and passed to the speech synthesis model, which iterates over the input to produce audio chunks.

In a minute, a person speaking in English can generally say 120 to 150 words, which can be as much as 200 tokens for token-based AI models. On an inexpensive T4 GPU, XTTS V2 can easily synthesize enough tokens of speech for real-time TTS output.

By default, XTTS V2 returns the entire spoken text as a single response. Instead, we can implement a model server that streams output as it is generated, enabling near real-time TTS narration.

Before following this tutorial, please make sure to:

1. [Create a Baseten account](https://app.baseten.co/signup/?next=/) or sign in to your existing account.
2. Create an API key and copy it someplace safe, you’ll need it for two future steps.
3. Install Truss, Baseten’s open source model packaging framework, with `pip install truss`.

To download and deploy an out-of-the-box implementation of the XTTS V2 streaming endpoint, run:

bash

```
git clone https://github.com/basetenlabs/truss-examples/
cd xtts-streaming
truss push
```
Provide your API key when prompted during `truss push`. Follow along below for detailed instructions on building and deploying the endpoint.

XTTS V2 is natively capable of streaming real-time TTS. We just need to build an API endpoint that supports this feature.

The model server, [implemented in the Truss](https://github.com/basetenlabs/truss-examples/tree/main/xtts-streaming) as `model.py`, is nearly a hundred lines of Python, so we won’t go through it line by line. Instead, we’ll take a look at the most relevant parts of the code.

When the model server is initialized, we need to load the model weights onto the GPU with the correct configuration. This is handled by the `load()` function.

python

```
def load(self):
    device = "cuda"
    model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    config = XttsConfig()
    config.load_json(os.path.join(model_path, "config.json"))
    self.model = Xtts.init_from_config(config)
    self.model.load_checkpoint(config, checkpoint_dir=model_path, eval=True)
    self.model.to(device)
```
To ensure [inference](https://www.baseten.co/blog/ai-inference-explained/) remains fast, we also set the speaker at load time.

```
self.speaker = {
    "speaker_embedding": self.model.speaker_manager.speakers[SPEAKER_NAME][
        "speaker_embedding"
    ]
    .cpu()
    .squeeze()
    .half()
    .tolist(),
    "gpt_cond_latent": self.model.speaker_manager.speakers[SPEAKER_NAME][
        "gpt_cond_latent"
    ]
    .cpu()
    .squeeze()
    .half()
    .tolist(),
}
```
For inference, we run the `predict()` function within the Truss. This function passes the input text into the model for narration. We use XTTS V2’s built-in `inference_stream()` function to receive streaming output from the model.

```
def predict(self, model_input):
    text = model_input.get("text")
    language = model_input.get("language", "en")
    chunk_size = int(
        model_input.get("chunk_size", 150)
    )  # Ensure chunk_size is an integer
    add_wav_header = False
    streamer = self.model.inference_stream(
        text,
        language,
        gpt_cond_latent,
        speaker_embedding,
        stream_chunk_size=chunk_size,
        enable_text_splitting=True,
    )
```
To pass that output back to the user, we yield bytes as chunks become available.

```
for chunk in streamer:
    processed_chunk = self.wav_postprocess(chunk)
    processed_bytes = processed_chunk.tobytes()
    yield processed_bytes
```
These bytes correspond to chunks of audio in a wav format and can be decoded on the client, as we’ll demonstrate below.

This model server enables a \~200 millisecond round trip time to first chunk, of which less than 100 milliseconds is spent on inference. When deployed on an inexpensive T4 GPU, the model offers production-ready performance.

Before deployment, set GPU resources in `config.yaml` to use the least expensive available T4 instance:

yaml

```
resources:
  accelerator: T4
  cpu: '3'
  memory: 10Gi
  use_gpu: true
```
Once the model server is fully implemented with Truss, it’s time to deploy to production. To deploy the real-time TTS streaming endpoint, run:

`truss push`
This will create a development deployment of your model on Baseten. The development deployment has scale to zero (so your deployment will automatically spin down when not in use) and live reload (so you can quickly make changes to your model deployment). However, it has limited autoscaling capabilities and is not designed for production use. You can learn more about the model lifecycle in the documentation.

How you consume the model output depends on your application. You can use this model to power any application. For this tutorial, we’ll just stream the audio with a quick Python script.

To play the model output, you’ll need to [install ffmpeg](https://ffmpeg.org/download.html). On Mac, we recommend getting the package with:

`brew install ffmpeg`
From there, create a file `call.py` and paste the following invocation code:

```
import subprocess
import sys
import os
from typing import Iterator
import time
import requests
text_to_read = """
All the world's a stage, and all the men and women merely players:
they have their exits and their entrances; and one man in his time
plays many parts, his acts being seven ages.
"""
def tts() -> Iterator[bytes]:
    model_id = "" # Paste model ID here
    baseten_api_key = os.environ["BASETEN_API_KEY"]
    start = time.perf_counter()
    res = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={"text": text_to_read, "chunk_size": 20},
        stream=True,
    )
    end = time.perf_counter()
    print(f"Time to make POST: {end-start}s", file=sys.stderr)
    if res.status_code != 200:
        print("Error:", res.text)
        sys.exit(1)
    first = True
    for chunk in res.iter_content(chunk_size=512):
        if first:
            end = time.perf_counter()
            print(f"Time to first chunk: {end-start}s", file=sys.stderr)
            first = False
        if chunk:
            yield chunk
    print("⏱️ response.elapsed:", res.elapsed)
def stream_ffplay(audio_stream, output_file=None):
    if output_file is None:
        ffplay_cmd = ["ffplay", "-nodisp", "-autoexit", '-f', 's16le', '-ar', '24000', '-ac', '1', "-"]
    else:
        print("Saving to", output_file)
        ffplay_cmd = ["ffmpeg", "-y", "-f", "wav", "-i", "-", output_file]
    with subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE) as ffplay_proc:
        try:
            for chunk in audio_stream:
                ffplay_proc.stdin.write(chunk)
        except BrokenPipeError:
            pass  # Handle the case where ffplay ends prematurely
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            ffplay_proc.stdin.close()
            ffplay_proc.wait()
stream_ffplay(tts(),None)
```
Before calling the model, make sure to:

1. Paste your `model_id` (see image below) into the sample code.
2. Ensure your Baseten API key is saves as the environment variable `BASETEN_API_KEY`.

You can add any text to the `text_to_read` variable, then call the model with:

`python call.py`
In moments, your real-time TTS narration will begin playing. Make sure you have your volume on!
