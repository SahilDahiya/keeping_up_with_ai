---
title: 'Zero to real-time transcription: The complete Whisper V3 streaming tutorial'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/zero-to-real-time-transcription-the-complete-whisper-v3-websockets-tutorial
author: Alex Ker
published: '2025-07-28'
fetched: '2026-11-12T06:10:12Z'
classifier: null
taxonomy_rev: 2
words: 869
content_sha256: c63fb05b78404547556efdf917c88bb7c113c4181d302df50328241963a78ccb
---

# Zero to real-time transcription: The complete Whisper V3 streaming tutorial

AI engineering
# Zero to real-time transcription: The complete Whisper V3 streaming tutorial

Whisper V3 is a leading open-source audio transcription model for speech-to-text use cases. Use WebSockets with Whisper to stream audio in and text out.


- Authors
- Date
- July 28, 2025

Whisper is a leading open-source transcription model released by OpenAI. In this post, we'll provide a quick overview of why WebSockets make sense for real-time speech transcription through Whisper V3 and walk through a complete implementation example on Baseten.

Traditional HTTP request-based inference creates significant friction for streaming applications due to connection overhead and latency. WebSockets navigates around this by maintaining a persistent, bidirectional connection between the server and client, enabling seamless real-time communication. Rather than requiring headers and new connections for each request, WebSockets establish a single channel for continuous data exchange.

This makes WebSockets ideal for real-time applications like AI transcription, live phone calls, and agentic interactions; clients can stream audio chunks while simultaneously receiving transcription results without interruption.

Let’s step through a code example of how to stream from your laptop microphone and get your voice transcribed in real-time, which is adaptable to any production web application with a Python backend.

Baseten created a custom implementation of Whisper with support for streaming over WebSockets. Start by deploying this implementation from the model library.

After the model appears in your account, save the Baseten model ID and generate a Baseten API key if you don’t already have one.

Then, create a Baseten API key from the [API keys page](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

`export BASETEN_API_KEY=my_api_key`
Let’s understand the code we will run to transcribe our voice. You can find the complete code here, so you don’t need to worry about copy-pasting the following code chunks.

We first need to install the required packages for using WebSockets, capturing audio, and converting data. You can paste this into your terminal:

`pip install websockets sounddevice numpy`
You can now paste in the model ID for the deployed Whisper model into the `model_id` variable. We also set metadata for our transcription that will be passed to the endpoint initially.

python

```
import asyncio
import websockets
import sounddevice as sd
import numpy as np
import json
import os
# Audio config
SAMPLE_RATE = 16000
CHUNK_SIZE = 512
CHUNK_DURATION = CHUNK_SIZE / SAMPLE_RATE
CHANNELS = 1
headers = {"Authorization": f"Api-Key {os.getenv('BASETEN_API_KEY')}"}
model_id = "BASETEN_MODEL_ID"
metadata = {
    "whisper_params": {
        "audio_language": "en",
        "show_word_timestamps": True,
    },
    "streaming_params": {
        "encoding": "pcm_s16le",
        "sample_rate": 16000,
        "enable_partial_transcripts": True,
        "partial_transcript_interval_s": 1.0,
        "final_transcript_max_duration_s": 30,
    },
    "streaming_vad_config": {
        "threshold": 0.5,
        "min_silence_duration_ms": 300,
        "speech_pad_ms": 30,
    },
}
```
Now this is the meat of the code. We will break this down section by section. We start an asynchronous event loop, connect to the Whisper server running Baseten with `.connect`, and send the configurations of Whisper via metadata.

```
async def stream_microphone_audio(ws_url):
    loop = asyncio.get_running_loop()
    async with websockets.connect(ws_url, additional_headers=headers) as ws:
        print("Connected to server")
        await ws.send(json.dumps(metadata))
        print("Sent metadata to server")
```
We initialize a queue for the audio data and create a callback function that triggers when the microphone captures audio, converting the input data into 16-bit integers and putting this final data form into the queue in a threadsafe way for sending. This queue acts as a buffer between the real-time audio capture and the WebSocket transmission, allowing the two processes to run independently.

```
send_queue = asyncio.Queue()
def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"Audio warning: {status}")
    int16_data = (indata * 32767).astype(np.int16).tobytes()
    loop.call_soon_threadsafe(send_queue.put_nowait, int16_data)
```
We start the input stream with `sounddevice` and the with keyword, Python’s context manager for graceful cleanup.

```
with sd.InputStream(
    samplerate=SAMPLE_RATE,
    blocksize=CHUNK_SIZE,
    channels=CHANNELS,
    dtype="float32",
    callback=audio_callback,
):
    print("Streaming mic audio...")
```
Inside it, we define two async functions. `send_audio` continuously checks the queue for new audio, sending to the server in chunks indefinitely. `recieve_server_messages` continuously receives transcribed text from the WebSocket and prints. We also use asyncio.gather to keep both async functions running concurrently.

```
async def send_audio():
    while True:
        chunk = await send_queue.get()
        await ws.send(chunk)
async def receive_server_messages():
    while True:
        response = await ws.recv()
        try:
            message = json.loads(response)
            is_final = message.get("is_final")
            transcript = message.get("transcript")
            if not is_final:
                print(f"[partial] {transcript}")
            elif is_final:
                print(f"[final] {transcript}")
            else:
                print(f"[unknown type] {message}")
        except Exception as e:
            print("Non-JSON message or parse error:", response, "| Error:", str(e))
        # Run send + receive tasks concurrently
        await asyncio.gather(send_audio(), receive_server_messages())
ws_url = f"wss://model-{model_id}.api.baseten.co/environments/production/websocket"
asyncio.run(stream_microphone_audio(ws_url))
```
This example uses a truss deployment. If you're using a chain deployment, replace `model_id` with your chain ID and use the chain URL format instead: `wss://chain-{chain_id}.api.baseten.co/environments/production/websocket`

Go into the terminal, paste in all the parts of the code, and run `python websocket.py`. Start talking into the mic and you can view the partial transcriptions being sent back to you in real time!

You can run real-time transcription with Whisper by concurrently sending audio data and receiving text data from an endpoint with our streaming Whisper implementation. With WebSockets, each user maintains a connection with the server for the entire duration of their session. In production, it’s important to set [appropriate autoscaling settings](https://docs.baseten.co/deployment/autoscaling#autoscaling) so that you can support more concurrent users as the number of active connections grows.

Whatever you’re transcribing, run it on Baseten with production-grade real-time speech-to-text inference with Whisper V3 on WebSockets.
