---
title: 'Zero to real-time text-to-speech: The complete Orpheus + WebSockets tutorial'
kind: blog
topic: inference
subtopic: serving
secondary_topics:
- product-engineering/case-studies
summary: Walks through streaming text-to-speech with the open-source Orpheus TTS model
  over a persistent WebSocket connection on Baseten, avoiding per-request HTTP connection
  overhead for real-time audio generation.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/zero-to-real-time-text-to-speech-the-complete-orpheus-websockets-tutorial
author: Alex Ker
published: '2025-08-08'
fetched: '2026-11-12T06:10:16Z'
classifier: claude
taxonomy_rev: 2
words: 848
content_sha256: 0ad8c9b5aad9489f108d8d2b8289b09513ab5cbf60559dcbf5e844dde41d1535
---

# Zero to real-time text-to-speech: The complete Orpheus + WebSockets tutorial

AI engineering
# Zero to real-time text-to-speech: The complete Orpheus + WebSockets tutorial

Orpheus is a leading open-source TTS model. Use WebSockets with Orpheus to stream text in and audio out.


- Authors
- Date
- August 8, 2025

[Orpheus](https://github.com/canopyai/Orpheus-TTS/tree/main) is an open-source text-to-speech model released by Canopy Labs. In this post, we'll provide a quick overview of why WebSockets make sense for real-time text to speech and walk through a complete implementation example on Baseten you can adopt in any application today.

Traditional HTTP request-based inference creates significant friction for streaming applications due to connection overhead and latency. WebSockets navigates around this by maintaining a persistent, bidirectional connection between the server and client, enabling seamless real-time communication. Rather than requiring headers and new connections for each request, WebSockets establish a single channel for continuous data exchange.

This makes Websockets ideal for real-time applications such as voice-enabled customer support, language translation, or interactive voice assistants for accessibility; clients can stream audio chunks while simultaneously receiving transcription results without interruption.

Let’s step through a code example of how to stream text from the Baseten Orpheus endpoint to audio that can play aloud.

Baseten created a custom implementation of Orpheus with support for streaming over WebSockets. [Start by deploying this implementation from the model library.](https://www.baseten.co/library/orpheus-tts/)

After the model appears in your account, save the Baseten model ID and generate a Baseten API key if you don’t already have one.

Then, create a Baseten API key from the [API keys page](https://app.baseten.co/settings/api_keys) and save it as an environment variable

`export BASETEN_API_KEY=my_api_key`

While Orpheus starts up on Baseten, let’s understand the code we will run that plays the text in audio that we receive from the endpoint.

We first need to install the required packages required for using websockets, capturing audio, and converting data. You can paste this into your terminal:

`pip install pyaudio aiohttp` 

We expect you to set the Baseten API Key you grabbed from Step 1 as the `$BASETEN_API_KEY` environment variable. And you can now paste in the model ID for the deployed Orpheus model into the `MODEL_ID` variable. We also set parameters we want for streaming.

python

```
import os, json, asyncio
import urllib3
import pyaudiofrom aiohttp 
import ClientSession, WSMsgType
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("BASETEN_API_KEY")
MODEL_ID = "BASETEN_MODEL_ID"
WS_URL = f"wss://model-{MODEL_ID}.api.baseten.co/environments/production/websocket"
VOICE       = "tara"    
MAX_TOKENS  = 2000
BUFFER_SIZE = 5         # words / chunk
SAMPLE_RATE = 24000     # audio quality (24kHz)
WIDTH       = pyaudio.paInt16
CHANNELS    = 1
```
Now this is the main utility function, `stream_tts`, where we first open up a speaker output stream with a `pyaudio` object. Then we connect to the website with the appropriate headers for authentication, and send the metadata we set above.

```
async def stream_tts(text: str):   
  pa = pyaudio.PyAudio()   
  stream = pa.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, output=True)   
  
  headers = {"Authorization": f"Api-Key {API_KEY}"}   
  print(f"🔗 Connecting to WebSocket: {WS_URL}")   
  async with ClientSession(headers=headers) as sess:       
    try:           
      async with sess.ws_connect(WS_URL) as ws:               
        print("✅ WS connected")               
        # send metadata once               
        await ws.send_json({                   
          "voice": VOICE,                   
          "max_tokens": MAX_TOKENS,                   
          "buffer_size": BUFFER_SIZE,               
        })               
        print("📤 metadata sent")
```
We also define an asynchronous audio `receiver` function that continuously listens for audio data from the server. When the WebSocket receives audio bytes from the Orpheus endpoint, the data is played immediately by writing to the stream we opened above with `pyaudio` through your computer speaker.

Since the WebSocket is a bi-direction channel, we can also send words in the for loop, and we have sent some sample words for Orpheus to turn into audio below.

```
               ...
               # start audio receiver
               async def receiver():                   
                 async for msg in ws:                       
                   if msg.type == WSMsgType.BINARY:                           
                     print(f"⏯️  playing {len(msg.data)} bytes")                           
                     stream.write(msg.data)                       
                   elif msg.type in (WSMsgType.CLOSE, WSMsgType.CLOSED):                           
                     print("🔒 server closed")                           
                     return               
                     
                recv = asyncio.create_task(receiver())               
                
                # send words               
                for w in text.strip().split():                   
                  await ws.send_str(w)               
                print("📤 words sent")               
                
                # signal end-of-text               
                await ws.send_str("__END__")               
                print("📤 END sentinel sent — waiting for audio")               
                
                # wait until server closes               
                await recv       
            except Exception as e:           
              print(f"❌ Connection error: {e}")   
          stream.stop_stream()   
          stream.close()   
          pa.terminate()   
          print("🎉 done")
     if __name__ == "__main__":   
        sample = (       
          "Nothing beside remains. Round the decay of that colossal wreck, "       
          "boundless and bare, The lone and level sands stretch far away."   
        )     
        async def main():       
          # run TTS       
          await stream_tts(sample)     
        asyncio.run(main())
```
Go into the terminal, paste in all the parts of the code and run `python call.py.` You will now hear the text dictated realistically through your computer speaker.

To recap, we showed how to run real-time speech-to-text via WebSockets that concurrently send text data and receive audio data from a Baseten production-grade Orpheus endpoint. We can’t wait to see what you build.

You can run real-time speech-to-text via WebSockets that concurrently send text data and receive audio data from our [Orpheus implementation](https://www.baseten.co/library/orpheus-tts/). With WebSockets, each user maintains a connection with the server for the entire duration of their session. In production, it’s important to set [appropriate autoscaling settings](https://docs.baseten.co/deployment/autoscaling#autoscaling) so that you can support more concurrent users as the number of active connections grows.

Whatever text you want to turn into speech, run it on Baseten with production-grade real-time text-to-speech inference with Whisper V3 on WebSockets without worry.
