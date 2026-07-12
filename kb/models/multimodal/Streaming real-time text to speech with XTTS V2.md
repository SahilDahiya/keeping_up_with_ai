---
title: Streaming real-time text to speech with XTTS V2
topic: models
subtopic: multimodal
secondary_topics:
- inference/serving
summary: Covers streaming real-time text-to-speech serving with XTTS v2.
source: baseten
url: https://www.baseten.co/blog/streaming-real-time-text-to-speech-with-xtts-v2/
author: Het Trivedi; Philip Kiely
published: '2024-04-18'
fetched: '2026-07-11T04:09:45Z'
classifier: codex
taxonomy_rev: 1
words: 1367
content_sha256: c784a61922430b6cd2086d5f63feaaefbc7b0e55bce7ff4bc79ed18b7ab6b414
triage: keep
skip_reason: null
---

# Streaming real-time text to speech with XTTS V2

![Streaming TTS](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747441444-stream-tts.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

In this tutorial, we [deploy a streaming endpoint for XTTS V2](https://github.com/basetenlabs/truss-examples/tree/main/xtts-streaming), a state of the art open source text to speech model with voice cloning capabilities. The streaming endpoint has a total round-trip time to first chunk of as little as 200 milliseconds and delivers near real-time audio playback for a given text  — making it an ideal example of a real-time TTS deployment in action.

A text to speech model (or speech synthesis model) is a type of generative AI model that creates a natural, humanlike narration of a text input. A strong text to speech model lets you turn any book into an audiobook or any article into a podcast. But with streaming TTS output, text to speech models can power an entire new class of AI applications.

When you chat with an LLM, the model starts responding as soon as the first characters of output are ready rather than making you wait for it to write the entire reply. With an optimized LLM deployment, you can get that time to first token below a couple hundred milliseconds, making the chat feel instant.

You can do the same for text to speech models. Streaming audio output in real-time TTS mode with super-fast (~200ms) time to first chunk unlocks massive use cases across conversational user interfaces.

In this tutorial, we’ll build a streaming real-time TTS endpoint for XTTS 2, a realistic text to speech model with support for over a dozen languages.

![Video](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fimage.mux.com%2Fmup2IgMz7vVt2qBpGjnTeOI8HuDSJhOc%2Fthumbnail.jpg&w=3840&q=75)

## Why streaming TTS works with XTTS V2

XTTS V2 is a high-quality open source model that takes in text and, optionally, a voice sample as input and converts the text to an audio recording of the spoken text in the chosen voice. It only needs a six-second audio sample for voice cloning and is capable of generating speech in 17 languages.

Like an LLM, text to speech models like XTTS V2 are autoregressive models that work in tokens. The input text is tokenized and passed to the speech synthesis model, which iterates over the input to produce audio chunks.

In a minute, a person speaking in English can generally say 120 to 150 words, which can be as much as 200 tokens for token-based AI models. On an inexpensive T4 GPU, XTTS V2 can easily synthesize enough tokens of speech for real-time TTS output.

By default, XTTS V2 returns the entire spoken text as a single response. Instead, we can implement a model server that streams output as it is generated, enabling near real-time TTS narration.

## Prerequisites and quick start

Before following this tutorial, please make sure to:

- [Create a Baseten account](https://app.baseten.co/signup/?next=/)or sign in to your existing account.
- Create an - [API key](https://docs.baseten.co/observability/api-keys)and copy it someplace safe, you’ll need it for two future steps.
- Install Truss, Baseten’s open source model packaging framework, with - `pip install truss`.

To download and deploy an out-of-the-box implementation of the XTTS V2 streaming endpoint, run:

```
git clone https://github.com/basetenlabs/truss-examples/
cd xtts-streaming
truss push
```
Provide your API key when prompted during `truss push`. Follow along below for detailed instructions on building and deploying the endpoint.

## Building a streaming endpoint

XTTS V2 is natively capable of streaming real-time TTS. We just need to build an API endpoint that supports this feature.

The model server, [implemented in the Truss](https://github.com/basetenlabs/truss-examples/tree/main/xtts-streaming) as `model.py`, is nearly a hundred lines of Python, so we won’t go through it line by line. Instead, we’ll take a look at the most relevant parts of the code.

When the model server is initialized, we need to load the model weights onto the GPU with the correct configuration. This is handled by the `load()` function.

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
1self.speaker = {
2    "speaker_embedding": self.model.speaker_manager.speakers[SPEAKER_NAME][
3        "speaker_embedding"
4    ]
5    .cpu()
6    .squeeze()
7    .half()
8    .tolist(),
9    "gpt_cond_latent": self.model.speaker_manager.speakers[SPEAKER_NAME][
10        "gpt_cond_latent"
11    ]
12    .cpu()
13    .squeeze()
14    .half()
15    .tolist(),
16}
```
For inference, we run the `predict()` function within the Truss. This function passes the input text into the model for narration. We use XTTS V2’s built-in `inference_stream()` function to receive streaming output from the model.

```
1def predict(self, model_input):
2    text = model_input.get("text")
3    language = model_input.get("language", "en")
4    chunk_size = int(
5        model_input.get("chunk_size", 150)
6    )  # Ensure chunk_size is an integer
7    add_wav_header = False
8
9    streamer = self.model.inference_stream(
10        text,
11        language,
12        gpt_cond_latent,
13        speaker_embedding,
14        stream_chunk_size=chunk_size,
15        enable_text_splitting=True,
16    )
```
To pass that output back to the user, we yield bytes as chunks become available.

```
for chunk in streamer:
    processed_chunk = self.wav_postprocess(chunk)
    processed_bytes = processed_chunk.tobytes()
    yield processed_bytes
```
These bytes correspond to chunks of audio in a wav format and can be decoded on the client, as we’ll demonstrate below.

This model server enables a ~200 millisecond round trip time to first chunk, of which less than 100 milliseconds is spent on inference. When deployed on an inexpensive T4 GPU, the model offers production-ready performance.

Before deployment, set GPU resources in `config.yaml` to use the least expensive available T4 instance:

```
resources:
  accelerator: T4
  cpu: '3'
  memory: 10Gi
  use_gpu: true
```
## Deploying XTTS V2 to production

Once the model server is fully implemented with Truss, it’s time to deploy to production. To deploy the real-time TTS streaming endpoint, run:

`truss push`This will create a development deployment of your model on Baseten. The development deployment has scale to zero (so your deployment will automatically spin down when not in use) and live reload (so you can quickly make changes to your model deployment). However, it has limited autoscaling capabilities and is not designed for production use. You can learn more about the [model lifecycle in the documentation](https://docs.baseten.co/deploy/lifecycle).

## Consuming streaming output

How you consume the model output depends on your application. You can use this model to power any application. For this tutorial, we’ll just stream the audio with a quick Python script.

To play the model output, you’ll need to [install ffmpeg](https://ffmpeg.org/download.html). On Mac, we recommend getting the package with:

`brew install ffmpeg`From there, create a file `call.py` and paste the following invocation code:

```
1
2import subprocess
3import sys
4import os
5from typing import Iterator
6import time
7import requests
8
9
10text_to_read = """
11All the world's a stage, and all the men and women merely players:
12they have their exits and their entrances; and one man in his time
13plays many parts, his acts being seven ages.
14"""
15
16
17def tts() -> Iterator[bytes]:
18
19    model_id = "" # Paste model ID here
20    baseten_api_key = os.environ["BASETEN_API_KEY"]
21
22    start = time.perf_counter()
23    res = requests.post(
24        f"https://model-{model_id}.api.baseten.co/development/predict",
25        headers={"Authorization": f"Api-Key {baseten_api_key}"},
26        json={"text": text_to_read, "chunk_size": 20},
27        stream=True,
28    )
29    end = time.perf_counter()
30    print(f"Time to make POST: {end-start}s", file=sys.stderr)
31
32    if res.status_code != 200:
33        print("Error:", res.text)
34        sys.exit(1)
35
36    first = True
37    for chunk in res.iter_content(chunk_size=512):
38        if first:
39            end = time.perf_counter()
40            print(f"Time to first chunk: {end-start}s", file=sys.stderr)
41            first = False
42        if chunk:
43            yield chunk
44
45    print("⏱️ response.elapsed:", res.elapsed)
46
47def stream_ffplay(audio_stream, output_file=None):
48    if output_file is None:
49        ffplay_cmd = ["ffplay", "-nodisp", "-autoexit", '-f', 's16le', '-ar', '24000', '-ac', '1', "-"]
50    else:
51        print("Saving to", output_file)
52        ffplay_cmd = ["ffmpeg", "-y", "-f", "wav", "-i", "-", output_file]
53
54    with subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE) as ffplay_proc:
55        try:
56            for chunk in audio_stream:
57                ffplay_proc.stdin.write(chunk)
58
59        except BrokenPipeError:
60            pass  # Handle the case where ffplay ends prematurely
61        except Exception as e:
62            print(f"Unexpected error: {e}")
63        finally:
64            ffplay_proc.stdin.close()
65            ffplay_proc.wait()
66
67stream_ffplay(tts(),None)
```
Before calling the model, make sure to:

- Paste your - `model_id`(see image below) into the sample code.
- Ensure your Baseten API key is saves as the environment variable - `BASETEN_API_KEY`.

![Find your model ID in on the model overview tab](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1713393852-screenshot-2024-04-16-at-8-42-05-am.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

You can add any text to the `text_to_read` variable, then call the model with:

`python call.py`In moments, your real-time TTS narration will begin playing. Make sure you have your volume on!
