---
title: 'NVIDIA Nemotron 3 Diarization: real-time speaker labels at a cent per audio
  hour'
kind: blog
topic: models
subtopic: architectures
secondary_topics:
- inference/serving
summary: NVIDIA Nemotron 3 Diarization is a ~100M-parameter streaming transformer
  built on Streaming Sortformer that labels up to 8 speakers per 320ms chunk using
  an arrival-order speaker cache and FIFO frame buffer instead of embeddings or clustering,
  hitting 9.8% DER on AISHELL-4 at the low-latency profile (vs 27.2% for its predecessor)
  and sustaining 500+ concurrent hour-long streams on an RTX PRO 6000.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-nemotron-3-diarization/
author: Ansel Erol
published: '2026-09-23'
fetched: '2026-09-24T06:10:31Z'
classifier: claude
taxonomy_rev: 2
words: 1226
content_sha256: 9aa635625c17963d0adf4531906176ff1393c264c2d910396030741e6f492fb3
---

# NVIDIA Nemotron 3 Diarization: real-time speaker labels at a cent per audio hour

![Nemotron 3 diarization](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790018010-nemotron-3-diarization-blog.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Use NVIDIA Nemotron 3 Diarization from [Baseten’s Model Library](https://www.baseten.co/library/nemotron-3-diarization/), with presets for prerecorded and streaming diarization, and real-time diarized transcription. This is an open, end-to-end diarization model that replaces the usual segmentation-plus-embedding pipeline and its tuning with a single pass, labeling up to eight speakers at a configurable interval as low as every 320ms. 

We optimized it on an RTX PRO 6000, which can sustain over 500 concurrent hour-long diarization streams (190 with transcription added). The same per-speaker activity can be used to inform VAD, endpointing, and turn-taking for voice agents.

## **An end-to-end streaming architecture**

Speaker diarization segments an audio stream by when each distinct speaker is talking, outputs timings for each distinct voice, and assigns every span a consistent speaker label. In conjunction with transcription, diarization can attribute transcribed words to who said them in a conversation.

The NVIDIA Nemotron 3 Diarization model has a ~100M-parameter transformer-based architecture built on top of [NVIDIA Streaming Sortformer](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/). It turns 16 kHz audio into 10ms frames and emits a T×8 matrix of speaker-activity probabilities. 

Two pieces of state carry a conversation across chunks: an arrival-order speaker cache (speaker_0 is the first voice heard, and stays that way) and a FIFO (“First In, First Out”) of recent frames, with no embeddings or clustering required for an unbounded audio length.

## **Latency configuration for diverse use cases**

While prior diarization models require extensive configuration of several different parameters or lack support for multiple latency profiles entirely, the same Nemotron 3 Diarization checkpoint can serve each request at four algorithmic latencies between 0.32 and 30.4 seconds, referring to how much future audio the model sees before it commits a label. To accommodate diverse application requirements ranging from real-time agent interactions to offline media processing, Nemotron 3 Diarization supports flexible algorithmic latency settings within a single unified checkpoint.

![Latency profiles of a single checkpoint.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790115516-checkpoint_diagram.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Latency profiles of a single checkpoint.

Figure 1 illustrates how these latency profiles map directly to chunk sizes and right-context lookahead windows. Moving from the ultra-low profile to the standard low profile trades a modest increase in buffer delay for continuous quality gains. This predictability enables developers to configure buffer sizes dynamically per request without redeploying underlying model instances.

## **High quality across four configurable latency profiles**

We report diarization error rate (DER) with overlap included and no collar. Nemotron 3 Diarization holds its accuracy as latency drops. Moving from the 30-second offline profile to the 0.32-second ultra-low profile increases DER by only 1-2 points compared to prerecorded, with quality sustained beyond four speakers. On AISHELL-4 at the “low” profile, we observed a DER of 9.8% against 27.2% for Streaming Sortformer v2.1, a significant improvement compared to this model’s predecessor.

To evaluate standard diarization accuracy across varied acoustic environments and speaker counts, we measured DER across benchmark datasets without applying a time collar.

![Nemotron 3 Diarization offers leading performance across all three latency profiles.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790185995-error-rate_diagram_update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Nemotron 3 Diarization offers leading performance across all three latency profiles.

The benchmarking results highlight consistent stability across multiple benchmark datasets in multiple languages, such as NOTSOFAR, AMI, CALLHOME, and AISHELL, outperforming Meta Muse Voice Transcribe on all datasets at even the ultra-low configuration, and losing to pyannote Community-1 only on AMI. Even under ultra-low latency configurations, the error rate remains within a tight margin of offline baselines, confirming robust speaker attribution under real-time constraints. Streaming diarization on Baseten remains close to prerecorded quality across the tested latency profiles.

## **Speaker activity as a voice-activity and turn-taking signal**

Speaker-attributed time segments are only one way to use Nemotron 3 Diarization. At its core, the model tracks speech activity per speaker in 10ms increments. This raw data can be used by voice applications to support three key capabilities:

- **Voice activity detection** : By combining data across all audio channels, it detects speech directly from the audio stream rather than relying on volume levels.
- **Speaker-specific end-of-turn detection** : It tracks when a specific speaker stops talking for a set duration. This helps an AI voice agent distinguish between the primary user finishing a sentence and background chatter from someone else in the room.
- **Turn-taking and interruptions** : The order in which voices appear identifies the primary speaker. If a second voice starts speaking, the model detects an interruption; if both speak at once, it flags overlapping speech, responding in roughly 300ms on ultra-low latency settings.

## **Day 0 support for prerecorded, streaming, and speaker-attributed transcription**

To streamline deployment across different audio infrastructure designs, Baseten exposes the model through three specialized serving presets. Figure 3 provides an architectural overview of these presets along with their target workloads and throughput characteristics.

![Three presets on Baseten.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790115680-three-ways_diagram.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Three presets on Baseten.

These modular presets allow voice applications to choose between stateless batch requests, persistent WebSocket streams for live speaker tracking, or joint end-to-end transcription pipelines, matching backend infrastructure requirements directly.

Each latency level runs as its own ready-to-use instance, so you can easily choose your speed per request without redeploying. The real-time transcription option pairs the speaker tracker with NVIDIA's 600M English speech recognition model, [NVIDIA Parakeet V2 ASR](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2), which is also in the Nemotron speech family. By using speaker activity to guide transcription on the same audio stream, it accurately captures both sides of a conversation, even when people talk over each other.

Combining speech recognition with diarization typically requires managing separate model pipelines and aligning transcripts post-hoc. Our real-time system directly conditions the ASR model on speaker activity features within the primary forward pass. By feeding per-speaker activity vectors directly into the initial encoder layers of Parakeet V2, the pipeline transcribes overlapped audio channels in a single pass, eliminating duplicate feature extraction steps and preserving temporal alignment between words and speakers.

## **Nemotron 3 Diarization performance on Baseten**

Load came from k6 inside the cluster with a one-stream control on an idle replica in every run; every server frame is archived.

To establish reliable capacity limits for production infrastructure, we benchmarked total concurrent streaming capacity per GPU under continuous load tests. Figure 4 illustrates latency performance across varying concurrent stream counts on a single NVIDIA RTX PRO 6000.

![On Baseten, Nemotron 3 Diarization can support up to 500 streams per RTX-6000 on the low-latency setting.](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1790186211-concurrent-streams_diagram_update.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) On Baseten, Nemotron 3 Diarization can support up to 500 streams per RTX-6000 on the low-latency setting.

The stress test results demonstrate flat latency scaling up to maximum hardware saturation points. By managing hardware resources strictly within predictable GPU utilization boundaries, system latency remains stable near single-stream baseline values until hard capacity limits are reached.

Using identical files and hardware, Baseten’s optimized serving preset delivered ~1.35x higher batch processing throughput than the NVIDIA reference setup used in our testing. Over an HTTP connection, a single GPU can continuously process 200 six-minute audio files every minute while maintaining steady response times.

For live transcription, the streaming and batch setups deliver virtually identical accuracy, successfully reconstructing speaker-tagged transcripts straight from the speech recognition model.

## **Deploy Nemotron 3 Diarization today**

Nemotron 3 Diarization is available on [Hugging Face](https://huggingface.co/nvidia/Nemotron-3-Diarization) and in the [Baseten Model Library](https://www.baseten.co/library/nemotron-3-diarization/) as batch, streaming, and real-time diarized transcription presets. Deploy one in a couple of clicks, pick a latency profile per request, and pair it with the ASR you already run — or [talk to our engineers](https://www.baseten.co/talk-to-us/?model=nemotron-3-td-nemotron-asr) about how we can optimize your voice workload.
