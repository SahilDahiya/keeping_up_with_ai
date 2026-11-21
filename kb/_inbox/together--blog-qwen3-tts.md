---
title: Qwen3 TTS is now available on Together AI
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: together
url: https://www.together.ai/blog/qwen3-tts
author: Anthony Ji; Charles Duong; Sebastien Beurnier; Sahil Yadav; Sonny Khan
published: '2026-11-20'
fetched: '2026-11-21T06:06:18Z'
classifier: null
taxonomy_rev: 2
words: 1228
content_sha256: 8f1de87cf4f54e6e555234702bb60d2589ab16f52fe9694e1c00895d91dc28fb
---

# Qwen3 TTS is now available on Together AI

Summary

- **Qwen3 TTS on Together AI:** Qwen's open text-to-speech model, on Together Serverless Inference and dedicated endpoints at \$20 per 1M characters.
- **One voice, many deliveries:** nine preset voices that change tone and emotion from a plain-language instruction such as "excited and upbeat."
- **10 languages per voice:** every preset speaks Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian.
- **Built for real-time voice:** first audio in as little as 97ms, with HTTP streaming and a WebSocket API for text that arrives in pieces.

Starting today, developers can run [Qwen3 TTS](https://www.together.ai/models/qwen3-tts-12hz-1-7b) on Together AI, with first audio in as little as 97ms.

Qwen3 TTS is an open text-to-speech model that separates who is speaking from how they speak. You choose one of nine preset voices, and that voice stays the same while you change its delivery with a plain-language instruction, such as "excited and upbeat," or move it between 10 languages.

Together AI's inference team tuned the serving stack for Qwen3 TTS so that speech starts streaming quickly enough for real-time conversation. The model is available now on Together Serverless Inference and on dedicated endpoints.

## Tell it how to say the line

The same sentence can land as good news or bad news depending on how it's said, and with Qwen3 TTS you decide which by describing the delivery in a few words. Here the voice `aiden` reads one line three times. The voice and the words don't change between clips, only the instruction.

The instruction controls the delivery, and the voice stays the one you chose. You can keep that same voice when you change languages too.

## Keep one voice across 10 languages

Every preset voice speaks all 10 supported languages: Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian. That lets a product keep the same voice when it moves into a new market. Here `aiden`, an English voice, reads the same order update in four languages.

Supply the text in the language you select; the four clips above use separately translated text. Each voice also has a native language, and Qwen recommends using a voice in its native language for the best quality, so listen to the languages your application needs before you settle on a preset.

## Choose a voice in VoiceFinder

The quickest way to choose a preset is to hear each one say your own lines. [VoiceFinder](https://voicefinder.together.ai/) lists the Qwen3 TTS voices, plays a sample of each and reads the text you enter in any of them.

1. Open [voicefinder.together.ai](https://voicefinder.together.ai/), select `Qwen/Qwen3-TTS-12Hz-1.7B` in the model menu and select **Find voices**.
2. Select **Preview** to play a sample of a voice.
3. Select **Try custom text**, enter up to 500 characters and select **Generate** to hear that voice read your text. Repeat with another voice to compare them on the same text.
4. Select **Show code** to get the request for that voice in Python, TypeScript or cURL.

The nine preset voices, with each one's native language and Qwen's description:

## Generate speech

You need the Together Python SDK (`pip install together`) and a `TOGETHER_API_KEY`. This request sets the voice, the language and the instruction together, and produces the excited reading of the line above.

The Python SDK passes `instructions` through `extra_body`. If an instruction doesn't seem to change the delivery, check that the field is spelled `instructions`, since a misspelled field is skipped without an error.

Parameters for this model:

Word timestamps (`alignment=word`) aren't supported for Qwen3 TTS.

## Stream audio for a voice agent

In a voice agent, speech has to start before the whole reply has been synthesized. On Together AI, Qwen3 TTS returns first audio in as little as 97ms, and it streams in two ways. The right one depends on whether you have the full text when you make the request.

### When you have the full text: streaming over HTTP

With `stream=True` and `response_format="raw"`, the speech API returns server-sent events as the audio is generated. Each `conversation.item.audio_output.delta` event carries a base64-encoded chunk of audio. This script receives the stream, decodes each chunk and saves the audio to a file.

The output is 16-bit mono PCM at 24 kHz, and the instruction applies to a streamed request the same way it does to a complete one. To play speech as it arrives, send each decoded chunk to your audio output instead of a file.

### When the text is still being written: WebSocket

If the text comes from a language model token by token, the WebSocket endpoint lets you send it in pieces. You open one connection, append text as it becomes available and commit when the input is complete, and the server synthesizes each sentence once it has the whole sentence. This script sends an order update in two pieces and saves the audio that comes back. It needs the `websockets` package, version 14 or later (`pip install websockets`).

The connection URL carries the model, voice, language and audio settings (the WebSocket endpoint names raw PCM `pcm`), and the audio arrives in the same base64 events as the HTTP stream. The [WebSocket guide](https://docs.together.ai/docs/inference/text-to-speech/websocket) lists every message type.

## Get started

- Compare the voices in [VoiceFinder](https://voicefinder.together.ai/)
- Read the [text-to-speech docs](https://docs.together.ai/docs/text-to-speech), the [streaming guide](https://docs.together.ai/docs/inference/text-to-speech/streaming) and the [WebSocket guide](https://docs.together.ai/docs/inference/text-to-speech/websocket)
- View the [Qwen3 TTS model page](https://www.together.ai/models/qwen3-tts-12hz-1-7b)
- Read Qwen's [model card on Hugging Face](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)

## FAQs

### How much does Qwen3 TTS cost on Together AI?

Qwen3 TTS costs \$20 per 1M characters on Together Serverless Inference. The model is also available on dedicated endpoints.

### How fast is Qwen3 TTS on Together AI?

Qwen3 TTS returns first audio in as little as 97ms on Together AI when you stream the response, on a serving stack our inference team tuned for real-time voice.

### How do I control the tone of a Qwen3 TTS voice?

Send a plain-language description of the delivery in the `instructions` field of the speech request, such as `excited and upbeat`. In the Python SDK, pass it through `extra_body`. An instruction changes the emotion and tone of the voice and doesn't change who it sounds like.

### Can one Qwen3 TTS voice speak more than one language?

Yes, each of the nine Qwen3 TTS preset voices can speak all 10 supported languages. Set `voice` to the voice name and `language` to the language of the text, and send the text in that language. Qwen recommends using each voice in its native language for the best quality.

### Does Qwen3 TTS support streaming on Together AI?

Yes, Qwen3 TTS supports streaming on Together AI in two ways. Over HTTP, set `stream` to `true` and `response_format` to `raw` to receive server-sent events with base64-encoded PCM audio. Over WebSocket, send text in pieces and receive audio as it's generated.

### What audio formats does Qwen3 TTS return?

Qwen3 TTS returns `wav`, `mp3`, `raw` (PCM) or `mulaw` audio on Together AI, at a sample rate of 24000 (the default) or 8000. It doesn't return `opus`, `aac` or `flac`.

### How do I compare Qwen3 TTS voices before choosing one?

Open [VoiceFinder](https://voicefinder.together.ai/) and select `Qwen/Qwen3-TTS-12Hz-1.7B` in the model menu. You can preview each voice and generate up to 500 characters of your own text with it.

### Is Qwen3 TTS open source?

Yes, Qwen released Qwen3 TTS 12Hz 1.7B under the Apache 2.0 license. The weights are on Hugging Face.
