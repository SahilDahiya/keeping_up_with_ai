---
title: Reachy Mini goes fully local
kind: blog
topic: infra-platform
subtopic: edge
secondary_topics:
- inference/serving
summary: Runs a full cascaded voice stack (VAD -> STT -> LLM -> TTS) locally on-device
  behind an OpenAI-Realtime-API-compatible /v1/realtime WebSocket, replacing the cloud
  backend for the Reachy Mini robot; argues cascades beat end-to-end S2S models on
  flexibility and latency and shows which local components to swap in.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/local-reachy-mini-conversation
author: Amir Mahla; Andres Marafioti
published: '2026-05-27'
fetched: '2026-07-14T22:03:35Z'
classifier: claude
taxonomy_rev: 1
words: 1808
content_sha256: 2c7c5501886c8966a48f0257cfdc745d6a6390657fb5c2b18b142fa08568b764
---

# Reachy Mini goes fully local

# 
	[
		
	](https://huggingface.co#reachy-mini-goes-fully-local)
	
		Reachy Mini goes fully local
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/local-reachy-mini-conversation.md)

[  Upvote 66 ](https://huggingface.co/login?next=%2Fblog%2Flocal-reachy-mini-conversation)

![Amir Mahla's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/67f2f500e329a81a62a05d44/DOlzc8GFQzrnfVrsOdtbN.png) 

  ![Andres Marafioti's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/65d66b494bbd0d92b641cdbb/6-7dm7B-JxcoS1QlCPdMN.jpeg) 

  [conversation app](https://github.com/pollen-robotics/reachy_mini_conversation_app)and start talking to it. Until now, you had to send your audio to a server. But not anymore. Today we'll walk you through running the whole stack locally.

This stack is powered by [ speech-to-speech](https://github.com/huggingface/speech-to-speech), our cascaded VAD → STT → LLM → TTS pipeline that exposes a Realtime API-compatible 

`/v1/realtime` WebSocket. Once you launch the backend, point the robot at it from the UI.Cascades are the most flexible option in the open-source landscape today, and with the right pieces they're also the fastest. We'll recommend the components we like best, but the whole point of a cascade is that you can swap them. New models drop every week.


TL;DR

- Deploy a local speech backend for your Reachy Mini.
- We use our
`speech-to-speech`library, a cascade approach.- Recommended:
llama.cppwithGemma 4,Silero VAD,Parakeet-TDT 0.6B v3 STT,Qwen3-TTS.

## 
	[
		
	](https://huggingface.co#quick-start)
	
		Quick start
	

This blog walks you through running conversations with Reachy Mini fully locally. No cloud, no API keys, no data leaving your machine. Here's a video showing this live:

### 
	[
		
	](https://huggingface.co#locally-serving-the-llm)
	
		Locally serving the LLM
	

To serve the LLM, we'll use Hugging Face's `llama.cpp`. If you need to install it, the simplest way is `brew install llama.cpp` or `winget install llama.cpp`, for more help, [check the docs](https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md).
First, we'll run:

```
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF -np 2 -c 65536 -fa on --swa-full
```
And done! The first time it will download the model, subsequent launches are fast.

## What do those flags do?

- `-hf ggml-org/gemma-4-E4B-it-GGUF`— pulls the model straight from the Hub. First run downloads it, subsequent runs use the cache.
- `-np 2`— two parallel slots. Lets the server handle a second request (e.g. a quick interruption) without blocking on the first.
- `-c 65536`— 64k context window, shared across slots. Plenty of headroom for long conversations.
- `-fa on`— flash attention. Faster and lower memory, basically free on modern hardware.
- `--swa-full`— keeps the full sliding-window attention cache instead of recomputing it. Trades a bit of RAM for noticeably faster prompt processing on Gemma.

### 
	[
		
	](https://huggingface.co#setting-up-speech-to-speech)
	
		Setting up speech-to-speech
	

We'll begin by simply installing the library

```
uv pip install speech-to-speech
```
Then, while we are serving the LLM in another terminal, we can simply run:

```
speech-to-speech --responses_api_base_url "http://127.0.0.1:8080" --responses_api_api_key "" --mode local
```
And you can start talking to the model through your terminal! The first time it will need to download Parakeet-TDT 0.6B v3 and Qwen3TTS, but subsequent launches are fast.

Here's a video showing the local conversation mode:

Now, after you've tried it in `--mode local`, you can run again the command without that option to serve speech-to-speech to the robot.

### 
	[
		
	](https://huggingface.co#connecting-reachy-mini-to-speech-to-speech)
	
		Connecting Reachy Mini to speech-to-speech
	

Once you have llama.cpp and speech-to-speech running, you can start the robot with the desktop app and launch the conversation app. In the UI from the conversation app, you need to choose the local mode by clicking on "edit connection" in the HF backend. Here's a video showing how to do it:

And you're done. You can start talking to your robot. Every stage of the pipeline is a trade-off: there are faster TTS models with lower quality, slower STT models with higher quality. We optimized for multilingual, you might want to optimize for a single language. The rest of the blog covers how to customize.

## 
	[
		
	](https://huggingface.co#going-deeper)
	
		Going deeper
	

### 
	[
		
	](https://huggingface.co#why-run-your-own-speech-to-speech-server)
	
		Why run your own Speech-to-Speech server?
	

Hosted realtime backends are convenient, but running your own engine unlocks three things:

- **Privacy.**Audio never leaves your network, the entire pipeline runs on hardware you control.
- **No API costs.**No per-minute or per-token fees.
- **Full control over the pipeline.**Swap any piece: VAD, STT, LLM, TTS. Whenever something better lands on the Hub 🤗.

The `speech-to-speech` repo gives you all of that in a single CLI. It boots a WebSocket server at `/v1/realtime` that speaks the same protocol Reachy Mini already knows how to talk to.

### 
	[
		
	](https://huggingface.co#our-opinionated-defaults-vad-stt-tts)
	
		Our opinionated defaults: VAD, STT, TTS
	

A cascaded voice pipeline has four stages: VAD, STT, LLM, and TTS. For three of them, we pick solid defaults so you can focus on the LLM:

| Stage | Choice | Why | 
|---|---|---|
| VAD | Silero VAD v5 | Tiny, accurate, runs on CPU. The de-facto default in the open-source voice-agent world. | 
| STT | Parakeet-TDT 0.6B v3 | Streaming-friendly, very fast, great quality on English. | 
| TTS | Qwen3-TTS | Expressive, low-latency, multilingual, supports custom voices. | 

We are opinionated about these choices, feel free to swap them out for your own if you have a preference.

### 
	[
		
	](https://huggingface.co#choosing-your-llm)
	
		Choosing your LLM
	

The LLM is the layer with the most impact on latency and overall performance of the system. We support two options: **run a model locally** (llama.cpp, MLX, Transformers, vLLM), or **use a server with a Responses API** (OpenAI, Gemini, HF Inference Endpoints, llama.cpp, vLLM, etc).

#### 
	[
		
	](https://huggingface.co#the-responses-api-decouple-the-brain-from-the-voice-loop)
	
		The Responses API: decouple the brain from the voice loop
	

The main bottleneck in the system is LLM inference latency. To address that, we support external inference engines exposed through the Responses API protocol.

The `speech-to-speech` engine therefore supports a second mode where the LLM lives in a separate process as long as it speaks the Responses API protocol. You launch your model server in one terminal, you launch the voice loop in another terminal, and the two talk over HTTP.

##### 
	[
		
	](https://huggingface.co#option-1-llamacpp-in-one-terminal-speech-to-speech-in-the-other)
	
		Option 1: llama.cpp in one terminal, speech-to-speech in the other
	

**Terminal 1: llama.cpp server:**

```
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF -np 2 -c 65536 -fa on --swa-full
```
**Terminal 2: speech-to-speech client:**

```
speech-to-speech \
  --mode realtime \
  --stt parakeet-tdt \
  --tts qwen3 \
  --llm_backend responses-api \
  --model_name "ggml-org/gemma-4-E4B-it-GGUF" \
  --responses_api_base_url "http://127.0.0.1:8080/v1"
```
##### 
	[
		
	](https://huggingface.co#option-2-vllm-in-one-terminal-speech-to-speech-in-the-other)
	
		Option 2: vLLM in one terminal, speech-to-speech in the other
	


Requires vLLM ≥ 0.21.0.Full support for the Responses API protocol, including tool-call streaming used by the speech-to-speech backend, landed in vLLM 0.21.0. Older versions will boot but trip up as soon as the assistant tries to call a tool.

When serving a model through vLLM for this pipeline, three flags are effectively required:

- `--enable-auto-tool-choice`
- `--tool-call-parser <tool_parser_name>`— picks the per-family parser that turns the model's raw output into structured tool calls (e.g.- `qwen3_coder`for Qwen3 instruct models,- `llama3_json`for Llama 3,- `hermes`for Hermes-style models, ...).
- `--default-chat-template-kwargs '{"enable_thinking":false}'`: disables the- `<think>`reasoning channel for models that support it. For harder agentic tasks you can flip this to- `true`and let the model reason, but for a natural-feeling conversation we strongly recommend keeping it off: every thinking token is latency the user hears as silence before the robot starts speaking.

**Terminal 1: vLLM inference server ( Qwen/Qwen3-4B-Instruct-2507):**

```
vllm serve Qwen/Qwen3-4B-Instruct-2507 \
  --port 8000 \
  --host 127.0.0.1 \
  --max-model-len 32768 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --default-chat-template-kwargs '{"enable_thinking":false}' \
  --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":1}'
```
The

`--speculative-config`line enables Multi-Token Prediction (MTP). It isoptional, but it has a great impact on end-to-end latency. Leave it on whenever the model supports it.

**Terminal 2: speech-to-speech client:**

```
speech-to-speech \
  --mode realtime \
  --stt parakeet-tdt \
  --tts qwen3 \
  --llm_backend responses-api \
  --model_name "Qwen/Qwen3-4B-Instruct-2507" \
  --responses_api_base_url "http://127.0.0.1:8000/v1"
```
##### 
	[
		
	](https://huggingface.co#option-3-hugging-face-inference-endpoints)
	
		Option 3: Hugging Face Inference Endpoints
	

Same protocol, but the model runs on a managed GPU on Hugging Face. Deploy any chat model as an Inference Endpoint, then point the voice loop at the endpoint URL:

```
speech-to-speech \
  --mode realtime \
  --stt parakeet-tdt \
  --tts qwen3 \
  --llm_backend responses-api \
  --model_name "Qwen/Qwen3-4B-Instruct-2507" \
  --responses_api_base_url "https://<your-endpoint>.endpoints.huggingface.cloud/v1" \
  --responses_api_api_key "$HF_TOKEN"
```
##### 
	[
		
	](https://huggingface.co#option-4-hugging-face-inference-providers)
	
		Option 4: Hugging Face Inference Providers
	

If you don't want to manage your own endpoint, use an [Inference Provider](https://huggingface.co/docs/inference-providers). Hugging Face routes your request to a third-party backend (e.g. Together, Fireworks, Replicate) with a single URL:

```
speech-to-speech \
  --mode realtime \
  --stt parakeet-tdt \
  --tts qwen3 \
  --llm_backend responses-api \
  --model_name "Qwen/Qwen3.6-35B-A3B:deepinfra" \
  --responses_api_base_url "https://router.huggingface.co/v1" \
  --responses_api_api_key "$HF_TOKEN"
```
##### 
	[
		
	](https://huggingface.co#option-5-openai-or-any-openai-compatible-provider)
	
		Option 5: OpenAI (or any OpenAI-compatible provider)
	

When you want to test against a frontier model with zero infra, point the same flag at OpenAI:

```
speech-to-speech \
  --mode realtime \
  --stt parakeet-tdt \
  --tts qwen3 \
  --llm_backend responses-api \
  --model_name "gpt-5.4" \
  --responses_api_api_key "$OPENAI_API_KEY"
```
The `--responses_api_*` flags work the same for any provider that implements the protocol (OpenRouter, Together, Fireworks, …). Swap the base URL and the API key, keep the rest of the pipeline identical.

#### 
	[
		
	](https://huggingface.co#running-the-llm-in-process)
	
		Running the LLM in-process
	

##### 
	[
		
	](https://huggingface.co#option-1-local-llm-on-mlx-apple-silicon)
	
		Option 1: Local LLM on MLX (Apple Silicon)
	

If you are on a Mac, MLX is the lowest-friction way to run a real model with sane latency. We recommend **Qwen3-4B-Instruct-2507**, which is small enough to feel instant on M-series chips and capable enough to hold a conversation.

```
speech-to-speech \
  --llm_backend mlx-lm \
  --model_name "mlx-community/Qwen3-4B-Instruct-2507-bf16"
```
The server listens on `ws://127.0.0.1:8765/v1/realtime` by default. Leave it running, connect the conversation app to the local backend, and you are talking to your robot.

##### 
	[
		
	](https://huggingface.co#option-2-local-llm-on-transformers-cuda--cpu--mps)
	
		Option 2: Local LLM on Transformers (CUDA / CPU / MPS)
	

Same idea, but using vanilla `transformers`. Use this if you are on a CUDA box, on Linux, or if you want to swap models freely without re-converting weights for MLX.

```
speech-to-speech \
  --llm_backend transformers \
  --model_name "Qwen/Qwen3-4B-Instruct-2507"
```

Tip.`Qwen3-4B-Instruct-2507`is another good option for LLM because it gives a good speed/quality balance on a single consumer GPU. You can point`--model_name`at any HF model the backend supports — for example a larger Gemma, Qwen, or a Mistral.

### 
	[
		
	](https://huggingface.co#running-the-engine-on-your-laptop-the-app-on-the-robot)
	
		Running the engine on your laptop, the app on the robot
	

If you are running the voice engine on your laptop and the conversation app on a Reachy Mini Wireless, the only thing that changes is the URL. Make sure the engine binds to a LAN address (not just `127.0.0.1`) and use the laptop's IP from the robot when you select the IP in the UI.

If you don't know your IP, here's how to find it:

## macOS

```
ipconfig getifaddr en0    # wifi
ipconfig getifaddr en1    # ethernet (sometimes en0, varies)
```
## Linux

```
hostname -I
```
## Windows

```
ipconfig
```
Look for "IPv4 Address" under your active adapter.

You want the `192.168.x.x` or `10.x.x.x` one. If you see `169.254.x.x`, you're not actually on the network.

## 
	[
		
	](https://huggingface.co#wrap-up)
	
		Wrap up
	

You now have a fully local voice loop:

- A robot listening with **Silero**,
- transcribing with **Parakeet-TDT 0.6B v3**,
- thinking with whichever LLM you picked, whether that's local MLX, local Transformers, a vLLM or llama.cpp server next door, or a hosted Responses API endpoint,
- and answering with **Qwen3-TTS**.

Star [ huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) and 

[, and come tell us in the discussions which open-source cascade you ended up running on your robot.](https://github.com/pollen-robotics/reachy_mini_conversation_app)

`pollen-robotics/reachy_mini_conversation_app`
